from functions import calculator, organize_files, generate_password, unit_conversion, copy_text_and_csv

def main():
    while True:
        print("\n--- Modular CLI Toolkit ---")
        print("1. Calculator")
        print("2. File Organizer")
        print("3. Password Generator")
        print("4. Unit Conversion (cm to inches)")
        print("5. Copy .txt and .csv files")
        print("0. Exit")

        choice = input("Select an option: ").strip()
        if choice == '1':
            calculator()
        elif choice == '2':
            organize_files()
        elif choice == '3':
            generate_password()
        elif choice == '4':
            unit_conversion()
        elif choice == '5':
            copy_text_and_csv()
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
