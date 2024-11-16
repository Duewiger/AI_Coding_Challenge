interface ChatResponse {
    reply: string;
    error?: string;
}

const form = document.querySelector("form") as HTMLFormElement;
const questionInput = document.querySelector(".question-input") as HTMLInputElement;
const previousChat = document.querySelector(".previous-chat textarea") as HTMLTextAreaElement;

form.addEventListener("submit", async (e: Event) => {
    e.preventDefault();

    const userQuestion = questionInput.value;
    questionInput.value = "";

    previousChat.value += `Du: ${userQuestion}\n`;

    previousChat.value += "Assistent: Der Assistent schreibt ...\n";

    try {
        const response = await fetch("http://127.0.0.1:8000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ question: userQuestion }),
        });

        if (!response.ok) {
            throw new Error("API request failed.");
        }

        const data: ChatResponse = await response.json();
        const reply = data.reply || "Keine Antwort erhalten.";

        previousChat.value = previousChat.value.replace(
            "Assistent: Der Assistent schreibt ...\n",
            `Assistent: ${reply}\n\n`
        );
    } catch (error) {
        console.error("Error:", error);

        previousChat.value = previousChat.value.replace(
            "Assistent: Der Assistent schreibt ...\n",
            "Assistent: Fehler beim Abrufen der Antwort.\n\n"
        );
    }
});