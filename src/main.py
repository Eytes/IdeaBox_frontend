from contextlib import asynccontextmanager

import flet.fastapi as flet_fastapi
from fastapi import FastAPI

from pages import main_page


@asynccontextmanager
async def lifespan(app: FastAPI):
    await flet_fastapi.app_manager.start()
    yield
    await flet_fastapi.app_manager.shutdown()


app = FastAPI(lifespan=lifespan)
app.mount("/app", flet_fastapi.app(main_page))
