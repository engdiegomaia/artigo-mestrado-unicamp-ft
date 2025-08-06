# Dissertação de Mestrado - UNICAMP FT
## Estudo sobre estratégias para Otimização computacional visando eficiência energética e Latência no Processamento Hiperespectral Embarcado

[![made-with-latex](https://img.shields.io/badge/Made%20with-LaTeX-1f425f.svg)](https://www.latex-project.org/) ![Organized](https://img.shields.io/badge/Structure-Organized-brightgreen) ![Apache license](https://img.shields.io/badge/license-Apache%202.0-blue) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) 

**Autor**: Diego Maia  
**Email**: maia.df11@gmail.com  
**GitHub**: [@maia-diego](https://github.com/maia-diego)  
**Instituição**: Faculdade de Tecnologia (FT) - UNICAMP  

## 📊 Status Atual do Projeto

**Etapa Atual**: ✅ **Projeto Reconstruído do Zero - Base Teórica Completa**  
**Última Atualização**: 2025-01-03  
**Progresso Geral**: 40% (Estrutura teórica completa + Metodologia definida)

### 🎯 Próximos Passos Imediatos:
- Iniciar implementação dos módulos especializados (FPGA/GPU/CPU)
- Configurar ambiente de desenvolvimento heterogêneo
- Implementar profiling sistemático para baseline
- Desenvolver módulo FPGA de pré-processamento

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
│   ├── figuras/                    # Figuras e diagramas
│   └── logotipos/                  # Logos institucionais
│
├── 📁 documentos/                  # 📚 DOCUMENTAÇÃO E RELATÓRIOS
│   ├── README.md                   # Documentação principal (cópia)
│   ├── CHANGELOG.md                # Histórico de mudanças
│   ├── DicasUteisTextosAcademicos.md # Dicas de escrita
│   ├── relatorio-etapa1.pdf        # Relatório da Etapa 1
│   ├── relatorio-etapa1.md         # Versão markdown do relatório
│   ├── esboco-estado-da-arte.md    # Esboço do estado da arte
│   ├── matriz-temas-artigos.md     # Matriz temática dos artigos
│   ├── fichamento-artigos-prioritarios.md # Fichamentos detalhados
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

### 📄 Conteúdo da Nova Dissertação
- **Título**: Estudo sobre estratégias para Otimização computacional visando eficiência energética e Latência no Processamento Hiperespectral Embarcado
- **Foco**: Sistema Heterogêneo CPU+GPU+FPGA com Pipeline Especializado
- **Estrutura**: 7 capítulos + bibliografia com 20 referências da revisão sistemática
- **Base Teórica**: Análise de 20 artigos científicos com técnicas comprovadas

### 🔍 Principais Contribuições da Nova Versão
1. **Arquitetura heterogênea completa** integrando CPU+GPU+FPGA
2. **Framework de codesign sistemático** baseado em profiling detalhado
3. **Integração de técnicas comprovadas**: Compressive sensing, EMCR, ELM, CNNs 3D
4. **Metodologia experimental robusta** com validação em aplicações práticas
5. **Metas quantitativas definidas**: 3x redução consumo, 4x redução latência, 6.7x aumento throughput
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

## 🎯 Plano de Execução (8 Etapas)

| Etapa | Título | Duração | Status | Entregáveis Principais |
|-------|--------|---------|--------|----------------------|
| **1** | Revisão e Organização da Bibliografia | 1 semana | ✅ **Concluída** | Banco bibliográfico, fichamento, gaps identificados |
| **2** | Reestruturação do Levantamento Teórico | 1 semana | 🔄 **Próxima** | Capítulo teórico atualizado |
| **3** | Definição da Metodologia | 1 semana | ⏳ Pendente | Metodologia detalhada, fluxogramas |
| **4** | Desenvolvimento Experimental | 2 semanas | ⏳ Pendente | Código implementado, experimentos |
| **5** | Análise dos Resultados | 1 semana | ⏳ Pendente | Análises estatísticas, validação |
| **6** | Redação dos Capítulos Principais | 2 semanas | ⏳ Pendente | Introdução, metodologia, resultados |
| **7** | Conclusões e Finalização | 1 semana | ⏳ Pendente | Conclusões, trabalhos futuros |
| **8** | Revisão e Ajustes Finais | 1 semana | ⏳ Pendente | Dissertação final para submissão |

**Estimativa Total**: 10 semanas

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
