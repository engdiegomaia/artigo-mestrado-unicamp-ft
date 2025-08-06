#!/usr/bin/env python3
"""
Script para gerar Gantt Chart do cronograma do projeto de mestrado.
Gera um arquivo HTML com visualização interativa do cronograma e uma imagem PNG.

Autor: Diego Maia
Data: 2025-08-05
Versão: 2.2 - Imagem PNG no novo caminho com fontes maiores
"""

import datetime
from datetime import timedelta
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patches import Rectangle
import numpy as np


def create_gantt_data():
    """
    Cria os dados do Gantt Chart baseado no cronograma detalhado do projeto.
    
    Returns:
        dict: Dados estruturados para o Gantt Chart
    """
    
    # Data de início: Hoje (2025-08-05)
    start_date = datetime.date(2025, 8, 5)
    
    # Data de defesa: Setembro 2026
    defense_date = datetime.date(2026, 9, 30)
    
    # Estrutura das tarefas detalhadas
    tasks = [
        # ===== ETAPA 1: FUNDAMENTAÇÃO TEÓRICA (Agosto 2025 - Janeiro 2026) =====
        {
            "id": "etapa1",
            "name": "Etapa 1: Fundamentação Teórica e Estado da Arte",
            "start": start_date.strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(days=150)).strftime("%Y-%m-%d"),  # 5 meses
            "progress": 25,
            "dependencies": "",
            "color": "#4CAF50"
        },
        {
            "id": "1.1",
            "name": "1.1 Revisão Sistemática da Literatura",
            "start": start_date.strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(days=45)).strftime("%Y-%m-%d"),  # 1.5 meses
            "progress": 80,
            "dependencies": "",
            "color": "#81C784"
        },
        {
            "id": "1.2",
            "name": "1.2 Análise de Técnicas de Otimização",
            "start": (start_date + timedelta(days=30)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(days=90)).strftime("%Y-%m-%d"),  # 2 meses
            "progress": 40,
            "dependencies": "1.1",
            "color": "#81C784"
        },
        {
            "id": "1.3",
            "name": "1.3 Caracterização de Sistemas Heterogêneos",
            "start": (start_date + timedelta(days=75)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(days=120)).strftime("%Y-%m-%d"),  # 1.5 meses
            "progress": 20,
            "dependencies": "1.2",
            "color": "#81C784"
        },
        {
            "id": "1.4",
            "name": "1.4 Framework Conceitual e Metodologia",
            "start": (start_date + timedelta(days=105)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(days=150)).strftime("%Y-%m-%d"),  # 1.5 meses
            "progress": 0,
            "dependencies": "1.3",
            "color": "#81C784"
        },
        
        # ===== ETAPA 2: DESENVOLVIMENTO EXPERIMENTAL (Janeiro - Maio 2026) =====
        {
            "id": "etapa2",
            "name": "Etapa 2: Desenvolvimento Experimental e Validação",
            "start": (start_date + timedelta(days=150)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(days=300)).strftime("%Y-%m-%d"),  # 5 meses
            "progress": 0,
            "dependencies": "1.4",
            "color": "#2196F3"
        },
        {
            "id": "2.1",
            "name": "2.1 Configuração do Ambiente Experimental",
            "start": (start_date + timedelta(days=150)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(days=180)).strftime("%Y-%m-%d"),  # 1 mês
            "progress": 0,
            "dependencies": "1.4",
            "color": "#64B5F6"
        },
        {
            "id": "2.2",
            "name": "2.2 Implementação de Protótipos",
            "start": (start_date + timedelta(days=165)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(days=240)).strftime("%Y-%m-%d"),  # 2.5 meses
            "progress": 0,
            "dependencies": "2.1",
            "color": "#64B5F6"
        },
        {
            "id": "2.3",
            "name": "2.3 Validação e Testes Experimentais",
            "start": (start_date + timedelta(days=225)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(days=300)).strftime("%Y-%m-%d"),  # 2.5 meses
            "progress": 0,
            "dependencies": "2.2",
            "color": "#64B5F6"
        },
        
        # ===== ETAPA 3: ANÁLISE E REDAÇÃO (Maio - Agosto 2026) =====
        {
            "id": "etapa3",
            "name": "Etapa 3: Análise de Resultados e Redação",
            "start": (start_date + timedelta(days=300)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(days=420)).strftime("%Y-%m-%d"),  # 4 meses
            "progress": 0,
            "dependencies": "2.3",
            "color": "#FF9800"
        },
        {
            "id": "3.1",
            "name": "3.1 Análise Estatística dos Resultados",
            "start": (start_date + timedelta(days=300)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(days=330)).strftime("%Y-%m-%d"),  # 1 mês
            "progress": 0,
            "dependencies": "2.3",
            "color": "#FFB74D"
        },
        {
            "id": "3.2",
            "name": "3.2 Redação dos Capítulos Principais",
            "start": (start_date + timedelta(days=315)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(days=390)).strftime("%Y-%m-%d"),  # 2.5 meses
            "progress": 0,
            "dependencies": "3.1",
            "color": "#FFB74D"
        },
        {
            "id": "3.3",
            "name": "3.3 Discussão e Conclusões",
            "start": (start_date + timedelta(days=375)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(days=420)).strftime("%Y-%m-%d"),  # 1.5 meses
            "progress": 0,
            "dependencies": "3.2",
            "color": "#FFB74D"
        },
        
        # ===== ETAPA 4: FINALIZAÇÃO E SUBMISSÃO (Agosto - Setembro 2026) =====
        {
            "id": "etapa4",
            "name": "Etapa 4: Finalização e Preparação para Defesa",
            "start": (start_date + timedelta(days=420)).strftime("%Y-%m-%d"),
            "end": defense_date.strftime("%Y-%m-%d"),  # 1.5 meses
            "progress": 0,
            "dependencies": "3.3",
            "color": "#E91E63"
        },
        {
            "id": "4.1",
            "name": "4.1 Revisão e Ajustes Finais",
            "start": (start_date + timedelta(days=420)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(days=450)).strftime("%Y-%m-%d"),  # 1 mês
            "progress": 0,
            "dependencies": "3.3",
            "color": "#F06292"
        },
        {
            "id": "4.2",
            "name": "4.2 Preparação da Apresentação",
            "start": (start_date + timedelta(days=435)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(days=465)).strftime("%Y-%m-%d"),  # 1 mês
            "progress": 0,
            "dependencies": "4.1",
            "color": "#F06292"
        },
        {
            "id": "4.3",
            "name": "4.3 Simulação de Defesa e Ajustes",
            "start": (start_date + timedelta(days=450)).strftime("%Y-%m-%d"),
            "end": defense_date.strftime("%Y-%m-%d"),  # 1 mês
            "progress": 0,
            "dependencies": "4.2",
            "color": "#F06292"
        },
        
        # ===== MILESTONES PRINCIPAIS =====
        {
            "id": "milestones",
            "name": "Milestones Principais",
            "start": start_date.strftime("%Y-%m-%d"),
            "end": defense_date.strftime("%Y-%m-%d"),
            "progress": 0,
            "dependencies": "",
            "color": "#9C27B0"
        },
        {
            "id": "m1",
            "name": "M1: Framework Conceitual Completo",
            "start": (start_date + timedelta(days=150)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(days=150)).strftime("%Y-%m-%d"),
            "progress": 0,
            "dependencies": "1.4",
            "color": "#BA68C8"
        },
        {
            "id": "m2",
            "name": "M2: Protótipos Validados",
            "start": (start_date + timedelta(days=300)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(days=300)).strftime("%Y-%m-%d"),
            "progress": 0,
            "dependencies": "2.3",
            "color": "#BA68C8"
        },
        {
            "id": "m3",
            "name": "M3: Dissertação Completa",
            "start": (start_date + timedelta(days=420)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(days=420)).strftime("%Y-%m-%d"),
            "progress": 0,
            "dependencies": "3.3",
            "color": "#BA68C8"
        },
        {
            "id": "m4",
            "name": "M4: Defesa",
            "start": defense_date.strftime("%Y-%m-%d"),
            "end": defense_date.strftime("%Y-%m-%d"),
            "progress": 0,
            "dependencies": "4.3",
            "color": "#BA68C8"
        }
    ]
    
    return {
        "title": "Cronograma Detalhado - Dissertação de Mestrado (Agosto 2025 - Setembro 2026)",
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date": defense_date.strftime("%Y-%m-%d"),
        "tasks": tasks
    }


def generate_png_gantt(gantt_data):
    """
    Gera uma imagem PNG do Gantt Chart usando matplotlib.
    
    Args:
        gantt_data (dict): Dados do Gantt Chart
    """
    
    # Configurar o estilo do matplotlib
    plt.style.use('default')
    plt.rcParams['font.family'] = 'DejaVu Sans'
    plt.rcParams['font.size'] = 14  # Aumentado de 10 para 14
    
    # Criar figura e eixos
    fig, ax = plt.subplots(figsize=(16, 12))
    
    # Converter datas
    start_date = datetime.datetime.strptime(gantt_data['start_date'], '%Y-%m-%d')
    end_date = datetime.datetime.strptime(gantt_data['end_date'], '%Y-%m-%d')
    
    # Filtrar tarefas (excluir milestones e etapas principais)
    task_tasks = [task for task in gantt_data['tasks'] if task['id'].startswith(('1.', '2.', '3.', '4.'))]
    milestone_tasks = [task for task in gantt_data['tasks'] if task['id'].startswith('m')]
    
    # Preparar dados para o gráfico
    task_names = []
    task_starts = []
    task_durations = []
    task_colors = []
    
    for task in task_tasks:
        task_names.append(task['name'])
        start = datetime.datetime.strptime(task['start'], '%Y-%m-%d')
        end = datetime.datetime.strptime(task['end'], '%Y-%m-%d')
        duration = (end - start).days
        task_starts.append(start)
        task_durations.append(duration)
        task_colors.append(task['color'])
    
    # Criar barras horizontais
    y_positions = np.arange(len(task_names))
    
    for i, (start, duration, color) in enumerate(zip(task_starts, task_durations, task_colors)):
        ax.barh(y_positions[i], duration, left=start, height=0.6, 
                color=color, alpha=0.8, edgecolor='black', linewidth=0.5)
    
    # Adicionar milestones como pontos
    milestone_positions = []
    milestone_dates = []
    milestone_names = []
    
    for i, milestone in enumerate(milestone_tasks):
        milestone_date = datetime.datetime.strptime(milestone['start'], '%Y-%m-%d')
        milestone_positions.append(i)
        milestone_dates.append(milestone_date)
        milestone_names.append(milestone['name'])
    
    # Plotar milestones
    if milestone_tasks:
        ax.scatter(milestone_dates, [len(task_names) + i for i in range(len(milestone_tasks))], 
                  s=100, color='#9C27B0', marker='D', edgecolors='black', linewidth=1, zorder=5)
    
    # Configurar eixos
    ax.set_yticks(y_positions)
    ax.set_yticklabels(task_names, fontsize=12)  # Aumentado de 9 para 12
    
    # Configurar eixo X (datas)
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    ax.xaxis.set_minor_locator(mdates.MonthLocator())
    
    # Rotacionar labels do eixo X
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right', fontsize=11)  # Adicionado fontsize=11
    
    # Adicionar linha de tempo atual
    current_date = datetime.datetime.now()
    if start_date <= current_date <= end_date:
        ax.axvline(x=current_date, color='red', linestyle='--', linewidth=2, alpha=0.8, label='Hoje')
        ax.text(current_date, ax.get_ylim()[1], ' Hoje', 
                verticalalignment='top', fontsize=12, color='red', fontweight='bold')  # Aumentado de 10 para 12
    
    # Configurar limites dos eixos
    ax.set_xlim(start_date - timedelta(days=10), end_date + timedelta(days=10))
    ax.set_ylim(-0.5, len(task_names) + len(milestone_tasks) - 0.5)
    
    # Adicionar título
    ax.set_title('Cronograma Detalhado - Dissertação de Mestrado\nAgosto 2025 - Setembro 2026', 
                 fontsize=18, fontweight='bold', pad=20)  # Aumentado de 14 para 18
    
    # Adicionar legendas
    legend_elements = [
        plt.Rectangle((0,0),1,1, facecolor='#4CAF50', alpha=0.8, label='Etapa 1: Fundamentação Teórica'),
        plt.Rectangle((0,0),1,1, facecolor='#2196F3', alpha=0.8, label='Etapa 2: Desenvolvimento Experimental'),
        plt.Rectangle((0,0),1,1, facecolor='#FF9800', alpha=0.8, label='Etapa 3: Análise e Redação'),
        plt.Rectangle((0,0),1,1, facecolor='#E91E63', alpha=0.8, label='Etapa 4: Finalização'),
        plt.scatter([], [], s=100, color='#9C27B0', marker='D', edgecolors='black', label='Milestones')
    ]
    
    if start_date <= current_date <= end_date:
        legend_elements.append(plt.Line2D([0], [0], color='red', linestyle='--', linewidth=2, label='Data Atual'))
    
    ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1, 1), fontsize=11)  # Aumentado de 9 para 11
    
    # Adicionar grid
    ax.grid(True, alpha=0.3, axis='x')
    
    # Ajustar layout
    plt.tight_layout()
    
    return fig


def generate_html_gantt(gantt_data):
    """
    Gera arquivo HTML com Gantt Chart interativo.
    
    Args:
        gantt_data (dict): Dados do Gantt Chart
    """
    
    html_template = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cronograma Detalhado - Dissertação de Mestrado</title>
    <script src="https://cdn.jsdelivr.net/npm/d3@7"></script>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1600px;
            margin: 0 auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 30px;
        }
        .gantt-container {
            overflow-x: auto;
            margin-top: 20px;
        }
        .task-bar {
            fill: #4CAF50;
            stroke: #2E7D32;
            stroke-width: 1;
        }
        .task-bar:hover {
            opacity: 0.8;
        }
        .milestone {
            fill: #9C27B0;
            stroke: #7B1FA2;
            stroke-width: 2;
        }
        .task-label {
            font-size: 12px;
            fill: #333;
        }
        .axis text {
            font-size: 10px;
        }
        .axis path, .axis line {
            stroke: #ccc;
        }
        .legend {
            margin-top: 20px;
            padding: 15px;
            background: #f9f9f9;
            border-radius: 5px;
        }
        .legend-item {
            display: inline-block;
            margin-right: 20px;
            margin-bottom: 10px;
        }
        .legend-color {
            display: inline-block;
            width: 20px;
            height: 15px;
            margin-right: 8px;
            border-radius: 3px;
        }
        .progress-info {
            margin-top: 20px;
            padding: 15px;
            background: #e3f2fd;
            border-radius: 5px;
            border-left: 4px solid #2196F3;
        }
        .timeline-info {
            margin-top: 15px;
            padding: 10px;
            background: #f3e5f5;
            border-radius: 5px;
            border-left: 4px solid #9c27b0;
        }
        .current-phase {
            margin-top: 15px;
            padding: 10px;
            background: #e8f5e8;
            border-radius: 5px;
            border-left: 4px solid #4caf50;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Cronograma Detalhado - Dissertação de Mestrado</h1>
        <div class="progress-info">
            <h3>📊 Status Atual</h3>
            <p><strong>Etapa Atual:</strong> Etapa 1 - Fundamentação Teórica (25% concluída)</p>
            <p><strong>Próximo Milestone:</strong> Framework Conceitual Completo (Janeiro 2026)</p>
            <p><strong>Defesa Prevista:</strong> Setembro 2026</p>
        </div>
        
        <div class="current-phase">
            <h3>🎯 Fase Atual: Revisão Sistemática da Literatura</h3>
            <p><strong>Progresso:</strong> 80% concluído</p>
            <p><strong>Próxima Tarefa:</strong> Análise de Técnicas de Otimização</p>
        </div>
        
        <div class="timeline-info">
            <h3>📅 Timeline Geral</h3>
            <p><strong>Início:</strong> Agosto 2025 | <strong>Fim:</strong> Setembro 2026</p>
            <p><strong>Duração Total:</strong> 14 meses</p>
            <p><strong>Etapas Principais:</strong> 4 etapas com 12 tarefas detalhadas</p>
        </div>
        
        <div class="gantt-container" id="gantt-chart"></div>
        
        <div class="legend">
            <h3>🎨 Legenda</h3>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #4CAF50;"></span>
                <span>Etapa 1: Fundamentação Teórica</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #2196F3;"></span>
                <span>Etapa 2: Desenvolvimento Experimental</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #FF9800;"></span>
                <span>Etapa 3: Análise e Redação</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #E91E63;"></span>
                <span>Etapa 4: Finalização e Defesa</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #9C27B0;"></span>
                <span>Milestones Principais</span>
            </div>
        </div>
    </div>

    <script>
        // Dados do Gantt Chart
        const ganttData = """ + json.dumps(gantt_data, indent=2) + """;
        
        // Configurações do gráfico
        const margin = {top: 50, right: 50, bottom: 100, left: 250};
        const width = 1400 - margin.left - margin.right;
        const height = 700 - margin.top - margin.bottom;
        
        // Escalas de tempo
        const startDate = new Date(ganttData.start_date);
        const endDate = new Date(ganttData.end_date);
        
        const xScale = d3.scaleTime()
            .domain([startDate, endDate])
            .range([0, width]);
            
        const yScale = d3.scaleBand()
            .domain(ganttData.tasks.map(d => d.name))
            .range([0, height])
            .padding(0.1);
        
        // Criar SVG
        const svg = d3.select("#gantt-chart")
            .append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", `translate(${margin.left},${margin.top})`);
        
        // Eixos
        const xAxis = d3.axisBottom(xScale)
            .tickFormat(d3.timeFormat("%b %Y"))
            .tickSize(-height);
            
        const yAxis = d3.axisLeft(yScale);
        
        svg.append("g")
            .attr("class", "axis")
            .attr("transform", `translate(0,${height})`)
            .call(xAxis);
            
        svg.append("g")
            .attr("class", "axis")
            .call(yAxis);
        
        // Barras das tarefas
        svg.selectAll(".task-bar")
            .data(ganttData.tasks.filter(d => d.id.length > 2)) // Excluir etapas principais
            .enter()
            .append("rect")
            .attr("class", "task-bar")
            .attr("x", d => xScale(new Date(d.start)))
            .attr("y", d => yScale(d.name))
            .attr("width", d => {
                const start = new Date(d.start);
                const end = new Date(d.end);
                return xScale(end) - xScale(start);
            })
            .attr("height", yScale.bandwidth())
            .attr("fill", d => d.color)
            .attr("rx", 3)
            .on("mouseover", function(event, d) {
                d3.select(this).style("opacity", 0.7);
                // Tooltip
                const tooltip = d3.select("body").append("div")
                    .attr("class", "tooltip")
                    .style("position", "absolute")
                    .style("background", "rgba(0,0,0,0.8)")
                    .style("color", "white")
                    .style("padding", "8px")
                    .style("border-radius", "4px")
                    .style("font-size", "12px")
                    .style("pointer-events", "none");
                    
                tooltip.html(`
                    <strong>${d.name}</strong><br/>
                    Início: ${new Date(d.start).toLocaleDateString('pt-BR')}<br/>
                    Fim: ${new Date(d.end).toLocaleDateString('pt-BR')}<br/>
                    Progresso: ${d.progress}%
                `)
                .style("left", (event.pageX + 10) + "px")
                .style("top", (event.pageY - 10) + "px");
            })
            .on("mouseout", function() {
                d3.select(this).style("opacity", 1);
                d3.selectAll(".tooltip").remove();
            });
        
        // Milestones
        svg.selectAll(".milestone")
            .data(ganttData.tasks.filter(d => d.id.startsWith('m')))
            .enter()
            .append("circle")
            .attr("class", "milestone")
            .attr("cx", d => xScale(new Date(d.start)))
            .attr("cy", d => yScale(d.name) + yScale.bandwidth() / 2)
            .attr("r", 6)
            .on("mouseover", function(event, d) {
                d3.select(this).style("opacity", 0.7);
                const tooltip = d3.select("body").append("div")
                    .attr("class", "tooltip")
                    .style("position", "absolute")
                    .style("background", "rgba(0,0,0,0.8)")
                    .style("color", "white")
                    .style("padding", "8px")
                    .style("border-radius", "4px")
                    .style("font-size", "12px")
                    .style("pointer-events", "none");
                    
                tooltip.html(`
                    <strong>${d.name}</strong><br/>
                    Data: ${new Date(d.start).toLocaleDateString('pt-BR')}
                `)
                .style("left", (event.pageX + 10) + "px")
                .style("top", (event.pageY - 10) + "px");
            })
            .on("mouseout", function() {
                d3.select(this).style("opacity", 1);
                d3.selectAll(".tooltip").remove();
            });
        
        // Linha de tempo atual
        const currentDate = new Date();
        if (currentDate >= startDate && currentDate <= endDate) {
            svg.append("line")
                .attr("x1", xScale(currentDate))
                .attr("x2", xScale(currentDate))
                .attr("y1", 0)
                .attr("y2", height)
                .attr("stroke", "#FF5722")
                .attr("stroke-width", 2)
                .attr("stroke-dasharray", "5,5");
                
            svg.append("text")
                .attr("x", xScale(currentDate) + 5)
                .attr("y", 20)
                .attr("fill", "#FF5722")
                .attr("font-weight", "bold")
                .text("Hoje");
        }
    </script>
</body>
</html>
    """
    
    return html_template


def main():
    """
    Função principal que gera o Gantt Chart.
    """
    print("Gerando Gantt Chart detalhado do cronograma do projeto de mestrado...")
    
    # Criar dados do Gantt
    gantt_data = create_gantt_data()
    
    # Gerar HTML
    html_content = generate_html_gantt(gantt_data)
    
    # Salvar arquivo HTML
    output_file = "cronograma_mestrado_gantt.html"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    # Gerar imagem PNG
    print("Gerando imagem PNG do cronograma...")
    fig = generate_png_gantt(gantt_data)
    
    # Criar diretório se não existir
    import os
    png_dir = "assets/imagens_artigo/cronogramas"
    os.makedirs(png_dir, exist_ok=True)
    
    # Salvar imagem PNG no novo caminho
    png_file = os.path.join(png_dir, "cronograma_mestrado_gantt.png")
    fig.savefig(png_file, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    
    print(f"✅ Gantt Chart detalhado gerado com sucesso!")
    print(f"📁 Arquivo HTML: {output_file}")
    print(f"🖼️ Arquivo PNG: {png_file}")
    print(f"🌐 Abra o arquivo HTML no navegador para visualização interativa")
    print(f"📄 Use o arquivo PNG para inclusão na dissertação")
    
    # Mostrar resumo do cronograma
    print("\n📅 RESUMO DO CRONOGRAMA DETALHADO:")
    print(f"   • Início: {gantt_data['start_date']}")
    print(f"   • Defesa: {gantt_data['end_date']}")
    print(f"   • Duração: 14 meses")
    print(f"   • Etapas: 4 principais")
    print(f"   • Tarefas: 12 detalhadas")
    print(f"   • Milestones: 4 críticos")
    
    print("\n🎯 MILESTONES PRINCIPAIS:")
    milestones = [task for task in gantt_data['tasks'] if task['id'].startswith('m')]
    for milestone in milestones:
        print(f"   • {milestone['name']}: {milestone['start']}")
    
    print("\n📋 ETAPAS PRINCIPAIS:")
    etapas = [task for task in gantt_data['tasks'] if task['id'].startswith('etapa')]
    for etapa in etapas:
        print(f"   • {etapa['name']}: {etapa['start']} - {etapa['end']}")


if __name__ == "__main__":
    main() 