from lib.post import Post

"""
Post constructs with an id, title, contents, views and user_id
"""
def test_post_constructs():
    post = Post(1, 'Test Title', 'Test Contents', 30, 1)
    assert post.id == 1
    assert post.title == "Test Title"
    assert post.contents == "Test Contents"
    assert post.views == 30
    assert post.user_id == 1

"""
We can format posts to strings nicely
"""
def test_posts_format_nicely():
    post = Post(1, 'Test Title', 'Test Contents', 30, 1)
    assert str(post) == "Post(1, Test Title, Test Contents, 30, 1)"

"""
We can compare two identical posts
And have them be equal
"""
def test_posts_are_equal():
    post1 = Post(1, 'Test Title', 'Test Contents', 30, 1)
    post2 = Post(1, 'Test Title', 'Test Contents', 30, 1)
    assert post1 == post2