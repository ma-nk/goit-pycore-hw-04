from argparse import ArgumentError


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    if len(args) != 2:
        raise ArgumentError(args, "Input should contain exactly two arguments")
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def get_all_contacts(contacts):
    return "\n".join(f'{name} : {value}' for (name, value) in contacts.items())


def get_user_phone(args, contacts):
    if len(args) != 1:
        raise ArgumentError(args, "Input should contain single username")
    username = args[0].strip()
    try:
        phone = contacts[username]
        return phone
    except KeyError:
        return "That username does not exist"


def change_phone(args, contacts):
    if len(args) != 2:
        return "Input should contain exactly two arguments"

    user, phone = args
    if user not in contacts:
        return "That username does not exist"

    contacts[user] = phone
    return f"Updated {user} contact with phone {phone}"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(get_user_phone(args, contacts))
        elif command == "all":
            print(get_all_contacts(contacts))
        elif command == "change":
            print(change_phone(args, contacts))
        else:
            print("Invalid command.")
            break


if __name__ == "__main__":
    main()
