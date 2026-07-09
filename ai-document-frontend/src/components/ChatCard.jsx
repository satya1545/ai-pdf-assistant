import { useState } from "react";
import { askQuestion } from "../services/chatService";

function ChatCard() {

    const [question, setQuestion] = useState("");
    const [messages, setMessages] = useState([]);
    const [loading, setLoading] = useState(false);

    const sendQuestion = async () => {

        if (!question.trim()) return;

        const userQuestion = question;

        setMessages(prev => [
            ...prev,
            {
                sender: "user",
                text: userQuestion
            }
        ]);

        setQuestion("");

        setLoading(true);

        try {

            const response = await askQuestion(userQuestion);

            setMessages(prev => [
                ...prev,
                {
                    sender: "ai",
                    text: response.answer
                }
            ]);

        } catch {

            setMessages(prev => [
                ...prev,
                {
                    sender: "ai",
                    text: "Something went wrong."
                }
            ]);

        }

        setLoading(false);

    };

    return (

        <div className="bg-white rounded-xl shadow p-6">

            <h2 className="text-xl font-bold mb-4">
                🤖 AI Assistant
            </h2>

            <div className="h-80 overflow-y-auto border rounded-lg p-4 mb-4 space-y-4">

                {
                    messages.map((msg, index) => (

                        <div
                            key={index}
                            className={
                                msg.sender === "user"
                                    ? "text-right"
                                    : "text-left"
                            }
                        >

                            <span
                                className={
                                    msg.sender === "user"

                                        ? "bg-blue-600 text-white inline-block px-4 py-2 rounded-xl"

                                        : "bg-gray-200 inline-block px-4 py-2 rounded-xl"
                                }
                            >

                                {msg.text}

                            </span>

                        </div>

                    ))
                }

                {
                    loading &&
                    <div className="text-gray-500 italic">
                        🤖 Gemini is thinking...
                    </div>
                }

            </div>

            <div className="flex gap-2">

                <input
                    className="flex-1 border rounded-lg px-4 py-2"
                    placeholder="Ask anything about your document..."
                    value={question}
                    onChange={(e) => setQuestion(e.target.value)}
                    onKeyDown={(e) => {

                        if (e.key === "Enter")
                            sendQuestion();

                    }}
                />

                <button
                    onClick={sendQuestion}
                    className="bg-blue-600 text-white px-6 rounded-lg"
                >
                    Send
                </button>

            </div>

        </div>

    );

}

export default ChatCard;