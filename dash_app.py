import dash

from dash import Dash, html, dcc, Input, Output, State
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import random
import time
#from app import app

def init_dashboard(server):
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashboard/',
        external_stylesheets=[dbc.themes.FLATLY],
        title = "S.O.P.H.I.A."
    )

    # Base de Dados
    df_pizza = pd.read_csv("./dados/Complexidades das Demandas.csv")
    df_barra1 = pd.read_csv("./dados/Consultores Ociosos.csv")
    df_barra2 = pd.read_csv("./dados/Contrato x Demanda.csv")
    df_barra3 = pd.read_csv("./dados/Custo x Venda.csv")
    df_barra4 = pd.read_csv("./dados/Consultores x Complexidade de Atendimentos.csv")
    df_barra5 = pd.read_csv("./dados/Atendimentos ao Longo do Tempo.csv")
    df_linha = pd.read_csv("./dados/Custo ao Longo do Tempo.csv")
    df_linha2 = pd.read_csv("./dados/ProjecaoAbril.csv")

    # Criação de gráficos
    pizza=px.pie(
        df_pizza,
        values='ATENDIMENTOS',
        names='COMPLEXIDADE',
        title="Complexidades das Demandas",
        color='COMPLEXIDADE',
        color_discrete_map={
                    'N1': '#22155C', # troca cor barar 4 bara 5 e pizza
                    'N2': '#6458F0',
                    'N3': '#6DDCF4'
        }
    )
    pizza.update_layout(title_x=0.5)

    barra1 = px.bar(
        df_barra1,
        x="SENIORIDADE",
        y="CONSULTORES",
        color="SENIORIDADE",
        color_discrete_map={
                    'Estagiário': '#6DDCF4',
                    'Junior': '#699AF2',
                    'Pleno': '#7C3C95',
                    'Senior': '#22155C',
                    'Expert': '#000024',
        },
        title="Consultores Ociosos por Senioridade",
        text_auto=True
    )
    barra1.update_layout(title_x=0.5)

    barra2 = px.histogram(
        df_barra2,
        x="TIPO",
        y="% ATENDIMENTOS",
        color="SENIORIDADE",
        color_discrete_map={
                    'Estagiário': '#6DDCF4',
                    'Junior': '#699AF2',
                    'Pleno': '#7C3C95',
                    'Senior': '#22155C',
                    'Expert': '#000024',
        },
        title="Contrato x Demanda",
        #text_auto=True
    )
    barra2.update_layout(title_x=0.5)

    barra3 = px.bar(
        df_barra3,
        x="TIPO",
        y="VALOR",
        color="TIPO",
        color_discrete_map={
                    'Custo Atendimento': '#a80000',
                    'Valor do Contrato': '#59EE6A'
        },
        title="Custo x Valor do Contrato em R$"
    )
    barra3.update_layout(title_x=0.5)

    barra4 = px.bar(
        df_barra4,
        x="SENIORIDADE",
        y="ATENDIMENTOS",
        color="COMPLEXIDADE",
        color_discrete_map={
                        'N1': '#22155C',
                        'N2': '#6458F0',
                        'N3': '#6DDCF4'
        },
        title="Consultores x Complexidade de Atendimentos"
        #text_auto=True
    )
    barra4.update_layout(title_x=0.5)

    barra5 = px.bar(
        df_barra5,
        x="DATA",
        y="ATENDIMENTOS",
        color="COMPLEXIDADE",
        color_discrete_map={
                        'N1': '#22155C',
                        'N2': '#6458F0',
                        'N3': '#6DDCF4'
        },
        title="Atendimentos ao Longo do Tempo"
    )
    barra5.update_layout(title_x=0.5)

    linha = px.line(
        df_linha,
        x="DATA",
        y="CUSTO",
        title="Custo ao Longo do Tempo",
    )
    linha.update_layout(title_x=0.5)
    linha.update_traces(line_color='#a80000')

    linha2 = px.line(
        df_linha2,
        x="DATA",
        y="CUSTO",
        title="Projeção do Custo de Abril",
    )
    linha2.update_layout(title_x=0.5)
    linha2.update_traces(line_color='#AB9EAA')

    # Criação das Divs de cada Gráfico
    div_pizza = html.Div([dcc.Graph(id='pizza', figure=pizza)])
    div_barra1 = html.Div([dcc.Graph(id='barra1', figure=barra1)])
    div_barra2 = html.Div([dcc.Graph(id='barra2', figure=barra2)])
    div_barra3 = html.Div([dcc.Graph(id='barra3', figure=barra3)])
    div_barra4 = html.Div([dcc.Graph(id='barra4', figure=barra4)])
    div_barra5 = html.Div([dcc.Graph(id='barra5', figure=barra5)])
    div_linha = html.Div([dcc.Graph(id='linha', figure=linha)])
    div_linha2 = html.Div([dcc.Graph(id='linha2', figure=linha2)])

    # Criação do Filtro
    dfFiltro = pd.read_csv("./dados/Lista Projetos.csv")
    opcoesFiltro = list(dfFiltro['Projetos'].unique())
    opcoesFiltro.append("Todos")


    # Criação da Barra de Navegação
    nav =  dbc.Nav( 
        [
             dbc.NavItem(dbc.NavLink("Perfil", active=True, href="/perfil/", external_link=True,style={
                            "display": "flex",
                            "justify-content": "center",  
                            "align-self": "center", 
                            "font-weight": "bold",  
                            "font-size": "16px" , 
                            "color":"#6458F0"
                        })),
             dbc.NavItem(dbc.NavLink("Sair", active=True, href="/", external_link=True, style={
                            "display": "flex",
                            "justify-content": "center",  
                            "align-self": "center", 
                            "font-weight": "bold",  
                            "font-size": "16px" , 
                            "color": "#6458F0"
                        })),
        ], 
        className="justify-content-end", 
        style={'border-color':'#0B2D4B','background-color': 'white', 'font-size': '14px', 'color':'#0B2D4B'}
        #box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    )


    # INICIO LAYOUT
    dash_app.layout = html.Div(children=[
        
        html.Div(
            nav
        ),
        
        html.Img(src=r'assets/logo-no-background.svg', style={'width': '200px', 'display': 'block', 'margin': 'auto', 'margin-top': '50px','margin-bottom': '80px' }, alt='image'),
        

        dbc.Container([
            dbc.Row([
                dbc.CardGroup([
                    dbc.Label("Filtro de Projetos"),
                    dbc.Select(opcoesFiltro, value='Todos',id='filtro-dropdown')
                ],class_name="mb-4 col-md-3 justify-content-center")
            ],class_name="justify-content-center"),
            # Add the button to trigger an action
            dbc.Row(
                dbc.Col(
                    dbc.Button(
                        [
                            "Consulte a S.O.P.H.I.A.! "
                        ],
                        id="my-button",
                        style={'background-color': '#6458F0'},  # Custom background color
                        className="btn btn-secondary"
                    ),
                    width={"size": 6, "offset": 3},  # Size and offset for horizontal centering
                    className="text-center"
                ),
                className="mb-4"  # Add some margin at the bottom
            ),
            #ALERT CONSULTA SOPHIA
            dcc.Loading(id="loading-1", style={'margin':'20px', 'display':'block'}, color="#6458F0", type="circle", children=[
                html.Div(id="output-div", style={'display':'none'}, 
                    children=[
                        dbc.Alert(
                            "This is a light alert",
                            color="light",
                            id="alert-fade",
                            dismissable=True,
                            is_open=True,
                            duration=300000,
                        ),
                    ]
                )]
            ),
            dbc.Row([
                dbc.Col([div_pizza], md=4),
                dbc.Col([div_barra4], md=8) #troca cor
            ]),
            dbc.Row([
                dbc.Col([div_barra5]) #troca cor
            ]),
            dbc.Row([
                dbc.Col([div_barra1])
            ]),
            dbc.Row([
                dbc.Col([div_barra2], md=6),
                dbc.Col([div_barra3], md=6)
            ]),
            dbc.Row([
                dbc.Col([div_linha])
            ]),
            dbc.Row([
                dbc.Col([div_linha2])
            ])
        ])
    ]
    )

    ###################################### work in progress

    def register_callbacks(app):
        @app.callback(
            [Output('pizza', 'figure'),
            Output('barra4', 'figure'),
            Output('linha', 'figure'),
            Output('barra2', 'figure'),
            Output('barra5', 'figure'),
            Output('barra3', 'figure')],
            [Input('filtro-dropdown', 'value')]
        )

        def update_output(value):
        # Your existing update logic for the graphs
            if value == "Todos":
                    pizza = px.pie(
                                df_pizza,
                                values='ATENDIMENTOS',
                                names='COMPLEXIDADE',
                                title="Complexidades das Demandas",
                                color='COMPLEXIDADE',
                                color_discrete_map={
                                            'N1': '#22155C', # troca cor
                                            'N2': '#6458F0',
                                            'N3': '#6DDCF4'
                                }
                            )
                    pizza.update_layout(title_x=0.5)
                
                    barra4 = px.bar(
                                df_barra4,
                                x="SENIORIDADE",
                                y="ATENDIMENTOS",
                                color="COMPLEXIDADE",
                                color_discrete_map={
                                                'N1': '#22155C',
                                                'N2': '#6458F0',
                                                'N3': '#6DDCF4'
                                },
                                title="Consultores x Complexidade de Atendimentos"
                                #text_auto=True
                            )
                    barra4.update_layout(title_x=0.5)
                
                    barra5 = px.bar(
                                df_barra5,
                                x="DATA",
                                y="ATENDIMENTOS",
                                color="COMPLEXIDADE",
                                color_discrete_map={
                                                'N1': '#22155C',
                                                'N2': '#6458F0',
                                                'N3': '#6DDCF4'
                                },
                                title="Atendimentos ao Longo do Tempo"
                            )
                    barra5.update_layout(title_x=0.5)
                
                    barra2 = px.histogram(
                                df_barra2,
                                x="TIPO",
                                y="% ATENDIMENTOS",
                                color="SENIORIDADE",
                                color_discrete_map={
                                            'Estagiário': '#6DDCF4',
                                            'Junior': '#699AF2',
                                            'Pleno': '#7C3C95',
                                            'Senior': '#22155C',
                                            'Expert': '#000024',
                                },
                                title="Contrato x Demanda",
                                #text_auto=True
                            )
                    barra2.update_layout(title_x=0.5)


                    barra3 = px.bar(
                            df_barra3,
                            x="TIPO",
                            y="VALOR",
                            color="TIPO",
                            color_discrete_map={'Custo Atendimento': '#a80000','Valor do Contrato': '#59EE6A'},
                            title="Custo x Valor do Contrato em R$"
                        )
                    barra3.update_layout(title_x=0.5)


                    linha = px.line(
                                df_linha,
                                x="DATA",
                                y="CUSTO",
                                title="Custo ao Longo do Tempo",
                            )
                    linha.update_layout(title_x=0.5)
                    linha.update_traces(line_color='#a80000')
                
            else:
                    df_pizza_filtrada = df_pizza.loc[df_pizza['PROJETOS'] == value,:]
                    pizza = px.pie(
                        df_pizza_filtrada,
                        values='ATENDIMENTOS',
                        names='COMPLEXIDADE',
                        title="Complexidades das Demandas",
                        color='COMPLEXIDADE',
                        color_discrete_map={
                                    'N1': '#22155C', # troca cor
                                    'N2': '#6458F0',
                                    'N3': '#6DDCF4'
                        }
                    )
                    pizza.update_layout(title_x=0.5)
                
                    df_barra4_filtrada = df_barra4.loc[df_barra4['PROJETOS'] == value,:]
                    barra4 = px.bar(
                                df_barra4_filtrada,
                                x="SENIORIDADE",
                                y="ATENDIMENTOS",
                                color="COMPLEXIDADE",
                                color_discrete_map={
                                                'N1': '#22155C',
                                                'N2': '#6458F0',
                                                'N3': '#6DDCF4'
                                },
                                title="Consultores x Complexidade de Atendimentos"
                                #text_auto=True
                            )
                    barra4.update_layout(title_x=0.5)
                
                    df_barra5_filtrada = df_barra5.loc[df_barra5['PROJETOS'] == value,:]
                    barra5 = px.bar(
                                df_barra5_filtrada,
                                x="DATA",
                                y="ATENDIMENTOS",
                                color="COMPLEXIDADE",
                                color_discrete_map={
                                                'N1': '#22155C',
                                                'N2': '#6458F0',
                                                'N3': '#6DDCF4'
                                },
                                title="Atendimentos ao Longo do Tempo"
                            )
                    barra5.update_layout(title_x=0.5)
                
                    df_barra2_filtrada = df_barra2.loc[df_barra2['PROJETOS'] == value,:]
                    barra2 = px.histogram(
                                df_barra2_filtrada,
                                x="TIPO",
                                y="% ATENDIMENTOS",
                                color="SENIORIDADE",
                                color_discrete_map={
                                            'Estagiário': '#6DDCF4',
                                            'Junior': '#699AF2',
                                            'Pleno': '#7C3C95',
                                            'Senior': '#22155C',
                                            'Expert': '#000024',
                                },
                                title="Contrato x Demanda",
                                #text_auto=True
                            )
                    barra2.update_layout(title_x=0.5)


                    df_barra3_filtrada = df_barra3.loc[df_barra3['PROJETOS'] == value,:]
                    barra3 = px.bar(
                            df_barra3_filtrada,
                            x="TIPO",
                            y="VALOR",
                            color="TIPO",
                            color_discrete_map={'Custo Atendimento': '#a80000','Valor do Contrato': '#59EE6A'},
                            title="Custo x Valor do Contrato em R$"
                        )
                    barra3.update_layout(title_x=0.5)


                    df_linha_filtrada = df_linha.loc[df_linha['PROJETOS'] == value,:]
                    linha = px.line(
                                df_linha_filtrada,
                                x="DATA",
                                y="CUSTO",
                                title="Custo ao Longo do Tempo",
                            )
                    linha.update_layout(title_x=0.5)
                    linha.update_traces(line_color='#a80000')


            return pizza, barra4, linha, barra2, barra5, barra3
            # pass

        @app.callback(
            [Output('output-div', 'style'), 
            Output('alert-fade', 'children'),
            Output('alert-fade', 'is_open')],
            [Input('my-button', 'n_clicks')]
        )

        def on_button_click(n_clicks):
            phrases = [
                "A análise da base de dados do Projeto1-Basis indica que a equipe foi corretamente dimensionada para o projeto, com a maioria dos atendimentos realizados por consultores estagiários ou juniores. A complexidade dos atendimentos ficou majoritariamente em Nível 1 (89%), enquanto apenas 11% foram de Nível 2. Atendimentos de Nível 1 ocorreram ao longo de todo o período, e os de Nível 2 foram esporádicos a partir do segundo mês.",
                "A análise da base de dados do Projeto1-Funcional revela que a equipe foi dimensionada incorretamente, com uma maior necessidade de Consultores Seniors e menor uso de consultores Plenos do que o esperado. A complexidade dos atendimentos foi dividida entre Nível 1 (46%), Nível 2 (24%) e Nível 3 (30%). Atendimentos de Nível 1 e 3 ocorreram durante todo o período, enquanto os de Nível 2 ganharam relevância a partir do segundo mês.",
                "A análise da base de dados do Projeto2-Funcional indica que a equipe foi dimensionada de forma incorreta, com maior necessidade de Consultores Seniors e menor uso de consultores Plenos do que o previsto. A complexidade dos atendimentos foi distribuída entre Nível 1 (60%) e Nível 3 (40%). Ambos os níveis de atendimento ocorreram durante todo o período, mas sua frequência diminuiu ao longo do tempo."
            ]
            random_phrase = random.choice(phrases)

            if n_clicks:
                # change visibility of the spinner to true
                time.sleep(1.5)
                # change visibility of the spinner to false
                return {'display': 'block'}, random_phrase, True
            else:
                return {'display': 'none'}, "", False

        # @app.callback(
        #     Output("alert-fade", "is_open"),
        #     [Input("my-button", "n_clicks")],
        #     [State("alert-fade", "is_open")],
        #     )
        
        # def toggle_alert(n, is_open):
        #     if n:
        #         return not is_open
        #     return is_open

    register_callbacks(dash_app)
    return dash_app.server