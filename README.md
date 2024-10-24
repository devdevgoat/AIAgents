```markdown
# Agent Persona Management with OpenAI

This project provides a Python class `Agent` that utilizes the OpenAI API to manage and interact with different "personas". These personas are predefined or dynamically created configurations that guide the behavior and responses of an AI model. The primary purpose is to manage text and image processing instructions to the AI model in a personalized way depending on the specified persona.

## Features

- **Dynamic Persona Management**: Create and configure different personas using text-based prompts.
- **Text and Image Processing**: Send instructions as text or combined text and image prompts to an AI model.
- **OpenAI Integration**: Leverages the OpenAI GPT models via the OpenAI API.

## File Structure

- `Agent`: A Python class managing persona creation, setting, and instruction processing.
- `main.py`: Example usages of the `Agent` class demonstrating both existing and new persona creation and instruction handling.

## Agent Class

### Initialization

```python
Agent(personaName:str="default", newPersonaPrompt:str=None)
```

- **personaName**: Name of the persona to use. If it does not exist, it will be created using `newPersonaPrompt`.
- **newPersonaPrompt**: Custom prompt to associate with a new persona if the `personaName` does not exist.

### Methods

- `setPersona(personaName)`: Sets the active persona with system prompts loaded from files.
- `loadPersonas(folder_path)`: Loads all persona prompts from a specified directory of persona files.
- `CreatePersona(personaName, personaPrompt)`: Creates a new persona file with the given prompt.
- `CreateTextPrompt(prompt, role)`: Constructs a text prompt object for sending to the API.
- `CreateImagePrompt(imgPath, prompt)`: Constructs an image-based prompt for using within the API by encoding the image into Base64 format.
- `encodeImgFromPath(image_path)`: Encodes an image from the specified path into a Base64 string.
- `instruct(prompt)`: Sends a text instruction to the AI model and returns the model's text response.
- `parseImage(imgPath, prompt)`: Sends an image instruction to the AI model to process and returns the response text.
- `instructMultiText(prompts)`: Sends multiple text instructions to the AI model and returns all completion results.

## Example Usage

Below is an example demonstrating how to use the `Agent` class:

```python
from agent import Agent

# Create a worker persona and use it
worker = Agent("worker")
worker_response = worker.instruct("Say hello")
print(worker_response)

# Create a reviewer persona and use it
reviewer = Agent("reviewer")
reviewer_response = reviewer.instruct("Say hello")
print(reviewer_response)
```

## Setup Instructions

1. **Environment Setup**: Ensure the `.env` file contains `APIKEY` for OpenAI access.
2. **Persona Files Directory**: Place your persona files in a folder named `personas` in the project root.

## Dependencies

- `openai`: This is required for API calls.
- `python-dotenv`: Used for loading environment variables from a .env file.
- `os` and `base64`: Standard libraries used for file and string operations.

Ensure all dependencies are installed using pip:

```sh
pip install openai python-dotenv
```

## Notes

- If a persona does not exist, it automatically creates one using a default prompt if `newPersonaPrompt` is not specified.
- The system prompt must be a valid string and stored in the `personas` directory to modify existing personas.
- This implementation assumes the use of OpenAI GPT models such as "gpt-4o" for processing tasks.
```
