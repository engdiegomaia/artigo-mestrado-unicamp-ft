# Esboço do Estado da Arte - Levantamento Teórico

## Introdução

A agricultura de precisão tem se beneficiado significativamente dos avanços em sensoriamento remoto hiperespectral, especialmente com o uso de drones. Esta tecnologia permite a aquisição de dados espectrais detalhados para classificação precisa do uso e cobertura da terra (LULC).

## 1. Fundamentos do Sensoriamento Remoto Hiperespectral

### 1.1 Princípios Básicos
O sensoriamento remoto hiperespectral baseia-se na aquisição de imagens em centenas de bandas espectrais estreitas e contíguas. Sistemas como o AVIRIS estabeleceram os fundamentos técnicos, operando com 614 amostras, 512 linhas e 224 bandas espectrais.

### 1.2 Processamento e Correções
- **Correção Atmosférica**: ACORN (Atmospheric CORrection Now)
- **Correção Radiométrica**: Calibração radiância para reflectância
- **Correção Geométrica**: Georreferenciamento preciso

## 2. Classificação LULC com Imagens Hiperespectrais

### 2.1 Estado da Arte (Lou et al., 2024)
Três gerações de métodos:
1. **Métodos Tradicionais**: Estatísticas clássicas, PCA
2. **Machine Learning**: SVM, Random Forest, k-NN  
3. **Deep Learning**: CNN, LSTM, arquiteturas híbridas

### 2.2 Desempenho Comparativo
Deep learning supera métodos tradicionais em:
- Grandes volumes de dados
- Heterogeneidade espectral complexa
- Classificação multi-escala
- Variabilidade temporal

## 3. Sistemas Hiperespectrais com Drones

### 3.1 Vantagens
- Flexibilidade temporal
- Alta resolução espacial  
- Redução de interferência atmosférica
- Custo-efetividade

### 3.2 Desafios
- Distorções radiométricas e geométricas
- Limitações de payload
- Processamento em tempo real

## 4. Métodos de Correção (Shin et al., 2024)

### 4.1 Correção Radiométrica - ELM
- Melhoria de 5-55% na reflectância
- Correlações de 0.97-0.99
- Painéis de referência espectral

### 4.2 Pipeline de Processamento
1. Pré-processamento inicial
2. Correção radiométrica (ELM)
3. Correção geométrica (GCPs)
4. Filtragem espectral  
5. Redução de dimensionalidade

## 5. Aplicações em Agricultura

- Detecção de estresse hídrico
- Monitoramento nutricional
- Detecção de pragas/doenças
- Estimativa de produtividade
- Classificação de cobertura

## 6. Lacunas e Oportunidades

### Limitações Identificadas
- Falta de metodologias integradas
- Poucos estudos comparativos sistemáticos
- Validação limitada em condições brasileiras
- Necessidade de otimização para tempo real

### Oportunidades de Pesquisa
- Pipeline completo desde aquisição até classificação
- Deep learning especializado para drones
- Validação experimental comparativa
- Adaptação para agricultura brasileira 