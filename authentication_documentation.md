# Authentication System Documentation

## Overview

The authentication system uses token-based authentication provided by Django REST framework. Users can register, log in, and manage their profiles. Upon successful registration or login, a token is generated and returned to the user. This token is used to authenticate subsequent requests.

## Endpoints

### 1. Register

- **URL:** `/api/user/register/`
- **Method:** `POST`
- **Request Parameters:**

  ```json
  {
    "username": "string",
    "password": "string",
    "email": "string"
  }
  ```

- **Response:** A JSON object containing a token.

  ```json
  {
    "token": "string"
  }
  ```

### 2. Login

- **URL:** `/api/user/login/`
- **Method:** `POST`
- **Request Parameters:**

  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```

- **Response 201 Created:** A JSON object containing a token.

  ```json
  {
    "token": "string"
  }
  ```
