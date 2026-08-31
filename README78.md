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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5b3db4f-7805-3f57-b4c7-add689432305 | -3.45295 | -61.71949 | 2026-08-31 05:55:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9aac5262-86fc-380b-b3ea-31230e44bfed | -8.9946 | -70.71236 | 2026-08-31 05:55:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 931d2bff-b207-399e-a218-c8b4a8eb5b89 | -9.83782 | -64.97676 | 2026-08-31 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1853d308-bb61-3de2-847d-d5f00fa8e912 | -19.16186 | -57.40335 | 2026-08-31 05:57:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 446e0430-1072-3670-86a1-ef56fe58d3a5 | -19.15586 | -57.39705 | 2026-08-31 05:57:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 4a5adf8a-3b10-36af-8f51-eda70caec753 | -22.04684 | -56.09442 | 2026-08-31 05:57:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8425a08b-55b4-30da-8aa6-f3ecceba2caa | -22.04726 | -56.08803 | 2026-08-31 05:57:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3fe1bd26-5023-36a9-a522-55d0e7684323 | -20.25674 | -58.15716 | 2026-08-31 05:57:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.5 |
| 88a0c6f3-1bef-3afd-acbb-ef7f74ee4463 | -20.25766 | -58.14675 | 2026-08-31 05:57:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.3 |
| 0c000d09-6a0e-3f4b-9838-a9afdd5e647d | -19.12094 | -57.42126 | 2026-08-31 05:57:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| c51e5b1b-e4da-32f0-87fb-6cc24327a705 | -20.25719 | -58.15197 | 2026-08-31 05:57:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.3 |
| fb2316c9-024e-338c-be44-c782c0f14d93 | -19.12146 | -57.41562 | 2026-08-31 05:57:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 548fe1a5-914a-38d9-b35e-939dac2a6a7b | -19.12095 | -57.42199 | 2026-08-31 05:57:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 89d5f647-6b41-3138-8eef-8b05bacf84b9 | -19.12144 | -57.41634 | 2026-08-31 05:57:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.5 |
| b518b6cf-3d71-3d59-a7be-dd14547bbea9 | -20.25045 | -58.15653 | 2026-08-31 05:57:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a50ccd7d-be0a-3f79-86c2-50c5a1c6d3d6 | -22.04389 | -56.09386 | 2026-08-31 05:57:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fe7a38ed-9abf-3dcc-a535-1bed614e3743 | -6.1294 | -57.6833 | 2026-08-31 06:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 4198e41b-79a1-3903-8a81-90cfe571b4f6 | -5.2362 | -55.9112 | 2026-08-31 06:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 3f3f87dd-ba37-368a-9d93-b6f12be8ada3 | -5.2547 | -55.9105 | 2026-08-31 06:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 136.8 |
| f6585681-07dc-31ae-8d15-0f4717bb73d1 | -17.6155 | -46.6607 | 2026-08-31 06:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 4015fa1a-7587-3a79-a469-1f78d68787f9 | -20.2631 | -58.1437 | 2026-08-31 06:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.3 |
| 96d226fc-7de8-3e39-9c0b-5709acc0204a | -17.6355 | -46.6565 | 2026-08-31 06:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 74.6 |
| a4776ea6-2f16-3707-8fb3-4da2606e7a51 | -5.2548 | -55.8907 | 2026-08-31 06:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 1366f4c7-2140-38ab-88ff-247239368e57 | -5.2548 | -55.8907 | 2026-08-31 06:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 9ccde628-34fc-3e17-b891-4bb2ce79d98e | -6.1294 | -57.6833 | 2026-08-31 06:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 611f61b1-091a-3ef1-9a5a-2bd53c596d69 | -17.6355 | -46.6565 | 2026-08-31 06:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 166.6 |
| feb30baa-63e7-3e66-8f59-dedc2d4cfc80 | -6.6036 | -58.5972 | 2026-08-31 06:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| abcf2f4b-3cf9-370e-8d5a-6bdf4d68e3ee | -6.1109 | -57.684 | 2026-08-31 06:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 00c5f6d9-c641-3cb2-bcf5-c0170794caf2 | -5.2547 | -55.9105 | 2026-08-31 06:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 160.6 |
| 2bc9bb2f-a935-3a99-9d99-352324c1b21a | -6.6035 | -58.6166 | 2026-08-31 06:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 4d31fe9f-5383-38eb-90fb-ad99e38bb685 | -5.2362 | -55.9112 | 2026-08-31 06:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 1e714cf4-181f-3cb9-949a-6635deb41ca9 | -6.6219 | -58.6159 | 2026-08-31 06:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.6 |
| e66c74a1-fd09-377b-95c1-d45e2007171f | -17.6155 | -46.6607 | 2026-08-31 06:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 284.2 |
| 554c61bb-d7fc-3285-9e70-80b5e1d3749c | -6.622 | -58.5965 | 2026-08-31 06:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 2d6d5f33-384d-392f-9694-de2ec59e9e2c | -5.2548 | -55.8907 | 2026-08-31 06:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 38c54306-0285-335c-ae80-2f1db0ec27e8 | -6.6035 | -58.6166 | 2026-08-31 06:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 60089b60-069b-3574-832d-6e18bc492610 | -6.622 | -58.5965 | 2026-08-31 06:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| bac7d4e1-8154-3cce-96bc-09006572733c | -6.6036 | -58.5972 | 2026-08-31 06:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 5d3fc88b-e8f6-3a4c-b6e4-c8aba3c4e684 | -17.6155 | -46.6607 | 2026-08-31 06:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 41b6f81c-ca56-30a0-a564-853d8935fce3 | -5.2362 | -55.9112 | 2026-08-31 06:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| f81a40d9-bac9-3d90-be3b-0bf045f0d73d | -5.2547 | -55.9105 | 2026-08-31 06:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 150.6 |
| 39e676a4-0607-341a-81c7-1b662158f947 | -6.1294 | -57.6833 | 2026-08-31 06:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 92ad4f58-f30f-32be-99de-4e06b47df221 | -6.1295 | -57.6637 | 2026-08-31 06:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 3fb4baef-5fc2-3b55-b281-eb7d6e5cd4c5 | -5.2547 | -55.9105 | 2026-08-31 06:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 6002f7f1-fdc2-367e-a3d4-cc841eb85d09 | -6.1294 | -57.6833 | 2026-08-31 06:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 6f4d9fc2-9256-3cbd-bc94-143e9ef7b505 | -6.6036 | -58.5972 | 2026-08-31 06:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 134.1 |
| ee1f36e0-bbe3-374f-941f-f60cd091a450 | -6.622 | -58.5965 | 2026-08-31 06:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 645788ba-816d-3223-b8d7-f24d4321aa7d | -5.2362 | -55.9112 | 2026-08-31 06:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 2a9ade51-2a41-36e6-aaf3-7d577df4efdc | -6.6035 | -58.6166 | 2026-08-31 06:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 05efc8eb-3cfa-3db2-973d-ac445323909a | -5.2548 | -55.8907 | 2026-08-31 06:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 293027b6-2f22-34bf-8b2b-303facf9d4b9 | -6.1294 | -57.6833 | 2026-08-31 06:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 42010a07-e7bf-3d66-a36d-f924da5dfdc7 | -5.2547 | -55.9105 | 2026-08-31 06:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| da95ab61-a46f-3763-acfc-6d828d6005d0 | -6.6035 | -58.6166 | 2026-08-31 06:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 0bac15db-e67a-3228-89c7-2b606de0912f | -5.2548 | -55.8907 | 2026-08-31 06:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 6af47c22-ae3f-3fd8-bf06-4834bf3a4101 | -5.2362 | -55.9112 | 2026-08-31 06:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| f0d7dc7a-e449-3d8d-8c7f-1516eddabbf8 | -19.174 | -57.3952 | 2026-08-31 06:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.1 |
| 5abf6cdf-949f-3a88-9b21-420aff05effb | -6.622 | -58.5965 | 2026-08-31 06:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| ebfcbe5e-14d3-3fd1-9880-cf3befc1eeab | -19.154 | -57.3978 | 2026-08-31 06:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.2 |
| f4a532f8-68af-36f4-8bc2-53bd9fce6bfd | -6.6036 | -58.5972 | 2026-08-31 06:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 151.6 |
| c2fd44f3-dd02-36a2-a407-18a3d697a914 | -8.39425 | -70.08633 | 2026-08-31 06:40:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 281661d5-c0ce-30b2-b944-c731ed762c50 | -8.67469 | -66.51917 | 2026-08-31 06:40:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d6b53359-b771-3544-9ff8-75addc72a829 | -8.23097 | -71.03266 | 2026-08-31 06:40:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f48f9c7-86c7-3c22-a2d4-96f61a1edb2a | -9.00767 | -70.56387 | 2026-08-31 06:40:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63855213-a98d-37df-b68a-41683313e406 | -7.44615 | -73.06957 | 2026-08-31 06:40:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ee8e5bd-adb7-3eb3-b7b3-4f5e07d2afe2 | -7.44651 | -73.07126 | 2026-08-31 06:40:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 89b3eaa3-23a5-32a3-91b7-062f6e42de4c | -8.01057 | -70.06648 | 2026-08-31 06:40:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 909f1462-9065-3895-b038-d5ce6125fbe7 | -8.86802 | -66.77877 | 2026-08-31 06:40:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d1643f27-2e08-3633-b1a7-b6b7578120d6 | -8.60405 | -70.20392 | 2026-08-31 06:40:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54347065-5df4-3089-85d0-9d44f39f2036 | -8.60921 | -70.2085 | 2026-08-31 06:40:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 024fb8a2-e3ac-3162-beca-9f58a8159c98 | -8.60356 | -70.20776 | 2026-08-31 06:40:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ea2d5d2-ef8c-3055-8172-b689e6e07a89 | -8.42129 | -70.14506 | 2026-08-31 06:40:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c763299-70c8-3b1b-93ee-b1e1de5181a9 | -8.78299 | -71.02889 | 2026-08-31 06:40:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85988118-c5c4-33c9-8d22-b6a8e6e2c96e | -8.87422 | -66.78626 | 2026-08-31 06:40:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a0a19d7-9686-3d80-8983-9d6ef5c5fed2 | -9.50744 | -70.46799 | 2026-08-31 06:40:00 | NOAA-21 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6cacc16-1699-3352-84aa-76515a6b227f | -8.68092 | -66.52712 | 2026-08-31 06:40:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3c391861-5313-322d-9699-bc2257818ee4 | -10.10267 | -68.40469 | 2026-08-31 06:40:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 587bc94a-6018-3c7c-b41c-aec00accf412 | -8.60872 | -70.21234 | 2026-08-31 06:40:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c1d7909-dada-3cc4-ab6a-7ea7ecc43517 | -8.70314 | -69.97402 | 2026-08-31 06:40:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7c6c699-8fa9-3c44-a1a0-df35995373d0 | -8.60307 | -70.21162 | 2026-08-31 06:40:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7c10814f-67a8-36fc-9017-404430bf966d | -8.70262 | -69.97797 | 2026-08-31 06:40:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 010b597a-bdde-312b-981c-2a330ed21f80 | -8.36097 | -70.86141 | 2026-08-31 06:40:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d97d46e-b5aa-3b9d-bfe2-f902cebb3ee2 | -7.44548 | -73.07426 | 2026-08-31 06:40:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 616ad0d6-cb31-36f1-86b0-a58eb0e2735a | -8.3759 | -70.83182 | 2026-08-31 06:40:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 377dae46-312f-3de4-ab62-98d24ae52be2 | -3.53172 | -49.47059 | 2026-08-31 06:48:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2e391e27-df6a-395c-a297-b273d5dc46d6 | -3.86534 | -49.108 | 2026-08-31 06:48:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 8495dc8c-95b6-3ded-ab6b-d1a027e70346 | -5.2547 | -55.9105 | 2026-08-31 06:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 8bfa6317-64ce-3e75-a314-4704ab45b7f4 | -6.622 | -58.5965 | 2026-08-31 06:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 9ecf31c4-66a4-3a9f-8750-5d904ce5e24f | -5.2548 | -55.8907 | 2026-08-31 06:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| dae9ccf3-816e-31db-b80c-1e4ab1290076 | -6.6036 | -58.5972 | 2026-08-31 06:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 121.3 |
| dfe976e5-21bc-34ff-8387-463f8b8f6a95 | -6.1294 | -57.6833 | 2026-08-31 06:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 4c7db361-15c4-3f04-b610-66c27392c615 | -19.174 | -57.3952 | 2026-08-31 06:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.6 |
| 0ede0548-c2f7-3ff6-a627-770ed80efd49 | -19.154 | -57.3978 | 2026-08-31 06:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.9 |
| 012133be-4c1f-376b-a5f7-c5fd68e07c93 | -6.1109 | -57.684 | 2026-08-31 06:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 43e11188-1f23-3612-8c24-1636287c87c9 | -6.6035 | -58.6166 | 2026-08-31 06:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| e1b18c91-d1d2-336e-889d-1572664471ca | -7.98 | -44.2731 | 2026-08-31 06:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 14221dbf-8a4e-34b5-8e22-6f378868b047 | -8.74478 | -46.44299 | 2026-08-31 06:50:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3638e428-b46a-3b2e-8a3a-e4dd4bb91c2a | -6.61752 | -58.56767 | 2026-08-31 06:50:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 271c918a-b5aa-3860-946a-9237e8a4a86c | -7.97148 | -44.28484 | 2026-08-31 06:50:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 37458702-721d-311f-bdbd-fab5f30980bd | -5.23947 | -55.903 | 2026-08-31 06:50:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| ee80d976-5c27-3864-945f-016ee0c9a459 | -9.42276 | -45.64808 | 2026-08-31 06:50:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |


[Clique aqui para ver as próximas entradas](README79.md)
