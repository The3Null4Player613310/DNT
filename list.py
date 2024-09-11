################################################################
#DNT: list.py
#Copyright © 2024 Allison Munn
#FULL COPYRIGHT NOTICE IS IN README
################################################################

import sys
#from oauth2client import client as cl;
import httplib2 as hlib;
from oauth2 import service_account as sa;

PACKAGE = "com.thenullplayer.dnt"
URL = "https://www.googleapis.com/auth/androidpublisher";
SAE = "";
KEY = "";
SAI = "";

def main():

    args = argv[1:];
    
    for i in range(len(args)):
        val = args[i];
        if (val[0:1] == "-"):
            if (val[0:2] == "--"):
                match val:
                    case "--sae":
                        SAE = args[i+1];
                        break;
                    case "--key":
                        KEY = args[i+1];
                        break;
                     case "--sai":
                        SAI = args[i+1];
                        break;
            else:
                for v in val:
                    match v:
                        case "s":
                             SAE = args[i+1];
                             args = args[0:i] + args[i+1:];
                             break;
                        case "k":
                             KEY = args[i+1];
                             args = args[0:i] + args[i+1:];
                             break;
                         case "i":
                             SAI = args[i+1];
                             args = args[0:i] + args[i+1:];
                             break;

    print("LIST:");
    
    #get service account info
    sa_info = json.load(SAI)
    
    #setup credentials
    cred = sa.Credentials.from_service_account_info(sa_info, scopes=[URL])
    
    #setup credentials # old
    #cred = cl.SignedJwtAssertionCredentials(SAE, KEY, scope=URL);
    
    #setup http
    http = hlib.Http();
    #http = cred.authorize(http);
    
    cred.apply(http);
    
    #setup service
    service = build("androidpublisher", "v3", http=http);
    
    try:
        edit_request = service.edits().insert(body={}, packageName=PACKAGE);
        print(edit_request);
        
        result = edit_request.execute();
        print(result);
        
    except GoogleAuthError:
        print("Token Error");
    
    return 0;

if __name__ == "__main__":
    main();