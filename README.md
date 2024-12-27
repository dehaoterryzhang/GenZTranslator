# GenZ Translator

Welcome to the GenZ Translator! This app translates text between formal English and Gen Z language, making communication fun and accessible, especially between Gen Z and other generations.

## Table of Contents
- Features
- Installation
- Usage
- Libraries Used

## Features
- Translate formal English to Gen Z language.
- Translate Gen Z language to formal English.
- User-friendly interface built with Streamlit.
- Powered by OpenAI's GPT-4o for accurate and context-aware translations.
- Ability to adjust response creativity.

## Installation

### Prerequisites
- Python 3.8 or higher

### Steps
1. **Clone the repository:**

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up OpenAI API key:**
    - Obtain your OpenAI API key from OpenAI.
    - Create a `.env` file in the root directory of the project and add your API key:
      ```plaintext
      OPENAI_API_KEY=your_openai_api_key
      ```

5. **Run the app:**
    ```bash
    streamlit run app.py
    ```

## Usage
1. Open your web browser and go to `http://localhost:8501`.
2. Enter the text you want to translate in the input box.
3. Select the translation direction (Formal to Gen Z or Gen Z to Formal).
4. Click the "Translate" button to see the translated text.

## Libraries Used
- **OpenAI SDK:** For accessing OpenAI's GPT-4 model.
- **Streamlit:** For building the web interface.
- **dotenv:** For managing environment variables.
