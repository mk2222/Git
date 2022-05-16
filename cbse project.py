import pandas as pd
import numpy as np
import mysql.connector as sql
import time as t
import random as rd
import matplotlib.pyplot as py
mydb=sql.connect(host='localhost',user='root',password='mkmkmk@1234')
cursor=mydb.cursor()
admin_input=0
def database():
    cursor.execute('create database if not exists game11;')
    cursor.execute('use game11')
    cursor.execute('create table if not exists admin(password varchar(20));')
    cursor.execute('create table if not exists user_name(Username varchar(100) primary key,Password varchar(100))')
    cursor.execute('create table if not exists team(Team_Code varchar(5) primary key,\
                       Team_Name varchar(30))')
    cursor.execute('create table if not exists players(Team_Id varchar(5),Player_ID varchar(8) primary key,Player_Name varchar(30),\
                       Nationality varchar(20),Role varchar(20),Points float,foreign key(team_id) references team(team_code))')
    cursor.execute('create table if not exists matches(Match_id char(4) primary key,fixture varchar(100),\
                       status varchar(9),Start_Time Datetime)')
    cursor.execute('create table if not exists playing11(MatchId char(4)\
                                   ,PlayerId varchar(8),\
                                   runs int,wickets int,foreign key\
                                   (matchid) references matches(match_id),\
                                   foreign key (playerid) references players(player_id))')
    cursor.execute('create table if not exists \
                       pointstbl(Sno int auto_increment not null primary key,m_id char(4),u_id varchar(100),teamid varchar(5)\
                                 ,playerid varchar(8),runs int,wickets int,points int\
                                     ,foreign key(m_id) references matches(match_id),foreign key(u_id) references user_name(username)\
                                         ,foreign key(teamid) references team(team_code),\
                                             foreign key(playerid) references players(player_id))')
    cursor.execute('select count(*) from admin;')
    s=cursor.fetchone()[0]      
    if s==0:
        cursor.execute('insert into admin values("Bestie1234");')
        mydb.commit()
database()   
if mydb.is_connected():
    print('---------------------------------')
    print('Welcome to Game 11')
    print('---------------------------------')
else:
    print('Connection Not Established.')       
def welcome():
    print('Login As:')
    print('1.Admin')
    print('2.User')
    print('3.Exit')
    welcome_input=int(input('Enter Your Choice:'))
    if welcome_input==1:
        print('Welcome Admin')
        pass_admin=input('Enter Password:')
        cursor.execute('select password from admin')
        fetch=cursor.fetchone()[0]
        print('Please Wait. Verifying Password.\n')
        t.sleep(3)
        if fetch==pass_admin:
            print('Password matched successfully.\n')
            cursor.execute("select now()")
            d=cursor.fetchone()[0]
            print('Logged in at:',d,'\n')
            admin()
        else:
            print('Wrong Password!\n Try Again.')
            welcome()
    elif welcome_input==2:
        user_input=input('What Do You Want To Do?\n\
        1.LogIn\n\
        2.Signup\n\
        Enter Response:')
        
        if user_input=='1':
            global user_name
            user_name=input('Enter UserName: ')
            cursor.execute('select count(*) from user_name where username="{}"'.format(user_name))
            user_select=cursor.fetchone()[0]
            if user_select==1:
                user_pass=input('Enter Password: ')
                global password
                cursor.execute('select password from user_name where username="{}"'.format(user_name))
                password=cursor.fetchone()[0]
                print('Checking Password',end=' ')
                n=5
                while n>0:
                    print('.',end=' ',sep=' ')
                    t.sleep(1)
                    n-=1
                t.sleep(2)
                if password==user_pass:
                     print('Password matched successfully.\n')
                     cursor.execute("select now()")
                     d=cursor.fetchone()[0]
                     print('Logged in at:',d,'\n')
                     user()
                else:
                    print('Wrong Password!\n Try Again.')
                    welcome()
            else:
                print('No such user found! Please signup.')
                welcome()
        elif user_input=='2':
            user_name=input('Enter UserName: ')
            password=input('Enter Password: ')
            repass=input('ReEnter Password: ')
            cursor.execute('insert into user_name values("{}","{}")'.format(user_name,password))
            mydb.commit()
            if password==repass:
                a=rd.randrange(1,100)
                b=rd.randrange(1,100)
                user_verify=int(input('Human Verification:\n\
                '+str(a)+'+'+str(b)+'=?'+'\n\
                Enter Response:'))
                if user_verify==a+b:
                    print('Verifying......')
                    t.sleep(1)
                    print('Signup Verified.')
                    print('Please Login Now')
                    welcome()
                else:
                    print('Bot Detected!\n\
                    Terminating')
            else:
                print('Password do not match!\n\
                Please Try Again!')
                welcome()
        else:
            print('Invalid Input!\nTry Again.')
            welcome()
    elif welcome_input==3:
        print('Thank You For Using Game11.')
    else:
        print('Invalid Input!\nTry Again.')
        welcome()
        

        
def admin():    
    print('1.Create Match')
    print('2.Show Teams')
    print('3.Add Team')
    print('4.Update Team')
    print('5.ScoreBoard')
    print('6.Reset Password')
    print('7.View Graph Stats')
    print('8.Log Out.')
    admin_input=int(input('What you want to do?'))
    if admin_input==6:
        password_admin=input('Enter New Password:')
        cursor.execute('update admin set password="{}"'.format(password_admin))
        mydb.commit()
        print('Resetting Password.............')
        t.sleep(2)
        print('Password reset successful')
        print('Please Re-Login:\n')
        welcome()
    elif admin_input==3:
        
        t_code=input('Enter Team Code: ')
        t_name=input('Enter Team Name: ')
        cursor.execute('insert into team values("{}","{}")'.format(t_code,t_name))
        mydb.commit()
        
        for n in range(15):
            t_id=input('Enter Team Id: ')
            p_id=input('Enter Player Id: ')
            p_name=input('Enter Player Name: ')
            p_nation=input("Enter PLayer\'s Nationality: ")
            p_role=input('Enter Player Role: ')
            p_point=float(input('Enter player points: '))
            cursor.execute('insert into players values("{}","{}","{}","{}","{}","{}")'.format(t_id,p_id,p_name,p_nation,p_role,p_point))
            mydb.commit()
            
        print('Adding Team.',end=' ')
        n=5
        while n>5:
            print('.',end=' ',sep=' ')
            t.sleep(1)
            n-=1
        t.sleep(3)
        print('Team Added Successfully.')
        print('Taking you back to the main menu. Please Wait.....\n')
        t.sleep(2)
        admin()

    elif admin_input==8:
        print('Logging out.....\n')
        t.sleep(3)
        welcome()
    elif admin_input==2:
        cursor.execute('Select count(Team_name) from team')
        t1=cursor.fetchone()[0]
        if t1==0:
            print('No Teams Exists.')
            admin()
        elif t1>0:
            print('Fetching Data.........\n')
            t.sleep(3)
            print('We have the following teams:')
            cursor.execute('select distinct Team_name from team')
            team_show=cursor.fetchall()
            cursor.execute('Select count(*) from team')
            n=cursor.fetchone()[0]
            team_data=pd.DataFrame(team_show,index=[np.arange(1,n+1)],columns=['Teams'])
            print(team_data)
            team_input=(input('Enter Team Name to see Players: '))
           # team_select=team_data.at[team_input,'Teams'][0]
            print(team_input)
            cursor.execute('select player_name,role,points from players where nationality="{}"'.format(team_input))
            player_show=cursor.fetchall()
            cursor.execute('select count(*) from players where nationality="{}"'.format(team_input))
            p=cursor.fetchone()[0]
            player_data=pd.DataFrame(player_show,columns=['Player Name','Role','Points'],index=[np.arange(1,p+1)])
            print(player_data)
            t.sleep(3)
            out=int(input('Do you want to go back or logout?\n\
                      1.Go Back.\n\
                      2.Logout\n\
                          Reply: '))
            if out==1:
                admin()
            elif out==2:
                welcome()
    elif admin_input==4:
        per=True
        while per:
            print('Fetching Data.........\n')
            t.sleep(3)
            print('We have the following teams:')
            cursor.execute('select distinct Team_name from team')
            team_show=cursor.fetchall()
            cursor.execute('Select count(*) from team')
            n=cursor.fetchone()[0]
            team_data=pd.DataFrame(team_show,index=[np.arange(1,n+1)],columns=['Teams'])
            print(team_data)
            team_input=(input('Select Team to see Players: '))
            #team_select=team_data.at[team_input,'Teams'][0]
            cursor.execute('select player_id,player_name,role,points from players where nationality="{}"'.format(team_input))
            player_show=cursor.fetchall()
            cursor.execute('select count(*) from players where nationality="{}"'.format(team_input))
            p=cursor.fetchone()[0]
            player_data=pd.DataFrame(player_show,columns=['Player Id','Player Name','Role','Points'],index=[np.arange(1,p+1)])
            print(player_data)
            t.sleep(3)
            Update_player=int(input('What to update?\n\
            1.Player Name\n\
            2.Player Role\n\
            3.Player Points\n\
            4.Replace Player\n\
            5.Go Back\n\
            Enter Your Choice: '))
            if Update_player==1:
                playerid=input('Enter Player Id: ')
                update_name=input('Enter New Name: ')
                cursor.execute('update players set player_name="{}" where player_id="{}"'.format(update_name,playerid))
                mydb.commit()
                print('Updating Data.......')
                t.sleep(3)
                print('Data Updated Successfully.')
                ask=int(input('Do You Want To Continue?\n\
                1.Yes\n\
                2.No\n\
                Enter Response:'))
                if ask==1:
                    continue
                elif ask==2:
                    admin()
            elif Update_player==2:
                playerid=input('Enter Player Id: ')
                update_role=input('Enter New Role: ')
                cursor.execute('update players set Role="{}" where player_id="{}"'.format(update_role,playerid))
                mydb.commit()
                print('Updating Data.......')
                t.sleep(3)
                print('Data Updated Successfully.')
                ask=int(input('Do You Want To Continue?\n\
                1.Yes\n\
                2.No\n\
                Enter Response:'))
                if ask==1:
                    continue
                elif ask==2:
                    admin()
            elif Update_player==3:
                playerid=input('Enter Player Id: ')
                update_point=input('Enter New Points: ')
                cursor.execute('update players set points="{}" where player_id="{}"'.format(update_point,playerid))
                mydb.commit()
                print('Updating Data.......')
                t.sleep(3)
                print('Data Updated Successfully.')
                ask=int(input('Do You Want To Continue?\n\
                1.Yes\n\
                2.No\n\
                Enter Response:'))
                if ask==1:
                    continue
                elif ask==2:
                    admin()
            elif Update_player==4:
                playerid=input('Enter Player Id: ')
                update_name=input('Enter New Name: ')
                update_role=input('Enter New Role: ')
                update_point=input('Enter New Points: ')
                cursor.execute('update players set player_name="{}" where player_id="{}"'.format(update_name,playerid))
                cursor.execute('update players set Role="{}" where player_id="{}"'.format(update_role,playerid))
                cursor.execute('update players set points="{}" where player_id="{}"'.format(update_point,playerid))
                mydb.commit()
                print('Updating Data.......')
                t.sleep(3)
                print('Data Updated Successfully.')
                ask=int(input('Do You Want To Continue?\n\
                1.Yes\n\
                2.No\n\
                Enter Response:'))
                if ask==1:
                    continue
                elif ask==2:
                    admin()
            elif Update_player==5:
                admin()
            else:
                print('Invalid Input!')
                print('Terminating!')
                admin()
    elif admin_input==1:
        cursor.execute('select count(*) from team')
        mt1=cursor.fetchone()[0]
        if mt1<2:
            print('Insufficient Teams to create match.')
            admin()
        elif mt1>=2:
            cursor.execute('select substr(max(match_id),2) from matches')
            data=cursor.fetchone()[0]
            mid=''
            cnt=0
            if data==None:
                cnt=1
                mid="M"+str(cnt)
               
            else:
               cnt=int(data)
               cnt+=1
               mid="M"+str(cnt)
            a=input('Enter Team1: ')
            b=input('Enter Team2: ')
            m_fix=a+' vs '+b
            m_stat=input('Enter Match Status: ')
            m_time=input('Enter Date of Match[format:YYYY-MM-DD HH:MM:SS]')
            cursor.execute('insert into matches values("{}","{}","{}","{}")'.format(mid,m_fix,m_stat,m_time))
            mydb.commit()
            lst_team=[a,b]
            a_team=[]
            
            for x in lst_team:
                cursor.execute('select player_id,player_name from players where nationality="{}"'.format(x))
                show=cursor.fetchall()
                team_data=pd.DataFrame(show,columns=['Player_Code','Player_Name'])
                print(team_data.to_string(index=False))
                i=1    
                while True:
                    
                    p_code=input('Enter Player code who are playing: ')
                    if p_code not in a_team:
                        a_team.append(p_code)
                        
                        cursor.execute('insert into playing11 (matchid,playerid)\
                                       values("{}","{}")'.format(mid,p_code))
                        mydb.commit()
                    i+=1
                    if i>11:
                        if x==b:
                            print('Match Created Successfully.')
                            admin()
                        break
                
                
            
    elif admin_input==5:
        cursor.execute('select match_id,fixture from matches')
        match=cursor.fetchall()
        match_df=pd.DataFrame(match,columns=['Match Id','Fixture'])
        print(match_df.to_string(index=False))
        match_input=input("Enter Match id for scoreboard to be updated: ")
        
        cursor.execute('select player_name from players,playing11 where players.player_id=playing11.playerid \
                       and playing11.matchid="{}"'.format(match_input))
        score=cursor.fetchall()
        score_df=pd.DataFrame(score,columns=['Player Name'])
        
        score_lst=[]
        for i in range(len(score_df)):
            score_lst.append(score_df.iat[i,0])
        
        for x in score_lst:
            print('Player Name:',x)
            x_run=int(input('Enter Runs Scored:'))
            x_wicket=int(input('Enter Wickets Taken:'))
            points=x_run*1+x_wicket*3
            cursor.execute('select player_id from players where player_name="{}"'.format(x))
            d=cursor.fetchone()[0]
            cursor.execute('update pointstbl set runs={} where m_id="{}" and playerid="{}"'.format(x_run,match_input,d))
            mydb.commit()
            cursor.execute('update playing11 set runs={} where matchid="{}" and playerid="{}"'.format(x_run,match_input,d))
            mydb.commit()
            cursor.execute('update pointstbl set wickets={} where m_id="{}" and playerid="{}"'.format(x_wicket,match_input,d))
            mydb.commit()
            cursor.execute('update playing11 set wickets={} where matchid="{}" and playerid="{}"'.format(x_wicket,match_input,d))
            mydb.commit()
            cursor.execute('update pointstbl set points={} where m_id="{}" and playerid="{}"'.format(points,match_input,d))
            mydb.commit()
        print('Adding Runs and Wickets.',end=' ')
        n=5
        while n>0:
            print('.',sep=' ',end=' ')
            t.sleep(1)
            n-=1
        t.sleep(1)
        print('Runs and Wickets added.')
        cursor.execute('update matches set status="Completed" where match_id="{}"'.format(match_input))
        mydb.commit()
        admin()
    elif admin_input==7:
        g_input=int(input('Welcome to Statistics Region.Select Any One Option From Below:\n\
                          1.Batsman Performance\n\
                          2.Bowler Performance\n\
                          Enter Response: '))

        if g_input==1:
            cursor.execute('select match_id,fixture from matches where status="completed"')
            match=cursor.fetchall()
            match_df=pd.DataFrame(match,columns=['Match Id','Fixture'])
            print(match_df.to_string(index=False))
            g_match=input('Enter Match Id For Which You Want To See The Graphs:')
            cursor.execute('select distinct(nationality) from players,playing11 where playing11.matchid="{}" \
                           and playing11.playerid=players.player_id'.format(g_match))
            team=cursor.fetchall()
            t_df=pd.DataFrame(team)
            t_lst=[]
            for x in range(len(t_df)):
                t_lst.append(t_df.iat[x,0])
            
            cursor.execute('select playing11.matchid,players.player_name,playing11.runs from playing11,players \
                           where playing11.matchid="{}" and playing11.playerid=players.player_id \
                               and players.nationality="{}";'.format(g_match,t_lst[0]))
            g_run=cursor.fetchall()
            g_df=pd.DataFrame(g_run,columns=['MatchId','Player Name','Runs'])
            print(g_df.to_string(index=False))
            x=np.arange(len(g_df['Player Name']))
            ser=pd.Series(x)
            py.plot(ser,g_df['Runs'],color='cyan',marker='o',markeredgecolor='b',markerfacecolor='b',label=t_lst[0])
            py.legend()
            py.ylim(0,(g_df['Runs'].max()+10))
            py.title('Runs Scored By Batsman Of A Team:',fontname='Algerian',fontsize=25)
            py.xticks(x,g_df['Player Name'],rotation=90,fontname='Monotype corsiva',fontsize=20)
            py.yticks(fontname='Monotype corsiva',fontsize=20)
            py.xlabel('Players:',fontname='Times New Roman',fontsize=20)
            py.ylabel('Runs Scored:',fontname='Times New Roman',fontsize=20)
            py.savefig('1.svg')
            py.show()

            cursor.execute('select playing11.matchid,players.player_name,playing11.runs\
                           from playing11,players where playing11.matchid="{}" and playing11.playerid=players.player_id\
                               and players.nationality="{}";'.format(g_match,t_lst[1]))
            g_run1=cursor.fetchall()
            g_df1=pd.DataFrame(g_run1,columns=['MatchId','Player Name','Runs',])
            print(g_df1.to_string(index=False))
            y=np.arange(len(g_df['Player Name']))
            ser1=pd.Series(y)
            py.plot(ser1,g_df1['Runs'],color='yellow',marker='o',markeredgecolor='orange',markerfacecolor='orange',label=t_lst[1])
            py.legend()  
            py.ylim(0,(g_df1['Runs'].max()+10))
            py.xticks(y,g_df1['Player Name'],rotation=90,fontname='Monotype corsiva',fontsize=20)
            py.title('Runs Scored By Batsman Of A Team:',fontname='Algerian',fontsize=25)
            py.ylabel('Runs Scored:',fontname='Times New Roman',fontsize=20)
            py.xlabel('Players:',fontname='Times New Roman',fontsize=20)
            py.yticks(fontname='Monotype corsiva',fontsize=20)
            py.savefig('2.svg')
            py.show()
            
            use=int(input('What Do You Want To Do?\n\
                      1.Back.\n\
                      2.LogOut\n\
                      Enter Response:'))
            if use==1:
                admin()
            elif use==2:
                welcome()
            else:
                print('Invalid Input.Terminating!')
                welcome()

        elif g_input==2:
            cursor.execute('select match_id,fixture from matches')
            match=cursor.fetchall()
            match_df=pd.DataFrame(match,columns=['Match Id','Fixture'])
            print(match_df.to_string(index=False))
            g_match=input('Enter Match Id For Which You Want To See The Graphs:')
            cursor.execute('select distinct(nationality) from players,playing11 where playing11.matchid="{}" \
                           and playing11.playerid=players.player_id'.format(g_match))
            team=cursor.fetchall()
            t_df=pd.DataFrame(team)
            t_lst=[]
            for x in range(len(t_df)):
                t_lst.append(t_df.iat[x,0])
            
            cursor.execute('select playing11.matchid,players.player_name,playing11.wickets from playing11,players\
                           where playing11.matchid="{}" and playing11.playerid=players.player_id\
                               and players.nationality="{}";'.format(g_match,t_lst[0]))
            g_run=cursor.fetchall()
            g_df=pd.DataFrame(g_run,columns=['MatchId','Player Name','Wickets'])
            print(g_df.to_string(index=False))
            x=np.arange(len(g_df['Player Name']))
            ser=pd.Series(x)
            py.plot(ser,g_df['Wickets'],color='cyan',marker='o',markeredgecolor='b',markerfacecolor='b',label=t_lst[0])
            py.legend()
            py.title('Wickets Taken By Bowler Of A Team:',fontname='Algerian',fontsize=25)
            py.xticks(x,g_df['Player Name'],rotation=90,fontname='Monotype corsiva',fontsize=20)
            py.ylim(0,(g_df['Wickets'].max()+1))
            py.xlabel('Players:',fontname='Times New Roman',fontsize=20)
            py.ylabel('Wickets Taken:',fontname='Times New Roman',fontsize=20)
            py.yticks(fontname='Monotype corsiva',fontsize=20)
            py.savefig('3.svg')
            py.show()

            cursor.execute('select playing11.matchid,players.player_name,playing11.wickets\
                           from playing11,players where playing11.matchid="{}" \
                               and playing11.playerid=players.player_id and players.nationality="{}";'.format(g_match,t_lst[1]))
            g_run1=cursor.fetchall()
            g_df1=pd.DataFrame(g_run1,columns=['MatchId','Player Name','Wickets'])
            print(g_df1.to_string(index=False))
            y=np.arange(len(g_df['Player Name']))
            ser1=pd.Series(y)
            py.plot(ser1,g_df1['Wickets'],color='yellow',marker='o',markeredgecolor='orange',markerfacecolor='orange',label=t_lst[1])
            py.legend()            
            py.xticks(y,g_df1['Player Name'],rotation=90,fontname='Monotype corsiva',fontsize=20)
            py.yticks(fontname='Monotype corsiva',fontsize=20)
            py.title('Wickets Taken By Bowler Of A Team:',fontname='Algerian',fontsize=25)
            py.xlabel('Players:',fontname='Times New Roman',fontsize=20)
            py.ylabel('Wickets Taken:',fontname='Times New Roman',fontsize=20)
            py.savefig('4.svg')
            
            py.ylim(0,(g_df1['Wickets'].max()+1))
            py.show()
            use=int(input('What Do You Want To Do?\n\
                      1.Back.\n\
                      2.LogOut\n\
                      Enter Response:'))
            if use==1:
                admin()
            elif use==2:
                welcome()
            else:
                print('Invalid Input.Terminating!')
                welcome()
    else:
        print()
        print('Invalid Input!')
        print()
        admin()
        


def user():
    print('Welcome',user_name)
    user_fx=int(input('What you want to do?\n\
    1.Create Team\n\
    2.See Results\n\
    3.See Matches\n\
    4.See Team\n\
    5.Change Password\n\
    6.Log Out\n\
    Enter Your Response: '))
    if user_fx==5:
         n=3
         while n>0:
            chnge_pass=input('Enter Current Password:')
            if chnge_pass==password:
                re_pass=input('Enter New Password: ')
                cursor.execute('update user_name set password="{}" where username="{}"'.format(re_pass,user_name))
                mydb.commit()
                print('Resetting Password.',end=' ')
                n=5
                while n>0:
                    print('.',end=' ',sep=' ')
                    t.sleep(1)
                    n-=1
                t.sleep(2)
                print('Password Reset Successful. Login Again!')
                welcome()
            else:
                print('Incorrect password.')
                print('Try Again!')
                n-=1
                if n==0:
                    print('Daily Limit Exceeded!Terminating!')
                    welcome()
    elif user_fx==3:
        cursor.execute('select count(*) from matches')
        s1=cursor.fetchone()[0]
        if s1==0:
            print('No Match Scheduled Yet!')
            t.sleep(2)
            user()
        else:    
            cursor.execute('select * from matches where start_time>(select now())')
            match_show=cursor.fetchall()
            match_df=pd.DataFrame(match_show,columns=['Match Id','Fixture','Status','Start Time'])
            if match_df.empty:
                print('No Match Scheduled Yet!')
                use=int(input('What Do You Want To Do?\n\
                              1.Back.\n\
                              2.LogOut\n\
                              Enter Response:'))
                if use==1:
                    user()
                elif use==2:
                    welcome()
                else:
                    print('Invalid Input.Terminating.')
                    welcome()
            elif len(match_df)>0:
                print(match_df.to_string(index=False))
                t.sleep(3)
                use=int(input('What Do You Want To Do?\n\
                              1.Back.\n\
                              2.LogOut\n\
                              Enter Response:'))
                if use==1:
                    user()
                elif use==2:
                    welcome()
                else:
                    print('Invalid Input.Terminating.')
                    welcome()
    elif user_fx==4:
        cursor.execute('select count(distinct(matches.match_id)) from matches,pointstbl where pointstbl.u_id="{}" and matches.match_id=pointstbl.m_id'.format(user_name))
        s2=cursor.fetchone()[0]
        if s2==0:
            print('No Team Exists.')
            t.sleep(2)
            user()
        else:
            cursor.execute('select distinct(matches.match_id),matches.fixture from matches,pointstbl\
                           where pointstbl.u_id="{}" and matches.match_id=pointstbl.m_id'.format(user_name))
            match=cursor.fetchall()
            match_df=pd.DataFrame(match,columns=['Match Id','Fixture'])
            print()
            print(match_df.to_string(index=False))
            print()
            team_input=input('Enter Match Id to View Team: ')
            cursor.execute('select pointstbl.playerid,players.player_name from pointstbl,players where m_id="{}"\
                           and u_id="{}"and pointstbl.playerid=players.player_id order by playerid'.format(team_input,user_name))
            team=cursor.fetchall()
            team_show=pd.DataFrame(team,columns=['Player Id','Player Name'])
            print('Fetching Data.',end=' ')
            n=5
            while n>0:
                print('.',end=' ',sep=' ')
                t.sleep(1)
                n-=1
            t.sleep(2)
            print()
            print(team_show.to_string(index=False))
            t.sleep(3)
            print()
            use=int(input('What Do You Want To Do?\n\
                          1.Back.\n\
                          2.LogOut\n\
                          Enter Response:'))
            if use==1:
                user()
            elif use==2:
                welcome()
            else:
                print('Invalid Input.Terminating.')
                welcome()
    elif user_fx==2:
        cursor.execute('select count(distinct(matches.match_id)) from matches,pointstbl\
                            where pointstbl.u_id="{}" and matches.match_id=pointstbl.m_id'.format(user_name))
        s3=cursor.fetchone()[0]
        if s3==0:
            print('No team created by user.')
            t.sleep(2)
            user()
        else:           
            cursor.execute('select distinct(matches.match_id),matches.fixture from matches,pointstbl\
                                where pointstbl.u_id="{}" and matches.match_id=pointstbl.m_id'.format(user_name))
            match=cursor.fetchall()
            match_df=pd.DataFrame(match,columns=['Match Id','Fixture'])
            print()
            print(match_df.to_string(index=False))
            result_input=input('Enter Match Id to View Results: ')
            
            cursor.execute(' select u_id,sum(points) from pointstbl where m_id="{}" and points is not null group by\
                           u_id order by sum(points) desc'.format(result_input))
            df=cursor.fetchall()
            dtf=pd.DataFrame(df,columns=['User Name','Points Scored'])
            print()
            print('Calculating Result.',end=' ')
            n=5
            while n>0:
                print('.',sep=' ',end=' ')
                t.sleep(1)
                n-=1
            t.sleep(2)
            print()
            print(dtf.to_string(index=False))
            t.sleep(3)
            print()
            use=int(input('What Do You Want To Do?\n\
                          1.Back.\n\
                          2.LogOut\n\
                          Enter Response:'))
            if use==1:
                user()
            elif use==2:
                welcome()
            else:
                print('Invalid Input.Terminating!')
                welcome()
    elif user_fx==1:
        
        cursor.execute('select count(*) from matches')
        s1=cursor.fetchone()[0]
        
        if s1==0:
            print('No Match Scheduled Yet!')
            t.sleep(2)
            user()
        else:    
            cursor.execute('select match_id,fixture,start_time from matches where start_time>(select now())')
            match_show=cursor.fetchall()
            match_df=pd.DataFrame(match_show,columns=['Match Id','Fixture','Start Time'])
            if match_df.empty:
                print('No Match Scheduled Yet!')
                use=int(input('What Do You Want To Do?\n\
                              1.Back.\n\
                              2.LogOut\n\
                              Enter Response:'))
                if use==1:
                    user()
                elif use==2:
                    welcome()
                else:
                    print('Invalid Input.Terminating.')
                    welcome()
            elif len(match_df)>0:
                print(match_df.to_string(index=False))
                t.sleep(3)
                
            m_select=input('Enter Match:')
            credit=100
            p_count=11
            p_select=[]
            w_count=0
            bat_count=0
            bowl_count=0
            all_count=0
            bat_list=[]
            all_list=[]
            wicket_list=[]
            bowl_list=[]
            cursor.execute('select player_id from players where role="batsman"')
            bat_fetch=cursor.fetchall()
            bat=pd.DataFrame(bat_fetch)
            for i in range(len(bat)):
                bat_list.append(bat.iat[i,0])
            bat_tuple=tuple(bat_list)
            cursor.execute('select player_id from players where role like "%all%"')
            all_fetch=cursor.fetchall()
            all_=pd.DataFrame(all_fetch)
            for i in range(len(all_)):
                all_list.append(all_.iat[i,0])
            all_tuple=tuple(all_list)
            cursor.execute('select player_id from players where role="bowler"')
            bowl_fetch=cursor.fetchall()
            bowl=pd.DataFrame(bowl_fetch)
            for i in range(len(bowl)):
                bowl_list.append(bowl.iat[i,0])
            bowl_tuple=tuple(bowl_list)
            cursor.execute('select player_id from players where role like "%wicket%"')
            wk_fetch=cursor.fetchall()
            wk=pd.DataFrame(wk_fetch)
            for i in range(len(wk)):
                wicket_list.append(wk.iat[i,0])
            wicket_tuple=tuple(wicket_list)
                
            while p_count>0:
                print('            Which player you want?')
                p_input=int(input('                1.Batsman\n\
                2.WicketKeeper\n\
                3.All-Rounder\n\
                4.Bowler\n\
                Enter Input:'))
                print()
                
                
                
                if p_input==1:
                    if bat_count>4:
                            print('Maximum Batsman Reached.Please select other players.')
                            continue
                    while bat_count<=4:
                      #  if credit>70:
                        print('Credits Left:',credit)
                        cursor.execute(' select distinct(playerid),player_name,points from \
                                       playing11,players where playing11.playerid=players.player_id \
                                           and players.role="batsman" and playing11.matchid="{}" and player_id in{}'.format(m_select,bat_tuple))
                        dtfp=cursor.fetchall()
                        player=pd.DataFrame(dtfp,columns=['PlayerId','Player Name','Points'])
                        print(player.to_string(index=False))
                        print()
                        p_select=input('Enter PlayerId to be selected:')
                        cursor.execute('select player_name from players where player_id="{}"'.format(p_select))
                        pname=cursor.fetchone()[0]
                        p_confirm=input('Are you sure to select'+ pname+'?(Once selected player cannot be changed!(Y/N)')
                        if p_confirm=='y' or p_confirm=='Y':
                            cursor.execute('select team_id from players where player_id="{}"'.format(p_select))
                            tname=cursor.fetchone()[0]
                            cursor.execute('insert into pointstbl(m_id,u_id,teamid,playerid)\
                                           values("{}","{}","{}","{}")'.format(m_select,user_name,tname,p_select))
                            mydb.commit()
                            bat_count+=1
                            p_count-=1
                            cursor.execute('select points from players where player_id="{}"'.format(p_select))
                            point_deduct=cursor.fetchone()[0]
                            credit-=point_deduct
                            bat_list.remove(p_select)
                            bat_tuple=tuple(bat_list)
                            if p_count==0:
                                print('Saving Team.',end=' ')
                                
                                n=5
                                while n>0:
                                     print('.',end=' ',sep=' ')
                                     t.sleep(1)
                                     n-=1
                                t.sleep(2)
                                print('Team Saved Successfully.')
                                print()
                                user()
                            break
                        else:
                            print('Batsman was not selected.')
                            break
                        
                elif p_input==2:
                    if w_count==1:
                            print('Maximum Wicket-Keeper Reached.Please select other players.')
                            continue 
                    while w_count<1:
                        print('Credits Left:',credit)
                        cursor.execute(' select distinct(playerid),player_name,points \
                                       from playing11,players where playing11.playerid=players.player_id \
                                           and players.role like "%wicket%" and playing11.matchid="{}"\
                                               and player_id in{}'.format(m_select,wicket_tuple))
                        dtfp=cursor.fetchall()
                        player=pd.DataFrame(dtfp,columns=['PlayerId','Player Name','Points'])
                        print(player.to_string(index=False))
                        print()
                        p_select=input('Enter PlayerId to be selected:')
                        cursor.execute('select player_name from players where player_id="{}"'.format(p_select))
                        pname=cursor.fetchone()[0]
                        p_confirm=input('Are you sure to select'+ pname+'?(Once selected player cannot be changed!(Y/N)')
                        if p_confirm=='y' or p_confirm=='Y':
                            cursor.execute('select team_id from players where player_id="{}"'.format(p_select))
                            tname=cursor.fetchone()[0]
                            cursor.execute('insert into pointstbl(m_id,u_id,teamid,playerid) \
                                           values("{}","{}","{}","{}")'.format(m_select,user_name,tname,p_select))
                            mydb.commit()
                            w_count+=1
                            p_count-=1
                            cursor.execute('select points from players where player_id="{}"'.format(p_select))
                            point_deduct=cursor.fetchone()[0]
                            credit-=point_deduct
                            wicket_list.remove(p_select)
                            wicket_tuple=tuple(wicket_list)
                            if p_count==0:
                                print('Saving Team.',end=' ')
                                n=5
                                while n>0:
                                     print('.',end=' ',sep=' ')
                                     t.sleep(1)
                                     n-=1
                                t.sleep(2)
                                print('Team Saved Successfully.')
                                print()
                                user()
                                
                            break
                        else:
                            print('Wicket-Keeper was not selected.')
                            break
                        
                elif p_input==3:
                    if all_count>2:
                            print('Maximum All-Rounders Reached.Please select other players.')
                            continue 
                    while all_count<=2:
                        print('Credits Left:',credit)
                        cursor.execute(' select distinct(playerid),player_name,points\
                                       from playing11,players where playing11.playerid=players.player_id \
                                           and players.role like "%all%" and playing11.matchid="{}" and player_id in{}'.format(m_select,all_tuple))
                        dtfp=cursor.fetchall()
                        player=pd.DataFrame(dtfp,columns=['PlayerId','Player Name','Points'])
                        print(player.to_string(index=False))
                        print()
                        p_select=input('Enter PlayerId to be selected:')
                        cursor.execute('select player_name from players where player_id="{}"'.format(p_select))
                        pname=cursor.fetchone()[0]
                        p_confirm=input('Are you sure to select'+ pname+'?(Once selected player cannot be changed!(Y/N)')
                        if p_confirm=='y' or p_confirm=='Y':
                            cursor.execute('select team_id from players where player_id="{}"'.format(p_select))
                            tname=cursor.fetchone()[0]
                            cursor.execute('insert into pointstbl(m_id,u_id,teamid,playerid) \
                                           values("{}","{}","{}","{}")'.format(m_select,user_name,tname,p_select))
                            mydb.commit()
                            all_count+=1
                            p_count-=1
                            cursor.execute('select points from players where player_id="{}"'.format(p_select))
                            point_deduct=cursor.fetchone()[0]
                            credit-=point_deduct
                            all_list.remove(p_select)
                            all_tuple=tuple(all_list)
                            if p_count==0:
                                print('Saving Team.',end=' ')
                                n=5
                                while n>0:
                                     print('.',end=' ',sep=' ')
                                     t.sleep(1)
                                     n-=1
                                t.sleep(2)
                                print('Team Saved Successfully.')
                                print()
                                user()
                        
                            break
                        
                        else:
                            print('All-Rounder was not selected.')
                            break
                        
                elif p_input==4:
                    if bowl_count>4:
                            print('Maximum bowlers Reached.Please select other players.')
                            continue 
                    while bowl_count<=4:
                        print('Credits Left:',credit)
                        cursor.execute(' select distinct(playerid),player_name,points from playing11,players where playing11.playerid\
                                       =players.player_id and players.role="bowler" \
                                           and playing11.matchid="{}" and player_id in{}'.format(m_select,bowl_tuple))
                        dtfp=cursor.fetchall()
                        player=pd.DataFrame(dtfp,columns=['PlayerId','Player Name','Points'])
                        print(player.to_string(index=False))
                        print()
                        p_select=input('Enter PlayerId to be selected:')
                        cursor.execute('select player_name from players where player_id="{}"'.format(p_select))
                        pname=cursor.fetchone()[0]
                        p_confirm=input('Are you sure to select'+ pname+'?(Once selected player cannot be changed!(Y/N)')
                        if p_confirm=='y' or p_confirm=='Y':
                            cursor.execute('select team_id from players where player_id="{}"'.format(p_select))
                            tname=cursor.fetchone()[0]
                            cursor.execute('insert into pointstbl(m_id,u_id,teamid,playerid) \
                                           values("{}","{}","{}","{}")'.format(m_select,user_name,tname,p_select))
                            mydb.commit()
                            bowl_count+=1
                            p_count-=1
                            cursor.execute('select points from players where player_id="{}"'.format(p_select))
                            point_deduct=cursor.fetchone()[0]
                            credit-=point_deduct
                            bowl_list.remove(p_select)
                            bowl_tuple=tuple(bowl_list)
                            if p_count==0:
                                print('Saving Team.',end=' ')
                                n=5
                                while n>0:
                                     print('.',end=' ',sep=' ')
                                     t.sleep(1)
                                     n-=1
                                t.sleep(2)                        
                                print('Team Saved Successfully.')
                                print()
                                user()
                            break
                        else:
                            print('Bowler was not selected.')
                            break
               
                else:
                    print()
                    print('Team was not saved.')
                    cursor.execute('delete from pointstbl where u_id="{}"'.format(user_name))
                    mydb.commit()
                    print('Invalid Input!Terminating!')
                    user()
            
        
        
                    
               
                
            
    elif user_fx==6:
        print()
        print('Logging Out.................')
        t.sleep(2)
        print()
        welcome()
    else:
        print()
        print('Invalid Input!')
        print()
        user()      
        

        
    
        
    
welcome()   