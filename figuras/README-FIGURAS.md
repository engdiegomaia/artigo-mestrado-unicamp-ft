# Guia de Organização de Figuras - Dissertação UNICAMP-FT

## 📁 Estrutura de Pastas

```
figuras/
├── capitulos/           # Figuras organizadas por capítulo
│   ├── cap01-introducao/
│   ├── cap02-levantamento/
│   ├── cap03-metodologia/
│   ├── cap04-resultados/
│   └── cap05-conclusoes/
├── diagramas/           # Diagramas de blocos, fluxogramas, arquiteturas
├── graficos/            # Gráficos, plots, charts
├── esquemas/            # Esquemas técnicos, circuitos, layouts
└── tabelas/             # Tabelas complexas em formato de imagem
```

## 🎯 Convenções de Nomenclatura

### Padrão Geral
```
[tipo]-[capitulo]-[numero]-[descricao-breve].[extensao]
```

### Exemplos por Tipo:

#### **Figuras por Capítulo:**
- `fig-cap01-01-arquitetura-hiperespectral.pdf`
- `fig-cap02-02-comparacao-algoritmos.png`
- `fig-cap03-03-metodologia-proposta.pdf`

#### **Diagramas:**
- `diag-arquitetura-fpga-gpu.pdf`
- `diag-fluxo-processamento.pdf`
- `diag-pipeline-otimizado.pdf`

#### **Gráficos:**
- `graf-performance-comparativa.pdf`
- `graf-consumo-energetico.pdf`
- `graf-throughput-latencia.pdf`

#### **Esquemas:**
- `esq-sistema-embarcado.pdf`
- `esq-memoria-hierarquia.pdf`
- `esq-paralelizacao.pdf`

#### **Tabelas:**
- `tab-comparacao-tecnicas.pdf`
- `tab-resultados-benchmark.pdf`
- `tab-especificacoes-hardware.pdf`

## 📐 Especificações Técnicas

### **Formatos Recomendados:**
- **PDF**: Figuras vetoriais, diagramas, esquemas (PREFERENCIAL)
- **PNG**: Screenshots, figuras rasterizadas (300 DPI mínimo)
- **EPS**: Figuras vetoriais para compatibilidade LaTeX
- **SVG**: Figuras vetoriais editáveis (converter para PDF/EPS)

### **Resoluções:**
- **Figuras rasterizadas**: Mínimo 300 DPI
- **Screenshots**: Mínimo 150 DPI, preferível 300 DPI
- **Gráficos**: Vetoriais sempre que possível

### **Dimensões:**
- **Largura máxima**: 17 cm (largura da página UNICAMP-FT)
- **Altura máxima**: 23 cm (altura útil da página)
- **Figuras pequenas**: Mínimo 8 cm de largura para legibilidade

## 🎨 Padrões Visuais

### **Cores:**
- **Gráficos**: Usar paleta consistente e acessível
- **Diagramas**: Cores contrastantes para diferentes elementos
- **Evitar**: Cores muito saturadas ou difíceis de imprimir

### **Fontes:**
- **Tamanho mínimo**: 10pt para texto em figuras
- **Fonte recomendada**: Times New Roman ou Arial
- **Consistência**: Mesma fonte em todas as figuras

### **Elementos:**
- **Legendas**: Sempre incluir quando necessário
- **Eixos**: Rotular claramente com unidades
- **Títulos**: Evitar títulos nas figuras (usar caption LaTeX)

## 📝 Integração com LaTeX

### **Comando Padrão:**
```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{figuras/tipo/nome-arquivo}
    \caption{Descrição clara e completa da figura}
    \label{fig:nome-descritivo}
\end{figure}
```

### **Exemplos de Uso:**
```latex
% Figura do capítulo 1
\includegraphics[width=0.9\textwidth]{figuras/capitulos/cap01-introducao/fig-cap01-01-arquitetura-hiperespectral}

% Diagrama
\includegraphics[width=\textwidth]{figuras/diagramas/diag-arquitetura-fpga-gpu}

% Gráfico
\includegraphics[width=0.7\textwidth]{figuras/graficos/graf-performance-comparativa}
```

### **Labels Recomendados:**
- `\label{fig:cap01-arquitetura}` - Figuras por capítulo
- `\label{fig:diag-fpga-gpu}` - Diagramas
- `\label{fig:graf-performance}` - Gráficos
- `\label{fig:esq-sistema}` - Esquemas
- `\label{tab:comparacao}` - Tabelas

## 🔧 Ferramentas Recomendadas

### **Criação de Figuras:**
- **Diagramas**: Draw.io, Lucidchart, Visio
- **Gráficos**: MATLAB, Python (matplotlib), R, Excel
- **Esquemas**: Inkscape, Adobe Illustrator
- **Edição**: GIMP, Photoshop

### **Conversão de Formatos:**
- **ImageMagick**: Conversão em lote
- **Inkscape**: SVG para PDF/EPS
- **GIMP**: Redimensionamento e otimização

## 📋 Checklist de Qualidade

### **Antes de Incluir uma Figura:**
- [ ] Formato adequado (PDF preferencial)
- [ ] Resolução suficiente (300 DPI mínimo)
- [ ] Nomenclatura seguindo padrão
- [ ] Localizada na pasta correta
- [ ] Texto legível (mínimo 10pt)
- [ ] Cores adequadas para impressão
- [ ] Elementos claramente identificados

### **No LaTeX:**
- [ ] Comando `\includegraphics` correto
- [ ] Caption descritiva e completa
- [ ] Label único e descritivo
- [ ] Referência no texto (`\autoref{fig:...}`)
- [ ] Posicionamento adequado (`[htbp]`)

## 📊 Tipos Específicos por Capítulo

### **Capítulo 1 - Introdução:**
- Arquiteturas de sistemas hiperespectrais
- Fluxo de processamento geral
- Comparações conceituais
- Diagramas de contexto

### **Capítulo 2 - Levantamento:**
- Comparações entre técnicas
- Taxonomias e classificações
- Gráficos de performance da literatura
- Tabelas comparativas

### **Capítulo 3 - Metodologia:**
- Fluxogramas metodológicos
- Diagramas de arquitetura proposta
- Esquemas de simulação
- Modelos matemáticos

### **Capítulo 4 - Resultados:**
- Gráficos de performance
- Comparações quantitativas
- Análises estatísticas
- Validações experimentais

### **Capítulo 5 - Conclusões:**
- Sínteses visuais
- Comparações finais
- Roadmaps futuros

## 🚀 Dicas de Produtividade

### **Organização:**
1. Criar figuras conforme escreve cada seção
2. Manter versões fonte (`.drawio`, `.psd`, `.ai`) separadas
3. Usar controle de versão para figuras importantes
4. Documentar fontes de dados para gráficos

### **Automação:**
1. Scripts para conversão em lote
2. Templates para gráficos recorrentes
3. Macros para formatação consistente
4. Backup automático das figuras

### **Colaboração:**
1. Compartilhar pasta figuras com orientador
2. Usar comentários em arquivos editáveis
3. Manter log de alterações importantes
4. Versionar figuras críticas

## ⚠️ Cuidados Especiais

### **Direitos Autorais:**
- Sempre citar fonte de figuras adaptadas
- Obter permissão para figuras de terceiros
- Criar figuras próprias sempre que possível
- Documentar origens de dados

### **Qualidade de Impressão:**
- Testar impressão em preto e branco
- Verificar legibilidade em diferentes tamanhos
- Evitar dependência excessiva de cores
- Usar padrões/texturas quando necessário

### **Consistência:**
- Manter estilo visual uniforme
- Usar mesma paleta de cores
- Padronizar tamanhos de fonte
- Alinhar elementos similares

---

**Última Atualização**: 2025-09-06
**Versão**: 1.0
**Autor**: Sistema de Organização de Dissertação UNICAMP-FT
