from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users={
    'brocode':{
        'mail':'secret@gmail',
        'password':'123'
    }
}

#only for developer
@app.get('/')
def user_list():
    return users

@app.get('/search')
def search_username(username):
    if username not in users:
        return {'error':'this user is not exist.'}
    else:
        return users[username]

@app.post('/registration/{username}')
def registration(username,mail,password):
    for i in users:
        if i==username:
            return {'error':'this user name is used try another one.'}
        elif users[i]['mail']==mail:
            return {'error':'this mail is be used try another one.'}
        else:
            users[i]['mail']=mail
            users[i]['password']=password
            return users[i]



@app.post('/login/{username}')
def login(mail, password):
    for i in users:
        if users[i]['mail'] != mail or users[i]['password'] != password:
            return {'error':'you entered wrong mail or password.'}
        return users[i]
