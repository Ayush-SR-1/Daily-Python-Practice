import random 

quiz_bank = [
    ['Which keyword is used to define a function in Python?', 'func', 'define', 'def', 'function', 3],
    ['What is the output of print(type([]))?', "<class 'tuple'>", "<class 'list'>", "<class 'dict'>", "<class 'set'>", 2],
    ['Which of the following data types is considered immutable in Python?', 'List', 'Set', 'Dictionary', 'Tuple', 4],
    ['What will be the output of print(2 ** 3 + 2)?', '12', '16', '10', '64', 3],
    ['Which of the following is the correct way to calculate the remainder of 5 ÷ 2?', '5 / 2', '5 % 2', '5 // 2', '5 ^ 2', 2],
    ['What is the purpose of the pass keyword in Python?', 'It terminates the loop entirely.', 'It skips the rest of the code in the current iteration.', 'It is a null placeholder used when a statement is required syntactically but you do not want any command to execute.', 'It raises an exception.', 3],
    ['What will be the output of the following code? \n x = "Python" \n print(x[1:4])', 'Pyt', 'yth', 'ytho', 'ytho', 2],
    ['How do you merge two dictionaries (e.g., d1 and d2) in Python 3.9+?', 'd1.update(d2)', 'd1 + d2', 'd1 | d2', 'merge(d1, d2)', 3],
    ['What happens when you try to access a key that does not exist in a standard Python dictionary?', 'It returns None.', 'It automatically adds the key with a None value.', 'It throws a KeyError.', 'It throws a ValueError.', 3],
    ['What does *args allow a function to accept?', 'A keyworded dictionary of variables.', 'A variable number of non-keyworded positional arguments.', 'Only lists as arguments.', 'Exactly one argument.', 2],
    ['What is the output of the following list comprehension? \n print([x for x in range(3) if x % 2 == 0])', '[1]', '[0, 2]', '[0, 1, 2]', '[2]', 2],
    ['Which statement accurately describes a Python Generator?', 'It returns all values at once in a list.', 'It stores the entire sequence in memory.', 'It uses the yield keyword to return one value at a time, evaluating lazily.', 'It is generally slower for massive datasets than a regular list.', 3],
    ['What will the following code output? \n def modify_list(lst=[]): \n lst.append(1)\n return lst \n print(modify_list()) \n print(modify_list())', '[1] followed by [1]', '[1] followed by [1, 1]', '[] followed by [1]', 'Error', 2],
    ['What will be the output of this equality check? print(1.2 + 2.1 == 3.3)', "True", "False", "None", "Error", 1],           
    ['What is the result of the following bitwise operation? \n x = 1 \n print(x << 2)', '2', '4', '8', '1', 2]
]

money= 0
prize_pool_money= [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]

for i in range(0, len(quiz_bank)):

    print(f" /n---  Question {i+1} is for money {prize_pool_money[i]}  ---n/")
    
    random_index = random.randrange(len(quiz_bank))
    current_question = quiz_bank.pop(random_index)
    
    print(current_question[0])
    print(f"1. {current_question[1]}")
    print(f"2. {current_question[2]}")
    print(f"3. {current_question[3]}")
    print(f"4. {current_question[4]}")
    
    user_input = int(input("Choice an option from 1 - 4: "))
    
    if user_input == current_question[5]:
    
        print("Correct Answer")
        money = prize_pool_money[i]
        
        if i == len(prize_pool_money) - 1:
            print("Congratulations! You answered the final question!")
            break
        
        print("Do you want to continue? If Yes then press 1 or else press 0: ", end= "")
        next= int(input())
        
        if next != 1:
            print("You chose to quit and walk away with your current winnings.")
            break
        
    else:
        print("Wrong Answer")
        print(f"The Correct Answer is {current_question[5]}")
        
        if money >= 320000:
            money = 320000
        elif money >= 10000:
            money = 10000
        else:
            money = 0
            
        break

print("=================================")
print("GAME OVER!! You have won: ₹", money)
print("=================================")











