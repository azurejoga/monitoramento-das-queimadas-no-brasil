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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1345965-e557-3652-8ffc-0b38e5de8548 | -2.4324 | -66.4758 | 2024-10-08 05:21:00 | NOAA-20 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5218091-c075-3686-84c5-25e8fcdb43df | -3.28698 | -47.12521 | 2024-10-08 05:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 829b3d7d-040c-3f0a-88c5-de10b06df187 | -3.28617 | -47.13092 | 2024-10-08 05:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50014634-595f-3fd6-8cb3-8aa9a37aca4c | -3.93888 | -46.44844 | 2024-10-08 05:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 39e8be4d-6ca7-3e3d-b8b8-875772d959d2 | -3.93798 | -46.45485 | 2024-10-08 05:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a151c509-5f9f-3c05-995f-67aa23e5133d | -3.93444 | -46.44452 | 2024-10-08 05:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 3a99205a-eda1-350f-b65f-1db95f66808b | -3.93345 | -46.45126 | 2024-10-08 05:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| f7df1da6-e4e5-35e9-8990-111fecc406ec | -3.93184 | -46.44748 | 2024-10-08 05:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f1f4acdd-ec8d-3ea0-9878-d82869d360cc | -3.93091 | -46.45414 | 2024-10-08 05:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 7e790f38-6fff-3b94-b8bc-4b4c11e77169 | -3.92742 | -46.44347 | 2024-10-08 05:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b95765e0-561a-3419-b399-eaed2c6e6b84 | -3.46221 | -47.66403 | 2024-10-08 05:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 76d78d54-252e-326b-91c6-3c5195d41f03 | -3.46143 | -47.66942 | 2024-10-08 05:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| faef1500-3e2f-3364-adb0-11dcce499ac5 | -3.22109 | -48.92698 | 2024-10-08 05:21:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 517edd45-578a-3979-a07c-ee7ce3dd7920 | -3.22043 | -48.93135 | 2024-10-08 05:21:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21152258-b804-381c-a0f8-940ad2452870 | -2.79207 | -48.56914 | 2024-10-08 05:21:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fe8cfde9-f8f9-3c9d-9664-1783a5742bf5 | -2.79138 | -48.57381 | 2024-10-08 05:21:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2a2db4ab-19c1-3c9d-ae8f-ecd1e93e0014 | -2.79071 | -48.57839 | 2024-10-08 05:21:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8d199aa3-90da-3868-9e7b-7f3b470ef1c6 | -2.40498 | -48.59551 | 2024-10-08 05:21:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54bcd839-54ea-3ee3-a928-382aa44e0305 | -2.40429 | -48.60011 | 2024-10-08 05:21:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70e060a2-7e98-3e7c-a133-8550a7571478 | -4.39595 | -48.69612 | 2024-10-08 05:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff9bfe39-f2ea-36d3-b5b0-89c37e887dc7 | -4.38979 | -48.69512 | 2024-10-08 05:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3be19828-fb96-3949-869d-8a60c44e6263 | -4.38293 | -48.6991 | 2024-10-08 05:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57d4e0f9-1ae6-35f1-9623-2aab820050ed | -4.38228 | -48.70371 | 2024-10-08 05:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e20d7d10-0ee3-3657-a580-2943fb09e4a1 | -4.18837 | -48.57143 | 2024-10-08 05:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e6eebd77-35d8-3748-b872-80241f1db0a4 | -4.1877 | -48.57612 | 2024-10-08 05:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08403d37-463f-36b9-b79e-c3a0a374e1fe | -4.09761 | -48.25988 | 2024-10-08 05:21:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64fe177b-ccfa-3c5e-a9b9-fd1e763c5dc2 | -4.09688 | -48.26485 | 2024-10-08 05:21:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebcf1bfb-0848-39c9-a6a6-a9109199d837 | -4.09613 | -48.26987 | 2024-10-08 05:21:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a824e9d7-abf3-3c88-befb-aeeae3ad00fd | -4.09461 | -48.25615 | 2024-10-08 05:21:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4194897-1d9b-3957-8d02-f3cb2d5f0940 | -4.09391 | -48.26113 | 2024-10-08 05:21:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e13c21fb-e09d-317b-ba83-ce827261b1d4 | -4.09321 | -48.26614 | 2024-10-08 05:21:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8dc1a0a-564a-3def-a7a9-87b65d77e4ef | -1.44804 | -48.88012 | 2024-10-08 05:21:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2eed3dcf-918e-3551-991f-0644ff23e601 | -1.44739 | -48.8842 | 2024-10-08 05:21:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 963254f3-48ae-3c84-835a-95c7b84a503d | -1.44671 | -48.88258 | 2024-10-08 05:21:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 076582dc-c8bf-365e-82dd-bebb875b3492 | -1.44609 | -48.88667 | 2024-10-08 05:21:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ae4f0f0-c0eb-3b8b-b349-9b5b2e7a591e | -3.50417 | -50.27387 | 2024-10-08 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9384d416-5cdb-3780-a599-6fb46b9bfc63 | -3.10345 | -50.38847 | 2024-10-08 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1a418e0a-22ab-3a6e-81d8-ed5e9b2276b8 | -3.10297 | -50.39165 | 2024-10-08 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f7786ef3-1b82-3bc7-b5e0-cdff9b17db25 | -3.0347 | -50.44173 | 2024-10-08 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6eb4b688-1905-365b-bd1b-c5e8eae6afe5 | -2.98366 | -49.52559 | 2024-10-08 05:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 084614d8-ea14-3d69-aa55-9ca55be8e590 | -2.98306 | -49.52964 | 2024-10-08 05:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 06d433ab-3066-32b1-a9ee-764bc9ed0d62 | -2.98248 | -49.53356 | 2024-10-08 05:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 821648da-134b-34ea-b518-1610d8d47e83 | -2.97793 | -49.52466 | 2024-10-08 05:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b2196cfb-ec46-335b-aadd-3041cab577fe | -2.97734 | -49.52868 | 2024-10-08 05:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6568b773-c342-32d2-af23-3d09119fb977 | -2.97676 | -49.53262 | 2024-10-08 05:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6158ebce-4eb8-3219-8722-5ba99fc5b2ba | -2.64152 | -49.26995 | 2024-10-08 05:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b158edcd-dc4d-32ec-afa4-eedb020bd628 | -2.6409 | -49.27402 | 2024-10-08 05:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12b2c905-0ae2-3ab0-a0f1-717841faddf1 | -2.45739 | -50.26003 | 2024-10-08 05:21:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 842e6ff3-7cff-33a6-90ad-dd289f55bc55 | -2.45197 | -50.25922 | 2024-10-08 05:21:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4da2381-e755-3c39-a811-c63c6cbab214 | -5.00747 | -49.59484 | 2024-10-08 05:21:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62bbd732-804b-3f90-b665-64eddf996d9d | -5.00687 | -49.59913 | 2024-10-08 05:21:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f872ed7f-f190-3bcd-a730-9a7ad00a4dbf | -4.95231 | -49.64706 | 2024-10-08 05:21:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4b354562-cc88-3bd5-8025-ed9ffc02bd10 | -4.94647 | -49.64605 | 2024-10-08 05:21:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49edb7c0-7c4a-3744-98fe-97282f21a591 | -4.85121 | -50.77219 | 2024-10-08 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1c63b08-209e-3fa5-90c6-68ca8d2c9e4e | -4.8284 | -49.81603 | 2024-10-08 05:21:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a82eabb6-75b7-377d-ac8a-54ce3a480e21 | -4.82766 | -49.81615 | 2024-10-08 05:21:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc47536b-8985-35d4-97f2-3376005f4536 | -4.82262 | -49.81516 | 2024-10-08 05:21:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0eef1672-c1db-3867-a90d-3450f3b5c171 | -4.8221 | -50.82101 | 2024-10-08 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd7c8285-20c0-35d7-96a8-d85a91c8ee33 | -4.82188 | -49.8153 | 2024-10-08 05:21:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e167927-8761-368a-9b28-fc10f7ec91f2 | -4.81668 | -50.8203 | 2024-10-08 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20f440ec-2697-3b4d-aba8-ca854956d269 | -4.46156 | -50.50589 | 2024-10-08 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e419824b-147c-34aa-90c8-511eaf61caa7 | -4.42051 | -50.78896 | 2024-10-08 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d257f46-1772-3a00-9323-9183fbb15ea3 | -4.37256 | -50.81684 | 2024-10-08 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c80f1ef-4d21-3c30-bca2-60b2c2f9d753 | -3.94832 | -49.96124 | 2024-10-08 05:21:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9107923-211c-3192-86db-cf9ae3002913 | -3.94777 | -49.96513 | 2024-10-08 05:21:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc283a90-b7d0-3f5b-ba8c-8445187741bc | -3.94496 | -49.96269 | 2024-10-08 05:21:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f8bfa2d-6ce2-386a-9e61-28a5291642a9 | -5.46287 | -50.66869 | 2024-10-08 05:21:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 683fecbd-64aa-3fb3-8e67-7b3129c8af6a | -5.41807 | -49.95947 | 2024-10-08 05:21:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0180b6eb-3f55-35eb-948a-f264e10d6177 | -5.06433 | -50.66139 | 2024-10-08 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff5daf4c-aef4-3fe2-aa29-76c1c02bf589 | -5.06383 | -50.66497 | 2024-10-08 05:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b487fb9-108f-3b4a-86a6-1189234dc09d | -2.15384 | -50.88373 | 2024-10-08 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb6409f7-2e32-3f33-ba7a-ff5cd37e5a3c | -2.1382 | -50.70469 | 2024-10-08 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a8d57418-ab7a-35f9-bafb-5f753e78d5f9 | -2.32111 | -50.52366 | 2024-10-08 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7129c2be-18ed-337e-95a5-5aab30faafc7 | -2.26497 | -50.6089 | 2024-10-08 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ec6a096-35fd-37ee-ae1b-a4650c56b190 | -2.25969 | -50.60812 | 2024-10-08 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8210eeef-c711-36ae-a673-cabc8c0e6347 | -3.59453 | -51.37349 | 2024-10-08 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0bc9ba2-9356-3412-a6c1-3c75bddaf23e | -3.59409 | -51.37651 | 2024-10-08 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c3324b6-7547-39f2-9d4c-4d1c01d025a9 | -3.48527 | -50.81154 | 2024-10-08 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bae5c92-72d1-3bdd-8f30-1e062298853d | -3.48478 | -50.8148 | 2024-10-08 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5d04d243-03c5-3ba8-80f8-8011c6cb0ff0 | -3.38722 | -51.4616 | 2024-10-08 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 379dd58a-51cc-3765-a7ab-6bfe3492f3c7 | -3.38261 | -51.45781 | 2024-10-08 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d54b97ee-43c2-367d-97c5-d963f80e9efe | -3.38216 | -51.46076 | 2024-10-08 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4a841901-1c9b-3d58-bc59-e4090ed40cb1 | -3.05074 | -51.10013 | 2024-10-08 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3eae856-cda2-35a5-8ee5-75a8527c809e | -3.04556 | -51.09948 | 2024-10-08 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b84a72b2-752c-3c19-b9fb-2c0a5ade9e90 | -2.97488 | -51.03139 | 2024-10-08 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e586bada-3cc9-3e71-86b3-0b39c2393549 | -2.97016 | -51.02747 | 2024-10-08 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4ceb07a-a100-3863-857c-184241bdf6b8 | -2.9697 | -51.03059 | 2024-10-08 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e052f443-3c9f-3110-a8e8-d9938d0e3aaf | -2.80827 | -51.39334 | 2024-10-08 05:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 023561d6-7a43-37ed-8b7a-7ad2578f0920 | -4.63422 | -50.98025 | 2024-10-08 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8f31167-e173-3ca2-8330-18708c4c2e17 | -4.63371 | -50.9837 | 2024-10-08 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae8225b2-be84-3cc6-a811-7874989b54ff | -4.62888 | -50.97948 | 2024-10-08 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d9ba553-5c70-37e3-8ac0-de6c0b212062 | -4.62838 | -50.98291 | 2024-10-08 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a51aefb9-66c1-3a65-a61e-5f4cb7529314 | -4.62788 | -50.98637 | 2024-10-08 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d746fa75-820b-3067-9c27-bbd4560ca23f | -4.62736 | -50.9899 | 2024-10-08 05:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 470bfd44-4099-37d8-967c-4025d013b3c5 | -4.15283 | -51.04408 | 2024-10-08 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b19c7320-9acb-3cdf-8a3f-bdcf428b8625 | -4.15235 | -51.04742 | 2024-10-08 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c7f541b2-833d-3246-b27f-3d83759685a6 | -4.15188 | -51.05064 | 2024-10-08 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1c355df1-a037-32ac-97aa-cc4f66ff8fcc | -4.06157 | -51.11943 | 2024-10-08 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b0f6b1e-68c9-33e3-ba41-115dbffd4681 | -4.0611 | -51.12265 | 2024-10-08 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2b47a29-0c53-3ffe-a69c-2c64d508067e | -4.05631 | -51.11883 | 2024-10-08 05:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README110.md)
