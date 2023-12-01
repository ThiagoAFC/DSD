# main.py

from fastapi import FastAPI
from app.routers import users, posts, comments, likes, messages

app = FastAPI()

# Configurar as rotas
app.include_router(users.router, prefix="/api", tags=["users"])
app.include_router(posts.router, prefix="/api", tags=["posts"])
app.include_router(comments.router, prefix="/api", tags=["comments"])
app.include_router(likes.router, prefix="/api", tags=["likes"])
app.include_router(messages.router, prefix="/api", tags=["messages"])

if __name__ == "__main__":
    import uvicorn

    # Iniciar o servidor com Uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
