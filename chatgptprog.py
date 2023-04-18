import openai
import os
import requests
import json
from PIL import Image, ImageTk
from io import BytesIO
import tkinter as tk

# Set the OpenAI API key
openai.api_key = "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"

def generate_image():
    # Get the user input from the textbox
    prompt = prompt_textbox.get("1.0", tk.END).strip()

    # Generate text using GPT-3
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      max_tokens=50
    )
    output_text = response.choices[0].text.strip()

    # Set the DALL-E API parameters
    url = "https://api.openai.com/v1/images/generations"
    api_key = "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"
    model = "image-alpha-001"
    prompt1 = prompt

    # Set the request headers and body
    headers = {"Content-Type": "application/json",
               "Authorization": f"Bearer {api_key}"}
    data = {"model": model,
            "prompt": prompt1,
            "num_images": 1,
            "size": "512x512"}

    # Send the HTTP POST request to the API endpoint
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Extract the image URL from the API response
    image_url = response.json()['data'][0]['url']

    # Display the generated image
    image_data = requests.get(image_url).content
    image = Image.open(BytesIO(image_data))
    photo = ImageTk.PhotoImage(image)
    image_label.configure(image=photo)
    image_label.image = photo


# Create a GUI window
window = tk.Tk()
window.title("DALL-E Image Generator")

# Add a textbox for user input
prompt_label = tk.Label(window, text="Describe the picture you want to generate:")
prompt_label.pack()
prompt_textbox = tk.Text(window, height=3, width=50)
prompt_textbox.pack()

# Add a button to generate the image
generate_button = tk.Button(window, text="Generate Image", command=generate_image)
generate_button.pack()

# Add an image element to display the generated image
image_label = tk.Label(window)
image_label.pack()

# Start the GUI event loop
window.mainloop()


