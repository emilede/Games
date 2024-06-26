import random

teams = {"Antwerp": 1, "Benfica": 1, "Braga": 1, "Celtic": 1, "Crvena Zvezda": 1, "Feyenoord": 1, 
         "Galatasaray": 1, "Lens": 1, "Manchester United": 1, "Milan": 1, "Newcastle": 1, "Salzburg": 1, 
         "Sevilla": 1, "Shaktar": 1, "Union Berlin": 1, "Young Boys": 1, "Copenhagen": 2, "Porto": 2, 
         "Inter": 2, "Lazio": 2, "Leizig": 2, "Napoli": 2, "PSV": 2,
          "Real Sociadad": 3, "Arsenal": 4, "Atletico": 4, "Barcalona": 4,
         "Manchester City": 4, "Bayern Munich": 5, "PSG": 5, "Dortmund": 6, "Real Madrid": 6}


t1_score = 0
t2_score = 0

t1_shot = 0
t2_shot = 0

def toss(h_t):
    x = random.choice(['H', 'T'])
    if(h_t == x):
        print("You won, you shoot first.")
        return 1

    if(h_t != x):
        print("You lost, opponents shoot first.")
        return 0
    
def score(x):
    if(x == 1):
        print("He scores!!!")
    else:
        print("Straight to the keeper")
    return

def opp_shot(team):
    global t2_score
    global t2_shot
    print(team + " is shooting...")
    result = random.choice(["Top Left", "Bottom Left", "Panenka!", "Top Right", "Bottom Right", "SLIP!"])
    
    if(len(result) >= 7):
        print("They shoot..." + result)
        side = keeper_side()
        if(side in result):
            print("The keeper dives " + side + "! Saved!")
        
        else: 
            score(1)
            t2_score += 1

    else:
        print("Its a ..." + result)

        if(result == "Panenka"):
            if(score(random.randint(0, 1)) == True):
                t2_score += 1
        
        if(result == "SLIP!"):
            t2_shot += 1

    return


def keeper_side():
    x = random.randint(0, 1)

    if(x == 0):
        return "Left"

    if(x == 1):
        return "Right"
    
def your_shot(team):

    global t1_score
    global t1_shot

    spot = input("Pick your spot(Top Left, Bottom Left, Panenka, Top Right, Bottom Right): ")
    if('left' not in spot.lower() and 'right' not in spot.lower() and 'panenka' not in spot.lower()):
        print("He has no technique. Its a miss!")
        t1_shot += 1
        return 

    print(team + " is shooting...")
    result = spot

    if(random.randint(0,5) == 1):
        print("He's slipped!!")
        t1_shot += 1
        return
    
    if('left' in spot.lower() or 'right' in spot.lower()):
        print("They shoot..." + result)
        side = keeper_side()
        if(side in result):
            print("The keeper dives " + side + "! Saved!")
        
        else: 
            score(1)
            t1_score += 1

    
    else:
        print("Its a ... " + result)
        if(result.lower() == "panenka"):
            if(score(random.randint(0, 1)) == True):
                t1_score += 1

    return


def game_over(round, team1, team2):

    g_o = False

    if round == 3 and (t1_score + 2 < t2_score):
        print(team2 + " wins the Champions league!")
        print("With a score of: " + str(t1_score) + " to " + str(t2_score))
        g_o = True

    if round == 4 and (t1_score > t2_score + 2):
        print(team1 + " wins the Champions league!")
        print("With a score of: " + str(t1_score) + " to " + str(t2_score))
        g_o = True

    if round == 4 and (t1_score + 2 < t2_score):
        print(team2 + " wins the Champions league!")
        print("With a score of: " + str(t1_score) + " to " + str(t2_score))
        g_o = True

    if round == 5 and (t1_score < t2_score):
        print(team2 + " wins the Champions league!")
        print("With a score of: " + str(t1_score) + " to " + str(t2_score))
        g_o = True

    if round == 5 and (t1_score > t2_score + 1):
        print(team1 + " wins the Champions league!")
        print("With a score of: " + str(t1_score) + " to " + str(t2_score))
        g_o = True

    if round > 5 and (t1_score < t2_score):
        print(team2 + " wins the Champions league!")
        print("With a score of: " + str(t1_score) + " to " + str(t2_score))
        g_o = True

    if round > 5 and (t1_score > t2_score):
        print(team1 + " wins the Champions league!")
        print("With a score of: " + str(t1_score) + " to " + str(t2_score))
        g_o = True

    return g_o

def scores(t1, t2):
    
    print(t1 + ":" + str(t1_score))
    print(t2 + ":" + str(t2_score))

    return 
    
    


def main():

    team1 = random.choice(list(teams.keys()))
    del(teams[team1])
    team2 = random.choice(list(teams.keys()))

    print("--------------------------------------------------------")
    print("After an incredible season of Champions League Football,")

    print("We have reached the final.") 
    print("Between " + team1 + " and " + team2 + ".")
    
    print(team1 + ": 1 or "+ team2 + ": 2" )
    x = 0
    while(x != 1 or x != 2):
        x = input("Pick your team: ")
        if(int(x) == 1):
            print("You picked " + team1)
            break
        
        if(int(x) == 2):
            print("You picked " + team2)
            break
        
        print("Invalid team")
    
    print("After 90 long minutes, the game remains drawn. We go to extra time.")
    print("Another 30 minutes pass ... Pentalies will decide the game")
    
    '''
    res = ' '
    res = input("Coin toss for which team shoots first(H or T?): ")    
    toss(res)
    '''

    round = 1

    print(team1 + " shoots first!")

    while(True):
        print("Round: " + str(round))
        if game_over(round, team1, team2) == True:
            break
        your_shot(team1)
        if game_over(round, team1, team2) == True:
            break
        opp_shot(team2)
        if game_over(round, team1, team2) == True:
            break
        scores(team1, team2)
        round += 1




    




    print("--------------------------------------------------------")
    return

main()

    
    


