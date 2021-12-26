- python -m venv env
- .\env\Scripts\activate.bat 
- pip install py-solc-x
- pip install web3

- npm install -g yarn
- yarn global add ganache-cli

# Lesson 4: [Web3.py Simple Storage](https://github.com/PatrickAlphaC/web3_py_simple_storage)
💻 Code: https://github.com/PatrickAlphaC/web3_py_simple_storage
### Installing VSCode, Python, and Web3
- [Developer Bootcamp Setup Instructions (metamask, vscode, python, nodejs..)](https://chain.link/bootcamp/brownie-setup-instructions)
- [VSCode](https://code.visualstudio.com/download)
- [VSCode Crash Course](https://www.youtube.com/watch?v=WPqXP_kLzpo)
- Extensions
- Short Cuts:
  - [VSCode Shortcuts](https://code.visualstudio.com/docs/getstarted/keybindings)
  - [VSCode MacOS Shortcuts](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf)
- [Python](https://www.python.org/downloads/)
  - Install Troubleshooting
- Terminal
- Making a directory/Folder
- Opening the folder up with VSCode
- Creating a new file
- Syntax Highlights
- Remember to save!
- Setting linting compile version
- VSCode Solidity Settings
  - Formatting & Format on Save
  - Solidity Prettier
  - [Python Black](https://pypi.org/project/black/)
  - [pip](https://pypi.org/project/pip/)
### Our First Python Script with Web3.py - Deploying a Contract
- Reading our solidity file
- Running a Python Script in the Terminal
- [MaxOS Shortcuts](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf)
- [Windows Shortcuts](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)
- [Linux Shortcuts](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-linux.pdf)
- Compiling in Python
- [py-solc-x](https://pypi.org/project/py-solc-x/)
  - compile_standard
- Colorized Brackets
- JSON ABI 
- Saving Compiled Code
- Formatting JSON
- Deploying in Python
  1. Get Bytecode
  2. Get ABI
  3. Choose Blockchain to Deploy To
    - Local Ganache Chain
      - [Ganache UI](https://www.trufflesuite.com/ganache)
      - [Ganache Command Line](https://github.com/trufflesuite/ganache-cli)
- [Web3.py](https://web3py.readthedocs.io/en/stable/)
- HTTP / RPC Provider
- Private Keys MUST start with "0x"
- Contract Object
- Building a Transaction
- Account Nonce 
- Calling "Contructor"
- Transaction Parameters
- Signing the Transaction
- NEVER put your private key directly in your code
- [Setting Environment Variables (Windows, Linux, MacOS)](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html)
  - [More on Windows Environment Variables](https://www.youtube.com/watch?v=tqWDiu8a4gc&t=40s)
- Exported Environment Variables Only Last the Duration of the Shell/Terminal
- Private Key PSA
- .env file
- .gitignore
- Loading .env File in Python
  - [python-dotenv](https://pypi.org/project/python-dotenv/)
- Viewing our Transaction / Deployment in Ganache
- Waiting for Block Confirmations
### Interacting with Our Contract in Python & Web3.py
- 2 Things you always need
  1. Contract Address
  2. Contract ABI
- Getting address from transaction receipt
- Calling a view function with web3.py
  - Call vs Transact
- Updating State with Web3.py
- [ganache-cli](https://github.com/trufflesuite/ganache-cli)
  - Installing Ganache
    - [Install Nodejs](https://nodejs.org/en/)
    - [Install Yarn](https://classic.yarnpkg.com/en/docs/install)
- Working with ganache-cli
- Open a new terminal in the same window
- Deploying to a testnet
- [Infura](https://infura.io/)
- [Alchemy](https://www.alchemy.com/)
- Using Infura RPC URL / HTTP Provider
- [Chain Ids](https://chainlist.org/)
- Wow this seems like a lot of work... Is there a better way?
