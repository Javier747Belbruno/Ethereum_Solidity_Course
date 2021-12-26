[YouTube Video](https://www.youtube.com/watch?v=M576WGiDBdQ)

<br/>
<p align="center">
<a href="https://www.youtube.com/watch?v=M576WGiDBdQ" target="_blank">
<img src="./img/youtube_thumbnail.jpeg" width="350" alt="Solidity, Blockchain, and Smart Contract Course – Beginner to Expert Python Tutorial">
</a>
</p>
<br/>

Welcome to the repository for the Ultimate Solidity, Blockchain, and Smart Contract - Beginner to Expert Full Course | Python Edition FreeCodeCamp course!

# Table of Contents
- [Table of Contents](#table-of-contents)
- [Resources For This Course](#resources-for-this-course)
    - [Questions](#questions)
    - [Windows Support](#windows-support)
- [Lesson 0: Welcome To Blockchain](#lesson-0-welcome-to-blockchain)
  - [What is a Blockchain?](#what-is-a-blockchain)
  - [Making Your First Transaction](#making-your-first-transaction)
  - [How Do Blockchains Work?](#how-do-blockchains-work)
    - [Consensus](#consensus)
  - [The Future](#the-future)
  - [Miscellaneous](#miscellaneous)
- [Lesson 1: Welcome to Remix! Simple Storage](#lesson-1-welcome-to-remix-simple-storage)
    - [Everything in this section can be read about in the Solidity Documentation](#everything-in-this-section-can-be-read-about-in-the-solidity-documentation)
    - [Remix](#remix)
    - [Basic Solidity](#basic-solidity)
    - [Deploying to a "Live" network](#deploying-to-a-live-network)
- [Lesson 2: Storage Factory](#lesson-2-storage-factory)
    - [Inheritance, Factory Pattern, and Interacting with External Contracts](#inheritance-factory-pattern-and-interacting-with-external-contracts)
- [Lesson 3: Fund Me](#lesson-3-fund-me)
    - [Payable, msg.sender, msg.value, Units of Measure](#payable-msgsender-msgvalue-units-of-measure)
    - [Chainlink Oracles](#chainlink-oracles)
    - [Importing from NPM and Advanced Solidity](#importing-from-npm-and-advanced-solidity)
- [Lesson 4: Web3.py Simple Storage](#lesson-4-web3py-simple-storage)
    - [Installing VSCode, Python, and Web3](#installing-vscode-python-and-web3)
    - [Our First Python Script with Web3.py - Deploying a Contract](#our-first-python-script-with-web3py---deploying-a-contract)
    - [Interacting with Our Contract in Python & Web3.py](#interacting-with-our-contract-in-python--web3py)
- [Lesson 5: Brownie Simple Storage](#lesson-5-brownie-simple-storage)
    - [Brownie Introduction](#brownie-introduction)
    - [Installing Brownie](#installing-brownie)
    - [Brownie Simple Storage Project](#brownie-simple-storage-project)
    - [Testing Basics](#testing-basics)
    - [[Brownie console]](#brownie-console)
- [Lesson 6: Brownie Fund Me](#lesson-6-brownie-fund-me)
    - [Introduction](#introduction)
    - [Dependencies, Deploying, and Networks](#dependencies-deploying-and-networks)
    - [Funding and Withdrawing Python Scripts](#funding-and-withdrawing-python-scripts)
    - [Testing across networks](#testing-across-networks)
    - [Git](#git)
- [Lesson 7: SmartContract Lottery](#lesson-7-smartcontract-lottery)
    - [Introduction](#introduction-1)
    - [`Lottery.sol`](#lotterysol)
    - [Testing Lottery.sol](#testing-lotterysol)
    - [Lottery.sol Testnet Deployment](#lotterysol-testnet-deployment)
- [Lesson 8: Chainlink Mix](#lesson-8-chainlink-mix)
  - [Brownie Mixes](#brownie-mixes)
- [Lesson 9: ERC20s, EIPs, and Token Standards](#lesson-9-erc20s-eips-and-token-standards)
- [Lesson 10: Defi & Aave](#lesson-10-defi--aave)
    - [Defi Intro](#defi-intro)
    - [Aave UI](#aave-ui)
    - [Programmatic Interactions with Aave](#programmatic-interactions-with-aave)
    - [Testing](#testing)
- [Lesson 11: NFTs](#lesson-11-nfts)
    - [Non-Technical Explainer](#non-technical-explainer)
    - [Simple NFT](#simple-nft)
    - [SimpleCollectible Testing](#simplecollectible-testing)
    - [Advanced NFT](#advanced-nft)
    - [Advanced deploy_and_create](#advanced-deploy_and_create)
    - [Creating Metadata & IPFS](#creating-metadata--ipfs)
- [Lesson 12: Upgrades](#lesson-12-upgrades)
    - [Introduction to upgrading smart contracts](#introduction-to-upgrading-smart-contracts)
    - [Upgrades-mix and code](#upgrades-mix-and-code)
    - [Testing Upgrades](#testing-upgrades)
    - [Upgrades on a testnet](#upgrades-on-a-testnet)
- [Bonus Lesson 13: Full Stack Defi](#bonus-lesson-13-full-stack-defi)
    - [Defi Stake Yield Brownie Scripts & Tests](#defi-stake-yield-brownie-scripts--tests)
    - [Testing our Defi Stake Yield Brownie Dapp](#testing-our-defi-stake-yield-brownie-dapp)
    - [Front End / Full Stack](#front-end--full-stack)
- [Closing and Summary](#closing-and-summary)
  - [Security](#security)
  - [Where do I go now?](#where-do-i-go-now)
    - [Learning More](#learning-more)
    - [Community](#community)
    - [Hackathons](#hackathons)

# Resources For This Course
### Questions
- [Github Discussions](https://github.com/smartcontractkit/full-blockchain-solidity-course-py/discussions)
  - Ask questions and chat about the course here!
- [Stack Exchange Ethereum](https://ethereum.stackexchange.com/)
  - Great place for asking technical questions about Ethereum
- [StackOverflow](https://stackoverflow.com/)
  - Great place for asking technical questions overall

### Windows Support
- [Setup your windows environment](https://medium.com/@cromewar/how-to-setup-windows-10-11-for-smart-contract-development-and-brownie-e7d8d13555b3)
  - Learn how to install all the tools you will need for this course on a windows machine

# Lesson 0: Welcome To Blockchain
## What is a Blockchain?
- [Bitcoin Whitepaper](https://bitcoin.org/bitcoin.pdf)
- [Ethereum Whitepaper](https://ethereum.org/en/whitepaper/)
- [Hybrid Smart Contracts](https://blog.chain.link/hybrid-smart-contracts-explained/)
- [Blockchain Oracles](https://betterprogramming.pub/what-is-a-blockchain-oracle-f5ccab8dbd72?source=friends_link&sk=d921a38466df8a9176ed8dd767d8c77d)
- [What is a blockchain](https://www.investopedia.com/terms/b/blockchain.asp)
## Making Your First Transaction
- [Metamask](https://metamask.io/)
- [Etherscan](https://etherscan.io/)
- [Rinkeby Etherscan](https://rinkeby.etherscan.io/)
- [Kovan Etherscan](https://kovan.etherscan.io/)
- Rinkeby Faucet (Check the [link token contracts page](https://docs.chain.link/docs/link-token-contracts/#rinkeby))
  - NOTE: The Chainlink documentation always has the most up to date faucets on their [link token contracts page](https://docs.chain.link/docs/link-token-contracts/#rinkeby). If the faucet above is broken, check the chainlink documentation for the most up to date faucet.  
- OR, use the [Kovan ETH Faucet](https://faucets.chain.link/), just be sure to swap your metamask to kovan!
- [Gas and Gas Fees](https://ethereum.org/en/developers/docs/gas/)
- [Wei, Gwei, and Ether Converter](https://eth-converter.com/)
- [ETH Gas Station](https://ethgasstation.info/)
## How Do Blockchains Work? 
- [Blockchain Demo](https://andersbrownworth.com/blockchain/)
- [Public / Private Keys](https://andersbrownworth.com/blockchain/public-private-keys/keys)
- [Layer 2 and Rollups](https://ethereum.org/en/developers/docs/scaling/layer-2-rollups/)
- [Decentralized Blockchain Oracles](https://blog.chain.link/what-is-the-blockchain-oracle-problem/)
- [Block Rewards](https://www.investopedia.com/terms/b/block-reward.asp)
- [Run Your Own Ethereum Node](https://geth.ethereum.org/docs/getting-started)
### Consensus
- [Consensus](https://wiki.polkadot.network/docs/learn-consensus)
- [Proof of Stake](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/)
- [Proof of Work](https://ethereum.org/en/developers/docs/consensus-mechanisms/pow/)
- [Nakamoto Consensus](https://blockonomi.com/nakamoto-consensus/)
## The Future
- [Ethereum 2](https://ethereum.org/en/eth2/)
## Miscellaneous 
- [DAOs](https://www.investopedia.com/tech/what-dao/)