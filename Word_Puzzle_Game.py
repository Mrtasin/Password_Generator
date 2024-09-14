import random

def Result(word):
    input_word = input(f"Arrange the Word : {''.join(random.sample(word,len(word))).upper()} = ")
    if input_word.upper() == word.upper() :
        return True
    return False

def Word_Puzzle(Word_List):
    Word_List = random.sample(Word_List, len(Word_List))
    Score = 0
    for word in Word_List:
        if Result(word):
            print("Cracct")
            Score += 1
        else:
            print("Worng")
            Score -= 1
    else:
        print(f"Final score is : {Score}")

Word_Puzzle(['Tasin','Coder','lambda','break','while'])
