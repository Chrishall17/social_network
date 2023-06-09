from lib.post_repository import PostRepository
from lib.post import Post

"""
When we call PostRepository#all
We get a list of Post objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = PostRepository(db_connection) # Create a new PostRepository

    posts = repository.all() # Get all users

    # Assert on the results
    assert posts == [
        Post(1, 'Test Title', 'Test Contents', 30, 1),
    ]

"""
When we call PostRepository#find
We get a single Post object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    post = repository.find(1)
    assert post == Post(1, 'Test Title', 'Test Contents', 30, 1)

"""
When we call PostRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    repository.create(Post(2, 'Test Title 2', 'Test Contents 2', 32, 1))

    result = repository.all()
    assert result == [
        Post(1, 'Test Title', 'Test Contents', 30, 1),
        Post(2, 'Test Title 2', 'Test Contents 2', 32, 1),
    ]

"""
When we call PostRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    repository.delete(1) 

    result = repository.all()
    assert result == [

    ]