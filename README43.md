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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40ee57cb-dfca-391b-8315-d2071838b023 | -15.34141 | -56.69271 | 2024-11-26 05:03:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bdece15b-74b1-3180-8fcb-87e6eed4b7e7 | -11.93294 | -62.92725 | 2024-11-26 05:03:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b2b6d0d-6d49-3e3b-aa82-7785e020514a | -12.0389 | -54.676 | 2024-11-26 05:03:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf0d1f93-ca29-3282-873a-5a91d5dcc847 | -15.33806 | -56.69217 | 2024-11-26 05:03:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6cd62b3b-3ab2-3281-b8ed-58e35789f444 | -9.92837 | -59.93136 | 2024-11-26 05:03:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 007e9bba-43e9-3a8d-8357-8d661bfe0299 | -12.02047 | -62.95191 | 2024-11-26 05:03:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c06f7a3f-ff10-3062-a8cf-c8c22e1fbd0c | -16.02437 | -57.58683 | 2024-11-26 05:03:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8c0a06c-f10e-34bc-9154-305022ae5c1a | -9.54782 | -61.9334 | 2024-11-26 05:03:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 032a735c-66de-3601-85bd-efbf682365cf | -9.55696 | -61.95457 | 2024-11-26 05:03:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 640a0da1-6cab-3193-897f-cab34b4287a7 | -9.55761 | -61.95076 | 2024-11-26 05:03:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cade68d6-1644-3305-a1bb-9644b60c61fe | -17.63599 | -57.58804 | 2024-11-26 05:05:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 18ec4376-9119-3581-b71f-751a9d76e1fa | -17.65263 | -57.59082 | 2024-11-26 05:05:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 829e44f3-aeef-336c-98d6-188dd6557cc5 | -17.63266 | -57.58748 | 2024-11-26 05:05:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| e36db368-6f4c-3eb0-b2b3-65b60fa64fef | -20.80129 | -53.55106 | 2024-11-26 05:05:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b03acacd-f6a8-3b12-8eb1-05c841d4793f | -18.1114 | -51.16368 | 2024-11-26 05:05:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6d332b4-d03c-329b-a2fa-5e030d76450e | -20.70548 | -54.64085 | 2024-11-26 05:05:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0266629-6831-36d3-887a-57252a7dfe9b | -20.7972 | -53.5504 | 2024-11-26 05:05:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 531c3d7e-5872-3867-bb4c-b3ecaa9f02ff | -17.63322 | -57.58384 | 2024-11-26 05:05:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| cf576ae8-fb17-3751-b27b-3db561fe4e79 | -17.63988 | -57.58495 | 2024-11-26 05:05:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 284eeb5e-2091-35bc-8f5d-5932a3ec40ef | -17.65319 | -57.58717 | 2024-11-26 05:05:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a274a596-7793-3506-bd8a-3da371cd6ff3 | -19.67004 | -49.89521 | 2024-11-26 05:05:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b3f1130-582f-3398-a683-59c8d5a17cbf | -20.32477 | -48.83371 | 2024-11-26 05:05:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0267c4f3-3fbd-38c1-9de7-dea280e8db12 | -20.32513 | -48.8299 | 2024-11-26 05:05:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69f981aa-c02b-3e13-b843-a7725176988b | -23.7472 | -49.01808 | 2024-11-26 05:05:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e30c7fe6-2c31-3b4b-89be-2953cbd4d328 | -20.64447 | -56.58831 | 2024-11-26 05:05:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a579a014-3be7-3ffa-a644-4b2210a3c259 | -17.64321 | -57.58551 | 2024-11-26 05:05:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 132e700b-9340-3982-add9-96c21eb970af | -18.24596 | -55.39458 | 2024-11-26 05:05:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 64fefd75-f47d-33b9-8fd2-270f019101fb | -17.63711 | -57.58075 | 2024-11-26 05:05:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 52a80a9c-b869-36dd-9958-79230c450b26 | -20.32004 | -48.8306 | 2024-11-26 05:05:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 87f2dc1d-9dd6-3dcc-ba7b-8b23d43bd761 | -21.55959 | -54.20267 | 2024-11-26 05:05:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 37c54e1c-f8e9-3948-8723-374b8df05937 | -16.88741 | -57.51368 | 2024-11-26 05:05:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f21d5177-0d84-36f7-82dd-6bbc4926d415 | -17.56513 | -57.47518 | 2024-11-26 05:05:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a3806972-6b1d-34f8-b941-70df7027cead | -17.64654 | -57.58606 | 2024-11-26 05:05:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.2 |
| 74631c28-21f6-3adb-8318-a0779aec40a3 | -21.56356 | -54.20327 | 2024-11-26 05:05:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cd4b0fd6-3b4d-33a4-a00f-946bde06443e | -20.3252 | -48.83493 | 2024-11-26 05:05:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24e7355b-1a8b-3afc-b1cf-79dc6d1edbda | -17.63655 | -57.5844 | 2024-11-26 05:05:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 8302a3f4-cf56-3cf3-98cf-9c63a64003e3 | -18.11077 | -51.1689 | 2024-11-26 05:05:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43c57aac-9b15-370b-8a4c-ad69599dfeee | -20.32559 | -48.83112 | 2024-11-26 05:05:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b37f1ce7-69e4-3461-9eb6-d729c1a7d22c | -17.72098 | -54.93122 | 2024-11-26 05:05:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7112af51-719a-367e-8cf1-cba8fab4af46 | -18.24375 | -55.39663 | 2024-11-26 05:05:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d16399da-2707-3146-95f9-4d4fb51ef3c9 | -22.10545 | -49.61525 | 2024-11-26 05:05:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f65f71ba-06b4-387b-9edf-816140d86d6a | -22.07316 | -56.45464 | 2024-11-26 05:05:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 49a7434a-be65-39a0-b900-4c308faeaa22 | -19.67517 | -49.89579 | 2024-11-26 05:05:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 064f7775-97ab-316d-b301-81912eb54724 | -17.64265 | -57.58915 | 2024-11-26 05:05:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| b219dcae-7a49-32f3-b4a4-d796c0ad861d | -17.6549 | -57.55376 | 2024-11-26 05:05:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 87b77fd4-ecfb-3f6c-b2eb-3dc31d4fc0b9 | -20.31959 | -48.82933 | 2024-11-26 05:05:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06021eda-ea73-3d50-84b9-0cf8c7dd45ee | -17.56846 | -57.47573 | 2024-11-26 05:05:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0b9ca5a1-e0a8-31b9-926f-97fe10b92225 | -17.70397 | -54.94656 | 2024-11-26 05:05:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83a5703b-f2bf-3ff2-82ab-e7f82f690cb7 | -19.1905 | -52.32161 | 2024-11-26 05:05:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5cfe061-8950-38f6-99eb-34ea0813d098 | -18.11539 | -51.16945 | 2024-11-26 05:05:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58611774-e0ed-3709-bbb5-5f53a0aed4b6 | -17.65157 | -57.5532 | 2024-11-26 05:05:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ed5de1cf-b1cc-3035-8001-d05bf66f6ed0 | -17.64986 | -57.58662 | 2024-11-26 05:05:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.2 |
| f1a5c614-e19a-3b5e-bfaa-f9b9622589be | -22.10009 | -49.61444 | 2024-11-26 05:05:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d09b5946-f185-30d8-b247-77d9893f778a | -24.73011 | -52.19486 | 2024-11-26 05:08:00 | NOAA-20 | MATO RICO | PARANÁ | Brasil | 4115739 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ce669930-beb0-3843-b163-3bdcae824228 | -3.1876 | -48.4387 | 2024-11-26 05:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 127.7 |
| bba94536-c90c-3f64-b391-706725198104 | -2.6943 | -51.9831 | 2024-11-26 05:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 75226ed8-e3b9-3982-9083-a595392ae5e5 | -3.1691 | -48.4394 | 2024-11-26 05:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 512a5573-7bd9-3ced-95a4-e167bde92543 | -3.1877 | -48.4172 | 2024-11-26 05:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 856a2b6a-4e1b-3e60-b2d4-bf02f24a8161 | -3.1465 | -45.2504 | 2024-11-26 05:20:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 3c5516df-2a2e-33dd-8ac3-a0a1fa8a9341 | -3.1691 | -48.4394 | 2024-11-26 05:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 5d4f19f4-8f49-3e10-8ec9-12cbfe815819 | -3.1877 | -48.4172 | 2024-11-26 05:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| b3482feb-f8ca-362c-a271-d25d96e32106 | -3.1876 | -48.4387 | 2024-11-26 05:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 9fb018a5-4e9b-3be1-bcc4-eba93c3dd41c | -4.24882 | -48.66692 | 2024-11-26 05:22:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6a49ada6-47ad-32a7-9a59-ae1ed0f6bb81 | -3.14349 | -45.24451 | 2024-11-26 05:22:00 | AQUA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| fb8230d7-f02b-3de3-9a0e-ffed02b00080 | -4.29545 | -48.23172 | 2024-11-26 05:22:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 63e83f8c-7545-30e6-beb8-aca6cef3d8b6 | -4.65689 | -47.93956 | 2024-11-26 05:22:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b30f155b-5891-3482-bd86-2883b1e8438a | -3.95936 | -48.08029 | 2024-11-26 05:22:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 03278c68-69d1-3c38-8abc-1932e51e1b80 | -3.91239 | -42.42552 | 2024-11-26 05:22:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 3d1349c8-1f36-310f-ab59-cccf9d48a0d5 | -3.17774 | -48.43146 | 2024-11-26 05:22:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 154.4 |
| 684bb944-7c98-366e-86ef-5d9a0529445a | -3.17947 | -48.42004 | 2024-11-26 05:22:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| f4ee6f53-82f5-3804-9e17-81dd86fc7d88 | -3.91402 | -42.41449 | 2024-11-26 05:22:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 8f062b4b-646f-3992-bf53-c79e074b185c | -2.57422 | -45.46556 | 2024-11-26 05:22:00 | AQUA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4a9abbec-b0a8-3c55-94f4-31a06c8e101b | -2.71204 | -46.26233 | 2024-11-26 05:22:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 32ca1ebf-ac3c-3e68-b728-6e571361ecd5 | -5.76486 | -47.81119 | 2024-11-26 05:22:00 | AQUA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ca6e8349-7120-3fbf-8e43-5f29f4cb63b8 | -3.9042 | -42.41309 | 2024-11-26 05:22:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| bb72910a-111e-3926-b8fc-d1771446b390 | -3.97227 | -48.06034 | 2024-11-26 05:22:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 408.0 |
| 08bd1d74-4abb-3014-a356-0beb988a101c | -4.30454 | -47.51268 | 2024-11-26 05:22:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e8f475f7-9e5e-334b-8c29-25829dd3e610 | -2.92566 | -48.01075 | 2024-11-26 05:22:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6448b00b-922a-3f92-98d0-7dcf99933aed | -2.71826 | -46.28185 | 2024-11-26 05:22:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 19f66e3d-d758-374b-b633-caf0257588c4 | -4.65534 | -47.94981 | 2024-11-26 05:22:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 27e3acf0-d60e-330b-97cf-d5e6ba933325 | -6.17982 | -43.40475 | 2024-11-26 05:22:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ef5bb88d-ab81-348a-8fcf-31462b4ac331 | -3.9803 | -48.0724 | 2024-11-26 05:22:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 232.3 |
| 31520bd1-a341-320a-81ef-894648a68e24 | -4.04582 | -48.31954 | 2024-11-26 05:22:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2a29167d-065d-3567-9456-e2d09e6f7da4 | -2.54284 | -46.40276 | 2024-11-26 05:22:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 44b27411-9ec1-3945-a9cc-4caf0288715d | -3.07223 | -49.19626 | 2024-11-26 05:22:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| e6a7c8e6-56ca-34bc-a6e7-c6035576da9c | -3.9787 | -48.08297 | 2024-11-26 05:22:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 195.1 |
| 88362f41-b2c9-343a-af8e-4607b8374be7 | -4.35836 | -48.07814 | 2024-11-26 05:22:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 28c65f2e-6ce1-3cbe-90a9-abc6082fdec8 | -3.16775 | -48.42997 | 2024-11-26 05:22:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dd0e4691-5b65-312e-bc68-d59abd5ef257 | -3.16601 | -48.44139 | 2024-11-26 05:22:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c837335f-e1ab-3ef2-8dd1-d1825c1963fa | -2.93474 | -48.8169 | 2024-11-26 05:22:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 861bf861-9f27-3650-b52e-090978a61cdb | -3.98189 | -48.06195 | 2024-11-26 05:22:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 123.1 |
| f29b7e45-83f0-3253-bfba-62b860361522 | -3.38515 | -44.17328 | 2024-11-26 05:22:00 | AQUA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 65d7db3b-f880-39e5-90a9-19fe35cd9944 | -1.5856 | -45.461 | 2024-11-26 05:22:00 | AQUA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| eff652e9-16fc-3d08-87ba-70c6320c7843 | -4.23883 | -48.66543 | 2024-11-26 05:22:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c7f4c69c-a889-3dc5-8dd8-a1b4c7cefde7 | -6.18933 | -43.40623 | 2024-11-26 05:22:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9bd40261-0051-3557-a321-231a7e316313 | -6.18785 | -43.4166 | 2024-11-26 05:22:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| facc3b87-340c-3c04-9a8a-84462e24ca0f | -4.30604 | -47.50288 | 2024-11-26 05:22:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 996adb2d-36d2-35a0-abd7-d9d740ba6537 | -3.38651 | -44.16421 | 2024-11-26 05:22:00 | AQUA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 3a2ddcaa-0d52-3c13-8454-d500c842b89f | -3.96262 | -48.05897 | 2024-11-26 05:22:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 212.4 |
| 70241e0d-a9b3-3159-bdc0-5918e52279d4 | -3.96904 | -48.08157 | 2024-11-26 05:22:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 249.7 |


[Clique aqui para ver as próximas entradas](README44.md)
