from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional

app =FastAPI()

users={
    'username12':{
        'mail':'harish19',
        'password':'secret21',
    }
}

class User(BaseModel):
    mail:str
    password:str

class Update(BaseModel):
    mail: Optional[str] = None
    password: Optional[str] = None

@app.get('/')
def start_api():
    return {'welcome':'to fastapi.'}

@app.get('/search/{ur_id}')
def search_user(ur_id:str=Path(None, description='User id here.')):
    return users[ur_id]

@app.post('/registration/{ur_id}')
def registration(ur_id:str, user:User):
    if ur_id in users:
        return {'Error':'this id is already exist..'}
    else:
        users[ur_id]=user
        return users[ur_id]

@app.post('/login/{username}')
def login(mail, password):
    for i in users:
        if users[i]['mail'] != mail or users[i]['password'] != password:
            return {'error':'you entered wrong mail or password.'}
        return users[i]

@app.put('/update/{ur_id}')
def update_Userid(ur_id : str , update: Update):
    if ur_id not in users:
        return {'error':'no user exists'}

    if update.mail!=None:
        users[ur_id].mail=update.mail
    if update.password!=None:
        users[ur_id].password=update.password

    return users[ur_id]

@app.delete('/fordelete/{ur_id}')
def delete_user(ur_id:str):
    if ur_id not in users:
        return {'error':'no such user to delete..'}
    del users[ur_id]
    return {'task':'successfull'}
