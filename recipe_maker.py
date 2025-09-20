import pandas as pd

def load_recipes(filepath):
    df = pd.read_csv(filepath, usecols=['Title', 'Ingredients', 'Instructions'])
    df['Ingredients'] = df['Ingredients'].apply(eval)
    return df


def search_recipes(df, search_ingredients):
    search_ingredients = [i.lower() for i in search_ingredients]
    def contains_ingredients(ingredients):
        ingredients_lower = [ing.lower() for ing in ingredients]
        return all(any(si in ing for ing in ingredients_lower) for si in search_ingredients)
    filtered = df[df['Ingredients'].apply(contains_ingredients)]
    return filtered


def display_recipe(recipe):
    print(f"Title: {recipe['Title']}\n")
    print("Ingredients:")
    for ingredient in recipe['Ingredients']:
        print(f"- {ingredient}")
    print("\nInstructions:")
    print(recipe['Instructions'])
    print("\n" + "="*40 + "\n")

def main():
    filepath = "13k-recipes.csv"  
    print("Loading recipes dataset...")
    recipes_df = load_recipes(filepath)
    print(f"Loaded {len(recipes_df)} recipes.\n")

    while True:
        user_input = input("Enter ingredient(s) separated by commas (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        ingredients = [i.strip() for i in user_input.split(',') if i.strip()]
        results = search_recipes(recipes_df, ingredients)
        if results.empty:
            print("No matching recipes found.\n")
            continue
        print(f"Found {len(results)} matching recipes. Showing top 3:\n")
        for idx, row in results.head(3).iterrows():
            display_recipe(row)

if __name__ == "__main__":
    main()
