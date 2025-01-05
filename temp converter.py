def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin."""
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit."""
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def main():
    print("Welcome to the Temperature Converter!")
    print("1: Celsius to Fahrenheit")
    print("2: Fahrenheit to Celsius")
    print("3: Celsius to Kelvin")
    print("4: Kelvin to Celsius")
    print("5: Fahrenheit to Kelvin")
    print("6: Kelvin to Fahrenheit")

    choice = input("Choose a conversion (1-6): ")

    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius):.2f}°F")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F is equal to {fahrenheit_to_celsius(fahrenheit):.2f}°C")
    elif choice == "3":
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C is equal to {celsius_to_kelvin(celsius):.2f} K")
    elif choice == "4":
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"{kelvin} K is equal to {kelvin_to_celsius(kelvin):.2f}°C")
    elif choice == "5":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F is equal to {fahrenheit_to_kelvin(fahrenheit):.2f} K")
    elif choice == "6":
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"{kelvin} K is equal to {kelvin_to_fahrenheit(kelvin):.2f}°F")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
