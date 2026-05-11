# GRC & Security Audit Logger
# Purpose: Demonstrate automated compliance logging for GRC roles
import datetime

def log_audit_finding():
    print("--- AtoZ Security Compliance Audit ---")
    
    # GRC specific inputs
    control_id = input("Enter Security Control ID (e.g., AC-1): ")
    finding = input("Describe the Audit Finding: ")
    
    # severity logic (Core PCEP/SOC concept)
    print("Select Severity: 1-Low, 2-Medium, 3-High")
    severity = input("Enter Level (1-3): ")
    
    levels = {"1": "LOW", "2": "MEDIUM", "3": "HIGH"}
    status = levels.get(severity, "UNKNOWN")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        with open("security_audit_log.txt", "a") as audit_file:
            audit_file.write(f"[{timestamp}] [SEVERITY: {status}] [ID: {control_id}] - {finding}\n")
        print(f"\n✅ Audit entry saved under Severity: {status}")
    except Exception as e:
        print(f"❌ System Error: {e}")

if __name__ == "__main__":
    log_audit_finding()
