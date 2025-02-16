import flet as ft
import os
import sqlite3
import plotly.graph_objects as go

from flet.plotly_chart import PlotlyChart

cor_cinza = "#1a1a1a"
cor_branca = "#ebebeb"
cor_azul = "#1968a8"
cor_vermelha = "#f22929"
cor_verde = "#18661f"
cor_transparente = ft.colors.TRANSPARENT
negrito = ft.FontWeight.BOLD
fonte = "Roboto"

def tela_painel_administrador_aba1(page: ft.Page):
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

    def quantidade_de_usuarios():
        banco_cadastros = os.path.join(os.path.dirname(__file__), '..', 'data', 'cadastros.db')
        banco_cadastros = os.path.abspath(banco_cadastros)
        conn = sqlite3.connect(banco_cadastros)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT COUNT(*) FROM tabela_cadastros
        """)
        quantidade_de_usuarios_total = cursor.fetchone()[0]
        entrada1_painel_administrador_aba1.content.value = quantidade_de_usuarios_total
        entrada1_painel_administrador_aba1.update()
        conn.close()

    def aprovacoes_pendentes():
        banco_cadastros = os.path.join(os.path.dirname(__file__), '..', 'data', 'cadastros.db')
        banco_cadastros = os.path.abspath(banco_cadastros)
        conn = sqlite3.connect(banco_cadastros)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT COUNT(*) FROM tabela_cadastros WHERE cargo = "none"
        """)
        aprovacoes_pendentes_total = cursor.fetchone()[0]
        entrada2_painel_administrador_aba1.content.value = aprovacoes_pendentes_total
        entrada2_painel_administrador_aba1.update()
        conn.close()

    def total_por_cargo():
        banco_cadastros = os.path.join(os.path.dirname(__file__), '..', 'data', 'cadastros.db')
        banco_cadastros = os.path.abspath(banco_cadastros)
        conn = sqlite3.connect(banco_cadastros)
        cursor = conn.cursor()
        cargos = ["Administrador", "Diretor", "Financeiro", "Gerente", "Operador", "Recursos Humanos", "Supervisor", "TI"]
        valores = []
        for cargo in cargos:
            cursor.execute(f"""SELECT COUNT(*) FROM tabela_cadastros WHERE cargo = ?""", (cargo,))
            valores.append(cursor.fetchone()[0])
        conn.close()
        cores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']
        figura = go.Figure(
            data=[
                go.Pie(labels=cargos, values=valores, marker=dict(colors=cores),textinfo="percent",
                insidetextfont=dict(color=cor_branca), pull=[0.1 if v == max(valores) else 0 for v in valores])
            ]
        )
        figura.update_layout(
            title="Distribuição de Cargos",
            title_font=dict(size=20, family=fonte, color=cor_branca),
            paper_bgcolor=cor_cinza,
            font=dict(color=cor_branca),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.5,
                xanchor="center",
                x=0.5
            )
        )
        grafico1_painel_administrador_aba1.content = PlotlyChart(figura)
        grafico1_painel_administrador_aba1.update()

    entrada1_painel_administrador_aba1 = ft.Container(
        content=ft.TextField(
            text_align=ft.TextAlign.CENTER, cursor_color=cor_branca, cursor_width=2, cursor_height=20,
            selection_color=cor_azul, text_size=16, text_vertical_align=0, label="Quantidade de Usuários",
            color=cor_branca, border_radius=15, border_width=2, border_color=cor_branca,
            text_style=ft.TextStyle(size=16, font_family=fonte, color=cor_branca), label_style=ft.TextStyle(size=20,
            font_family=fonte, color=cor_branca,  weight=negrito), value="", read_only=True
        ),
        alignment=ft.alignment.center,
        width=200,
        height=40
    )

    entrada2_painel_administrador_aba1 = ft.Container(
        content=ft.TextField(
            text_align=ft.TextAlign.CENTER, cursor_color=cor_branca, cursor_width=2, cursor_height=20,
            selection_color=cor_azul, text_size=16, text_vertical_align=0, label="Aprovações Pendentes",
            color=cor_branca, border_radius=15, border_width=2, border_color=cor_branca,
            text_style=ft.TextStyle(size=16, font_family=fonte, color=cor_branca), label_style=ft.TextStyle(size=20,
            font_family=fonte, color=cor_branca,  weight=negrito), value="", read_only=True
        ),
        alignment=ft.alignment.center,
        width=200,
        height=40
    )

    grafico1_painel_administrador_aba1 = ft.Container(
        alignment=ft.alignment.center,
        width=1240,
        height=510

    )

    linha1_painel_administrador_aba1 = ft.Container(
        content=ft.Row(
            [
                entrada1_painel_administrador_aba1,
                entrada2_painel_administrador_aba1
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center
    )


    fundo1_painel_administrador_aba1 = ft.Container(
        content=ft.Column(
            [
                linha1_painel_administrador_aba1,
                grafico1_painel_administrador_aba1
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        alignment=ft.alignment.center,
        bgcolor=cor_cinza,
        width=1240,
        height=580,
        border_radius=15
    )

    tela_atual = ft.Container(
        content=ft.Column(
            [
                fundo1_painel_administrador_aba1
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center
    )

    page.add(tela_atual)
    quantidade_de_usuarios()
    aprovacoes_pendentes()
    total_por_cargo()

#ft.app(target=tela_painel_administrador_aba1)