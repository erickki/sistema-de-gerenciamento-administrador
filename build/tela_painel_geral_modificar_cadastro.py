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

def tela_painel_geral_cadastro(page: ft.Page):
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

    fundo1_painel_geral_cadastro = ft.Container(
        content=ft.Column(
            [
                
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

    fundo2_painel_geral_cadastro = ft.Container(
        content=ft.Column(
            [
                
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center,
        bgcolor=cor_branca,
        width=1240,
        height=50,
        border_radius=15
    )

    tela_atual = ft.Container(
        content=ft.Column(
            [
                fundo1_painel_geral_cadastro,
                fundo2_painel_geral_cadastro
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        alignment=ft.alignment.center
    )

    page.add(tela_atual)

ft.app(target=tela_painel_geral_cadastro)