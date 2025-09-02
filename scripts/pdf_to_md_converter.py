#!/usr/bin/env python3
"""
Script para conversão de PDFs para Markdown
Desenvolvido para o projeto de dissertação UNICAMP-FT

Autor: Diego Maia
Data: 2025-01-03
"""

import os
import sys
import argparse
import re
from pathlib import Path
from typing import List, Optional, Dict
import PyPDF2


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extrai texto de um arquivo PDF.
    
    Args:
        pdf_path (str): Caminho para o arquivo PDF
        
    Returns:
        str: Texto extraído do PDF
    """
    try:
        text = ""
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Extrair texto de todas as páginas
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                page_text = page.extract_text()
                text += f"\n\n--- Página {page_num + 1} ---\n\n"
                text += page_text
                
        return text
    
    except Exception as e:
        print(f"Erro ao extrair texto do PDF {pdf_path}: {str(e)}")
        return ""


def clean_text(text: str) -> str:
    """
    Limpa e formata o texto extraído do PDF.
    
    Args:
        text (str): Texto bruto extraído do PDF
        
    Returns:
        str: Texto limpo e formatado
    """
    # Remover linhas vazias excessivas
    text = re.sub(r'\n\s*\n\s*\n', '\n\n', text)
    
    # Corrigir quebras de linha no meio de palavras
    text = re.sub(r'(\w+)-\s*\n\s*(\w+)', r'\1\2', text)
    
    # Normalizar espaçamento
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\n\s+', '\n', text)
    
    # Remover caracteres especiais problemáticos
    text = text.replace('\x00', '')
    text = text.replace('\ufeff', '')
    
    return text.strip()


def convert_to_markdown(text: str, title: str) -> str:
    """
    Converte texto extraído para formato Markdown.
    
    Args:
        text (str): Texto extraído e limpo
        title (str): Título do documento
        
    Returns:
        str: Texto formatado em Markdown
    """
    markdown_content = f"""# {title}

**Documento**: PDF convertido para Markdown
**Data de Conversão**: {get_current_date()}

---

## Conteúdo Extraído

{text}

---

## Metadados

- **Fonte**: PDF original
- **Processamento**: Conversão automática via PyPDF2
- **Formato de Saída**: Markdown (.md)
- **Observações**: Texto extraído pode conter formatação irregular devido à conversão automática

"""
    
    return markdown_content


def get_current_date() -> str:
    """Retorna a data atual no formato YYYY-MM-DD"""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d")


def convert_pdf_to_md(pdf_path: str, output_dir: str, custom_title: Optional[str] = None) -> bool:
    """
    Converte um arquivo PDF para Markdown.
    
    Args:
        pdf_path (str): Caminho do arquivo PDF
        output_dir (str): Diretório de saída
        custom_title (str, optional): Título customizado
        
    Returns:
        bool: True se a conversão foi bem-sucedida
    """
    try:
        # Verificar se o arquivo PDF existe
        if not os.path.exists(pdf_path):
            print(f"❌ Erro: Arquivo PDF não encontrado: {pdf_path}")
            return False
        
        # Extrair texto do PDF
        print(f"📄 Extraindo texto de: {pdf_path}")
        text = extract_text_from_pdf(pdf_path)
        
        if not text.strip():
            print(f"⚠️  Aviso: Nenhum texto foi extraído de {pdf_path}")
            return False
        
        # Limpar texto
        text = clean_text(text)
        
        # Definir título
        pdf_name = Path(pdf_path).stem
        title = custom_title if custom_title else pdf_name
        
        # Converter para Markdown
        markdown_content = convert_to_markdown(text, title)
        
        # Criar diretório de saída se não existir
        os.makedirs(output_dir, exist_ok=True)
        
        # Definir nome do arquivo de saída
        output_file = os.path.join(output_dir, f"{pdf_name}.md")
        
        # Salvar arquivo Markdown
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"✅ Conversão concluída: {output_file}")
        return True
        
    except Exception as e:
        print(f"❌ Erro na conversão de {pdf_path}: {str(e)}")
        return False


def convert_directory(input_dir: str, output_dir: str) -> Dict[str, bool]:
    """
    Converte todos os PDFs de um diretório.
    
    Args:
        input_dir (str): Diretório com os PDFs
        output_dir (str): Diretório de saída
        
    Returns:
        Dict[str, bool]: Dicionário com resultados da conversão
    """
    results = {}
    
    # Encontrar todos os arquivos PDF
    pdf_files = []
    for file in os.listdir(input_dir):
        if file.lower().endswith('.pdf'):
            pdf_files.append(os.path.join(input_dir, file))
    
    if not pdf_files:
        print(f"❌ Nenhum arquivo PDF encontrado em {input_dir}")
        return results
    
    print(f"📚 Encontrados {len(pdf_files)} arquivos PDF para conversão...")
    
    # Converter cada PDF
    for i, pdf_path in enumerate(pdf_files, 1):
        print(f"\n[{i}/{len(pdf_files)}] Processando: {os.path.basename(pdf_path)}")
        results[pdf_path] = convert_pdf_to_md(pdf_path, output_dir)
    
    return results


def main():
    """Função principal do script"""
    parser = argparse.ArgumentParser(
        description='Converte arquivos PDF para Markdown',
        epilog='Exemplo: python pdf_to_md_converter.py -i documentos/artigos -o documentos/artigos_convertidos'
    )
    
    parser.add_argument('-i', '--input', required=True,
                        help='Arquivo PDF ou diretório com PDFs')
    parser.add_argument('-o', '--output', required=True,
                        help='Diretório de saída para os arquivos Markdown')
    parser.add_argument('-t', '--title',
                        help='Título personalizado (apenas para arquivo único)')
    
    args = parser.parse_args()
    
    print("🔄 Iniciando conversão PDF para Markdown...")
    print(f"📥 Entrada: {args.input}")
    print(f"📤 Saída: {args.output}")
    
    # Verificar se a entrada é um arquivo ou diretório
    if os.path.isfile(args.input):
        # Conversão de arquivo único
        success = convert_pdf_to_md(args.input, args.output, args.title)
        if success:
            print("\n✅ Conversão concluída com sucesso!")
        else:
            print("\n❌ Falha na conversão!")
            sys.exit(1)
    
    elif os.path.isdir(args.input):
        # Conversão de diretório
        results = convert_directory(args.input, args.output)
        
        # Relatório final
        successful = sum(1 for success in results.values() if success)
        total = len(results)
        
        print(f"\n📊 RELATÓRIO DE CONVERSÃO:")
        print(f"   • Total de arquivos: {total}")
        print(f"   • Convertidos com sucesso: {successful}")
        print(f"   • Falhas: {total - successful}")
        
        if successful == total:
            print("\n✅ Todas as conversões foram concluídas com sucesso!")
        elif successful > 0:
            print(f"\n⚠️  {successful} de {total} conversões foram bem-sucedidas.")
        else:
            print("\n❌ Todas as conversões falharam!")
            sys.exit(1)
    
    else:
        print(f"❌ Erro: Entrada '{args.input}' não é um arquivo nem diretório válido!")
        sys.exit(1)


if __name__ == "__main__":
    main()
