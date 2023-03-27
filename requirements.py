import pandas as pd

def rowNum(house):
    hNum = 0
    if house == "Alpha_Chi_Rho":
        hNum = 0
    elif house == "Delta_Upsilon":
        hNum = 1
    elif house == "Delta_Zeta":
        hNum = 2
    elif house == "Kappa_Delta_Chi":
        hNum = 3
    elif house == "Phi_Kappa_Sigma":
        hNum = 4
    elif house == "Phi_Sigma_Sigma":
        hNum = 5
    elif house == "Sigma_Chi":
        hNum = 6
    elif house == "Sigma_Phi_Epsilon":
        hNum = 7
    elif house == "Tau_Epsilon_Phi":
        hNum = 8
    elif house == "Tau_Kappa_Epsilon":
        hNum = 9
    elif house == "Theta_Phi_Alpha":
        hNum = 10
    elif house == "Zeta_Nu'":
        hNum = 11


    return hNum

def gpaF(hNum,file):
    hGPAF = pd.read_excel(file,usecols="B", )
    result = hGPAF.iloc[hNum]['GPA > Male/Female Fall']
    return result

def gpaS(hNum,file):
    hGPAS = pd.read_excel(file,usecols="C", )
    result = hGPAS.iloc[hNum]['GPA > Male/Female Spring']
    return result

def goodStandingF(hNum, file):
    hGSF = pd.read_excel(file,usecols="D", )
    result = hGSF.iloc[hNum]['All Members in good standing Fall']
    return result

def goodStandingS(hNum, file):
    hGSS = pd.read_excel(file,usecols="E", )
    result = hGSS.iloc[hNum]['All Members in good standing Spring']
    return result

def studyHoursF(hNum, file):
    hSHF = pd.read_excel(file,usecols="F", )
    result = hSHF.iloc[hNum]['4 Study hours a week Fall']
    return result

def studyHoursS(hNum, file):
    hSHS = pd.read_excel(file,usecols="G", )
    result = hSHS.iloc[hNum]['4 Study hours a week Spring']
    return result

def sscEventsF(hNum, file):
    sscF = pd.read_excel(file, usecols="H" )
    result = sscF.iloc[hNum]['SSC Events Fall']
    return result

def sscEventsS(hNum, file):
    sscS = pd.read_excel(file, usecols="I", )
    result = sscS.iloc[hNum]['SSC Events Spring']
    return result

def campusEvent(hNum, file):
    cpEvent = pd.read_excel(file, usecols="J", )
    result = cpEvent.iloc[hNum]['80% participation in campus events']
    return result

def communityService(hNum, file):
    comService = pd.read_excel(file, usecols="K", )
    result = comService.iloc[hNum]['15 hours community service per member']
    return result

def charityMoneyRised(hNum, file):
    charity = pd.read_excel(file, usecols="L", )
    result = charity.iloc[hNum]['$25 raised per person per year']
    return result

def organationAwards(hNum, file):
    orgAward = pd.read_excel(file, usecols="M", )
    result = orgAward.iloc[hNum]['Understanding Organization/awards']
    return result

def adpotSocialJustice(hNum, file):
    socialJustice = pd.read_excel(file, usecols="N", )
    result = socialJustice.iloc[hNum]['Adopt a social justice org']
    return result

def hostSocialJusticeETF(hNum, file):
    hostF = pd.read_excel(file, usecols="O", )
    result = hostF.iloc[hNum]['Social Justice Event Fall']
    return result

def hostSocialJusticeETS(hNum, file):
    hostS = pd.read_excel(file, usecols="P", )
    result = hostS.iloc[hNum]['Social Justice Event Spring']
    return result

def sexualAwarenessF(hNum, file):
    saF = pd.read_excel(file, usecols="Q", )
    result = saF.iloc[hNum]['Sexuality/Gender Training Fall']
    return result

def sexualAwarenessS(hNum, file):
    saS = pd.read_excel(file, usecols="R", )
    result = saS.iloc[hNum]['Sexuality/Gender Training Spring']
    return result

def event1(hNum, file):
    eventT1 = pd.read_excel(file, usecols="S", )
    result = eventT1.iloc[hNum]['Event Training 1']
    return result

def event2(hNum, file):
    eventT2 = pd.read_excel(file, usecols="T", )
    result = eventT2.iloc[hNum]['Event Training 2']
    return result

def event3(hNum, file):
    eventT3 = pd.read_excel(file, usecols="U", )
    result = eventT3.iloc[hNum]['Event Training 3']
    return result

def socialEvent(hNum, file):
    eventT3 = pd.read_excel(file, usecols="V", )
    result = eventT3.iloc[hNum]['Events Listed on KL']
    return result

def noAlcoholEventF(hNum, file):
    noAlcF = pd.read_excel(file, usecols="W", )
    result = noAlcF.iloc[hNum]['Dry Social Event Fall']
    return result

def noAlcoholEventS(hNum, file):
    noAlcS = pd.read_excel(file, usecols="X", )
    result = noAlcS.iloc[hNum]['Dry Social Event Spring']
    return result

def communitySocialF(hNum, file):
    comSF = pd.read_excel(file, usecols="Y", )
    result = comSF.iloc[hNum]['Dry Community Events Fall']
    return result

def communitySocialS(hNum, file):
    comSS = pd.read_excel(file, usecols="Z", )
    result = comSS.iloc[hNum]['Dry Community Events Spring']
    return result

def fslCommunityF(hNum, file):
    fslComF = pd.read_excel(file, usecols="AA", )
    result = fslComF.iloc[hNum]['FSL community Fall 1']
    return result

def fslCommunityS(hNum, file):
    fslComS = pd.read_excel(file, usecols="AB", )
    result = fslComS.iloc[hNum]['FSL community Spring 2']
    return result

def townOrUnivInspect(hNum, file):
    insp =pd.read_excel(file, usecols="AC",)
    result = insp.iloc[hNum]['University/Town Inspections']
    return result

def insurance(hNum, file):
    insure =pd.read_excel(file, usecols="AD",)
    result = insure.iloc[hNum]['Insurance By Renewal']
    return result

def MHFSGreater(hNum, file):
    insure =pd.read_excel(file, usecols="AE",)
    result = insure.iloc[hNum]['MHFS <80']
    return result

def MHFSLess(hNum, file):
    insure =pd.read_excel(file, usecols="AF",)
    result = insure.iloc[hNum]['MHFS >80']
    return result

def riskManF(hNum, file):
    riskF =pd.read_excel(file, usecols="AG",)
    result = riskF.iloc[hNum]['Risk Management Fall']
    return result

def riskManS(hNum, file):
    riskS =pd.read_excel(file, usecols="AH",)
    result = riskS.iloc[hNum]['Risk Management Spring']
    return result

def drugAlcoholF(hNum, file):
    preventF =pd.read_excel(file, usecols="AI",)
    result = preventF.iloc[hNum]['Drug&Alcohol Fall']
    return result

def drugAlcoholS(hNum, file):
    preventS =pd.read_excel(file, usecols="AJ",)
    result = preventS.iloc[hNum]['Drug&Alcohol Spring']
    return result

def insureBefore(hNum, file):
    insureB =pd.read_excel(file, usecols="AK",)
    result = insureB.iloc[hNum]['Insurance Listed Before']
    return result

def insureLate(hNum, file):
    insureL =pd.read_excel(file, usecols="AL",)
    result = insureL.iloc[hNum]['Insurance Listed After']
    return result

def allDocTurnIn(hNum, file):
    allDoc =pd.read_excel(file, usecols="AM",)
    result = allDoc.iloc[hNum]['Organization Bylaws Turned In']
    return result

def turnInOnTime(hNum, file):
    turnIn =pd.read_excel(file, usecols="AN",)
    result = turnIn.iloc[hNum]['Bylaws Turned in on time']
    return result

def anualBudget(hNum,file):
    anual = pd.read_excel(file, usecols="AO",)
    result = anual.iloc[hNum]['Annual Budget ']
    return result

def submitForms(hNum,file):
    submit = pd.read_excel(file, usecols="AP",)
    result = submit.iloc[hNum]['Submitting Alcohol Forms > 5 days']
    return result

def riskManagementAlc(hNum, file):
    turnIn =pd.read_excel(file, usecols="AQ",)
    result = turnIn.iloc[hNum]['Risk Management With Alcohol']
    return result

def deadlinesFall(hNum, file):
    deadline =pd.read_excel(file, usecols="AR",)
    result = deadline.iloc[hNum]['Fall Deadlines']
    return result

def deadlinesSpring(hNum, file):
    deadline =pd.read_excel(file, usecols="AS",)
    result = deadline.iloc[hNum]['Spring Deadlines']
    return result

