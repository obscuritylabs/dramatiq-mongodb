from dramatiq_mongodb import __version__


def test_version() -> None:
    """Tests that the version is accessible and locked to a specific number.

    This test will be removed when real tests are added.
    """
    assert __version__ == "0.1.0"  # Act
