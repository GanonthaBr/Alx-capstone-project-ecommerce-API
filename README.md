# My Cosmetic Natural Project

## Setup Instructions

Follow these steps to set up the Django project on your local machine.

### Prerequisites

- Python 3.x
- pip
- virtualenv

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/GanonthaBr/alx-Backend-Django-capstone-project.git
   cd mycosmeticnaturalproject
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply the migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

8. **Access the project:**
   Open your web browser and go to `http://127.0.0.1:8000/`.

### Additional Notes

- To deactivate the virtual environment, simply run:

  ```bash
  deactivate
  ```

- Make sure to configure your database settings in `settings.py` if you are using a database other than SQLite.

- For any additional configuration, refer to the Django documentation.

ALL ENDPOINTS
Users:
[POST] api/user/register/ :Register a new user, returns auth token
Response Sample:
{
"token": "6dc8aa7b4c33a8b9305b20b8c48237572aeae1f2"
}
[POST] api/user/login/ :Login a new user with credentials, returns auth token
Response Sample:
{
"token": "6dc8aa7b4c33a8b9305b20b8c48237572aeae1f2"
}
[GET] api/user/profile :Display details on the current authenticated user
Response Sample:
{
"id": 1,
"username": "Ganontha",
"email": "BGanontha@gmail.com",
"bio": "Software Developer",
"profile_picture": "/profile_pic/countryside-women-discussing-out-field.jpg",
"phone": "+22789853603"
}
[PUT] api/user/profile/ :Update details on this current user
Response Sample:
{
"id": 1,
"username": "Ganontha",
"email": "BGanontha@gmail.com",
"bio": "Software Developer",
"profile_picture": "/profile_pic/countryside-women-discussing-out-field.jpg",
"phone": "+22789853603"
}

PRODUCTS

[GET] api/products: Get list of all products, authentication not required
Response sample:
{
"count": 3,
"next": null,
"previous": null,
"results": [
{
"id": 1,
"name": "Creme AloeVera",
"description": "Creme de peau important en periode de fraicheur",
"price": "2500.00",
"stock_quantity": 20,
"image": "http://127.0.0.1:8000/products/banner_Ad_1.jpg",
"created_date": "2024-12-24T14:23:38.619504Z",
"category": 1
},
{
"id": 2,
"name": "Huile chebe",
"description": "Huile de chebe pourvos barbesetchevuex",
"price": "3500.00",
"stock_quantity": 20,
"image": "http://127.0.0.1:8000/products/banner_Ad_1_zFacfhh.jpg",
"created_date": "2024-12-24T14:24:53.097219Z",
"category": 2
},
{
"id": 3,
"name": "Huile corne",
"description": "Huile de chebe pourvos barbesetchevuex",
"price": "3500.00",
"stock_quantity": 20,
"image": "http://127.0.0.1:8000/products/banner_Ad_1_zuJtyZF.jpg",
"created_date": "2024-12-24T14:25:00.666582Z",
"category": 2
}
]
}
[POST] api/products/ : Add a new product, authentication required
Response sample:
{
"id": 3,
"name": "Huile corne",
"description": "Huile de chebe pourvos barbesetchevuex",
"price": "3500.00",
"stock_quantity": 20,
"image": "http://127.0.0.1:8000/products/banner_Ad_1_zuJtyZF.jpg",
"created_date": "2024-12-24T14:25:00.666582Z",
"category": 2
}
[PUT] api/products/<int:product_id>/ : Update a product with product_id, auth required
[DELETE] api/products/<int:product_id>/ : Remove a product with product_id, auth required

WISHLIST
[POST] api/wishlist/add/<int:product_id>/ :add a product to wish list using its id, auth required
Response Sample:
{
"id": 5,
"created_date": "2024-12-28T14:32:56.916208Z",
"product": 2,
"user": 1
}

[GET] api/wishlist :Display all items in the wishlist, auth required
Response Sample:
[
{
"id": 3,
"created_date": "2024-12-24T15:45:16.270467Z",
"product": 3,
"user": 1
},
{
"id": 5,
"created_date": "2024-12-28T14:32:56.916208Z",
"product": 2,
"user": 1
}
]
[DELETE] /api/wishlist/<int:product_id> :Remove item from wish list with its ID

CART
[GET] /api/cart :List all items from cart associated to this user
Response Sample:
[
{
"product": 2,
"quantity": 200,
"cart": 9
},
{
"product": 3,
"quantity": 2,
"cart": 9
}
]

[POST] /api/cart/add/<int:product_id> :Add product to the cart
Response Sample:
{
"product": 2,
"quantity": 201,
"cart": 9
}

[DELETE] /api/cart/remove/<int:product_id> :Remove this product from the cart
Response Sample:

[UPDATE] /api/cart/update/<int:product_id>/?quantity=number :Update the quantity of this product in the cart
Response Sample:
?quantity=20
{
"product": 3,
"quantity": 20,
"cart": 9
}
