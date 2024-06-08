import flet as ft

from modules.idea_box_app import IdeaBoxApp


async def index_view(page: ft.Page):
    page.title = "IdeaBox"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE
    await page.add_async(IdeaBoxApp())
