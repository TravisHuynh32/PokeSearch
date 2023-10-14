from pokebase import move
import webbrowser

# basic Pokemon Move Finder Program

def fetch_pokemon_id(name):
    poke = move(name) 
    print("ID:")
    print("-------------")
    print("The move " + name + " has an id of: " + str(poke.id))
    print("")

def fetch_pokemon_power(name):
    poke = move(name) 
    print("Power:")
    print("-------------")
    if poke.power < 100: 
        print(name + " has " + str(poke.power) + " power")
        print("The power on this move is less than 100, wow so shit haha!")
        compare_eq = (poke.power / 100) * 100
        print(name + " is " + str(compare_eq) + "% of Earthquake(ID: 84)")
        print("") 
    elif poke.power == 100: 
        print(name + " has " + str(poke.power) + " power")
        print("WOW! I have much respect for this move! It has power that has the same power as earthquake OMG!!!")
        compare_eq = (poke.power / 100) * 100
        print(name + " is " + str(compare_eq) + "% of Earthquake(ID: 84)")
        print("") 
    else: 
        print(name + " has " + str(poke.power) + " power")
        print("Bruh, ain't no way its better than stab eq, how does it have more power :( ")
        compare_eq = (poke.power / 100) * 100
        print(name + " is " + str(compare_eq) + "% of Earthquake(ID: 84)")
        print("")



def main(): 
    print("Hello! Welcome to my program that allows you to search information about a specific move in Pokemon!")
    print("What type of move do you want to learn about in Pokemon?")
    print("-------------------------------------------------------------------------------------------------------")

    name = input()

    if (name != move(name)):
        print("ERROR: The move that you inputted does not exist. Please check name again, or check your spelling or format")
        exit()

    print("Fetching " + name + "\n")
    
    fetch_pokemon_id(name)
    fetch_pokemon_power(name)

if __name__ == '__main__':
    main()