# 🥗 Recipe CLI Search Tool

A command-line program to search and explore thousands of recipes from a CSV dataset.  
Supports ingredient search, title search, random selection, keyword finding, and ingredient frequency analysis.

---

## 📚 Features

- **Ingredient Search:** Find recipes containing all specified ingredients.
- **Title Search:** Look up recipes by their exact title.
- **Random Recipe:** Discover a random recipe from the dataset.
- **Keyword Search:** Search titles or instructions for keywords.
- **Ingredient Frequency:** Analyze most common ingredients in the dataset.
- **Export Results:** Save your latest search as a CSV file.
- **Recipe Display:** Print recipes in a user-friendly format.
- **Extensible:** Easily add new features and functions.

---

## 🚀 Getting Started

1. **Clone the repository:**
2. **Install dependencies:**
3. **Prepare your data:**
- Place your `13k-recipes.csv` file in the project directory.
- The CSV should at minimum contain columns: `Title`, `Ingredients`, `Instructions`.
- You may use a small sample for testing.

---

## ⚙️ Usage

Run the program from your terminal:

### Interactive Options

You will see an options menu for:
- Searching by ingredients
- Listing all recipe titles
- Searching by title
- Selecting a random recipe
- Searching by keyword
- Ingredient frequency analysis
- Exporting last search results
- Exiting the program

**Sample ingredient search:**
**Sample keyword search:**
---

## 📁 File Descriptions

- `recipe_finder.py`: Python program containing all recipe search logic.
- `requirements.txt`: Dependencies (`pandas`).
- `13k-recipes.csv`: Your recipe data source.

---

## 🧩 Adding Your Own Recipes

- Add rows to the CSV file with `Title`, `Ingredients` (list or stringified list), and `Instructions`.

---

## 🛠️ Contributing

Contributions and suggestions are welcome!  
Feel free to open issues or pull requests.  
Please ensure your code is well-commented and tested.

---

## 📜 License

This project is released under the MIT License.

---

## 👥 Credits

Developed by Tanveer Singh.  
Inspired by open-source culinary and data science projects.

