#
# Plotting utilies
# ML Utilities
#

import numpy as np
import matplotlib.pyplot as plt

# Plot the 2D classification decision boundary for the given dataset features
# space given by given feature a and b with the given step resolution
def plot_2d_decison_bounds(model, feature_a, feature_b, step=0.1):
    # construct mesh grid to evaluate classifier over
    a_range = np.arange(np.min(feature_a), np.max(feature_a), step=step)
    b_range = np.arange(np.min(feature_b), np.max(feature_b), step=step)
    a_mesh, b_mesh = np.meshgrid(a_range, b_range)
    meshgrid = np.stack([a_mesh, b_mesh], axis=-1) # stack on last axis

    # obtain predictions with classifier model
    preds = model.predict(meshgrid.reshape((-1, 2)))
    grid_dim = a_mesh.shape
    pred_grid = preds.reshape(grid_dim)

    plt.contourf(a_mesh, b_mesh, pred_grid, alpha=0.4)


if __name__ == "__main__":
    # Decision boundary test
    from sklearn import datasets
    from sklearn.ensemble import RandomForestClassifier

    iris = datasets.load_iris()
    X = iris.data[:, [0, 2]]
    y = iris.target
    model = RandomForestClassifier(n_estimators=200, max_depth=2)
    model.fit(X, y)

    feature_a, feature_b = X[:,0], X[:, 1]

    plot_2d_decison_bounds(model, feature_a, feature_b)
    plt.scatter(feature_a, feature_b, c=y.astype("int"), cmap="coolwarm", s=20)
    plt.show()
