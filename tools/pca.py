import numpy as np
from sklearn.decomposition import PCA
import joblib

class PCAReducer:
    def __init__(self, out_dim=256, whiten=False):
        """
        out_dim : target PCA dimension
        whiten : whether to apply PCA whitening
        """
        self.out_dim = out_dim
        self.whiten = whiten
        self.pca = PCA(n_components=out_dim, whiten=whiten)

    def fit(self, features: np.ndarray):
        """
        features: (N, D) numpy array
        """
        assert features.ndim == 2, "Input must be 2D (N, D)"
        self.pca.fit(features)

    def transform(self, features: np.ndarray):
        """
        features: (N, D) numpy array
        returns: (N, out_dim)
        """
        return self.pca.transform(features)

    def fit_transform(self, features: np.ndarray):
        return self.pca.fit_transform(features)

    def save(self, path):
        joblib.dump(self.pca, path)

    def load(self, path):
        self.pca = joblib.load(path)

# features: (num_frames, FEAT_DIM)
pca = PCAReducer(out_dim=256)

pca.fit(train_features)
train_pca = pca.transform(train_features)
val_pca   = pca.transform(val_features)

pca.save("pca_256.joblib")
      
        