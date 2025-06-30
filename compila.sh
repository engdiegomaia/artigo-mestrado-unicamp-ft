#!/bin/bash
#
# Script de compilação para dissertação UNICAMP-FT
# Adaptado para nova estrutura organizacional do projeto
#
# Autor: Diego Maia
# Data: 2024-12-19
#
# Exemplo de utilização:
#    ./compila.sh tese.tex
#
# Verificações iniciais
if [ $# -ne 1 ]; then
  echo "Você deve informar o nome do arquivo principal como parâmetro" 1>&2
  echo -e "Exemplo:\n\t $0 tese.tex\n" 1>&2
  exit 1
fi

# Verifica se o arquivo existe na pasta src/
ARQUIVO_ENTRADA="src/$1"
if [ ! -f "$ARQUIVO_ENTRADA" ]; then
  echo "Arquivo $ARQUIVO_ENTRADA não encontrado!" 1>&2
  echo "Certifique-se de que o arquivo está na pasta src/" 1>&2
  exit 1
fi

# Variáveis que contêm informações sobre o nome do arquivo
NOMEARQCOMPLETO=$1
NOMEARQ=`basename "${NOMEARQCOMPLETO}" .tex`

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
LIGHTBLUE='\033[1;34m'
NC='\033[0m' # No Color

# Verifica se os comandos necessários estão instalados
PDFLATEX=`which pdflatex 2>/dev/null`
PDFLATEX="${PDFLATEX} -halt-on-error -file-line-error"
if [ $? -eq 1 ]; then 
  echo "O compilador pdflatex não está instalado" 1>&2
  echo "Acesse o site https://www.tug.org/texlive/acquire-netinstall.html" 1>&2
  exit 2
fi

BIBER=`which biber 2>/dev/null`
if [ $? -eq 1 ]; then
  echo "O compilador biber não está instalado" 1>&2
  echo "Acesse o site https://www.tug.org/texlive/acquire-netinstall.html" 1>&2
  exit 2
fi

MAKEINDEX=`which makeindex 2>/dev/null`
if [ $? -eq 1 ]; then
  echo "O compilador makeindex não está instalado" 1>&2
  echo "Acesse o site https://www.tug.org/texlive/acquire-netinstall.html" 1>&2
  exit 3
fi

# Cria pastas necessárias se não existirem
mkdir -p compilacao dist

# Cria links simbólicos para assets na pasta src (se não existirem)
cd src
if [ ! -L "figuras" ]; then
  ln -sf ../assets/figuras figuras 2>/dev/null
fi
if [ ! -L "logotipos" ]; then
  ln -sf ../assets/logotipos logotipos 2>/dev/null
fi
cd ..

echo -e "${LIGHTBLUE}=== COMPILAÇÃO DA DISSERTAÇÃO ===${NC}"
echo -e "${LIGHTBLUE}Estrutura do projeto:${NC}"
echo -e "  📁 src/         → Arquivos LaTeX"
echo -e "  📁 compilacao/  → Arquivos temporários"
echo -e "  📁 dist/        → PDF final"
echo -e "  📁 assets/      → Figuras e logotipos\n"

# Primeira compilação
echo -e ">>> ${GREEN}Primeira rodada de compilação${NC}"
echo -e ">>> ${LIGHTBLUE}Se houver erros, o script vai parar. Aguarde!${NC}\n"

cd src
${PDFLATEX} -output-directory=../compilacao ${NOMEARQCOMPLETO} | \
            awk 'BEGIN{IGNORECASE = 1}/warning|!/,/^$/;'

if [ ${PIPESTATUS[0]} -ne 0 ]; then
  echo -e "${RED}Houve erros durante a compilação inicial.${NC}" 1>&2
  echo -e "${RED}Corrija o erro e execute o script novamente.${NC}\n" 1>&2
  cd ..
  exit 4
fi
cd ..

echo -e "${GREEN}========== Primeira compilação completa ==========${NC}"

# Referências bibliográficas
echo -e "\n>>> ${LIGHTBLUE}Resolvendo as referências bibliográficas.${NC}"
echo -e ">>> ${LIGHTBLUE}Aguarde!${NC}"

cd compilacao
${BIBER} ${NOMEARQ}
if [ $? -ne 0 ]; then
  echo -e "${RED}Houve problemas nas referências bibliográficas.${NC}"
  echo -e "${RED}Tente localizar e resolver o problema.${NC}"
  cd ..
  exit 5
fi
cd ..

echo -e "${GREEN}======= Resolução das referências completa ======${NC}"

# Lista de siglas e abreviações
echo -e "\n>>> ${LIGHTBLUE}Resolvendo a lista de siglas.${NC}"
echo -e ">>> ${LIGHTBLUE}Aguarde!${NC}"

cd compilacao
ARQNLO="${NOMEARQ}.nlo"
ARQNLS="${NOMEARQ}.nls"
NOMENCL="nomencl.ist"

${MAKEINDEX} ${ARQNLO} -s ${NOMENCL} -o ${ARQNLS}
if [ $? -ne 0 ]; then
  echo -e "${RED}Houve problemas na geração da lista de símbolos.${NC}"
  echo -e "${RED}Tente localizar e resolver o problema.${NC}"
  cd ..
  exit 6
fi
cd ..

echo -e "${GREEN}======= Resolução da lista de símbolos completa ======${NC}\n"

# Segunda compilação
echo -e ">>> ${LIGHTBLUE}Segunda rodada de compilação${NC}" 
echo -e ">>> ${LIGHTBLUE}Não devem aparecer erros agora. Aguarde!${NC}\n"

cd src
${PDFLATEX} -output-directory=../compilacao ${NOMEARQCOMPLETO} | \
            awk 'BEGIN{IGNORECASE = 1}/warning|!/,/^$/;'

if [ ${PIPESTATUS[0]} -ne 0 ]; then
  echo -e "${RED}Houve erros durante a segunda compilação.${NC}" 1>&2
  cd ..
  exit 7
fi
cd ..

echo -e "${GREEN}======= Segunda rodada de compilação completa =======${NC}\n"

# Terceira compilação
echo -e ">>> ${LIGHTBLUE}Terceira rodada de compilação${NC}"
echo -e ">>> ${LIGHTBLUE}Finalizando o documento. Aguarde!${NC}\n"

cd src
${PDFLATEX} -output-directory=../compilacao ${NOMEARQCOMPLETO} | \
            awk 'BEGIN{IGNORECASE = 1}/warning|!/,/^$/;'

if [ ${PIPESTATUS[0]} -ne 0 ]; then
  echo -e "${RED}Houve erros durante a terceira compilação.${NC}" 1>&2
  cd ..
  exit 8
fi
cd ..

# Move o PDF final para a pasta dist/
if [ -f "compilacao/${NOMEARQ}.pdf" ]; then
  cp "compilacao/${NOMEARQ}.pdf" "dist/${NOMEARQ}.pdf"
  echo -e "${GREEN}======= Compilação concluída com sucesso! =======${NC}"
  echo -e ">>> ${LIGHTBLUE}PDF gerado: ${GREEN}dist/${NOMEARQ}.pdf${NC}"
  echo -e ">>> ${LIGHTBLUE}Arquivos temporários: ${GREEN}compilacao/${NC}"
  
  # Mostra informações do arquivo final
  if command -v du >/dev/null 2>&1; then
    TAMANHO=$(du -h "dist/${NOMEARQ}.pdf" | cut -f1)
    echo -e ">>> ${LIGHTBLUE}Tamanho do arquivo: ${GREEN}${TAMANHO}${NC}"
  fi
  
  echo -e "\n${GREEN}🎉 Dissertação compilada com sucesso! 🎉${NC}\n"
else
  echo -e "${RED}Erro: PDF não foi gerado corretamente.${NC}" 1>&2
  exit 9
fi

exit 0
