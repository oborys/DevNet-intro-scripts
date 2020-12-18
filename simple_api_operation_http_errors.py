import requests
requests.packages.urllib3.disable_warnings()
from requests.exceptions import Timeout
import base64


USER_DNA = "devnetuser"
PASSWORD_DNA = "Cisco123!"
DEF_TIMEOUT = 10

def main():
    API_Server = "https://sandboxdnac.cisco.com/"
    #  functions
    sandboxAvailability(API_Server)
    checkSimpleRequest(API_Server)


def sandboxAvailability(API_Server):
    response = requests.get(API_Server)
    if response.status_code != 200:
        #send notification to bot
        print("Error", response.status_code)
        exit()
    print("response.status_code (HTTP Status codes): ", response.status_code)
    print("response.content: ", response.content[:50])
    print("response.text: ", response.text[:50])
    return (response.status_code)

def checkSimpleRequest(API_Server):
    API_Endpoint = API_Server + "api/system/v1/"
    Path = "auth/token"
    API_Resource =  API_Endpoint + Path
    usrPasDna = USER_DNA + ":" + PASSWORD_DNA
    basicDNA = base64.b64encode(usrPasDna.encode()).decode()
    HTTP_Request_header = {"Authorization": "Basic %s" % basicDNA,
                "Content-Type": "application/json;"}
    body_json = ""

    try:
        # API Operation
        response = requests.post(API_Resource, data=body_json, headers=HTTP_Request_header, verify=False, timeout=DEF_TIMEOUT)
    except Timeout as e:
        raise Timeout(e)
    tokenDNA = response.json()['Token']
    urlSimpleDNA = API_Server + "api/v1/network-device/"
    urlSimpleDNAerror = API_Server + "api/v1/network-devic/"
    HTTP_Request_header = {'x-auth-token': tokenDNA}
    try:
        response = requests.get(urlSimpleDNA, headers=HTTP_Request_header)
        print ("\n API Operation: GET https://sandboxdnac.cisco.com/api/v1/network-device/ \n", response.json())
        if response.status_code != 200:
            print("Error SimpleRequest status_code != 200")

            exit()
    except Timeout as e:
        raise Timeout(e)
    try:
        b = response.json()['response'][0]['type']
    except IndexError:
        print("Error SimpleRequest index")
        exit()

    tokenDNAexp = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI1ZjhlYjhhZDc1MTYxMjRlODczYTg0YmYiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlNWE0MzI2NzUxNjEyMDBjYzRhYzk2MyJdLCJ0ZW5hbnRJZCI6IjVlNWE0MzI1NzUxNjEyMDBjYzRhYzk1YyIsImV4cCI6MTYwNDMyMTkzOSwiaWF0IjoxNjA0MzE4MzM5LCJqdGkiOiI5NWI2ZmUyYS01OWYzLTQ4NTMtODliOC0wZDVjYjJmMTQ5YjciLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.b4WGuTHFu97PvvheuCbjzXQfWlLbWSAKylt8vk_930MEtQC4FPjrn9FT_AiD6GTIpbWl6qW_NXfhbkVfw3R0rMu7XOJSFKpqRYDocGSz6oy2F6mURo41dhnKQ4tz2CEfgoFOUPOXahOypYw8vEBz__5iHf3quRe1Iqhnj4STntIHh7XoZoY_3Qj_G69ZsEycu-ooJ0BORnYPcVDBcYjmr2TbW6lOS1l-4PgnVxQBNO-uGYIv14H6C6kjMeJxHCurBMGWL0uln2Em5cgU7FvvvGAfy-9DYA5WMMGmBJVEFvT0MxZg8yrupbfoFDbhHmgPmXMo2Yeugb-spVzir_Bq5g"
    HTTP_Request_header_expired = {'x-auth-token': tokenDNAexp}
    try:
        response = requests.get(urlSimpleDNA, headers=HTTP_Request_header)
        response_error_resource = requests.get(urlSimpleDNAerror, headers=HTTP_Request_header)
        print (response.json())

        response_error_token = requests.get(urlSimpleDNA, headers=HTTP_Request_header_expired)
        if response_error_token.status_code == 401:
            print("\n response_error_token ", response_error_token.status_code)
            # catch 401 and regenarate token
        response_error_operation = requests.post(urlSimpleDNA, headers=HTTP_Request_header)
        print ("response_error_operation ", response_error_operation.status_code)
        print ("response_error_resource ", response_error_resource.status_code)
    except Timeout as e:
        raise Timeout(e)

if __name__ == "__main__":
    main()
