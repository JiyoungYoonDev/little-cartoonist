from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1 import auth, children, teachers, themes, projects, pages, strokes, assists, conversations, stories, comics

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}


# Auth
app.include_router(auth.router, prefix=settings.API_V1_PREFIX)

# Children
app.include_router(children.router, prefix=settings.API_V1_PREFIX)

# Teachers
app.include_router(teachers.router, prefix=settings.API_V1_PREFIX)

# Themes
app.include_router(themes.router, prefix=settings.API_V1_PREFIX)

# Projects
app.include_router(projects.router, prefix=settings.API_V1_PREFIX)

# Pages
app.include_router(pages.router, prefix=settings.API_V1_PREFIX)

# Strokes
app.include_router(strokes.router, prefix=settings.API_V1_PREFIX)

# Assist
app.include_router(assists.router, prefix=settings.API_V1_PREFIX)

# Conversations
app.include_router(conversations.router, prefix=settings.API_V1_PREFIX)

# Stories
app.include_router(stories.router, prefix=settings.API_V1_PREFIX)

# Comics
app.include_router(comics.router, prefix=settings.API_V1_PREFIX)
