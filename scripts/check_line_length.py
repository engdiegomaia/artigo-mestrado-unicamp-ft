#!/usr/bin/env python3
"""
Script para verificar e aplicar automaticamente a regra de 80 caracteres 
em arquivos LaTeX do projeto.

Uso:
    python scripts/check_line_length.py [--fix] [--verbose]
    
Opções:
    --fix      Aplica correções automaticamente
    --verbose  Mostra informações detalhadas
"""

import os
import sys
import argparse
import re
from pathlib import Path

def find_tex_files(project_root):
    """Encontra todos os arquivos .tex no projeto."""
    tex_files = []
    for root, dirs, files in os.walk(project_root):
        # Ignora pastas de output e dist
        dirs[:] = [d for d in dirs if d not in ['output', 'dist', '__pycache__']]
        for file in files:
            if file.endswith('.tex'):
                tex_files.append(os.path.join(root, file))
    return tex_files

def check_line_length(file_path, max_length=80):
    """Verifica se há linhas que excedem o limite de caracteres."""
    long_lines = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                # Remove quebras de linha e espaços em branco
                line = line.rstrip('\r\n')
                
                # Ignora linhas de comentário que começam com %
                if line.strip().startswith('%'):
                    continue
                    
                # Ignora linhas que são apenas espaços em branco
                if not line.strip():
                    continue
                
                # Verifica se a linha excede o limite
                if len(line) > max_length:
                    long_lines.append({
                        'line_num': line_num,
                        'length': len(line),
                        'content': line[:100] + '...' if len(line) > 100 else line
                    })
    except Exception as e:
        print(f"Erro ao ler arquivo {file_path}: {e}")
        
    return long_lines

def fix_long_lines(file_path, max_length=80):
    """Aplica correções automáticas para linhas longas."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        fixed_lines = []
        
        for line in lines:
            if len(line) <= max_length:
                fixed_lines.append(line)
                continue
                
            # Se a linha é muito longa, tenta quebrá-la
            if line.strip().startswith('\\'):
                # Comandos LaTeX - quebra após o comando
                if '\\section{' in line or '\\subsection{' in line or '\\subsubsection{' in line:
                    # Quebra títulos de seção
                    if '\\label{' in line:
                        # Separa o comando do label
                        parts = line.split('\\label{')
                        if len(parts) == 2:
                            fixed_lines.append(parts[0])
                            fixed_lines.append('\\label{' + parts[1])
                        else:
                            fixed_lines.append(line)
                    else:
                        fixed_lines.append(line)
                else:
                    fixed_lines.append(line)
            else:
                # Texto normal - quebra em pontos lógicos
                if len(line) > max_length:
                    # Quebra em pontos lógicos
                    words = line.split()
                    current_line = ""
                    
                    for word in words:
                        if len(current_line + " " + word) <= max_length:
                            current_line += (" " + word) if current_line else word
                        else:
                            if current_line:
                                fixed_lines.append(current_line)
                            current_line = word
                    
                    if current_line:
                        fixed_lines.append(current_line)
                else:
                    fixed_lines.append(line)
        
        # Escreve o arquivo corrigido
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(fixed_lines))
            
        return True
        
    except Exception as e:
        print(f"Erro ao corrigir arquivo {file_path}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(
        description='Verifica e corrige linhas longas em arquivos LaTeX'
    )
    parser.add_argument(
        '--fix', 
        action='store_true', 
        help='Aplica correções automaticamente'
    )
    parser.add_argument(
        '--verbose', 
        action='store_true', 
        help='Mostra informações detalhadas'
    )
    parser.add_argument(
        '--max-length', 
        type=int, 
        default=80, 
        help='Comprimento máximo de linha (padrão: 80)'
    )
    
    args = parser.parse_args()
    
    # Encontra a raiz do projeto
    project_root = Path(__file__).parent.parent
    tex_files = find_tex_files(project_root)
    
    print(f"🔍 Verificando {len(tex_files)} arquivos LaTeX...")
    print(f"📏 Limite de caracteres: {args.max_length}")
    print()
    
    total_long_lines = 0
    files_with_issues = []
    
    for tex_file in tex_files:
        relative_path = os.path.relpath(tex_file, project_root)
        long_lines = check_line_length(tex_file, args.max_length)
        
        if long_lines:
            files_with_issues.append(tex_file)
            total_long_lines += len(long_lines)
            
            if args.verbose:
                print(f"⚠️  {relative_path}:")
                for issue in long_lines:
                    print(f"   Linha {issue['line_num']}: {issue['length']} chars")
                    print(f"   {issue['content']}")
                print()
            
            # Aplica correções se solicitado
            if args.fix:
                if fix_long_lines(tex_file, args.max_length):
                    print(f"✅ Corrigido: {relative_path}")
                else:
                    print(f"❌ Erro ao corrigir: {relative_path}")
    
    # Resumo final
    print("=" * 50)
    if files_with_issues:
        print(f"📊 Resumo:")
        print(f"   Arquivos com problemas: {len(files_with_issues)}")
        print(f"   Total de linhas longas: {total_long_lines}")
        
        if not args.fix:
            print(f"\n💡 Para corrigir automaticamente, execute:")
            print(f"   python scripts/check_line_length.py --fix")
    else:
        print("🎉 Todos os arquivos estão dentro do limite de caracteres!")
    
    print(f"\n📁 Arquivos verificados: {len(tex_files)}")
    print(f"📏 Limite aplicado: {args.max_length} caracteres")

if __name__ == "__main__":
    main()
