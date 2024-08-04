line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("where do you want to hide your tresure?") 
coloumn_name = ["A","B","C"]

row = int(position[1])-1
coloumn = coloumn_name.index(position[0].upper())

# if position[0] == 'A':
#   coloumn = 0;
# elif position[0] == 'B':
#   coloumn = 1
# else:
#   coloumn = 2

map[row][coloumn] = "X"
print(f"{line1}\n{line2}\n{line3}")