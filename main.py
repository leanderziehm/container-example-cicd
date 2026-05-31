from Fastapi import FastAPI # does capitalization matter in python?
# todo add cors

app = FastAPI()

count = 0

@app.get("/")
def index():
  global count
  count += 1
  return count
