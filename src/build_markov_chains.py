import re
import json
import ast
import random
from collections import defaultdict, Counter

# Função para carregar o texto da Bíblia
def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# Pré-processamento: remove pontuação, números e converte para minúsculas
def preprocess_text(text):
    text = re.sub(r'[^\w\sáàâãäéèêëíìîïóòôõöúùûüç]', '', text)  # Remove pontuação
    text = re.sub(r'\d+', '', text)  # Remove números
    text = text.lower()
    return text

# Função para construir a cadeia de Markov com probabilidades
def build_markov_chain(text, file_path, order):
    words = text.split()
    chain = defaultdict(list)
    
    # Construir a cadeia
    for i in range(len(words) - order):
        current_state = tuple(words[i:i + order])
        next_word = words[i + order]
        chain[current_state].append(next_word)
    
    # Converter para probabilidades
    markov_prob = {}
    for state, next_words in chain.items():
        total = len(next_words)
        word_counts = Counter(next_words)
        markov_prob[state] = {word: count / total for word, count in word_counts.items()}
    
    # Salvar como JSON com chaves serializadas
    with open(file_path, 'w', encoding='utf-8') as file:
        serialized_chain = {str(k): v for k, v in markov_prob.items()}
        json.dump(serialized_chain, file, indent=4)

# Função para carregar a cadeia de Markov
def load_markov_chain(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        chain = json.load(file)
    return {ast.literal_eval(k): v for k, v in chain.items()}  # Desserialização segura

# Função para gerar frases destacando os estados e suas 5 transições mais prováveis
def generate_sentence(chain, order, max_length=20):
    state = random.choice(list(chain.keys()))  # Escolher um estado inicial aleatório
    sentence = list(state)

    print("\nGerando frase passo a passo...\n")

    for _ in range(max_length - order):
        if state not in chain:
            break
        
        next_words = chain[state]
        
        # Ordenar as transições por probabilidade
        sorted_transitions = sorted(next_words.items(), key=lambda x: x[1], reverse=True)
        
        # Exibir o estado atual e as 5 transições mais prováveis
        print(f"Estado atual: {state}")
        print("Transições mais prováveis:")
        for word, prob in sorted_transitions[:5]:
            print(f"  {word}: {prob:.2%}")
        
        # Escolher a próxima palavra com base nas probabilidades
        next_word = random.choices(list(next_words.keys()), weights=next_words.values())[0]
        
        print(f"Palavra escolhida: {next_word}\n")
        
        sentence.append(next_word)
        state = tuple(sentence[-order:])  # Atualizar estado para os últimos "order" palavras

    return ' '.join(sentence)

# Construção das cadeias de Markov
file_path = 'biblia_completa.txt'
bible_text = load_text(file_path)
bible_text = preprocess_text(bible_text)  # Agora remove números também

# Criar cadeias de ordem 1, 2 e 3
build_markov_chain(bible_text, 'src/markov_chain_order1.json', order=1)
build_markov_chain(bible_text, 'src/markov_chain_order2.json', order=2)
build_markov_chain(bible_text, 'src/markov_chain_order3.json', order=3)

# Carregar uma cadeia de Markov de ordem n e gerar uma frase com explicação passo-a-passo
chain_order1 = load_markov_chain('src/markov_chain_order1.json')
sentence = generate_sentence(chain_order1, order=1)
print("\nFrase gerada:", sentence)

chain_order2 = load_markov_chain('src/markov_chain_order2.json')
sentence = generate_sentence(chain_order2, order=2)
print("\nFrase gerada:", sentence)

chain_order3 = load_markov_chain('src/markov_chain_order3.json')
sentence = generate_sentence(chain_order3, order=3)
print("\nFrase gerada:", sentence)