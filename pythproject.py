print("###################")
print("Welcome to Pythoquizzy.")
print("Get ready to boost your concepts of python with us.")

ques_bank = [    #set of questions and their respective answer
    {"text": "Which of the following is the correct extension of the Python file?", "answer": "c"},
    {"text": "Is Python code compiled or interpreted?", "answer": "a"},
    {"text": "All keywords in Python are in _________", "answer": "d"},
    {"text": "What will be the value of the following Python expression?\n4 + 3 % 5", "answer": "a"},
    {"text": "Which of the following is used to define a block of code in Python language?", "answer": "a"},
    {"text": "Which keyword is used for function in Python language?", "answer": "b"},
    {"text": "Which of the following character is used to give single-line comments in Python?", "answer": "b"},
    {"text": "What will be the output of the following Python code?\ni = 1\nwhile True:\n    if i%3 == 0:\n        break\n    print(i)\n    i += 1", "answer": "b"},
    {"text": "Which of the following functions can help us to find the version of python that we are currently working on?", "answer": "d"},
    {"text": "Python supports the creation of anonymous functions at runtime, using a construct called __________", "answer": "c"},
    {"text": "What is the order of precedence in python?", "answer": "d"},
    {"text": "What will be the output of the following Python code snippet if x=1?\nx<<2", "answer": "a"},
    {"text": "What does pip stand for python?", "answer": "c"},
    {"text": "Which of the following is true for variable names in Python?", "answer": "b"},
    {"text": "What are the values of the following Python expressions?\n2*(32)\n(23)2\n23*2", "answer": "a"},
]

options = [  #list of opyions for each questions
    ["a) .python", "b) .pl", "c) .py", "d) .p"],
    ["a) Python code is both compiled and interpreted", "b) Python code is neither compiled nor interpreted", "c) Python code is only compiled", "d) Python code is only interpreted"],
    ["a) Capitalized", "b) lower case", "c) UPPER CASE", "d) None of the mentioned"],
    ["a) 7", "b) 2", "c) 4", "d) 1"],
    ["a) Indentation", "b) Key", "c) Brackets", "d) All of the mentioned"],
    ["a) Function", "b) def", "c) Fun", "d) Define"],
    ["a) //", "b) #", "c) !", "d) /*"],
    ["a) 1 2 3", "b) error", "c) 1 2", "d) none of the mentioned"],
    ["a) sys.version(1)", "b) sys.version(0)", "c) sys.version()", "d) sys.version"],
    ["a) pi", "b) anonymous", "c) lambda", "d) none of the mentioned"],
    ["a) Exponential, Parentheses, Multiplication, Division, Addition, Subtraction", "b) Exponential, Parentheses, Division, Multiplication, Addition, Subtraction", "c) Parentheses, Exponential, Multiplication, Division, Subtraction, Addition", "d) Parentheses, Exponential, Multiplication, Division, Addition, Subtraction"],
    ["a) 4", "b) 2", "c) 1", "d) 8"],
    ["a) Pip Installs Python", "b) Pip Installs Packages", "c) Preferred Installer Program", "d) All of the mentioned"],
    ["a) underscore and ampersand are the only two special characters allowed", "b) unlimited length", "c) all private members must have leading and trailing underscores", "d) none of the mentioned"],
    ["a) 512, 64, 512", "b) 512, 512, 512", "c) 64, 512, 64", "d) 64, 64, 64"],
]

score = 0  #Initial score set to 0 and made to increment if answer goes correct and no increment if answer goes incorrect.
level = 1  # Initial level set to 1

def check_ans(user_ans, correct_ans):  #function to check the answer
    if user_ans == correct_ans:
        return True
    else:
        return False

print(f"********** Level {level} **********")
for ques_num in range(5):  # Loop through each question in level 1
    print("")
    print(ques_bank[ques_num]["text"])
    for i in options[ques_num]:
        print(i)

    user_ans = input("Enter your choice (a/b/c/d): ").lower()  # Lower used just in case user enters Uppercase alphabet
    is_correct = check_ans(user_ans, ques_bank[ques_num]["answer"])
    if is_correct:
        print("Hurray!!! Your selected choice is correct answer.")
        score += 1
    else:
        print("Oops!!! Better luck next time.")

if score == 5:
    print("Congratulations! You have qualified for Level 2.")
    print("********** Level 2 **********")
    for ques_num in range(5, 10):  # Loop through each question in level 2
        print("")
        print(ques_bank[ques_num]["text"])
        for i in options[ques_num]:
            print(i)

        user_ans = input("Enter your choice (a/b/c/d): ").lower()  # Lower used just in case user enters Uppercase alphabet
        is_correct = check_ans(user_ans, ques_bank[ques_num]["answer"])
        if is_correct:
            print("Hurray!!! Your selected choice is correct answer.")
            score += 1
        else:
            print("Oops!!! Better luck next time.")

    if score >= 10:
        print("Congratulations! You have qualified for Level 3.")
        print("********** Level 3 **********")
        for ques_num in range(10, 15):  # Loop through each question in level 3
            print("")
            print(ques_bank[ques_num]["text"])
            for i in options[ques_num]:
                print(i)

            user_ans = input("Enter your choice (a/b/c/d): ").lower()  # Lower used just in case user enters Uppercase alphabet
            is_correct = check_ans(user_ans, ques_bank[ques_num]["answer"])
            if is_correct:
                print("Hurray!!! Your selected choice is correct answer.")
                score += 1
            else:
                print
