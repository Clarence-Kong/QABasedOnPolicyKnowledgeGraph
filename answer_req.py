# -*- coding: utf-8 -*-
# Author: Clarence Kong<clarencekong@qq.com,https://github.com/Clarence-Kong>
# @Time: 4/29/2021 8:59 AM
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from chatbot_graph import ChatBotGraph

# hand = ChatBotGraph()
app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:3002",
    "http://localhost:3003",
    "http://localhost:20230",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class People(BaseModel):
    name: str
    age: int
    address: str
    salary: float


class Answer(BaseModel):
    answer: str


@app.post('/insert')
def insert(people: People):
    age_after_10_years = people.age + 10
    msg = f'此人名字叫做：{people.name}，十年后此人年龄：{age_after_10_years}'
    return {'success': True, 'msg': msg} @ app.post('/insert')


@app.get('/que/{que}')
def answer(que: str):
    hand = ChatBotGraph()
    # ans = ChatBotGraph.chat_main(que)
    ans = hand.chat_main(que)
    msg = f'ans'
    print('ask: ',que)
    print('ans: ',ans)
    return {'success': True, 'msg': ','.join(ans.split('\n'))}


if __name__ == '__main__':
    uvicorn.run(app='answer_req:app', port=20230)