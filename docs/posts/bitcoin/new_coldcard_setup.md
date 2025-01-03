# New COLDCARD Setup

COLDCARD is called COLDCARD not because it feels cold, or my jokes are cold :cold_face:, but because it’s completely offline. When setup properly, COLDCARD can be used without ever connecting to internet, making it the safest way to store Bitcoin.

I’ve had more than one friend fall victim to hacks of imToken, and lost all their assets. These threats are real. And as Bitcoin enters bull run, breaking 100,000$ not long ago, understanding how to protect your bitcoin from hackers becomes ever more important.

At minimal:

1. Do not store bitcoin on exchanges not even on Coinbase. (remember Mt.Gox, FTX, etc. etc.)
2. Do not store bitcoin in hot wallets; its just unsafe
3. Do not buy BTC ETFs; not your keys, not your coins


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

Think of it as a "wallet of a wallet". Even if one knows your mnemonic, he wouldn't be able to access your wallet without knowing the passphrase.

## STEP 3 - Setup Desktop Wallet

Export your COLDCARD wallet from COLDCARD via MicroSD and import the wallet to your Sparrow client on Desktop. During this process, you will need to store your passphrase, remember your XFP, your account number and verify Sparrow's received addresses are the same as the ones from your COLDCARD.

### Store Passphrase

Save the passphrase to the MicroSD card once entered. COLDCARD does not store the passphrase. It can only loads the passphrase from the MicroSD card. The passphrase stored in MicroSD is encrypted at rest with AES-256 using a key derived from the seed and a hash of the MicroSD's serial number. One MicroSD can only be used for one COLDCARD.

Only people who have access to both your MicroSD card and COLDCARD (and be able to open it).

### XFP

XFP is useful for making sure you are using the correct wallet. The fingerprint of the public key is just the 4 bytes of the RIPEMD160 hash of the wallet's public key displayed as an 8-character hexadecimal string.


### Account

The account number is used for deriving wallet's key.

E.g., if you enter 100 using segwit-wallet, the derivation path of the first address becomes: `m/84'/0'/100'/0/0`. 

Therefore, it's important to remember and set account number accordingly in the address explorer to verify that the address you are sending Bitcoin to actually belong to you.


### Address Verification

Enter your account number and select the wallet type. Most wallets are Native Segwit (P2WPKH).

You can export the top 250 receive addresses to a csv file to your MicroSD card to verify that they match with what the Sparrow displays. For every transaction, we can quickly verify that the two lists match with each other. We can do the same type of verifications with the change address as well.


## STEP 4 - Move fund from exchange to wallet

### Take small steps

Always move small amount first to make sure your wallet is setup correctly. What we want to see is that those amounts are reflected on the blockchain with the correct receive address.

Also, practice signing a transaction from your COLDCARD to prove control of the fund. Either send it back to the exchange receive address or some other address of yours.

### Recovery

Before depositing any larger amounts into the wallet. Practice at least one round of recovery to prove that you can recover your wallet given the mnemonic and the passphrase. Do so by destroying the seed stored on your COLDCARD and re-import the seed and passphrase. Once applied, you should see the same XFP as previously seen.

### Decoy

A simple decoy wallet can be the wallet generated from your mnemonic only with empty passphrase. The majority of your BTC then is stored in the real wallet with the actual passphrase that only you know. COLDCARD is designed to not store your passphrase making the decoy approach possible. Note that if you decide to lock down the seed, you will effectively lose this ability.

### Secrets

Needless to say one should be extremely cautious where the mnemonic and the passphrase are stored, but keep in mind that your COLDCARD and the MicroSD card should also be kept securely. Same for the PINs that can unlock your COLDCARD. If you choose to use any password manager to store any of your secrets, understand that any compromises of the password manager risk compromising your Bitcoins[^6]. Pay attention to all of the following:

- mnemonic
- passphrase
- COLDCARD
- MicroSD card
- any password manager that stores anything of the above[^7]

[^6]: To prevent this, never store your seed or passphrase or any information about them in any password managers. Storing PINs to COLDCARD is usually considered safe because any thieves would need to obtain your physical COLDCARD AND know the PINs to take your BTCs. However, any person who know your seed + passphrase will be able to access your fund.

[^7]: e.g., if you store COLDCARD's PINs in any password manager, consider turning on 2FA at least and use a long enough password. Also make sure no one can access the password manager except you (biometric verification e.g., using FaceID).


### Finally

Move the remaining funds to your cold storage. You should practice sending and receiving BTC reguarly and transfer any BTC from exchanges as soon as the money lands there. The goal is minimize the time BTC sits in any exchanges, and rest all BTCs in cold storage.
