
# -------------------- RECIPE SELECTION --------------------

print("What do you crave right now?")

print(
    "Brownies [D01]",
    "Chocolate Chip Cookies [D02]",
    "Gulab Jamun [D03]",
    "Chicken Biryani [M01]",
    sep="\n"
)

food_code = input("Type the recipe code and let's get cookin'! ")

recipes = {
    "D01": "brownies.txt",
    "D02": "chocolate_chip_cookies.txt",
    "D03": "gulab_jamun.txt",
    "M01": "chicken_biryani.txt"
}

servings = int(input("How many people are you cooking for? "))


# -------------------- INGREDIENT EXTRACTION --------------------

def extract_ingredients(filename):

    ingredients = []
    inside_ingredients = False

    with open(filename, "r") as file:

        for line in file:

            line = line.strip()

            if "Ingredients:" in line:
                inside_ingredients = True
                continue

            if "----------" in line:
                inside_ingredients = False

            if inside_ingredients and line:
                ingredients.append(line.split())

    # Convert numerical quantities from strings to integers

    for ingredient in ingredients:
        for i in range(len(ingredient)):

            if ingredient[i].isdigit():
                ingredient[i] = int(ingredient[i])

    return ingredients


# -------------------- SERVING SIZE MULTIPLIER --------------------

def multiply_ingredients(ingredients, servings):

    if servings > 1:

        for ingredient in ingredients:

            for i in range(len(ingredient)):

                if type(ingredient[i]) == int:
                    ingredient[i] = ingredient[i] * servings

    return ingredients


# -------------------- DISPLAY RECIPE --------------------

def display_recipe(filename, ingredients, servings):

    with open(filename, "r") as file:

        display_recipe_text = True

        for line in file:

            if display_recipe_text:

                if "serving size:" in line:
                    print("Serving size:", servings)

                elif "Ingredients:" in line:

                    print(line, end="")

                    for ingredient in ingredients:
                        print(*ingredient)

                    display_recipe_text = False

                else:
                    print(line, end="")

            elif "Instructions:" in line:

                display_recipe_text = True
                print(line, end="")


# -------------------- DIETARY RESTRICTIONS --------------------

dietary_keywords = {

    "lactose intolerance": [
        "milk", "butter", "cream", "cheese", "yogurt", "yoghurt"
    ],

    "peanut allergy": [
        "peanut", "groundnut"
    ],

    "gluten allergy": [
        "flour", "wheat", "bread", "pasta", "barley",
        "rye", "couscous", "breadcrumbs"
    ]
}


# -------------------- INGREDIENT SUBSTITUTES --------------------

substitutes = {

    "milk": "oat milk or almond milk",
    "butter": "plant-based butter",
    "cream": "coconut cream",
    "cheese": "vegan cheese",
    "yogurt": "coconut yogurt",
    "yoghurt": "coconut yogurt",

    "peanut": "sunflower seed butter",
    "groundnut": "sunflower seeds",

    "flour": "gluten-free flour blend",
    "wheat": "gluten-free flour blend",
    "bread": "gluten-free bread",
    "pasta": "gluten-free pasta",
    "barley": "quinoa",
    "rye": "gluten-free oats",
    "couscous": "quinoa",
    "breadcrumbs": "gluten-free breadcrumbs"
}


# -------------------- SELECT DIETARY RESTRICTIONS --------------------

def get_dietary_restrictions():

    print("\nDo you have any dietary restrictions?")

    print(
        "1. Lactose intolerance",
        "2. Peanut allergy",
        "3. Gluten allergy",
        "0. No restrictions",
        sep="\n"
    )

    restriction_options = {
        "1": "lactose intolerance",
        "2": "peanut allergy",
        "3": "gluten allergy"
    }

    selected_restrictions = []

    choice = input("Enter your choice (e.g. 1,3): ")

    choices = choice.split(",")

    for item in choices:

        item = item.strip()

        if item in restriction_options:
            selected_restrictions.append(restriction_options[item])

    return selected_restrictions


# -------------------- CHECK INGREDIENTS AND SUGGEST SUBSTITUTES --------------------

def suggest_substitutes(ingredients, selected_restrictions):

    conflicts = []
    suggested_substitutes = []

    for ingredient in ingredients:

        ingredient_name = " ".join(str(item) for item in ingredient).lower()

        for restriction in selected_restrictions:

            for keyword in dietary_keywords[restriction]:

                if keyword in ingredient_name:

                    conflicts.append(ingredient_name)

                    suggested_substitutes.append([
                        ingredient_name,
                        substitutes[keyword]
                    ])

                    break

    print("\nDietary Restriction Results:")

    if len(conflicts) == 0:

        print("No matching ingredients found. Safe to cook!")

    else:

        print("The following ingredients need to be substituted:")

        for original, replacement in suggested_substitutes:

            print(
                "- " + original +
                " --> Replace with: " + replacement
            )


# -------------------- MAIN PROGRAM --------------------

ingredients = extract_ingredients(recipes[food_code])

ingredients = multiply_ingredients(ingredients, servings)

print("\n-------------------- YOUR RECIPE --------------------\n")

display_recipe(recipes[food_code], ingredients, servings)

selected_restrictions = get_dietary_restrictions()

suggest_substitutes(ingredients, selected_restrictions)
