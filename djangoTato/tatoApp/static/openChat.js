const messageBubble = document.getElementById('message-bubble');
const chatbotContainer = document.getElementById('chatbotContainer');
let isOpen = false;

messageBubble.addEventListener('click', function(event) {
  if (isOpen) {
    chatbotContainer.style.display = 'none';
    isOpen = false;
  } else {
    chatbotContainer.style.display = 'block';
    isOpen = true;
  }
});
