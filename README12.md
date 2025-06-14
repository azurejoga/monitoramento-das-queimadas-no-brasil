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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5d2a7c0-cd26-3e1f-96be-accd71d9f649 | -7.2174 | -44.72817 | 2025-06-14 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c0e4128-e7e4-35f2-9cf2-88af0a35ad71 | -7.20889 | -44.73798 | 2025-06-14 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0954f30-eaec-3651-a142-44be86262581 | -7.43442 | -45.42044 | 2025-06-14 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 962eb369-7989-34a0-8ad4-f703c6728820 | -7.23129 | -43.10615 | 2025-06-14 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e553bf63-d02f-338e-b567-ac5af16c8eaa | -7.23066 | -43.58477 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9f91c5ff-9c53-3cc4-a52b-95ef7006b06c | -7.24175 | -43.10425 | 2025-06-14 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| decab62b-b033-3aee-a326-d3184bfa0dd7 | -6.60091 | -43.89077 | 2025-06-14 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3c7e8e5b-7742-3169-bad4-bab04a4ae29b | -7.63379 | -43.6781 | 2025-06-14 04:12:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c8a4ae4-2787-3b79-8ba2-ffeb1be0b151 | -7.43159 | -45.41611 | 2025-06-14 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 052515b6-8cd8-3e5f-802d-da73ff0fd46f | -7.63434 | -43.67463 | 2025-06-14 04:12:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e828375-5fac-3c5c-824d-b3df8b28686e | -7.47636 | -37.41537 | 2025-06-14 04:12:00 | NOAA-20 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 838131b3-65f5-340f-90c4-557f5602f03a | -6.59924 | -43.90125 | 2025-06-14 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a023d719-933e-3f78-b6f3-9a75e7faffed | -6.54841 | -42.39385 | 2025-06-14 04:12:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7ffcad61-fa4f-3df7-83e7-1fae5d5e7733 | -7.22186 | -43.6403 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58223cad-cfa8-3fad-9942-5429d763e4d6 | -5.89906 | -43.45488 | 2025-06-14 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0063f02a-86c1-35f5-a821-178a94fe6d0e | -7.23011 | -43.58824 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c858122b-3f91-33d5-999d-8a5ec8e81a6c | -7.21751 | -43.10752 | 2025-06-14 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e6b3e7b0-419b-3274-9fd7-d8bc63869c05 | -7.07263 | -43.55282 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9432e315-4e79-3f4f-af83-9904d7dca6ff | -7.22294 | -43.59066 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df6bffbb-13b8-32ae-84db-6d94158f6a1c | -7.17769 | -43.53375 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ee59b0fb-fbe8-3d67-94b1-53f6c6087fc8 | -6.59979 | -43.89775 | 2025-06-14 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d53160de-d6cf-3d6b-ab9d-b161cf9b8daf | -7.45876 | -45.50986 | 2025-06-14 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb6175f6-f72b-3872-a062-8673598945b9 | -6.94927 | -42.89108 | 2025-06-14 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.8 |
| 7e1af3c5-0c51-3deb-9745-fe73e211a9a0 | -8.75581 | -46.7262 | 2025-06-14 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8713d3d-bbb5-317d-ad72-89f7ffb43594 | -6.33603 | -43.74142 | 2025-06-14 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ced53c3-3dfa-3a02-bc8a-5ace3ebd3279 | -7.00816 | -43.83108 | 2025-06-14 04:12:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 452504aa-03a9-3dd6-8612-074c2d19fa55 | -6.60479 | -43.88781 | 2025-06-14 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cae9cbef-4e75-3705-8878-135b0c5007e6 | -7.61227 | -43.66401 | 2025-06-14 04:12:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c775c53-da89-3b02-a967-49522dcf4c72 | -8.07615 | -43.11198 | 2025-06-14 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 35.5 |
| 18f6bfeb-13af-34a1-9e6d-c69100c3b1bc | -7.45247 | -45.50495 | 2025-06-14 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2a55210a-3e7a-33ff-b7f8-410577fe8700 | -7.22136 | -43.10458 | 2025-06-14 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1697b4e5-6838-35e2-b692-d697c97582ce | -6.68694 | -43.96944 | 2025-06-14 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f2719f9-9aec-3b46-93bd-1b6c2b6b9950 | -6.95214 | -42.89513 | 2025-06-14 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 38.6 |
| 30efc4e5-2e10-3f2f-8fdc-50d9e0f76a34 | -7.11113 | -43.43823 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ed63708b-bc97-314c-b66f-ffa7ed0e7925 | -7.23183 | -43.10268 | 2025-06-14 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b6d7c704-c315-3ee2-9381-881c236364ae | -5.91562 | -43.45751 | 2025-06-14 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 25d0685e-8dc6-33a2-bbee-4bb602cfb292 | -5.78026 | -43.6245 | 2025-06-14 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c27a281f-46a3-3412-b5a1-528c8e6891f3 | -7.63765 | -43.67515 | 2025-06-14 04:12:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2928fc1-2b9e-3da3-8a1b-5af932e0550a | -7.45592 | -45.50551 | 2025-06-14 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 80671bc6-10af-3f7a-add2-e7a791c3ec01 | -6.96489 | -42.68375 | 2025-06-14 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3bdb07b6-99d7-3c18-a2a2-ec47492c595f | -7.88975 | -43.43429 | 2025-06-14 04:12:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3b4c2a71-3fbf-3c9e-b7f2-c0bfab6e9d89 | -7.20948 | -44.73436 | 2025-06-14 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86728c73-d096-32cd-a0a4-39a60afd9112 | -7.19313 | -43.54329 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| eeb97c3b-c8d1-3b9e-8fe1-2be1341c9cc9 | -6.94634 | -42.80186 | 2025-06-14 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5b3d3f33-8d6c-3d03-bb70-9c3bb006d511 | -7.46283 | -45.50663 | 2025-06-14 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db233d72-2d9e-3e6b-9e79-eb44ac277c1c | -6.00768 | -44.32933 | 2025-06-14 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cea759d9-88f0-388e-a160-8807b1705210 | -7.23568 | -43.09974 | 2025-06-14 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 42fcf8b5-55bd-3bef-8ea4-6b3603c03ae4 | -6.95268 | -42.89167 | 2025-06-14 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 38.6 |
| aace451f-ea6c-3a79-b29a-38f462c988e2 | -5.91176 | -43.46046 | 2025-06-14 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 28c7a2bb-c8f7-3c0d-8f43-25fe488881ce | -7.45937 | -45.50607 | 2025-06-14 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 582fab34-e972-33b8-becc-593f57703614 | -7.61283 | -43.66054 | 2025-06-14 04:12:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5be16682-7a72-3e4c-8ea3-a49a2c80913f | -7.2142 | -43.107 | 2025-06-14 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 3f336101-5b5c-3f16-97b9-73e3934bc76e | -6.4909 | -42.84719 | 2025-06-14 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b528debd-77b7-3d37-be25-b7241c0535ec | -7.22798 | -43.10563 | 2025-06-14 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b639a2db-fa27-3622-8575-96f2ae07a341 | -7.63542 | -43.625 | 2025-06-14 04:12:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93cac829-2bd7-3fa0-908b-4097ef32bdc4 | -7.2109 | -43.10648 | 2025-06-14 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| fe6ac620-9d20-3851-af45-37008ecfc98a | -4.575 | -37.82122 | 2025-06-14 04:12:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5a259e6e-370b-33ef-85dc-cbede701d27f | -7.00746 | -43.53539 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b59a7ce-6b77-3fb8-bc5c-56813ca7babb | -7.19203 | -43.55022 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 53832341-d658-3bea-a142-a00a8eaa7d9a | -7.08316 | -43.65758 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33a82f03-f7be-3d3b-be76-4fddb5783df7 | -6.94249 | -42.80481 | 2025-06-14 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 30c279af-3aa9-37ec-bb59-5de2278c13a6 | -6.21146 | -43.32668 | 2025-06-14 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f9045d55-b318-3f61-9be3-2cbeeef757a9 | -5.77309 | -43.47725 | 2025-06-14 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fab25ba8-d348-3ff8-a663-16c0ffd08d58 | -7.23292 | -43.09576 | 2025-06-14 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| aca99e29-11be-31b5-a008-7c0d3962450b | -9.10361 | -44.30705 | 2025-06-14 04:12:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a61ba3d1-f8a7-3e5e-964b-221085e5b28f | -7.45654 | -45.50172 | 2025-06-14 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 28d73985-f330-3302-9858-f822dd730a58 | -5.4488 | -44.81677 | 2025-06-14 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41ac4534-3b82-32e9-87ac-8aa8ac322fc7 | -7.17076 | -43.53288 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 99008953-bedb-3d85-9ca7-5037cd6c157a | -6.60368 | -43.89479 | 2025-06-14 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| de70dbb6-7851-32da-8721-083e6b276dda | -6.69026 | -43.96998 | 2025-06-14 04:12:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7d64721-96aa-3f72-bacc-dea8e5135813 | -7.39646 | -43.3946 | 2025-06-14 04:12:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0bca00e1-a9a2-362f-800c-d5076c38180f | -7.11167 | -43.43477 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1e3f9284-c782-39f2-a575-05c6ab2255c1 | -2.66536 | -47.39912 | 2025-06-14 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b47a965-feb1-3c49-a15f-6e735a6b7f00 | -7.07208 | -43.55629 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd989cf4-afc4-3287-b0d9-7f64749ee0d6 | -6.96212 | -42.67976 | 2025-06-14 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d8b9e081-86c2-3d4f-9b2c-42ce6acadb6c | -5.44939 | -44.81306 | 2025-06-14 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83953bca-6716-3748-a33e-5d1d23eaa6db | -7.07594 | -43.55335 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf7fd154-c6db-3d3b-9c9c-e1f6856362cf | -5.78081 | -43.62101 | 2025-06-14 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02f13a6c-c440-3e08-a980-e1b204676c02 | -5.90292 | -43.45194 | 2025-06-14 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 90a56bcd-ce6d-31b9-aec4-f6e40555a85e | -7.00691 | -43.53884 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30887b7f-95f7-3855-9661-092ecb92466f | -7.01203 | -43.82812 | 2025-06-14 04:12:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6498c5f8-abed-339d-92ca-19f232ea510f | -5.90347 | -43.44847 | 2025-06-14 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 610cf415-47a8-3884-a98e-179c6b3e750c | -7.23899 | -43.10026 | 2025-06-14 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ba85324e-e8ba-3aa4-b2bd-184427d916e8 | -7.67347 | -43.64173 | 2025-06-14 04:12:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 463d7e21-6ab0-3a57-bd3e-48e55b2bf3d3 | -7.39315 | -43.39407 | 2025-06-14 04:12:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2b95b9f5-397e-39a5-898f-39378c25bb32 | -6.9585 | -42.81087 | 2025-06-14 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| e9e0c10b-b6d1-37cc-9042-ceebbdb4a6f2 | -7.67402 | -43.63825 | 2025-06-14 04:12:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 347c9b31-cc2c-3c9f-a806-cb5a044a4814 | -6.9458 | -42.80532 | 2025-06-14 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8275e181-f6ce-3266-82ff-dea5e88f6774 | -7.22625 | -43.59119 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ae8d5de-3fe0-3c77-a4bc-b82fc1b508b3 | -5.90237 | -43.45541 | 2025-06-14 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69c31d11-ec93-352c-aa28-1d2ffdd0d795 | -6.60369 | -44.25919 | 2025-06-14 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93e14a51-a45c-30a2-b7fe-63a919a8f21d | -5.44936 | -44.8129 | 2025-06-14 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1fc4801-3c47-310c-abd8-fa841f63981d | -7.18432 | -43.55611 | 2025-06-14 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 797ac358-d423-3678-9282-a5f1eaf3c675 | -7.67844 | -43.65319 | 2025-06-14 04:12:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bec7bc23-a7b4-30e9-8f1b-ab1140cedbc7 | -7.22082 | -43.10805 | 2025-06-14 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 07c752a9-bb66-33f2-b646-e52efd4e78dc | -6.95904 | -42.8074 | 2025-06-14 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 15190852-4810-3d02-99cf-b516a29d424a | -6.9516 | -42.89859 | 2025-06-14 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 28.7 |
| a315e0fb-0ce3-31b6-bc53-dfd24dd78b17 | -8.7594 | -46.72681 | 2025-06-14 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3313255c-8acd-37ed-a121-1d645e58f56a | -7.24066 | -43.11118 | 2025-06-14 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3d36a8da-cea6-3d20-86fd-586d33a327e7 | -5.88455 | -44.35399 | 2025-06-14 04:12:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README13.md)
