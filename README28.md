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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bfd8a703-77e2-38b8-9ffd-0def382037c4 | -6.42521 | -42.61782 | 2025-09-14 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 56642408-0fe4-3a02-853f-b95e0c6c1007 | -3.22965 | -47.63287 | 2025-09-14 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7fd7822-935d-373b-871c-eb7cc733bcf8 | -5.96517 | -47.01888 | 2025-09-14 04:38:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49fcac22-29f5-3109-98ae-4b98e16a0eb5 | -3.21907 | -47.63484 | 2025-09-14 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f82e7ed-e285-35f2-bd90-231d85365a16 | -3.59436 | -47.51796 | 2025-09-14 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| e119b080-2358-3de5-8ccc-c2c74cbce12f | -6.08861 | -43.13839 | 2025-09-14 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6b45cfa2-cc2f-3fd2-8211-2bde9dc49d7e | -3.66401 | -50.94948 | 2025-09-14 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8722a38b-7a0c-3edd-a08b-639c04ff2c51 | -3.60164 | -47.51542 | 2025-09-14 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dccd6d80-78be-3eb5-9a16-96b179359183 | -6.30087 | -44.57867 | 2025-09-14 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e51539a-f500-3abf-9ffa-34485d4606a1 | -3.79467 | -47.58534 | 2025-09-14 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34608af3-b2dd-31b7-843e-1898d7fde569 | -3.21925 | -47.1289 | 2025-09-14 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a04c26c5-3097-3824-afca-8122db6182fd | -1.19776 | -46.15359 | 2025-09-14 04:38:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 727dd064-4a23-3717-8768-963e789b0660 | -6.18003 | -41.14831 | 2025-09-14 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8fe7252e-862b-3f8a-9eac-ef783d458f67 | -6.43235 | -42.63314 | 2025-09-14 04:38:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4f0905b3-c29c-3b66-a7c3-b99b2115c253 | -3.33463 | -44.44701 | 2025-09-14 04:38:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6cc6b91-f658-38ca-93a9-d595cb1f8de3 | -3.27965 | -43.52481 | 2025-09-14 04:38:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d004db6-55d6-3120-a515-e269fcc1a2a6 | -6.32947 | -43.95439 | 2025-09-14 04:38:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17004ce5-000a-315b-b14d-b62ce31d5dae | -4.48532 | -48.11174 | 2025-09-14 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be6887e5-46b5-3dcd-b671-2a84c234f25d | -2.29965 | -48.1451 | 2025-09-14 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7f9ee86-c5f5-3f2c-a4b6-49de60f27132 | -5.95342 | -42.79931 | 2025-09-14 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8841e901-7ec4-3bba-9df9-ff40a4b467fa | -5.2057 | -44.31625 | 2025-09-14 04:38:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c7438a8c-95ef-3371-9811-fc206e8a8c09 | -5.79439 | -43.88657 | 2025-09-14 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f4543d99-b9ee-30b4-bfaf-8c7132b7edd3 | -3.00774 | -47.8364 | 2025-09-14 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2989c963-7e62-3556-9593-b11046017ee2 | -5.73036 | -43.19085 | 2025-09-14 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a93b0503-9544-37f7-98e5-fc5c6f8c483e | -6.16639 | -42.75523 | 2025-09-14 04:38:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 49d38f41-b435-31c7-8b9a-9625e96b3584 | -6.21161 | -42.506 | 2025-09-14 04:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9f1160b8-48ae-3222-842e-d353dba62486 | -4.80114 | -42.74223 | 2025-09-14 04:38:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66ebee30-1b90-3d5e-be3c-a78c96db12eb | -6.12447 | -42.95126 | 2025-09-14 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 9f241aba-d917-3963-b9a2-9044780ba30b | -6.10474 | -45.94361 | 2025-09-14 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94846a18-f170-3041-98ac-3dc9172ac5a6 | -5.64707 | -43.89227 | 2025-09-14 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e82b2cb4-96e6-344c-b583-b274f1c41b60 | -6.33364 | -43.95504 | 2025-09-14 04:38:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 584a106c-6251-3562-91b2-563aad573574 | -3.86997 | -52.38894 | 2025-09-14 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c24b91e7-2bc6-3ef7-82bd-c11e7771e060 | -6.02126 | -46.35602 | 2025-09-14 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b78236a0-4830-3065-a75e-3980143b29f2 | -6.05854 | -43.56064 | 2025-09-14 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c0ef8ab6-79f7-3a61-a746-0b7af32813b5 | -3.60219 | -47.51184 | 2025-09-14 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 130a0b31-592b-3aa2-8d3d-82dd5a4e01a6 | 1.14644 | -53.0796 | 2025-09-14 04:38:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f99c059-11a5-3130-90e4-094be02ff1f5 | -5.40245 | -44.82619 | 2025-09-14 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61e2a9d0-3460-3fa2-9550-dafaac8f908d | -3.60974 | -51.04827 | 2025-09-14 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81ef7280-0ecd-32f8-aa2a-f307d43ce7fc | -6.12668 | -43.94927 | 2025-09-14 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f8b8a346-0763-3f6c-84d8-fb1072905ab6 | -6.30488 | -44.57924 | 2025-09-14 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7f37295-b9b7-3e4b-9637-132b2e472e72 | -2.4375 | -48.61353 | 2025-09-14 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0f3fb4fa-147f-3c1d-975f-66be1650e1e2 | -2.95272 | -47.44508 | 2025-09-14 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2091eaa6-a553-3842-8809-6b5a72fff927 | -5.95938 | -47.01009 | 2025-09-14 04:38:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6412e7f-794e-3a67-8b63-c2ce8244cdef | -6.10106 | -45.94308 | 2025-09-14 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8435384b-3d34-3df6-b1be-fcde4b70f50f | -3.31879 | -44.18138 | 2025-09-14 04:38:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc301f21-f174-3c8a-8562-56bed371a2b2 | -4.04396 | -43.34473 | 2025-09-14 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 349f8461-a0d5-3e07-8c93-b41319aba581 | -3.22296 | -47.63184 | 2025-09-14 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94d29a89-c137-3feb-9020-025013e1e208 | -3.79803 | -47.58585 | 2025-09-14 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 336413f4-06ae-36c9-9835-d5dbe688996d | -3.22685 | -47.62882 | 2025-09-14 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07215818-e6d5-377a-89fe-7190fcdedd2c | -6.45435 | -43.60072 | 2025-09-14 04:38:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f4646ee-27ba-3e7c-be1b-040563d38709 | -3.89858 | -40.92099 | 2025-09-14 04:38:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a8e2c325-556b-3e60-b82b-c7a0e5347236 | -6.12384 | -42.95565 | 2025-09-14 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9335ed4e-3443-38e6-9dea-7fdb2ddf26ee | -3.21961 | -47.63131 | 2025-09-14 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15859fe3-1b4c-3ccb-b35a-fcaaaaa84e6c | -5.96055 | -47.00234 | 2025-09-14 04:38:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff5cac04-aae7-35d7-93dd-7cdb62a2e8ef | -6.1651 | -42.76423 | 2025-09-14 04:38:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 33384164-aee4-33fb-a7a9-f93dfbbbffb4 | -5.26313 | -48.57943 | 2025-09-14 04:38:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6120f39-ce64-3942-b816-e929bb48e3a9 | -11.70668 | -46.90127 | 2025-09-14 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5bb558e3-bb82-3907-9d62-96e769d4ab35 | -5.7323 | -49.30107 | 2025-09-14 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a10e159-e0c0-3250-86b1-7a95d1c86b5d | -7.02679 | -44.53512 | 2025-09-14 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef798340-dd95-3b40-8171-1ae17fad5d52 | -11.44889 | -46.91179 | 2025-09-14 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c918dcf2-a5c8-328d-b3cd-d17c917d6e21 | -11.38824 | -48.1885 | 2025-09-14 04:40:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 726cb3f9-40dc-3d54-b6b3-c780276858c1 | -10.93095 | -47.35939 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7303e8ae-9980-37ed-83c2-b46fbcd1ab72 | -6.98864 | -44.54067 | 2025-09-14 04:40:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8fd4fe60-53cc-3fcd-8a54-34a75a6fc4b0 | -11.24575 | -47.63058 | 2025-09-14 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0434fd5c-d802-38a4-8930-31309a083b12 | -11.44471 | -50.7819 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ef2c8db-2086-3a26-b59d-7dfda3338735 | -9.87473 | -46.45182 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec468dfe-aeeb-32d0-ae8f-69e895beb27d | -11.47939 | -50.79823 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 029ba968-ecdf-3012-a6bd-b20d64cf78bf | -11.45461 | -50.78349 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c26fd3e3-361f-30d2-9a80-77e68e41a64a | -9.66109 | -45.87727 | 2025-09-14 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f88dee4-fa35-35b4-8c91-75773d58e175 | -13.02253 | -47.99112 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10029100-cdae-39dd-92df-7598b31413b0 | -12.93022 | -47.9449 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d07f007-54e8-3fab-916c-2ee9913e5333 | -10.34151 | -50.50328 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23e07654-f24f-37e5-8a07-f027aa8ec0e5 | -10.34754 | -50.48639 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c265d24-5a0e-3470-b70b-0e85b1b03c61 | -9.1149 | -46.94055 | 2025-09-14 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb377306-c585-31c8-a5a8-e9f89bc490a3 | -11.46449 | -50.74205 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 888c349e-95c3-362d-bf39-0168f24212e4 | -7.39224 | -49.97758 | 2025-09-14 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1381e284-3bf4-3446-9d9d-f27b20b9e37d | -8.35083 | -44.73018 | 2025-09-14 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a614178-3ebf-32d1-8cf5-c8640a4f79fe | -11.78517 | -47.40017 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42fc1d9b-2252-30c3-8d26-a27d8c01dece | -9.01645 | -47.04758 | 2025-09-14 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99ef3329-f14d-3b66-a0e2-7aa30ff69836 | -11.45197 | -46.91676 | 2025-09-14 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84d049ba-2e40-37d0-a9ec-e9a4b6d9a9cf | -12.78609 | -47.14095 | 2025-09-14 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4175685e-c953-3481-939c-958c77854b17 | -10.7547 | -44.77746 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3862d1a6-6a71-3d1b-9f52-f4472a859ec1 | -12.97361 | -48.00042 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b03a69bf-e149-3496-ae60-7cfa415dc981 | -8.96145 | -44.44392 | 2025-09-14 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0623855-d9d2-3f00-bc8c-5901ca664cc2 | -11.47716 | -50.76918 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 83c1fdcc-68ae-34c9-a3fc-870b58efa898 | -8.18144 | -46.77465 | 2025-09-14 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 602edf33-832b-303d-be2d-ed7bf897c7cb | -12.77433 | -48.00518 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b9dfce44-593c-3faa-a411-70adb34571f5 | -10.89931 | -45.56318 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cfd0421-47ee-347f-8b07-66a4aadef4a8 | -12.75112 | -48.01423 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4b28860d-b540-3082-9194-6208dc5555f9 | -11.49586 | -50.75784 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bcbdccd6-e67d-3843-8859-3ed1bbe8d53c | -11.45405 | -50.76548 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 721b3c0c-84bb-32da-9b04-85105a9c6f5e | -10.71818 | -48.69404 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c64fa70-fd68-3369-bc66-2ebd6df3e33d | -6.38146 | -47.25712 | 2025-09-14 04:40:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea2296fa-b90c-31b0-97c3-b100ddae7258 | -11.44515 | -46.91134 | 2025-09-14 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e0da791-08c5-3fd6-80b0-6d29ed9d6e3d | -9.00411 | -45.76321 | 2025-09-14 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fdc32c15-144a-3b7a-ad5d-79bc982ea46f | -10.88113 | -48.18822 | 2025-09-14 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b9b53bf9-c967-3110-a47d-92b60b568dec | -6.80309 | -51.37722 | 2025-09-14 04:40:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 20934861-e9b1-37cf-a564-60818cfb80a5 | -12.04336 | -46.53613 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bebce3e1-060f-359e-9ec3-8ae2141cb3eb | -10.91986 | -45.59237 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 131ad97c-23d3-3e2f-85e5-9d457b57fa68 | -10.78503 | -45.98438 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README29.md)
