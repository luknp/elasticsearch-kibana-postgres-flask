from fastapi import FastAPI
from datetime import datetime

from fastapi.responses import RedirectResponse
from config import DATABASE_URL, ELASTICSEARCH_URL
import databases
from elasticsearch import AsyncElasticsearch

database = databases.Database(DATABASE_URL)
es = AsyncElasticsearch(ELASTICSEARCH_URL)



app = FastAPI(title="OoD - Cloud FastAPI")



@app.on_event("startup")
async def startup_event():
    await database.connect()
    
    

@app.on_event("shutdown")
async def shutdown_event():
    await database.disconnect()
    await es.close()


@app.get("/")
async def docs_redirect():
    return RedirectResponse(url="/docs")


@app.get("/healthcheck", tags=["public"])
def healthcheck():
    message = "alive and kicking"
    response = {
        "message": message,
        "time": datetime.utcnow(),
    }
    return response

@app.get('/db/all', tags=["database"])
async def get_rows():
    output = await database.fetch_all("select * from games limit 100")
    return output


@app.get("/es/healthcheck", tags=["elastisearch"])
async def index():
    output = await es.cluster.health()
    return output

@app.get("/es/all", tags=["elastisearch"])
async def get_all():
    output = await es.search(index="games", body={"size": 100, "query": {"match_all": {}}})
    return output

@app.get("/es/{id}", tags=["elastisearch"])
async def get_one(id: int):
    output = await es.get(index="games", id=id)
    return output