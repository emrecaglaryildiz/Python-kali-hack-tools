def analyze_attack_logs(log_file):
    with open(log_file, 'r') as file:
        logs = file.readlines()
    for log in logs:
        if "FAILED" in log or "ERROR" in log:
            print(f"Potential issue detected: {log}")

log_file = "attack_logs.txt"
analyze_attack_logs(log_file)
