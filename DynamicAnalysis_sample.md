## 3. 動的所見（Dynamic Findings）

### 3.1 実行環境（Execution Environment）
解析の再現性を担保するための環境情報を記載。

| Item | Value | Note |
| :--- | :--- | :--- |
| **Date/Time (UTC)** | `YYYY-MM-DD HH:MM:SS` | |
| **OS / Build** | `Windows 10 x64 (Build 19045)` | |
| **VM Snapshot** | `[Snapshot Name]` | Clean state verified |
| **Network Mode** | `Host-Only` / `Custom (Simulated)` | |
| **Tools Config** | FakeNet-NG: `Enabled (Ver X.X)`<br>Procmon: `Ver X.X` | |
| **Sample SHA256** | `[HASH_VALUE]` | |

### 3.2 システムアクティビティ（System Activity）
*Source: Procmon, Sysmon, API Monitor*

#### 3.2.1 Process Tree & Execution Flow
親子関係、PID、およびコマンドライン引数を記録。
*Format: `ProcessName.exe (PID: 1234) > ChildProc.exe (PID: 1235)`*

```text
[ROOT] Parent.exe (PID: [PID])
 └─ [CMD] Command line: "[FULL_COMMAND_LINE]"
     │
     ├─ Child_1.exe (PID: [PID])
     │   └─ [CMD] "[ARGUMENTS]"
     │
     └─ Child_2.exe (PID: [PID])
         └─ [Injection Target] svchost.exe (PID: [PID])
```
### 3.2.2 Significant File I/O
ドロッパー機能や構成ファイルの作成・変更・削除。一時ファイルは除外。

| Operation | File Path | SHA256 / Context |
| :--- | :--- | :--- |
| **Create** | `C:\Users\[User]\AppData\Local\Temp\[Name].exe` | `[HASH]` (Payload) |
| **Modify** | `C:\Windows\System32\drivers\etc\hosts` | Added malicious entry |
| **Delete** | `[Original_Sample_Path]` | Self-deletion |

### 3.2.3 Registry & Configuration Changes
マルウェアの設定保持やシステム設定の改ざん。

| Operation | Key Path | Value Name | Data / Type |
| :--- | :--- | :--- | :--- |
| **Set** | `HKCU\Software\[MalwareName]` | `Config` | `[Binary Data]` |
| **Set** | `HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings` | `ProxyServer` | `[IP]:[Port]` |

### 3.2.4 Persistence Mechanisms (ASEP)
Autoruns差分および永続化の痕跡。

* **Technique:** `[Registry Run Key / Service / Scheduled Task / Startup Folder]`
* **Location:** `[Path or Key]`
* **Target:** `[Command or Binary Path]`
* **Observation:** (例: システム再起動後にペイロードが実行されることを確認)

### 3.3 ネットワークアクティビティ（Network Activity）
*Source: FakeNet-NG, Wireshark, Suricata*

#### 3.3.1 DNS Queries
名前解決の試行と応答。

| Domain Name | Record Type | Response (IP/CNAME) | Assessment |
| :--- | :--- | :--- | :--- |
| `malicious-domain[.]com` | A | `192.0.2.1` | **C2** (Confirmed) |
| `connectivitycheck.gstatic.com` | A | `[Real IP]` | Connectivity Check |

#### 3.3.2 HTTP(S) Traffic
通信の詳細内容。User-Agentや特徴的なヘッダ。

* **Endpoint:** `http://[C2_HOST]/[URI]`
* **Method:** `POST`
* **User-Agent:** `Mozilla/5.0 (Windows NT 10.0; Win64; x64)...`
* **Payload/Pattern:**
    ```text
    [Request Body Hex/ASCII Dump]
    key=value&id=[bot_id]
    ```
* **JA3 Fingerprint:** `[JA3_HASH]` (if TLS)
* **Notes:** (例: 既知のマルウェアファミリ [Family Name] のビーコンパターンと一致)

#### 3.3.3 Other Network Artifacts
TCP/UDPの未解決通信やカスタムプロトコル。

* **Connection:** `[SrcIP]:[SrcPort] -> [DstIP]:[DstPort] (TCP/UDP)`
* **Payload Header:** `0x[HEX]` (Magic Bytes)
* **Observation:** (例: カスタム暗号化プロトコルによるC2通信の可能性)

### 3.4 解析者メモ・仮説（Analyst Notes & Hypotheses）
* **Fact:** (観測された事実のみを記載)
* **Hypothesis:** (事実に基づく推論。例: この挙動から、ランサムウェアの準備段階であると推測される)
