questions = [
    ["Which of these is a primary color?", "Green", "Purple", "Orange", "Red", 4],
    ["The capital of France is:", "Berlin", "Rome", "Paris", "Madrid", 3],
    ["What is the chemical symbol for gold?", "Go", "Au", "Ag", "Fe", 2],
    ["Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo", 2],
    ["What is the largest planet in our solar system?", "Earth", "Mars", "Jupiter", "Saturn", 3],
    ["Which sea borders India to the south?", "Baltic Sea", "Red Sea", "Arabian Sea", "Black Sea", 3],
    ["Who is known as the 'Father of the Nation' in India?", "Jawaharlal Nehru", "Sardar Vallabhbhai Patel", "Mahatma Gandhi", "Subhas Chandra Bose",3],
    ["What is the name of the longest river in the world?", "Amazon River", "Nile River", "Yangtze River", "Mississippi River", 2],
    ["What is the name of the first Indian woman to win an Olympic medal?", "P.T. Usha", "Karnam Malleswari", "Saina Nehwal", "Sania Mirza", 2],
    ["Which country gifted the Statue of Liberty to the United States?", "Canada", "Germany", "France", "United Kingdom", 3],
    ["Which sea borders India to the south?", "Baltic Sea", "Red Sea", "Arabian Sea", "Black Sea", 3],
    ["Who is known as the 'Father of the Nation' in India?", "Jawaharlal Nehru", "Sardar Vallabhbhai Patel", "Mahatma Gandhi", "Subhas Chandra Bose",3],
    ["What is the name of the longest river in the world?", "Amazon River", "Nile River", "Yangtze River", "Mississippi River", 2],
    ["What is the name of the first Indian woman to win an Olympic medal?", "P.T. Usha", "Karnam Malleswari", "Saina Nehwal", "Sania Mirza", 2],
    ["Which country gifted the Statue of Liberty to the United States?", "Canada", "Germany", "France", "United Kingdom", 3]
]
levels = [
    "₹1,000",
    "₹2,000", 
    "₹3,000",
    "₹5,000",
    "₹10,000",
    "₹20,000",
    "₹40,000",
    "₹80,000",
    "₹1,60,000",
    "₹3,20,000",
    "₹6,40,000",
    "₹12,50,000",
    "₹25,00,000",
    "₹50,00,000",
    "₹1,00,00,000" 
]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"Question for Rs:{levels[i]}")
    print(f"Safe levels--->{levels[4]}--> {levels[9]}--> {levels[14]}\n")
    print(f"{question[0]}")
    print(f"1.{question[1]}   2.{question[2]}")
    print(f"3.{question[3]}   4.{question[4]}")
    reply=int(input("Enter your answer(1-4) and 0 to quit:"))
    if(reply==0):
        print(f"congratulations you won Rs:{levels[i-1]}")
        break
    if(reply==question[-1]):
        print(f"Option {question[-1]} is correct answer\nyou won Rs{levels[i]}!\n")
        if(i==4):
            money=10,000
        elif(i==9):
            money=32,0000
        elif(i==14):
            money=1,00,00,000        
    else:
        print("wrong answer!")      
        break  
print("------->✨✨<-------") 
print("Total winnings💵🎊\n")    
if(i==4 or i==9 or i==14):
    print(f"Your total won money is Rs:₹{money}\n") 
elif(reply==0):    
    print(f"Your total won money is Rs:{levels[i-1]}\n")   
else:
     print(f"Your total won money is Rs:₹0\n")   
     