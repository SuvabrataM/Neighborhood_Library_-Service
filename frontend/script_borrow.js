const BASE_URL = "http://127.0.0.1:8000";


// ---------------- BORROW BOOK ----------------

async function borrowBook() {

    const borrowData = {

        member_id: parseInt(
            document.getElementById("borrow_member_id").value
        ),

        book_id: parseInt(
            document.getElementById("borrow_book_id").value
        )
    };

    const response = await fetch(`${BASE_URL}/borrow/`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(borrowData)
    });

    const data = await response.json();

    if (!response.ok) {
        alert(data.detail);
        return;
    }

    alert("Book Borrowed Successfully");

    console.log(data);
}


// ---------------- RETURN BOOK ----------------

async function returnBook() {

    const recordId =
        document.getElementById("return_record_id").value;

    const response = await fetch(
        `${BASE_URL}/borrow/return/${recordId}`,
        {
            method: "PUT"
        }
    );

    const data = await response.json();

    if (!response.ok) {
        alert(data.detail);
        return;
    }

    alert("Book Returned Successfully");

    console.log(data);
}


// ---------------- CURRENT HOLDINGS ----------------

async function getCurrentHoldings() {

    const memberId =
        document.getElementById("holding_member_id").value;

    const response = await fetch(
        `${BASE_URL}/borrow/member_currentholding/${memberId}`
    );

    const data = await response.json();

    const tableBody =
        document.querySelector("#borrowTable tbody");

    tableBody.innerHTML = "";

    data.forEach(record => {

        tableBody.innerHTML += `
            <tr>
                <td>${record.id}</td>
                <td>${record.member_id}</td>
                <td>${record.book_id}</td>
                <td>${record.book_title}</td>
                <td>${record.borrowed_at}</td>
                <td>${record.returned_at ?? "Not Returned"}</td>
            </tr>
        `;
    });
}


// ---------------- BORROW HISTORY ----------------

async function getBorrowHistory() {

    const memberId =
        document.getElementById("history_member_id").value;

    const response = await fetch(
        `${BASE_URL}/borrow/history/${memberId}`
    );

    const data = await response.json();

    const tableBody =
        document.querySelector("#borrowTable tbody");

    tableBody.innerHTML = "";

    data.forEach(record => {

        tableBody.innerHTML += `
            <tr>
                <td>${record.id}</td>
                <td>${record.member_id}</td>
                <td>${record.book_id}</td>
                <td>${record.book_title}</td>
                <td>${record.borrowed_at}</td>
                <td>${record.returned_at ?? "Not Returned"}</td>
            </tr>
        `;
    });
}