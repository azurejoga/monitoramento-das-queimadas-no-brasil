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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b439236-4c50-3880-b403-82b8de83f3d8 | -20.25023 | -46.47651 | 2025-04-22 04:10:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| f0119436-4c77-3f98-b3c7-aa9eb41be086 | -20.25089 | -46.47262 | 2025-04-22 04:10:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a19750bf-9127-3121-8038-fb0cd56eba14 | -22.24891 | -52.97461 | 2025-04-22 04:10:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b3c0c87c-96f3-3652-9b1d-de0351c5f096 | -21.22413 | -48.61316 | 2025-04-22 04:10:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7b352d07-98ca-310a-b2d3-4590fe276da4 | -20.24932 | -49.3459 | 2025-04-22 04:10:00 | NOAA-20 | ORINDIÚVA | SÃO PAULO | Brasil | 3534203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 21650916-2459-373c-847a-40b1e9c9557f | -21.22047 | -48.61241 | 2025-04-22 04:10:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 822c858d-2efc-3fcb-a529-cb0378776944 | -20.3765 | -45.60188 | 2025-04-22 04:10:00 | NOAA-20 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38ff44f1-a34a-3986-93e4-4ff13b0502ad | -30.89401 | -51.60654 | 2025-04-22 04:12:00 | NOAA-20 | ARAMBARÉ | RIO GRANDE DO SUL | Brasil | 4300851 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 3a65b394-32bc-33ad-912b-a660e80a0998 | -30.89536 | -51.60783 | 2025-04-22 04:12:00 | NOAA-20 | ARAMBARÉ | RIO GRANDE DO SUL | Brasil | 4300851 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 00fa877d-7d06-36e9-ae49-8417052a963e | -5.00845 | -56.17457 | 2025-04-22 04:55:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d0e91c0-9fc1-3da9-b2fd-1a1e389eb697 | -6.48426 | -53.48232 | 2025-04-22 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 254f7965-eee2-3c97-9c46-3c07dc76fa17 | -11.0851 | -54.52883 | 2025-04-22 04:57:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26373a67-3db1-318d-8099-b9b3eb902946 | -7.57001 | -45.84432 | 2025-04-22 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd9f57ff-5e19-300e-933e-da35a776dee9 | -11.25723 | -52.47041 | 2025-04-22 04:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c940a561-f6af-3051-bb7f-d63f92ed5451 | -7.56688 | -45.84269 | 2025-04-22 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c008d442-05d5-392f-885b-c88d9ec4bcac | -11.41014 | -52.95015 | 2025-04-22 04:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7cb8da6c-c81b-33ae-ac06-15f354008112 | -7.57043 | -45.84114 | 2025-04-22 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5953ae9c-b6d5-33b3-b599-59fca7925e66 | -11.27372 | -52.45655 | 2025-04-22 04:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd6ec114-0654-3fac-95c0-2a5ed7b1b2f0 | -11.57547 | -47.6276 | 2025-04-22 04:57:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f99b0bca-df9e-3f51-ab9b-9db144fa30c5 | -11.58094 | -47.62289 | 2025-04-22 04:57:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb3cb97c-946a-3529-85d3-adf2a086a79c | -7.57242 | -45.84029 | 2025-04-22 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4129466-5262-30ba-b224-b4afba1135f5 | -11.27725 | -52.45709 | 2025-04-22 04:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ce56ba3-6132-3c8a-b003-1cbece52e957 | -11.40725 | -52.94577 | 2025-04-22 04:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9a2b3a04-237d-3d95-8df8-394f09d6b5a8 | -11.28077 | -52.45762 | 2025-04-22 04:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5edb2461-04c2-32ca-a1f3-273cd07d416c | -11.27312 | -52.46057 | 2025-04-22 04:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a9ac0be3-8cc1-3098-9bb3-3bb5d1b2cc82 | -7.57197 | -45.84348 | 2025-04-22 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99eaf19f-fb3f-39c2-a978-42718d06c85a | -11.41072 | -52.94628 | 2025-04-22 04:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06537a26-8b87-367a-a41a-d69e7aca2f3b | -11.27665 | -52.46111 | 2025-04-22 04:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5605f99b-ed2c-3286-befd-959a90157c05 | -7.56731 | -45.83958 | 2025-04-22 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45ccd010-003d-3d1d-b856-6fe050977785 | -7.57085 | -45.83796 | 2025-04-22 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 209b7cc8-592b-34be-8d0a-a5c46fadeb39 | -7.56775 | -45.83646 | 2025-04-22 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 420f293a-42d7-3c07-9d92-99356b0a5634 | -11.26076 | -52.47097 | 2025-04-22 04:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 376cb78e-acbd-3fe9-ad9f-37070a03b6a4 | -13.13988 | -53.25016 | 2025-04-22 04:57:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b148babd-aad5-3c7a-a048-729a4088daf3 | -13.13293 | -53.24909 | 2025-04-22 04:57:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dceb9f0e-04ac-349c-a6ec-71f2457b034f | -11.40437 | -52.94138 | 2025-04-22 04:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c622b245-1905-30fc-8c00-927f25e94135 | -13.13641 | -53.24962 | 2025-04-22 04:57:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40405692-8488-3173-8c3a-8f6d57240ead | -18.23385 | -48.19702 | 2025-04-22 04:59:00 | NOAA-21 | CUMARI | GOIÁS | Brasil | 5206602 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbd4c2c5-24ff-3b8f-86b3-4a9f6234f0c8 | -16.68237 | -43.88783 | 2025-04-22 04:59:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6333dcc0-4241-318d-a643-409426bccee9 | -15.25708 | -47.46178 | 2025-04-22 04:59:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ea6d547-0fb9-36af-a4a3-bf3f62f4f0c5 | -15.25745 | -47.45865 | 2025-04-22 04:59:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 30ec610b-f231-3a83-a182-da2f95c3ccbc | -17.26803 | -49.01009 | 2025-04-22 04:59:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0662785-5914-30a0-a17c-4cce6bf83aac | -19.66267 | -51.3406 | 2025-04-22 04:59:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73e7504e-4d55-3190-b0d2-b1fc919fe3fe | -14.65946 | -50.18646 | 2025-04-22 04:59:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c3fefa9-3687-3fe6-a904-2949f3e85f56 | -15.26254 | -47.45935 | 2025-04-22 04:59:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c94fae8-84b0-31ca-9e71-7aaff8be7a27 | -20.47972 | -53.67636 | 2025-04-22 05:01:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cac8237e-257a-3269-a88a-b6eb7db41343 | -21.58651 | -56.45537 | 2025-04-22 05:01:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 61cde3c5-ec40-32b7-a864-eeca3dac20fa | -20.25564 | -49.6744 | 2025-04-22 05:01:00 | NOAA-21 | AMÉRICO DE CAMPOS | SÃO PAULO | Brasil | 3501806 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d046ba52-14c6-355e-a2fa-d053573f7683 | -21.6715 | -49.05701 | 2025-04-22 05:01:00 | NOAA-21 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7cde7dc-5557-32fb-a767-8af05976e214 | -22.24942 | -52.97415 | 2025-04-22 05:01:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1d6b3648-5c9b-3507-9117-67c41d579c63 | -21.08931 | -49.24328 | 2025-04-22 05:01:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c8002a0c-55a7-3277-898b-0bb62b94486e | -24.24337 | -50.73934 | 2025-04-22 05:01:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 05ff28aa-a74d-33c2-ba87-67a3db75647c | -21.13321 | -55.96649 | 2025-04-22 05:01:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e3bc5f9-11e5-360d-90f6-54c72d9e45b5 | -21.2256 | -48.61445 | 2025-04-22 05:01:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 31071319-2de8-303b-9456-1bb0f51ada70 | -30.39216 | -54.25442 | 2025-04-22 05:04:00 | NOAA-21 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| eeaadd5f-ee85-377a-9ec2-79bb4a420697 | -30.3926 | -54.25033 | 2025-04-22 05:04:00 | NOAA-21 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 64517094-df2a-3eef-802b-293397b0b7a1 | -7.39197 | -39.75185 | 2025-04-22 05:14:00 | AQUA_M-M | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 10.2 |
| c9b7934e-4d80-3b25-a300-6e715b036274 | -15.25138 | -47.45604 | 2025-04-22 05:16:00 | AQUA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 129f0fa4-27e4-351a-9a1a-52fbb96e240a | -11.27299 | -52.46029 | 2025-04-22 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1c781ee-2dc8-3c4b-ab42-b39f75248528 | -13.13619 | -53.2512 | 2025-04-22 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c6f02a1-1ec2-3c02-aede-37b3b5bac91e | -11.27521 | -52.46067 | 2025-04-22 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94bf347c-73d5-3547-9953-233c2b12c799 | -11.27565 | -52.45731 | 2025-04-22 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86735a88-4772-3e38-ba60-a8d14e337713 | -11.27341 | -52.45691 | 2025-04-22 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf10955d-a7c4-3c1e-8531-f937ccd09231 | -11.27876 | -52.45761 | 2025-04-22 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b703a5ee-9bd1-372d-a92f-1816502b3838 | -11.26986 | -52.45998 | 2025-04-22 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d110f31-0a29-3f5c-b6da-4efd15996365 | -11.27834 | -52.46099 | 2025-04-22 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8ce707f-7f58-3b3e-8710-077b9169f03a | -13.13098 | -53.25051 | 2025-04-22 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a79021c1-e572-32ea-ba23-4e9191d64746 | -26.78089 | -53.23819 | 2025-04-22 05:29:00 | NPP-375D | MARAVILHA | SANTA CATARINA | Brasil | 4210506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8816cfaa-742a-3453-a1e6-9728e5eeb968 | -30.39262 | -54.25064 | 2025-04-22 05:29:00 | NPP-375D | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 222d9e86-eb6d-3026-813e-c86b4a89508b | -9.32759 | -37.03234 | 2025-04-22 11:55:00 | TERRA_M-M | DOIS RIACHOS | ALAGOAS | Brasil | 2702504 | 27 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 56fb2cba-9879-35ff-a325-4312b2867920 | -8.45201 | -36.22472 | 2025-04-22 11:55:00 | TERRA_M-M | TACAIMBÓ | PERNAMBUCO | Brasil | 2614709 | 26 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 0bcd6283-d418-38cb-be4a-7f46c7409d18 | -9.80825 | -36.89019 | 2025-04-22 11:55:00 | TERRA_M-M | GIRAU DO PONCIANO | ALAGOAS | Brasil | 2702900 | 27 | 33 | nan | nan | nan | Caatinga | 11.9 |
| b3414237-fe5a-35b9-b1c2-c762bfe0f0f8 | -8.91238 | -39.92416 | 2025-04-22 11:55:00 | TERRA_M-M | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 2a548351-2c90-3e7c-b6b4-fe9c23207ee1 | -9.80686 | -36.90011 | 2025-04-22 11:55:00 | TERRA_M-M | GIRAU DO PONCIANO | ALAGOAS | Brasil | 2702900 | 27 | 33 | nan | nan | nan | Caatinga | 60.2 |
| d2dc0654-cb11-37a7-849c-2b32dca6e1ac | -9.32624 | -37.04195 | 2025-04-22 11:55:00 | TERRA_M-M | DOIS RIACHOS | ALAGOAS | Brasil | 2702504 | 27 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a43d96f0-36dd-31b1-8c0d-d7980289c504 | -8.11752 | -35.66308 | 2025-04-22 11:55:00 | TERRA_M-M | BEZERROS | PERNAMBUCO | Brasil | 2601904 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 99595062-93bd-3113-87e4-7b0b09fa73a4 | -8.00789 | -36.97804 | 2025-04-22 11:55:00 | TERRA_M-M | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 5a679cfe-26b9-3e7a-bd13-e3bdf25d1315 | -9.626 | -36.94292 | 2025-04-22 11:55:00 | TERRA_M-M | JARAMATAIA | ALAGOAS | Brasil | 2703700 | 27 | 33 | nan | nan | nan | Caatinga | 7.5 |
| ccce4ff9-43ec-3250-a206-d32cac6a1749 | -13.14676 | -40.68617 | 2025-04-22 11:57:00 | TERRA_M-M | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 88f01453-b6ee-3dfd-b773-1b42792f06fe | -11.09357 | -37.37915 | 2025-04-22 11:57:00 | TERRA_M-M | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 4f9d1779-da42-32a8-8c32-b153ab70fe19 | -11.14557 | -38.26072 | 2025-04-22 11:57:00 | TERRA_M-M | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| a0ea5bd7-0c13-3388-89a0-1790db8b5948 | -13.10492 | -41.27583 | 2025-04-22 11:57:00 | TERRA_M-M | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| c4a365fa-5fc4-359d-be28-7abed5d804a7 | -10.70783 | -38.87206 | 2025-04-22 11:57:00 | TERRA_M-M | QUIJINGUE | BAHIA | Brasil | 2925907 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 8c4c17e2-4198-31ff-8b4a-c58afa39e5ff | -13.10344 | -41.28563 | 2025-04-22 11:57:00 | TERRA_M-M | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| ce8b4151-3a39-31e0-bb95-b88b4b109db2 | -13.1454 | -40.69548 | 2025-04-22 11:57:00 | TERRA_M-M | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 50064d6d-bb91-3efc-b131-323883aff7da | -10.70655 | -38.88098 | 2025-04-22 11:57:00 | TERRA_M-M | QUIJINGUE | BAHIA | Brasil | 2925907 | 29 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 790f81e9-c6c7-3777-a132-5abd6d4043ce | -10.56687 | -38.75732 | 2025-04-22 11:57:00 | TERRA_M-M | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |


