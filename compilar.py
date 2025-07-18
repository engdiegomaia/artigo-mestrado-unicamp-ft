#!/usr/bin/env python3
import os
import shutil
import subprocess

print("=== COMPILANDO TESE UNICAMP-FT ===")

# 1. Limpar e criar pastas
print("1. Preparando ambiente...")
if os.path.exists("compilacao"):
    shutil.rmtree("compilacao")
if os.path.exists("dist"):
    shutil.rmtree("dist")

os.makedirs("compilacao", exist_ok=True)
os.makedirs("dist", exist_ok=True)
os.makedirs("src/figuras", exist_ok=True)
os.makedirs("src/logotipos", exist_ok=True)

# 2. Copiar assets
print("2. Copiando assets...")
if os.path.exists("assets/figuras"):
    for f in os.listdir("assets/figuras"):
        if os.path.isfile(f"assets/figuras/{f}"):
            shutil.copy2(f"assets/figuras/{f}", f"src/figuras/{f}")
            print(f"   ✓ {f}")

if os.path.exists("assets/logotipos"):
    for f in os.listdir("assets/logotipos"):
        if os.path.isfile(f"assets/logotipos/{f}"):
            shutil.copy2(f"assets/logotipos/{f}", f"src/logotipos/{f}")
            print(f"   ✓ {f}")

# 3. Compilar
print("3. Compilando LaTeX...")

os.chdir("src")
print("   3.1. Primeira compilação...")
subprocess.run("pdflatex -halt-on-error -file-line-error -output-directory=../compilacao tese.tex", shell=True, check=True)

os.chdir("../compilacao")
print("   3.2. Bibliografia...")
subprocess.run("biber tese", shell=True)

print("   3.3. Nomenclatura...")
subprocess.run("makeindex tese.nlo -s nomencl.ist -o tese.nls", shell=True)

os.chdir("../src")
print("   3.4. Segunda compilação...")
subprocess.run("pdflatex -halt-on-error -file-line-error -output-directory=../compilacao tese.tex", shell=True, check=True)

print("   3.5. Terceira compilação...")
subprocess.run("pdflatex -halt-on-error -file-line-error -output-directory=../compilacao tese.tex", shell=True, check=True)

os.chdir("..")

# 4. Finalizar
print("4. Finalizando...")
if os.path.exists("compilacao/tese.pdf"):
    shutil.copy2("compilacao/tese.pdf", "dist/tese.pdf")
    tamanho = os.path.getsize("dist/tese.pdf")
    print(f"   ✓ PDF criado: dist/tese.pdf ({tamanho//1024} KB)")
    print("\n🎉 SUCESSO! Tese compilada! 🎉")
else:
    print("   ✗ ERRO: PDF não foi gerado!") 