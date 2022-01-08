from pymongo.database import Database


def test_mongodb_version(mongodb: Database) -> None:
    """Test that the version of MongoDB used for testing is within tollerance."""
    minimum_version = (3, 0, 0)
    values = mongodb.client.server_info()["version"].split(".")

    actual_version = tuple(map(int, values))  # Act

    assert minimum_version <= actual_version
