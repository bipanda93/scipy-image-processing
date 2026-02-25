# 🖼️ Traitement d'Images avec SciPy ndimage

> Atelier pratique : 5 transformations d'images avec scipy.ndimage

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python)](https://www.python.org/)
[![SciPy](https://img.shields.io/badge/SciPy-1.7+-8CAAE6?logo=scipy)](https://scipy.org/)

## 📋 Description

Ce projet explore cinq transformations fondamentales du traitement d'images avec `scipy.ndimage` :

1. **Flou Gaussien** - Lissage par convolution gaussienne
2. **Détection de Contours (Sobel)** - Extraction de gradients
3. **Rotation** - Transformation affine
4. **Zoom** - Rééchantillonnage spatial
5. **Filtre de Moyenne** - Lissage uniforme

## 🚀 Installation
```bash
pip install -r requirements.txt
```

## 💻 Utilisation
```bash
python atelier_scipy_ndimage.py
```

## 📊 Transformations Implémentées

### 1. Flou Gaussien
**Principe :** Convolution G(x,y) = (1/2πσ²)·exp(−(x²+y²)/2σ²)

### 2. Sobel (Détection de Contours)
**Principe :** Magnitude du gradient M = √(Gx² + Gy²)

### 3. Rotation
**Principe :** Transformation affine + interpolation spline

### 4. Zoom
**Principe :** Rééchantillonnage avec interpolation

### 5. Filtre de Moyenne
**Principe :** Moyenne uniforme I'(x,y) = (1/n²)·ΣΣI(x+i,y+j)

## 📁 Structure
```
scipy-image-processing/
├── atelier_scipy_ndimage.py    # Script principal
├── atelier_image.jpg            # Image source
├── rapport_final_scipy.pdf      # Rapport détaillé
├── requirements.txt             # Dépendances
├── README.md                    # Ce fichier
└── LICENSE                      # Licence MIT
```

## 👨‍💻 Auteur

**Franck Ulrich BIPANDA**
- Master 2 Data Engineer - Digital School of Paris
- [LinkedIn](https://www.linkedin.com/in/franck-bipanda-13392372)
- [GitHub](https://github.com/bipanda93)

## 📜 Licence

MIT License - Voir [LICENSE](LICENSE)
