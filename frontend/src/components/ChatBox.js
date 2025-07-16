import React, { useState, useEffect } from "react";
import config from "../config";
import "./ChatBox.css";

function ChatBox() {
  const [messages, setMessages] = useState([]);
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);

  // Add first welcome message
  useEffect(() => {
    setMessages([{ text: "🤖 Hello! I'm SMG-EV Assistant. How can I help you today?", sender: "bot" }]);
  }, []);

  const askBot = async () => {
    setLoading(true);
    if (!query.trim()) return;

    const userMessage = { text: query, sender: "user" };
    setMessages((prev) => [...prev, userMessage]);

    try {
      setQuery("");
      const res = await fetch(`${config.API_URL}/ask`, {
        method: "POST",
        headers: {
           "Content-Type": "application/json",   
          },
        body: JSON.stringify({ query }),
      });
      const data = await res.json();
      console.log("data" ,data);
      const botMessage = { text: data.response, sender: "bot" };
      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        { text: "Sorry, something went wrong.", sender: "bot" },
      ]);
    }finally{
      setLoading(false);
    }
  };

  const handleKeyPress = (event) => {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      askBot();
    } else if (event.key === "Enter" && event.shiftKey) {
      setQuery((prev) => prev + "\n");
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-header">🤖 SMG-EV Assistant</div>

      <div className="chat-box">
  {messages.map((msg, index) => (
    <div key={index} className={`message ${msg.sender}`}>
      {msg.text}
    </div>
  ))}
  {loading && (
    <div className="message bot">
      Typing...
    </div>
  )}
</div>


      <div className="chat-input">
        <textarea
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={handleKeyPress}
          placeholder="Type your message..."
          rows="2"
        />
        <button onClick={askBot}>Send</button>
      </div>
    </div>
  );
}

export default ChatBox;
