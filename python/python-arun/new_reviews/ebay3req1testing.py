import lxml
from lxml import etree
import urllib2
import lxml.html as lh
from bs4 import BeautifulSoup as BS

k=0
#f=open('/home/aknauhwar/Desktop/ebay testing/ebaytext.txt' , "w")
#default http://www.ebay.com/itm/
doc = lh.parse("http://www.ebay.com/itm/271362049663")

text = doc.xpath('//*[id("seeCompLnk")]/text()')


if "See compatible vehicles" in text :
    print "yes"
    k=1
else :
    print "bad request"
    #getProductDetails
    
    
#find epid:
'''epidDoc = urllib.urlopen("http://www.ebay.com/itm/271362049663").read()
soup1=BS(epidDoc)
x=soup1.findAll()
t=soup.findAll('div', attrs={'class' : 'image-imageContainer'})'''
textepid=doc.xpath('//*[id("w1-8epid")]/div[1]/text()')
p_eid =0
for i in textepid :
    #print i
    if "eBay Product ID: EPID" in i :
        id = i.split("EPID")
        p_eid=id[1]
        print p_eid
        break
    
        

    
    


print len(textepid)


    
if k:
    
        
    doc2 = urllib.urlopen("http://frame.ebay.com/ebaymotors/ws/eBayISAPI.dll?GetFitmentData&rand=0.3967430352423186&site=100&req=2&cid=46102&item=271362049663&ct=20&pn=&page=1&cb=jQuery").read()
    
    soup = BS(doc2)
    
    t=soup.findAll('body')
    
    
    m=str(t[0])
    k=m.split('"pageInfo":')
    if "null" in k[1] :
        #request1 case find epid 
        print "collect epid"
        pid= eid
        url3="http://frame.ebay.com/ebaymotors/ws/eBayISAPI.dll?GetFitmentData&rand=0.3635987357117708&site=100&req=1&cid=33567&pid="+pid+"&item=271362049663&ct=20&page=1&cb=jQuery"
        print url3
        doc3=urllib.urlopen(url3).read()
        soup3=BS(doc3)
        
        j=soup3.findAll('body')
        
        print j[0]
    
    else :
        for r in t :
        
        #     print 
            #print('\n\n\n\n')
            #f.write(str(r)+'\n\n\n\n\n')
            print "request2"
          
#f.close

    