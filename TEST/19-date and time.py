from datetime import datetime
current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S.%f")
print("Current Date and Time:", formatted_datetime)