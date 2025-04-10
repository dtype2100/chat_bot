import gradio as gr

def respond(message, history):
    return "응답: " + message

chatbot = gr.ChatInterface(fn=respond)
chatbot.launch()
