# API Endpoints Documentation

## Accounts Endpoints

### Register

- **URL**: `/api/user/register/`
- **Method**: `POST`
- **Request Parameters**:
  ```json
  {
    "username": "string",
    "password": "string",
    "email": "string"
  }
  ```
- **Expected Response**:
  - 201 Created
    ```json
    {
      "token": "string"
    }
    ```
  - 400 Bad Request
    ```json
    {
      "errors": "object"
    }
    ```

### Login

- **URL**: `/api/user/login/`
- **Method**: `POST`
- **Request Parameters**:
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Expected Response**:
  - 201 Created
    ```json
    {
      "token": "string"
    }
    ```
  - 400 Bad Request
    ```json
    {
      "errors": "object"
    }
    ```

### Profile

- **URL**: `/api/user/profile/`
- **Method**: `GET`, `PUT`
- **Request Parameters** (GET): None
- **Request Parameters** (PUT):
  ```json
  {
    "username": "string",
    "email": "string",
    "bio": "string",
    "profile_picture": "string",
    "phone": "string"
  }
  ```
- **Expected Response**:
  - GET 200 OK:
    ```json
    {
      "id": "integer",
      "username": "string",
      "email": "string",
      "bio": "string",
      "profile_picture": "string",
      "phone": "string"
    }
    ```
  - PUT 202 Created
    ```json
    {
      "id": "integer",
      "username": "string",
      "email": "string",
      "bio": "string",
      "profile_picture": "string",
      "phone": "string"
    }
    ```
  - 400 Bad Request
    ```json
    {
      "errors": "object"
    }
    ```

## Products Endpoints

### Categories

- **URL**: `/api/products/categories/`
- **Method**: `GET`, `POST`
- **Request Parameters** (GET): None
- **Request Parameters** (POST):
  ```json
  {
    "name": "string"
  }
  ```
- **Expected Response**:
  - GET 200 OK:
    ```json
    [
      {
        "id": "integer",
        "name": "string"
      }
    ]
    ```
  - POST 201 Created:
    ```json
    {
      "id": "integer",
      "name": "string"
    }
    ```
  - 400 Bad Request
    ```json
    {
      "errors": "object"
    }
    ```

### Products

- **URL**: `/api/products/`
- **Method**: `GET`, `POST`
- **Request Parameters** (GET): Query Parameters: category, min_price, max_price
- **Request Parameters** (POST):
  ```json
  {
    "name": "string",
    "category": "integer",
    "price": "decimal"
  }
  ```
- **Expected Response**:
  - GET 200 OK:
    ```json
    [
      {
        "id": "integer",
        "name": "string",
        "category": "integer",
        "price": "decimal"
      }
    ]
    ```
  - POST 201 Created:
    ```json
    {
      "id": "integer",
      "name": "string",
      "category": "integer",
      "price": "decimal"
    }
    ```
  - 400 Bad Request
    ```json
    {
      "errors": "object"
    }
    ```

## Wishlist

### Wishlist

- **URL**: `/api/wishlist/`
- **Method**: `GET`, `POST`
- **Request Parameters** (GET): None
- **Expected Response**:
  - GET 200 OK:
    ```json
    [
      {
        "id": "integer",
        "name": "string",
        "category": "integer",
        "price": "decimal"
      }
    ]
    ```

### Add to Wishlist

- **URL**: `/api/wishlist/add/<int:product_id>/`
- **Method**: `POST`
- **Request Parameters**: None
- **Expected Response**:
  - POST 201 Created:
    ```json
    {
      "message": "Product added to wishlist"
    }
    ```
  - 400 Bad Request:
    ```json
    {
      "errors": "object"
    }
    ```

### Remove from Wishlist

- **URL**: `/api/wishlist/remove/<int:product_id>/`
- **Method**: `DELETE`
- **Request Parameters**: None
- **Expected Response**:
  - DELETE 204 No Content:
    ```json
    {
      "message": "Product removed from wishlist"
    }
    ```
  - 400 Bad Request:
    ```json
    {
      "errors": "object"
    }
    ```

## Cart Endpoints

### Cart Details

- **URL**: `/api/cart/`
- **Method**: `GET`
- **Request Parameters**: None
- **Expected Response**:
  - GET 200 OK:
    ```json
    [
      {
        "id": "integer",
        "product": "integer",
        "quantity": "integer"
      }
    ]
    ```

### Add to Cart

- **URL**: `/api/cart/add/<int:product_id>/`
- **Method**: `POST`
- **Request Parameters**: None
- **Expected Response**:
  - POST 201 Created:
    ```json
    {
      "id": "integer",
      "product": "integer",
      "quantity": "integer"
    }
    ```
  - 400 Bad Request:
    ```json
    {
      "errors": "object"
    }
    ```

### Remove from Cart

- **URL**: `/api/cart/remove/<int:product_id>/`
- **Method**: `DELETE`
- **Request Parameters**: None
- **Expected Response**:
  - DELETE 204 No Content:
    ```json
    {
      "message": "Product removed from cart"
    }
    ```
  - 400 Bad Request:
    ```json
    {
      "errors": "object"
    }
    ```

### Update Cart Item

- **URL**: `/api/cart/update/<int:product_id>/`
- **Method**: `PUT`
- **Request Parameters**: `quantity` (integer)
- **Expected Response**:
  - PUT 202 Accepted:
    ```json
    {
      "id": "integer",
      "product": "integer",
      "quantity": "integer"
    }
    ```
  - 400 Bad Request:
    ```json
    {
      "errors": "object"
    }
    ```
