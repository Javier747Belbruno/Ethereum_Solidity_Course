from brownie import SimpleStorage, accounts


def test_simple_storage():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected


def test_updating_storage():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    tx = simple_storage.store(42, {"from": account})
    tx.wait(1)
    updated_value = simple_storage.retrieve()
    expected = 42
    # Assert
    assert updated_value == expected
