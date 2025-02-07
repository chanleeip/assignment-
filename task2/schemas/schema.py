from pydantic import BaseModel,model_validator,Field,ValidationError,HttpUrl
from pydantic_core import ErrorDetails
from typing import Dict,List,Optional



CUSTOM_MESSAGES = {
    'value_error': 'Refer Docs for available values !!!',
    'url_scheme': 'Check Docs',
    'missing':'Bruhh check the docs'
}

def convert_errors(
    e: ValidationError, custom_messages: Dict[str, str]
) -> List[ErrorDetails]:
    new_errors: List[ErrorDetails] = []
    for error in e.errors():
        custom_message = custom_messages.get(error['type'])
        if custom_message:
            ctx = error.get('ctx')
            error['msg'] = (
                custom_message.format(**ctx) if ctx else custom_message
            )
        if "ctx" in error and "error" in error["ctx"]:
            error["ctx"]["error"] = str(error["ctx"]["error"])
        print(error,"jeds\n")
        new_errors.append(error)

    return new_errors


    
class AuthResponseModel(BaseModel):
    token:str=None
    expiry_time:int=None
    error:str=None

class AuthRequesteModel(BaseModel):
    username:str
    password:str
    role:Optional[str]="user"

