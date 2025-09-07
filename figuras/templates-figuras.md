# Templates para Criação de Figuras - Dissertação UNICAMP-FT

## 🎨 Paleta de Cores Padrão

### **Cores Principais:**
- **Azul Principal**: #1f77b4 (RGB: 31, 119, 180)
- **Laranja**: #ff7f0e (RGB: 255, 127, 14)
- **Verde**: #2ca02c (RGB: 44, 160, 44)
- **Vermelho**: #d62728 (RGB: 214, 39, 40)
- **Roxo**: #9467bd (RGB: 148, 103, 189)
- **Marrom**: #8c564b (RGB: 140, 86, 75)

### **Cores Neutras:**
- **Cinza Escuro**: #333333
- **Cinza Médio**: #666666
- **Cinza Claro**: #cccccc
- **Preto**: #000000
- **Branco**: #ffffff

## 📊 Templates para Gráficos

### **1. Gráfico de Barras Comparativo**
```python
import matplotlib.pyplot as plt
import numpy as np

# Configurações
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 12
plt.rcParams['figure.figsize'] = (10, 6)

# Dados exemplo
categorias = ['FPGA', 'GPU', 'CPU', 'Híbrido']
throughput = [250, 180, 45, 320]
cores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Criar gráfico
fig, ax = plt.subplots()
bars = ax.bar(categorias, throughput, color=cores, alpha=0.8, edgecolor='black', linewidth=0.5)

# Configurações
ax.set_ylabel('Throughput (fps)', fontweight='bold')
ax.set_xlabel('Arquitetura', fontweight='bold')
ax.grid(True, alpha=0.3, axis='y')
ax.set_ylim(0, max(throughput) * 1.1)

# Adicionar valores nas barras
for bar, value in zip(bars, throughput):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 5,
            f'{value}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('graf-throughput-comparativo.pdf', dpi=300, bbox_inches='tight')
plt.show()
```

### **2. Gráfico de Linhas (Performance vs Tempo)**
```python
import matplotlib.pyplot as plt
import numpy as np

# Configurações
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 12

# Dados exemplo
tempo = np.linspace(0, 100, 50)
fpga_perf = 250 + 10 * np.sin(tempo/10) + np.random.normal(0, 5, 50)
gpu_perf = 180 + 15 * np.cos(tempo/8) + np.random.normal(0, 8, 50)

# Criar gráfico
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(tempo, fpga_perf, 'o-', color='#1f77b4', linewidth=2, 
        markersize=4, label='FPGA', alpha=0.8)
ax.plot(tempo, gpu_perf, 's-', color='#ff7f0e', linewidth=2, 
        markersize=4, label='GPU', alpha=0.8)

# Configurações
ax.set_xlabel('Tempo (s)', fontweight='bold')
ax.set_ylabel('Performance (fps)', fontweight='bold')
ax.grid(True, alpha=0.3)
ax.legend(frameon=True, fancybox=True, shadow=True)

plt.tight_layout()
plt.savefig('graf-performance-tempo.pdf', dpi=300, bbox_inches='tight')
plt.show()
```

### **3. Scatter Plot (Trade-off Analysis)**
```python
import matplotlib.pyplot as plt
import numpy as np

# Dados exemplo
np.random.seed(42)
n_points = 20

# FPGA
fpga_power = np.random.uniform(5, 15, n_points//4)
fpga_perf = 300 - 10 * fpga_power + np.random.normal(0, 20, n_points//4)

# GPU
gpu_power = np.random.uniform(20, 50, n_points//4)
gpu_perf = 400 - 5 * gpu_power + np.random.normal(0, 30, n_points//4)

# Criar gráfico
fig, ax = plt.subplots(figsize=(10, 8))
ax.scatter(fpga_power, fpga_perf, c='#1f77b4', s=100, alpha=0.7, 
           label='FPGA', edgecolors='black', linewidth=0.5)
ax.scatter(gpu_power, gpu_perf, c='#ff7f0e', s=100, alpha=0.7, 
           label='GPU', edgecolors='black', linewidth=0.5)

# Configurações
ax.set_xlabel('Consumo Energético (W)', fontweight='bold')
ax.set_ylabel('Performance (fps)', fontweight='bold')
ax.grid(True, alpha=0.3)
ax.legend()

plt.tight_layout()
plt.savefig('graf-tradeoff-energia-performance.pdf', dpi=300, bbox_inches='tight')
plt.show()
```

## 🔧 Templates para Diagramas (Draw.io)

### **1. Diagrama de Arquitetura de Sistema**
```xml
<!-- Template básico para Draw.io -->
<mxGraphModel>
  <root>
    <!-- Componentes principais -->
    <mxCell id="sensor" value="Sensor&#xa;Hiperespectral" style="rounded=1;fillColor=#e1d5e7;strokeColor=#9673a6"/>
    <mxCell id="fpga" value="FPGA&#xa;Processamento" style="rounded=1;fillColor=#d5e8d4;strokeColor=#82b366"/>
    <mxCell id="gpu" value="GPU&#xa;Aceleração" style="rounded=1;fillColor=#fff2cc;strokeColor=#d6b656"/>
    <mxCell id="memoria" value="Memória&#xa;DDR4" style="rounded=1;fillColor=#f8cecc;strokeColor=#b85450"/>
    
    <!-- Conexões -->
    <mxCell id="conn1" value="Dados&#xa;Brutos" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1"/>
  </root>
</mxGraphModel>
```

### **2. Fluxograma de Metodologia**
```
Início
  ↓
[Levantamento Bibliográfico]
  ↓
[Definição de Métricas]
  ↓
[Modelagem Teórica]
  ↓
[Simulação]
  ↓
[Análise de Resultados]
  ↓
[Síntese da Arquitetura]
  ↓
Fim
```

## 📐 Templates para Esquemas Técnicos

### **1. Layout de Memória**
```
+------------------+
|   Cache L1       |  ← 32 KB
+------------------+
|   Cache L2       |  ← 256 KB
+------------------+
|   Cache L3       |  ← 2 MB
+------------------+
|   Memória DDR4   |  ← 8 GB
+------------------+
|   Armazenamento  |  ← 256 GB SSD
+------------------+
```

### **2. Pipeline de Processamento**
```
Entrada → [Pré-proc.] → [Classif.] → [Pós-proc.] → Saída
    ↓         ↓           ↓           ↓         ↓
  Dados    Filtros   Algoritmos   Validação  Resultados
```

## 📊 Templates para Tabelas Complexas

### **1. Tabela de Comparação de Técnicas**
```latex
\begin{table}[htbp]
\centering
\caption{Comparação de técnicas de processamento hiperespectral}
\label{tab:comparacao-tecnicas}
\begin{tabular}{|l|c|c|c|c|c|}
\hline
\textbf{Técnica} & \textbf{Throughput} & \textbf{Latência} & \textbf{Energia} & \textbf{Precisão} & \textbf{Complexidade} \\
                 & \textbf{(fps)}      & \textbf{(ms)}     & \textbf{(W)}     & \textbf{(\%)}     & \textbf{(O(n))} \\
\hline
FPGA-CNN         & 250                 & 4.0               & 12               & 94.2              & O(n²) \\
\hline
GPU-SVM          & 180                 & 5.6               & 35               & 92.8              & O(n³) \\
\hline
CPU-RF           & 45                  & 22.2              & 65               & 89.5              & O(n log n) \\
\hline
Híbrido          & 320                 & 3.1               & 28               & 96.1              & O(n²) \\
\hline
\end{tabular}
\end{table}
```

## 🎯 Configurações Padrão para Ferramentas

### **MATLAB**
```matlab
% Configurações padrão para figuras
set(0, 'DefaultFigureRenderer', 'painters');
set(0, 'DefaultFigureColor', 'white');
set(0, 'DefaultAxesFontName', 'Times New Roman');
set(0, 'DefaultAxesFontSize', 12);
set(0, 'DefaultTextFontName', 'Times New Roman');
set(0, 'DefaultTextFontSize', 12);

% Salvar figura
print(gcf, 'nome-figura.pdf', '-dpdf', '-r300');
```

### **Python (Matplotlib)**
```python
# Configurações globais
plt.rcParams.update({
    'font.family': 'Times New Roman',
    'font.size': 12,
    'axes.labelweight': 'bold',
    'axes.grid': True,
    'grid.alpha': 0.3,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.format': 'pdf'
})
```

### **R (ggplot2)**
```r
# Tema padrão
theme_dissertacao <- theme_minimal() +
  theme(
    text = element_text(family = "Times New Roman", size = 12),
    axis.title = element_text(face = "bold"),
    panel.grid.minor = element_blank(),
    panel.grid.major = element_line(alpha = 0.3)
  )

# Aplicar tema
ggplot(data) + 
  geom_point() + 
  theme_dissertacao
```

## 📏 Dimensões Padrão

### **Figuras Simples:**
- Largura: 12-15 cm
- Altura: 8-10 cm
- DPI: 300

### **Figuras Complexas:**
- Largura: 15-17 cm
- Altura: 10-12 cm
- DPI: 300

### **Diagramas:**
- Largura: 14-16 cm
- Altura: Variável conforme conteúdo
- Formato: PDF vetorial

### **Gráficos:**
- Largura: 12-14 cm
- Altura: 8-10 cm
- Formato: PDF vetorial

## 🔍 Checklist de Qualidade

### **Antes de Finalizar:**
- [ ] Fonte Times New Roman, tamanho ≥ 10pt
- [ ] Cores contrastantes e acessíveis
- [ ] Elementos claramente identificados
- [ ] Eixos rotulados com unidades
- [ ] Legenda quando necessária
- [ ] Resolução adequada (300 DPI)
- [ ] Formato correto (PDF preferencial)
- [ ] Nomenclatura seguindo padrão
- [ ] Testado em impressão P&B

---

**Nota**: Estes templates servem como ponto de partida. Adapte conforme necessário para suas necessidades específicas, sempre mantendo consistência visual em toda a dissertação.
