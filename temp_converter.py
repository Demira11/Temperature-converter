def convert_temp(start_temp, temp_unit):
    if temp_unit == "f":
        celsius = (start_temp - 32) * 5/9
        kelvin = celsius + 273.15
        print(f"{start_temp}°F is equal to {celsius:.2f}°C and {kelvin:.2f}K")

    elif temp_unit == "C":
        fahrenheit = (start_temp * 9/5) + 32
        kelvin = start_temp + 273.15
        print(f"{start_temp}°C is equal to {fahrenheit:.2f}°F and {kelvin:.2f}K")

    elif temp_unit == "K":
        celsius = start_temp - 273.15
        fahrenheit = (celsius * 9/5) + 32
        print(f"{start_temp}K is equal to {celsius:.2f}°C and {fahrenheit:.2f}°F")

    else:
        print("Invalid temperature unit. Please enter 'f', 'C', or 'K'.")

# Get user inputs
start_temp = float(input("Enter the starting temperature: "))
temp_unit = input("Enter the temperature unit (f, C, or K): ")

# Call the convert_temp method
convert_temp(start_temp, temp_unit)
