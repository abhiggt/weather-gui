import tkinter as tk
import requests
import webbrowser

def get_weather():
    global temperature_unit
    api_key = "8568da25818157d76051c7f5142f771b"
    city = city_entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={temperature_unit}"
    response = requests.get(url)
    weather_data = response.json()
    
    if response.status_code == 200:
        if "main" in weather_data:
            temperature = weather_data["main"].get("temp")
            wind_speed = weather_data["wind"].get("speed")
            description = weather_data["weather"][0].get("description")
            if temperature is not None and wind_speed is not None and description is not None:
                weather_label.config(text=f"{temperature}°", padx=20)
                wind_label.config(text=f"Wind Speed: {wind_speed} m/s")
                description_label.config(text=f"Condition: {description.title()}")
                show_tips(temperature)
                change_color(temperature)
                return
    weather_label.config(text="City not found")
    tips_label.config(text="")
    wind_label.config(text="")
    description_label.config(text="")

def show_tips(temperature):
    if temperature < 0:
        tips_label.config(text="Thand ka mahaul! Rajaii mei jaa")
    elif 0 <= temperature < 5:
        tips_label.config(text="Bhaisaaab, haath sekk lo")
    elif 5 <= temperature < 10:
        tips_label.config(text="Thandi hai zabardastt, jacket pehn lo.")
    elif 10 <= temperature < 15:
        tips_label.config(text="Mausam thik hai, thoda thanda hai.")
    elif 15 <= temperature < 20:
        tips_label.config(text="Bahar ka mausam accha hai, enjoy karo.")
    elif 20 <= temperature < 25:
        tips_label.config(text="Mausam garm ho raha hai, ice cream khaa .")
    elif 25 <= temperature < 30:
        tips_label.config(text="Garmi aa gayi hai, Zyaada paani peeyo.")
    elif 30 <= temperature <= 40:
        tips_label.config(text="Bohot garmi hai yaar! AC mei baitho")
    else:
        tips_label.config(text="Kahan Suraj mei baith gaya hai kya?")

def change_color(temperature):
    if temperature < 10:
        root.config(bg="aqua")
    elif 10 <= temperature < 20:
        root.config(bg="white")
    elif 20 <= temperature < 30:
        root.config(bg="#FFFF99")  # light yellow
    elif 30 <= temperature:
        root.config(bg="#FFA500")  # bright orange

def open_google_weather(event):
    city = city_entry.get()
    url = f"https://www.google.com/search?q=weather+{city}"
    webbrowser.open_new_tab(url)

root = tk.Tk()
root.title("Mausampy")
root.configure(bg="white")  # Default background color

temperature_unit = "metric"

# Create GUI elements
weather_frame = tk.Frame(root, bg="white")
weather_frame.pack(pady=30)

weather_label = tk.Label(weather_frame, text="", font=("Consolas", 60), bg="white", fg="#111")
weather_label.pack()

city_entry = tk.Entry(root, font=("Arial", 18), bg="white", fg="#111", insertbackground="#111")
city_entry.pack(padx=20, pady=(20, 0), ipadx=10, ipady=5)

search_button = tk.Button(root, text="Search", command=get_weather, bg="grey", fg="white")
search_button.pack(padx=20,pady=10, ipadx=10, ipady=5)

tips_label = tk.Label(root, text="", font=("Lucida Sans", 12), bg="white", fg="#111", wraplength=500)
tips_label.pack(pady=20)

wind_label = tk.Label(root, text="", font=("Arial", 14), bg="white", fg="#111")
wind_label.pack()

description_label = tk.Label(root, text="", font=("Arial", 14), bg="white", fg="#111")
description_label.pack()

mausampy_label = tk.Label(root, text="mausampy 🌦", font=("Consolas",20), fg="#111", cursor="hand2")
mausampy_label.pack(pady=(20, 10))
mausampy_label.bind("<Button-1>", open_google_weather)

root.mainloop()
