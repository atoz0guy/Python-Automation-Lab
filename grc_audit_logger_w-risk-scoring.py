# GRC & Security Audit Logger with Risk Scoring
# Purpose: Demonstrate automated risk calculation for GRC/SOC roles
import datetime

def log_audit_finding():
    print("--- AtoZ Security Risk Assessment Tool ---")
    
    control_id = input("Enter Security Control ID (e.g., AC-2): ")
    finding = input("Describe the Finding: ")
    
    # Risk Scoring Logic (1-5 Scale)
    print("\nScale: 1 (Low) to 5 (Critical)")
    likelihood = int(input("Likelihood of occurrence (1-5): "))
    impact = int(input("Business impact if exploited (1-5): "))
    
    # Formula: Risk Score = Likelihood * Impact
    risk_score = likelihood * impact
    
    # Categorization based on score
    if risk_score >= 15:
        rating = "CRITICAL"
    elif risk_score >= 8:
        rating = "MEDIUM"
    else:
        rating = "LOW"

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        with open("security_audit_log.txt", "a") as audit_file:
            entry = (f"[{timestamp}] [SCORE: {risk_score}] [RATING: {rating}] "
                     f"[ID: {control_id}] - {finding}\n")
            audit_file.write(entry)
        print(f"\n✅ Audit saved. Calculated Risk Score: {risk_score} ({rating})")
    except Exception as e:
        print(f"❌ System Error: {e}")

if __name__ == "__main__":
    log_audit_finding()
