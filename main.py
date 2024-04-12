# For random
import random
# all question types
all_question_types = ["+", "-", "x", "/"]

# Global  comments
score = 0
first_number = random.randrange(1, 20)
second_number = random.randrange(1, 20)
question_number = 0
question_count = 0
final_question_count = 0

def int_checker(question):
    # Repeats until right
    while True:
        try:
            # Trys to return an int
            return int(input(question))
        except:
            # If cant return int print this
            print("Please enter a valid number")


def one_question():
    #these give the question diffrent numbers
    global question_types, score
    question_types = random.choice(all_question_types)
    first_number = random.randrange(1, 20)
    second_number = random.randrange(1, 20)
    correct_answer = 0.0
#this gives the diffrent question types
    if question_types == "+":
        correct_answer = first_number + second_number
    elif question_types == "-":
        correct_answer = first_number - second_number
    elif question_types == "x":
        correct_answer = first_number * second_number
    elif question_types == "/":
        correct_answer = first_number / second_number
    correct_answer = round(correct_answer, 1)
    question = "What is {} {} {}? (rounded to the first decimal place)\n".format(first_number, question_types, second_number)
    #this stores the user answer
    user_answer = float(input(question))
    user_answer = round(user_answer, 1)
    if user_answer == round(correct_answer, 1):
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect! The correct answer was {correct_answer}")
def main():
    global question_number, question_count, final_question_count
    while True:
        game = input("Are you ready to play? (Y/N)\n").capitalize()
#this is to start the questions
        if game == "Yes" or game == "Y":
            question_count = question_number + int_checker(f"How many questions do you want {username}?\n")
            final_question_count += question_count
            print("Alrighty Then Starting Quiz")
            break

        elif game == "No" or game == "N":
            print("Too Bad you playing")
        else:
            print("Bro put a valid answer")

    for question_number in range(question_count):
        print(f"Question {question_number + 1}")
        one_question()

    print("Well done")
    print(f"You Got {score} / {final_question_count} correct!")
#this is the start of the game
print("~~~~~Math Quiz~~~~~")
username = input("Enter your name please\n").capitalize()
print("Welcome to the game {}".format(username))

main()
#this lets me replay the code
replay = input("Would you like to replay? (Y/N)\n").upper()
if replay == "YES" or replay == "Y":
    main()
elif replay == "NO" or replay == "N":
    print("Thank you for playing")

