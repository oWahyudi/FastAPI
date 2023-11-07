from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse,PlainTextResponse
from router import blog_router,user_router,article_router,product_router
from db import dbschema ,database
from shared.customexception import StoryException


app=FastAPI()
app.include_router(blog_router.router)
app.include_router(user_router.router)
app.include_router(article_router.router)
app.include_router(product_router.router)


@app.get('/')
def index():
    return {'message': 'Index page'}

@app.exception_handler(StoryException)
def storyexception_handler(request:Request, ex: StoryException):
    return JSONResponse(status_code=418, content={'detail':ex.name})

dbschema.Base.metadata.create_all(database.engine)



