'''
Created on 05-Dec-2013

@author: aknauhwar
'''

import lxml
from lxml import etree
import urllib
import lxml.html as lh
from bs4 import BeautifulSoup as BS
import json
import simplejson
import ast
import mechanize
import random 
import decimal
import time
#parse the page for various 
#to find time of execution
start_time = time.time()

def gen_random_decimal(i,d):
    return decimal.Decimal('%d.%d' % (random.randint(0,i),random.randint(0,d)))

def filterquote(str):
    str0=str.replace('{"', '{DOUBLE')
    str1=str0.replace('":"', '{DOUBLE:DOUBLE')
    str2=str1.replace('":', 'DOUBLE:')
    str3=str2.replace('"}', 'DOUBLE}')
    str4=str3.replace('["', '[DOUBLE')
    str5=str4.replace('"]', 'DOUBLE]')
    str6=str5.replace('","', 'DOUBLE,DOUBLE')
    str7=str6.replace('",', 'DOUBLE,')
    str8=str7.replace(',"', ',DOUBLE')
    
    str9=str8.replace('"' , '&quot')
    str10=str9.replace('DOUBLE' , '"')
    return str10
       
def Find_pid( doc) :
    
    #text=doc.xpath('//*[id("w1-8epid")]/div[1]/text()')
    try :
            text=doc.xpath('//div/div/div/div/div/div/div/div/div/text()')
            p_eid = -1
            for i in text : 
                #print i
                if "eBay Product ID: EPID" in i :
                    id = i.split("EPID")
                    p_eid=id[1]
                    break
        
    except :
        p_eid= -1    
    return p_eid

def Find_cid(doc) :
    # not worthy
    text=doc.xpath('//div/div/a[text()="Print"]/@href')
    c_id= -1
    for i in text : 
        print i
        if "category=" in i :
            id = i.split("category=")
            c_id=id[1]
            break
        
 
    return c_id

def Pagecount(doc1 , doc2 ,f2 ,input_data):

    #get jsonpage and fing pagecount
    soup = BS(doc2)
    t=soup.findAll('body')
    m=str(t[0])
    k=m.split('"pageInfo":')
    if "null" in k[1] :
        soup3=BS(doc1)
        
        j=soup3.findAll('body')
        
        n=str(j[0])
        r=n.split('"pageInfo"')
        if "null" not in r[1] :
            l=n.split('"totalPageCount":')
            #print l[0]
            r=l[1]
            s=r.split(',"pageRecordCount"')
            id =int(s[0])+100000
        else :
            id=0
            f2.write(input_data+"    #showing it has compability list but no list found"+"\n")
    else :
        id1=m.split('"totalPageCount":')
        id2=id1[1]
        id3=id2.split(',"pageRecordCount"')
        print
        id=int(id3[0])
        
    return id   
    
def Compabilitylist(doc):
    try :
            text = doc.xpath('//*[id("seeCompLnk")]/text()')
            if "See compatible vehicles" in text :
                return 1
            else :
                return  0
    except :
        return 0
         
            
def APIreq2call(item_id , page_count , f , input_data ,f2 , f3): 
    start_time2 = time.time()
    i=1
    result=[]
    k=0
    while i <= page_count :
        try :
                    time.sleep(0.15)
                    randomapi2=str(gen_random_decimal(0,9999999999999999))
                    call_url= "http://frame.ebay.com/ebaymotors/ws/eBayISAPI.dll?GetFitmentData&rand="+randomapi2+"&site=100&req=2&cid=33567&item="+item_id+"&ct=20&pn=&page=%d&cb=jQuery"%i
                    b = mechanize.Browser()
                    # Set any header you like:
                    b.addheaders = [('Content-Type', 'text; charset=utf-8')]
                    response = b.open(call_url)
                    data = response.read()
                    #print data
                    
                    lin = data.strip('jQuery(')
                    line=lin.strip(');')
                    
                    #line5=filterquote(line) 
                    try:
                            oo = json.loads(line)
                    except ValueError, e:
                            print"DOUBLE QUOTE "*5
                            line5=filterquote(line)
                            try:
                                oo = json.loads(line5)
                            
                            except ValueError, e:
                                f3.write(input_data+'    #still double quote(i.e 21",) problen or invalid json'+"on page %d of json"%i+"\n")
                                i=i+1
                                continue
                            except :
                                f3.write(input_data+'    #still double quote(i.e 21",) problen or invalid json'+"on page %d of json"%i+"\n")
                                i=i+1
                                continue
                            #oo = json.loads(line5)
                    except :
                            print"DOUBLE QUOTE "*5
                            line5=filterquote(line)
                            try:
                                oo = json.loads(line5)
                            
                            except ValueError, e:
                                f3.write(input_data+'    #still double quote(i.e 21",) problen or invalid json'+"on page %d of json"%i+"\n")
                                i=i+1
                                continue
                            except :
                                f3.write(input_data+'    #still double quote(i.e 21",) problen or invalid json'+"on page %d of json"%i+"\n")
                                i=i+1
                                continue
                        
                        
                    
                    #oo = json.loads(line5)
                    #print "JSON parsing example: ", oo['data']
                    daata= oo['data']
                    for rs in daata :
                        if 'FitmentComments' not in rs.keys() :
                            FitmentComments=""
                        else :
                            FitmentComments=rs['FitmentComments'][0]
                            if FitmentComments is None:
                                FitmentComments=""
                            
                        if 'Model' not in rs.keys() :
                            Model=""
                        else :
                            Model=rs['Model'][0]
                            if Model is None:
                                Model=""
                            
                        if 'Year' not in rs.keys() :
                            Year=""
                        else :
                            Year=rs['Year'][0] 
                            if Year is None:
                                Year="" 
                            
                        if 'Make' not in rs.keys() :
                            Make=""
                        else :
                            Make=rs['Make'][0]
                            if Make is None:
                                Make=""
                            
                        if 'Trim' not in rs.keys() :
                            Trim="ALL"
                        else :
                            Trim=rs['Trim'][0]
                            if Trim is None:
                                Trim=""
                                f3.write(input_data +"             check if engine is none or all "+"\n")
                          
                        if 'Engine' not in rs.keys() :
                            Engine="ALL"
                        else :
                            Engine=rs['Engine'][0]
                            if Engine is None:
                                Engine=""            
                                f3.write(input_data +"             check if engine is none or all "+"\n")
                        f.write(input_data+"|"+FitmentComments+"|"+Year+"|"+Make+"|"+Model+"|"+Trim+"|"+Engine+"\n")
                        #print rs['FitmentComments'][0]
                        #print rs['Model'][0]
                        #print  rs['Year'][0]
                        #print  rs['Make'][0]
                        #print rs['Engine'][0]
                        #print type(rs)
                        #break
                        k=k+1
                        print k  
                 
                    #f.write("\n\n\n\n")
                    #f.write("%d"%i+chr(10)+ m )
            
                    i=i+1
        
        except :
            f3.write(input_data+'      maybe could not load page ,URLlerror  connection reset by peer '+"on page %d of json"%i+"\n")
            f3.flush()
            i=i+1                   
        
    if(k) :
        f2.write(input_data+"  #count ="+str(k)+"\n")
    else :
        pass
    print "api2 is the gospel truth right now"
    #f.write("\n\n\n\n"+"api2 is the gospel truth right now")
    print time.time() - start_time2, "seconds it took in api2 for processing   %s"%str(page_count)
    
def APIreq1call(item_id , page_count , pid , f , input_data , f2 ,f3): 
    start_time1 = time.time()
    i=1
    k=0
    while i <= page_count :
        try :
                    time.sleep(0.15)
                    randomapi1=str(gen_random_decimal(0,9999999999999999))
                    call_url="http://frame.ebay.com/ebaymotors/ws/eBayISAPI.dll?GetFitmentData&rand="+randomapi1+"&site=100&req=1&cid=33567&pid="+pid+"&item="+item_id+"&ct=20&page=%d&cb=jQuery"%i
                    b = mechanize.Browser()
                    # Set any header you like:
                    b.addheaders = [('Content-Type', 'text; charset=utf-8')]
                    response = b.open(call_url)
                    data = response.read()
                    #print data
                    
                    lin = data.strip('jQuery(')
                    line=lin.strip(');')
                    
                    #line5=filterquote(line) 
                    try:
                            oo = json.loads(line)
                    except ValueError, e:
                            print"DOUBLE QUOTE "*5
                            line5=filterquote(line)
                            try:
                                oo = json.loads(line5)
                            
                            except ValueError, e:
                                f3.write(input_data+'    #still double quote(i.e 21",) problen or invalid json'+"on page %d of json"%i+"\n")
                                i=i+1
                                continue
                            except :
                                f3.write(input_data+'    #still double quote(i.e 21",) problen or invalid json'+"on page %d of json"%i+"\n")
                                i=i+1
                                continue
                            #oo = json.loads(line5)
                    except :
                            print"DOUBLE QUOTE "*5
                            line5=filterquote(line)
                            try:
                                oo = json.loads(line5)
                            
                            except ValueError, e:
                                f3.write(input_data+'    #still double quote(i.e 21",) problen or invalid json'+"on page %d of json"%i+"\n")
                                i=i+1
                                continue
                            except :
                                f3.write(input_data+'    #still double quote(i.e 21",) problen or invalid json'+"on page %d of json"%i+"\n")
                                i=i+1
                                continue
                    
                    #oo = json.loads(line5)
                    #print "JSON parsing example: ", oo['data']
                    daata= oo['data']
                    for rs in daata :
                        if 'FitmentComments' not in rs.keys() :
                            FitmentComments=""
                        else :
                            FitmentComments=rs['FitmentComments'][0]
                            if FitmentComments is None:
                                FitmentComments=""
            
                        if 'Model' not in rs.keys() :
                            Model=""
                        else :
                            Model=rs['Model'][0]
                            if Model is None:
                                Model=""
                            
                        if 'Year' not in rs.keys() :
                            Year=""
                        else :
                            Year=rs['Year'][0]
                            if Year is None:
                                Year=""  
                            
                        if 'Make' not in rs.keys() :
                            Make=""
                        else :
                            Make=rs['Make'][0]
                            if Make is None:
                                Make=""
                            
                        if 'Trim' not in rs.keys() :
                            Trim="ALL"
                        else :
                            Trim=rs['Trim'][0]
                            if Trim is None:
                                Trim=""
                                f3.write(input_data +"             check if engine is none or all "+"\n")
                        if 'Engine' not in rs.keys() :
                            Engine="ALL"
                        else :
                            Engine=rs['Engine'][0]
                            if Engine is None:
                                Engine=""
                                f3.write(input_data +"             check if engine is none or all "+"\n")
                        f.write(input_data+"|"+FitmentComments+"|"+Year+"|"+Make+"|"+Model+"|"+Trim+"|"+Engine+"\n")
            
                        #print rs['FitmentComments']       
                        #print rs['FitmentComments'][0]
                        #print rs['Model'][0]
                        #print  rs['Year'][0]
                        #print  rs['Make'][0]
                        #print rs['Engine'][0]
                        k=k+1
                        print k  
                    #f.write("\n\n\n\n")
                    #f.write("%d"%i+"\n" +chr(10)+ m )
            
                    i=i+1
        except :
            f3.write(input_data+'      maybe could not load page ,URLlerror  connection reset by peer '+"on page %d of json"%i+"\n")
            f3.flush()
            i=i+1
            
        
    if(k) :
        f2.write(input_data+"  #count ="+str(k)+"\n")
    else :
        pass
    print "api1 is the gospel truth right now"
    #f.write("\n\n\n\n"+"api1 is the gospel truth right now")
    print time.time() - start_time1, "seconds it took in api2 for processing   %s"%str(page_count)                          

def main():

    #item_id ="110900855342"
    #item_id="161027979079"
    #item_id="390743382652"
    count=1202
    f=open('/home/aknauhwar/Desktop/ebay testing/EbayFinal/Fianl feb31/ebaytext.txt' , "a")
    f1=open('/home/aknauhwar/Desktop/ebay testing/EbayFinal/Fianl feb31/ebay_no_Compatibility_list.txt' , "a")  #no list or bad url or removed product or no item_id
    f2=open('/home/aknauhwar/Desktop/ebay testing/EbayFinal/Fianl feb31/ebay_list_count.txt' , "a")   
    f3=open('/home/aknauhwar/Desktop/ebay testing/EbayFinal/Fianl feb31/ebay_debugging.txt' , "a")  #for any other error
    input=open('/home/aknauhwar/Desktop/ebay testing/EbayFinal/ebay final input/input_feb31' , "r")
    input_string= input.readlines()
    for input_data in input_string[1202:] :
        #time.sleep(1)
        if(input_data) :
            input_data=input_data.strip('\n')
            #print input_data+"arun"
            #break
            inputdict= str(input_data).split("|")
            MF=inputdict[0]
            MPN=inputdict[1]
            MN=inputdict[2]
            item_id=inputdict[3];
            #item_id="390743382652"
            #print MF , MPN , MN , Item_id 
            #print type(MF)
            if item_id :   
                        url="http://www.ebay.com/itm/"+item_id
                        try :
                            doc = lh.parse(url)
                        except IOError as e:
                            #print "I/O error({0}): {1}".format(e.errno, e.strerror)
                            f1.write(str(count)+"      #bad url or either product removed"+"\n") #this count will be one less than actual position of element in the file as if we are writing 200 it means it will be 201 in input file 
                            count=count+1
                            continue
                        except ValueError:
                            #print "Could not convert data to an integer."
                            f1.write(str(count)+"      #bad url or either product removed"+"\n")
                            count=count+1
                            continue
                        except:
                            #print "Unexpected error:", sys.exc_info()[0]
                            f1.write(str(count)+"      #bad url or either product removed"+"\n")
                            count=count+1
                            continue 
                               
                        #print doc
                        cid = "33567"
                        pid=  str(Find_pid(doc))
                        random1=str(gen_random_decimal(0,9999999999999999))
                        random2=str(gen_random_decimal(0,9999999999999999))
                        url2 = "http://frame.ebay.com/ebaymotors/ws/eBayISAPI.dll?GetFitmentData&rand="+random2+"&site=100&req=2&cid="+cid+"&item="+item_id+"&ct=20&pn=&page=1&cb=jQuery"
                        url1 = "http://frame.ebay.com/ebaymotors/ws/eBayISAPI.dll?GetFitmentData&rand="+random1+"&site=100&req=1&cid="+cid+"&pid="+pid+"&item="+item_id+"&ct=20&page=1&cb=jQuery"   
                        #doc2 = urllib.urlopen(url2).read()
                        #doc1 = urllib.urlopen(url1).read()
                        try :
                            doc2 = urllib.urlopen(url2).read()
                        except :
                            f1.write(input_data+"    "+str(count)+"      #bad url or either product removed or no pid"+"\n")
                            count=count+1
                            if count==15000 :
                                    break
                            continue
                        
                        try:
                            doc1 = urllib.urlopen(url1).read()
                        except :
                            f1.write(input_data+"    "+str(count)+"      #bad url or either product removed  or no pid"+"\n")
                            count=count+1
                            if count==15000 :
                                    break
                            continue
                        #check if compability list is present or not 
                        check_list=Compabilitylist(doc)
                        page_count=0
                        api_request_number=0
                        if(check_list) :
                            page_count=Pagecount(doc1 , doc2 , f2 , input_data)
                        
                        else :
                            print "no list found"
                            #f1.write(input_data+"      #no compability list"+"\n")
                        if page_count :
                                if (page_count > 10000 ) :
                                    page_count=page_count-100000
                                    api_request_number= 1
                                    
                                else :
                                    api_request_number= 2
                        print page_count
                        #check if compability list is present or not 
                        #check_list=Compabilitylist(doc)
                        
                        if check_list :
                            
                            if(api_request_number==2) :          
                                APIreq2call(item_id , page_count , f , input_data ,f2 ,f3)
                                
                                
                            
                            elif (api_request_number==1) :
                                APIreq1call(item_id , page_count , pid , f , input_data ,f2 ,f3)
                                
                            else :
                                print "need to review "
                                f3.write(input_data+"      #list exist someother problem maybe showing compatibility list but none"+"\n")
                                
                                
                            
                            
                            
                        else :
                            f1.write(input_data+"      #no compability list"+"\n") 
                            print "do some manual work"
            else :
                print "NO ITEM ID FOUND"
                f1.write(str(count)+"      #no item_id"+"\n")                
                            
        else :
            print "check if end of file"
            f1.write(str(count)+"\n")
        count = count+1
        print "this is count number %d"%count * 3
        # if we start with count=2999 and break at count=4999 , it means that it will start with 3000th line of file and will go on till 4999th line yes it will be doing crawling for 4999th line , it is included into it. 
        if count==15000 :
            break
        
    f.close()
    input.close()     
    f1.close()
    f2.close()
    f3.close()
main()

print time.time() - start_time, "seconds this is the time for whole run of this script"  
    
    
    
    
    
    
