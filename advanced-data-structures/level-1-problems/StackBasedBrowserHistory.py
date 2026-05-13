back_stack = []
forward_stack = []

current_page = "A"

# Visit B
back_stack.append(current_page)
current_page = "B"

# Visit C
back_stack.append(current_page)
current_page = "C"

# Back
forward_stack.append(current_page)
current_page = back_stack.pop()

# Forward
back_stack.append(current_page)
current_page = forward_stack.pop()

print("Current Page:", current_page)