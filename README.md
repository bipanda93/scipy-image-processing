# 🖼️ Traitement d'Images avec SciPy ndimage

> Atelier pratique : 5 transformations d'images avec scipy.ndimage

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python)](https://www.python.org/)
[![SciPy](https://img.shields.io/badge/SciPy-1.7+-8CAAE6?logo=scipy)](https://scipy.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.21+-013243?logo=numpy)](https://numpy.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📋 Description

Projet explorant 5 transformations fondamentales du traitement numérique d'images avec `scipy.ndimage`.

**Image utilisée :** Portrait (612 × 408 px, RGB)  
**Stack :** Python • SciPy • NumPy • Matplotlib • Computer Vision

## 🎯 Transformations Implémentées

### 1. Flou Gaussien (`gaussian_filter`)
**Principe :** Convolution G(x,y) = (1/2πσ²)·exp(−(x²+y²)/2σ²)

- σ = 3 : Flou modéré
- σ = 8 : Flou fort

**Use case :** Réduction de bruit, prétraitement ML

---

### 2. Détection de Contours Sobel (`sobel`)
**Principe :** Magnitude du gradient M = √(Gx² + Gy²)

- Détection bords nets (museau, oreilles, yeux)
- Fond flou → zones sombres

**Use case :** Segmentation d'objets, détection de visages

---

### 3. Rotation (`rotate`)
**Principe :** Transformation affine + interpolation spline

- 30° (reshape=False) : Grille inchangée (408×612)
- 45° (reshape=True) : Grille élargie (721×721)

**Use case :** Data augmentation, correction d'orientation

---

### 4. Zoom (`zoom`)
**Principe :** Rééchantillonnage spatial avec interpolation

- ×2 : Agrandissement (816×1224 px)
- ×0.5 : Réduction (204×306 px)

**Use case :** Changement de résolution, multi-échelles

---

### 5. Filtre de Moyenne (`uniform_filter`)
**Principe :** Moyenne I'(x,y) = (1/n²)·ΣΣI(x+i,y+j)

- size=10 : Lissage modéré
- size=25 : Lissage fort

**Use case :** Réduction de bruit rapide, temps réel

## 📊 Résultats Comparatifs

| Transformation | Fonction SciPy | Paramètre clé | Effet visuel |
|----------------|----------------|---------------|--------------|
| Flou Gaussien | `gaussian_filter()` | σ (sigma) | Lissage naturel |
| Sobel | `sobel()` | axis | Détection bords |
| Rotation | `rotate()` | angle | Pivote l'image |
| Zoom | `zoom()` | facteur | Agrandit/réduit |
| Filtre Uniforme | `uniform_filter()` | size | Lissage uniforme |

## 🚀 Installation
```bash
git clone https://github.com/bipanda93/scipy-image-processing.git
cd scipy-image-processing

pip install -r requirements.txt
```

## 💻 Utilisation
```bash
python atelier_scipy_ndimage.py
```

Les résultats sont sauvegardés dans `./results/`

## 📁 Structure
```
scipy-image-processing/
├── atelier_scipy_ndimage.py    # Script principal
├── atelier_image.jpg            # Image source
├── rapport_final_scipy.pdf      # Rapport détaillé
├── requirements.txt             # Dépendances
├── README.md                    # Ce fichier
├── LICENSE                      # MIT License
└── results/                     # Images générées
    ├── 00_original.jpg
    ├── 01_gaussian_comparison.jpg
    ├── 02_sobel_contours.jpg
    ├── 03_rotations.jpg
    ├── 04_zooms.jpg
    ├── 05_uniform_filters.jpg
    └── 06_vue_ensemble.jpg
```

## 📈 Applications Pratiques

### Computer Vision
- Détection d'objets (Sobel)
- Reconnaissance faciale (flou gaussien)
- OCR (détection de bords)

### Deep Learning
- Data Augmentation (rotation, zoom)
- Prétraitement CNN
- Feature Engineering

### Analyse d'Images Médicales
- IRM/Scanner (réduction de bruit)
- Détection d'anomalies (Sobel)

## 👨‍💻 Auteur

**Franck Ulrich BIPANDA**

Master 2 Data Engineer - Digital School of Paris

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Franck_Bipanda-blue?logo=linkedin)](https://www.linkedin.com/in/franck-bipanda-13392372)
[![GitHub](https://img.shields.io/badge/GitHub-bipanda93-black?logo=github)](https://github.com/bipanda93)
[![Portfolio](https://img.shields.io/badge/Portfolio-orange)](https://www.datascienceportfol.io/bipandaf)

## 📜 Licence

MIT License - Voir [LICENSE](LICENSE)

## 📚 Ressources

- [Documentation SciPy ndimage](https://docs.scipy.org/doc/scipy/reference/ndimage.html)
- [NumPy User Guide](https://numpy.org/doc/stable/user/index.html)
- [Computer Vision Course (Stanford CS231n)](http://cs231n.stanford.edu/)

---

⭐ **Si ce projet vous a été utile, donnez-lui une étoile !** ⭐
