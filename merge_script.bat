@echo off
echo === MERGE PARA MAIN ===
git add .
git commit -m "feat: otimizar formatacao A4 e novo titulo - capa proporcional, conflitos corrigidos"
git checkout main
git merge artigo-2
git push origin main
echo === MERGE CONCLUIDO ===
pause