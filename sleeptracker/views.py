from django.shortcuts import render
from .forms import SleepRecordForm
from .chatgpt_rec import generate_recommendations, load_sleep_data_from_json
from django.http import JsonResponse
from sleeptracker.Management.commands import run_index

def some_view(request):
    recommendations = None
    if request.method == 'POST':
        form = SleepRecordForm(request.POST)
        if form.is_valid():
            # Process the data, for example, save it to the database
            form.save()
            # Run the indexing process asynchronously
            run_index.delay('/Users/zhenye/PycharmProjects/AqualRestBackEnd/sleep_records.json')
            # Redirect to a new URL or indicate success
            return render(request, 'success_template.html')
    else:
        form = SleepRecordForm()

    # Render the form with any context you need
    return render(request, 'some_template.html', {'form': form, 'recommendations': recommendations})

def chatgpt_api_1(request):
    user_input = request.GET.get('user_input', '')
    if user_input:
        print("in chatgpt_api")
        data_for_recommendations = load_sleep_data_from_json('/Users/zhenye/PycharmProjects/AqualRestBackEnd/sleepData.json')
        recommendations = generate_recommendations(data_for_recommendations)
        return JsonResponse({'response': recommendations})
    else:
        return JsonResponse({'error': 'No input provided'})

def chatgpt_api(request):
    user_input = request.GET.get('user_input', '')
    if user_input:
        data_for_recommendations = load_sleep_data_from_json('/Users/zhenye/PycharmProjects/AqualRestBackEnd/sleepData.json')
        recommendations = generate_recommendations(data_for_recommendations)
        return JsonResponse({'response': recommendations})
    else:
        return JsonResponse({'error': 'No input provided'})