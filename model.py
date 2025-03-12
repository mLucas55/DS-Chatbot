import ollama
from history import add_to_history, supply_history

# Prompts DeepSeek through the Ollama library to generate a response based on user input
# The response is streamed back to the user in real-time
def generate_response(user_input, extra):
    history = supply_history()
    payload = history + user_input

    response = ollama.chat(
        model="deepseek-r1:7b",
        messages=[{"role": "user", 
                   "content": payload}],
        stream=True
    )

    generated_text = ""

    # Generator function that yields chunks of text to enable real-time streaming
    for chunk in response:
        text_chunk = chunk.message.content

        if "<think>" in text_chunk.lower():
            # Stream a placeholder to prevent Gradio from timing out
            yield "..."

        else:
            # Stream actual content
            print(text_chunk, end="", flush=True)
            yield generated_text + text_chunk
            generated_text += text_chunk
    
    add_to_history(generated_text)
