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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6c76877-3e7e-3065-9aea-b27804a8588a | -9.6022 | -48.375 | 2025-09-06 00:15:00 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9753433-46e6-3b55-9319-0bd454e887ce | -13.5395 | -46.957401 | 2025-09-06 00:15:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3c8cf7e6-293b-3268-8311-95afff8d56f5 | -7.5302 | -50.350899 | 2025-09-06 00:15:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63f7ef74-e919-370d-be76-f9bd2dde3f97 | -18.2376 | -45.981499 | 2025-09-06 00:15:00 | METOP-B | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 15c00ec7-72e6-3d7a-8ba1-b17e0ba57198 | -14.3697 | -48.050499 | 2025-09-06 00:15:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 09317f2d-e991-3c17-88ad-54378a018133 | -11.4031 | -52.219799 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 108645f1-4e49-3e50-a77f-3975765ae258 | -8.5739 | -49.673302 | 2025-09-06 00:15:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dec08a71-2e8c-3d99-a297-b66501f24cb1 | -21.635799 | -48.036999 | 2025-09-06 00:15:00 | METOP-B | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bf327230-4a62-310b-9038-6a06b26ba347 | -10.0222 | -50.555099 | 2025-09-06 00:15:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d170849-3d2f-34c2-bc30-528687dc4637 | -8.1482 | -48.323799 | 2025-09-06 00:15:00 | METOP-B | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 920074c7-2d5f-3f46-adb7-9e54568e0ef3 | -11.0609 | -46.443501 | 2025-09-06 00:15:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cc76d48a-b2ee-3945-a179-aed5fb8ac30c | -15.5244 | -53.6022 | 2025-09-06 00:15:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 08e91a6d-ec91-3cfe-beee-7d8a028dcce1 | -4.1825 | -48.1063 | 2025-09-06 00:15:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 092e31ca-527e-36de-bc4b-573bc0ada3c7 | -20.34 | -46.505901 | 2025-09-06 00:15:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 857d0a3d-b67c-39a0-a8da-27d653226a34 | -23.9506 | -49.5443 | 2025-09-06 00:15:00 | METOP-B | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | nan |
| 416a5bbc-e049-3475-a44b-66a413f324f7 | -12.8047 | -54.8535 | 2025-09-06 00:15:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8ed9ec2f-1087-30a8-8cc4-8205c63c208b | -11.4092 | -52.199799 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 83c5392b-9fea-327d-9faf-c6ef060d593e | -9.6405 | -48.868198 | 2025-09-06 00:15:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8fbbbd73-ac0c-343c-97cb-8acd740af8ba | -5.5288 | -49.319401 | 2025-09-06 00:15:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee826be1-d046-3e1e-9e09-542337ca9f1e | -3.4953 | -49.577099 | 2025-09-06 00:15:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3190d930-09e5-38dc-97b4-de4e6f3ec01a | -6.6141 | -52.827202 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7805b0e3-06be-3526-8ab1-14d37a1fafce | -12.3234 | -53.866299 | 2025-09-06 00:15:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b3f827f8-c43b-3bd3-bc40-0210c7bf4c41 | -9.5066 | -49.516701 | 2025-09-06 00:15:00 | METOP-B | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ad04408-2de4-39e0-8467-55ab829d37f1 | -17.9433 | -51.814098 | 2025-09-06 00:15:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 01d96203-2cab-3e66-80e0-f0207194a95f | -8.7334 | -48.680599 | 2025-09-06 00:15:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 271750bb-7561-34f6-b9c4-e8f03df2352b | -10.1209 | -51.487701 | 2025-09-06 00:15:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9855c2b0-bbf3-398a-a654-dfd5220ac3d2 | -5.5203 | -46.476398 | 2025-09-06 00:15:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4333ad69-aae5-391e-9022-c2e0c9033609 | -8.6773 | -47.294498 | 2025-09-06 00:15:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b34c691-f7a0-316b-bced-6d60a6dcdabc | -9.8288 | -48.374699 | 2025-09-06 00:15:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61f40f62-24ad-361d-8ea1-5aed0537cba8 | -14.3795 | -48.048199 | 2025-09-06 00:15:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e4b521d1-7d80-3cae-b217-18788b5f3559 | -9.483 | -49.3176 | 2025-09-06 00:15:00 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 414f0ae6-d8b8-3e7f-a56a-53e12727ef8c | -18.245701 | -45.971901 | 2025-09-06 00:15:00 | METOP-B | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ca387507-aa4e-3712-8176-67ef6d6588e7 | -14.3851 | -48.121101 | 2025-09-06 00:15:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c015c470-3d6b-328c-a496-d89940977df6 | -8.1597 | -52.5746 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a75524e-2533-33ba-8257-a5adf29681b4 | -14.3769 | -48.130402 | 2025-09-06 00:15:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7838b425-7f19-3a34-844c-8cb48601dbc6 | -9.8948 | -48.118099 | 2025-09-06 00:15:00 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2cbcc1cf-dd55-38d5-b10e-1b0df83bd3d8 | -5.5303 | -49.326302 | 2025-09-06 00:15:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e08d54b8-64d5-304a-81c8-86544273a856 | -16.457199 | -49.4035 | 2025-09-06 00:15:00 | METOP-B | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 24aa1e8a-f393-3a51-bc6a-e13987fa47ee | -15.3534 | -49.859501 | 2025-09-06 00:15:00 | METOP-B | SÃO PATRÍCIO | GOIÁS | Brasil | 5220280 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1b7644f4-1b38-35fd-a4f3-b566983df6e9 | -12.5812 | -48.201698 | 2025-09-06 00:15:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 909b5153-38f8-3472-bbdc-bf08b169e32b | -22.648001 | -49.2271 | 2025-09-06 00:15:00 | METOP-B | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 03ba26b4-a90b-32b7-8ce6-2dfc10a99b38 | -4.8312 | -49.791 | 2025-09-06 00:15:00 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19393a51-a211-3881-b022-1cb1c2953947 | -23.9426 | -49.556099 | 2025-09-06 00:15:00 | METOP-B | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | nan |
| 1040868e-8294-3ebf-86d1-56c25d6de7b2 | -6.0846 | -53.458401 | 2025-09-06 00:15:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8ebb70a-fc7f-32f4-b90b-a01917948e23 | -16.345301 | -42.3955 | 2025-09-06 00:15:00 | METOP-B | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a6ee42f0-cede-3ffd-8c4a-f94326716b4d | -2.2689 | -47.800499 | 2025-09-06 00:15:00 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae223387-6740-33b9-b59e-c6211ec067ae | -13.0812 | -46.8456 | 2025-09-06 00:15:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 89b81334-f184-3c43-ad5c-786dabc0551f | -12.8588 | -47.139099 | 2025-09-06 00:15:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3aee2262-57bd-3a72-bf3b-a99d6469ceaa | -23.9639 | -49.5616 | 2025-09-06 00:15:00 | METOP-B | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | nan |
| e3a2ec51-2c9d-3e8f-bda0-531a4de6440b | -5.5526 | -51.827099 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b370c0fe-dc99-3a66-aa8f-49c93f1bcdc8 | -11.1897 | -43.606499 | 2025-09-06 00:15:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 38a3428d-4103-358d-8672-bbdb3e0f0e15 | -12.4922 | -45.004398 | 2025-09-06 00:15:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 407a57d8-45c5-3287-b386-32fe8c01a6cf | -9.381 | -40.645599 | 2025-09-06 00:15:00 | METOP-B | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 27cff8ea-4666-3b5c-be0a-7aa69dde05c3 | -6.8594 | -50.899502 | 2025-09-06 00:15:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47fcd7a5-32eb-39c2-9e38-bd649800b592 | -16.1373 | -52.989899 | 2025-09-06 00:15:00 | METOP-B | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5514a674-86eb-3057-9a24-e33b889f61a4 | -18.0721 | -43.073002 | 2025-09-06 00:15:00 | METOP-B | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cded9cda-bbd8-36bf-9f34-4888762a6cfb | -12.7727 | -54.845699 | 2025-09-06 00:15:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2fe5687e-6917-35b3-a65f-94715bb806a0 | -10.4128 | -44.374599 | 2025-09-06 00:15:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 476ed1ba-9ef9-3d32-a719-9dce14e5547e | -15.3518 | -49.8517 | 2025-09-06 00:15:00 | METOP-B | SÃO PATRÍCIO | GOIÁS | Brasil | 5220280 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ab5982b3-efb4-33c6-ba82-124b2697ea04 | -8.8049 | -49.833801 | 2025-09-06 00:15:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f20bab3-1891-326b-80d6-fe3a41389c36 | -8.7065 | -45.146801 | 2025-09-06 00:15:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fcb8cc00-2720-32c5-a52b-f3fed34a7b12 | -6.0689 | -53.480499 | 2025-09-06 00:15:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92afc9b1-4fe5-346d-9448-1fcc07e64fb2 | -10.5904 | -47.775002 | 2025-09-06 00:15:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be98265d-5b63-3b35-b775-4cbf62c452d3 | -9.4824 | -51.144199 | 2025-09-06 00:15:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4a58e16-7da6-3af0-903d-5dfde54fcddf | -9.5428 | -51.091202 | 2025-09-06 00:15:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a1ea444-d335-3f6c-9985-d560cc00bc89 | -6.2013 | -46.123001 | 2025-09-06 00:15:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8bd1b05-c81b-325a-8a1e-59e5cfc79d61 | -10.9552 | -48.206299 | 2025-09-06 00:15:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89e8b419-dc5c-3eeb-a54f-d8f87fb553ff | -5.7416 | -45.695599 | 2025-09-06 00:15:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d41d4f52-835a-342e-a3b2-3cc73d909fe1 | -6.3426 | -49.5485 | 2025-09-06 00:15:00 | METOP-B | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0853d73b-773d-326d-b1bd-348989ebe45f | -13.3651 | -48.162399 | 2025-09-06 00:15:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f13ad462-c61c-35b2-88be-60d4781c84e7 | -16.347799 | -42.405899 | 2025-09-06 00:15:00 | METOP-B | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3d63452e-d820-3fdc-a3e3-6212d9d314fe | -8.1647 | -48.305401 | 2025-09-06 00:15:00 | METOP-B | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eb6f9fdd-fb35-3e69-a0b5-0cb5a0dae852 | -9.533 | -51.093399 | 2025-09-06 00:15:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3454c668-2498-3446-b8c3-fde21e49ff9d | -6.608 | -52.8461 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74f9e60f-8ed2-35de-a251-ca6014941100 | -11.3411 | -47.3564 | 2025-09-06 00:15:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 844adbd1-614f-3a76-b4b4-222ace2f6e15 | -9.1964 | -54.768002 | 2025-09-06 00:15:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b8786b4-c12b-3f32-8bc5-a11f6d0576f0 | -7.9016 | -45.3652 | 2025-09-06 00:15:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fa481f37-c42e-31d4-84df-4c7be88142b6 | -8.1542 | -52.549 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bede93c1-df4f-3b49-960d-a1b200a561d2 | -16.447399 | -49.405701 | 2025-09-06 00:15:00 | METOP-B | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e17db853-98dc-3d9f-b337-a67f43910556 | -9.4889 | -51.1269 | 2025-09-06 00:15:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f74f2b7b-7bb4-33d3-88d0-89a1b5a5f771 | -12.6995 | -48.926601 | 2025-09-06 00:15:00 | METOP-B | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb610dc1-2425-3c9f-babd-cb9e21ab24c0 | -5.6637 | -52.191399 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62970a90-54ab-34f7-bbc6-1cd3ce38a6d6 | -7.1336 | -48.530899 | 2025-09-06 00:15:00 | METOP-B | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53624ca8-5e90-3b0d-b3a0-917b7becbc61 | -8.8864 | -47.036301 | 2025-09-06 00:15:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a82cf115-e6a5-32aa-9b15-cd9b895e6205 | -6.0728 | -53.451599 | 2025-09-06 00:15:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b6cd9c7-c789-3d65-920f-58bbd904bb78 | -14.9853 | -44.053398 | 2025-09-06 00:15:00 | METOP-B | SÃO JOÃO DAS MISSÕES | MINAS GERAIS | Brasil | 3162450 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| e2a1f50d-f1d4-39a2-b413-51010b0617e6 | -11.0053 | -55.049301 | 2025-09-06 00:15:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 137225ea-498d-353f-b7d9-e202d8f768a7 | -9.5098 | -49.021 | 2025-09-06 00:15:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1eab3972-c5f6-3668-aebb-5a3632973067 | -6.6729 | -52.814499 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf133e3d-58a6-3abe-9590-59c2c232cbf1 | -9.8341 | -48.168701 | 2025-09-06 00:15:00 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5251aa10-d737-35db-a989-3ef7d5a5282a | -7.8558 | -52.402199 | 2025-09-06 00:15:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcc802ec-b1aa-3c8f-86ad-66b27d6927e2 | -12.8153 | -48.096802 | 2025-09-06 00:15:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec237f4d-672d-39bb-8b8b-2147ad39cd40 | -20.7244 | -44.062401 | 2025-09-06 00:15:00 | METOP-B | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1eea113f-32cc-353f-96e2-0610715457ff | -15.5147 | -53.604099 | 2025-09-06 00:15:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 25114f96-ce8c-37c3-9fcf-9dd83565d908 | -14.9793 | -52.429901 | 2025-09-06 00:15:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4eafcc31-3d90-3337-80d3-6d23fbe76bbe | -12.3086 | -53.893501 | 2025-09-06 00:15:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d6d9354f-097d-3a74-b597-9bec13e1957b | -4.866 | -45.429199 | 2025-09-06 00:15:00 | METOP-B | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 260dc0c6-5932-39c4-b867-2726c05919e9 | -5.6241 | -46.390499 | 2025-09-06 00:15:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f3952b78-1a59-3c21-82b8-7c942b87d22e | -5.5222 | -46.484798 | 2025-09-06 00:15:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8d0c23b-71d9-3d9b-8fa0-8f2ba455b12b | -7.5318 | -50.357899 | 2025-09-06 00:15:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
