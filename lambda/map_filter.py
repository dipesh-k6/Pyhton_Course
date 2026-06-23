posts = [
    {"title": "AI", "likes": 15},
    {"title": "Django", "likes": 42},
    {"title": "Python", "likes": 7},
    {"title": "React", "likes": 30},
]

filter_likes = list(filter(lambda post: post.get("likes")>20, posts))
titles = list(map(lambda post: post.get("title"), posts))

print(filter_likes)
print(titles)