'''
)MS Dhoni aged X years, is a Cancerian, born with very strong Mars in his birth chart. Notably, Mars is the ruling planet for sports. Write a program to get the age of Dhoni as an integer and display the same.
Input Format:
Input is an integer that corresponds to the age of Dhoni.
Output Format: 
Display the age.
Refer sample Input and Output for formatting specifications.
[All the text in bold corresponds to the Input]
Sample Input and Output:
Enter the age:
35
Age of Dhoni is 35

'''
a=int(input())
print("Age of Dhoni is",a)
...
)After Dhoni made it to the pinnacle of Success as Indian Captain, Mr. Banerjee was once invited by the Media to recall his association with Dhoni. Mr. Banerjee quoted one important moment that complemented the traits of Dhoni. It was when he approached Dhoni and asked him if he would play cricket for the school team saying "Will you be a wicketkeeper?" and was taken aback by Dhoni's confident reply "I will if I get a chance". Write a program to display the answers of Dhoni that impressed his master.
Input and Output Format:
Refer Sample input and output for formatting specifications.
All text in bold corresponds to input and the rest corresponds to output.
Sample Input and Output:
Banerjee's Question:
Will you be a wicketkeeper?
Dhoni's Reply:
I will if i get a chance.
For Banerjee's question "Will you be a wicketkeeper?" Dhoni's confident reply was "I will if I get a chance."
...
p=input("Banerjee's Question:\n")
r=input("Dhoni's Reply:\n")
print("For Banerjee's Question \"{}\" Dhoni's Confident reply was \"{}\"".format(p,r))
...
def get_team_details(team_number):
    print(f"Team {team_number}:")
    team_name = input("Team Name:\n").strip()
    score = input("Score:\n").strip()
    overs = input("Overs played:\n").strip()
    return team_name, score, overs

def display_match_details(team1, team2):
    print("Match Details:")
    print(f"Team 1:")
    print(f"Name: {team1[0]}")
    print(f"Score: {team1[1]}")
    print(f"Overs played: {team1[2]}")
    print(f"Team 2:")
    print(f"Name: {team2[0]}")
    print(f"Score: {team2[1]}")
    print(f"Overs played: {team2[2]}")

# Get details for both teams
team1_details = get_team_details(1)
team2_details = get_team_details(2)

# Display the match details
display_match_details(team1_details, team2_details)
...
...
