# Dissertação de Mestrado - UNICAMP FT
## Classificação LULC usando Imagens Hiperespectrais de Drones

[![made-with-latex](https://img.shields.io/badge/Made%20with-LaTeX-1f425f.svg)](https://www.latex-project.org/) ![Organized](https://img.shields.io/badge/Structure-Organized-brightgreen) ![Apache license](https://img.shields.io/badge/license-Apache%202.0-blue) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity) 

**Autor**: Diego Maia  
**Email**: maia.df11@gmail.com  
**GitHub**: [@maia-diego](https://github.com/maia-diego)  
**Instituição**: Faculdade de Tecnologia (FT) - UNICAMP  

## 📊 Status Atual do Projeto

**Etapa Atual**: ✅ **Projeto Completamente Reorganizado**  
**Última Atualização**: 2024-12-19  
**Progresso Geral**: 70% (Estrutura principal completa + Projeto organizado)

### 🎯 Próximos Passos Imediatos:
- Testar compilação com nova estrutura
- Finalizar capítulos de **Resultados** e **Discussão**
- Implementar experimentos práticos com dados reais
- Validação da metodologia proposta

## 🔬 Contexto da Pesquisa

### Área de Pesquisa:
- **Sensoriamento Remoto Hiperespectral**
- **Classificação de Uso e Cobertura da Terra (LULC)**
- **Agricultura de Precisão com Drones/VANTs**
- **Processamento de Imagens e Machine Learning**

### Problema de Pesquisa:
Como melhorar a acurácia da classificação LULC utilizando imagens hiperespectrais coletadas por drones, aplicando técnicas avançadas de processamento e algoritmos de deep learning.

### Hipóteses Principais:
- **H1**: Algoritmos de deep learning superam métodos tradicionais para classificação de imagens hiperespectrais
- **H2**: Correções radiométricas adequadas melhoram significativamente a acurácia da classificação
- **H3**: Redução de dimensionalidade preserva informação relevante mantendo eficiência computacional

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
│   ├── metodologia.tex             # Capítulo: Metodologia
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

### 📊 Descobertas da Revisão Bibliográfica Incorporadas
- **3 gerações** de métodos LULC identificadas
- **Deep learning supera** métodos tradicionais em cenários complexos  
- **Empirical Line Method** com 5-55% melhoria na reflectância
- **4 lacunas principais** na literatura atual
- **Correlações 0.97-0.99** alcançadas em estudos de validação

### 🎯 Próxima Evolução (v2.0 - Etapa 2)
- Expansão do capítulo teórico (20-25 páginas)
- Integração completa dos 14 artigos analisados
- Reestruturação em 6 seções conforme esboço criado
- Incorporação de template UNICAMP-FT oficial

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

## 🎯 Objetivos e Metas

### Objetivo Geral:
Desenvolver e validar uma metodologia para classificação de uso e cobertura da terra (LULC) utilizando imagens hiperespectrais coletadas por drones, com foco em aplicações de agricultura de precisão.

### Objetivos Específicos:
1. Avaliar diferentes algoritmos de classificação (tradicionais vs. deep learning)
2. Otimizar pipeline de pré-processamento para imagens hiperespectrais de drones
3. Comparar eficácia de técnicas de redução de dimensionalidade
4. Validar metodologia em cenário real de agricultura
5. Contribuir para estado da arte em sensoriamento remoto hiperespectral

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

**Última atualização**: 2024-12-17  
**Próxima revisão prevista**: Ao completar Etapa 2 (Reestruturação Teórica)
