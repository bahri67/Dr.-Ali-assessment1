# 01-MathsQuiz/maths_quiz.py
# --------------------------------------------------------
# Exercise 1 - Maths Quiz
# --------------------------------------------------------
# Functions required by the brief:
# 1. displayMenu()
# 2. randomInt()
# 3. decideOperation()
# 4. displayProblem()
# 5. isCorrect()
# 6. displayResults()
# --------------------------------------------------------

import random

# --------------------------------------------------------
# 1. Display the difficulty menu and return user choice
# --------------------------------------------------------
def displayMenu():
    print("\nDIFFICULTY LEVEL")
    print(" 1. Easy")
    print(" 2. Moderate")
    print(" 3. Advanced")
    while True:
        choice = input("Choose a level (1-3): ").strip()
        if choice in ('1', '2', '3'):
            return int(choice)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# --------------------------------------------------------
# 2. Generate random integers based on difficulty level
# --------------------------------------------------------
def randomInt(level):
    if level == 1:       # Easy - 1-digit
        return random.randint(1, 9)
    elif level == 2:     # Moderate - 2-digit
        return random.randint(10, 99)
    elif level == 3:     # Advanced - 4-digit
        return random.randint(1000, 9999)

# --------------------------------------------------------
# 3. Randomly decide between addition or subtraction
# --------------------------------------------------------
def decideOperation():
    return random.choice(['+', '-'])

# --------------------------------------------------------
# 4. Display a single arithmetic problem and return user’s answer
# --------------------------------------------------------
def displayProblem(num1, num2, operation):
    print(f"\n{num1} {operation} {num2} = ?")
    while True:
        answer = input("Enter your answer: ")
        if answer.lstrip('-').isdigit():
            return int(answer)
        else:
            print("Please enter a valid number.")

# --------------------------------------------------------
# 5. Check if the user's answer is correct
# --------------------------------------------------------
def isCorrect(userAnswer, correctAnswer):
    if userAnswer == correctAnswer:
        print("✅ Correct!")
        return True
    else:
        print("❌ Incorrect.")
        return False

# --------------------------------------------------------
# 6. Display final results and ranking
# --------------------------------------------------------
def displayResults(score):
    print("\n----------- RESULTS -----------")
    print(f"Final Score: {score} / 100")

    if score > 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"

    print(f"Rank: {grade}")
    print("--------------------------------\n")

# --------------------------------------------------------
# Main quiz logic (combines all functions)
# --------------------------------------------------------
def playQuiz():
    level = displayMenu()
    totalScore = 0

    for question in range(1, 11):
        num1 = randomInt(level)
        num2 = randomInt(level)
        operation = decideOperation()

        # Compute correct answer
        if operation == '+':
            correctAnswer = num1 + num2
        else:
            correctAnswer = num1 - num2

        print(f"\nQuestion {question} of 10")
        userAnswer = displayProblem(num1, num2, operation)

        # First attempt
        if isCorrect(userAnswer, correctAnswer):
            totalScore += 10
            continue

        # Second attempt
        print("Try again...")
        userAnswer = displayProblem(num1, num2, operation)
        if isCorrect(userAnswer, correctAnswer):
            totalScore += 5
        else:
            print(f"The correct answer was {correctAnswer}.")

    displayResults(totalScore)

# --------------------------------------------------------
# Replay Option
# --------------------------------------------------------
def main():
    print("Welcome to the Maths Quiz!")
    while True:
        playQuiz()
        playAgain = input("Would you like to play again? (y/n): ").lower()
        if playAgain != 'y':
            print("Thanks for playing! Goodbye 👋")
            break

# --------------------------------------------------------
# Run the program
# --------------------------------------------------------
if __name__ == "__main__":
    main()
