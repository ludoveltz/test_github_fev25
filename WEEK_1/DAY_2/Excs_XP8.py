def run_quiz(data):
    correct_answers = 0
    wrong_answers = []
    
    print("\n=== STAR WARS QUIZ ===\n")
    
    # Loop through each question
    for question_data in data:
        # Ask question and get user's answer
        print(question_data["question"])
        user_answer = input("Your answer: ").strip()
        
        # Check if answer is correct
        if user_answer.lower() == question_data["answer"].lower():
            correct_answers += 1
            print("Correct! ✨\n")
        else:
            # Store wrong answers for later
            wrong_answers.append({
                "question": question_data["question"],
                "user_answer": user_answer,
                "correct_answer": question_data["answer"]
            })
            print("Incorrect! 😕\n")

    return correct_answers, wrong_answers

def display_results(correct_answers, wrong_answers, total_questions):
    """Function to display quiz results."""
    print("\n=== QUIZ RESULTS ===")
    print(f"Correct answers: {correct_answers}/{total_questions}")
    print(f"Incorrect answers: {len(wrong_answers)}/{total_questions}")
    
    # Calculate percentage
    percentage = (correct_answers / total_questions) * 100
    
    # Display appropriate message based on score
    if percentage == 100:
        print("\nPerfect score! You are a true Jedi Master! 🌟")
    elif percentage >= 80:
        print("\nGreat job! The Force is strong with you! ⚔️")
    elif percentage >= 50:
        print("\nNot bad, young Padawan. Keep training! 🎯")
    else:
        print("\nTime to brush up on your Star Wars knowledge! 📚")
    
    # Display wrong answers if any
    if wrong_answers:
        print("\n=== QUESTIONS YOU MISSED ===")
        for i, wrong in enumerate(wrong_answers, 1):
            print(f"\nQuestion {i}:")
            print(f"Q: {wrong['question']}")
            print(f"Your answer: {wrong['user_answer']}")
            print(f"Correct answer: {wrong['correct_answer']}")
    
    # Ask to play again if too many wrong answers
    if len(wrong_answers) > 3:
        print("\nYou had more than 3 wrong answers.")
        play_again = input("Would you like to try again? (yes/no): ").lower()
        return play_again == 'yes'
    
    return False

def main():
    """Main function to run the quiz."""
    data = [
        {
            "question": "What is Baby Yoda's real name?",
            "answer": "Grogu"
        },
        {
            "question": "Where did Obi-Wan take Luke after his birth?",
            "answer": "Tatooine"
        },
        {
            "question": "What year did the first Star Wars movie come out?",
            "answer": "1977"
        },
        {
            "question": "Who built C-3PO?",
            "answer": "Anakin Skywalker"
        },
        {
            "question": "Anakin Skywalker grew up to be who?",
            "answer": "Darth Vader"
        },
        {
            "question": "What species is Chewbacca?",
            "answer": "Wookiee"
        }
    ]
    
    play = True
    while play:
        # Run the quiz
        correct_answers, wrong_answers = run_quiz(data)
        
        # Display results and check if player wants to play again
        play = display_results(correct_answers, wrong_answers, len(data))

# Start the quiz
if __name__ == "__main__":
    main()
