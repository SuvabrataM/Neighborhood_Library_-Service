const BASE_URL = "http://127.0.0.1:8000";

// ================= ADD MEMBER =================

async function addMember() {

    const member = {

        name: document.getElementById("member_name").value,
        email: document.getElementById("member_email").value,
        phone: document.getElementById("member_phone").value
    };

    const response = await fetch(`${BASE_URL}/members/`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(member)
    });

    const data = await response.json();

    alert(data.name + " added successfully");
}

// ================= GET MEMBERS =================

async function getMembers() {

    const response = await fetch(`${BASE_URL}/members/`);

    const members = await response.json();

    const tableBody = document.querySelector("#membersTable tbody");

    tableBody.innerHTML = "";

    members.forEach(member => {

        tableBody.innerHTML += `
            <tr>
                <td>${member.id}</td>
                <td>${member.name}</td>
                <td>${member.email}</td>
                <td>${member.phone}</td>
            </tr>
        `;
    });
}

// ================= SEARCH MEMBER BY ID =================

async function searchMemberById() {

    const memberId = document.getElementById("search_member_id").value;

    const response = await fetch(
        `${BASE_URL}/members/search/id/${memberId}`
    );

    const member = await response.json();

    const tableBody = document.querySelector("#membersTable tbody");

    tableBody.innerHTML = `
        <tr>
            <td>${member.id}</td>
            <td>${member.name}</td>
            <td>${member.email}</td>
            <td>${member.phone}</td>
        </tr>
    `;
}

// ================= SEARCH MEMBER BY NAME =================

async function searchMemberByName() {

    const name = document.getElementById("search_member_name").value;

    const response = await fetch(
        `${BASE_URL}/members/search/name/${name}`
    );

    const members = await response.json();

    const tableBody = document.querySelector("#membersTable tbody");

    tableBody.innerHTML = "";

    members.forEach(member => {

        tableBody.innerHTML += `
            <tr>
                <td>${member.id}</td>
                <td>${member.name}</td>
                <td>${member.email}</td>
                <td>${member.phone}</td>
            </tr>
        `;
    });
}

// ================= SEARCH MEMBER BY PHONE =================

async function searchMemberByPhone() {

    const phone = document.getElementById("search_member_phone").value;

    const response = await fetch(
        `${BASE_URL}/members/search/phone/${phone}`
    );

    const members = await response.json();

    const tableBody = document.querySelector("#membersTable tbody");

    tableBody.innerHTML = "";

    members.forEach(member => {

        tableBody.innerHTML += `
            <tr>
                <td>${member.id}</td>
                <td>${member.name}</td>
                <td>${member.email}</td>
                <td>${member.phone}</td>
            </tr>
        `;
    });
}

// ================= UPDATE MEMBER =================

async function updateMember() {

    const memberId = document.getElementById("update_member_id").value;

    const updatedData = {};

    const name = document.getElementById("update_member_name").value;
    const email = document.getElementById("update_member_email").value;
    const phone = document.getElementById("update_member_phone").value;

    if (name) updatedData.name = name;
    if (email) updatedData.email = email;
    if (phone) updatedData.phone = phone;

    const response = await fetch(
        `${BASE_URL}/members/${memberId}`,
        {
            method: "PUT",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(updatedData)
        }
    );

    const data = await response.json();

    alert("Member updated successfully");

    console.log(data);
}

// ================= DELETE MEMBER BY ID =================

async function deleteMemberById() {

    const memberId = document.getElementById("delete_member_id").value;

    const response = await fetch(
        `${BASE_URL}/members/delete/id/${memberId}`,
        {
            method: "DELETE"
        }
    );

    const data = await response.json();

    alert(data.message);
}

// ================= DELETE MEMBER BY NAME =================

async function deleteMemberByName() {

    const name = document.getElementById("delete_member_name").value;

    const response = await fetch(
        `${BASE_URL}/members/delete/name/${name}`,
        {
            method: "DELETE"
        }
    );

    const data = await response.json();

    alert(data.message);
}

// ================= DELETE MEMBER BY PHONE =================

async function deleteMemberByPhone() {

    const phone = document.getElementById("delete_member_phone").value;

    const response = await fetch(
        `${BASE_URL}/members/delete/phone/${phone}`,
        {
            method: "DELETE"
        }
    );

    const data = await response.json();

    alert(data.message);
}