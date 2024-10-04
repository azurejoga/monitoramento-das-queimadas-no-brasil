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

## Dados Diários - Página 180

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c0a27da-fee2-3b76-8a0e-bd68b269042e | -16.99176 | -56.77111 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 3d28760e-797f-3ca7-853b-b293f56bc715 | -16.99143 | -56.77187 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| e46a5e03-b130-3b0d-99cd-bd1cd65084c7 | -16.99124 | -56.77671 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| c5de32d7-746a-37b3-a7f4-9f38c2232e49 | -16.99087 | -56.77745 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 2b86556e-8fa0-3664-8219-2fa119837fc0 | -16.98528 | -56.77034 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d7b3f2a1-a693-3492-89e3-87f00cd7956d | -16.98494 | -56.77113 | 2024-10-04 05:53:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 4ed3bfaf-e666-3896-80d7-f35db0aa4e1b | -18.89699 | -57.70065 | 2024-10-04 05:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b37eb436-8e6a-385a-bc8b-54d142efc8f3 | -18.8965 | -57.70582 | 2024-10-04 05:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 390291bb-19be-3abc-bde1-08af56b3887c | -18.89462 | -57.70467 | 2024-10-04 05:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 82f213c8-fa4a-356d-b987-fdc481831d7d | -18.89025 | -57.70513 | 2024-10-04 05:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0d6b2ac5-9c49-368c-bc70-ae854a08e04a | -18.88836 | -57.70395 | 2024-10-04 05:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4c0a17f3-60c1-345f-bb11-7cd219bc9545 | -18.88399 | -57.70442 | 2024-10-04 05:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4086db1f-f175-396b-81f8-aae2b064e791 | -18.69276 | -57.28902 | 2024-10-04 05:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| da5e7a58-0cd1-3083-b360-ae1c2e86a91c | -18.69226 | -57.29449 | 2024-10-04 05:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 61e845fb-69b4-3df9-8237-0e6d06882f53 | -16.58349 | -58.21104 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 58eaf8d0-3efe-3f8b-ba6b-58eb96083ba2 | -16.58256 | -58.21999 | 2024-10-04 05:53:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 67bcdece-77f9-38e7-aa2c-182d314c2607 | -15.36531 | -58.15003 | 2024-10-04 05:53:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ed79b7b-a9f5-3041-aa51-992dc110f9d3 | -15.36447 | -58.15115 | 2024-10-04 05:53:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b5e0f2e-b293-36c4-9cd8-85a9db302e7f | -15.35899 | -58.15359 | 2024-10-04 05:53:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab88a72e-980b-31dd-84f8-04974fcee0b2 | -15.35818 | -58.15467 | 2024-10-04 05:53:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01e4351b-fa25-3f86-b2e2-5f9204e00aba | -15.35323 | -58.15207 | 2024-10-04 05:53:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e469b8e-dcdf-39ff-a02f-f6259ad84030 | -15.1251 | -59.02615 | 2024-10-04 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3879168d-96f5-3d14-9feb-5078614af953 | -14.17629 | -60.25452 | 2024-10-04 05:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bec451d8-108f-3f42-a45f-948fe1e6c2a7 | -14.17594 | -60.25748 | 2024-10-04 05:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d1720c0-3d0a-30f1-954b-be8d01064320 | -14.17559 | -60.26044 | 2024-10-04 05:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12f9baa4-d1c5-3be3-8cd8-1f50b6432a3d | -11.08 | -46.55 | 2024-10-04 06:04:21 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ae79e890-a6ee-3a53-a6bb-d073adf2e272 | -11.08 | -46.5 | 2024-10-04 06:04:21 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d979d165-e955-3a55-94a3-d9873eb8a4c2 | -11.08 | -46.45 | 2024-10-04 06:04:21 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 67c7a2b5-ab5f-30b0-83e0-fa59692a69ea | -11.11 | -46.56 | 2024-10-04 06:04:21 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4ba18116-f72f-344d-b7d0-17dbcc2b52e9 | -11.11 | -46.51 | 2024-10-04 06:04:21 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7ff8dcf1-5c11-3e8d-bd37-babde932727e | -3.37 | -42.31 | 2024-10-04 06:05:08 | MSG-03 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 89f6d8ca-a58d-32ee-9823-167af2d98f48 | -3.37 | -42.27 | 2024-10-04 06:05:08 | MSG-03 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cb9c10a2-12d8-30a9-8ed3-a441c82b1f12 | -3.29 | -50.43 | 2024-10-04 06:05:08 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc9f716e-2cbb-3b59-bf1f-2a636311dada | -6.8741 | -59.03273 | 2024-10-04 06:08:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0172a144-5b36-34f1-b4cc-181553d27450 | -7.14509 | -59.31963 | 2024-10-04 06:08:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| db328222-3e28-3fe5-b1f9-8ad222b598a0 | -7.13693 | -59.3117 | 2024-10-04 06:08:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 41ef1fc6-4b67-361b-9e85-8cec4cb2a220 | -7.05637 | -59.29966 | 2024-10-04 06:08:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3c7fbf9a-04ff-3e60-b42d-e0c9e4ceb75d | -6.72306 | -59.12335 | 2024-10-04 06:08:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 651d60da-06ac-3c30-98bf-727d4972fcbd | -6.71276 | -59.13102 | 2024-10-04 06:08:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d9e18905-8d30-3d3c-9cdd-c3050be72950 | -4.09953 | -48.481 | 2024-10-04 06:08:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| a36e648f-a955-346e-a2d1-488a6adbf39d | -4.09216 | -48.47209 | 2024-10-04 06:08:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 402fe3c1-e6c8-370c-8bdf-fd9a7f1ba573 | -4.08758 | -48.50454 | 2024-10-04 06:08:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| a6d047a7-d7d7-378f-8ea1-2694cac17631 | -4.08354 | -48.4783 | 2024-10-04 06:08:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| d46b79c9-1ace-36c6-a9f7-f0cdd0923951 | -3.31309 | -50.43574 | 2024-10-04 06:08:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 23b6cc08-a8d1-3cbe-8f2d-599d533151cd | -3.30995 | -50.45804 | 2024-10-04 06:08:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 348.2 |
| 748aa6db-7af6-3b1a-9c72-d33ae3bd3829 | -3.29951 | -50.43385 | 2024-10-04 06:08:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 310713bf-bf25-3976-91ef-fe35d3e21285 | -3.29641 | -50.45604 | 2024-10-04 06:08:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| d5b8eecc-fdc5-3530-b411-8ff1e54c8eee | -3.28953 | -50.44796 | 2024-10-04 06:08:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 7e65cdb6-cb8c-344e-8750-c1911c75375c | -3.24811 | -50.3504 | 2024-10-04 06:08:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| f5a6089e-d8a1-3e9c-bb02-63fab125b9dd | -3.24489 | -50.37306 | 2024-10-04 06:08:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| bda4eebb-e713-3091-aed6-7104ea789428 | -3.49782 | -50.8062 | 2024-10-04 06:08:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 517f6e67-72da-3a8f-8752-6868814199a6 | -3.49496 | -50.81078 | 2024-10-04 06:08:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 11a28ec9-8686-3cab-a28f-4c423fd5dc7e | -2.89507 | -50.70651 | 2024-10-04 06:08:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 2e6b62f5-02b5-330a-a768-2befc4120de7 | -2.97666 | -53.72868 | 2024-10-04 06:08:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 63f1237d-ac0c-3f71-b5ee-8956e2bb6168 | -16.60426 | -57.17588 | 2024-10-04 06:10:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.5 |
| a57a5cd5-cf67-3855-b730-0b1c476705a3 | -16.6027 | -57.18769 | 2024-10-04 06:10:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.3 |
| 359d8cd8-f033-3f0a-9cbe-4559c65a4038 | -16.59271 | -57.18629 | 2024-10-04 06:10:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| d95e3f7b-49a3-3999-9fe9-0cb238a79bd5 | -16.56891 | -57.29026 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| d7c1bb92-b346-35cb-9cd1-085193acadc5 | -16.42276 | -57.38636 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 0d6c459b-69c5-317a-81bf-717dc346285e | -16.42122 | -57.39774 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 10ae0a9f-2b98-3601-baeb-cf16dccc198b | -16.41293 | -57.38498 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| cbba4658-1bfc-377a-bf2f-e26312323622 | -16.41139 | -57.39638 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 005dba7e-b6c6-3c02-8707-cdb808c45f4d | -16.08766 | -57.52839 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7035f71e-d064-305e-85b3-f2393add933c | -16.07796 | -57.52703 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d50dfd85-54e6-349a-9fe9-3004574fa2c0 | -15.7958 | -57.33621 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 162261e3-1fa5-3455-bca8-fdff03e68a20 | -15.79262 | -57.35937 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 14f2959f-e195-314e-b38e-95343dfe0cf1 | -15.71399 | -57.42696 | 2024-10-04 06:10:00 | AQUA_M-M | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 42d3a6bf-d441-3b42-929c-ce06d18e0cf2 | -15.6573 | -57.39045 | 2024-10-04 06:10:00 | AQUA_M-M | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e35e00a0-b07a-3255-bbde-d51787d5fb15 | -15.65584 | -57.40123 | 2024-10-04 06:10:00 | AQUA_M-M | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 53a6ecda-6ad8-33b6-a208-c59ceecf9259 | -17.11435 | -56.77869 | 2024-10-04 06:10:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.7 |
| 16aeeee5-7b6c-3a20-bc2e-0ca3e77f8360 | -17.11271 | -56.79142 | 2024-10-04 06:10:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| ba1548ae-b31c-3323-a240-0a5836e97105 | -17.04258 | -56.71014 | 2024-10-04 06:10:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 7e7fc686-7d4e-3be6-b9ff-4ce96acfae71 | -17.01855 | -56.73292 | 2024-10-04 06:10:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 38.8 |
| 802a2acd-adde-3f4d-bce8-c50031b06912 | -17.01691 | -56.74569 | 2024-10-04 06:10:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.3 |
| e378ca75-6150-3e7b-910e-69c7434558f3 | -17.00657 | -56.74427 | 2024-10-04 06:10:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 37.9 |
| d4c6f27a-f523-3a92-8a7f-3eb508cdcfe6 | -17.00332 | -56.76974 | 2024-10-04 06:10:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.0 |
| 6e16678d-65a1-3849-880b-ba1f00615ee3 | -16.99601 | -56.76313 | 2024-10-04 06:10:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.9 |
| 43a2d285-041f-3003-8f46-b57081b1fd61 | -16.99431 | -56.77582 | 2024-10-04 06:10:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.1 |
| 4168b27f-6a89-3151-8e33-d2fae8276a5e | -16.99299 | -56.76833 | 2024-10-04 06:10:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.4 |
| 088b2e42-4eed-3563-bce0-9d7d3d7e6d8c | -16.92144 | -57.7012 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 57a1fb87-a941-39bb-b4fc-208267d46c0e | -16.85064 | -57.46674 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.7 |
| cf2ee135-607c-36c0-84f8-e4cf8baf6b9e | -16.79274 | -57.82343 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 001cde77-4c53-3c04-9eb3-2ee00007800c | -16.7407 | -57.45605 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| eedd122c-7108-3c63-a03b-f6aff66c8240 | -16.73918 | -57.46748 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.4 |
| d06c686c-f71c-3129-b3b3-dbd60dbb8f0f | -16.68856 | -57.4546 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.3 |
| e01504d4-1c49-33d5-b71e-f84a83c7bc54 | -16.68702 | -57.466 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.5 |
| a313de42-0888-34ea-8100-ea66d985e6cd | -16.67873 | -57.45321 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 890b7a6d-c839-35d4-89df-8680884afa3b | -17.19283 | -57.35037 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.4 |
| 680e7609-1d23-372b-9703-572415bf56a9 | -17.19216 | -57.35558 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.8 |
| 6db76e6a-489e-3afb-91e7-45441a2e8e71 | -17.1913 | -57.36214 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 7c86bbdc-1e5b-33c5-a9f4-d004bb06e87c | -17.17744 | -57.38935 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 4369411b-c330-3458-b29c-87c5f9c43daa | -17.17586 | -57.40103 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.9 |
| 677e6f29-fdb7-344c-b6b2-98fbda9dc815 | -17.15915 | -57.37486 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| 95d84466-a245-38bb-830c-83d741e6613f | -17.15758 | -57.38656 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.5 |
| 29b0a215-abc7-3ce6-8215-522799029296 | -17.15601 | -57.39824 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.3 |
| 2e5bd7f7-6454-309f-ab2c-0580a7a8cdca | -17.14453 | -57.4085 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| 7493a1f6-2c88-3ac9-b253-8e5cc52dfaf3 | -18.69902 | -57.2891 | 2024-10-04 06:10:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 865501ba-9805-371c-be4c-ddfb9efcdcc0 | -16.58557 | -58.205 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 990d6840-caa2-3998-b009-d61d48a9e3b7 | -16.58412 | -58.21543 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 15fa0d5f-5d11-3266-a70c-3d2da78ed31c | -16.53568 | -58.21896 | 2024-10-04 06:10:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |


[Clique aqui para ver as próximas entradas](README181.md)
