import numpy as np
from scipy.cluster.hierarchy import dendrogram
from sklearn.cluster import KMeans, AgglomerativeClustering as HClust

def compute_linkage(hclust):
    counts = np.zeros(hclust.children_.shape[0])
    n_samples = len(hclust.labels_)
    for i, merge in enumerate(hclust.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack([hclust.children_, hclust.distances_,
                                      counts]).astype(float)
    return linkage_matrix

def plot_hclust(data, labels, linkage_method, ax, cut=-np.inf):
    cargs = {'above_threshold_color': 'grey', 'color_threshold': cut}
    hc = HClust(n_clusters=None,
                distance_threshold=0,
                linkage=linkage_method.lower()).fit(data)
   # linkage_ = linkage(hc, method=linkage_method.lower())
    linkage_ = compute_linkage(hc)
    dendrogram(linkage_, ax=ax, labels = np.asarray(labels), leaf_font_size=10, **cargs)
    ax.set_title(f'{linkage_method} linkage')
    return hc