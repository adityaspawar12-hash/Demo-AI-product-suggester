def suggest_phone(budget, purpose):
    if budget <= 15000:

        if purpose == "gaming":
            return ["Redmi Note 12", "Realme Narzo 50"]

        elif purpose == "camera":
            return ["Samsung M14", "Redmi 12"]

        else:
            return ["Realme C55", "Redmi 12"]

    elif budget <= 30000:

        if purpose == "gaming":
            return ["iQOO Z6 Pro", "Poco X5 Pro"]

        elif purpose == "camera":
            return ["Samsung F54", "Vivo V27"]

        else:
            return ["OnePlus Nord CE 3 Lite", "iQOO Z7"]

    else:

        if purpose == "gaming":
            return ["iPhone 13", "OnePlus 11"]

        elif purpose == "camera":
            return ["Pixel 7", "iPhone 13"]

        else:
            return ["Samsung S21 FE", "OnePlus 11"]


def main():
    print("---- AI Product Suggestion System ----")

    category = input("Enter category (phone): ").lower()
    budget = int(input("Enter your budget: "))
    purpose = input("Enter purpose (gaming/camera/general): ").lower()

    if category == "phone":
        suggestions = suggest_phone(budget, purpose)

        print("\nRecommended Phones:")
        for phone in suggestions:
            print("-", phone)
    else:
        print("Category not available yet.")


main()