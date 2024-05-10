import numpy as np
from matplotlib import pyplot as plt

def plot_fitted_resids(fitted, resid, show_resid_quantiles=True, nbins=5):
    plt.scatter(fitted, resid)
    plt.xlabel("Fitted values")
    plt.ylabel("Residuals")
    if show_resid_quantiles:
        # bin the residuals using the range of the fitted values, then plot the quantiles of the residuals in each bin
        bins = np.linspace(np.min(fitted), np.max(fitted), nbins)
        bin_inds = np.digitize(fitted, bins)
        # collect the residuals in each bin
        bin_resids = []
        for i in range(len(bins)):
            bin_resids.append(resid[bin_inds==i])
        # compute the outer quantiles of the residuals in each bin
        bin_quantiles = []
        for i in range(len(bins)):
            if len(bin_resids[i])>0:
                bin_quantiles.append(np.quantile(bin_resids[i], [0.025, 0.975]))
            else:
                bin_quantiles.append([0,0])
        plt.plot(bins, [q[0] for q in bin_quantiles], color="red", linestyle="dashed")
        plt.plot(bins, [q[1] for q in bin_quantiles], color="red", linestyle="dashed")
        plt.show()

def plot_outliers(fitted, resid_studentized, threshold=3):
    plt.scatter(fitted, resid_studentized)
    plt.xlabel("Fitted values")
    plt.ylabel("Studentized residuals")
    plt.axhline(threshold, color="red", linestyle="dashed")
    plt.axhline(-threshold, color="red", linestyle="dashed")
    plt.show()

def plot_leverage(fitted, leverage, threshold=0.05):
    plt.scatter(fitted, leverage)
    plt.xlabel("Fitted values")
    plt.ylabel("Leverage")
    plt.axhline(threshold, color="red", linestyle="dashed")
    plt.show()