import yaml
import json
import pandas as pd
import ollama

# -------------------------------
# Load Devices
# -------------------------------
with open('../inventory/devices.yaml') as f:
    devices = yaml.safe_load(f)["devices"]

# -------------------------------
# Load Policy Rules
# -------------------------------
with open('../policies/policy.json') as f:
    policy = json.load(f)

results = []

# -------------------------------
# Process Each Device
# -------------------------------
for device in devices:
    try:
        print(f"Processing {device['host']}...")

        # -------------------------------
        # Simulated Device Configuration
        # -------------------------------
        config = """
                hostname R1
                line vty 0 4
                transport input ssh
                no transport input telnet
                service password-encryption
                """

        device_result = {"Device": device["host"]}

        # -------------------------------
        # Rule-Based Validation
        # -------------------------------
        for rule_name, rule in policy["rules"].items():
            command = rule["command"]

            if command in config:
                if rule.get("required", False):
                    status = "PASS"
                else:
                    status = "FAIL"
            else:
                if rule.get("required", False):
                    status = "FAIL"
                else:
                    status = "PASS"

            device_result[rule_name.upper()] = status

            # -------------------------------
            # Add Failure Reason (Clean Format)
            # -------------------------------
            if status == "FAIL":
                if "Reason" not in device_result:
                    device_result["Reason"] = f"{rule_name} failed"
                else:
                    device_result["Reason"] += f", {rule_name} failed"

        # -------------------------------
        # AI ANALYSIS USING OLLAMA
        # -------------------------------
        try:
            ai_prompt = f"""
Analyze this network configuration.

Respond in ONE LINE only:
Issues | Risk Level | Fix

Config:
{config}
"""
            response = ollama.chat(
                model="llama3",
                messages=[{"role": "user", "content": ai_prompt}]
            )

            ai_output = response['message']['content']
            clean_ai_output = ai_output.replace("\n", " ").replace(",", " -")
            device_result["AI Analysis"] = clean_ai_output

            # -------------------------------
            # Extract Risk Level
            # -------------------------------
            if "high" in ai_output.lower():
                device_result["Risk Level"] = "High"
            elif "medium" in ai_output.lower():
                device_result["Risk Level"] = "Medium"
            else:
                device_result["Risk Level"] = "Low"

        except Exception as ai_error:
            device_result["AI Analysis"] = "AI analysis failed"
            device_result["Risk Level"] = "Unknown"

        # -------------------------------
        # Final Status Calculation
        # -------------------------------
        if all(
            v == "PASS"
            for k, v in device_result.items()
            if k not in ["Device", "Reason", "AI Analysis", "Risk Level"]
        ):
            device_result["Final Status"] = "PASS"
        else:
            device_result["Final Status"] = "FAIL"

        results.append(device_result)

    except Exception as e:
        print(f"❌ Error for {device['host']}: {e}")

# -------------------------------
# Generate CSV Report
# -------------------------------
df = pd.DataFrame(results)
df.to_csv('../reports/audit_report.csv', index=False)

print("✅ AI-Powered Network Audit Completed!")