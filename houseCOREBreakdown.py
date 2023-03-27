from tkinter import *
import requirements as req
import houseCrest as crest

def points(root, house, file):
    houseNum = req.rowNum(house)
    crest.crest(root, houseNum)

    #Understand the importance of scholarship and practice academic responsibility.
    scholar = Label(root, text="Understand the importance of scholarship:", font=('Arial', 12))
    scholar.place(x=20, y=360)

    section1Total = 14
    section1Pt = 0

    #GPAs higher than the all male or all female community average, 4 points - 2 per semester
    gpaF = req.gpaF(houseNum, file)
    if gpaF == 1:
        gpaFall = Label(root, text = "GPA > Male/Female Fall", background='green')
        gpaFall.place(x=20, y=400)
        section1Pt = section1Pt + 2
    elif gpaF == 0:
        gpaFall = Label(root, text = "GPA > Male/Female Fall", background='red')
        gpaFall.place(x=20, y=400)
    else:
        gpaFall = Label(root, text="GPA > Male/Female Fall")
        gpaFall.place(x=20, y=400)

    gpaS = req.gpaS(houseNum, file)
    if gpaS == 1:
        gpaSpring = Label(root, text="GPA > Male/Female Spring", background='green')
        gpaSpring.place(x=20, y=420)
        section1Pt = section1Pt + 2
    elif gpaS == 0:
        gpaSpring = Label(root, text="GPA > Male/Female Spring", background='red')
        gpaSpring.place(x=20, y=420)
    else:
        gpaSpring = Label(root, text="GPA > Male/Female Spring")
        gpaSpring.place(x=20, y=420)

    #Having all new members remain in good academic standing, 4 points - 2 per semester
    goodSDF = req.goodStandingF(houseNum,file)
    if goodSDF == 1:
        goodSDFall = Label(root, text="All Members In Good Standing Fall", background='green')
        goodSDFall.place(x=20, y=440)
        section1Pt = section1Pt + 2
    elif goodSDF == 0:
        goodSDFall = Label(root, text="All Members In Good Standing Fall", background='red')
        goodSDFall.place(x=20, y=440)
    else:
        goodSDFall = Label(root, text="All Members In Good Standing Fall")
        goodSDFall.place(x=20, y=440)

    goodSDS = req.goodStandingS(houseNum, file)
    if goodSDS == 1:
        goodSDSpring = Label(root, text="All Members In Good Standing Spring", background='green')
        goodSDSpring.place(x=20, y=460)
        section1Pt = section1Pt + 2
    elif goodSDS == 0:
        goodSDSpring = Label(root, text="All Members In Good Standing Spring", background='red')
        goodSDSpring.place(x=20, y=460)
    else:
        goodSDSpring = Label(root, text="All Members In Good Standing Spring")
        goodSDSpring.place(x=20, y=460)

    #Creating and executing an academic plan for each semester based on the needs of current and new member,
    #2 points (1 point per semester) for hosting a minimum of 4 study hours per week each semester - APPENDIX PAGE 1
    fourHRStudyF = req.studyHoursF(houseNum, file)
    if fourHRStudyF == 1:
        hrStudyFall = Label(root, text="Four Study Hours A Week Fall", background='green')
        hrStudyFall.place(x=20, y=480)
        section1Pt = section1Pt + 1
    elif fourHRStudyF == 0:
        hrStudyFall = Label(root, text="Four Study Hours A Week Fall", background='red')
        hrStudyFall.place(x=20, y=480)
    else:
        hrStudyFall = Label(root, text="Four Study Hours A Week Fall")
        hrStudyFall.place(x=20, y=480)

    fourHRStudyS = req.studyHoursF(houseNum, file)
    if fourHRStudyS == 1:
        hrStudySpring = Label(root, text="Four Study Hours A Week Spring", background='green')
        hrStudySpring.place(x=20, y=500)
        section1Pt = section1Pt + 1
    elif fourHRStudyS == 0:
        hrStudySpring = Label(root, text="Four Study Hours A Week Spring", background='red')
        hrStudySpring.place(x=20, y=500)
    else:
        hrStudySpring = Label(root, text="Four Study Hours A Week Spring")
        hrStudySpring.place(x=20, y=500)

    # Attend or host an event with Student Achievement Services related to academic integrity, study skills, time management, etc.
    #4 points (2 per semester) -APPENDIX PAGE X,  1 point for less than 100% of chapter in attendance,2 points for 100% of chapter in attendance
    sscEventF = req.sscEventsF(houseNum,file)
    if sscEventF == 2:
        sscEventFall = Label(root, text="Host or Attend SAS Event > 80 Percent Fall", background='green')
        sscEventFall.place(x=20, y=520)
        section1Pt = section1Pt + 2
    elif sscEventF == 1:
        sscEventFall = Label(root, text="Host or Attend SAS Event < 80 Fall", background='yellow')
        sscEventFall.place(x=20, y=520)
        section1Pt = section1Pt + 1
    elif sscEventF == 0:
        sscEventFall = Label(root, text="Host or Attend SAS Event < 80 Fall", background='red')
        sscEventFall.place(x=20, y=520)
    else:
        sscEventFall = Label(root, text="Host or Attend SAS Event Fall")
        sscEventFall.place(x=20, y=520)

    sscEventS = req.sscEventsS(houseNum, file)
    if sscEventS == 2:
        sscEventSpring = Label(root, text="Host or Attend SAS Event > 80 Percent Spring", background='green')
        sscEventSpring.place(x=20, y=540)
        section1Pt = section1Pt + 2
    elif sscEventS == 1:
        sscEventSpring = Label(root, text="Host or Attend SAS Event < 80 Spring", background='yellow')
        sscEventSpring.place(x=20, y=540)
        section1Pt = section1Pt + 1
    elif sscEventS == 0:
        sscEventSpring = Label(root, text="Host or Attend SAS Event < 80 Spring", background='red')
        sscEventSpring.place(x=20, y=540)
    else:
        sscEventSpring = Label(root, text="Host or Attend SAS Event Spring")
        sscEventSpring.place(x=20, y=540)

    section1Result = Label(root, text ="Total points achieved in section 1 is " + str(section1Pt) + " out of "+ str(section1Total))
    section1Result.place(x=20, y=580)

    # Engage in Clarkson University community events, Potsdam community service, other service and philanthropic events.
    community = Label(root, text="Engage In The Community:", font=('Arial', 12))
    community.place(x=400, y=60)

    section2Total = 16
    section2Pt = 0

    # 10 points - Have 80% of chapter members participate in at least one of the following by hosting an event, table,
    # or other agreed upon activity as a part of the larger event.
    campusEt = req.campusEvent(houseNum, file)
    if campusEt == 1:
        campEvent = Label(root, text="Campus Event 80% attendance", background='green')
        campEvent.place(x=400, y=100)
        section2Pt = section2Pt + 10
    elif campusEt == 0:
        campEvent = Label(root, text="Campus Event 80% attendance", background='red')
        campEvent.place(x=400, y=100)
    else:
        campEvent = Label(root, text="Campus Event 80% attendance")
        campEvent.place(x=400, y=100)

    #2 points - At least 15 hours of community service per year per member on average.
    communityEt = req.campusEvent(houseNum, file)
    if communityEt == 1:
        comET = Label(root, text="15 hrs of Community Service per Member", background='green')
        comET.place(x=400, y=120)
        section2Pt = section2Pt + 2
    elif communityEt == 0:
        comET = Label(root, text="15 hrs of Community Service per Member", background='red')
        comET.place(x=400, y=120)
    else:
        comET = Label(root, text="15 hrs of Community Service per Member")
        comET.place(x=400, y=120)

    #2 points - At least $25 of philanthropic donations raised per member per year on average.
    charityMoney = req.campusEvent(houseNum, file)
    if charityMoney == 1:
        charMoney = Label(root, text="$25 raised per Person per Year", background='green')
        charMoney.place(x=400, y=140)
        section2Pt = section2Pt + 2
    elif charityMoney == 0:
        charMoney = Label(root, text="$25 raised per Person per Year", background='red')
        charMoney.place(x=400, y=140)
    else:
        charMoney = Label(root, text="$25 raised per Person per Year")
        charMoney.place(x=400, y=140)

    #2 points - Provide detailed understanding of the organizations and entities served by the chapter and any
    # distinguished awards or numbers related to that service.
    orgAwardsUND = req.campusEvent(houseNum, file)
    if orgAwardsUND == 1:
        awardUND = Label(root, text="Understanding Organization/awards", background='green')
        awardUND.place(x=400, y=160)
        section2Pt = section2Pt + 2
    elif orgAwardsUND == 0:
        awardUND = Label(root, text="Understanding Organization/awards", background='red')
        awardUND.place(x=400, y=160)
    else:
        awardUND = Label(root, text="Understanding Organization/awards")
        awardUND.place(x=400, y=160)

    section2Result = Label(root, text="Total points achieved in section 2 is " + str(section2Pt) + " out of " + str(section2Total))
    section2Result.place(x=400, y=200)

    # Demonstrate an awareness of and appreciation for social justice issues.
    justice = Label(root, text="Awareness Of Social Justice:", font=('Arial', 12))
    justice.place(x=400, y=240)

    section3Total = 10
    section3Pt = 0

    #Engage with a social justice organization or campaign
    socialJustice = req.adpotSocialJustice(houseNum, file)
    if socialJustice == 1:
        awardUND = Label(root, text="Adopt a Social Justice", background='green')
        awardUND.place(x=400, y=280)
        section3Pt = section3Pt + 4
    elif socialJustice == 0:
        awardUND = Label(root, text="Adopt a Social Justice", background='red')
        awardUND.place(x=400, y=280)
    else:
        awardUND = Label(root, text="Adopt a Social Justice")
        awardUND.place(x=400, y=280)

    # Partner with Clarkson University to host and attend events related to social justice issues,
    # 4 points (2 points per semester)
    hostSJF = req.hostSocialJusticeETF(houseNum, file)
    if hostSJF == 1:
        hostF = Label(root, text="Host a Social Justice Event Fall", background='green')
        hostF.place(x=400, y=300)
        section3Pt = section3Pt + 2
    elif hostSJF == 0:
        hostF = Label(root, text="Host a Social Justice Event Fall", background='red')
        hostF.place(x=400, y=300)
    else:
        hostF = Label(root, text="Host a Social Justice Event Fall")
        hostF.place(x=400, y=300)

    hostSJS = req.hostSocialJusticeETS(houseNum, file)
    if hostSJS == 1:
        hostS = Label(root, text="Host a Social Justice Event Spring", background='green')
        hostS.place(x=400, y=320)
        section3Pt = section3Pt + 2
    elif hostSJS == 0:
        hostS = Label(root, text="Host a Social Justice Event Spring", background='red')
        hostS.place(x=400, y=320)
    else:
        hostS = Label(root, text="Host a Social Justice Event Spring")
        hostS.place(x=400, y=320)

    #Participate in a training or conference session dedicated to awareness of and education pertaining to topics
    # including sexual assault, racial issues, LGBTQ+ issues, etc.
    #2 points (1 per semester)
    sexualAwareF = req.sexualAwarenessF(houseNum, file)
    if sexualAwareF == 1:
        sexualAF = Label(root, text="Sexuality/Gender Training Fall", background='green')
        sexualAF.place(x=400, y=340)
        section3Pt = section3Pt + 1
    elif sexualAwareF == 0:
        sexualAF = Label(root, text="Sexuality/Gender Training Fall", background='red')
        sexualAF.place(x=400, y=340)
    else:
        sexualAF = Label(root, text="Sexuality/Gender Training Fall")
        sexualAF.place(x=400, y=340)

    sexualAwareS = req.sexualAwarenessS(houseNum, file)
    if sexualAwareS == 1:
        sexualAS = Label(root, text="Sexuality/Gender Training Spring", background='green')
        sexualAS.place(x=400, y=360)
        section3Pt = section3Pt + 1
    elif sexualAwareS == 0:
        sexualAS = Label(root, text="Sexuality/Gender Training Spring", background='red')
        sexualAS.place(x=400, y=360)
    else:
        sexualAS = Label(root, text="Sexuality/Gender Training Spring")
        sexualAS.place(x=400, y=360)

    section3Result = Label(root, text="Total points achieved in section 3 is " + str(section3Pt) + " out of " + str(section3Total))
    section3Result.place(x=400, y=400)

    # Engage in Clarkson University community events, Potsdam community service, other service and philanthropic events.
    responsible = Label(root, text="Demonstrate personal responsibility:", font=('Arial', 12))
    responsible.place(x=700, y=60)

    section4Total = 32
    section4Pt = 0

    eventTraining1 = req.event1(houseNum, file)
    if eventTraining1 == 1:
        et1 = Label(root, text="Event Training 1", background='green')
        et1.place(x=700, y=100)
        section4Pt = section4Pt + 1
    elif eventTraining1 == 0:
        et1 = Label(root, text="Event Training 1", background='red')
        et1.place(x=700, y=100)
    else:
        et1 = Label(root, text="Event Training 1")
        et1.place(x=700, y=100)

    eventTraining2 = req.event2(houseNum, file)
    if eventTraining2 == 1:
        et2 = Label(root, text="Event Training 2", background='green')
        et2.place(x=700, y=120)
        section4Pt = section4Pt + 1
    elif eventTraining2 == 0:
        et2 = Label(root, text="Event Training 2", background='red')
        et2.place(x=700, y=120)
    else:
        et2 = Label(root, text="Event Training 2")
        et2.place(x=700, y=120)

    eventTraining3 = req.event3(houseNum, file)
    if eventTraining3 == 1:
        et3 = Label(root, text="Event Training 3", background='green')
        et3.place(x=700, y=140)
        section4Pt = section4Pt + 1
    elif eventTraining3 == 0:
        et3 = Label(root, text="Event Training 3", background='red')
        et3.place(x=700, y=140)
    else:
        et3 = Label(root, text="Event Training 3")
        et3.place(x=700, y=140)

    socialEventKL = req.socialEvent(houseNum, file)
    if socialEventKL == 1:
        alcKL = Label(root, text="Events Listed on KL", background='green')
        alcKL.place(x=700, y=160)
        section4Pt = section4Pt + 1
    elif socialEventKL == 0:
        alcKL = Label(root, text="Events Listed on KL", background='red')
        alcKL.place(x=700, y=160)
    else:
        alcKL = Label(root, text="Events Listed on KL")
        alcKL.place(x=700, y=160)

    noAlcEventF = req.noAlcoholEventF(houseNum, file)
    if noAlcEventF == 1:
        noAclF = Label(root, text="Dry Social Event Fall", background='green')
        noAclF.place(x=700, y=180)
        section4Pt = section4Pt + 1
    elif noAlcEventF == 0:
        noAclF = Label(root, text="Dry Social Event Fall", background='red')
        noAclF.place(x=700, y=180)
    else:
        noAclF = Label(root, text="Dry Social Event Fall")
        noAclF.place(x=700, y=180)

    noAlcEventS = req.noAlcoholEventS(houseNum, file)
    if noAlcEventS == 1:
        noAclS = Label(root, text="Dry Social Event Spring", background='green')
        noAclS.place(x=700, y=200)
        section4Pt = section4Pt + 1
    elif noAlcEventS == 0:
        noAclS = Label(root, text="Dry Social Event Spring", background='red')
        noAclS.place(x=700, y=200)
    else:
        noAclS = Label(root, text="Dry Social Event Spring")
        noAclS.place(x=700, y=200)

    communitySocialF = req.noAlcoholEventF(houseNum, file)
    if communitySocialF == 1:
        csF = Label(root, text="Dry Community Events Fall", background='green')
        csF.place(x=700, y=220)
        section4Pt = section4Pt + 1
    elif communitySocialF == 0:
        csF = Label(root, text="Dry Community Events Fall", background='red')
        csF.place(x=700, y=220)
    else:
        csF = Label(root, text="Dry Community Events Fall")
        csF.place(x=700, y=220)

    communitySocialS = req.noAlcoholEventF(houseNum, file)
    if communitySocialS == 1:
        csS = Label(root, text="Dry Community Events Spring", background='green')
        csS.place(x=700, y=240)
        section4Pt = section4Pt + 1
    elif communitySocialF == 0:
        csS = Label(root, text="Dry Community Events Spring", background='red')
        csS.place(x=700, y=240)
    else:
        csS = Label(root, text="Dry Community Events Spring")
        csS.place(x=700, y=240)

    fslComF1 = req.noAlcoholEventF(houseNum, file)
    if fslComF1 == 2:
        comF1 = Label(root, text="FSL community Fall", background='green')
        comF1.place(x=700, y=260)
        section4Pt = section4Pt + 2
    elif fslComF1 == 1:
        comF1 = Label(root, text="FSL community Fall", background='yellow')
        comF1.place(x=700, y=260)
        section4Pt = section4Pt + 1
    elif fslComF1 == 0:
        comF1 = Label(root, text="FSL community Fall", background='red')
        comF1.place(x=700, y=260)
    else:
        comF1 = Label(root, text="FSL community Fall")
        comF1.place(x=700, y=260)

    fslComS2 = req.noAlcoholEventF(houseNum, file)
    if fslComS2 == 2:
        comS2 = Label(root, text="FSL community Spring", background='green')
        comS2.place(x=700, y=280)
        section4Pt = section4Pt + 2
    elif fslComS2 == 1:
        comS2 = Label(root, text="FSL community Spring", background='yellow')
        comS2.place(x=700, y=280)
        section4Pt = section4Pt + 1
    elif fslComS2 == 0:
        comS2 = Label(root, text="FSL community Spring", background='red')
        comS2.place(x=700, y=280)
    else:
        comS2 = Label(root, text="FSL community Spring")
        comS2.place(x=700, y=280)

    inspection = req.townOrUnivInspect(houseNum, file)
    if inspection == 1:
        inspect = Label(root, text="University/Town Inspections", background='green')
        inspect.place(x=700, y=300)
        section4Pt = section4Pt + 1
    elif inspection == 0:
        inspect = Label(root, text="University/Town Inspections", background='red')
        inspect.place(x=700, y=300)
    else:
        inspect = Label(root, text="University/Town Inspections")
        inspect.place(x=700, y=300)

    insurance = req.insurance(houseNum, file)
    if insurance == 1:
        insure = Label(root, text="Insurance By Renewal", background='green')
        insure.place(x=700, y=320)
        section4Pt = section4Pt + 1
    elif insurance == 0:
        insure = Label(root, text="Insurance By Renewal", background='red')
        insure.place(x=700, y=320)
    else:
        insure = Label(root, text="Insurance By Renewal")
        insure.place(x=700, y=320)

    MHFSGreater = req.MHFSGreater(houseNum, file)
    MHFSLess = req.MHFSLess(houseNum, file)
    if MHFSGreater == 2 and MHFSLess == 2:
        MHFG = Label(root, text="80% of chapter holding a MHFA certification", background='green')
        MHFG.place(x=700, y=340)
        section4Pt = section4Pt + 4
    elif MHFSGreater == 0 and MHFSLess == 2:
        MHFL = Label(root, text="Less than 80% of chapter holding a MHFA certification", background='yellow')
        MHFL.place(x=700, y=340)
        section4Pt = section4Pt + 2
    elif insurance == 0:
        insure = Label(root, text="No one holds MHFA certification", background='red')
        insure.place(x=700, y=340)
    else:
        insure = Label(root, text="MHFA certification")
        insure.place(x=700, y=340)

    riskManagementF = req.insurance(houseNum, file)
    if riskManagementF == 1:
        riskF = Label(root, text="Risk Management Fall", background='green')
        riskF.place(x=700, y=360)
        section4Pt = section4Pt + 2
    elif riskManagementF == 0:
        riskF = Label(root, text="Risk Management Fall", background='red')
        riskF.place(x=700, y=360)
    else:
        riskF = Label(root, text="Risk Management Fall")
        riskF.place(x=700, y=360)

    riskManagementS = req.insurance(houseNum, file)
    if riskManagementS == 1:
        riskS = Label(root, text="Risk Management Spring", background='green')
        riskS.place(x=700, y=380)
        section4Pt = section4Pt + 2
    elif riskManagementS == 0:
        riskS = Label(root, text="Risk Management Spring", background='red')
        riskS.place(x=700, y=380)
    else:
        riskS = Label(root, text="Risk Management Spring")
        riskS.place(x=700, y=380)

    drugAndAlcoholF = req.drugAlcoholF(houseNum, file)
    if drugAndAlcoholF == 1:
        preventF = Label(root, text="Drug&Alcohol Fall", background='green')
        preventF.place(x=700, y=400)
        section4Pt = section4Pt + 2
    elif drugAndAlcoholF == 0:
        preventF = Label(root, text="Drug&Alcohol Fall", background='red')
        preventF.place(x=700, y=400)
    else:
        preventF = Label(root, text="Drug&Alcohol Fall")
        preventF.place(x=700, y=400)

    drugAndAlcoholS = req.drugAlcoholS(houseNum, file)
    if drugAndAlcoholS == 1:
        riskS = Label(root, text="Drug&Alcohol Spring", background='green')
        riskS.place(x=700, y=420)
        section4Pt = section4Pt + 2
    elif drugAndAlcoholS == 0:
        riskS = Label(root, text="Drug&Alcohol Spring", background='red')
        riskS.place(x=700, y=420)
    else:
        riskS = Label(root, text="Drug&Alcohol Spring")
        riskS.place(x=700, y=420)

    insuranceBefore = req.insureBefore(houseNum, file)
    insuranceLate = req.insureLate(houseNum, file)
    if insuranceBefore == 2 and insuranceLate == 2:
        insure = Label(root, text="Insurance Listed Before", background='green')
        insure.place(x=700, y=440)
        section4Pt = section4Pt + 4
    elif insuranceBefore == 0 and insuranceLate == 2:
        insure = Label(root, text="Insurance Listed After", background='yellow')
        insure.place(x=700, y=440)
        section4Pt = section4Pt + 2
    elif insurance == 0:
        insure = Label(root, text="Did not turn in Insurance", background='red')
        insure.place(x=700, y=440)
    else:
        insure = Label(root, text="Turn in Insurance")
        insure.place(x=700, y=440)

    section4Result = Label(root, text="Total points achieved in section 4 is " + str(section4Pt) + " out of " + str(section4Total))
    section4Result.place(x=700, y=480)

    # self-governance and work collaboratively to create and achieve community goals
    governance = Label(root, text="Practice self-governance:", font=('Arial', 12))
    governance.place(x=700, y=520)

    section5Total = 18
    section5Pt = 0

    allDocTurnIn = req.allDocTurnIn(houseNum, file)
    turnedInOnTime = req.turnInOnTime(houseNum, file)
    if allDocTurnIn == 1 and turnedInOnTime == 1:
        allDoc = Label(root, text="All Docs Turned In On Time", background='green')
        allDoc.place(x=700, y=560)
        section5Pt = section5Pt + 2
    elif allDocTurnIn == 1 and insuranceLate == 0:
        allDoc = Label(root, text="All Docs Turned In,But Not On Time", background='yellow')
        allDoc.place(x=700, y=560)
        section5Pt = section5Pt + 1
    elif allDocTurnIn == 0:
        allDoc = Label(root, text="No Docs Turned In", background='red')
        allDoc.place(x=700, y=560)
    else:
        allDoc = Label(root, text="Bylaws,JBoard,Constitution")
        allDoc.place(x=700, y=560)

    annualBudget = req.anualBudget(houseNum, file)
    if annualBudget == 1:
        budget = Label(root, text="Annual Budget", background='green')
        budget.place(x=700, y=580)
        section5Pt = section5Pt + 1
    elif annualBudget == 0:
        budget = Label(root, text="Annual Budget ", background='red')
        budget.place(x=700, y=580)
    else:
        budget = Label(root, text="Annual Budget ")
        budget.place(x=700, y=580)

    submittAllAlcForms = req.submitForms(houseNum, file)
    if submittAllAlcForms == 1:
        alcForms = Label(root, text="Organization’s Registration For Alcohol Event", background='green')
        alcForms.place(x=700, y=600)
        section5Pt = section5Pt + 5
    elif submittAllAlcForms == 0:
        alcForms = Label(root, text="Organization’s Registration For Alcohol Event", background='red')
        alcForms.place(x=700, y=600)
    else:
        alcForms = Label(root, text="Organization’s Registration For Alcohol Event")
        alcForms.place(x=700, y=600)

    riskManagementPlan = req.submitForms(houseNum, file)
    if riskManagementPlan == 1:
        riskPlan = Label(root, text="Organization’s Registration For Alcohol Event", background='green')
        riskPlan.place(x=700, y=600)
        section5Pt = section5Pt + 5
    elif submittAllAlcForms == 0:
        riskPlan = Label(root, text="Organization’s Registration For Alcohol Event", background='red')
        riskPlan.place(x=700, y=600)
    else:
        riskPlan = Label(root, text="Organization’s Registration For Alcohol Event")
        riskPlan.place(x=700, y=600)

    deadlineF = req.deadlinesFall(houseNum, file)
    if deadlineF == 1:
        deadlinef = Label(root, text="Fall Deadlines", background='green')
        deadlinef.place(x=700, y=620)
        section5Pt = section5Pt + 5
    elif deadlineF == 0:
        deadlinef = Label(root, text="Fall Deadlines", background='red')
        deadlinef.place(x=700, y=620)
    else:
        deadlinef = Label(root, text="Fall Deadlines")
        deadlinef.place(x=700, y=620)

    deadlineS = req.deadlinesSpring(houseNum, file)
    if deadlineS == 1:
        deadlines = Label(root, text="Spring Deadlines", background='green')
        deadlines.place(x=700, y=640)
        section5Pt = section5Pt + 5
    elif deadlineS == 0:
        deadlines = Label(root, text="Spring Deadlines", background='red')
        deadlines.place(x=700, y=640)
    else:
        deadlines = Label(root, text="Spring Deadlines")
        deadlines.place(x=700, y=640)

    section5Result = Label(root, text="Total points achieved in section 5 is " + str(section5Pt) + " out of " + str(section5Total))
    section5Result.place(x=700, y=680)

    maxscore = section1Total+section2Total+section3Total+section4Total+section5Total
    resultScore = section1Pt + section2Pt + section3Pt + section4Pt + section5Pt

    result = Label(root, text="Total points achieved is " + str(resultScore) + " out of " + str(maxscore))
    result.place(x=400, y=650)

    achieveLevel = 0

    if resultScore >= 80:
        achieveLevel = 5
    elif resultScore >= 60 and resultScore <= 79.5:
        achieveLevel = 4
    elif resultScore >= 45 and resultScore <= 59.5:
        achieveLevel = 3
    elif resultScore >= 30 and resultScore <= 44.5:
        achieveLevel = 2
    elif resultScore >= 1 and resultScore <= 29.5:
        achieveLevel = 1
    else:
        achieveLevel = 0

    level = Label(root, text="Level Achieve From The Score Of " + str(resultScore) + " Is "+ str(achieveLevel), font=('Arial', 12))
    level.place(x=350, y=650)

