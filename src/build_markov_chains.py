import re
from collections import defaultdict
import json
import ast

# Função para carregar o texto da Bíblia
def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# Pré-processamento simplificado
def preprocess_text(text):
    text = re.sub(r'[^\w\sáàâãäéèêëíìîïóòôõöúùûüç]', '', text)  
    text = text.lower()
    return text

# Função para construir a cadeia de Markov
def build_markov_chain(text, file_path, order):
    words = text.split()
    chain = defaultdict(list)
    for i in range(len(words) - order):
        current_state = tuple(words[i:i + order])
        next_word = words[i + order]
        chain[current_state].append(next_word)
    
    # Salvar como JSON com chaves serializadas
    with open(file_path, 'w', encoding='utf-8') as file:
        serialized_chain = {str(k): v for k, v in chain.items()}
        json.dump(serialized_chain, file)

# Função para carregar a cadeia de Markov
def load_markov_chain(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        chain = json.load(file)
    return {ast.literal_eval(k): v for k, v in chain.items()}  # Desserialização segura

# Construir as cadeias de Markov
file_path = '../biblia_completa.txt'
bible_text = load_text(file_path)
bible_text = preprocess_text(bible_text)

build_markov_chain(bible_text, 'markov_chain_order1.json', order=1)
build_markov_chain(bible_text, 'markov_chain_order2.json', order=2)
build_markov_chain(bible_text, 'markov_chain_order3.json', order=3)