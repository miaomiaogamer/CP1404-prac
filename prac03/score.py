def main():
    score = float(input("Enter score: "))
    print(determine(score))


def determine(score):
    if score < 0 or score > 100:
        return "Error"
    elif score >= 90:
        return "Very good"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
