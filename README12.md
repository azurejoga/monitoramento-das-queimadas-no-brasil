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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d589284-4fb2-370d-ac61-27bed1082001 | -9.21907 | -45.32931 | 2026-06-23 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| da0e1666-6518-3c27-9ea3-cab9a6cdd3fd | -10.90993 | -54.13878 | 2026-06-23 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| edec8fb6-8825-3791-9a1c-5a98f1251050 | -5.82664 | -45.06158 | 2026-06-23 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5e3fac38-4290-367e-95f0-20f59d7656a1 | -5.8198 | -45.07584 | 2026-06-23 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3d57718-65fd-314f-8e58-b548d4eaf553 | -10.77751 | -54.11373 | 2026-06-23 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9912a19-f1b7-33e8-9d2c-bfe48fcd3ce1 | -11.55406 | -48.2745 | 2026-06-23 04:51:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2754aa56-6b69-38ee-bc05-225e66288caf | -6.36846 | -43.59908 | 2026-06-23 04:51:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 02459f4a-b904-3e9b-98cd-b4d82aadd878 | -11.80986 | -47.34694 | 2026-06-23 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0e93914-639f-3bc0-907d-8789a5ed3299 | -5.79482 | -43.634 | 2026-06-23 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb22438f-69ae-3900-94e9-4aa0d5b253b6 | -6.93835 | -51.94172 | 2026-06-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 458afdb5-70f1-3cbd-821a-d26fa6f22fd6 | -5.30026 | -43.68641 | 2026-06-23 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8354b42-c8ee-349f-bca4-a9b9aea181da | -9.22392 | -45.32994 | 2026-06-23 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3247c969-62b9-3308-9717-81e41a5d76fd | -6.62225 | -43.93455 | 2026-06-23 04:51:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91236b87-32c0-3a70-8fec-e2777a9683cc | -5.80423 | -43.78978 | 2026-06-23 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a5d53d4-ab70-3ced-9a9a-f5b2ab2a1906 | -10.97696 | -48.15394 | 2026-06-23 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c77146d7-c611-3167-a77f-d9035d8e3b2a | -10.12906 | -52.11313 | 2026-06-23 04:51:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1b1fc2d6-c668-3e88-a5c8-e89f4b25c990 | -5.82121 | -45.06601 | 2026-06-23 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ecb616ea-9a20-3f3c-9702-0a4c522ddbd0 | -8.12777 | -47.89036 | 2026-06-23 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f47d19cd-47bb-3453-8121-cc045f69b332 | -9.46198 | -49.83316 | 2026-06-23 04:51:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b63d957a-6c31-39d1-a8ba-1534c9bba543 | -11.05692 | -49.57469 | 2026-06-23 04:51:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 73a70a95-7653-3fbb-8e44-0b72e90db2c7 | -11.55478 | -48.27489 | 2026-06-23 04:51:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 094c4353-95d9-3d33-9609-547d9caab015 | -11.48392 | -46.68461 | 2026-06-23 04:51:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 92b11bad-5acd-3a3b-8ff9-6d45d221d6a2 | -5.30496 | -43.69017 | 2026-06-23 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74a87847-2454-38da-a0b4-cb0feb8e9b7b | -11.80604 | -47.34201 | 2026-06-23 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2a3ae57c-7365-34fe-9e16-6e69fca1c83e | -11.88939 | -43.83972 | 2026-06-23 04:51:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ea58fed-b735-37b2-afed-7aeb67d84706 | -8.9725 | -47.97947 | 2026-06-23 04:51:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8bdb72d-c7a7-3184-b0cb-95852cf76874 | -4.35236 | -47.76641 | 2026-06-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 295812a0-ffb4-3dae-96c5-c08dc187a922 | -8.08313 | -46.37993 | 2026-06-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 01d934c2-8b2d-35a5-9492-d27b3b0a2738 | -11.58286 | -47.43578 | 2026-06-23 04:51:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c03a9f0-febe-3f6b-aced-a53cd55bf3ff | -7.35383 | -47.02227 | 2026-06-23 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 993e031a-9379-3bba-b54e-15b9f6ac530d | -9.21834 | -45.33474 | 2026-06-23 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 85442bb6-b543-3ebc-844e-8bd0df293be6 | -10.12148 | -52.2032 | 2026-06-23 04:51:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3277e58a-b0e1-33a1-8a9b-ec202c5daa0b | -11.28875 | -43.33366 | 2026-06-23 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 40755569-062c-3822-84c8-adfa3d87856d | -9.09037 | -47.52264 | 2026-06-23 04:51:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e10676c0-a90a-3f79-84d3-d73fafd9d78b | -6.997 | -42.89433 | 2026-06-23 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 1d2885c0-c158-36d9-9e89-0f7dae648590 | -10.38898 | -56.7134 | 2026-06-23 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6f1ece2b-78a9-3bc0-897e-94c11758c382 | -8.22013 | -46.78835 | 2026-06-23 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 699a7702-20ba-3854-aa68-267eb068d68a | -8.8685 | -46.94087 | 2026-06-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 11192bbe-7835-39f1-ac84-c53b88059e46 | -6.93558 | -51.93774 | 2026-06-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4bf237b-9d8f-338a-aa47-493df6c10335 | -9.12964 | -50.93497 | 2026-06-23 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7ad548f-2ff6-3950-a30d-b954efe79325 | -8.86363 | -46.94434 | 2026-06-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d2024792-50a0-3a67-9428-c47e9388e10f | -9.45835 | -49.83262 | 2026-06-23 04:51:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8db6f9d3-81aa-3af3-b3cc-b6635abb9eb1 | -8.31611 | -45.39408 | 2026-06-23 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64e80b71-b9ec-3cf1-9b13-4c95141637dc | -10.12202 | -52.19963 | 2026-06-23 04:51:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b3fdf4fd-af81-39b3-a8af-c7f2448f30df | -5.83062 | -45.06715 | 2026-06-23 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c315c7e-1050-3d5f-b7a4-d5517dd2407e | -8.98157 | -47.97361 | 2026-06-23 04:51:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 843b7a46-a06e-3044-a683-0a8108e7d8d3 | -5.82592 | -45.06654 | 2026-06-23 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 58c5077a-ff03-373d-a7fb-8c757bb08537 | -6.515 | -47.38878 | 2026-06-23 04:51:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b325c78a-40b6-306a-8560-ccb73115c651 | -10.54006 | -47.71585 | 2026-06-23 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67dedb37-ff6f-3af1-8df8-c0693b9f4d6e | -10.7742 | -54.1132 | 2026-06-23 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a03f320d-dcad-3bea-99c4-46cb912ce471 | -10.76814 | -54.10863 | 2026-06-23 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78d6602a-3e2c-3311-ba3f-2702976466c4 | -11.80167 | -47.34136 | 2026-06-23 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ce652007-ffd5-3a61-b546-a200ef481bd6 | -9.38233 | -58.20493 | 2026-06-23 04:51:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2cdf4f49-94cc-3b65-bb25-735a67a0619a | -11.05413 | -52.46535 | 2026-06-23 04:51:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e20cc65e-0955-33f7-b579-3e237ff9e2b5 | -4.45686 | -48.02486 | 2026-06-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c9aa5ac-297b-3523-95d4-7ea1723ab820 | -10.29728 | -46.46127 | 2026-06-23 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a711d06-8f26-399a-9be4-0f6094a8677c | -11.91282 | -43.40854 | 2026-06-23 04:51:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b623e797-ee2b-356f-9c16-6f0bc9c620ef | -11.81042 | -47.34265 | 2026-06-23 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c90c8aa-4554-3b78-bb91-187c127af515 | -9.74338 | -47.88136 | 2026-06-23 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2a461c1-a32f-39d1-9b92-bad09c6e3437 | -7.13144 | -45.87989 | 2026-06-23 04:51:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0da999c3-4924-343a-b15c-03e5d13e9012 | -10.77807 | -54.11021 | 2026-06-23 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a6c60ae-13e7-352e-ad03-65416263cc4e | -11.90709 | -43.40782 | 2026-06-23 04:51:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5157f8e6-1e04-3fd3-925c-56c233b80669 | -8.44117 | -51.56723 | 2026-06-23 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6844e0f3-7d26-3a2f-9806-889899791fe1 | -9.77664 | -48.97363 | 2026-06-23 04:51:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3325068-f729-3ffd-99d5-920eb2998097 | -10.13016 | -52.10597 | 2026-06-23 04:51:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e44bea7-8e69-3bf3-87c3-ef768944553d | -9.77596 | -48.97838 | 2026-06-23 04:51:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f1f63b9-0c0e-3fe1-a6fa-02bc4c85a086 | -11.88984 | -43.83599 | 2026-06-23 04:51:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a195005a-f43f-3f2a-b615-6c9b114f6f76 | -9.1262 | -50.93444 | 2026-06-23 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a65bab3-0802-3cc1-9a42-bf0fdeb4f6b9 | -11.84029 | -47.07759 | 2026-06-23 04:51:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6fdf16ac-ba27-3c22-b42d-bfc168e17521 | -10.97747 | -48.15024 | 2026-06-23 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b16cad1b-db30-3b61-9944-bfee49326874 | -6.25415 | -48.52352 | 2026-06-23 04:51:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c6a111c-fda5-39cf-8150-46b9817988f9 | -6.22557 | -48.4509 | 2026-06-23 04:51:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| df4be33b-c781-3cd3-8bf5-f01a602dd9f5 | -8.86309 | -46.94821 | 2026-06-23 04:51:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 45fb5767-7c74-30d6-95d0-7d689c2312bb | -9.21659 | -47.9301 | 2026-06-23 04:51:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0320daea-9050-38a2-8597-9355e3cd7b79 | -7.9153 | -48.24915 | 2026-06-23 04:51:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fed1fa8e-8f11-312f-8186-06ebb12ce378 | -9.77978 | -48.97896 | 2026-06-23 04:51:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a72e3917-ebc4-36de-9f64-5245da89f87d | -6.99649 | -42.89801 | 2026-06-23 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| a4af2be9-432b-34a5-9060-9eabfaf84adc | -7.72673 | -44.5641 | 2026-06-23 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a3dfcff-11d9-3a0b-bedc-57ecce07fae1 | -5.80044 | -43.63161 | 2026-06-23 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c68a99ae-c7af-3ea3-991e-188d3ca6c9a0 | -6.9345 | -51.94468 | 2026-06-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 826cfa4f-1580-343b-b30b-3e8f1c7a295a | -6.57606 | -44.56695 | 2026-06-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a32aeabd-4324-3a8f-a209-442ce2db3ff4 | -10.02355 | -59.34703 | 2026-06-23 04:51:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a58f41be-596b-35bf-9b01-a6a9632f25f0 | -9.07782 | -47.5523 | 2026-06-23 04:51:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6372bfb-9991-3d04-b900-e49ba5f3a733 | -6.18804 | -44.86506 | 2026-06-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0b8d7bf-40af-3565-9ff4-1e58fc55a000 | -8.98106 | -47.97719 | 2026-06-23 04:51:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03704f8c-9d6e-320a-9420-41fe5d5dd706 | -10.01928 | -59.34627 | 2026-06-23 04:51:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 732293b2-5376-3464-bd57-ce00180154ed | -7.63744 | -50.0331 | 2026-06-23 04:51:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c8badde-b3c5-3c11-91f3-fe9cb6c1529a | -6.19289 | -44.8667 | 2026-06-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37a69593-9dd0-3d5f-9f44-69f25237416a | -11.4788 | -46.68832 | 2026-06-23 04:51:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 90a09027-7714-3372-88aa-a533df2d8149 | -5.82808 | -45.05159 | 2026-06-23 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ca5e1061-63b9-334d-85e6-35173c99d159 | -7.44263 | -46.03627 | 2026-06-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89650138-8ba1-3c53-91dc-34f9038cd460 | -10.65849 | -47.22649 | 2026-06-23 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fde6d6e3-cb47-31ec-af1c-4e00e7690198 | -10.11339 | -47.55468 | 2026-06-23 04:51:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff935078-fb93-348c-8a0b-200a69dc27fc | -10.88299 | -49.54421 | 2026-06-23 04:51:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 39b2603a-7a05-3be3-8f4d-357a75781c69 | -9.57865 | -49.11371 | 2026-06-23 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 209fb1c1-10cc-30c3-a6bb-253955fd13e1 | -10.61331 | -47.46509 | 2026-06-23 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76a7e040-3b10-3178-b870-959437108816 | -11.0497 | -52.47195 | 2026-06-23 04:51:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e5a0775-d5ea-3fa4-8c08-11dbfc5c9130 | -11.04746 | -52.4643 | 2026-06-23 04:51:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76a70b0f-ec29-3e0e-a820-ecf56f67ddc2 | -6.22662 | -48.44872 | 2026-06-23 04:51:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e450d8b7-d6d6-3f07-accb-b1837249d480 | -7.1346 | -45.87866 | 2026-06-23 04:51:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README13.md)
