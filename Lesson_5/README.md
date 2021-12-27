# Lesson 5: [Brownie Simple Storage](https://github.com/PatrickAlphaC/brownie_simple_storage)
💻 Code: https://github.com/PatrickAlphaC/brownie_simple_storage
### Brownie Introduction
- Some Users:
  - https://yearn.finance/
  - https://curve.fi/
  - https://badger.finance/
### Installing Brownie
- [Installing Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html)
  - Install pipx
    - python -m pip install --user pipx
    - python -m pipx ensurepath

  - pipx install eth-brownie
  - Testing Successful Install

  On Windows:
  - `C:\Users\User\.local\pipx\venvs\eth-brownie\Scripts\activate.bat`
  
### Brownie Simple Storage Project
- A new Brownie project with `brownie init`
  - Project Basic Explanation
- Adding `SimpleStorage.sol` to the `contracts` folder
- Compiling with `brownie compile`
- Brownie deploy script
  - `def main` is brownie's entry point
- brownie defaults to a `development` `ganache` chain that it creates
- Placing functions outside of the `main` function
- brownie `accounts`
  - 3 Ways to Add Accounts
    1. `accounts[0]`: Brownie's "default" ganache accounts
       - Only works for local ganache 
    2. `accounts.load("...")`: Brownie's encrypted command line (MOST SECURE)
       - Run `brownie accounts new <name>` and enter your private key and a password
    3. `accounts.add(config["wallets"]["from_key"])`: Storing Private Keys as an environment variable, and pulling from our `brownie-config.yaml`
        - You'll need to add `dotenv: .env` to your `brownie-config.yaml` and have a `.env` file
- Importing a Contract
- Contract.Deploy
- View Function Call in Brownie
- State-Changing Function Call in Brownie / Contract Interaction
- `transaction.wait(1)`
### Testing Basics
- `test_simple_storage.py`
- Arrange, Act, Assert
- [`assert`](https://docs.pytest.org/en/6.2.x/assert.html)
- `brownie test`
- `test_updating_storage`
- [Pytest / Brownie Test Tips](https://docs.pytest.org/en/6.2.x/)
- Deploy to a Testnet
- `brownie networks list`
- Development vs Ethereum
  - Development is temporary
  - Ethereum networks persist
- RPC URL / HTTP Provider in Brownie
- The network flag
  - `list index out of range`
- `get_account()`
- `networks.show_active()`
- build/deployments
- Accessing previous deployments
- Interacting with contracts deployed in our brownie project
### [Brownie console]
- `brownie console`
