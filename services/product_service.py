# =========================
# MOCK PRODUCT SERVICE
# PocketSmart AI
# =========================


def get_home_products(
    room,
    style,
    budget
):

    products = [

        {
            "name": "Modern Study Table",
            "category": "Furniture",
            "price": 2499,
            "source": "Amazon",
            "link": "https://www.amazon.in/"
        },

        {
            "name": "LED Decorative Lamp",
            "category": "Lighting",
            "price": 899,
            "source": "Flipkart",
            "link": "https://www.flipkart.com/"
        },

        {
            "name": "Minimalist Wall Shelf",
            "category": "Storage",
            "price": 1299,
            "source": "IKEA",
            "link": "https://www.ikea.com/in/en/"
        },

        {
            "name": "Decorative Indoor Plant",
            "category": "Decoration",
            "price": 499,
            "source": "Amazon",
            "link": "https://www.amazon.in/"
        }

    ]


    affordable_products = [

        product

        for product in products

        if product["price"] <= budget

    ]


    return affordable_products