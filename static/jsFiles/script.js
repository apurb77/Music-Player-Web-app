// Get the input element and card container
const searchInput = document.getElementById('searchInput');
const cards = document.querySelectorAll('.card');

// Function to filter cards based on input
const filterCards = () => {
  const filterValue = searchInput.value.toLowerCase();
  
  cards.forEach(card => {
    const title = card.querySelector('.card-title').textContent.toLowerCase();
    const text = card.querySelector('.card-text').textContent.toLowerCase();
    
    if (title.includes(filterValue) || text.includes(filterValue)) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
};

// Listen for input event on search input
searchInput.addEventListener('input', filterCards);
