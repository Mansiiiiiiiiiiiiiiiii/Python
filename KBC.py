def ask_questions_and_calculate_amount(questions_and_answers):
    total_amount = 0
    
    for question, correct_answer, amount in questions_and_answers:
        print(question)
        user_answer = input("Your answer: ").strip()
        
        if user_answer.lower() == correct_answer.lower():
            total_amount += amount
            print("Correct! You've earned ${}.".format(amount))
        else:
            print("Incorrect. The correct answer was '{}'.".format(correct_answer))
        
        print()  # Print a newline for better readability
    
    return total_amount

def main():
    questions_and_answers = [
        ("What is the capital of France?", "Paris", 50),
        ("What is 5 + 7?", "12", 30),
        ("What color do you get when you mix red and white?", "Pink", 20),
        # Add more questions and their corresponding correct answers and amounts
    ]
    
    print("Welcome to the Quiz Game!")
    print("-------------------------")
    final_amount = ask_questions_and_calculate_amount(questions_and_answers)
    
    print("Game over!")
    print("You are taking home ${}.".format(final_amount))

if __name__ == "__main__":
    main()
