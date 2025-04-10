

def alinear_centrado(df):
    """
    Aplica estilos de alineación centrada a un DataFrame.
    """
    return df.style.set_properties(**{'text-align': 'center'}) \
                    .set_table_styles([
                        {'selector': 'th', 'props': [('text-align', 'center')]},  # Alineación de encabezados al centro
                        {'selector': 'td', 'props': [('text-align', 'center')]}   # Alineación de celdas al centro
                    ])


def alinear_izquierda(df):
    """
    Aplica estilos de alineación centrada a un DataFrame.
    """
    return df.style.set_properties(**{'text-align': 'left'}) \
                    .set_table_styles([
                        {'selector': 'th', 'props': [('text-align', 'left')]},  # Alineación de encabezados al centro
                        {'selector': 'td', 'props': [('text-align', 'left')]}   # Alineación de celdas al centro
                    ])

def alinear_derecha(df):
    """
    Aplica estilos de alineación centrada a un DataFrame.
    """
    return df.style.set_properties(**{'text-align': 'right'}) \
                    .set_table_styles([
                        {'selector': 'th', 'props': [('text-align', 'right')]},  # Alineación de encabezados al centro
                        {'selector': 'td', 'props': [('text-align', 'right')]}   # Alineación de celdas al centro
                    ])