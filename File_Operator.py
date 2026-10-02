from datetime import datetime

class journalmanager:

    def __init__(self):
        self.filename = "journal.txt"

    def add_entry(self):
        try: 
            with open(self.filename, "x"):
                pass 
        except FileExistsError:
            pass

        entry = input("\nEnter your journal entry: ")

        with open(self.filename, "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{timestamp}]\n")
            file.write(f"{entry}\n")
            file.write("------------------------------\n")
        print("\nEntry added successfully!")

    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                data = file.read()

            if data.strip() == "":
                print("\nNo journal entries found.")
            else: 
                print("\nYour journal entries: ")
                print("----------------------------------------")
                print(data)

        except FileNotFoundError:
            print("\nError: No journal entries found. Start by adding a new entry!")

    def search_entry(self):
        try:
            with open(self.filename, "r") as file:
                data = file.read()

            keyword = input("\nEnter a keyword or date to search: ")

            lines = data.splitlines()
            found = False

            print("\nMatching Entries:")
            print("----------------------------------------")

            for i in range(len(lines)):
                if keyword.lower() in lines[i].lower():
                    if lines[i].startswith("["):
                        print(lines[i])
                        if i + 1 < len(lines):
                            print(lines[i + 1])
                    else:
                        if i > 0:
                            print(lines[i - 1])
                        print(lines[i])
                    print()
                    found = True

            if found == False:
                print("No entries were found for the keyword:", keyword)

        except ValueError:
            print(f"\nError: No entries were found for the keyword: {keyword}.")

    def delete_entries(self):
        try:
            with open(self.filename, "r") as file:
                data = file.read()

            if data.strip() == "":
                print("\nNo journal to delete.")
                return

            choice = input("\nAre you sure you want to delete all entries? (yes/no): ")
            
            if choice == "yes":
                with open(self.filename, "w") as file:
                    pass
                print("\nAll journal entries have been deleted.")
            else: 
                print("Delete cancelled.")

        except FileNotFoundError:
            print("\nNo Journal entries to delete.")

journal = journalmanager()

print("Welcome to Personal Journal Manager!")

while True:

    print("\nPlese select an option: ")
    print("1. Add a new Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    try:
        choice = int(input("\nUser Input: "))

        if choice == 1:
            journal.add_entry()
        elif choice == 2:
            journal.view_entries()
        elif choice == 3:
            journal.search_entry()
        elif choice == 4:
            journal.delete_entries()
        elif choice == 5:
            print("\nThank you using Personal Journal Manager. GoodBye!")
            break
        else:
            print("\nInvalid Option")

    except ValueError:
        print("\nInvalid option. Please select from the menu.")