from pydialogflow_fulfillment import DialogflowResponse
from pydialogflow_fulfillment import SimpleResponse, Confirmation, OutputContexts, Suggestions

CONTEXT_ASK_PROGRAMME = "GetGraduateProgrammeFee-ask-programme"
DATA_FILE = "data/GetGraduateProgrammeFee.json"

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
    if has_params("graduate-programme", params):
        return askProgramme(req)
    
    application_group = params["application_group"]
    graduate_programme = params["graduate-programme"]


    res = DialogflowResponse("will look up file and return")
    print(res.get_final_response())
    return res.get_final_response()
