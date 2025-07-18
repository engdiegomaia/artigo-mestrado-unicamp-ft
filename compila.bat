@echo off
setlocal EnableDelayedExpansion

:: Script de compilação para dissertação UNICAMP-FT (Versão Windows)
:: Adaptado do script bash original
::
:: Autor: Claude (adaptação do script de Diego Maia)
:: Data: 2024-03-19
::
:: Exemplo de utilização:
::    compila.bat tese.tex

:: Cores para output
set "RED=[91m"
set "GREEN=[92m"
set "LIGHTBLUE=[94m"
set "NC=[0m"

:: Verificações iniciais
if "%~1"=="" (
    echo %RED%Você deve informar o nome do arquivo principal como parâmetro%NC% 1>&2
    echo.
    echo Exemplo:
    echo     %~nx0 tese.tex
    echo.
    exit /b 1
)

:: Verifica se o arquivo existe na pasta src/
set "ARQUIVO_ENTRADA=src\%~1"
if not exist "%ARQUIVO_ENTRADA%" (
    echo %RED%Arquivo %ARQUIVO_ENTRADA% não encontrado!%NC% 1>&2
    echo %RED%Certifique-se de que o arquivo está na pasta src/%NC% 1>&2
    exit /b 1
)

:: Variáveis que contêm informações sobre o nome do arquivo
set "NOMEARQCOMPLETO=%~1"
set "NOMEARQ=%~n1"

:: Verifica se os comandos necessários estão no PATH
where pdflatex >nul 2>&1
if errorlevel 1 (
    echo %RED%O compilador pdflatex não está instalado ou não está no PATH%NC% 1>&2
    echo %RED%Acesse o site https://www.tug.org/texlive/acquire-netinstall.html%NC% 1>&2
    exit /b 2
)

where biber >nul 2>&1
if errorlevel 1 (
    echo %RED%O compilador biber não está instalado ou não está no PATH%NC% 1>&2
    echo %RED%Acesse o site https://www.tug.org/texlive/acquire-netinstall.html%NC% 1>&2
    exit /b 2
)

where makeindex >nul 2>&1
if errorlevel 1 (
    echo %RED%O compilador makeindex não está instalado ou não está no PATH%NC% 1>&2
    echo %RED%Acesse o site https://www.tug.org/texlive/acquire-netinstall.html%NC% 1>&2
    exit /b 3
)

:: Cria pastas necessárias se não existirem
if not exist "compilacao" mkdir compilacao
if not exist "dist" mkdir dist

:: Cria links simbólicos para assets na pasta src (se não existirem)
cd src
if not exist "figuras" mklink /D figuras ..\assets\figuras >nul 2>&1
if not exist "logotipos" mklink /D logotipos ..\assets\logotipos >nul 2>&1
cd ..

echo %LIGHTBLUE%=== COMPILAÇÃO DA DISSERTAÇÃO ===%NC%
echo %LIGHTBLUE%Estrutura do projeto:%NC%
echo   📁 src/         → Arquivos LaTeX
echo   📁 compilacao/  → Arquivos temporários
echo   📁 dist/        → PDF final
echo   📁 assets/      → Figuras e logotipos
echo.

:: Primeira compilação
echo ^>^>^> %GREEN%Primeira rodada de compilação%NC%
echo ^>^>^> %LIGHTBLUE%Se houver erros, o script vai parar. Aguarde!%NC%
echo.

cd src
pdflatex -halt-on-error -file-line-error -output-directory=..\compilacao %NOMEARQCOMPLETO%
if errorlevel 1 (
    echo %RED%Houve erros durante a compilação inicial.%NC% 1>&2
    echo %RED%Corrija o erro e execute o script novamente.%NC% 1>&2
    cd ..
    exit /b 4
)
cd ..

echo %GREEN%========== Primeira compilação completa ==========%NC%

:: Referências bibliográficas
echo.
echo ^>^>^> %LIGHTBLUE%Resolvendo as referências bibliográficas.%NC%
echo ^>^>^> %LIGHTBLUE%Aguarde!%NC%

cd compilacao
biber %NOMEARQ%
if errorlevel 1 (
    echo %RED%Houve problemas nas referências bibliográficas.%NC%
    echo %RED%Tente localizar e resolver o problema.%NC%
    cd ..
    exit /b 5
)
cd ..

echo %GREEN%======= Resolução das referências completa ======%NC%

:: Lista de siglas e abreviações
echo.
echo ^>^>^> %LIGHTBLUE%Resolvendo a lista de siglas.%NC%
echo ^>^>^> %LIGHTBLUE%Aguarde!%NC%

cd compilacao
makeindex %NOMEARQ%.nlo -s nomencl.ist -o %NOMEARQ%.nls
if errorlevel 1 (
    echo %RED%Houve problemas na geração da lista de símbolos.%NC%
    echo %RED%Tente localizar e resolver o problema.%NC%
    cd ..
    exit /b 6
)
cd ..

echo %GREEN%======= Resolução da lista de símbolos completa ======%NC%
echo.

:: Segunda compilação
echo ^>^>^> %LIGHTBLUE%Segunda rodada de compilação%NC%
echo ^>^>^> %LIGHTBLUE%Não devem aparecer erros agora. Aguarde!%NC%
echo.

cd src
pdflatex -halt-on-error -file-line-error -output-directory=..\compilacao %NOMEARQCOMPLETO%
if errorlevel 1 (
    echo %RED%Houve erros durante a segunda compilação.%NC% 1>&2
    cd ..
    exit /b 7
)
cd ..

echo %GREEN%======= Segunda rodada de compilação completa =======%NC%
echo.

:: Terceira compilação
echo ^>^>^> %LIGHTBLUE%Terceira rodada de compilação%NC%
echo ^>^>^> %LIGHTBLUE%Finalizando o documento. Aguarde!%NC%
echo.

cd src
pdflatex -halt-on-error -file-line-error -output-directory=..\compilacao %NOMEARQCOMPLETO%
if errorlevel 1 (
    echo %RED%Houve erros durante a terceira compilação.%NC% 1>&2
    cd ..
    exit /b 8
)
cd ..

:: Move o PDF final para a pasta dist/
if exist "compilacao\%NOMEARQ%.pdf" (
    copy "compilacao\%NOMEARQ%.pdf" "dist\%NOMEARQ%.pdf" >nul
    echo %GREEN%======= Compilação concluída com sucesso! =======%NC%
    echo ^>^>^> %LIGHTBLUE%PDF gerado: %GREEN%dist\%NOMEARQ%.pdf%NC%
    echo ^>^>^> %LIGHTBLUE%Arquivos temporários: %GREEN%compilacao\%NC%
    
    :: Mostra informações do arquivo final
    for %%I in ("dist\%NOMEARQ%.pdf") do set "TAMANHO=%%~zI"
    if !TAMANHO! GTR 1048576 (
        set /a "TAMANHO=!TAMANHO!/1048576"
        echo ^>^>^> %LIGHTBLUE%Tamanho do arquivo: %GREEN%!TAMANHO! MB%NC%
    ) else if !TAMANHO! GTR 1024 (
        set /a "TAMANHO=!TAMANHO!/1024"
        echo ^>^>^> %LIGHTBLUE%Tamanho do arquivo: %GREEN%!TAMANHO! KB%NC%
    ) else (
        echo ^>^>^> %LIGHTBLUE%Tamanho do arquivo: %GREEN%!TAMANHO! bytes%NC%
    )
    
    echo.
    echo %GREEN%🎉 Dissertação compilada com sucesso! 🎉%NC%
    echo.
) else (
    echo %RED%Erro: PDF não foi gerado corretamente.%NC% 1>&2
    exit /b 9
)

exit /b 0 