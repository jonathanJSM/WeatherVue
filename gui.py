# gui.py
import tkinter as tk
import weather_api

def update_weather(city_entry, temperature_label, description_label, weather_icon_label, weather_condition_label):
    city = city_entry.get()
    weather_data = weather_api.get_weather(city)

    if 'main' in weather_data and 'temp' in weather_data['main']:
        temperature_label.config(text=f"Temperature: {weather_data['main']['temp']}°C")
    else:
        temperature_label.config(text="Temperature: N/A")

    if 'weather' in weather_data and weather_data['weather']:
        description_label.config(text=f"Weather: {weather_data['weather'][0]['description']}")
        weather_icon_path = f"weather_icons/{weather_data['weather'][0]['icon']}.png"
        try:
            weather_icon = tk.PhotoImage(file=weather_icon_path)
            weather_icon_label.config(image="")
            animate_fade_in(weather_icon_label, weather_icon)
        except tk.TclError:
            weather_icon_label.config(image="")
        weather_condition_label.config(text=weather_data['weather'][0]['main'])
    else:
        description_label.config(text="Weather: N/A")
        weather_icon_label.config(image="")
        weather_condition_label.config(text="")

def setup_ui(app):
    app.geometry("300x400")

    city_label = tk.Label(app, text="Enter City:", font=("Helvetica", 14))
    city_label.pack(pady=10)

    city_entry = tk.Entry(app, font=("Helvetica", 12))
    city_entry.pack(padx=10, pady=5)

    get_weather_button = tk.Button(app, text="Get Weather", font=("Helvetica", 12), command=lambda: update_weather(city_entry, temperature_label, description_label, weather_icon_label, weather_condition_label))
    get_weather_button.pack(pady=5)

    temperature_label = tk.Label(app, text="Temperature: N/A", font=("Helvetica", 14))
    temperature_label.pack(pady=10)

    description_label = tk.Label(app, text="Weather: N/A", font=("Helvetica", 12))
    description_label.pack(pady=10)

    weather_icon_label = tk.Label(app)
    weather_icon_label.pack(pady=10)

    weather_condition_label = tk.Label(app, text="", font=("Helvetica", 12))
    weather_condition_label.pack(pady=10)

def animate_fade_in(widget, image, alpha=0):
    widget.config(image=image)
    widget.image = image
    widget.alpha = alpha

    if widget.alpha < 255:
        widget.alpha += 5
        new_image = image.subsample(2, 2).copy()
        new_image.putalpha(widget.alpha)
        widget.config(image=new_image)
        widget.image = new_image
        widget.after(50, lambda: animate_fade_in(widget, image, widget.alpha))
