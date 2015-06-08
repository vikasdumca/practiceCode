#Send Content-type header to browser
print "Content-type: text/html"
print
 
#import the HTTP, DOM and ConfigParser modules needed
import httplib, ConfigParser
from xml.dom.minidom import parse, parseString
 

# open config file
config = ConfigParser.ConfigParser()
config.read("/home/aknauhwar/python/apicall/config.ini")
 
# specify eBay API dev,app,cert IDs
devID = config.get("Keys", "Developer")
appID = config.get("Keys", "Application")
certID = config.get("Keys", "Certificate")


print devID
#get the server details from the config file
serverUrl = config.get("Server", "URL")
serverDir = config.get("Server", "Directory")
 
 
# specify eBay token
# note that eBay requires encrypted storage of user data
userToken = config.get("Authentication", "Token")
 
 
#eBay Call Variables
#siteID specifies the eBay international site to associate the call with
#0 = US, 2 = Canada, 3 = UK, ....
siteID = "0"
#verb specifies the name of the call
verb = "GeteBayOfficialTime"
#The API level that the application conforms to
compatabilityLevel = "433"
 
 
#Setup the HTML Page with name of call as title
print "<HTML>"
print "<HEAD><TITLE>", verb, "</TITLE></HEAD>"
print "<BODY>"

# FUNCTION: buildHttpHeaders
# Build together the required headers for the HTTP request to the eBay API
def buildHttpHeaders():
    httpHeaders = {"X-EBAY-API-COMPATIBILITY-LEVEL": compatabilityLevel,
               "X-EBAY-API-DEV-NAME": devID,
               "X-EBAY-API-APP-NAME": appID,
               "X-EBAY-API-CERT-NAME": certID,
               "X-EBAY-API-CALL-NAME": verb,
               "X-EBAY-API-SITEID": siteID,
               "Content-Type": "text/xml"}
    return httpHeaders
    
    
# FUNCTION: buildRequestXml
# Build the body of the call (in XML) incorporating the required parameters to pass
def buildRequestXml():
    requestXml = "<?xml version='1.0' encoding='utf-8'?>"+\
              "<GeteBayOfficialTimeRequest xmlns=\"urn:ebay:apis:eBLBaseComponents\">"+\
              "<RequesterCredentials><eBayAuthToken>" + userToken + "</eBayAuthToken></RequesterCredentials>" + \
              "</GeteBayOfficialTimeRequest>"
    return requestXml
    
