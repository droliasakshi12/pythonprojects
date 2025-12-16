<h1>PYTHON 🐍</h1>

<h2>OVERVIEW 💡</h2>
<h4>
•	This repository includes projects for beginners who have keen interest in learning python programming language. 
•	There are 4 projects and each project has included the core of python.
</h4>

<h2>Concepts Covered 📌</h2> <br>
<h5>
•	 Conditional Statement (if -elif – else )
•	Loops (for loop , while loop , Break)
•	Object oriented programing  (class , functions , objects)
•	Python Standard Libraries.
•	Lists , dictionary 
</h5>
</br>

<h1>1.	7 UP and 7 DOWN 🎲🎲</h1>
<h4>
•	This is a game played on basis of prediction where the user have to guess whether the number will be more than 7 or less than 7.
•	In this game the user have to guess that the number will be more than 7 or less than or equal to 7. 
•	If the guess is same as users guess then they won the game , else they loose.
</h4>

<b>•	In this project we have created 2 different functions:</b>
Roll_dice() 🎲
Play_	7_up_7_down  7️⃣
•	In roll_dice() function, we have used the random module to generate the number between 1 to 6 and returned the total of two dice.

•	In play_7_up_7_down() function  
	User input is taken to  ask the user for their guess if there input is not equal to ‘up’ , ‘down’ , ‘exact’  , an error will occur.
	Made the use of conditional statement to print the output according to the users choice.

🚀Execution 
<code>
•	 play_7_up_7_down()
</code>

<h1>2.	Dice Rolling Simulator 🎲</h1>
<h4>
•	Used the random function to generate the values between 1 to 6 as in dice.
•	Included the use  of conditional statement to check for the conditions and print the output .
•	Taking the input from the user to roll the dice or not.
</h4>

<h1>3.	Password Strength Checker 🔑🔏</h1>
<h4>
•	This project is to check the strength of the password created by the user .
•	Created 2 functions:
<code>
-	checkPass()
-	Validatepass()
</code>
•	checkPass() :
-	used the Global keyword  (variables that can be used outside the functions)
-	Checking if everything is False. 
-	Used for loop to check the length  of the password , this is done to identify the strength of the password.

•	Validatepass():
-	Taking the password input from the user  
-	Checking if the password is ‘Strong’ , ‘Moderate’ , ‘weak’
</h4>

<h1>4.Snake and Ladders 🐍🪜</h1>
<h4>
•	In this game there can be multiple players they have to roll the dice and have to make the move according to the number in dice 
•	If the user ends at a number where there is a snake it will come backward or eaten by the snake .
•	If the  user ends at a number where there is a ladder it will move forward or climb the ladder.

•	Functions created:
<code>
dice()
Snl()
</code>

•	In dice() function :
-	So here a random number is  generated between 1 to 6 and each time the number is generated it is added.

•	In snl() function :
-	Created a snake and ladder  variable which is a dictionary where the key and value is given. 
-	According to the total value  of the dice the user will either climb the ladder or eaten by the snake.

•	Used while loop to roll the dice each time user want it the total is equal to 100 they won the game , else it will keep running until the user reaches to 100.
</h4>
