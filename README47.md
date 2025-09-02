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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a26ffc5b-07d3-3ca9-8659-9ab21e70dfb3 | -11.89034 | -46.75182 | 2025-09-02 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b4bb3eb-ab12-3cba-856b-898844a08a61 | -7.70103 | -50.27089 | 2025-09-02 04:14:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a92444dd-c1dc-3ff5-97b3-2a2af506aba9 | -9.1299 | -46.05012 | 2025-09-02 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e1c6ecc-b155-34bb-a542-55f45a0e98f1 | -7.46513 | -44.8082 | 2025-09-02 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a8d8e24-71f9-3169-88da-06fb772d97cc | -11.79433 | -46.40357 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0b4711c8-8cf0-3b63-8566-4237d27f318c | -11.79839 | -46.40035 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 865f7f5d-276f-3e05-94cd-ba459ef7c9b3 | -12.92931 | -56.97355 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1d688a98-4bd0-3cd5-a335-24f334f69467 | -17.70688 | -46.8924 | 2025-09-02 04:17:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 961ccdc0-ec5c-3f94-b2bc-8a29f3f07233 | -15.56148 | -48.35837 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d6bac472-3b7e-35e7-97fd-0f1073045c82 | -12.93275 | -56.99537 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d672efde-6ddb-32a3-a7da-0467b98cde55 | -18.09049 | -50.47508 | 2025-09-02 04:17:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 059b263b-214c-3db2-951f-198d0ad921ff | -14.79052 | -48.20625 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b96ef3d-a998-3505-ac5f-a1673c001034 | -12.92381 | -57.00071 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 569352f2-d001-3df8-83c8-5ea6da0fd284 | -17.28909 | -49.19912 | 2025-09-02 04:17:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ee6167ff-52f4-35b7-98f8-22339e73a2c2 | -14.21298 | -48.05484 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6e52d25-1629-358c-b24b-527f4c6657c8 | -14.72704 | -46.75091 | 2025-09-02 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7c1658f-535a-3a5a-95f4-9a7f44e6ffb0 | -15.97075 | -48.23893 | 2025-09-02 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 971cfa6b-3248-3d37-b7ab-39f62d99575f | -14.79666 | -48.2229 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 05b071be-eff2-3ecc-85fb-26e394c78b19 | -15.68159 | -48.94196 | 2025-09-02 04:17:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a28bda6f-8451-3468-a8e6-6c4ed330d6c0 | -20.69718 | -46.312 | 2025-09-02 04:17:00 | NOAA-20 | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 676a5269-6838-3a7a-9bc2-2c1452b35906 | -13.8969 | -48.08111 | 2025-09-02 04:17:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e6ad1e7-6b9e-34bd-b7f7-cc1a4847dfe5 | -15.4383 | -43.31351 | 2025-09-02 04:17:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 221742cf-72d8-3f69-9aeb-683f4554737a | -12.93209 | -56.96682 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8a3a8637-938d-366e-ac61-88b92dee196f | -15.72664 | -53.67553 | 2025-09-02 04:17:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1bb6a5a1-f662-37bf-889b-a387dd44892c | -14.59744 | -48.05167 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1d1ef2b6-da2b-3fd4-839b-6c29dda2119c | -12.93093 | -56.97234 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d238de48-9a05-32d5-b025-b8d17eb740a2 | -14.8582 | -46.74183 | 2025-09-02 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4b67e965-f114-3c34-9973-43f940d10863 | -14.76317 | -48.1499 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 92666fa3-49c7-3053-9b57-cdc7e289d279 | -15.56432 | -48.38468 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4ffc9e64-6f0d-3dfd-8a04-e159ed2d1204 | -14.4889 | -45.94719 | 2025-09-02 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 66e623c9-24a6-3c27-b1a9-d340b9dd8ef4 | -15.5623 | -48.33224 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3b66618f-0eec-3cc1-8392-bf84160213b3 | -18.0444 | -47.74221 | 2025-09-02 04:17:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 07321741-5380-3ce3-a846-8418e2a3209a | -16.59444 | -48.98401 | 2025-09-02 04:17:00 | NOAA-20 | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b8073430-f88b-3ab3-a339-2af960ce8a7c | -16.73981 | -49.37932 | 2025-09-02 04:17:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 852a56a0-5820-3b94-bd61-5ffd95aec77b | -16.63151 | -44.58694 | 2025-09-02 04:17:00 | NOAA-20 | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0edd723a-6783-31ce-84f7-a46f865d350f | -18.08661 | -50.47438 | 2025-09-02 04:17:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 88bd840f-c7d0-3f29-a5be-ac317aa26224 | -14.7897 | -48.18927 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 142c5937-f0d1-32ce-90ed-47da4553d37d | -15.58435 | -48.37558 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2133c12c-9ce4-3ee9-9d97-a7f555fd14f3 | -14.59389 | -48.05096 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 37e96018-b25f-3a63-ad9c-3250cedf4e23 | -14.76248 | -48.15393 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25487c31-4092-3f07-9c54-e21ef8a786df | -14.58721 | -48.0559 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0905830-0652-3eb2-8b09-34e59ee670ed | -14.6039 | -48.0356 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7b60e6e-df01-3bde-a4e7-e2e296b870d4 | -16.40782 | -45.65128 | 2025-09-02 04:17:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34e62036-2dd5-33e5-a866-18c82aaae0d0 | -14.23105 | -51.66402 | 2025-09-02 04:17:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b060ee1d-84da-3bc5-8278-0af2cae7b646 | -15.11638 | -48.17882 | 2025-09-02 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c589af49-06ba-3429-bd72-67c39f78f6ab | -15.78859 | -42.12896 | 2025-09-02 04:17:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 08a271c9-bd0a-3e8c-8494-7d22cd10fc9f | -12.93158 | -57.00092 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0c62e849-4046-3b6b-b783-be77832578e8 | -14.81833 | -48.35521 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 745d46d7-d561-30bd-8cb7-1f604e081404 | -14.73786 | -46.74884 | 2025-09-02 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 923045a9-7880-3996-bc8b-86f0a3412244 | -14.55797 | -48.96366 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41673045-09af-3671-a1ee-ac5aebf03303 | -15.55935 | -48.34935 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 90a3ac8c-7d95-394d-bda3-f58a75a826d3 | -12.91748 | -56.94163 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 83545796-1373-3567-b86a-cc9b94c7b7d9 | -15.72724 | -48.94117 | 2025-09-02 04:17:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 429c166a-3589-3d8a-bec7-2fa13801e4dc | -17.23928 | -43.75776 | 2025-09-02 04:17:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f6760682-89d3-32a0-9b84-a514585efb3c | -14.62048 | -48.93689 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ce71ad7-ad8f-30cd-abf9-e4f7923a5b0b | -20.1195 | -46.01275 | 2025-09-02 04:17:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42d34858-d60a-3649-9996-94cb3ea483bb | -14.76603 | -48.15473 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d8cc4087-b05e-3d2a-9002-e9c1d2a3252b | -13.32398 | -51.79071 | 2025-09-02 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0cfc785a-260e-362b-bb62-095b83947bf0 | -14.61106 | -48.03666 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8924a222-f90d-360f-a6e0-e9b2cf0da3c2 | -15.09952 | -48.11293 | 2025-09-02 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bf3e099-6dcc-30e5-9b92-7f8f4d3181be | -12.91886 | -56.99817 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 30b23586-473d-39b3-839c-e3001520ca15 | -14.21225 | -48.05907 | 2025-09-02 04:17:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5297593f-9fbf-35bd-a2a8-b6a61eb2a983 | -15.57148 | -48.386 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b895766d-bc0d-3793-bd53-b629f1b18b49 | -13.90193 | -48.07336 | 2025-09-02 04:17:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b66f97d1-c220-394b-b48f-5365da181d3a | -14.22304 | -51.65763 | 2025-09-02 04:17:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| efbf88fb-19ea-3dd7-bd0c-01a520a5aa61 | -21.18239 | -45.6096 | 2025-09-02 04:17:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a2c146b-9f88-349b-a75a-43351faf0662 | -14.27023 | -45.2534 | 2025-09-02 04:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 246e67bd-bbdf-3d34-a9f0-0025438f4b5b | -14.63002 | -48.94853 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac44a6f9-f7d3-3d85-87d4-eedaaa716e0c | -17.61425 | -46.6455 | 2025-09-02 04:17:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| acca1728-e3ca-38b7-999d-bbec88c09d0c | -14.78803 | -48.18742 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 467e78ac-705a-35f6-a2b3-dbf927d45a1a | -14.20251 | -48.3787 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b70124ac-1a8a-33a4-ab28-bc8c03674c14 | -19.41691 | -43.79208 | 2025-09-02 04:17:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f0b035e-bb3a-3f92-9d36-0e79c4a2285a | -16.8845 | -44.66499 | 2025-09-02 04:17:00 | NOAA-20 | IBIAÍ | MINAS GERAIS | Brasil | 3129608 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a3d6819e-6e4d-3a81-83db-2d2f0abbe379 | -12.90248 | -56.94982 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e8822d60-5095-3aec-abfb-15719a640f4b | -14.72026 | -46.74976 | 2025-09-02 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65da6763-f752-3e9e-81d1-7f313becfda4 | -14.59172 | -48.06343 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bde6b7c5-c25f-35af-a074-9cc8cbda800f | -18.15878 | -47.91814 | 2025-09-02 04:17:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5340ee1c-3fc7-36bc-84b6-bcbdd484508c | -14.58624 | -54.56484 | 2025-09-02 04:17:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f787a8a3-079d-3a26-bd46-c31e43055266 | -15.55291 | -48.34391 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ad2e398-143f-3b43-a9e3-12be1643853d | -12.92162 | -56.95345 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ecf5a550-887a-3b5a-948e-378cca9a2c81 | -18.36937 | -46.02433 | 2025-09-02 04:17:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5b9d37d8-201a-3442-8a5f-42b89f44b933 | -14.49165 | -45.95137 | 2025-09-02 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 919b2ccd-ab31-38a2-a243-c79b9f5b4483 | -15.43487 | -43.31297 | 2025-09-02 04:17:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0b833ab3-4dec-3492-9c87-86a82110d728 | -17.70078 | -46.88751 | 2025-09-02 04:17:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ca2d673b-8fe6-39c3-9228-7a69c36fdde3 | -14.07195 | -50.15041 | 2025-09-02 04:17:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4bee7958-65f1-3a3a-b13e-4f69da840278 | -12.91784 | -56.93221 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1f1c88f-902f-3471-b2d0-3a859a57eed9 | -14.58444 | -54.54575 | 2025-09-02 04:17:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb46b4a5-ea62-325a-90c8-a1fb13e82b09 | -14.60163 | -48.06993 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3e190250-54a9-316e-a322-af699a0e3e50 | -15.55157 | -48.33038 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cd80f58c-4af1-3acc-8dfd-f6fda83adee6 | -15.6808 | -48.94648 | 2025-09-02 04:17:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12a9b86e-325d-379a-a0c2-ef2ee24f8f05 | -12.91882 | -56.95992 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ef2ccb2-606d-34bb-8432-9aea866ecdcf | -12.9177 | -56.96542 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 484df45c-58ab-3632-9589-8f6f2c4b58a6 | -12.92383 | -56.94298 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f4f807a2-77ea-30b2-bcad-29c3c7eff3dc | -14.47794 | -53.07378 | 2025-09-02 04:17:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4749ad73-eae3-3914-b4f3-681e4208c333 | -14.58203 | -54.54621 | 2025-09-02 04:17:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7134ea3b-cdfa-355a-b434-01157eb3ce80 | -14.6118 | -48.03239 | 2025-09-02 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c3afb95a-c8e2-3a2c-a0d3-74ff5481e945 | -15.56513 | -48.33721 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9c15670b-274f-3d36-a29e-0fced555ade5 | -15.55589 | -48.32667 | 2025-09-02 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1006569f-bb3f-356c-9eb6-c16faab65a90 | -14.26142 | -45.24463 | 2025-09-02 04:17:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7cea945-e03b-3784-a150-d14ea72affc1 | -12.90715 | -56.95212 | 2025-09-02 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README48.md)
