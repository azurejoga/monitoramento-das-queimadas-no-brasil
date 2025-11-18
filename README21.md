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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f7c8d16-df9f-3496-a92c-ec897889466b | -4.30109 | -42.12041 | 2025-11-18 04:18:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 27880f71-9768-34a9-a08c-bae871069bd1 | -1.33041 | -49.32205 | 2025-11-18 04:18:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1e10c1a3-55eb-3330-a52b-9f7afd3f4f54 | -3.04902 | -47.01891 | 2025-11-18 04:18:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5915e131-393d-39c9-a460-86f692bbb0b9 | -3.2505 | -43.03816 | 2025-11-18 04:18:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4328a86a-7dbd-37a7-a4b9-31fa61546ce0 | -3.18081 | -48.02802 | 2025-11-18 04:18:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| b167e5f9-cdf2-34c3-838c-d16c62cad724 | -2.51169 | -47.82231 | 2025-11-18 04:18:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2af81e7a-f4d8-363b-aa20-24c17b30446e | -3.59839 | -40.96752 | 2025-11-18 04:18:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5ec27998-9838-336a-a7e0-a95fc927a36a | -2.50124 | -49.34906 | 2025-11-18 04:18:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5baa9580-016f-33fc-902a-29a024ed1c98 | -2.85898 | -45.23304 | 2025-11-18 04:18:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea4dec48-27a2-313f-a022-1b211c2cc39d | -3.17769 | -46.57829 | 2025-11-18 04:18:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c4d0ccb-e58a-3928-abde-1366532039e9 | -3.44808 | -40.74765 | 2025-11-18 04:18:00 | NOAA-21 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a1354bd1-cbd5-3634-86c9-1f4faec059b5 | -2.86755 | -51.47303 | 2025-11-18 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3bd27e0-fcbc-3c2a-9288-84a3108cb831 | -2.49705 | -49.3484 | 2025-11-18 04:18:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d541ac07-3323-39cc-a3d6-139c4db83dd9 | -3.4085 | -46.90439 | 2025-11-18 04:18:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e73445aa-f789-32ea-ad00-c7ac64e101e3 | -3.02563 | -47.83711 | 2025-11-18 04:18:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cbe86a4c-1798-3745-b7ad-cfc06b99da92 | -3.56109 | -47.30949 | 2025-11-18 04:18:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90e89464-cf0a-3550-a401-17a4833bf0df | -3.02729 | -44.46423 | 2025-11-18 04:18:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6e58b3f-cb54-3f1c-859f-3dbf899ec184 | -2.68778 | -49.16842 | 2025-11-18 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4d2ffb25-e8a7-318c-a449-55b739c4780b | -3.02867 | -47.84226 | 2025-11-18 04:18:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ddc85444-e79c-32e4-9928-5b4c6593c40e | -2.4899 | -49.33941 | 2025-11-18 04:18:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b84ec00a-64fe-3f25-833f-4abb13f86853 | -3.02489 | -47.84167 | 2025-11-18 04:18:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 247a2cfb-24b1-3d01-8224-af08d3632fba | -0.88511 | -51.99733 | 2025-11-18 04:18:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ada25d38-61e9-30b9-9a74-7090706fe30d | -1.31211 | -54.18639 | 2025-11-18 04:18:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1bf059c-95e6-3a64-803a-e0ef46ec6ace | -2.52225 | -47.80492 | 2025-11-18 04:18:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 14c5e3ae-8e68-334c-96bd-886c418d2be4 | -2.81861 | -48.24705 | 2025-11-18 04:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba562aeb-373a-3c7f-ac2b-d4a4b5141fe7 | -1.33467 | -49.32271 | 2025-11-18 04:18:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8571a897-e796-3952-aed9-0ee35669b324 | -2.82965 | -45.42028 | 2025-11-18 04:18:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ca128275-85b7-3fb2-b3c5-88043fe5f756 | -3.72444 | -39.13572 | 2025-11-18 04:18:00 | NOAA-21 | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5d31611f-2be5-396f-8006-7219b7445eee | -2.91875 | -47.84982 | 2025-11-18 04:18:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1852c512-3b0f-3ca8-8f19-04c516dec4d1 | -1.43598 | -48.90712 | 2025-11-18 04:18:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dde9d097-b4bc-30a1-96a1-7c70e6dbf454 | -2.5311 | -51.18626 | 2025-11-18 04:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 65338db0-b0c2-3711-a1e0-5489b3182307 | -3.46138 | -40.51763 | 2025-11-18 04:18:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 12a702f5-9ec7-3458-81f9-191d66a768db | -3.58803 | -43.60097 | 2025-11-18 04:18:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37afe643-fe2e-39c2-afea-239d81607d66 | -3.47581 | -46.06765 | 2025-11-18 04:18:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b09919e7-0013-32b7-9b7d-83a4e0cf0b6f | -3.17622 | -48.03215 | 2025-11-18 04:18:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 47bf8193-4656-32fd-9a9b-e3265adf8fad | -0.99238 | -47.07401 | 2025-11-18 04:18:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 5a381c4e-2131-3d0f-a4f0-140d86072884 | -3.38613 | -46.14243 | 2025-11-18 04:18:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74522db2-780b-3135-9b29-20f18430667d | -1.63327 | -45.75056 | 2025-11-18 04:18:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6cbfd31-9c71-3e51-b881-73b6370e2072 | -2.95015 | -45.34631 | 2025-11-18 04:18:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 524dacb8-a669-3a91-a4d2-ab19c67341cf | -3.79411 | -45.83166 | 2025-11-18 04:18:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eac39f93-6f0b-3b55-87aa-3e788a05ed48 | -3.66577 | -44.81739 | 2025-11-18 04:18:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99ee2f42-a78b-3a36-98fe-0189bd04be58 | -2.49347 | -49.34391 | 2025-11-18 04:18:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bfee4b31-9c2c-3d4e-8447-8b03e645be0d | -4.46265 | -41.80096 | 2025-11-18 04:18:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a426e0bf-1852-377b-a776-edab9989481d | -3.04968 | -47.0148 | 2025-11-18 04:18:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34e6af09-4df5-37e4-a197-b83af18b8c17 | -1.41943 | -48.90456 | 2025-11-18 04:18:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99775735-ccf0-3957-82a6-5e1e9ab72a06 | -2.59384 | -45.1402 | 2025-11-18 04:18:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31548f8c-ac1e-3ad0-8556-65d76660fd7f | -3.38049 | -41.18209 | 2025-11-18 04:18:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 989d766e-bc20-3bfa-96f4-b224f1ff5660 | -2.82683 | -45.41612 | 2025-11-18 04:18:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8c3bc98c-b0fd-309e-bd42-0e3af584ad44 | -2.52152 | -47.80952 | 2025-11-18 04:18:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 9a71130a-fc0b-377f-9db2-7e822833d158 | -2.2822 | -51.93148 | 2025-11-18 04:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d6f5c8e-7dbc-3f05-80be-6eebe6f9b33c | -1.80739 | -54.71473 | 2025-11-18 04:18:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a8032626-8b1e-3a80-b042-48aa475c29eb | -2.91658 | -49.57231 | 2025-11-18 04:18:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2537ae62-2044-36fb-b710-2e68dd0f9a27 | -3.24717 | -43.03765 | 2025-11-18 04:18:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a3572d31-b223-34df-acdf-6d9e549fd387 | -3.02398 | -44.46372 | 2025-11-18 04:18:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| caaae80a-835d-35cf-afd7-7068bafa499a | -2.13023 | -46.27584 | 2025-11-18 04:18:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87703e41-531e-3d99-adef-ab3d25bcda3d | -3.47236 | -46.06712 | 2025-11-18 04:18:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ff0a73c-2397-3611-8fd4-62a677ed0d4c | -1.33894 | -49.32337 | 2025-11-18 04:18:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ab821ce5-06fd-34a5-add6-e1b53bfc8c02 | -3.50854 | -44.86451 | 2025-11-18 04:18:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5202e42-e156-30eb-a2f8-8be5d54eb15a | -2.91721 | -49.56837 | 2025-11-18 04:18:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ac15d63c-e0de-336d-9739-2fd90209bf47 | -3.58526 | -43.59702 | 2025-11-18 04:18:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef83cd95-59ef-3b7c-a2f0-8bd8eb95727d | -1.19375 | -48.93179 | 2025-11-18 04:18:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 030b26aa-e555-3f31-98e7-3e00ee4a162d | -3.25436 | -43.03519 | 2025-11-18 04:18:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| a64d8a1f-2f47-3780-857e-372d6d71667d | -3.01278 | -44.3841 | 2025-11-18 04:18:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cd5f860-9b98-3dfa-82d3-19d2b5e06c6b | -0.88462 | -52.00042 | 2025-11-18 04:18:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39db2850-c5e5-3884-b5a6-aca297f317ae | -3.60732 | -43.60748 | 2025-11-18 04:18:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ffd1eca3-b8b6-3420-903f-9609b5364675 | -3.12981 | -45.74727 | 2025-11-18 04:18:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 44b06d94-08fa-3f28-9e2e-af8241bb0b9a | -1.9206 | -48.80302 | 2025-11-18 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 4d48a397-5a64-3518-b4ab-a17bf243a723 | -3.34854 | -46.29753 | 2025-11-18 04:18:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91573dc2-cb49-3780-9be1-66a2538dd45b | -1.34193 | -49.327 | 2025-11-18 04:18:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c43a0c1-5c50-3314-8cc6-d85a0fff3bda | -3.49363 | -45.11045 | 2025-11-18 04:18:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f46451ed-943a-3b25-a27e-def4b9903c81 | -3.02843 | -44.47859 | 2025-11-18 04:18:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f6478d8-39b4-353b-99fb-6cedf4549cda | -3.78524 | -45.59526 | 2025-11-18 04:18:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2c1310af-ffd7-3eed-9d84-cd3278758b02 | -3.08277 | -48.13103 | 2025-11-18 04:18:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77c785fd-861e-3c76-a2d5-e9cb4ecb4748 | -3.60191 | -40.96841 | 2025-11-18 04:18:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cbbed060-64b6-32fb-9b23-a0b637c38ec8 | -3.17331 | -46.60605 | 2025-11-18 04:18:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10697f50-04f3-3105-8e21-b861a289b4a5 | -2.97821 | -48.77233 | 2025-11-18 04:18:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85eaff14-421e-37ce-8a9c-bba0eb62bd79 | -3.35268 | -43.49342 | 2025-11-18 04:18:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9338292c-c3ea-3e0b-a697-4854f5ef45b7 | -2.8678 | -49.47282 | 2025-11-18 04:18:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8cf831f-b344-3b0b-a76c-380c11cf93b7 | -3.38673 | -46.13868 | 2025-11-18 04:18:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98ea998a-2022-342e-8829-c46983d17bb3 | -1.98749 | -48.51237 | 2025-11-18 04:18:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a36f9c87-ea86-3bde-97c4-23d5c9be3d9e | -2.49409 | -49.34006 | 2025-11-18 04:18:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d82cc6f3-bf75-31a7-84ea-6cf535f124d9 | -2.45507 | -48.90589 | 2025-11-18 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f844594-f00f-3a4c-9c9e-f34506a9344e | -2.40155 | -45.71106 | 2025-11-18 04:18:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a264bcb3-e3bd-3087-8195-70cd67c9c706 | -3.45768 | -40.51743 | 2025-11-18 04:18:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 72f3c7ae-2b12-3339-ae16-973cfeff341c | -3.78186 | -45.59474 | 2025-11-18 04:18:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54e90c64-dc92-30ea-b8cd-93c13aa4e513 | -1.45937 | -53.42925 | 2025-11-18 04:18:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aec0dd8a-dee2-3d91-9999-556cfb386123 | -2.99142 | -51.07401 | 2025-11-18 04:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b8a5ff7-10a7-3699-bc06-29a13c4a3512 | -2.47481 | -48.22805 | 2025-11-18 04:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 0180d6d1-d1b9-3b64-bd9f-839a054205e9 | -1.32614 | -49.32139 | 2025-11-18 04:18:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0aee392b-e216-3188-80eb-ae71a45dde0e | -3.1775 | -48.02965 | 2025-11-18 04:18:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| bd5b3368-958e-3bf6-a865-283c315afa9c | -3.45702 | -40.52174 | 2025-11-18 04:18:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3ed06611-1b8a-303e-9807-cbd8d541c8af | -2.86235 | -45.23357 | 2025-11-18 04:18:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f0f0e3d3-4507-3373-8f8f-29223f1dbd60 | -2.83215 | -46.7233 | 2025-11-18 04:18:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 50c7b27d-1e7f-3b1c-bc4e-853864d9721e | -1.19608 | -48.93157 | 2025-11-18 04:18:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8a64d02-48a6-327e-af7a-63a2159c6017 | -3.18038 | -46.60717 | 2025-11-18 04:18:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 380fb964-4a0e-3c64-874b-a5150bfc4a1c | -2.5155 | -47.8229 | 2025-11-18 04:18:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 503f47db-205b-322e-aad3-1043b6ce29ad | -4.03374 | -42.10285 | 2025-11-18 04:18:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3e7e31c4-3473-3555-be48-a35a13bc4ec5 | -3.01332 | -44.38065 | 2025-11-18 04:18:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de3c456e-d3ff-3087-af79-96003db2660d | -1.19791 | -48.93243 | 2025-11-18 04:18:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 80c3a143-d0c2-32f6-ba46-bade632dbb0e | -2.77613 | -48.6541 | 2025-11-18 04:18:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README22.md)
