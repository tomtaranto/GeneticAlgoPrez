# Presentation algorithme génétique

## Contenu

- [Présentation](#présentation)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Hands-On](#Hands-On)

## Présentation

Ce projet est une présentation de l'algorithme génétique. Il a été réalisé dans le cadre des journées de partage
d'[Ekinox](www.ekinox.io).

Il permet de trouver les parametres optimaux pour avoir le meilleur café possible.

## Installation

### Python

Se rendre dans le dossier python

```bash
  cd python
```

Installer les dépendances

```bash
  poetry install
```

Lancer les tests

```bash
  poetry run pytest
```

Lancer le projet

```bash
  poetry run python main.py
```

### Java

Se rendre dans le dossier java

```bash
  cd java
```

Installer les dépendances

```bash
  mvn clean install
```

Lancer les tests

```bash
  mvn test
```

Lancer le projet
```bash
  mvn exec:java -Dexec.mainClass="com.ekinox.geneticalgo.Main"
```


## Typescript

Se rendre dans le dossier typescript

```bash
  cd typescript
```

Installer les dépendances

```bash
  npm install
```

Lancer les tests

```bash
  npm test
```

Lancer le projet

```bash
  npm start
```

## Utilisation

Un premier algorithme est déjà implémenté.

Le but du hands-on est de modifier l'algo.

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

Utiliser le dataset `"paris_metro"` pour tester l'impact de cette variable. Partir de 0 et augmenter petit à petit le
nombre.

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














