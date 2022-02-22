import pandas as pd
df = pd.read_csv('weball2020.txt', sep='|', header=None)
df2=df.loc[:,[0,1,2,4,5,7,18,19]]
df1 = df2.rename(columns={0:"ID"})
df1 = df1.rename(columns={1:"Name"})
df1 = df1.rename(columns = {2:"I/C"})
df1 = df1.rename(columns = {4:"Party"})
df1 = df1.rename(columns = {5:"$$"})
df1 = df1.rename(columns = {7:"Expenditures"})
df1 = df1.rename(columns = {18:"State"})
dfbase = df1.rename(columns = {19:"District"})
Status='First'
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
        pass
    elif body == 'P':
        pass
    elif body == 'C':
        pass
    elif body == 'A':
        pass
def Welcome(status):
    if status == 'First':
        print('Hello, welcome to the FEC2019-20 filings explorer.')
        x=str(input('Would you like to look at Presidential, Senate, House,Congress(Senate+House,or All) data. Please respond using P,S,H,C,A'))
        return x
    elif status == 'Returning':
        Status=str(input('Would you like to look at more data? Y/N?'))
        if Status == 'Y':
            x=str(input('Would you like to look at Presidential, Senate, House, or Congressional(Senate+House) data? Please respond using P,S,H,C'))
            return x
        elif Status == 'N':
            exit()
def Looking(name):
    x=Welcome(Status)
    if x == 'H':
        y=str(input('Would you like to look at a certain congressional district, a certain state, or the House as a whole? Please respond using District, State, House'))
        if y == 'District':
            Sta=str(input("Which State's congressional district race would you like to look at? Please respond using the appropriate two letter abbreviation."))
            Dis=int(input("Which District of that state would you like to look at? Please respond using the number."))
            Type=str(input('Would you like to see the top raisers in this district, or the top spenders? Please respond using Raised,Spent'))
            Party=str(input('Would you like to look at Republicans,Democrats,or all parties? Please respond using R,D,A'))
            Based=DataFrame(x,Sta,Party,Dis)
            Data(Based,Type)
        elif y == 'State':
            Dis='N/A'
            Sta=str(input("Which State's congressional district would you like to look at? Please respond using the appropriate two letter abbreviation."))
            Type=str(input('Would you like to see the top raisers in this state, or the top spenders? Please respond using Raised,Spent'))
            Party=str(input('Would you like to look at Republicans,Democrats,or all parties? Please respond using R,D,A'))
            Based=DataFrame(x,Sta,Party,Dis)
            Data(Based,Type)
        elif y == 'House':
            Sta='N/A'
            Dis='N/A'
            Type=str(input('Would you like to see the top raisers in the house, or the top spenders? Please respond using Raised,Spent'))
            Party=str(input('Would you like to look at Republicans,Democrats,or all parties? Please respond using R,D,A'))
            Based=DataFrame(x,Sta,Party,Dis)
            Data(Based,Type)
    elif x == 'S':
        y=str(input('Would you like to look at a certain state, or the Senate as a whole? Please respond using State,Senate'))
        if y == 'State':
            Sta=str(input("Which State's senatorial race would you like to look at? Please respond using the appropriate two letter abbreviation."))
    elif x == 'C':
        pass
    elif x == 'P':
        pass
    elif x == 'A':
        pass
def Data(dataframe,type):
    pass












Looking('Hi')
