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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17c45286-cb29-3747-9275-e33a69de8acd | -15.3669 | -52.67034 | 2026-08-30 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41c15a70-60ad-3575-a243-e19d18f99608 | -10.56825 | -59.617 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df3c5c1d-0809-34dd-ac06-c65b1f81cdc4 | -11.48218 | -45.05284 | 2026-08-30 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 13917d9c-2d25-3e71-bf03-7f0f2efb9cf3 | -14.14594 | -52.84344 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 91cf7be1-9e9e-359e-b321-022fb4d62054 | -11.15262 | -50.58558 | 2026-08-30 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 413e9281-c68e-3f83-93ee-6209a366512f | -14.4076 | -52.55277 | 2026-08-30 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f9f12d9b-8fc8-3b19-86b5-fd9ad79eeb9f | -12.92374 | -45.89386 | 2026-08-30 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49001af4-745d-36b7-abe2-26c51aa3687e | -9.88706 | -60.2802 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4387f3a1-3c70-3903-98e9-b99513e88738 | -14.15815 | -52.81985 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ea7d5a3-4747-3075-a678-f32c1bfebdf1 | -11.29146 | -54.04388 | 2026-08-30 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3e373b78-8687-3c89-9737-8f2e88c73b2f | -11.21685 | -45.08356 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f38e17b-42fd-357a-a225-f45468f74cf7 | -13.93555 | -43.99679 | 2026-08-30 04:34:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ecad2150-5080-30a7-a37b-0cad89ea3a43 | -16.71917 | -47.63908 | 2026-08-30 04:34:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16bdad80-f914-3c6c-a25e-308e7db62c77 | -12.77933 | -46.45761 | 2026-08-30 04:34:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a990353-967f-39f6-ba55-470fcb322b16 | -11.21976 | -45.08801 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9075e20e-f417-31f9-afe6-eb682008119c | -11.23664 | -45.09462 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e319d90b-e987-3272-8183-a8362c0a7698 | -11.33791 | -45.1424 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a77a9235-aad9-37b5-a424-f64af9f2c5b4 | -16.34594 | -50.98451 | 2026-08-30 04:34:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3370fb9-19d1-3ab6-a57b-243652cb9d80 | -8.49847 | -55.29381 | 2026-08-30 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 474d0fd0-1509-39b2-af72-7e92883aec3f | -17.28532 | -46.01043 | 2026-08-30 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21efcd31-d6d6-3f0a-b1b0-76c36c075cd7 | -13.83365 | -54.1095 | 2026-08-30 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fbb84dd-fc7b-32bb-bcdb-445ce25a95fc | -10.79064 | -45.33007 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9ac75ebe-a744-373b-aa93-32f091d91006 | -7.32664 | -60.60943 | 2026-08-30 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3bced9ae-311f-3843-94e2-c2ca6f54291b | -11.44084 | -61.48858 | 2026-08-30 04:34:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0a452297-5b3e-3959-82a6-e2d20a524684 | -8.50298 | -55.29752 | 2026-08-30 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67e3f01f-d00f-39cc-b7c8-29db479bd1ee | -11.21342 | -45.05886 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78816bcc-f791-3649-b88d-650b8bed9133 | -9.15258 | -59.50836 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7830d92f-eea6-3937-ba19-ef7be9369916 | -10.05702 | -48.68975 | 2026-08-30 04:34:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b0e29ede-73c3-301f-ace2-dfe4d821cfd1 | -9.1532 | -59.50544 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fe8ff619-1573-3155-ab7b-e4d1feb3b3b4 | -11.23834 | -54.01138 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 1bc59ebb-5745-3333-b22a-2b77c8c7ba95 | -16.35021 | -51.0014 | 2026-08-30 04:34:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 792ea22d-3d7d-3827-ba8b-05ca03d1cb2a | -11.81342 | -51.04389 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| af7bc7f4-a433-33aa-81c9-b8a6b4b52a3c | -11.79312 | -51.05355 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 5510ac15-7162-363e-8905-6fe631852bf6 | -14.19075 | -52.86196 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fb051311-5f4b-3a38-b5e0-e9761482c45c | -7.31477 | -60.61488 | 2026-08-30 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 56a900c3-96a4-38aa-9494-524056179a6f | -14.91024 | -52.63406 | 2026-08-30 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83e4548b-8d34-384d-8f36-4177172ecd76 | -11.8127 | -51.04818 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 0ceab2f0-7bb0-3176-89ee-8fcd56d6a934 | -10.7707 | -54.04379 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 618a42d7-8743-37ff-91e7-524f7bb43c01 | -12.43473 | -42.8894 | 2026-08-30 04:34:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3c98e355-c723-3f45-bb36-39eb3c0f8114 | -10.35554 | -49.97846 | 2026-08-30 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 07b6cb0c-ab13-3043-aaf9-6ccbbf7dd11a | -10.81018 | -45.31744 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ca70a82e-a508-3d02-a587-ce23e5a790fb | -11.00376 | -49.67685 | 2026-08-30 04:34:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e337817-c2d0-36fe-a965-744d62e4e8b6 | -10.75582 | -54.05013 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1a649a9-2b8a-386c-b1e6-344904d46ac5 | -14.42951 | -52.56205 | 2026-08-30 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 32c82018-edd0-3f92-946e-07ebcc19bc20 | -9.9516 | -53.99984 | 2026-08-30 04:34:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bcdfc4ef-77b8-3eb1-ac6e-cd5010575f6d | -7.30907 | -60.60626 | 2026-08-30 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9c774645-6a98-3d7a-954d-d6a309648158 | -14.98771 | -48.17696 | 2026-08-30 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd97bc9c-9bc6-3186-9255-70e2a9bd7292 | -11.51408 | -45.54284 | 2026-08-30 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32fc5da7-8d09-31cb-95e7-6449915a37e3 | -11.16312 | -51.2949 | 2026-08-30 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7cde9f11-ad83-3c7f-a9ab-f143d86496be | -17.27132 | -46.04059 | 2026-08-30 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03e9d67d-1fda-346d-b8cb-fcfc41b62ea9 | -16.28059 | -42.57665 | 2026-08-30 04:34:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 785a0b9b-0d3d-3678-a121-bcb59727bd0e | -8.62605 | -54.69651 | 2026-08-30 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 800ce9a1-1710-3887-952d-2e59fad68141 | -12.78271 | -46.4581 | 2026-08-30 04:34:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9983690-253e-3547-a2df-90536a9652a1 | -11.80977 | -51.04637 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| b0dc85e5-032e-3f3e-86fa-a50483bcaf3c | -14.16203 | -52.82053 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f9741f2-e96d-3b90-9f82-a3708c4f375c | -14.33693 | -47.23211 | 2026-08-30 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6703e854-5247-3e10-a69b-09c206ebd99e | -9.23903 | -60.4192 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9509f749-55a7-3a93-874f-b0d38eddc0a0 | -16.2918 | -48.88493 | 2026-08-30 04:34:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af562208-5aab-36b2-96c7-3c50950aad22 | -10.81176 | -50.50634 | 2026-08-30 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 50352bc4-d683-37d4-a5bc-31e083707be5 | -13.69576 | -45.0485 | 2026-08-30 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 741e71d8-ce03-383f-a004-4444c901dcd4 | -10.99344 | -50.52268 | 2026-08-30 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7a1c51fa-281f-3eec-b0ec-7adb6846bfff | -14.40294 | -52.55693 | 2026-08-30 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd72541b-17a3-358f-9d98-9f393f78523a | -8.23446 | -54.95733 | 2026-08-30 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5f275e0-1b71-39a0-b110-f10401115231 | -14.91502 | -52.63357 | 2026-08-30 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a6b0aa1-d0e4-3e2c-9e04-8e350eda5339 | -9.41578 | -51.68859 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 76fc3458-7a20-38ef-92d8-085f3c04b209 | -10.49412 | -59.61609 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 83f0dc30-c3f4-3a84-98a6-5939a00c1893 | -7.29627 | -60.59631 | 2026-08-30 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a92bd21-dea9-310c-b2b7-e278a092f7c4 | -14.14295 | -52.83775 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce7bff64-54c3-3749-9228-16591d72788b | -9.66074 | -55.10464 | 2026-08-30 04:34:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1fe4a2bd-a30b-3ad2-8ca8-6cec9c312d23 | -10.76475 | -44.87239 | 2026-08-30 04:34:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68f6d489-0408-384d-9e29-f62e58a2ef24 | -10.14568 | -45.70487 | 2026-08-30 04:34:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebc03e5f-66a8-3a78-913a-fb825f3e2b70 | -11.16389 | -51.29041 | 2026-08-30 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bdd18403-a5e4-3e6d-9ea5-7f843bb10f37 | -14.91403 | -52.63474 | 2026-08-30 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b819ab1d-dd81-38ef-a5ba-07ff06a53e55 | -11.14904 | -50.58495 | 2026-08-30 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ac58d37-0550-3d1d-9639-310fa6818acb | -10.76628 | -54.04292 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a98fcc81-b764-3766-b493-6f736fe2595e | -11.35386 | -45.1629 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 20a1659c-f948-356b-8da0-64fdbd876abb | -15.11914 | -53.57698 | 2026-08-30 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5becf5f6-1d9c-3c53-b8ca-82a69eb658f7 | -11.33906 | -45.15838 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fe94511-8144-3354-9a20-01ab1bd94e1f | -9.93929 | -60.52376 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1e0f3463-7c54-34e8-a670-221bdfffa3aa | -11.49799 | -50.27941 | 2026-08-30 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3c83bd7-1d25-3d74-b1a0-7703620de4a2 | -9.20004 | -51.56088 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8fbf4b1b-fb36-3e70-a859-c7e833890c5f | -11.57178 | -44.03047 | 2026-08-30 04:34:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ebf2264-d0f7-3ca8-96a6-64369a505261 | -11.02627 | -57.24555 | 2026-08-30 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ac73c406-a146-35fd-bc60-7efef55d5771 | -16.34674 | -51.00086 | 2026-08-30 04:34:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 70c5c5d3-00fb-3f65-b855-85fcc21133cd | -16.33788 | -43.44169 | 2026-08-30 04:34:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3e7a0fb5-6fed-37e9-9b8d-dc47791a449e | -14.44537 | -58.47746 | 2026-08-30 04:34:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e69fb78-c7e0-324f-bb46-85104f1ecb91 | -11.03045 | -57.22407 | 2026-08-30 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 10c7d271-0100-3d3a-abea-ca01af0d5919 | -11.33733 | -45.14626 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e056c12-24d9-390f-972d-cc636de0688f | -10.95153 | -43.03537 | 2026-08-30 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.8 |
| c957fa1f-b0e9-31c2-8e4f-c6289f9df380 | -11.24348 | -54.00795 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a395ff51-b5ae-3aa4-bb6b-810f3b17650a | -9.17275 | -59.6102 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fbed7899-348d-3134-a360-2a255f40d40b | -10.72746 | -50.85665 | 2026-08-30 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 184ccda2-0d00-3fb0-bb3f-dfe698bff742 | -10.74774 | -54.04419 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a92aaa37-c030-3df4-b83a-83a1491314b8 | -10.73446 | -54.04175 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 3076229b-c76f-3032-8034-4e2b0b1bca14 | -16.34724 | -50.9768 | 2026-08-30 04:34:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 699f7f6f-6f8d-3a05-b61a-3cfb9a7959cf | -11.27139 | -45.32314 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e5e8733e-a9c2-317d-9a05-8af902460730 | -14.16381 | -52.8105 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ccbb7a76-936a-3ef9-8eff-f79172324f51 | -11.02318 | -49.688 | 2026-08-30 04:34:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc3915b3-c055-3f77-9cfe-59d03b27e2c2 | -9.16443 | -59.51636 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bc2cd88-311f-3e17-90f2-5dae9818a880 | -17.28175 | -46.00991 | 2026-08-30 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README43.md)
