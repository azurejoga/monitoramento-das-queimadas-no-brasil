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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8095220-7150-3cee-85d3-0e0a4a0230b5 | -6.53675 | -56.18954 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c45acfe-25d1-32d1-8089-4ce22e58442d | -4.10695 | -47.92995 | 2025-07-27 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6b399110-6d02-37d1-9ad7-082c46a05eda | -6.67131 | -43.96989 | 2025-07-27 04:57:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6d1f24c-a374-3e18-aa44-73071fd5b1d2 | -6.6663 | -58.85217 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cd4ce722-5863-38d7-9b71-64c3905493e9 | -6.6571 | -58.83572 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f69d3527-2ced-30a3-847f-19bda388eadf | -6.40026 | -53.3355 | 2025-07-27 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64c0e6cc-18e1-30e9-b751-de974150ee8c | -2.58107 | -51.92503 | 2025-07-27 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65fe1352-ee73-3ec9-b535-e69a1fffb14a | -7.087 | -44.90714 | 2025-07-27 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f56b558-e2d5-3dca-9b2d-aae38bfde951 | -9.03564 | -45.40108 | 2025-07-27 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 50b412b9-50e2-3068-9ace-ec08e72c8906 | -6.64084 | -58.83802 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05a08b9d-f490-3078-8c9e-b2c21083b0b6 | -4.0346 | -42.52442 | 2025-07-27 04:57:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d89bae34-d3e7-3593-9647-6947bae7b87f | -8.872 | -49.00795 | 2025-07-27 04:57:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b18b6c80-2211-3036-a5cd-502737558784 | -2.79314 | -49.59786 | 2025-07-27 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa65496a-6dd7-3f89-9842-491a092599aa | -2.81524 | -49.00585 | 2025-07-27 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9b08684-35da-388d-b133-6e9a711114e9 | -6.49354 | -56.19778 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 56616683-cf63-3f49-b26b-181df9cb3940 | -6.66644 | -58.82726 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 083147af-4a85-3f79-9983-f240e676d203 | -6.62539 | -58.83541 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28273d8f-de4a-3be6-ae68-a43331d9b5f7 | -6.67483 | -58.84858 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 97dcbdd1-5633-301a-8ec4-0ceb1fadf5cb | -6.00942 | -44.04752 | 2025-07-27 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c6e80f5f-99d0-3b79-8166-b66e94137442 | -6.01458 | -44.0527 | 2025-07-27 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4457784-a666-3959-acf8-768a7fa61b72 | -6.70098 | -43.07105 | 2025-07-27 04:57:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3d1b9d9d-8cfc-382e-8d6a-94b78c63d2ac | -6.54074 | -56.18642 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bae7d107-7601-3c9b-9379-4c60c4a1481f | -8.17266 | -43.2 | 2025-07-27 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e1fa8252-a58d-3d60-b153-e499d221c500 | -6.6555 | -58.84539 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f9d4cbe-c622-35ad-a572-8b6fe89c6fff | -2.74401 | -48.68645 | 2025-07-27 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81827a32-afa5-3c73-a3f6-0b9439c8d181 | -6.65775 | -58.85579 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c774fc61-4d62-31c6-9fa7-d65840f5adeb | -4.11136 | -47.95919 | 2025-07-27 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69b26999-e1ed-3f48-8434-f537bdcc5240 | -8.29426 | -45.00543 | 2025-07-27 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| db7460d4-3a8c-3dc2-adc5-47dfff1e6942 | -6.62516 | -58.8605 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8940cab5-e59c-3fad-9248-4ee76a5a64a0 | -6.53956 | -56.19376 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20398675-3ad1-321a-8021-5b43faa5547d | -6.40251 | -53.34306 | 2025-07-27 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a1e0587-d1ce-351f-b32b-a30794e5631b | -4.10091 | -48.20321 | 2025-07-27 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 568afaa8-4e13-382a-8706-61380de2530a | -6.89004 | -43.10622 | 2025-07-27 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f5898ba-ec2e-3e2b-ad9d-44efac193360 | -6.53616 | -56.19322 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 050332e6-d1a5-3f1c-bb36-d24587c9c465 | -2.82948 | -52.35817 | 2025-07-27 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4f40053-84a6-3842-a430-13a53798388f | -6.6262 | -58.83059 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be20373c-5d71-35f8-868a-46a9b61a0836 | -3.06816 | -49.49568 | 2025-07-27 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5027725c-d8dc-30d7-91cf-b5419be668aa | -6.65324 | -58.8351 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d31338dd-32b7-3aa0-b022-6f2309dc7345 | -6.65243 | -58.83994 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61a3afb1-76b4-3e61-bc60-523cbb4395f7 | -6.89133 | -44.81341 | 2025-07-27 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81744ee2-2f01-334e-87e7-c15b99353f47 | -4.11077 | -47.96317 | 2025-07-27 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb700b84-a73f-39be-9a04-35ebed6c2217 | -4.07641 | -42.53851 | 2025-07-27 04:57:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c4128006-a135-3cb4-bbf3-61797a41592c | -6.63068 | -58.85129 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fe90846a-1cb6-3d2d-8450-db3a25736a1b | -6.67017 | -58.8528 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f86ae8c7-7204-378a-847c-b8e62fff0630 | -4.06464 | -42.53403 | 2025-07-27 04:57:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bd0ae4f9-4bbd-3230-b05e-ab506f0795ca | -3.91687 | -46.44825 | 2025-07-27 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18b8a440-0574-3986-a4bf-d8f546efc02b | -9.43416 | -51.76025 | 2025-07-27 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d9053251-55b3-3f72-97aa-f09adb46aec6 | -7.29236 | -60.18489 | 2025-07-27 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c991c7d-b800-3fe2-8208-0ddd0aa92a6d | -8.30489 | -45.01073 | 2025-07-27 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d12fdaae-94a9-344c-8a68-88df4fce6e0a | -9.43538 | -51.75202 | 2025-07-27 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ecbbcbaa-b51c-356d-80b3-06a486321f30 | -7.74784 | -51.12614 | 2025-07-27 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 30619c96-837d-30aa-948c-182b8c17dba0 | -2.74454 | -48.68302 | 2025-07-27 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56656e69-db28-3ee3-87b4-6f5fd849b7d2 | -2.9038 | -48.24426 | 2025-07-27 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4aecb7d0-3525-3d58-b95d-3ffd870c3e21 | -7.56905 | -61.40177 | 2025-07-27 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ae3fe6c2-a779-353e-9f4f-feedfcd6ccaf | -9.57535 | -49.90606 | 2025-07-27 04:57:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f880770-c9c7-337c-9927-48f48b0fa8dc | -6.62457 | -58.84026 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 308f3ead-6295-33d3-aa9c-191dba0a6050 | -6.63392 | -58.8319 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9e89bf85-0d41-332d-80f7-072c2fdef5c2 | -6.54977 | -56.1954 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fde8afea-5aeb-3280-97d1-90ac79d5fbd3 | -6.55153 | -56.18439 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3443e2cb-eede-3a33-932b-9e5028cc266a | -5.74315 | -43.95176 | 2025-07-27 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d6bd87f-df8f-3401-b263-60dce3389679 | -6.65017 | -58.82965 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5254dd05-f762-3aec-9cf3-b9b0ef642a7b | -6.65388 | -58.85516 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| afd8ce72-0c4d-314b-8886-f3932f4fb4a7 | -6.89557 | -43.11204 | 2025-07-27 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80682e60-1896-3135-9a49-e3a6129841ab | -7.10439 | -59.76423 | 2025-07-27 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c484ed97-52c0-3dde-a8ec-ad574e15b237 | -9.92235 | -48.90505 | 2025-07-27 04:57:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e18780ef-6e14-3dcc-aee2-ad66de85d189 | -7.04779 | -43.57838 | 2025-07-27 04:57:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 13825965-80c8-3424-9c39-62b59145523b | -6.0089 | -44.0514 | 2025-07-27 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8cf7079-8c43-3fd9-8a01-e8a94e46437c | -4.10148 | -48.19945 | 2025-07-27 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61181bde-d4eb-3876-be45-e3dca1da3cd3 | -6.64695 | -58.84902 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f3eb26b1-cac9-34e4-836e-ec494dbeb001 | -6.67644 | -58.83882 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ac6d579-c0b7-3a3b-bd03-95663e30e8ff | -6.67148 | -43.96865 | 2025-07-27 04:57:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04ee3d0e-0b5a-3099-9325-60572240e727 | -6.64325 | -58.82357 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06f93eb3-32f4-3ac9-b35b-dd1599249273 | -4.10454 | -48.20767 | 2025-07-27 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6320d46c-e9b9-369d-baa2-e36f0a072d89 | -6.55598 | -56.2002 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1159488-f17b-3ba2-966f-524876915d19 | -6.54578 | -56.19854 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3cdfe320-c98f-3879-9b1d-cc03d9c0ae22 | -4.13945 | -47.6487 | 2025-07-27 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f8f4437-ac17-340a-99cb-cd59ff1436cd | -7.55848 | -61.40934 | 2025-07-27 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1483559f-91c3-3557-a387-83874bf95c14 | -6.54355 | -56.19064 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5064602-7d0b-310b-b443-d038edbaf7fb | -6.89381 | -52.87276 | 2025-07-27 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfbb4ae5-e645-30ad-bd45-f2cb304e4570 | -7.37243 | -43.43055 | 2025-07-27 04:57:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26fd800e-b2df-308f-bebc-32bd14063c1c | -2.90324 | -48.24792 | 2025-07-27 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e7eca5a6-7227-36cf-919d-a13a54010ac5 | -6.64533 | -58.85877 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 3cf68639-1419-38eb-bf30-aa263373d12c | -2.81125 | -49.00786 | 2025-07-27 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 13464dfc-4c47-3647-ae07-914f6bb1e627 | -4.9603 | -43.73314 | 2025-07-27 04:57:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6960cc0f-ca17-37fc-9e40-4d2e19f78218 | -7.7509 | -51.13096 | 2025-07-27 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 17810eb2-8da6-32b8-87f2-dd534d4456b1 | -3.39296 | -47.49215 | 2025-07-27 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f5f076e4-a338-3c8d-a061-0e77c3dcd01e | -7.56298 | -61.41014 | 2025-07-27 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c546385c-533f-3e0a-a783-d43f69c4ba3d | -10.01033 | -48.22528 | 2025-07-27 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de828896-270c-3d96-a555-0e012d8eda18 | -4.13507 | -47.64811 | 2025-07-27 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d1fbd31-d344-3c67-9a76-bff9612e609b | -6.01892 | -44.05231 | 2025-07-27 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ca4c35b-72ab-3fb6-808c-8f664901b8fe | -7.16915 | -59.82708 | 2025-07-27 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 08654ee3-bba2-3cd9-a747-6a4485f8c9e3 | -3.36848 | -47.62863 | 2025-07-27 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9341431-1ed2-330f-b66a-50ab6a497447 | -6.63698 | -58.83735 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3045c845-39ae-3bce-b463-3be8b10c16b7 | -7.28807 | -43.07905 | 2025-07-27 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 277b66c4-b53c-341c-b69a-7a5f138533be | -6.64164 | -58.83321 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7a74398d-f8ee-332e-b637-ecd5b19894af | -8.17107 | -43.19755 | 2025-07-27 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 84bce18b-3017-390a-865f-9579559473a4 | -6.67563 | -58.84371 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 89144491-bdd9-3526-aa65-e88b72cccc3f | -4.1106 | -47.93483 | 2025-07-27 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 00fa6512-598c-37b7-8c33-ec11d68661a0 | -6.67403 | -58.85345 | 2025-07-27 04:57:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ccf0912b-62a2-397c-815f-57d71684d56f | -6.54414 | -56.18697 | 2025-07-27 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README16.md)
