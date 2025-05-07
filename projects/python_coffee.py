liquids = ["Milk", "Water", "Ice Cubes"]
sweetener = ["Brown Sugar", "Granulated Sugar", "Nutella", "Vanilla Extract"]
coffee_type = ["Instant Coffee", "Coffee Powder"]

oneMinuite = {
    "Name": "1-Minute Instant Iced Coffee",
    "Liquids": [
        { "amount": 1, "liquid": liquids[0]},
        { "amount": 2, "liquid": liquids[1]},
        { "amount": 1, "liquid": liquids[2]}
    ],
    "Sweetener": {"amount": 3, "Type": sweetener[0]},
    "Coffee": {"amount": 3, "Type": coffee_type[0]}
}

dalgona = {
    "Name": "Dalgona Coffee",
    "Liquids": [
        { "amount": 1, "liquid": liquids[0]},
        { "amount": 2, "liquid": liquids[1]}
    ],
    "Sweetener": {"amount": 3, "Type": sweetener[1]},
    "Coffee": {"amount": 3, "Type": coffee_type[0]}
}

NutellaIC = {
    "Name": "Nutella Iced Coffee",
    "Liquids": [
        { "amount": 3, "liquid": liquids[0]},
        { "amount": 3, "liquid": liquids[2]}
    ],
    "Sweetener": [
        {"amount": 4, "Type": sweetener[1]},
        {"amount": 4, "Type": sweetener[2]},
        {"amount": 4, "Type": sweetener[3]}],
    "Coffee": {"amount": 2, "Type": coffee_type[1]},

}

def printRecipe(recipe):
    for k, v in recipe.items():
        if isinstance(v, list):
            print(f"{k}:")
            for item in v:
                print(f"  - {item['amount']} Tablespoons of {item.get('liquid', item.get('Type'))}")
        elif isinstance(v, dict):  # If it's a single dictionary (Coffee)
            print(f"{k}: {v['amount']} Tablespoons of {v.get('Type')}")
        else:
            print(f"{k}: {v}")

printRecipe(NutellaIC)
printRecipe(dalgona)
printRecipe(oneMinuite)