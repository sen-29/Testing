#import pandas as pd
from selenium import webdriver
import time
#data = pd.read_csv("users_dancing.csv") 
#print(data.head())
count =0
usrname= ["1234567890",
"2148566473",
"2175386976",
"5922199961",
"6422500845",
"4796685918",
"4384750786",
"5988121525",
"6977246351",
"8396766113",
"5657840257",
"9396917940",
"5182159823",
"3348521171",
"4824856917",
"3417585994",
"5844688186",
"6767266490",
"4964805088",
"3409005597",
"4373074525",
"6833250962",
"2575950281",
"8163612533",
"4448584045",
"5008001491",
"7189541708",
"3436154611",
"6335060706",
"3472155143",
"5032306305",
"3442699854",
"4936507345",
"5068423964",
"8333910533",
"5189999254",
"9427749379",
"8355687411",
"6093219669",
"4398786089",
"4849744873",
"5735617228",
"8719950391",
"8579996163",
"9243278849",
"8639302773"]

password=["2000",
"BEFSarcb",
"BLNSadeu",
"CGDEwht",
"CIOHordt",
"CQCOendt",
"DDQScdxr",
"DGWPbtr",
"DVMXxrdr",
"EQLWphap",
"FSKPggkb",
"FYKGruow",
"GPXIqvku",
"GUWNnyqx",
"IAJXlog",
"IHJOuvsu",
"IOOObpp",
"IQFMzhl",
"JIVSwmdk",
"KPQPxrjx",
"KVWCsgs",
"MFGDwdwf",
"MLEJuukw",
"MUOTehzr",
"MYPPphau",
"NECDyggx",
"NMPApqfw",
"OKYXhoac",
"PKLOrel",
"PKMCoqh",
"QHDCnvwd",
"QHFFbsa",
"QOQMsbo",
"RBLJptns",
"RWSOfsbc",
"TBXIxmvt",
"TZYXacbh",
"UBUMenm",
"UUMOqcdr",
"WLRBbmqb",
"WNKUewhs",
"WZQFjmaf",
"XLMNdqtu",
"XWPQcace",
"YATDrmy",
"YPAYulye"]
for x in range(15):  
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "/usr/bin/chromium"
    driver = webdriver.Chrome("/home/ujjval/Downloads/chromedriver_linux64/chromedriver")
    driver.get('http://127.0.0.1:5000/')
    driver.find_element_by_name("username").send_keys(usrname[x])
    driver.find_element_by_name("password").send_keys(password[x])
    driver.find_element_by_name("username").submit()
    time.sleep(2)
  
    oh=driver.find_elements_by_partial_link_text("View")
    #print(oh)

    if len(oh)>0:
        count=count+1
        print(usrname[x] +" data entry is working")
    else:
        print(usrname[x] +" data entry is not working")
print(count)
