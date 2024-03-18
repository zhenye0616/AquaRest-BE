import openai
import json

def load_sleep_data_from_json(file_path):
    with open(file_path, 'r') as file:
        sleep_data = json.load(file)
    return sleep_data

# Load sleep data from your JSON file
sleep_data = load_sleep_data_from_json('/Users/zhenye/PycharmProjects/AqualRestBackEnd/sleep_records.json')

# Format the sleep data into a string for generating recommendations
formatted_data = []
for record in sleep_data:
    formatted_data.append(
        f"Date: {record['date']}, Sleep Time: {record['sleep_time_hours']} hours, Sleepiness Level: {record['sleepiness_level']}"
    )

# Join the formatted data into a single string
data_for_recommendations = "\n".join(formatted_data)

# Set your OpenAI API key
#put openAI


def generate_recommendations(data):
    try:
        # Convert the data into a readable string format for the prompt
        prompt_text = "Generate sleep recommendations based on the following data:\n"
        for entry in data:
            prompt_text += f"Date: {entry['date']}, Sleep time: {entry['hours']} hours, Sleepiness level: {entry['sleepinessLevel']}\n"

        #print(prompt_text)

        # Call the ChatGPT API to generate recommendations based on the formatted prompt
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt_text,
            max_tokens=150
        )
        print("generate_rec")
        #print(response)
        return response.choices[0].text.strip()

    except openai.error.RateLimitError:
        print("Rate limit exceeded. Please try again later.")
        return "Summary not available due to rate limit."
    except Exception as e:
        print(f"An error occurred: {e}")
        return 'An error occurred in summarization.'


