# Organização das Imagens do Artigo

Esta pasta contém todas as imagens organizadas para uso na dissertação de mestrado sobre processamento hiperespectral embarcado.

## 📁 Estrutura de Pastas

### 📊 `cronogramas/`
Contém gráficos e visualizações de cronogramas do projeto.
- **cronograma_mestrado_gantt.png** - Gráfico Gantt detalhado do cronograma (Agosto 2025 - Setembro 2026)

### 🏗️ `diagramas_arquitetura/`
Contém diagramas da arquitetura do sistema heterogêneo proposto.
- *Pasta preparada para futuros diagramas*

### 📈 `graficos_performance/`
Contém gráficos de performance, consumo energético e latência.
- *Pasta preparada para gráficos de resultados experimentais*

### 🔬 `resultados_experimentais/`
Contém imagens de resultados de experimentos e validações.
- *Pasta preparada para screenshots e imagens de experimentos*

### 🌈 `imagens_hiperespectrais/`
Contém imagens de exemplo de dados hiperespectrais.
- **starwars21280.jpg** - Imagem de exemplo hiperespectral

### 🏛️ `logos_institucionais/`
Contém logos e elementos institucionais da UNICAMP.
- **logo-unicamp.pdf** - Logo oficial da UNICAMP
- **logo-unicamp.eps** - Logo UNICAMP em formato EPS
- **logoFT.png** - Logo da Faculdade de Tecnologia
- **white.pdf, blanco.pdf, branco.pdf** - Versões em branco dos logos

## 📋 Convenções de Nomenclatura

### Imagens de Cronogramas
- Formato: `cronograma_[tipo]_[data].png`
- Exemplo: `cronograma_mestrado_gantt.png`

### Diagramas de Arquitetura
- Formato: `diagrama_[componente]_[tipo].png`
- Exemplo: `diagrama_sistema_heterogeneo.png`

### Gráficos de Performance
- Formato: `grafico_[metrica]_[dataset].png`
- Exemplo: `grafico_consumo_energetico_indian_pines.png`

### Resultados Experimentais
- Formato: `resultado_[experimento]_[data].png`
- Exemplo: `resultado_validacao_cs_2025-08-05.png`

### Imagens Hiperespectrais
- Formato: `[dataset]_[banda]_[descricao].jpg`
- Exemplo: `indian_pines_banda_100_agricultura.jpg`

## 🔧 Uso na Dissertação

### Inclusão no LaTeX
```latex
\includegraphics[width=0.8\textwidth]{../assets/imagens_artigo/cronogramas/cronograma_mestrado_gantt.png}
```

### Referência no Texto
```latex
A Figura \ref{fig:cronograma} apresenta o cronograma detalhado...
```

## 📝 Manutenção

### Adicionando Novas Imagens
1. Escolha a pasta apropriada baseada no tipo de imagem
2. Use a convenção de nomenclatura estabelecida
3. Atualize este README se necessário
4. Atualize as referências no LaTeX

### Formatos Suportados
- **PNG**: Para gráficos, diagramas e screenshots
- **JPG**: Para imagens fotográficas e dados hiperespectrais
- **PDF**: Para logos e diagramas vetoriais
- **EPS**: Para compatibilidade com LaTeX

### Resolução Recomendada
- **Gráficos**: 300 DPI para impressão
- **Diagramas**: 300 DPI para clareza
- **Imagens**: 150-300 DPI dependendo do uso

## 🎯 Próximas Imagens Planejadas

### Diagramas de Arquitetura
- Diagrama do sistema heterogêneo CPU+GPU+FPGA
- Pipeline de processamento hiperespectral
- Fluxograma da metodologia de validação

### Gráficos de Performance
- Comparação de consumo energético entre técnicas
- Análise de trade-offs precisão vs latência
- Benchmarks de throughput

### Resultados Experimentais
- Screenshots dos protótipos implementados
- Resultados de validação experimental
- Análises estatísticas dos dados

---

**Última atualização**: 2025-08-05  
**Responsável**: Diego Maia  
**Projeto**: Dissertação de Mestrado - UNICAMP FT 