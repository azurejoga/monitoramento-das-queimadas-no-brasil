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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c702886-6b4d-3990-bab4-c19fb13a8242 | -2.9705 | -39.841599 | 2024-12-17 00:09:00 | METOP-C | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3fb14bb1-f2c4-340a-86b2-d5f4fca63163 | -4.6752 | -44.037201 | 2024-12-17 00:09:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9dd5e2b-a4da-3151-98bb-f63f7e4a6e10 | -5.9815 | -41.562 | 2024-12-17 00:09:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8832d59e-69a0-3816-a56d-3a7d03020565 | -5.208 | -43.294998 | 2024-12-17 00:09:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 64560485-9da6-3733-afa9-b6d90cfe1b39 | -4.8762 | -44.1553 | 2024-12-17 00:09:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a63189f-c40b-3c16-99e5-91b3514cf05e | -4.5222 | -44.0424 | 2024-12-17 00:09:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b1ba2c32-01ed-3c1e-b26f-b3bd9b8b8fb2 | -3.1818 | -46.671101 | 2024-12-17 00:09:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 10f613ce-c8d4-3ab0-bd9a-e66247ab391c | -1.2351 | -46.766499 | 2024-12-17 00:09:00 | METOP-C | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4056dd1-2dda-3f0f-a623-0ea623f6a0f4 | -4.886 | -44.153198 | 2024-12-17 00:09:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c1e2052c-4c49-309d-a51f-ba185dd4dca3 | -5.2026 | -44.5611 | 2024-12-17 00:09:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b82f7274-398b-3d20-ab13-e9065ab101ed | -4.3938 | -41.4203 | 2024-12-17 00:09:00 | METOP-C | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ffc5d6fe-16f1-3495-b010-dcc928a6f2cd | -3.9915 | -47.274399 | 2024-12-17 00:09:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45a4e856-28fe-3553-9adb-bb2cfc1a68e2 | -8.9883 | -35.943802 | 2024-12-17 00:09:00 | METOP-C | IBATEGUARA | ALAGOAS | Brasil | 2703007 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| edf69775-bc1b-3cf3-bbba-e8ebe0056151 | -2.0469 | -46.637501 | 2024-12-17 00:09:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9785c17-f87c-3263-8acb-ad4d2aa0f5e6 | -6.1905 | -35.2066 | 2024-12-17 00:09:00 | METOP-C | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3ee583de-e7d1-3a65-b8cf-89098851e3b2 | -4.0922 | -46.714001 | 2024-12-17 00:09:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 63a6dda0-a929-3fcd-869e-f67050c8078e | -3.3275 | -39.689098 | 2024-12-17 00:09:00 | METOP-C | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1110f770-866e-3bf9-be0f-238d9b080a58 | -4.6711 | -44.019299 | 2024-12-17 00:09:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4505171-8fe1-36b2-8b00-334e9c23ce1e | -4.8645 | -41.3601 | 2024-12-17 00:09:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8b6af819-d421-324e-920b-325f584de50b | -6.8556 | -44.759998 | 2024-12-17 00:09:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 207649ec-9d03-3827-abaf-f73c511352fb | -4.7001 | -44.378601 | 2024-12-17 00:09:00 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e565ec1-94b2-3691-b506-80ffe15d4c85 | -0.7492 | -47.736801 | 2024-12-17 00:09:00 | METOP-C | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 765edc5d-c4cb-3249-ba36-d6e3ab483825 | -7.5679 | -35.097401 | 2024-12-17 00:09:00 | METOP-C | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8d635c78-6acd-312c-b689-eb966c82f999 | -3.8374 | -45.845501 | 2024-12-17 00:09:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 99c739a4-3f88-38cd-8353-c9ce747353ec | -5.5553 | -37.989101 | 2024-12-17 00:09:00 | METOP-C | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 188ec21f-afb8-3a6c-baf5-07d4e7c14640 | -1.2227 | -46.756802 | 2024-12-17 00:09:00 | METOP-C | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bd20483-7701-345f-90a7-0332c5562131 | -4.9628 | -44.959702 | 2024-12-17 00:09:00 | METOP-C | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d1e0bb9-2947-34c0-bf88-09592e4be4eb | -3.2393 | -46.790798 | 2024-12-17 00:09:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f82bbf0e-41bd-3a99-a73d-b45166a2cf56 | -9.9629 | -36.527802 | 2024-12-17 00:09:00 | METOP-C | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 934e508d-705a-3d39-8186-51ddf58b69dd | -4.698 | -44.369202 | 2024-12-17 00:09:00 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4988f95e-809d-3580-8337-e7d1df6e1cb5 | -5.1791 | -37.526299 | 2024-12-17 00:09:00 | METOP-C | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| eba09418-b622-3edb-ae1e-aba26f956eca | -6.2091 | -46.206501 | 2024-12-17 00:09:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc05387b-3e1c-315b-afe8-7cb907dc42c7 | -4.6829 | -44.0261 | 2024-12-17 00:09:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a7531ca-11f0-387f-b1cb-956de31e0327 | -3.3152 | -53.3744 | 2024-12-17 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 06dde8bb-7349-388c-a6f7-9f6824ba9113 | -5.0936 | -43.9176 | 2024-12-17 00:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 336.1 |
| 083983e3-da84-3908-bed8-a80840de6cbe | -5.0938 | -43.8945 | 2024-12-17 00:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 178.3 |
| e7255cad-bf44-3580-b02c-0c289975847e | 4.4435 | -60.9657 | 2024-12-17 00:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 97.3 |
| c93e9b6f-ffe8-3809-9dc4-5af4eb105111 | -5.0751 | -43.8958 | 2024-12-17 00:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 139.0 |
| aa90d88e-d1d7-3e26-97e1-0285d35242fc | -18.8994 | -56.056 | 2024-12-17 00:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.7 |
| 586cde17-6a4c-38d1-a145-317055ca0da1 | -3.2968 | -53.3749 | 2024-12-17 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 689baf51-4e3e-3be3-9c8f-b58499fd1b77 | -6.1953 | -46.2215 | 2024-12-17 00:10:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 74586edf-4c3c-3518-8082-328a1b3586c3 | -3.2969 | -53.3547 | 2024-12-17 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| f963efba-3b2e-32fa-919b-e173a9c536af | -1.4147 | -47.4665 | 2024-12-17 00:10:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| f30935d8-1633-3bf6-ae0d-e6513b3651de | -5.1365 | -43.2419 | 2024-12-17 00:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| b177056d-7941-3ec5-97e0-5ee8b0d4550a | -5.1123 | -43.9164 | 2024-12-17 00:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 7b90a47b-00fa-3712-9bbc-8bc3014fc41f | -5.0749 | -43.9189 | 2024-12-17 00:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 215.1 |
| dfb3dc10-eae5-3678-bcab-3f9c2cf01a96 | -4.8861 | -44.1613 | 2024-12-17 00:10:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 116.8 |
| b6794c13-d2a6-3bae-89cd-1e2218f0c517 | -19.0842 | -52.8527 | 2024-12-17 00:10:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 76cca23a-9126-31e5-8bba-f909baa8a048 | -19.0837 | -52.8745 | 2024-12-17 00:10:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 82.7 |
| fd7cf98e-d3f3-3c3c-bc29-0eaad26bf06a | 4.4618 | -60.9653 | 2024-12-17 00:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 8cdf5da5-1b49-394f-a282-fecb4eab6677 | -6.214 | -46.2202 | 2024-12-17 00:10:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 89170eb8-1daa-3ebc-ac2e-58fc7fd01156 | -4.7952 | -46.4012 | 2024-12-17 00:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 59fc5b7c-96b6-35fb-8b21-c66f8798d3d1 | -15.0865 | -59.6487 | 2024-12-17 00:10:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| a4a072ba-4307-307d-9fa1-8ce3ae06c2cc | -3.1503 | -53.1762 | 2024-12-17 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| bfb10014-dfb4-3447-b31d-42cfebfe23e1 | -19.1043 | -52.8493 | 2024-12-17 00:10:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 762d7f30-cca7-31df-a7bd-022e6ea81df7 | -4.886 | -44.1843 | 2024-12-17 00:10:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 167.1 |
| 9155b011-8b1e-36c1-9577-27ff083dbdce | -4.9047 | -44.1831 | 2024-12-17 00:10:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 5eef64e9-13b6-30bd-833e-3b1262d7dac3 | -3.2969 | -53.3547 | 2024-12-17 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| cf8fb983-0b85-3537-93e5-9114f911b8c8 | -6.214 | -46.2202 | 2024-12-17 00:20:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 569336d8-ee3a-3268-9556-3ba834280fb7 | -5.0938 | -43.8945 | 2024-12-17 00:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 208.9 |
| ccc40be5-b19b-3b8d-b09e-42d50b0d5854 | -5.0936 | -43.9176 | 2024-12-17 00:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 405.2 |
| 04f1aa83-1523-370b-8c4a-c8f02d277ba7 | -18.8994 | -56.056 | 2024-12-17 00:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.6 |
| 6488750b-4c18-3af6-8b92-bdca76c4bedd | -19.1043 | -52.8493 | 2024-12-17 00:20:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 2666a655-3e87-35aa-be3d-9ecd1a1fe169 | -5.0749 | -43.9189 | 2024-12-17 00:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 0c1153be-e6d1-3e0a-a3b9-87fd2e59a3ab | -19.0837 | -52.8745 | 2024-12-17 00:20:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 2a970633-1935-39b4-8b3e-4f3058e65c4d | -4.7952 | -46.4012 | 2024-12-17 00:20:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 083de9aa-b12d-3255-8166-e943166760fc | -10.0682 | -36.1275 | 2024-12-17 00:20:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 112.1 |
| a2103582-3dbe-3591-8e39-5dc321bea6bd | -4.886 | -44.1843 | 2024-12-17 00:20:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| fc3601c3-8122-3817-a2c7-8400d4a6201a | -3.1503 | -53.1762 | 2024-12-17 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| adfc5e07-f223-361b-8a07-c939f47757ca | -3.3153 | -53.3541 | 2024-12-17 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| ae44afca-7488-3cfc-879f-60537f9ce358 | -3.3152 | -53.3744 | 2024-12-17 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 31f05d70-7333-3953-95f3-b1742fcf356b | -1.3962 | -47.4667 | 2024-12-17 00:20:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| c655ba83-40df-384d-a6f4-92f2d7bbc1b2 | -3.2506 | -46.8049 | 2024-12-17 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 0c33720b-e3d8-36ad-8cbf-04d27a35232d | -5.1365 | -43.2419 | 2024-12-17 00:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| fa4c7b76-087e-3a94-b1ff-44cf5a715ff8 | -3.2968 | -53.3749 | 2024-12-17 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 418235c6-d5de-3f93-8159-70c5f5717deb | -6.1953 | -46.2215 | 2024-12-17 00:20:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 00a38e3e-8142-390f-9fda-4aee5b001651 | -5.1123 | -43.9164 | 2024-12-17 00:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 072cee41-3b68-301f-a7bc-602361242040 | -19.0842 | -52.8527 | 2024-12-17 00:20:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 2f678e92-8ba9-39fe-b7ac-2e17adcb2c70 | -5.0751 | -43.8958 | 2024-12-17 00:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 124.8 |
| d6f1dc67-4e2e-3fd6-8d19-baf1a0570206 | 4.4435 | -60.9657 | 2024-12-17 00:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 98.2 |
| d5727860-4b66-35a6-9217-a7134038507e | -19.1038 | -52.8711 | 2024-12-17 00:20:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 83.4 |
| d0e73401-ad4d-366f-a549-8cd94865919c | -15.0865 | -59.6487 | 2024-12-17 00:20:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| f6ce7e2b-ea59-323f-aaea-cf144b961778 | 4.4435 | -60.9657 | 2024-12-17 00:30:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 37f109b8-d72d-3f55-a20c-46e0d3935238 | -1.4147 | -47.4665 | 2024-12-17 00:30:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| fa3b3700-a9c7-3ad6-91cc-4a87b0437845 | -5.1123 | -43.9164 | 2024-12-17 00:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 64db5950-a3f7-38d8-82d8-98b99bd1c837 | -5.0938 | -43.8945 | 2024-12-17 00:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 222.8 |
| 8f189bb3-0008-353b-b086-c127877ae95c | -5.0936 | -43.9176 | 2024-12-17 00:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 345.6 |
| 1dade6f6-173f-3716-b112-5c41bbf30eec | -5.0751 | -43.8958 | 2024-12-17 00:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 173.0 |
| f236db52-2387-3f76-a295-e4cc42fe4ef8 | -6.2142 | -46.1978 | 2024-12-17 00:30:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 6ccae455-963e-388f-8174-a8340a3c3495 | -3.2968 | -53.3749 | 2024-12-17 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| df24d6ed-824b-340f-a0f6-3a8671adca69 | -6.1953 | -46.2215 | 2024-12-17 00:30:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| ff0d6afb-9b94-3928-8a0d-98dceb813714 | -4.886 | -44.1843 | 2024-12-17 00:30:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 739084ec-a231-3e72-aca8-2366f34498c8 | -5.0749 | -43.9189 | 2024-12-17 00:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 225.1 |
| bbfd28fd-4ee5-33fa-aac1-291129cf9c05 | -4.2337 | -44.0159 | 2024-12-17 00:30:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 37b9706d-bddd-3020-abf4-d93ebd14169e | -3.1503 | -53.1762 | 2024-12-17 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| a491c416-551a-3c2a-a2d5-353eb8aaadb6 | -6.214 | -46.2202 | 2024-12-17 00:30:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 08dda7f9-fd33-3eb0-bbd7-7a78acb860ff | -5.1365 | -43.2419 | 2024-12-17 00:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 7951ee93-ad17-32a6-8f3a-ae13c95830b0 | -3.2969 | -53.3547 | 2024-12-17 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| d653f22f-f387-33f4-96e9-b87915b18893 | -5.1365 | -43.2419 | 2024-12-17 00:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 9846f24c-51e5-3a1a-aada-93f9073aeee5 | -5.1125 | -43.8933 | 2024-12-17 00:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |


[Clique aqui para ver as próximas entradas](README4.md)
