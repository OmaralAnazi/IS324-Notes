Riyadh_Forecast_forWeekOne = {
    "Saturday":  {'humidity': 10, 'temperature': 35, 'wind': 19},
    "Sunday":    {'humidity': 15, 'temperature': 30, 'wind': 28},
    "Monday":    {'humidity': 26, 'temperature': 33, 'wind': 12},
    "Tuesday":   {'humidity': 20, 'temperature': 40, 'wind': 7},
    "Wednesday": {'humidity': 30, 'temperature': 41, 'wind': 10},
    "Thursday":  {'humidity': 40, 'temperature': 37, 'wind': 5},
    "Friday":    {'humidity': 23, 'temperature': 38, 'wind': 15}
}

Riyadh_Forecast_forWeekTwo = {
    "Saturday":  {'humidity': 15, 'temperature': 25, 'wind': 29},
    "Sunday":    {'humidity': 35, 'temperature': 31, 'wind': 18},
    "Monday":    {'humidity': 25, 'temperature': 30, 'wind': 22},
    "Tuesday":   {'humidity': 10, 'temperature': 27, 'wind': 3},
    "Wednesday": {'humidity': 34, 'temperature': 38, 'wind': 12},
    "Thursday":  {'humidity': 35, 'temperature': 33, 'wind': 9},
    "Friday":    {'humidity': 13, 'temperature': 43, 'wind': 12}
}

Riyadh_Forecast_forMonthOne = {
    "Week1": Riyadh_Forecast_forWeekOne,
    "Week2": Riyadh_Forecast_forWeekTwo
    # I'm lazy to make Week3 and Week4 ...
}

# Accessing data
print(Riyadh_Forecast_forMonthOne["Week1"]["Wednesday"]["temperature"])  # prints: 41

# Is Sunday in the first week hotter than the second week?
print(Riyadh_Forecast_forMonthOne["Week1"]["Sunday"]["temperature"] >
      Riyadh_Forecast_forMonthOne["Week2"]["Sunday"]["temperature"])  # 30 > 31 -> prints: False

# Deleting
temp = Riyadh_Forecast_forMonthOne["Week1"]["Friday"]["wind"]
del Riyadh_Forecast_forMonthOne["Week1"]["Friday"]["wind"]
print(Riyadh_Forecast_forMonthOne["Week1"]["Friday"])  # prints: {'humidity': 23, 'temperature': 38}


# Adding
Riyadh_Forecast_forMonthOne["Week1"]["Friday"]["wind"] = temp  # Don't delete your data again stupid!!
print(Riyadh_Forecast_forMonthOne["Week1"]["Friday"]) # prints: {'humidity': 23, 'temperature': 38, 'wind': 15}

