from lib.user_repository import UserRepository
from lib.user import User

"""
When we call UserRepository#all
We get a list of Artist objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = UserRepository(db_connection) # Create a new UserRepository

    users = repository.all() # Get all users

    # Assert on the results
    assert users == [
        User(1, "email@test.com", "Test Username"),
    ]

"""
When we call UserRepository#find
We get a single User object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)

    user = repository.find(1)
    assert user == User(1, "email@test.com", "Test Username")

"""
When we call UserRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)

    repository.create(User(2, "email2@test.com", "Test Username 2"))

    result = repository.all()
    assert result == [
        User(1, "email@test.com", "Test Username"),
        User(2, "email2@test.com", "Test Username 2"),
    ]

"""
When we call UserRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    repository.delete(1) 

    result = repository.all()
    assert result == [

    ]