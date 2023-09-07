class RecipeBook:
    def __init__(self):
        self.recipes = {}

    def add_recipe(self, name, ingredients, instructions):
        self.recipes[name] = {'ingredients': ingredients, 'instructions': instructions}
        print(f"Recipe '{name}' added to the book.")

    def get_recipe(self, name):
        recipe = self.recipes.get(name)
        if recipe:
            print(f"Recipe: {name}")
            print("Ingredients:")
            for ingredient in recipe['ingredients']:
                print("- " + ingredient)
            print("Instructions:")
            for step, instruction in enumerate(recipe['instructions'], start=1):
                print(f"{step}. {instruction}")
        else:
            print(f"Recipe '{name}' not found in the book.")

    def list_recipes(self):
        print("Recipes in the book:")
        for recipe_name in self.recipes:
            print("- " + recipe_name)


def main():
    recipe_book = RecipeBook()

    while True:
        print("\nRecipe Book Menu:")
        print("1. Add Recipe")
        print("2. Get Recipe")
        print("3. List Recipes")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(',')
            instructions = []
            print("Enter instructions (Enter 'done' when finished):")
            while True:
                step = input()
                if step.lower() == 'done':
                    break
                instructions.append(step)
            recipe_book.add_recipe(name, ingredients, instructions)
        elif choice == '2':
            name = input("Enter recipe name: ")
            recipe_book.get_recipe(name)
        elif choice == '3':
            recipe_book.list_recipes()
        elif choice == '4':
            print("Exiting Recipe Book.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
