#!/usr/bin/env python3
"""
Script para análise automática de artigos científicos
Gera resumos detalhados identificando tecnologias, hardware, modelos, testes e resultados

Autor: Diego Maia
Data: 2025-01-03
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime


class ArticleAnalyzer:
    """Classe para análise de artigos científicos"""
    
    def __init__(self):
        """Inicializa o analisador com padrões de busca"""
        
        # Padrões para identificar tecnologias
        self.tech_patterns = {
            'frameworks': [
                r'tensorflow|pytorch|keras|caffe|opencv|scikit-learn|pandas|numpy',
                r'cuda|opencl|openmp|mpi|hadoop|spark|docker|kubernetes',
                r'ros|gazebo|slam|pcl|vtk|itk|eigen|boost',
                r'matlab|simulink|labview|python|c\+\+|java|javascript|r\b'
            ],
            'algorithms': [
                r'cnn|convolutional neural network|lstm|rnn|svm|random forest|k-means',
                r'pca|principal component analysis|ica|lda|qda|bayesian|decision tree',
                r'gradient descent|backpropagation|adaboost|xgboost|neural network',
                r'deep learning|machine learning|artificial intelligence|reinforcement learning'
            ],
            'hyperspectral': [
                r'hyperspectral|multispectral|spectral imaging|spectral analysis',
                r'aviris|hyperion|chris|hico|prisma|desis|enmap',
                r'spectral unmixing|endmember|spectral library|spectral signature',
                r'atmospheric correction|radiometric calibration'
            ]
        }
        
        # Padrões para identificar hardware
        self.hardware_patterns = {
            'processors': [
                r'intel|amd|arm|nvidia|qualcomm|snapdragon|cortex|xeon|i\d+|ryzen',
                r'gpu|cpu|tpu|fpga|asic|dsp|microcontroller|raspberry pi',
                r'cuda cores|tensor cores|compute units|processing units'
            ],
            'memory': [
                r'ram|ddr\d+|gddr\d+|hbm|cache|memory|storage|ssd|hdd',
                r'\d+\s*gb|gigabyte|terabyte|megabyte|\d+\s*mb|\d+\s*tb'
            ],
            'sensors': [
                r'cmos|ccd|infrared|thermal|lidar|radar|camera|sensor',
                r'spectrometer|radiometer|photometer|detector|array'
            ]
        }
        
        # Padrões para identificar modelos/métodos
        self.model_patterns = [
            r'model|method|approach|algorithm|technique|framework|architecture',
            r'proposed|novel|new|improved|enhanced|optimized|efficient',
            r'classification|regression|clustering|segmentation|detection|recognition',
            r'supervised|unsupervised|semi-supervised|reinforcement'
        ]
        
        # Padrões para identificar testes/experimentos
        self.test_patterns = [
            r'experiment|test|evaluation|validation|benchmark|comparison',
            r'dataset|database|ground truth|training|testing|validation set',
            r'accuracy|precision|recall|f1-score|auc|mse|rmse|mae',
            r'performance|efficiency|speed|throughput|latency|execution time'
        ]
        
        # Padrões para identificar resultados
        self.result_patterns = [
            r'result|outcome|finding|conclusion|achievement|improvement',
            r'\d+%|\d+\.\d+%|accuracy of|precision of|recall of',
            r'faster|slower|better|worse|higher|lower|increased|decreased',
            r'outperform|superior|inferior|comparable|competitive'
        ]

    def extract_sections(self, text: str) -> Dict[str, str]:
        """
        Extrai seções principais do artigo.
        
        Args:
            text (str): Texto completo do artigo
            
        Returns:
            Dict[str, str]: Dicionário com as seções extraídas
        """
        sections = {}
        
        # Padrões comuns de seções
        section_patterns = {
            'abstract': r'abstract|resumo',
            'introduction': r'introduction|introdução|1\.\s*introduction',
            'methodology': r'methodology|method|métodos|approach|2\.\s*method',
            'experiments': r'experiment|test|evaluation|avaliação|4\.\s*experiment',
            'results': r'results|resultados|findings|5\.\s*results',
            'conclusion': r'conclusion|conclusão|conclusões|6\.\s*conclusion',
            'references': r'references|referências|bibliography'
        }
        
        text_lower = text.lower()
        
        for section_name, pattern in section_patterns.items():
            match = re.search(pattern, text_lower)
            if match:
                start_pos = match.start()
                # Encontrar o próximo cabeçalho ou final do texto
                next_section = None
                for other_pattern in section_patterns.values():
                    if other_pattern != pattern:
                        next_match = re.search(other_pattern, text_lower[start_pos + 50:])
                        if next_match:
                            if next_section is None or next_match.start() < next_section:
                                next_section = next_match.start() + start_pos + 50
                
                if next_section:
                    sections[section_name] = text[start_pos:next_section].strip()
                else:
                    sections[section_name] = text[start_pos:start_pos + 2000].strip()
        
        return sections

    def find_patterns(self, text: str, patterns: List[str]) -> List[str]:
        """
        Encontra padrões específicos no texto.
        
        Args:
            text (str): Texto para buscar
            patterns (List[str]): Lista de padrões regex
            
        Returns:
            List[str]: Lista de matches encontrados
        """
        matches = []
        text_lower = text.lower()
        
        for pattern in patterns:
            found = re.findall(pattern, text_lower, re.IGNORECASE)
            matches.extend(found)
        
        # Remover duplicatas e limpar
        unique_matches = list(set(matches))
        return [match.strip() for match in unique_matches if match.strip()]

    def extract_metrics(self, text: str) -> List[str]:
        """
        Extrai métricas numéricas do texto.
        
        Args:
            text (str): Texto para analisar
            
        Returns:
            List[str]: Lista de métricas encontradas
        """
        metrics = []
        
        # Padrões para métricas comuns
        metric_patterns = [
            r'accuracy[:\s]+(\d+\.?\d*%?)',
            r'precision[:\s]+(\d+\.?\d*%?)',
            r'recall[:\s]+(\d+\.?\d*%?)',
            r'f1[-\s]score[:\s]+(\d+\.?\d*%?)',
            r'mse[:\s]+(\d+\.?\d*)',
            r'rmse[:\s]+(\d+\.?\d*)',
            r'execution time[:\s]+(\d+\.?\d*\s*\w+)',
            r'processing time[:\s]+(\d+\.?\d*\s*\w+)',
            r'fps[:\s]+(\d+\.?\d*)',
            r'throughput[:\s]+(\d+\.?\d*\s*\w+)'
        ]
        
        for pattern in metric_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches:
                metrics.append(match)
        
        return metrics

    def analyze_article(self, content: str, title: str) -> Dict:
        """
        Analisa um artigo completo.
        
        Args:
            content (str): Conteúdo do artigo
            title (str): Título do artigo
            
        Returns:
            Dict: Análise completa do artigo
        """
        # Extrair seções
        sections = self.extract_sections(content)
        
        # Analisar tecnologias
        technologies = {}
        for tech_type, patterns in self.tech_patterns.items():
            technologies[tech_type] = self.find_patterns(content, patterns)
        
        # Analisar hardware
        hardware = {}
        for hw_type, patterns in self.hardware_patterns.items():
            hardware[hw_type] = self.find_patterns(content, patterns)
        
        # Analisar modelos/métodos
        models = self.find_patterns(content, self.model_patterns)
        
        # Analisar testes
        tests = self.find_patterns(content, self.test_patterns)
        
        # Analisar resultados
        results = self.find_patterns(content, self.result_patterns)
        
        # Extrair métricas
        metrics = self.extract_metrics(content)
        
        # Extrair palavras-chave importantes
        keywords = self.extract_keywords(content)
        
        return {
            'title': title,
            'sections': sections,
            'technologies': technologies,
            'hardware': hardware,
            'models': models,
            'tests': tests,
            'results': results,
            'metrics': metrics,
            'keywords': keywords
        }

    def extract_keywords(self, text: str) -> List[str]:
        """
        Extrai palavras-chave importantes do texto.
        
        Args:
            text (str): Texto para analisar
            
        Returns:
            List[str]: Lista de palavras-chave
        """
        # Palavras-chave específicas para processamento hiperespectral
        key_terms = [
            'hyperspectral', 'multispectral', 'spectral', 'imaging', 'remote sensing',
            'classification', 'segmentation', 'detection', 'recognition', 'analysis',
            'algorithm', 'method', 'approach', 'technique', 'framework', 'model',
            'neural network', 'deep learning', 'machine learning', 'artificial intelligence',
            'fpga', 'gpu', 'cpu', 'embedded', 'real-time', 'parallel', 'optimization',
            'accuracy', 'performance', 'efficiency', 'speed', 'throughput',
            'dataset', 'benchmark', 'evaluation', 'validation', 'comparison'
        ]
        
        found_keywords = []
        text_lower = text.lower()
        
        for term in key_terms:
            if term in text_lower:
                found_keywords.append(term)
        
        return found_keywords

    def generate_summary(self, analysis: Dict) -> str:
        """
        Gera um resumo formatado da análise.
        
        Args:
            analysis (Dict): Resultado da análise
            
        Returns:
            str: Resumo formatado em Markdown
        """
        title = analysis['title']
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        summary = f"""# Análise do Artigo: {title}

**Data da Análise**: {current_date}
**Analisado por**: Sistema Automático de Análise de Artigos

---

## 📋 Resumo Executivo

Este documento apresenta uma análise automatizada do artigo científico, identificando tecnologias, hardware, modelos, métodos de teste e resultados principais.

## 🔧 Tecnologias Identificadas

### Frameworks e Bibliotecas
{self._format_list(analysis['technologies'].get('frameworks', []))}

### Algoritmos e Métodos
{self._format_list(analysis['technologies'].get('algorithms', []))}

### Tecnologias Hiperespectrais
{self._format_list(analysis['technologies'].get('hyperspectral', []))}

## 💻 Hardware Identificado

### Processadores
{self._format_list(analysis['hardware'].get('processors', []))}

### Memória e Armazenamento
{self._format_list(analysis['hardware'].get('memory', []))}

### Sensores e Dispositivos
{self._format_list(analysis['hardware'].get('sensors', []))}

## 🧠 Modelos e Métodos

{self._format_list(analysis['models'])}

## 🧪 Testes e Avaliações

{self._format_list(analysis['tests'])}

## 📊 Resultados e Métricas

### Resultados Principais
{self._format_list(analysis['results'])}

### Métricas Numéricas
{self._format_list(analysis['metrics'])}

## 🔑 Palavras-Chave

{self._format_list(analysis['keywords'])}

## 📑 Seções Identificadas

{self._format_sections(analysis['sections'])}

---

## 📝 Observações

- Esta análise foi gerada automaticamente através de processamento de texto
- Pode conter imprecisões devido à conversão PDF → Markdown
- Recomenda-se verificação manual para validação completa
- Padrões identificados através de expressões regulares e busca por palavras-chave

## 🔍 Metodologia de Análise

1. **Extração de Texto**: Conversão PDF → Markdown via PyPDF2
2. **Identificação de Padrões**: Busca por regex patterns específicos
3. **Categorização**: Classificação em tecnologias, hardware, modelos, etc.
4. **Extração de Métricas**: Identificação de valores numéricos e percentuais
5. **Geração de Resumo**: Formatação estruturada dos resultados

---

**Arquivo Original**: {title}
**Processado em**: {current_date}
"""
        
        return summary

    def _format_list(self, items: List[str]) -> str:
        """Formata lista de itens para Markdown"""
        if not items:
            return "- *Nenhum item identificado*\n"
        
        formatted = []
        for item in items[:20]:  # Limitar a 20 itens
            formatted.append(f"- {item}")
        
        if len(items) > 20:
            formatted.append(f"- *... e mais {len(items) - 20} itens*")
        
        return "\n".join(formatted) + "\n"

    def _format_sections(self, sections: Dict[str, str]) -> str:
        """Formata seções identificadas"""
        if not sections:
            return "- *Nenhuma seção claramente identificada*\n"
        
        formatted = []
        for section_name, content in sections.items():
            preview = content[:200].replace('\n', ' ') + "..." if len(content) > 200 else content
            formatted.append(f"- **{section_name.title()}**: {preview}")
        
        return "\n".join(formatted) + "\n"


def main():
    """Função principal"""
    print("🔍 Iniciando análise automática dos artigos...")
    
    # Diretórios
    input_dir = "documentos/artigos_convertidos"
    output_dir = "documentos/analise_artigos"
    
    # Verificar se diretório existe
    if not os.path.exists(input_dir):
        print(f"❌ Erro: Diretório {input_dir} não encontrado!")
        sys.exit(1)
    
    # Criar diretório de saída
    os.makedirs(output_dir, exist_ok=True)
    
    # Inicializar analisador
    analyzer = ArticleAnalyzer()
    
    # Encontrar arquivos MD
    md_files = [f for f in os.listdir(input_dir) if f.endswith('.md')]
    
    if not md_files:
        print(f"❌ Nenhum arquivo .md encontrado em {input_dir}")
        sys.exit(1)
    
    print(f"📚 Encontrados {len(md_files)} arquivos para análise...")
    
    successful = 0
    
    # Processar cada arquivo
    for i, filename in enumerate(md_files, 1):
        print(f"\n[{i}/{len(md_files)}] Analisando: {filename}")
        
        try:
            # Ler arquivo
            input_path = os.path.join(input_dir, filename)
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Analisar
            title = Path(filename).stem
            analysis = analyzer.analyze_article(content, title)
            
            # Gerar resumo
            summary = analyzer.generate_summary(analysis)
            
            # Salvar análise
            output_filename = f"analise_{filename}"
            output_path = os.path.join(output_dir, output_filename)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(summary)
            
            print(f"✅ Análise salva: {output_filename}")
            successful += 1
            
        except Exception as e:
            print(f"❌ Erro ao processar {filename}: {str(e)}")
    
    # Relatório final
    print(f"\n📊 RELATÓRIO DE ANÁLISE:")
    print(f"   • Total de arquivos: {len(md_files)}")
    print(f"   • Analisados com sucesso: {successful}")
    print(f"   • Falhas: {len(md_files) - successful}")
    
    if successful == len(md_files):
        print("\n✅ Todas as análises foram concluídas com sucesso!")
    else:
        print(f"\n⚠️  {successful} de {len(md_files)} análises foram bem-sucedidas.")


if __name__ == "__main__":
    main()
