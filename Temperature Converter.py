def main():
    user_input = float(input("Enter the temperature: "))
    unit = input("What unit is it(F, C, K): ").upper()
    if unit not in ["K", "C", "F"]:
        print("Invalid")
        main()
        return
    convert_to = input("What unit you want to convert to: ").upper()
    if convert_to not in ["K", "C", "F"]:
        print("Invalid")
        main()
        return

    if unit == "C" and convert_to == "F":
        F = ( user_input* 9/5) + 32
        print(f"Converted to: {F}F")
    elif unit == "F" and convert_to == "C":
        C = (user_input - 32) * 5/9
        print(f"Converted to: {C}C")
    elif unit == "C" and convert_to == "K":
        K = user_input + 273.15
        print(f"Converted to: {K}K")
    elif unit == "K" and convert_to == "C":
        C = user_input - 273.15
        print(f"Converted to: {C}C")
    elif unit == "F" and convert_to == "K":
        K = (user_input - 32) * 5/9 + 273.15
        print(f"Converted to: {K}K")
    elif unit == "K" and convert_to == "F":
        F = (user_input - 273.15) * 9/5 + 32
        print(f"Converted to: {F}F")
    else:
        print("No need for Conversion")

main()






