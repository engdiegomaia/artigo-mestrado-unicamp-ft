# Fichamento dos Artigos Prioritários - Etapa 1

## 1. AVIRIS for Dummies: Understanding Hyperspectral Remote Sensing

**Autor**: Dr. Sylvio Mannel  
**Tipo**: Guia Técnico  
**Ano**: 2020  
**Instituição**: NASA JPL  

### Resumo
Guia técnico prático para processamento de dados AVIRIS. Foca na superação das dificuldades iniciais com parâmetros técnicos específicos (614 samples, 512 lines, 224 bands) e metodologias de correção atmosférica usando ACORN.

### Contribuições Principais
- Parâmetros técnicos validados para AVIRIS
- Workflow de correção atmosférica (ACORN modo 1 e 2)
- Configurações RGB recomendadas para visualização
- Metodologia de calibração espectral

### Relevância: Alta - Fundamentos técnicos essenciais

---

## 2. Land Use/Land Cover Classification Using Hyperspectral Images: A Review

**Autores**: Chen Lou, Mohammed A. A. Al-qaness, et al.  
**Journal**: Geo-spatial Information Science  
**Ano**: 2024  
**DOI**: 10.1080/10095020.2024.2332638  

### Resumo  
Revisão abrangente sobre classificação LULC usando imagens hiperespectrais. Analisa métodos tradicionais e modernos (machine learning, deep learning), identifica tendências atuais e desafios na área.

### Contribuições Principais
- Síntese do estado da arte em classificação LULC
- Análise comparativa de diferentes abordagens
- Identificação de tendências emergentes (deep learning)
- Direções futuras de pesquisa

### Relevância: Muito Alta - Mapeia estado da arte da área específica

---

## 3. Feasibility of Real-Time Embedded Hyperspectral Compressive Sensing

**Autores**: Olivier Lim, Stéphane Mancini, Mauro Dalla Mura  
**Journal**: Sensors  
**Ano**: 2022  
**DOI**: 10.3390/s22249793  

### Resumo
Estudo sobre viabilidade de sistemas hiperespectrais compressivos em tempo real. Explora aquisições compressivas que permitem amostragem com menos aquisições que técnicas clássicas.

### Contribuições Principais
- Demonstração de viabilidade de sistemas embarcados
- Redução significativa de dados sem perda de qualidade  
- Aplicabilidade em agricultura e sensoriamento remoto
- Avanços em processamento tempo real

### Relevância: Média-Alta - Otimização para sistemas de drones

---

## 4. Robust Radiometric and Geometric Correction Methods for Drone-Based Hyperspectral Imaging

**Autores**: Hyoung-Sub Shin, Seung-Hwan Go, Jong-Hwa Park  
**Journal**: Korean Journal of Remote Sensing  
**Ano**: 2024  
**DOI**: 10.7780/kjrs.2024.40.3.2  

### Resumo
Métodos robustos de correção radiométrica e geométrica para imageamento hiperespectral com drones em aplicações agrícolas. Aborda distorções no pré-processamento de dados de drones.

### Contribuições Principais
- **Empirical Line Method (ELM)**: Melhoria de 5-55% na reflectância
- **Correção geométrica**: Transformação rubber sheet com pontos de controle
- **Validação robusta**: Correlações de 0.97-0.99
- **Perfil espectral uniforme** através das bandas

### Relevância: Muito Alta - Aplicação direta ao projeto

---

## Síntese dos Gaps Identificados

### Limitações dos Métodos Atuais
1. **Adaptação para drones**: Métodos como ACORN focam em sensores aerotransportados
2. **Validação comparativa limitada**: Poucos estudos comparam sistematicamente métodos tradicionais vs deep learning
3. **Processamento tempo real**: Limitações computacionais para implementação embarcada
4. **Especificidade agrícola**: Falta metodologias otimizadas para agricultura de precisão

### Oportunidades de Pesquisa
1. **Pipeline integrado**: Metodologia completa desde aquisição até classificação
2. **Deep learning**: Exploração de CNN/LSTM para classificação LULC com drones
3. **Validação experimental**: Estudos comparativos em cenários reais
4. **Otimização agrícola**: Métodos específicos para condições brasileiras

### Principais Resultados/Contribuições
- Metodologia simplificada para iniciantes em AVIRIS
- Parâmetros técnicos validados para abertura de imagens
- Workflow de correção atmosférica com ACORN modo 1 e 2
- Recomendações para calibração espectral usando alvos brilhantes

### Palavras-chave
AVIRIS, sensoriamento remoto hiperespectral, correção atmosférica, ACORN, georreferenciamento, calibração espectral

### Relevância para a Pesquisa
**Alta** - Fornece fundamentos técnicos essenciais para processamento de dados hiperespectrais, especialmente correção atmosférica e parâmetros de configuração.

### Limitações Identificadas
- Foca apenas em dados AVIRIS de baixa resolução (20m)
- Baseado em versões antigas do ENVI (3.4/3.5)
- Limitado a correções básicas

### Conexões com Outros Artigos
Complementa os artigos sobre correções radiométricas em drones e serve como base técnica para os métodos de classificação LULC.

---

## 2. Land Use/Land Cover (LULC) Classification Using Hyperspectral Images: A Review

**Autores**: Chen Lou, Mohammed A. A. Al-qaness, Dalal AL-Alimi, et al.  
**Journal**: Geo-spatial Information Science  
**Ano**: 2024  
**DOI**: 10.1080/10095020.2024.2332638  

### Resumo
Revisão abrangente sobre classificação de uso e cobertura da terra usando imagens hiperespectrais. O artigo analisa métodos tradicionais e modernos, incluindo machine learning e deep learning, para classificação LULC. Identifica tendências atuais e desafios na área.

### Metodologia Abordada
- **Revisão sistemática** de métodos de classificação LULC
- **Comparação de algoritmos**: tradicionais vs. machine learning vs. deep learning
- **Análise de datasets** hiperespectrais comumente utilizados
- **Métricas de avaliação** para classificação LULC

### Principais Resultados/Contribuições
- Síntese do estado da arte em classificação LULC hiperespectral
- Identificação de tendências emergentes (deep learning)
- Análise comparativa de diferentes abordagens
- Direções futuras de pesquisa identificadas

### Palavras-chave
Land use land cover, LULC classification, hyperspectral images, remote sensing, machine learning, deep learning

### Relevância para a Pesquisa
**Muito Alta** - Artigo de revisão fundamental que mapeia o estado da arte e tendências na área específica da pesquisa.

### Limitações Identificadas
- Possível falta de foco em aplicações específicas de agricultura
- Limitações dos métodos tradicionais não totalmente exploradas
- Necessidade de mais estudos comparativos práticos

### Conexões com Outros Artigos
Artigo central que conecta todos os outros, fornecendo contexto teórico amplo para as aplicações específicas de drones e correções radiométricas.

---

## 3. Feasibility of a Real-Time Embedded Hyperspectral Compressive Sensing Imaging System

**Autores**: Olivier Lim, Stéphane Mancini, Mauro Dalla Mura  
**Journal**: Sensors  
**Ano**: 2022  
**Volume**: 22, Article 9793  
**DOI**: 10.3390/s22249793  

### Resumo
Estudo sobre a viabilidade de sistemas de imageamento hiperespectral compressivo em tempo real incorporados. Explora alternativas aos sistemas convencionais através de aquisições compressivas que permitem amostragem de dados com menos aquisições que técnicas clássicas, mesmo abaixo da taxa de Nyquist.

### Metodologia Abordada
- **Compressive sensing** para imageamento hiperespectral
- **Sistemas embedded** para processamento em tempo real
- **Algoritmos de reconstrução** para recuperação de dados
- **Aplicações multi-domínio**: sensoriamento remoto, agricultura, astronomia, geologia, medicina

### Principais Resultados/Contribuições
- Demonstração da viabilidade de sistemas compressivos embarcados
- Redução significativa de dados sem perda de qualidade
- Aplicabilidade em múltiplas áreas incluindo agricultura
- Avanços em processamento em tempo real

### Palavras-chave
Hyperspectral imaging, compressive sensing, embedded systems, real-time processing, agriculture, remote sensing

### Relevância para a Pesquisa
**Média-Alta** - Relevante para otimização de sistemas de drones e redução de dados, especialmente para aplicações em tempo real.

### Limitações Identificadas
- Complexidade computacional dos algoritmos de reconstrução
- Necessidade de validação em cenários agrícolas específicos
- Limitações de hardware para implementação embarcada

### Conexões com Outros Artigos
Complementa os métodos de correção em drones fornecendo alternativas para otimização de aquisição de dados.

---

## 4. Robust Radiometric and Geometric Correction Methods for Drone-Based Hyperspectral Imaging in Agricultural Applications

**Autores**: Hyoung-Sub Shin, Seung-Hwan Go, Jong-Hwa Park  
**Journal**: Korean Journal of Remote Sensing  
**Ano**: 2024  
**Volume**: 40(3), páginas 257-268  
**DOI**: 10.7780/kjrs.2024.40.3.2  

### Resumo
Estudo focado em métodos robustos de correção radiométrica e geométrica para imageamento hiperespectral com drones em aplicações agrícolas. Aborda os desafios de distorções radiométricas e geométricas no pré-processamento de dados hiperespectrais adquiridos por drones.

### Metodologia Abordada
- **Correção radiométrica**: Empirical Line Method (ELM) com painéis de referência espectral
- **Correção geométrica**: Transformação rubber sheet com pontos de controle terrestre
- **Validação**: Correlações altas (0.97-0.99) entre medições
- **Aplicação**: Monitoramento e manejo agrícola

### Principais Resultados/Contribuições
- **Melhoria na reflectância**: 5-55% de melhoria para painéis de referência
- **Perfil espectral uniforme** através das bandas
- **Correção efetiva** de ruído do sensor e variações na irradiância solar
- **Validação robusta** com altas correlações

### Palavras-chave
Drone-based hyperspectral imaging, radiometric correction, geometric correction, empirical line method, agricultural applications, reflectance

### Relevância para a Pesquisa
**Muito Alta** - Diretamente aplicável ao projeto, fornecendo metodologias específicas para correção de dados de drones hiperespectrais em agricultura.

### Limitações Identificadas
- Desvios menores observados em comprimentos de onda específicos
- Necessidade de painéis de referência calibrados
- Dependência de pontos de controle terrestre para correção geométrica

### Conexões com Outros Artigos
Conecta diretamente com os fundamentos do AVIRIS e aplica-se aos métodos de classificação LULC, fornecendo o pipeline de pré-processamento essencial.

---

## Síntese dos Gaps Identificados

### Limitações dos Métodos Atuais
1. **Correções atmosféricas**: Métodos como ACORN focam em sensores aerotransportados, necessitando adaptação para drones
2. **Validação limitada**: Poucos estudos comparam sistematicamente métodos tradicionais vs. deep learning em cenários reais
3. **Processamento em tempo real**: Limitações computacionais para implementação embarcada
4. **Especificidade agrícola**: Falta de metodologias otimizadas especificamente para agricultura de precisão

### Oportunidades de Pesquisa
1. **Pipeline integrado**: Desenvolvimento de metodologia completa desde aquisição até classificação
2. **Deep learning aplicado**: Exploração de CNN/LSTM para classificação LULC com dados de drones
3. **Validação comparativa**: Estudos experimentais comparando diferentes abordagens
4. **Otimização agrícola**: Métodos específicos para culturas e condições brasileiras

### Justificativa para a Contribuição
A pesquisa proposta preenche lacunas importantes ao:
- Integrar correções radiométricas otimizadas para drones com classificação avançada
- Comparar sistematicamente métodos tradicionais e deep learning
- Validar em cenário real de agricultura de precisão
- Desenvolver pipeline completo e reproduzível 