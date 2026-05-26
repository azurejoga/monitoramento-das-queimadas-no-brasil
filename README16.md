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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 032bd8c7-45ee-37f1-8b34-9966f15d7c06 | -7.1352 | -44.0785 | 2026-05-26 14:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 9f9057b8-8172-3c6a-8e24-d08cfc0b810b | -5.7941 | -45.104 | 2026-05-26 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 29748ce2-eba6-3623-80ae-819d58cae145 | -7.1541 | -44.0767 | 2026-05-26 14:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 0b397f39-c81b-3f62-9670-74fa0d6b1d31 | -6.8939 | -47.4519 | 2026-05-26 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 8a6327fa-ff69-39b7-b667-4a8103945d5d | -7.1355 | -44.0553 | 2026-05-26 14:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 126.2 |
| b1163120-6ffc-31b0-b511-c4f9ae1e05c7 | -7.1543 | -44.0536 | 2026-05-26 14:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 2fd56485-288d-3691-b0c5-1c705aaf9406 | -5.7941 | -45.104 | 2026-05-26 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 06718bb8-1e11-350d-be19-b617b4d2f7f2 | -7.1541 | -44.0767 | 2026-05-26 14:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| eee41223-99b4-3e51-b06a-a619d284ac50 | -7.1355 | -44.0553 | 2026-05-26 14:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 111.7 |
| ac48c300-dc3a-38a2-8a76-496a66688a2d | -7.1352 | -44.0785 | 2026-05-26 14:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 4a549310-07f8-3ab0-8c91-b6a787b10b81 | -10.8706 | -51.2196 | 2026-05-26 14:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| d9523b9b-2aef-3c41-b03a-c87d36f07beb | -11.3584 | -52.9514 | 2026-05-26 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| b3ab6bfb-2e56-3754-8d3f-0dc4811a52bb | -5.7941 | -45.104 | 2026-05-26 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| d2dfb86a-9408-305a-89f0-0bc53269b7ee | -7.2664 | -45.8218 | 2026-05-26 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 600ba657-de4b-37b6-9272-0edef95af2d0 | -7.8194 | -42.0333 | 2026-05-26 14:30:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 176.5 |
| b33312fe-28fc-3562-9f73-97b6557b4cd1 | -7.1352 | -44.0785 | 2026-05-26 14:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 31944445-f5d9-3c1a-86e1-1c606107448c | -7.1355 | -44.0553 | 2026-05-26 14:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 116.3 |
| d77c076a-dc52-3a05-8714-0ad55380dd0e | -11.3584 | -52.9514 | 2026-05-26 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 83386567-6ed9-3ab0-800b-816485e71f28 | -10.8706 | -51.2196 | 2026-05-26 14:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| df53d097-6822-3b9d-8509-77af865bdd75 | -8.925 | -51.8399 | 2026-05-26 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 9babee57-b256-3dd7-8ff8-471457184de8 | -5.7941 | -45.104 | 2026-05-26 14:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| c6ed1e08-f241-3efd-8f84-a40e34cb0ec7 | -7.1352 | -44.0785 | 2026-05-26 14:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 87409708-6f0d-3f8c-b341-ed326bb7a4af | -7.2664 | -45.8218 | 2026-05-26 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 0b143d43-09d8-3ad8-9d18-46ca8eedd0c6 | -11.3584 | -52.9514 | 2026-05-26 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 31309c19-8a48-3b06-b1c2-4cb8bbcd1868 | -7.1355 | -44.0553 | 2026-05-26 14:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 118.8 |
| a0bb37a3-67ca-38e4-be34-7cab56612fc5 | -11.3581 | -52.9722 | 2026-05-26 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| dc4d07c8-1285-368f-b890-e2de9d15f902 | -7.1352 | -44.0785 | 2026-05-26 14:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 103.6 |
| da6738ae-beef-3963-97e2-085a7101aaf5 | -8.925 | -51.8399 | 2026-05-26 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 45c91ba8-25da-3728-81f9-24f48bd04280 | -5.7941 | -45.104 | 2026-05-26 14:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 0e778439-c05d-39b0-9e1c-5dd1d8a40ccd | -10.8706 | -51.2196 | 2026-05-26 14:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 7c48473b-9a76-3313-ac81-193eb8b60f54 | -11.3584 | -52.9514 | 2026-05-26 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 119.8 |
| fbae7589-a81d-3aa2-ab4b-f1f2c75d50ee | -7.1355 | -44.0553 | 2026-05-26 14:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 2c9d5ecd-bb54-3b12-b719-2453c353016b | -6.2121 | -48.5668 | 2026-05-26 15:00:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 8d4adb28-5062-3316-9110-27832c2b4776 | -8.925 | -51.8399 | 2026-05-26 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 05ab3200-0737-3f06-b002-d8f67ad2951b | -8.9436 | -51.8592 | 2026-05-26 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| b016e162-11b8-388e-a559-51165e5c6cf2 | -7.1352 | -44.0785 | 2026-05-26 15:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 67b26419-6ffe-3187-999a-2effde03c775 | -5.7941 | -45.104 | 2026-05-26 15:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 18e365ae-ad79-3cb4-9463-dcbf3a96f408 | -11.3581 | -52.9722 | 2026-05-26 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 4d0a18e6-f8bd-30e3-8610-a9e2e8996371 | -11.3584 | -52.9514 | 2026-05-26 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 987dd3b7-5bb6-3882-94db-b4315268c06c | -7.1355 | -44.0553 | 2026-05-26 15:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 741c3806-e813-3a7e-bd47-4174a36fe1b1 | -10.7391 | -49.7619 | 2026-05-26 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 8145f0e7-a9f4-318b-820c-f832b05e8386 | -6.8939 | -47.4519 | 2026-05-26 15:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 3f6b3c8d-422f-3402-9f4b-19ef50704003 | -11.3581 | -52.9722 | 2026-05-26 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 598aacdb-21a4-38eb-a4da-6972fa053ca2 | -11.3584 | -52.9514 | 2026-05-26 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 152.2 |
| 0f2fcf9b-bc4a-365d-8f85-06a98c1f354f | -7.1355 | -44.0553 | 2026-05-26 15:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 7376caa4-674a-3273-8858-118aa8cfcdde | -5.7941 | -45.104 | 2026-05-26 15:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 7bd173cb-43fc-32de-97dd-75af7ee6c0ae | -7.1352 | -44.0785 | 2026-05-26 15:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 106.4 |
| d65151c7-2eca-32f2-a07f-728e6d8ae4bf | -7.2664 | -45.8218 | 2026-05-26 15:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| ca3d148c-fac7-3349-aa41-2c1680972736 | -7.1355 | -44.0553 | 2026-05-26 15:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 3e511376-dd65-3ed0-be59-d231eb609909 | -10.9095 | -54.1071 | 2026-05-26 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 7449009a-8e4e-3060-8054-bf3c43e05608 | -8.9436 | -51.8592 | 2026-05-26 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| e8169710-01cb-3f01-a522-41432f3f90a5 | -11.3584 | -52.9514 | 2026-05-26 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 164.5 |
| 322c7ac7-3835-35af-9521-7cb0a9855a1f | -5.7941 | -45.104 | 2026-05-26 15:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 32d22e75-9f1d-379d-83b4-703782764bfb | -5.3065 | -43.0663 | 2026-05-26 15:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 45877f47-9343-3332-9236-3f9106195d38 | -7.1352 | -44.0785 | 2026-05-26 15:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| c72b444f-559f-38bd-91e1-6314c9961011 | -8.925 | -51.8399 | 2026-05-26 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 5744ddad-af36-3419-ae1f-36a1bb59ca66 | -5.3065 | -43.0663 | 2026-05-26 15:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 89e076a9-6bc6-301f-ba19-6ccc230357e9 | -11.3584 | -52.9514 | 2026-05-26 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 178.4 |
| 40acc4bd-a59b-3354-a9be-0172617a6fc9 | -7.1352 | -44.0785 | 2026-05-26 15:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| c89b0d90-2a44-3526-a7ca-9096e745baa0 | -10.9095 | -54.1071 | 2026-05-26 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 336e7e35-21db-3275-936c-4569e59fb28b | -10.7391 | -49.7619 | 2026-05-26 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 212e242b-5404-3614-a8ec-ec3d59314084 | -5.7941 | -45.104 | 2026-05-26 15:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 8322dd6b-82e6-3b8f-99c9-55f351b6a1c9 | -10.8706 | -51.2196 | 2026-05-26 15:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| ea7611c4-2af1-3a7d-84a9-bc2cf2755eae | -8.925 | -51.8399 | 2026-05-26 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 372e32f6-c6e9-33c8-b3b0-b91fd2c68acf | -10.7391 | -49.7619 | 2026-05-26 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 18e35f12-372a-3c55-98a0-2bc6443772d0 | -7.1352 | -44.0785 | 2026-05-26 15:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| c460d82e-9962-3f80-aff4-84dbf30774fc | -8.925 | -51.8399 | 2026-05-26 15:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 63f098de-498e-3c8f-9f72-3ff9e40f777a | -5.7941 | -45.104 | 2026-05-26 15:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 2b372a6d-7d77-35b5-91b9-cd0a1c6a170f | -5.3065 | -43.0663 | 2026-05-26 15:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 624c5bb0-11bd-3d6c-bf42-ded9612bb4ae | -11.3584 | -52.9514 | 2026-05-26 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 177.0 |
| 1bc51c8e-1677-3836-930c-49a5731a63ae | -8.9334 | -49.4273 | 2026-05-26 15:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| e8b986e0-2a1d-3504-b197-4a7ba0a59c6c | -8.9436 | -51.8592 | 2026-05-26 15:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 8fda0ff2-8bbc-3b80-beec-1127de503d5e | -5.7941 | -45.104 | 2026-05-26 15:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 92fd2e16-ccd1-3446-b9fe-12affaf20628 | -7.1352 | -44.0785 | 2026-05-26 15:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 9656f049-1148-3a7c-9a6a-4ce53e3a182b | -11.3581 | -52.9722 | 2026-05-26 15:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 3cba4ab4-bfd5-3de9-8dda-72466ce497b6 | -8.9334 | -49.4273 | 2026-05-26 16:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| bb6c4544-35fa-307d-aa05-5df6be91bb85 | -7.1352 | -44.0785 | 2026-05-26 16:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 33b02682-8d27-30ce-b492-8f7599759f35 | -6.2119 | -48.5884 | 2026-05-26 16:00:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 38f4cf2b-8cad-3034-b6b1-22bdb3289982 | -11.3584 | -52.9514 | 2026-05-26 16:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 145.9 |
| 1242f865-72a0-36a6-8161-3ca7fe3f78a4 | -10.9095 | -54.1071 | 2026-05-26 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 388b5754-4584-3b0f-b205-ccb374c2df8a | -7.8194 | -42.0333 | 2026-05-26 16:00:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 232.0 |
| 21241540-a00a-35da-9267-1aff41670053 | -5.7941 | -45.104 | 2026-05-26 16:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| db6e266f-1d54-3a20-a616-12ae21fa3cc6 | -6.2121 | -48.5668 | 2026-05-26 16:00:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 75c42eb1-0ade-382f-962f-2c5dd963f7e5 | -10.7391 | -49.7619 | 2026-05-26 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 121.6 |
| adb6337b-6dac-3f58-95db-5360ac706e40 | -11.3584 | -52.9514 | 2026-05-26 16:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 134.7 |
| 602b4eee-413c-3c44-93ad-d959ea0ce860 | -11.3584 | -52.9514 | 2026-05-26 16:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 164.3 |
| cab247f6-54a5-3205-b58b-322d0422c5ad | -10.9095 | -54.1071 | 2026-05-26 16:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 8c996463-6ee1-3dd7-9da6-d3799b15a96b | -7.1352 | -44.0785 | 2026-05-26 16:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 4c0b529e-4f29-30cc-a027-8bbbd47d1a5f | -11.3581 | -52.9722 | 2026-05-26 16:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| ef8165ef-8f41-35b5-b247-4468c164d300 | -10.8706 | -51.2196 | 2026-05-26 16:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 6a7e52cf-25e5-3ace-8512-2f06883c7448 | -7.0125 | -45.0069 | 2026-05-26 16:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| a2089971-c680-391f-a5b2-ecf70f1a7f8d | -10.7391 | -49.7619 | 2026-05-26 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 6ddc12d8-31ed-350f-b6e6-ffabdff66c04 | -12.4677 | -46.5195 | 2026-05-26 16:30:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| d2a8322e-132c-33d9-a2de-c0a5678fa9ef | -11.3581 | -52.9722 | 2026-05-26 16:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| ea42d0fe-6e5e-34c6-9e07-c021bc312fdf | -7.8381 | -42.0552 | 2026-05-26 16:30:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 83.7 |
| 9e98ccf8-42db-3770-9bc5-845f6ffa305d | -10.7181 | -49.9146 | 2026-05-26 16:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| c6a2c56d-06fa-380c-a206-7d24b64d72fb | -10.9255 | -49.9779 | 2026-05-26 16:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| a160e821-aef6-3790-8d9a-652bfa11a2be | -10.8706 | -51.2196 | 2026-05-26 16:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |


