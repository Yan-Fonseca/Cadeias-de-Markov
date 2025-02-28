# Geração de Texto com Cadeias de Markov

Este projeto utiliza Cadeias de Markov de ordens 1, 2 e 3 para gerar texto com noção de contexto, analisando a probabilidade de uma palavra vir em seguida. O corpus utilizado é o texto da Bíblia, e o projeto inclui uma interface gráfica para facilitar a construção de frases.

## Funcionalidades

1. **Geração de Texto**:
   - Utiliza Cadeias de Markov de ordens 1, 2 e 3 para gerar texto com base no contexto das palavras anteriores.
   - Seleciona as 5 palavras mais prováveis para seguir uma dada sequência de palavras.

2. **Análise de Probabilidades**:
   - Calcula as probabilidades de transição entre palavras.
   - Exibe as 5 palavras mais prováveis para seguir uma sequência de palavras.

3. **Interface Gráfica**:
   - Interface amigável para inserir palavras iniciais e visualizar as sugestões de palavras seguintes.
   - Permite gerar frases completas com base no modelo treinado.

4. **Corpus da Bíblia**:
   - O texto da Bíblia é utilizado como corpus para treinar o modelo.
   - O texto é pré-processado para remover pontuações, números e converter para minúsculas.
