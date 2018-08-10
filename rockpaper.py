# rock paper scissor game
usr_a = input("Enter your choice A:")
usr_b = input ("Enter your choice B:")
print("A choose " + usr_a)
print("B choose " + usr_b)
while usr_a == "rock":
        if usr_b == "scissor":
            print("A beats B")
        elif usr_b == "paper":
            print("B beats A")
        elif usr_b == "rock":
            print("Match is draw")
        break
while usr_b == "rock":
        if usr_a == "scissor":
            print("B beats A")
        elif usr_a == "paper":
            print("A beats B")
        elif usr_a == "rock":
            print("Match is draw")
        break
