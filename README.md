Weather App
Weather App is a simple desktop application that provides real-time weather data for any city in the world. Users can input a city name to view the current temperature, weather conditions, humidity, and more.

Features
Weather Data: Retrieve real-time weather data from OpenWeatherMap API by entering a city name.
Timezone & Local Time: Displays the local time and timezone for the selected city.
User-Friendly Interface: A clean and intuitive interface built with Tkinter.

Technologies Used
Python: Main programming language.
Tkinter: GUI (Graphical User Interface) framework.
OpenWeatherMap API: Fetches weather data.
Geopy: Retrieves latitude and longitude information from city names.
TimezoneFinder: Determines the timezone and local time based on city coordinates.
Pytz: Handles timezone-related operations.

Installation Requirements
This app requires Python 3.x and the following Python libraries:
requests
geopy
timezonefinder
pytz
tkinter (Usually included with Python, but may need to be installed separately on some systems)


Steps to Set Up Install Python dependencies:
pip install requests geopy timezonefinder pytz

Usage
Once the app opens, you'll see a search box where you can enter a city name.
After entering a city, click the search button to fetch the weather data for that city.
The weather data includes temperature, weather description, wind speed, humidity, and pressure.
