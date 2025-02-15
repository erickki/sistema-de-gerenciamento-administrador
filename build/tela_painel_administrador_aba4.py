import flet as ft
import os
import sqlite3

cor_cinza = "#1a1a1a"
cor_branca = "#ebebeb"
cor_azul = "#1968a8"
cor_vermelha = "#f22929"
cor_verde = "#18661f"
cor_transparente = ft.colors.TRANSPARENT
negrito = ft.FontWeight.BOLD
fonte = "Roboto"

def tela_painel_administrador_aba4(page: ft.Page):
    page.bgcolor = cor_cinza
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = ft.padding.all(0)
    page.title = "Painel - Administrador."
    page.window.alignment = ft.alignment.top_center
    page.window.width = 1280 # Largura
    page.window.height = 720 # Altura
    page.window.maximizable = True
    page.window.minimizable = True
    page.expand = True

    def carregar_dados_painel_administrador_aba4():
        banco_cadastros = os.path.join(os.path.dirname(__file__), '..', 'data', 'cadastros.db')
        banco_cadastros = os.path.abspath(banco_cadastros)
        conn = sqlite3.connect(banco_cadastros)
        cursor = conn.cursor()
        cursor.execute("""
        PRAGMA table_info(tabela_cadastros_logs)
        """)
        colunas = [col[1] for col in cursor.fetchall()]
        cursor.execute("""
        SELECT * FROM tabela_cadastros_logs
        WHERE id_empresa <> 'admin'
        """)
        dados = cursor.fetchall()
        conn.close()
        return colunas, dados

    colunas, dados = carregar_dados_painel_administrador_aba4()

    cabecalho_painel_administrador_aba4 = [ft.DataColumn(ft.Text(nome),
                                            heading_row_alignment=ft.MainAxisAlignment.START) for nome in colunas]
    
    dados_painel_administrador_aba4 = [ft.DataRow(cells=[ft.DataCell(ft.Text(str(campo))) for campo in linha])
                               for linha in dados]

    def filtrar_nomes(e):
        nome_busca = entrada1_painel_administrador_aba4.content.value.strip()
        banco_cadastros = os.path.join(os.path.dirname(__file__), '..', 'data', 'cadastros.db')
        banco_cadastros = os.path.abspath(banco_cadastros)
        conn = sqlite3.connect(banco_cadastros)
        cursor = conn.cursor()
        if nome_busca:
            cursor.execute("""
            SELECT * FROM tabela_cadastros_logs
            WHERE nome LIKE ?
            AND id_empresa <> 'admin'
            """, (f"%{nome_busca}%",))
        else:
            cursor.execute("""
            SELECT * FROM tabela_cadastros_logs
            WHERE id_empresa <> 'admin'
            """)
        dados_filtrados = cursor.fetchall()
        conn.close()
        dados_painel_administrador_aba4 = [ft.DataRow(cells=[ft.DataCell(ft.Text(str(campo))) for campo in linha])
                                            for linha in dados_filtrados]
        tabela1_painel_administrador_aba4.content = ft.DataTable(
            columns=cabecalho_painel_administrador_aba4, rows=dados_painel_administrador_aba4, border_radius=15,
            column_spacing=10, data_row_color=cor_branca, data_text_style=ft.TextStyle(size=12, font_family=fonte,
            color=cor_cinza), bgcolor=cor_branca, divider_thickness=2, heading_row_color=cor_branca,
            heading_text_style=ft.TextStyle(size=14, font_family=fonte, color=cor_cinza, weight=negrito), width=1230,
            height=520, show_bottom_border=True, show_checkbox_column=True
        )
        page.update()

    def filtrar_datas(e):
        data_inicial = entrada2_painel_administrador_aba4.content.value.strip()
        data_final = entrada3_painel_administrador_aba4.content.value.strip()
        banco_cadastros = os.path.join(os.path.dirname(__file__), '..', 'data', 'cadastros.db')
        banco_cadastros = os.path.abspath(banco_cadastros)
        conn = sqlite3.connect(banco_cadastros)
        cursor = conn.cursor()
        query = """
        SELECT * FROM tabela_cadastros_logs
        WHERE 1=1
        AND id_empresa <> 'admin'
        """
        params = []
        if data_inicial:
            query += " AND substr(data_hora_log, 1, 10) >= ?"
            params.append(data_inicial)
        if data_final:
            query += " AND substr(data_hora_log, 1, 10) <= ?"
            params.append(data_final)
        cursor.execute(query, params)
        dados_filtrados = cursor.fetchall()
        conn.close()
        dados_painel_administrador_aba4 = [
            ft.DataRow(cells=[ft.DataCell(ft.Text(str(campo))) for campo in linha])
            for linha in dados_filtrados
        ]
        tabela1_painel_administrador_aba4.content = ft.DataTable(
            columns=cabecalho_painel_administrador_aba4,
            rows=dados_painel_administrador_aba4,
            border_radius=15,
            column_spacing=10,
            data_row_color=cor_branca,
            data_text_style=ft.TextStyle(size=12, font_family=fonte, color=cor_cinza),
            bgcolor=cor_branca,
            divider_thickness=2,
            heading_row_color=cor_branca,
            heading_text_style=ft.TextStyle(size=14, font_family=fonte, color=cor_cinza, weight=negrito),
            width=1230,
            height=520,
            show_bottom_border=True,
            show_checkbox_column=True
        )
        page.update()

    tabela1_painel_administrador_aba4 = ft.Container(
        content=ft.DataTable(
            columns=cabecalho_painel_administrador_aba4, rows=dados_painel_administrador_aba4, border_radius=15, column_spacing=10,
            data_row_color=cor_branca, data_text_style=ft.TextStyle(size=12, font_family=fonte, color=cor_cinza),
            bgcolor=cor_branca, divider_thickness=2, heading_row_color=cor_branca,
            heading_text_style=ft.TextStyle(size=14, font_family=fonte, color=cor_cinza, weight=negrito), width=1230,
            height=520, show_bottom_border=True, show_checkbox_column=True
        ),
        alignment=ft.alignment.center,
        bgcolor=cor_branca,
        width=1240,
        height=530,
        border_radius=15
    )

    fundo1_painel_administrador_aba4 = ft.Container(
        content=ft.Column(
            [
                tabela1_painel_administrador_aba4
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center,
        bgcolor=cor_branca,
        width=1240,
        height=530,
        border_radius=15
    )

    entrada1_painel_administrador_aba4 = ft.Container(
        content=ft.TextField(
            text_align=ft.TextAlign.START, cursor_color=cor_branca, cursor_width=2, cursor_height=20,
            selection_color=cor_azul, text_size=12, text_vertical_align=0, label="Localizar Nome", color=cor_branca,
            border_radius=15, border_width=2, border_color=cor_branca, text_style=ft.TextStyle(size=12,
            font_family=fonte, color=cor_branca), label_style=ft.TextStyle(size=14, font_family=fonte, color=cor_branca,
            weight=negrito), on_change=filtrar_nomes
        ),
        alignment=ft.alignment.center,
        width=200,
        height=40
    )

    entrada2_painel_administrador_aba4 = ft.Container(
        content=ft.TextField(
            text_align=ft.TextAlign.START, cursor_color=cor_branca, cursor_width=2, cursor_height=20,
            selection_color=cor_azul, text_size=12, text_vertical_align=0, label="Data Inicial", color=cor_branca,
            border_radius=15, border_width=2, border_color=cor_branca, text_style=ft.TextStyle(size=12,
            font_family=fonte, color=cor_branca), label_style=ft.TextStyle(size=14, font_family=fonte, color=cor_branca,
            weight=negrito), on_change=filtrar_datas
        ),
        alignment=ft.alignment.center,
        width=200,
        height=40
    )

    entrada3_painel_administrador_aba4 = ft.Container(
        content=ft.TextField(
            text_align=ft.TextAlign.START, cursor_color=cor_branca, cursor_width=2, cursor_height=20,
            selection_color=cor_azul, text_size=12, text_vertical_align=0, label="Data Final", color=cor_branca,
            border_radius=15, border_width=2, border_color=cor_branca, text_style=ft.TextStyle(size=12,
            font_family=fonte, color=cor_branca), label_style=ft.TextStyle(size=14, font_family=fonte, color=cor_branca,
            weight=negrito), on_change=filtrar_datas
        ),
        alignment=ft.alignment.center,
        width=200,
        height=40
    )

    fundo2_painel_administrador_aba4 = ft.Container(
        content=ft.Row(
            [
                entrada1_painel_administrador_aba4,
                entrada2_painel_administrador_aba4,
                entrada3_painel_administrador_aba4
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center,
        bgcolor=cor_cinza,
        width=1240,
        height=50,
        border_radius=15
    )

    tela_atual = ft.Container(
        content=ft.Column(
            [
                fundo1_painel_administrador_aba4,
                fundo2_painel_administrador_aba4
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center
    )

    page.add(tela_atual)

#ft.app(target=tela_painel_administrador_aba4)