import pandas as pd
import random

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


def list_all_titles(df):
    print("Recipe Titles:")
    for idx, title in enumerate(df['Title'], 1):
        print(f"{idx}. {title}")
    print("")

def search_by_title(df, title_query):
    matches = df[df['Title'].str.lower() == title_query.lower()]
    return matches

def get_random_recipe(df):
    idx = random.randint(0, len(df) - 1)
    return df.iloc[idx]

def search_by_keyword(df, keyword):
    keyword = keyword.lower()
    filtered = df[df['Instructions'].str.lower().str.contains(keyword) |
                 df['Title'].str.lower().str.contains(keyword)]
    return filtered

def count_ingredient_frequency(df, top_n=10):
    from collections import Counter
    all_ingredients = [ing.lower() for ingredients in df['Ingredients'] for ing in ingredients]
    freq = Counter(all_ingredients)
    print(f"Top {top_n} most common ingredients:")
    for ingredient, count in freq.most_common(top_n):
        print(f"{ingredient}: {count}")
    print("")

def export_results_to_csv(results_df, filename="recipes_found.csv"):
    results_df.to_csv(filename, index=False)
    print(f"{len(results_df)} recipes exported to '{filename}'.")


def main():
    filepath = "13k-recipes.csv"
    print("Loading recipes dataset...")
    recipes_df = load_recipes(filepath)
    print(f"Loaded {len(recipes_df)} recipes.\n")

    while True:
        print("Options:\n"
              "1. Search by ingredients\n"
              "2. List all recipe titles\n"
              "3. Search by exact title\n"
              "4. Get a random recipe\n"
              "5. Search by keyword\n"
              "6. Ingredient frequency analysis\n"
              "7. Export last search to CSV\n"
              "Type 'exit' to quit.")
        user_choice = input("Enter option: ").strip()
        last_results = None

        if user_choice == '1':
            user_input = input("Enter ingredient(s), comma-separated: ")
            ingredients = [i.strip() for i in user_input.split(',') if i.strip()]
            results = search_recipes(recipes_df, ingredients)
            last_results = results
            if results.empty:
                print("No matching recipes found.\n")
            else:
                print(f"Found {len(results)} matching recipes. Showing top 3:\n")
                for idx, row in results.head(3).iterrows():
                    display_recipe(row)

        elif user_choice == '2':
            list_all_titles(recipes_df)

        elif user_choice == '3':
            title_query = input("Enter the exact recipe title: ")
            results = search_by_title(recipes_df, title_query)
            last_results = results
            if results.empty:
                print("No recipe found with that title.\n")
            else:
                for idx, row in results.iterrows():
                    display_recipe(row)

        elif user_choice == '4':
            recipe = get_random_recipe(recipes_df)
            display_recipe(recipe)

        elif user_choice == '5':
            keyword = input("Enter keyword to search in titles or instructions: ")
            results = search_by_keyword(recipes_df, keyword)
            last_results = results
            if results.empty:
                print("No recipes found with that keyword.\n")
            else:
                print(f"Found {len(results)} matching recipes. Showing top 3:\n")
                for idx, row in results.head(3).iterrows():
                    display_recipe(row)

        elif user_choice == '6':
            try:
                n = int(input("Show top how many ingredients? [default 10]: ") or 10)
            except Exception:
                n = 10
            count_ingredient_frequency(recipes_df, top_n=n)

        elif user_choice == '7':
            if last_results is not None and not last_results.empty:
                filename = input("Enter filename (default recipes_found.csv): ").strip() or "recipes_found.csv"
                export_results_to_csv(last_results, filename=filename)
            else:
                print("No recent search to export.\n")

        elif user_choice.lower() == 'exit':
            break
        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main()
