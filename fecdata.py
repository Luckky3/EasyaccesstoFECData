import pandas as pd
df = pd.read_csv('weball2020.txt', sep='|', header=None)
df2=df.loc[:,[0,1,2,4,5,7,18,19]]
df1 = df2.rename(columns={0:"ID"})
df1 = df1.rename(columns={1:"Name"})
df1 = df1.rename(columns = {2:"I/C"})
df1 = df1.rename(columns = {4:"Party"})
df1 = df1.rename(columns = {5:"$$"})
df1 = df1.rename(columns = {7:"Spend"})
df1 = df1.rename(columns = {18:"State"})
dfbase = df1.rename(columns = {19:"District"})
def DataFrame(body,state,party,district):
    if body == 'H':
        dfhouse = dfbase.loc[df1['ID']<'I']
        if state == 'N/A':
            if party == 'A':
                return dfhouse
            elif party == 'R':
                dfhouseR=dfhouse.loc[dfhouse['Party']=='REP']
                return dfhouseR
            elif party == 'D':
                dfhouseD=dfhouse.loc[dfhouse['Party']=='DEM']
                return dfhouseD
        else:
            if district == 'N/A':
                dfhouseState=dfhouse.loc[dfhouse['State']==state]
                if party == 'A':
                    return dfhouseState
                elif party == 'R':
                    dfhouseRState=dfhouseState.loc[dfhouse['Party']=='REP']
                    return dfhouseRState
                elif party == 'D':
                    dfhouseStateD=dfhouse.loc[dfhouse['Party']=='DEM']
                    return dfhouseStateD
            else:
                dfhouseDistrict=dfhouse.loc[(dfhouse['State'] == state) & (dfhouse['District'] == district)]
                if party == 'A':
                    return dfhouseDistrict
                elif party == 'R':
                    dfhouseRDistrict=dfhouseDistrict.loc[dfhouse['Party']=='REP']
                    return dfhouseRDistrict
                elif party == 'D':
                    dfhouseDistrictD=dfhouseDistrict.loc[dfhouse['Party']=='DEM']
                    print(dfhouseDistrictD)
                    return dfhouseDistrictD
    elif body == 'S':
        dfSenate = dfbase.loc[dfbase['ID']>'R']
        if state == 'N/A':
            if party == 'A':
                return dfSenate
            elif party == 'R':
                dfSenateR=dfSenate.loc[dfSenate['Party']=='REP']
                return dfSenateR
            elif party == 'D':
                dfSenateD=dfSenate.loc[dfSenate['Party']=='DEM']
                return dfSenateD
        else:
            dfSenateState=dfSenate.loc[dfSenate['State']==state]
            if party == 'A':
                return dfSenateState
            elif party == 'R':
                dfSenateStateR=dfSenateState.loc[dfSenateState['Party']=='REP']
                return dfSenateStateR
            elif party == 'D':
                dfSenateStateD=dfSenateState.loc[dfSenateState['Party']=='DEM']
                return dfSenateStateD
    elif body == 'P':
        dfP1 = dfbase.loc[dfbase['ID']<'R']
        dfPres = dfP1.loc[dfP1['ID']>'I']
        if party == 'A':
            return dfPres
        elif party == 'D':
            dfPresD = dfPres.loc[dfPres['Party']=='DEM']
            return dfPresD
        elif party == 'D':
            dfPresR = dfPres.loc[dfPres['Party']=='REP']
            return dfPresR
    elif body == 'C':
        dfC1 = dfbase.loc[dfbase['ID']>'R']
        dfC2 = dfbase.loc[dfbase['ID']<'I']
        dfCongress = pd.concat([dfC1,dfC2])
        if state == 'N/A':
            if party == 'A':
                return dfCongress
            elif party == 'R':
                dfCongressR=dfCongress.loc[dfCongress['Party']=='REP']
                return dfCongressR
            elif party == 'D':
                dfCongress=dfCongress.loc[dfCongress['Party']=='DEM']
                return dfCongress
        else:
            dfCongressState=dfCongress.loc[dfCongress['State']==state]
            if party == 'A':
                return dfCongressState
            elif party == 'R':
                dfCongressStateR=dfCongressState.loc[dfCongressState['Party']=='REP']
                return dfCongressStateR
            elif party == 'D':
                dfCongressStateD=dfCongressState.loc[dfCongressState['Party']=='DEM']
                return dfCongressStateD
    elif body == 'A':
        if party == 'A':
            return dfbase
        elif party == 'R':
            dfRepublicans = dfbase.loc[dfbase['Party']=='REP']
            return dfRepublicans
        elif party == 'D':
            dfDemocrats = dfbase.loc[dfbase['Party']=='DEM']
            return dfDemocrats

def Welcome(status):
    if status == 'First':
        print('Hello, welcome to the FEC2019-20 filings explorer.')
        c=0
        while c==0:
            x=str(input('Would you like to look at Presidential, Senate, House,Congress(Senate+House),or All data. Please respond using P,S,H,C,A'))
            if x == 'P' or x == 'S' or x == 'H' or x == 'C' or x == 'A':
                c=1
                return x
            else:
                print('Your response did not match any of the accepted responses. Please try again.')
                c=0
    elif status == 'Returning':
        c=0
        while c==0:
            Status=str(input('Would you like to look at more data? Y/N?'))
            if Status == 'Y':
                k=0
                while k==0:
                    x=str(input('Would you like to look at Presidential, Senate, House,Congress(Senate+House),or All data. Please respond using P,S,H,C,A'))
                    if x == 'P' or x == 'S' or x == 'H' or x == 'C' or x == 'A':
                        return x
                    else:
                        print('Your response did not match any of the accepted responses. Please try again.')
                        k=0
            elif Status == 'N':
                print("Hope you found what you were looking for! Please come again!")
                exit()
            else:
                print('Your response did not match any of the accepted responses. Please try again.')
                c=0
def Looking(status):
    x=Welcome(status)
    c=0
    if x == 'H':
        c=0
        while c == 0:
            y=str(input('Would you like to look at a certain congressional district, a certain state, or the House as a whole? Please respond using District, State, House'))
            if y == 'District':
                Sta=str(input("Which State's congressional district race would you like to look at? Please respond using the appropriate two letter abbreviation."))
                Check(Sta)
                Dis=int(input("Which District of that state would you like to look at? Please respond using the number."))
                Check(Dis)
                Type=str(input('Would you like to see the top raisers in this district, or the top spenders? Please respond using Raised,Spent'))
                Check(Type)
                Party=str(input('Would you like to look at Republicans,Democrats,or all parties? Please respond using R,D,A'))
                Check(Type)
                Based=DataFrame(x,Sta,Party,Dis)
                Data(Based,Type)
                status='Returning'
                Looking(status)
            elif y == 'State':
                Dis='N/A'
                Sta=str(input("Which State's congressional district would you like to look at? Please respond using the appropriate two letter abbreviation."))
                Check(Sta)
                Type=str(input('Would you like to see the top raisers in this state, or the top spenders? Please respond using Raised,Spent'))
                Check(Type)
                Party=str(input('Would you like to look at Republicans,Democrats,or all parties? Please respond using R,D,A'))
                Check(Party)
                Based=DataFrame(x,Sta,Party,Dis)
                Data(Based,Type)
                status='Returning'
                Looking(status)
            elif y == 'House':
                Sta='N/A'
                Dis='N/A'
                Type=str(input('Would you like to see the top raisers in the house, or the top spenders? Please respond using Raised,Spent'))
                Check(Type)
                Party=str(input('Would you like to look at Republicans,Democrats,or all parties? Please respond using R,D,A'))
                Check(Party)
                Based=DataFrame(x,Sta,Party,Dis)
                Data(Based,Type)
                status='Returning'
                Looking(status)
            else:
                print('Your response did not match any of the accepted responses. Please try again.')
    elif x == 'S':
        c=0
        while c == 0:
            y=str(input('Would you like to look at a certain state, or the Senate as a whole? Please respond using State,Senate'))
            if y == 'State':
                Dis='N/A'
                Sta=str(input("Which State's senatorial race would you like to look at? Please respond using the appropriate two letter abbreviation."))
                Check(Sta)
                Type=str(input('Would you like to see the top raisers in this state, or the top spenders? Please respond using Raised,Spent'))
                Check(Type)
                Party=str(input('Would you like to look at Republicans,Democrats,or all parties? Please respond using R,D,A'))
                Check(Party)
                Based=DataFrame(x,Sta,Party,Dis)
                Data(Based,Type)
                status='Returning'
                Looking(status)
            elif y == 'Senate':
                Dis='N/A'
                Sta='N/A'
                Type=str(input('Would you like to see the top raisers in the senate, or the top spenders? Please respond using Raised,Spent'))
                Check(Type)
                Party=str(input('Would you like to look at Republicans,Democrats,or all parties? Please respond using R,D,A'))
                Check(Party)
                Based=DataFrame(x,Sta,Party,Dis)
                Data(Based,Type)
                status='Returning'
                Looking(status)
            else:
                print('Your response did not match any of the accepted responses. Please try again.')
    elif x == 'P':
        Sta='N/A'
        Dis='N/A'
        Type=str(input('Would you like to see the top presidential candidate raisers or the top spenders? Please respond using Raised,Spent'))
        Check(Type)
        Party=str(input('Would you like to look at Republicans,Democrats,or all parties? Please respond using R,D,A'))
        Check(Party)
        Based=DataFrame(x,Sta,Party,Dis)
        Data(Based,Type)
        status='Returning'
        Looking(status)
    elif x == 'C':
        c=0
        while c == 0:
            y=str(input('Would you like to look at a certain state, or the Congress as a whole? Please respond using State,Congress'))
            if y == 'State':
                Dis='N/A'
                Sta=str(input("Which State's Congressional races would you like to look at? Please respond using the appropriate two letter abbreviation."))
                Check(Sta)
                Type=str(input('Would you like to see the top raisers in this state, or the top spenders? Please respond using Raised,Spent'))
                Check(Type)
                Party=str(input('Would you like to look at Republicans,Democrats,or all parties? Please respond using R,D,A'))
                Check(Party
                Based=DataFrame(x,Sta,Party,Dis)
                Data(Based,Type)
                status='Returning'
                Looking(status)
            elif y == 'Congress':
                Dis='N/A'
                Sta='N/A'
                Type=str(input('Would you like to see the top raisers in Congress, or the top spenders? Please respond using Raised,Spent'))
                Check(Type)
                Party=str(input('Would you like to look at Republicans,Democrats,or all parties? Please respond using R,D,A'))
                Check(Party)
                Based=DataFrame(x,Sta,Party,Dis)
                Data(Based,Type)
                status='Returning'
                Looking(status)
            else:
                print('Your response did not match any of the accepted responses. Please try again.')
    elif x == 'A':
        Dis='N/A'
        Sta='N/A'
        Type=str(input('Would you like to see the top raisers, or the top spenders? Please respond using Raised,Spent'))
        Check(Type)
        Party=str(input('Would you like to look at Republicans,Democrats,or all parties? Please respond using R,D,A'))
        Check(Party)
        Based=DataFrame(x,Sta,Party,Dis)
        Data(Based,Type)
        status='Returning'
        Looking(status)
def Data(dataframe,type):
    DF=dataframe
    if type == 'Raised':
        DF=DF.loc[:,['Name','I/C','Party','$$','State','District']]
        dfsort = DF.sort_values('$$', ascending=False)
        def format(x):
            return "${:.2f}M".format(x/1000000)
        dfsort['$$'] = dfsort['$$'].apply(format)
        candidates=dfsort.shape[0]
        print(dfsort.head(candidates))
        dfmost=dfsort.head(1)
        amount1=str(dfmost.iat[0,3])
        party1=str(dfmost.iat[0,2])
        candidate1=str(dfmost.iat[0,0])
        status1=str(dfmost.iat[0,1])
        if status1 == 'C':
            s='a challenger'
        elif status1 == 'I':
            s='the incumbent'
        answer=('The candidate who raised the most was ' + candidate1 + ' who raised ' + amount1 +'.'+' They are a registered '+ party1 + ' and ran as ' + s + '.')
        print(answer)
        return
    elif type == 'Spent':
        DF=DF.loc[:,['Name','I/C','Party','Spend','State','District']]
        dfsort = DF.sort_values('Spend', ascending=False)
        def format(x):
            return "${:.2f}M".format(x/1000000)
        dfsort['Spend'] = dfsort['Spend'].apply(format)
        candidates=dfsort.shape[0]
        print(dfsort.head(candidates))
        dfmost=dfsort.head(1)
        amount1=str(dfmost.iat[0,3])
        party1=str(dfmost.iat[0,2])
        candidate1=str(dfmost.iat[0,0])
        status1=str(dfmost.iat[0,1])
        if status1 == 'C':
            s='a challenger'
        elif status1 == 'I':
            s='the incumbent'
        answer=('The candidate who spent the most was ' + candidate1 + ' who spent ' + amount1 +'.'+' They are a registered '+ party1 + ' and ran as ' + s + '.')
        print(answer)
        return


Looking('First')

def Check(mode):
    pass








