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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 317f485e-7a2c-3a88-81d0-35bb5bb50235 | -13.81252 | -53.78658 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b41667d6-15ae-3e25-8b99-b96977aa71a3 | -13.23453 | -54.17956 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b20ff1ed-a958-3bde-8da5-e6fcef14c2fc | -15.52559 | -52.99744 | 2026-08-15 04:17:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44baa0d2-0be9-3564-93a6-f600049ac11c | -14.46045 | -45.67191 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f2c4e1f-83dd-3784-8b98-1675663fd742 | -13.24038 | -54.18067 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 38dcc7cd-f201-33dd-92e6-38be9dd03f79 | -14.08818 | -53.71289 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d2cc5db-172a-3168-9243-b9d93b52ebea | -14.09028 | -54.52417 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 178d24c0-b2bf-3787-9059-bf9a151e0c32 | -14.44819 | -45.68599 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b9a65ca-cfd7-3382-ac0d-d0e35f196976 | -19.25134 | -44.37363 | 2026-08-15 04:17:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1da09178-1666-3694-9a2c-85878cc7ca60 | -14.45701 | -45.67131 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc4e0ee7-5fbf-35cd-9fce-53d80744d1c0 | -23.50418 | -51.72848 | 2026-08-15 04:17:00 | NOAA-20 | MARIALVA | PARANÁ | Brasil | 4114807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c194c63b-da04-394d-89f2-b843e51a04f6 | -18.54806 | -48.19704 | 2026-08-15 04:17:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 025c5329-83ac-3e8f-a9f8-a0b8acf356fa | -13.24941 | -54.19596 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e58373dc-154f-3cd3-a129-93c9e90c8b8b | -16.83542 | -42.25879 | 2026-08-15 04:17:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6d1c15ad-d18b-39b7-95b6-df35d5ebe7a0 | -14.09962 | -53.62855 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 237b4da0-5dd3-34f9-ade4-42baf718a559 | -19.25191 | -44.36999 | 2026-08-15 04:17:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2819f70-ee2f-37a7-a678-61fbf63fa33e | -14.92262 | -46.64384 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6aac93ab-7925-3efb-85c7-e239e146b9eb | -14.92337 | -46.63936 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 131d84bb-2e64-39cd-9b79-e8a371c9890f | -14.25981 | -52.03313 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d37f9c07-ac6d-30bb-a4b7-01f9dc1c5b07 | -14.72293 | -52.88436 | 2026-08-15 04:17:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc2003fd-f2b7-3070-b672-4451484684e9 | -15.2158 | -52.72402 | 2026-08-15 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31a68a37-0a5d-3703-952c-38cb0ed02d8e | -14.42794 | -51.91454 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 45fe8d00-149e-331a-a4d6-b79fc4a6a2a1 | -14.4268 | -51.92034 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 09fe92af-d4f8-3e62-9568-e08387dbed27 | -16.90279 | -54.16102 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a5fa8d0-2ff5-3eeb-8b2a-c21e9b9896ca | -14.30786 | -53.06861 | 2026-08-15 04:17:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6334408d-e509-373d-97c5-0a60e38057f4 | -15.65034 | -48.2062 | 2026-08-15 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2045bafa-e8d2-36c6-8caa-93f1ee7d8d60 | -13.82913 | -53.77641 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ae729f6-9c67-3446-839c-fd370348a6fe | -14.43347 | -51.85392 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c8aca74-fb57-3fc1-8066-728ce15f3a71 | -16.19588 | -45.26584 | 2026-08-15 04:17:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db6c419b-d309-3faf-b4ac-f976024a835b | -13.26195 | -54.19414 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5c07e89-856e-35ad-8f92-5d63e920be22 | -14.43129 | -51.91934 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| ef78d018-d016-310b-abbc-ef7f169a96b3 | -16.87249 | -54.14249 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e44bdcc-6a7b-3de4-a35d-be5fb13169fa | -15.03576 | -47.03815 | 2026-08-15 04:17:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdcccdd3-91cb-3692-9c0d-82375e18cd98 | -14.42525 | -51.92412 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 93cf4230-c66a-3672-a50e-de61b31253b3 | -16.89265 | -54.15506 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d13d2fe-884b-3a10-b0e2-c5fbec0258db | -14.6007 | -46.73536 | 2026-08-15 04:17:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 929cb98e-852d-38ad-b86f-75a872d7867c | -21.06173 | -48.3931 | 2026-08-15 04:17:00 | NOAA-20 | TAQUARAL | SÃO PAULO | Brasil | 3553658 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 192d9ece-0193-3815-9214-1149b13431c0 | -14.49167 | -52.03707 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efcc4f1e-a142-3dbc-af67-23188fb82c91 | -13.23629 | -54.17095 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f74b7c6-fa04-3379-a2ac-8ccc62430c81 | -14.44008 | -51.90506 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 308d3472-3d77-354c-83c6-a05f23261412 | -14.94682 | -46.63068 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43bda89e-f639-34a1-b5b6-3a2679e6c730 | -16.10928 | -49.8644 | 2026-08-15 04:17:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5f47f46c-651e-3ecb-b7b8-032f0fa4b350 | -14.44121 | -51.89933 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 712819e6-5e74-3914-87ce-94da118f64d0 | -19.52233 | -44.09253 | 2026-08-15 04:17:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04a5c17d-65b8-332c-9671-25e8173127f4 | -14.45418 | -45.67118 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e715af2-90ab-30db-9594-bf208c4af01b | -14.45571 | -45.67901 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a40590ec-6840-3b6e-9228-4e0314f1bc45 | -16.89628 | -54.13999 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 36b8843a-65f4-391e-8d3f-10a9061f512b | -14.60787 | -46.73666 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5792f5b-ae81-311e-8297-1cb064376adb | -16.89004 | -54.14257 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9af47357-33d9-32ad-85f8-bceda1fae2e1 | -15.51146 | -52.98712 | 2026-08-15 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dcebc2be-c508-3506-8b20-c95e44a91035 | -14.74715 | -48.24198 | 2026-08-15 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 07e0e44d-2dff-3861-aac5-f3b3c0c8f224 | -14.30526 | -53.06783 | 2026-08-15 04:17:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8f7ea497-e902-3916-afcb-a59275de91b8 | -15.07046 | -46.58244 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c57f0cb9-204b-3a1f-9ecd-82d1dcf45591 | -14.49665 | -52.03809 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 550600fe-f283-3616-9140-f042e7921119 | -14.44004 | -45.69248 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 295373e6-1233-33cd-bcce-54ba430a201a | -14.08996 | -53.62599 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 825940d5-2b92-3394-8ff1-1a542c537627 | -15.92186 | -43.52313 | 2026-08-15 04:17:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| becf7fc5-9e5e-38d0-ab5b-b7a76f1bd729 | -20.55586 | -49.31031 | 2026-08-15 04:17:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8449ae65-9970-36d2-9b4e-5aeae1f4b90b | -14.75416 | -48.24765 | 2026-08-15 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a2a5d554-1fe8-3900-8ca2-ca76268cc8a0 | -18.16373 | -47.99058 | 2026-08-15 04:17:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7c11b9d6-dc5b-3149-8e63-d13525e1c30f | -13.25527 | -54.19707 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e8e26238-e1f1-3312-b7ed-7b982b6cf00c | -17.67004 | -42.57215 | 2026-08-15 04:17:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4c8c5e37-27ce-366c-ac9e-5197f8530988 | -18.58117 | -41.28118 | 2026-08-15 04:17:00 | NOAA-20 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4f9a579f-3492-3212-9969-9418281ce3ea | -16.90126 | -54.17012 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d16106a4-bd9f-3065-a732-2f05726f69c9 | -14.4928 | -52.03117 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e91f837b-ebd3-376a-b65d-faf44025306c | -14.44768 | -51.91865 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1144c91c-446e-38a0-a125-04ebc5176a0c | -15.52292 | -53.01052 | 2026-08-15 04:17:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e685a77-49a0-3c34-8eec-a06d9f8ddf88 | -14.45697 | -45.67564 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db7b5b74-3b12-3b78-a3b7-da6fc4c240eb | -14.07789 | -53.67805 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e659ddb-3faa-3e91-ac16-5559eef4a42a | -14.46323 | -45.67636 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6bc78b4d-8b5b-38b4-a67d-28c6eb962e39 | -14.43288 | -51.91557 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 6f5ee1e0-0f73-3c8a-82ed-f59d7d7f7ede | -14.95043 | -46.62576 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d8539a4-f377-34b5-95c3-e51a58cbce82 | -18.85423 | -47.06672 | 2026-08-15 04:17:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1af3a48d-45a0-3ba9-9c43-02088efa0baf | -15.16188 | -52.83357 | 2026-08-15 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 667151df-905e-33ce-ade1-9e8699c2e9ab | -14.42635 | -51.91831 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e0a9cc2a-ee26-3417-91b5-9046e4bb4060 | -14.42855 | -51.85291 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 63a54545-41c8-3a0a-971c-4b900e9db557 | -14.74626 | -48.24703 | 2026-08-15 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee87221d-6e85-311a-b73a-7477f59bc2ac | -15.03928 | -52.22536 | 2026-08-15 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c17b475-4cbc-3b97-9ca2-91d3869ca145 | -16.87333 | -54.1384 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a66efee5-ae29-37d9-9d7a-7e1386e2a815 | -16.71578 | -46.40263 | 2026-08-15 04:17:00 | NOAA-20 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4de825ea-083e-3ec4-bf73-eff0c0418365 | -18.95328 | -48.30641 | 2026-08-15 04:17:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e04762eb-837d-3f62-9e55-828bae5aecb5 | -15.65054 | -48.21441 | 2026-08-15 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1cd92775-4677-3966-bdb3-ecb818248fa6 | -14.60355 | -46.74023 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 576285e9-e323-3d27-ab43-92f79c8170c8 | -14.92624 | -46.62243 | 2026-08-15 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 78bceea6-00b4-300c-90fd-2ab8dbee9e38 | -15.03903 | -52.68998 | 2026-08-15 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e28b4aa2-0c98-3f97-83f2-f1ce67412abc | -16.89346 | -54.1511 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 65bade26-76f5-33f2-839e-e41117efb768 | -14.07412 | -53.6768 | 2026-08-15 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8fb85d8f-e3f7-3a8f-b544-e47e0ef6f9a5 | -14.43211 | -51.94553 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5987ca8-9ee3-3acb-924f-94cff40ad48e | -14.26038 | -52.03017 | 2026-08-15 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb4705c3-d93b-3367-9a36-f2a0ab1172b4 | -14.44348 | -45.69309 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 024181a8-0f6a-38fb-9e7b-3c8078ffe913 | -20.80417 | -44.73458 | 2026-08-15 04:17:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9b7c63eb-86f8-385a-b5a5-3d8b2cf2ddf2 | -14.4598 | -45.67576 | 2026-08-15 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2cd4c77c-c738-392a-812e-6f4f36cef1e9 | -16.89426 | -54.14719 | 2026-08-15 04:17:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8726fe0b-6fec-350a-b8f6-9bbd9102cbba | -21.46068 | -48.67094 | 2026-08-15 04:19:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddbc2b44-c106-399f-9145-14280f352754 | -21.46635 | -48.61412 | 2026-08-15 04:19:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06c25127-fba6-327b-a22a-dd4708d849e5 | -22.67966 | -47.55011 | 2026-08-15 04:19:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 4b9c9ca1-5fe6-3dd9-8c27-763dc8873e51 | -22.34181 | -48.48991 | 2026-08-15 04:19:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 03207148-9787-337d-80e0-a4649e765703 | -23.008 | -45.50941 | 2026-08-15 04:19:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cc979dd3-33bc-3643-8e35-37fbf6de1a46 | -22.99701 | -52.42704 | 2026-08-15 04:19:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bcced7af-40e9-3600-883d-abf521e1f52c | -21.46996 | -48.61483 | 2026-08-15 04:19:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README21.md)
