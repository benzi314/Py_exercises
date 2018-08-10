# this is a rock paper scissor game
usr_a = input("Your name A:")
usr_b = input("Your name B:")
c1 = input(usr_a+ ", Select rock paper or scissor:")
c2 = input(usr_b+ ", Select rock paper or scissor:")
def game(c1,c2):
    if c1 == c2:
        return("Match is draw")
    elif c1 == "rock":
        if c2 == "scissor":
            return(usr_a + "wins" + usr_b)
        else:
            return (usr_b + "wins" + usr_a)
    elif c1 == "scissor":
        if c2 == paper:
            return(usr_a + "wins" + usr_b)
        else:
            return (usr_b + "wins" + usr_a)
    elif c1 == "paper":
        if c2 == "rock":
            return(usr_a + " wins " + usr_b)
        else:
            return (usr_b + " wins " + usr_a)
    else:
        return("You have given invalid inputs: TRY AGAIN")
    return
print(game(c1,c2))
