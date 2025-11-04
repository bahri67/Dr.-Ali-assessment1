import random

# === Function to load jokes from file ===
def load_jokes(filename):
    jokes = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if "?" in line:  # split setup and punchline
                    setup, punchline = line.split("?", 1)
                    jokes.append((setup.strip() + "?", punchline.strip()))
    except FileNotFoundError:
        print("Error: jokes.txt file not found.")
    return jokes


# === Function to tell a random joke ===
def tell_joke(jokes):
    if not jokes:
        print("No jokes available.")
        return
    setup, punchline = random.choice(jokes)
    print("\nAlexa: " + setup)
    input("Press Enter to hear the punchline...")
    print("Alexa: " + punchline + "\n")


# === Main Function ===
def main():
    jokes = load_jokes("jokes.txt")

    print("=== Alexa Joke Assistant ===")
    print("Type 'Alexa tell me a joke' to hear one or 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "quit":
            print("Alexa: Goodbye! Have a funny day 😄")
            break
        elif user_input == "alexa tell me a joke":
            tell_joke(jokes)
        else:
            print("Alexa: I didn’t understand that. Try typing 'Alexa tell me a joke' or 'quit'.")

# === Run the program ===
if __name__ == "__main__":
    main()
