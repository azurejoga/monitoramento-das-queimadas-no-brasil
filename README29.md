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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a03a276-b176-3df3-af8f-e83ed6713ccc | -11.03979 | -55.37875 | 2025-06-28 06:10:00 | AQUA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 0710fb27-20d7-35a8-8fc1-9cc9adc1f1cb | -10.83044 | -53.75097 | 2025-06-28 06:10:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ca92f1bc-47d1-35a7-9761-bf69126e6afb | -11.03013 | -55.37731 | 2025-06-28 06:10:00 | AQUA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| d0f09292-669d-32bf-97d0-12f8ccc9f4cf | -10.8394 | -53.75238 | 2025-06-28 06:10:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 988a5688-fdfa-3241-bba1-c51ead075ada | -9.43809 | -63.46603 | 2025-06-28 06:10:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da3ca03e-654f-3ed2-b74a-708f53df3d87 | -9.03645 | -63.98226 | 2025-06-28 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6abc46d8-e6ec-342b-be9b-75e2f3ae23ac | -11.88534 | -58.73415 | 2025-06-28 06:10:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 33651423-d530-3a1c-b294-14976ae4c831 | -9.43852 | -63.46283 | 2025-06-28 06:10:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 941fb8bb-9d4d-3189-95af-414de4e53c60 | -9.42799 | -63.46147 | 2025-06-28 06:10:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75019b4d-b4e8-3888-b671-e5734e736731 | -9.43739 | -63.46362 | 2025-06-28 06:10:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72f0f39a-e512-3048-b727-ad020b1bb339 | -9.44266 | -63.46426 | 2025-06-28 06:10:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24b6af33-a23f-3d8e-b51f-82364820f0c3 | -11.87814 | -58.72807 | 2025-06-28 06:10:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59b3f7a2-7b10-3025-8ed4-4db49ccb7e2b | -9.42842 | -63.45827 | 2025-06-28 06:10:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ffab8b02-05e5-3e37-9d12-1ef17b528197 | -9.60231 | -63.47003 | 2025-06-28 06:10:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cd6674c-1da8-3215-bec7-0ea649cae333 | -9.43781 | -63.46035 | 2025-06-28 06:10:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e7e4530-32e0-358d-b563-7ff0374b523b | -11.88458 | -58.73657 | 2025-06-28 06:10:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3f5c148-e38f-3ef7-ae4c-29e0082c0e07 | -9.13169 | -63.91828 | 2025-06-28 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b83b918-141e-3707-a33f-442da96c0242 | -9.4438 | -63.46345 | 2025-06-28 06:10:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| de0f5886-6559-3439-9b14-ea1930157e1f | -9.03604 | -63.98523 | 2025-06-28 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9395e189-eff9-3009-bd8b-dcaded948253 | -9.13211 | -63.91523 | 2025-06-28 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bba0e6b0-d4cf-3700-9384-95b350fe843a | -11.0455 | -55.3773 | 2025-06-28 06:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 74cc283a-59fa-3d2d-b17b-8824e8453dfd | -11.0455 | -55.3773 | 2025-06-28 06:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 83224353-48f0-3da5-92f7-890b8f105fca | -11.0455 | -55.3773 | 2025-06-28 06:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 51dd8878-d512-3cda-a70b-3305c8f8d777 | -11.0455 | -55.3773 | 2025-06-28 06:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 2724b227-b584-3a00-ac3d-06396f65e45a | -9.7041 | -56.1843 | 2025-06-28 07:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| d7daca9f-8f19-3ce8-8b33-9f77ca178b02 | -11.0455 | -55.3773 | 2025-06-28 07:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| bb4f911e-6e3f-3281-b42d-75acf807170d | -11.0455 | -55.3773 | 2025-06-28 07:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| d7835b78-d188-30bb-8c29-e5e188a9ef95 | -11.0455 | -55.3773 | 2025-06-28 07:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 3536eb1f-41ce-399d-a079-fbcbd690a632 | -11.0455 | -55.3773 | 2025-06-28 07:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| d2af00cf-7061-35ea-8591-6d7f7673a4fa | -11.0455 | -55.3773 | 2025-06-28 07:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 457f2f4e-ea51-347f-b0ef-c66c49715485 | -11.0455 | -55.3773 | 2025-06-28 07:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| fd54bb52-d5da-36aa-9e7c-6b02892b0a12 | -11.0455 | -55.3773 | 2025-06-28 08:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| f912f151-8af2-3f2c-baef-35c8d758e536 | -11.0455 | -55.3773 | 2025-06-28 08:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 1a007e50-29ab-335b-a324-ad32f6d5dbc4 | -11.0455 | -55.3773 | 2025-06-28 08:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 2262fad7-5b69-3336-ba1b-c667f0f3537e | -11.0455 | -55.3773 | 2025-06-28 08:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 77190e26-e655-3180-a5d6-05927f46a9fb | -11.0455 | -55.3773 | 2025-06-28 08:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| c9120e3f-1214-3ab6-8c73-e9d0592df398 | -11.0455 | -55.3773 | 2025-06-28 08:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 84164b1e-d9cb-30b3-b63d-e9ed41ca5090 | -11.0455 | -55.3773 | 2025-06-28 09:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 8a88a6cd-c6fb-3a72-8f2a-667a2142b431 | -11.0455 | -55.3773 | 2025-06-28 09:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| f7053026-3dff-3b11-80a5-d61a9c186de8 | -11.0455 | -55.3773 | 2025-06-28 09:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 7a6ea98d-04b6-3d76-8309-c814421d9f7b | -14.2442 | -45.5002 | 2025-06-28 10:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 128.2 |
| a1cdeffb-7e82-3d74-9e9f-13e06c5a5091 | -14.2442 | -45.5002 | 2025-06-28 10:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 159.2 |
| add964a7-1781-3a53-bc13-67199115fc4c | -14.2437 | -45.5235 | 2025-06-28 11:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 77bfa8ec-f405-3144-9ce4-93a673641636 | -14.2442 | -45.5002 | 2025-06-28 11:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 16e875c8-1b45-36ee-8ab9-3b70507a20a3 | -14.2442 | -45.5002 | 2025-06-28 11:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 156.5 |
| eed05fa2-df79-3811-8375-f3022f23446b | -14.2437 | -45.5235 | 2025-06-28 11:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| e18323e5-bb36-323e-891e-ecd41735b681 | -14.2442 | -45.5002 | 2025-06-28 11:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 161.8 |
| e7c75dc3-f032-30f0-94eb-72c30eda212e | -11.2664 | -52.7527 | 2025-06-28 11:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| c76f6898-1ee7-3293-99e1-520532ed354c | -14.2442 | -45.5002 | 2025-06-28 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| e6d04fa7-a15b-3e07-8bbc-1400cf5d07b6 | -11.2664 | -52.7527 | 2025-06-28 11:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 13be8e3c-4b82-3ccb-9bd0-627d73a9a182 | -14.2442 | -45.5002 | 2025-06-28 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 0221954d-fdac-3939-84e4-f3c34c9c5c34 | -6.90396 | -43.98626 | 2025-06-28 11:47:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| da604d9d-e364-3ccd-9354-88dacf610b4e | -6.90699 | -43.96718 | 2025-06-28 11:47:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 05d7388f-0a9a-3175-865e-0236283aac7a | -7.22066 | -43.07145 | 2025-06-28 11:47:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 22f57611-291f-3e26-a7f0-10233892db33 | -7.21811 | -43.08758 | 2025-06-28 11:47:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| c44d6104-b6d6-326b-8066-e1897b4a788c | -6.9505 | -42.88017 | 2025-06-28 11:47:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.4 |
| d3a4cd5b-e922-382c-9fa0-8f051c669931 | -5.45707 | -43.07761 | 2025-06-28 11:47:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| b275a2cb-9e7f-3e21-91b9-661024f6dc0c | -6.95177 | -42.88965 | 2025-06-28 11:47:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 4f992a80-0c93-3738-82ea-daadd6347d35 | -14.37946 | -46.12706 | 2025-06-28 11:49:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| abc9ded2-3c2e-3bd6-afaf-04bebf7c88b4 | -14.24541 | -45.52512 | 2025-06-28 11:49:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 1667bcdb-2b82-3abf-82e5-140760644b99 | -14.23298 | -45.52291 | 2025-06-28 11:49:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 38.0 |
| dac6605d-4b0e-38d8-8761-413cdae3e343 | -11.57026 | -47.43169 | 2025-06-28 11:49:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| bab54c3f-d1c9-3d4e-a521-fdc2c2a1e06a | -17.62602 | -44.63804 | 2025-06-28 11:49:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 5d8691cd-9dc3-3fd8-a8be-21b3e9378dbc | -14.24136 | -43.53563 | 2025-06-28 11:49:00 | TERRA_M-M | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| efb9f5aa-fe68-3e2e-a8d7-eb9c817010ab | -10.58128 | -43.32257 | 2025-06-28 11:49:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 0ad7933e-f728-37ba-8d10-6f9fe545864d | -16.26679 | -42.04155 | 2025-06-28 11:49:00 | TERRA_M-M | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| d4efdfee-5cce-3ede-8eab-9dbf4b45f9e2 | -11.5685 | -47.45461 | 2025-06-28 11:49:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 33.5 |
| e8cf7c40-46e2-3558-84d2-b292780d868c | -10.57978 | -43.33088 | 2025-06-28 11:49:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 910c887b-4290-3218-a4db-826ff1cce765 | -16.26843 | -42.03102 | 2025-06-28 11:49:00 | TERRA_M-M | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| e988c20d-8e52-330b-ab3d-31e15eb51cda | -14.23621 | -45.50386 | 2025-06-28 11:49:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| ddca8544-cd33-314a-9bdf-39a69c4d007d | -13.58264 | -45.24858 | 2025-06-28 11:49:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| c0168955-7a7d-3171-9164-615a4dbe014d | -17.61752 | -44.62181 | 2025-06-28 11:49:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 27.9 |
| d686fc3c-aa50-37cc-b8ce-a2453b376213 | -12.26893 | -46.76514 | 2025-06-28 11:49:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| f31ad959-8de9-3719-bea4-16f2430f2f53 | -14.24863 | -45.50601 | 2025-06-28 11:49:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 27be545a-63bc-3307-94b4-6bdc9c34a7e2 | -17.6151 | -44.63632 | 2025-06-28 11:49:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 7d37f72b-9e5f-3893-b87d-7692827f1e2d | -14.23762 | -43.52835 | 2025-06-28 11:49:00 | TERRA_M-M | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| c370d7f5-79a4-3214-a08f-c1d0f0108b3e | -14.2442 | -45.5002 | 2025-06-28 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| a4c19eea-a58f-3b6e-ba97-f6ac6433f428 | -11.2664 | -52.7527 | 2025-06-28 11:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 127.5 |
| b6dccc33-de5a-3a69-bf68-293c271e0f36 | -19.37777 | -44.79858 | 2025-06-28 11:51:00 | TERRA_M-M | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6f22ce2a-97e5-3dc6-8e88-9880a6b5bdfe | -11.2664 | -52.7527 | 2025-06-28 12:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 142.7 |
| 72512bbb-4654-36ee-a87f-da5656a4ee39 | -8.5909 | -51.5746 | 2025-06-28 12:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| cfe0e103-d839-3b32-b8bc-2ba0896894e4 | -12.2523 | -46.7766 | 2025-06-28 12:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 1f12d26b-f916-37e6-a99e-0b177d65993d | -12.2527 | -46.754 | 2025-06-28 12:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 3895300d-7231-3283-a477-d47c0f67c599 | -14.2442 | -45.5002 | 2025-06-28 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 72d75808-6c03-376a-94fa-e3c9442a8e27 | -12.2527 | -46.754 | 2025-06-28 12:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 1244a96c-3590-3342-a61c-8e40d146c0a7 | -8.5909 | -51.5746 | 2025-06-28 12:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| e9d2f86f-5122-3246-a8f5-323b30ed5d96 | -12.2523 | -46.7766 | 2025-06-28 12:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 23eaec7e-01d7-36c2-a8e4-6a3a387570ba | -14.2442 | -45.5002 | 2025-06-28 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| bbde748b-1f17-372b-8670-7518ea6e5151 | -11.2664 | -52.7527 | 2025-06-28 12:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 923880ff-ef7c-34aa-8e63-2e50e7865923 | -8.5909 | -51.5746 | 2025-06-28 12:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| e3806df8-1294-315b-89ce-18bc25a2b2dd | -12.2523 | -46.7766 | 2025-06-28 12:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 34284223-16a9-3544-b3ea-c2b8319dc916 | -12.2527 | -46.754 | 2025-06-28 12:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 4c46d82c-ff5f-355d-972d-545cf9945459 | -11.2664 | -52.7527 | 2025-06-28 12:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 183.9 |
| e0bbe5bb-0f5f-3314-a908-f255c6cace39 | -14.2442 | -45.5002 | 2025-06-28 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| e9d2946b-9a13-3d78-b7e8-255b0e36b1ef | -14.2247 | -45.5036 | 2025-06-28 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 4b5781dc-76f3-346c-814b-7db101e0dd55 | -11.2853 | -52.7508 | 2025-06-28 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 6ad95210-e5c4-3b4b-8269-b194d16284de | -12.2715 | -46.7739 | 2025-06-28 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 70113008-47b8-384c-8540-6b1d271812a9 | -12.2527 | -46.754 | 2025-06-28 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 0ab6e6d3-d21f-3753-ab98-856e01d5408a | -11.2664 | -52.7527 | 2025-06-28 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 202.1 |
| b74abe4e-a285-37a3-bb97-a445b87b585e | -12.2523 | -46.7766 | 2025-06-28 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |


[Clique aqui para ver as próximas entradas](README30.md)
