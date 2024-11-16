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
| 7985c6fd-b8bb-34ff-b93e-5968d4e54a03 | -3.2009 | -45.5405 | 2024-11-16 02:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 85.4 |
| ae8ea7b8-a1c8-3249-a254-d6cec28f0a01 | -3.1456 | -54.5259 | 2024-11-16 02:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 482bb815-a2bd-3b3b-b464-1f84af8f638e | -3.7207 | -45.6755 | 2024-11-16 02:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 2aacf3ff-ba17-35cd-a0a0-258ba50552c9 | -2.1379 | -53.7043 | 2024-11-16 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| adf4b809-6576-3794-81b6-d6790e475da3 | -4.9971 | -44.3149 | 2024-11-16 02:00:00 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| dd9760b2-753f-3bed-958d-fd2126071e0c | -2.1562 | -53.7039 | 2024-11-16 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 85ee6209-322b-330d-9631-baa20b18eff1 | -3.7393 | -45.6747 | 2024-11-16 02:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 111.6 |
| e7d62aa0-6653-33a3-a76c-a47c6f44c071 | -17.5879 | -57.4917 | 2024-11-16 02:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.6 |
| ace96bbc-5404-3517-9753-e328515f62cf | -16.958 | -57.6269 | 2024-11-16 02:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 133.2 |
| f1cc36ee-f211-3ccf-9ccc-7eaa93016ab1 | -2.5594 | -54.0382 | 2024-11-16 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| ebc77107-5942-3fc2-8f33-a1152ae5b033 | -16.9577 | -57.6473 | 2024-11-16 02:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.2 |
| 2e9656b5-7805-3e8e-8259-edb1c83ef666 | -3.1453 | -45.4978 | 2024-11-16 02:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 2e8574d4-645b-3f7c-ae0b-a91a977694ff | -5.6796 | -35.6418 | 2024-11-16 02:00:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 77.2 |
| 2ecf732c-251f-356a-8ca7-f07903c30b2e | -2.7801 | -48.5592 | 2024-11-16 02:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| b52d0f3a-035f-334c-862a-fbaad0dd7add | -2.1562 | -53.7241 | 2024-11-16 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| f7469249-f291-329f-8478-2062b68ee625 | -3.2008 | -45.5629 | 2024-11-16 02:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 7d539afa-2b02-3bc1-aabf-f36c849cb434 | -2.5642 | -46.8938 | 2024-11-16 02:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 5b50333a-4fcd-3837-bd0f-88764869cc1f | -3.0354 | -45.1419 | 2024-11-16 02:00:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 7675592a-825b-3d73-ba0e-4d29512d999e | -3.7394 | -45.6523 | 2024-11-16 02:00:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 193.7 |
| a78185ba-6711-3224-bd4d-9f35591f12b6 | -16.93046 | -57.63225 | 2024-11-16 02:00:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 27.8 |
| 194957b9-6ff4-3df2-8aad-2b92cffda125 | -17.56371 | -57.55466 | 2024-11-16 02:00:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.0 |
| 6052b1da-7ec3-3553-8e8b-17b16c1fc472 | -17.56761 | -57.43735 | 2024-11-16 02:00:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.0 |
| c5ccb9d7-527b-3b14-a7e5-e5ce0c2dc484 | -9.65228 | -65.74095 | 2024-11-16 02:00:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fad63068-b058-3c3f-bfbc-c5fa5c1482ae | -17.55829 | -57.5226 | 2024-11-16 02:00:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.7 |
| e2647c53-0b89-3f82-8fe2-3e6096e06321 | -15.91851 | -59.27735 | 2024-11-16 02:00:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a742f442-0697-30ca-bc48-c0c35538aba9 | -10.12474 | -65.02197 | 2024-11-16 02:00:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 8744e1a4-30de-3f56-98ca-a7737cead469 | -9.58533 | -64.58187 | 2024-11-16 02:00:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6067c889-cae1-3e18-b5d8-baed4b43b5b1 | -10.12599 | -65.031 | 2024-11-16 02:00:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 18.5 |
| b86cdab9-dfa0-38af-ab16-8e0c8df32c74 | -16.10021 | -60.10534 | 2024-11-16 02:00:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| f5cf835c-9f80-381e-98b9-b8d6fa32be1b | -17.63217 | -57.55183 | 2024-11-16 02:00:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.8 |
| 8d12dde5-bf0c-3981-80d1-0ed9dc9b419f | -17.54958 | -57.54079 | 2024-11-16 02:00:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.1 |
| 519f1ca5-76b4-379b-91c8-42c23f98602f | -16.93317 | -57.64838 | 2024-11-16 02:00:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 1672e45d-cc07-3ad5-9c4b-0a8c7af291d1 | -16.09768 | -60.10001 | 2024-11-16 02:00:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 30.1 |
| a195cffd-8206-32b3-8a79-b452696e3e5f | -17.57034 | -57.45366 | 2024-11-16 02:00:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.0 |
| d57a65ea-da4d-3e84-9a8d-70831c972a3c | -16.95611 | -57.64412 | 2024-11-16 02:00:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.6 |
| 0af504cb-cd78-36d3-aec8-9f0d93656ead | -16.0154 | -59.37337 | 2024-11-16 02:00:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 205d5df3-7bd8-3e8f-9bb4-23185771cd75 | -16.94194 | -57.63012 | 2024-11-16 02:00:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.5 |
| ec86710d-ff1b-3bda-b7e0-740064cedc73 | -16.96758 | -57.64198 | 2024-11-16 02:00:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 1c9985a1-0ac1-37b7-a520-378e5c6c5d28 | -16.94464 | -57.64624 | 2024-11-16 02:00:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.8 |
| c2dfefe1-1cb9-32e6-b694-e70375ddf662 | -16.09842 | -60.09396 | 2024-11-16 02:00:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 12b8da5d-401f-3c33-aeea-9f7d3522bda7 | -16.95342 | -57.62798 | 2024-11-16 02:00:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.5 |
| 5bcdedfc-14b7-38aa-96c3-2b0bfba05579 | -17.5778 | -57.56848 | 2024-11-16 02:00:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.5 |
| 5a26ca2f-6139-346f-a11c-90d4e066b397 | -17.77954 | -57.60023 | 2024-11-16 02:00:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.4 |
| a92c6a95-7cbb-37b4-98d5-f584d63af606 | -15.67192 | -59.73293 | 2024-11-16 02:00:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e7764094-d2c7-312a-87fc-01bcbb58e3c5 | -16.09595 | -60.08858 | 2024-11-16 02:00:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 947fb8be-490a-3c59-aff9-5da5780510f7 | -17.54685 | -57.52476 | 2024-11-16 02:00:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.3 |
| 964ccd76-8f66-3323-a4bf-2fb38be3454e | -15.91642 | -59.26416 | 2024-11-16 02:00:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 090ed4d6-bafe-3372-a40d-8d2b827d2323 | -9.70664 | -64.19653 | 2024-11-16 02:00:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6ff85e43-d5c8-39bb-93c0-7ecb506a19e1 | -10.03182 | -64.22186 | 2024-11-16 02:00:00 | TERRA_M-M | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 99d84b80-511e-32d4-b906-0e4e4f479160 | -17.59186 | -57.58224 | 2024-11-16 02:00:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.8 |
| 69b27563-d336-3be8-b458-00fe56a3fbf7 | -17.5664 | -57.5706 | 2024-11-16 02:00:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.2 |
| 6348bba5-45e7-3796-9d82-4233b4dff3d8 | -17.65285 | -57.46511 | 2024-11-16 02:00:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 5d64ed5a-7b90-3181-8c28-db4b0b6a87a9 | -17.57512 | -57.55251 | 2024-11-16 02:00:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.1 |
| f33f0556-1b13-3e1e-bd15-a858d83362a1 | -17.65012 | -57.44891 | 2024-11-16 02:00:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 43478359-29c1-30ab-9f51-eb9f4d3bca3d | -9.58548 | -66.40307 | 2024-11-16 02:02:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 204eb2c5-815e-3fb9-9a71-7d40811b9abf | -9.70061 | -66.9735 | 2024-11-16 02:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a7f09809-9bbd-39ed-9fa1-fec43e167bbf | -9.06977 | -65.85655 | 2024-11-16 02:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1cfc541e-7de9-38d5-9d5f-0aa0e963c234 | -9.24779 | -63.6242 | 2024-11-16 02:02:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d5861e95-1211-32ae-be26-97dd79a25b24 | -9.70417 | -66.96713 | 2024-11-16 02:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6cf963e5-77e6-399b-8717-60dc3f9f9ef4 | -9.70553 | -66.97761 | 2024-11-16 02:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 336b646e-4949-39fa-b487-970a024c4693 | -9.0788 | -65.85528 | 2024-11-16 02:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e4dc4f2e-035a-3884-b0dd-292b3c746fc7 | -3.7685 | -50.7908 | 2024-11-16 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 0d00c702-e261-3a0d-86e5-7efe0399b649 | -3.7208 | -45.6531 | 2024-11-16 02:10:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 0a995f96-b42d-3b5f-9fdf-8b1d2c0d532c | -3.1823 | -45.5412 | 2024-11-16 02:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 55.8 |
| b42fc2d1-a291-3e80-90f9-e5d96b2f553a | -2.1562 | -53.7039 | 2024-11-16 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| f909f7e4-0141-38cf-88b5-0d991396b266 | -3.7394 | -45.6523 | 2024-11-16 02:10:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 63d76c86-671f-3696-8a17-a2956461947d | -3.1273 | -54.5264 | 2024-11-16 02:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 94f54433-c38a-375c-999c-c43ee9d3d049 | -3.1822 | -45.5636 | 2024-11-16 02:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 3fa2f2cc-2e56-3a27-937b-1c1181d461fe | -3.7207 | -45.6755 | 2024-11-16 02:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 30211f4c-7bb1-39bf-9059-7ee5207f8336 | -3.2008 | -45.5629 | 2024-11-16 02:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 0922a66e-72fb-391f-ad9b-516fb3d428aa | -3.2009 | -45.5405 | 2024-11-16 02:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 0b73dda4-8c9f-37f0-b15d-1a8b42cef7d3 | -3.7393 | -45.6747 | 2024-11-16 02:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 7be52581-7b98-3e76-8184-5ba93fcb4753 | -16.958 | -57.6269 | 2024-11-16 02:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.0 |
| 35a8d415-2cd0-387b-be59-0767cb817f72 | -6.1363 | -42.578 | 2024-11-16 02:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| f67b1637-4b4a-38d2-9c5f-7148886c7011 | -16.9577 | -57.6473 | 2024-11-16 02:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.2 |
| acf76e93-6420-3a4e-add1-a3cdaa0d39be | -4.9971 | -44.3149 | 2024-11-16 02:10:00 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 27b82418-c03c-3a88-b98a-f66de5e4cd21 | -16.9384 | -57.6291 | 2024-11-16 02:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.8 |
| b282373a-d298-36e8-954f-32af573afe69 | -2.3595 | -47.1408 | 2024-11-16 02:10:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 8433a864-37cf-3dbd-9ac9-2d47009c1c3d | -2.78 | -48.5806 | 2024-11-16 02:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| d0bb1225-656e-3a49-9a11-84d934546141 | -5.6796 | -35.6418 | 2024-11-16 02:10:00 | GOES-16 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 89.2 |
| 436e92b6-fffd-3a84-9a9c-e0ca86a19c5c | -2.1379 | -53.7043 | 2024-11-16 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| ec90bbea-a87e-37d5-a8c4-dea76fc08227 | -2.1562 | -53.7241 | 2024-11-16 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| bca6afbf-01a1-3a5c-9230-c25deb9d2c8e | -2.5456 | -46.8944 | 2024-11-16 02:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 7e82edde-d71e-3e59-9ffc-c63165d1a9b2 | -2.5642 | -46.8938 | 2024-11-16 02:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 39ec3475-f548-390a-a971-054b6818d869 | -3.0356 | -45.1193 | 2024-11-16 02:10:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 01f2b74e-c461-394e-b750-87d03351973d | -2.1378 | -53.7244 | 2024-11-16 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 24c4fbc4-278d-36fa-9f8c-88af574c9ce6 | -3.0354 | -45.1419 | 2024-11-16 02:10:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 7abe9be9-ca16-3f4c-b777-0cb8cb935616 | -2.651 | -48.477 | 2024-11-16 02:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 4c01d032-5470-357b-9000-27b49f518af3 | -2.2299 | -53.6219 | 2024-11-16 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 946f20ee-d8d6-328d-9748-8b8403017f87 | -2.1562 | -53.7039 | 2024-11-16 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| dfc1d86b-e505-315a-b8ca-788e04934e0c | -3.7393 | -45.6747 | 2024-11-16 02:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 126.2 |
| 39a9e77c-cf88-36ee-8027-1b58071472a2 | -4.9784 | -44.3161 | 2024-11-16 02:20:00 | GOES-16 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| fd88d3b3-0baa-31de-9bde-a1870c38f7f2 | -16.9577 | -57.6473 | 2024-11-16 02:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.2 |
| dbd66a89-4ca9-320f-9265-5d18a281b8d8 | -3.0354 | -45.1419 | 2024-11-16 02:20:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 128.9 |
| 09e4ba47-7501-3b46-af3b-e5e0ce3afea7 | -3.7394 | -45.6523 | 2024-11-16 02:20:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 190.1 |
| 8a82b798-3298-3854-b259-dbea30b06143 | -3.7208 | -45.6531 | 2024-11-16 02:20:00 | GOES-16 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 57.7 |
| bca9f559-ed00-3fe1-9caf-3d27c53c9564 | -2.2299 | -53.6018 | 2024-11-16 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 25e83747-3c12-3d86-9512-c2e463e141a4 | -2.5456 | -46.8944 | 2024-11-16 02:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 70c6a19c-0853-3d07-80fa-677ebee1cdf5 | -2.1378 | -53.7244 | 2024-11-16 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 35cbf7cd-8395-3756-b0c2-66521aea6b33 | -3.1822 | -45.5636 | 2024-11-16 02:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 55.5 |


[Clique aqui para ver as próximas entradas](README13.md)
