def give_options(x, y, z):
    print("a):", x)
    print("b):", y)
    print("c):", z)

print("Hello! Welcome to the Anime Quiz!")
print("All questions carry 10 marks each.")
ans = input("Are you ready to play (yes/no): ")

note = "Note: Write answers! Do not write the option (a/b/c)."
score = 0
total_questions = 4

# All correct answers in lowercase for case-insensitive comparison
correct_ans = ["monkey d. luffy", "konoha", "death note", "eren yeager"]

if ans.lower() == "yes":
    print(note)

    print("\nQuestion 1: Who is the main protagonist of One Piece?")
    give_options("Naruto Uzumaki", "Monkey D. Luffy", "Ichigo Kurosaki")
    ans = input(">>> ").strip().lower()
    if ans == correct_ans[0]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    print(note)
    print("\nQuestion 2: What is the name of the village Naruto belongs to?")
    give_options("Konoha", "Suna", "Kiri")
    ans = input(">>> ").strip().lower()
    if ans == correct_ans[1]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    print(note)
    print("\nQuestion 3: Which anime features a notebook that kills anyone whose name is written in it?")
    give_options("Tokyo Ghoul", "Attack on Titan", "Death Note")
    ans = input(">>> ").strip().lower()
    if ans == correct_ans[2]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    print(note)
    print("\nQuestion 4: Who is the main character of Attack on Titan?")
    give_options("Levi Ackerman", "Eren Yeager", "Armin Arlert")
    ans = input(">>> ").strip().lower()
    if ans == correct_ans[3]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")

    final_score = score * 10
    print("\nQuiz Completed!")
    print(f"Your score: {final_score} / 40")

    if final_score < 30:
        print("Oof, better luck next time!")
    elif final_score == 30:
        print("Great job! You're quite the otaku!")
    else:
        print("Perfect score! You're an anime expert!")
else:
    print("Maybe next time!")