from fastapi import FastAPI
from router import blog_router,user_router
from db import dbschema ,database


app=FastAPI()
app.include_router(blog_router.router)
app.include_router(user_router.router)


@app.get('/')
def index():
    return {'message': 'Index page'}

dbschema.Base.metadata.create_all(database.engine)



