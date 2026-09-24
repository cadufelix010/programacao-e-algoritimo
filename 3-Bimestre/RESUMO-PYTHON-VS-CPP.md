# Resumo de Estudos — Python x C++

## Por que estudar Python?

Python é uma linguagem de programação de sintaxe simples e fácil de ler. Ela permite focar mais na solução do problema e menos na quantidade de código necessária.

É utilizada em diversas áreas, como:

- Desenvolvimento de sistemas
- Automação
- Ciência de dados
- Inteligência artificial
- Aplicações web
- Scripts e ferramentas

## Principais diferenças

| Conceito | C++ | Python |
|---|---|---|
| Exibir texto | `cout` | `print()` |
| Ler dados | `cin` | `input()` |
| Blocos | Chaves `{}` | Indentação |
| Condição | `if (...) {}` | `if ...:` |
| Repetição | `while (...) {}` | `while ...:` |
| Variáveis | Tipo declarado | Tipo identificado automaticamente |
| Funções | Tipo + nome | `def nome():` |
| Lista | `vector` | `list` |

## Exemplo de condição

### C++

```cpp
if (idade >= 18) {
    cout << "Maior de idade";
} else {
    cout << "Menor de idade";
}
```

### Python

```python
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")
```

## Estruturas importantes em Python

### Lista

```python
nomes = ["Carlos", "Conrado"]
nomes.append("Aluno")
```

### Tupla

```python
coordenada = (10, 20)
```

### Dicionário

```python
produto = {
    "nome": "X-Burguer",
    "preco": 18.50
}
```

## Conclusão

A lógica de programação permanece a mesma entre C++ e Python. O que muda principalmente é a forma de escrever as instruções.
