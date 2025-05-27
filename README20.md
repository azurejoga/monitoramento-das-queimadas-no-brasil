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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0157db96-3542-3dd9-8b24-1ba3a3d731b1 | -18.8488 | -53.582 | 2025-05-27 11:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 175.2 |
| c0373046-1302-3e98-9d08-2bde3381d3d8 | -7.9827 | -50.7201 | 2025-05-27 11:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 824a67fb-b6e2-3454-957b-a7ff81d38428 | -18.8488 | -53.582 | 2025-05-27 11:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 192.4 |
| 03c87f78-73dd-3ecc-84f8-1069905ce737 | -13.7065 | -45.2454 | 2025-05-27 11:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 1388aa17-763e-3297-9460-8202d78f62de | -7.9827 | -50.7201 | 2025-05-27 11:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 123.1 |
| e702a34b-1325-3a53-9bb0-e1c4be690bf8 | -12.3324 | -49.9857 | 2025-05-27 11:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 105.2 |
| be8c058b-4926-3043-9030-f9758bc63e64 | -7.9827 | -50.7201 | 2025-05-27 11:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 142.3 |
| 738571c7-41f2-3545-8e74-b632a107b19d | -13.7065 | -45.2454 | 2025-05-27 11:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| a557f7ea-0512-3e64-9831-25a749325f01 | -12.3324 | -49.9857 | 2025-05-27 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 46c95628-3768-35ce-b888-90155a383d90 | -7.6236 | -45.7672 | 2025-05-27 12:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| a56fba4a-24c0-3ee9-b2b5-2ff9f0c5f073 | -7.9827 | -50.7201 | 2025-05-27 12:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 61897eb0-3866-3a51-9c94-a9db25ac672f | -12.3324 | -49.9857 | 2025-05-27 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 178.6 |
| e669a9b5-bc48-3e79-a089-6a524c8d4404 | -6.51061 | -43.63564 | 2025-05-27 12:02:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2ea14925-c430-3f47-8015-462ec431c5d0 | -7.2496 | -43.76134 | 2025-05-27 12:02:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1f8e2249-4b59-35a5-9326-b7bb6b5d6504 | -6.895 | -47.82563 | 2025-05-27 12:02:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 016a7098-fe8a-34ef-ba5a-0a646c4cc958 | -7.62455 | -45.75323 | 2025-05-27 12:02:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 1414a03d-defd-30c2-a179-273409ee7ac6 | -7.28555 | -43.23312 | 2025-05-27 12:02:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 35.2 |
| 0511b217-41f2-3340-8fd9-020bba9456d9 | -6.50892 | -43.6468 | 2025-05-27 12:02:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 41dafdd8-0d37-3e44-9219-21afaa3eb3a8 | -8.10988 | -43.13865 | 2025-05-27 12:02:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 99a0c3de-a539-365c-8a33-4a88266aaeb0 | -9.24957 | -40.95513 | 2025-05-27 12:02:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| f40c7b03-cbeb-3003-ae6f-7caf56454e31 | -7.28894 | -43.24025 | 2025-05-27 12:02:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 84306514-42f0-3db6-a290-9b40afac7720 | -9.22744 | -40.00892 | 2025-05-27 12:02:00 | TERRA_M-T | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 89aa893c-d4e2-3a7a-8107-00dfdf0c5131 | -7.23543 | -43.5068 | 2025-05-27 12:02:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 819cc7b6-5ade-382a-a881-a7a6af395529 | -6.83988 | -44.92762 | 2025-05-27 12:02:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 7999491e-e8ff-366f-b308-442d261a872a | -6.84103 | -42.79391 | 2025-05-27 12:02:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 30cad6f2-c28d-3da4-a640-75427bf21889 | -6.3327 | -43.37757 | 2025-05-27 12:02:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| df38388b-8a80-3f03-b820-b3652dd95cc0 | -7.29052 | -43.22989 | 2025-05-27 12:02:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 239ce6ab-272b-3dcb-9298-ea3a56d19bc8 | -9.19086 | -40.53021 | 2025-05-27 12:02:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| ee642628-10aa-3626-b473-13e2bdb5df9d | -7.20549 | -43.98561 | 2025-05-27 12:02:00 | TERRA_M-T | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 24fae8ec-de16-3bfe-b9c4-918e7e61a18c | -7.60674 | -43.42285 | 2025-05-27 12:02:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e3cbb53e-964c-3861-a204-30d69a25132b | -6.3343 | -43.36665 | 2025-05-27 12:02:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 362.2 |
| c20df211-5147-3c9b-b204-c7d9c4d25824 | -7.28403 | -43.2435 | 2025-05-27 12:02:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 77de6fbe-b6f0-357b-b23f-73bc9dbb1d85 | -7.60829 | -43.41239 | 2025-05-27 12:02:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 32.1 |
| e9efeae1-e2b4-3244-991e-8eb0daa2549c | -7.60183 | -43.38995 | 2025-05-27 12:02:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2730967b-7ee3-3038-a72b-bfa918794abe | -6.83955 | -42.80387 | 2025-05-27 12:02:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| c37e9ded-e8b6-3739-aff8-584722ee451d | -7.20171 | -43.10955 | 2025-05-27 12:02:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 74a4f93e-c994-39b1-bb0c-c6d104dab10f | -9.25085 | -40.94622 | 2025-05-27 12:02:00 | TERRA_M-T | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| befda31e-4111-3618-9a22-d75e336e8f55 | -6.22546 | -43.34443 | 2025-05-27 12:02:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 649f6276-6397-39b8-b291-c30f72056143 | -7.60839 | -46.64988 | 2025-05-27 12:02:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 3252fa7b-5f80-3dfd-8593-5fe2129801cc | -8.75531 | -44.9114 | 2025-05-27 12:02:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a65a4a77-d0df-31fc-98bf-0eb0d3e6a229 | -6.46735 | -43.71462 | 2025-05-27 12:02:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e65485ca-2209-3e32-bb39-99d12720caf5 | -6.33589 | -43.35582 | 2025-05-27 12:02:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c38d09a1-dc7c-33a6-844c-ad9ffc560692 | -7.60985 | -43.40191 | 2025-05-27 12:02:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 196a78b6-b412-3b90-8169-7c98d92ec7fd | -7.56825 | -43.35297 | 2025-05-27 12:02:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| e5edecda-f249-3444-86d3-c63d0d9ce6cb | -7.23702 | -43.49601 | 2025-05-27 12:02:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| b7b41977-9e9f-3089-9b71-1a93f7b4da77 | -7.22643 | -43.10855 | 2025-05-27 12:02:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 652ebfc3-9864-3b16-9204-c82b2570bfa4 | -6.63361 | -43.21127 | 2025-05-27 12:02:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 1df35edb-e858-3ca4-bc62-cbea9489af63 | -14.70518 | -45.40443 | 2025-05-27 12:04:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 994113f0-602f-3b05-9094-332d196f99e9 | -10.23263 | -47.42714 | 2025-05-27 12:04:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 1832a3b7-f2f6-3448-b16a-a699abd65b43 | -10.01484 | -47.55109 | 2025-05-27 12:04:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 96f8e124-f4a7-3877-adbc-d685f84cddf5 | -13.70318 | -45.25512 | 2025-05-27 12:04:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 471a345a-3a68-38e4-b132-446dae580d1c | -14.70693 | -45.39307 | 2025-05-27 12:04:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |
| a591351e-7e6f-3d54-b70e-6a24c8c158da | -16.33685 | -43.51602 | 2025-05-27 12:04:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 03314e7f-5615-335f-8eb9-397159f3217b | -10.01046 | -47.56401 | 2025-05-27 12:04:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 2c8640da-0f1a-3b59-828c-3cbde19fb05c | -9.61229 | -47.75319 | 2025-05-27 12:04:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 5aaeec74-b5fb-328a-a5fb-5411d6118799 | -12.07701 | -47.35396 | 2025-05-27 12:04:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e1c8a42b-2d0f-39f1-bb4a-0340dfbc5c0d | -14.70931 | -45.38847 | 2025-05-27 12:04:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f7467aa8-3b0f-3ab6-aea0-1306a2113fe4 | -11.76878 | -46.42606 | 2025-05-27 12:04:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 14753933-f3de-353e-bcd2-931a6896edbe | -17.2578 | -47.08423 | 2025-05-27 12:04:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a00fcb55-6881-3c4c-9f73-759ca9e9f41f | -13.69684 | -45.23067 | 2025-05-27 12:04:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cad72382-cd4e-31c8-94ab-a166d1fccaeb | -13.28199 | -43.6504 | 2025-05-27 12:04:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2e530d59-369c-31b0-9629-099c41e56df9 | -13.07585 | -45.27012 | 2025-05-27 12:04:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 5cd72dbf-3d19-3c7c-9c52-936f019902aa | -13.90737 | -46.10766 | 2025-05-27 12:04:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d83ddd87-c067-314c-b65c-324123f01edb | -14.7075 | -45.39977 | 2025-05-27 12:04:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 32.1 |
| fa3d1e96-c76a-37af-b75b-99e950ea6f04 | -13.69508 | -45.24207 | 2025-05-27 12:04:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 0d34807d-3060-31d6-a57e-d34226121bf3 | -17.96461 | -44.41578 | 2025-05-27 12:04:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 52.1 |
| a98be92e-21c1-3f7c-b022-282e078ba289 | -13.07214 | -45.29345 | 2025-05-27 12:04:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 786bbd8d-a18b-382c-a839-cc152a61569f | -10.04231 | -46.27141 | 2025-05-27 12:04:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| a54113e0-e18f-362e-a6be-2dd7010d1275 | -15.69579 | -41.69264 | 2025-05-27 12:04:00 | TERRA_M-T | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| ec79f17f-07f7-3963-b957-15a5d79b71ad | -13.07399 | -45.28178 | 2025-05-27 12:04:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| aa237da9-781b-3922-8946-ea90f09b6c8e | -11.77121 | -46.41827 | 2025-05-27 12:04:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| b16d19cf-8036-3fc6-99c8-ae4718d3d1d7 | -10.63665 | -48.08162 | 2025-05-27 12:04:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 787a8be6-bc91-3cf4-9449-b65006c3f846 | -12.38348 | -49.9859 | 2025-05-27 12:04:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 29be9c2f-cc27-3919-b9aa-d15b0de2440b | -10.03105 | -46.26938 | 2025-05-27 12:04:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| df11df74-21d5-38d4-b244-396ea41a3b89 | -10.04102 | -46.27727 | 2025-05-27 12:04:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 65c9b4f0-40be-3f56-be85-4df2c117ed0c | -12.37044 | -49.98969 | 2025-05-27 12:04:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 7346d12c-11bb-3a60-9a7a-2e99223cc431 | -12.34001 | -49.97825 | 2025-05-27 12:04:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 213.1 |
| 04b1ed94-d78c-38e8-8d40-e7c717116110 | -17.23493 | -46.78971 | 2025-05-27 12:04:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 02a9b38d-c936-3f21-8a01-da2cdc0b78f8 | -10.71472 | -49.62346 | 2025-05-27 12:04:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| dfa4fd53-0cdb-3ae2-b9f5-e294b5d7bb4b | -10.01162 | -47.57027 | 2025-05-27 12:04:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 27462daf-624e-3d83-83a8-a3b11ea5a0be | -11.14663 | -49.17874 | 2025-05-27 12:04:00 | TERRA_M-T | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| e057bae8-3c30-304e-b1e3-c729793a51b1 | -14.66657 | -45.20272 | 2025-05-27 12:04:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 90165817-0f65-345a-bbc3-c687e5928a94 | -10.7154 | -49.63067 | 2025-05-27 12:04:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 1b0cc3ed-9e10-3fa1-a87b-8c0d2504d7bd | -9.61136 | -47.75928 | 2025-05-27 12:04:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 29d949f2-196a-3a5a-af2b-8643a1bf77f7 | -11.21476 | -48.62207 | 2025-05-27 12:04:00 | TERRA_M-T | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 6724f3ef-7da1-3400-876f-d5e310eb3287 | -12.36898 | -49.98343 | 2025-05-27 12:04:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| ee0e1c4a-40f3-3eb8-bff1-a0db0b2f6804 | -9.60909 | -47.77322 | 2025-05-27 12:04:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| b7d464df-696e-35f4-976d-9547e934c54a | -14.66831 | -45.19166 | 2025-05-27 12:04:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9fdd99c1-0a08-34c3-99c8-e04fa7cb3b8d | -13.70495 | -45.24366 | 2025-05-27 12:04:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| ea43f767-5bc6-323e-8f07-cdc806e7e049 | -18.86897 | -53.58735 | 2025-05-27 12:06:00 | TERRA_M-T | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 11cb6230-99cd-390a-bc01-bd4ae02f0acb | -18.86414 | -53.58032 | 2025-05-27 12:06:00 | TERRA_M-T | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 6f5a8f70-4bc7-34c7-b7de-66d46cc329ca | -18.85647 | -53.61877 | 2025-05-27 12:06:00 | TERRA_M-T | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 486.9 |
| d9a468a1-a968-3c81-a367-b99fdc4c662d | -18.85255 | -53.58348 | 2025-05-27 12:06:00 | TERRA_M-T | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 217.1 |
| c07bff5b-153c-3b7d-81d6-b960f5200540 | -24.40333 | -49.91167 | 2025-05-27 12:06:00 | TERRA_M-T | PIRAÍ DO SUL | PARANÁ | Brasil | 4119400 | 41 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 1ede5190-ac12-3d4d-832a-48b731246228 | -24.40465 | -49.9008 | 2025-05-27 12:06:00 | TERRA_M-T | PIRAÍ DO SUL | PARANÁ | Brasil | 4119400 | 41 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 7acc03a2-5e9a-3663-b8b6-e2571ec12470 | -18.84765 | -53.57673 | 2025-05-27 12:06:00 | TERRA_M-T | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 7757e77c-e1c3-3ee8-941f-9c6cd25492ae | -18.86105 | -53.62581 | 2025-05-27 12:06:00 | TERRA_M-T | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 243.5 |
| 5d13b573-3c2e-3596-b4bf-0237bfe177b3 | -12.3706 | -49.981 | 2025-05-27 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 38614783-450d-3d55-b612-87d66f214c2a | -7.9827 | -50.7201 | 2025-05-27 12:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 8dc632f9-3917-3428-8477-1f2998e478d9 | -12.3324 | -49.9857 | 2025-05-27 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 137.1 |


[Clique aqui para ver as próximas entradas](README21.md)
