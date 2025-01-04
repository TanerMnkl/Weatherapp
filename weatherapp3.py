
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getweather():
    city = textfield.get()

    if not city.strip():
        messagebox.showerror("Error", "Please enter a city name!")
        return

    try:
        # Use a proper user_agent
        geolocator = Nominatim(user_agent="weatherApp_your_email@example.com")
        location = geolocator.geocode(city)

        # Handle invalid or missing locations
        if location is None:
            messagebox.showerror("Error", "City not found! Please try again.")
            return

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        # Output the result for confirmation
        if result:
            print(f"Timezone: {result}")
        else:
            print("Timezone not found!")

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M:%p")
        clock.config(text=current_time)
        name.config(text="Current Weather")

        # Extract latitude and longitude
        lat = location.latitude
        lon = location.longitude

        # Construct API URL
        apikey = "7247d8cc561a901bd4ada79f5b4e776b"
        api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}"

        # Make API request and parse JSON data
        json_data = requests.get(api).json()

        # Check if the API response is valid
        if json_data.get("cod") != 200:
            messagebox.showerror("Error", f"Error: {json_data.get('message', 'Unable to fetch weather data.')}")
            return

        # Extract weather data
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)  # Convert from Kelvin to Celsius
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind_speed = json_data['wind']['speed']

        # Update UI
        t.config(text=(temp, "°"))
        c.config(text=(condition, "|", "FEELS LIKE", temp, "°"))
        w.config(text=f"{wind_speed} m/s")
        h.config(text=f"{humidity}%")
        d.config(text=f"{description}")
        p.config(text=f"{pressure} hPa")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


#Search Box
Search_image=PhotoImage(file="Copy of search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=('poppins',25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

Search_icon=PhotoImage(file="Copy of search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getweather)
myimage_icon.place(x=400,y=34)


#Logo
Logo_image=PhotoImage(file="Copy of logo.png")
logo=Label(image=Logo_image)
logo.place(x=150,y=100)

#Bottom Box
Frame_image=PhotoImage(file="Copy of box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root, font=("Helvetica",15))
name.place(x=30,y=100)
clock=Label(root, font=("Helvetica",20))
clock.place(x=30,y=1)

#label
label1=Label(root,text="WIND",font=("Helvetica",15,"bold"),fg="White",bg="#1ab5ef")
label1.place(x=120,y=400)

label1=Label(root,text="HUMIDITY",font=("Helvetica",15,"bold"),fg="White",bg="#1ab5ef")
label1.place(x=250,y=400)

label1=Label(root,text="DESCRIPTION",font=("Helvetica",15,"bold"),fg="White",bg="#1ab5ef")
label1.place(x=430,y=400)

label1=Label(root,text="PRESSURE",font=("Helvetica",15,"bold"),fg="White",bg="#1ab5ef")
label1.place(x=650,y=400)

t=Label(font=("Arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial", 15,"bold"))
c.place(x=400,y=250)


w=Label(text="...",font=("Arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)

h=Label(text="...",font=("Arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)

d=Label(text="...",font=("Arial",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)

p=Label(text="...",font=("Arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)









root.mainloop()

