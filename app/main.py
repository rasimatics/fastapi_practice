from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from app.users.routes import user_routes
from app.posts.endpoints.category import category_routes
from app.posts.endpoints.post import post_routes


app = FastAPI()


@app.get('/')
def index():
    return {'detail':'FastApi example. Go to /docs to see all endpoints'}


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


app.add_middleware(SessionMiddleware, secret_key='secret')


app.include_router(user_routes)
app.include_router(category_routes)
app.include_router(post_routes)

