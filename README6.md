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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 116cdd85-7820-374b-98ba-82590d9dd24e | -3.29314 | -44.43316 | 2025-12-08 12:14:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 26.2 |
| ce91fe81-93ab-3c16-bcc1-a9c425c780d2 | -0.66297 | -47.43924 | 2025-12-08 12:14:00 | TERRA_M-T | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 033f8424-61e0-3f61-86cc-e2319c1c4a22 | -1.05171 | -47.42853 | 2025-12-08 12:14:00 | TERRA_M-T | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| d5067b64-6a37-3211-8ec4-3c1c0ddb22ea | -4.32938 | -43.8199 | 2025-12-08 12:14:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 399.4 |
| 0308d42e-e7e2-3ad7-a2e1-98d7e126a950 | -1.06472 | -48.10616 | 2025-12-08 12:14:00 | TERRA_M-T | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 5e6eada7-147a-3c89-83cc-74e9cd524fe4 | -3.29213 | -45.6283 | 2025-12-08 12:14:00 | TERRA_M-T | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 22065b1a-582d-3058-83f1-1af1314e348b | -5.17684 | -44.4945 | 2025-12-08 12:14:00 | TERRA_M-T | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 33a3007b-5c00-3c3c-9977-059896f40da2 | -2.31012 | -47.72628 | 2025-12-08 12:14:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 70e763f4-6837-33c7-9029-cf1be3352a5c | -3.28412 | -45.63112 | 2025-12-08 12:14:00 | TERRA_M-T | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 89c9fe35-1d10-3f7d-a0e8-7ba2e42c627e | -4.31713 | -43.83125 | 2025-12-08 12:14:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 92f5b1cc-f1a4-3cb8-952d-54b511ea2e2d | -4.16977 | -43.72136 | 2025-12-08 12:14:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 6dfe18ee-5caa-3444-a409-1cb9f60b21f0 | -1.05234 | -46.53016 | 2025-12-08 12:14:00 | TERRA_M-T | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1180f516-438a-3dc5-81e6-21e2fc3cf2a1 | -3.98136 | -42.51379 | 2025-12-08 12:14:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 19.2 |
| e183f4e0-a562-37a0-9557-7ab7f7343636 | -2.64291 | -46.9608 | 2025-12-08 12:14:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 0d4eee8f-b347-30d9-841e-beefaa4a6a59 | -2.11098 | -45.96145 | 2025-12-08 12:14:00 | TERRA_M-T | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 92615451-efdc-3a75-bbef-4371adae57f7 | -2.25524 | -46.11488 | 2025-12-08 12:14:00 | TERRA_M-T | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0c31de31-3e96-3299-ace9-be30ba11a013 | -3.45066 | -42.69408 | 2025-12-08 12:14:00 | TERRA_M-T | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 70717689-2e74-3470-87ae-0e37e2f27513 | -2.80176 | -42.32396 | 2025-12-08 12:14:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a34b638e-7150-3a51-8bcf-00b44df91a6d | -4.4774 | -42.99557 | 2025-12-08 12:14:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a1ea9f1a-cbb6-3f85-9760-c84c9611c89b | -2.77733 | -42.41518 | 2025-12-08 12:14:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| e5fd04c4-105b-3c2f-8c1f-d3b8310e7a06 | -1.54374 | -47.21582 | 2025-12-08 12:14:00 | TERRA_M-T | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1b1a9dbd-c0ce-3b41-9d6b-af0ff8952bc2 | -1.55791 | -47.6346 | 2025-12-08 12:14:00 | TERRA_M-T | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a242d223-6bcc-3022-aa08-a80e6ce92e03 | -3.29469 | -44.42195 | 2025-12-08 12:14:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| e815741b-72b4-3f2b-8c07-881ed0f244e8 | -2.95512 | -45.8009 | 2025-12-08 12:14:00 | TERRA_M-T | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 43c2443f-487e-3b49-805e-ae7c810c8d94 | -3.58766 | -43.03645 | 2025-12-08 12:14:00 | TERRA_M-T | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 438b10dc-123a-3837-a4f2-616125e7e344 | -0.38993 | -51.95266 | 2025-12-08 12:14:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 130700c5-87b1-396e-ba9b-700e7bacf104 | -2.23553 | -46.44288 | 2025-12-08 12:14:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b27f6e8e-e33c-3238-8ae6-bee46b3b4fbb | -0.66171 | -47.44803 | 2025-12-08 12:14:00 | TERRA_M-T | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 99f04b8a-3a08-3d57-b3a1-013132d06371 | -1.87926 | -47.05803 | 2025-12-08 12:14:00 | TERRA_M-T | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3ef1057d-8dba-3dee-89b1-6fea2e7c9075 | -2.89997 | -42.2793 | 2025-12-08 12:14:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 1e17fdcd-8af7-3486-a18a-8d875e175dcc | -4.65577 | -43.1213 | 2025-12-08 12:14:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 5920ea96-c1b5-3edb-9206-a3eaa7046845 | -4.32762 | -43.83268 | 2025-12-08 12:14:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 139.4 |
| dd4b8fd2-4455-3119-8d88-e3ccdd159261 | -21.66512 | -47.15755 | 2025-12-08 12:21:00 | TERRA_M-T | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| f31c3527-9564-34ee-ad2a-82b4322e2d79 | -26.74553 | -51.24082 | 2025-12-08 12:23:00 | TERRA_M-T | CAÇADOR | SANTA CATARINA | Brasil | 4203006 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 84257565-cb97-35b5-be0e-8ed06d830d1e | -25.22963 | -49.25837 | 2025-12-08 12:23:00 | TERRA_M-T | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 4b4a097f-21a5-3a35-b4ba-52a6d0a7f474 | -26.7469 | -51.23042 | 2025-12-08 12:23:00 | TERRA_M-T | CAÇADOR | SANTA CATARINA | Brasil | 4203006 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 892e279e-44b4-359d-ae0f-4e0b4889570b | -26.1407 | -51.43281 | 2025-12-08 12:23:00 | TERRA_M-T | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| d9b22e90-9d0c-3568-ab8e-562ed5e63acc | -26.13933 | -51.44289 | 2025-12-08 12:23:00 | TERRA_M-T | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 55c48583-779e-32e5-af27-95cbcad4b3f5 | -3.1424 | -42.2977 | 2025-12-08 12:40:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |


