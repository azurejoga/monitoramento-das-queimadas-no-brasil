# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2064ec52-4481-3b4c-b5a4-c35935fec670 | -5.86991 | -45.90513 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10a59aa5-0c12-378c-8d1d-e74f3524d1f8 | -5.6628 | -45.03845 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19c665f4-2e6e-3fb9-9f2e-248c1a508666 | -6.12115 | -43.38579 | 2025-09-18 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac72d950-3d86-3860-81e7-dd5848603deb | -5.90292 | -45.72404 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94ea7bcc-830f-3225-9eaf-9b244920e079 | -5.95291 | -47.01372 | 2025-09-18 04:12:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 243ec71f-da33-3d07-ab76-ccd999567bc5 | -6.55753 | -43.59011 | 2025-09-18 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d14c4dca-03d6-3201-9575-b5eee75f2edb | -4.65536 | -47.56242 | 2025-09-18 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85b46a75-fd11-3c33-9d05-de4b5f2268dd | -3.15857 | -43.25975 | 2025-09-18 04:12:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 57156374-a071-3470-a010-dbe17eb82c24 | -5.80716 | -45.90751 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4093c5ce-9e99-3d4b-92cd-b631399b78e9 | -3.30564 | -48.71471 | 2025-09-18 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fedbb9e1-0280-3d10-9b16-3ad4fe341e18 | -0.91136 | -47.54636 | 2025-09-18 04:12:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f969ca5-19ee-31e5-8ad0-b19f6e4aa553 | -5.06627 | -41.16381 | 2025-09-18 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0fed5b5a-96ee-36e1-99ac-5d1a00218be4 | -4.66721 | -46.31811 | 2025-09-18 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60a02d86-f409-38f8-86a4-1f61d81118c2 | -6.44889 | -44.50928 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a52e2147-06ef-3109-b5c0-47e0b2cbdf39 | -6.40206 | -43.3277 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df653363-4096-3d63-97e5-c00e04c2e8d1 | -7.03467 | -44.17886 | 2025-09-18 04:12:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fbb1817a-12b3-30b5-9df4-834c689f1f57 | -5.8085 | -45.89939 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 124ad5fe-4762-33b3-b665-e395cfb1b4c1 | -3.24744 | -48.76838 | 2025-09-18 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b1c1278-4158-33a9-b77a-32605073dcfd | -3.13862 | -44.42448 | 2025-09-18 04:12:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33dccbfc-5d0a-3cf3-90ed-5cdfc3a578a2 | -5.32611 | -44.99372 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0d927aba-8ea1-3f22-9348-9c9aaa30a3d2 | -5.54103 | -44.96576 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f8f46e0-5ca9-3a3a-95fc-b129fd55fbca | -6.67782 | -45.30891 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a986af0a-8155-388b-a4af-92fa02c98b51 | -5.81093 | -45.9291 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1662d81-5e48-3478-b4e5-fefbe198764d | -5.81228 | -45.92092 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18872a54-488e-344f-a2f3-5a934b2d3407 | -5.79357 | -43.93114 | 2025-09-18 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9cd55deb-63ef-354b-b2d8-c4ecd61ae660 | -3.84476 | -40.36827 | 2025-09-18 04:12:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9e4ac96f-6238-3094-b04b-641ca7b5057f | -4.10367 | -40.47992 | 2025-09-18 04:12:00 | NOAA-20 | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ecdf1fb6-f62e-3c53-8b9d-536c2c92b66e | -5.8904 | -45.89175 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0944739e-6ebe-31c5-98cc-f60c31471383 | -2.29698 | -48.14478 | 2025-09-18 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fbf2eccd-0593-3b86-ba60-234552690d76 | -5.63032 | -43.88728 | 2025-09-18 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f726c11a-3c12-3940-82a2-8d1d6c87a181 | -4.69923 | -41.95308 | 2025-09-18 04:12:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 10a31b01-218b-34b1-9ea0-1d4582c19515 | -5.8547 | -45.88602 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8ce34793-7768-39b5-a2a6-bacff4503cad | -6.55421 | -43.5896 | 2025-09-18 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2b695f5d-ee7a-3b6b-974f-59347ae511a0 | -5.80783 | -45.90344 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae10e78a-1c49-3856-9e1a-3c39cb8ac778 | -6.3341 | -44.24493 | 2025-09-18 04:12:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3164f324-5507-3df5-8c4c-724b5ca0bc1a | -5.89397 | -45.89232 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9205e9e9-e4c3-3b8e-9710-7700c83941b3 | -6.39325 | -43.34051 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7be97f2-5a45-3464-b507-b9fb07a9c76f | -6.5213 | -44.14054 | 2025-09-18 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8302aa76-222e-35b5-b00d-6ed1fb0e37de | -6.95599 | -44.56386 | 2025-09-18 04:12:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1e1247d1-575e-318d-8080-a43be06e4113 | -5.94842 | -47.01575 | 2025-09-18 04:12:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30680101-7f7e-3464-af07-a6b86090907c | -2.96104 | -48.5891 | 2025-09-18 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7784f22-7386-3456-aa57-6019a2dc43ed | -5.21923 | -45.18082 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6e127fa2-27ec-3ed6-97b4-0643062f62cf | -5.95779 | -45.03421 | 2025-09-18 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2c8668f-7a74-337e-b19b-5ab40a0c0249 | -5.48739 | -45.40513 | 2025-09-18 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 06c81b41-b614-360a-9276-99dc731a1e2c | -3.74197 | -49.05344 | 2025-09-18 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a019e017-380c-3f77-9b40-4941f1f1a966 | -6.54737 | -44.01456 | 2025-09-18 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ef0b70b-df95-3507-bc33-98042a7bed49 | -5.47615 | -44.32224 | 2025-09-18 04:12:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68e945fa-0476-309e-84b1-f463d8799a24 | -6.48434 | -43.90027 | 2025-09-18 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a25ae06d-bf28-3c62-8362-aa0517605439 | -5.81944 | -45.92204 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a901fc1-ea76-3c1b-a805-e40e217eda67 | -6.39875 | -43.32719 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4685450-0bc5-35f6-9a66-d0210bf9f0e4 | -5.53419 | -42.17226 | 2025-09-18 04:12:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| aa96bc23-a16e-3eca-977d-d78b864470ac | -5.44069 | -46.68205 | 2025-09-18 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28c96054-2d19-349d-b9ca-31cb59f74e5f | -6.94445 | -35.18597 | 2025-09-18 04:12:00 | NOAA-20 | CUITÉ DE MAMANGUAPE | PARAÍBA | Brasil | 2505238 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c592c4ee-0e5e-369f-8a84-96f524c0fc42 | -6.75268 | -46.00232 | 2025-09-18 04:12:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d368bee6-d364-3f50-92da-188c75f4b9a3 | -5.95718 | -45.03798 | 2025-09-18 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b70fb28-0e29-3666-832f-2c9a055a1bad | -6.99715 | -44.89828 | 2025-09-18 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3879ecc-7936-3def-bec2-92ff99f6e79d | -6.58655 | -41.3867 | 2025-09-18 04:12:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 408b8bad-4493-3f02-b83d-c89782cd9355 | -5.04945 | -43.09497 | 2025-09-18 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf0f2d8b-45d9-3243-9853-17234ec2924a | -6.87606 | -43.95934 | 2025-09-18 04:12:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f2e8ec0-bf44-3a4f-8e7c-deaf34eb766e | -5.80842 | -45.90898 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2b675bb-4765-3cd4-9951-c19566d27bf0 | -6.41389 | -42.66997 | 2025-09-18 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 68644d7f-18e9-3d72-a27e-e11805895aad | -3.27149 | -52.42213 | 2025-09-18 04:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59dc0499-5a35-39c0-9fda-024f9c348890 | -7.00458 | -44.61613 | 2025-09-18 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8a35c9a2-adc4-3c84-8b5f-7c24181332b0 | -5.88564 | -45.65178 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b58e6ab5-5722-3897-bfb9-4e88bf3575c8 | -4.69706 | -41.967 | 2025-09-18 04:12:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f2422932-f3bc-36e6-a1bb-ab4db9349703 | -6.58995 | -41.38722 | 2025-09-18 04:12:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 44586927-8db4-3d0e-8eff-3a221ddcf64a | -5.7687 | -43.70063 | 2025-09-18 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee87af24-3da6-3673-9ef0-83cf269bd0b3 | -3.34904 | -39.28017 | 2025-09-18 04:12:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f3036dc8-f5ab-38ed-bcb6-3cc0193b78b0 | -3.83669 | -40.37469 | 2025-09-18 04:12:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 87418eb7-bf71-3546-8597-3ae9a7d44eae | -3.83728 | -40.37096 | 2025-09-18 04:12:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6e643adf-60cd-3465-b82a-fd90f4038456 | -6.22728 | -43.14384 | 2025-09-18 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bf3de4a5-36bf-38ec-b8f8-5ad173a0cbed | -6.19424 | -45.11301 | 2025-09-18 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8cf7929-26e1-3467-a221-e5c5a45cd079 | -6.43249 | -44.37434 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c21d5b37-028e-3d3d-8c3a-47d75a66c649 | -7.05731 | -44.35329 | 2025-09-18 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9038c931-d075-3574-9e34-18b8721e887d | -3.1539 | -49.48128 | 2025-09-18 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20f3608e-2ebd-38be-aa97-8d7cceef9677 | -2.64108 | -48.04857 | 2025-09-18 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28d4f533-0aa2-3034-9084-a68ec0360700 | -3.05035 | -45.10818 | 2025-09-18 04:12:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ca2beb5a-33ca-3696-afc8-e84fb59e2b57 | -7.0319 | -44.17481 | 2025-09-18 04:12:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3f9a8b6-7d73-3ed3-bc6a-a22c592d8b2d | -5.67128 | -43.15823 | 2025-09-18 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 294de933-5a07-32f5-a721-01e9db696bad | -4.24605 | -48.27316 | 2025-09-18 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b79b359-5751-337b-828b-1a7be964d11d | -3.05278 | -47.01162 | 2025-09-18 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 00f0cac8-b5f3-3b75-bc11-43827ac50069 | -3.85519 | -40.3468 | 2025-09-18 04:12:00 | NOAA-20 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ae79cc64-bd4b-30e2-8666-770eb09f1126 | -6.86859 | -44.17423 | 2025-09-18 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0b9eb06-898e-3ca8-9454-15cdd6e5236c | -6.26992 | -45.12137 | 2025-09-18 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76e1e0ff-f763-33bf-a769-45a2e1fd499e | -6.45292 | -43.30682 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e021ef7-5b57-30a2-8b7c-08609836d124 | -6.60014 | -45.64513 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 839eedfd-fce0-30a2-bd5a-7b3a48dd8dfd | -6.41912 | -43.30557 | 2025-09-18 04:12:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4d1f0bd-9449-382d-8d61-14844d87dfa6 | -5.78062 | -45.96777 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80e58f4f-2b2a-3a8f-a76a-09c5f2b02c4f | -3.75105 | -47.69054 | 2025-09-18 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 147fb356-ee7c-324f-a222-b2a1b2aa2aae | -3.89357 | -38.4411 | 2025-09-18 04:12:00 | NOAA-20 | EUSÉBIO | CEARÁ | Brasil | 2304285 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 03a04fc6-5005-33c2-8bd4-dadc6013bee6 | -4.55357 | -41.49221 | 2025-09-18 04:12:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fb4bcb16-7207-3d15-b9dc-111f7e7d187f | -6.21024 | -45.12324 | 2025-09-18 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d49ad45-a495-3e56-9a9d-288096275f4b | -6.2353 | -49.22539 | 2025-09-18 04:12:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cba5250-9ef2-3744-a069-0c75b1f3c428 | -5.80907 | -45.9049 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c0a2053-a871-3a66-aae8-3ba0e4dc1fe8 | -7.06009 | -44.35739 | 2025-09-18 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f358df58-6223-3e1e-bba6-ea67fdf68bef | -6.68127 | -45.30951 | 2025-09-18 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d96f8f3-8226-3715-9e0f-70cdea834742 | -1.61407 | -46.66943 | 2025-09-18 04:12:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a16b5a11-5395-3462-a44d-3637d3069f47 | -6.31286 | -42.40514 | 2025-09-18 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 18829806-7b21-3567-bb2e-39fd66ac2d5d | -6.7727 | -44.7049 | 2025-09-18 04:12:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 33bfdfbe-d0f2-30f9-9b1f-70c272884851 | -5.80938 | -45.91624 | 2025-09-18 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README12.md)
