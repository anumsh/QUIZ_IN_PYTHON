#fill_in_the_blanks QUIZ
# here I have made  4 functions and 3 prompt
# 1st prompt to select difficulty level and 2nd is number of guesses user want to have  and 3rd is for filling the correct answer
# 1st function is : difficulty_level(), 2nd function is show_answer(), 3rd is show_question() and 4th is fill_in_the_blank()
print " Let Play ....fill_in_the_blanks quiz"'\n'

#there is three level of questions (below is question string of three level (easy,medium and hard) along with answers list and blank list too
easy_question = """ Python is a  high-level, __1__ , interactive and object-oriented scripting language.Python is designed to be highly  __2__ .
Python is processed at  __3__  by the interpreter.Python provides  __4__  to all major commercial databases. \n"""
easy_answers = ["interpreted","readable","runtime","interfaces"]

medium_question = """ __1__  are nothing but  __2__  memory locations to store values. Python variables do not need  __3__  declaration to memory space.
The declaration happens  __4__ when you assign a value to a variable. \n"""
medium_answers = ["variables","reserved","explicit","automatically"]

hard_question = """Python does not support a __1__ type; these are treated as __2__ of length one, thus also considered a __3__ .We can create them simply by enclosing characters in quotes.
Python treats single quotes the __4__ as double quotes. \n"""
hard_answers = ["character","strings","substring","same"]

blanks = ["_1_","_2_","_3_","_4_"]

# we are asking user to select the difficulty level for quiz. user have to type the difficulty level,if user will type some thing else other than easy,medium and hard
# he will unable to play the quiz.
# we are also asking for number of guesses user want to have before the game is over.
# for example : if the user_tries for 3 times , if he choose easy level for quiz, and he fills wrong answers for _1_ blank , then still he can play for 2 more times
# to guess the _1_ blank. but if he is unable to fill correct answer, game will over for him and he wil restart the game.
user_input = raw_input("Please select a game difficulty by typing it in. Options are : Easy , Medium or Hard  \n")
user_input=user_input.lower()

# procedure for checking difficulty level which is selected by user.
# here input will be user_difficulty_selected and output will be level(easy or medium or hard) ans user_tries
# if user will type Easy with "E" caps, Medium with "M" caps, hard with "H" caps , lower() function will convert caps into lower letters
# easy becomes easy, Medium becomes medium, Hard becomes hard
# the output is stored in variable level,user_tries
def difficulty_level(user_input):
    level_list=["easy","medium","hard"]
    while user_input not in level_list:
        user_input = raw_input("Please select a game difficulty by typing it in. Options are : Easy , Medium or Hard  \n " )
        user_input=user_input.lower()
    if user_input in level_list:
        user_tries=raw_input("Please select how many 'GUESSES' you want to have before the game is over  \n")
        user_tries=int(user_tries)
        return user_input,user_tries



#procedure for retrieving answers for level which is choosen by user.
# here input is  difficulty level and output is answers and questions of corresponding level
# output is stored in variable answerlist,question
def question_answer(levelinput):
    if levelinput == "easy":
        return easy_answers, easy_question
    elif levelinput == "medium":
        return medium_answers,medium_question
    elif  levelinput == "hard":
        return hard_answers,hard_question


level,user_tries = difficulty_level(user_input)
answerlist,question=question_answer(level)


# procedure in which user will play quiz by filling the answers according to level he choosen
# inputs are string, answerslist and blanklist
# output will be , if user will fill correct answer, he will win the quiz .
# there is options for trying the answers, if user will not guess the answer with number of tries he choose , game is over, he have to start the quiz again
def fill_in_the_blank(question, answerlist, blank):
    print "\nthe current paragraph reads as such:   "+ question
    i,guess = 0,0
    while (i < len(answerlist)) and (guess < user_tries) :
         answer = raw_input("What should be substituted for" + blank[i]+ "? \n")
         if answer == answerlist[i]:
             print "Correct! \n"
             question = question.replace("_"+blank[i]+"_",answerlist[i])
             print question
             i =i + 1
             if i == len(answerlist):
                print "YOU WIN!!!!! play  QUIZ for another level"
         else:
              print "Try Again \n"
              guess=guess + 1
              if guess == user_tries:
                print "Sorry , your  " + str(user_tries) + " tries are over and unfortunately game is over. Thanks for playing."

fill_in_the_blank(question,answerlist,blanks)
