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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0cc3e02-877c-3090-8c93-4cb9b034b87d | -5.5716 | -44.8927 | 2024-10-17 01:05:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| f338a111-58e2-3327-8479-f4f3448550a8 | -5.9788 | -45.3621 | 2024-10-17 01:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| a367d789-4d0a-31b0-ae44-4df7836d25f2 | -6.7274 | -43.5589 | 2024-10-17 01:05:44 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 7c1213fd-b6dc-3914-8047-8055bf38bc14 | -7.8727 | -45.3593 | 2024-10-17 01:05:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 105.1 |
| cb6f7015-dfea-31fb-ba3c-303916580801 | -7.873 | -45.3366 | 2024-10-17 01:05:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 79e7d8b0-ce7a-3a08-b5e0-187bd4c08b0c | -10.129 | -56.7722 | 2024-10-17 01:06:04 | GOES-16 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 146.4 |
| f31b67ab-82e6-3112-acb3-124d96ad83a1 | -11.7308 | -64.9769 | 2024-10-17 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 8ea95d17-307f-39a5-b62d-ffad3a9e827e | -11.7309 | -64.9579 | 2024-10-17 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 137a40e0-b2df-35d7-bce7-9991dcd98f5e | -11.7495 | -64.976 | 2024-10-17 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 6c4493bf-d2d2-3558-b2be-6542e49e3243 | -11.7497 | -64.9571 | 2024-10-17 01:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 077ced1b-7131-318b-8993-eec9f62df283 | -11.8812 | -64.9513 | 2024-10-17 01:06:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 0a1222fa-bbc3-36e4-8056-c7dbc9487f9d | -11.8814 | -64.9323 | 2024-10-17 01:06:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 102.1 |
| f4e6cc65-d64c-308e-9f2c-8a6b8e72b57f | -11.8815 | -64.9134 | 2024-10-17 01:06:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 4e398106-9019-3f96-bf3f-2c79afec1cdb | -11.9002 | -64.9315 | 2024-10-17 01:06:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| f47b8c48-b06a-3689-b848-e8119a4e6987 | -11.9383 | -64.854 | 2024-10-17 01:06:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| d36455b9-0490-3a7e-983c-5c749cd3a3b4 | -11.9571 | -64.8531 | 2024-10-17 01:06:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 12fe7c62-5e9e-3336-a424-69025d6f4b6a | -12.3613 | -53.1396 | 2024-10-17 01:06:16 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 6236fd5e-503b-3525-a491-a5984d8a23a8 | -17.1664 | -56.8439 | 2024-10-17 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.8 |
| 5250d0e2-a51c-324d-b7dc-252f36ba4248 | -17.1667 | -56.8232 | 2024-10-17 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.7 |
| be4f7bb2-94f0-336d-bff4-2dfb059c9f08 | -17.1671 | -56.8026 | 2024-10-17 01:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 84eac52e-6068-393f-9b56-ebcf6f94f068 | -17.2177 | -57.3102 | 2024-10-17 01:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.3 |
| 6e3f877c-fe2a-3055-a34c-32974cb8775a | -17.2373 | -57.3079 | 2024-10-17 01:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.5 |
| 91c75c94-30a0-3812-a9c7-4829b14cd4ee | -17.8638 | -57.4789 | 2024-10-17 01:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.6 |
| a9058afd-9e39-32ed-8e83-2aea22b77605 | -17.8873 | -57.2496 | 2024-10-17 01:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.4 |
| f16daba7-4b28-3276-943c-af0a6ad9f654 | -17.8246 | -57.4631 | 2024-10-17 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.0 |
| 3fa3a2e9-5cdd-39e6-920e-c833ecc80177 | -17.8444 | -57.4607 | 2024-10-17 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.1 |
| a9bf56dc-2315-31bc-ba09-9847f26e5bf6 | -17.8641 | -57.4583 | 2024-10-17 01:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.2 |
| b7c19f85-6561-330a-8894-ed2a0fdbe50c | -18.254 | -56.6029 | 2024-10-17 01:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.6 |
| a3950c43-a9ef-3a07-9f69-774fad6a6d5e | -23.0098 | -47.171902 | 2024-10-17 01:11:43 | METOP-C | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6891c44f-5bcc-3bea-9345-c17f8a21edb0 | -23.0123 | -47.181801 | 2024-10-17 01:11:43 | METOP-C | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 74e4f2a0-cd4a-3850-904b-67cf8eafa11c | -22.3071 | -48.330399 | 2024-10-17 01:11:58 | METOP-C | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d320ee47-c87a-3eae-8203-64f8673e6acf | -23.0868 | -51.635502 | 2024-10-17 01:11:58 | METOP-C | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b9384363-3a3f-3248-9d0c-72b47945e195 | -20.5895 | -47.547199 | 2024-10-17 01:12:23 | METOP-C | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 50ce1b01-58cf-337f-ac97-ec048d686156 | -20.474701 | -47.5033 | 2024-10-17 01:12:25 | METOP-C | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9dd6d43e-99cb-37e9-bb87-8fc0ad1153f4 | -20.4772 | -47.5135 | 2024-10-17 01:12:25 | METOP-C | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b6e3aad5-6043-3fae-ab07-46f5d6ceffc0 | -20.1994 | -52.1348 | 2024-10-17 01:12:47 | METOP-C | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1e905544-5aa9-3b37-b012-4afca46bdfe4 | -20.201 | -52.142101 | 2024-10-17 01:12:47 | METOP-C | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a9f29359-6f99-30ec-94a2-77e089d44246 | -20.188 | -52.129902 | 2024-10-17 01:12:47 | METOP-C | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a2dd25e3-7d48-3af1-a01d-c321bae46821 | -20.1896 | -52.137199 | 2024-10-17 01:12:47 | METOP-C | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a6594b2e-3355-3fb4-a365-3f8b0c005c08 | -20.249701 | -55.419498 | 2024-10-17 01:12:57 | METOP-C | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 82d62b37-68b4-3fbf-a194-c2bdbb416cfb | -20.2514 | -55.4282 | 2024-10-17 01:12:57 | METOP-C | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 06bc3042-53df-38fe-b23b-6dd86e435431 | -18.2453 | -56.368 | 2024-10-17 01:13:33 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3b704a8c-66bc-378a-80dc-79b9c171bd1c | -18.226299 | -56.325199 | 2024-10-17 01:13:33 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 46f324f7-c41b-30c2-9389-6de81ff7928a | -18.262199 | -56.602699 | 2024-10-17 01:13:33 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7fefd38b-48c7-31cc-82d1-65b2982a2d6f | -18.264099 | -56.612 | 2024-10-17 01:13:33 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4dfea29d-57bc-363b-b0aa-d63e8885d5e6 | -18.252399 | -56.604801 | 2024-10-17 01:13:34 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b3f13d21-a559-3968-8f8f-e6f3b190fac9 | -18.240801 | -56.597698 | 2024-10-17 01:13:34 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ffe9b767-a72a-3c99-96d9-029765175d33 | -18.242701 | -56.606998 | 2024-10-17 01:13:34 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 74eedbcf-0fe1-3c59-ac09-826fb1e9c475 | -18.2446 | -56.616199 | 2024-10-17 01:13:34 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 09493968-8a43-39c0-bdb6-718521881e55 | -12.3773 | -53.112301 | 2024-10-17 01:14:57 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4601fba9-3b5d-30ff-9588-c2a0c003ddb2 | -12.3691 | -53.1217 | 2024-10-17 01:14:57 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| da730538-e9ce-353c-9540-65ede32617d4 | -12.3708 | -53.128799 | 2024-10-17 01:14:57 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9489b647-ebec-3175-93e9-d593a3557654 | -12.3724 | -53.135899 | 2024-10-17 01:14:57 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 850b5092-78d5-3c7d-8253-38a0c47435bb | -12.374 | -53.143101 | 2024-10-17 01:14:57 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b50f5f3-6b4c-38e8-89cf-d5ba9a8501d2 | -12.361 | -53.1311 | 2024-10-17 01:14:57 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 108915a2-6812-3ab3-968c-66524e7190ac | -12.3626 | -53.138199 | 2024-10-17 01:14:57 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7f018179-b224-314a-9bfe-f612103e9527 | -12.3642 | -53.145401 | 2024-10-17 01:14:57 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fe73f9c6-8c65-3ba8-b95b-6f8bc358977c | -12.5071 | -55.191002 | 2024-10-17 01:15:02 | METOP-C | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8b33db8c-43d3-3781-af6e-7b933e54e082 | -12.5087 | -55.198101 | 2024-10-17 01:15:02 | METOP-C | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c8846d8-4298-3fc5-aae0-4bdc737cb549 | -12.2722 | -54.554001 | 2024-10-17 01:15:04 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e3a17979-a797-396b-bd2d-b5a9b4a5d9d8 | -10.8705 | -52.3587 | 2024-10-17 01:15:18 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 678e407a-271a-3dfd-8ab1-fd1ba5f4ba51 | -2.5962 | -48.2634 | 2024-10-17 01:15:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 79efe468-fe12-3b5e-a8d4-1a31ae549882 | -2.6147 | -48.2629 | 2024-10-17 01:15:21 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| a3bda63b-5d6b-32e5-879c-daacfc039aa7 | -2.8333 | -49.1562 | 2024-10-17 01:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| a57fe732-9cbb-36b5-a4a6-a840b6c54e24 | -2.9673 | -48.0147 | 2024-10-17 01:15:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 158a2e77-0ba4-35be-b76b-86de2efde980 | -2.9674 | -47.9931 | 2024-10-17 01:15:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 169.2 |
| 20b0237e-081f-3afc-bd03-533304aaad1f | -2.9859 | -47.9925 | 2024-10-17 01:15:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| fa1d3e37-5a76-3ac5-a017-b9ab4abadd0f | -3.2225 | -48.9306 | 2024-10-17 01:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 4a2a7ffb-fef9-38ea-b20f-0cbe1b9f60a1 | -3.2226 | -48.9092 | 2024-10-17 01:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| bac6b5ba-8e62-3e61-92b4-476439fbe30a | -3.2945 | -45.402 | 2024-10-17 01:15:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 213ddc32-e2de-3a6b-b3d3-8675b677f04f | -3.5087 | -51.0914 | 2024-10-17 01:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 5ff927cc-606d-382b-b298-8749591b9524 | -3.5086 | -51.1122 | 2024-10-17 01:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 1f4afffd-0289-34f6-a64f-9c66b9a4540b | -10.2092 | -51.6562 | 2024-10-17 01:15:26 | METOP-C | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e3d1a42-799c-33f5-893d-4c06965c21bf | -3.7007 | -45.9223 | 2024-10-17 01:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 96.8 |
| c002900e-18a3-3bc4-a86f-4c5321e81180 | -3.7009 | -45.9 | 2024-10-17 01:15:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 4f444902-ee43-3f8b-909c-ff6922d12a37 | -10.1997 | -52.316799 | 2024-10-17 01:15:29 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f765f4fe-6815-350b-8973-43de374d1333 | -10.2015 | -52.324501 | 2024-10-17 01:15:29 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0c9177b4-4618-38ee-86f9-b40057ab3b8b | -10.19 | -52.319099 | 2024-10-17 01:15:29 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e99dd6c-4f63-3145-8da8-3e3b7133e0e7 | -10.1918 | -52.326801 | 2024-10-17 01:15:29 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa5a0603-b9be-3a2f-ab9b-98b16652a8a9 | -5.5716 | -44.8927 | 2024-10-17 01:15:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 7f4924f0-b49d-3399-aaf7-6dadd402aaeb | -7.8761 | -45.345402 | 2024-10-17 01:15:39 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d7e149f2-8be8-3b84-aa0d-cea153b9baf5 | -7.8665 | -45.3479 | 2024-10-17 01:15:39 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 130848ec-4773-3c56-a92f-12eb21d2d54a | -7.8721 | -45.369801 | 2024-10-17 01:15:39 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 67e04d9f-4fcb-3c50-b443-506c4ba2fce6 | -5.9788 | -45.3621 | 2024-10-17 01:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| b1b8206d-c11a-30a7-a10a-6d741d9a11aa | -6.7274 | -43.5589 | 2024-10-17 01:15:44 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 142.6 |
| b4e21e1b-dbdf-3494-af2b-cec4b2ada5af | -10.2927 | -56.9888 | 2024-10-17 01:15:44 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 68981389-bbe4-340f-8190-4cf847bbf22c | -10.2944 | -56.996601 | 2024-10-17 01:15:44 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a1a2bcd2-fc53-3dca-a604-2a57288aef82 | -10.2961 | -57.004299 | 2024-10-17 01:15:44 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9482b259-1987-32c2-9252-3aa0220a5db2 | -10.131 | -56.767899 | 2024-10-17 01:15:46 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7f55faeb-6012-30cc-b5e6-a198221e76db | -10.1327 | -56.775398 | 2024-10-17 01:15:46 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c27d1717-c79f-3d64-9385-30f9f5a3c50c | -10.1343 | -56.783001 | 2024-10-17 01:15:46 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a46374c9-1895-3f23-b5c1-9a480679be5e | -10.1212 | -56.7701 | 2024-10-17 01:15:46 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f43426b7-5457-362e-b990-3b210eab3ec0 | -10.1229 | -56.777599 | 2024-10-17 01:15:46 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 35889bb0-cf72-319e-964e-f1c735d28ba5 | -7.8539 | -45.3611 | 2024-10-17 01:15:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 4379eafd-df73-3c00-89ad-01a77691892c | -7.8727 | -45.3593 | 2024-10-17 01:15:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| d8c258d6-3e35-39d4-b86b-923e5b3a9244 | -6.7385 | -43.555698 | 2024-10-17 01:15:50 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ada3743f-4d4d-3bb5-b522-543147c0368e | -6.7289 | -43.558201 | 2024-10-17 01:15:50 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b210db61-d56b-34f5-8949-c564488b3965 | -6.7367 | -43.588501 | 2024-10-17 01:15:50 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a077660c-a764-3c9e-971f-f20620210aef | -9.9158 | -57.517899 | 2024-10-17 01:15:52 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 04369911-7c54-376d-b2b5-a5569c539e1c | -9.9176 | -57.526001 | 2024-10-17 01:15:52 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
