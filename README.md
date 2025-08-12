# Dissertação de Mestrado - UNICAMP FT
## Estudo sobre estratégias para Otimização computacional visando eficiência energética e Latência no Processamento Hiperespectral Embarcado

[![made-with-latex](https://img.shields.io/badge/Made%20with-LaTeX-1f425f.svg)](https://www.latex-project.org/) ![Organized](https://img.shields.io/badge/Structure-Organized-brightgreen) ![Apache license](https://img.shields.io/badge/license-Apache%202.0-blue) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) 

**Autor**: Diego Maia  
**Email**: maia.df11@gmail.com  
**GitHub**: [@maia-diego](https://github.com/maia-diego)  
**Instituição**: Faculdade de Tecnologia (FT) - UNICAMP  

## 📊 Status Atual do Projeto

**Etapa Atual**: ✅ **Etapa 1: Fundamentação Teórica e Estado da Arte**  
**Última Atualização**: 2025-08-12  
**Progresso Geral**: 30% (Catalogação sistemática concluída)

### 🎯 Próximos Passos Imediatos (Etapa 1):
- ✅ **CONCLUÍDO**: Catalogação sistemática de 25 artigos com métricas quantitativas
- ✅ **CONCLUÍDO**: Implementação da fase de qualificação UNICAMP no cronograma
- ✅ **CONCLUÍDO**: Redução da Etapa 1 de 5 para 4 meses
- Completar revisão sistemática da literatura (85% concluída)
- Finalizar análise de técnicas de otimização (60% concluída)
- Desenvolver caracterização de sistemas heterogêneos (40% concluída)
- Estabelecer framework conceitual e metodologia (20% concluída)
- Preparar documentação para qualificação UNICAMP (Dezembro 2025)

## 🔬 Contexto da Pesquisa

### Área de Pesquisa:
- **Processamento Hiperespectral Embarcado**
- **Sistemas Heterogêneos (CPU+GPU+FPGA)**
- **Codesign Hardware/Software para Otimização Energética**
- **Aplicações em Tempo Real: Agricultura de Precisão, UAVs, Monitoramento**

### Estruturação da Pesquisa em Duas Etapas:

**Etapa 1 - Mestrado (2025)**: Validação de metodologias de integração de sistemas heterogêneos, focando na análise do estado da arte, caracterização de trade-offs e desenvolvimento de framework conceitual.

**Etapa 2 - Doutorado (2026-2029)**: Proposição e implementação de arquitetura otimizada integrada, baseada nas validações e diretrizes estabelecidas na Etapa 1.

### Problema de Pesquisa da Etapa 1:
Como validar e quantificar o potencial de integração de técnicas comprovadas de otimização em sistemas heterogêneos para processamento hiperespectral embarcado, estabelecendo metodologias e frameworks conceituais para orientar futuras implementações práticas.

### 📊 Principais Descobertas da Catalogação Sistemática (25 artigos):

**Gaps Identificados:**
- **96% dos trabalhos** focam em técnicas isoladas (apenas 1 sistema completo UAV)
- **88% reportam métricas parciais** (apenas 3 trabalhos com FPS+latência+consumo+precisão)
- **80% validação sintética** (apenas 2 validações em campo real)

**Oportunidades Mapeadas:**
- **Redução combinada**: 90-95% (EMCR 80% + CS 50-70%)
- **Eficiência energética**: FPGA + GPU + CPU pode atingir <15W
- **Throughput integrado**: >100 fps com precisão >95%
- **Speedup típico**: 18-21x vs CPU baseline

**Configuração Ótima Identificada:**
1. **FPGA** (Zynq UltraScale+): Correção + Seleção EMCR (80% redução, <5ms, <5W)
2. **GPU** (Jetson Orin): CS/PCA (50-70% redução adicional, <10ms, <10W)  
3. **CPU** (ARM Cortex-A78): Classificação leve (CNN/SVM, <5ms, <5W)

### Hipóteses Principais da Etapa 1:
- **H1**: A análise sistemática de técnicas comprovadas pode demonstrar, através de simulações e protótipos conceituais, o potencial teórico de redução energética superior a 20x em sistemas hiperespectrais embarcados
- **H2**: É possível estabelecer, através de modelagem e validação conceitual, que um framework arquitetural heterogêneo pode teoricamente atingir metas de latência <50ms/frame mantendo precisão >95%
- **H3**: Uma metodologia sistemática de avaliação pode identificar e quantificar os trade-offs fundamentais entre precisão, consumo e latência, estabelecendo um framework de decisão para a Etapa 2

## 📁 Nova Estrutura Organizacional do Projeto

```
artigo-mestrado-unicamp-ft/
├── 📄 compila.sh                   # Script de compilação principal
├── 📄 README.md                    # Documentação do projeto
├── 📄 .gitignore                   # Arquivos ignorados pelo Git
├── 📄 LICENSE.txt                  # Licença do projeto
├── 📄 CITATION.cff                 # Informações de citação
│
├── 📁 src/                         # 📝 ARQUIVOS LATEX PRINCIPAIS
│   ├── tese.tex                    # Documento principal
│   ├── introducao.tex              # Capítulo: Introdução
│   ├── levantamento.tex            # Capítulo: Estado da Arte
│   ├── desenvolvimento.tex         # Capítulo: Metodologia
│   ├── resultados.tex              # Capítulo: Resultados
│   ├── discussao.tex               # Capítulo: Discussão
│   ├── conclusoes.tex              # Capítulo: Conclusões
│   ├── agradecimentos.tex          # Agradecimentos
│   ├── apendices.tex               # Apêndices
│   ├── listaSimbolos.tex           # Lista de símbolos
│   ├── bibliografia.bib            # Bibliografia principal
│   ├── tese-FT.cls                 # Classe LaTeX UNICAMP-FT
│   ├── figuras/                    # → Link para ../assets/figuras/
│   └── logotipos/                  # → Link para ../assets/logotipos/
│
├── 📁 compilacao/                  # 🔧 ARQUIVOS TEMPORÁRIOS DE COMPILAÇÃO
│   ├── *.aux                       # Arquivos auxiliares LaTeX
│   ├── *.log                       # Logs de compilação
│   ├── *.bcf, *.bbl               # Arquivos de bibliografia
│   ├── *.out, *.toc               # Índices e links
│   └── *.nlo, *.nls               # Lista de símbolos
│
├── 📁 dist/                        # 📖 DOCUMENTOS FINAIS
│   └── tese.pdf                    # PDF final da dissertação
│
├── 📁 assets/                      # 🖼️ RECURSOS VISUAIS
│   ├── figuras/                    # Figuras e diagramas (legado)
│   ├── logotipos/                  # Logos institucionais
│   └── imagens_artigo/             # 🎨 IMAGENS ORGANIZADAS DO ARTIGO
│       ├── cronogramas/            # Gráficos de cronograma
│       ├── diagramas_arquitetura/  # Diagramas do sistema
│       ├── graficos_performance/   # Gráficos de performance
│       ├── resultados_experimentais/ # Resultados experimentais
│       ├── imagens_hiperespectrais/ # Dados hiperespectrais
│       └── logos_institucionais/   # Logos organizados
│
├── 📁 documentos/                  # 📚 DOCUMENTAÇÃO E RELATÓRIOS
│   ├── README.md                   # Documentação principal (cópia)
│   ├── CHANGELOG.md                # Histórico de mudanças
│   ├── DicasUteisTextosAcademicos.md # Dicas de escrita
│   ├── qualificacao-unicamp.md     # 📋 Documento para qualificação UNICAMP
│   ├── resumo-executivo-qualificacao.md # 📊 Resumo das mudanças implementadas
│   ├── relatorio-etapa1.pdf        # Relatório da Etapa 1
│   ├── relatorio-etapa1.md         # Versão markdown do relatório
│   ├── esboco-estado-da-arte.md    # Esboço do estado da arte
│   ├── matriz-temas-artigos.md     # Matriz temática dos artigos
│   ├── fichamento-artigos-prioritarios.md # Fichamentos detalhados
│   ├── catalogacao-sistematica-tecnicas-metricas.md # 📊 Catalogação sistemática de 25 artigos com métricas quantitativas
│   └── bibliografia-organizada.bib # Bibliografia organizada
│
├── 📁 referencias/                 # 📖 MATERIAL DE REFERÊNCIA
│   ├── templates_unicamp/          # Templates oficiais UNICAMP-FT
│   ├── meus_trabalhos/            # Trabalhos anteriores (estilo)
│   └── levantamento_teorico/      # Base teórica e artigos
│
├── 📁 config/                      # ⚙️ CONFIGURAÇÕES
│   ├── .cursor/                    # Regras do editor Cursor
│   ├── compila.sh                  # Script original de compilação
│   └── _config.yml                 # Configurações do projeto
│
├── 📁 dissertacao-versoes/         # 📚 VERSÕES DA DISSERTAÇÃO
│   └── v1.0-etapa1/               # Primeira versão completa
│
└── 📁 etapas/                      # 📋 PLANO DE EXECUÇÃO
    ├── 00-plano-geral.md
    ├── 01-revisao-bibliografia.md
    ├── 02-reestruturacao-teorico.md
    ├── 03-definicao-metodologia.md
    ├── 04-desenvolvimento-experimental.md
    ├── 05-analise-resultados.md
    ├── 06-redacao-capitulos.md
    ├── 07-conclusoes-finalizacao.md
    └── 08-revisao-ajustes-finais.md
```

## 🎓 Dissertação v2.0 - Reconstrução Completa

**Localização**: `src/`  
**Status**: ✅ **Base Teórica Completa** - Pronta para implementação  
**Data**: 2025-01-03  

### 📄 Conteúdo da Dissertação (Estrutura Simplificada)
- **Título**: Estudo sobre estratégias para Otimização computacional visando eficiência energética e Latência no Processamento Hiperespectral Embarcado
- **Foco**: Validação metodológica para integração de sistemas heterogêneos
- **Estrutura**: 5 capítulos diretos + bibliografia com 20 referências da revisão sistemática
- **Base Teórica**: Análise sistemática, modelagem conceitual e protótipos de prova de conceito

### 🔍 Principais Contribuições da Estrutura Simplificada
1. **Framework arquitetural conceitual** para sistemas heterogêneos integrados
2. **Metodologia de validação sistemática** baseada em simulação e protótipos
3. **Análise quantitativa de trade-offs**: Compressive sensing, EMCR, codesign HW/SW
4. **Protocolos de avaliação** para sistemas heterogêneos embarcados
5. **Diretrizes técnicas** para implementação da arquitetura otimizada na Etapa 2
6. **Base bibliográfica sólida** com 20 artigos sistematicamente analisados

### 📊 Técnicas Integradas da Revisão Bibliográfica
- **Compressive Sensing** (Lim et al.): 50-70% redução de dados
- **Seleção EMCR** (Martins et al.): 80% redução processamento, 99.7% precisão
- **Codesign HW/SW** (Hwang et al.): 43.5x melhoria energética
- **GPU Embarcadas** (Díaz et al.): 330 fps em Jetson TX2
- **CNNs Ultra-eficientes** (TakuNet): 37.685 parâmetros, >650 fps

### 🎯 Próximos Passos (Implementação)
- Configuração ambiente heterogêneo (FPGA + GPU + CPU)
- Implementação módulo FPGA (ELM + EMCR + CS encoder)
- Desenvolvimento pipeline GPU (CGNE + CNNs 3D)
- Integração sistema completo com balanceamento dinâmico

## 🎯 Plano de Execução (4 Etapas Principais + Qualificação)

| Etapa | Título | Duração | Status | Entregáveis Principais |
|-------|--------|---------|--------|----------------------|
| **1** | Fundamentação Teórica e Estado da Arte | 4 meses | 🔄 **Em Andamento** | Framework conceitual, metodologia de validação |
| **Q** | **Fase de Qualificação UNICAMP** | **1 mês** | ⏳ **Pendente** | **Documentação para qualificação, apresentação** |
| **2** | Desenvolvimento Experimental e Validação | 5 meses | ⏳ Pendente | Protótipos implementados, dados experimentais |
| **3** | Análise de Resultados e Redação | 4 meses | ⏳ Pendente | Capítulos da dissertação, análise estatística |
| **4** | Finalização e Preparação para Defesa | 1.5 meses | ⏳ Pendente | Dissertação final, apresentação de defesa |

**Duração Total**: 14 meses (Agosto 2025 - Setembro 2026)
**Qualificação UNICAMP**: Janeiro 2026

### 🎓 Fase de Qualificação UNICAMP (Dezembro 2025 - Janeiro 2026)

**Objetivo**: Apresentação e aprovação da qualificação perante banca examinadora da UNICAMP-FT.

**Componentes da Qualificação**:
- **Q1: Preparação para Qualificação** (2 semanas): Finalização da documentação e preparação da apresentação
- **Q2: Qualificação UNICAMP** (1 semana): Apresentação formal perante banca examinadora
- **Q3: Ajustes Pós-Qualificação** (1 semana): Implementação de sugestões e correções da banca

**Entregáveis para Qualificação**:
- Documento de qualificação com fundamentação teórica completa
- Apresentação formal (slides) com metodologia e cronograma
- Framework conceitual validado e metodologia de validação
- Cronograma detalhado para desenvolvimento experimental

**Cronograma da Qualificação**:
- **Início**: 10 de Dezembro 2025
- **Apresentação**: 30 de Dezembro 2025
- **Ajustes**: 9 de Janeiro 2026
- **Início Etapa 2**: 10 de Janeiro 2026

### 📊 Progresso Detalhado da Etapa 1:
- **1.1 Revisão Sistemática da Literatura**: 80% concluída
- **1.2 Análise de Técnicas de Otimização**: 40% concluída  
- **1.3 Caracterização de Sistemas Heterogêneos**: 20% concluída
- **1.4 Framework Conceitual e Metodologia**: 0% concluída

## 📅 Cronograma Detalhado

### 🎯 Milestones Principais:
- **M1: Framework Conceitual Completo** (Dezembro 2025): Conclusão da fundamentação teórica
- **M2: Qualificação UNICAMP** (Janeiro 2026): Apresentação e aprovação da qualificação
- **M3: Protótipos Validados** (Junho 2026): Validação experimental das técnicas
- **M4: Dissertação Completa** (Outubro 2026): Documento final redigido
- **M5: Defesa** (Setembro 2026): Apresentação e defesa da dissertação

### 📈 Visualização do Cronograma:
- **Arquivo HTML**: `cronograma_mestrado_gantt.html` - Visualização interativa com D3.js
- **Seção na Dissertação**: Capítulo 3 (Metodologia) - Seção "Cronograma de Execução"
- **Controle**: Monitoramento semanal com orientador e revisões mensais

### 🔄 Sistema de Controle:
- **Reuniões Semanais**: Acompanhamento do progresso das tarefas
- **Revisões Mensais**: Avaliação geral e ajustes no cronograma
- **Contingências**: Buffer de 2 semanas por etapa para imprevistos

## 📚 Bibliografia Principal

### Documento Base:
- `250526_levatamento_teorico_v3.pdf` - Levantamento teórico inicial (467KB, 5119 linhas)

### Artigos de Referência Prioritários:
- **Land use land cover LULC classification using hyperspectral images a review.pdf** (8.7MB)
- **AVIRIS_for_Dummies.pdf** (121KB, 1019 linhas)
- **Robust Radiometric and Geometric Correction Methods for Drone-Based Hyperspectral Imaging.pdf** (6.3MB)
- **remotesensing-12-03338-v2.pdf** (3.6MB)
- **remotesensing-14-04579-v2.pdf** (5.4MB)
- **sensors-22-09793-v3.pdf** (583KB, 5678 linhas)

### Trabalhos de Referência de Estilo:
- `admin,+BJD+115+Dezembro.pdf` - Publicação acadêmica
- `projeto_final.pdf` - Projeto final (944KB, 7317 linhas)
- `plano-de-gerenciamento-de-config.pdf` - Documentação técnica
- `instrumentovirtualecgwavelet.pdf` - Implementação técnica

## ⚙️ Configuração e Desenvolvimento

### Template Base:
Este projeto utiliza o **Template UNICAMP-FT** adaptado para dissertações de mestrado, seguindo as normas institucionais (Instrução Normativa CPG 002/2021).

### Regras de Desenvolvimento Ativas:
- **Gestão de README**: Leitura obrigatória antes de tarefas + atualização após conclusão
- **Estilo de Escrita**: Baseado nos trabalhos anteriores do autor (`meus_trabalhos/`)
- **Padrões UNICAMP-FT**: Formatação e estrutura institucional (`templates_unicamp/`)
- **Commits**: Padrão conventional (feat, fix, docs, refactor)
- **Contexto Contínuo**: Preservação da memória do projeto entre sessões

### Compilação:
```bash
# Compilação completa (incluindo bibliografia)
./compila.sh tese.tex

# Ambiente recomendado: TeXLive completo + Python 3.8+
```

## 📈 Histórico de Mudanças Recentes

### 2025-08-12:
- ✅ **Implementação da Fase de Qualificação UNICAMP** - Adicionada fase completa de qualificação (Dezembro 2025 - Janeiro 2026) com 3 subfases: preparação, qualificação e ajustes pós-qualificação.
- ✅ **Redução da Etapa 1 de 5 para 4 meses** - Cronograma ajustado para acomodar a fase de qualificação, mantendo a duração total de 14 meses.
- ✅ **Atualização do Script de Cronograma** - Versão 3.0 do script gantt_chart.py com suporte à fase de qualificação e novos milestones.
- ✅ **5 Milestones Principais** - Reorganização dos milestones incluindo M2: Qualificação UNICAMP (Janeiro 2026).
- ✅ **Cronograma Visual Atualizado** - Gantt Chart HTML e PNG atualizados com nova estrutura incluindo qualificação.
- ✅ **Documentação Completa** - README atualizado com seção específica sobre qualificação e cronograma detalhado.

### 2025-08-06:
- ✅ **Fundamentação de Sistemas Heterogêneos Aprofundada** - Adicionado estudo de caso industrial.
- ✅ **Análise da SightLine Applications** - Integrada ao capítulo de metodologia como exemplo prático de arquitetura heterogênea (CPU, GPU, DSP, NPU).
- ✅ **Validação com Fontes Primárias** - O SoC Qualcomm QCS8250, utilizado pela SightLine, foi confirmado através de documentação da Lantronix.
- ✅ **Bibliografia Expandida** - Adicionada referência técnica do System-on-Module da Lantronix para embasar o estudo de caso.
- ✅ **Conexão Teoria-Prática Reforçada** - O novo texto serve como ponte entre o framework arquitetural conceitual e as implementações do mundo real.


### 2025-08-05:
- ✅ **Cronograma detalhado atualizado** - Gantt Chart com 14 meses (Agosto 2025 - Setembro 2026)
- ✅ **4 etapas principais definidas** - Fundamentação Teórica, Desenvolvimento Experimental, Análise/Redação, Finalização
- ✅ **12 tarefas detalhadas** - Cronograma granular com dependências e milestones
- ✅ **Seção de cronograma na dissertação** - Adicionada ao capítulo de metodologia
- ✅ **Visualização interativa** - Gráfico Gantt HTML com progresso em tempo real
- ✅ **Milestones críticos** - 4 pontos de verificação importantes (M1-M4)
- ✅ **Controle e acompanhamento** - Sistema de monitoramento semanal e mensal
- ✅ **Estrutura de imagens organizada** - Nova organização em `assets/imagens_artigo/` com 6 categorias
- ✅ **Script de Gantt atualizado** - Versão 2.2 com fontes maiores e novo caminho de saída
- ✅ **Integração com compilação** - Script de compilação atualizado para copiar imagens organizadas

### 2025-01-03:
- ✅ **Reconstrução completa do projeto do zero** - Nova base teórica baseada na revisão de 20 artigos
- ✅ **Arquitetura heterogênea definida** - Sistema CPU+GPU+FPGA com pipeline especializado
- ✅ **Introdução reescrita** - Contextualização sobre sistemas heterogêneos e codesign HW/SW
- ✅ **Levantamento bibliográfico completo** - Análise sistemática de 20 artigos com categorização por relevância
- ✅ **Metodologia detalhada** - 4 fases de desenvolvimento com implementações específicas
- ✅ **Bibliografia atualizada** - 20 referências organizadas por relevância com notas técnicas
- ✅ **Estrutura LaTeX completa** - 7 capítulos com seções preparadas para implementação
- ✅ **Metas quantitativas estabelecidas** - Targets específicos de performance, consumo e latência
- ✅ **Conformidade UNICAMP-FT corrigida** - Documento ajustado para usar classe oficial tese-FT.cls
- ✅ **Comandos institucionais implementados** - Capa, folha de aprovação e elementos pré-textuais conforme padrão
- ✅ **Sistema de bibliografia atualizado** - Compatibilidade com biblatex e estilo ABNT da instituição

### 2024-12-19: 
- ✅ **Reestruturação completa da dissertação** - Reescrita focada no tema correto
- ✅ **Título atualizado** - "Classificação de Uso e Cobertura da Terra usando Imagens Hiperespectrais de Drones"
- ✅ **Introdução reescrita** - Contextualização adequada sobre LULC e drones hiperespectrais
- ✅ **Levantamento bibliográfico expandido** - 6 seções abrangentes sobre estado da arte
- ✅ **Metodologia reformulada** - Pipeline completo para classificação LULC com deep learning
- ✅ **Bibliografia atualizada** - Inclusão de artigos de referência dos treinados
- ✅ **Resumo/Abstract atualizados** - Alinhamento com novo foco da pesquisa
- ✅ **Consistência temática** - Eliminação de desconexões entre README e dissertação

### 2024-12-17:
- ✅ **Etapa 1 concluída** - Revisão e Organização da Bibliografia
- ✅ **14 artigos analisados** e catalogados no banco bibliográfico
- ✅ **4 artigos prioritários** com fichamento detalhado
- ✅ **Matriz temática** criada organizando artigos por 6 categorias
- ✅ **Gaps na literatura** identificados e documentados
- ✅ **Esboço do estado da arte** estruturado em 6 seções
- ✅ **Relatório da Etapa 1** gerado em PDF (relatorio-etapa1.pdf)
- ✅ **Base teórica sólida** estabelecida para próximas etapas
- ✅ **Dissertação v1.0 criada** - Primeira versão completa (16 páginas, 188KB PDF)
- ✅ **Estrutura completa** com 6 capítulos, resumo/abstract, bibliografia organizada
- ✅ **Compilação bem-sucedida** usando LaTeX padrão (classe report)

### 2024-12-16:
- ✅ **Criado plano detalhado de 8 etapas** para escrita da dissertação
- ✅ **Configurado .gitignore** para pastas de referência (`templates_unicamp/`, `levantamento_teorico/`, `meus_trabalhos/`)
- ✅ **Estabelecidas regras de estilo** baseadas em trabalhos anteriores
- ✅ **Definidos padrões UNICAMP-FT** para formatação
- ✅ **Repositório enviado para GitHub** com sucesso
- ✅ **README atualizado** com contexto específico do projeto
- ✅ **Criada regra de gestão de README** para manutenção contínua do contexto

### Configurações Implementadas:
- **Regra de Gestão de README**: Atualização automática do contexto a cada tarefa
- **Regras Cursor**: Manutenção de contexto e estilo de escrita
- **Estrutura de etapas**: Pasta `etapas/` com 8 etapas detalhadas
- **Bibliografia organizada**: Artigos categorizados por temática
- **Templates de referência**: Padrões UNICAMP-FT e exemplos institucionais

## 🎯 Objetivos e Metas da Etapa 1 (Mestrado)

### Objetivo Geral da Etapa 1:
Validar e quantificar o potencial de integração de técnicas comprovadas de otimização em sistemas heterogêneos para processamento hiperespectral embarcado, gerando análises detalhadas do estado da arte e estabelecendo metodologias de avaliação para orientar futuras implementações.

### Objetivos Específicos da Etapa 1:
1. **Realizar análise sistemática** do estado da arte em processamento hiperespectral embarcado, catalogando técnicas comprovadas
2. **Caracterizar quantitativamente** os trade-offs através de simulações e protótipos conceituais
3. **Desenvolver metodologia de avaliação** para sistemas heterogêneos, estabelecendo métricas e benchmarks
4. **Validar conceitos fundamentais** através de implementações de prova de conceito das técnicas mais promissoras
5. **Propor framework arquitetural** para integração sistemática, definindo especificações para a Etapa 2
6. **Estabelecer baseline experimental** para quantificar potencial de melhoria e orientar desenvolvimento futuro

### Metas da Etapa 1:
- **Validação Conceitual**: Demonstrar potencial teórico de redução energética >20x através de modelagem
- **Framework Metodológico**: Estabelecer protocolos de avaliação para sistemas heterogêneos
- **Diretrizes Técnicas**: Definir especificações arquiteturais para implementação na Etapa 2
- **Baseline Quantitativo**: Caracterizar trade-offs precisão vs consumo vs latência com datasets padrão

### Objetivos da Etapa 2 (Doutorado - 2026-2029):
- **Implementação Prática**: Desenvolver arquitetura heterogênea completa CPU+GPU+FPGA
- **Otimização Avançada**: Algoritmos adaptativos de qualidade vs recursos com gestão inteligente de energia
- **Validação Real**: Aplicações práticas em agricultura de precisão, monitoramento ambiental e industrial
- **Metas Quantitativas**: Performance >30 fps, consumo <15W, latência <40ms, precisão >95%

## 🔗 Links Úteis

- **Template Overleaf**: [Template UNICAMP-FT](https://pt.overleaf.com/latex/templates/template-para-teses-e-dissertacoes-na-ft-slash-unicamp/rhznqbkjvpcr)
- **Repositório GitHub**: [artigo-mestrado-unicamp-ft](https://github.com/maia-diego/artigo-mestrado-unicamp-ft)
- **CTAN (pacotes LaTeX)**: https://ctan.org
- **Normas UNICAMP**: Instrução Normativa CPG 002/2021

## 🎓 Dissertação v1.0 - Primeira Versão Completa

**Localização**: `dissertacao-versoes/v1.0-etapa1/`  
**Status**: ✅ **Compilada com sucesso** (16 páginas, 188KB)  
**Data**: 2024-12-17  

### 📄 Conteúdo da Dissertação
- **Título**: Classificação de Uso e Cobertura da Terra (LULC) usando Imagens Hiperespectrais de Drones
- **Subtítulo**: Uma Abordagem Baseada em Deep Learning para Agricultura de Precisão
- **Páginas**: 16 (capa + 6 capítulos + bibliografia + apêndices)
- **Bibliografia**: 14 referências organizadas e catalogadas

### 🔍 Principais Contribuições desta Versão
1. **Estrutura acadêmica completa** seguindo padrões UNICAMP-FT
2. **Fundamentação teórica sólida** baseada na Etapa 1
3. **3 hipóteses claramente formuladas** com base na literatura
4. **Lacunas científicas identificadas** e justificativa robusta
5. **Pipeline metodológico** integrado (aquisição → classificação)
6. **Resumo/Abstract** bilíngue profissional

### 🎯 Próxima Evolução (v2.0 - Etapa 2)
- Expansão do capítulo teórico (20-25 páginas)
- Integração completa dos 14 artigos analisados
- Reestruturação em 6 seções conforme esboço criado
- Incorporação de template UNICAMP-FT oficial

---

**Última atualização**: 2025-01-03  
**Próxima revisão prevista**: Ao completar Etapa 2 (Reestruturação Teórica)
