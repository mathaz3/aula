# Jogo Armague 🃏⚔️

Este repositório contém a lógica do jogo **Armague**, uma competição entre dois jogadores, Túlio e Pedro, que disputam entre si utilizando cartas com atributos de combate. O jogo foi criado como uma forma divertida de decidir quem levaria as bandejas após o almoço no RU.

## 🕹️ Regras do Jogo

O jogo é composto por **três duelos** entre as cartas dos jogadores. Cada carta possui os seguintes atributos:

- **Classe:** Guerreiro (1), Mago (2) ou Arqueiro (3)
- **Ataque:** Valor numérico
- **Vida:** Valor numérico

### ⚔️ Dinâmica dos Duelos

1. Antes do duelo, os atributos das cartas podem ser modificados com base nas classes, conforme a tabela de bônus abaixo.
2. Em cada duelo, **a carta com menos pontos de vida ataca primeiro**.
   - Se as cartas tiverem a mesma vida, **Pedro ataca primeiro**.
3. Após o primeiro ataque, se a carta oponente não morrer (vida > 0), ela contra-ataca.
4. O duelo termina após esse segundo ataque.

### 🧮 Bônus de Classe

- **Guerreiro vs Arqueiro:** Guerreiro ganha +30% de vida.
- **Arqueiro vs Mago:** Arqueiro ganha +25% de ataque.
- **Mago vs Guerreiro:** Mago ganha +15% de vida e +15% de ataque.

### 💀 Condições de Derrota

Uma carta morre se seus pontos de vida forem **menores ou iguais a 0** após um ataque.

### 🏆 Critérios de Vitória de um Duelo

- Vence quem **eliminar a carta adversária**.
- Se nenhuma carta for eliminada:
  - Vence quem tiver **mais vida restante**.
  - Se empatar, vence quem tiver **mais ataque restante**.

### 🧠 Observações

- O ataque consiste em subtrair os pontos de vida do inimigo com base no valor de ataque do agressor.
- Os ataques entre cartas nunca são iguais (é garantido que sempre há um desempate).

## 👨‍💻 Entrada do Programa

O programa espera como entrada os dados das cartas dos jogadores, nesta ordem:

```text
ClassePedro1 AtaquePedro1 VidaPedro1
ClassePedro2 AtaquePedro2 VidaPedro2
ClassePedro3 AtaquePedro3 VidaPedro3
ClasseTulio1 AtaqueTulio1 VidaTulio1
ClasseTulio2 AtaqueTulio2 VidaTulio2
ClasseTulio3 AtaqueTulio3 VidaTulio3

como por exemplo:
1 10 50
2 12 40
3 15 35
3 10 45
1 11 42
2 14 38


📋 Saída Esperada
Para cada rodada, o programa imprime o vencedor:
Rodada1: Pedro
Rodada2: Tulio
Rodada3: Pedro

Ao final, imprime o vencedor geral:
Pedro vitorioso
