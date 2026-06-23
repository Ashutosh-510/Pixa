from fastapi import FastAPI
app = FastAPI()

text_posts = {
    1: {"title": "Post 1", "content": "Content of post 1"},
    2: {"title": "Post 2", "content": "Content of post 2"},
    3: {"title": "Post 3", "content": "Content of post 3"},
    4: {"title": "Post 4", "content": "Content of post 4"},
}

@app.get('/posts')
def get_posts():
    return text_posts

#get post by id
@app.get('/post/{post_id}')
def get_postID(post_id: int):
    if post_id not in text_posts:
        return {"error": "Post not found"}
    return text_posts[post_id]

#query parameters
@app.get('/posts')
def get_posts_with_query(skip:int=1 , limit:int=1):
    return list(text_posts.values())[skip: skip + limit]
