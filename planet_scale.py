import tkinter as tk
from tkinter import font as tkfont

def radius_calculator(radius):
    radius_of_planets = {
    'Sun': 696340, 'Mercury': 2440, 'Venus': 6052, 'Earth': 6371,
    'Mars': 3390, 'Jupiter': 69911, 'Saturn': 58232, 'Uranus': 25362, 'Neptune': 24622}
    new_radius={}
    for planet in radius_of_planets:
        radius_in_meters=((radius*radius_of_planets[planet])/radius_of_planets['Sun'])
        new_radius[planet]=round(radius_in_meters, 5)
    return new_radius
def orbit_calculator(radius):
    orbital_distance_in_million_km = {
    'Mercury': 58, 'Venus': 108, 'Earth': 150, 'Mars': 228,
    'Jupiter': 778, 'Saturn': 1446, 'Uranus': 2928, 'Neptune': 4472}
    new_orbit_distance={}
    for planet in orbital_distance_in_million_km:
        orbit_in_meters=((orbital_distance_in_million_km[planet]*radius)/0.696340)
        new_orbit_distance[planet]=round(orbit_in_meters,5)
    return new_orbit_distance

def data_formatter(new_radius,new_orbit_distance,sun_radius):
    radius_and_orbit_distance={}
    for planet in [new_radius,new_orbit_distance]:
        for key, value in planet.items():
            if key in radius_and_orbit_distance:
                radius_and_orbit_distance[key].append(value)
            else:
                radius_and_orbit_distance[key] = [value]
    output_data = []
    output_data.append(f"{'Planet Name':<15} {'Radius (meters)':<20} {'Orbit Distance (meters)'}")
    output_data.append('-' * 50)
    # Display the sun
    sun_radius = radius_and_orbit_distance.get('Sun', [''])[0]
    output_data.append(f"{'Sun':<15} {sun_radius:<20}")
    # Display planets
    for planet, values in radius_and_orbit_distance.items():
        if planet != 'Sun':
            radius = values[0]
            orbit_distance = values[1] if len(values) > 1 else 'N/A'
            output_data.append(f"{planet:<15} {radius:<20} {orbit_distance}")
    return "\n".join(output_data)

def calculate():
    radius = entry.get()
    try:
        radius = int(radius)
        new_radius=radius_calculator(radius)
        new_orbit_distance=orbit_calculator(radius)
        output_data=data_formatter(new_radius,new_orbit_distance,radius)
        output_label.config(text=f"{output_data}")
    except ValueError:
        output_label.config(text="Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Sun Solar System Scale Calculator")
root.geometry("1280x720")
font = tkfont.Font(family="Poppins", size=12)
title_label = tk.Label(root, text="Enter Radius of Sun in meters", font=font)
title_label.pack(pady=10)
entry = tk.Entry(root, font=font)
entry.pack(pady=5)
calculate_button = tk.Button(root, text="Calculate", font=font, command=calculate)
calculate_button.pack(pady=10)
output_label = tk.Label(root, text="", font=font)
output_label.pack(pady=10)
root.eval('tk::PlaceWindow . center')
root.mainloop()
