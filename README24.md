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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| def3cbc7-fe38-3764-9071-ee8eec9057ab | -9.0234 | -61.596199 | 2024-10-10 01:06:22 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4e53f3a8-3f9f-31d0-8a37-a0087b612396 | -9.0111 | -61.5863 | 2024-10-10 01:06:22 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 96460866-9f1e-3d6f-987f-4ef83926072e | -9.0136 | -61.598202 | 2024-10-10 01:06:22 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 168d90e8-41c5-3b5b-ac33-866bad1b219e | -9.0013 | -61.588299 | 2024-10-10 01:06:22 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 35b079dd-a5ce-3979-9edd-1d931d90015a | -8.9891 | -61.578602 | 2024-10-10 01:06:22 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f8c3b6de-5e2c-3aaf-9aea-14449e20aaed | -8.9915 | -61.590401 | 2024-10-10 01:06:22 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7f2ed15c-7015-3dc0-bbfb-6253c4922c8a | -8.994 | -61.602299 | 2024-10-10 01:06:22 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4e219311-3f95-387b-b213-f1842cb1fb3e | -13.8374 | -44.5455 | 2024-10-10 01:06:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 06fb6e1d-c18e-3401-b3a2-8add84201bb7 | -13.8379 | -44.522 | 2024-10-10 01:06:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 6304d33a-666a-36a1-902e-3e07198b3de9 | -5.384 | -45.965199 | 2024-10-10 01:06:23 | METOP-B | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f2370d8-0a52-3bba-9f94-38b8f2fbfaed | -5.3743 | -45.967602 | 2024-10-10 01:06:23 | METOP-B | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54f2debd-acbd-3a75-b2b7-172d3188efaa | -8.1188 | -57.667099 | 2024-10-10 01:06:23 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fec6806e-8df3-3b5f-8313-2ad141f5c66c | -8.0976 | -57.664101 | 2024-10-10 01:06:23 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 212d5ac3-e017-33e0-b34f-5c56ac279ffa | -6.3049 | -49.9604 | 2024-10-10 01:06:23 | METOP-B | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 557be66e-8718-3657-a214-2b6374f28095 | -6.308 | -49.9734 | 2024-10-10 01:06:23 | METOP-B | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcf48930-9b51-395d-802b-2b2ecbff739f | -6.2982 | -49.9757 | 2024-10-10 01:06:24 | METOP-B | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65bc731f-7b80-3227-a310-150769cccfd6 | -7.5494 | -55.3475 | 2024-10-10 01:06:24 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 257bdf0a-046d-3ce9-a476-a1126717399c | -8.115 | -58.0238 | 2024-10-10 01:06:24 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f3b97137-1a36-3690-9527-6f61dd8e3074 | -8.1167 | -58.0313 | 2024-10-10 01:06:24 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 51351d66-a039-3a13-b767-352c27791a9c | -8.1035 | -58.018398 | 2024-10-10 01:06:24 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6773b81a-9f11-3d4e-9bc4-89fd47680f95 | -8.1051 | -58.025902 | 2024-10-10 01:06:24 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd91c219-7384-3a21-9c7e-e8da8b19b347 | -8.1068 | -58.033401 | 2024-10-10 01:06:24 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 990db1e5-4069-3cf0-8a89-250697b2f2d8 | -8.8424 | -61.462399 | 2024-10-10 01:06:24 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3c5bde57-2534-33a9-ae52-84ae38ebaf6b | -5.3332 | -46.588699 | 2024-10-10 01:06:26 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a268348-614a-31b7-82d8-914792648e8e | -8.9006 | -62.3288 | 2024-10-10 01:06:26 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b62004e5-7d44-300f-804f-487f241acf43 | -8.9034 | -62.342098 | 2024-10-10 01:06:26 | METOP-B | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4909361a-4377-3bed-9603-05f829ffc494 | -6.3971 | -51.695702 | 2024-10-10 01:06:29 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f671da78-cf0f-363a-8e62-81949f6b6c96 | -6.3994 | -51.7057 | 2024-10-10 01:06:29 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee702214-a16c-3602-afdd-2f88a9a69a73 | -5.7433 | -49.2481 | 2024-10-10 01:06:30 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 904c1050-6b57-395a-860b-a450b70bb2b4 | -6.602 | -52.8811 | 2024-10-10 01:06:30 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8906050-1553-3b00-86ae-1eb7bca38a0e | -4.8938 | -45.924 | 2024-10-10 01:06:30 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 69b0de67-f73c-3c9a-9c41-48f0aeac8b1c | -6.5923 | -53.061501 | 2024-10-10 01:06:31 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65939920-1b6a-3d74-9cc0-abd4e03f0ad1 | -8.6822 | -63.0434 | 2024-10-10 01:06:32 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 980dc377-02f6-3340-9567-0d5cdd2053a8 | -8.6853 | -63.058201 | 2024-10-10 01:06:32 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ebbc7ba5-8a28-33b9-ba46-657ba148bc4e | -8.6883 | -63.072899 | 2024-10-10 01:06:32 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 913cdf8e-6fae-3b4b-a9d1-585fb5f7a35c | -6.3854 | -52.7034 | 2024-10-10 01:06:33 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25d53557-bd12-345e-9f79-05d34ee5179f | -6.3874 | -52.7122 | 2024-10-10 01:06:33 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c87ddfb-68f0-3fd7-bf33-5c53328af478 | -6.3895 | -52.720901 | 2024-10-10 01:06:33 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c96bb797-f9b1-3bfa-9a34-182e787c0c82 | -8.2344 | -61.145401 | 2024-10-10 01:06:33 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 17a4811c-0af5-3745-917d-be6585dfd1f8 | -8.2367 | -61.1563 | 2024-10-10 01:06:33 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ad070b1-9f84-338a-91e2-852e5bfb6a6b | -8.239 | -61.167099 | 2024-10-10 01:06:33 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bad7179a-0270-3dc0-8e9b-318c6a6ac33b | -5.444 | -48.900501 | 2024-10-10 01:06:33 | METOP-B | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 455fdc1a-6825-3672-a3f3-a54eb66a665c | -5.4478 | -48.916302 | 2024-10-10 01:06:33 | METOP-B | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 839abb07-3b1d-3534-bafc-103b56afcfa9 | -8.2269 | -61.158298 | 2024-10-10 01:06:33 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| adf49378-d754-3506-8998-96534e690e37 | -8.2292 | -61.169201 | 2024-10-10 01:06:33 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 62fd9880-3dba-3422-b7e7-f3c87e73183b | -8.2315 | -61.18 | 2024-10-10 01:06:33 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bb46b3fb-8feb-32b7-a120-fe0c1dcedf4b | -6.8755 | -55.103001 | 2024-10-10 01:06:34 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03611e6e-25c2-3dc9-ad2c-c0ecf10fe93a | -6.8771 | -55.110001 | 2024-10-10 01:06:34 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3ba8cc8-4b0f-31eb-ac9c-ed6f36aff0c6 | -5.9612 | -51.507599 | 2024-10-10 01:06:35 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b253886-f287-3ec7-9229-a2924ce101fb | -8.1452 | -61.255299 | 2024-10-10 01:06:35 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 656b9260-1231-3fe9-95a2-d5686bc21450 | -8.1663 | -61.3549 | 2024-10-10 01:06:35 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 514e76e2-38a0-35ec-b69a-05dfe4c60720 | -6.1342 | -52.687401 | 2024-10-10 01:06:37 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f96242c1-4160-3920-b71b-46555c33b44f | -6.1224 | -52.680901 | 2024-10-10 01:06:37 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 878a2d23-7024-347f-9b50-a5109537c11a | -6.1244 | -52.689701 | 2024-10-10 01:06:37 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abb66016-95ea-3d85-b60c-2923d4c1dbae | -7.9887 | -61.2883 | 2024-10-10 01:06:38 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa873d74-f151-3c55-b7bb-1458e85d4a52 | -7.991 | -61.299301 | 2024-10-10 01:06:38 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 772ac43a-3735-34e9-bcfd-de7a886d327c | -5.0065 | -48.3195 | 2024-10-10 01:06:38 | METOP-B | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fee59dcf-1a66-3919-b58a-01a4b8f08838 | -5.7486 | -51.435699 | 2024-10-10 01:06:38 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3276aa9-b103-329d-957b-55abea178382 | -5.7511 | -51.446201 | 2024-10-10 01:06:38 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7a8bde0-a2ff-38ce-b93c-9fc56c200670 | -4.9968 | -48.3218 | 2024-10-10 01:06:38 | METOP-B | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 013acadb-13d0-38d4-99dc-84becb1ec9a3 | -7.9305 | -61.254902 | 2024-10-10 01:06:38 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fc63ec23-5f86-370e-9868-4ab1347d7741 | -7.9308 | -61.5933 | 2024-10-10 01:06:40 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 08f71b44-b9a6-39eb-a692-1d8044fd8aa6 | -5.9067 | -52.551601 | 2024-10-10 01:06:40 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ea19744-e338-3458-8d9e-9bfde30e79d3 | -4.4717 | -46.577702 | 2024-10-10 01:06:40 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2172ca8a-e240-32c5-a4f5-46e5ca6e80b4 | -4.4563 | -46.556301 | 2024-10-10 01:06:40 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1fb1b413-1f76-37f8-ad1d-02c53472ce48 | -4.4621 | -46.580002 | 2024-10-10 01:06:40 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ea93fcc9-ed60-383f-9690-d75b5aa2666b | -4.4524 | -46.582401 | 2024-10-10 01:06:40 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b9c30e4a-7f6e-361d-a9d4-7b7691f01f96 | -7.7712 | -61.3228 | 2024-10-10 01:06:41 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0489b517-3cce-3aa4-b216-6fef41fd30e3 | -7.7735 | -61.333698 | 2024-10-10 01:06:41 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 47843dc2-5520-35a9-ac32-283ac0254706 | -6.9166 | -57.764599 | 2024-10-10 01:06:43 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81dd20ab-00d2-3ef3-8fb9-8b3bebbbff96 | -5.912 | -53.418701 | 2024-10-10 01:06:43 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6027072-e699-32b9-9089-f8037e2bcd5f | -5.9139 | -53.426899 | 2024-10-10 01:06:43 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65b90007-99ea-3766-8d55-791b151fc445 | -7.6389 | -61.181301 | 2024-10-10 01:06:43 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b508ad9c-09fe-306b-b423-ce12ff010769 | -7.6412 | -61.192001 | 2024-10-10 01:06:43 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 54476841-4bef-3566-a083-1c2a2058f706 | -6.4714 | -56.004002 | 2024-10-10 01:06:43 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d3b9df3-df3c-3721-95f2-e784f1d22f7b | -6.473 | -56.010899 | 2024-10-10 01:06:43 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9701851b-3c5e-313f-ac29-aad9c0c978ac | -6.4746 | -56.017799 | 2024-10-10 01:06:43 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa6fd504-1b98-31ad-bf28-8416390a2eca | -7.4709 | -60.587601 | 2024-10-10 01:06:44 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4ae7b96c-d999-3d84-b8d7-7f315c98790f | -7.1378 | -59.2855 | 2024-10-10 01:06:44 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6f23ac7c-b279-35a4-a2dd-4a5b4acca432 | -7.1396 | -59.2938 | 2024-10-10 01:06:44 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 264ed893-bf84-3068-a69d-2090e9500043 | -7.128 | -59.287601 | 2024-10-10 01:06:45 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 877e8ab9-730c-3994-ac61-94028852244e | -7.1298 | -59.295898 | 2024-10-10 01:06:45 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cea9e686-0bf5-34b9-905b-aa72ce9aec78 | -7.1326 | -59.3559 | 2024-10-10 01:06:45 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1f9b27fd-e83e-3047-98a6-7472f992a0ca | -7.1344 | -59.364201 | 2024-10-10 01:06:45 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9590037a-ba40-3699-8930-bc3459e00fc2 | -7.1362 | -59.372501 | 2024-10-10 01:06:45 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| df6b11fd-e6f0-3542-8231-9fb0b9826550 | -7.0781 | -59.246899 | 2024-10-10 01:06:45 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 028db571-2dd5-381e-b244-093d77f92ddc | -7.0799 | -59.2551 | 2024-10-10 01:06:45 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e88fe701-1304-3dd3-a85b-b9cd60bb5142 | -7.0816 | -59.263199 | 2024-10-10 01:06:45 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2e296370-036d-3513-95ef-0f4cac5814e0 | -7.0683 | -59.249001 | 2024-10-10 01:06:45 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 52ee7ccd-3209-3244-88cb-67a342d74ea5 | -7.0701 | -59.257198 | 2024-10-10 01:06:45 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3d1b80c6-a094-31a5-b556-fd0f065051ad | -7.0774 | -59.385201 | 2024-10-10 01:06:46 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a62f1bf4-1dcb-39a3-880c-ea87ef10db80 | -7.0793 | -59.393501 | 2024-10-10 01:06:46 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba4b5cad-8ee5-3127-b2ea-e0850e85c868 | -7.0811 | -59.401798 | 2024-10-10 01:06:46 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 66fb27d1-b3ed-375e-9841-db1352fa0318 | -3.6985 | -44.9146 | 2024-10-10 01:06:46 | METOP-B | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 08dd3202-5742-35fa-9150-92164153e2bf | -3.7063 | -44.946201 | 2024-10-10 01:06:46 | METOP-B | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f0aaf2ba-9fb5-3bf2-b96f-1502bac8ff29 | -7.0676 | -59.387299 | 2024-10-10 01:06:46 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4f7965b2-3f65-3ba9-9b77-b1a237d4d56d | -7.0695 | -59.395699 | 2024-10-10 01:06:46 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 395c3963-4987-3fc2-bf8f-005f7a8f80a7 | -7.0713 | -59.403999 | 2024-10-10 01:06:46 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 33fe5424-989f-35b4-bc77-9de0fec9b928 | -3.6967 | -44.948502 | 2024-10-10 01:06:46 | METOP-B | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2f842298-d0f3-393f-a192-6bbb3c466219 | -7.0597 | -59.3978 | 2024-10-10 01:06:46 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README25.md)
