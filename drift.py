def detect_drift(data: dict) -> bool:
    """
    Simple drift detection placeholder.
    This checks if the average transaction amount crosses a threshold.
    Replace with real statistical drift detection later.
    """

    # Ensure transactions exist
    if "transactions" not in data:
        return False

    transactions = data["transactions"]
    if not isinstance(transactions, list) or len(transactions) == 0:
        return False

    # Extract amounts
    amounts = []
    for t in transactions:
        if "amount" in t:
            amounts.append(t["amount"])

    if not amounts:
        return False

    avg_amount = sum(amounts) / len(amounts)

    # Example drift rule:
    # If average transaction amount > 5000, consider it drift.
    return avg_amount > 5000
