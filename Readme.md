# 🚀 Python-Driven Network Inventory Auditor with Compliance Validation

## 📌 Overview
This project is a Python-based network automation tool that audits network device configurations and validates them against predefined security policies.

It simulates real-world enterprise network auditing systems used to improve security, reduce manual effort, and ensure compliance.

---

## 🎯 Features
- 🔍 Multi-device processing using YAML inventory
- 📜 Policy-driven compliance validation (JSON-based)
- ⚡ Dynamic rule engine (no hardcoding)
- 📊 Automated CSV report generation
- ❌ Failure detection with clear reasons
- 🧪 Simulation mode (no physical devices required)

---

## 🛠️ Tech Stack
- Python
- PyYAML
- pandas
- Netmiko *(optional for real device integration)*

---

## 📁 Project Structure
Network-Automation-Auditor/
│
├── inventory/
│ └── devices.yaml
│
├── policies/
│ └── policy.json
│
├── scripts/
│ └── auditor.py
│
├── reports/
│ └── audit_report.csv
│
├── output/
└── README.md


---

## ⚙️ How It Works
1. Loads device details from `devices.yaml`
2. Loads compliance rules from `policy.json`
3. Simulates device configuration (or connects to real devices)
4. Validates configuration against policies
5. Generates a structured CSV audit report

---

## ▶️ How to Run

### 1. Create Virtual Environment
python -m venv venv


### 2. Activate Environment

venv\Scripts\activate


### 3. Install Dependencies

pip install pyyaml pandas


### 4. Run the Script

cd scripts
python auditor.py


---

## 📊 Sample Output
| Device | SSH | TELNET | Reason | Final Status |
|--------|-----|--------|--------|--------------|
| 192.168.1.1 | PASS | FAIL | telnet failed | FAIL |

---

## 🧠 Key Concepts Implemented
- Network Automation
- Configuration Auditing
- Policy-Based Validation
- Data Processing & Reporting
- Scalable System Design

---

## 🚀 Future Enhancements
- 🔗 Real device integration using Netmiko (SSH)
- 📊 Dashboard visualization (Power BI / Streamlit)
- 🌐 Multi-vendor support
- ⚙️ Advanced compliance rules

---

## 💼 Resume Impact
Developed a Python-based network compliance auditing system that automates configuration validation using policy-driven logic and generates structured reports, improving efficiency and scalability.

---

## 📌 Author
Anasuri Nithish Chandra.
