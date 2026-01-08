# ABOUTME: Stores curated cooking recipes for the product pack.
# ABOUTME: Provides structured recipe data for rendering outputs.
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Recipe:
    title: str
    servings: str
    ingredients: list[str]
    steps: list[str]


def get_popular_recipes() -> list[Recipe]:
    return [
        Recipe(
            title="Spaghetti Carbonara",
            servings="4 servings",
            ingredients=[
                "1 lb (450 g) spaghetti",
                "4 oz (115 g) guanciale or pancetta, diced",
                "3 large eggs + 1 yolk",
                "1 cup (90 g) finely grated Pecorino Romano (or half pecorino/half parmesan)",
                "Lots of black pepper",
                "Salt",
            ],
            steps=[
                "Boil pasta in salted water until al dente.",
                "Crisp guanciale/pancetta in a skillet over medium heat; turn off heat when done.",
                "Whisk eggs + yolk + cheese + heavy black pepper in a bowl.",
                "Reserve 1 cup pasta water, drain pasta.",
                "Toss hot pasta in the skillet with the pork. Off heat, add egg/cheese mix, tossing fast. Add splashes of pasta water until glossy and creamy (not scrambled).",
                "Serve with more pepper and cheese.",
            ],
        ),
        Recipe(
            title="Chicken Tikka Masala",
            servings="4 servings",
            ingredients=[
                "1.5 lb (680 g) chicken thighs, bite-size",
                "1 cup plain yogurt",
                "3 cloves garlic, grated",
                "1 Tbsp grated ginger",
                "2 tsp garam masala, 1 tsp cumin, 1 tsp paprika, 1 tsp salt",
                "2 Tbsp oil or ghee",
                "1 onion, diced",
                "2 Tbsp tomato paste",
                "1 can (14 oz) crushed tomatoes",
                "1/2–1 cup heavy cream (or coconut milk)",
                "Cilantro, rice/naan",
            ],
            steps=[
                "Marinate chicken in yogurt + garlic + ginger + spices for 30 min (or overnight).",
                "Broil or pan-sear chicken until browned (it can finish in sauce).",
                "Sauté onion in oil/ghee until soft. Add tomato paste 1 min.",
                "Add crushed tomatoes; simmer 10–15 min.",
                "Stir in cream; add chicken; simmer until cooked through.",
                "Finish with cilantro; serve with rice/naan.",
            ],
        ),
        Recipe(
            title="Smash Burgers",
            servings="4 burgers",
            ingredients=[
                "1.25 lb (570 g) 80/20 ground beef",
                "Salt + pepper",
                "4 potato buns",
                "4–8 slices American cheese",
                "Thin-sliced onion (optional)",
                "Sauce: mayo + ketchup + diced pickles (or your favorite)",
            ],
            steps=[
                "Divide beef into 4 loose balls (don’t compact).",
                "Heat cast iron very hot. Toast buns; set aside.",
                "Add a ball, smash hard with a spatula (use parchment) for 10 seconds. Salt.",
                "Cook 60–90 sec until edges crisp; flip; add onions (optional) + cheese; cook 45–60 sec.",
                "Assemble with sauce, pickles, lettuce/tomato if you want.",
            ],
        ),
        Recipe(
            title="Chicken Fajitas",
            servings="4 servings",
            ingredients=[
                "1.5 lb chicken breast/thigh strips",
                "2 bell peppers + 1 onion, sliced",
                "2 Tbsp oil",
                "Spice mix: 2 tsp chili powder, 1 tsp cumin, 1 tsp smoked paprika, 1/2 tsp garlic powder, salt",
                "1 lime",
                "Tortillas",
            ],
            steps=[
                "Toss chicken with half the oil + spices; rest 10 min.",
                "Sear chicken in a hot pan until browned and cooked; remove.",
                "Cook peppers/onions with remaining oil; salt; keep some bite.",
                "Return chicken; squeeze lime; serve in warm tortillas.",
            ],
        ),
        Recipe(
            title="Weeknight Fried Rice",
            servings="4 servings",
            ingredients=[
                "4 cups cooked day-old rice (cold)",
                "2 eggs",
                "2 Tbsp neutral oil",
                "1 cup diced carrots/peas (frozen ok)",
                "3 cloves garlic, minced",
                "3 Tbsp soy sauce",
                "1 tsp sesame oil (optional)",
                "Green onions",
            ],
            steps=[
                "Scramble eggs in a hot wok/pan with a little oil; set aside.",
                "Add oil; cook veggies 2–3 min; add garlic 30 sec.",
                "Add rice; break up clumps; stir-fry until hot and slightly toasted.",
                "Add soy sauce around the edges; toss. Add eggs back.",
                "Finish with sesame oil + green onions.",
            ],
        ),
        Recipe(
            title="Classic Tacos (Ground Beef)",
            servings="8 tacos",
            ingredients=[
                "1 lb ground beef",
                "1/2 onion, diced",
                "2 tsp chili powder, 1 tsp cumin, 1/2 tsp oregano, salt",
                "1/2 cup water",
                "Tortillas",
                "Toppings: salsa, shredded lettuce, cheese, cilantro, lime",
            ],
            steps=[
                "Brown beef with onion; drain excess fat if needed.",
                "Add spices + water; simmer 5–8 min until saucy.",
                "Warm tortillas; fill; top.",
            ],
        ),
        Recipe(
            title="Caesar Salad",
            servings="4 servings",
            ingredients=[
                "1 large romaine, chopped",
                "Croutons",
                "Parmesan",
                "Dressing: 1 egg yolk (or 2 Tbsp mayo)",
                "1 small garlic clove, grated",
                "2 tsp Dijon",
                "2 Tbsp lemon juice",
                "2–4 anchovy fillets, mashed (or 1 tsp Worcestershire)",
                "1/3 cup olive oil",
                "Black pepper, salt",
            ],
            steps=[
                "Whisk dressing base; slowly stream in olive oil until creamy.",
                "Toss romaine with dressing; add croutons + parmesan.",
            ],
        ),
        Recipe(
            title="Pad Thai",
            servings="3–4 servings",
            ingredients=[
                "8 oz rice noodles",
                "2 Tbsp oil",
                "2 eggs",
                "8 oz shrimp or chicken (optional)",
                "2 cups bean sprouts",
                "3 green onions",
                "Crushed peanuts, lime, cilantro",
                "Sauce: 3 Tbsp fish sauce",
                "2 Tbsp tamarind paste (or 3 Tbsp lime + 1 Tbsp brown sugar as a backup)",
                "2–3 Tbsp brown sugar",
                "1–2 Tbsp soy sauce (optional)",
            ],
            steps=[
                "Soak noodles in warm water until pliable; drain.",
                "Stir-fry protein (if using); push aside; scramble eggs.",
                "Add noodles + sauce; toss until glossy and tender (add a splash of water if dry).",
                "Toss in sprouts + green onions briefly; serve with peanuts + lime.",
            ],
        ),
        Recipe(
            title="Chocolate Chip Cookies",
            servings="about 24",
            ingredients=[
                "1 cup (226 g) butter, softened",
                "3/4 cup brown sugar + 1/2 cup white sugar",
                "2 eggs",
                "2 tsp vanilla",
                "2 1/4 cups all-purpose flour",
                "1 tsp baking soda",
                "1 tsp salt",
                "2 cups chocolate chips",
            ],
            steps=[
                "Heat oven to 350°F (175°C).",
                "Cream butter + sugars. Beat in eggs + vanilla.",
                "Mix flour + baking soda + salt; combine. Fold in chips.",
                "Scoop onto sheet; bake 10–12 min until edges set.",
                "Cool 5 min on tray, then rack.",
            ],
        ),
        Recipe(
            title="Banana Bread",
            servings="1 loaf",
            ingredients=[
                "3 very ripe bananas, mashed",
                "1/2 cup melted butter (or neutral oil)",
                "3/4 cup sugar (less if bananas are super sweet)",
                "2 eggs",
                "1 tsp vanilla",
                "1 1/2 cups flour",
                "1 tsp baking soda",
                "1/2 tsp salt",
                "Optional: 1/2 tsp cinnamon, nuts, chocolate",
            ],
            steps=[
                "Heat oven to 350°F (175°C). Grease a loaf pan.",
                "Whisk bananas + butter + sugar + eggs + vanilla.",
                "Fold in dry ingredients just until combined.",
                "Bake 50–60 min until a toothpick comes out mostly clean.",
                "Cool 15 min in pan, then turn out.",
            ],
        ),
    ]
