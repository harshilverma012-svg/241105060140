print("Voting Analytics")
candidates = int(input("Enter candidate count: "))
if candidates <= 0:
    print("Invalid candidate number")
else:
    i = 0
    highest = 0
    winner = -1   # -1 means no winner yet
    while i < candidates:
        votes = int(input("Enter votes: "))
        if votes > highest:
            highest = votes
            winner = i
        i = i + 1
    print("Winner index:", winner)
    print("Highest votes:", highest)
    if highest == 0:
        print("No votes cast")
