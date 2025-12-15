# Static Analysis Report

## 1. Administrative Information
- **Case ID:** `[YYYYMMDD-###]`
- **Analyst:** `[Name]`
- **Analysis Date:** `[YYYY-MM-DD]`
- **Sample Name (Original):** `[Filename]`

## 1. Executive Summary (Overview)

### 1.1 Sample Identity & Metadata
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

## 2. Static Analysis Findings

### 2.1 PE Structure & Header Anomalies
*異常値（セクション名、サイズ不整合、RWE権限など）のみ記述。*

| Section Name | Virtual Size | Raw Size | Characteristics / Entropy |
| :--- | :--- | :--- | :--- |
| `.text` | `0x...` | `0x...` | `Execute/Read` |
| `[Suspicious]` | `0x...` | `0x...` | `[High Entropy / RWX]` |

### 2.2 Imports (IAT) & Capabilities
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

### 2.3 Interesting Strings
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

### 2.4 Inference from Static Triage
```text
capa.exe
```
- **ラベル:** `[Malicious(悪性)/ Suspicious(疑わしい) / Benign(良性)`
- **Family / Label:** `[e.g., Emotet, CobaltStrike Beacon]`
- **Confidence Level:** `[High / Medium / Low]`

**Key Findings:**
1.  **Capabilities:** `[要約: C2通信、ダウンローダー機能など]`
2.  **Infrastructure:** `[要約: 通信先の特徴]`
3.  **Obfuscation:** `[要約: パッキングや難読化の手法]`
