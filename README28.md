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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4dec2c0-98c0-381d-b375-c21e2d2d135d | -17.93698 | -44.57105 | 2024-10-09 01:11:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a04fa716-53cc-3196-a603-cf788c7e1e5e | -17.92504 | -44.57331 | 2024-10-09 01:11:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b88f58d4-4a72-3c1a-a65e-40cfad4d28d0 | -17.90127 | -41.46024 | 2024-10-09 01:11:00 | TERRA_M-M | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.7 |
| ccda3d30-edb2-30ea-b158-2cc874360430 | -17.89858 | -41.45445 | 2024-10-09 01:11:00 | TERRA_M-M | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.6 |
| c720d44a-c648-3e5b-9057-bf0504083a1c | -17.89574 | -41.43024 | 2024-10-09 01:11:00 | TERRA_M-M | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.4 |
| d36840d0-3d17-3987-859f-d583c3272473 | -17.89277 | -41.42408 | 2024-10-09 01:11:00 | TERRA_M-M | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 40.5 |
| 4c67a7cc-e341-3fd5-bf09-d79eff53463e | -17.88299 | -43.2838 | 2024-10-09 01:11:00 | TERRA_M-M | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 429717b3-b165-3c37-81fe-ecff380d514c | -17.86996 | -43.28725 | 2024-10-09 01:11:00 | TERRA_M-M | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| b7e9ee98-6c15-37e9-b4d9-7df9d5b7ae24 | -17.8662 | -57.68572 | 2024-10-09 01:11:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.3 |
| c88e58e0-e8e0-3bca-824d-95b3f38564ce | -17.86381 | -57.66254 | 2024-10-09 01:11:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.8 |
| 84262562-c391-3729-8ed1-0f600f454273 | -17.70775 | -40.18146 | 2024-10-09 01:11:00 | TERRA_M-M | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 32.0 |
| b7e0a926-fbbd-340e-91b6-680d28fca47e | -17.70341 | -40.18743 | 2024-10-09 01:11:00 | TERRA_M-M | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 46.8 |
| 9c992a5c-89dc-373d-ace5-aa118db35f9c | -17.64536 | -53.03176 | 2024-10-09 01:11:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 85dca735-3f86-30f3-a3fe-579aae98820d | -17.59982 | -44.51091 | 2024-10-09 01:11:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| cb8378ce-621d-38d1-a716-d954e84fdbc4 | -16.54462 | -45.28572 | 2024-10-09 01:11:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 02e49832-5e60-35bb-b3e3-b1260ed122c2 | -16.53733 | -45.2937 | 2024-10-09 01:11:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 07593121-6602-3554-9de9-5cdbfcdb6dd7 | -16.53301 | -45.28786 | 2024-10-09 01:11:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 22.0 |
| e2a7dc50-472a-35e6-8f16-58e115054365 | -16.48718 | -43.8156 | 2024-10-09 01:11:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 32.4 |
| f7950b05-1b74-3339-8692-848a0ccb5c70 | -16.2651 | -51.49937 | 2024-10-09 01:11:00 | TERRA_M-M | DIORAMA | GOIÁS | Brasil | 5207105 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e2cac710-2349-3d90-8748-329a8a38fa99 | -16.26382 | -51.49004 | 2024-10-09 01:11:00 | TERRA_M-M | DIORAMA | GOIÁS | Brasil | 5207105 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3eedcfbf-670d-322f-9d72-71954a6e5a33 | -15.18882 | -49.42593 | 2024-10-09 01:11:00 | TERRA_M-M | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2b23d37a-e36d-3e77-ba10-aa8d2d47b113 | -15.18739 | -49.41615 | 2024-10-09 01:11:00 | TERRA_M-M | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 75e7c85f-ebad-3e49-bdb9-070b8a506090 | -15.1797 | -49.42734 | 2024-10-09 01:11:00 | TERRA_M-M | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 23.5 |
| dc983bb5-e6c2-37b7-babb-0a3a7e575dba | -15.17825 | -49.41755 | 2024-10-09 01:11:00 | TERRA_M-M | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 0ae683ca-7e65-3887-9fb4-8b959840c968 | -14.81824 | -46.63486 | 2024-10-09 01:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| ca880cf0-4890-3a6c-ac07-9b0baecd833d | -14.50466 | -43.84314 | 2024-10-09 01:11:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a1b5c240-3f46-370a-ab8d-6d1543464f57 | -14.13902 | -44.95033 | 2024-10-09 01:11:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 89b0a5bf-78ab-3aca-b106-ede1d66f74b4 | -14.11728 | -44.97423 | 2024-10-09 01:11:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| dd1f2d6a-c45c-3bd4-be48-07a186521563 | -14.08506 | -44.16393 | 2024-10-09 01:11:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| e458f67d-5207-3ec4-bfde-95a1f5d0c64f | -14.07199 | -44.4801 | 2024-10-09 01:11:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 8138b66f-6656-3698-a02f-7c4e90afc432 | -14.0616 | -44.48754 | 2024-10-09 01:11:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| fe2e6353-fd47-3778-977b-00af31e4c197 | -14.05801 | -44.4662 | 2024-10-09 01:11:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 005c726d-a477-3cd2-9a87-00883deb0a59 | -13.9379 | -44.53918 | 2024-10-09 01:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 405.1 |
| db3db0b9-3819-3755-80b2-4c69cb6c5ecb | -13.93429 | -44.51811 | 2024-10-09 01:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 951a8ae7-40ba-3fc4-ad3b-372c7c9aa459 | -13.92731 | -44.54659 | 2024-10-09 01:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| b7445335-a51c-38c0-8bfe-57dcdd9ca3a6 | -13.92495 | -44.54158 | 2024-10-09 01:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 8a857d2d-118d-3d48-81bc-905df40ed439 | -13.92385 | -44.52558 | 2024-10-09 01:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 148.5 |
| fa1783fa-13a6-3f37-8041-640714ab0a44 | -13.92133 | -44.52058 | 2024-10-09 01:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 403.5 |
| c443be78-2606-31f9-8f1d-01e532a7a5b7 | -13.92038 | -44.50449 | 2024-10-09 01:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 379db856-341a-33ab-a168-b21e29c6e2a3 | -13.912 | -44.54399 | 2024-10-09 01:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 1ec4b673-b5e2-3015-9211-8f38fda74350 | -13.91091 | -44.52818 | 2024-10-09 01:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 406.9 |
| 671d4573-dc18-323f-a5dc-e088346d48a0 | -13.90839 | -44.52316 | 2024-10-09 01:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 329.5 |
| 93801c66-d314-3382-8d58-a33ce59b0c35 | -13.90742 | -44.50709 | 2024-10-09 01:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 1ee877c7-39c3-361c-89ad-6fa0b83fd980 | -13.89796 | -44.53072 | 2024-10-09 01:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| d21946dd-719c-398e-835e-ef629b2d19d6 | -13.89383 | -44.28291 | 2024-10-09 01:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 8477be89-1363-350f-a3e4-90e3dbb56d73 | -13.84018 | -44.58386 | 2024-10-09 01:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 507.1 |
| 73d56116-fe8e-3487-85df-acc72826be1b | -13.83885 | -44.56923 | 2024-10-09 01:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 4575a3ca-ff83-39f0-bf34-4487766cc05a | -13.83656 | -44.56282 | 2024-10-09 01:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| d761086f-56ab-3f9e-bec9-17a89d4447b8 | -13.80779 | -43.623 | 2024-10-09 01:11:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| bc8d9103-e1e9-3a0e-8c46-f393adccb614 | -13.55048 | -45.44581 | 2024-10-09 01:11:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 81b0bdb2-2b4d-34f1-9ddb-26871bc992de | -13.53836 | -45.44821 | 2024-10-09 01:11:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 3ad1577a-5dd0-3c84-8226-658ed5df63b4 | -13.4068 | -61.92429 | 2024-10-09 01:13:00 | TERRA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 87.4 |
| a79b860b-aea2-3200-aae4-f85cdc0797c3 | -13.39058 | -61.91938 | 2024-10-09 01:13:00 | TERRA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 134.0 |
| c2c42536-b113-30d8-9985-67e13e0869c2 | -13.38938 | -61.92608 | 2024-10-09 01:13:00 | TERRA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 164.5 |
| 5e7b5dc5-3c86-37d5-bba2-991d8ec492be | -13.3772 | -61.96271 | 2024-10-09 01:13:00 | TERRA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 60.9 |
| bb3e48de-aeb7-3565-9600-05659b943626 | -13.37627 | -61.96938 | 2024-10-09 01:13:00 | TERRA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 4358be22-0e53-3ac3-b551-26ab7c9dacbc | -13.29903 | -53.73808 | 2024-10-09 01:13:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 64263a3b-e173-3527-8a36-8bc0557f5982 | -13.15955 | -51.68283 | 2024-10-09 01:13:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 67fbd852-7c7d-34c7-8ce5-c275bb35c630 | -13.1583 | -51.6738 | 2024-10-09 01:13:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3c91a259-0729-3eb2-b11f-335d820e2d86 | -13.10656 | -60.15472 | 2024-10-09 01:13:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 4a37a183-18a5-3d4d-9785-043d4b3f8db2 | -12.84701 | -52.82588 | 2024-10-09 01:13:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 0b07e16a-96e9-3aba-9d02-440181395e4a | -12.73322 | -48.42903 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 161a817b-2984-301e-84c3-d3e86bae2ad4 | -12.73144 | -48.41735 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 54416fb4-1071-3f9e-bb7d-d6931dadc6ae | -12.72332 | -48.43056 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 1b2a7ab7-a312-38f3-a8b7-085aa67088a8 | -12.72152 | -48.41883 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 7d985f99-24ff-3dd1-9121-3d89b1889b7b | -12.67158 | -54.72326 | 2024-10-09 01:13:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| b374a604-6173-3ef0-aae2-1397fff4ae98 | -12.66168 | -54.72468 | 2024-10-09 01:13:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 3d3d3774-2dc9-377b-92db-43cf791f9678 | -12.65615 | -47.03403 | 2024-10-09 01:13:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f01428d6-de89-3b7b-abdf-cdc7f0704cc4 | -12.65471 | -47.04007 | 2024-10-09 01:13:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7f755257-e623-35af-9d6d-85eaf2b9cfe2 | -12.62865 | -53.12075 | 2024-10-09 01:13:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 517021d3-421a-3c8c-b04f-fc8f8e535441 | -12.6183 | -56.51876 | 2024-10-09 01:13:00 | TERRA_M-M | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| e33ff4b4-b47c-3495-be6e-aceb2a7cb915 | -12.616 | -53.02528 | 2024-10-09 01:13:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0604177f-6794-374f-8e29-1e37c1180e10 | -12.60821 | -53.03223 | 2024-10-09 01:13:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| aae0bc25-1ddc-34e7-80e0-3b5eb55820d3 | -12.58611 | -53.07415 | 2024-10-09 01:13:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9887cc20-9131-3561-802b-1515c116ac34 | -12.58483 | -53.06461 | 2024-10-09 01:13:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5127d43c-72cf-36b6-9fcd-71c9d89719e1 | -12.57702 | -53.07542 | 2024-10-09 01:13:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cb2ce2fa-0ef8-3a03-a630-f9ff4ec52799 | -12.57574 | -53.06592 | 2024-10-09 01:13:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 7b2617d4-9cdf-31c9-b2fd-ffaf33e8ce44 | -12.56666 | -53.06721 | 2024-10-09 01:13:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 33a32a32-aee6-34aa-a9ea-61ad958e6993 | -12.48614 | -53.15298 | 2024-10-09 01:13:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 71611cb8-9041-3648-b2f4-a4c23d7c413a | -12.47576 | -53.14471 | 2024-10-09 01:13:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6d6ad308-156e-3c3b-a52d-5ef7ff629fce | -12.47176 | -53.18436 | 2024-10-09 01:13:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 23cd55b7-2391-3945-9b95-8e8fd0ba5ae4 | -12.45748 | -47.31396 | 2024-10-09 01:13:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 520c2c09-b8db-3f3e-bef3-d44b6e8d74db | -12.37376 | -47.68153 | 2024-10-09 01:13:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| fd564b3b-b6f7-3eb7-b259-764e982d5c94 | -12.31871 | -50.9427 | 2024-10-09 01:13:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5e95ca2f-6cb0-3b81-9ad7-9106fd0c63c6 | -12.31603 | -59.17762 | 2024-10-09 01:13:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 24.1 |
| b2652a01-d697-3c12-b02f-fd65dd3184ff | -12.29727 | -57.88411 | 2024-10-09 01:13:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| f640baac-7d3b-3af3-a658-1e2d42040724 | -12.2958 | -57.88995 | 2024-10-09 01:13:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| cfbbfc32-de99-3e8e-943f-66abd1f9fad8 | -12.20497 | -50.59327 | 2024-10-09 01:13:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 73d76b43-591e-3578-abf8-63090f9c95cc | -12.20378 | -46.73282 | 2024-10-09 01:13:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| a9e769d8-85b5-3c0b-a2b1-db0535369d6c | -12.20364 | -50.58398 | 2024-10-09 01:13:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6e2759f9-cc98-3357-ab4d-fd0f40b43488 | -12.20137 | -46.71756 | 2024-10-09 01:13:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 344b29e6-724a-3c03-93e8-f6b199dc01cc | -12.01508 | -51.07207 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e01fef9b-e710-3c3a-a2fd-e77c1ffa3a6f | -12.01379 | -51.06297 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 9e8d2eea-b234-33ac-aa24-71b5e43410f0 | -12.0125 | -51.05387 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| e37458fd-4290-342b-8a4b-72568983e4c1 | -12.00619 | -51.0734 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a57f6d12-c1f3-32e0-a71e-ace893f31aff | -12.0049 | -51.0643 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b50129e8-1394-3fc2-9ed8-e71b36f7acb3 | -12.00361 | -51.0552 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 9ac5f456-cfdf-36f3-a20e-0b48eb3c503f | -11.99601 | -51.06564 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 23.0 |
| e700c84b-d057-3523-89e7-24221f47beba | -11.99471 | -51.05654 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 1b177f1d-0ecd-3096-858b-b893d7a8eea7 | -11.98712 | -51.06697 | 2024-10-09 01:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |


[Clique aqui para ver as próximas entradas](README29.md)
