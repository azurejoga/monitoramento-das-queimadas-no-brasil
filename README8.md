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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4de07d9b-6d7f-39a0-a72f-74e202d3096c | -6.78857 | -44.10379 | 2025-07-27 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6882d55d-aee3-3a2a-a73c-ebbe640b7664 | -5.47868 | -41.7804 | 2025-07-27 04:06:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e0f39dc8-d484-3c65-998d-f0c466b25ee0 | -6.63018 | -43.04187 | 2025-07-27 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4fd1780-2c13-3e36-ae06-8d4a725074e0 | -6.67278 | -43.9716 | 2025-07-27 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 481238f4-f4b9-3ffa-941d-f4656f86971d | -6.4075 | -41.14582 | 2025-07-27 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8040ad0e-fb42-3e53-95a9-9e184639a94f | -6.14572 | -42.58627 | 2025-07-27 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b95cebdb-a2fb-3262-85ae-38b441c5aa3d | -7.28958 | -43.08478 | 2025-07-27 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5dbc01d7-57a5-3f1d-8486-b783b0c142bc | -6.05637 | -42.92881 | 2025-07-27 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1315b47b-e9c1-3f64-b8a8-a9cb140d73ed | -5.78162 | -43.60677 | 2025-07-27 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b2a5e854-e4d7-311a-90ea-26fb0602e283 | -4.10565 | -48.20441 | 2025-07-27 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52aaf144-1c68-30b0-a6c0-c1ccc462e39a | -4.10101 | -48.20372 | 2025-07-27 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6dadbac-d366-355a-a347-85637e58e495 | -6.6734 | -43.96778 | 2025-07-27 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ca473ff-a384-3742-82bf-f2b05315708e | -2.74414 | -48.68462 | 2025-07-27 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c84adffc-7cf0-3737-bfd2-be727f1b45e3 | -6.89477 | -43.1138 | 2025-07-27 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e31ef16a-2e55-3169-bec9-a72ffbeeb213 | -3.06305 | -49.49726 | 2025-07-27 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 70f47458-3b5b-39b8-af86-62e8f33ac5c7 | -3.39985 | -47.50009 | 2025-07-27 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dab3fe54-ee53-3a9a-87e4-473700e2a27f | -6.56362 | -41.51443 | 2025-07-27 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9aca42be-4964-364d-b2b3-5deb5cde1192 | -7.00288 | -42.34649 | 2025-07-27 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 471acc4c-89b8-3b3e-b782-9f200139a8c1 | -3.57126 | -49.50819 | 2025-07-27 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e44399a-e372-35c0-889c-c8a2f08a391e | -3.56872 | -49.50845 | 2025-07-27 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| df64601f-e4f5-355d-b4e6-4675f5abfd67 | -5.74067 | -43.94877 | 2025-07-27 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 197d14a1-778b-387e-a6e3-781d3318ee71 | -4.1048 | -48.2094 | 2025-07-27 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c2779f1-2aba-30dc-b51c-b221f345d591 | -3.06664 | -49.50742 | 2025-07-27 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28d5f689-9149-3542-b511-be7230b3c41c | -6.12689 | -42.55444 | 2025-07-27 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fdf2f778-d0fb-39d8-9d14-784848ddc432 | -4.61781 | -43.318 | 2025-07-27 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90fddfef-a828-3e9a-9564-b7320ad57f65 | -4.11039 | -48.12371 | 2025-07-27 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13812d55-2639-3345-9f49-674c676751e9 | -4.10253 | -48.2011 | 2025-07-27 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ad7dab9-c10f-3be3-aa05-df0119999563 | -6.47847 | -43.48314 | 2025-07-27 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1387ad8-f24e-3e2a-9e60-12b7d6abd5f5 | -7.0106 | -42.34059 | 2025-07-27 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e1095e4b-ed2f-393f-9603-6dbb6fd95bd9 | -2.90377 | -48.24468 | 2025-07-27 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ffd859ef-cb18-3e92-a536-210c6aeb7c4d | -6.01095 | -44.04998 | 2025-07-27 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 66b77b48-0d0e-37c1-b9a5-27937af33953 | -3.3954 | -47.49929 | 2025-07-27 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 03a71497-b7aa-3d2f-9a1a-91c8250aa081 | -6.22777 | -44.52296 | 2025-07-27 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a5e9af47-856b-3722-a6b6-a9827c72958b | -6.88259 | -44.19377 | 2025-07-27 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9a22610-786b-3f05-8110-a27e4eef77f4 | -6.55643 | -41.49562 | 2025-07-27 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| de8ec33e-5f05-3219-a45d-3f57e80b0330 | -7.00398 | -42.33953 | 2025-07-27 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3b0503a4-0f31-3972-bf91-46f5c8a87db4 | -6.70036 | -43.06801 | 2025-07-27 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad03c4dd-0581-31a0-afb2-4b8035a856f2 | -5.52349 | -43.20467 | 2025-07-27 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e688d603-0679-3067-899d-8936e5b700e3 | -5.43937 | -46.28925 | 2025-07-27 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 781b2989-0960-300a-a0ef-427856586978 | -2.79344 | -49.5969 | 2025-07-27 04:06:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb8a47cc-61ed-3327-8bc6-19f746a2b999 | -3.23733 | -42.0732 | 2025-07-27 04:06:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bf3338f-9452-307e-a91c-9f8008f0115a | -5.60253 | -45.08236 | 2025-07-27 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a31a9039-cc76-3f38-bdc4-65729d6975d4 | -6.86973 | -43.68967 | 2025-07-27 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d7a6fc9-fe15-348f-be34-6e80e74517a7 | -6.63075 | -43.03829 | 2025-07-27 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a575e57-f534-3548-bac2-e66ac80808ec | -6.87789 | -43.13317 | 2025-07-27 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b96e77e-0e95-3c15-9d65-e6f0a5725b95 | -6.12745 | -42.55091 | 2025-07-27 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f42d2a67-0192-310e-a68d-2d443fdc4dd6 | -5.185 | -44.9537 | 2025-07-27 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c35f7907-e14b-36a7-9c69-0a56672e5b9a | -6.89502 | -43.12436 | 2025-07-27 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94381524-8084-3eff-81a9-ea514eb43e85 | -3.11632 | -48.96498 | 2025-07-27 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a1974b3f-1c9b-3a64-88ee-781526785e2d | -3.91495 | -46.44891 | 2025-07-27 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8677ec54-98cd-3dbf-b246-6322cb83af9c | -7.09237 | -44.04478 | 2025-07-27 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72dfb9b3-4f93-3f13-b13c-056ab5b05ba7 | -3.57176 | -49.5051 | 2025-07-27 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0d27f011-45ab-30fc-b127-d6d56319ed2a | -5.67719 | -42.79552 | 2025-07-27 04:06:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 58a83eff-03df-3464-8772-6f00dad4e891 | -5.67776 | -42.79197 | 2025-07-27 04:06:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c2a4880f-8acd-3d43-b640-5a215c20744d | -6.89162 | -44.80476 | 2025-07-27 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b1580ac9-658e-390f-8824-e64592943309 | -5.29047 | -45.40875 | 2025-07-27 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1164fd09-fcea-3daf-b51a-a890d8434d8b | -5.6805 | -43.6687 | 2025-07-27 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d47ff228-38af-3381-85eb-2cace87592d1 | -6.99365 | -43.33612 | 2025-07-27 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 884d4945-fd1c-3c81-bf8b-36d0befd3e8e | -3.74362 | -49.04812 | 2025-07-27 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a6132d0-b874-304a-82df-096851362779 | -6.00681 | -44.05339 | 2025-07-27 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b53ac2b-307c-3de6-a5aa-ccb262765f00 | -4.13218 | -47.65293 | 2025-07-27 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f750180-2365-3368-b7f3-1e478c1f7bb7 | -3.39168 | -47.49412 | 2025-07-27 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7c4ce747-29f3-3497-9254-4d0e3322e572 | -5.78506 | -43.60732 | 2025-07-27 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 494a4905-620c-3f7e-baf0-2553363cda76 | -2.57865 | -51.9245 | 2025-07-27 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d93778de-027e-3201-b27b-38df31d95e2b | -6.45316 | -43.94077 | 2025-07-27 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8b10782-0ee4-34a3-9589-b764e0cec62c | -4.61377 | -43.32119 | 2025-07-27 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2e0770e8-8d5e-380b-a59b-c232f73a06fa | -2.58551 | -51.92081 | 2025-07-27 04:06:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dca7506e-b0b6-3b50-b0da-6a6cfd0b200d | -6.60342 | -39.38914 | 2025-07-27 04:06:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 797fb710-0de4-3266-8ff8-067718f28039 | -4.13293 | -47.64843 | 2025-07-27 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fcfae06e-ae9a-3007-a1ac-32dd8b0c9bc5 | -5.77757 | -43.60994 | 2025-07-27 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| dbee6a13-1220-318b-910c-859690ff9de8 | -5.74478 | -43.94547 | 2025-07-27 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28b93842-5051-3f19-ba49-0391c11f930a | -5.18711 | -44.95658 | 2025-07-27 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c5bfda5a-a091-31b6-94e0-3cf6cfee6aaf | -5.67326 | -42.79858 | 2025-07-27 04:06:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5ed5297f-6c89-3c31-9905-afe67b69845e | -6.00745 | -44.04949 | 2025-07-27 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b350e20-54fd-3a53-973e-a0197a88f41f | -6.78919 | -44.09995 | 2025-07-27 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ba41299-189c-37f5-8671-f7afaeb2b667 | -6.54657 | -41.51528 | 2025-07-27 04:06:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fb6e4ce9-1957-3a1b-a425-09f45cd663fd | -5.46491 | -44.33287 | 2025-07-27 04:06:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eae0d71a-d26c-30d7-823c-2e30011aa89a | -4.03326 | -42.51819 | 2025-07-27 04:06:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| faa48548-9768-3dca-bbc1-78c3462bbe65 | -6.38701 | -47.34061 | 2025-07-27 04:06:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6bdeee53-6e6b-3022-9c91-dfc3c3d9f6e5 | -4.10453 | -47.93076 | 2025-07-27 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8a8f4c8f-e93b-3f89-a801-78fc47265315 | -6.01732 | -44.05492 | 2025-07-27 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5e4671c-d087-32f8-b8dd-54915d6c6d43 | -3.06254 | -49.50034 | 2025-07-27 04:06:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5367da3-f07a-3e59-8680-04474507fee0 | -6.00808 | -44.04559 | 2025-07-27 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5237fff6-31b1-3c02-b7f2-25f257859b64 | -3.92113 | -42.40876 | 2025-07-27 04:06:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ed532298-5545-34ce-b6b3-dd98c6168491 | -6.53834 | -45.60651 | 2025-07-27 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bcc5128-9bc8-3432-83ad-e75699472ab5 | -6.89534 | -43.11022 | 2025-07-27 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85da6777-0461-3e82-ab05-78d5c8e40e76 | -3.27483 | -48.8147 | 2025-07-27 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 630f4e1b-2145-3c8e-9a40-64667d4a7e33 | -7.16906 | -38.43689 | 2025-07-27 04:06:00 | NOAA-20 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 74022965-76fe-3ff7-a113-3a8d6110d9bf | -6.67122 | -44.46822 | 2025-07-27 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bd27b4c-4e3c-30bd-9235-674a7a0e0817 | -7.04942 | -43.57756 | 2025-07-27 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| acae903a-c74b-3248-94b2-90de143afda9 | -4.06632 | -42.53788 | 2025-07-27 04:06:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ac58db2d-5453-36f8-ba4d-336042d6fb2b | -6.88582 | -43.10501 | 2025-07-27 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 78df3490-9eb2-3348-ac4a-7ec612f64294 | -7.0952 | -44.04915 | 2025-07-27 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b29daf6-e985-35d4-8d30-db17630895fb | -6.52455 | -43.34749 | 2025-07-27 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b1772fa-1e95-3edf-9a3b-13259a788181 | -6.14239 | -42.58574 | 2025-07-27 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1f081acf-b023-396a-82d3-aba76005a28d | -7.09871 | -43.42398 | 2025-07-27 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2821172e-042f-35ea-a050-b752c772e04a | -4.82038 | -47.31804 | 2025-07-27 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c776046-10de-3c63-a339-65426f460023 | -6.39124 | -45.31957 | 2025-07-27 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10288e47-82fc-32be-8d35-54e0525137fa | -6.47467 | -43.98335 | 2025-07-27 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da4b5da2-e363-3f89-aad3-7d2df95f6659 | -6.8864 | -43.10142 | 2025-07-27 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README9.md)
