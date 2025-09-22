# Cronograma de Execução da Dissertação - 10 Meses

## Visão Geral
- **Duração Total**: 10 meses (40 semanas)
- **Estrutura**: 6 fases principais
- **Foco**: Aquisição de hardware + Implementação + Publicação + Defesa

## Cronograma Detalhado

### 📦 Fase 1: Aquisição e Setup de Hardware (8 semanas)
**Meses 1-2 | Semanas 1-8**

#### Semanas 1-3: Aquisição de Hardware
- Especificação técnica detalhada
- Cotação e aquisição das plataformas:
  - FPGA Xilinx Zynq-7020 (ZedBoard)
  - NVIDIA Jetson Xavier NX Developer Kit
  - Instrumentação energética (INA219, multímetros)
  - Componentes auxiliares

#### Semanas 4-6: Setup dos Ambientes
- Instalação e configuração:
  - Vivado Design Suite 2023.2
  - GHDL 3.0 para simulação VHDL
  - CUDA Toolkit 12.0, cuDNN 8.9
  - Ferramentas de profiling (NSight)
- Validação de funcionalidade básica

#### Semanas 7-8: Testes Preliminares
- Compilação de exemplos básicos
- Validação da instrumentação energética
- Configuração do dataset Salinas Valley
- Documentação do ambiente experimental

---

### ⚡ Fase 2: Implementação FPGA (6 semanas)
**Mês 3 + início Mês 4 | Semanas 9-14**

#### Semanas 9-10: Pipeline de Pré-processamento
- Correção radiométrica em VHDL
- Filtragem espacial (Gaussiano e mediano)
- Seleção de bandas espectrais
- Otimização de recursos DSP48E1 e BRAM

#### Semanas 11-12: Redução Dimensional
- Implementação PCA em ponto fixo
- Algoritmo EMCR para seleção de características
- Análise de trade-offs precisão vs recursos
- Paralelização de operações matriciais

#### Semanas 13-14: Classificação e Integração
- Classificadores SVM/k-NN otimizados
- Cálculo de índices de vegetação (NDVI, NDRE, EVI, SAVI)
- Integração completa do pipeline FPGA
- Caracterização inicial de performance

---

### 🚀 Fase 3: Implementação GPU (6 semanas)
**Mês 4-5 | Semanas 15-20**

#### Semanas 15-16: Kernels de Pré-processamento
- Kernels CUDA otimizados para Volta
- Exploração de shared memory e coalescing
- Implementação OpenCL para comparação

#### Semanas 17-18: Redução Dimensional GPU
- PCA/KPCA com cuBLAS otimizado
- Análise de occupancy para throughput máximo
- Kernel PCA com RBF otimizado

#### Semanas 19-20: Classificação e Integração
- Classificadores com TensorRT
- Kernels customizados para algoritmos específicos
- Integração completa do pipeline GPU

---

### 🔬 Fase 4: Validação Experimental (6 semanas)
**Mês 5-6 | Semanas 21-26**

#### Semanas 21-23: Coleta de Dados
- Testes exaustivos com dataset Salinas Valley
- Métricas de performance (throughput, latência)
- Eficiência energética (GOPS/W, J/pixel)
- Qualidade de classificação (OA, Kappa, F1-score)

#### Semanas 24-26: Análise Estatística
- Análise estatística comparativa rigorosa
- Testes de significância (t-test, ANOVA)
- Análise de Pareto multi-objetivo
- Modelos matemáticos de performance

---

### 📄 Fase 5: Síntese e Publicação (6 semanas)
**Mês 6-7 | Semanas 27-32**

#### Semanas 27-29: Síntese de Resultados
- Proposição da arquitetura heterogênea otimizada
- Especificação arquitetural detalhada
- Interfaces e protocolos de comunicação
- Validação teórica dos modelos

#### Semanas 30-32: Publicação Científica
- Redação de artigo científico
- Submissão para conferência/periódico de impacto:
  - IEEE Transactions on Computers
  - ACM Computing Surveys
  - Conferências: IPDPS, HPCA
- Estabelecimento de visibilidade científica

---

### 🎓 Fase 6: Escrita da Dissertação e Defesa (12 semanas)
**Mês 8-10 | Semanas 33-40**

#### Semanas 33-36: Redação da Dissertação
- Capítulos de resultados e discussão
- Integração de dados experimentais
- Análises estatísticas e síntese arquitetural
- Narrativa coerente e tecnicamente rigorosa

#### Semanas 37-38: Revisão e Formatação
- Revisão completa da dissertação
- Formatação conforme normas ABNT e UNICAMP-FT
- Preparação de figuras e tabelas de alta qualidade
- Revisão bibliográfica final

#### Semanas 39-40: Preparação da Defesa
- Elaboração da apresentação
- Simulação de defesa com orientador
- Preparação de material suplementar
- Submissão da versão final para a banca

---

## Marcos Importantes

| Semana | Marco | Entregável |
|--------|-------|------------|
| 8 | Hardware Adquirido | Ambiente experimental completo |
| 14 | FPGA Implementado | Pipeline FPGA funcional |
| 20 | GPU Implementado | Pipeline GPU funcional |
| 26 | Validação Concluída | Resultados experimentais completos |
| 32 | Artigo Submetido | Publicação científica |
| 36 | Dissertação Redigida | Versão preliminar completa |
| 40 | Defesa Realizada | Mestrado concluído |

## Recursos Necessários

### Hardware
- FPGA Xilinx Zynq-7020 (~$500-800)
- NVIDIA Jetson Xavier NX (~$400-600)
- Instrumentação energética (~$100-200)
- Componentes auxiliares (~$200-300)

### Software
- Vivado Design Suite (licença acadêmica)
- CUDA Toolkit (gratuito)
- Ferramentas de desenvolvimento (gratuitas/acadêmicas)

### Humanos
- 1 mestrando (40h/semana)
- 1 orientador (supervisão semanal)
- Acesso a laboratório de pesquisa

## Riscos e Mitigações

### Principais Riscos
1. **Atraso na aquisição de hardware** → Início antecipado do processo
2. **Problemas de compatibilidade** → Testes extensivos na Fase 1
3. **Complexidade de implementação** → Prototipagem incremental
4. **Resultados experimentais insuficientes** → Validação contínua

### Estratégias de Mitigação
- Buffer de tempo entre fases críticas
- Validação contínua de resultados
- Comunicação regular com orientador
- Documentação detalhada de todo o processo
