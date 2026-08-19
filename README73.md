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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8e17f07-b102-3d96-bacb-d9fc40f367f5 | -9.42064 | -60.42711 | 2026-08-19 07:26:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 5eb842a7-41f2-3eec-9d9e-54235563a44b | -9.39844 | -60.57047 | 2026-08-19 07:26:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5eec846e-ef23-347b-b50d-e5146aa12db4 | -19.75981 | -57.93533 | 2026-08-19 07:29:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| b7d4b373-46b2-31fd-9b88-1ed9db7da065 | -19.76139 | -57.92357 | 2026-08-19 07:29:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| ec2c2880-bb21-36a9-ba66-e728cc945a9b | -19.74997 | -57.93391 | 2026-08-19 07:29:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.9 |
| 7887f488-f58a-3064-801e-8c892effa4bc | -19.75155 | -57.92215 | 2026-08-19 07:29:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.3 |
| a2ebd046-57e4-310b-8368-4d3c4041cfa2 | -19.75664 | -57.95877 | 2026-08-19 07:29:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 5448c45d-c0f6-373d-b8d4-95f8994e3df8 | -8.5785 | -54.7566 | 2026-08-19 07:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 27f29be9-7793-3824-b649-2ee31a03de08 | -8.5598 | -54.7579 | 2026-08-19 07:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 55175d5c-7c10-3209-81f6-dc3967574232 | -6.0912 | -57.9187 | 2026-08-19 07:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 6b5c3026-9faf-3bd1-a72c-267b769056fa | -9.4256 | -60.4353 | 2026-08-19 07:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 40ea9ba7-ee59-3c2d-85a6-5f6e5c4ff350 | -19.7643 | -57.9399 | 2026-08-19 07:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.7 |
| 53c7dbf9-0079-32a6-bb1e-4c6864db895e | -5.9198 | -43.6264 | 2026-08-19 07:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 62469fd6-5153-3835-b1c3-85cc1c4f2bd1 | -14.8033 | -46.6453 | 2026-08-19 07:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 9e108fff-0ae7-32ce-8b86-52640bbf8165 | -14.8033 | -46.6453 | 2026-08-19 07:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 9dfc6669-9bf3-35ed-ab92-f5f40ed8142e | -8.5785 | -54.7566 | 2026-08-19 07:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| b85a0120-b9e1-3a1e-8589-1a662584efc1 | -8.5598 | -54.7579 | 2026-08-19 07:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 7e206bd8-ffaf-3a27-af72-a7306791be44 | -9.4256 | -60.4353 | 2026-08-19 07:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 897bf948-8971-3d37-a8b2-cb2218fc7fa5 | -14.8028 | -46.6683 | 2026-08-19 07:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| e88c350e-bba5-3987-8a1e-8929e280586d | -6.0912 | -57.9187 | 2026-08-19 07:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| dbdac983-05b1-3de8-b1d4-fe4b62775f09 | -6.0912 | -57.9187 | 2026-08-19 07:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 021d6f5e-abf0-3369-b12b-541f824031aa | -8.5785 | -54.7566 | 2026-08-19 07:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 323c618c-a398-3e58-8eed-d1bcd5cb8e13 | -14.8028 | -46.6683 | 2026-08-19 07:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| b17c7d66-c3ab-34fa-b341-6c7fc1b430c0 | -14.8033 | -46.6453 | 2026-08-19 07:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 97.4 |
| f0cb9648-01b6-32d9-901a-ede4346526db | -8.5598 | -54.7579 | 2026-08-19 07:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| fc7678bd-6b44-3be5-8ec9-3ce029dd9caf | -5.9198 | -43.6264 | 2026-08-19 08:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| e7810bba-7c62-3bb2-a6af-f6ff7a67322a | -6.0912 | -57.9187 | 2026-08-19 08:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| ab987a88-4988-379f-8355-ffd8342c9ac3 | -8.5598 | -54.7579 | 2026-08-19 08:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 3ad99b9f-0b0a-3336-b088-ae310189b5fd | -8.5785 | -54.7566 | 2026-08-19 08:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| ba971576-11fd-312b-b4cd-fad25b5b7344 | -14.8033 | -46.6453 | 2026-08-19 08:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 89.0 |
| f3d46d84-e574-3d67-97bd-e56781658ece | -8.5598 | -54.7579 | 2026-08-19 08:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 7a8492e4-a7ea-35e5-8ba2-69aba02248cc | -14.8033 | -46.6453 | 2026-08-19 08:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 180d6bce-f8f0-3b89-a680-6bb12bf3a8ce | -6.0912 | -57.9187 | 2026-08-19 08:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| d30970f5-0856-34ce-9dde-9c2e98461226 | -11.1178 | -47.2654 | 2026-08-19 08:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 82acf41e-338d-31c5-91ae-15b8ff0f2b32 | -8.5785 | -54.7566 | 2026-08-19 08:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 3a4bed29-0c3a-342b-952a-681bf6e66233 | -6.0912 | -57.9187 | 2026-08-19 08:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 19f8f82d-9aee-349c-940a-06784271b2bc | -14.8033 | -46.6453 | 2026-08-19 08:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 2144a048-9b1a-306e-b73f-333b45d451f1 | -8.5785 | -54.7566 | 2026-08-19 08:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 167a641d-0ef2-3e46-a400-70cdcdbe92bc | -8.5598 | -54.7579 | 2026-08-19 08:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| e08d2575-24b5-3e83-90ef-f106322cd074 | -14.8033 | -46.6453 | 2026-08-19 08:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 60f4a2e2-39a0-3f80-af00-bd21ee49e4f2 | -8.5785 | -54.7566 | 2026-08-19 08:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 2d74e655-cfe2-3801-95d3-c2fe5260602b | -6.0912 | -57.9187 | 2026-08-19 08:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 128.0 |
| a919be55-7ea1-3053-9d18-9dfd9a5c02d8 | -6.0913 | -57.8992 | 2026-08-19 08:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 6bb720f6-45a9-3cb7-8266-475cf222c2cc | -14.8033 | -46.6453 | 2026-08-19 08:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 023ab79a-c18e-39f9-b879-3dd65de63552 | -6.0912 | -57.9187 | 2026-08-19 08:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 129.3 |
| 2291b54a-5ee4-3635-9eec-3b24ed47a5b3 | -8.5785 | -54.7566 | 2026-08-19 08:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| f12a8c1a-2253-381c-bba0-9f5dce2a8f56 | -8.5598 | -54.7579 | 2026-08-19 08:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 65adafdf-7082-3bca-9e91-e1834f3fd263 | -6.0912 | -57.9187 | 2026-08-19 08:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |
| a9dd8a4c-e48c-3827-b067-8d90378308d4 | -6.0912 | -57.9187 | 2026-08-19 09:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 0cfcf675-0831-3576-b28f-89d5a1556799 | -6.0912 | -57.9187 | 2026-08-19 09:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 12b050a2-9aeb-3806-8f6d-af689267f9e5 | -6.0912 | -57.9187 | 2026-08-19 09:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 3f214c58-c56e-3b84-a3bf-d0e7d565c17f | -14.2017 | -52.9065 | 2026-08-19 10:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 4a069b78-07c1-3734-8da2-82f113b23048 | -14.2021 | -52.8854 | 2026-08-19 10:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 8375fda8-5c81-3c4d-b9ac-54160450ff75 | -14.8033 | -46.6453 | 2026-08-19 10:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 218.8 |
| 3b4b88ff-09f8-3860-b26e-e453dcd50aef | -14.7837 | -46.6487 | 2026-08-19 10:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 1de12de2-dddd-3551-9dbf-54640fc506f9 | -14.8033 | -46.6453 | 2026-08-19 10:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 274.6 |
| 9e7d18b8-2ad6-38d7-84fa-1d76a8f32d6c | -14.8033 | -46.6453 | 2026-08-19 10:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 6e76959b-f035-31fe-8dbb-b4ac184ae6e8 | -7.35651 | -38.93176 | 2026-08-19 10:56:00 | TERRA_M-M | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| aac42717-e121-354e-b5cd-dd8de2ad7a26 | -5.0976 | -37.78254 | 2026-08-19 10:56:00 | TERRA_M-M | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| e3c4d8d7-8525-384e-bbc1-25760b86bd49 | -13.00994 | -42.22525 | 2026-08-19 10:58:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 2848c017-42a4-326e-b735-4bc47fe48564 | -14.8033 | -46.6453 | 2026-08-19 11:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 80e42028-2162-3776-8cb5-76c5d5d2d936 | -21.95417 | -41.22792 | 2026-08-19 11:00:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 19.4 |
| 47b758b6-f59d-3621-89eb-cb8f7a6a5d62 | -6.6323 | -45.5148 | 2026-08-19 11:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 235da546-e2d1-3362-8023-a3481017d6c1 | -14.8033 | -46.6453 | 2026-08-19 11:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 158.3 |
| 35e5f191-77e5-3f0b-96bd-90d11882ffaa | -9.4366 | -48.2955 | 2026-08-19 11:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 33787e2e-ff8a-33f3-90a7-e4c7ff4a493d | -14.8033 | -46.6453 | 2026-08-19 12:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 8201469b-eaf0-3674-942a-d6edbab36f00 | -9.4366 | -48.2955 | 2026-08-19 12:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| a9086649-3e8b-368a-a8a6-125f03384f4a | -14.2017 | -52.9065 | 2026-08-19 12:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 62ab222b-02c5-3aea-8efe-740fdba4f3cc | -14.221 | -52.9041 | 2026-08-19 12:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 88.8 |
| ca208809-06c0-341c-a339-db4f6612c95a | -15.3838 | -52.7315 | 2026-08-19 12:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 5407bf37-373d-3b50-8da5-62c7d19b4f99 | -14.221 | -52.9041 | 2026-08-19 12:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 7b2b9248-e438-3883-adb1-f235f5b4fe9c | -14.2017 | -52.9065 | 2026-08-19 12:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 3f4d43cf-3172-3914-b388-83466a54be75 | -6.0912 | -57.9187 | 2026-08-19 12:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 668024e2-29e1-321c-894a-e45ee1dab8e1 | -9.1078 | -46.046 | 2026-08-19 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 7b12a437-a0df-3cc6-9ba9-40c60ba7adf3 | -9.1267 | -46.044 | 2026-08-19 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| feec4740-2f21-32df-9dd7-b50972d59483 | -11.404 | -47.2287 | 2026-08-19 12:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 1b3b5760-84cf-32d7-9615-532c8aa290b1 | -21.5343 | -52.0046 | 2026-08-19 12:30:00 | GOES-19 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 186.8 |
| 0e7e6697-16be-307e-84c8-d7a602efae4f | -6.0912 | -57.9187 | 2026-08-19 12:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 464cf2a3-a555-3a05-93b0-fc2663464d0a | -9.127 | -46.0214 | 2026-08-19 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 76646f05-ff46-316a-bf73-6285b257fbab | -9.1078 | -46.046 | 2026-08-19 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| f9d83496-159a-35e1-b202-0fdd8c4ac6b6 | -11.4036 | -47.2511 | 2026-08-19 12:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 5b0d5a4c-d5b3-3890-9320-29cbf2b32bdc | -14.221 | -52.9041 | 2026-08-19 12:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 958986ab-8962-3932-b895-6bc8e1e96651 | -5.00419 | -49.46876 | 2026-08-19 12:32:00 | TERRA_M-T | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| ff7acb39-2fea-3be3-9854-7b7c33a12d89 | -3.1052 | -61.19843 | 2026-08-19 12:32:00 | TERRA_M-T | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cba26dc2-5272-3565-8a72-7f2e4e5e033d | -3.45847 | -56.80228 | 2026-08-19 12:32:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 51984367-3588-3091-97df-341fbd1dcbab | -3.45716 | -56.81149 | 2026-08-19 12:32:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 73fe897c-77fb-38ca-ad6d-b67905b142c5 | -6.7055 | -58.93831 | 2026-08-19 12:34:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.9 |
| ab489725-eb75-331c-bde5-a83094538417 | -7.53822 | -55.5821 | 2026-08-19 12:34:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3dc23257-6956-33b8-bf33-969d6d60c084 | -6.88451 | -59.03904 | 2026-08-19 12:34:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 254fa7f0-763e-3105-9056-b8d0609b4057 | -6.14799 | -57.86285 | 2026-08-19 12:34:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a29ff3a3-24d4-3f53-a3d0-947dbe1f3b5a | -6.62963 | -59.07495 | 2026-08-19 12:34:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9454da79-c737-3d3c-a322-e1373130186c | -6.39944 | -51.7354 | 2026-08-19 12:34:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| bc7f04d6-4841-399f-bb1e-f26ec093553a | -6.34187 | -54.90687 | 2026-08-19 12:34:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 984f15df-82c0-30cc-aef3-8d3a7f85e3fa | -4.46848 | -55.45524 | 2026-08-19 12:34:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ac0b2d0c-357e-3958-8e5e-1cf1092e1698 | -8.90059 | -60.59215 | 2026-08-19 12:34:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 90d83375-e0aa-32ae-98dc-229667defa50 | -6.0101 | -57.86515 | 2026-08-19 12:34:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c459cd02-6e82-3615-a77d-5eb60a3dab50 | -6.35225 | -54.9083 | 2026-08-19 12:34:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 69c8896b-f41f-3f24-8989-f8e7b9741a3c | -10.11916 | -52.11633 | 2026-08-19 12:34:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 25.3 |
| e467816a-0c0b-3be9-920e-fdb23a84aab5 | -5.4354 | -48.40441 | 2026-08-19 12:34:00 | TERRA_M-T | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 210ec80e-0d55-3905-a0e2-bc3b8c2ea822 | -10.02049 | -59.34972 | 2026-08-19 12:34:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |


[Clique aqui para ver as próximas entradas](README74.md)
