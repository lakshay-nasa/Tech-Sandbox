# Book Library API with Ruby on Rails

Welcome to the Book Library API built with Ruby on Rails! This API allows you to manage a collection of books, perform CRUD operations, and interact with the PostgreSQL db using JSON.

## Getting Started

### Prerequisites

- Ruby
- Ruby On Rails
- PostgreSQL
- Postman (for testing API endpoints)

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone <repository-url>

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone <repository-url>
    ```

2. Navigate into the project directory:

   ```bash
   cd book-library-api
    ```

3. Install dependencies:

   ```bash
   bundle install
    ```

4. Set up the PostgreSQL  database:

   ```bash
   rails db:create
   rails db:migrate
    ```

## Running the Application

To start the Rails server, run the following command:

   ```bash
   rails server
```


Once the server is running, you can access the application in your web browser at http://localhost:3000.

## Endpoints

### Retrieve All Books

- **GET** `/api/v1/books`
  - Returns a JSON array of all books in the library.

### Retrieve a Specific Book

- **GET** `/api/v1/books/:id`
  - Returns details of a specific book identified by `:id`.

### Create a New Book

- **POST** `/api/v1/books`
  - Creates a new book with the provided data in the request body.
  - Required parameters: `title`, `description`, `rating`.

### Update a Book

- **PUT** `/api/v1/books/:id`
  - Updates the details of a specific book identified by `:id`.
  - Required parameters: `title`, `description`, `rating`.

### Delete a Book

- **DELETE** `/api/v1/books/:id`
  - Deletes a specific book identified by `:id`.
