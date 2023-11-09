from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse,PlainTextResponse
from router import blog_router,user_router,article_router,product_router
from auth import authentication_router
from db import dbschema ,database
from shared.customexception import StoryException
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI Application
app=FastAPI()


# Include the routers for various parts of the application.
app.include_router(authentication_router.router)
app.include_router(blog_router.router)
app.include_router(user_router.router)
app.include_router(article_router.router)
app.include_router(product_router.router)



@app.get('/')
def index():
    return {'message': 'Index page'}

# Define custom exception handler
@app.exception_handler(StoryException)
def storyexception_handler(request:Request, ex: StoryException):
    return JSONResponse(status_code=418, content={'detail':ex.name})

dbschema.Base.metadata.create_all(database.engine)


# Define the list of allowed origins
origins=[
    'http://localhost:3000'
]

# Configure and add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)


# Start your FastAPI application
#if __name__ == "__main__":
#    import uvicorn
#    uvicorn.run(app, host="0.0.0.0", port=8000)

