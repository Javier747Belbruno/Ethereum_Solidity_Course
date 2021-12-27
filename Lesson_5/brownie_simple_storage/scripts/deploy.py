from brownie import accounts, SimpleStorage


def deploy_simple_storage():
    simple_storage = SimpleStorage.deploy({"from": accounts[0]})
    stored_value = simple_storage.retrieve()
    print("The stored value is: {}".format(stored_value))
    # Update
    tx = simple_storage.store(42, {"from": accounts[0]})
    tx.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print("The updated stored value is: {}".format(updated_stored_value))


def main():
    deploy_simple_storage()
