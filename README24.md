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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9b1184c-3e38-308e-9244-3ace1d492088 | -2.15687 | -51.2341 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d8b74b9-90fa-373c-98e3-21721faee896 | -2.18812 | -48.40243 | 2024-11-19 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e79c10eb-3a10-3501-b8e4-a7019d6bcdd8 | -1.81689 | -52.69485 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 875947f4-030e-3415-8d8d-8685136aa2a9 | -3.28534 | -54.11356 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d8026d4-f0ec-3483-9699-e98cff46e7c5 | -1.55034 | -53.09929 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cca2ad1a-4763-3d8d-b991-4efe3b953f9b | -2.46354 | -47.02946 | 2024-11-19 04:46:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 713967c0-6c4b-3331-b691-f9a989b04632 | -3.12172 | -53.70718 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c240b99-abb6-3bc1-ad2a-b684f8ee0927 | -2.6568 | -51.7088 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f45e16f1-d2b8-3a11-b1f7-78cedb503d2f | -4.99133 | -44.33551 | 2024-11-19 04:46:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 967da08e-c794-3c66-9754-ffb826ade1ee | -2.95193 | -48.31861 | 2024-11-19 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 863fe8f7-fed9-3452-9d45-47cf6d47dea9 | -5.16992 | -45.71642 | 2024-11-19 04:46:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 55ef2b48-e4fc-3d82-b423-2d0efaf7982f | -0.31646 | -51.49364 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 67de5e71-f56a-3414-83fc-883ce6576b29 | -2.61186 | -48.2487 | 2024-11-19 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 34136879-233a-3088-b069-5edfd8276448 | -3.34007 | -51.6706 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b4a4565-0146-34bd-8837-fd34e2c5bf17 | -3.53104 | -50.256 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e0732d9-684a-3aa0-b5d2-7e9776b386de | -3.90067 | -52.41042 | 2024-11-19 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a7a730fe-9b60-38b9-bb1d-c3d28e97ad1f | -0.65778 | -51.68707 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fbda9d82-1cf0-3b1c-aff7-0550bf50d00e | -3.13978 | -52.98061 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 014f4252-bfbe-3597-902e-f923dd868217 | -4.54668 | -48.015 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 9a1efaef-53ff-30a0-a65a-f85f1a79f235 | -3.041 | -54.40154 | 2024-11-19 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0176d0e3-8a8a-3d48-96cf-f59795b82370 | -0.34182 | -51.46429 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b948306-3ba5-3e2b-8671-b6fe089db71e | -4.18732 | -48.56285 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 895c7218-4331-3f6c-ab80-4422b72807de | -1.7939 | -46.80561 | 2024-11-19 04:46:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 272ce6a6-f8cd-364b-a5ff-652a5dbed859 | -1.98545 | -47.96624 | 2024-11-19 04:46:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7888e26b-9bbf-35c9-b60b-fbb0a518ca04 | -1.14181 | -51.69468 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4bab76ca-8c3c-3dde-b4e8-e8d9dad6267d | -7.39849 | -42.75972 | 2024-11-19 04:46:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 18c8f998-d5a9-3665-be14-8081fb4cb0d0 | -1.62662 | -52.62261 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 610cefae-1d07-3345-84b1-efa0f922fb3a | -3.28462 | -54.11802 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6af604c-47ea-3df8-9225-75bc028f7a48 | -1.69507 | -52.75614 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 291ae3e1-9b2d-32c8-87c0-01fb2a892d7a | -2.1652 | -51.96737 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 845f970e-d25e-3a63-9ea5-481fee810c44 | -2.21928 | -50.46554 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 849dca8b-6b5e-35ea-b70a-fa0e8f39881f | -1.39564 | -51.59708 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 16fd8267-8353-3bab-9c7f-d963060bb4f2 | -2.39146 | -45.8012 | 2024-11-19 04:46:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a9c6d45-856d-3094-9d5e-aca3797d39ff | -3.56949 | -51.44495 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5dffa2a1-f9ec-3b72-95bb-2815ab6ab319 | -2.71407 | -46.08116 | 2024-11-19 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1ea0e8e-0298-3b39-bef1-fac2b9693d31 | -2.13906 | -50.6501 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72247346-077f-3bc9-96c6-80e056d3cfe7 | -3.5111 | -50.22822 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 26489062-d1ca-3b2b-a8cc-b4bd52ff125f | -2.43526 | -50.41178 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85c98326-1666-38bf-bc3d-cf9f046f25a6 | -2.41098 | -50.30262 | 2024-11-19 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d0dbab7-7adb-39f8-8845-db985846f508 | -1.95398 | -54.45395 | 2024-11-19 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 46c8b356-821b-35fc-9887-51772693ded3 | -1.06198 | -51.75256 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d121b603-0b4a-3d59-9fd4-be1dd7333669 | -3.05908 | -54.40888 | 2024-11-19 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e3c2c357-6026-318e-a88e-e3cee9138c70 | -1.45836 | -52.29375 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3932932b-ac3f-3562-9be1-bb90ca0d17aa | -2.43471 | -50.28525 | 2024-11-19 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ceb5d22-0ad4-32df-8dcc-4b6c9815f16d | -4.06367 | -46.86599 | 2024-11-19 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5aecb36d-6dbe-3fd1-9d47-6ca0964d9dcc | -5.528 | -49.6988 | 2024-11-19 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c2abee6-e49b-3163-a826-c538b23b16b5 | 0.3081 | -49.81044 | 2024-11-19 04:46:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b10de74a-47e9-32d5-ad7d-2c947bf7dbc2 | -2.23369 | -46.48216 | 2024-11-19 04:46:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e670ae11-4445-3012-a872-c529ad189323 | -5.51197 | -50.19891 | 2024-11-19 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a20c0f40-e743-31c6-adc9-cc099a976f02 | -2.68315 | -46.23203 | 2024-11-19 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afa7884c-f1a7-3f7d-9e1a-58c1896eae80 | -4.55377 | -48.01607 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| cfddc2b7-4ab1-34bb-891a-0cb213e4d14d | -2.14236 | -50.65061 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 104884e7-c77b-3c6d-ac56-0ef48c934d2b | -7.88998 | -44.22023 | 2024-11-19 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d89581d9-75db-3174-937d-a0b8249aa2c2 | 0.15689 | -51.08426 | 2024-11-19 04:46:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3e6ce28-1130-3d80-8c62-d69e51d4d2ab | -3.74011 | -51.33273 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b85029f7-691a-3120-821f-f5d799d02603 | -7.91068 | -45.9407 | 2024-11-19 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6cecda8a-8efc-3a8d-88e2-f13f07026c1f | -1.63438 | -52.58445 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ade4f1e2-91b9-3453-b784-5c24d3c0dc20 | -3.06643 | -53.28234 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c561124e-c1b2-34da-99d9-0d39f82b5041 | -1.65807 | -52.53706 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d277f7e-2d50-3f5c-853e-0a6b261b56b6 | 0.34136 | -50.41419 | 2024-11-19 04:46:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ddd6eead-28e4-3bc8-bb7e-1e872501e622 | -3.5288 | -50.24861 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47105789-338d-37a6-afcc-86973ddc6ccf | -2.13461 | -52.07454 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50ede1a4-cf5b-3209-8adb-e09cf82e40c0 | -3.88454 | -46.48033 | 2024-11-19 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a45bb9aa-0379-3395-9f74-74622fdaf68a | -1.46924 | -51.97612 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e0c5b08-b468-3328-a908-10e55a32b084 | -1.21066 | -51.78692 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c614d7b-b882-3661-b56d-266f9e29b968 | -7.99768 | -44.37366 | 2024-11-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c4cddde6-e168-392f-aeca-04dfa6a9ca0e | -2.26051 | -50.46135 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e148932-35d2-3ef1-b406-a4871f915287 | -4.05005 | -54.37615 | 2024-11-19 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f3c62d1-edcd-3bbf-a932-4ed4b0656947 | -1.10785 | -51.93207 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07e0b502-42e9-36b2-a7c1-61e201356813 | -3.04195 | -49.46195 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77b15f6d-f5ac-3dee-98f6-b07445b7c9b3 | -2.67933 | -46.23145 | 2024-11-19 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c3691ca-1e7f-3495-bca0-afb1fbf71e93 | -3.51164 | -50.22477 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 00e168a2-4efb-348e-91ed-1035bf22e31c | -3.4011 | -52.72778 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 832a39a0-9b2d-32d6-97ac-f857cdf3ac01 | -1.39663 | -51.99088 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35bb0777-ae1b-3056-884a-16f7248a2670 | -2.64494 | -46.22622 | 2024-11-19 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1236dfc-999a-38a2-bd28-009cd8f9d179 | -2.87752 | -51.47622 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07fa0721-62ed-384c-8c37-ec74e60d3c57 | -4.48323 | -47.66464 | 2024-11-19 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 930f25a0-9c7c-3a98-ba3c-8f6de273f736 | -2.81272 | -54.02425 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e20f0362-0932-35ab-8748-5f06d9789d37 | -3.22019 | -53.84158 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2b6abe9-e777-35ba-99db-1ffaa44665c8 | -1.70578 | -52.14801 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 10e464f8-f421-3b99-a9fd-98077cbbc8ea | -3.06208 | -51.38293 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 978c1458-6cbb-3549-b51e-ee098f5b86ba | -1.39569 | -52.42347 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0769a41c-eda6-366c-9d83-6b1fc7b07d88 | -3.72323 | -52.44699 | 2024-11-19 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b850dd4a-1f38-3859-b80b-d01e3af403bc | -3.99249 | -49.40191 | 2024-11-19 04:46:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14c31da8-0383-3c4d-b268-a100b50fd7cb | -1.00165 | -47.99696 | 2024-11-19 04:46:00 | NOAA-21 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84188a9e-b4ee-3f08-b4e3-b9eedb11438a | -3.52854 | -54.67914 | 2024-11-19 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a5310d7-8802-3dbf-bb4f-5ff1919a92d8 | -5.65771 | -45.1995 | 2024-11-19 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6a4e965-b674-3530-b477-5be73ad0f150 | -7.56642 | -46.45597 | 2024-11-19 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b1532e8-c08a-31a3-a5af-8f3cfd9c8c57 | 0.38136 | -50.86489 | 2024-11-19 04:46:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d005ce3d-ab94-3da5-98c0-a52408b97706 | -3.48919 | -53.98887 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20adcf07-fe54-3076-8085-056f33b5d7fa | -4.1136 | -43.5941 | 2024-11-19 04:46:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 5d20e105-476c-3845-8aff-d6bb4ecf3015 | -5.98457 | -45.35897 | 2024-11-19 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6229be28-dbbe-31f8-9c9a-e16234ffd9d3 | -1.45423 | -52.34328 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffd46e1d-6c7b-325e-88dc-3c141983dce8 | -1.19991 | -51.76668 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f6b845e1-cf17-36c5-a1b4-21e89b5d2ef4 | -4.82725 | -47.31795 | 2024-11-19 04:46:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5dee090-b086-3211-9cbb-eb4dc7a6248b | -2.26611 | -50.81848 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac062065-cf8f-3ff5-a977-18fd792850dc | -3.59769 | -53.99128 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8112ba36-bd29-3f16-9182-eeb773ac47a3 | -3.49827 | -54.74605 | 2024-11-19 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26b586fc-bfd6-36f0-9496-2905be0f29ca | -2.64683 | -48.38428 | 2024-11-19 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e6adc58-24a7-35ff-86b3-d1f534000f4f | -4.57981 | -48.01188 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README25.md)
