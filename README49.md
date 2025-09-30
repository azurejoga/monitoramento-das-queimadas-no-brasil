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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3fd2f9df-b558-3980-9e40-4df5930186e7 | -6.20329 | -44.35912 | 2025-09-30 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b584c337-3fdb-3ad7-8036-f8edecb1e6ae | -4.79493 | -49.46185 | 2025-09-30 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2627c58b-9108-3964-9724-24b611d6855a | -7.29205 | -42.86512 | 2025-09-30 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| edad78fc-84ad-3460-bea0-ea55ed2863e4 | -4.77774 | -41.04351 | 2025-09-30 04:38:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e5418a6e-9344-33cb-a4cd-23f66b1e01df | -4.95821 | -47.60445 | 2025-09-30 04:38:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ee3b69ef-c40b-3b6e-b7ee-740a199815b1 | -2.07045 | -56.87753 | 2025-09-30 04:38:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd9e6aa1-f7da-3fc8-98f4-2e58d8e9fbcc | -4.87534 | -48.88323 | 2025-09-30 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9873ca20-27d4-3925-b9a7-cbf8f596c7bb | -4.25923 | -48.5574 | 2025-09-30 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a2937879-398a-3f20-9c18-13e3b5680aea | -3.59365 | -48.98707 | 2025-09-30 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cce818e8-85dc-3324-82c3-5da53cb9d47d | -7.01526 | -44.47316 | 2025-09-30 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6f1e3d45-4d8c-3bd6-98ff-ba906f00b4b7 | -4.80873 | -50.736 | 2025-09-30 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8be38fe3-2e6d-3703-9664-81d965c5996e | -6.25415 | -43.6539 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e514f82-b628-3143-9848-3278b33598dc | -3.25502 | -49.12701 | 2025-09-30 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2a28d7a6-eac8-3878-88f5-9af381ed948f | -6.09076 | -42.44553 | 2025-09-30 04:38:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f17fd383-bf58-374b-a1b2-c8fd5acbe649 | -4.68179 | -50.50231 | 2025-09-30 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22ba067c-24e7-3c9e-b682-dc7ba7c45e0a | -5.91428 | -43.91356 | 2025-09-30 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec02033b-2ff0-3dca-a3e5-6d3c4781d3c8 | -4.33247 | -47.88797 | 2025-09-30 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86aef1f6-7f3a-31a0-953a-f5c283c0fb0a | -5.91421 | -43.70517 | 2025-09-30 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5474e6f6-e4e3-322d-a38d-6d1f7ad696c1 | -5.78054 | -51.75586 | 2025-09-30 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ab38bf3-6633-3a92-bfc2-277e5d81979e | -6.14093 | -43.48329 | 2025-09-30 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49c2f2a4-6417-3c8a-99f1-e3852786f5b1 | -5.33376 | -43.73434 | 2025-09-30 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 3a3d4364-82e7-3b93-b19b-331154b7b0c1 | -5.02875 | -42.99197 | 2025-09-30 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 515081f7-0b0a-3ee6-975e-2681781443ce | -5.8168 | -42.7781 | 2025-09-30 04:38:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5360267a-2b73-3b25-bf8d-1ed2ee83670f | -5.76965 | -42.85144 | 2025-09-30 04:38:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 388d3c2f-dc66-361a-94fc-1e638d003a0a | -4.37253 | -55.88802 | 2025-09-30 04:38:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 975c7ec7-19c6-3234-8404-a7b7ab70c72d | -3.94588 | -52.17326 | 2025-09-30 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c319f264-d4c6-3d33-9f9d-c9b9c51d1e28 | -5.04814 | -45.31048 | 2025-09-30 04:38:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 54101eb2-9811-362f-939f-92327e8f9ed7 | -4.39516 | -44.40186 | 2025-09-30 04:38:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7555357b-df9f-3888-a959-41f55441bc15 | -5.82389 | -42.7809 | 2025-09-30 04:38:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e6cafc81-6273-3bad-97a9-293c4e4b3416 | -5.50922 | -42.7288 | 2025-09-30 04:38:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0f2fb386-bfa2-3fab-90e0-f41ed8157312 | -4.8931 | -43.46775 | 2025-09-30 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 074b858a-d3fe-35bc-9f09-337235548fa5 | -4.98017 | -50.63724 | 2025-09-30 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d2a4711-0b32-3657-b2b2-fc1da7da8afb | -3.28216 | -50.0355 | 2025-09-30 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 95d65231-8647-3dea-b7aa-226e8393ff32 | -6.25956 | -43.91578 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 121733c1-6158-3232-8b73-32dd6f27903b | -6.90911 | -43.99902 | 2025-09-30 04:38:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1045a73b-ac85-34d4-9276-0504a42f57ef | -6.45905 | -44.00266 | 2025-09-30 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 88a87d3c-8c17-37a2-b51a-17a63fd9ecc8 | -4.40821 | -44.39626 | 2025-09-30 04:38:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18073d62-94e4-3e80-81d5-cb6f2bd2d5f9 | -5.2535 | -42.90437 | 2025-09-30 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ecab624b-fb80-304d-a243-779dc1cc66a6 | -3.25832 | -49.12753 | 2025-09-30 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cf77ef32-fe13-337c-aa89-5ce17ca4c0ac | -5.06547 | -42.9916 | 2025-09-30 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e387d724-74f1-3b0a-b1af-5e22a26be591 | -6.02918 | -49.40312 | 2025-09-30 04:38:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0a69b818-ce8f-34fa-a299-0fafe5724c74 | -5.33432 | -43.73056 | 2025-09-30 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 1ea01c5d-623e-318d-89bf-7ee29856de73 | -5.21915 | -45.22633 | 2025-09-30 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8f34c68a-9025-3c0e-b8b6-7815f747266d | -7.02809 | -44.78127 | 2025-09-30 04:38:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 873b14d2-22de-340f-9c11-d03560852a56 | -5.78303 | -51.74053 | 2025-09-30 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c234ef4f-9265-34e1-a936-a010285ee526 | -3.68177 | -53.97742 | 2025-09-30 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c00234b8-2f02-30c8-9074-17737ed69fe7 | -3.74811 | -51.38076 | 2025-09-30 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 150c3641-28c0-37f4-9ba2-962e8252a354 | -5.8793 | -48.1153 | 2025-09-30 04:38:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| faf3b676-e86c-3398-88f2-2b3acf1ddeb7 | -2.6913 | -54.76708 | 2025-09-30 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f42f4efd-09bd-32d3-81f4-b848b8167e8e | -0.0937 | -51.27521 | 2025-09-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c8622eb7-0701-3e88-9d5f-2e93d8fbbe2b | -6.08658 | -42.4412 | 2025-09-30 04:38:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 653ddaef-a434-3834-b3d8-05e470738580 | -6.49984 | -44.26702 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 02f985a9-9ccf-36b6-81e5-5e71ad5a8017 | -6.53705 | -42.83314 | 2025-09-30 04:38:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| fd73c322-fdfd-3aac-bfa8-1e54610a8c43 | -2.30526 | -48.14544 | 2025-09-30 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 446af388-87f3-395d-94d1-4fe22e7374cc | -5.74813 | -42.87478 | 2025-09-30 04:38:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 0a27e00b-a13a-30ab-a7ee-be7eb008e5dd | -6.69333 | -42.79612 | 2025-09-30 04:38:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 9494679f-c756-39e9-a486-2ad17f47064c | -4.40035 | -44.39508 | 2025-09-30 04:38:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 901fc064-6be5-322b-b56e-562b10743bad | -5.82508 | -42.784 | 2025-09-30 04:38:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 813c297a-75e4-3fee-9c34-91a76500e1c0 | -4.64307 | -50.67999 | 2025-09-30 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e575b220-1aba-3ac3-9c3b-d38149e9696f | -7.17271 | -41.70427 | 2025-09-30 04:38:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ebeb35e6-acd7-38b1-95a1-1ff8308beba4 | -3.88841 | -42.51295 | 2025-09-30 04:38:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 76111ae6-ac85-380a-9392-51116b75926e | -6.87745 | -45.09503 | 2025-09-30 04:38:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d991ee16-4bb6-3cc1-849d-4960ff60d0ab | -3.2225 | -47.63346 | 2025-09-30 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3af25d6a-8825-3f0e-9c99-19bd25c2163e | -7.36149 | -42.09367 | 2025-09-30 04:38:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a0f107d6-c896-308e-bf07-4ed62d0e6485 | -6.55696 | -43.41396 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1875aca0-db0c-34ce-b066-b5eefd8bcd16 | -4.66566 | -46.46462 | 2025-09-30 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a345e449-a4df-3a1d-b442-dd1903d2c15e | -3.41998 | -51.23232 | 2025-09-30 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71c7604b-52b2-33bb-9641-624766838bd5 | -5.27058 | -42.88022 | 2025-09-30 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fc5e326b-ccd9-3b59-bf17-8c68dadb5b12 | -6.47431 | -44.21525 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ce44f31-a3f4-3930-b419-079e7f84e538 | -4.58442 | -50.68946 | 2025-09-30 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 62f2aac2-3fe7-3ba7-b68e-562c0617da71 | -4.58385 | -50.69306 | 2025-09-30 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce935829-1d11-3f81-a568-3f74f006c5ef | -5.73285 | -43.96341 | 2025-09-30 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cf66ea1e-3840-3812-832e-cc2129461fcb | -5.7282 | -43.96637 | 2025-09-30 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 25d5678d-c7d4-3fea-800a-978e50d05310 | -6.3117 | -45.90087 | 2025-09-30 04:38:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a96fb543-105b-318a-9ba2-826abd650773 | -6.14811 | -42.79119 | 2025-09-30 04:38:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cfb254b2-cd7e-334f-a179-ebde6b20d340 | -5.88028 | -45.80689 | 2025-09-30 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbbd54c3-e468-347e-8eab-b8efc51090a5 | -5.92803 | -43.51955 | 2025-09-30 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20651c10-4ed7-3bfa-8237-9c391c33d11b | -6.36568 | -45.10338 | 2025-09-30 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23e876f4-5e01-3b45-b208-a0e4c2fd85ee | -3.33994 | -43.39389 | 2025-09-30 04:38:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8842d5c3-e005-3425-8dcb-10b11d21521d | -4.14682 | -44.42479 | 2025-09-30 04:38:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0e2f6a9-8113-366a-9dc8-366342579633 | -6.08687 | -42.44004 | 2025-09-30 04:38:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 06dfe1ff-841c-35cf-a2e0-d987b61c6338 | -5.74202 | -42.67788 | 2025-09-30 04:38:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 649cb267-74f3-306f-882b-8f2bbbf007c7 | -5.89388 | -47.59281 | 2025-09-30 04:38:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2620247-2a18-3008-bb32-7dbd9ba3b18c | -5.51777 | -43.86813 | 2025-09-30 04:38:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35ea6e09-18be-3258-99a1-1839128faf09 | -1.50221 | -47.47111 | 2025-09-30 04:38:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2027427e-0833-349b-83fa-46a66731c628 | -2.95011 | -48.94537 | 2025-09-30 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b4478ef-b7a7-3213-8a7f-526de2124cdc | -6.30673 | -45.90886 | 2025-09-30 04:38:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12f5ee6c-781b-3f98-a98c-506e40c80072 | -4.26307 | -48.55447 | 2025-09-30 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bcdfc534-d83a-3113-ba3e-361e27adb4d1 | -6.09237 | -42.66648 | 2025-09-30 04:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a793d96e-4eff-3669-bb63-cad9cae93851 | -5.28353 | -43.16214 | 2025-09-30 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 81415cf3-ef3b-3b9d-8822-49221bd16cb8 | -5.42362 | -42.29092 | 2025-09-30 04:38:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 27564b2c-a773-38f3-876e-7076d823bfec | -7.17508 | -41.701 | 2025-09-30 04:38:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a18d6b8b-70aa-37e3-817c-1043d9703839 | -5.97378 | -44.13406 | 2025-09-30 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8200435d-fc73-3cd0-9d15-d3738b977ccf | -6.21406 | -44.20012 | 2025-09-30 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b2d9203-a957-3aa4-9321-9b9282712da7 | -5.7503 | -42.66669 | 2025-09-30 04:38:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 5ff3fe64-6da3-3e63-b4ef-6689b791b2fd | -6.38533 | -42.91484 | 2025-09-30 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6424600e-1ae9-324e-879c-4a3ae1f4c6c2 | -1.59464 | -54.05872 | 2025-09-30 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6fa4211-b806-3cce-98e8-82483c79cf3c | -6.06662 | -44.87706 | 2025-09-30 04:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b7f4ecc-a57c-389e-b3a2-0a5d55b1b33e | -6.09368 | -42.65719 | 2025-09-30 04:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 1c241fce-394d-3f35-9c8f-2996ca679568 | -5.84685 | -44.86964 | 2025-09-30 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README50.md)
