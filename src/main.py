import os

import flet.fastapi as flet_fastapi

from views.index import index_view

app = flet_fastapi.app(index_view, assets_dir=os.path.abspath("assets"))
