# Pipeline ETL Joconde - Modern Data Stack

Pipeline ETL automatisé pour le catalogue national des œuvres d'art des musées français.

## Description

Pipeline ETL qui collecte, transforme et charge les données du catalogue Joconde - la base de données des collections des musées de France.

**Volume traité :** 721 629 œuvres d'art  
**Qualité finale :** 90.6% de conservation après filtrage (653 686 enregistrements)  
**Stack :** Dagster + dbt + PostgreSQL + Polars + Docker

## Architecture

### Stack Technique

- **Orchestration** : Dagster
- **Transformation** : dbt
- **Stockage** : PostgreSQL (staging + production)
- **Processing** : Polars
- **Containerisation** : Docker

### Flux de Données

```
API Joconde (JSON)
        ↓
    EXTRACT (Python)
        ↓
STAGING (PostgreSQL)
721 629 enregistrements bruts
        ↓
  TRANSFORM (dbt)
  Nettoyage + Tests qualité
        ↓
PRODUCTION (PostgreSQL)
653 686 enregistrements validés
```

## Caractéristiques

**Performance**
- Optimisation -90% temps de traitement (Polars)
- Compression 10x : 450MB → 45MB
- Pipeline optimisé pour grandes volumétries

**Qualité des Données**
- Taux de qualité 90.6% après filtrage
- Tests dbt automatiques
- Validation schéma + business rules
- Déduplication rigoureuse

**Observabilité**
- Dagster UI : monitoring temps réel
- Data Lineage : traçabilité complète
- Documentation auto-générée (dbt)
- Logs détaillés

**Architecture**
- Staging → Production : environnements séparés
- Transformations dbt : SQL versionné et testé
- Containerisation : reproductibilité garantie

## Métriques

| Métrique | Valeur |
|----------|--------|
| Œuvres totales | 721 629 |
| Production | 653 686 |
| Taux qualité | 90.6% |
| Optimisation temps | -90% |
| Compression | 10x |

## Installation

### Prérequis

- Python 3.10+
- PostgreSQL 14+
- Docker

### Setup

```bash
git clone https://github.com/bipanda93/ETL-pipeline-Joconde.git
cd ETL-pipeline-Joconde

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

createdb joconde_staging
createdb joconde_production

cp .env.example .env
```

## Utilisation

### Lancer Dagster

```bash
dagster dev
```

Accéder à l'interface : http://localhost:3000

### Exécuter dbt

```bash
cd dbt_project

dbt run
dbt test
dbt docs generate
dbt docs serve
```

## Structure

```
ETL-pipeline-Joconde/
├── dagster_project/
│   ├── assets/
│   ├── resources/
│   └── jobs/
├── dbt_project/
│   ├── models/
│   │   ├── staging/
│   │   └── production/
│   └── tests/
├── sql/
├── requirements.txt
└── README.md
```

## Pipeline Détaillé

### Extract

Extraction depuis API Joconde via Dagster asset.

### Load Staging

Chargement données brutes en PostgreSQL staging.

### Transform

Transformations dbt :
- Nettoyage des données
- Déduplication
- Validation qualité
- Tests automatiques

### Production

Chargement données validées en PostgreSQL production.

## Tests

```bash
dbt test
dbt test --select staging
dbt test --select production
```

## Optimisations

**Performance**
- Polars pour traitement parallélisé
- Indexation PostgreSQL
- Compression des données

**Qualité**
- Déduplication multi-critères
- Validation en couches (staging + production)
- Tests dbt automatiques

## Auteur

**Franck Ulrich BIPANDA**

Master 2 Data Engineer - Digital School of Paris

- [LinkedIn](https://www.linkedin.com/in/franck-bipanda-13392372)
- [GitHub](https://github.com/bipanda93)
- [Portfolio](https://www.datascienceportfol.io/bipandaf)

## Licence

MIT License

## Ressources

- [API Joconde](https://data.culture.gouv.fr/)
- [Dagster](https://docs.dagster.io/)
- [dbt](https://docs.getdbt.com/)
- [Polars](https://pola-rs.github.io/polars/)
