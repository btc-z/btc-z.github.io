---
draft: true
title: A Brief Guide to Bitcoin Self Custody
date: 2024-02-09
categories:
  - Bitcoin
---

## Motivation

The question of "who can control money and who can control its issuance" is not a technical question but an ethical one. People who control money also control life and death.

To share my favorite quote from the [Inalienable Property Rights](https://dergigi.com/2022/04/03/inalienable-property-rights/):

!!!quote
    This is neither hard to see nor hard to understand: if you can dictate who gets the money, you can dictate who is well off and who is not. If you can decide who is allowed to create new money, you can decide who has to work for money and who gets it unjustly, with the stroke of a pen or the push of a button.2 If you can control the flow of money, you can decide who can pay, who can get paid, who can withdraw, who has access to their bank accounts, and who has access to financial infrastructure in general. In short: you can decide who will be deplatformed from society. In the most extreme cases, this is a matter of life and death. Who gets to eat and who must starve; who gets to prosper, and who must perish.

One can choose to be ruled by rulers or ruled by rules. And self-custodying your Bitcoin is perhaps the very first step to gaining financial self-sovereignty. Exchange can take your money anytime, don't forget the lessons from FTX. And it was not long after the approval of Bitcoin's Spot ETF did I decided to re-post this writing as a gentle reminder to myself and to those who are dear to me: "Not your keys, not your coins". Own your keys. Or at least know how.

## Code

I have open-sourced my code here: [self-custody](https://github.com/btc-z/self-custody)

## Setup

It will probably take less than half of your Sunday afternoon to understand everything in the setup:

![](https://private-user-images.githubusercontent.com/119766095/303808289-80343a5e-9244-4b75-98c1-acc27b4eed03.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDc1MzA4OTgsIm5iZiI6MTcwNzUzMDU5OCwicGF0aCI6Ii8xMTk3NjYwOTUvMzAzODA4Mjg5LTgwMzQzYTVlLTkyNDQtNGI3NS05OGMxLWFjYzI3YjRlZWQwMy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMjEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDIxMFQwMjAzMThaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lODI0NzJlYWFiYzkzYWEzZTFkMTg0MTcwYTYyNjE2MjlmMTY1YjYwYWJkZDgzNjkyMDgzYWI1NmE4OGNkOGUwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.oU8T2quzf8XfmuU1y5guec0sQFJUL9DI-nXO-Bgaxbk)

Here are the 5 things that you need to self custody:

- [ColdCard Mk4](https://coldcard.com/docs/coldcard-mk4) as Hardware Wallet
- [bitcoind](https://bitcoin.org/en/bitcoin-core/) as full node
- [Fulcrum](https://sparrowwallet.com/docs/server-performance.html) as SPV (Simplified Payment Verification)
- [Sparrow](https://sparrowwallet.com/) as wallet
- Metal Plate (buy anywhere) to store the seed phrase


## ColdCard

ColdCard is a hardware wallet focused on air-gapped security and offline storage, primarily suitable for those who prioritize security for their Bitcoin holdings. It is the hardware wallet that I use and is the only one that I would recommend to my friends because ColdCard is open-sourced (its code has been reviewed by top programmers and cryptographers in the world)

It looks like a pocket calculator, is light to travel (about 30g or less than the weight of 1 cup of espresso), and you can easily take it through airport security, and no one knows that there are 1 million dollars worth of Bitcoin inside because cryptography is magic.

I have studied and sketched the ColdCard security model below:

![](https://private-user-images.githubusercontent.com/119766095/303808490-c8e7d253-40ba-48ec-8877-a1a6455c83cd.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDc1MzExNDQsIm5iZiI6MTcwNzUzMDg0NCwicGF0aCI6Ii8xMTk3NjYwOTUvMzAzODA4NDkwLWM4ZTdkMjUzLTQwYmEtNDhlYy04ODc3LWExYTY0NTVjODNjZC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMjEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDIxMFQwMjA3MjRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05NTM2ZDM4Yjk4OTM1YWQxZjllZGU2Y2NmMWUxYmJkOTAwNzVhNjZhMDQ3ZmI0YmNjODE5ZDNiY2Q0YmU2OWRjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.PuQgt3RSJ7N7t76RiguICSxzrC3ZxQcFiz4knsXmDX8)

The PIN is for the ColdCard hardware device only. Its primary function is to encrypt the wallet and to protect the private keys inside. Therefore, you do not need the device PIN to recover your Bitcoin wallet. To recover your Bitcoin wallet, you only need mnemonic phrases and the extension word (passphrase).

Having access to the device PIN implies having access to the BIP-39 mnemonic 12/24 words, and any 13th or 15th extension word. Because of this, you should use a long and high-entropy PIN. By default, ColdCard will brick the device if entered incorrectly 13 times. You can also set an idle timeout to avoid “evil maid attacks”, this is very similar to the auto-lock feature on your iPhone. In addition, if you rarely spend Bitcoin, you can even set a login countdown time to further delay the next login time to as many as 28 days.

For plausible deniability, you can set a trick PIN to create a duress wallet and deposit a small amount of sats to act as a honey pot in case you are under threat.

If you want to create multiple wallets from the same seed phrase and want to delegate one wallet to someone else while concealing the seed phrase, you can choose to use the “lockdown seed” option on the device, which effectively converts the key into a BIP-32 key instead and erases the seed phrase.

## BIP39: Passphrase or No Passphrase?

I used BIP-39 24 seed words for generating a new wallet. The default passphrase, when not provided, is just an empty string `""` . A quick read from the BIP-39 proposal and BIP-32 proposal convinced me to add a passphrase because:

1. flexible to own up to about 5.9 x 10¹⁹⁷ different wallets
2. provides plausible deniability because every passphrase produces a valid wallet; therefore, it protects you against the “$5 wrench attacks”

![$5 wrench attack](https://private-user-images.githubusercontent.com/119766095/303808643-d4aedad5-5f09-40b1-84e1-86d6f3b56b7d.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDc1MzEzNTMsIm5iZiI6MTcwNzUzMTA1MywicGF0aCI6Ii8xMTk3NjYwOTUvMzAzODA4NjQzLWQ0YWVkYWQ1LTVmMDktNDBiMS04NGUxLTg2ZDZmM2I1NmI3ZC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMjEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDIxMFQwMjEwNTNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zOGI1NzdlMTA3MjhiYjgyYTkyNzgwMjY3ZDVmOTgzMjNhYTg0NWVhMTIyZjBjY2ZjMDg2YWY1MjBhOGM4ZGM1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.SLh4ZKXbwGKUu4mT4CVuu1Lnh6uNWPOLN7iLbhvo3HY)

!!! note
    Having a seed passphrase is like having a two-factor authentication. Not only do you need to have the 24 words, but you also need to know where in that 5.9 x 10¹⁹⁷ possible wallet space you stored it.


!!! warning
    The seed passphrase is an extension word. Do not confuse it with the pin or password to encrypt a wallet. Forgetting the passphrase will cause you to lose Bitcoin stored in that wallet.


!!! note
    Once you apply the passphrase, ColdCard will display an 8-digit extended fingerprint (XFP). As the name suggested, XFP is for identifying which wallet we are using.

!!! warning
    ColdCard doesn’t store the passphrase on its hardware device. Knowing the seed passphrase is similar to knowing where the diamond is in a desert. Losing it, you won’t be able to find where your Bitcoin is stored even if you have the 24-seed-passwords.


## Sparrow

While ColdCard excels in offline security and transaction signing, Sparrow offers complementary features, convenience, and a user-friendly interface for managing your Bitcoin holdings, especially when you need to interact with your wallet beyond storage. There are 3 stages of using Sparrow:

![](https://private-user-images.githubusercontent.com/119766095/303809705-6d847dc1-bf57-45c4-ac4c-db9656f39555.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDc1MzI3NzIsIm5iZiI6MTcwNzUzMjQ3MiwicGF0aCI6Ii8xMTk3NjYwOTUvMzAzODA5NzA1LTZkODQ3ZGMxLWJmNTctNDVjNC1hYzRjLWRiOTY1NmYzOTU1NS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMjEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDIxMFQwMjM0MzJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zOTNjN2QwMGM3OTkzMGM5Yjk1NWI3NjYyMzhmNGYzNGY2YzAwYzc2MTFkN2MyNmFmZGRhOTRkMmYzYjcwMWRhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.Cim6_LDF8JsUcsFY2Ejx7HOFSp_ENaOwyx4aT72Scgw)

Running the expert-level Private Electrum Server would index all Bitcoin transactions equally which prevents attackers from knowing which address is yours, so it is naturally the most recommended setup.

In reality, I encourage you to play with the setup progressively with a small amount of Bitcoin at first. Going from ground zero to expert level is impractical.

For example, I use the Public Electrum server for my BlueWallet mobile app on my iOS device for very small transactions (less than 100$). I have also tested with the Private Bitcoin Core first before moving on to the Private Electrum Server option during my early endeavors in self-custody.

It is also important to keep in mind that the set-up you desire should be proportional to the amount of Bitcoin you hold. If you own a small amount of Bitcoin, then setting up a Private Electrum Server might not be worth the effort (unless you are just curious). Similarly, the more Bitcoin you hold, the more you would naturally care about the security of the self-custody setup. There are measures that I will explain which will make your self-custody relatively secure.

![](https://private-user-images.githubusercontent.com/119766095/303808880-20e16faa-fc48-469f-9864-0ce13b9c7340.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDc1MzE2ODQsIm5iZiI6MTcwNzUzMTM4NCwicGF0aCI6Ii8xMTk3NjYwOTUvMzAzODA4ODgwLTIwZTE2ZmFhLWZjNDgtNDY5Zi05ODY0LTBjZTEzYjljNzM0MC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMjEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDIxMFQwMjE2MjRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mZTNlNGM0OTJmMGFjMmVkYWUzNWFmMDk0ZDA3YzJhNjJiZmVkM2EyMmVlZTk5Zjc2NmE2NWRhMGI2MTdiOTdlJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.PfQBbnhDQAfc0g5XAZNfd2blUe2rqL32DbB31B_8upQ)


## "Not your node, not your rule"

“Not your node, not your rule”, running a Bitcoin node yourself allows you to validate transactions and broadcast blocks using rules that everyone else has agreed to. Not running your node means that you have to trust someone else is doing it.

Sometimes, it is acceptable to connect to a node operated by a family member or a close friend whom you trust. And hopefully, this post provides certain assurance that running a node isn’t as hard as you might think.

Details of how to start a node can be found [here](https://github.com/btc-z/self-custody).

I am running my node in Docker on an old Macbook, but you can run it on Windows or Linux just the same (because Docker). Do make sure you have met the resource requirement specified [here](https://bitcoin.org/en/bitcoin-core/features/requirements).

Once `bitcoind` finishes syncing, you should see something like this in the log.

```
bitcoind [date] UpdateTip: new bes=****block-hash**** height=***block-height****
```

At this step, you will be able to test integration between Bitcoin Core and Sparrow Wallet. As shown below, after clicking the **Test Connection**, we see the expected success message “BWT v.0.2.4”...


![](https://private-user-images.githubusercontent.com/119766095/303809134-18e24938-9850-46ad-a4ca-849cababd068.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDc1MzE5OTMsIm5iZiI6MTcwNzUzMTY5MywicGF0aCI6Ii8xMTk3NjYwOTUvMzAzODA5MTM0LTE4ZTI0OTM4LTk4NTAtNDZhZC1hNGNhLTg0OWNhYmFiZDA2OC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMjEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDIxMFQwMjIxMzNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yZjdmMmY5NDNkMDNlNWVlZTY4MzMwYTdhYWI3NWZkMDU0NWQ1ZDgxZjk5YWMxNGEwNTdkMDRhNTRhOGU3NGExJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.znponAM_uYjvsINZdwIIIvcMcwSTxIAltHNb9I2ukGY)


## Running Fulcrum

Similar to starting Bitcoin Core, I have described how to run fulcrum here: https://github.com/btc-z/self-custody#run-fulcrum. We chose Fulcrum instead of other implementations based on the [Server Performance Guide](https://sparrowwallet.com/docs/server-performance.html).

Fulcrum performs a full index on Bitcoin transactions, which is something Bitcoin Core itself doesn’t do. Therefore, using a Fulcrum as a Private Electrum Server makes sure that outsiders don’t know what your address(es) are.

After Fulcrum finishes indexing, which took about 2 days on my old Mac, we would see something like the below:

![](https://private-user-images.githubusercontent.com/119766095/303811326-beb05f67-7063-4795-9854-ee45a5144534.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDc1MzUxNjIsIm5iZiI6MTcwNzUzNDg2MiwicGF0aCI6Ii8xMTk3NjYwOTUvMzAzODExMzI2LWJlYjA1ZjY3LTcwNjMtNDc5NS05ODU0LWVlNDVhNTE0NDUzNC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMjEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDIxMFQwMzE0MjJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yZmU0ZDViOTJiM2YzMzkzN2UwZGFhNzk0NWFhNTEzMDljZGVmMzhkZjdmNWFmZGFhZTE3YjA4YWI1Zjg4ZjFmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.wq7VYKkirDaizTudWdVptFdKP_3Hw5o7zCgFcTJaq0E)

Similar to how we tested the Bitcoin Core connection, now navigate to the Electrum Private Server tab and tap **Test Connection**.

![](https://private-user-images.githubusercontent.com/119766095/303811347-f82f1fd0-6791-4767-8951-a2e701724f2e.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDc1MzUxOTUsIm5iZiI6MTcwNzUzNDg5NSwicGF0aCI6Ii8xMTk3NjYwOTUvMzAzODExMzQ3LWY4MmYxZmQwLTY3OTEtNDc2Ny04OTUxLWEyZTcwMTcyNGYyZS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMjEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDIxMFQwMzE0NTVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04ZWRiYzg3YmExNmRlZGFiNjc5MzcyZDllNTVmNmNmMDNjYzlmZGVjMTI3YjkzMDA4YzA2ZTdjY2JiZWNmZjY2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.tCVbUkvrXWspPJtfV0rVwodzObud2VUaf0xYaeiXpLk)


We see that the connection to the Fulcrum 1.9.0 server was successful.

At this point, your Sparrow wallet is safe to use! Let's look at how to send and receive Bitcoin now.

## Receive Bitcoin

In Sparrow, click **Addresses** to view a set of Receive and Change addresses.

Why so many addresses? The best answer I have heard is from ["is it possible to brute force bitcoin address creation in order to steal money?"](https://bitcoin.stackexchange.com/questions/22/is-it-possible-to-brute-force-bitcoin-address-creation-in-order-to-steal-money)]: it is simply much cheaper to mine than to hack as hacking takes tremendously more processing power.


Inside any Bitcoin wallet, you have an extremely large number of Bitcoin addresses for this reason. Consequently, it is highly recommended to never re-use Bitcoin addresses. Sparrow conveniently refreshes a new receive address automatically so that each receive address is only associated with a single transaction.


![](https://private-user-images.githubusercontent.com/119766095/303811561-faa2cbb7-0933-4c92-9d55-0316ed87b28c.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDc1MzU1NTksIm5iZiI6MTcwNzUzNTI1OSwicGF0aCI6Ii8xMTk3NjYwOTUvMzAzODExNTYxLWZhYTJjYmI3LTA5MzMtNGM5Mi05ZDU1LTAzMTZlZDg3YjI4Yy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMjEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDIxMFQwMzIwNTlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05YTIxMTUxMTE0Zjk0OTljM2M4OGY1M2JhOGQzODI2YzJhNWEyYjFkZWY2MjM1NDk2MmRmMTc2MjQyYWZiZDQ1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.NHv3-j8Vfvxsj-WL3Rlk5KXTtO5_WDVJpyslC8MfrKw)

As shown in the above image, I have tested sending a small amount of Bitcoin from my mobile BlueWallet to ColdCard, and also from Binance to my ColdCard. Sparrow allows users to label addresses, conveniently.

When a transaction is broadcasted from my BlueWallet or Binance, it will take on average 10 minutes to have 1 confirmation. After 6 confirmations, the transaction is then assumed to be secure. Why 6? because at that point, it becomes nearly impossible to mess around with that transaction anymore. What does this mean to you? When you receive a Bitcoin, wait for about an hour (10 minutes / per confirmation, so 6 confirmations in an hour) before you treat that transaction as final.

## Send Bitcoin

In the **Send** tab, you can create a transaction by filling in

1. (required) Pay To address (use QR scan if possible to avoid incorrect typing of address)
2. (required) amount in sats or BTC
3. (optional) label: to record this transaction
4. (optional) select fee: if you don’t like the default fee, you can adjust the fee depending on how soon you want it to be completed. The quicker, the more expensive.
5. (optional) optimize by efficiency or privacy

![](https://private-user-images.githubusercontent.com/119766095/303811609-e1f8ac62-079a-4225-93cf-ce0d25f34c2c.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDc1MzU2NDMsIm5iZiI6MTcwNzUzNTM0MywicGF0aCI6Ii8xMTk3NjYwOTUvMzAzODExNjA5LWUxZjhhYzYyLTA3OWEtNDIyNS05M2NmLWNlMGQyNWYzNGMyYy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMjEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDIxMFQwMzIyMjNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xNzNmMDhhMmEwODUxMzRhNzY0MjA1YTU1NjQ5MjVlZGJkYzU1ZTFhZGNiYTVjMGJhN2MxMTc5ZDg3ZGJmZTE0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.Om-aFgrnrqpi8K-1evfvNhx5T4uNXeS4W1cvTt7x7Pk)

Next, we will save the PSBT transaction data into the MicroSD card to be hooked up with ColdCard.

![](https://private-user-images.githubusercontent.com/119766095/303811620-e03ccb6a-a7f3-4c24-9bed-4392eef32aa8.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDc1MzU2NzMsIm5iZiI6MTcwNzUzNTM3MywicGF0aCI6Ii8xMTk3NjYwOTUvMzAzODExNjIwLWUwM2NjYjZhLWE3ZjMtNGMyNC05YmVkLTQzOTJlZWYzMmFhOC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMjEwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDIxMFQwMzIyNTNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02MTQzYzdlYzgxM2U2ZjAzNjA4NTk1OGMzOTQ4MjI1NzdiYzU3MGU2ZTcyY2VlMmZlMTFhMjg5MDk1YzljZGQ5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.JpbemgFHimc5NI2OL1Z8KvQDiRcFw4uYzPqwQfKKMIg)

1. save the PSBT transaction into the MicroSD.
2. Open ColdCard and insert MicroSD.
3. Sign transaction on ColdCard (a file with the format label-final.txn will be written to MicroSD)
4. back to Sparrow with MicroSD connected, and load in the signed transaction.
5. Click Broadcast
6. Congrats! Your transaction is now submitted to the blockchain p2p network.



## Securing Seed

It is worth repeating: losing your seed means your Bitcoins are forever lost. There isn’t a customer service desk that you can call to recover your lost Bitcoin if you lost your seed phrase.

It also means that storing your seed in a device that has an internet connection is exposed to attacks.

The best way to store a secret is to store it in a place that only you know. There are factors to consider when choosing such a location and medium to store. Risks like natural disasters can be reduced using materials like stainless steel or titanium. Even when such risks are unavoidable, you can use multi-sig to further secure your assets so that losing one key isn’t catastrophic. Let me know if you are interested in learning more about this. I will write another article if there is enough interest.

## What's Next?

Raise an issue [here](https://github.com/btc-z/self-custody/issues) if you have questions or if any steps don't work for you. I usually respond within a week. At last, allow me share this quote to remind us why all this matters:

!!!quote
    Law, Language, and Money. A healthy trifecta of these three is absolutely essential for a free society to flourish. If freedom is a value you hold in high regard, this translates to (1) free speech, (2) sound money, and (3) individual property rights. Bitcoin uses (1) to create (2) and enforce (3)—without the necessity of violence. After all, no amount of violence will ever solve a math problem, as Jacob Appelbaum said so beautifully.

**In math, we trust** [finis]