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
| 93337339-3452-3115-a255-513310e28e8d | 2.20378 | -60.24894 | 2025-01-11 05:37:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff419e14-1e95-34dd-ae05-6cf6cbb131ea | 3.37941 | -60.25766 | 2025-01-11 05:37:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26e6df6b-1647-3c3e-b1d0-7dfe3786a20d | 2.20738 | -60.24832 | 2025-01-11 05:37:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3929584d-ecba-3775-bf5b-83422c232fd4 | -3.32143 | -52.44413 | 2025-01-11 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0de6f936-eb16-330f-88ea-c000f761df9e | -3.32091 | -52.44523 | 2025-01-11 05:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 23600568-1ae6-37f0-9c14-78fd0d9b7974 | -3.45981 | -53.96169 | 2025-01-11 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6bfd4b5-99de-3ce6-b288-eb72ad0aa16a | -3.46045 | -53.95731 | 2025-01-11 05:40:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 306b29c6-7f7a-3f4d-8185-a0db1a006c85 | -3.87098 | -54.23293 | 2025-01-11 05:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 573b65c6-8a2d-36a8-be5c-1a80a9c45b03 | -2.79434 | -54.17297 | 2025-01-11 05:40:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56561f09-9b88-315b-a340-2856d3f6cc96 | -19.66566 | -54.41565 | 2025-01-11 05:44:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 205732cc-9cd9-38da-8f33-33d3a13b9ea3 | -19.34444 | -54.16362 | 2025-01-11 05:44:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c380d515-d271-3029-8ff0-775a89a61b38 | -19.3471 | -54.16463 | 2025-01-11 05:44:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 65f88ff0-d3f5-30b7-bdaa-a566edcf34d5 | -19.34389 | -54.17054 | 2025-01-11 05:44:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0dbcd0c7-6b73-3fdf-bbbd-248b81472008 | -30.38756 | -56.16426 | 2025-01-11 05:46:00 | NOAA-20 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| a03a0b0f-3556-30df-bf44-eb80edebe490 | -30.38093 | -56.15676 | 2025-01-11 05:46:00 | NOAA-20 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 2601c142-3ce4-393b-a4e2-d6dd3ddd7e06 | -30.37399 | -56.1565 | 2025-01-11 05:46:00 | NOAA-20 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 1b7c3b99-cd67-3d95-acf1-58748288f389 | -3.8675 | -54.22076 | 2025-01-11 06:16:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 19b1616a-a557-3344-9f8e-d9c210bc3d85 | -3.45582 | -53.95521 | 2025-01-11 06:16:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 29e72399-7580-326d-b399-15d201a6094e | -3.86571 | -54.23298 | 2025-01-11 06:16:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 22edd2f9-75c0-3833-a911-43c45aee4788 | -23.61927 | -55.19585 | 2025-01-11 06:22:00 | AQUA_M-M | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 73b6a1e1-def2-329d-9ff1-3febbb2c7de6 | -8.905 | -35.5937 | 2025-01-11 07:00:00 | GOES-16 | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 80.6 |
| be2026a9-128b-3300-875d-78262d88f15d | -2.49478 | -44.07397 | 2025-01-11 12:16:00 | TERRA_M-T | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 3599096f-fef1-3027-ac28-d249fff262e8 | -4.17734 | -38.58191 | 2025-01-11 12:16:00 | TERRA_M-T | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 51169616-d32a-33d6-8ee2-f312f310e12e | -3.96756 | -39.82244 | 2025-01-11 12:16:00 | TERRA_M-T | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 263cf65b-3711-39e8-b49c-3f67e517b265 | -4.18736 | -38.36195 | 2025-01-11 12:16:00 | TERRA_M-T | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 11.4 |
| b727d12e-3d1c-3bce-837b-e6effd2cf3f6 | -4.53239 | -42.93644 | 2025-01-11 12:16:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| dbb3ec78-2fe1-3e14-8928-e545f8e2ac2f | -5.38563 | -39.1578 | 2025-01-11 12:16:00 | TERRA_M-T | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 25.5 |
| 8d11d787-9134-3c70-8537-a5437c3ac327 | -3.98858 | -39.86067 | 2025-01-11 12:16:00 | TERRA_M-T | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 7daf066c-977a-3b38-8c7f-1fa833bf61f7 | -3.96619 | -39.83199 | 2025-01-11 12:16:00 | TERRA_M-T | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 111.8 |
| 58db9a86-110f-304f-b0ed-f9a260072f87 | -4.39816 | -39.90281 | 2025-01-11 12:16:00 | TERRA_M-T | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 11.9 |
| c61805ac-0731-3aa0-a8da-4ad95572d77c | -7.38077 | -38.84113 | 2025-01-11 12:18:00 | TERRA_M-T | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 12538b3a-85a6-3997-8e9f-fd75cb0015c4 | -6.54962 | -39.60274 | 2025-01-11 12:18:00 | TERRA_M-T | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 6d1938db-f812-3262-bc35-41a8da4afe09 | -5.7593 | -39.04414 | 2025-01-11 12:18:00 | TERRA_M-T | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 8ab4fd9f-6fd8-3f98-87c7-ce17e5e2991a | -7.34587 | -39.17017 | 2025-01-11 12:18:00 | TERRA_M-T | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 702a2d08-b045-3e90-b6f8-3637ab80514d | -19.84754 | -47.72242 | 2025-01-11 12:21:00 | TERRA_M-T | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e03a8f6a-c886-3fbb-9a95-a2ad34dea4d3 | -20.00376 | -48.60642 | 2025-01-11 12:21:00 | TERRA_M-T | PIRAJUBA | MINAS GERAIS | Brasil | 3150703 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| ca2f44a7-61ab-3ca5-98b6-1eb68d30dc7e | -22.84013 | -48.8498 | 2025-01-11 12:21:00 | TERRA_M-T | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 861316cc-9d94-3ddb-bc00-506a538df25a | -3.9624 | -39.8366 | 2025-01-11 14:00:00 | GOES-16 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 105.1 |
| 7d3ddae1-ad48-38b0-a953-539f4ef0a154 | 3.6222 | -60.3379 | 2025-01-11 14:10:00 | GOES-16 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 76.5 |


