# =============================
# 🎯 Python Quiz Game
# Made by: [Maryamm!]
# =============================
import random

#  Questions stored in a list of dictionaries
questions = [
    {"question": "What is the capital of Pakistan?", "answer": "islamabad"},
    {"question": "How many planets are in our solar system?", "answer": "8"},
    {"question": "What does CPU stand for?", "answer": "central processing unit"},
    {"question": "Which language is used for AI and Data Science?", "answer": "python"},
    {"question": "What is 15 x 4?", "answer": "60"},
    {"question": "What do you call a fish without eyes?","answer":"fsh"},
    {"question": "What has keys but no locks no space but a room?" ,"answer":"keyboard"}
]

# --- Function to run the quiz ---
def run_quiz(questions):
    score = 0        # Variable to track score
    total = len(questions)   # Total number of questions

    print("=" * 40)
    print("Welcome to the Python Quiz Game! 🎯")
    print("=" * 40)

    #Shuffle Questions
    random.shuffle(questions)


    # --- Loop through each question ---
    for i, q in enumerate(questions):
        print(f"Q{i+1}: {q['question']}")
        user_answer = input("Your Answer: ").strip().lower()

        if user_answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['answer']}\n")
    # --- Show Final Result ---
    print("=" * 40)
    print(f"Quiz Finished! Your Score: {score}/{total}")

    if score == total:
        print("🏆 Excellent! Perfect Score!")
    elif score >= total // 2:
        print("👍 Good Job! Keep it up!")
    else:
        print("📚 Keep Practicing!")

    print("=" * 40)
while True:
    print("1.Start Quizz:)")
    print("2.Exit")
    choice = input("Enter your Choice: ")
    if choice == "1":
      run_quiz(questions)
    elif choice == "2":
      print("Good BYE👋")
      break
    else:
      print("Invalid choice!Try again.")
