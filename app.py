import gradio as gr
from model import generate_response

# Launch the chat interface with generate_response as callback function
app = gr.ChatInterface(
    generate_response,
    type='messages',
    flagging_mode='never',
    save_history=True,
)

if __name__ == "__main__":
    app.launch(share=True)