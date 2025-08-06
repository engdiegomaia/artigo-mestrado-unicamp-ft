#!/usr/bin/env python3
"""
Script para obter a data e hora atual formatada para atualização do README.

Este script retorna a data e hora atual em diferentes formatos úteis para
documentação e atualização de timestamps no projeto.

Autor: Diego Maia
Data: 2025-01-03
Versão: 1.0
"""

import datetime
import sys


def get_current_datetime():
    """
    Obtém a data e hora atual em diferentes formatos.
    
    Returns:
        dict: Dicionário com diferentes formatos de data/hora
    """
    now = datetime.datetime.now()
    
    formats = {
        # Formato ISO padrão (YYYY-MM-DD HH:MM:SS)
        'iso': now.strftime('%Y-%m-%d %H:%M:%S'),
        
        # Formato ISO apenas data (YYYY-MM-DD)
        'iso_date': now.strftime('%Y-%m-%d'),
        
        # Formato brasileiro (DD/MM/YYYY HH:MM)
        'br': now.strftime('%d/%m/%Y %H:%M'),
        
        # Formato brasileiro apenas data (DD/MM/YYYY)
        'br_date': now.strftime('%d/%m/%Y'),
        
        # Formato para README (YYYY-MM-DD)
        'readme': now.strftime('%Y-%m-%d'),
        
        # Formato completo para logs (YYYY-MM-DD HH:MM:SS)
        'full': now.strftime('%Y-%m-%d %H:%M:%S'),
        
        # Formato compacto (YYYYMMDD_HHMMSS)
        'compact': now.strftime('%Y%m%d_%H%M%S'),
        
        # Formato RFC 3339 (ISO 8601)
        'rfc3339': now.isoformat(),
        
        # Formato para commits Git
        'git': now.strftime('%Y-%m-%d %H:%M'),
    }
    
    return formats


def print_datetime_formats():
    """
    Imprime todos os formatos de data/hora disponíveis.
    """
    formats = get_current_datetime()
    
    print("=== FORMATOS DE DATA E HORA ATUAL ===")
    print(f"Data/Hora atual: {formats['full']}")
    print()
    
    for format_name, formatted_date in formats.items():
        print(f"{format_name:12}: {formatted_date}")
    
    print()
    print("=== USO RECOMENDADO PARA README ===")
    print(f"Última Atualização: {formats['readme']}")
    print(f"Timestamp completo: {formats['full']}")


def get_specific_format(format_name):
    """
    Retorna um formato específico de data/hora.
    
    Args:
        format_name (str): Nome do formato desejado
        
    Returns:
        str: Data/hora formatada
        
    Raises:
        ValueError: Se o formato não for reconhecido
    """
    formats = get_current_datetime()
    
    if format_name not in formats:
        available_formats = ', '.join(formats.keys())
        raise ValueError(f"Formato '{format_name}' não reconhecido. Formatos disponíveis: {available_formats}")
    
    return formats[format_name]


def main():
    """
    Função principal do script.
    """
    # Verificar argumentos da linha de comando
    if len(sys.argv) > 1:
        if sys.argv[1] in ['-h', '--help', 'help']:
            print("Uso: python get_current_datetime.py [formato]")
            print()
            print("Formatos disponíveis:")
            formats = get_current_datetime()
            for format_name, formatted_date in formats.items():
                print(f"  {format_name:12}: {formatted_date}")
            print()
            print("Exemplos:")
            print("  python get_current_datetime.py readme")
            print("  python get_current_datetime.py iso")
            print("  python get_current_datetime.py br")
            return
        
        # Obter formato específico
        try:
            format_name = sys.argv[1]
            result = get_specific_format(format_name)
            print(result)
        except ValueError as e:
            print(f"Erro: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # Mostrar todos os formatos
        print_datetime_formats()


if __name__ == "__main__":
    main() 