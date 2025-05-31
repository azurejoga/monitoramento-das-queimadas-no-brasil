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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 793da72a-2081-349c-9908-f24081efe2e4 | -14.02315 | -55.13924 | 2025-05-31 05:18:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 145a44ac-ab56-3358-a72a-c8dfb10bac81 | -13.94077 | -54.48935 | 2025-05-31 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df914da8-7667-332c-98f3-0f1b49f7f6ad | -14.0174 | -55.11859 | 2025-05-31 05:18:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3bef52ac-58de-3c18-b734-85950d96d858 | -15.8955 | -43.4523 | 2025-05-31 05:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 91.0 |
| ecfc25bd-5b4a-390c-93d2-cebea75117ec | -15.8757 | -43.4566 | 2025-05-31 05:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 7f45f0ea-a457-3659-a5bc-aff209b11f95 | -11.8365 | -51.2854 | 2025-05-31 05:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 0774c94a-b815-3615-85b4-afd6ede97666 | -11.8368 | -51.2641 | 2025-05-31 05:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 8aa0f140-77e1-37d0-9381-9789f8f1a6ab | -23.33401 | -53.06765 | 2025-05-31 05:21:00 | NOAA-20 | TAPIRA | PARANÁ | Brasil | 4126900 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 73cf3c29-5600-3e09-9888-a675d9d10868 | -10.462 | -47.9428 | 2025-05-31 05:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| ffecc35d-be4b-3b45-9d53-9b93fb3988e0 | -11.8368 | -51.2641 | 2025-05-31 05:30:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 6d918404-2f64-333c-ad5b-a963b2d4e9f6 | -15.8955 | -43.4523 | 2025-05-31 05:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 101.5 |
| a07ab38f-afe9-3138-adeb-1b149481e629 | -15.8757 | -43.4566 | 2025-05-31 05:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 2efcec64-a9eb-3690-9760-d4d8fac999bd | -11.8368 | -51.2641 | 2025-05-31 05:40:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 82ca3e2d-4dc7-3459-8a86-be3379ff7dec | -15.8955 | -43.4523 | 2025-05-31 05:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 78.8 |
| e1e6e2f1-4fd7-3e36-b732-bf38331eb4f7 | -15.8757 | -43.4566 | 2025-05-31 05:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 65.4 |
| c5e01284-bb20-3aad-8897-c0e9b3e156ae | -10.462 | -47.9428 | 2025-05-31 05:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| eef89864-7248-3c5b-addd-7775bad24eae | -10.462 | -47.9428 | 2025-05-31 05:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| b4188d1d-9128-370f-bc0f-fb5d960b1999 | -11.8368 | -51.2641 | 2025-05-31 05:50:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 7bc8d4b3-be96-367b-b0fa-e6815c8ec38d | -15.8757 | -43.4566 | 2025-05-31 05:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 1a34fb0e-d132-3ac5-b721-eaf5dc766628 | -15.8955 | -43.4523 | 2025-05-31 05:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 45fb9e9a-a012-3dae-bd16-f15b30a8d1de | -10.65249 | -49.43441 | 2025-05-31 05:59:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f2e37aab-08b3-3902-ac39-1efc8f11e728 | -10.46563 | -47.93495 | 2025-05-31 05:59:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 37bda701-7c82-3dd6-a0e2-1aa79a1bdc7d | -12.01294 | -49.52072 | 2025-05-31 05:59:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| c283e68f-dd78-3f5d-8503-51e67d74c6f5 | -8.46945 | -49.59787 | 2025-05-31 05:59:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ce50cdf4-19f6-3972-9d9c-27e80851beed | -7.23849 | -43.08683 | 2025-05-31 05:59:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 25.3 |
| f4ce740c-1d6d-39b7-81a0-e533d5e03822 | -7.57703 | -45.85971 | 2025-05-31 05:59:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| b8a378b5-255d-3e38-97f6-faf973b52687 | -12.0115 | -49.53085 | 2025-05-31 05:59:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 64227226-4bc8-3256-97da-6068a8eb9071 | -7.31 | -47.02895 | 2025-05-31 05:59:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c7a34b21-dc8f-32b3-bc1d-df938e662073 | -10.65391 | -49.42453 | 2025-05-31 05:59:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 100ee9f3-00fa-3f45-b48a-baca76185149 | -10.45559 | -47.93343 | 2025-05-31 05:59:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 54744b81-beb4-3904-8c9a-cbb6a4513c47 | -12.02226 | -49.52206 | 2025-05-31 05:59:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 40.7 |
| eec3a4dc-be70-3776-8f83-fb2e406cef7b | -10.82436 | -56.93967 | 2025-05-31 05:59:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 6ae2040d-9a35-3c63-bb32-9fab81eac0ca | -11.83295 | -51.27208 | 2025-05-31 05:59:00 | AQUA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 955eaa5a-e6d4-3eb7-a0ea-ac550e27b425 | -10.82942 | -56.9477 | 2025-05-31 05:59:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 67781c42-bb87-3913-b7ff-f1d2dbcaae7d | -10.46401 | -47.94681 | 2025-05-31 05:59:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 685448a4-f9d6-3089-aa28-3baa4a3dd0e4 | -10.72832 | -49.27994 | 2025-05-31 05:59:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f98ad9b3-4a22-34f8-8def-68130dc8f1b3 | -8.47844 | -49.59918 | 2025-05-31 05:59:00 | AQUA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3f1c3364-357b-3e55-a7a7-e8945443f767 | -10.73763 | -49.28129 | 2025-05-31 05:59:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f094adc3-e5b3-3767-bbfa-0ab10d711d52 | -10.45397 | -47.94535 | 2025-05-31 05:59:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 35.1 |
| f2a30e9c-12e2-3a69-9ff8-6c017afc0f6a | -12.0237 | -49.51196 | 2025-05-31 05:59:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 620af46e-013c-33d9-879d-07c7dd1754ef | -11.83429 | -51.26311 | 2025-05-31 05:59:00 | AQUA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| b8af1ea8-f0f2-3050-83e8-0b8b08244f8e | -10.64327 | -49.43304 | 2025-05-31 05:59:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 40.3 |
| fbef34bc-9c74-3cef-91be-5239f8511e86 | -11.82414 | -51.27074 | 2025-05-31 05:59:00 | AQUA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 0a892d3b-5dae-3905-9c58-ebd75b5497f9 | -11.82547 | -51.26178 | 2025-05-31 05:59:00 | AQUA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 4e6aee51-c210-3ac6-a956-ccd2fb2ed31f | -10.64468 | -49.42317 | 2025-05-31 05:59:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 88d64af6-fc17-3aee-88df-0c7b7e075c86 | -11.14294 | -53.93822 | 2025-05-31 05:59:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e6f3bc4f-7df6-3dd5-b605-dc95237136a7 | -15.8757 | -43.4566 | 2025-05-31 06:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 0ab0616d-2c5e-35af-8920-544b34350298 | -11.8368 | -51.2641 | 2025-05-31 06:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 23975169-970c-3572-9002-25960d11b8c6 | -10.462 | -47.9428 | 2025-05-31 06:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 9efc1994-44b1-3589-a6fb-60d023f1aad3 | -15.8955 | -43.4523 | 2025-05-31 06:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 1e0f0035-e03a-3824-9719-a345f932361b | -15.88488 | -43.42656 | 2025-05-31 06:01:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 251f6188-82ee-30f8-9ed9-acaa2b6e8492 | -13.09943 | -45.2785 | 2025-05-31 06:01:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 61518114-4324-3cc2-ba1b-b9851538b0d3 | -15.88151 | -43.45812 | 2025-05-31 06:01:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 77b6b951-9822-3c4a-853f-c1e1ecbd72e5 | -15.8955 | -43.4523 | 2025-05-31 06:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 0dc143ea-3e41-309b-ba66-f07601d46f26 | -11.8368 | -51.2641 | 2025-05-31 06:10:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 49b4690d-b5ff-3fcc-b8d0-7890b1b31f1a | -10.462 | -47.9428 | 2025-05-31 06:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 180eb51b-4d2c-30ce-9b66-d71657ac2c50 | -15.8757 | -43.4566 | 2025-05-31 06:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 70.8 |
| fb11b48f-4069-392e-95b7-257a159ed2af | -10.462 | -47.9428 | 2025-05-31 06:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 4417f6fd-b277-3efe-aac8-3b0e787925c8 | -11.8368 | -51.2641 | 2025-05-31 06:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 794376db-ff41-332e-aa36-de4ed432c295 | -15.8757 | -43.4566 | 2025-05-31 06:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 874dcd55-9ba8-3adf-a4c7-f808523bca59 | -15.8955 | -43.4523 | 2025-05-31 06:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 93.9 |
| b35043b0-00e9-36f6-8730-cd260eaf5d56 | -11.8365 | -51.2854 | 2025-05-31 06:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 4a865ae7-e44d-38be-8ad1-2872942e2202 | -15.8955 | -43.4523 | 2025-05-31 06:30:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 1054ed05-671a-3ea3-9e74-e56b02d7aae6 | -10.462 | -47.9428 | 2025-05-31 06:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 7d2f01e3-76ee-3220-a316-75e48185ecfe | -11.8368 | -51.2641 | 2025-05-31 06:30:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 5f82e134-090e-3384-ae6c-60c1332d0aa2 | -11.8365 | -51.2854 | 2025-05-31 06:30:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 41f3d583-1bd8-326c-a233-7fccb47a0ba9 | -15.8955 | -43.4523 | 2025-05-31 06:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 26943541-c13e-3fb3-a340-df4856519c55 | -10.462 | -47.9428 | 2025-05-31 06:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| f23a8d24-c50c-308e-9f98-d94c63231f60 | -15.8757 | -43.4566 | 2025-05-31 06:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 5277060b-74cf-322e-841e-ae52bb71e4ce | -11.8368 | -51.2641 | 2025-05-31 06:40:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 4848f53b-8837-3282-9cdc-edc364ad0c0f | -15.8955 | -43.4523 | 2025-05-31 06:50:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 94.7 |
| f5ba99d6-916b-3d78-82f8-7a256daa352f | -11.8368 | -51.2641 | 2025-05-31 06:50:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 29b9850a-bd1e-33d9-b85d-591946b40d7b | -11.8365 | -51.2854 | 2025-05-31 06:50:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 3ebb0141-cb8b-3762-b0b5-66316b771258 | -15.8955 | -43.4523 | 2025-05-31 07:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 84.3 |
| bc0923dc-7f44-3cec-a5de-c3aa787ba800 | -10.462 | -47.9428 | 2025-05-31 07:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| b0293cf2-1242-3374-876b-33fdb9c98803 | -11.8365 | -51.2854 | 2025-05-31 07:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |
| c5401bd1-1b66-3a79-b96b-740952c02000 | -11.8368 | -51.2641 | 2025-05-31 07:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 15753992-6a06-3338-8113-69fa6fb4d8b2 | -11.8368 | -51.2641 | 2025-05-31 07:10:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 34f3ce71-4945-3757-89bb-4b6f5f90dcd6 | -11.8368 | -51.2641 | 2025-05-31 07:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| f556cce4-ba11-3424-b479-972af0a67168 | -10.462 | -47.9428 | 2025-05-31 07:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 84827081-809d-3d0a-a1fc-5c2480d5a8c3 | -15.8955 | -43.4523 | 2025-05-31 07:20:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 93a398a2-bffa-3cdd-8e5a-b1cd473ee8ee | -10.462 | -47.9428 | 2025-05-31 07:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| cc4eff30-f982-3de0-b566-59c5519a1db5 | -11.8368 | -51.2641 | 2025-05-31 07:30:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| eb6b855c-e1bd-3f09-8f32-e80db3ae8daf | -11.8365 | -51.2854 | 2025-05-31 07:30:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| b7d4fa9a-f145-30ef-be73-d69ddc677bce | -11.8368 | -51.2641 | 2025-05-31 07:40:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| bd427897-a2a4-3f89-bbb2-99b43e112264 | -11.8365 | -51.2854 | 2025-05-31 07:40:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 13704527-fe6f-3a33-b235-0292113d5464 | -10.462 | -47.9428 | 2025-05-31 07:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 46.4 |
| f9f8ecbd-0127-3e51-aaea-897ba7eb5782 | -11.8368 | -51.2641 | 2025-05-31 07:50:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 109.5 |
| b8319bc6-3eab-3263-811e-2edfa4178f81 | -11.8365 | -51.2854 | 2025-05-31 07:50:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| a5a1a628-f377-35a3-90ec-595484b1345b | -11.8365 | -51.2854 | 2025-05-31 08:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 55.8 |
| cd174800-c1e1-3fd0-bf29-5953f2610234 | -11.8368 | -51.2641 | 2025-05-31 08:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 607cecea-a2bb-39a2-b2d4-0ff5bdc8bc05 | -11.8368 | -51.2641 | 2025-05-31 08:10:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 3562aa91-d00f-37ba-8281-13d4fb72f785 | -11.8365 | -51.2854 | 2025-05-31 08:10:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 84728ce3-a34d-3453-935c-a7d68a1bfa4b | -11.8365 | -51.2854 | 2025-05-31 08:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| d11a8876-5bdd-359b-b2a4-23c456cafee9 | -11.8368 | -51.2641 | 2025-05-31 08:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| d6a2b3d7-3077-3b81-b02d-97054f417565 | -11.8365 | -51.2854 | 2025-05-31 08:30:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| d0d199bc-72d9-34e0-b1d2-da0dab2256f9 | -11.8368 | -51.2641 | 2025-05-31 08:30:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 53f382e4-4942-33b0-a666-8a3748794348 | -11.8368 | -51.2641 | 2025-05-31 08:40:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 00fa3700-8752-38f2-9bc4-3aaa85f86bb3 | -11.8365 | -51.2854 | 2025-05-31 08:40:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| e08ccb71-f6c1-32dd-9567-a8d424821f93 | -11.8365 | -51.2854 | 2025-05-31 08:50:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 53.7 |


[Clique aqui para ver as próximas entradas](README20.md)
