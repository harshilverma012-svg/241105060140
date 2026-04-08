print("Voting Analytics")
candidates = int(input("Enter candidate count: "))
i = 0
highest = 0
winner = 0
while i < candidates:
votes = int(input("Enter votes: ")) i
f votes > highest:
highest = votes
winner = i
i = i + 1 print("Winner index:", winner)
print("Highest votes:", highest
if highest = 0:
print("No votes cast")
if candidates <= 0:
print("Invalid candidate number")
