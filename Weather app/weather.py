import tkinter as tk
from PIL import Image, ImageTk
import requests
import time

def on_entry_click(event):
    if textfield.get() == placeholder_text:
        textfield.delete(0, tk.END)
        textfield.configure(fg='black')

def on_focus_out(event):
    if textfield.get() == '':
        textfield.insert(0, placeholder_text)
        textfield.configure(fg='gray')

def getweather():
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=e948b4fd36e154f9fa79e0812c969f69"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunrise'] + 10800))
    sunset = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunset'] + 10800))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = (
        "\n"
        + "Max Temp: "
        + str(max_temp)
        + "\n"
        + "Min Temp: "
        + str(min_temp)
        + "\n"
        + "Pressure: "
        + str(pressure)
        + "\n"
        + "Humidity: "
        + str(humidity)
        + "\n"
        + "Wind Speed: "
        + str(wind)
        + "\n"
        + "Sunrise: "
        + sunrise
        + "\n"
        + "Sunset: "
        + sunset
    )
    label1.config(text=final_info)
    label2.config(text=final_data)

    # Update weather icon based on the condition
    if condition == "Clear":
        image_path = "Image/clear.png"
    elif condition == "Rain":
        image_path = "Image/rain.png"
    elif condition == "Clouds":
        image_path = "Image/cloudy.png"
    else:
        image_path = "Image/weather.png"

    # Load the image
    weather_icon = Image.open(image_path)

    # Resize the image
    icon_width = 60 # Adjust the width as needed
    icon_height = 60  # Adjust the height as needed
    weather_icon = weather_icon.resize((icon_width, icon_height), Image.ANTIALIAS)

    # Convert the resized image to PhotoImage
    weather_icon = ImageTk.PhotoImage(weather_icon)

    icon_label.config(image=weather_icon)
    icon_label.image = weather_icon

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

placeholder_text = 'Enter city name'

textfield = tk.Entry(canvas, font=t)
textfield.insert(0, placeholder_text)
textfield.config(fg='gray')
textfield.bind('<FocusIn>', on_entry_click)
textfield.bind('<FocusOut>', on_focus_out)
textfield.pack(pady=20)
textfield.focus()

label1 = tk.Label(canvas, font=t)
label1.pack()

icon_label = tk.Label(canvas)
icon_label.pack()

label2 = tk.Label(canvas, font=f)
label2.pack()

get_button = tk.Button(canvas, text="Get Weather", font=t, command=getweather)
get_button.pack(pady=20)

canvas.mainloop()
