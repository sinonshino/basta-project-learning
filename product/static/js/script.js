
// Set the width of the side navigation to 250px and the left margin of the page content to 250px
document.getElementById("mySidenav").style.width = "250px";
document.getElementById("main").style.marginLeft = "250px";
document.getElementsByClassName("toggle-button")[0].style.left = "220px";

// A button which can open and close the sidenav
function toggleNav() {
    const sideNav = document.getElementById("mySidenav");
    const mainContent = document.getElementById("main");
    const toggleButton =  document.getElementsByClassName("toggle-button")[0];

    if (sideNav.style.width === "250px") {
        sideNav.style.width = "0";
        mainContent.style.marginLeft = "0";
        toggleButton.style.left = "-30px";
    } else {
        sideNav.style.width = "250px";
        mainContent.style.marginLeft = "250px";
        toggleButton.style.left = "220px";

    }
    toggleButton.classList.toggle('active');

}

// Add event listeners to the dropdown arrows with the class 'dropdown-arrow'
const dropdownArrows = document.querySelectorAll('.dropdown-arrow');

dropdownArrows.forEach(arrow => {
    arrow.addEventListener('click', toggleSubcategories);
});

// Function to toggle subcategories when a dropdown arrow is clicked
function toggleSubcategories(event) {
    event.preventDefault();
    const arrow = event.currentTarget;
    const parent = arrow.parentElement;
    const children = parent.nextElementSibling;

    if (children) {
        if (children.style.display === 'block') {
            children.style.display = 'none';
            parent.querySelector('.dropdown-arrow').style.transform = 'rotate(-90deg)';
        } else {
            children.style.display = 'block';
            parent.querySelector('.dropdown-arrow').style.transform = 'rotate(0deg)';
        }
    }
}

// Button to add product to cart
document.getElementById('add-to-cart').addEventListener('click', function() {
    // Retrieve the product's ID
    var productID = this.getAttribute('data-product-id')

    // Add the product to cart
    function addToCart(productID) {
        alert('Product added to cart! Product ID: ' + productId)
    }
})