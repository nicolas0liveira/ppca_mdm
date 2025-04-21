import matplotlib.pyplot as plt

DEFAULT_STYLE = 'seaborn-v0_8'
DEFAULT_FONT = 'DejaVu Sans'
DEFAULT_FONTSIZE = 12

def set_plot_style(style=DEFAULT_STYLE, font=DEFAULT_FONT, fontsize=DEFAULT_FONTSIZE, report_mode=False):
    """
    Define o tema visual dos gráficos matplotlib.
    """
    if report_mode:
        style = 'default'  # visual limpo para relatórios impressos

    plt.style.use(style)

    plt.rcParams.update({
        'font.family': font,
        'font.size': fontsize,
        'axes.titlesize': fontsize + 2,
        'axes.labelsize': fontsize,
        'xtick.labelsize': fontsize - 1,
        'ytick.labelsize': fontsize - 1,
        'legend.fontsize': fontsize - 1,
        'figure.titlesize': fontsize + 4,
        'axes.grid': not report_mode,
        'grid.alpha': 0.3 if not report_mode else 0.0,
        'grid.linestyle': '--',
        'axes.facecolor': 'white' if report_mode else plt.rcParams['axes.facecolor'],
        'savefig.facecolor': 'white'
    })

def get_default_colors(n=10):
    """
    Retorna uma lista de n cores da paleta tab10.
    """
    from matplotlib.cm import get_cmap
    cmap = get_cmap('tab10')
    return [cmap(i) for i in range(n)]


def get_category_colors(mapping=None):
    """
    Retorna um dicionário de cores por categoria.

    Parameters:
    - mapping: dict, ex: {'S': '#1b9e77', 'N': '#d95f02'}
    """
    if mapping is None:
        mapping = {
            'S': '#1b9e77',
            'SIM': '#1b9e77',
            'N': '#d95f02',
            'NAO': '#d95f02',
            'NÃO': '#d95f02',
        }
    return mapping