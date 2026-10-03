def create_ticket(description: str, category: str, priority: str) -> dict:
    new_ticket = {
        "description": description,
        "category": category,
        "priority": priority,
    }

    return new_ticket


