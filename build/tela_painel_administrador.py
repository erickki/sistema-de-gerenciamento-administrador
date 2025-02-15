import flet as ft

cor_cinza = "#1a1a1a"
cor_cinza2 = "#8a8a8a"
cor_branca = "#ebebeb"
cor_azul = "#0390fc"
cor_vermelha = "#f22929"
cor_verde = "#18661f"
cor_transparente = ft.colors.TRANSPARENT
negrito = ft.FontWeight.BOLD
fonte = "Roboto"

def tela_painel_administrador(page: ft.Page):
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
    page.auto_scroll = True
    page.scroll = True

    from build.tela_painel_administrador_aba1 import tela_painel_administrador_aba1
    from build.tela_painel_administrador_aba2 import tela_painel_administrador_aba2
    from build.tela_painel_administrador_aba3 import tela_painel_administrador_aba3
    from build.tela_painel_administrador_aba4 import tela_painel_administrador_aba4

    def carregar_aba1():
        page.clean()
        page.add(tela_atual)
        fundo2_painel_administrador.content = tela_painel_administrador_aba1(page)
        page.update()

    def carregar_aba2():
        page.clean()
        page.add(tela_atual)
        fundo2_painel_administrador.content = tela_painel_administrador_aba2(page)
        page.update()

    def carregar_aba3():
        page.clean()
        page.add(tela_atual)
        fundo2_painel_administrador.content = tela_painel_administrador_aba3(page)
        page.update()

    def carregar_aba4():
        page.clean()
        page.add(tela_atual)
        fundo2_painel_administrador.content = tela_painel_administrador_aba4(page)
        page.update()

    def carregar_geral(e):
        if e.control.selected_index == 0:
            carregar_aba1()
        elif e.control.selected_index == 1:
            carregar_aba2()
        elif e.control.selected_index == 2:
            carregar_aba3()
        elif e.control.selected_index == 3:
            carregar_aba4()

    # Aba - Geral
    barra_de_navegacao1_painel_administrador = ft.Container(
        content=ft.Tabs(
            tabs=[
                ft.Tab(text="Painel de Estatísticas"),
                ft.Tab(text="Aprovação de Cadastros"),
                ft.Tab(text="Gerenciamento de Cadastros"),
                ft.Tab(text="Controle de Acessos e Logs")
            ], tab_alignment=ft.TabAlignment.START, divider_color=cor_cinza, indicator_color=cor_branca,
            indicator_border_radius=15, indicator_border_side=ft.BorderSide(width=2, color=cor_branca),
            indicator_padding=0, indicator_tab_size=True, label_color=cor_branca, label_text_style=ft.TextStyle(size=14,
            weight=negrito, font_family=fonte), unselected_label_color=cor_cinza2,
            unselected_label_text_style=ft.TextStyle(size=14, weight=negrito, italic=True, font_family=fonte),
            overlay_color=cor_transparente, divider_height=2, indicator_thickness=2, on_change=carregar_geral
        ),
        alignment=ft.alignment.center,
        width=1240,
        height=50,
        border_radius=15
    )

    fundo1_painel_administrador = ft.Container(
        content=ft.Column(
            [
                barra_de_navegacao1_painel_administrador
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center,
        bgcolor=cor_cinza,
        width=1240,
        height=50,
        border_radius=15
    )

    fundo2_painel_administrador = ft.Container(
        content=None
    )

    tela_atual = ft.Container(
        content=ft.Column(
            [
                fundo1_painel_administrador,
                fundo2_painel_administrador
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center
    )

    page.add(tela_atual)
    carregar_aba1()

#ft.app(target=tela_painel_administrador)