# Qualificação UNICAMP - Dissertação de Mestrado

**Autor**: Diego Maia  
**Email**: maia.df11@gmail.com  
**Instituição**: Faculdade de Tecnologia (FT) - UNICAMP  
**Data da Qualificação**: 30 de Dezembro 2025  
**Orientador**: [Nome do Orientador]  

## 📋 Informações Gerais

### Título da Dissertação
**Estudo sobre estratégias para Otimização computacional visando eficiência energética e Latência no Processamento Hiperespectral Embarcado**

### Área de Pesquisa
- **Processamento Hiperespectral Embarcado**
- **Sistemas Heterogêneos (CPU+GPU+FPGA)**
- **Codesign Hardware/Software para Otimização Energética**
- **Aplicações em Tempo Real: Agricultura de Precisão, UAVs, Monitoramento**

## 🎯 Objetivos da Qualificação

### Objetivo Geral
Validar e quantificar o potencial de integração de técnicas comprovadas de otimização em sistemas heterogêneos para processamento hiperespectral embarcado, gerando análises detalhadas do estado da arte e estabelecendo metodologias de avaliação para orientar futuras implementações.

### Objetivos Específicos
1. **Realizar análise sistemática** do estado da arte em processamento hiperespectral embarcado, catalogando técnicas comprovadas
2. **Caracterizar quantitativamente** os trade-offs através de simulações e protótipos conceituais
3. **Desenvolver metodologia de avaliação** para sistemas heterogêneos, estabelecendo métricas e benchmarks
4. **Validar conceitos fundamentais** através de implementações de prova de conceito das técnicas mais promissoras
5. **Propor framework arquitetural** para integração sistemática, definindo especificações para a Etapa 2
6. **Estabelecer baseline experimental** para quantificar potencial de melhoria e orientar desenvolvimento futuro

## 📊 Fundamentação Teórica

### Estado da Arte - Principais Descobertas

**Catalogação Sistemática de 25 Artigos:**

**Gaps Identificados:**
- **96% dos trabalhos** focam em técnicas isoladas (apenas 1 sistema completo UAV)
- **88% reportam métricas parciais** (apenas 3 trabalhos com FPS+latência+consumo+precisão)
- **80% validação sintética** (apenas 2 validações em campo real)

**Oportunidades Mapeadas:**
- **Redução combinada**: 90-95% (EMCR 80% + CS 50-70%)
- **Eficiência energética**: FPGA + GPU + CPU pode atingir <15W
- **Throughput integrado**: >100 fps com precisão >95%
- **Speedup típico**: 18-21x vs CPU baseline

### Técnicas Integradas da Revisão Bibliográfica
- **Compressive Sensing** (Lim et al.): 50-70% redução de dados
- **Seleção EMCR** (Martins et al.): 80% redução processamento, 99.7% precisão
- **Codesign HW/SW** (Hwang et al.): 43.5x melhoria energética
- **GPU Embarcadas** (Díaz et al.): 330 fps em Jetson TX2
- **CNNs Ultra-eficientes** (TakuNet): 37.685 parâmetros, >650 fps

### Configuração Ótima Identificada
1. **FPGA** (Zynq UltraScale+): Correção + Seleção EMCR (80% redução, <5ms, <5W)
2. **GPU** (Jetson Orin): CS/PCA (50-70% redução adicional, <10ms, <10W)  
3. **CPU** (ARM Cortex-A78): Classificação leve (CNN/SVM, <5ms, <5W)

## 🔬 Metodologia Proposta

### Framework Arquitetural Conceitual
**Sistema Heterogêneo Integrado:**
- **Pipeline Especializado**: Cada componente otimizado para sua função específica
- **Balanceamento Dinâmico**: Adaptação automática baseada em carga e recursos
- **Gestão Inteligente de Energia**: Controle adaptativo de consumo vs performance

### Metodologia de Validação
**4 Fases de Desenvolvimento:**

1. **Fase 1: Análise e Modelagem** (Concluída)
   - Revisão sistemática da literatura
   - Caracterização de técnicas de otimização
   - Framework conceitual

2. **Fase 2: Implementação Experimental** (Pós-qualificação)
   - Configuração ambiente heterogêneo
   - Implementação módulos especializados
   - Validação experimental

3. **Fase 3: Análise e Otimização** (Pós-qualificação)
   - Análise de performance
   - Otimização de parâmetros
   - Validação com datasets reais

4. **Fase 4: Documentação e Conclusões** (Pós-qualificação)
   - Redação da dissertação
   - Análise de resultados
   - Diretrizes para implementação

## 📅 Cronograma Detalhado

### Etapa 1: Fundamentação Teórica (Agosto - Dezembro 2025) ✅
- **1.1 Revisão Sistemática**: 85% concluída
- **1.2 Análise de Técnicas**: 60% concluída
- **1.3 Caracterização de Sistemas**: 40% concluída
- **1.4 Framework Conceitual**: 20% concluída

### Fase de Qualificação (Dezembro 2025 - Janeiro 2026) 🔄
- **Q1: Preparação**: 10-24 Dezembro 2025
- **Q2: Qualificação**: 30 Dezembro 2025
- **Q3: Ajustes**: 2-9 Janeiro 2026

### Etapa 2: Desenvolvimento Experimental (Janeiro - Junho 2026) ⏳
- **2.1 Configuração Ambiente**: Janeiro 2026
- **2.2 Implementação Protótipos**: Fevereiro-Abril 2026
- **2.3 Validação Experimental**: Maio-Junho 2026

### Etapa 3: Análise e Redação (Junho - Outubro 2026) ⏳
- **3.1 Análise Estatística**: Junho 2026
- **3.2 Redação Capítulos**: Julho-Setembro 2026
- **3.3 Discussão e Conclusões**: Outubro 2026

### Etapa 4: Finalização (Outubro - Setembro 2026) ⏳
- **4.1 Revisão Final**: Outubro 2026
- **4.2 Preparação Apresentação**: Novembro 2026
- **4.3 Defesa**: Setembro 2026

## 🎯 Hipóteses de Pesquisa

### Hipóteses Principais
- **H1**: A análise sistemática de técnicas comprovadas pode demonstrar, através de simulações e protótipos conceituais, o potencial teórico de redução energética superior a 20x em sistemas hiperespectrais embarcados
- **H2**: É possível estabelecer, através de modelagem e validação conceitual, que um framework arquitetural heterogêneo pode teoricamente atingir metas de latência <50ms/frame mantendo precisão >95%
- **H3**: Uma metodologia sistemática de avaliação pode identificar e quantificar os trade-offs fundamentais entre precisão, consumo e latência, estabelecendo um framework de decisão para a Etapa 2

## 📈 Metas Quantitativas

### Metas da Etapa 1 (Validação Conceitual)
- **Validação Conceitual**: Demonstrar potencial teórico de redução energética >20x através de modelagem
- **Framework Metodológico**: Estabelecer protocolos de avaliação para sistemas heterogêneos
- **Diretrizes Técnicas**: Definir especificações arquiteturais para implementação na Etapa 2
- **Baseline Quantitativo**: Caracterizar trade-offs precisão vs consumo vs latência com datasets padrão

### Metas da Etapa 2 (Pós-qualificação)
- **Performance**: >30 fps em tempo real
- **Consumo Energético**: <15W total do sistema
- **Latência**: <40ms por frame
- **Precisão**: >95% em classificação hiperespectral

## 📚 Bibliografia Principal

### Artigos de Referência (20 artigos sistematicamente analisados)
1. **Lim et al.** - Compressive Sensing para redução de dados (50-70%)
2. **Martins et al.** - Seleção EMCR para otimização (80% redução, 99.7% precisão)
3. **Hwang et al.** - Codesign HW/SW (43.5x melhoria energética)
4. **Díaz et al.** - GPU embarcadas (330 fps Jetson TX2)
5. **TakuNet** - CNNs ultra-eficientes (37.685 parâmetros, >650 fps)

### Documentação Técnica
- **SightLine Applications**: Estudo de caso industrial com SoC Qualcomm QCS8250
- **Lantronix System-on-Module**: Documentação técnica para validação de arquiteturas heterogêneas

## 🎓 Contribuições Esperadas

### Contribuições da Etapa 1
1. **Framework arquitetural conceitual** para sistemas heterogêneos integrados
2. **Metodologia de validação sistemática** baseada em simulação e protótipos
3. **Análise quantitativa de trade-offs**: Compressive sensing, EMCR, codesign HW/SW
4. **Protocolos de avaliação** para sistemas heterogêneos embarcados
5. **Diretrizes técnicas** para implementação da arquitetura otimizada na Etapa 2
6. **Base bibliográfica sólida** com 20 artigos sistematicamente analisados

### Contribuições Futuras (Etapa 2 - Doutorado)
- **Implementação Prática**: Desenvolver arquitetura heterogênea completa CPU+GPU+FPGA
- **Otimização Avançada**: Algoritmos adaptativos de qualidade vs recursos com gestão inteligente de energia
- **Validação Real**: Aplicações práticas em agricultura de precisão, monitoramento ambiental e industrial

## 📋 Entregáveis para Qualificação

### Documentos Obrigatórios
1. **Documento de Qualificação** (este documento)
2. **Apresentação Formal** (slides para apresentação)
3. **Cronograma Detalhado** (Gantt Chart atualizado)
4. **Bibliografia Organizada** (20 artigos principais)

### Apresentação
- **Duração**: 30 minutos de apresentação + 30 minutos de discussão
- **Estrutura**: 
  - Introdução e contexto (5 min)
  - Estado da arte e fundamentação teórica (10 min)
  - Metodologia e framework conceitual (10 min)
  - Cronograma e próximos passos (5 min)

## 🔗 Links e Referências

- **Repositório do Projeto**: [GitHub - artigo-mestrado-unicamp-ft](https://github.com/maia-diego/artigo-mestrado-unicamp-ft)
- **Cronograma Interativo**: `cronograma_mestrado_gantt.html`
- **Documentação Completa**: `README.md`
- **Template UNICAMP-FT**: [Overleaf Template](https://pt.overleaf.com/latex/templates/template-para-teses-e-dissertacoes-na-ft-slash-unicamp/rhznqbkjvpcr)

---

**Data de Criação**: 12 de Agosto de 2025  
**Última Atualização**: 12 de Agosto de 2025  
**Versão**: 1.0 - Documento para Qualificação UNICAMP
