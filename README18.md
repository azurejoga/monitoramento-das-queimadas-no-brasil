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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf990219-54e6-32ab-b6c8-0aa7da1b8ad6 | -9.89953 | -63.58632 | 2025-10-22 05:16:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b002d73-fe3b-31b6-b13e-644089ee3a9d | -9.00335 | -65.93378 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 2da01151-e60c-3dd4-8de1-ee63a06257e6 | -9.89749 | -64.88397 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96a5f56c-eb96-36e9-a9b5-c8260b6119b2 | -8.99235 | -65.91817 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d7233f3-0b51-3b80-ba5d-97cbce6a61ad | -7.93154 | -46.02324 | 2025-10-22 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 53c47e85-77c7-3378-be5b-64fe962c1511 | -9.00121 | -65.91975 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ed50c653-4385-3e2b-9304-d375bcc68cd5 | -9.7297 | -64.93902 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9be2bcc-4fbb-3dd3-9673-26cd029500fa | -9.91126 | -65.02365 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9694911-175b-3e50-91a5-fb9a32b5fc04 | -9.00931 | -65.92574 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3397b28e-95cf-3fac-8671-5a2659c1232f | -9.01068 | -65.94429 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f99189a9-80eb-3cf2-aeab-be33f76f309d | -8.99678 | -65.91896 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8293df0e-176e-36b7-a3d9-97a879db3b0d | -9.37912 | -64.49331 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63b6979c-d63d-3c8a-897a-428c4ec4e84c | -9.00259 | -65.9382 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 36df25f1-971c-37f7-85b4-e340f4f69011 | -8.11447 | -55.08595 | 2025-10-22 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 551b1919-195f-3c63-9855-aad912b3632d | -9.90715 | -65.02293 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecf454c7-5458-321b-88bf-acb73df783ca | -9.09251 | -67.69118 | 2025-10-22 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| addd7927-8c30-3b6b-9bb9-2bf95586284c | -7.93242 | -46.0166 | 2025-10-22 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6c07f3cf-3f49-3822-bf3f-d47d24b47fab | -9.65007 | -65.25421 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6b5738b-c3a6-3d81-9f5a-84e696608bee | -9.90997 | -65.03114 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e41ae1c-be38-326e-8c4d-2609b26fc8c0 | -9.48659 | -65.64787 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f751f717-1d84-377f-9d9c-36511015ec16 | -4.84134 | -50.62 | 2025-10-22 05:16:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a4a6158-299f-3431-860e-92883400d6ba | -9.00045 | -65.92416 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 11b2a3fa-c35b-351b-b8ce-2ac17cbb2b8c | -8.99892 | -65.93298 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 598a8091-9246-3e3d-b0e3-902eee0c891b | -9.01004 | -65.94157 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 53f9c087-40b2-36c2-b503-d6d42e100dc1 | -7.92623 | -46.01769 | 2025-10-22 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b201c693-f67f-304c-a953-e9477a2b9359 | -9.483 | -65.64296 | 2025-10-22 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1c1cb4e-6e7b-3dbb-9b1b-e87ccf5b4259 | -9.10618 | -65.94042 | 2025-10-22 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2aa29a39-9749-30e9-978a-7b6b989ec505 | -8.11827 | -55.08651 | 2025-10-22 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| faea140e-95c4-33a7-b776-ba4d1cf37eca | -9.86043 | -64.16621 | 2025-10-22 05:16:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e954271-12d5-3f1a-88a8-83bd3c7bf363 | -14.68784 | -48.7896 | 2025-10-22 05:18:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8cf782b6-f242-3424-906d-506573f4063f | -18.14572 | -52.98575 | 2025-10-22 05:18:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4209edc3-87d7-3c9c-b17c-056def7887d9 | -18.16749 | -52.97329 | 2025-10-22 05:18:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f57274f-11ef-3c6a-8e2a-d802dad79932 | -12.37635 | -63.8703 | 2025-10-22 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fafa1e5d-6793-3d34-9a2b-cf03c67c99fa | -18.15141 | -52.98035 | 2025-10-22 05:18:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 455b4321-7b2c-3907-a20f-5b1bc74f3498 | -11.21771 | -62.37012 | 2025-10-22 05:18:00 | NOAA-20 | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7fd9a55f-2e8a-34d9-a09d-2f5e5126aee8 | -15.28142 | -59.24039 | 2025-10-22 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f7081661-4868-353e-821c-fa422379ac9f | -18.15208 | -52.97439 | 2025-10-22 05:18:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee31a58e-8748-3199-ad16-b42a86d2e20f | -10.01286 | -67.8763 | 2025-10-22 05:18:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3f61aa1-2f9a-3ddb-ad50-858e209eefea | -14.53678 | -53.76752 | 2025-10-22 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 391661b3-b954-37c5-8f17-7db3bbe61ba7 | -10.92452 | -68.58657 | 2025-10-22 05:18:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 931c9efe-1bbc-3329-aabd-57d48e7c431a | -17.02105 | -55.91164 | 2025-10-22 05:18:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 7cc38907-106c-3618-806e-57aa5ed1aa87 | -9.98051 | -67.73923 | 2025-10-22 05:18:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db609332-75a8-3d97-a276-534dd16316f1 | -17.67363 | -54.21442 | 2025-10-22 05:18:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d751225c-b45a-39e6-b4ed-c323ff5b996d | -9.71454 | -67.4113 | 2025-10-22 05:18:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5f22d77-59cc-358c-892f-1a1d3192f66b | -9.72811 | -67.47585 | 2025-10-22 05:18:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1722da93-316d-38f0-9da6-578200a7ff62 | -12.12905 | -63.20836 | 2025-10-22 05:18:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e77972e7-b1ef-3547-b59e-7c2b9bbfd66e | -9.74899 | -67.10786 | 2025-10-22 05:18:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78c0096e-86bb-3081-b66c-74cdad51cd49 | -11.86588 | -63.36559 | 2025-10-22 05:18:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10203b5a-7511-3956-8910-0f16bf60bbf0 | -9.7143 | -67.48441 | 2025-10-22 05:18:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5445b6f1-a1d3-35df-9da9-524c008899dc | -9.71162 | -67.48393 | 2025-10-22 05:18:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ba0b924-3eb1-33a0-8d66-5737fd036b3f | -14.87341 | -56.24643 | 2025-10-22 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8cecafd7-6552-3d7a-837b-1b2a7350c65f | -10.94038 | -65.20848 | 2025-10-22 05:18:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d719aea-0ddb-37b4-82e2-6dd19f0a34ba | -16.24207 | -49.59469 | 2025-10-22 05:18:00 | NOAA-20 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34d6bc3d-e3aa-3f92-b4ef-fdaa6e1ded89 | -14.6946 | -48.78605 | 2025-10-22 05:18:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ec888f9-45cc-3f15-aac6-6ab5c38ccd3d | -9.80538 | -67.59308 | 2025-10-22 05:18:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1129282a-d643-35c2-9957-9271b6a25aa7 | -9.81027 | -67.594 | 2025-10-22 05:18:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9ab9035-6c58-32dd-a7af-383a4592f26a | -15.29949 | -59.25854 | 2025-10-22 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6973b713-9ce6-331c-a2f7-1f7dde250bbc | -14.6538 | -53.10826 | 2025-10-22 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4cf0f41-7a6f-3745-be87-f9f7744a24fc | -9.79779 | -67.0328 | 2025-10-22 05:18:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a894ba4-7a33-367b-9361-399da609151a | -12.37928 | -63.87544 | 2025-10-22 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e9f1e04-a70a-3590-93b2-32bed2b649f9 | -14.91609 | -55.81916 | 2025-10-22 05:18:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8783e220-4a43-3481-89b7-da5fff04d3cc | -15.48806 | -50.46019 | 2025-10-22 05:18:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4065718-6975-31b9-816e-8771a2700e10 | -16.04194 | -54.26723 | 2025-10-22 05:18:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 821f17f3-6874-3201-b59e-24776acf6599 | -14.65859 | -53.10861 | 2025-10-22 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30627219-aaee-32be-bc4d-105672cb03df | -9.73087 | -67.47631 | 2025-10-22 05:18:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6b7a8db6-d92b-3ec2-8a09-a08b4deadb01 | -18.15175 | -52.97736 | 2025-10-22 05:18:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b24f289-9a67-3a9a-b4b5-7671d2a1e0de | -12.38032 | -64.18861 | 2025-10-22 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc6567d5-1559-3768-a9d6-1edc49b241c8 | -9.96075 | -66.74142 | 2025-10-22 05:18:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2400752-ed57-36bd-b9f9-4d6bf7b61ef1 | -14.74771 | -54.11374 | 2025-10-22 05:18:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e776130a-c04e-3d4c-8377-8d91bf12fc4a | -17.67304 | -54.21932 | 2025-10-22 05:18:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e79f52b2-9f1b-31d5-90f7-18efc38ed2d9 | -18.20409 | -52.96538 | 2025-10-22 05:18:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c30924e5-0d25-36ef-bebe-482aee423110 | -15.48723 | -50.46759 | 2025-10-22 05:18:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5a784df-d7f5-31c0-afd3-af915cfa7226 | -12.58893 | -62.0146 | 2025-10-22 05:18:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e461b993-0184-330e-8dac-f0885c7786fc | -12.13551 | -63.21379 | 2025-10-22 05:18:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a9aa3694-8ec4-3104-ac64-468e0761f905 | -10.29476 | -67.99797 | 2025-10-22 05:18:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2c3ebcd-b19a-3ba8-a366-b22609743e12 | -9.79749 | -67.02694 | 2025-10-22 05:18:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e24d2048-5178-36c9-b2bb-99f20e0e6326 | -12.27115 | -63.87191 | 2025-10-22 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e61a5e9b-fb1e-3860-955f-39b8cca075fc | -10.41267 | -63.44191 | 2025-10-22 05:18:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ee2e34a3-fa98-3e47-89af-10cdbffb7b88 | -9.80726 | -67.59547 | 2025-10-22 05:18:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6bbee6d8-f2f5-3dbb-bb7a-c24c884f3bdd | -12.13193 | -63.21317 | 2025-10-22 05:18:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cdd0b444-0a8b-3d34-b75a-e5a546b2c5b1 | -9.71531 | -67.47895 | 2025-10-22 05:18:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72ba4475-694a-3303-9f4d-aa55d1620859 | -9.71647 | -67.48489 | 2025-10-22 05:18:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 29b527fd-5da6-3514-a908-09f660b3bb87 | -18.11616 | -48.53293 | 2025-10-22 05:18:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 459f413b-2f5e-3e33-9c45-2081ef3d257f | -16.09781 | -55.4166 | 2025-10-22 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dea72301-19fb-36bc-b3af-11e0b8db7a49 | -9.93316 | -68.22252 | 2025-10-22 05:18:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55df451b-6ba5-33a9-b8c4-2199397814fe | -10.92709 | -68.58533 | 2025-10-22 05:18:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 05df638d-10e9-31aa-add1-0162da1725c5 | -10.01391 | -67.8706 | 2025-10-22 05:18:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d4a1960-4394-3956-ad41-e3e44ee6ed23 | -16.77103 | -52.49209 | 2025-10-22 05:18:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0c6e8c0-da22-3a97-a8fa-14a6c10767d1 | -15.28086 | -59.24413 | 2025-10-22 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb10080d-9b10-343a-b6ad-b5d6dcef3752 | -12.51245 | -48.58057 | 2025-10-22 05:18:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0675ca16-15a0-3c5a-81cd-160681d01eca | -10.92964 | -68.58756 | 2025-10-22 05:18:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7fc3867e-30bc-3624-8819-0a7ca51b0685 | -9.71914 | -67.48537 | 2025-10-22 05:18:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf33374f-9675-36a4-89ae-fc9dc3c194b2 | -18.20374 | -52.96839 | 2025-10-22 05:18:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35675347-164c-39c8-8bde-7050facaaec2 | -12.13264 | -63.20899 | 2025-10-22 05:18:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b710ce04-13c6-3d87-9b71-d97caaa02607 | -10.94447 | -65.20927 | 2025-10-22 05:18:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce0e3886-1ddc-36ab-ad4a-bf88441887b0 | -9.9604 | -66.73911 | 2025-10-22 05:18:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c466418-c347-3ccf-854e-4dce537a5977 | -9.72602 | -67.47537 | 2025-10-22 05:18:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d3fffc67-210f-3c18-9a9f-4bf7318099ae | -10.75766 | -64.93854 | 2025-10-22 05:18:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5c79ebc-d6d3-3402-ae3f-f3b2e8b47fa5 | -14.80036 | -54.7154 | 2025-10-22 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a67619b6-ac59-3983-97fa-a6a17784fc72 | -9.72327 | -67.47483 | 2025-10-22 05:18:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README19.md)
