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
| 59c44a5b-7a8d-31c8-b41a-0cb570a584fe | -14.90455 | -47.73547 | 2026-08-29 00:05:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 8bd20d8c-2d1e-3909-976d-3b196bcf0571 | -14.19087 | -48.75208 | 2026-08-29 00:05:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 34d8792b-a287-3416-8060-954742ebd3ae | -14.89775 | -52.60915 | 2026-08-29 00:05:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 11565138-14dc-3ef7-9bc8-0e22b023333a | -14.92104 | -56.333 | 2026-08-29 00:05:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 38.4 |
| f92489da-c123-3bed-bb93-6ec0a1092060 | -14.07509 | -44.06388 | 2026-08-29 00:05:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 99757c9f-ec4e-3051-861c-036acdc30469 | -14.89933 | -52.62198 | 2026-08-29 00:05:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 177fd356-8d08-36b2-b603-d2a7ed679ede | -17.62868 | -51.61253 | 2026-08-29 00:05:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 9aa09a6f-5803-350b-a5e6-2efc3224c9a4 | -17.59885 | -51.61659 | 2026-08-29 00:05:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 25.5 |
| fc682c3f-4b4d-35d1-a402-845162d8323a | -13.59275 | -45.78214 | 2026-08-29 00:05:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 25a34f3c-e380-38f9-bfa1-12881c956e03 | -14.93226 | -56.30756 | 2026-08-29 00:05:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 6c0bbf77-49fd-3523-aa4b-2bfbe2d97c11 | -17.58889 | -51.61779 | 2026-08-29 00:05:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d7e4dec1-70ac-320b-9912-17745b56eafd | -14.41473 | -52.57759 | 2026-08-29 00:05:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 57d65057-6957-3eaa-941a-5cacf1dfd6e6 | -17.59173 | -51.64151 | 2026-08-29 00:05:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 26.2 |
| f2bafd5a-58f5-341c-9dba-a6906f28b3a3 | -14.9009 | -52.63476 | 2026-08-29 00:05:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 8bc90bc5-22b6-33ba-a0e3-8effcfbed4ee | -14.92824 | -56.33866 | 2026-08-29 00:05:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| b9c7029c-ba8d-3a1d-8582-69dfbf1293ec | -14.9348 | -56.3315 | 2026-08-29 00:05:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| fe15d9eb-bde2-3d5c-86be-000bfffafa8f | -17.58035 | -51.63097 | 2026-08-29 00:05:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 846e3cc1-a8ec-3723-8baa-eaddfd7f762c | -14.43965 | -52.61206 | 2026-08-29 00:05:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 74b3e4c7-46a8-35ac-a961-0c9b6973ee2d | -14.17451 | -48.76374 | 2026-08-29 00:05:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0d496cfe-578e-3ebf-a8fa-d79ac92f8989 | -14.42642 | -52.58868 | 2026-08-29 00:05:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| dbea6ba6-59ab-3ff0-84da-8a88b3edb55a | -14.91272 | -52.64591 | 2026-08-29 00:05:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| dc07738e-3247-3883-8377-81e2082c09fe | -15.76599 | -50.04832 | 2026-08-29 00:05:00 | TERRA_M-M | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 22.4 |
| bb2afcae-9f1a-3a72-a3ce-a421d07e5a3d | -17.58179 | -51.64297 | 2026-08-29 00:05:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 6b3fcbfa-42be-3cff-add6-1cd01374c459 | -14.18206 | -48.75338 | 2026-08-29 00:05:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 815d5d58-3e22-3f52-9e9c-e64474026477 | -16.47768 | -49.24032 | 2026-08-29 00:05:00 | TERRA_M-M | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bd4ba87a-caac-3418-8627-34bbac10bc55 | -17.63014 | -51.62441 | 2026-08-29 00:05:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 431a40d9-6f9b-3cb6-a88d-2d28182c2d2c | -14.63513 | -50.90295 | 2026-08-29 00:05:00 | TERRA_M-M | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 922b6cb5-1124-3a86-b79a-32e3a12ac8cc | -17.59032 | -51.62976 | 2026-08-29 00:05:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 0419dd2b-d703-38f6-8340-7a07badf6864 | -14.44117 | -52.6244 | 2026-08-29 00:05:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5274702f-f246-3121-8a29-e769f8a67f0a | -14.91447 | -56.34007 | 2026-08-29 00:05:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 930a882a-74e9-35f1-aa49-ae4b8650f572 | -14.94597 | -56.3059 | 2026-08-29 00:05:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 41.2 |
| a9a91e95-d705-3b3a-9a0b-85f129000679 | -14.19213 | -48.76112 | 2026-08-29 00:05:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4a72931e-304e-31c9-8932-c0eecb6acdf3 | -14.39595 | -50.05845 | 2026-08-29 00:05:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0d799ce5-022e-3323-9508-5d0774808a7d | -17.61875 | -51.61394 | 2026-08-29 00:05:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 07514583-7b84-3a32-b4b3-3aff0d812302 | -15.64388 | -45.9193 | 2026-08-29 00:05:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| e9900beb-5c0b-3ff3-9edd-6bd888b8a60a | -14.91115 | -52.63326 | 2026-08-29 00:05:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 4a74b14c-a3fb-3961-8b75-65187b82d539 | -13.35151 | -43.65162 | 2026-08-29 00:05:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| c541c118-1c4a-3fc3-b190-63bb4a3d006e | -15.11929 | -53.5918 | 2026-08-29 00:05:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 35e92a69-5170-3c63-97ee-9add612e4d20 | -14.94854 | -56.32984 | 2026-08-29 00:05:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 2dadaf43-6d28-32b8-a8d8-896995d7cabe | -14.90588 | -47.74485 | 2026-08-29 00:05:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 33.1 |
| f479e980-f909-338a-898f-99ebdb79119e | -16.51916 | -47.73632 | 2026-08-29 00:05:00 | TERRA_M-M | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 78b5c1a0-cc0f-3ed9-98d6-1f5b3ade9bcb | -17.28241 | -46.02259 | 2026-08-29 00:05:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c1f5914b-7c6e-32cd-b7c6-86fc1db867fb | -15.11752 | -53.57703 | 2026-08-29 00:05:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 3e2e737e-5c1b-35b2-836a-907b9f7a7707 | -14.92554 | -56.31478 | 2026-08-29 00:05:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 31.2 |
| b17fbe50-f837-3d24-8fad-821a086191c1 | -12.7912 | -46.45284 | 2026-08-29 00:07:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ae5dd7fd-a64b-3c28-8fb0-266eb018fa4d | -8.81735 | -49.63281 | 2026-08-29 00:07:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| f33a6226-5ee2-3586-b7fc-446262e0648b | -10.75224 | -54.02651 | 2026-08-29 00:07:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 951c4458-01f8-3f1e-ac1f-ce1651a437b7 | -10.53858 | -50.47397 | 2026-08-29 00:07:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 589b27e4-501e-3eef-9fcd-a6b976cd0c3a | -11.71864 | -54.52544 | 2026-08-29 00:07:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 46c24a02-cf0f-3e83-9874-ff56bc80b664 | -8.59859 | -54.77934 | 2026-08-29 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 175da466-67bd-3105-95b5-8d99dda45c8e | -7.28666 | -45.8467 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| e8607b68-bb6a-3887-8444-ecea41ee3d81 | -12.2506 | -50.53889 | 2026-08-29 00:07:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| de14ee68-07a3-399d-945a-ebd07bf013ff | -11.01966 | -49.68541 | 2026-08-29 00:07:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 03d13101-9f13-3a8c-b753-560083540531 | -9.42991 | -51.68996 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| f98af816-4b0c-3700-9924-4997a0582c4f | -11.21976 | -51.30132 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 41d1bf1f-0f64-34b3-abf8-2446f95345f0 | -8.98742 | -50.80297 | 2026-08-29 00:07:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 74e37c21-48c1-3204-80c5-517bb18fbe19 | -8.24446 | -54.96473 | 2026-08-29 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 82aeacb4-7e5b-3ea3-bdbe-c271319b043a | -7.27781 | -45.86292 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 201.3 |
| 79bc7329-f452-388d-83e5-be59f570b28d | -6.90798 | -43.65551 | 2026-08-29 00:07:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 8765e4f0-e2e2-3c19-9b3b-799d9540dab0 | -7.30192 | -49.53621 | 2026-08-29 00:07:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 830366ea-3322-34f1-8788-facbb7af6710 | -14.49731 | -58.50134 | 2026-08-29 00:07:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 34.7 |
| d11bc318-e3d3-3acd-b5f7-6d9baa7f2223 | -9.9345 | -60.42139 | 2026-08-29 00:07:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 48038f40-26cb-339a-a302-16c12579ceea | -14.17051 | -52.82867 | 2026-08-29 00:07:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7a5936a9-737b-36e4-b5e6-2d55927a8711 | -8.76921 | -50.08074 | 2026-08-29 00:07:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0b44602d-599a-3c33-81bf-1d48479e6d78 | -7.29635 | -49.96406 | 2026-08-29 00:07:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| cc3f153e-5305-3f26-800a-159b5538d97d | -11.02661 | -57.2465 | 2026-08-29 00:07:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 878454f7-79b3-3c63-ac1b-ab4c63c4bcf0 | -12.18905 | -50.56341 | 2026-08-29 00:07:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3257e5b6-b1f2-37d9-8f82-f152d1a715ef | -9.69156 | -46.56104 | 2026-08-29 00:07:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 3acf1206-d135-3c74-84f4-0fd8cb9b2362 | -8.5821 | -54.82447 | 2026-08-29 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| d54bdf60-b8d9-3b4a-ae2e-e6fbe4a05f4c | -9.68997 | -46.55544 | 2026-08-29 00:07:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| a534a208-0778-327e-a1fe-a41223204cd7 | -8.01757 | -48.01524 | 2026-08-29 00:07:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 42.1 |
| dcc1da2e-cd5f-36b7-ac30-256ba76e4d4d | -8.60918 | -54.84485 | 2026-08-29 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| af616875-b1ec-3a95-824c-32a6271f191f | -8.0161 | -48.00494 | 2026-08-29 00:07:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| bcdf0fb2-6caf-3481-a01e-47e5491941d3 | -11.26912 | -54.05444 | 2026-08-29 00:07:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6d038caa-e74e-3650-b7c6-954c1d4a8a66 | -14.19421 | -52.8511 | 2026-08-29 00:07:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| fdc481f3-3891-3678-a372-900fa061abb2 | -11.48226 | -45.10818 | 2026-08-29 00:07:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 5983a023-8899-3651-b8ff-6064dc6190c0 | -7.35357 | -55.17075 | 2026-08-29 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 2c6f8181-cbd8-36a2-bbae-90a359d1deda | -8.97737 | -50.79528 | 2026-08-29 00:07:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 7d14259f-5501-3a21-ac55-b4e29f570270 | -11.36272 | -45.14885 | 2026-08-29 00:07:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 53158c53-e4dd-3ae3-8be4-32cde6b43891 | -7.28875 | -49.97415 | 2026-08-29 00:07:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 98d4a9df-3886-3567-b05d-288b2f1a7e3f | -11.18873 | -51.27647 | 2026-08-29 00:07:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c4e6f521-7717-3b37-80ed-22a9aa4359ce | -8.04633 | -54.00794 | 2026-08-29 00:07:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| eaf7e710-454d-305c-a84c-48594f4a1b0d | -9.42637 | -51.59395 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| fc047442-06cc-36d1-8fa1-d092c40db92c | -11.20689 | -51.27394 | 2026-08-29 00:07:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bbef451a-cbd6-39ad-be79-47791bf11a78 | -9.19975 | -51.55134 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c6e42eae-f7e9-3506-8e58-e3c1f26b879e | -11.04324 | -57.21326 | 2026-08-29 00:07:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 9b384a20-7757-3d2a-8021-fa4c56cc3659 | -8.52313 | -55.35362 | 2026-08-29 00:07:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| eed9d73c-cbcc-35bc-85dd-96b71529deee | -11.1809 | -51.28386 | 2026-08-29 00:07:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 7b37f10a-9892-3d2a-a08c-facdb56668b0 | -8.53629 | -55.2736 | 2026-08-29 00:07:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| b2a7645b-cf7d-33a3-823c-f46c27d0bcd5 | -12.76012 | -44.272 | 2026-08-29 00:07:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 78aa75fd-f016-392a-96a7-21c0da25ef4e | -7.30319 | -49.54527 | 2026-08-29 00:07:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| c7ad224b-9bbb-3ae3-95a4-a8ee09610309 | -9.96729 | -53.92883 | 2026-08-29 00:07:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| c853b53d-4da9-3023-9cc9-6bd1b4fd8aad | -9.2306 | -51.57579 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 19b19c5b-badb-3154-bb68-545c669cc6c2 | -11.0209 | -57.26513 | 2026-08-29 00:07:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| f95539d4-cb74-369e-80cd-41316538d157 | -8.52509 | -55.36939 | 2026-08-29 00:07:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e3102eca-5e35-3f26-b384-0474afa8d59b | -9.20876 | -51.54991 | 2026-08-29 00:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 897d01f7-0b48-3b05-82b7-a93d8104ec28 | -11.02935 | -57.21503 | 2026-08-29 00:07:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 29540775-b39f-3215-8ddf-9dcff4dac0de | -5.34211 | -45.17485 | 2026-08-29 00:07:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c736ca33-0e95-3d0e-a46a-5425e2289241 | -12.7815 | -46.45447 | 2026-08-29 00:07:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| d2f880de-68aa-3ec8-a462-b570fc5deeff | -9.93903 | -60.46318 | 2026-08-29 00:07:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 32.3 |


[Clique aqui para ver as próximas entradas](README3.md)
