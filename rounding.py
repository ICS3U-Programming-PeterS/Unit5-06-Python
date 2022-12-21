#!/usr/bin/env python3

# Created by: Peter Sobowale
# Created on: Dec 14 2022
# This program asks the user to enter a decimal
# it then sends it to a function then rounds it


# function that rounds decimals
def round_decimal(dec_array, decimal_place):
    # how to round a decimal
    dec_array[0] = dec_array[0] * (10**decimal_place)
    dec_array[0] += 0.5
    dec_array[0] = int(dec_array[0])
    dec_array[0] = dec_array[0] / (10**decimal_place)


# Function to get the users number
def main():
    # declare empty list
    user_dec = []

    # Explain what the program is about
    print("This program rounds decimals to the number of decimal places entered ")

    # get the users decimal number
    dec_num_string = input("Enter a decimal number: ")

    try:
        dec_num_float = float(dec_num_string)

        # append the users number to the list
        user_dec.append(dec_num_float)

        # Get number of decimal places
        decimal_place_str = input("Enter the number of decimal places: ")

        try:
            # Convert the number of decimal numbers to an integer
            decimal_place_int = int(decimal_place_str)

            # Check if the number is negative
            if decimal_place_int < 0:
                # Tell them if it isn't
                print("{} is not a positive integer.".format(decimal_place_int))
            else:

                # Call the function that rounds the number
                round_decimal(user_dec, decimal_place_int)
                # Display the rounded number
                print(
                    "{} rounded to {} decimals is {}".format(
                        dec_num_float, decimal_place_int, user_dec[0]
                    )
                )

        # Message fro invalid input on second conversion
        except Exception:
            print("Invalid input!")

    # invalid input if string enter instead of float
    except Exception:
        print("{} is not a decimal number".format(dec_num_string))


if __name__ == "__main__":
    main()
