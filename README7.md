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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42093aa8-da06-3cfa-954c-4b72788ad5f7 | -1.20605 | -47.92137 | 2025-11-24 04:33:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b66cc7a2-61a3-3b21-acd5-0e00d86046dd | 2.2282 | -50.87976 | 2025-11-24 04:33:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 221ba58e-f3c2-32fc-9292-b04ac8538227 | -1.82764 | -45.57782 | 2025-11-24 04:36:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50a64d16-78d1-3d16-8a55-313ea0052315 | -3.28007 | -48.80715 | 2025-11-24 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ba0ebde-775b-35af-a6eb-3ae9e5e277a3 | -2.92671 | -48.23693 | 2025-11-24 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 448cb330-bbc6-3575-8539-277dc9a16cdf | -4.3421 | -44.32825 | 2025-11-24 04:36:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97f510d2-eca1-3a0e-9016-e95b1e85814f | -2.92783 | -48.22984 | 2025-11-24 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5ff7b0fe-8b83-36e3-a1e5-d6804d1cfa78 | -3.83676 | -50.74972 | 2025-11-24 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 534c16ec-2d79-32c6-9e19-5a3ca68e60b3 | -3.43035 | -52.63112 | 2025-11-24 04:36:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63a07295-80b6-3d21-9973-13b1600085dd | -3.3975 | -47.57015 | 2025-11-24 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d56c62ae-0a59-3a7c-9223-9758536dcb07 | -3.60444 | -55.46751 | 2025-11-24 04:36:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5e6fc14b-09d8-3796-b169-61a8ef523fc2 | -2.87877 | -45.26818 | 2025-11-24 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 51fa7445-e549-3f48-a411-b68955a6f1f0 | -4.12881 | -45.22359 | 2025-11-24 04:36:00 | NPP-375D | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa86bc9d-4c45-3028-ad8c-29cf696fdcd7 | -2.88107 | -51.80753 | 2025-11-24 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7593a7f7-13f6-303a-8161-a5805ea0558c | -2.87078 | -51.79549 | 2025-11-24 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5a71e825-a795-3e22-bae8-384cc4a78c5f | -4.45558 | -45.76982 | 2025-11-24 04:36:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 436d8f43-868b-3a0f-9f6e-3ebba0087d4f | -2.16187 | -45.98705 | 2025-11-24 04:36:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59b3b256-0db0-3d58-9c78-ed4a22bb0d01 | -4.82337 | -43.82655 | 2025-11-24 04:36:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 93371235-c4a1-34a9-9b2d-5aa13895aeaa | -6.84131 | -46.27307 | 2025-11-24 04:36:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f47f9d88-a433-3d79-8ba1-0b6f4ac0fe4d | -4.26955 | -40.85913 | 2025-11-24 04:36:00 | NPP-375D | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 08fbfef7-64b4-3a83-804b-a0d943908d34 | -3.96492 | -43.9677 | 2025-11-24 04:36:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 195ffe20-3435-3e7f-8aae-97dc09293a06 | -2.43611 | -44.02517 | 2025-11-24 04:36:00 | NPP-375D | RAPOSA | MARANHÃO | Brasil | 2109452 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c8051f59-9f2e-3065-ab75-91a35830876c | -2.93063 | -48.23391 | 2025-11-24 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e507c06-abee-306f-9629-162b2f50e6f9 | -3.28811 | -43.4002 | 2025-11-24 04:36:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 325d3b84-f51f-3a44-981d-14bcc3bf1048 | -4.00396 | -43.33334 | 2025-11-24 04:36:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 084e2dba-e839-3cd5-aeae-c106821375e6 | -3.20664 | -45.76054 | 2025-11-24 04:36:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02c6c808-b9f1-3b61-a0ea-0be5ffa481b5 | -4.21344 | -48.6979 | 2025-11-24 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6fbb464-c05b-3e9d-8570-03d75c7c34be | -2.46493 | -48.11375 | 2025-11-24 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 12495322-4ae9-30d8-8f33-914c8f01d8f4 | -3.60102 | -40.98397 | 2025-11-24 04:36:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dde8b5da-29c3-359c-80f7-5402d9c982e6 | -1.8282 | -45.57427 | 2025-11-24 04:36:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 069ac792-6ce8-317a-87ee-f16d489d216e | -4.63075 | -45.85579 | 2025-11-24 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed500c2d-e627-3b01-9e0f-613fab7f2c85 | -3.82688 | -48.99356 | 2025-11-24 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f7f829b7-3cb5-3838-911e-2f5d38fbb09a | -3.72036 | -43.22141 | 2025-11-24 04:36:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 099bcead-f5b7-3ffc-a387-63cfd9af4288 | -3.71318 | -44.00631 | 2025-11-24 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72f19c02-f8ea-32f9-ae10-2c2f6febcb23 | -7.30305 | -45.43839 | 2025-11-24 04:36:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f996911e-750f-3467-b4fb-d0a55de4b3ba | -2.87791 | -51.80179 | 2025-11-24 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 649d8c9f-e493-3f68-b32b-5cec47c239ce | -4.21006 | -48.69737 | 2025-11-24 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4feddc99-54cf-3189-96bb-2dd3fdb8e778 | -4.61973 | -45.63344 | 2025-11-24 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8343f462-bd02-3b8b-9831-036aeb26ccd4 | -2.14592 | -46.41222 | 2025-11-24 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0158ee4a-10f2-38f5-81f5-9785a333ae5c | -6.23426 | -46.40426 | 2025-11-24 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4454708-2813-3119-863f-7b4d4af84498 | -4.66249 | -46.05336 | 2025-11-24 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 562a3d67-a860-3186-a10f-975541065af2 | -3.17323 | -50.24186 | 2025-11-24 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00937190-a95a-3c94-89c7-a2bf03aa7289 | -3.9666 | -46.4792 | 2025-11-24 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f358168f-bf4e-327a-afcf-fa1d56e66b1a | -1.14507 | -54.14871 | 2025-11-24 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 485af524-cd0f-3e32-8e8d-91df35cacdec | -4.39501 | -45.73104 | 2025-11-24 04:36:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c3e7c907-3d9f-3b28-a15d-29b0d383b2e0 | -4.26887 | -40.86361 | 2025-11-24 04:36:00 | NPP-375D | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| d54d0b7b-7bee-3125-8902-b06199ae97a8 | -4.54302 | -45.50083 | 2025-11-24 04:36:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31aedef2-3830-369c-a7f4-685be7513c93 | -4.64383 | -45.90609 | 2025-11-24 04:36:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3db2cbce-a937-360a-932f-7b23bc87dcf4 | -3.82465 | -48.98568 | 2025-11-24 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa82c153-a44f-3ba2-b6eb-701c13cdcbd8 | -2.13928 | -46.41118 | 2025-11-24 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 06cf64cc-5c8e-3a16-87dc-82c0aa51ea13 | -4.96441 | -44.15804 | 2025-11-24 04:36:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d513a955-ee8c-368a-ac34-d0e867335fbe | -4.10863 | -49.06736 | 2025-11-24 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 934348fa-99ba-3063-bf95-4521fd3809a2 | -4.10123 | -49.06997 | 2025-11-24 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dea38144-68fb-3b9d-b16b-e1fab78d6925 | -7.46908 | -39.96322 | 2025-11-24 04:36:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b512f613-3201-3991-ac46-8b46753532e6 | -4.52847 | -45.61617 | 2025-11-24 04:36:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| e6dee584-2f92-3caf-9a37-4090fe2f901d | -2.43252 | -44.02461 | 2025-11-24 04:36:00 | NPP-375D | RAPOSA | MARANHÃO | Brasil | 2109452 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6ee51ee-be09-323a-9418-cc9a3b80ebe5 | -3.21906 | -50.16466 | 2025-11-24 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecf42f5d-d7c5-3e09-945b-c627e1d8e270 | -4.06313 | -47.30373 | 2025-11-24 04:36:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d310f3e1-5be1-3a22-8301-ebc9118acc2b | -4.21286 | -48.70147 | 2025-11-24 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1a5ab35-e849-3406-a74f-aed6e7dfecca | -1.86252 | -54.06298 | 2025-11-24 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de1cd6e5-5165-380e-8f54-ac77df02710b | -4.7162 | -46.46574 | 2025-11-24 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83cc6ae1-7d4e-3909-9e7d-0543180bef66 | -4.62316 | -45.63394 | 2025-11-24 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ee9ca3e-96a5-3971-9f68-424ab93b4416 | -5.81595 | -48.68599 | 2025-11-24 04:36:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5e4acefa-33bd-3e70-ae75-870158a7da04 | -4.16684 | -46.49571 | 2025-11-24 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e4d3d000-cafb-307a-ab0d-d6de629ebedd | -4.7067 | -46.46065 | 2025-11-24 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b783c2bf-9d8e-3010-bde5-e83a867ab986 | -3.49439 | -46.01647 | 2025-11-24 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ffcad990-9c34-315a-9ff4-2aa497337eee | -2.79935 | -45.35411 | 2025-11-24 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 223af6d0-f3ba-37aa-b129-635e92fcb69c | -4.71395 | -46.45819 | 2025-11-24 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6566b83b-0597-3db4-aec3-9be2d2dff855 | -4.71451 | -46.45467 | 2025-11-24 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 30fd071c-ce51-3ce8-ab9e-9e6189632766 | -2.14647 | -46.40876 | 2025-11-24 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a5939748-f491-3b59-86b6-5407835e2ffb | -4.10464 | -49.0705 | 2025-11-24 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c1b8486-a581-3907-8176-2152b02551c9 | -4.82644 | -43.83157 | 2025-11-24 04:36:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3c349cae-4142-3683-87ca-71919d482ee6 | -2.2248 | -51.78132 | 2025-11-24 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e2b92c7-7948-396a-801c-f0c97a17ffed | -2.9356 | -52.33966 | 2025-11-24 04:36:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 604dfc54-3e27-3b6b-8037-fc8e4dadf3f9 | -2.69574 | -49.51393 | 2025-11-24 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22928ec4-fabc-30d6-b41c-b1c26799c263 | -5.66357 | -46.59487 | 2025-11-24 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 211f3bd9-b82d-375e-b4b4-6f4af34181a0 | -3.22525 | -45.73036 | 2025-11-24 04:36:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f68f25ee-bbf0-3e8d-a7e7-cb29e3f26157 | -2.88422 | -51.81328 | 2025-11-24 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cec66e5c-1553-3b4c-a66d-1af508846893 | -4.82955 | -43.8299 | 2025-11-24 04:36:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b235a381-c889-3735-8004-3603c99e7a01 | -4.42587 | -48.91958 | 2025-11-24 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89841158-45ae-3402-9bd1-fdeafa9666ed | -2.87934 | -45.2871 | 2025-11-24 04:36:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ae1de136-6e6d-3cf3-b646-a9b00c2db24c | -2.66864 | -49.86675 | 2025-11-24 04:36:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aadc67ee-6307-3217-a543-4214bde473da | -1.95146 | -46.27212 | 2025-11-24 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d4d01af-96da-3d6e-987c-3d1c3f32f41e | -4.66587 | -46.0539 | 2025-11-24 04:36:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8264afc2-0848-31a8-8b7a-823d425b40ec | -3.56354 | -49.43737 | 2025-11-24 04:36:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 259ffb68-98de-3507-a83a-daf11f1274ec | -3.62532 | -53.62395 | 2025-11-24 04:36:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2357527-45c3-31b8-97ec-aaa70f6efbca | -3.59679 | -44.95835 | 2025-11-24 04:36:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74cb2b0b-f166-3a33-9acd-6e7bad32970d | -2.40987 | -48.61223 | 2025-11-24 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 238c7b15-5107-3f60-9a7a-36eab8a3b969 | -3.27681 | -46.04438 | 2025-11-24 04:36:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3be2408-ae25-32d1-ac35-7ab1439ab300 | -4.81838 | -43.82817 | 2025-11-24 04:36:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4e1800c4-e6e2-35c4-a604-2b1608308a99 | -5.3321 | -46.74555 | 2025-11-24 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3202d630-8139-3f4a-8804-e5a42d036ed4 | -4.52161 | -45.61521 | 2025-11-24 04:36:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e3b55a3-d32d-3270-9483-47889d993659 | -4.06645 | -47.30425 | 2025-11-24 04:36:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b959695a-b5a4-34d6-8570-cd0b80331892 | -4.31562 | -50.10158 | 2025-11-24 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73fdc027-897d-35cc-8802-bd4eca253233 | -3.79861 | -50.01973 | 2025-11-24 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c1be6e8-f4db-327e-b77c-ea92beb00cea | -3.81154 | -43.3559 | 2025-11-24 04:36:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ffa9832-6c94-32a8-a69c-a99675c0c4d5 | -5.87527 | -45.28138 | 2025-11-24 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d03b6077-53e8-32c3-a170-ab1a2e1101b0 | -6.55482 | -43.21199 | 2025-11-24 04:36:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5ff22d12-9c29-3108-9c3a-05fb103c7df9 | -4.03026 | -48.88 | 2025-11-24 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cebf31b4-2b49-3722-b065-1dac7a6dbabf | -3.21904 | -45.93008 | 2025-11-24 04:36:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README8.md)
