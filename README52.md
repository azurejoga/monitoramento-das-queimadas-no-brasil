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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7b2df89-7993-353d-904b-c403bf8d5ef5 | -8.77777 | -50.07525 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f62c821-71c6-3eb5-810b-a27d9a3cbe73 | -6.33996 | -55.87998 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 952a098b-ff82-3b81-b0e6-9ee0a0cf83eb | -9.45599 | -51.71221 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d8de3e08-ff5c-3d16-bd0e-f7788bd0dbbf | -7.35601 | -55.16477 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bf7b203-1832-3dc5-97f2-79e94e561867 | -9.22281 | -51.57443 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b510c18-08bc-38e2-bced-61b8e62e75c1 | -4.84829 | -45.40442 | 2026-08-28 05:10:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 95c67133-c1ee-3db6-b4f1-50a4471fb5b9 | -6.25139 | -53.36213 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32811dfb-6bfd-3b43-bbe6-f7c4912b67c6 | -6.27488 | -53.34965 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a68d41da-81e9-3a5d-954f-374752d08c97 | -8.81131 | -50.0872 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c6164a3-3537-3e78-b6a1-4ba70d7e9366 | -5.87886 | -52.18583 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8ea0507-b3ed-36b7-8334-c8d5701c5b3f | -6.279 | -53.34624 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91ad7ea0-5bc6-300d-abff-f214d703eff0 | -6.83703 | -55.61433 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35135f4a-5968-3ed2-aa4f-4034bbfc5616 | -9.46608 | -51.69908 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52cec4e6-5850-3c08-9bb7-9b6eb9e8b4ae | -9.2826 | -57.07358 | 2026-08-28 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f39e0256-8bca-3821-abc8-c05b981edba0 | -8.24418 | -54.97667 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ac94190-7505-3d62-9db8-5dd5512b0f97 | -6.52711 | -55.25153 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1314f1aa-b2dc-3b2c-80c6-394b72f5cf9e | -6.17798 | -55.46409 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9964ff0-3cb2-3b50-b7b1-dadeb7447fd5 | -8.77403 | -49.94391 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5255b873-8d43-3485-a0bf-67d47c939667 | -8.16153 | -54.95291 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ef6db13-e380-31e4-9b43-2d787cc15d18 | -5.26247 | -50.96866 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 807b26e3-d51e-38d4-b4b4-74f6ccf08344 | -6.19226 | -55.41655 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ae99593-c529-3e8f-8cf6-cb6499cfbd8c | -8.08308 | -45.85937 | 2026-08-28 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 211b2e12-87b5-3fca-bf65-c52e5c536065 | -7.25928 | -45.8708 | 2026-08-28 05:10:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b8f3068e-3752-3152-a91b-d85d7ff978d1 | -5.99067 | -55.72557 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b5d169d-df04-3643-9211-42ad3c1b4078 | -8.59295 | -54.78313 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 804607a5-0be6-324d-a0bc-5338508344c9 | -6.42328 | -54.93651 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10a287e0-41a3-3b5a-b0ad-cb1c1d6525d0 | -7.37788 | -55.14984 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f34f311a-6de2-392d-8aaf-7bc27b22e649 | -6.84773 | -47.45465 | 2026-08-28 05:10:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a008b862-a7d8-3af8-93ae-ea75e651e972 | -8.59578 | -54.78735 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3e028761-e380-3b5a-9e3d-8b8a7ce3fd70 | -7.26039 | -45.86264 | 2026-08-28 05:10:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 00150ae7-da6c-36d5-ab4b-17c9d5fbafa5 | -9.22426 | -51.53502 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78515f54-3525-3a3d-9e27-b4960f7ead95 | -8.21938 | -54.95844 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 41d8b5f6-4eb1-3067-83d6-328f67762895 | -5.29095 | -50.94157 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5f39b38-0fcc-38bc-b22b-be5c36c7c3db | -6.64617 | -53.19067 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8e8a445-4d49-3c7c-9a3a-c82cb538af6b | -8.08363 | -45.85516 | 2026-08-28 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f22c7b9-9c55-3618-9a3f-a6e632ba4ad5 | -6.83738 | -52.49744 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5bed9dbb-a1d7-3ec7-926d-9679d9b0c359 | -6.64679 | -53.18663 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15ba25ea-bddc-3d46-a4e9-fb70ccc87226 | -6.97338 | -55.63255 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 297e540a-c672-3c6f-b39e-b14d07129372 | -8.01002 | -48.40991 | 2026-08-28 05:10:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3dfc494-e962-3b49-8b2f-62ca898d69e7 | -6.2796 | -53.3423 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14f4b83b-5535-3575-8764-fdbee20746ec | -7.57563 | -61.30301 | 2026-08-28 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d6764ec-776a-363b-aaf3-ced3288e1aac | -6.23709 | -53.4799 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 871f9746-5e8b-34ae-b712-1c4d93364031 | -6.59645 | -55.43782 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bd0bb6a-fd48-39fc-b85b-de54af262cfd | -6.59313 | -55.4373 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae8f7482-22b0-3c1e-a7f4-d9316a97c86c | -5.98591 | -52.1947 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82e0ae68-429d-3394-9607-0e2961fbe008 | -9.43342 | -51.69817 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b94de5bb-25fa-310a-8349-a38cad3a0c9d | -9.42941 | -51.69761 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f080a7bd-4860-31b2-bc61-d2ded2c90b59 | -6.59259 | -55.44078 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1652a1d8-fe53-38ad-87f8-18a9f66021c8 | -10.89055 | -46.63571 | 2026-08-28 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2bd40c28-16e9-38cb-9c8b-9391bfbcc0c8 | -8.61925 | -50.01836 | 2026-08-28 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6aa111f8-edc4-3506-a6ae-95af9fa54f70 | -8.59181 | -54.7905 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2903728a-cea1-3b33-90b4-5294f6ec8ce9 | -7.58247 | -61.31139 | 2026-08-28 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8290548c-b726-30c0-8859-b0f50db74751 | -8.0896 | -45.80958 | 2026-08-28 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 670d35e8-16af-3d29-868d-c6915513fd08 | -4.84885 | -45.40045 | 2026-08-28 05:10:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 33c0119b-aefa-3734-abbc-82fae724c85e | -7.49645 | -55.28439 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6dacf5ba-11e5-357e-8568-fe2eea80131d | -6.23812 | -55.47 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af1187fa-fb33-3f64-ae7d-6fad979ee8e7 | -7.57623 | -61.2995 | 2026-08-28 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9ae3821c-3c24-38b7-b613-fef6ea0f4846 | -6.27016 | -53.35699 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc58a2fd-397a-3f0b-8478-c986cda8561e | -6.75577 | -46.13946 | 2026-08-28 05:10:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72c211f3-c10b-3fb3-a6dd-7d6ee08e03d3 | -6.13948 | -53.52504 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87889f62-1f75-3358-aa46-70e225198cbe | -7.4959 | -55.28791 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7954460-1265-3e6a-9e55-4fc9e898f253 | -9.65989 | -48.29695 | 2026-08-28 05:10:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3bf944e1-25f9-32f4-bba3-4650474ec5cd | -5.82538 | -50.21791 | 2026-08-28 05:10:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61ab13b2-3473-351e-9f34-06e994b30ffb | -9.45458 | -51.57834 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fde96380-0290-3a50-b680-73906ac2e8ea | -6.26341 | -55.41707 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5c01a15-1d83-3151-979a-9d3190e0aa1f | -6.12784 | -53.5312 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6ccf5a3-59c6-36ad-aad0-a7515bd1b7b4 | -5.86988 | -49.77549 | 2026-08-28 05:10:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06b56254-345b-33e5-bf2f-7f4cc1c30b13 | -6.43801 | -55.77507 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7351fa40-21e6-31e7-afba-369aa91c9b0c | -9.28204 | -57.07707 | 2026-08-28 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27b6f8b6-0283-3a9b-90af-d9422309315a | -4.56275 | -56.13927 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23125efc-9550-3c27-b743-a1212eba2ca9 | -8.58616 | -54.75949 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58e36afc-cf84-3ebc-b8a7-24bfed4081b4 | -8.24644 | -54.98432 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bba2ebe-981e-3039-a209-4dc4c923eb7c | -7.25515 | -45.85788 | 2026-08-28 05:10:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| f6943194-b092-3d90-9839-8a225d9562b1 | -4.84997 | -45.39258 | 2026-08-28 05:10:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f8ff17d3-5ee8-3402-bbdf-543a3dd4e65d | -9.96593 | -53.93671 | 2026-08-28 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 0866ed79-54a2-38a3-a096-33067b425f62 | -3.94229 | -54.8429 | 2026-08-28 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b50c4a9-bb06-3915-82a9-6accb11f6fcb | -7.8792 | -46.10108 | 2026-08-28 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3a7bb55b-19b9-3796-a88e-ea2821936fac | -8.08485 | -45.80859 | 2026-08-28 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c61177fa-fe57-35e1-8337-f7abe3204848 | -8.60664 | -54.71722 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2559c7d8-b666-3e03-a21e-34e213b5a344 | -5.9846 | -55.72107 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b7e1b720-eab4-3f73-9022-f7b884915a4e | -8.58957 | -54.76001 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88e89d93-51ec-3ec5-a899-3d4b2029138b | -7.2746 | -45.35346 | 2026-08-28 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0bbf0e9-6da4-3b6e-aaeb-4de578223fb3 | -8.53269 | -55.28172 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfe79374-8672-3b50-8f95-909340e8d396 | -7.07047 | -46.26433 | 2026-08-28 05:10:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd2d75c2-7db2-357b-b778-cf074f58f288 | -6.17494 | -57.79055 | 2026-08-28 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| edf4ece6-33df-30d4-a333-5fe39ce0bb2d | -8.22275 | -54.95898 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 73ea3d73-3738-323f-a8f4-5054c667d650 | -6.12377 | -53.53448 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1819a80b-b0ca-3192-a236-15062ebac784 | -6.24475 | -55.47105 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77786a63-f68e-3c85-a574-b4afe5bd2992 | -5.47564 | -45.1189 | 2026-08-28 05:10:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 633a6695-5e48-3dbc-9565-fcfad141680d | -6.83976 | -56.45621 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fef72590-ef85-3d09-ac0f-50828deade1f | -6.51932 | -55.23599 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 318651ad-e9fe-305f-b46b-1e3f409bf4af | -8.17212 | -46.17103 | 2026-08-28 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac307e17-a660-3468-a0f7-10b7980d8510 | -8.50646 | -55.33984 | 2026-08-28 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 774521d7-6d94-378f-9833-e269ee918772 | -7.58186 | -61.31493 | 2026-08-28 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86d26573-b7b9-3dd7-b98f-b8625ced63a0 | -8.11072 | -51.65975 | 2026-08-28 05:10:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5489913-dda7-3bbb-bed0-ab1addd9cb23 | -9.40419 | -51.63687 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ef62d2a-d657-3708-8cbe-ade941600d61 | -9.16464 | -49.96777 | 2026-08-28 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9e7315e-2ec1-3e7c-992e-30348b158b5d | -8.59692 | -54.77999 | 2026-08-28 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dc9cad48-7ce0-3c5c-9ff9-adfcab432d58 | -9.455 | -51.71907 | 2026-08-28 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9f35d78-84db-38a8-81a8-07e727e34e26 | -6.51212 | -55.23845 | 2026-08-28 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README53.md)
