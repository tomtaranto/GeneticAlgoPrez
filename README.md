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

### 1. Modifier la taille de la population

<details>
<summary>Résultats attendus</summary>
La convergence vers une solution est plus rapide lorsque la population est grande
</details>

### 2. Modifier le taux de mutation

<details>
<summary>Résultats attendus</summary>
Un taux moyen de mutation permet d'avoir des resultats plus rapidement.
Un taux trop fort de mutation peut empecher la convergence.
</details>

### 3. Implementer La fonction de selection `roulette`

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














