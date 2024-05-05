import gradio as gr
from openai import OpenAI

def generate_story(mc_description, style, genre, components, environment, story_type, base_url, api_key):
    # Set up OpenAI client
    client = OpenAI(base_url=base_url, api_key=api_key)
    
    # Create a prompt for the OpenAI model
    prompt = f"Generate a {story_type} story about a character named {mc_description} in a {style} world with a {genre} theme. Include {components} in the story."
    if environment:
        prompt += f" The story takes place in a {environment}."
    
    # Call the OpenAI API to generate a story
    completion = client.chat.completions.create(
        model="model-identifier",  # Replace with your model identifier
        messages=[
            {"role": "system", "content": "Always answer in a coherent and engaging story."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    
    # Return the generated story
    return completion.choices[0].message.content

def reset_inputs():
    # Reset all input fields
    return "", "", "", "", "", "", "", ""

with gr.Blocks() as demo:
    with gr.Row():
        mc_description = gr.Textbox(label="Describe your main character (MC)", placeholder="Enter a brief description of your MC, including traits, personality, and background")
        style = gr.Textbox(label="Enter a writing style", placeholder="e.g. Fantasy, Sci-Fi, Romance, Horror")
        genre = gr.Textbox(label="Enter a genre", placeholder="e.g. Adventure, Mystery, Thriller, Comedy")
        components = gr.Textbox(label="Enter additional story components (optional)", placeholder="e.g. Magic system, Alternate universe, Time travel, Space exploration")
        environment = gr.Textbox(label="Describe the environment (optional)", placeholder="e.g. Medieval castle, Futuristic city, Mysterious forest")
        story_type = gr.Radio(label="Story type", choices=["Full story", "Part by part"])
        base_url = gr.Textbox(label="Enter API base URL", placeholder="e.g. http://localhost:5001/v1")
        api_key = gr.Textbox(label="Enter OpenAI API key", placeholder="e.g. lm-studio")
    
    with gr.Row():
        generate_button = gr.Button("Generate Story")
        reset_button = gr.Button("Reset")
    
    output_story = gr.Textbox(label="Generated Story")
    
    generate_button.click(fn=generate_story, inputs=[mc_description, style, genre, components, environment, story_type, base_url, api_key], outputs=output_story)
    reset_button.click(fn=reset_inputs, inputs=None, outputs=[mc_description, style, genre, components, environment, story_type, base_url, api_key])

demo.launch()
