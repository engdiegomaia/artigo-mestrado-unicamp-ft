# Scripts Utilitários

Esta pasta contém scripts Python utilitários para auxiliar no desenvolvimento e manutenção do projeto.

## 📁 Estrutura

```
scripts/
├── README.md                    # Esta documentação
├── get_current_datetime.py      # Script para obter data/hora atual
└── requirements.txt             # Dependências Python (se necessário)
```

## 🔧 Scripts Disponíveis

### `get_current_datetime.py`

Script para obter a data e hora atual em diferentes formatos, especialmente útil para atualização de timestamps no README principal.

#### Uso Básico

```bash
# Mostrar todos os formatos disponíveis
python scripts/get_current_datetime.py

# Obter formato específico para README
python scripts/get_current_datetime.py --format readme

# Modo silencioso (apenas o valor)
python scripts/get_current_datetime.py --format readme --quiet
```

#### Formatos Disponíveis

| Formato | Descrição | Exemplo |
|---------|-----------|---------|
| `readme` | Formato para README (YYYY-MM-DD) | `2025-01-03` |
| `iso` | ISO padrão (YYYY-MM-DD HH:MM:SS) | `2025-01-03 14:30:25` |
| `iso_date` | ISO apenas data (YYYY-MM-DD) | `2025-01-03` |
| `br` | Formato brasileiro (DD/MM/YYYY HH:MM) | `03/01/2025 14:30` |
| `br_date` | Brasileiro apenas data (DD/MM/YYYY) | `03/01/2025` |
| `full` | Completo para logs (YYYY-MM-DD HH:MM:SS) | `2025-01-03 14:30:25` |
| `compact` | Compacto (YYYYMMDD_HHMMSS) | `20250103_143025` |
| `rfc3339` | RFC 3339 (ISO 8601) | `2025-01-03T14:30:25.123456` |
| `git` | Para commits Git (YYYY-MM-DD HH:MM) | `2025-01-03 14:30` |

#### Exemplos de Uso

```bash
# Para atualizar README
python scripts/get_current_datetime.py --format readme --quiet
# Saída: 2025-01-03

# Para logs detalhados
python scripts/get_current_datetime.py --format full
# Saída: Formato 'full': 2025-01-03 14:30:25

# Para commits Git
python scripts/get_current_datetime.py --format git
# Saída: Formato 'git': 2025-01-03 14:30
```

#### Integração com README Principal

Para atualizar automaticamente a data no README principal:

```bash
# Obter data atual
CURRENT_DATE=$(python scripts/get_current_datetime.py --format readme --quiet)

# Atualizar README (exemplo para Linux/Mac)
sed -i "s/Última Atualização: .*/Última Atualização: $CURRENT_DATE/" README.md

# Para Windows PowerShell
$CURRENT_DATE = python scripts/get_current_datetime.py --format readme --quiet
(Get-Content README.md) -replace "Última Atualização: .*", "Última Atualização: $CURRENT_DATE" | Set-Content README.md
```

## 📋 Requisitos

- Python 3.6+
- Módulos padrão: `datetime`, `sys`, `argparse`, `typing`

## 🚀 Instalação

Os scripts não requerem instalação adicional, pois utilizam apenas módulos da biblioteca padrão do Python.

## 📝 Convenções

- Todos os scripts devem ter documentação completa
- Usar type hints quando possível
- Incluir tratamento de erros adequado
- Seguir PEP 8 para formatação do código
- Incluir exemplos de uso na documentação

## 🔄 Manutenção

- Atualizar esta documentação quando novos scripts forem adicionados
- Manter compatibilidade com Python 3.6+
- Testar scripts antes de commit
- Documentar mudanças significativas

---

**Última atualização**: 2025-01-03  
**Autor**: Diego Maia 