import random
import json
import ast

# Função para carregar a cadeia de Markov
def load_markov_chain(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        chain = json.load(file)
    return {ast.literal_eval(k): v for k, v in chain.items()}  # Desserialização segura


# Função para gerar texto
def generate_text(markov_chain_file, start_words, length=20):
    markov_chain = load_markov_chain(markov_chain_file)
    current_state = tuple(start_words)
    result = list(current_state)
    
    for _ in range(length):
        if current_state not in markov_chain:
            print(f"Estado não encontrado: {current_state}")  # Debug
            break
        next_word = random.choice(markov_chain[current_state])
        result.append(next_word)
        current_state = tuple(result[-len(current_state):])
    
    return ' '.join(result)

# Verificar se os estados iniciais existem nos JSONs
def check_initial_state(file_path, state):
    markov_chain = load_markov_chain(file_path)
    print(f"Estado '{state}' existe: {state in markov_chain}")

# Verificar estados iniciais
check_initial_state('/home/yan/ufjf/markov/Cadeias-de-Markov/src/markov_chain_order2.json', ('no', 'princípio'))
check_initial_state('/home/yan/ufjf/markov/Cadeias-de-Markov/src/markov_chain_order3.json', ('no', 'princípio', 'criou'))

# Gerar texto
markov_chain_order1 = '/home/yan/ufjf/markov/Cadeias-de-Markov/src/markov_chain_order1.json'
markov_chain_order2 = '/home/yan/ufjf/markov/Cadeias-de-Markov/src/markov_chain_order2.json'
markov_chain_order3 = '/home/yan/ufjf/markov/Cadeias-de-Markov/src/markov_chain_order3.json'

start_words_order1 = ["assim"]
start_words_order2 = ["assim", "diz"]
start_words_order3 = ["assim", "diz", "o"]

text_order1 = generate_text(markov_chain_order1, start_words_order1, 30)
print("Texto gerado (ordem 1):", text_order1)

text_order2 = generate_text(markov_chain_order2, start_words_order2, 30)
print("Texto gerado (ordem 2):", text_order2)

text_order3 = generate_text(markov_chain_order3, start_words_order3, 30)
print("Texto gerado (ordem 3):", text_order3)