"""Plain English
Define main function
establish an open list to store the first set of names that corresponds to the president
open the text file that contains the presidents' names
read from the file and strip everything but the characters needed and assign each presidents 
name to a place on the list
establish an open list to store the names of all vice presidents
open the second text file that contains all vice presidents' names 
read into the file and strip it of all content except the characters we need
assign each string of names to a value inside the list 'vp'

take input from the user and prompt them with the question of naming a current or former president
iterate through a for loop for the length of the list with presidents' names
if the value in the list is equivalent to what the user input, print out the corresponding
name of the vice president that lies in the same position for its separate text file

run the main() function
"""

"""Pseudo Code
define main
pres = []
open presiden.txt file to read
pres = line.strip() for each line in the file
vp = []
open vps.txt file to read
vp = line.strip() for each line in the text file

president = input from user
prompt user with 'Name a current or former president (first and last name with capitalization):'
for i in range(len(pres)):
    if(president == pres[i]):
        print(vp[i])

main()
"""

def main():
    pres = []
    with open("/Users/CCott_000/Desktop/Spring2021/Project/presidents.txt", "r") as f:
        pres = [line.strip() for line in f]
    """for i in a_file:
        pres.append(str(i))
    """
    vp = []
    with open("/Users/CCott_000/Desktop/Spring2021/Project/vps.txt", "r") as f:
        vp = [line.strip() for line in f]
    #for i in pres:  
    #    print(i)
    """for i in b_file:
        vp.append(str(i))
    """
    #for i in vp:
    #    print(i)
    president = input("Name a current or former president (first and last name with capitalization): ")
    for i in range(len(pres)):
        if(president == pres[i]):
            print (vp[i]) 
    #print(vp[30])
if __name__ == "__main__":
    main()