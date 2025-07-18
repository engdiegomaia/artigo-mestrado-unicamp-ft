#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script simples de compilação para dissertação UNICAMP-FT
"""

import os
import sys
import shutil
import subprocess

def executar_comando(comando, pasta=None):
    """Executa um comando e mostra o resultado"""
    print(f">>> Executando: {comando}")
    if pasta:
        print(f">>> Na pasta: {pasta}")
    
    try:
        result = subprocess.run(
            comando, 
            shell=True, 
            cwd=pasta,
            check=True
        )
        print(">>> Comando executado com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f">>> ERRO: Comando falhou com código {e.returncode}")
        return False

def main():
    print("=== COMPILADOR SIMPLES PARA TESE UNICAMP-FT ===")
    
    # Verificar se tese.tex existe
    if not os.path.exists("src/tese.tex"):
        print("ERRO: Arquivo src/tese.tex não encontrado!")
        return
    
    # Criar pastas necessárias
    print("\n1. Criando pastas...")
    for pasta in ["compilacao", "dist", "src/figuras", "src/logotipos"]:
        os.makedirs(pasta, exist_ok=True)
        print(f"   ✓ {pasta}")
    
    # Copiar assets
    print("\n2. Copiando assets...")
    try:
        if os.path.exists("assets/figuras"):
            for arquivo in os.listdir("assets/figuras"):
                if os.path.isfile(f"assets/figuras/{arquivo}"):
                    shutil.copy2(f"assets/figuras/{arquivo}", f"src/figuras/{arquivo}")
                    print(f"   ✓ Figura: {arquivo}")
        
        if os.path.exists("assets/logotipos"):
            for arquivo in os.listdir("assets/logotipos"):
                if os.path.isfile(f"assets/logotipos/{arquivo}"):
                    shutil.copy2(f"assets/logotipos/{arquivo}", f"src/logotipos/{arquivo}")
                    print(f"   ✓ Logo: {arquivo}")
    except Exception as e:
        print(f"   AVISO: Erro ao copiar assets: {e}")
    
    # Compilar LaTeX
    print("\n3. Compilando LaTeX...")
    
    print("\n   3.1. Primeira compilação...")
    if not executar_comando("pdflatex -halt-on-error -file-line-error -output-directory=../compilacao tese.tex", "src"):
        print("ERRO: Primeira compilação falhou!")
        return
    
    print("\n   3.2. Processando bibliografia...")
    if not executar_comando("biber tese", "compilacao"):
        print("AVISO: Bibliografia pode ter problemas")
    
    print("\n   3.3. Processando nomenclatura...")
    if not executar_comando("makeindex tese.nlo -s nomencl.ist -o tese.nls", "compilacao"):
        print("AVISO: Nomenclatura pode ter problemas")
    
    print("\n   3.4. Segunda compilação...")
    if not executar_comando("pdflatex -halt-on-error -file-line-error -output-directory=../compilacao tese.tex", "src"):
        print("ERRO: Segunda compilação falhou!")
        return
    
    print("\n   3.5. Terceira compilação...")
    if not executar_comando("pdflatex -halt-on-error -file-line-error -output-directory=../compilacao tese.tex", "src"):
        print("ERRO: Terceira compilação falhou!")
        return
    
    # Mover PDF final
    print("\n4. Finalizando...")
    if os.path.exists("compilacao/tese.pdf"):
        shutil.copy2("compilacao/tese.pdf", "dist/tese.pdf")
        tamanho = os.path.getsize("dist/tese.pdf")
        print(f"   ✓ PDF criado: dist/tese.pdf ({tamanho} bytes)")
        print("\n🎉 SUCESSO! Tese compilada com sucesso! 🎉")
    else:
        print("   ✗ ERRO: PDF não foi gerado!")

if __name__ == "__main__":
    main() 