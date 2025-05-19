import os
from datetime import datetime


journal_folder = "journal"


if not os.path.exists(journal_folder):
    os.makedirs(journal_folder)

def get_filename(date_str):
    return os.path.join(journal_folder, f"{date_str}.txt")

def create_entry():
    today = datetime.now().strftime("%Y-%m-%d")
    filename = get_filename(today)

    if os.path.exists(filename):
        choice = input("Entry for today already exists. Overwrite (o) / Append (a) / Cancel (c)? ").lower()
        if choice == 'c':
            print("Operation cancelled.")
            return
        elif choice == 'o':
            mode = 'w'
        elif choice == 'a':
            mode = 'a'
        else:
            print("Invalid choice.")
            return
    else:
        mode = 'w'

    print("\nType your journal entry (end with a blank line):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    with open(filename, mode, encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Journal saved as '{journal}'.")

def view_entry():
    date_str = input("Enter date to view (YYYY-MM-DD): ")
    filename = get_filename(date_str)

    if os.path.exists(journal):
        with open(journal, 'r', encoding="utf-8") as f:
            content = f.read()
        print(f"\n--- Journal Entry for {date_str} ---\n")
        print(content)
    else:
        print("No journal entry found for that date.")

def delete_entry():
    date_str = input("Enter date to delete (YYYY-MM-DD): ")
    filename = get_filename(date_str)

    if os.path.exists(journal):
        os.remove(journal)
        print(f"Journal entry for {date_str} deleted.")
    else:
        print("No journal entry found for that date.")

def main():
    while True:
        print("\n--- Daily Journal Manager ---")
        print("1. Create Journal Entry")
        print("2. View Journal Entry")
        print("3. Delete Journal Entry")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            create_entry()
        elif choice == '2':
            view_entry()
        elif choice == '3':
            delete_entry()
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
