def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) < 2:
        return "Error: You must provide both name and phone number."
    name, phone = args[0], args[1]
    contacts[name] = phone
    return f"Contact {name} added."

def change_contact(args, contacts):
    if len(args) < 2:
        return "Error: You must provide both name and new phone number."
    name, phone = args[0], args[1]
    if name in contacts:
        contacts[name] = phone
        return f"Contact {name} updated."
    else:
        return f"Error: Contact {name} not found."

def show_phone(args, contacts):
    if len(args) < 1:
        return "Error: You must provide a name."
    name = args[0]
    if name in contacts:
        return f"{name}'s phone number: {contacts[name]}"
    else:
        return f"Error: Contact {name} not found."

def show_all(contacts):
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

