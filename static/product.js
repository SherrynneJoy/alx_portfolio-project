// Use template literals for concatenation
if (list === "<tr><th>Item</th><th>Value</th></tr>\n") {
    list += `<tr><td><i>empty</i></td>\n<td><i>empty</i></td></tr>\n`;
}

// Use let and const instead of var
let key = "";
const list = "<tr><th>Item</th><th>Value</th></tr>\n";

// Create separate functions for menu toggle and local storage handling
function toggleMenu() {
    menu.style.visibility = menu.style.visibility === "visible" ? "hidden" : "visible";
}

function handleLocalStorage() {
    // Functions for local storage handling
}

// Attach event listeners
close.addEventListener("click", toggleMenu);
open.addEventListener("click", toggleMenu);
window.addEventListener("load", handleLocalStorage);

function handleLocalStorage() {
    try {
        // Local storage operations
    } catch (error) {
        console.error("Error while accessing local storage:", error.message);
        alert("An error occurred while accessing local storage. Please try again later.");
    }
}
// Function to toggle the visibility of the menu
function toggleMenu() {
    // Toggle visibility logic
}

// Function to handle local storage operations
function handleLocalStorage() {
    // Local storage handling logic
}
