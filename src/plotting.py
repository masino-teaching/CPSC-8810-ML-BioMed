import matplotlib.pyplot as plt
import seaborn as sns

def plt_kde_grid(data, num_cols = 4, fig_size = (20, 20)):
    return plt_grid(data, sns.kdeplot, num_cols, fig_size)

def plt_box_grid(data, num_cols = 4, fig_size = (20, 20), add_xlabel = False):
    return plt_grid(data, sns.boxplot, num_cols, fig_size)

def plt_grid(data, plot_func, num_cols = 4, fig_size = (20, 20), add_xlabel = True):
    l = data.columns.tolist()
    num_figs = len(l)
    num_rows = -(-len(l) // num_cols)
    fig, ax = plt.subplots(num_rows, num_cols, figsize=fig_size, squeeze=False)
    row = 0
    col = 0
    cnt = 0
    for _ in l:
        plot_func(data[data.columns[cnt]], ax=ax[row, col])
        if add_xlabel:
            ax[row, col].set_xlabel(data.columns[cnt])
        cnt += 1
        if cnt % num_cols == 0:
            row += 1
            col = 0
        else:
            col += 1
    fig.tight_layout()
    plt.show()
    return fig, ax