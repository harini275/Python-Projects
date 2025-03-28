const chatInput = document.querySelector('.chat-input textarea');
const sendChatBtn = document.querySelector('#sendBTN');
const chatbox = document.querySelector(".chatbox");

const createChatLi = (message, className) => {
    const chatLi = document.createElement("li");
    chatLi.classList.add("chat", className);
    let chatContent = className === "chat-outgoing" ? `<p>${message} 😊</p>` : `<p>${message} 🤖</p>`;
    chatLi.innerHTML = chatContent;
    return chatLi;
};

const handleChat = async () => {
    const userMessage = chatInput.value.trim();
    if (!userMessage) {
        return;
    }
    
    // Display user's message
    chatbox.appendChild(createChatLi(userMessage, "chat-outgoing"));
    chatInput.value = ''; // Clear input after sending
    chatbox.scrollTo(0, chatbox.scrollHeight);

    // Send message to the Flask backend
    const response = await fetch('/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userMessage })
    });

    const data = await response.json();
    // Display chatbot's response
    chatbox.appendChild(createChatLi(data.response, "chat-incoming"));
    chatbox.scrollTo(0, chatbox.scrollHeight);
};

// Add event listener to the send button
sendChatBtn.addEventListener('click', handleChat);

// Allow pressing Enter to send the message
chatInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        handleChat();
        e.preventDefault(); // Prevents new line in textarea
    }
});