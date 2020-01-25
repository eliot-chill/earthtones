# this file grabs wind data for the specified location and saves it in the DB ready to be picked up for the front-end
import requests
import json

fake_data = '{"latitude": -37.090335, "longitude": 149.370666, "timezone": "Australia/Sydney", "currently": {"time": 1579964773, "summary": "Overcast", "icon": "cloudy", "precipIntensity": 0.0019, "precipProbability": 0.1, "precipType": "rain", "temperature": 63.93, "apparentTemperature": 64.66, "dewPoint": 63.55, "humidity": 0.99, "pressure": 1012.9, "windSpeed": 1.14, "windGust": 1.52, "windBearing": 268, "cloudCover": 0.94, "uvIndex": 0, "visibility": 10, "ozone": 279.3}, "hourly": {"summary": "Partly cloudy throughout the day.", "icon": "partly-cloudy-day", "data": [{"time": 1579964400, "summary": "Overcast", "icon": "cloudy", "precipIntensity": 0.002, "precipProbability": 0.11, "precipType": "rain", "temperature": 63.98, "apparentTemperature": 64.71, "dewPoint": 63.58, "humidity": 0.99, "pressure": 1013, "windSpeed": 1.14, "windGust": 1.52, "windBearing": 269, "cloudCover": 0.94, "uvIndex": 0, "visibility": 10, "ozone": 279.2}, {"time": 1579968000, "summary": "Overcast", "icon": "cloudy", "precipIntensity": 0.0013, "precipProbability": 0.09, "precipType": "rain", "temperature": 63.32, "apparentTemperature": 64.04, "dewPoint": 63.23, "humidity": 1, "pressure": 1012.5, "windSpeed": 1.18, "windGust": 1.66, "windBearing": 151, "cloudCover": 0.92, "uvIndex": 0, "visibility": 10, "ozone": 280.3}, {"time": 1579971600, "summary": "Overcast", "icon": "cloudy", "precipIntensity": 0.0009, "precipProbability": 0.07, "precipType": "rain", "temperature": 62.56, "apparentTemperature": 63.26, "dewPoint": 62.56, "humidity": 1, "pressure": 1012.1, "windSpeed": 1.32, "windGust": 2.08, "windBearing": 1, "cloudCover": 0.88, "uvIndex": 0, "visibility": 10, "ozone": 281}, {"time": 1579975200, "summary": "Mostly Cloudy", "icon": "partly-cloudy-night", "precipIntensity": 0.0006, "precipProbability": 0.05, "precipType": "rain", "temperature": 62.38, "apparentTemperature": 63.06, "dewPoint": 62.38, "humidity": 1, "pressure": 1011.8, "windSpeed": 1.53, "windGust": 2.69, "windBearing": 328, "cloudCover": 0.8, "uvIndex": 0, "visibility": 10, "ozone": 281.2}, {"time": 1579978800, "summary": "Mostly Cloudy", "icon": "partly-cloudy-night", "precipIntensity": 0.0003, "precipProbability": 0.04, "precipType": "rain", "temperature": 62.63, "apparentTemperature": 63.36, "dewPoint": 62.63, "humidity": 1, "pressure": 1012, "windSpeed": 1.76, "windGust": 3.34, "windBearing": 311, "cloudCover": 0.65, "uvIndex": 0, "visibility": 10, "ozone": 281.2}, {"time": 1579982400, "summary": "Partly Cloudy", "icon": "partly-cloudy-day", "precipIntensity": 0, "precipProbability": 0, "temperature": 63.29, "apparentTemperature": 64.11, "dewPoint": 63.29, "humidity": 1, "pressure": 1012.6, "windSpeed": 2.06, "windGust": 4.19, "windBearing": 328, "cloudCover": 0.47, "uvIndex": 0, "visibility": 10, "ozone": 280.7}, {"time": 1579986000, "summary": "Partly Cloudy", "icon": "partly-cloudy-day", "precipIntensity": 0, "precipProbability": 0, "temperature": 65.67, "apparentTemperature": 66.33, "dewPoint": 63.75, "humidity": 0.94, "pressure": 1012.7, "windSpeed": 2.45, "windGust": 5.56, "windBearing": 322, "cloudCover": 0.32, "uvIndex": 1, "visibility": 10, "ozone": 280}, {"time": 1579989600, "summary": "Clear", "icon": "clear-day", "precipIntensity": 0, "precipProbability": 0, "temperature": 70.26, "apparentTemperature": 70.63, "dewPoint": 62.93, "humidity": 0.78, "pressure": 1012.4, "windSpeed": 2.97, "windGust": 8.26, "windBearing": 311, "cloudCover": 0.26, "uvIndex": 3, "visibility": 10, "ozone": 278.7}, {"time": 1579993200, "summary": "Clear", "icon": "clear-day", "precipIntensity": 0, "precipProbability": 0, "temperature": 75.64, "apparentTemperature": 75.64, "dewPoint": 57.99, "humidity": 0.54, "pressure": 1011.9, "windSpeed": 3.51, "windGust": 11.47, "windBearing": 259, "cloudCover": 0.23, "uvIndex": 5, "visibility": 10, "ozone": 277.3}, {"time": 1579996800, "summary": "Clear", "icon": "clear-day", "precipIntensity": 0, "precipProbability": 0, "temperature": 79.29, "apparentTemperature": 79.29, "dewPoint": 51.03, "humidity": 0.37, "pressure": 1011.4, "windSpeed": 3.83, "windGust": 13.22, "windBearing": 279, "cloudCover": 0.2, "uvIndex": 8, "visibility": 10, "ozone": 276.2}, {"time": 1580000400, "summary": "Clear", "icon": "clear-day", "precipIntensity": 0, "precipProbability": 0, "temperature": 82, "apparentTemperature": 82, "dewPoint": 45.51, "humidity": 0.28, "pressure": 1011.1, "windSpeed": 3.77, "windGust": 12.04, "windBearing": 2, "cloudCover": 0.12, "uvIndex": 10, "visibility": 10, "ozone": 275.7}, {"time": 1580004000, "summary": "Clear", "icon": "clear-day", "precipIntensity": 0, "precipProbability": 0, "temperature": 84.37, "apparentTemperature": 84.37, "dewPoint": 41.07, "humidity": 0.22, "pressure": 1010.7, "windSpeed": 3.59, "windGust": 9.41, "windBearing": 167, "cloudCover": 0.05, "uvIndex": 12, "visibility": 10, "ozone": 275.5}, {"time": 1580007600, "summary": "Clear", "icon": "clear-day", "precipIntensity": 0, "precipProbability": 0, "temperature": 85.47, "apparentTemperature": 85.47, "dewPoint": 39.76, "humidity": 0.2, "pressure": 1010.5, "windSpeed": 3.71, "windGust": 7.68, "windBearing": 228, "cloudCover": 0, "uvIndex": 12, "visibility": 10, "ozone": 275.5}, {"time": 1580011200, "summary": "Clear", "icon": "clear-day", "precipIntensity": 0, "precipProbability": 0, "temperature": 85.05, "apparentTemperature": 85.05, "dewPoint": 44.27, "humidity": 0.24, "pressure": 1010.4, "windSpeed": 4.58, "windGust": 7.95, "windBearing": 220, "cloudCover": 0.01, "uvIndex": 10, "visibility": 10, "ozone": 275.9}, {"time": 1580014800, "summary": "Clear", "icon": "clear-day", "precipIntensity": 0, "precipProbability": 0, "temperature": 84.7, "apparentTemperature": 84.7, "dewPoint": 50.94, "humidity": 0.31, "pressure": 1010.3, "windSpeed": 5.77, "windGust": 9.11, "windBearing": 185, "cloudCover": 0.04, "uvIndex": 7, "visibility": 10, "ozone": 276.3}, {"time": 1580018400, "summary": "Clear", "icon": "clear-day", "precipIntensity": 0, "precipProbability": 0, "temperature": 81.28, "apparentTemperature": 81.28, "dewPoint": 56.74, "humidity": 0.43, "pressure": 1010.7, "windSpeed": 6.52, "windGust": 10.25, "windBearing": 159, "cloudCover": 0.07, "uvIndex": 4, "visibility": 10, "ozone": 276.4}, {"time": 1580022000, "summary": "Clear", "icon": "clear-day", "precipIntensity": 0, "precipProbability": 0, "temperature": 77.46, "apparentTemperature": 77.51, "dewPoint": 60.27, "humidity": 0.55, "pressure": 1011.6, "windSpeed": 6.5, "windGust": 11.49, "windBearing": 157, "cloudCover": 0.11, "uvIndex": 2, "visibility": 10, "ozone": 275.7}, {"time": 1580025600, "summary": "Clear", "icon": "clear-day", "precipIntensity": 0, "precipProbability": 0, "temperature": 72.34, "apparentTemperature": 72.49, "dewPoint": 61.36, "humidity": 0.68, "pressure": 1012.9, "windSpeed": 6.09, "windGust": 12.72, "windBearing": 162, "cloudCover": 0.17, "uvIndex": 0, "visibility": 10, "ozone": 274.5}, {"time": 1580029200, "summary": "Clear", "icon": "clear-day", "precipIntensity": 0, "precipProbability": 0, "temperature": 67.8, "apparentTemperature": 67.99, "dewPoint": 61.04, "humidity": 0.79, "pressure": 1014.1, "windSpeed": 5.44, "windGust": 12.57, "windBearing": 162, "cloudCover": 0.19, "uvIndex": 0, "visibility": 10, "ozone": 273.7}, {"time": 1580032800, "summary": "Clear", "icon": "clear-night", "precipIntensity": 0, "precipProbability": 0, "temperature": 64.22, "apparentTemperature": 64.41, "dewPoint": 60.19, "humidity": 0.87, "pressure": 1015.2, "windSpeed": 4.4, "windGust": 9.79, "windBearing": 160, "cloudCover": 0.16, "uvIndex": 0, "visibility": 10, "ozone": 273.3}, {"time": 1580036400, "summary": "Clear", "icon": "clear-night", "precipIntensity": 0, "precipProbability": 0, "temperature": 61.28, "apparentTemperature": 61.43, "dewPoint": 58.92, "humidity": 0.92, "pressure": 1016, "windSpeed": 3.09, "windGust": 5.63, "windBearing": 183, "cloudCover": 0.11, "uvIndex": 0, "visibility": 10, "ozone": 273.1}, {"time": 1580040000, "summary": "Clear", "icon": "clear-night", "precipIntensity": 0.0003, "precipProbability": 0.03, "precipType": "rain", "temperature": 59.06, "apparentTemperature": 59.06, "dewPoint": 57.18, "humidity": 0.93, "pressure": 1016.3, "windSpeed": 2.09, "windGust": 2.59, "windBearing": 212, "cloudCover": 0.1, "uvIndex": 0, "visibility": 10, "ozone": 273.5}, {"time": 1580043600, "summary": "Clear", "icon": "clear-night", "precipIntensity": 0.0003, "precipProbability": 0.03, "precipType": "rain", "temperature": 58.23, "apparentTemperature": 58.23, "dewPoint": 56.77, "humidity": 0.95, "pressure": 1016.3, "windSpeed": 1.63, "windGust": 1.88, "windBearing": 186, "cloudCover": 0.28, "uvIndex": 0, "visibility": 10, "ozone": 274.7}, {"time": 1580047200, "summary": "Partly Cloudy", "icon": "partly-cloudy-night", "precipIntensity": 0.0002, "precipProbability": 0.01, "precipType": "rain", "temperature": 58.28, "apparentTemperature": 58.28, "dewPoint": 56.6, "humidity": 0.94, "pressure": 1016, "windSpeed": 1.49, "windGust": 2.04, "windBearing": 69, "cloudCover": 0.54, "uvIndex": 0, "visibility": 10, "ozone": 276.3}, {"time": 1580050800, "summary": "Mostly Cloudy", "icon": "partly-cloudy-night", "precipIntensity": 0.0002, "precipProbability": 0.01, "precipType": "rain", "temperature": 58.23, "apparentTemperature": 58.23, "dewPoint": 56.47, "humidity": 0.94, "pressure": 1015.6, "windSpeed": 1.49, "windGust": 2.35, "windBearing": 263, "cloudCover": 0.73, "uvIndex": 0, "visibility": 10, "ozone": 277.4}, {"time": 1580054400, "summary": "Mostly Cloudy", "icon": "partly-cloudy-night", "precipIntensity": 0, "precipProbability": 0, "temperature": 57.58, "apparentTemperature": 57.58, "dewPoint": 56.26, "humidity": 0.95, "pressure": 1015.2, "windSpeed": 1.62, "windGust": 2.38, "windBearing": 293, "cloudCover": 0.82, "uvIndex": 0, "visibility": 10, "ozone": 277.3}, {"time": 1580058000, "summary": "Mostly Cloudy", "icon": "partly-cloudy-night", "precipIntensity": 0, "precipProbability": 0, "temperature": 56.94, "apparentTemperature": 56.94, "dewPoint": 56.13, "humidity": 0.97, "pressure": 1014.8, "windSpeed": 1.87, "windGust": 2.51, "windBearing": 358, "cloudCover": 0.86, "uvIndex": 0, "visibility": 10, "ozone": 276.6}, {"time": 1580061600, "summary": "Mostly Cloudy", "icon": "partly-cloudy-night", "precipIntensity": 0, "precipProbability": 0, "temperature": 57.14, "apparentTemperature": 57.14, "dewPoint": 56.27, "humidity": 0.97, "pressure": 1014.6, "windSpeed": 2.11, "windGust": 3, "windBearing": 354, "cloudCover": 0.86, "uvIndex": 0, "visibility": 10, "ozone": 275.6}, {"time": 1580065200, "summary": "Mostly Cloudy", "icon": "partly-cloudy-night", "precipIntensity": 0, "precipProbability": 0, "temperature": 58.12, "apparentTemperature": 58.12, "dewPoint": 56.45, "humidity": 0.94, "pressure": 1014.7, "windSpeed": 2.22, "windGust": 4.11, "windBearing": 3, "cloudCover": 0.83, "uvIndex": 0, "visibility": 10, "ozone": 274.3}, {"time": 1580068800, "summary": "Mostly Cloudy", "icon": "partly-cloudy-day", "precipIntensity": 0, "precipProbability": 0, "temperature": 60.12, "apparentTemperature": 60.18, "dewPoint": 57.94, "humidity": 0.93, "pressure": 1014.8, "windSpeed": 2.28, "windGust": 5.61, "windBearing": 21, "cloudCover": 0.78, "uvIndex": 0, "visibility": 10, "ozone": 272.7}, {"time": 1580072400, "summary": "Mostly Cloudy", "icon": "partly-cloudy-day", "precipIntensity": 0, "precipProbability": 0, "temperature": 63.04, "apparentTemperature": 63.19, "dewPoint": 59.5, "humidity": 0.88, "pressure": 1015.1, "windSpeed": 2.49, "windGust": 6.96, "windBearing": 35, "cloudCover": 0.71, "uvIndex": 1, "visibility": 10, "ozone": 271.4}, {"time": 1580076000, "summary": "Mostly Cloudy", "icon": "partly-cloudy-day", "precipIntensity": 0, "precipProbability": 0, "temperature": 67.01, "apparentTemperature": 67.17, "dewPoint": 60.57, "humidity": 0.8, "pressure": 1014.9, "windSpeed": 3.07, "windGust": 8.09, "windBearing": 35, "cloudCover": 0.63, "uvIndex": 3, "visibility": 10, "ozone": 271.1}, {"time": 1580079600, "summary": "Partly Cloudy", "icon": "partly-cloudy-day", "precipIntensity": 0, "precipProbability": 0, "temperature": 72, "apparentTemperature": 72.15, "dewPoint": 61.3, "humidity": 0.69, "pressure": 1014.5, "windSpeed": 3.84, "windGust": 9.09, "windBearing": 31, "cloudCover": 0.55, "uvIndex": 5, "visibility": 10, "ozone": 271.1}, {"time": 1580083200, "summary": "Partly Cloudy", "icon": "partly-cloudy-day", "precipIntensity": 0, "precipProbability": 0, "temperature": 75.73, "apparentTemperature": 75.77, "dewPoint": 60.29, "humidity": 0.59, "pressure": 1013.9, "windSpeed": 4.39, "windGust": 9.76, "windBearing": 33, "cloudCover": 0.51, "uvIndex": 7, "visibility": 10, "ozone": 270.8}, {"time": 1580086800, "summary": "Partly Cloudy", "icon": "partly-cloudy-day", "precipIntensity": 0, "precipProbability": 0, "temperature": 79.82, "apparentTemperature": 79.82, "dewPoint": 59.02, "humidity": 0.49, "pressure": 1013.1, "windSpeed": 4.53, "windGust": 9.83, "windBearing": 52, "cloudCover": 0.53, "uvIndex": 8, "visibility": 10, "ozone": 269.9}, {"time": 1580090400, "summary": "Partly Cloudy", "icon": "partly-cloudy-day", "precipIntensity": 0, "precipProbability": 0, "temperature": 83.35, "apparentTemperature": 83.35, "dewPoint": 57.78, "humidity": 0.42, "pressure": 1012.1, "windSpeed": 4.44, "windGust": 9.57, "windBearing": 61, "cloudCover": 0.59, "uvIndex": 8, "visibility": 10, "ozone": 268.5}, {"time": 1580094000, "summary": "Mostly Cloudy", "icon": "partly-cloudy-day", "precipIntensity": 0, "precipProbability": 0, "temperature": 85.07, "apparentTemperature": 85.07, "dewPoint": 57.72, "humidity": 0.4, "pressure": 1011.4, "windSpeed": 4.47, "windGust": 9.61, "windBearing": 63, "cloudCover": 0.65, "uvIndex": 8, "visibility": 10, "ozone": 267.5}, {"time": 1580097600, "summary": "Mostly Cloudy", "icon": "partly-cloudy-day", "precipIntensity": 0.0002, "precipProbability": 0.01, "precipType": "rain", "temperature": 83.58, "apparentTemperature": 83.66, "dewPoint": 59.94, "humidity": 0.45, "pressure": 1011, "windSpeed": 4.87, "windGust": 10.42, "windBearing": 94, "cloudCover": 0.7, "uvIndex": 7, "visibility": 10, "ozone": 266.9}, {"time": 1580101200, "summary": "Mostly Cloudy", "icon": "partly-cloudy-day", "precipIntensity": 0.0004, "precipProbability": 0.01, "precipType": "rain", "temperature": 80.21, "apparentTemperature": 81.64, "dewPoint": 63.21, "humidity": 0.56, "pressure": 1010.6, "windSpeed": 5.38, "windGust": 11.54, "windBearing": 133, "cloudCover": 0.76, "uvIndex": 5, "visibility": 10, "ozone": 266.6}, {"time": 1580104800, "summary": "Mostly Cloudy", "icon": "partly-cloudy-day", "precipIntensity": 0.0009, "precipProbability": 0.02, "precipType": "rain", "temperature": 76.6, "apparentTemperature": 77.27, "dewPoint": 66.26, "humidity": 0.7, "pressure": 1010.7, "windSpeed": 5.67, "windGust": 12.05, "windBearing": 96, "cloudCover": 0.82, "uvIndex": 3, "visibility": 10, "ozone": 266.3}, {"time": 1580108400, "summary": "Overcast", "icon": "cloudy", "precipIntensity": 0.0023, "precipProbability": 0.05, "precipType": "rain", "temperature": 73.66, "apparentTemperature": 74.49, "dewPoint": 67.17, "humidity": 0.8, "pressure": 1011.2, "windSpeed": 5.49, "windGust": 11.67, "windBearing": 110, "cloudCover": 0.89, "uvIndex": 2, "visibility": 10, "ozone": 266}, {"time": 1580112000, "summary": "Overcast", "icon": "cloudy", "precipIntensity": 0.0054, "precipProbability": 0.08, "precipType": "rain", "temperature": 69.99, "apparentTemperature": 70.91, "dewPoint": 66.89, "humidity": 0.9, "pressure": 1012.3, "windSpeed": 5.04, "windGust": 10.73, "windBearing": 128, "cloudCover": 0.95, "uvIndex": 0, "visibility": 10, "ozone": 265.6}, {"time": 1580115600, "summary": "Overcast", "icon": "cloudy", "precipIntensity": 0.0083, "precipProbability": 0.11, "precipType": "rain", "temperature": 67.67, "apparentTemperature": 68.64, "dewPoint": 66.41, "humidity": 0.96, "pressure": 1013.2, "windSpeed": 4.47, "windGust": 9.3, "windBearing": 143, "cloudCover": 1, "uvIndex": 0, "visibility": 10, "ozone": 265.5}, {"time": 1580119200, "summary": "Overcast", "icon": "cloudy", "precipIntensity": 0.0088, "precipProbability": 0.13, "precipType": "rain", "temperature": 65.78, "apparentTemperature": 66.66, "dewPoint": 65.21, "humidity": 0.98, "pressure": 1014, "windSpeed": 3.7, "windGust": 7.04, "windBearing": 142, "cloudCover": 1, "uvIndex": 0, "visibility": 10, "ozone": 265.7}, {"time": 1580122800, "summary": "Overcast", "icon": "cloudy", "precipIntensity": 0.0083, "precipProbability": 0.14, "precipType": "rain", "temperature": 64.43, "apparentTemperature": 65.27, "dewPoint": 64.43, "humidity": 1, "pressure": 1014.6, "windSpeed": 2.79, "windGust": 4.32, "windBearing": 132, "cloudCover": 1, "uvIndex": 0, "visibility": 10, "ozone": 266.1}, {"time": 1580126400, "summary": "Overcast", "icon": "cloudy", "precipIntensity": 0.0081, "precipProbability": 0.14, "precipType": "rain", "temperature": 63.42, "apparentTemperature": 64.23, "dewPoint": 63.42, "humidity": 1, "pressure": 1015, "windSpeed": 2.09, "windGust": 2.43, "windBearing": 121, "cloudCover": 1, "uvIndex": 0, "visibility": 10, "ozone": 266.2}, {"time": 1580130000, "summary": "Overcast", "icon": "cloudy", "precipIntensity": 0.0077, "precipProbability": 0.13, "precipType": "rain", "temperature": 62.76, "apparentTemperature": 63.53, "dewPoint": 62.76, "humidity": 1, "pressure": 1014.8, "windSpeed": 1.86, "windGust": 1.93, "windBearing": 114, "cloudCover": 1, "uvIndex": 0, "visibility": 10, "ozone": 265.8}, {"time": 1580133600, "summary": "Overcast", "icon": "cloudy", "precipIntensity": 0.0069, "precipProbability": 0.13, "precipType": "rain", "temperature": 62.35, "apparentTemperature": 63.06, "dewPoint": 62.35, "humidity": 1, "pressure": 1014.3, "windSpeed": 1.9, "windGust": 1.9, "windBearing": 109, "cloudCover": 1, "uvIndex": 0, "visibility": 10, "ozone": 265.1}, {"time": 1580137200, "summary": "Overcast", "icon": "cloudy", "precipIntensity": 0.0061, "precipProbability": 0.13, "precipType": "rain", "temperature": 61.85, "apparentTemperature": 62.49, "dewPoint": 61.85, "humidity": 1, "pressure": 1013.9, "windSpeed": 1.94, "windGust": 1.95, "windBearing": 100, "cloudCover": 1, "uvIndex": 0, "visibility": 10, "ozone": 264.6}]}, "daily": {"summary": "Light rain next Sunday.", "icon": "rain", "data": [{"time": 1579957200, "summary": "Clear throughout the day.", "icon": "clear-day", "sunriseTime": 1579979460, "sunsetTime": 1580030460, "moonPhase": 0.05, "precipIntensity": 0.0005, "precipIntensityMax": 0.0039, "precipIntensityMaxTime": 1579957200, "precipProbability": 0.21, "precipType": "rain", "temperatureHigh": 85.99, "temperatureHighTime": 1580008020, "temperatureLow": 56.42, "temperatureLowTime": 1580058900, "apparentTemperatureHigh": 85.49, "apparentTemperatureHighTime": 1580008020, "apparentTemperatureLow": 56.91, "apparentTemperatureLowTime": 1580058900, "dewPoint": 57.29, "humidity": 0.71, "pressure": 1012.5, "windSpeed": 3.34, "windGust": 13.23, "windGustTime": 1579997040, "windBearing": 198, "cloudCover": 0.35, "uvIndex": 12, "uvIndexTime": 1580005680, "visibility": 9.866, "ozone": 276.9, "temperatureMin": 57.74, "temperatureMinTime": 1580043600, "temperatureMax": 85.99, "temperatureMaxTime": 1580008020, "apparentTemperatureMin": 58.23, "apparentTemperatureMinTime": 1580043600, "apparentTemperatureMax": 85.49, "apparentTemperatureMaxTime": 1580008020}, {"time": 1580043600, "summary": "Mostly cloudy throughout the day.", "icon": "partly-cloudy-day", "sunriseTime": 1580065980, "sunsetTime": 1580116800, "moonPhase": 0.08, "precipIntensity": 0.002, "precipIntensityMax": 0.0088, "precipIntensityMaxTime": 1580118540, "precipProbability": 0.2, "precipType": "rain", "temperatureHigh": 85.58, "temperatureHighTime": 1580094120, "temperatureLow": 59.09, "temperatureLowTime": 1580148900, "apparentTemperatureHigh": 85.08, "apparentTemperatureHighTime": 1580094120, "apparentTemperatureLow": 60.03, "apparentTemperatureLowTime": 1580149200, "dewPoint": 60.63, "humidity": 0.8, "pressure": 1013.7, "windSpeed": 3.4, "windGust": 12.05, "windGustTime": 1580104980, "windBearing": 78, "cloudCover": 0.77, "uvIndex": 8, "uvIndexTime": 1580089500, "visibility": 10, "ozone": 270.2, "temperatureMin": 56.42, "temperatureMinTime": 1580058900, "temperatureMax": 85.58, "temperatureMaxTime": 1580094120, "apparentTemperatureMin": 56.91, "apparentTemperatureMinTime": 1580058900, "apparentTemperatureMax": 85.08, "apparentTemperatureMaxTime": 1580094120}, {"time": 1580130000, "summary": "Overcast throughout the day.", "icon": "cloudy", "sunriseTime": 1580152440, "sunsetTime": 1580203140, "moonPhase": 0.11, "precipIntensity": 0.0017, "precipIntensityMax": 0.0077, "precipIntensityMaxTime": 1580130000, "precipProbability": 0.37, "precipType": "rain", "temperatureHigh": 75.03, "temperatureHighTime": 1580187240, "temperatureLow": 53.11, "temperatureLowTime": 1580232360, "apparentTemperatureHigh": 74.75, "apparentTemperatureHighTime": 1580186940, "apparentTemperatureLow": 53.6, "apparentTemperatureLowTime": 1580232360, "dewPoint": 61.1, "humidity": 0.88, "pressure": 1014.6, "windSpeed": 3.09, "windGust": 9.12, "windGustTime": 1580200080, "windBearing": 145, "cloudCover": 1, "uvIndex": 6, "uvIndexTime": 1580178120, "visibility": 9.579, "ozone": 261.9, "temperatureMin": 55.73, "temperatureMinTime": 1580216400, "temperatureMax": 75.03, "temperatureMaxTime": 1580187240, "apparentTemperatureMin": 56.22, "apparentTemperatureMinTime": 1580216400, "apparentTemperatureMax": 74.75, "apparentTemperatureMaxTime": 1580186940}, {"time": 1580216400, "summary": "Clear throughout the day.", "icon": "clear-day", "sunriseTime": 1580238900, "sunsetTime": 1580289540, "moonPhase": 0.14, "precipIntensity": 0, "precipIntensityMax": 0.0002, "precipIntensityMaxTime": 1580234400, "precipProbability": 0.04, "temperatureHigh": 84.99, "temperatureHighTime": 1580267040, "temperatureLow": 56.76, "temperatureLowTime": 1580317500, "apparentTemperatureHigh": 84.49, "apparentTemperatureHighTime": 1580267040, "apparentTemperatureLow": 57.45, "apparentTemperatureLowTime": 1580317680, "dewPoint": 55.87, "humidity": 0.74, "pressure": 1016.6, "windSpeed": 2.85, "windGust": 7.71, "windGustTime": 1580280060, "windBearing": 109, "cloudCover": 0.21, "uvIndex": 13, "uvIndexTime": 1580264400, "visibility": 10, "ozone": 257.3, "temperatureMin": 53.11, "temperatureMinTime": 1580232360, "temperatureMax": 84.99, "temperatureMaxTime": 1580267040, "apparentTemperatureMin": 53.6, "apparentTemperatureMinTime": 1580232360, "apparentTemperatureMax": 84.49, "apparentTemperatureMaxTime": 1580267040}, {"time": 1580302800, "summary": "Clear throughout the day.", "icon": "clear-day", "sunriseTime": 1580325360, "sunsetTime": 1580375880, "moonPhase": 0.17, "precipIntensity": 0.0001, "precipIntensityMax": 0.0002, "precipIntensityMaxTime": 1580322600, "precipProbability": 0.07, "precipType": "rain", "temperatureHigh": 96.54, "temperatureHighTime": 1580356800, "temperatureLow": 64.34, "temperatureLowTime": 1580405820, "apparentTemperatureHigh": 96.04, "apparentTemperatureHighTime": 1580356800, "apparentTemperatureLow": 64.83, "apparentTemperatureLowTime": 1580405820, "dewPoint": 53.55, "humidity": 0.62, "pressure": 1015.3, "windSpeed": 3.16, "windGust": 7.47, "windGustTime": 1580342940, "windBearing": 323, "cloudCover": 0.04, "uvIndex": 13, "uvIndexTime": 1580350200, "visibility": 10, "ozone": 256.9, "temperatureMin": 56.76, "temperatureMinTime": 1580317500, "temperatureMax": 96.54, "temperatureMaxTime": 1580356800, "apparentTemperatureMin": 57.45, "apparentTemperatureMinTime": 1580317680, "apparentTemperatureMax": 96.04, "apparentTemperatureMaxTime": 1580356800}, {"time": 1580389200, "summary": "Clear throughout the day.", "icon": "clear-day", "sunriseTime": 1580411820, "sunsetTime": 1580462220, "moonPhase": 0.2, "precipIntensity": 0.0001, "precipIntensityMax": 0.0003, "precipIntensityMaxTime": 1580440380, "precipProbability": 0.04, "precipType": "rain", "temperatureHigh": 97.61, "temperatureHighTime": 1580442360, "temperatureLow": 73.53, "temperatureLowTime": 1580477160, "apparentTemperatureHigh": 97.11, "apparentTemperatureHighTime": 1580442360, "apparentTemperatureLow": 74.09, "apparentTemperatureLowTime": 1580478780, "dewPoint": 48.06, "humidity": 0.41, "pressure": 1014.5, "windSpeed": 5.09, "windGust": 21.86, "windGustTime": 1580449020, "windBearing": 9, "cloudCover": 0.11, "uvIndex": 13, "uvIndexTime": 1580436900, "visibility": 10, "ozone": 253.2, "temperatureMin": 64.34, "temperatureMinTime": 1580405820, "temperatureMax": 97.61, "temperatureMaxTime": 1580442360, "apparentTemperatureMin": 64.83, "apparentTemperatureMinTime": 1580405820, "apparentTemperatureMax": 97.11, "apparentTemperatureMaxTime": 1580442360}, {"time": 1580475600, "summary": "Possible light rain overnight.", "icon": "partly-cloudy-day", "sunriseTime": 1580498280, "sunsetTime": 1580548560, "moonPhase": 0.23, "precipIntensity": 0.0011, "precipIntensityMax": 0.0115, "precipIntensityMaxTime": 1580562000, "precipProbability": 0.32, "precipType": "rain", "temperatureHigh": 96.37, "temperatureHighTime": 1580526600, "temperatureLow": 59.17, "temperatureLowTime": 1580588100, "apparentTemperatureHigh": 95.87, "apparentTemperatureHighTime": 1580526600, "apparentTemperatureLow": 60.58, "apparentTemperatureLowTime": 1580588520, "dewPoint": 62.38, "humidity": 0.51, "pressure": 1009.6, "windSpeed": 7.14, "windGust": 29.29, "windGustTime": 1580494140, "windBearing": 306, "cloudCover": 0.8, "uvIndex": 7, "uvIndexTime": 1580519760, "visibility": 9.938, "ozone": 248, "temperatureMin": 73.53, "temperatureMinTime": 1580477160, "temperatureMax": 96.37, "temperatureMaxTime": 1580526600, "apparentTemperatureMin": 74.09, "apparentTemperatureMinTime": 1580478780, "apparentTemperatureMax": 95.87, "apparentTemperatureMaxTime": 1580526600}, {"time": 1580562000, "summary": "Possible light rain in the morning.", "icon": "rain", "sunriseTime": 1580584740, "sunsetTime": 1580634900, "moonPhase": 0.26, "precipIntensity": 0.0175, "precipIntensityMax": 0.084, "precipIntensityMaxTime": 1580601480, "precipProbability": 0.7, "precipType": "rain", "temperatureHigh": 74.62, "temperatureHighTime": 1580613060, "temperatureLow": 53.96, "temperatureLowTime": 1580668020, "apparentTemperatureHigh": 74.12, "apparentTemperatureHighTime": 1580613060, "apparentTemperatureLow": 54.45, "apparentTemperatureLowTime": 1580668020, "dewPoint": 61.05, "humidity": 0.89, "pressure": 1011, "windSpeed": 4.53, "windGust": 20.22, "windGustTime": 1580562000, "windBearing": 181, "cloudCover": 0.73, "uvIndex": 11, "uvIndexTime": 1580612400, "visibility": 7.797, "ozone": 258.3, "temperatureMin": 56.15, "temperatureMinTime": 1580648400, "temperatureMax": 75.05, "temperatureMaxTime": 1580562000, "apparentTemperatureMin": 56.64, "apparentTemperatureMinTime": 1580648400, "apparentTemperatureMax": 76.27, "apparentTemperatureMaxTime": 1580562000}]}, "flags": {"sources": ["cmc", "gfs", "icon", "isd", "madis"], "nearest-station": 9.834, "units": "us"}, "offset": 11}'

def call():
    # main call function
    # we'll have lat and long: -37.090335, 149.370666 (random place in aussie)
    # example: https://api.darksky.net/forecast/4c3f861aeda2d6678caa8239dcfb13f6/-37.090335,149.370666

    #CONFIG DATA
    url_base = "https://api.darksky.net/forecast/"
    key = "4c3f861aeda2d6678caa8239dcfb13f6"
    lat = "-37.090335"
    long = "149.370666"

    #PROG START
    # we need to call the api
    URL = url_base + key + "/" + lat + "," + long
    #r = requests.get(url = URL)
    r = fake_data
    rjson = json.loads(r)

    current_bearing = rjson["currently"]["windBearing"]
    forecast = rjson["hourly"]["data"]
    for i in range(12):
        print(forecast[i]["windBearing"])

    # then extract the wind data
    #data = r.json()
    #print(data)
    # then save the wind data to the db

if __name__ == "__main__":
    call()

