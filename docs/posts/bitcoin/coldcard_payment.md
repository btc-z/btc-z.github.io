---
draft: false
date: 2024-10-26
categories:
    - Bitcoin
---

# 如何安全支付Bitcoin

如何在使用冷钱包的情况下安全支付比特币

## 硬件

- COLDCARD: 冷钱包
- MicroSD Card: 用于airgapped的签名(以确保整个过程完全不联网)

## 软件

- Sparrow
- GPG Keychain Tool


## 更新Firmware

1. [官网指南](https://coldcard.com/docs/upgrade/#dont-trust-verify-the-firmware)
2. 下载最新firmware
3. 确认以下
   1. Confirm the Hash
      ```
      shasum -a256 ~/<fireware下载路径>/20...-coldcard.dfu
      ```
      确保output的hash和signature的hash一致, 一致的话意味着firmware在transfer过程中没有被修改过。
   2. Verify PGP Signature
      ```
      gpg --verify ~/<签名的下载路径>/signatures.txt 
      ```
      确保看到"Good signature from "Peter D. Gray peter@coinkite.com"的字样。
4. 用MicroSD card把新的firmware `.dfu` 文件安装到coldcard上
5. 更新后ColdCard会再次要求输入PINs，记得确认firmware的version。

## 安全支付Bitcoin 

尽可能使用Airgapped的方式，确保COLDCARD永远不和联网的机器连着。MicroSD card当中间人。

1. 打开Sparrow
2. Click `Send`
3. Fill in `Pay to`, `Label`, `Amount` details
4. `Create transaction`
5. `Finalize Transaction for Signing`
6. `Save transaction` to MicroSD card
7. move to COLDCARD
8. (remember to enter passphrase if you had one BIP39)
9. `Ready To Sign`
10. shoudl expect `Reading...` then `Validating...` 
11. confirm if transaction looks correct
12. a `-signed.psbt` file should be created by then
13. 把MicroSD插回电脑上
14. `Load Transaction`
15. Select the PSBT file and open
16. `Broadcas Transaction` now.
17. will take some time before the transaction is confirmed. 



