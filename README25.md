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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 742b676a-e1ef-35cf-af29-c7f5e2be6f47 | -5.8216 | -44.1196 | 2024-10-06 01:35:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 19334e0a-17ad-3a8a-951d-91d8a83acf5a | -6.9514 | -59.0666 | 2024-10-06 01:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 7a39943a-a8dd-36b2-bca9-1d84523bb603 | -6.9515 | -59.0473 | 2024-10-06 01:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 9b4f0692-f361-33d5-8b25-09dde66df4d1 | -6.9699 | -59.0658 | 2024-10-06 01:35:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 7e151c65-b413-39c6-bdb9-ef77e83e6527 | -8.2139 | -61.2022 | 2024-10-06 01:35:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 388fff33-7fc4-3339-9ce9-dba2197112d5 | -9.1263 | -60.6621 | 2024-10-06 01:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| ce064003-e2f0-3c9b-bbd6-1facd0f589f8 | -9.1449 | -60.6612 | 2024-10-06 01:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 9f5c45b6-e348-3ef9-a5bd-edcd6e0ea7ef | -9.1635 | -60.6603 | 2024-10-06 01:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| e87c12ff-e57c-3327-8489-9dad0b326b97 | -9.1759 | -61.5794 | 2024-10-06 01:35:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 41.6 |
| c67110ae-9dd3-3fe4-88d4-57baf48ed598 | -9.3275 | -46.5609 | 2024-10-06 01:35:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 28ae4c0a-81a9-3557-9838-37f82a13b49d | -9.3278 | -46.5385 | 2024-10-06 01:35:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 13c0c936-2124-33e8-ba82-6576c7846a51 | -9.3464 | -46.5589 | 2024-10-06 01:35:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 1c9a80f3-4b70-30f8-afe6-f2d89ebbb893 | -9.3467 | -46.5365 | 2024-10-06 01:35:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 230.9 |
| 8073045c-f18e-3598-a13e-3819dc5da0a9 | -9.3647 | -51.0898 | 2024-10-06 01:35:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 42bbe685-cb81-3e1e-9407-783137f70505 | -9.365 | -51.0687 | 2024-10-06 01:35:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 39db30dd-692f-31fe-9f9b-1ed8cd22c1b9 | -9.3835 | -51.0881 | 2024-10-06 01:35:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| d7039d59-b17d-316d-b052-bd64427c36d6 | -9.6779 | -64.6269 | 2024-10-06 01:36:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 5dcdd4cf-097a-3dc5-b6e2-31d983cf88e1 | -9.8552 | -60.2966 | 2024-10-06 01:36:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 63d056dd-8890-3b8d-ac92-dd8f25c816b1 | -11.0966 | -54.2336 | 2024-10-06 01:36:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 4c7094a2-a484-3563-b3ad-2dc979bb6ef3 | -11.1155 | -54.2319 | 2024-10-06 01:36:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| d0ed4355-e411-31ec-88bf-390fd3107f54 | -12.0211 | -63.7478 | 2024-10-06 01:36:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 18f89575-dcd6-37de-bf6c-41df6324ec37 | -12.6089 | -53.1338 | 2024-10-06 01:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 07208b6d-657e-373b-afce-84f977a289fc | -12.628 | -53.1317 | 2024-10-06 01:36:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 23fddbf3-c3a3-37de-88c9-b48028f53221 | -12.6283 | -53.1108 | 2024-10-06 01:36:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| bdb8347a-91d2-3da0-883e-f51ee265651b | -12.6474 | -53.1088 | 2024-10-06 01:36:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| aef17e7d-6ca3-3d2e-a744-1d802bf33493 | -12.6532 | -54.0415 | 2024-10-06 01:36:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 85e3f689-817d-339d-8114-8f38b94fbaa6 | -12.6535 | -54.0208 | 2024-10-06 01:36:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 63609172-832b-33db-a238-4484dca324a4 | -12.763 | -50.5352 | 2024-10-06 01:36:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 148.0 |
| cfa74254-2ab2-3630-bdcf-003964cfca0e | -13.6724 | -51.1911 | 2024-10-06 01:36:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 149.7 |
| c55d8d31-eacf-3b1c-b195-f7459de2b133 | -16.3959 | -57.3641 | 2024-10-06 01:36:38 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.3 |
| c049b5d5-6002-3b73-9f46-94fda3aef4c4 | -16.4151 | -57.3823 | 2024-10-06 01:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.2 |
| 04866faf-96d1-3072-83a6-4738f40593cb | -16.4155 | -57.3619 | 2024-10-06 01:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.4 |
| e462dc59-921c-30d2-a90d-436fb25a52a9 | -16.4158 | -57.3415 | 2024-10-06 01:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.9 |
| 9142dc51-1c45-33c1-ae86-764079e4f2a0 | -16.435 | -57.3597 | 2024-10-06 01:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.2 |
| 948caeb7-9071-3533-83f1-31968feedd79 | -16.4353 | -57.3393 | 2024-10-06 01:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.2 |
| e83d20d3-35a7-3179-a12c-b51a0da3da32 | -16.614 | -55.9214 | 2024-10-06 01:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 112.0 |
| 83acdee2-a19d-3a0e-8a44-458693c5b2bf | -16.6398 | -55.5452 | 2024-10-06 01:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 155.7 |
| bd12d0a7-394f-39ff-8e59-4fb9e75ffd5d | -16.6402 | -55.5243 | 2024-10-06 01:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 119.8 |
| d41df3a6-2744-36c0-8a84-8c4cbbe3a293 | -16.6594 | -55.5427 | 2024-10-06 01:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 102.2 |
| 85660992-4537-3f37-a959-066e86be2fa2 | -16.679 | -55.5402 | 2024-10-06 01:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 90.2 |
| 693cf4fa-4201-3de2-a0ba-12459104969d | -16.6983 | -55.5585 | 2024-10-06 01:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 128.2 |
| 8ac31abb-0309-34f1-b0df-6bc6ef369f19 | -16.6986 | -55.5377 | 2024-10-06 01:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 158.2 |
| cf864b86-089a-35ab-bf84-d433e2ee785f | -16.6871 | -57.4536 | 2024-10-06 01:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.1 |
| 0988a169-aafc-3750-bbf7-ffa62ed8f941 | -16.7067 | -57.4514 | 2024-10-06 01:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.9 |
| 2e2a596f-8931-32e7-9b3f-b48ca20676e9 | -16.8433 | -57.4562 | 2024-10-06 01:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.4 |
| 41d64733-02f3-32ca-80ac-c655cde67adb | -16.9545 | -56.6226 | 2024-10-06 01:36:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.2 |
| 6f90aae5-d990-3c0f-921f-16e1e8ddf4c3 | -16.7647 | -57.4856 | 2024-10-06 01:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.4 |
| fde38943-bab9-301c-9c5d-41ad8be2a900 | -16.8238 | -57.4584 | 2024-10-06 01:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.3 |
| 34a4102c-5f6c-3335-950f-192a758ef310 | -17.3837 | -42.6483 | 2024-10-06 01:36:42 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 2cf8331b-a3d8-3130-a9f1-3c9b19208499 | -17.0007 | -55.0607 | 2024-10-06 01:36:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 820281db-2e0f-3924-8a13-4247c7731ea8 | -17.1182 | -57.4039 | 2024-10-06 01:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.4 |
| 95add4a3-6ef6-33dc-a185-9ea768652095 | -17.1375 | -57.4221 | 2024-10-06 01:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.3 |
| eb2671d4-cefc-304b-8150-074557119550 | -17.1571 | -57.4198 | 2024-10-06 01:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.5 |
| a1466bda-b2c8-3d21-8f2a-71e7b4cf2a3b | -17.812 | -53.7859 | 2024-10-06 01:36:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 47665ea7-75d9-3bea-9465-15d7ad4e0305 | -18.6586 | -57.2759 | 2024-10-06 01:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.8 |
| e1699294-4ff0-379d-ac4c-de5615ca643a | -20.5813 | -49.3865 | 2024-10-06 01:37:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 71.4 |
| cfc475ff-be15-3d5a-940f-779bc742a48c | -20.582 | -49.3635 | 2024-10-06 01:37:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 032a2963-8361-35a3-8189-f4c817ffd554 | -21.5218 | -50.9088 | 2024-10-06 01:37:05 | GOES-16 | LUCÉLIA | SÃO PAULO | Brasil | 3527405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.2 |
| 4ed70861-8e0c-30fc-8d27-b9241215e5d8 | -25.0112 | -54.064098 | 2024-10-06 01:38:35 | METOP-C | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 020b3080-cb18-349d-b3dd-f780c4cf7db8 | -25.0135 | -54.073601 | 2024-10-06 01:38:35 | METOP-C | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 483be3a0-46a1-30ff-b1ef-1c386d668e33 | -25.0158 | -54.083099 | 2024-10-06 01:38:35 | METOP-C | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2114433e-d15f-3390-bada-71fc53d3147b | -21.5194 | -50.8773 | 2024-10-06 01:39:18 | METOP-C | SALMOURÃO | SÃO PAULO | Brasil | 3545100 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8b680838-8ee8-3b63-9fce-8b06d3871567 | -21.5238 | -50.893398 | 2024-10-06 01:39:18 | METOP-C | SALMOURÃO | SÃO PAULO | Brasil | 3545100 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 629df673-d6b2-3fcc-87bb-a9b092d2187a | -21.5098 | -50.880299 | 2024-10-06 01:39:18 | METOP-C | SALMOURÃO | SÃO PAULO | Brasil | 3545100 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7115b0ae-476e-3fa3-a38f-90c809ef8b5e | -21.5142 | -50.8964 | 2024-10-06 01:39:18 | METOP-C | SALMOURÃO | SÃO PAULO | Brasil | 3545100 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0100edb1-41d1-314d-a965-be9ebc53e2a4 | -22.5061 | -55.202099 | 2024-10-06 01:39:20 | METOP-C | LAGUNA CARAPÃ | MATO GROSSO DO SUL | Brasil | 5005251 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 11bd0fb1-832b-37c3-a86f-39129ad7a540 | -22.4963 | -55.2048 | 2024-10-06 01:39:20 | METOP-C | LAGUNA CARAPÃ | MATO GROSSO DO SUL | Brasil | 5005251 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bebf7c39-df39-3065-bd7f-a6c1fac28eaa | -20.5825 | -49.3438 | 2024-10-06 01:39:26 | METOP-C | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bee88403-cf58-3773-9bdc-eaef90feb318 | -20.5884 | -49.3647 | 2024-10-06 01:39:26 | METOP-C | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 612adeac-7494-370a-a7f1-90e224f063e6 | -20.572901 | -49.346901 | 2024-10-06 01:39:26 | METOP-C | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 480414e6-f29f-3ca9-bbc3-fdc8f9768179 | -20.5788 | -49.367699 | 2024-10-06 01:39:26 | METOP-C | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c0b3e381-1818-3407-b9a6-e9909cf83684 | -20.5847 | -49.3885 | 2024-10-06 01:39:26 | METOP-C | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e9697bcf-b405-3dc3-9a74-c0ce85639dcb | -20.5693 | -49.3708 | 2024-10-06 01:39:26 | METOP-C | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9f48ccca-6c7e-3a3a-b21b-332e9b9ec6b2 | -21.4018 | -57.2341 | 2024-10-06 01:39:45 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3574f056-3295-3233-b47b-68ecb41a81a4 | -21.403601 | -57.241798 | 2024-10-06 01:39:45 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4866e8b3-8b0f-3f4f-9dc8-e4ec7cbfc43d | -21.405399 | -57.2495 | 2024-10-06 01:39:45 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| dcdb48e4-e9c5-3b43-ac83-881b85baa04e | -20.773199 | -54.819302 | 2024-10-06 01:39:46 | METOP-C | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b177b0fa-bcc6-3af8-9712-58aee22ae9c8 | -19.656 | -56.451199 | 2024-10-06 01:40:10 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| abfe0ecb-3007-3ae3-a55f-98d0ac191286 | -19.658001 | -56.459599 | 2024-10-06 01:40:10 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 597a023b-605f-3b4e-9068-13363d0e6f32 | -18.884701 | -54.528801 | 2024-10-06 01:40:15 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e62ede70-0aa6-3737-b0ea-e6147dd7cd41 | -18.8874 | -54.539398 | 2024-10-06 01:40:15 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f1c3dfb4-aa59-3275-8a61-4e6c1abf97c4 | -18.875 | -54.531502 | 2024-10-06 01:40:15 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c2384507-8abc-3000-a4e3-80e6944c7ca3 | -18.877701 | -54.542099 | 2024-10-06 01:40:15 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| cbab3fe6-2825-314b-b452-73812437ffb5 | -18.8652 | -54.5341 | 2024-10-06 01:40:16 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d3d501a5-c706-33cc-a9a4-7423946addb1 | -19.1392 | -57.5061 | 2024-10-06 01:40:23 | METOP-C | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 42dfba7b-8ce4-32da-bf80-9ba5c8887d2a | -19.108801 | -57.464401 | 2024-10-06 01:40:23 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ac3d4c60-2f0d-33cb-b742-56a2274eab23 | -19.1106 | -57.472198 | 2024-10-06 01:40:23 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 219b47c1-983d-3116-a353-1f644a661065 | -19.100901 | -57.474701 | 2024-10-06 01:40:23 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3eb7a6b5-20fe-350f-9384-a68512f1a926 | -18.8813 | -57.686001 | 2024-10-06 01:40:28 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cbcf2b4e-5e77-3f98-8be7-f1a69be05439 | -18.699301 | -57.261501 | 2024-10-06 01:40:29 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 39b874fc-ac34-3cff-9679-29254f81df35 | -18.7012 | -57.269402 | 2024-10-06 01:40:29 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d552edb5-54a1-3f3d-bff7-122fde4fd4d7 | -18.702999 | -57.277401 | 2024-10-06 01:40:29 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 11917f4d-7265-3a70-b711-39e5ed03921f | -18.704901 | -57.285301 | 2024-10-06 01:40:29 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8c32820a-a5e3-3581-86cf-689e83eafb3c | -18.7197 | -57.3484 | 2024-10-06 01:40:29 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9ddb1b12-ed77-3e9b-9aca-4287dde504a7 | -18.7216 | -57.3563 | 2024-10-06 01:40:29 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cda91bfb-b84a-3f0d-a7a3-d02604ae27c0 | -18.689501 | -57.264 | 2024-10-06 01:40:29 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 21702c05-3787-3673-9303-a40776d9a8b2 | -18.7099 | -57.350899 | 2024-10-06 01:40:29 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cf2dcaf4-6063-3efa-8d6e-d5cfb7522aac | -18.6779 | -57.258598 | 2024-10-06 01:40:29 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a49a455f-d8fa-3e78-b5c1-1e5ad97b440b | -18.6798 | -57.266499 | 2024-10-06 01:40:29 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 40853cd5-963f-379d-8805-a73ea635d14e | -18.6663 | -57.253101 | 2024-10-06 01:40:29 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README26.md)
