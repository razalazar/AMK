# 🛡️ AMK Security & Open Source Governance

At **AMK (Agent Memory Kit)**, we understand that data sovereignty and codebase security are the highest priorities for Enterprise Software Architects. 

AMK operates as an integral part of your development lifecycle and handles proprietary code data. To ensure absolute trust, AMK was designed under a strict **Zero-Telemetry, Local-First** governance model.

This document outlines our security architecture and provides technical guides on how to audit the framework.

---

## 1. Governance and Trust

### 📖 100% Open Source & Auditable
AMK is distributed under the permissive **MIT License**. The entire source code is available in plain text. We do not use compiled binaries, obfuscated code, or closed-source tracking modules. Any cybersecurity expert can clone the repository, read it line by line, and verify its integrity.

### 🏠 Local-First Architecture
AMK does **NOT** send your proprietary code, prompts, or interaction logs to external servers (e.g., AWS, Azure, GCP, or foreign data centers). 
- All evolutionary memory data is stored locally in your workstation's file system or your company's private intranet.
- We do not inject tracking pixels, analytics, or telemetry scripts into the package.

---

## 2. How to Audit and Validate AMK (The Golden Tests)

We encourage developers and security teams to validate AMK's security claims using the following enterprise-grade auditing techniques:

### A. The Ultimate Test: The "Air-Gapped" (Offline) Execution
The most deterministic way to prove AMK does not exfiltrate data is to run it without the internet:
1. Disconnect your machine from the internet (turn off Wi-Fi/Ethernet).
2. Run your Python script with AMK installed (`InteractionMemory`, `CodeEvolutionMemory`).
3. **Result:** AMK will continue to function perfectly. It will successfully write the JSON logs to your local directory without crashing or waiting for a network timeout. This proves mathematically that no external API calls are being made by the core engine.

### B. Network Traffic Monitoring
If you cannot turn off your internet, you can use standard networking tools to monitor outbound connections:
- **macOS:** Use [Little Snitch](https://www.obdev.at/products/littlesnitch/index.html) or the built-in Network Monitor.
- **Linux/Windows:** Use `Wireshark`, `tcpdump`, or `GlassWire`.
- **Result:** While running an AMK script, filter the traffic by your Python process. You will observe **0 bytes** of outbound traffic sent by the `evomem` module.

### C. Inspecting the Package Before Installation
You do not have to blindly trust `pip install`. You can inspect the exact package contents downloaded from PyPI *before* running it:
1. Download the wheel without installing it:
   ```bash
   pip download evomem --no-deps
   ```
2. Unzip the downloaded `.whl` file (a wheel is simply a standard ZIP archive):
   ```bash
   unzip evomem-*.whl -d evomem_inspect
   ```
3. Open the `evomem_inspect` directory in your IDE. You can read every single `.py` file that will be installed on your machine. You will see that the codebase matches the GitHub repository exactly, with no hidden payload.

### D. Dependency Tree Auditing
Malware is often injected through deeply nested third-party dependencies. 
- AMK is designed to have a minimalist footprint. It relies almost exclusively on the Python Standard Library (e.g., `json`, `pathlib`, `datetime`). 
- You can verify our dependencies by running:
  ```bash
  pip show evomem
  ```
  Check the `Requires` section to validate the absence of bloated or suspicious external libraries.

---

## 3. Reporting Vulnerabilities
If you discover a security vulnerability within AMK, please do not disclose it publicly on the issue tracker. Instead, refer to the [Contact/Maintainer details in GitHub](https://github.com/inecore/AMK) or submit a secure vulnerability report through GitHub's standard Security Advisory channels. We are committed to patching and releasing fixes immediately.
