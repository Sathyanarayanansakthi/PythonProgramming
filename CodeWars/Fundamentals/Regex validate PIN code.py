# Regex validate PIN code

"""ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false"""


def validate_pin(pin):
    pin_str = str(pin)  # convert to string
    if pin_str.isdigit() and (len(pin_str) == 4 or len(pin_str) == 6):
        return True
    else:
        return False