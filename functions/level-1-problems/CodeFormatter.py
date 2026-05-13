def format_message(message: str):
    formatted_message = f"{40*'-'}{message}{40*'-'}"
    return formatted_message

message = input("Enter message: ")

formatted_message = format_message(message)

print(formatted_message)