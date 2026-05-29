const BASE_URL = "http://127.0.0.1:8000";

// ---------------- ADD BOOK ----------------

async function addBook() {

    const book = {

        title: document.getElementById("title").value,
        author: document.getElementById("author").value,
        isbn: document.getElementById("isbn").value,

        total_copies: parseInt(
            document.getElementById("total_copies").value
        ),

        available_copies: parseInt(
            document.getElementById("available_copies").value
        )
    };

    const response = await fetch(
        `${BASE_URL}/books/`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(book)
        }
    );

    const data = await response.json();

    alert("Book Added Successfully");

    console.log(data);

    getBooks();
}

// ---------------- UPDATE BOOK ----------------

async function updateBook() {

    const bookId =
        document.getElementById("update_book_id").value;

    const updatedBook = {};

    const title =
        document.getElementById("update_title").value;

    const author =
        document.getElementById("update_author").value;

    const isbn =
        document.getElementById("update_isbn").value;

    const totalCopies =
        document.getElementById("update_total_copies").value;

    const availableCopies =
        document.getElementById("update_available_copies").value;

    if (title !== "") {
        updatedBook.title = title;
    }

    if (author !== "") {
        updatedBook.author = author;
    }

    if (isbn !== "") {
        updatedBook.isbn = isbn;
    }

    if (totalCopies !== "") {
        updatedBook.total_copies = parseInt(totalCopies);
    }

    if (availableCopies !== "") {
        updatedBook.available_copies = parseInt(availableCopies);
    }

    const response = await fetch(
        `${BASE_URL}/books/${bookId}`,
        {
            method: "PUT",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(updatedBook)
        }
    );

    const data = await response.json();

    alert("Book Updated Successfully");

    console.log(data);

    getBooks();
}

// ---------------- GET ALL BOOKS ----------------

async function getBooks() {

    const response = await fetch(
        `${BASE_URL}/books/`
    );

    const books = await response.json();

    displayBooks(books);
}

// ---------------- DISPLAY BOOKS ----------------

function displayBooks(books) {

    const tableBody =
        document.querySelector("#booksTable tbody");

    tableBody.innerHTML = "";

    books.forEach(book => {

        tableBody.innerHTML += `
            <tr>
                <td>${book.id}</td>
                <td>${book.title}</td>
                <td>${book.author}</td>
                <td>${book.isbn}</td>
                <td>${book.total_copies}</td>
                <td>${book.available_copies}</td>
            </tr>
        `;
    });
}

// ---------------- SEARCH BOOK BY ID ----------------

async function searchBookById() {

    const id =
        document.getElementById("search_book_id").value;

    const response = await fetch(
        `${BASE_URL}/books/search/id/${id}`
    );

    const book = await response.json();

    displayBooks([book]);
}

// ---------------- SEARCH BOOK BY TITLE ----------------

async function searchBookByTitle() {

    const title =
        document.getElementById("search_title").value;

    const response = await fetch(
        `${BASE_URL}/books/search/title/${title}`
    );

    const book = await response.json();

    displayBooks([book]);
}

// ---------------- SEARCH BOOKS BY AUTHOR ----------------

async function searchBooksByAuthor() {

    const author =
        document.getElementById("search_author").value;

    const response = await fetch(
        `${BASE_URL}/books/search/author/${author}`
    );

    const books = await response.json();

    displayBooks(books);
}

// ---------------- DELETE BOOK BY ID ----------------

async function deleteBookById() {

    const id =
        document.getElementById("delete_book_id").value;

    const response = await fetch(
        `${BASE_URL}/books/delete/id/${id}`,
        {
            method: "DELETE"
        }
    );

    const data = await response.json();

    alert(data.message);

    getBooks();
}

// ---------------- DELETE BOOK BY TITLE ----------------

async function deleteBookByTitle() {

    const title =
        document.getElementById("delete_book_title").value;

    const response = await fetch(
        `${BASE_URL}/books/delete/title/${title}`,
        {
            method: "DELETE"
        }
    );

    const data = await response.json();

    alert(data.message);

    getBooks();
}

// ---------------- DELETE BOOKS BY AUTHOR ----------------

async function deleteBooksByAuthor() {

    const author =
        document.getElementById("delete_book_author").value;

    const response = await fetch(
        `${BASE_URL}/books/delete/author/${author}`,
        {
            method: "DELETE"
        }
    );

    const data = await response.json();

    alert(data.message);

    getBooks();
}
