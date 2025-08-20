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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 061010c9-97c3-3a44-aa19-78a9c999bf83 | -8.96317 | -60.50133 | 2025-08-20 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 8e0c54bc-74a9-377a-8723-c90dc5cf13ba | -9.73197 | -63.40479 | 2025-08-20 01:28:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 47f67dcb-af4a-3d1c-b8cf-b113c8ecacbd | -9.21667 | -59.69643 | 2025-08-20 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 639b26f0-526f-3f01-a0b2-2d612199f59b | -8.97218 | -60.50002 | 2025-08-20 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| b375687a-a452-34eb-a644-9ea33f8dd3ae | -9.89076 | -60.28391 | 2025-08-20 01:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 80445f18-a116-3b24-b6d2-cbc3e19333e7 | -7.02091 | -59.67361 | 2025-08-20 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2d283c7c-7392-3140-bede-7e68fdcf457f | -10.46592 | -64.47003 | 2025-08-20 01:28:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9179efd5-326a-3164-8ada-d7276fc18ce4 | -10.24237 | -64.48446 | 2025-08-20 01:28:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8fe13628-b5a4-31c0-96c0-bdc514e932d2 | -8.88758 | -62.40688 | 2025-08-20 01:28:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a1eac316-2249-358d-8ef5-b7a2b48e4681 | -10.4464 | -64.41053 | 2025-08-20 01:28:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 5bb66ee2-6d6c-31b1-be86-870726fc5297 | -8.43412 | -63.87491 | 2025-08-20 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e8e9ca21-de28-3e78-9f2c-0b5b910aee2e | -8.76379 | -64.20258 | 2025-08-20 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 513cfc25-d9e7-33ba-8161-547e85f5e3a0 | -8.8787 | -62.40815 | 2025-08-20 01:28:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 37.5 |
| a8629ebf-7c9a-37d0-acca-90f1f40c4a16 | -6.14055 | -57.71903 | 2025-08-20 01:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| ac418af4-731d-3d64-865b-f82d30e4a4a3 | -10.2522 | -64.48306 | 2025-08-20 01:28:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 690770b1-0cb2-32ae-bc75-ad8ca4181419 | -13.1558 | -54.9151 | 2025-08-20 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| c5c290b7-6282-3148-afc4-c2725bc16331 | -8.034 | -47.6639 | 2025-08-20 01:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 7790fb2f-4983-3f17-af6c-d1a05cc2d935 | -13.3349 | -54.4027 | 2025-08-20 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 68de8721-3ffe-33b5-b294-3efa89f8dbda | -4.912 | -43.2337 | 2025-08-20 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 0c0ec03d-03ca-312e-ab76-8b823d718b0e | -3.982 | -42.516 | 2025-08-20 01:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 50.9 |
| 6f841f8d-4518-340d-ae4c-ba1767906f88 | -12.9778 | -56.8614 | 2025-08-20 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 30af926b-da01-31c5-91af-23de51e8158f | -20.339 | -51.7062 | 2025-08-20 01:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 1851d3c8-ff4e-3bd3-9cd5-011699debb38 | -13.1367 | -54.9171 | 2025-08-20 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| eac9b61f-161d-342c-8e37-d6f40b19bd2f | -15.0002 | -54.8135 | 2025-08-20 01:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 96e7f9f6-9960-342a-9c80-3e44f9c80a4d | -13.1555 | -54.9357 | 2025-08-20 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 54b1d1d2-2398-350a-81b4-f5424ae7c74c | -13.1364 | -54.9376 | 2025-08-20 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| cb24105a-fdda-3c67-b9fc-2999fa1231a0 | 3.411 | -61.07721 | 2025-08-20 01:32:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 76eb29c3-c1bf-356f-a43b-9826aa7dec83 | -20.3385 | -51.7284 | 2025-08-20 01:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 60.2 |
| f73cbdba-1027-35d0-8b35-c2ec7274e84e | -4.912 | -43.2337 | 2025-08-20 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 7dacbe83-b3ae-36e5-8913-9282329bd318 | -3.982 | -42.516 | 2025-08-20 01:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 30.6 |
| fb762bfa-3a64-3f6b-94e2-d4f32e7741a0 | -15.0002 | -54.8135 | 2025-08-20 01:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 24a03663-7b20-3106-9054-412213022091 | -13.1555 | -54.9357 | 2025-08-20 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 2115bdc6-7be2-3547-8e4a-133d15fe88d5 | -13.1558 | -54.9151 | 2025-08-20 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 7d4674a6-74b2-3620-be4b-9c0e88421fb8 | -20.339 | -51.7062 | 2025-08-20 01:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 101.9 |
| b38ad9b8-af3c-3ed6-b19b-2530250f0393 | -13.1367 | -54.9171 | 2025-08-20 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 5c26abe7-75f2-3f2f-8107-78827ef80e35 | -13.1364 | -54.9376 | 2025-08-20 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 4e868001-c251-3f45-830b-f91879051364 | -8.034 | -47.6639 | 2025-08-20 01:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 23b412bf-3159-310c-ab02-fbf74508ac17 | -13.3349 | -54.4027 | 2025-08-20 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 00454b82-f1b1-3ac6-9ac6-0c0b73e97136 | -6.1476 | -57.7215 | 2025-08-20 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 82e627e5-ea78-3393-b236-883ffc5df878 | -13.1367 | -54.9171 | 2025-08-20 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 6d3305e4-2658-3c40-9a62-906db6104d36 | -13.1558 | -54.9151 | 2025-08-20 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 3bafc14c-0272-34b6-8dca-82f81e70919d | -3.982 | -42.516 | 2025-08-20 01:50:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 34.3 |
| dc08c700-5428-37d2-9ca2-68233b2d3729 | -13.1364 | -54.9376 | 2025-08-20 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 02c4762d-9306-3699-a389-9762c3451f1f | -20.3594 | -51.7023 | 2025-08-20 01:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 10712918-2d30-39c6-9ef4-579cd186708d | -13.3349 | -54.4027 | 2025-08-20 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 8edfe22e-f2a4-3cd4-a653-b5c5a3aeddba | -15.0002 | -54.8135 | 2025-08-20 01:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 48.7 |
| f9e5df8b-d86d-3821-8555-d7e90e44bd0f | -6.9605 | -42.8816 | 2025-08-20 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 33.6 |
| f47c16bc-07ab-3cbb-8b76-6632a43deee7 | -4.912 | -43.2337 | 2025-08-20 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| e469413a-ff67-3aca-bd6e-ba58a27daa89 | -13.1555 | -54.9357 | 2025-08-20 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 118.7 |
| b920f8bd-0bfe-3a21-9e3e-0d5cbaa88065 | -6.1476 | -57.7215 | 2025-08-20 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| b4b4bc91-ccc5-3e81-a178-742f11f3c160 | -20.339 | -51.7062 | 2025-08-20 01:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 7b75b90f-e795-3e5e-b6bc-d37de4c0e632 | -8.034 | -47.6639 | 2025-08-20 01:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 911a81df-75de-3409-8980-f35792b06075 | -8.8736 | -62.4067 | 2025-08-20 01:56:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 090f3c22-81fe-3224-af6f-e9b0e261c573 | -13.1509 | -54.940498 | 2025-08-20 01:56:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 34d0b719-7c9e-3ca5-87f6-62fbffcac715 | -12.977 | -56.853401 | 2025-08-20 01:56:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1346f0e8-b327-391b-a6f9-f65735dc5427 | -9.2319 | -60.330399 | 2025-08-20 01:56:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a405a610-3c85-37c1-9377-85948dfc07e5 | -9.2256 | -60.346298 | 2025-08-20 01:56:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b82f2c14-a42e-3de0-8885-ee8859eb75cc | -12.9823 | -56.873402 | 2025-08-20 01:56:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9c080744-9e06-3fc1-af5f-b008e2402cbb | -10.2458 | -64.477798 | 2025-08-20 01:56:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0074626c-a42a-38bc-a47c-c2cec2453f4c | -9.1796 | -59.584099 | 2025-08-20 01:56:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f98fe2b9-99cd-3619-808b-fed3760d1253 | -13.1531 | -54.910999 | 2025-08-20 01:56:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1cfecc25-eba4-3b5d-a2b4-b625722e195b | -8.8857 | -62.414398 | 2025-08-20 01:56:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c92bd772-ebfc-3cc1-9664-c91ff2e9cbf7 | -9.2353 | -60.3438 | 2025-08-20 01:56:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| badad8ec-645d-3b71-b1f2-78341ad16d1a | -13.1605 | -54.937801 | 2025-08-20 01:56:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2f09d3a0-8772-39fb-bb7f-503041cab7d3 | -10.4477 | -64.413696 | 2025-08-20 01:56:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a319dce3-5a58-3d92-8ad1-a8dd35487634 | -15.5297 | -56.064899 | 2025-08-20 01:56:00 | METOP-C | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 806e1da6-8786-36a9-88f7-3b2542532c0d | -9.2357 | -59.6021 | 2025-08-20 01:56:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 33e178fa-e43a-333d-bbae-a0c1c13297f5 | -9.1834 | -59.599201 | 2025-08-20 01:56:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a23d594-3895-33c2-914a-4e60a0023d32 | -20.3486 | -51.729599 | 2025-08-20 01:56:00 | METOP-C | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| de4f6697-befc-3146-a810-0fac01c22aa9 | -8.7641 | -64.196198 | 2025-08-20 01:56:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6fff3633-41d7-3399-880a-3b9b49fa30f1 | -10.2476 | -64.485397 | 2025-08-20 01:56:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 05f7bd6f-78c7-3ab4-89e6-f8de8881b4a3 | -11.6753 | -60.182701 | 2025-08-20 01:56:00 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0ac9ae6d-5314-385e-a354-f373d8ee4a4b | -10.4459 | -64.405998 | 2025-08-20 01:56:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 99a0e718-13f1-3f9e-81d6-cc8504a10c44 | -8.8833 | -62.4044 | 2025-08-20 01:56:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0bf0f7db-2617-3365-ba64-3fb6414c0293 | -6.9333 | -62.882801 | 2025-08-20 01:56:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4402ecb3-728d-3739-b378-fcd406171c98 | -9.2222 | -60.332802 | 2025-08-20 01:56:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 378f1e9a-3446-3834-b12b-8cb2b8fb69aa | -20.339001 | -51.697701 | 2025-08-20 01:56:00 | METOP-C | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fd5f4ffe-3565-3fa1-8e98-0715c452002d | -13.1414 | -54.943199 | 2025-08-20 01:56:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 71eab159-5c8f-3ea5-ae1c-9a490c52eedb | -8.8809 | -62.394299 | 2025-08-20 01:56:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 68bf4309-429d-3dc4-9953-80a4ec6085e0 | -13.1435 | -54.913799 | 2025-08-20 01:56:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e97e71cd-e7e9-31fe-9a95-f0207231d356 | -9.5211 | -60.538399 | 2025-08-20 01:56:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 03031e70-15a0-393d-adaf-f37b2034e869 | -15.0003 | -54.821701 | 2025-08-20 01:56:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e5398877-f80b-352e-9b2e-b5196a0e720d | -8.5659 | -70.059303 | 2025-08-20 01:56:00 | METOP-C | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 014bfaa8-e7ad-3522-96d8-0b62c937ab4b | -13.1558 | -54.9151 | 2025-08-20 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| a2412427-174a-39ab-808e-93a7690f5085 | -6.1476 | -57.7215 | 2025-08-20 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| b6e601f5-520b-34db-896b-07f98de37c11 | -8.034 | -47.6639 | 2025-08-20 02:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 05afa404-6e43-38db-a14c-e38d408ae21e | -20.339 | -51.7062 | 2025-08-20 02:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 737dfcf0-9723-3f9c-bdc9-933b9e356ffc | -13.1364 | -54.9376 | 2025-08-20 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 46f2d325-039c-3d4d-b7ce-a1eab46b9ccb | -13.1555 | -54.9357 | 2025-08-20 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 39b3064a-e9e7-35ca-a6c7-d535a9e62eb2 | -13.3349 | -54.4027 | 2025-08-20 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 754f3922-61d7-31f2-98bb-76487a0b9bf9 | -13.1367 | -54.9171 | 2025-08-20 02:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| bd9549d6-d3c2-3fdc-a82d-4d5090b27152 | -13.1558 | -54.9151 | 2025-08-20 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| d29d2226-5b11-3634-b21d-bd5fe508af9f | -13.1364 | -54.9376 | 2025-08-20 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| c0e7dcb9-0eec-3a4a-9d04-1f019cec0563 | -6.1476 | -57.7215 | 2025-08-20 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| d93813a6-89ac-3eb5-9c59-5eb3a2a5733d | -15.0002 | -54.8135 | 2025-08-20 02:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 47.0 |
| df0af97f-4286-380e-804f-d111b300c74d | -13.1367 | -54.9171 | 2025-08-20 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 251ce07d-6138-3b0c-b10c-9ced2f1d6fbe | -8.034 | -47.6639 | 2025-08-20 02:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 2ca572da-6ad8-33af-b241-adac2cb803f6 | -13.3349 | -54.4027 | 2025-08-20 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 6ecaa56f-6eff-3b66-b66b-d1385d084ea6 | -20.339 | -51.7062 | 2025-08-20 02:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 8142b603-154b-30cf-8513-5fc2e3d4b3bf | -9.1895 | -59.6364 | 2025-08-20 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |


[Clique aqui para ver as próximas entradas](README8.md)
