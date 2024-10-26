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
    df_linha = pd.read_csv("./dados/Custo ao Longo do Tempo com projecao.csv")
    df_linha2 = pd.read_csv("./dados/ProjecaoAbril.csv")
    df_barra6 = pd.read_csv("./dados/Atendimento x Senioridade.csv")
    df_barra7 = pd.read_csv("./dados/Atendimento_x_Senioridade_PREVISAO.csv")
    df_barra8 = pd.read_csv("./dados/Equipe por projeto.csv")

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
        title="Senioridade de Consultores Ociosos nos últimos 3 meses",
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
        title="Contratado x Atendimentos",
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
        title="Custo dos Atendimentos x Valor do Contrato em R$"
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
        title="Senioridade dos Consultores x Complexidade dos Atendimentos"
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
        title="Complexidade dos Atendimentos ao Longo do Tempo"
    )
    barra5.update_layout(title_x=0.5)

    # linha = px.line(
    #     df_linha,
    #     x="DATA",
    #     y="CUSTO",
    #     title="Custo dos Atendimentos ao Longo do Tempo",
    # )
    # linha.update_layout(title_x=0.5)
    # linha.update_traces(line_color='#a80000')

    linha2 = px.line(
        df_linha2,
        x="DATA",
        y="CUSTO",
        title="Projeção do Custo dos Atendimentos de Abril",
    )
    linha2.update_layout(title_x=0.5)
    linha2.update_traces(line_color='#AB9EAA')

    linha = px.line(
        df_linha,
        x="DATA",
        y="CUSTO",
        title="Custo ao Longo do Tempo",
        color="TIPO"
    )
    linha.update_layout(title_x=0.5)

    #Grafico de Atendimentos por senioridade ao longo do tempo + previsao
    barra6 = px.bar(
        df_barra6,
        x="DATA",
        y="ATENDIMENTOS",
        color="SENIORIDADE",
        color_discrete_map={
                        'Estagiário': '#6DDCF4',
                        'Junior': '#699AF2',
                        'Pleno': '#7C3C95',
                        'Senior': '#22155C',
                        'Expert': '#000024'
        },
        title="Atendimentos por Senioridade"
    )
    barra6.update_layout(title_x=0.5)

    barra7 = px.bar(
        df_barra7,
        x="DATA",
        y="ATENDIMENTOS",
        color="SENIORIDADE",
        color_discrete_map={
                        'Estagiário': '#6DDCF4',
                        'Junior': '#699AF2',
                        'Pleno': '#7C3C95',
                        'Senior': '#22155C',
                        'Expert': '#000024'
        },
        title="Projeção dos Atendimentos por Senioridade nos Próximos 3 Meses"
    )
    barra7.update_layout(title_x=0.5)

    barra8 = px.bar(
        df_barra8,
        x="PROJETOS",
        y="EQUIPE",
        color="SENIORIDADE",
        color_discrete_map={
                        'Estagiário': '#6DDCF4',
                        'Junior': '#699AF2',
                        'Pleno': '#7C3C95',
                        'Senior': '#22155C',
                        'Expert': '#000024'
        },
        title="Equipe por Projeto"
        #text_auto=True
    )
    barra8.update_layout(title_x=0.5)

    # Criação das Divs de cada Gráfico
    div_pizza = html.Div([dcc.Graph(id='pizza', figure=pizza)])
    div_barra1 = html.Div([dcc.Graph(id='barra1', figure=barra1)])
    div_barra2 = html.Div([dcc.Graph(id='barra2', figure=barra2)])
    div_barra3 = html.Div([dcc.Graph(id='barra3', figure=barra3)])
    div_barra4 = html.Div([dcc.Graph(id='barra4', figure=barra4)])
    div_barra5 = html.Div([dcc.Graph(id='barra5', figure=barra5)])
    div_linha = html.Div([dcc.Graph(id='linha', figure=linha)])
    div_linha2 = html.Div([dcc.Graph(id='linha2', figure=linha2)])
    div_barra6 = html.Div([dcc.Graph(id='barra6', figure=barra6)])
    div_barra7 = html.Div([dcc.Graph(id='barra7', figure=barra7)])
    div_barra8 = html.Div([dcc.Graph(id='barra8', figure=barra8)])

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
                dbc.Col(html.Button(html.Img(src=r'assets/icons8-mais-60.png', 
                                 style={'width': '20px', 'margin-left':'-20px'}, 
                                 alt='image'), id="icon-1", style={'border':'none', 'background-color':'white'}), md=1, style={'flex-grow': '0', 'max-width': '20px'}),
                dbc.Popover(
                            "Nesse gráfico de pizza baseado nos atendimentos dos meses de Janeiro a Março de 2024, observa-se que a maioria dos atendimentos está concentrada em tarefas de menor complexidade (N1), com destaque para o Projeto2-Funcional (230 atendimentos) e Projeto1-Basis (225 atendimentos). No entanto, em termos de maior complexidade (N3), o Projeto2-Funcional também lidera, com 156 atendimentos, enquanto o Projeto1-Funcional soma 112 atendimentos nessa categoria.",
                            target="icon-1",
                            body=True,
                            trigger="legacy",
                ),
                dbc.Col([div_barra4], md=7),
                dbc.Col(html.Button(html.Img(src=r'assets/icons8-mais-60.png', 
                                 style={'width': '20px'}, 
                                 alt='image'), id="icon-2", style={'border':'none', 'background-color':'white'}), md=1, style={'flex-grow': '0', 'max-width': '20px'}),
                dbc.Popover(
                            "Nesse gráfico de barras baseado nos atendimentos dos meses de Janeiro a Março de 2024, observa-se que Juniores e Estagiários são responsáveis pela maioria dos atendimentos de complexidade baixa (N1), especialmente no Projeto1-Basis e Projeto2-Funcional. No entanto, Seniores e Experts ganham destaque em tarefas mais complexas (N3), com o Projeto2-Funcional apresentando a maior carga de atendimentos N3, somando 91 atendimentos com profissionais senior e 18 com experts.",
                            target="icon-2",
                            body=True,
                            trigger="legacy",
                ),
            ]),
            dbc.Row([
                dbc.Col([div_barra5]),
                dbc.Col(html.Button(html.Img(src=r'assets/icons8-mais-60.png', 
                                 style={'width': '20px'}, 
                                 alt='image'), id="icon-3", style={'border':'none', 'background-color':'white'}), md=1, style={'flex-grow': '0', 'max-width': '20px'}),
                dbc.Popover(
                            "Os projetos Projeto1-Basis e Projeto1-Funcional têm atendimentos constantes de complexidade N1, com picos no início e fim de janeiro e fevereiro. O Projeto2-Funcional também apresenta uma frequência alta de atendimentos N1 no mesmo período. Atendimentos com complexidade N2 são mais frequentes nos últimos dias de fevereiro e início de março, dispersos em várias datas.",
                            target="icon-3",
                            body=True,
                            trigger="legacy",
                ),
            ]),
            dbc.Row([
                dbc.Col([div_barra1]),
                dbc.Col(html.Button(html.Img(src=r'assets/icons8-mais-60.png', 
                                 style={'width': '20px'}, 
                                 alt='image'), id="icon-4", style={'border':'none', 'background-color':'white'}), md=1, style={'flex-grow': '0', 'max-width': '20px'}),
                dbc.Popover(
                            "Nos meses de Janeiro a Março, o número de consultores ociosos representou um total de 24 profissionais distribuídos entre diferentes níveis de senioridade. A maior parte dos profissionais sem demandas alocadas concentrou-se na categoria sênior, representando mais da metade do total. Os níveis júnior e pleno seguiram em números mais equilibrados, enquanto estagiários e experts formaram as menores categorias.",
                            target="icon-4",
                            body=True,
                            trigger="legacy",
                ),
            ]),
            dbc.Row([
                dbc.Col([div_barra2], md=5),
                dbc.Col(html.Button(html.Img(src=r'assets/icons8-mais-60.png', 
                                 style={'width': '20px', 'margin-left':'-20px'}, 
                                 alt='image'), id="icon-9", style={'border':'none', 'background-color':'white'}), md=1, style={'flex-grow': '0', 'max-width': '20px'}),
                dbc.Popover(
                            "O gráfico Contratado x Atendimentos revela discrepâncias significativas na senioridade dos consultores contratados em relação aos que realmente atuaram nas demandas de cada projeto no período de Janeiro a Março de 2024. Por exemplo, no Projeto 1-Funcional, enquanto 40% dos consultores contratados eram Plenos, apenas 23,26% deles atuaram nas demandas. Da mesma forma, no Projeto 2-Funcional, 50% dos contratados eram Plenos, mas apenas 22,8% estavam presentes nas demandas. Essas diferenças indicam uma subutilização das competências mais avançadas nos projetos, sugerindo uma necessidade de reavaliação no processo de alocação de consultores.",
                            target="icon-9",
                            body=True,
                            trigger="legacy",
                ),
                dbc.Col([div_barra3], md=5),
                dbc.Col(html.Button(html.Img(src=r'assets/icons8-mais-60.png', 
                                 style={'width': '20px'}, 
                                 alt='image'), id="icon-10", style={'border':'none', 'background-color':'white'}), md=1, style={'flex-grow': '0', 'max-width': '20px'}),
                dbc.Popover(
                            "Nos meses de Janeiro a Março de 2024, observa-se uma discrepância significativa entre os custos de atendimento e os valores dos contratos em cada projeto. Por exemplo, no Projeto 1-Funcional, o custo de atendimento é de 71.703, enquanto o valor do contrato é de 50.400, resultando em uma diferença negativa de 21.303. Essa situação indica que os custos superam o valor acordado, sugerindo a necessidade de ajustes nos orçamentos e na gestão dos recursos. Além disso, no Projeto 2-Funcional, o custo de atendimento é de 53.782, contra um valor de contrato de 58.800, evidenciando uma margem de lucro mais saudável, mas que ainda requer uma análise detalhada para otimização.",
                            target="icon-10",
                            body=True,
                            trigger="legacy",
                ),
            ]),
            dbc.Row([
                dbc.Col([div_linha]),
                dbc.Col(html.Button(html.Img(src=r'assets/icons8-mais-60.png', 
                                 style={'width': '20px'}, 
                                 alt='image'), id="icon-5", style={'border':'none', 'background-color':'white'}), md=1, style={'flex-grow': '0', 'max-width': '20px'}),
                dbc.Popover(
                            "O gráfico Custos ao Longo do Tempo revela variações significativas nos gastos. No Projeto 1-Funcional, os custos aumentaram de 1.330 a 2.275 durante o mês de janeiro a março, evidenciando um crescimento contínuo. Por outro lado, o Projeto 1-Basis apresenta custos mais baixos, com flutuações que vão de 6 a 242, indicando um padrão de gastos menos consistente. O Projeto 2-Funcional, por sua vez, também apresenta custos crescentes, atingindo 2.208, o que sugere um aumento na demanda ou complexidade dos serviços prestados ao longo do período analisado.",
                            target="icon-5",
                            body=True,
                            trigger="legacy",
                ),
            ]),
            dbc.Row([
                dbc.Col([div_linha2]),
                dbc.Col(html.Button(html.Img(src=r'assets/icons8-mais-60.png', 
                                 style={'width': '20px'}, 
                                 alt='image'), id="icon-6", style={'border':'none', 'background-color':'white'}), md=1, style={'flex-grow': '0', 'max-width': '20px'}),
                dbc.Popover(
                            "A predição dos dados de custos de Abril de 2024 indica uma variação significativa entre as horas e valores gastos por consultor. Os valores totais de R$ 10.417,90, R$ 5.691,80 e R$ 9.119,00, com respectivos custos por hora de R$ 71,69, R$ 92,01 e R$ 73,25, refletem uma distribuição desigual de recursos. Isso sugere que a alocação de consultores pode impactar a eficiência dos projetos, exigindo uma revisão estratégica para otimizar a utilização de recursos e reduzir despesas. A discrepância nos custos por hora também pode refletir diferenças na senioridade e experiência dos consultores alocados.",
                            target="icon-6",
                            body=True,
                            trigger="legacy",
                ),
            ]),
            dbc.Row([
                dbc.Col([div_barra6]),
                dbc.Col(html.Button(html.Img(src=r'assets/icons8-mais-60.png', 
                                 style={'width': '20px'}, 
                                 alt='image'), id="icon-7", style={'border':'none', 'background-color':'white'}), md=1, style={'flex-grow': '0', 'max-width': '20px'}),
                dbc.Popover(
                            "A análise dos atendimentos realizados por diferentes níveis de senioridade entre janeiro e abril de 2024 destaca uma distribuição desigual na alocação de recursos. Os estagiários apresentaram o maior número de atendimentos, com um pico de 15 atendimentos em um único dia, refletindo uma dependência significativa de profissionais menos experientes em projetos funcionais. Por outro lado, os consultores seniores, embora menos frequentemente alocados, participaram ativamente em projetos-chave, o que sugere a necessidade de um equilíbrio na distribuição de tarefas para maximizar a eficiência e a qualidade do trabalho. Essa dinâmica entre as senioridades pode impactar a entrega dos projetos, evidenciando a importância de uma gestão estratégica de recursos humanos.",
                            target="icon-7",
                            body=True,
                            trigger="legacy",
                ),
            ]),
            dbc.Row([
                dbc.Col([div_barra7]),
                dbc.Col(html.Button(html.Img(src=r'assets/icons8-mais-60.png', 
                                 style={'width': '20px'}, 
                                 alt='image'), id="icon-8", style={'border':'none', 'background-color':'white'}), md=1, style={'flex-grow': '0', 'max-width': '20px'}),
                dbc.Popover(
                            "A análise dos dados de atendimentos por senioridade nos projetos prediz uma dependência significativa de Estagiários e Juniores, que em várias datas superarão os atendimentos dos profissionais mais experientes. Em particular, o volume de atendimentos dos estagiários nos projetos se destaca, especialmente em datas como 4 de abril e 2 de junho, onde poderão atingir números elevados. Apesar de Seniores e Plenos realizarem um número considerável de atendimentos, sua atuação pode ser menos frequente, sugerindo que os projetos podem estar se apoiando em uma força de trabalho menos experiente. Essa tendência pode levantar questões sobre a necessidade de um equilíbrio mais adequado entre as diferentes senioridades para garantir a qualidade e a eficiência nas entregas.",
                            target="icon-8",
                            body=True,
                            trigger="legacy",
                ),
            ]),
            dbc.Row([
                dbc.Col([div_barra8]),
                dbc.Col(html.Button(html.Img(src=r'assets/icons8-mais-60.png', 
                                 style={'width': '20px'}, 
                                 alt='image'), id="icon-11", style={'border':'none', 'background-color':'white'}), md=1, style={'flex-grow': '0', 'max-width': '20px'}),
                dbc.Popover(
                            "Analise SOPHIA",
                            target="icon-11",
                            body=True,
                            trigger="legacy",
                ),
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
            Output('barra3', 'figure'),
            Output('barra6', 'figure'),
            Output('barra7', 'figure'),
            Output('barra8','figure')],
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
                                title="Senioridade dos Consultores x Complexidade dos Atendimentos"
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
                                title="Complexidade dos Atendimentos ao Longo do Tempo"
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
                                title="Contratado x Atendimentos",
                                #text_auto=True
                            )
                    barra2.update_layout(title_x=0.5)


                    barra3 = px.bar(
                            df_barra3,
                            x="TIPO",
                            y="VALOR",
                            color="TIPO",
                            color_discrete_map={'Custo Atendimento': '#a80000','Valor do Contrato': '#59EE6A'},
                            title="Custo dos Atendimentos x Valor do Contrato em R$"
                        )
                    barra3.update_layout(title_x=0.5)


                    linha = px.line(
                        df_linha,
                        x="DATA",
                        y="CUSTO",
                        title="Custo ao Longo do Tempo",
                        color="TIPO"
                    )
                    linha.update_layout(title_x=0.5)

                    barra6 = px.bar(
                        df_barra6,
                        x="DATA",
                        y="ATENDIMENTOS",
                        color="SENIORIDADE",
                        color_discrete_map={
                                        'Estagiário': '#6DDCF4',
                                        'Junior': '#699AF2',
                                        'Pleno': '#7C3C95',
                                        'Senior': '#22155C',
                                        'Expert': '#000024'
                                    },
                        title="Atendimentos por Senioridade"
                            )
                    barra6.update_layout(title_x=0.5)

                    barra7 = px.bar(
                        df_barra7,
                        x="DATA",
                        y="ATENDIMENTOS",
                        color="SENIORIDADE",
                        color_discrete_map={
                                        'Estagiário': '#6DDCF4',
                                        'Junior': '#699AF2',
                                        'Pleno': '#7C3C95',
                                        'Senior': '#22155C',
                                        'Expert': '#000024'
                                    },
                        title="Projeção dos Atendimentos por Senioridade nos Próximos 3 Meses"
                            )
                    barra7.update_layout(title_x=0.5)

                    # barra8 = px.bar(
                    #     df_barra8,
                    #     x="PROJETOS",
                    #     y="CONSULTOR",
                    #     color="Senioridade",
                    #     color_discrete_map={
                    #                     'Estagiário': '#6DDCF4',
                    #                     'Junior': '#699AF2',
                    #                     'Pleno': '#7C3C95',
                    #                     'Senior': '#22155C',
                    #                     'Expert': '#000024'
                    #                 },
                    #     title="Consultores por Projeto"
                    # )
                    # barra8.update_layout(title_x=0.5)
                
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
                                title="Senioridade dos Consultores x Complexidade dos Atendimentos"
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
                                title="Complexidade dos Atendimentos ao Longo do Tempo"
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
                                title="Contratado x Atendimentos",
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
                            title="Custo dos Atendimentos x Valor do Contrato em R$"
                        )
                    barra3.update_layout(title_x=0.5)


                    df_linha_filtrada = df_linha.loc[df_linha['PROJETOS'] == value,:]
                    linha = px.line(
                        df_linha_filtrada,
                        x="DATA",
                        y="CUSTO",
                        title="Custo ao Longo do Tempo",
                        color="TIPO"
                    )
                    linha.update_layout(title_x=0.5)

                    df_barra6_filtrada = df_barra6.loc[df_barra6['PROJETOS'] == value,:]
                    barra6 = px.bar(
                            df_barra6_filtrada,
                            x="DATA",
                            y="ATENDIMENTOS",
                            color="SENIORIDADE",
                            color_discrete_map={
                                'Estagiário': '#6DDCF4',
                                'Junior': '#699AF2',
                                'Pleno': '#7C3C95',
                                'Senior': '#22155C',
                                'Expert': '#000024'
                            },
                            title="Atendimentos por Senioridade"
                        )
                    barra6.update_layout(title_x=0.5)

                    df_barra7_filtrada = df_barra7.loc[df_barra7['PROJETOS'] == value,:]
                    barra7 = px.bar(
                            df_barra7_filtrada,
                            x="DATA",
                            y="ATENDIMENTOS",
                            color="SENIORIDADE",
                            color_discrete_map={
                                'Estagiário': '#6DDCF4',
                                'Junior': '#699AF2',
                                'Pleno': '#7C3C95',
                                'Senior': '#22155C',
                                'Expert': '#000024'
                            },
                            title="Projeção dos Atendimentos por Senioridade nos Próximos 3 Meses"
                        )
                    barra7.update_layout(title_x=0.5)

                    # df_barra8_filtrada = df_barra8.loc[df_barra8['PROJETOS'] == value,:]
                    # barra8 = px.bar(
                    #         df_barra8_filtrada,
                    #         x="PROJETOS",
                    #         y="CONSULTOR",
                    #         color="SENIORIDADE",
                    #         color_discrete_map={
                    #             'Estagiário': '#6DDCF4',
                    #             'Junior': '#699AF2',
                    #             'Pleno': '#7C3C95',
                    #             'Senior': '#22155C',
                    #             'Expert': '#000024'
                    #         },
                    #         title="Projeção dos Atendimentos por Senioridade nos Próximos 3 Meses"
                    #     )
                    # barra8.update_layout(title_x=0.5)


            return pizza, barra4, linha, barra2, barra5, barra3, barra6, barra7, barra8
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
        #      [Output('details-1', 'style'),
        #      Output('alert-fade-dupe','children'),
        #      Output('alert-fade-dupe', 'is_open')],
        #      Input('icon-1', 'n_clicks')
        # )

        # def icon(n_clicks):
        #     if n_clicks:
        #         return {'display':'block'}, "Hi", True
        #     else:
        #          return {'display': 'none'}, "", False

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