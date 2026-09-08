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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae2580f7-11dc-3aab-8290-7bd61450c37c | -3.14104 | -60.65825 | 2026-09-08 05:04:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dec0d153-f312-3f49-ac47-d5ea511bdaa4 | -3.54358 | -48.17737 | 2026-09-08 05:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 5a2fc06b-f6d2-3413-b74a-43d265b83ec3 | -4.78332 | -44.40191 | 2026-09-08 05:04:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f06938a2-567c-3092-949f-e0462a6ace44 | -4.50448 | -55.71256 | 2026-09-08 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| eb0cf796-9785-336c-996f-b3096f9cf4b7 | -4.44119 | -54.83496 | 2026-09-08 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99d29500-8256-3d55-a6c4-72a2edf9cccd | -9.73905 | -43.50257 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a6e627e4-74b4-3f11-87b1-db444d8861ba | -4.43041 | -55.09632 | 2026-09-08 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18384713-9411-38e8-9809-3e278b1723f3 | -5.1874 | -59.76451 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 197f36b3-c01d-34f6-893b-7abe57270862 | -7.78012 | -49.60718 | 2026-09-08 05:04:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72fcefc7-490f-3f4f-9bd8-88ade333cdb9 | -3.70452 | -58.94043 | 2026-09-08 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2da8aa88-9627-3e8c-9726-52505a5a9691 | -6.67753 | -59.92986 | 2026-09-08 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73094917-4120-37f0-9861-b3943c532e95 | -9.76229 | -43.46995 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8263925d-4d5a-3bcb-9943-2274031d772d | -6.76443 | -59.43118 | 2026-09-08 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8c62dce9-26df-370b-8e88-3c7f4af0f043 | -9.70683 | -43.45387 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d46ade3a-fc38-3a91-b721-641496eb058f | -3.36683 | -50.39792 | 2026-09-08 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 554f8820-f323-3c35-8466-ab7d09794893 | -6.61691 | -44.71949 | 2026-09-08 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6cad95ed-88b3-331f-b25e-339e12c5b5df | -3.14721 | -60.64959 | 2026-09-08 05:04:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb526ab6-55de-32f2-b6a7-f5015f1a4359 | -4.11159 | -49.06267 | 2026-09-08 05:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6252d877-8ff1-392d-8537-7ead6aa336b8 | -5.55022 | -60.24621 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84136623-f617-3910-b70d-0448b4d1ab32 | -7.31706 | -49.61946 | 2026-09-08 05:04:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20f3890e-0c8c-38c7-8adf-d25f1cba9b43 | -4.42929 | -55.10342 | 2026-09-08 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69bc0d50-514c-331e-98f0-631f9affe8f0 | -4.36124 | -47.77903 | 2026-09-08 05:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bccc7ed6-c9eb-3311-b443-e3b215f3c9dc | -9.71199 | -43.46384 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5c57fa6e-f844-3814-95a2-e8b3357437f6 | -9.70566 | -43.43581 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 694f3679-a0c4-3fd8-a4dc-d086741dd25b | -2.56224 | -54.74833 | 2026-09-08 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8626b6f8-2744-3182-a35f-84641767b1ff | -4.04244 | -50.87109 | 2026-09-08 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fd777f7-cc83-3d9f-80fa-54e6d88d00a0 | -9.71189 | -43.41256 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| e1263a10-8fc1-356f-88db-4d4f32fa62b7 | -6.68167 | -59.93056 | 2026-09-08 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7371a986-0ade-34e2-8019-59d81126f089 | -3.06135 | -59.27892 | 2026-09-08 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22596344-39e3-31ad-8a4b-037aafafc2d2 | -5.36993 | -56.02223 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fb4b0bc6-cc46-328c-903a-168afab5bc98 | -2.89827 | -57.49166 | 2026-09-08 05:04:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9bc3af86-c231-379a-9497-e0cb9daa32dc | -9.76358 | -43.45973 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9d6dd3cf-1a6a-3abb-9daf-a9ed216f0d23 | -7.60867 | -47.28759 | 2026-09-08 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a863be96-707c-3280-aad3-49f2888f7299 | -9.71258 | -43.45899 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1b9286eb-384b-36d7-8060-e59c046260e1 | -6.69729 | -47.41833 | 2026-09-08 05:04:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ae5be181-665e-3180-bc19-fb0fbd1804fe | -5.80147 | -49.97943 | 2026-09-08 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42ca3932-8511-3e19-bb18-87dc37a3f6ad | -3.15104 | -60.65501 | 2026-09-08 05:04:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c3430414-4187-30d4-acee-57ae34d1e559 | -8.53019 | -63.85057 | 2026-09-08 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6ff4989-e1b4-3ede-b109-5d8eb067bd64 | -7.51582 | -45.24969 | 2026-09-08 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dbc789ce-127a-3e94-aa57-119dd4980933 | -5.15985 | -55.95453 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0aba30a9-957c-3073-b545-d5cda1eb95c7 | -5.32368 | -55.87519 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d88645b-4470-3529-9ff0-eca5a335ca71 | -4.98541 | -50.64366 | 2026-09-08 05:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52167fca-0ffe-34c5-a0d8-8b41b27868ce | -3.77764 | -58.84993 | 2026-09-08 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df4f5b21-91a5-3d4c-8aa1-96522d1cda64 | -3.81325 | -55.88931 | 2026-09-08 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1816e112-5339-36e9-88b9-b96bd47d119a | -4.98239 | -50.63884 | 2026-09-08 05:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fe67731-6453-31c7-93b4-2cd3475908d7 | -5.59218 | -45.37724 | 2026-09-08 05:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4763006-2fb7-3bdc-a9c8-f6ddaa748055 | -5.28458 | -60.11611 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51905fb6-cdd1-3d1f-b392-a04151923fef | -3.26811 | -50.02444 | 2026-09-08 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83c22da9-a52d-39e7-ac34-2a6f23ddc7c0 | -9.76294 | -43.46484 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 43916ac8-9ce8-31aa-90fb-19d173977ec4 | -9.74158 | -43.48242 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b6b851b-6b3d-3607-812b-a84c2fc40e07 | -5.37098 | -56.03757 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7dd9aca7-a3b5-3c56-9605-3a9b00182329 | -8.5296 | -63.85378 | 2026-09-08 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb6ac3aa-f438-3e4d-94e2-b0cab1e3371b | -4.34459 | -55.2248 | 2026-09-08 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53417f16-b05d-34b7-a9e7-45ca3b47751c | -7.06956 | -56.46554 | 2026-09-08 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8cef275f-6b0d-3f72-807f-2994ea15cd59 | -4.47959 | -48.19226 | 2026-09-08 05:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6c1ec24e-ccf3-34e2-8a62-2c9610cda71c | -9.72212 | -43.48506 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dec4fb93-3a0c-31e6-9dbd-f1ba149ac476 | -7.66659 | -46.05251 | 2026-09-08 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67d195cd-5bdf-38c5-af0f-db6f0b7bead3 | -9.71195 | -43.4366 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e5d9cd44-68d7-3ae4-b7c8-835bf19455d9 | -9.30102 | -44.35184 | 2026-09-08 05:04:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb538747-b9e7-3bfa-8606-305f95b86b00 | -3.03235 | -59.16828 | 2026-09-08 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c42e54e-505a-3a8f-9f1e-d6655489673f | -3.58769 | -58.68535 | 2026-09-08 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af30ec15-fb4f-381f-b7d8-b25a0af736b9 | -5.36875 | -56.02962 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3d3e4da-b021-3bf3-920c-7897905721a4 | -4.03823 | -50.87463 | 2026-09-08 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 709b42f8-307f-3448-9aa7-b89548b78852 | -4.4859 | -55.50446 | 2026-09-08 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95e950e4-1616-3a35-a3b8-983376e50c60 | -5.37157 | -56.03387 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c47da6de-cda0-3259-851f-7939a5822a90 | -5.36934 | -56.02592 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ab746537-05ff-3413-8ef8-57bdce48e7c7 | -4.10697 | -49.06633 | 2026-09-08 05:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4251b729-095d-3e19-b0af-c7dc97af8ff4 | -4.70363 | -49.1552 | 2026-09-08 05:04:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aee553ca-57a3-38ab-9fb6-9ed85334ecc4 | -4.34738 | -55.2289 | 2026-09-08 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 514ba02d-15c2-3d4e-a516-4c86a0b81286 | -6.50614 | -58.29033 | 2026-09-08 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e4791eab-8170-3262-a97c-15156450d81d | -9.72336 | -43.47507 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d77c820-6427-35f6-932f-3e66ba90190b | -9.74785 | -43.48329 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6485c072-2c52-318d-89d4-0a0f798c4c74 | -9.71586 | -43.40648 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 356cdf50-8c2d-3b76-b38d-233b4772bc41 | -7.06896 | -56.46925 | 2026-09-08 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 258cf7b6-335a-32d9-873f-2d7a2e853b7c | -7.67216 | -46.05027 | 2026-09-08 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12768ea5-44b7-3269-afca-bd6e2c536122 | -5.14161 | -55.95919 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f23e73c4-1283-3740-b100-cc75e1ece658 | -4.0454 | -50.87571 | 2026-09-08 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c6b1d50-7079-372e-a0e7-315777efac9b | -6.33241 | -43.35233 | 2026-09-08 05:04:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 28c787c3-b50d-320f-9d35-187fafef31c0 | -9.73843 | -43.50756 | 2026-09-08 05:04:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1c6154e7-7df1-3cb3-97bb-df30d2b7b800 | -7.3729 | -47.01862 | 2026-09-08 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c571345e-5984-3045-a8c7-f5bdd634ca37 | -6.33178 | -43.35695 | 2026-09-08 05:04:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f854b6f0-18aa-3fc0-b336-a4723fa17a06 | -3.38382 | -50.45667 | 2026-09-08 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6577efd5-3e18-386a-a284-ebaafdc66b29 | -3.89105 | -55.82132 | 2026-09-08 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 977a5146-a7db-38c3-b43d-01098a1a2607 | -4.4332 | -55.1004 | 2026-09-08 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae940a28-577e-3530-95fc-5e5c7a0cbe3b | -5.3106 | -56.1077 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50c6d1d3-df19-35fa-9c38-65e77de756c2 | -4.11211 | -49.0592 | 2026-09-08 05:04:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cecdd207-1b81-388b-b56f-de8986468923 | -4.929 | -55.82039 | 2026-09-08 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d085b5f-fc62-35ef-9477-7a32e1f69ebd | -5.54591 | -60.24549 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc30f259-089d-3b4b-a856-447a716ba9f2 | -5.44822 | -60.23545 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86033c30-a46a-3164-b9ff-459f1c35de75 | -5.47637 | -60.23775 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09502708-8d49-34bb-a3bf-6fade5785330 | -11.36454 | -45.74269 | 2026-09-08 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e003f03-88c5-39d9-859e-482a60bed05e | -4.03698 | -50.88279 | 2026-09-08 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18ff3a53-e9e9-3cb5-b8bd-cebc4530b63a | -3.03298 | -59.1645 | 2026-09-08 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 591e8295-8512-3c65-b453-6366b8de0070 | -4.3656 | -47.77968 | 2026-09-08 05:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 68742f49-6e4c-33ee-8729-0ffc38d05cc2 | -5.54659 | -60.24137 | 2026-09-08 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18df62f9-0a29-3d3f-9430-d5149363aa46 | -7.60796 | -47.29266 | 2026-09-08 05:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e926fd5-2447-36ee-9c26-cab0b2512c70 | -5.82674 | -53.8099 | 2026-09-08 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cdf7bb2-0e32-37c1-a4d5-f171b665f08f | -4.50788 | -55.71314 | 2026-09-08 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da23abae-6edc-3ebb-b729-8f9857260ca1 | -3.45157 | -59.51563 | 2026-09-08 05:04:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a16263b-cdfc-3e39-842a-9476b9a1d496 | -7.59108 | -50.39357 | 2026-09-08 05:04:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README22.md)
