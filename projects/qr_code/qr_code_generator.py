import qrcode
import os.path
from pathlib import Path

# defining the paths (edit on a different pc)
current_path = "/Users/eglootz/pydev/projects/qr_code/"
new_path = "/Users/eglootz/pydev/projects/qr_code/qr_codes/"

# getting input from the user
link = str(input("Please enter a valid link or string: "))

# defining the file name
# file_name = (f"{link}.jpg")

file_name = input("How would you like to call the file (without /)? ") + ".jpg"


# setting a variable for the new file path
location = os.path.join(new_path, file_name)

# checking if the qr-code already exists
print("Checking if the qr-code already exists...")
check_file = Path(location)
if not check_file.is_file():

    print(f"Generating QR-Code for '{link}'...")

    # making the qr-code
    img = qrcode.make(link)

    print(f"Saving the qr-code as {file_name}...")

    try:
        # saving the qr-code as a .jpg file
        img.save(file_name)
        # moving the file from the current directory into a different folder
        Path(f"{current_path}/{file_name}").rename(f"{location}")

        print(f"File saved at {location}")

    except TypeError:
        print("catching classes that do not inherit from BaseException is not allowed")

    except OSError:
        print("There is probably already a file with that name! Or you used a /. Figure it out.")

    except FileNotFoundError:
        print("you probably used a /")


else:
    print(
        f"A QR-Code for this website/string already exists! Please look into the folder {new_path}")
