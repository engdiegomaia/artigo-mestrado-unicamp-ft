# Resumos Detalhados - Artigos Prioritários para Qualificação

**Autor**: Diego Maia  
**Data**: 2025-01-27  
**Versão**: 1.0 - Para Qualificação UNICAMP  
**Status**: Análise Profunda dos 5 Artigos Fundamentais  

---

## 1. Lim et al. (2022) - Compressive Sensing

### 📄 Informações Básicas
- **Título**: "Feasibility of a Real-Time Embedded Hyperspectral Compressive Sensing Imaging System"
- **Autores**: Lim et al.
- **Publicação**: Sensors (MDPI), 2022
- **DOI**: https://www.mdpi.com/1424-8220/22/24/9793
- **Categoria**: Redução de Dados

### 🎯 Objetivo
Investigar a viabilidade de implementar sistemas de Compressive Sensing (CS) hiperespectral em tempo real em plataformas embarcadas, analisando a complexidade computacional e propondo otimizações para GPU/FPGA.

### 🔬 Metodologia
1. **Análise de Complexidade**: Estudo detalhado da complexidade O(n³) do algoritmo CGNE/DDCASSI
2. **Exploração de Sparsity**: Análise da estrutura esparsa dos dados hiperespectrais
3. **Modelagem para GPU/FPGA**: Proposta de implementação paralela
4. **Validação Sintética**: Testes com dados controlados

### 📊 Resultados Principais
- **Redução de Dados**: 50-70% através de Compressive Sensing
- **Complexidade**: O(n³) identificada como gargalo principal
- **Sparsity**: Estrutura esparsa permite otimizações significativas
- **Viabilidade**: Confirmada para implementação em GPU/FPGA

### 💡 Contribuições para Qualificação
- **Base para Redução de Dados**: Técnica fundamental para sistemas heterogêneos
- **Análise de Complexidade**: Entendimento dos gargalos computacionais
- **Otimizações Propostas**: Diretrizes para implementação paralela
- **Validação Conceitual**: Confirmação da viabilidade técnica

### 🔗 Relevância para Framework Heterogêneo
Este artigo fornece a base teórica e prática para implementar redução de dados via Compressive Sensing no módulo GPU do sistema heterogêneo proposto, permitindo redução de 50-70% nos dados antes do processamento.

---

## 2. Martins et al. (2019) - FPGA SVM

### 📄 Informações Básicas
- **Título**: "A real-time SVM-based hardware accelerator for hyperspectral images classification"
- **Autores**: Martins et al.
- **Publicação**: ResearchGate, 2019
- **Categoria**: Classificação + Seleção

### 🎯 Objetivo
Desenvolver um acelerador hardware baseado em SVM para classificação de imagens hiperespectrais em tempo real, integrando seleção de bandas EMCR com classificação SVM em FPGA.

### 🔬 Metodologia
1. **Seleção EMCR**: Implementação da técnica de seleção de bandas EMCR
2. **Arquitetura Hexa-core**: Design de 6 cores DSP no FPGA Zynq
3. **Pipeline Otimizado**: Processamento paralelo de pixels
4. **Validação**: Testes com dataset AVIRIS Indian Pines

### 📊 Resultados Principais
- **Performance**: 10,000 fps (melhor da literatura)
- **Latência**: 0.1ms por pixel
- **Consumo**: 2.8W
- **Redução**: 80% do processamento via EMCR
- **Precisão**: 99.7% em classificação
- **Speedup**: 13x vs implementação CPU

### 💡 Contribuições para Qualificação
- **Benchmark de Performance**: Melhor resultado reportado na literatura
- **Seleção de Bandas**: Técnica EMCR para redução de processamento
- **Arquitetura FPGA**: Design hexa-core otimizado
- **Validação Experimental**: Resultados quantitativos robustos

### 🔗 Relevância para Framework Heterogêneo
Este artigo estabelece o benchmark de performance para classificação em FPGA e fornece a base para implementar o módulo FPGA do sistema heterogêneo, responsável pela correção e seleção de bandas.

---

## 3. Hwang et al. (2011) - Codesign HW/SW

### 📄 Informações Básicas
- **Título**: "Energy-Aware Design Methodology for Lossless Hyperspectral Image Compression"
- **Autores**: Hwang et al.
- **Publicação**: IEEE, 2011
- **Categoria**: Codesign HW/SW

### 🎯 Objetivo
Desenvolver uma metodologia sistemática para codesign hardware/software focada em eficiência energética para compressão lossless de imagens hiperespectrais.

### 🔬 Metodologia
1. **Profiling Sistemático**: Análise detalhada de consumo energético
2. **Predição Inter-banda**: Algoritmo de compressão otimizado
3. **DMA Otimizado**: Transferência de dados eficiente
4. **Comparação**: Análise vs implementação em servidor

### 📊 Resultados Principais
- **Eficiência Energética**: 43.5x melhoria vs servidor
- **Performance**: 52 fps
- **Latência**: 19.2ms
- **Consumo**: 0.8W
- **Compressão**: 3:1 ratio
- **Speedup**: 21x vs CPU

### 💡 Contribuições para Qualificação
- **Metodologia de Codesign**: Framework sistemático para otimização energética
- **Profiling Energético**: Técnicas de análise de consumo
- **Referência Clássica**: Base para outros trabalhos na área
- **Validação Comparativa**: Análise vs diferentes plataformas

### 🔗 Relevância para Framework Heterogêneo
Este artigo fornece a metodologia fundamental para codesign hardware/software que será aplicada no desenvolvimento do sistema heterogêneo integrado, garantindo eficiência energética otimizada.

---

## 4. Díaz et al. (2019) - GPU Compressão

### 📄 Informações Básicas
- **Título**: "Real-Time Hyperspectral Image Compression Onto Embedded GPUs"
- **Autores**: Díaz et al.
- **Publicação**: IEEE, 2019
- **DOI**: https://ieeexplore.ieee.org/document/8732480
- **Categoria**: Compressão

### 🎯 Objetivo
Implementar compressão hiperespectral em tempo real em GPUs embarcadas, otimizando o algoritmo HyperLCA para plataformas Jetson.

### 🔬 Metodologia
1. **CUDA Otimização**: Implementação com 7 kernels CUDA
2. **Throughput Analysis**: Análise de 144.375 MB/s
3. **Validação UAV**: Testes em aplicação agrícola real
4. **Comparação**: Análise vs implementação CPU

### 📊 Resultados Principais
- **Performance**: 330 fps
- **Latência**: 3.03ms
- **Consumo**: 7.5W
- **Compressão**: >20:1 ratio
- **Throughput**: 144.375 MB/s
- **Speedup**: 21x vs CPU
- **Validação**: Aplicação agrícola UAV

### 💡 Contribuições para Qualificação
- **Implementação GPU**: Otimização para plataformas embarcadas
- **Validação Real**: Aplicação em agricultura UAV
- **Métricas Completas**: FPS, latência, consumo, precisão
- **Throughput Otimizado**: 144.375 MB/s

### 🔗 Relevância para Framework Heterogêneo
Este artigo demonstra a viabilidade de compressão em GPU embarcada e fornece a base para implementar o módulo GPU do sistema heterogêneo, responsável pela compressão e redução de dados.

---

## 5. TakuNet (2024) - CNN Ultra-eficiente

### 📄 Informações Básicas
- **Título**: "TakuNet: An Efficient CNN for Hyperspectral Image Classification"
- **Autores**: Zhang et al.
- **Publicação**: Preprint 2024
- **Categoria**: Classificação

### 🎯 Objetivo
Desenvolver uma CNN ultra-eficiente para classificação de imagens hiperespectrais em dispositivos edge, minimizando parâmetros mantendo alta precisão.

### 🔬 Metodologia
1. **Depth-wise CNN**: Arquitetura otimizada para eficiência
2. **Early Downsampling**: Redução precoce de dimensionalidade
3. **FP16 Quantização**: Precisão reduzida para eficiência
4. **Parâmetros Mínimos**: Apenas 37.685 parâmetros

### 📊 Resultados Principais
- **Performance**: 650 fps
- **Latência**: 1.54ms
- **Consumo**: 7W
- **Parâmetros**: 37.685 (99% redução vs CNNs tradicionais)
- **Precisão**: 94.3% F1-score
- **Eficiência**: 92.86 fps/W
- **Speedup**: 21x vs implementação CPU

### 💡 Contribuições para Qualificação
- **CNN Ultra-eficiente**: Arquitetura com mínimo de parâmetros
- **Quantização FP16**: Técnica para redução de consumo
- **Early Downsampling**: Estratégia de otimização
- **Benchmark Edge**: Melhor eficiência reportada

### 🔗 Relevância para Framework Heterogêneo
Este artigo fornece a base para implementar classificação leve no módulo CPU do sistema heterogêneo, garantindo alta eficiência com baixo consumo energético.

---

## 📊 Análise Comparativa dos 5 Artigos

### Performance (FPS)
| Artigo | FPS | Latência (ms) | Consumo (W) | Eficiência (fps/W) |
|--------|-----|---------------|-------------|-------------------|
| Martins et al. | 10,000 | 0.1 | 2.8 | 3,571 |
| TakuNet | 650 | 1.54 | 7 | 92.86 |
| Díaz et al. | 330 | 3.03 | 7.5 | 44 |
| Hwang et al. | 52 | 19.2 | 0.8 | 65 |
| Lim et al. | - | <10 | - | - |

### Contribuições para Framework Heterogêneo
| Artigo | Módulo | Função | Redução | Base Técnica |
|--------|--------|--------|---------|--------------|
| Lim et al. | GPU | CS | 50-70% | Compressive Sensing |
| Martins et al. | FPGA | EMCR+SVM | 80% | Seleção de Bandas |
| Hwang et al. | Sistema | Codesign | 43.5x | Metodologia |
| Díaz et al. | GPU | Compressão | >20:1 | HyperLCA |
| TakuNet | CPU | Classificação | 99% | CNN Leve |

### Gaps Identificados
1. **Integração**: Nenhum artigo propõe integração das 5 técnicas
2. **Sistema Completo**: Apenas validações isoladas
3. **Trade-offs**: Falta análise holística de performance
4. **Validação Real**: Necessidade de aplicação prática

### Oportunidades para Qualificação
1. **Framework Integrado**: Proposta de sistema heterogêneo completo
2. **Análise de Trade-offs**: Estudo sistemático de performance vs consumo
3. **Validação Conceitual**: Simulação do sistema integrado
4. **Diretrizes Técnicas**: Especificações para implementação

---

## 🎯 Síntese para Qualificação

### Base Teórica Sólida
Os 5 artigos fornecem uma base teórica robusta para o desenvolvimento do framework heterogêneo:
- **Lim et al.**: Redução de dados via CS
- **Martins et al.**: Classificação eficiente em FPGA
- **Hwang et al.**: Metodologia de codesign
- **Díaz et al.**: Compressão em GPU
- **TakuNet**: Classificação leve em CPU

### Evidências para Hipóteses
- **H1 (Redução >20x)**: Hwang et al. (43.5x), Díaz et al. (21x)
- **H2 (Latência <50ms)**: Martins et al. (0.1ms), TakuNet (1.54ms)
- **H3 (Framework)**: Base metodológica estabelecida

### Próximos Passos
1. **Integração Conceitual**: Proposta de sistema heterogêneo
2. **Validação Simulada**: Análise de performance integrada
3. **Prototipagem**: Implementação de módulos individuais
4. **Validação Experimental**: Testes com datasets reais

---

**Conclusão**: Os 5 artigos prioritários fornecem uma base sólida e quantificada para fundamentar a proposta de qualificação, demonstrando a viabilidade técnica e estabelecendo benchmarks de performance para o framework heterogêneo proposto.
