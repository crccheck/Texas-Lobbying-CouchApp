                                                                 Read_Me.txt
                        TEXAS ETHICS COMMISSION
                   DATA FROM LOBBY ACTIVITIES REPORTS

        www.ethics.state.tx.us  *  800.325.8506  *  512.463.5800


 This CD contains information from Lobby Activities reports filed electronically
 with the Texas Ethics Commission beginning February 10, 2005, and totals from
 reports filed on paper from 1993.  Most reports have been filed electronically
 beginning February 10, 2005, but some are filed on paper.  TEC staff enters totals
 from the Cover Page of reports filed on paper but does not enter detailed information
 from the Schedules.  Information from reports which have been superseded by corrected
 reports is not included.  The highest Repno covered in this data is 464916.

 The data is presented in the following formats:

 MS-Access 2000 format
 MS-Excel csv format



 S U M M A R Y

 TABLE_NAME     DATE_CREATED      #RECORDS    NOTES

 LaCvr          10/08/2010         115,182    Form LA Cover Sheet (totals)
 LaI4E          10/08/2010          10,177    Individual Reporting for Entity
 LaSubj         10/08/2010          75,225    Schedule A - Subject Matter
 LaDock         10/08/2010             397    Schedule A - Dockets
 LaTran         10/08/2010             716    Schedule B - Transportation
 LaFood         10/08/2010           4,762    Schedule C - Food & Beverages
 LaEnt          10/08/2010           1,402    Schedule D - Entertainment
 LaGift         10/08/2010           1,642    Schedule E - Gifts
 LaAwrd         10/08/2010             588    Schedule F - Awards & Mementos
 LaEvnt         10/08/2010           1,556    Schedule G - Events
 -----------------------------------------
                                   211,647

Table Structure: LaCvr; Form LA Cover Sheet information

  NOTE: Records are included only if the due date assigned by TEC staff
        is after January 10, 2005.  Most Lobby Activities reports due
        01/10/2005 were filed on paper; most reports due afterwards
        were filed electronically.  TEC staff enters totals from the
        cover page of paper reports, but does not enter any information
        from the schedules.
        

  #     Name           Description  (*)=see note        Type       Size

  1     REPNO          Unique Report#               (1) Number     10.0
  2     HOWFILED       Electronic or Paper          (2) Text          7
  3     CORR_NUM       Correction Number (0=Original)   Number      3.0
  4     CORR_EXPL      Explanation of Correction        Memo         10
  5     COR_AFF_CB     Correction Aff. Checkbox    (16) Text          1
  6     YEAR_APPL      Year Applicable                  Text          4
  7     FILER_ID       Filer Account#               (3) Text          8
  8     LOB_NAME       Lobbyist Current Name        (4) Text        100
  9     DUE_DATE       Date Report was Due              Date          8
 10     FILED_DATE     Date Report was Filed        (5) Date          8
 11     RPT_DATE       Date Report was Received     (6) Date          8
 12     RPT_BEG_DT     Period Covered Begin Date        Date          8
 13     RPT_END_DT     Period Covered End Date          Date          8
 14     ENTITY_CD      Entity Code                  (7) Text          3
 15     FILER_NAML     Lobbyist Last Name           (8) Text        100
 16     FILER_NAMF     Lobbyist First Name              Text         45
 17     FILER_NAMT     Lobbyist Title (e.g., Mr.)       Text         15
 18     FILER_NAMS     Lobbyist Suffix (e.g., Jr.)      Text          5
 19     FIILERSHORT    Lobbyist Nickname/Acronym        Text         25
 20     SIGN_PRINT     Lobbyist Name as Signed      (9) Text         55
 21     IND4ENT_YN     Individ Reporting for Entity?(10)Text          1
 22     RT_MOD_CB      Report Type Modified   (X=true)  Text          1
 23     RT_REG_CB      Report Type Regular    (X=true)  Text          1
 24     RT_1K_CB       Report Type Exceeded $1000       Text          1
 25     RT_FIN_CB      Report Type Final      (X=true)  Text          1
 26     RDL_JAN_CB     Report Deadline Jan 10 (X=true)  Text          1
 27     RDL_FEB_CB     Report Deadline Feb 10 (X=true)  Text          1
 28     RDL_MAR_CB     Report Deadline Mar 10 (X=true)  Text          1
 29     RDL_APR_CB     Report Deadline Apr 10 (X=true)  Text          1
 30     RDL_MAY_CB     Report Deadline May 10 (X=true)  Text          1
 31     RDL_JUN_CB     Report Deadline Jun 10 (X=true)  Text          1
 32     RDL_JUL_CB     Report Deadline Jul 10 (X=true)  Text          1
 33     RDL_AUG_CB     Report Deadline Aug 10 (X=true)  Text          1
 34     RDL_SEP_CB     Report Deadline Sep 10 (X=true)  Text          1
 35     RDL_OCT_CB     Report Deadline Oct 10 (X=true)  Text          1
 36     RDL_NOV_CB     Report Deadline Nov 10 (X=true)  Text          1
 37     RDL_DEC_CB     Report Deadline Dec 10 (X=true)  Text          1
 38     EXTYPE_TRAN    Transportation & Lodging         Number     10.2
 39     EXTYPE_FOOD    Food & Beverages                 Number     10.2
 40     EXTYPE_ENT     Entertainment                    Number     10.2
 41     EXTYPE_GIFT    Gifts                            Number     10.2
 42     EXTYPE_AWDS    Awards & Mementos                Number     10.2
 43     EXTYPE_EVNT    Pol Fundraisers / Charity Events Number     10.2
 44     EXTYPE_MEDA    Mass Media Communications        Number     10.2
 45     EXBEN_SEN      State Senators                   Number     10.2
 46     EXBEN_REP      State Representatives            Number     10.2
 47     EXBEN_OTH      Other Elected/Appointed Offcls   Number     10.2
 48     EXBEN_LEG      Legislative Branch Employees     Number     10.2
 49     EXBEN_EXEC     Executive Agency Employees       Number     10.2
 50     EXBEN_FAM      Family of Legis/Exec Branch      Number     10.2
 51     EXBEN_EVNT     Events - All Legis Invited       Number     10.2
 52     EXBEN_GUEST    Guests                           Number     10.2
 53     FILER_STAR     Date Registered (for YEAR_APPL)  Date          8
 54     FILER_ENDD     Date Terminated (for YEAR_APPL)  Date          8
 55     CVR_MEMO       Cover Sheet Memo                 Memo         10
 56     SUBJ_MEMO      Schedule A: Subject Matter Memo  Memo         10
 57     DOCK_MEMO      Schedule A: Dockets Memo         Memo         10
 58     TRAN_MEMO      Schedule B: Transportation Memo  Memo         10
 59     FOOD_MEMO      Schedule C: Food Memo            Memo         10
 60     ENT_MEMO       Schedule D: Entertainment Memo   Memo         10
 61     GIFT_MEMO      Schedule E: Gifts Memo           Memo         10
 62     AWRD_MEMO      Schedule F: Awards Memo          Memo         10
 63     EVNT_MEMO      Schedule G: Events Memo          Memo         10
 64     LOB_SORT       Lobbyist Name for sorting        Text        100


Table Structure: LaI4E; Form LA Cover Sheet Box 9 - Indivduals Reporting For Entity

  NOTE:  Form LA Instructions for this box state "Check 'YES' if you are
         reporting expenditures at the request of an entity that has chosen
         not to register pursuant to Ethics Commission rule 34.45.  If you     
         check 'YES' provide the name, address and phone number of the
         entity.  Checking 'YES' indicates that you are reporting not only
         expenditures attributable to you but also expenditures attributable
         to the entity listed."

  1     IDNO           Unique ID# for this record       Number     10.0
  2     REPNO          Unique Report#               (1) Number     10.0
  3     CORR_NUM       Correction Number (0=Original)   Number      3.0
  4     YEAR_APPL      Year Applicable                  Text          4
  5     FILER_ID       Filer Account#               (3) Text          8
  6     LOB_NAME       Lobbyist Current Name        (4) Text        100
  7     DUE_DATE       Date Report was Due              Date          8
  8     RPT_DATE       Date Report was Received     (6) Date          8
  9     RPT_BEG_DT     Period Covered Begin Date        Date          8
 10     RPT_END_DT     Period Covered End Date          Date          8
 11     I4E_NAML       Entity Name                      Text        100
 12     I4E_ADR1       Address Line 1                   Text         55
 13     I4E_ADR2       Address Line 2                   Text         55
 14     I4E_CITY       City                             Text         30
 15     I4E_STCD       State Code                       Text          2
 16     I4E_ZIP4       Zip Code                         Text         10
 17     I4E_PHONE      Phone Number                     Text         10
 18     LOB_SORT       Lobbyist Name for sorting        Text        100


Table Structure: LaSubj; Form LA Schedule A - Subject Matter Categories

  NOTE:  Form LA Schedule A Box 4 states "If your lobby communications
         pertained to subject matters not marked on your original lobby
         registration or on a previous amendment, check the appropriate boxes."
         Unlike other tables in this document, subject matter is based on the
         Year Applicable rather than due date.  This information was not entered
         from paper reports prior to the year 2000.

  1     IDNO           Unique ID# for this record       Number     10.0
  2     REPNO          Unique Report#               (1) Number     10.0
  3     REG_REPNO      REPNO - most recent REG     (11) Number     10.0
  4     CORR_NUM       Correction Number (0=Original)   Number      3.0
  5     YEAR_APPL      Year Applicable                  Text          4
  6     FILER_ID       Filer Account#               (3) Text          8
  7     LOB_NAME       Lobbyist Current Name        (4) Text        100
  8     DUE_DATE       Date Report was Due              Date          8
  9     RPT_DATE       Date Report was Received     (6) Date          8
 10     RPT_BEG_DT     Period Covered Begin Date        Date          8
 11     RPT_END_DT     Period Covered End Date          Date          8
 12     FORM_TYPE      Type of Form                (12) Text          8
 13     CATGNUM        Category Number                  Text          2
 14     CATG_DESC      Category Description             Text         50
 15     OTH_DESC       Description (if Category=Other)  Text         50
 16     LOB_SORT       Lobbyist Name for sorting        Text        100


Table Structure: LaDock; Form LA Schedule A - Docket Nos or Other Designation

  NOTE:  Form LA Instructions for this box state "List the docket number
         and the name of the state agency at which any administrative matter
         is pending about which you, anyone you retain or employ to appear      
         on your behalf, or anyone who appears on your behalf communicated
         with an officer of the executive or legislative branch of state
         government during the reporting period."

  1     IDNO           Unique ID# for this record       Number     10.0
  2     REPNO          Unique Report#               (1) Number     10.0
  3     CORR_NUM       Correction Number (0=Original)   Number      3.0
  4     YEAR_APPL      Year Applicable                  Text          4
  5     FILER_ID       Filer Account#               (3) Text          8
  6     LOB_NAME       Lobbyist Current Name        (4) Text        100
  7     DUE_DATE       Date Report was Due              Date          8
  8     RPT_DATE       Date Report was Received     (6) Date          8
  9     RPT_BEG_DT     Period Covered Begin Date        Date          8
 10     RPT_END_DT     Period Covered End Date          Date          8
 11     FORM_TYPE      Type of Form                (12) Text          8
 12     DESIG          Designation                      Text         20
 13     AGENCY_NM      Agency Name                      Text        100
 14     LOB_SORT       Lobbyist Name for sorting        Text        100


Table Structure: LaTran; Form LA Schedule B - Transportation & Lodging

  1     IDNO           Unique ID# for this record       Number     10.0
  2     REPNO          Unique Report#               (1) Number     10.0
  3     CORR_NUM       Correction Number (0=Original)   Number      3.0
  4     YEAR_APPL      Year Applicable                  Text          4
  5     FILER_ID       Filer Account#               (3) Text          8
  6     LOB_NAME       Lobbyist Current Name        (4) Text        100
  7     DUE_DATE       Date Report was Due              Date          8
  8     RPT_DATE       Date Report was Received     (6) Date          8
  9     RPT_BEG_DT     Period Covered Begin Date        Date          8
 10     RPT_END_DT     Period Covered End Date          Date          8
 11     CRED_CARD      Credit Card Expenditure     (13) Text          1
 12     EXPN_MONTH     Credit Card Expend Date     (14) Text          3
 13     REC_NAML       Recipient Last Name              Text        100
 14     REC_NAMF       Recipient First Name             Text         50
 15     REC_NAMT       Recipient Title (e.g., Mr.)      Text         15
 16     REC_NAMS       Recipient Suffix (e.g., Jr.)     Text          5
 17     REC_NAMN       Recipient Nickname               Text         25
 18     TRANS_TYPE     Type of Transportation           Text         50
 19     DPT_CITY       Departure City                   Text         30
 20     DPT_DATE       Departure Date                   Date          8
 21     ARV_CITY       Arrival City                     Text         30
 22     ARV_DATE       Arrival Date                     Date          8
 23     LODGE_NAME     Name of Lodging Establishment    Text        100
 24     LODGE_ADR1     Lodge Address Line 1             Text         55
 25     LODGE_ADR2     Lodge Address Line 2             Text         55
 26     LODGE_CITY     Lodge City                       Text         30
 27     LODGE_STCD     Lodge State Code                 Text          2
 28     LODGE_ZIP      Lodge Zip Code                   Text         10
 29     CHKIN_DATE     Check In Date                    Date          8
 30     CHKOUT_DAT     Check Out Date                   Date          8
 31     PURPOSE        Transportation/Lodging Purpose   Text        254
 32     LOB_SORT       Lobbyist Name for sorting        Text        100


Table Structure: LaFood; Form LA Schedule C - Food & Beverages

  #     Name           Description  (*)=see note        Type       Size

  1     IDNO           Unique ID# for this record       Number     10.0
  2     REPNO          Unique Report#               (1) Number     10.0
  3     CORR_NUM       Correction Number (0=Original)   Number      3.0
  4     YEAR_APPL      Year Applicable                  Text          4
  5     FILER_ID       Filer Account#               (3) Text          8
  6     LOB_NAME       Lobbyist Current Name        (4) Text        100
  7     DUE_DATE       Date Report was Due              Date          8
  8     RPT_DATE       Date Report was Received     (6) Date          8
  9     RPT_BEG_DT     Period Covered Begin Date        Date          8
 10     RPT_END_DT     Period Covered End Date          Date          8
 11     REC_NAML       Recipient Last Name              Text        100
 12     REC_NAMF       Recipient First Name             Text         50
 13     REC_NAMT       Recipient Title (e.g., Mr.)      Text         15
 14     REC_NAMS       Recipient Suffix (e.g., Jr.)     Text          5
 15     REC_SHORT      Recipient Nickname               Text         25
 16     EXP_PLACE      Name of Restaurant/Other Place   Text        100
 17     EXP_CITY       City                             Text         30
 18     EXP_STCD       State Code                       Text          2
 19     EXP_ZIP4       Zip Code                         Text         10
 20     CRED_CARD      Credit Card Expenditure     (13) Text          1
 21     EXP_DATE       Expenditure Date                 Date          8
 22     AMT_100_CB     Less than $100          (X=true) Text          1
 23     AMT_150_CB     $100 but less than $150 (X=true) Text          1
 24     AMT_200_CB     $150 but less than $200 (X=true) Text          1
 25     AMT_250_CB     $200 but less than $250 (X=true) Text          1
 26     AMT_300_CB     $250 but less than $300 (X=true) Text          1
 27     AMT_350_CB     $300 but less than $350 (X=true) Text          1
 28     AMT_400_CB     $350 but less than $400 (X=true) Text          1
 29     AMT_450_CB     $400 but less than $450 (X=true) Text          1
 30     AMT_500_CB     $450 but less than $500 (X=true) Text          1
 31     EXP_OTHER_     Exact $ in EXPAMOUNT    (X=true) Text          1
 32     EXPAMOUNT      Exact Amount                     Number     10.2
 33     nLow           Low end of amount range    (15)  Number     10.2
 34     nHigh          High end of amount range   (15)  Number     10.2
 35     LOB_SORT       Lobbyist Name for sorting        Text        100


Table Structure: LaEnt; Form LA Schedule D - Entertainment

  #     Name           Description  (*)=see note        Type       Size

  1     IDNO           Unique ID# for this record       Number     10.0
  2     REPNO          Unique Report#               (1) Number     10.0
  3     CORR_NUM       Correction Number (0=Original)   Number      3.0
  4     YEAR_APPL      Year Applicable                  Text          4
  5     FILER_ID       Filer Account#               (3) Text          8
  6     LOB_NAME       Lobbyist Current Name        (4) Text        100
  7     DUE_DATE       Date Report was Due              Date          8
  8     RPT_DATE       Date Report was Received     (6) Date          8
  9     RPT_BEG_DT     Period Covered Begin Date        Date          8
 10     RPT_END_DT     Period Covered End Date          Date          8
 11     REC_NAML       Recipient Last Name              Text        100
 12     REC_NAMF       Recipient First Name             Text         50
 13     REC_NAMT       Recipient Title (e.g., Mr.)      Text         15
 14     REC_NAMS       Recipient Suffix (e.g., Jr.)     Text          5
 15     REC_SHORT      Recipient Nickname               Text         25
 16     ENT_NAME       Place of Entertainment           Text        100
 17     ENT_ADR1       Address Line 1 (Not used)        Text         55
 18     ENT_ADR2       Address Line 2 (Not used)        Text         55
 19     ENT_CITY       City                             Text         30
 20     ENT_STCD       State Code                       Text          2
 21     ENT_ZIP4       Zip Code                         Text         10
 22     CRED_CARD      Credit Card Expenditure     (13) Text          1
 23     ENT_DATE       Expenditure Date                 Date          8
 24     AMT_100_CB     Less than $100          (X=true) Text          1
 25     AMT_150_CB     $100 but less than $150 (X=true) Text          1
 26     AMT_200_CB     $150 but less than $200 (X=true) Text          1
 27     AMT_250_CB     $200 but less than $250 (X=true) Text          1
 28     AMT_300_CB     $250 but less than $300 (X=true) Text          1
 29     AMT_350_CB     $300 but less than $350 (X=true) Text          1
 30     AMT_400_CB     $350 but less than $400 (X=true) Text          1
 31     AMT_450_CB     $400 but less than $450 (X=true) Text          1
 32     AMT_500_CB     $450 but less than $500 (X=true) Text          1
 33     EXP_OTHER_     Exact $ in EXPAMOUNT    (X=true) Text          1
 34     EXPAMOUNT      Exact Amount                     Number     10.2
 35     nLow           Low end of amount range    (15)  Number     10.2
 36     nHigh          High end of amount range   (15)  Number     10.2
 37     LOB_SORT       Lobbyist Name for sorting        Text        100


Table Structure: LaGift; Form LA Schedule E - Gifts

  #     Name           Description  (*)=see note        Type       Size

  1     IDNO           Unique ID# for this record       Number     10.0
  2     REPNO          Unique Report#               (1) Number     10.0
  3     CORR_NUM       Correction Number (0=Original)   Number      3.0
  4     YEAR_APPL      Year Applicable                  Text          4
  5     FILER_ID       Filer Account#               (3) Text          8
  6     LOB_NAME       Lobbyist Current Name        (4) Text        100
  7     DUE_DATE       Date Report was Due              Date          8
  8     RPT_DATE       Date Report was Received     (6) Date          8
  9     RPT_BEG_DT     Period Covered Begin Date        Date          8
 10     RPT_END_DT     Period Covered End Date          Date          8
 11     CRED_CARD      Credit Card Expenditure     (13) Text          1
 12     EXPN_MONTH     Credit Card Expend Date     (14) Text          3
 13     REC_NAML       Recipient Last Name              Text        100
 14     REC_NAMF       Recipient First Name             Text         50
 15     REC_NAMT       Recipient Title (e.g., Mr.)      Text         15
 16     REC_NAMS       Recipient Suffix (e.g., Jr.)     Text          5
 17     REC_SHORT      Recipient Nickname               Text         25
 18     GIFT_DSCR      Gift Description                 Text        254
 19     AMT_100_CB     Less than $100          (X=true) Text          1
 20     AMT_150_CB     $100 but less than $150 (X=true) Text          1
 21     AMT_200_CB     $150 but less than $200 (X=true) Text          1
 22     AMT_250_CB     $200 but less than $250 (X=true) Text          1
 23     AMT_300_CB     $250 but less than $300 (X=true) Text          1
 24     AMT_350_CB     $300 but less than $350 (X=true) Text          1
 25     AMT_400_CB     $350 but less than $400 (X=true) Text          1
 26     AMT_450_CB     $400 but less than $450 (X=true) Text          1
 27     AMT_500_CB     $450 but less than $500 (X=true) Text          1
 28     AMT_OTHER_     Exact $ in EXPAMOUNT    (X=true) Text          1
 29     EXPAMOUNT      Exact Amount                     Number     10.2
 30     nLow           Low end of amount range    (15)  Number     10.2
 31     nHigh          High end of amount range   (15)  Number     10.2
 32     LOB_SORT       Lobbyist Name for sorting        Text        100


Table Structure: LaAwrd; Form LA Schedule F - Awards & Mementos

  #     Name           Description  (*)=see note        Type       Size

  1     IDNO           Unique ID# for this record       Number     10.0
  2     REPNO          Unique Report#               (1) Number     10.0
  3     CORR_NUM       Correction Number (0=Original)   Number      3.0
  4     YEAR_APPL      Year Applicable                  Text          4
  5     FILER_ID       Filer Account#               (3) Text          8
  6     LOB_NAME       Lobbyist Current Name        (4) Text        100
  7     DUE_DATE       Date Report was Due              Date          8
  8     RPT_DATE       Date Report was Received     (6) Date          8
  9     RPT_BEG_DT     Period Covered Begin Date        Date          8
 10     RPT_END_DT     Period Covered End Date          Date          8
 11     CRED_CARD      Credit Card Expenditure     (13) Text          1
 12     EXPN_MONTH     Credit Card Expend Date     (14) Text          3
 13     REC_NAML       Recipient Last Name              Text        100
 14     REC_NAMF       Recipient First Name             Text         50
 15     REC_NAMT       Recipient Title (e.g., Mr.)      Text         15
 16     REC_NAMS       Recipient Suffix (e.g., Jr.)     Text          5
 17     REC_SHORT      Recipient Nickname               Text         25
 18     AWARD_DSCR     Gift Description                 Text        254
 19     AMT_100_CB     Less than $100          (X=true) Text          1
 20     AMT_150_CB     $100 but less than $150 (X=true) Text          1
 21     AMT_200_CB     $150 but less than $200 (X=true) Text          1
 22     AMT_250_CB     $200 but less than $250 (X=true) Text          1
 23     AMT_300_CB     $250 but less than $300 (X=true) Text          1
 24     AMT_350_CB     $300 but less than $350 (X=true) Text          1
 25     AMT_400_CB     $350 but less than $400 (X=true) Text          1
 26     AMT_450_CB     $400 but less than $450 (X=true) Text          1
 27     AMT_500_CB     $450 but less than $500 (X=true) Text          1
 28     AMT_OTHER_     Exact $ in EXPAMOUNT    (X=true) Text          1
 29     EXPAMOUNT      Exact Amount                     Number     10.2
 30     nLow           Low end of amount range    (15)  Number     10.2
 31     nHigh          High end of amount range   (15)  Number     10.2
 32     LOB_SORT       Lobbyist Name for sorting        Text        100

Table Structure: LaEvnt; Form LA Schedule G - Pol. Fundraisers & Charity Events

  1     IDNO           Unique ID# for this record (TEC) Number     10.0
  2     ITEM_ID        ID# for this record (filer)      Text         20
  3     BAKREF_ID      ITEM_ID of 1st record for event  Text         20
  4     REPNO          Unique Report# (TEC)         (1) Number     10.0
  5     CORR_NUM       Correction Number (0=Original)   Number      3.0
  6     YEAR_APPL      Year Applicable                  Text          4
  7     FILER_ID       Filer Account#               (3) Text          8
  8     LOB_NAME       Lobbyist Current Name        (4) Text        100
  9     DUE_DATE       Date Report was Due              Date          8
 10     RPT_DATE       Date Report was Received     (6) Date          8
 11     RPT_BEG_DT     Period Covered Begin Date        Date          8
 12     RPT_END_DT     Period Covered End Date          Date          8
 13     REC_NAML       Recipient Last Name              Text        100
 14     REC_NAMF       Recipient First Name             Text         50
 15     REC_NAMT       Recipient Title (e.g., Mr.)      Text         15
 16     REC_NAMS       Recipient Suffix (e.g., Jr.)     Text          5
 17     REC_SHORT      Recipient Nickname               Text         25
 18     CHARITY_CB     Charity Chekcbox       (X=true)  Text          1
 19     FUND_CB        Political Fundraiser   (X=true)  Text          1
 20     EVENT_NAME     Charity / Event Name             Text        100
 21     CRED_CARD      Credit Card Expenditure     (13) Text          1
 22     EVENT_DATE     Event Date                       Date          8
 23     BEN_NAML       Beneficiary Last Name            Text        100
 24     BEN_NAMF       Beneficiary First Name           Text         50
 25     BEN_NAMT       Beneficiary Title (e.g., Mr.)    Text         15
 26     BEN_NAMS       Beneficiary Suffix (e.g., Jr.)   Text          5
 27     BEN_SHORT      Beneficiary Nickname             Text         25
 28     LOB_SORT       Lobbyist Name for sorting        Text        100


 NOTES:

 (1)  REPNO: Unique Report Number assigned by TEC.

 (2)  HOWFILED: E-FILED = Electronic, PAPER = Paper (totals entered by TEC)

 (3)  FILER_ID: The filer's account number (assigned by TEC)

 (4)  LOB_NAME: The lobbyist name as currently stored in the TEC database.
      It may have been reported differently on the Lobby Activity Report.
 
 (5)  FILED_DATE: The date the report was filed.  If filed by U.S. Mail or
      common carrier, this is the postmark date.  If the date is not present
      or illegible, it is blank.  If the report is a correction, this is
      the date the correction was filed.  Thus, a report with a filed_date
      after the due date is NOT NECESSARILY LATE.

 (6)  RPT_DATE: The date the report was actually received by the Texas
      Ethics Commission.  There are circumstances in which a report
      received after the due date is NOT CONSIDERED LATE.  For example,
      a report filed on diskette is timely filed if it is postmarked by the
      deadline regardless of when it is received.

 (7)  ENTITY_CD: Lobbyist Entity Code on report:  ENT = Entity; IND = Individual

 (8)  FILER_NAML: Lobbyist Last/Entity name as reported in Lobby Activties
      Report.  The Lobbyist name may have changed since this report.  See
      #4 LOB_NAME above for most recent name.

 (9)  SIGN_PRINT: Lobbyist signature

(10)  IND4ENT_YN: Individual Reporting for Entity.  Y = Yes; N = No.
      This field corresponds to the checkbox in box 9 on the Cover Sheet
      of Form LA.

(11)  REG_REPNO:  Report Number of the most recently filed Registration
      or Amendment Registration. If REG_REPNO is higher than the REPNO
      of the LA, then the Subject Matter may be superseded.  Form LA,
      Schedule A, Box 4 states "If your lobby communications pertained to
      subject matters not marked on your original lobby registration or
      on a previous amendment, check the appropriate boxes."

(12)  FORM_TYPE: Type of Form:

      (only those from Form LA are included in this request)

      for Subject Matter Categories:
      REG-11  Form REG Cover Sheet Box 11 (Lobbyist subject matter)
      REG-A41 Form REG Schedule A  Part 4 (Client subject matter)  
      REG-B5  Form REG Schedule B  Box 5  (Assistant subject matter)
      LA-A4   Form LA  Schedule A  Box 4  (Supplmental Lobbyist subject matter)

      for Docket Nos. or Other Designation:
      REG-12  Form REG Cover Sheet Box 12 (Lobbyist Dockets)
      REG-A42 Form REG Schedule A  Part 4 (Client Dockets)  
      REG-B6  Form REG Schedule B  Box 6  (Assistant Dockets)
      LA-A5   Form LA  Schedule A  Box 5  (Lobbyist Dockets)

(13)  CRED_CARD:  Expenditure made by credit card. (X=true)

      The LA Instruction Guide states "check this box if the expenditure was
      made with a credit card.  This information is required because an
      expenditure made with a credit card may appear in either the report
      covering the period in which the charge is made or the report covering
      the period in which the credit card statement is received."

      This checkbox was added to Schedules B - G effective August, 2005.
      If checked, it explains why the expenditure date may be outside the
      period covered by the report.  On schedules with no expenditure date
      (B, E & F) an additional box was added to indicate the reporting period
      in which the expenditure was made (see next note.)

 (14) EXPN_MONTH:  The month in which a credit card expenditure was made
                   (see previous note.)

      Lobbyists who file activities reports using the regular (monthly) schedule
      enter the code for the month in which the expenditure occurred.  Lobbyists
      who file on the modified (annual) schedule may enter "ANN" to indicate the
      expenditure was made during the previous year.

      ANN = Annual
      JAN = January
      FEB = February
      MAR = March
      APR = April
      MAY = May
      JUN = June
      JUL = July
      AUG = August
      SEP = September
      OCT = October
      NOV = November
      DEC = December

 (15) Amounts nLow/nHigh:  On schedules where the amount of the expenditure
      is required, it can be  reported by checking a box corresponding a range.
      These amounts correspond to the lower and higher end of each range.  For example,
      if the checkbox labeled "less than $100.00" was checked, nLow will be $0.00, and
      nHigh will be $99.99.  If the checkbox labeled "$450 but less than $500" was checked, nLow will be $0.00,
      nLow will be $450.00 and nHigh will be $499.99.  If an exact amount was given,
      that amount will be in both nLow and nHigh.

 (16) COR_AFF_CB   A value of 'X' indicates the box was checked.  A blank means
                   it was not.  This corresponds to the checkbox on the correction
                   affidavit that is labeled:

          [ ]      Check ONLY if applicable:

                   I swear, or affirm, that I am filing this corrected report not later than the
                   14th business day after the date I learned that the original report as originally
                   filed is inaccurate or incomplete.  I swear, or affirm, that any error or
                   omission in the report as originally filed was made in good faith.
