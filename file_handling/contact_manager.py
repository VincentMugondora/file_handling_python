import os

FILE_NAME = "contacts.txt"

# Function to add a contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{phone},{email}\n")
    print("✅ Contact added successfully!\n")

# Function to view all contacts
def view_contacts():
    if not os.path.exists(FILE_NAME):
        print("⚠️ No contacts found!\n")
        return
    
    print("\n📜 Contact List:")
    with open(FILE_NAME, "r") as file:
        for line in file:
            name, phone, email = line.strip().split(",")
            print(f"📌 {name} | 📞 {phone} | 📧 {email}")
    print("\n")

# Function to search for a contact
def search_contact():
    search_name = input("Enter name to search: ").lower()
    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            name, phone, email = line.strip().split(",")
            if search_name in name.lower():
                print(f"\n✅ Found: {name} | 📞 {phone} | 📧 {email}\n")
                found = True
                break

    if not found:
        print("❌ Contact not found!\n")

# Function to delete a contact
def delete_contact():
    name_to_delete = input("Enter name of the contact to delete: ").lower()
    found = False

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    with open(FILE_NAME, "w") as file:
        for line in lines:
            name, phone, email = line.strip().split(",")
            if name.lower() != name_to_delete:
                file.write(line)
            else:
                found = True

    if found:
        print("✅ Contact deleted successfully!\n")
    else:
        print("❌ Contact not found!\n")

# Main menu
def main():
    while True:
        print("📖 CONTACT MANAGER 📖")
        print("1️⃣ Add Contact")
        print("2️⃣ View Contacts")
        print("3️⃣ Search Contact")
        print("4️⃣ Delete Contact")
        print("5️⃣ Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("👋 Exiting Contact Manager. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please enter a number between 1 and 5.\n")

# Run the program
if __name__ == "__main__":
    main()
