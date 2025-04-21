import os

def save_figure(fig, filename, output_dir='reports/figures', formats=('png',), dpi=300):
    """
    Salva uma figura matplotlib em múltiplos formatos.

    Parameters:
    - fig: matplotlib.figure.Figure
    - filename: str, nome do arquivo (sem extensão)
    - output_dir: str, pasta onde os arquivos serão salvos
    - formats: tuple, formatos desejados (ex: ('png', 'pdf'))
    - dpi: int, resolução da imagem

    Use Example: save_figure(fig, 'proporcao_indicador_ajuizado', formats=('png', 'pdf'))
    """
    os.makedirs(output_dir, exist_ok=True)
    for ext in formats:
        path = os.path.join(output_dir, f"{filename}.{ext}")
        fig.savefig(path, dpi=dpi, bbox_inches='tight')


