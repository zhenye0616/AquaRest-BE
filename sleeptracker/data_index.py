import json
from sleeptracker.models import SleepRecord
from decimal import Decimal

def index_data_to_file(file_path):
    # Retrieve all sleep records
    sleep_records = SleepRecord.objects.all()

    # Format data into a list of dictionaries
    formatted_data = []
    for record in sleep_records:
        formatted_data.append({
            'date': record.date.strftime('%Y-%m-%d'),
            'sleep_time_hours': float(record.sleep_time_hours),  # Convert Decimal to float
            'sleepiness_level': float(record.sleepiness_level),  # Convert Decimal to float
        })

    # Write data to file
    with open(file_path, 'w') as file:
        json.dump(formatted_data, file, indent=4)

    print(f"Indexed {len(formatted_data)} sleep records to {file_path}")

# Call the function with the desired file path
index_data_to_file('sleep_records.json')
