#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de compilação para dissertação UNICAMP-FT
Autor: Claude
Data: 2024-03-19

Exemplo de utilização:
    python compila_python.py tese.tex
"""

import os
import sys
import shutil
import subprocess
import argparse
from pathlib import Path
import time

class Colors:
    """Cores para output no terminal"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    LIGHTBLUE = '\033[94m'
    YELLOW = '\033[93m'
    NC = '\033[0m'  # No Color

def print_colored(message, color):
    """Imprime mensagem colorida"""
    print(f"{color}{message}{Colors.NC}")

def print_info(message):
    """Imprime mensagem informativa"""
    print_colored(f">>> {message}", Colors.LIGHTBLUE)

def print_success(message):
    """Imprime mensagem de sucesso"""
    print_colored(f">>> {message}", Colors.GREEN)

def print_error(message):
    """Imprime mensagem de erro"""
    print_colored(f">>> {message}", Colors.RED)

def check_command(command):
    """Verifica se um comando está disponível no PATH"""
    return shutil.which(command) is not None

def run_command(command, cwd=None, check=True):
    """Executa um comando e retorna o resultado"""
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            cwd=cwd, 
            check=check,
            capture_output=True, 
            text=True
        )
        return result
    except subprocess.CalledProcessError as e:
        print_error(f"Erro ao executar comando: {command}")
        print_error(f"Código de saída: {e.returncode}")
        print_error(f"Stderr: {e.stderr}")
        return None

def setup_directories():
    """Cria as pastas necessárias"""
    dirs = ['compilacao', 'dist', 'src/figuras', 'src/logotipos']
    for dir_path in dirs:
        try:
            os.makedirs(dir_path, exist_ok=True)
            print_info(f"Pasta criada/verificada: {dir_path}")
        except Exception as e:
            print_info(f"Pasta já existe: {dir_path}")

def copy_assets():
    """Copia os arquivos de assets para src/"""
    try:
        # Copiar figuras
        if os.path.exists('assets/figuras'):
            for file in os.listdir('assets/figuras'):
                src = os.path.join('assets/figuras', file)
                dst = os.path.join('src/figuras', file)
                if os.path.isfile(src):
                    shutil.copy2(src, dst)
                    print_info(f"Copiado: {src} -> {dst}")
        
        # Copiar logotipos
        if os.path.exists('assets/logotipos'):
            for file in os.listdir('assets/logotipos'):
                src = os.path.join('assets/logotipos', file)
                dst = os.path.join('src/logotipos', file)
                if os.path.isfile(src):
                    shutil.copy2(src, dst)
                    print_info(f"Copiado: {src} -> {dst}")
        
        print_success("Assets copiados com sucesso!")
        
    except Exception as e:
        print_error(f"Erro ao copiar assets: {e}")
        return False
    
    return True

def compile_latex(arquivo_entrada):
    """Compila o documento LaTeX"""
    nome_arquivo = Path(arquivo_entrada).stem
    
    print_colored("=== COMPILAÇÃO DA DISSERTAÇÃO ===", Colors.LIGHTBLUE)
    print_info("Estrutura do projeto:")
    print("  📁 src/         → Arquivos LaTeX")
    print("  📁 compilacao/  → Arquivos temporários")
    print("  📁 dist/        → PDF final")
    print("  📁 assets/      → Figuras e logotipos")
    print()
    
    # Primeira compilação
    print_info("Primeira rodada de compilação")
    result = run_command(
        f"pdflatex -halt-on-error -file-line-error -output-directory=../compilacao {arquivo_entrada}",
        cwd="src"
    )
    if not result:
        print_error("Erro na primeira compilação")
        return False
    
    print_success("Primeira compilação completa")
    
    # Referências bibliográficas
    print_info("Resolvendo as referências bibliográficas")
    result = run_command(f"biber {nome_arquivo}", cwd="compilacao")
    if not result:
        print_error("Erro nas referências bibliográficas")
        return False
    
    print_success("Resolução das referências completa")
    
    # Lista de siglas e abreviações
    print_info("Resolvendo a lista de siglas")
    result = run_command(
        f"makeindex {nome_arquivo}.nlo -s nomencl.ist -o {nome_arquivo}.nls",
        cwd="compilacao"
    )
    if not result:
        print_error("Erro na geração da lista de símbolos")
        return False
    
    print_success("Resolução da lista de símbolos completa")
    
    # Segunda compilação
    print_info("Segunda rodada de compilação")
    result = run_command(
        f"pdflatex -halt-on-error -file-line-error -output-directory=../compilacao {arquivo_entrada}",
        cwd="src"
    )
    if not result:
        print_error("Erro na segunda compilação")
        return False
    
    print_success("Segunda rodada de compilação completa")
    
    # Terceira compilação
    print_info("Terceira rodada de compilação")
    result = run_command(
        f"pdflatex -halt-on-error -file-line-error -output-directory=../compilacao {arquivo_entrada}",
        cwd="src"
    )
    if not result:
        print_error("Erro na terceira compilação")
        return False
    
    print_success("Terceira rodada de compilação completa")
    
    # Mover PDF final
    pdf_source = f"compilacao/{nome_arquivo}.pdf"
    pdf_dest = f"dist/{nome_arquivo}.pdf"
    
    if os.path.exists(pdf_source):
        shutil.copy2(pdf_source, pdf_dest)
        
        # Mostrar informações do arquivo
        file_size = os.path.getsize(pdf_dest)
        if file_size > 1048576:
            size_str = f"{file_size / 1048576:.1f} MB"
        elif file_size > 1024:
            size_str = f"{file_size / 1024:.1f} KB"
        else:
            size_str = f"{file_size} bytes"
        
        print_colored("======= Compilação concluída com sucesso! =======", Colors.GREEN)
        print_success(f"PDF gerado: {pdf_dest}")
        print_info(f"Tamanho do arquivo: {size_str}")
        print()
        print_colored("🎉 Dissertação compilada com sucesso! 🎉", Colors.GREEN)
        
        return True
    else:
        print_error("PDF não foi gerado corretamente")
        return False

def main():
    """Função principal"""
    parser = argparse.ArgumentParser(description='Compilador LaTeX para dissertação UNICAMP-FT')
    parser.add_argument('arquivo', help='Nome do arquivo principal (ex: tese.tex)')
    
    if len(sys.argv) == 1:
        print_error("Você deve informar o nome do arquivo principal como parâmetro")
        print()
        print("Exemplo:")
        print(f"    python {sys.argv[0]} tese.tex")
        sys.exit(1)
    
    args = parser.parse_args()
    
    # Verificar se o arquivo existe
    arquivo_entrada = f"src/{args.arquivo}"
    if not os.path.exists(arquivo_entrada):
        print_error(f"Arquivo {arquivo_entrada} não encontrado!")
        print_error("Certifique-se de que o arquivo está na pasta src/")
        sys.exit(1)
    
    # Verificar comandos necessários
    commands = ['pdflatex', 'biber', 'makeindex']
    for cmd in commands:
        if not check_command(cmd):
            print_error(f"O comando '{cmd}' não está instalado ou não está no PATH")
            print_error("Instale o TeX Live completo: https://www.tug.org/texlive/")
            sys.exit(2)
    
    print_success("Todas as dependências encontradas!")
    
    # Configurar diretórios
    setup_directories()
    
    # Copiar assets
    if not copy_assets():
        sys.exit(3)
    
    # Compilar LaTeX
    if compile_latex(args.arquivo):
        sys.exit(0)
    else:
        sys.exit(4)

if __name__ == "__main__":
    main() 