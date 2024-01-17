magicians = ['tom', 'patrick', 'adam']
for x in magicians: #for x in 
    print(f"{x.title()}, that was great session") 
#Tom, that was great session
#Patrick, that was great session
#Adam, that was great session
    
for value in range (1,5):
    print (value)
#1
#2
#3
#4

number = list(range(1,6))
print(number)
#[1, 2, 3, 4, 5]

numbers = list(range(1,21))
print(numbers)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

even_number = list(range(2,11,2)) #range(), can also create "spcaces" inside of the list for example you can create even or odd lists
print(even_number)
#[2, 4, 6, 8, 10]

squares = [] #create empty list
for value in range (1,11): #range() is defining to use numbers from 1 to 10
        square = value**2   #squares of previous created numbers from range()
        squares.append(square) #adding new values to the created list eariler 

print(squares)
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

min(squares)
#1
max(squares)
#100
sum(squares)
#385

players = ['tom', 'adam', 'dan', 'simon', 'oscar',' tobias']
print(players[0:3]) #it defines the range inside the list which values should be printed 
#['tom', 'adam', 'dan']

print (players[1:4]) #different values inside of []
#['adam', 'dan', 'simon']

print (players[:2]) #no value at the beggining then it will start from 0 position
#['tom', 'adam']

print(players[1:]) #starts from first position and will end at the end
#['adam', 'dan', 'simon', 'oscar', ' tobias']

print("That are our main three players:")
for player in players [:3]:
     print(player.title())
#That are our main three players:
#Tom
#Adam
#Dan 
     
my_foods = ['pizza', 'pasta', 'falafel', 'kebab', 'beef']
friends_food = my_foods [:] #command [:] is coping the list 
print (friends_food)
#['pizza', 'pasta', 'falafel', 'kebab', 'beef']

friends_food.append ('bananna') #various commands works with new copied list
print(friends_food)
#['pizza', 'pasta', 'falafel', 'kebab', 'beef', 'bananna']

dimensions = (200, 50) #tuple () is keeping the values and those values cannot be changed!
print(dimensions [0])
#200

menu = ('pizza', 'pasta', 'beef', 'ice creams')
print(menu[2])


menu = ('pizza', 'pasta', 'beef', 'ice creams')
print('Previous menu:')
for food in menu:
     print(food)

menu = ('pizza', 'pasta', 'sandwich', 'kebab')
print("Updated menu")
for food in menu:
     print(food)

#Previous menu:
#pizza
#pasta
#beef
#ice creams
#Updated menu
#pizza
#pasta
#sandwich
#kebab