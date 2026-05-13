try:
    int("abc")

except Exception as e:
    with open("error.log", "w") as file:
        file.write(f"{type(e).__name__}: {e}")

    print("Exception logged into error.log")