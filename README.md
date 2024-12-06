# Streamlit OpenAI Model Interface

This repository demonstrates a simple Streamlit app for interacting with G4F that can provide us OpenAI APIs freely. The app allows users to select a model, input prompts, and view responses.

## Features

- **Model Selection**: Choose between `gpt-3.5-turbo`, `gpt-4`, and `gpt-4o` models. (You can add more)
- **Prompt Input**: Enter custom prompts to query the selected model.
- **AI Responses**: View model responses directly in the app.

## Prerequisites

- Python 3.8 or higher
- [G4F](https://pypi.org/project/g4f/)
- [OpenAI](https://pypi.org/project/openai/0.26.5/)
- [Streamlit](https://streamlit.io/)
- `pip` for installing dependencies

## Installation

1. Clone this repository:
   ```bash
   git clonehttps://github.com/Ryan-PG/yt-g4f-streamlit.git
   cd yt-g4f-streamlit
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure your OpenAI-compatible API is running at `http://localhost:1337/v1`.

## Usage

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Select a model from the dropdown, enter a prompt in the text input, and click **Send** to get a response.

## File Description

- `app.py`: The main Streamlit application for interacting with the OpenAI models.

## Requirements

Dependencies are listed in the `requirements.txt` file:
```txt
streamlit
openai
```

To install them, run:
```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! Fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
