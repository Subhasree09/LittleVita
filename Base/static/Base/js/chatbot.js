document.addEventListener('DOMContentLoaded', function() {
    const chatIcon = document.getElementById('chatIcon');
    const chatContainer = document.getElementById('chatContainer');
    const userInput = document.getElementById('userInput');
    const sendButton = document.getElementById('sendButton');
    const chatWindow = document.getElementById('chatWindow');
    console.log('hello');
    
    chatIcon.addEventListener('click', function() {
        if (chatContainer.style.display === 'none') {
            chatContainer.style.display = 'block';
        } else {
            chatContainer.style.display = 'none';
        }
    });

    // sendButton.addEventListener('click', function() {
    //     const userMessage = userInput.value;
    //     if (userMessage) {
    //         // Append user message to chat window
    //         const userMessageElement = document.createElement('p');
    //         userMessageElement.textContent = userMessage;
    //         chatWindow.appendChild(userMessageElement);

    //         // Clear input field
    //         userInput.value = '';

    //         // Simulate chatbot response
    //         setTimeout(function() {
    //             const botMessageElement = document.createElement('p');
    //             botMessageElement.textContent = 'This is a bot response to your message: ' + userMessage;
    //             chatWindow.appendChild(botMessageElement);
    //         }, 1000); // Simulate a delay
    //     }
    // });
});
