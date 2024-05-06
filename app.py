import gradio as gr
from openai import OpenAI

def generate_story(mc_description, tone, genre, components, environment, story_type, pace, ending, base_url, api_key):
    # Set up OpenAI client
    client = OpenAI(base_url=base_url, api_key=api_key)
    
    # Create a prompt for the OpenAI model
    prompt = f"Generate a {story_type} story about a character named {mc_description} in a {tone} world with a {genre} theme. Include {components} in the story."
    if environment:
        prompt += f" The story takes place in a {environment}."
    prompt += f" The story should be told at a {pace} pace."
    if ending == "Endless":
        prompt += " The story should not have a definitive ending, leaving room for continuation."
    else:
        prompt += " The story should have a clear beginning, middle, and end."
    
    # Call the OpenAI API to generate a story
    completion = client.chat.completions.create(
        model="model-identifier",  # Replace with your model identifier
        messages=[
            {"role": "system", "content": "write a coherent, engaging and creative story."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    
    # Return the generated story
    return completion.choices[0].message.content

def continue_story(story, mc_description, tone, genre, components, environment, pace, base_url, api_key):
    # Set up OpenAI client
    client = OpenAI(base_url=base_url, api_key=api_key)
    
    # Create a prompt for the OpenAI model
    prompt = f"Continue the story from where it left off. The story is about a character named {mc_description} in a {tone} world with a {genre} theme. Include {components} in the story."
    if environment:
        prompt += f" The story takes place in a {environment}."
    prompt += f" The story should be told at a {pace} pace."
    
    # Call the OpenAI API to generate a continuation of the story
    completion = client.chat.completions.create(
        model="model-identifier",  # Replace with your model identifier
        messages=[
            {"role": "system", "content": "write a coherent, engaging and creative story."},
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": story}
        ],
        temperature=0.7,
    )
    
    # Return the generated continuation of the story
    return completion.choices[0].message.content

def reset_inputs():
    # Reset all input fields
    return "", "", "", "", "", "", "", "", ""

with gr.Blocks(theme="soft", title="AI Story Writer") as demo:
    with gr.Row():
        mc_description = gr.Textbox(label="Describe your main character (MC)", placeholder="Enter a brief description of your MC, including traits, personality, and background")
        tone = gr.Textbox(label="Enter a writing tone", placeholder="e.g. Dark, Fun, Nihilistic, Melancholy")
        genre = gr.Textbox(label="Enter a genre", placeholder="e.g. Adventure, Mystery, Thriller, Comedy")
        components = gr.Textbox(label="Enter additional story components (optional)", placeholder="e.g. Magic system, Alternate universe, Time travel, Space exploration")
        environment = gr.Textbox(label="Describe the environment (optional)", placeholder="e.g. Medieval castle, Futuristic city, Mysterious forest")
        story_type = gr.Radio(label="Story type", choices=["Full story", "Part"])
        pace = gr.Radio(label="Story pace", choices=["Fast", "Medium", "Slow"])
        ending = gr.Radio(label="Story ending", choices=["Endless", "Ending"])

    
    with gr.Row():
        generate_button = gr.Button("Generate Story")
        continue_button = gr.Button("Continue Story")
        reset_button = gr.Button("Reset")


    with gr.Row():
        base_url = gr.Textbox(label="Enter OpenAI API base URL", placeholder="Use Open AI or Local", value="http://localhost:5001/v1")
        api_key = gr.Textbox(label="Enter OpenAI API key", placeholder="e.g. lm-studio", value="none")
    
    output_story = gr.Textbox(label="Generated Story", show_copy_button=("True"))
    
    generate_button.click(fn=generate_story, inputs=[mc_description, tone, genre, components, environment, story_type, pace, ending, base_url, api_key], outputs=output_story)
    continue_button.click(fn=continue_story, inputs=[output_story, mc_description, tone, genre, components, environment, pace, base_url, api_key], outputs=output_story)
    reset_button.click(fn=reset_inputs, inputs=None, outputs=[mc_description, tone, genre, components, environment, story_type, pace, ending])
demo.launch()
