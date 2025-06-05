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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1133f2cb-fda8-37da-97cb-325dbc3e3905 | -7.90763 | -50.36141 | 2025-06-05 04:34:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 51f2167d-49eb-3213-8a3b-3d1f65b37336 | -10.55405 | -42.43673 | 2025-06-05 04:34:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 99111d9d-a39f-3dcb-820f-feccd1abfabd | -8.95309 | -47.284 | 2025-06-05 04:34:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 074d59e6-c530-3d5b-9d60-d087b7451b60 | -13.51055 | -56.56489 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b98e7b93-4a1b-3c99-a669-ca9ef7d4abbb | -13.51558 | -56.54552 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2efe36a8-481c-3d1e-9441-d6776766f4cf | -9.22667 | -48.85281 | 2025-06-05 04:34:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4afb418-6fea-30b5-bcea-23f57cf8275f | -10.84117 | -46.88821 | 2025-06-05 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72657f26-71fe-3674-81cb-8b2fc4e36abd | -11.06924 | -55.04453 | 2025-06-05 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 235ea409-115e-30d1-a55f-d75902f2da4f | -8.079 | -46.99549 | 2025-06-05 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ffc8a473-6495-361f-a95e-718295d873dd | -8.94864 | -47.29063 | 2025-06-05 04:34:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac062b2e-a30c-3967-ac45-69566eced103 | -14.236 | -45.4815 | 2025-06-05 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bea83515-2e28-37a0-9349-ce39673b8022 | -13.51705 | -56.58065 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f651f8df-bd47-3a58-bf20-8b75ff4e4a64 | -13.21746 | -49.0268 | 2025-06-05 04:34:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13728261-4b98-3602-8b14-37f3ac056832 | -10.84172 | -46.88449 | 2025-06-05 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36fdf033-3979-3c2e-a8c8-ac8d87c3b459 | -13.53279 | -56.55345 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9462679b-229b-3f17-8574-1c89d08f34c8 | -11.13829 | -53.94386 | 2025-06-05 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a29721fe-48db-3baf-8bfa-6de2b71d88f0 | -9.38474 | -48.4085 | 2025-06-05 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79eab57d-9e94-38f8-b1dc-e8d5b3c56177 | -13.5166 | -56.56483 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 842092c3-5c91-36b5-b491-a34aae96ed5e | -13.51482 | -56.57418 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bf7a1efb-4d15-3dbe-a835-2af2a69f3b3f | -11.63397 | -55.37682 | 2025-06-05 04:34:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4acf2cd9-3a65-328a-b013-2020263f6cde | -13.50517 | -56.56874 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89abe87e-2512-3ff6-bd64-01e6327bc156 | -13.52046 | -56.56184 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| cea50c8c-0f51-314f-941d-85c9fcc43670 | -9.22557 | -48.85976 | 2025-06-05 04:34:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5bc60cdc-53d9-3aa5-bacb-051c840b749d | -13.51121 | -56.59322 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aef762d5-793b-30f6-ad9b-107ca0c4d777 | -7.90702 | -50.36518 | 2025-06-05 04:34:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| fa7b19e4-b6d8-3c75-b260-8be9c100a83b | -12.45953 | -48.98059 | 2025-06-05 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a49b2e13-0f7e-3eb2-a368-92f08bbf5454 | -12.66434 | -58.21601 | 2025-06-05 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4462032f-ebc2-3621-80e7-d5c4b4f5bbd6 | -12.66572 | -58.22477 | 2025-06-05 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7a1dfbf3-5984-3293-bdae-47c6f4b61f4f | -7.9048 | -50.35709 | 2025-06-05 04:34:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f775c2a0-664b-3b00-8edb-d9d0d89df068 | -13.51755 | -56.58452 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eee43894-6e7f-3c3e-8fc3-6e07fbd589bc | -13.52867 | -56.56814 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 519c0890-32e9-3240-a4ae-145d489fa089 | -11.56273 | -47.61882 | 2025-06-05 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 579d5981-ccc2-39b5-b969-a445cede983d | -13.52375 | -56.55176 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3865363-b11a-38cd-b1a5-d1b439cbb71f | -13.52157 | -56.58154 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70dd52a4-4dfc-325b-be9e-64e5b56d3222 | -13.51678 | -56.55637 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 838e9079-975e-38d1-bb9b-133527e66994 | -12.2899 | -43.55083 | 2025-06-05 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 213ea215-dccf-346e-80ee-500281d97c0c | -10.05516 | -49.66175 | 2025-06-05 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ab6fd0b-f464-3dde-b8dc-ed8771810355 | -12.65286 | -54.12043 | 2025-06-05 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60972c21-7f23-3959-b3d6-8ad37d5aa0e4 | -10.6734 | -44.38002 | 2025-06-05 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 59b2ae68-3a25-3a38-bfb7-59fd798515fc | -14.16181 | -45.48842 | 2025-06-05 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c36d2e25-25a2-3aca-849c-e681b3bac77d | -9.51949 | -47.228 | 2025-06-05 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab56edc3-beb5-3ff4-91ed-9ec4c9e1f9cf | -13.08525 | -49.24351 | 2025-06-05 04:34:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d345b59e-63a5-3f1d-91a1-295a98491e1f | -13.51618 | -56.58544 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e2930d5-8ef6-36f2-a8d0-254df200a907 | -10.63213 | -49.43761 | 2025-06-05 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c380452e-4f02-3525-8615-b83654b09461 | -14.58111 | -46.75224 | 2025-06-05 04:34:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1aa0c84b-99a8-31e1-bdac-76c91c1c758a | -11.14286 | -53.94103 | 2025-06-05 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a1c5dfc-a997-3ffd-8279-571719bc2a28 | -13.52298 | -56.54793 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9d3ed56-36f2-3555-aa58-2f9c007d3058 | -10.29812 | -57.13979 | 2025-06-05 04:34:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad1c6b0f-c311-3046-9902-119b3fd9bb87 | -11.62309 | -55.3879 | 2025-06-05 04:34:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b46c66e-6eb4-3f74-9b1c-2d4e04532e4b | -10.53965 | -56.38938 | 2025-06-05 04:34:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 716404e9-fc09-30c7-91ed-6a0176bda9a1 | -14.15486 | -45.48249 | 2025-06-05 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 113c0242-6720-3a83-a9e6-2cbcaa58a3cc | -10.28374 | -49.65869 | 2025-06-05 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59979c4c-4d0e-3379-bb4c-9c4fcb8bbbd9 | -13.51443 | -56.59508 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1214d9b4-2acf-3f7c-ba4d-782815af3950 | -10.05849 | -49.66229 | 2025-06-05 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e5f5419-9d56-3c10-9d69-d19b08555f01 | -8.72877 | -47.98761 | 2025-06-05 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f60c71d2-9301-38d7-b79c-10f64ef66d3d | -8.87805 | -50.18547 | 2025-06-05 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5637580e-e0f5-3d46-9e16-863acf79f399 | -14.23154 | -45.48574 | 2025-06-05 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 88acf70c-9f58-3217-87e6-685799246925 | -11.54697 | -56.44229 | 2025-06-05 04:34:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 16bd9bb2-88d2-35d9-8162-c5d921d87215 | -11.56605 | -51.46926 | 2025-06-05 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c26a191c-c94e-3560-94b6-cb45c9268502 | -13.72055 | -58.67508 | 2025-06-05 04:34:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cebbb690-4730-324b-8312-dfc435a56b32 | -13.52113 | -56.56562 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 53a4b2a5-4884-3f17-9fd6-15f97d115431 | -10.5753 | -48.09953 | 2025-06-05 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b36dca12-63c8-309c-8b89-f209067a96a7 | -8.45924 | -46.47922 | 2025-06-05 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 14d7a96f-9d38-307c-8720-91b37cd4ae7a | -8.72169 | -48.01141 | 2025-06-05 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1066dee8-9430-3d30-a8ad-01008559efb4 | -10.68461 | -57.59504 | 2025-06-05 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7b980fa1-4ea3-3232-a25e-04dd9251f41e | -10.49684 | -53.66038 | 2025-06-05 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6bbe2f6d-19f1-39cb-a462-b9143ca6787c | -12.65922 | -58.215 | 2025-06-05 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 198a3518-7d2d-3825-a6bc-b6da8360a1a1 | -9.10865 | -48.65217 | 2025-06-05 04:34:00 | NOAA-21 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c35f8741-b8f3-3e3e-828d-df6e58ba44d5 | -13.51571 | -56.5695 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5c261681-e5ee-3619-a7db-e80d239dfad1 | -13.52569 | -56.59107 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99885c23-8f2d-3182-bdc7-854de2f7ef4d | -13.53112 | -56.58714 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4d00231-50d6-320c-a858-54ff32f874b1 | -10.82122 | -56.95951 | 2025-06-05 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 0049f8eb-0128-3214-bb78-87ab08b9345e | -10.65419 | -49.42678 | 2025-06-05 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8539e2a5-e6ba-3631-9d93-39e136fbe4da | -12.36545 | -54.17052 | 2025-06-05 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5a5f7f5-12ce-3f7c-b28f-6b0053d40735 | -9.51894 | -47.2316 | 2025-06-05 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57f5a326-908f-3543-9bb0-45afeff7c72e | -13.52415 | -56.56731 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| eaecfb39-3498-3ae9-b5e8-7d6dbbb1da8b | -12.66236 | -58.21434 | 2025-06-05 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 86d2412f-e752-3b50-89c5-7535220e9f16 | -13.0847 | -49.24703 | 2025-06-05 04:34:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a04c053-7d7c-30b6-89bf-231033b46fa0 | -13.52653 | -56.56182 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 158ee94a-a934-3ad5-b5db-81eaee2e8911 | -14.29351 | -47.98788 | 2025-06-05 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10ef5714-21ba-3d96-862e-66067e1296f5 | -10.65528 | -49.44132 | 2025-06-05 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dd81f8cf-ad8d-3c00-bb7e-f739b85997d4 | -13.50687 | -56.5594 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5c37a462-8d78-3749-bc86-d4e0b52ea48b | -13.50432 | -56.57337 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f685b078-4ed1-37fa-97f1-73746d164f36 | -12.41177 | -49.67823 | 2025-06-05 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfd523a0-c0f9-353f-9a59-cfbb1dbdb4fa | -13.52499 | -56.56267 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c6adc8e7-2391-3a63-98c8-a14e72b2e1f2 | -13.52915 | -56.54792 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba09419a-c819-3d5f-a12c-3a06e949cee2 | -13.5097 | -56.56956 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97b03ef1-59b8-3f9f-9e44-674c6c278720 | -13.51846 | -56.57974 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fbb99819-36ae-3f8f-8515-9bdd1993d5ae | -13.7233 | -43.86791 | 2025-06-05 04:34:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6f37c2c-1aa7-3468-9bb1-c7b4ce47d62a | -10.93983 | -55.33092 | 2025-06-05 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3efb05c-7398-3a72-a6d4-de224fbc37ff | -13.50773 | -56.55471 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d17a1c29-370d-3faf-a5dd-c076e9f12fe9 | -12.64894 | -54.1197 | 2025-06-05 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d529e3b-dd3d-3aca-b64c-48384327947d | -11.55054 | -56.42259 | 2025-06-05 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbb5f486-8f2a-3ab4-81e9-2a8790a8a0cd | -12.15582 | -46.59485 | 2025-06-05 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| addc0584-38cc-3000-9e0f-2aa0ad7b84da | -13.52244 | -56.57676 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 7d72e999-8131-39d7-9099-817fe851ec80 | -13.5274 | -56.55721 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7054614a-796d-3205-9155-a1937e29386b | -13.51962 | -56.56649 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 73d22707-a9b7-33d0-8307-a4dc25897058 | -11.07046 | -55.04455 | 2025-06-05 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a11192f-0c1e-3fbf-93ea-3247c975a451 | -8.96268 | -47.97061 | 2025-06-05 04:34:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e9055774-38cd-3af8-afaa-291c36a636c6 | -12.15231 | -46.59432 | 2025-06-05 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README11.md)
