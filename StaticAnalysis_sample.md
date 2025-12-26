# Static Analysis Report

## Administrative Information
- **Case ID:** `[YYYYMMDD-###]`
- **Analyst:** `[Name]`
- **Analysis Date:** `[YYYY-MM-DD]`
- **Sample Name (Original):** `[Filename]`

## Executive Summary (Overview)

### Sample Identity & Metadata
*必須項目は必ず埋め、不明な場合は N/A と記載すること。*
```text
sigcheck.exe -accepteula -nobanner -a -h -i -vt -v 
```
| Attribute | Value | Note / Anomaly |
| :--- | :--- | :--- |
| **SHA256** | `[Hash]` | |
| **MD5** | `[Hash]` | |
| **Imphash** | `[Hash]` | Import Table Hashing |
| **SSDeep** | `[Hash]` | Fuzzy Hashing |
| **File Type** | `[e.g., PE32+ executable]` | MIME: `application/x-dosexec` |
| **File Size** | `[Bytes]` | |
| **Compile Time** | `[UTC Timestamp]` | Check for TimeStomping |
| **Architecture** | `[x86 / x64 / .NET]` | |
| **Signature** | `[Signed / Unsigned]` | Signer: `[Name]` |
| **Entropy** | `[Score 0-8]` | >7.0 suggests packing |
| **VT detection** | `[0/77]` | |

---

## Static Analysis Findings

### Imports (IAT) & Capabilities
*機能に関連する重要APIのみを抜粋して記述。*

* **Networking (WinINet / Winsock):**
    * `InternetOpen`
    * `HttpSendRequest`
    * `[Other APIs...]`

* **Process / Injection:**
    * `VirtualAllocEx`
    * `CreateRemoteThread`
    * `[Other APIs...]`

* **Cryptography:**
    * `CryptDecrypt`
    * `[Other APIs...]`

### Interesting Strings
*FLOSS等で抽出した特徴的な文字列（IP、パス、typo、独自識別子など）。*
```text
floss.exe  
```
```text
[http://evil.com/gate.php](http://evil.com/gate.php)
C:\Users\Public\update.exe
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)
cmd.exe /c start
[Unique Mutex Name]
```
### DiE/PEiD（パッカー / コンパイラ推定）
| Item | Value |
|---|---|
| Version |  |
| Result: Packer |  |
| Result: Compiler/Linker |  |
| Notes |  |
| Evidence ref（detection tree / screenshot / export） |  |

### capa（capability列挙)
```text
capa.exe
```
| Item | Value |
|---|---|
| Version |  |
| Ruleset version/commit |  |
| Top capabilities（重要なものだけ） | ・1<br>・2<br>・3<br>|

### capa findings（rule + 根拠位置）
| Rule (capability) | Category/Namespace | Evidence locations（VA/RVA/func） | Notes |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

## 推測
*マルウェアの種類及び動的解析で確認する箇所*
```text

```
