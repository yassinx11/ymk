# Chatbot Knowledge Base

This project is a simple chatbot that uses a JSON-based knowledge base to provide answers to user questions. The chatbot can also learn new questions and answers from user input.

## Features

- Loads a knowledge base from a JSON file
- Finds the best match for a user's question based on string similarity
- Provides an answer from the knowledge base if a match is found
- Allows users to teach the chatbot new questions and answers
- Saves the updated knowledge base to the JSON file

## Usage

1. Run the `main.py` script to start the chatbot.
2. Type your questions, and the chatbot will respond with the best matching answer from the knowledge base.
3. If the chatbot doesn't know the answer, it will prompt you to provide the answer. The new question-answer pair will be saved to the knowledge base.
4. Type `bye` to exit the chatbot.

## Knowledge Base Format

The knowledge base is stored in a JSON file named `knowledgebase.json`. The file contains a list of questions and their corresponding answers:

```json
{
  "questions": [
    {
      "question": "hi",
      "answer": "Hi, how can I help you today?"
    },
    {
      "question": "hello",
      "answer": "Hello! What can I do for you?"
    },
    {
      "question": "what is python",
      "answer": "Python is a high-level programming language known for its simplicity and readability."
    },
    ...
  ]
}
```

You can add, modify, or remove questions and answers in this file to customize the chatbot's knowledge base.

## Code Structure

The main functionality of the chatbot is implemented in the `main.py` file, which includes the following functions:

- `load_knowledge_base(file_path: str) -> dict`: Loads the knowledge base from a JSON file.
- `save_knowledge_base(file_path: str, data: dict)`: Saves the updated knowledge base to a JSON file.
- `find_best_match(user_question: str, questions: list[str]) -> str | None`: Finds the best matching question from the knowledge base based on string similarity.
- `get_answer_for_question(question: str, knowledge_base: dict) -> str | None`: Retrieves the answer for a given question from the knowledge base.
- `chatbot()`: Runs the chatbot loop, handling user input and updating the knowledge base.

## Dependencies

This project requires the following Python packages:

- `json`
- `os`
- `difflib`

These dependencies are included in the standard Python library and do not require any additional installation.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on the project's GitHub repository.
