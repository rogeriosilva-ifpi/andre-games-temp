from fastapi import FastAPI

app = FastAPI()

jogos = [
  {'nome': 'Hollow Knight', 'genero': 'Ação'},
  {'nome': 'MineCraft', 'genero': 'Aventura'},
]

@app.get('/games')
def list_games():
  return jogos