# Day 4 Python - Evaluation Logic

def evaluate_response(response):
    score = 0
    
    if len(response) > 20:
        score += 1
    if "because" in response.lower():
        score += 1
    if "." in response:
        score += 1
    
    return score

print(evaluate_response("Water is important because it supports life."))
