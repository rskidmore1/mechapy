from mail import * 
from api import * 
from datetime import date 
import schedule
import time 



import email 



from email.parser import Parser
parser = Parser()

acctID = ''
opptidperm = ''

def mecha(): 
  #Gets email body 
  '''email = parser.parsestr(raw_email)



  bodytext=email.get_payload()[0].get_payload()
  if type(bodytext) is list:
    bodytext=','.join(str(v) for v in bodytext)

  #print bodytext






  def getName(): 
  
    #Creating getName method 
    num = bodytext.index('ID')
    start = num + 3 

    stop = start + 17
    
    #Add 15 char to end of ID 
    acctID = bodytext[start:stop]

 
  def checkName():
    subject = email.get('Subject')

    if subject == 'FW: Order Notification' or 'Fw: Order Notification':
      print 'The script works'
      getName()
    else: 
      print "Not the Notification email"
    print ''
    print "End of checkName and getName script" 

  checkName()'''

  acctID = '0011500001FOOfv' 

  
  report = sf.Report.get('') 


  obj2 = report["factMap"]["T!T"]["rows"]

  count = len(obj2)
  counter = 0 



  while counter < count: 
    

    sfdcID = obj2[counter]["dataCells"][6]["label"] #actually going to use salesforceID instead of opptid
    print sfdcID 

    opptid = obj2[counter]["dataCells"][1]["label"]
    print opptid 
    opptpayready = obj2[counter]["dataCells"][2]["label"]
    mechaclosed = obj2[counter]["dataCells"][3]["label"] 
    print ''



    if acctID == sfdcID and opptpayready == 'true' and mechaclosed == 'false':
      global opptidperm 
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
  print 'opptidperm ' + opptidperm


  



mecha()






