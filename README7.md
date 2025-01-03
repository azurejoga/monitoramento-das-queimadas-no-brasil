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
| e169a1e3-54af-37a6-9fa6-e8db9c75f8ea | -5.97337 | -44.29489 | 2025-01-03 04:50:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 622b5d3e-e356-3ce4-a674-09512bfd52c3 | -5.63023 | -44.83484 | 2025-01-03 04:50:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7eba5b98-532f-324e-b29c-409075160934 | -5.9235 | -43.78994 | 2025-01-03 04:50:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50cc4481-cf00-34e1-b4a1-589f1f0c6562 | -5.67339 | -45.21431 | 2025-01-03 04:50:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1569a979-86e8-3607-ac5f-53bb98451619 | -21.83109 | -56.41269 | 2025-01-03 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f332faa7-bcd7-3296-bb67-5bc0eb31f4af | -21.83051 | -56.4164 | 2025-01-03 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1755e0c-2941-3ef3-b956-93db41ca1161 | -21.81689 | -55.34261 | 2025-01-03 04:53:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3df54d69-969b-39f8-8015-b642ff4654b0 | -30.85911 | -55.52049 | 2025-01-03 04:55:00 | NOAA-20 | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| af0551b6-af52-3daa-ac8d-7846ab332382 | -29.45674 | -54.0714 | 2025-01-03 04:55:00 | NOAA-20 | SÃO MARTINHO DA SERRA | RIO GRANDE DO SUL | Brasil | 4319125 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 978b64b5-53e7-3509-8cc9-14515df956d0 | -30.85805 | -55.52219 | 2025-01-03 04:55:00 | NOAA-20 | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 95ecc3f9-bbfd-3471-bbb5-4ca7c5ded274 | -29.45303 | -54.0707 | 2025-01-03 04:55:00 | NOAA-20 | SÃO MARTINHO DA SERRA | RIO GRANDE DO SUL | Brasil | 4319125 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3341fefb-1cb2-3a54-874d-23064d4c2610 | 3.39849 | -60.53976 | 2025-01-03 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c5ccb1c-e4ba-34e4-a19a-a377847e8c4b | 1.32085 | -60.70265 | 2025-01-03 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67cdb743-d8c6-35dd-b077-8506bc122f46 | 3.27113 | -61.1297 | 2025-01-03 05:40:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91e2b3b4-3afe-3204-a5ec-d4a1ad9d3d5e | 1.32755 | -60.72238 | 2025-01-03 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df26471c-1f7b-3474-9255-9f4a3b6ee8c3 | 2.89901 | -60.40936 | 2025-01-03 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea13f61e-74fd-3ecf-aaa0-b5ea6751e345 | 2.52582 | -60.8064 | 2025-01-03 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 385580d8-01a2-3ec4-b602-f1b69e23ec94 | 3.54184 | -60.73395 | 2025-01-03 05:40:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a726f6fa-ad47-3c40-b0ff-481d562b259e | 2.91717 | -60.95835 | 2025-01-03 05:40:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16c3cb2c-c4c6-36d3-9e6e-e751f7b508be | -1.72627 | -53.23478 | 2025-01-03 05:42:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 30573797-a7eb-362d-b069-e9587d5ff0aa | -1.25659 | -53.8629 | 2025-01-03 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 870697f8-4e33-358f-b0fa-72a8a1630539 | -1.25684 | -53.86128 | 2025-01-03 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 750f84ec-d246-34f8-88c2-6d2f1f89d51d | -9.24039 | -60.33299 | 2025-01-03 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b0f6bbaa-7582-39da-a379-a14314b2a123 | -7.88941 | -61.46572 | 2025-01-03 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f2ba9a0-2613-31ca-9870-3d967362268f | -9.25529 | -60.31907 | 2025-01-03 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8daa00fa-ee22-3caf-a5c2-5c5a07b19e1c | -9.23983 | -60.33693 | 2025-01-03 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 73b4c700-d7c8-3125-b45c-6fe3c18fcf77 | -9.42051 | -64.52236 | 2025-01-03 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3db2fc48-4e6d-36da-a965-b7d41ccf09b4 | -9.25585 | -60.3184 | 2025-01-03 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0d5c34de-cc7f-3a66-b2e7-479847261e1c | -9.41996 | -64.52602 | 2025-01-03 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4633485f-50d7-3808-bf52-0014133a79ef | -21.8305 | -56.41286 | 2025-01-03 05:48:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e6cf8005-0587-3df9-99e6-6d17237b5724 | -21.82835 | -56.41401 | 2025-01-03 05:48:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0d0c7a0c-74b9-31fd-abb1-bd5bf2e025ef | -21.83474 | -56.41471 | 2025-01-03 05:48:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 79c32241-9289-325c-bd48-9c5fa9f11109 | -21.82517 | -56.41357 | 2025-01-03 05:59:00 | AQUA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1a4dac67-31b0-3b6f-aa03-bf649b8c2ed4 | -21.82658 | -56.40408 | 2025-01-03 05:59:00 | AQUA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 76a918d5-444e-3c9a-81ca-0a90f4a01b44 | -21.81548 | -55.33588 | 2025-01-03 05:59:00 | AQUA_M-M | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| af8fcf64-12bb-3990-b4bd-687633ef3b27 | 2.52376 | -60.80652 | 2025-01-03 06:05:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a7f92c1-f4c2-3ca5-8ab2-4b3f2560c0a1 | 1.32307 | -60.70582 | 2025-01-03 06:05:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae860998-4169-3d2a-8b08-92c2613c684a | 1.32251 | -60.70237 | 2025-01-03 06:05:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38410c34-98e0-3bdb-b987-d6f5f49a17ed | 2.52324 | -60.80336 | 2025-01-03 06:05:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b5b7212e-5355-34cd-a3f4-6f67d62ded0c | -9.2357 | -60.33563 | 2025-01-03 06:07:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22c37fa4-e139-3a06-8301-91bceff6f1f0 | -6.00201 | -38.19562 | 2025-01-03 11:53:00 | TERRA_M-M | SÃO FRANCISCO DO OESTE | RIO GRANDE DO NORTE | Brasil | 2411908 | 24 | 33 | nan | nan | nan | Caatinga | 5.7 |
| bf05583d-dc52-3699-b557-d7b17332e0de | -5.63641 | -39.28336 | 2025-01-03 11:53:00 | TERRA_M-M | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| e57c0735-f953-3246-9492-cf88cf03f141 | -5.63817 | -39.27161 | 2025-01-03 11:53:00 | TERRA_M-M | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 27.4 |
| 95cd7a91-44af-310e-a128-d796087e00c6 | -6.1008 | -37.5858 | 2025-01-03 11:53:00 | TERRA_M-M | PATU | RIO GRANDE DO NORTE | Brasil | 2409308 | 24 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 2300d847-6e40-332b-8c3c-68026c0a4a98 | -7.63096 | -37.53227 | 2025-01-03 11:55:00 | TERRA_M-M | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 3f1441b2-8e4f-37d6-a871-2eeb7eb38c86 | -8.65477 | -37.21474 | 2025-01-03 11:55:00 | TERRA_M-M | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 3e8e8be5-5f90-3c29-8a65-e8e3cebe39e9 | -10.08312 | -39.28638 | 2025-01-03 11:55:00 | TERRA_M-M | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 0944d38f-c3d1-39d0-aa76-7b6b0eb60c2f | -8.27135 | -37.63183 | 2025-01-03 11:55:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 16.4 |
| d544d2b8-bd8d-3b20-be80-9b7f7af19b9b | -7.72671 | -37.38448 | 2025-01-03 11:55:00 | TERRA_M-M | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 15.3 |
| b32e04f3-07a1-3baf-8b40-21f4bcd3bb71 | -6.66361 | -38.26023 | 2025-01-03 11:55:00 | TERRA_M-M | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 11.5 |
| d7c8edfa-1aba-3f25-9966-21cbe2f8a72e | -7.91679 | -37.28537 | 2025-01-03 11:55:00 | TERRA_M-M | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 99582e65-f631-3de0-94c1-541d5b8f67d7 | -7.62689 | -37.55988 | 2025-01-03 11:55:00 | TERRA_M-M | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 606c0715-c660-3795-a921-6c7c62a3ea86 | -8.84236 | -41.52332 | 2025-01-03 11:55:00 | TERRA_M-M | DOM INOCÊNCIO | PIAUÍ | Brasil | 2203453 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 088c1981-176c-3578-bcf7-1f9a690f46c5 | -8.70204 | -35.28485 | 2025-01-03 11:55:00 | TERRA_M-M | TAMANDARÉ | PERNAMBUCO | Brasil | 2614857 | 26 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| fcd6ecd3-bddb-3955-9d87-2e398c0fc367 | -6.51817 | -41.56973 | 2025-01-03 11:55:00 | TERRA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 28.9 |
| a9e60536-26ec-3c69-89a4-2039d1cce86f | -8.08386 | -37.71418 | 2025-01-03 11:55:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 298d7d0a-bcf8-3c4b-9439-a26f3d2931f0 | -8.7878 | -40.84755 | 2025-01-03 11:55:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 8b8bf832-147e-3e82-9cf4-0ad495c0c05f | -8.94115 | -37.34579 | 2025-01-03 11:55:00 | TERRA_M-M | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| af30bee1-23c6-37b6-84ff-fcba233d7622 | -8.26892 | -35.6121 | 2025-01-03 11:55:00 | TERRA_M-M | GRAVATÁ | PERNAMBUCO | Brasil | 2606408 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 6fe90b5c-2aa8-3a4e-91e4-b84ca1f55c54 | -7.13605 | -37.57147 | 2025-01-03 11:55:00 | TERRA_M-M | CATINGUEIRA | PARAÍBA | Brasil | 2504207 | 25 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 680c2fca-81c8-3847-ab95-6219b3ffa0e6 | -9.5961 | -37.08479 | 2025-01-03 11:55:00 | TERRA_M-M | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 201b383a-5b7b-38b9-a9f0-655376f7cdde | -8.22446 | -37.38564 | 2025-01-03 11:55:00 | TERRA_M-M | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 46.4 |
| 125abaf3-27df-3ecc-b0f0-0bc4860dbab6 | -6.50957 | -41.57858 | 2025-01-03 11:55:00 | TERRA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 40.6 |
| a25c208e-c11c-323f-a44d-9d488ce7dbb7 | -7.67 | -37.70477 | 2025-01-03 11:55:00 | TERRA_M-M | CARNAÍBA | PERNAMBUCO | Brasil | 2603900 | 26 | 33 | nan | nan | nan | Caatinga | 8.0 |
| d63bcf35-e5b7-34be-b800-836ef16e18e5 | -8.70335 | -35.27554 | 2025-01-03 11:55:00 | TERRA_M-M | TAMANDARÉ | PERNAMBUCO | Brasil | 2614857 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 39071c85-bf6c-3f9a-8442-8cb8bd8e0bc8 | -10.08467 | -39.27607 | 2025-01-03 11:55:00 | TERRA_M-M | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 33.1 |
| 7ed07ed9-88df-32ce-8408-34623c271d1b | -7.24599 | -35.28305 | 2025-01-03 11:55:00 | TERRA_M-M | PILAR | PARAÍBA | Brasil | 2511509 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 89585c9c-db40-3b2d-9f3d-fce5f4c3aff7 | -8.22579 | -37.37657 | 2025-01-03 11:55:00 | TERRA_M-M | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 38.0 |
| 0e7c2759-8464-3798-b85d-095b76824a9b | -13.00719 | -40.08485 | 2025-01-03 11:57:00 | TERRA_M-M | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Caatinga | 39.7 |
| 9400d762-7814-38af-8ca6-5b66d33c151b | -13.75965 | -40.33767 | 2025-01-03 11:57:00 | TERRA_M-M | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| b0ef6ad6-4554-31f4-9a56-afd860cb2232 | -12.81504 | -39.8175 | 2025-01-03 11:57:00 | TERRA_M-M | ITATIM | BAHIA | Brasil | 2916856 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| a9b48d27-2fbe-39cd-8ffc-b49510ad919b | -15.21529 | -39.5831 | 2025-01-03 11:57:00 | TERRA_M-M | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 358eb663-e115-32e0-9302-40016f9d1ef6 | -12.56124 | -40.5195 | 2025-01-03 11:57:00 | TERRA_M-M | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 13c649fa-b898-35af-aa2a-c6f5357c729a | -11.22621 | -37.61465 | 2025-01-03 11:57:00 | TERRA_M-M | ARAUÁ | SERGIPE | Brasil | 2800407 | 28 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 6d340820-2474-32e0-97b8-61ff8580850f | -10.78306 | -39.60477 | 2025-01-03 11:57:00 | TERRA_M-M | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 16446e25-b62d-3e2a-8a9a-35785151ae35 | -13.13755 | -41.75859 | 2025-01-03 11:57:00 | TERRA_M-M | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 93982c8d-193b-3453-9a94-a98ea8f7114c | -11.77165 | -38.66692 | 2025-01-03 11:57:00 | TERRA_M-M | ÁGUA FRIA | BAHIA | Brasil | 2900405 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 3ac659df-e792-3273-8524-3d7a67eab193 | -11.76262 | -38.6687 | 2025-01-03 11:57:00 | TERRA_M-M | ÁGUA FRIA | BAHIA | Brasil | 2900405 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 6dc69853-d039-3fe9-84b0-a43e9c6baf79 | -13.14733 | -40.11941 | 2025-01-03 11:57:00 | TERRA_M-M | IRAJUBA | BAHIA | Brasil | 2914208 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| e173a1ed-2c4c-3be2-be54-9163f6026b96 | -12.45675 | -40.21183 | 2025-01-03 11:57:00 | TERRA_M-M | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 48ca3c41-719f-3808-9d5d-ea04db9e0515 | -13.53343 | -40.01118 | 2025-01-03 11:57:00 | TERRA_M-M | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 26.5 |
| 9f71cfa2-7c1d-3088-9998-ffa40060fef7 | -10.62266 | -38.01706 | 2025-01-03 11:57:00 | TERRA_M-M | ADUSTINA | BAHIA | Brasil | 2900355 | 29 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 2886fed0-a82c-30d9-86f9-d9c66a50b697 | -10.46949 | -39.17128 | 2025-01-03 11:57:00 | TERRA_M-M | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 17.2 |
| aff67391-6b2b-37bf-9884-2a4674b42512 | -13.19291 | -40.6771 | 2025-01-03 11:57:00 | TERRA_M-M | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 17.7 |
| b2927ce2-ad68-3f32-8852-296999663d30 | -15.94277 | -38.97388 | 2025-01-03 11:57:00 | TERRA_M-M | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 730fbcac-f3a4-3006-90c2-ce42af638cd3 | -13.19468 | -40.66569 | 2025-01-03 11:57:00 | TERRA_M-M | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 9d4a4723-980b-3b20-9ec4-24a373955632 | -12.45501 | -40.20485 | 2025-01-03 11:57:00 | TERRA_M-M | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| c91d1307-0155-3fff-be66-b8b3b8cb27d7 | -13.01165 | -40.18438 | 2025-01-03 11:57:00 | TERRA_M-M | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 24.6 |
| d37a11da-76b7-3c74-b643-b60abafa38cc | -12.99765 | -40.08323 | 2025-01-03 11:57:00 | TERRA_M-M | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Caatinga | 19.4 |


