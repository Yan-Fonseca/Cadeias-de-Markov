import random
import json
import ast

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

# Verificar se os estados iniciais existem nos JSONs
def check_initial_state(file_path, state):
    markov_chain = load_markov_chain(file_path)
    print(f"Estado '{state}' existe: {state in markov_chain}")

# Carregar uma cadeia de Markov de ordem n e gerar uma frase com explicação passo-a-passo
chain_order1 = load_markov_chain('markov_chain_order1.json')
sentence = generate_sentence(chain_order1, order=1)
print("\nFrase gerada:", sentence)

chain_order2 = load_markov_chain('markov_chain_order2.json')
sentence = generate_sentence(chain_order2, order=2)
print("\nFrase gerada:", sentence)

chain_order3 = load_markov_chain('markov_chain_order3.json')
sentence = generate_sentence(chain_order3, order=3)
print("\nFrase gerada:", sentence)