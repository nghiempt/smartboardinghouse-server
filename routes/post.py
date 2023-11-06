from fastapi import APIRouter, Query
from models._index import post, ResponseObject
from config.db import conn
from schemas._index import Post
import http.client as HTTP_STATUS_CODE

postRouter = APIRouter(prefix="/api/v1")

@postRouter.get('/post/all')
async def get_all_posts():
    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, Post.serializeList(conn.execute(post.select()).fetchall()))

@postRouter.post('/post/create')
async def create_post(postInput: Post):
    conn.execute(post.insert().values(
        title=postInput.title,
        content=postInput.content,
        location=postInput.location,
        lat=postInput.lat,
        long=postInput.long,
        image=postInput.image,
        account_id=postInput.account_id,  
    ))
    conn.commit()
    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, Post.serializeList(conn.execute(post.select().where(post.c.account_id == postInput.account_id)).fetchall()))

@postRouter.get('/post/filter')
async def filter_posts_by_location(location: str = Query(..., description="Location to filter posts")):
    # Query the database to get posts that match the specified location
    posts = conn.execute(post.select().where(post.c.location == location)).fetchall()

    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]

    if not posts:
        status_code = HTTP_STATUS_CODE.NOT_FOUND
        status_message = HTTP_STATUS_CODE.responses[status_code]
        return ResponseObject(False, status_code, status_message, "No posts found for the specified location")

    return ResponseObject(True, status_code, status_message, Post.serializeList(posts))
