---
draft: true
date: 2024-11-13
title: New COLDCARD Setup
categories:
    - Bitcoin
---

# New COLDCARD Setup

![](https://i.imgflip.com/8eevp9.jpg)

COLDCARD is called COLDCARD not because it feels cold, or my jokes are cold :smile: :cold_face:, but because it’s completely offline. When setup properly, COLDCARD can be used without ever connecting to internet, making it the safest way to store Bitcoin.

I’ve had more than one friend fall victim to hacks of imToken, and lost all their assets. These threats are real. And as Bitcoin enters bull run, breaking 100,000$ not long ago, understanding how to protect your bitcoin from hackers becomes ever more important.

At minimal:

1. Do not store bitcoin on exchanges not even on Coinbase. (Mt.Gox, FTX, etc. etc.)
2. Do not store bitcoin in hot wallets; its just unsafe
3. Do not buy BTC ETFs; not your keys, not your coins
4. Start learning and using cold storage
5. Source your BTC and move them to cold storage asap afterwards.


## Recommended Readings

Check out COLDCARD's [official setup guide](https://coldcard.com/docs/quick/) if you haven't yet. I will only comment on COLDCARD's defense mechanism, and what to pay attention to when you setup a new one.


## STEP 1 - the device

If the device was ever altered by hackers, then you are storing your Bitcoin in a compromised device; therefore, sourcing your wallet from an official source is one of the most important steps.


## STEP 2 - Setup the device

If someone found your mnemonic, they get all of your BTCs.

If someone can access and open your COLDCARD, they can move your Bitcoin.

The most important defense is to physically secure your COLDCARD and your mnemonic seed phrases.

### Defense 1 - Device PIN

Use 6-digit pins for both  `prefix` and the `suffix` . Using just 2 digits will subject your device for brute force attack[^1]. If you forgot your PIN, you will need to buy a new COLDCARD device, but your bitcoin isn't lost as long as you still have the seed.

[^1]: COLDCARD bricks itself after some number of failed PIN attempts, in case someone is trying to guess your device password. Using a longer passport decreases the chance of brute force attack.

### Defense 2 - Anti-Phishing Phrase

COLDCARD uses the two-word anti-phishing phrase to protect against counterfeit device, this pops up between the prefix and suffix PINs. 

### Recommendations (Paranoid)

- Disable `NFC` mode during setup[^2]
- Disable `USB port` for transimitting data

Disable both and use only air-gap approach to sign transactions (use MicroSD card), and only then it is true COLDCARD not WARMCARD :wink:

[^2]: If the firmware on your wallet as well as the computer/phone are compromised, it's possible to lose the seed if you allow NFC (through tapping). It is possible, but difficult for both to be compromised. 

### Defense 3 - Dice Roll 

Extra peace in mind in case that some future bug is found in the pseudo random generator by COLDCARD, although it is unlikely since COLDCARD's firmware is open sourced. But neither did "Michael" knew that RoboForm's PW generator was tied to the password generation datetime. I find [this YouTube](https://www.youtube.com/watch?v=N2eKCAzM2kw) of how Joe & Bruno helped "Michael" recovered his lost 30 BTC inspiring especially when thinking about "should I use a dice roll"? Ironically, "Michael" would probably have sold most of the Bitcoin years ago if he hadn't forgotton his password (he said himself during an interview)[^3] :man_shrugging_tone1:

There are also greater philosophical debates about if true randomness exists, but I wouldn't go deep into that rabbithole.[^4] :rabbit:

[^3]: [How Researchers Cracked an 11-Year-Old Password to a $3 Million Crypto Wallet](https://www.wired.com/story/roboform-password-3-million-dollar-crypto-wallet/)
[^4]: Some even argue that atomic decay isn't truly random and our belief in randomness is only a product of ignorance. Talks are talks. No proofs of either really. So far it seems unpredictable, and you can bet a country on it. 


### Defense 4 - Add BIP-39[^5] Passphrase

A common approach to protect password tables in password-based cryptography is to combine a password with a salt to create a key. Opponents will be forced to search through not just the password tables but also possible salts, making dictionary attack less likely.

BIP-39 passphrase is the salt, and the mnemonic passphrase is the seed.

[^5]: [BIP-39 GitHub Proposal](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki)


**Work in Progress**


<!-- 



sdsds

 -->