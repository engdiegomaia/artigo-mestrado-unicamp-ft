#!/usr/bin/env python3
"""
Script para gerar Gantt Chart do cronograma do projeto de mestrado.
Gera um arquivo HTML com visualização interativa do cronograma e uma imagem PNG.

Autor: Diego Maia
Data: 2025-08-12
Versão: 3.0 - Incluindo fase de qualificação UNICAMP e ajuste de cronograma
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
    Cria os dados do Gantt Chart baseado no cronograma detalhado de 10 meses.
    Estruturado em 6 fases: Aquisição Hardware, Implementação FPGA, 
    Implementação GPU, Validação, Síntese/Publicação, Escrita/Defesa.
    
    Returns:
        dict: Dados estruturados para o Gantt Chart
    """
    
    # Data de início: Setembro 2024 (ajustado para refletir cronograma real)
    start_date = datetime.date(2024, 9, 1)
    
    # Data de defesa: Julho 2025 (10 meses depois)
    defense_date = datetime.date(2025, 7, 1)
    
    # Estrutura das tarefas baseada no cronograma de 10 meses (40 semanas)
    tasks = [
        # ===== FASE 1: AQUISIÇÃO E SETUP DE HARDWARE (8 semanas) =====
        {
            "id": "fase1",
            "name": "Aquisição e Setup de Hardware",
            "start": start_date.strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(weeks=8)).strftime("%Y-%m-%d"),  # 8 semanas
            "progress": 0,
            "dependencies": "",
            "color": "#4CAF50"
        },
        {
            "id": "1.1",
            "name": "Especificação e Aquisição de Hardware",
            "start": start_date.strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(weeks=3)).strftime("%Y-%m-%d"),  # 3 semanas
            "progress": 0,
            "dependencies": "",
            "color": "#81C784"
        },
        {
            "id": "1.2",
            "name": "Setup dos Ambientes de Desenvolvimento",
            "start": (start_date + timedelta(weeks=3)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(weeks=6)).strftime("%Y-%m-%d"),  # 3 semanas
            "progress": 0,
            "dependencies": "1.1",
            "color": "#81C784"
        },
        {
            "id": "1.3",
            "name": "Testes Preliminares e Validação",
            "start": (start_date + timedelta(weeks=6)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(weeks=8)).strftime("%Y-%m-%d"),  # 2 semanas
            "progress": 0,
            "dependencies": "1.2",
            "color": "#81C784"
        },
        
        # ===== FASE 2: IMPLEMENTAÇÃO FPGA (6 semanas) =====
        {
            "id": "fase2",
            "name": "Implementação FPGA",
            "start": (start_date + timedelta(weeks=8)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(weeks=14)).strftime("%Y-%m-%d"),  # 6 semanas
            "progress": 0,
            "dependencies": "1.3",
            "color": "#2196F3"
        },
        {
            "id": "2.1",
            "name": "Pipeline de Pré-processamento VHDL",
            "start": (start_date + timedelta(weeks=8)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(weeks=10)).strftime("%Y-%m-%d"),  # 2 semanas
            "progress": 0,
            "dependencies": "1.3",
            "color": "#64B5F6"
        },
        {
            "id": "2.2",
            "name": "Algoritmos PCA e EMCR Otimizados",
            "start": (start_date + timedelta(weeks=10)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(weeks=12)).strftime("%Y-%m-%d"),  # 2 semanas
            "progress": 0,
            "dependencies": "2.1",
            "color": "#64B5F6"
        },
        {
            "id": "2.3",
            "name": "Classificadores SVM/k-NN e Índices",
            "start": (start_date + timedelta(weeks=12)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(weeks=14)).strftime("%Y-%m-%d"),  # 2 semanas
            "progress": 0,
            "dependencies": "2.2",
            "color": "#64B5F6"
        },
        
        # ===== FASE 3: IMPLEMENTAÇÃO GPU (6 semanas) =====
        {
            "id": "fase3",
            "name": "Implementação GPU",
            "start": (start_date + timedelta(weeks=14)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(weeks=20)).strftime("%Y-%m-%d"),  # 6 semanas
            "progress": 0,
            "dependencies": "2.3",
            "color": "#FF9800"
        },
        {
            "id": "3.1",
            "name": "Kernels CUDA de Pré-processamento",
            "start": (start_date + timedelta(weeks=14)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(weeks=16)).strftime("%Y-%m-%d"),  # 2 semanas
            "progress": 0,
            "dependencies": "2.3",
            "color": "#FFB74D"
        },
        {
            "id": "3.2",
            "name": "PCA/KPCA com cuBLAS Otimizado",
            "start": (start_date + timedelta(weeks=16)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(weeks=18)).strftime("%Y-%m-%d"),  # 2 semanas
            "progress": 0,
            "dependencies": "3.1",
            "color": "#FFB74D"
        },
        {
            "id": "3.3",
            "name": "Classificadores com TensorRT",
            "start": (start_date + timedelta(weeks=18)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(weeks=20)).strftime("%Y-%m-%d"),  # 2 semanas
            "progress": 0,
            "dependencies": "3.2",
            "color": "#FFB74D"
        },
        
        # ===== FASE 4: VALIDAÇÃO EXPERIMENTAL (6 semanas) =====
        {
            "id": "fase4",
            "name": "Validação Experimental e Comparação",
            "start": (start_date + timedelta(weeks=20)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(weeks=26)).strftime("%Y-%m-%d"),  # 6 semanas
            "progress": 0,
            "dependencies": "3.3",
            "color": "#9C27B0"
        },
        {
            "id": "4.1",
            "name": "Testes Exaustivos com Dataset Salinas",
            "start": (start_date + timedelta(weeks=20)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(weeks=23)).strftime("%Y-%m-%d"),  # 3 semanas
            "progress": 0,
            "dependencies": "3.3",
            "color": "#BA68C8"
        },
        {
            "id": "4.2",
            "name": "Análise Estatística e Otimização Pareto",
            "start": (start_date + timedelta(weeks=23)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(weeks=26)).strftime("%Y-%m-%d"),  # 3 semanas
            "progress": 0,
            "dependencies": "4.1",
            "color": "#BA68C8"
        },
        
        # ===== FASE 5: SÍNTESE E PUBLICAÇÃO (6 semanas) =====
        {
            "id": "fase5",
            "name": "Síntese e Publicação",
            "start": (start_date + timedelta(weeks=26)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(weeks=32)).strftime("%Y-%m-%d"),  # 6 semanas
            "progress": 0,
            "dependencies": "4.2",
            "color": "#FF5722"
        },
        {
            "id": "5.1",
            "name": "Proposição da Arquitetura Heterogênea",
            "start": (start_date + timedelta(weeks=26)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(weeks=29)).strftime("%Y-%m-%d"),  # 3 semanas
            "progress": 0,
            "dependencies": "4.2",
            "color": "#FF8A65"
        },
        {
            "id": "5.2",
            "name": "Redação e Submissão de Artigo Científico",
            "start": (start_date + timedelta(weeks=29)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(weeks=32)).strftime("%Y-%m-%d"),  # 3 semanas
            "progress": 0,
            "dependencies": "5.1",
            "color": "#FF8A65"
        },
        
        # ===== FASE 6: ESCRITA DA DISSERTAÇÃO E DEFESA (12 semanas) =====
        {
            "id": "fase6",
            "name": "Escrita da Dissertação e Defesa",
            "start": (start_date + timedelta(weeks=32)).strftime("%Y-%m-%d"),
            "end": defense_date.strftime("%Y-%m-%d"),  # 8 semanas restantes
            "progress": 0,
            "dependencies": "5.2",
            "color": "#E91E63"
        },
        {
            "id": "6.1",
            "name": "Redação dos Capítulos de Resultados",
            "start": (start_date + timedelta(weeks=32)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(weeks=36)).strftime("%Y-%m-%d"),  # 4 semanas
            "progress": 0,
            "dependencies": "5.2",
            "color": "#F06292"
        },
        {
            "id": "6.2",
            "name": "Revisão e Formatação Final",
            "start": (start_date + timedelta(weeks=36)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(weeks=38)).strftime("%Y-%m-%d"),  # 2 semanas
            "progress": 0,
            "dependencies": "6.1",
            "color": "#F06292"
        },
        {
            "id": "6.3",
            "name": "Preparação da Defesa",
            "start": (start_date + timedelta(weeks=38)).strftime("%Y-%m-%d"),
            "end": defense_date.strftime("%Y-%m-%d"),  # 2 semanas
            "progress": 0,
            "dependencies": "6.2",
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
            "color": "#795548"
        },
        {
            "id": "m1",
            "name": "M1: Hardware Configurado",
            "start": (start_date + timedelta(weeks=8)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(weeks=8)).strftime("%Y-%m-%d"),
            "progress": 0,
            "dependencies": "1.3",
            "color": "#A1887F"
        },
        {
            "id": "m2",
            "name": "M2: Implementação FPGA Completa",
            "start": (start_date + timedelta(weeks=14)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(weeks=14)).strftime("%Y-%m-%d"),
            "progress": 0,
            "dependencies": "2.3",
            "color": "#A1887F"
        },
        {
            "id": "m3",
            "name": "M3: Implementação GPU Completa",
            "start": (start_date + timedelta(weeks=20)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(weeks=20)).strftime("%Y-%m-%d"),
            "progress": 0,
            "dependencies": "3.3",
            "color": "#A1887F"
        },
        {
            "id": "m4",
            "name": "M4: Validação Experimental Concluída",
            "start": (start_date + timedelta(weeks=26)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(weeks=26)).strftime("%Y-%m-%d"),
            "progress": 0,
            "dependencies": "4.2",
            "color": "#A1887F"
        },
        {
            "id": "m5",
            "name": "M5: Artigo Científico Submetido",
            "start": (start_date + timedelta(weeks=32)).strftime("%Y-%m-%d"),
            "end": (start_date + timedelta(weeks=32)).strftime("%Y-%m-%d"),
            "progress": 0,
            "dependencies": "5.2",
            "color": "#A1887F"
        },
        {
            "id": "m6",
            "name": "M6: Defesa da Dissertação",
            "start": defense_date.strftime("%Y-%m-%d"),
            "end": defense_date.strftime("%Y-%m-%d"),
            "progress": 0,
            "dependencies": "6.3",
            "color": "#A1887F"
        }
    ]
    
    return {
        "title": "Cronograma Detalhado - Dissertação de Mestrado (10 meses - 40 semanas)",
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
    
    # Filtrar tarefas (incluir fases e subtarefas, excluir apenas milestones)
    task_tasks = [task for task in gantt_data['tasks'] if task['id'].startswith(('fase', '1.', '2.', '3.', '4.', '5.', '6.'))]
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
    ax.set_title('Cronograma Detalhado - Dissertação de Mestrado\n10 meses (40 semanas) - 6 Fases', 
                 fontsize=18, fontweight='bold', pad=20)  # Aumentado de 14 para 18
    
    # Adicionar legendas
    legend_elements = [
        plt.Rectangle((0,0),1,1, facecolor='#4CAF50', alpha=0.8, label='Fase 1: Aquisição Hardware'),
        plt.Rectangle((0,0),1,1, facecolor='#2196F3', alpha=0.8, label='Fase 2: Implementação FPGA'),
        plt.Rectangle((0,0),1,1, facecolor='#FF9800', alpha=0.8, label='Fase 3: Implementação GPU'),
        plt.Rectangle((0,0),1,1, facecolor='#9C27B0', alpha=0.8, label='Fase 4: Validação Experimental'),
        plt.Rectangle((0,0),1,1, facecolor='#FF5722', alpha=0.8, label='Fase 5: Síntese e Publicação'),
        plt.Rectangle((0,0),1,1, facecolor='#E91E63', alpha=0.8, label='Fase 6: Escrita e Defesa'),
        plt.scatter([], [], s=100, color='#795548', marker='D', edgecolors='black', label='Milestones')
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
            <p><strong>Cronograma:</strong> 10 meses estruturados em 6 fases principais</p>
            <p><strong>Primeira Fase:</strong> Aquisição e Setup de Hardware (8 semanas)</p>
            <p><strong>Publicação Científica:</strong> Semanas 29-32</p>
            <p><strong>Defesa Prevista:</strong> Semana 40 (final do cronograma)</p>
        </div>
        
        <div class="current-phase">
            <h3>🎯 Estrutura do Cronograma</h3>
            <p><strong>Fase 1-3:</strong> Hardware, FPGA e GPU (20 semanas)</p>
            <p><strong>Fase 4-6:</strong> Validação, Publicação e Defesa (20 semanas)</p>
        </div>
        
        <div class="timeline-info">
            <h3>📅 Timeline Geral</h3>
            <p><strong>Duração Total:</strong> 40 semanas (10 meses)</p>
            <p><strong>Fases Principais:</strong> 6 fases com 18 tarefas detalhadas</p>
            <p><strong>Milestones:</strong> 6 marcos críticos</p>
        </div>
        
        <div class="gantt-container" id="gantt-chart"></div>
        
        <div class="legend">
            <h3>🎨 Legenda das 6 Fases</h3>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #4CAF50;"></span>
                <span>Fase 1: Aquisição e Setup de Hardware</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #2196F3;"></span>
                <span>Fase 2: Implementação FPGA</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #FF9800;"></span>
                <span>Fase 3: Implementação GPU</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #9C27B0;"></span>
                <span>Fase 4: Validação Experimental</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #FF5722;"></span>
                <span>Fase 5: Síntese e Publicação</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #E91E63;"></span>
                <span>Fase 6: Escrita e Defesa</span>
            </div>
            <div class="legend-item">
                <span class="legend-color" style="background-color: #795548;"></span>
                <span>Milestones Críticos</span>
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
            .data(ganttData.tasks.filter(d => d.id.startsWith('fase') || d.id.match(/^\d\./))) // Incluir fases e subtarefas
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
    print(f"   • Duração: 10 meses (40 semanas)")
    print(f"   • Fases: 6 principais estruturadas")
    print(f"   • Tarefas: 18 detalhadas")
    print(f"   • Milestones: 6 críticos")
    
    print("\n🎯 MILESTONES PRINCIPAIS:")
    milestones = [task for task in gantt_data['tasks'] if task['id'].startswith('m')]
    for milestone in milestones:
        print(f"   • {milestone['name']}: {milestone['start']}")
    
    print("\n📋 FASES PRINCIPAIS:")
    fases = [task for task in gantt_data['tasks'] if task['id'].startswith('fase')]
    for fase in fases:
        print(f"   • {fase['name']}: {fase['start']} - {fase['end']}")
        
    print("\n⚡ ESTRUTURA DO CRONOGRAMA:")
    print("   • Semanas 1-8: Aquisição e Setup de Hardware")
    print("   • Semanas 9-14: Implementação FPGA")  
    print("   • Semanas 15-20: Implementação GPU")
    print("   • Semanas 21-26: Validação Experimental")
    print("   • Semanas 27-32: Síntese e Publicação")
    print("   • Semanas 33-40: Escrita e Defesa")


if __name__ == "__main__":
    main() 