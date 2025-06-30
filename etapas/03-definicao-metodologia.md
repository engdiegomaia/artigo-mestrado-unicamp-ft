# Etapa 3: Definição da Metodologia

**Duração**: 1 semana  
**Objetivo**: Especificar detalhadamente a metodologia de pesquisa, algoritmos e procedimentos experimentais

## Pré-requisitos
- ✅ Etapa 2 concluída
- ✅ Gaps na literatura identificados
- ✅ Levantamento teórico atualizado
- ✅ Justificativa da contribuição definida

## Tarefas Específicas

### 3.1 Definição do Problema de Pesquisa (Dia 1)

#### Formulação da Questão de Pesquisa:
- **Pergunta principal**: Como melhorar a classificação LULC usando imagens hiperespectrais de drones?
- **Perguntas específicas**:
  - Quais algoritmos de classificação são mais eficazes?
  - Como otimizar o pré-processamento das imagens?
  - Qual a acurácia comparativa com métodos tradicionais?

#### Definição de Hipóteses:
- **H1**: Algoritmos de deep learning superam métodos tradicionais
- **H2**: Correções radiométricas melhoram significativamente a classificação
- **H3**: Redução de dimensionalidade preserva informação relevante

#### Criar arquivo: `problema-pesquisa.md`

### 3.2 Especificação dos Dados (Dia 2)

#### Descrição do Dataset:
- **Fonte dos dados**: Imagens hiperespectrais coletadas por drone
- **Área de estudo**: [Definir localização específica]
- **Período de coleta**: [Definir cronograma]
- **Resolução espacial**: [Especificar]
- **Resolução espectral**: [Número de bandas]

#### Características das Imagens:
- **Formato**: ENVI, GeoTIFF, ou similar
- **Georeferenciamento**: Sistema de coordenadas
- **Condições de aquisição**: Altura de voo, condições climáticas
- **Calibração**: Procedimentos de calibração radiométrica

#### Classes de LULC:
1. **Agricultura**:
   - Culturas anuais (milho, soja, trigo)
   - Culturas perenes (frutíferas)
   - Pastagens

2. **Vegetação Natural**:
   - Floresta nativa
   - Cerrado
   - Vegetação ripária

3. **Outros Usos**:
   - Área urbana
   - Solo exposto
   - Corpos d'água

### 3.3 Metodologia de Pré-processamento (Dia 3)

#### Pipeline de Processamento:

1. **Correção Radiométrica**:
   - Correção de dark current
   - Correção de flat field
   - Conversão para reflectância
   - **Referência**: Robust Radiometric and Geometric Correction Methods.pdf

2. **Correção Geométrica**:
   - Ortorretificação
   - Registro de imagens
   - Reprojeção cartográfica

3. **Correção Atmosférica**:
   - Método FLAASH ou ATCOR
   - Remoção de espalhamento
   - Correção de absorção

4. **Filtros de Ruído**:
   - Filtros espaciais (mediana, Gaussian)
   - Filtros espectrais (Savitzky-Golay)
   - Remoção de bandas ruidosas

#### Algoritmos Específicos:
- **Linguagem**: Python com bibliotecas spectral, scikit-learn
- **Ferramentas**: ENVI, QGIS, GDAL
- **Hardware**: Especificações mínimas necessárias

### 3.4 Algoritmos de Classificação (Dia 4)

#### Métodos Tradicionais (Baseline):
1. **Support Vector Machine (SVM)**:
   - Kernel RBF
   - Otimização de hiperparâmetros
   - Validação cruzada

2. **Random Forest**:
   - Número de árvores: 100-500
   - Profundidade máxima otimizada
   - Importância das features

3. **Maximum Likelihood**:
   - Assumindo distribuição normal
   - Matriz de covariância

#### Métodos Avançados (Contribuição):
1. **Convolutional Neural Networks (CNN)**:
   - Arquitetura 1D para dados espectrais
   - Arquitetura 2D-3D para dados espaciais-espectrais
   - Transfer learning

2. **Recurrent Neural Networks (RNN/LSTM)**:
   - Para sequências espectrais
   - Memória de longo prazo

3. **Ensemble Methods**:
   - Combinação de classificadores
   - Voting classifiers
   - Stacking

#### Redução de Dimensionalidade:
- **Principal Component Analysis (PCA)**
- **Independent Component Analysis (ICA)**
- **Minimum Noise Fraction (MNF)**
- **Linear Discriminant Analysis (LDA)**

### 3.5 Planejamento Experimental (Dia 5)

#### Delineamento Experimental:
1. **Divisão dos Dados**:
   - Treinamento: 70%
   - Validação: 15%
   - Teste: 15%

2. **Estratégia de Amostragem**:
   - Estratificada por classe
   - Espacialmente representativa
   - Temporalmente distribuída

3. **Validação**:
   - K-fold cross-validation (k=10)
   - Leave-one-out para dados limitados
   - Validação temporal se aplicável

#### Métricas de Avaliação:
- **Acurácia global**
- **Precisão e recall por classe**
- **F1-score**
- **Kappa de Cohen**
- **Matriz de confusão**
- **Tempo de processamento**

### 3.6 Implementação e Ferramentas (Dias 6-7)

#### Dia 6: Especificação Técnica
**Ambiente de Desenvolvimento**:
- **Python 3.8+** com Anaconda
- **Bibliotecas principais**:
  - spectral, scikit-learn, tensorflow/pytorch
  - gdal, rasterio, geopandas
  - matplotlib, seaborn para visualização

**Hardware Necessário**:
- **RAM**: Mínimo 16GB (recomendado 32GB)
- **GPU**: NVIDIA com CUDA para deep learning
- **Storage**: SSD para processamento rápido

#### Dia 7: Cronograma de Implementação
**Cronograma de Desenvolvimento**:
- Semana 1: Configuração do ambiente
- Semana 2: Implementação do pré-processamento
- Semana 3: Implementação dos classificadores
- Semana 4: Testes e validação
- Semana 5: Otimização e comparação

## Entregáveis da Etapa 3

### 1. Documento de Metodologia
- Arquivo: `metodologia-detalhada.tex`
- Extensão: 15-20 páginas
- Formatação UNICAMP-FT

### 2. Fluxograma Metodológico
- Diagrama completo do pipeline
- Formato vetorial (SVG/PDF)
- Integrado ao documento LaTeX

### 3. Especificação de Dados
- Arquivo: `especificacao-dados.md`
- Descrição detalhada do dataset
- Protocolos de coleta

### 4. Código de Implementação
- Repositório Git com estrutura definida
- Documentação dos algoritmos
- Scripts de pré-processamento

### 5. Cronograma Experimental
- Arquivo: `cronograma-experimentos.xlsx`
- Marcos e entregas
- Alocação de recursos

## Critérios de Conclusão da Etapa

✅ Metodologia completamente especificada  
✅ Algoritmos de classificação definidos  
✅ Pipeline de pré-processamento detalhado  
✅ Métricas de avaliação estabelecidas  
✅ Cronograma experimental criado  
✅ Ambiente de desenvolvimento configurado  

## Validação da Metodologia

### Checklist de Qualidade:
- [ ] Metodologia é reproduzível?
- [ ] Algoritmos são apropriados para o problema?
- [ ] Métricas de avaliação são adequadas?
- [ ] Cronograma é realista?
- [ ] Recursos necessários estão disponíveis?

### Revisão por Pares:
- Apresentar metodologia para colegas/orientador
- Incorporar feedback recebido
- Ajustar aspectos problemáticos

## Próximos Passos
Preparação para **Etapa 4**: Desenvolvimento Experimental - implementação prática da metodologia definida. 