# creating pandas Table
import pandas as pd 

Data = { 'Team':['CSK','RCB','SRH','MI','DC','GT','PKXI','LSG','RR','KKR'],'Matches Played':[0,0,0,0,0,0,0,0,0,0],'Won':[0,0,0,0,0,0,0,0,0,0],'Lost':[0,0,0,0,0,0,0,0,0,0],'Tie':[0,0,0,0,0,0,0,0,0,0],'Points':[0,0,0,0,0,0,0,0,0,0],'N.R.R':[0,0,0,0,0,0,0,0,0,0]}
Table = pd.DataFrame(Data)
Table.set_index("Team",inplace=True)
no =0 
while(no <= 90):
    no += 1
  #Getting Information from User
    print(f"Enter Today's Match stats. Match {no} of 90:")
    
    teams = input("Enter names of two teams(1stBatting-2ndBatting):")
    teamlist =teams.split("-")
    print("Enter scores of each team in format:(teamruns-teamwicketslost-teamballsplayed)")
    team1 = input(f"Enter {teamlist[0]} score: ")
    team2 = input(f"Enter {teamlist[1]} score: ")
    teamwon = input("Won By:")
    #Calculating all values
    team1score= team1.split("-")
    team2score= team2.split("-")

    team1runs = int(team1score[0])
    team1wick = int(team1score[1])
    team1balls = int(team1score[2])
    team2runs = int(team2score[0])
    team2wick = int(team2score[1])
    team2balls = int(team2score[2])

    if(teamwon == teamlist[0]):
        team1nrr = (team1runs-team2runs)*2
        team2nrr = (team1runs-team2runs)*(-2)
    
    
    elif(teamwon == teamlist[1]):
        team1nrr = ((120*(team2runs)/team2balls)-team1runs)*2
        team2nrr = ((120*(team2runs)/team2balls)-team1runs)*(-2)
    
    else:
        team1nrr =0 
        team2nrr =0 
        Table.loc[teamlist[0],"Tie"]+=1
        Table.loc[teamlist[1],"Tie"]+=1
     #updating the Table
    Table.loc[teamlist[0],"Matches Played"]+=1
    Table.loc[teamlist[1],"Matches Played"]+=1 
    if(teamwon == teamlist[0]):
        Table.loc[teamlist[0],"Won"]+=1 
        Table.loc[teamlist[0],"Points"]+=2 
        Table.loc[teamlist[0],"N.R.R"]+=team1nrr 
        Table.loc[teamlist[1],"Lost"]+=1
        Table.loc[teamlist[1],"Points"]+=2
        Table.loc[teamlist[1],"N.R.R"]+=team2nrr
    elif(teamwon == teamlist[1]):
        Table.loc[teamlist[1],"Won"]+=1 
        Table.loc[teamlist[1],"Points"]+=2 
        Table.loc[teamlist[1],"N.R.R"]+=team2nrr 
        Table.loc[teamlist[0],"Lost"]+=1
        Table.loc[teamlist[0],"Points"]+=2
        Table.loc[teamlist[0],"N.R.R"]+=team1nrr
        
       #displaying the Table 
    Table.sort_values('N.R.R')
    print(Table)
