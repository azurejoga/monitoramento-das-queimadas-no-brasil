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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca8c113b-27c7-3831-94ca-f1efc94f5d39 | -8.21355 | -64.09614 | 2026-09-24 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e64c984-3da2-315a-bdca-c31f06d3a972 | -8.92295 | -61.48704 | 2026-09-24 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a24dfe77-f7e6-3ca7-8f22-76bf3dbb6c39 | -8.93657 | -68.55974 | 2026-09-24 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2c6ff11-15cd-31a5-8c0f-d0ce857b3cf5 | -6.67314 | -58.5851 | 2026-09-24 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f03da814-f784-31e9-b38e-d1a0cc3b63d8 | -6.43853 | -59.96059 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5eabcfa2-bd91-3fb1-8e71-17f56c280982 | -11.59863 | -58.50722 | 2026-09-24 05:50:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20ca9087-5f61-3ca0-8ddd-4d2c0af10443 | -6.89753 | -55.57311 | 2026-09-24 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0579ae78-4c7c-3022-a08b-081e43978b87 | -8.02892 | -71.36264 | 2026-09-24 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 3e974f53-d80e-3cd4-92d9-73d7543ba09f | -8.27084 | -54.76863 | 2026-09-24 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9f0ae7b8-1e59-3edf-9eb3-f9f3e02b7c7d | -7.52248 | -70.39517 | 2026-09-24 05:50:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fe4470f-2360-341c-8374-bd69df8cc05b | -7.66342 | -69.93039 | 2026-09-24 05:50:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c759d26-4dba-3245-b7c3-147873a0a56b | -11.92551 | -63.15747 | 2026-09-24 05:50:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 719850da-579b-36e2-ad8f-80cfb1e3ca12 | -8.58393 | -67.31419 | 2026-09-24 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22e35dd0-a6ac-3fb4-bbc1-2ac9832097b5 | -10.4848 | -68.23454 | 2026-09-24 05:50:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eaf3ba2e-1a5b-3d12-9c68-10d8962c0bfa | -8.92728 | -61.48773 | 2026-09-24 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83b4b3d3-d851-37da-82c0-365509087307 | -6.68261 | -55.05161 | 2026-09-24 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b80a7ca-2df1-3ad4-ae7c-d1309d97db36 | -7.51258 | -61.4851 | 2026-09-24 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f7d3519c-e07d-3ac3-91e2-94507e3d7abb | -8.35388 | -70.54821 | 2026-09-24 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad444711-a4bb-3de7-a30c-1c000b4b3491 | -6.31014 | -59.94726 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cdd504e2-738f-3c69-8dac-1917c15228c0 | -6.6726 | -58.55106 | 2026-09-24 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8296679-ab69-3427-8a2e-29673726fdd9 | -6.46224 | -55.00608 | 2026-09-24 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bfa10b9-36fb-3d90-972a-0302e8bbc527 | -10.24056 | -68.2957 | 2026-09-24 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7e9d777-0568-3696-b94e-dea578fb4c96 | -8.11488 | -70.14276 | 2026-09-24 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c48062f-7d74-36e1-90dd-52b1fd7a6d3e | -8.91318 | -68.64299 | 2026-09-24 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d5c6868-53a3-3d2c-b619-ecc70e7e289d | -7.99446 | -71.33832 | 2026-09-24 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5935a372-a7f7-3164-83b0-ae2dc2c106bf | -6.1218 | -57.75996 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f981384-4fe8-348b-9b02-ac21e5f78a52 | -6.10803 | -59.87668 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ead2e289-5f84-3055-92f1-b798fa32a784 | -9.04558 | -65.42516 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ac943cd-63cf-3f5f-b663-c84f35838cd6 | -8.56927 | -70.88504 | 2026-09-24 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aac40b36-3aa4-3358-952e-d7cd8a48c2ce | -5.86284 | -60.15981 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d14d6a19-bb59-305f-9c4f-bf39e1bb0a71 | -5.86195 | -60.15784 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 266807dd-854c-3540-a0dd-47ca388c1a50 | -9.03828 | -61.65794 | 2026-09-24 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 77440e4d-1e85-3390-bc38-94b154331943 | -9.64202 | -67.06995 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bab50809-ead4-348a-bfe2-ecffab29cbbd | -6.11374 | -59.87993 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1ee3fd5b-7272-3a82-84d1-9ac67087f31f | -8.58612 | -62.51472 | 2026-09-24 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e82d496d-c16d-319d-9dd7-94b1397f5681 | -7.87818 | -61.17745 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29255718-7e42-3d45-8b25-84a9f403e904 | -8.90985 | -68.64246 | 2026-09-24 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2c649fa4-6928-34dc-b510-c982767102a0 | -9.72389 | -65.02473 | 2026-09-24 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16a2c14d-fc3b-3263-938c-c46250640ba0 | -6.68191 | -55.05703 | 2026-09-24 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6dfd6fbd-3e44-3fae-b6ee-72baa2e75b0a | -9.19404 | -65.79102 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a0a4103-8b9a-3a86-9d6f-3d6e3bedd6f9 | -9.04095 | -65.40878 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 613d2e67-40b5-39a3-88c7-b9d388ced6ae | -6.1027 | -57.67941 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0b59b9c-a15d-3d09-90c6-a4d5ae4da476 | -9.70066 | -64.91418 | 2026-09-24 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 24737b9c-69e3-3a79-b736-4f582f6c2fba | -6.11199 | -59.88233 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5ff07528-da5e-374f-b5bd-4f524cdd8ba5 | -8.26647 | -54.77567 | 2026-09-24 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| dc47c781-6d9f-361d-aa78-6ec3b38b1057 | -8.86914 | -62.53768 | 2026-09-24 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83db4b3e-b0c0-3b78-b1d1-fae12a46ecf4 | -8.37866 | -70.5312 | 2026-09-24 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 195c271f-4ec9-3bc2-af90-9ab471199b3d | -8.31593 | -70.53355 | 2026-09-24 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ff1757e-e6dc-32c4-93ae-49f6fe898bb5 | -6.10515 | -57.68013 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86314e90-d038-3ba1-8500-e7c5c1893882 | -6.54978 | -62.91754 | 2026-09-24 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 814864ff-a393-386c-9142-439078a69de3 | -9.19641 | -65.61071 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0313121c-9b0b-399c-924a-971ad0fe4a80 | -8.64284 | -67.02467 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b42fc5f4-f356-3aad-8e8c-9e21a10e5ef3 | -6.4645 | -54.99765 | 2026-09-24 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb9a3d6a-bf4e-3b26-bb46-ce6c9441e524 | -7.66794 | -66.9957 | 2026-09-24 05:50:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a15b3f2e-fb70-378b-8023-0c07dfebf24c | -8.02442 | -71.36659 | 2026-09-24 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a6b146b4-d505-3bb1-a49a-356b3916c83f | -6.44385 | -59.95638 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b9cef98-9505-368d-abac-9a33073a4c83 | -5.91923 | -59.92376 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29775e8c-70cd-3414-a4e5-89fd32ec9061 | -10.24332 | -68.29973 | 2026-09-24 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac4445ca-2967-3b7b-9cca-802aba44d245 | -7.51957 | -70.39046 | 2026-09-24 05:50:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a2fbd7de-1770-3fcf-8a60-be8ea6cfef86 | -9.10908 | -61.43465 | 2026-09-24 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cc51d6d-e60d-305e-b1cf-3d2ffc350ac2 | -9.04961 | -65.42187 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5bc81a9-5268-34e0-8213-3f669e00ad08 | -7.52606 | -70.39576 | 2026-09-24 05:50:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b82ae507-3cb5-34b5-bc82-8a1e4738f507 | -7.47765 | -63.81001 | 2026-09-24 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cdc33bb2-cde7-33c0-a800-405b6fa0ea85 | -7.05003 | -62.93539 | 2026-09-24 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 981521d7-7f1a-3439-add7-cc2174271884 | -8.26725 | -54.76949 | 2026-09-24 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4ad6ac34-8883-32d0-89e9-0fdee515547a | -8.63085 | -66.99017 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 275c71ff-cb58-356d-af13-f9bda0f7b7fd | -9.93421 | -60.7159 | 2026-09-24 05:50:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 87c85b1a-15e1-3d1d-bb6f-46ce7cd10d1a | -8.64946 | -67.0257 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6600f68a-e5d2-3c55-b0d4-126f6fa5ada1 | -6.11266 | -59.87744 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 80c58113-e888-301f-9725-2a8e99e628e1 | -9.22448 | -67.39441 | 2026-09-24 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75ed5659-0b5a-36b9-be47-0ee74514b486 | -7.66848 | -66.99223 | 2026-09-24 05:50:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eca7ff4b-b56c-3d6b-9a77-b775e324d6f9 | -8.91478 | -71.33897 | 2026-09-24 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3466f3fe-acaa-3740-9845-d0ad226b1c15 | -9.76163 | -65.03876 | 2026-09-24 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01ac7a90-cd03-3724-bf00-0e3bd9b8c7cb | -8.64642 | -70.937 | 2026-09-24 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d27b454-cbbf-3ac2-9c25-b6d3547f22b2 | -8.6423 | -67.02816 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3f5d45b-4cd7-39e0-8632-4f6b34a2e097 | -6.10736 | -59.88153 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bf73baf6-3cc8-3e91-81ec-e226de1fbcf0 | -7.52181 | -70.39928 | 2026-09-24 05:50:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01002db2-e804-3146-aa21-bd9d5651c1a2 | -8.02948 | -63.89516 | 2026-09-24 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5e52720-1320-3f31-969e-77c53bdb3670 | -8.63138 | -66.98669 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3606fa63-587f-399c-9bde-fa92e3a51267 | -9.22172 | -67.3904 | 2026-09-24 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b38686c2-cef3-3292-ba37-5148bb267c8b | -8.98254 | -65.40472 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b82c9d7a-ed1f-3f80-b896-9b9d1d1e985d | -8.88996 | -62.54364 | 2026-09-24 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cd0626fa-8566-3e89-a2c3-bb8af1cead09 | -7.66898 | -70.07323 | 2026-09-24 05:50:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7128256f-7df4-3151-a4ef-4aa38386ade7 | -6.77528 | -63.14396 | 2026-09-24 05:50:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 486f3d0a-4fa5-36fd-8b34-7844d76137b9 | -8.30715 | -56.36769 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d31a2b5-5054-39fd-b84c-91d7d0b716df | -7.90666 | -61.16455 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bc07100-19a6-3ee1-b0c8-3c89645c56ed | -7.42012 | -70.10796 | 2026-09-24 05:50:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bef759d0-7203-328c-8e93-20e477eb3679 | -8.87381 | -62.54127 | 2026-09-24 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39e832d2-bbc5-3208-a56b-3cc3af731fa0 | -8.19853 | -70.47347 | 2026-09-24 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e63eb8aa-0a5e-303b-9150-685c09c077d3 | -8.87785 | -62.54187 | 2026-09-24 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4efd2a27-77d6-3855-b889-21b58056f262 | -6.76773 | -63.14282 | 2026-09-24 05:50:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51bc0c8c-e0f4-36c2-9142-9ed6dfb63379 | -6.92666 | -62.90454 | 2026-09-24 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6efc18e3-8073-3818-9f66-1a9717e40c83 | -6.60777 | -59.9275 | 2026-09-24 05:50:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eb7d4a59-d0fa-3d3e-8f78-b2a535a5d01c | -6.68158 | -58.56186 | 2026-09-24 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 599b5276-2848-33ee-9fee-624dd3895413 | -6.67355 | -58.58212 | 2026-09-24 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a176df6-f645-3e51-a80d-c06e7eee9acf | -8.91405 | -71.34341 | 2026-09-24 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9128292d-a819-3d39-9193-acd4dab3d77b | -8.54982 | -66.72289 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2ecfb64b-fa71-3fd7-a0b2-a1a213468721 | -8.65729 | -62.47795 | 2026-09-24 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abce4e82-d431-38d1-9146-17de4ac7aeeb | -7.87637 | -61.18274 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66bd2b05-ce04-3eed-b1f2-de46d8123a6d | -6.08265 | -57.62588 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README86.md)
