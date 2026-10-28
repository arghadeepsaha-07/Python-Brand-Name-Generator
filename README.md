# Brand Name Generator

A Python command-line application that suggests brand names through interactive category selection.

## Features
- **Interactive Menu:** Choose AI/Tech, Food/Beverages, or Fitness.
- **Random Selection:** Displays 10 brand names from the selected category.
- **Flexible Input:** Accepts menu numbers and supported category keywords.
- **JSON History:** Saves selected brand names and categories in `brand_category.json`.
- **Duplicate Prevention:** Avoids saving identical brand-category records.

## Technologies
- Python 3
- `random` module
- `json` module

## Installation and Usage

1. Install Python 3.
2. Clone this repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/Brand_Name_Generator.git
   ```

3. Open the project folder.
4. Run the application:

   ```bash
   python main.py
   ```

5. Select a category and view the suggested names.

## Data Storage

The application stores selected names and categories in `brand_category.json`. Existing records are loaded before new records are saved.

## Future Improvements
- Generate original brand names by combining words.
- Save favorite names separately.
- View and delete saved records.
- Add automated tests and error handling.

## Project Status

Beginner-level Python project under development.

**Learning Outcomes:** Lists, loops, functions, conditional statements, random selection, file handling, and JSON serialization.
