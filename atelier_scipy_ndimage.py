# =============================================================================
#  ATELIER SCIPY — Traitement d'Images avec scipy.ndimage
#  Digital School of Paris — Mastère Data Engineering
#  Auteur : Franck
# =============================================================================
#
#  Bibliothèques requises :
#    pip install scipy numpy matplotlib Pillow
#
#  Lancer le script :
#    python atelier_scipy_ndimage.py
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from PIL import Image

# =============================================================================
# PARTIE 1 — CHARGEMENT DE L'IMAGE
# =============================================================================

# Charger l'image depuis le disque et la convertir en tableau NumPy
image = np.array(Image.open("atelier_image.jpg"))

# Afficher les dimensions
print("=" * 50)
print("image.shape :", image.shape)
#  → (360, 480, 3)
#    axe 0 : 360 lignes    (hauteur en pixels)
#    axe 1 : 480 colonnes  (largeur en pixels)
#    axe 2 : 3 canaux      (Rouge, Vert, Bleu — valeurs 0-255)
print("image.dtype :", image.dtype)   # uint8
print("=" * 50)

# Afficher l'image originale
plt.figure(figsize=(7, 5))
plt.imshow(image)
plt.title("Image Originale — shape: {}".format(image.shape))
plt.axis("off")
plt.tight_layout()
plt.show()


# =============================================================================
# PARTIE 2 — TRANSFORMATIONS scipy.ndimage
# =============================================================================

# Helper : afficher deux images côte à côte pour comparaison
def comparer(img_a, title_a, img_b, title_b, cmap_b=None):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.imshow(img_a)
    ax1.set_title(title_a, fontweight="bold")
    ax1.axis("off")
    ax2.imshow(img_b, cmap=cmap_b)
    ax2.set_title(title_b, fontweight="bold")
    ax2.axis("off")
    plt.tight_layout()
    plt.show()


# ─────────────────────────────────────────────────────────────────────────────
# TRANSFORMATION 1 — Flou Gaussien
# ─────────────────────────────────────────────────────────────────────────────
# Mathématiquement : convolution de l'image avec une gaussienne 2-D
#   G(x,y) = (1 / 2πσ²) × exp(-(x²+y²) / 2σ²)
# Chaque pixel devient la moyenne PONDÉRÉE de ses voisins.
# Plus σ est grand → fenêtre plus large → flou plus fort.

gauss3 = ndimage.gaussian_filter(image, sigma=3)
gauss8 = ndimage.gaussian_filter(image, sigma=8)

comparer(image,  "Originale",
         gauss3, "Flou Gaussien σ = 3  (modéré)")
comparer(image,  "Originale",
         gauss8, "Flou Gaussien σ = 8  (fort)")


# ─────────────────────────────────────────────────────────────────────────────
# TRANSFORMATION 2 — Détection de contours (Sobel)
# ─────────────────────────────────────────────────────────────────────────────
# Mathématiquement : approximation du gradient spatial de l'image.
#   Gx = image * Kx   (noyau [-1, 0, 1] amplifié)
#   Gy = image * Ky   (noyau [-1, 0, 1]ᵀ amplifié)
#   M  = √(Gx² + Gy²)   ← magnitude du gradient = force du contour
# Un contour correspond à un changement brusque d'intensité → gradient élevé.

gray   = image.mean(axis=2)                      # niveaux de gris
sob_x  = ndimage.sobel(gray, axis=1)             # gradient horizontal
sob_y  = ndimage.sobel(gray, axis=0)             # gradient vertical
sobel_mag  = np.hypot(sob_x, sob_y)             # magnitude
sobel_norm = (sobel_mag / sobel_mag.max() * 255).astype(np.uint8)

comparer(image,      "Originale (niveaux de gris)",
         sobel_norm, "Contours Sobel — magnitude gradient", cmap_b="gray")


# ─────────────────────────────────────────────────────────────────────────────
# TRANSFORMATION 3 — Rotation
# ─────────────────────────────────────────────────────────────────────────────
# Mathématiquement : transformation affine appliquée à chaque coordonnée.
#   |x'|   |cos θ  -sin θ| |x|
#   |y'| = |sin θ   cos θ| |y|
# Les pixels intermédiaires sont reconstruits par interpolation spline (ordre 3).
# reshape=True → agrandit la grille pour éviter tout rognage.
# cval=20     → couleur de remplissage des zones vides.

rot30 = ndimage.rotate(image,  30, reshape=False, mode="constant", cval=20)
rot45 = ndimage.rotate(image,  45, reshape=True,  mode="constant", cval=20)

comparer(image,
         "Originale  (360×480)",
         np.clip(rot30, 0, 255).astype(np.uint8),
         "Rotation 30° — reshape=False  (360×480)")

comparer(image,
         "Originale  (360×480)",
         np.clip(rot45, 0, 255).astype(np.uint8),
         "Rotation 45° — reshape=True  (594×594)")


# ─────────────────────────────────────────────────────────────────────────────
# TRANSFORMATION 4 — Zoom
# ─────────────────────────────────────────────────────────────────────────────
# Mathématiquement : rééchantillonnage par interpolation spline.
# Chaque coordonnée destination (xd, yd) est ramenée à la coordonnée source :
#   xs = xd / zoom_x,   ys = yd / zoom_y
# La valeur est estimée par interpolation d'ordre 3 (spline cubique).
# zoom=(2, 2, 1) → ×2 en H et L, canaux inchangés.

zoom_in  = ndimage.zoom(image, (2.0, 2.0, 1))   # agrandir ×2
zoom_out = ndimage.zoom(image, (0.5, 0.5, 1))   # réduire  ×0.5

print("Zoom ×2  :", np.clip(zoom_in,  0, 255).astype(np.uint8).shape)   # (720, 960, 3)
print("Zoom ×0.5:", np.clip(zoom_out, 0, 255).astype(np.uint8).shape)   # (180, 240, 3)

comparer(image,
         "Originale  (360×480)",
         np.clip(zoom_in, 0, 255).astype(np.uint8),
         "Zoom ×2  → (720×960)")

comparer(image,
         "Originale  (360×480)",
         np.clip(zoom_out, 0, 255).astype(np.uint8),
         "Zoom ×0.5 → (180×240)")


# ─────────────────────────────────────────────────────────────────────────────
# TRANSFORMATION 5 — Filtre de Moyenne (uniforme)
# ─────────────────────────────────────────────────────────────────────────────
# Mathématiquement : convolution avec un noyau constant de taille n×n.
#   I'(x,y) = (1/n²) × Σᵢ Σⱼ I(x+i, y+j)   pour i,j ∈ [−n/2 ; n/2]
# Tous les voisins ont le MÊME poids (contrairement au gaussien).
# Effet : lissage uniforme — atténue le bruit mais crée un léger effet de bloc.

uni10 = ndimage.uniform_filter(image, size=10)
uni25 = ndimage.uniform_filter(image, size=25)

comparer(image,
         "Originale",
         uni10.astype(np.uint8),
         "Filtre Uniforme size=10  (modéré)")

comparer(image,
         "Originale",
         uni25.astype(np.uint8),
         "Filtre Uniforme size=25  (fort)")


# =============================================================================
# FIGURE DE SYNTHÈSE — Toutes les transformations
# =============================================================================
fig, axes = plt.subplots(3, 4, figsize=(20, 14))
fig.patch.set_facecolor("#0E1117")

panels = [
    (image,                                            None,   "Original (360×480, 3 ch)"),
    (gauss3,                                           None,   "Gaussien sigma=3"),
    (gauss8,                                           None,   "Gaussien sigma=8"),
    (sobel_norm,                                       "gray", "Sobel — contours"),
    (image,                                            None,   "Original (ref)"),
    (np.clip(rot30, 0, 255).astype(np.uint8),          None,   "Rotation 30 deg"),
    (np.clip(rot45, 0, 255).astype(np.uint8),          None,   "Rotation 45 deg (594x594)"),
    (np.clip(zoom_in, 0, 255).astype(np.uint8),        None,   "Zoom x2  (720x960)"),
    (image,                                            None,   "Original (ref)"),
    (np.clip(zoom_out, 0, 255).astype(np.uint8),       None,   "Zoom x0.5 (180x240)"),
    (uni10.astype(np.uint8),                           None,   "Uniforme size=10"),
    (uni25.astype(np.uint8),                           None,   "Uniforme size=25"),
]

for ax, (arr, cm, title) in zip(axes.flat, panels):
    ax.imshow(arr, cmap=cm)
    ax.set_title(title, color="white", fontsize=9, pad=5)
    ax.axis("off")

plt.suptitle("Atelier SciPy — scipy.ndimage — Synthese des transformations",
             color="white", fontsize=15, fontweight="bold")
plt.tight_layout()
plt.show()
