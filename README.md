# Presentation algorithme génétique

## Contenu

- [Présentation](#présentation)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Hands-On](#Hands-On)

## Présentation

Ce projet est une présentation de l'algorithme génétique. Il a été réalisé dans le cadre des journées de partage d'[Ekinox](www.ekinox.io).

## Installation

### [Colab](https://colab.research.google.com/)

On peut suivre [ce lien](https://colab.research.google.com/github/tomtaranto/GeneticAlgoPrez/blob/main/GeneticAlgoHandsOn.ipynb) pour y acceder directement

OU

On peut recuperer le notebook stocké sur github directement depuis Colab:

```
Fichier > Importer un notebook > Github > L'url de ce repo (https://github.com/tomtaranto/GeneticAlgoPrez) > selectionner le notebook
```

On peut ensuiter executer les cellules unes à unes.


### Local
 
Pour installer le projet en local. Il faut installer les dependances python

```bash
poetry install
```

On peut ensuite lancer l'algo avec la commande

```bash
poetry run python main.py
```


## Utilisation

Un premier algorithme est déjà implémenté.

On peut essayer de modifier les constantes définies en début du fichier pour voir leur impact sur les résultats obtenus.

A la fin de chaque execution, on obtient un GIF qui montre le meilleur individu de chaque génération.


## Hands-On

### 1. Modifier la variable `POPULATION_SIZE`

<details>
<summary>Résultats attendus</summary>
La convergence vers une solution est plus rapide lorsque la population est grande
</details>

### 2. Modifier la variable `MUTATION_RATE`

<details>
<summary>Résultats attendus</summary>
La convergence vers une solution est plus rapide lorsque la mutation est dans l'intervalle [0.1, 0.9]
</details>


### 3. Modifier la variable `NEW_ELEMENTS_EACH_GENERATION`

Utiliser le dataset `"paris_metro"` pour tester l'impact de cette variable. Partir de 0 et augmenter petit à petit le nombre.

<details>
<summary>Résultats attendus</summary>
L'apparition de nouveaux éléments permet de ne pas rester coincé sur les minimas locaux. Attention, un trop grand nombre de nouveaux éléments peut ralentir fortement la convergence.
</details>

### 4. Implementer La fonction de selection `roulette`

Ici, chaque individu a une probabilité d'être séléctionné proportionnelle à son score

<details>
<summary>Implémentation</summary>
TODO
</details>

### 4. Implementer La fonction de selection `tournament`

Ici, chaque individu a une probabilité d'être séléctionné proportionnelle à son score

<details>
<summary>Implémentation</summary>
TODO
</details>














