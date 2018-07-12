from mail import * 
from api import * 
from datetime import date 
import schedule
import time 
import threading 



import email 



from email.parser import Parser
parser = Parser()

acctID = ''
opptidperm = '' 
opptid = ''
bodytext = '' 

def mecha(): 
  mail.list() #Gets all emails 
  mail.select("inbox") # Gets inbox (instead of like "sent")



  result, data = mail.search(None, "ALL") #Gets "all" emails, I think maybe
 
  ids = data[0] # data is a list.
  id_list = ids.split() # ids is a space separated string 
  latest_email_id = id_list[-1] # get the latest
 
  result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
 
  raw_email = data[0][1]

  #print raw_email

  with open('data.txt', 'w') as outfile:
      json.dump(raw_email, outfile)
  global bodytext
  #Gets email body 
  email = parser.parsestr(raw_email)



  bodytext=email.get_payload()[0].get_payload()
  if type(bodytext) is list:
    bodytext=','.join(str(v) for v in bodytext)








  def getName(): 
    
    #Creating getName method 
    num = bodytext.index('ID')
    start = num + 4

    stop = start + 18
    
    #Add 15 char to end of ID 
    global acctID 
    acctID = bodytext[start:stop]
    acctID = acctID.strip()
    


 
  def checkName():
    subject = email.get('Subject')

    if subject == 'FW: Order Notification' or subject == 'Fw: Order Notification':
      print 'The script works'
      getName()
    else: 
      print "Not the Notification email"
    print ''
    print "End of checkName and getName script" 

  checkName()
  
  print 'acctID: '  + acctID 
  print acctID   


  report = sf.Report.get('') 


  obj2 = report["factMap"]["T!T"]["rows"]

  count = len(obj2)
  counter = 0 



  while counter < count: 
    
    global acctID 
    global opptid
    sfdcID = obj2[counter]["dataCells"][6]["label"] #actually going to use salesforceID instead of opptid
    print sfdcID 

    opptid = obj2[counter]["dataCells"][1]["label"]
    print opptid 
    opptpayready = obj2[counter]["dataCells"][2]["label"]
    mechaclosed = obj2[counter]["dataCells"][3]["label"] 

    print ''



    if acctID == sfdcID and opptpayready == 'true' and mechaclosed == 'false':
      global opptidperm
      global opptid 
      print sfdcID 
      opptidperm = opptid
      opptpayreadyperm = opptpayready
      print "The if else loop with payready true worked."
      today = date.today().isoformat()
      closedwon = sf.Opportunity.update( opptidperm, {'StageName': 'Closed Won'})
      closedwondate = sf.Opportunity.update( opptidperm, {'CloseDate': today}) 
      mechaclosedmark = sf.Opportunity.update( opptidperm, {'mechaclosed__c': 'true'})


  
    
    print "This is pass %s" % counter 
    counter = counter + 1

    #test this section with testing.py and api.py
  print 'opptidperm: ' + opptidperm
  print 'acctID: ' + acctID 
  print 'sfdcID: ' + sfdcID 

 

#mecha()


def printMecha():
  print "mecha done "
  print ''

otherCounter = 0 


schedule.every(10).seconds.do(mecha)
schedule.every(10).seconds.do(printMecha)

while 1: 
  schedule.run_pending()




