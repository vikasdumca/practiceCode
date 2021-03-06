import httplib
from xml.dom.minidom import parse, parseString, Node

devKey = "ddc0ad4e-3e54-4179-a429-2df0f9667fda"
appKey = "arunkuma-47b1-467b-a87e-0528caad791f"
certKey = "1dc93f1d-9d5a-4955-838f-d69cad0b7cc5"

userToken = 'AgAAAA**AQAAAA**aAAAAA**jxG9Ug**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4GhC5aLoAqdj6x9nY+seQ**hnkCAA**AAMAAA**zMKhCJ2nht+IV9g6kdM89yUZ8J4VlMPdJBskG00lC959pmUAMHwe0i28m9j1IU1M65gZ5uonuIqaCumxV7UIb1qm55IjmHOmIW6EYKJQrVKDtYtUnw5q7JGhrus4CND+7ghser4e1Go90q+A5JOMqqLff+9JoEp+n2EsI7g+p2sUEPMZOhXD1McmGN+tzA4OmghX26FkA6REF57i6tfF6C04rpNJxaeLRMiUW/Dzq7rniWyOrOwLVf4PtRVmTtDe0M5dBnYJXahYNicZ7iS18D7YPhxfNkTRtbRbxDo5s7kNZwYBYsrbg/bq3ZGy6njF9gU1n9RaNjW01Qu80wXAyqVo7YDcpXznKbOm7jJ0xkb+CZe94i2pf7rmHK7kvu8N8ejY29GiNlzDZ3gV/2CL54Q+fZV+IqWyeatwuIb1LrdjUsaiN2otNIv9HuAnbj44839ucQY6WaiCCcUuerG4TDu3l2khtmT6MF/gKtLpxZ8t0ylnEHG3R81FzxAOVRnwpGI1pIrwfXKnLMzDFWX1sqTjLsQrNCHtoebJWNWl7wgaAzDBEiwiGJGo+AjL5tepVJoxuKrxNTBYNAD/4EWeBjTvJ3A3OGfM/1qNFFQ6z0kV2ToHTKShkUbwTslgARrxDHcOQdtYomHFlp2Q/O8CKntOG0lJl5BJc/Hj3yTDpiGgR3MHQ+kBB3r1wk9qjxgaCiZ8lBY/+Iy8uPjh31YlM7uz9uzQ9u5I4yUcM7eNDsWtMtf2a5Hhgx8VX5a+QV4J'


serverUrl = 'api.ebay.com'


def getHeaders(apicall,siteID="0",compatabilityLevel = "433"):
  headers = {"X-EBAY-API-COMPATIBILITY-LEVEL": compatabilityLevel,
             "X-EBAY-API-DEV-NAME": devKey,
             "X-EBAY-API-APP-NAME": appKey,
             "X-EBAY-API-CERT-NAME": certKey,
             "X-EBAY-API-CALL-NAME": apicall,
             "X-EBAY-API-SITEID": siteID,
             "Content-Type": "text/xml"}
  return headers



def sendRequest(apicall,xmlparameters):
  connection = httplib.HTTPSConnection(serverUrl)
  connection.request("POST", '/ws/api.dll', xmlparameters, getHeaders(apicall))
  response = connection.getresponse(  )
  if response.status != 200:
    print "Error sending request:" + response.reason
  else:
    data = response.read(  )
    connection.close(  )
  return data


def getSingleValue(node,tag):
  nl=node.getElementsByTagName(tag)
  if len(nl)>0:
    tagNode=nl[0]
    if tagNode.hasChildNodes(  ):
      return tagNode.firstChild.nodeValue
  return '-1'




def doSearch(query,categoryID=None,page=1):
  xml = "<?xml version='1.0' encoding='utf-8'?>"+\
        "<GetSearchResultsRequest xmlns=\"urn:ebay:apis:eBLBaseComponents\">"+\
        "<RequesterCredentials><eBayAuthToken>" +\
        userToken +\
        "</eBayAuthToken></RequesterCredentials>" + \
        "<Pagination>"+\
          "<EntriesPerPage>200</EntriesPerPage>"+\
          "<PageNumber>"+str(page)+"</PageNumber>"+\
        "</Pagination>"+\
        "<Query>" + query + "</Query>"
  if categoryID!=None:
    xml+="<CategoryID>"+str(categoryID)+"</CategoryID>"
  xml+="</GetSearchResultsRequest>"

  data=sendRequest('GetSearchResults',xml)
  response = parseString(data)
  itemNodes = response.getElementsByTagName('Item');
  results = []
  for item in itemNodes:
    itemId=getSingleValue(item,'ItemID')
    itemTitle=getSingleValue(item,'Title')
    itemPrice=getSingleValue(item,'CurrentPrice')
    itemEnds=getSingleValue(item,'EndTime')
    results.append((itemId,itemTitle,itemPrice,itemEnds))
  return results







def getCategory(query='',parentID=None,siteID='0'):
  lquery=query.lower(  )
  xml = "<?xml version='1.0' encoding='utf-8'?>"+\
        "<GetCategoriesRequest xmlns=\"urn:ebay:apis:eBLBaseComponents\">"+\
        "<RequesterCredentials><eBayAuthToken>" +\
        userToken +\
        "</eBayAuthToken></RequesterCredentials>"+\
        "<DetailLevel>ReturnAll</DetailLevel>"+\
        "<ViewAllNodes>true</ViewAllNodes>"+\
        "<CategorySiteID>"+siteID+"</CategorySiteID>"
  if parentID==None:
    xml+="<LevelLimit>1</LevelLimit>"
  else:
    xml+="<CategoryParent>"+str(parentID)+"</CategoryParent>"
  xml += "</GetCategoriesRequest>"
  data=sendRequest('GetCategories',xml)
  categoryList=parseString(data)
  catNodes=categoryList.getElementsByTagName('Category')
  for node in catNodes:
    catid=getSingleValue(node,'CategoryID')
    name=getSingleValue(node,'CategoryName')
    if name.lower(  ).find(lquery)!=-1:
      print catid,name




def getItem(itemID):
  xml = "<?xml version='1.0' encoding='utf-8'?>"+\
        "<GetItemRequest xmlns=\"urn:ebay:apis:eBLBaseComponents\">"+\
        "<RequesterCredentials><eBayAuthToken>" +\
        userToken +\
        "</eBayAuthToken></RequesterCredentials>" + \
        "<ItemID>" + str(itemID) + "</ItemID>"+\
        "<DetailLevel>ItemReturnAttributes</DetailLevel>"+\
        "</GetItemRequest>"
  data=sendRequest('GetItem',xml)
  result={}
  response=parseString(data)
  result['title']=getSingleValue(response,'Title')
  sellingStatusNode = response.getElementsByTagName('SellingStatus')[0];
  result['price']=getSingleValue(sellingStatusNode,'CurrentPrice')
  result['bids']=getSingleValue(sellingStatusNode,'BidCount')
  seller = response.getElementsByTagName('Seller')
  result['feedback'] = getSingleValue(seller[0],'FeedbackScore')
  attributeSet=response.getElementsByTagName('Attribute');
  attributes={}
  for att in attributeSet:
    attID=att.attributes.getNamedItem('attributeID').nodeValue
    attValue=getSingleValue(att,'ValueLiteral')
    attributes[attID]=attValue
  result['attributes']=attributes
  return result



laptops=doSearch('laptop')


print laptops


a=getCategory('computers')

print a





































