import json, os
from difflib import get_close_matches

def load_knowledge_base(file_path: str) -> dict:
    if not os.path.exists(file_path):
        return {"questions": []}
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        if 'data' in data:  # SQuAD format
            questions = []
            for article in data['data']:
                for paragraph in article['paragraphs']:
                    for qa in paragraph['qas']:
                        if qa['answers']:
                            questions.append({
                                'question': qa['question'],
                                'answer': qa['answers'][0]['text']
                            })
            return {'questions': questions}
        return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches = get_close_matches(user_question.lower(), [q.lower() for q in questions], n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base.get('questions', []):
        if q['question'].lower() == question.lower():
            return q['answer']
    return None

def chatbot():
    knowledge_base = load_knowledge_base('knowledgebase.json')
    print("Bot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input('You: ').strip()
        if user_input.lower() == 'bye':
            print("Bot says: bye")
            break
        best_match = find_best_match(user_input, [q['question'] for q in knowledge_base.get('questions', [])])
        if best_match:
            answer = get_answer_for_question(best_match, knowledge_base)
            print(f'Bot says: {answer}')
        else:
            print("Bot says: I don't know the answer, can you teach me?")
            new_answer = input('Type the answer or skip: ').strip()
            if new_answer.lower() != 'skip':
                if 'questions' not in knowledge_base:
                    knowledge_base['questions'] = []
                knowledge_base['questions'].append({'question': user_input, 'answer': new_answer})
                save_knowledge_base('knowledgebase.json', knowledge_base)
                print('Bot says: Thank you, I learned a new response!')

if __name__ == '__main__':
    chatbot()
