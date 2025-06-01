import os
import shutil
import random
import string


def calculator():
    try:
        a = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        b = float(input("Enter second number: "))

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0:
                print("Error: Cannot divide by zero.")
                return
            result = a / b
        else:
            print("Invalid operator.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

# File Organizer
def organize_files():
    src = input("Enter source folder path: ").strip()
    if not os.path.exists(src):
        print("Source folder not found.")
        return

    for file in os.listdir(src):
        ext = os.path.splitext(file)[1][1:]  # get extension without dot
        if ext:  # only files with extensions
            folder = os.path.join(src, ext)
            os.makedirs(folder, exist_ok=True)
            try:
                shutil.move(os.path.join(src, file), os.path.join(folder, file))
                print(f"Moved '{file}' to folder '{ext}'")
            except Exception as e:
                print(f"Failed to move '{file}': {e}")


def generate_password():
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Length must be positive.")
            return
    except ValueError:
        print("Please enter a valid integer.")
        return

    chars = string.ascii_letters + string.digits + string.punctuation
    password_chars = list(map(lambda _: random.choice(chars), range(length)))
    password = ''.join(password_chars)
    print(f"Generated password: {password}")


def unit_conversion():
    raw = input("Enter values in cm (comma-separated): ")
    try:
        cm_values = list(map(float, raw.split(',')))
        inches = list(map(lambda x: round(x / 2.54, 2), cm_values))
        print(f"Values in inches: {inches}")
    except ValueError:
        print("Invalid input. Please enter numeric values separated by commas.")

def copy_text_and_csv():
    src_folder = input("Enter source folder path: ").strip()
    dest_folder = input("Enter destination folder path: ").strip()

    if not os.path.exists(src_folder):
        print("Source folder does not exist.")
        return

    os.makedirs(dest_folder, exist_ok=True)
    files_copied = [f for f in os.listdir(src_folder) if f.endswith(('.txt', '.csv'))]

    for f in files_copied:
        shutil.copy(os.path.join(src_folder, f), os.path.join(dest_folder, f))
        print(f"Copied: {f}")

    if not files_copied:
        print("No .txt or .csv files found.")
