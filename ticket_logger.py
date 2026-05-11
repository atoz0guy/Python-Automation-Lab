# IT Help Desk Ticket Logger

# Purpose: Practice basic Python inputs and file handling for PCEP
import datetime

def create_ticket():
    print("--- AtoZ IT Support Ticket System ---")
    
    # Using input() - a core PCEP concept
    customer = input("Enter Customer Name: ")
    issue = input("Describe the Technical Issue: ")
    
    # Get current time for the log
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # File handling: 'a' means append (add to the end)
    try:
        with open("ticket_log.txt", "a") as log_file:
            log_file.write(f"[{timestamp}] {customer}: {issue}\n")
        print("\n✅ Success: Ticket has been logged to ticket_log.txt")
    except Exception as e:
        print(f"❌ Error: Could not save ticket. {e}")

if __name__ == "__main__":
    create_ticket()
