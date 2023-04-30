---
draft: false
date: 2024-04-11
title: Never Get Hacked
categories:
    - Bitcoin
---

# How to secure your Bitcoin from active attackers: Electrum Server

![](/assets/electrum/bitcoin_vault.png)

The moment you decide to take [self-custody](./self_custody.md) of your Bitcoin, you become your own bank. To safeguard your assets requires understanding basic security, recognizing potential risks, and implementing protective measures against hackers.

$500 worth of BTC might not necessitate the strongest vault, the need for stringent security grows alongside your assets. Initially, you might find yourself connecting to a public Electrum server. This is a significant first step away from relying on centralized exchanges (E.g., Mt.Gox 2014, Bitfinex 2016, QuadrigaCX 2019, Cryptopia 2019, FCoin 2020, OKEx 2020, Thodex 2021, FTX 2022!!!). So you should pat yourself on the back if you have started offloading your assets from CEX. However, using a public Electrum server poses several risks:

1) **Privacy Exposure**: Public servers can potentially log and monitor your transactions and IP addresses. This opens up the possibility for malicious actors to trace transactions back to your wallet and possibly to your real-world identity.

2) **Security Risk**: There's a risk that the server could present you with incorrect information, misleading you about the status of your transactions or balance.


## Level 1 (Beginner) - Public Electrum Server

Most people start by connecting to a public Electrum server. This approach is manageable with a small amount of Bitcoin. However, it's important to understand that at this stage, your transaction details and IP address are not private. The risk of you becoming a target for attackers increases as your asset value grows.


## Level 2 - (Intermediate) Bitcoin Core

Those who grasp the risks associated with exposing their IP address and asset holdings often consider running a Bitcoin Core node. This represents the most significant step up in security against passive attackers, as your transactions won't be accessible to others. The primary function of a Bitcoin Core node is to validate transactions locally, ensuring that no transaction details leak. Additionally, by running a node, you contribute to the decentralization of the Bitcoin network. In short, you should run your node. As the motto goes: 

!!!quote
    "Not your node, not your rules".

The ethos of Bitcoin is to not be ruled by rulers (Feds, Central Bank or anyone who has access to the money printer), but ruled by rules. Without running a Bitcoin node yourself, this can never be possible. Plus, running a Bitcoin Node is the most direct way to start appreciating why Bitcoin is greater than anything that comes afterward.

!!!quote
    "Imitation is the sincerest form of flattery that mediocrity can pay to greatness." (Oscar Wilde)

## Level 3 (EXPERT LEVEL) Private Electrum Server

Upon accumulating a significant amount of Bitcoin, and rightly growing more security-conscious, it's time to consider protection against active attackers. Many places recommend doing this step if the asset value is greater than $100,000, I recommend my friends to do this step if greater than $50,000 because I am extra risk aversed. While running a Bitcoin Core node shields your transactions from public view, it doesn't protect your public keys and balances. A common concern of Bitcoin Core is that it, while secure, stores your public keys and balances unencrypted. This poses a risk if the device you use for self-custody is frequently connected to the internet, exposing it to potential hacker attacks.


### How Electrum Server works

A private Electrum server allows you to enjoy all the benefits (doing validation yourself and securing your transactions) of running a Bitcoin Core node while also providing an additional layer of security for your wallet's sensitive information. An electrum server achieves this by imposing an address level indexing over transactions. That is: provided with an arbitrary address, the server will return transactions associated with that particular address only. This is something that Bitcoin Core implementation isn't able to do. 

Architecturally, an electrum server acts as a middle layer between the wallet (e.g., Sparrow) and the Bitcoin Core. It is important to note that **full** address is extremely important because only full address indexing ensures no information about the wallet is stored on the hardware. This characteristic is what makes level 3 level 3. Any true cold storage methods should never have wallet information leaked outside of the wallet file.

### Tutorial

In the following sections, we will explore the steps to set up your own private Electrum server, ensuring your Bitcoin holdings are secured against both passive and active threats. This tutorial is for Mac users only. (With enough interest, I might write one for the other OS, DM me pls if you need help). 

#### Requirement

You have a Bitcoin Core running. Read [here](https://bitcoin.org/en/full-node#mac-os-x-instructions) if you don't know how to get a Bitcoin Core node running.

#### Electrs

There are three popular Electrum server implementations:

- ElectrumX: great for public server use, not as great for personal use.
- Electrs: I recommend Electrs. It is written in Rust, very clean code. 
- Fulcrum: written in C++, very performant, but supports Shitcoins so I don't recommend Fulcrum.

I recommend Electrs over Fulcrum and ElectrumX. To set up Electrs on Mac, it took me about 10 minutes to start the process and waited for about 12 hours for the indexing to complete as of April 2024 (with the current Bitcoin blockchain size at about 500+ GB, and 33+ GB extra storage space for indexing).


Make sure homebrew is installed:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Install Rust

```bash
brew install rust
```

Make sure Bitcoin Core is synced to the tip (latest block).


Clone the `electrs` repo

```bash
git clone https://github.com/romanz/electrs.git
cd electrs
```

Compile `electrs` using Cargo, rust's package manager.

```bash
cargo build --release
```

Run `electrs`  by passing in the bitcoind directory path. 

```bash
cargo run --release --bin electrs -- --bitcoind-dir=YOUR-BICOIND-DATA-FILE-PATH
```

Assume you have Bitcoin Core synced to the latest, and everything installed properly, the last step should take about 12-16 hours (depending on how performant your computer is) to finish the indexing.

The only issue that I have encountered while setting up `eletrs` on my old Mac book is I had to increase the open file limit to have `electrs` finish its DB compaction step. I have run:

```bash
nlimit -n 1024
```
to set the limit on the number of open files that a process can have at any one time. 

Without this step, the DB compaction step on Mac would fail. More details can be found on this GitHub [issue](https://github.com/romanz/electrs/issues/918).


#### Help

Setting up a private Electrum server with Bitcoin Core will give you maximum privacy and security. The process took me a day to finish (most time is spent waiting for the indexing to be completed). DM me if you need help or submit an issue [here](https://github.com/btc-z/btc-z.github.io/issues).  


















