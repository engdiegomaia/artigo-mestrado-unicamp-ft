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
set "NOME_SAIDA=dissertacao"

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

:: Função para configurar ambiente automatizado
call :setup_automated_build

goto :main_execution

:setup_automated_build
:: Cria todas as pastas necessárias
if not exist "output" mkdir output
if not exist "dist" mkdir dist
if not exist "sections" mkdir sections

:: Cria links simbólicos para assets na pasta src (se não existirem)
cd src
if not exist "figuras" mklink /D figuras ..\assets\figuras >nul 2>&1
if not exist "logotipos" mklink /D logotipos ..\assets\logotipos >nul 2>&1
cd ..

:: Configura variáveis de ambiente LaTeX para automação
set "TEXMFOUTPUT=..\output"
set "BIBINPUTS=.;..\sections;..\src;..\assets;"
set "TEXINPUTS=.;..\sections;..\src;..\assets;"
set "BSTINPUTS=.;..\sections;..\src;"

echo %GREEN%✅ Ambiente automatizado configurado%NC%
exit /b 0

:main_execution

:: Verifica se latexmk está disponível para build automatizado
where latexmk >nul 2>&1
if errorlevel 1 (
    set "USE_LATEXMK=false"
    echo %LIGHTBLUE%ℹ️ latexmk não encontrado - usando método tradicional%NC%
) else (
    set "USE_LATEXMK=true"
    echo %GREEN%✅ latexmk detectado - usando build automatizado%NC%
)

echo %LIGHTBLUE%=== COMPILAÇÃO DA DISSERTAÇÃO ===%NC%
echo %LIGHTBLUE%Estrutura do projeto:%NC%
echo   📁 src/         → Arquivo LaTeX principal
echo   📁 sections/    → Capítulos e seções
echo   📁 output/      → Arquivos temporários
echo   📁 dist/        → PDF final
echo   📁 assets/      → Figuras e logotipos
echo.

:: Escolhe método de compilação
if "%USE_LATEXMK%"=="true" (
    call :automated_build_latexmk
    set "BUILD_SUCCESS=%errorlevel%"
) else (
    call :traditional_build
    set "BUILD_SUCCESS=%errorlevel%"
)

goto :finalize_build

:automated_build_latexmk
echo ^>^>^> %GREEN%Build automatizado com latexmk%NC%
echo ^>^>^> %LIGHTBLUE%Compilação completa em uma execução%NC%
echo.

cd src
latexmk -pdf -bibtex -output-directory=..\output -auxdir=..\output -interaction=nonstopmode -synctex=1 -file-line-error -jobname=%NOME_SAIDA% %NOMEARQCOMPLETO%
set "BUILD_RESULT=%errorlevel%"
cd ..

if %BUILD_RESULT% equ 0 (
    echo %GREEN%✅ Build automatizado concluído com sucesso!%NC%
    exit /b 0
) else (
    echo %RED%❌ Erro no build automatizado%NC%
    exit /b 1
)

:traditional_build
echo ^>^>^> %GREEN%Compilação tradicional (3 passos)%NC%
echo.

:: Primeira compilação
echo ^>^>^> %GREEN%Primeira rodada de compilação%NC%
echo ^>^>^> %LIGHTBLUE%Se houver erros, o script vai parar. Aguarde!%NC%
echo.

cd src
pdflatex -halt-on-error -file-line-error -output-directory=..\output -jobname=%NOME_SAIDA% %NOMEARQCOMPLETO%
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

cd output
biber %NOME_SAIDA%
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

cd output
makeindex %NOME_SAIDA%.nlo -s nomencl.ist -o %NOME_SAIDA%.nls
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
pdflatex -halt-on-error -file-line-error -output-directory=..\output -jobname=%NOME_SAIDA% %NOMEARQCOMPLETO%
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
pdflatex -halt-on-error -file-line-error -output-directory=..\output -jobname=%NOME_SAIDA% %NOMEARQCOMPLETO%
if errorlevel 1 (
    echo %RED%Houve erros durante a terceira compilação.%NC% 1>&2
    cd ..
    exit /b 8
)
cd ..

set "BUILD_SUCCESS=0"
exit /b 0

:finalize_build
:: Finalização do build
for /f "tokens=1-3 delims=/ " %%a in ("%date%") do set YY=%%c& set MM=%%a& set DD=%%b
set TS=%YY:~2%%MM%%DD%
:: Replace the above with robust PowerShell-based timestamp
for /f %%i in ('powershell -NoProfile -Command "(Get-Date).ToString(\"yyMMdd\")"') do set TS=%%i

if %BUILD_SUCCESS% equ 0 (
    if exist "output\%NOME_SAIDA%.pdf" (
        :: Move o PDF final para a pasta dist/
        copy "output\%NOME_SAIDA%.pdf" "dist\%TS%_%NOME_SAIDA%.pdf" >nul
        
        echo COMPILACAO AUTOMATIZADA CONCLUIDA!
        echo PDF gerado: dist\%TS%_%NOME_SAIDA%.pdf
        echo Arquivos temporarios: output\
        echo Secoes organizadas: sections\
        
        :: Mostra informacoes do arquivo final
        for %%I in ("dist\%TS%_%NOME_SAIDA%.pdf") do set "TAMANHO=%%~zI"
        if !TAMANHO! GTR 1048576 (
            set /a "TAMANHO=!TAMANHO!/1048576"
            echo Tamanho do arquivo: !TAMANHO! MB
        ) else if !TAMANHO! GTR 1024 (
            set /a "TAMANHO=!TAMANHO!/1024"
            echo Tamanho do arquivo: !TAMANHO! KB
        ) else (
            echo Tamanho do arquivo: !TAMANHO! bytes
        )
        
        :: Mostra estatisticas do build
        if "%USE_LATEXMK%"=="true" (
            echo Metodo utilizado: Build automatizado - latexmk
        ) else (
            echo Metodo utilizado: Compilacao tradicional - 3 passos
        )
        
        echo.
        echo Dissertacao compilada automaticamente!
        echo Todos os arquivos organizados nas pastas corretas.
        echo.
        exit /b 0
    ) else (
        echo ERRO: PDF nao foi gerado corretamente. 1>&2
        echo Verifique os logs em output\ para mais detalhes. 1>&2
        exit /b 9
    )
) else (
    echo ERRO na compilacao. 1>&2
    echo Verifique os logs em output\ para mais detalhes. 1>&2
    exit /b 9
)

exit /b 0 