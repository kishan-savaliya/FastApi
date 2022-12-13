from fastapi import FastAPI
from app.Routes.user_route import user
from app.Routes.competition_route import competition
from app.Routes.entry_route import entry

app = FastAPI()

app.include_router(user)
app.include_router(competition)
app.include_router(entry)
