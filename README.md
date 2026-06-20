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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 949334d5-e79e-3cba-b3a3-c107b669cb10 | -13.1333 | -53.8041 | 2026-06-20 00:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 139.7 |
| a95b9631-11a8-3f29-b507-7a859059fe78 | -11.5984 | -65.1338 | 2026-06-20 00:00:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 80e90169-f2a4-3209-8e17-b994ca6d8379 | -9.0155 | -63.5411 | 2026-06-20 00:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 29a3269a-f58a-367d-86fa-81dd23d7597c | -13.1339 | -53.7625 | 2026-06-20 00:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| e8b72f0f-c46d-3e3c-845e-b50d92ba7f96 | -9.0339 | -63.5593 | 2026-06-20 00:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 1bb3fbe9-14c0-35ea-b640-6c5dde224dfe | -10.7114 | -60.7505 | 2026-06-20 00:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 0e723f6c-3b5c-3dfd-8d63-f8572521da2b | -10.6925 | -60.7709 | 2026-06-20 00:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 2cec5938-858d-3acd-a752-4f540ce74891 | -11.0619 | -52.4812 | 2026-06-20 00:00:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 25b437a7-3cc5-3a1d-8f81-f7eb3811f124 | -5.813 | -45.0799 | 2026-06-20 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 123f3851-8751-3bb0-9a93-37596434b1e0 | -13.1142 | -53.8062 | 2026-06-20 00:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 9e1387cb-351f-3c6e-b5c7-e0d9926280ac | -13.1145 | -53.7854 | 2026-06-20 00:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 136.4 |
| 925e0978-b1c3-3a69-a5be-420d71f43f61 | -13.1874 | -50.3517 | 2026-06-20 00:00:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 1feb9310-2f78-328d-bd3a-a0841d76c97f | -13.1528 | -53.7812 | 2026-06-20 00:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 69156467-c360-3666-8ae3-7b0353acc026 | -9.034 | -63.5404 | 2026-06-20 00:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 70.8 |
| daaa8763-3999-30d6-b860-76d94fb65159 | -13.1336 | -53.7833 | 2026-06-20 00:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 302.6 |
| d8255790-e8d5-3de4-8d5a-6a57672d6996 | -13.2069 | -50.3275 | 2026-06-20 00:00:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 86.2 |
| e9c65877-87c3-3e8f-a34f-f5b996fa7631 | -13.2066 | -50.3492 | 2026-06-20 00:00:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 545e1f72-1394-37be-95d7-a886c0d1c243 | -8.6338 | -47.762 | 2026-06-20 00:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| e7ba4f5c-7540-3a97-9d2f-2e0813d632bf | -8.6341 | -47.74 | 2026-06-20 00:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| c71ab2b4-c305-32d6-8c54-47c701534536 | -10.6926 | -60.7516 | 2026-06-20 00:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 72d40098-7fae-3513-8e5c-34b1b3e7787e | -8.6526 | -47.7602 | 2026-06-20 00:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 8c766f8c-cfe9-3858-b1fb-6137d5d7e35d | -9.0154 | -63.56 | 2026-06-20 00:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| e768ac8d-5863-3a18-af9a-4e6a0771fa23 | -6.3703 | -43.5898 | 2026-06-20 00:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 760e672b-d6ff-30fc-b5b1-c9d66e867b97 | -9.0339 | -63.5593 | 2026-06-20 00:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| b1642023-104f-394b-ad0c-6dedfa218126 | -8.6526 | -47.7602 | 2026-06-20 00:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 3912463d-d240-3aeb-92da-fc5a6a7d1e38 | -12.5531 | -45.0174 | 2026-06-20 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| e7204e03-7b3c-3c37-81fc-83e3f0d9762e | -5.813 | -45.0799 | 2026-06-20 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| a9b76a8e-5419-35a8-8f3d-ff1384fba6ab | -9.0154 | -63.56 | 2026-06-20 00:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 7eb8cac5-3f0c-3227-aee5-179bca1fb3a0 | -13.2066 | -50.3492 | 2026-06-20 00:10:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 0b37a9c9-a6bb-354a-a540-edcaac173723 | -10.6926 | -60.7516 | 2026-06-20 00:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 151eeae5-0242-3c29-9cfc-a26a8b867677 | -9.0155 | -63.5411 | 2026-06-20 00:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 73f21920-f364-3d69-ab40-d4ad4ea33dd0 | -9.034 | -63.5404 | 2026-06-20 00:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 023747bd-c0f0-354e-bdce-b6f079c3fdb9 | -12.5531 | -45.0174 | 2026-06-20 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| b764936b-0ac2-3350-b56b-fa27e5c846fc | -13.2066 | -50.3492 | 2026-06-20 00:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 139.1 |
| f68ff552-0895-321c-97a1-d0dd9683e896 | -13.1333 | -53.8041 | 2026-06-20 00:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 4b5e30f8-00c8-3955-a074-43b2bdb0334d | -13.2069 | -50.3275 | 2026-06-20 00:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 0f6a500a-db7c-3235-80cf-fbc9167b564a | -9.5343 | -40.3282 | 2026-06-20 00:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 67.7 |
| 311445db-cc41-3b1f-9c61-93e2989f25e1 | -8.6526 | -47.7602 | 2026-06-20 00:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 3c16c6db-d85b-355a-8591-8310fa2a74e7 | -9.0154 | -63.56 | 2026-06-20 00:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 208db9d0-b491-3010-a865-41cfd048bbca | -13.1142 | -53.8062 | 2026-06-20 00:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| a34d3edc-1fe1-3d27-9318-de314dff5cf1 | -5.813 | -45.0799 | 2026-06-20 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| b41e39d1-9f1c-3fc8-9f48-f3166d1732f2 | -13.1336 | -53.7833 | 2026-06-20 00:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 143.4 |
| 998d6df7-6912-3632-9cf5-1c519661c4d6 | -13.1145 | -53.7854 | 2026-06-20 00:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 123.7 |
| c1267fd3-5b18-3f80-8382-af1c4e1f7966 | -9.0155 | -63.5411 | 2026-06-20 00:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 59.9 |
| c535ac86-6bbb-3bc0-92e0-963d6ce69e29 | -8.6338 | -47.762 | 2026-06-20 00:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 73da5a3a-0b62-3c39-bf4e-13f34bc64191 | -9.0339 | -63.5593 | 2026-06-20 00:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 43.7 |
| e2b88426-8cad-314a-8bf3-06c1eb74b8e5 | -9.034 | -63.5404 | 2026-06-20 00:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 4a3e6d6c-7399-365c-9a35-fe1552d39991 | -13.1874 | -50.3517 | 2026-06-20 00:20:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 65.5 |
| e7c69f6c-5dd2-3400-b36e-1159bee4983c | -17.32076 | -49.6083 | 2026-06-20 00:22:00 | TERRA_M-M | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 40e99f43-d49c-32a1-b107-5349d1d39216 | -17.35356 | -42.63625 | 2026-06-20 00:22:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 864226a9-0dc0-37bb-a846-abfffb1da5e5 | -9.56301 | -48.67748 | 2026-06-20 00:24:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| baafd982-8fb4-3b09-9d1c-6d54348dcdce | -11.36112 | -55.82069 | 2026-06-20 00:24:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8c4409b7-3816-3483-bcc3-4ca99a93462b | -8.6536 | -47.77354 | 2026-06-20 00:24:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| aa7d150d-a335-3f61-8cf9-6b01443a6f68 | -6.78096 | -46.32594 | 2026-06-20 00:24:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 238737b9-4ac2-3a37-b2fc-9744b5af33da | -13.20593 | -50.35324 | 2026-06-20 00:24:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 22.9 |
| cc5cb2bd-fee0-3cfa-a2e3-b31d5920ac01 | -7.79829 | -46.46268 | 2026-06-20 00:24:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| f8640e48-375a-3213-a83b-ad863911890a | -9.75124 | -47.88164 | 2026-06-20 00:24:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 1a0414de-31a1-340f-aa81-a81ec26d5ad5 | -13.28872 | -45.22091 | 2026-06-20 00:24:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| d801971e-bb29-3bd3-89cc-6f54d4172260 | -12.31335 | -46.73965 | 2026-06-20 00:24:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e10c7e59-5ec0-3732-8f3d-302289e74930 | -13.19715 | -50.35068 | 2026-06-20 00:24:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 56e32747-621a-3049-92b0-4fae25a4b361 | -11.31174 | -54.73439 | 2026-06-20 00:24:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 9498c2b5-58dc-35e5-b18d-d5c70c59e5f0 | -8.6489 | -47.74221 | 2026-06-20 00:24:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 1e9f5806-c3cc-375c-b581-57a14461d441 | -11.63346 | -48.5389 | 2026-06-20 00:24:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| f357a16f-2894-36ed-8889-4fdb780e0d18 | -9.71803 | -48.88252 | 2026-06-20 00:24:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 3e88f5f2-57e1-39c3-8c8e-883a71c4156d | -12.13511 | -48.26757 | 2026-06-20 00:24:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d110dd86-1fac-3d68-8428-7f4439f06303 | -12.54444 | -45.00952 | 2026-06-20 00:24:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| b109e94e-7ad1-39b9-a908-373b5a71ddb6 | -7.80931 | -46.45558 | 2026-06-20 00:24:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a41d7b71-7bcf-38d7-b58f-20e318281410 | -10.76797 | -54.10546 | 2026-06-20 00:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| ccee2401-6a69-363c-8c97-aab80238ff2a | -11.31035 | -54.72395 | 2026-06-20 00:24:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 25.1 |
| f0d06656-530c-30c8-a5bb-a2d417b28f9c | -7.29554 | -55.32013 | 2026-06-20 00:24:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 5bf2e0e7-fad6-3c42-8e00-f571f7cc19ee | -8.98386 | -47.98289 | 2026-06-20 00:24:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| fc93cb7d-fe7b-3fd4-b36d-9a2cf8440058 | -13.12379 | -53.78363 | 2026-06-20 00:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 184.3 |
| 08244181-11d8-3351-a297-2fae87afa637 | -7.63423 | -50.02336 | 2026-06-20 00:24:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 4b9d7777-65f3-3fc1-90c5-b95ecd95ce20 | -8.63741 | -47.74399 | 2026-06-20 00:24:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 23431038-7016-3f95-a2d8-0b480231d57d | -13.5112 | -54.43338 | 2026-06-20 00:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 455935c1-bc30-3fcb-9e7e-5470ac35cc69 | -13.14225 | -53.78101 | 2026-06-20 00:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 10405110-5f4f-3aff-97c1-d87897491f0f | -11.31583 | -54.72753 | 2026-06-20 00:24:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 56d05a5c-381e-3f71-abd0-3796019d6e2c | -13.14481 | -53.80079 | 2026-06-20 00:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1d18f3db-b644-3244-b02c-a90c6497aec8 | -13.14353 | -53.79089 | 2026-06-20 00:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 07b88c13-d04b-3385-abb1-c0c82f289e8b | -12.55004 | -54.58796 | 2026-06-20 00:24:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 64c7165f-4c47-3de3-b3f1-e3ccccf303b3 | -10.7763 | -54.10818 | 2026-06-20 00:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ddb80c2b-9f63-3fff-bb96-307d22bb9e17 | -10.59659 | -44.32314 | 2026-06-20 00:24:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 38.8 |
| f3cc5c24-ecb8-38b1-8437-794ea9127772 | -11.07248 | -52.4808 | 2026-06-20 00:24:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 0cc0cd3b-0143-364e-aa02-8a4c4d3a2d2e | -13.20454 | -50.34368 | 2026-06-20 00:24:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 2659412f-4d49-373f-b39b-bfa4abf60ee1 | -13.11746 | -53.7905 | 2026-06-20 00:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 242bd5ed-3a85-3488-8545-5643694a945f | -13.1343 | -53.79221 | 2026-06-20 00:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 663f83b8-4810-395e-a13a-5fb58c85552e | -12.78515 | -44.49558 | 2026-06-20 00:24:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 5907ba38-3919-360c-a525-d7672f1fbbbf | -14.91164 | -52.00111 | 2026-06-20 00:24:00 | TERRA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6bae10fd-d00e-3ce5-961b-3a0b5aabcdfc | -13.13558 | -53.80212 | 2026-06-20 00:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 051e4da0-9709-35a1-8126-dcc3bc4ae420 | -12.51872 | -48.29691 | 2026-06-20 00:24:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 43.3 |
| e8cc18ab-58dc-3845-8003-8aad13d3e582 | -6.7797 | -46.34167 | 2026-06-20 00:24:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 0e1ad8fc-d282-33da-b95c-923a83aedd6d | -13.12635 | -53.80347 | 2026-06-20 00:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 8821716e-17ab-3fe0-a0bf-6df25b6668cd | -13.13302 | -53.78231 | 2026-06-20 00:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 143.2 |
| af6e0797-60e3-3053-b0ef-38e1c8123a19 | -10.06013 | -48.09494 | 2026-06-20 00:24:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 285956d3-53f5-33bc-a059-f42d12546c17 | -8.98323 | -47.97732 | 2026-06-20 00:24:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 858abebb-7615-39fd-82f2-5b631981044b | -13.50984 | -54.42271 | 2026-06-20 00:24:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6f456615-4271-3397-95be-ac94a71531af | -12.5437 | -45.02649 | 2026-06-20 00:24:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 15b25726-9726-3071-8ed5-f73e37bdefee | -6.78422 | -46.34742 | 2026-06-20 00:24:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 81eb437e-3fba-3fb6-ac08-2d8174609b66 | -10.76926 | -54.1151 | 2026-06-20 00:24:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 913ffa1d-3117-3536-8933-197030d680e8 | -13.11877 | -53.8004 | 2026-06-20 00:24:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |


[Clique aqui para ver as próximas entradas](README2.md)
