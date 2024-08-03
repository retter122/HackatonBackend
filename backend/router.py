from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .user.router import router as user_router
from .tutorial.router import router as tutorial_router
from .modules.router import router as module_router
from .comments.router import router as comment_router
from .tags.router import router as tag_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router)
app.include_router(tutorial_router)
app.include_router(module_router)
app.include_router(comment_router)
app.include_router(tag_router)
