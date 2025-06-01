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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5bbedc4-1de9-37e7-b383-a3d1f61cf2d9 | -2.37481 | -51.88038 | 2025-06-01 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea67566b-58d8-3ead-b54d-2e88ac26c54f | -6.29189 | -51.11415 | 2025-06-01 04:55:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41742aa2-5516-3311-8736-2a435e919cd8 | -8.68457 | -46.64182 | 2025-06-01 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e7ffda0-1361-39c5-b863-46fab683afa6 | -6.86393 | -47.84092 | 2025-06-01 04:55:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5866e7c-b0d5-3bd1-a3c1-0c9735656bc5 | -6.44679 | -45.72615 | 2025-06-01 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 541e1bda-5ed0-3daa-98f2-ffddf86be63c | -8.67783 | -46.6455 | 2025-06-01 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65cddedb-1dca-3d38-9638-ab2043c72206 | -4.24655 | -47.58486 | 2025-06-01 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e978ea0-b557-3680-9a85-de267d10e482 | -5.84643 | -47.88936 | 2025-06-01 04:55:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9867fc0e-4d04-3d04-8aab-63c88148febb | -9.39942 | -48.94538 | 2025-06-01 04:55:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19f56eca-eaab-3744-b74a-0985b0cf5552 | -8.72472 | -50.26497 | 2025-06-01 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c79ee362-103d-39d0-a717-6e5629f4e210 | -2.58252 | -51.91976 | 2025-06-01 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d9f9516-bc1c-3968-a9a2-986b91dcd03b | -8.67289 | -46.64476 | 2025-06-01 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 11bf0ae2-9c2b-31fb-bf14-b6ca2cf7a8c8 | -8.6737 | -46.63899 | 2025-06-01 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99bf460d-8658-3e05-b9f4-7ed1a65c9e66 | -7.07971 | -46.55565 | 2025-06-01 04:55:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3a71d3e-7e5f-3a77-b220-381d16451b9d | -6.63611 | -47.34854 | 2025-06-01 04:55:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac6ee89f-21ee-3df9-85f0-cae0b4db4469 | -6.44638 | -45.72913 | 2025-06-01 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f5c1ae6-9527-3d3f-8a63-b49b55e26e35 | -7.22881 | -43.12287 | 2025-06-01 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5e1c904a-c4c7-3264-8384-4cb91b99d680 | -6.4515 | -45.72974 | 2025-06-01 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe0a0214-993f-3ff6-a30d-0a71499b2333 | -8.68278 | -46.64614 | 2025-06-01 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0eaf7a6c-2130-3bf2-aa7a-ad4006c8e4c3 | -9.40125 | -48.42328 | 2025-06-01 04:55:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52df2a6b-237e-3cdb-a04b-edcf68099a39 | -8.66795 | -46.64401 | 2025-06-01 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 04db6631-a680-3aaa-bf42-a631040faae3 | -7.58233 | -45.86538 | 2025-06-01 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90710003-ada8-384d-97e4-b13a3197c267 | -7.22235 | -43.12461 | 2025-06-01 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 080220e8-86b6-3986-b1b9-dd14ae7775d8 | -4.48523 | -48.86687 | 2025-06-01 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c1450e4-1f0b-360d-a8ac-125722b47a43 | -8.7308 | -47.98753 | 2025-06-01 04:55:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f57d1a48-7c69-3757-a7cf-f03e138ac9bc | -8.67961 | -46.6412 | 2025-06-01 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d2e7c941-a6d1-36a2-a37e-e2eab4542ba4 | -2.37201 | -51.87629 | 2025-06-01 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 91ae02f7-9b8f-3d96-9fb0-3451140017b0 | -7.2227 | -43.12191 | 2025-06-01 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 95325b07-6bf1-3c53-9856-4386ba95ab8b | -8.6836 | -46.64032 | 2025-06-01 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ba09e8e-4c93-3b4c-bea5-09d4a16ba372 | -7.31031 | -47.02302 | 2025-06-01 04:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f154359a-7698-33b6-b5fc-c2100ae88842 | -7.22106 | -43.134 | 2025-06-01 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 6abe0e9b-ff09-3da1-ad94-2c27d9ebc449 | -7.22782 | -43.13018 | 2025-06-01 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 755defa0-8639-3f80-a74f-5a8902e356d4 | -6.68438 | -55.19904 | 2025-06-01 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0142e1f7-1583-34ea-ad2b-8e8a69dfe31c | -7.22147 | -43.13137 | 2025-06-01 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 89239217-92d2-3596-b099-0e72493284b5 | -8.73142 | -47.98306 | 2025-06-01 04:55:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 142dcfd5-156a-3fad-ac5d-d3159809c602 | -2.58195 | -51.92333 | 2025-06-01 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8827a7be-4d5d-3b5e-9ce9-690c4ff9658f | -4.36976 | -55.76954 | 2025-06-01 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbd7e984-7c83-3ca2-92f3-4ba089b0bc52 | -6.68495 | -55.19551 | 2025-06-01 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4c853d7-eeb9-31d3-bd95-004caf6c9137 | -6.63338 | -55.00763 | 2025-06-01 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14e11261-051a-393b-85a1-d14f19cfaeb6 | -7.21536 | -43.13044 | 2025-06-01 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cd50b9fc-adca-3ab7-bacc-95654d313b0f | -7.26182 | -49.51007 | 2025-06-01 04:55:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 723610f2-ec6f-3174-a679-8067a14d4082 | -7.0076 | -44.62202 | 2025-06-01 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| babe42db-db55-3952-b278-09ecd7fa1fd0 | -10.82613 | -56.94415 | 2025-06-01 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83c20b49-2682-387d-896f-a1a8b5705186 | -11.03613 | -53.99956 | 2025-06-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 928677e8-deeb-3828-83c1-c7a9be8d6ce8 | -14.0191 | -55.13861 | 2025-06-01 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12d04f92-70a8-3832-a528-c2002b6a9648 | -13.72151 | -58.67381 | 2025-06-01 04:57:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7172196-09c6-30db-8cb1-817d429e72e4 | -10.8277 | -56.95583 | 2025-06-01 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e8847ff-e9d2-301c-bd25-03f2f86e06ef | -9.38625 | -63.43384 | 2025-06-01 04:57:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c04e3c6c-7568-30bb-8309-2cfe878d4f0b | -11.43984 | -55.00519 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec53b985-5c25-3fd9-87a8-b9b6d432fbd9 | -11.90179 | -54.78624 | 2025-06-01 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64de3484-bdd9-3ed4-87cd-b4ceb5fe9cc3 | -10.07413 | -52.75251 | 2025-06-01 04:57:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37733fca-e161-34a4-b0d4-1e163fd0b30e | -14.57245 | -58.74824 | 2025-06-01 04:57:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 75eaea9e-6c91-35c0-ba43-e9fbdbe94e3e | -12.66271 | -58.21684 | 2025-06-01 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3caf7176-4d44-3ef9-beae-c9d2fe886403 | -10.61053 | -57.60936 | 2025-06-01 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e02eeadc-42f2-3aa3-81d2-42ab1db0bebd | -12.53042 | -57.18696 | 2025-06-01 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45a6e03b-9b85-33c2-b034-5dcd6b54e0c2 | -15.06054 | -43.8718 | 2025-06-01 04:57:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e664a52d-967b-3d53-825a-faec6b5b2042 | -13.95461 | -54.4929 | 2025-06-01 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36d034e5-486c-38a6-8b6c-61cedaf71dd9 | -9.80024 | -54.72152 | 2025-06-01 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2673cd3b-2b69-3722-88af-2aa259d38e6d | -13.10226 | -52.28628 | 2025-06-01 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8d083171-2f5c-3084-aa7f-78adc3ff741b | -11.07487 | -54.77731 | 2025-06-01 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea9f1e65-e585-3916-9d71-01027176f7c3 | -9.3857 | -63.43684 | 2025-06-01 04:57:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f1b74ec-535b-3085-9e10-b676a32dff8a | -11.91695 | -54.42377 | 2025-06-01 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e11a204d-3ec8-350d-80f6-b47903a81170 | -11.4222 | -55.09596 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e668b20-52f5-3a22-a6ac-2c57e32f8f72 | -11.78538 | -54.77131 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2992c8ab-a5a0-3601-91b8-7f100af34bfe | -11.35769 | -55.20419 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d5acf5da-badf-368f-a91c-bf78593b9c73 | -14.03075 | -55.12946 | 2025-06-01 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abc69586-e1d8-3fd6-8f6c-07241e8d4719 | -10.29534 | -59.09734 | 2025-06-01 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2dec79c6-a604-3ebc-87a3-79a7a0cfad4d | -12.45699 | -57.20539 | 2025-06-01 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e9eef97-2457-32d0-b2ed-d1321ea8cfeb | -11.44315 | -55.00573 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8b08b61-c38d-3b12-9c68-bb22842a5386 | -10.14412 | -52.13631 | 2025-06-01 04:57:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b3ba09a8-3b75-3489-9b7b-87c7a1b8d75b | -14.68991 | -45.08699 | 2025-06-01 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74822fe2-417c-365f-85cf-02b2d619964c | -11.08096 | -54.78189 | 2025-06-01 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b34f291c-bc96-3e85-b7b9-389fc42256c0 | -9.92798 | -59.90255 | 2025-06-01 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 7b787aea-dd80-3b55-b402-3489e0b86133 | -10.19807 | -52.64719 | 2025-06-01 04:57:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c8dd0eb-70a4-3aa2-b4da-8a0469c85cba | -10.3056 | -57.14475 | 2025-06-01 04:57:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e6ebc158-f935-319f-983f-775fc3dc666f | -12.72149 | -54.97108 | 2025-06-01 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 744aa5b8-03c0-317a-a69c-a1ee103454e3 | -14.02742 | -55.12892 | 2025-06-01 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7525d859-57d0-3256-a8d9-4211a52e07de | -14.81016 | -48.36558 | 2025-06-01 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9024c502-e759-39c1-aab8-0711dc5770cd | -11.57209 | -47.45507 | 2025-06-01 04:57:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c91a48c4-5cf0-38bb-81ba-5a1677a13461 | -9.93197 | -59.90326 | 2025-06-01 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72bf9be0-1401-3a19-acbb-9bcb0287b832 | -11.91471 | -54.41606 | 2025-06-01 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5ab3c4c-e0c7-3c24-8900-d3fcba2f01e5 | -11.08537 | -54.77539 | 2025-06-01 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ad67635-cfb7-30e4-aa36-4c70ed079b65 | -9.3952 | -56.00943 | 2025-06-01 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b8d7a30-3b83-3e9e-937c-1c82109f7a3f | -11.41668 | -55.08787 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d50fd5c4-4fe4-3fcc-a2d6-a90572f5ff8b | -13.09022 | -45.2714 | 2025-06-01 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d12eb0e5-27a7-3140-9cfe-015056f9e21d | -11.14319 | -53.9415 | 2025-06-01 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b01f2a7c-c258-3d25-8164-43665c687ec1 | -13.09599 | -45.27212 | 2025-06-01 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82a1140a-3d9f-39c8-947d-2a8a9c27ed1b | -11.4299 | -55.00359 | 2025-06-01 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f97944a6-3609-3d09-84b7-5d74272dce85 | -12.0825 | -54.58126 | 2025-06-01 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38fb3d5f-2533-3e15-915c-f50199320210 | -14.68836 | -45.1009 | 2025-06-01 04:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3e8773e-efd1-3387-9794-1e48b570b7fc | -14.01799 | -55.1237 | 2025-06-01 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac5b2e09-4eb9-3920-9823-736a408ec72e | -14.60303 | -47.9669 | 2025-06-01 04:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec034083-6825-3846-b592-d4162385d78f | -10.30621 | -57.14097 | 2025-06-01 04:57:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24207074-af9d-3bdb-bd2f-f7e534231905 | -11.92139 | -54.41711 | 2025-06-01 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6821b7c2-c501-3204-bc55-9091950171c4 | -10.65466 | -49.42748 | 2025-06-01 04:57:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f69bc773-f769-37f2-b4b8-0d5b10f545ba | -12.0154 | -49.5286 | 2025-06-01 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75e94766-8b45-3307-b7ae-64c440f21b67 | -12.46183 | -54.91547 | 2025-06-01 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8571af8d-7ec6-35f5-ba2d-51a5c4692e55 | -14.03574 | -55.1413 | 2025-06-01 04:57:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6be1e1e5-83a6-3312-9957-aaee4735ed89 | -17.11264 | -49.14141 | 2025-06-01 04:57:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d7ecd7e-38fa-3d1d-93d1-2556dfd637a3 | -11.07764 | -54.78135 | 2025-06-01 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README12.md)
