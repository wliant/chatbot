from pydialogflow_fulfillment import DialogflowResponse
from pydialogflow_fulfillment import SimpleResponse, Confirmation, OutputContexts, Suggestions
import json

CONTEXT_ASK_PROGRAMME = "GetGraduateProgrammeFee-ask-programme"
DATA_FILE = "data/GetGraduateProgrammeFee.json"

with open(DATA_FILE, 'r') as infile:
    data = json.load(infile)

def has_params(theKey, params):
    return theKey in params and params[theKey] != ""

def askProgramme(req):
    res = DialogflowResponse("What is the graduate programme you are looking at?")
    res.add(OutputContexts(req.get_project_id(), req.get_session_id(),CONTEXT_ASK_PROGRAMME,5,req.get_paramters()))
    print(res.get_final_response())
    return res.get_final_response()

def process(req):
    params = req.get_paramters()
    print(params)
    #if has_params("graduate-programme", params):
    #    return askProgramme(req)
    
    application_group = "" if "application-group" not in params else params["application-group"] 
    graduate_programme = "" if "graduate-programme" not in params else params["graduate-programme"]

    result = [item["answer"] for item in data 
                    if item["graduate-programme"] == graduate_programme 
                        and item["application-group"] == application_group]

    if len(result) == 0:
        return DialogflowResponse("Unknown programme {0}".format(graduate_programme)).get_final_response()
    return DialogflowResponse("The programme fee is {0}".format(result[0])).get_final_response()