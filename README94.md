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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b275dd0-4750-316f-b088-ec2cacfc3b1f | -10.09674 | -59.16183 | 2025-09-13 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c68482c2-1e8f-3cea-ba82-aa9fc7054df3 | -9.50112 | -55.96448 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| fca152e4-cfc2-31bf-9c69-627da3997b78 | -10.27502 | -57.79672 | 2025-09-13 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| acb956a9-c08c-33bc-8c43-f50b95006943 | -9.25497 | -59.40524 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d5676e4-93cd-3009-9c09-a8d8ac026d2a | -10.91444 | -55.67882 | 2025-09-13 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d02dc3a-2b7c-3928-9796-86f5e08ac334 | -12.10948 | -44.89503 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6fffaa66-357b-3d93-b09e-22c994c30fb4 | -10.79066 | -50.53651 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 06309bde-8bbd-3d76-aa3d-3c5b66fe7864 | -10.01647 | -51.7317 | 2025-09-13 04:59:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c762096-9f22-35ff-bf92-559839196112 | -12.10803 | -44.85714 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e0ca5e5-9eb2-336a-8db7-527bb7bff579 | -11.47476 | -43.607 | 2025-09-13 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 685333f0-8349-31e8-86a8-b56ca456f251 | -16.31342 | -48.89831 | 2025-09-13 04:59:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 134c03e6-4bd6-3146-b9ec-eeb46cf3f52a | -15.15471 | -50.12687 | 2025-09-13 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6e1a5e73-788d-3fac-b391-6e6172b61425 | -11.44982 | -43.57273 | 2025-09-13 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5a59768-c7ea-3884-b260-e728560ce58b | -11.63029 | -46.91771 | 2025-09-13 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 506ad116-d7de-3d90-ae04-63c69b4b136b | -15.2426 | -51.39999 | 2025-09-13 04:59:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 03aa6c10-1a1a-3dca-8dcd-7b5a8ad17763 | -14.19251 | -46.27525 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 37ecbedc-43fa-3b29-b13c-09f5b523dd1f | -12.7995 | -47.99434 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 55fcef7a-10ef-304d-9f55-63a9dbb00433 | -11.38902 | -50.47077 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7ae170fa-824a-378a-9b32-1b825a1753fc | -12.91784 | -54.79878 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f23a5391-ecac-3dec-a8cb-f0935c29ab55 | -11.87092 | -50.56855 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 1522bf32-7ad4-3a16-94be-c8a2ae29e34e | -14.38794 | -60.28522 | 2025-09-13 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b90b660-af94-37ec-baf6-cb806ec69e78 | -10.20898 | -51.66778 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e33cadec-63d2-3775-ae5a-30324ae17167 | -11.37044 | -59.14612 | 2025-09-13 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0dafffb-9c19-3072-9f09-671b3bc83c60 | -13.90305 | -48.28918 | 2025-09-13 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 566ab1b8-887c-3889-9f0d-3014d733d559 | -14.70398 | -45.14913 | 2025-09-13 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| eac928c9-b9a9-3863-91ec-c84dab3077f7 | -15.69975 | -50.58094 | 2025-09-13 04:59:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 47694b16-804d-3a7d-bf11-f1168168fca1 | -11.18435 | -55.08517 | 2025-09-13 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e63907b9-78c4-3082-9100-01ed513ea73d | -10.51199 | -51.54242 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aa9cd985-519b-3bc3-afb1-f6a745214625 | -10.5151 | -51.53587 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| de35965b-2db3-3c9f-828e-cb9a17e5958f | -14.71968 | -59.71843 | 2025-09-13 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43b4fd7f-f04f-3831-92e9-f80232d71203 | -14.18025 | -46.28425 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 80880874-b6e1-33d8-875d-5b3c66a83edd | -10.35427 | -50.50689 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73ee901d-fb22-3bff-b15d-1a8736f78719 | -9.51859 | -59.73251 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45c1e217-a17a-3f3e-a040-18a13c6a528e | -11.09661 | -51.96639 | 2025-09-13 04:59:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 012bf10f-edf4-3bf4-97cb-3a038218d9b1 | -15.76721 | -53.49583 | 2025-09-13 04:59:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b6ddfda1-b933-3440-99d9-1f1476af1137 | -10.52384 | -51.50094 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51b83802-d0a6-34e3-bb3d-d2c4e10faa5a | -11.14105 | -50.72357 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 16f1055f-0e1e-3656-ba0c-80433ee16025 | -12.86797 | -62.1018 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 432c0d1d-c4d9-37de-bded-b514b28fd080 | -12.66034 | -44.24293 | 2025-09-13 04:59:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0484652f-0ff2-39b1-8b2d-36c5d3c11959 | -15.8671 | -49.94736 | 2025-09-13 04:59:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c5ded1e9-a423-3aaf-863d-3aa5838d2a28 | -15.6738 | -54.34835 | 2025-09-13 04:59:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f0da1f5-a2af-3aba-bc90-dfc5b9015273 | -11.87444 | -50.57269 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b3e3451a-2d80-3da1-882e-5e817e65e4a2 | -11.15936 | -50.70674 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 29951f91-5f8b-3e3e-8910-0d68f81e241f | -10.85336 | -48.18715 | 2025-09-13 04:59:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d36c4142-88f4-3e18-af29-48536ba54eb7 | -15.78695 | -52.22482 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 10c83f98-e38e-3689-9f30-83b16fc3f987 | -14.75107 | -55.61202 | 2025-09-13 04:59:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 22791e71-c787-3592-84a9-33a816e3b83f | -15.69552 | -50.5804 | 2025-09-13 04:59:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e6e6403e-97a7-3ee2-86be-cba237b0a423 | -10.50449 | -51.54189 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bec9845b-c39f-3cc2-8442-7610154ed12d | -14.19668 | -46.23967 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a5d86a6d-225c-390c-8917-dbedcf168027 | -11.80185 | -50.55203 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3167b5cf-9eac-30d0-8eb0-d97b302c6231 | -9.49055 | -55.98811 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d71db69-7f39-3e08-8143-4082a0ab3e94 | -11.12821 | -50.70095 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9b980700-396d-3297-bfd5-ea53e9ed47a5 | -11.57907 | -50.57006 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| bda7b06d-f3e5-3824-ae85-b4650d1156df | -15.28227 | -53.77581 | 2025-09-13 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4378431-9e42-334c-83ed-1069a7df05ce | -11.13607 | -50.7021 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 542bfbe3-30d2-39dd-b63f-07565a50a0fc | -10.50325 | -51.53941 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0fbc5650-ccce-3ce6-8c62-3e01d27592cb | -9.50777 | -55.96555 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d709caaf-ed40-30f4-bb92-b088eb86e717 | -11.01806 | -51.34018 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f52ee373-1208-300d-9bf4-e70433c32a97 | -9.16708 | -60.30197 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7aab6ba1-ce0d-363d-8f5b-a84d65f1f3f8 | -11.43736 | -45.6254 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 09955afa-c2f4-3f30-a93d-0434a9011e3d | -10.41493 | -50.61769 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 31669597-371a-39b4-ba33-cefd67b2eeee | -11.99926 | -47.76291 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 037d2960-6c2d-3448-8c30-5f1193c88fa2 | -11.76668 | -51.51473 | 2025-09-13 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8e9be6c9-0347-3836-b7ca-cba5799b3ec7 | -14.19515 | -46.25275 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6197f23f-288f-39bd-a128-ca38ff575b95 | -14.2036 | -46.27614 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4dab3fd9-3e93-3aca-9281-61e2e0d4642d | -11.0939 | -51.43382 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 7d56347b-d466-35ab-ac11-e71a37b1a13e | -10.71375 | -48.61332 | 2025-09-13 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 818df9e7-96fc-36bb-b084-0a8a0132fc2a | -9.79915 | -61.51389 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e266f82e-454d-3f78-b4b9-ab5ccdf2deed | -12.96054 | -54.74297 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df1764bd-5224-35bb-b097-e6e1c06d11dc | -12.85978 | -62.12218 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc99fb48-36de-39ba-8045-2336e94b163b | -13.78151 | -46.29295 | 2025-09-13 04:59:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a1f5c721-6af9-3b5b-a239-f3e2fecf7a22 | -10.52253 | -51.53693 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 643e5f8f-0cb9-3ec4-b867-6dd1ea41645a | -11.70877 | -46.54897 | 2025-09-13 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c218db9b-8ea7-3519-9071-21a4c902324f | -14.20878 | -46.2797 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f4d90eb9-1075-3ba2-986e-a3254c0666b2 | -12.10916 | -47.57827 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 658012ea-fdb8-32e3-a6e0-bd21bba85e74 | -14.19982 | -46.26071 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 35f6fe81-1e05-32d3-91b6-e850abe58b96 | -14.18577 | -46.28497 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d4bd2936-4db3-36d7-bc20-bee157d7f349 | -11.19283 | -51.41758 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3013e915-5b09-37b3-84fc-014c307779a1 | -14.17741 | -46.26059 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| c1b3b95d-0ac1-37cf-a43e-524f9a0591ff | -10.51003 | -51.55573 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9a098701-9357-30d9-9b42-d073eb9fe42e | -11.63066 | -46.91486 | 2025-09-13 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c22f4fa2-f1da-3708-bf90-3892a70cbd94 | -9.89162 | -58.33256 | 2025-09-13 04:59:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da509562-7293-34fd-8ace-4fe7eed0645c | -12.09338 | -44.87986 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1ed9ad7c-a6bc-39cf-b4dc-1ec8a6645d00 | -12.1256 | -47.59005 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8e4b89b5-c9ba-34ff-b089-4e487cad63e1 | -15.71291 | -50.58144 | 2025-09-13 04:59:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 14f517e5-0199-3d22-9a04-83bfbc4bd210 | -15.68764 | -50.57492 | 2025-09-13 04:59:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3fc8468-72bd-339e-b137-29c31b6474b8 | -11.88646 | -50.57444 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1a5d8c60-a0a6-3446-a9dc-23d26453d1ec | -11.45874 | -43.5787 | 2025-09-13 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45661b0f-37be-3eca-9c5e-fa3ac79f261b | -21.58022 | -48.41884 | 2025-09-13 05:01:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 8aeb0208-c0fc-3ecb-bdaf-9623be74da94 | -16.49934 | -55.11975 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 130ea430-79b1-3b05-a50b-8eb0eb618cca | -16.33512 | -51.54599 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 289771d3-fd43-3d71-b6d1-2b6c9ae1cdd9 | -16.60786 | -49.46948 | 2025-09-13 05:01:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4ec3cbf0-1bab-3a45-9e67-ee81acc3d34d | -20.33963 | -46.66496 | 2025-09-13 05:01:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b59b2ac6-8ff7-308d-bbf1-d8e8e45df42d | -17.41756 | -49.24123 | 2025-09-13 05:01:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3e70d915-c709-37ac-b273-a78133da40e3 | -21.62357 | -46.81996 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| aa1319e5-0645-397a-8b8a-e918b2c59b40 | -18.98838 | -48.42447 | 2025-09-13 05:01:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f56b4dc3-5762-3a56-aef2-6504ac0545f3 | -18.8924 | -47.05922 | 2025-09-13 05:01:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2e90d972-76a6-369c-a291-218f92e85609 | -17.12943 | -48.50191 | 2025-09-13 05:01:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9763ba22-0e83-3840-8340-21d177aaa3cd | -16.53685 | -51.74151 | 2025-09-13 05:01:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a11ac14f-27ce-398a-b1cc-ddd80ffc5033 | -21.58517 | -48.42269 | 2025-09-13 05:01:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README95.md)
