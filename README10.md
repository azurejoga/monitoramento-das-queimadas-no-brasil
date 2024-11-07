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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8e374e1-99d2-3949-9732-23fcd8b990d9 | -5.034 | -46.8521 | 2024-11-07 00:40:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 139.8 |
| 60cede85-8328-329a-90b0-b42bf8a12b0d | -3.7033 | -48.9986 | 2024-11-07 00:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| d2bd2bb2-46a4-363e-93b1-c21e47e25fae | -5.0526 | -46.851 | 2024-11-07 00:40:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 108.1 |
| b1786163-0dd3-3086-aad6-359c41a855d9 | -2.8016 | -52.9414 | 2024-11-07 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 4d9b0e72-a814-392a-a638-1700473f93ab | -3.0207 | -53.443 | 2024-11-07 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 10034f1d-142f-3f6b-bafc-97f7cfd7be29 | -5.0528 | -46.8289 | 2024-11-07 00:40:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 55.3 |
| b04baf86-6be6-3a5c-94f7-c0dc4be7b73a | -2.8167 | -48.6653 | 2024-11-07 00:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 9920ec59-aa54-3dcd-a011-173177ac3300 | -1.1831 | -53.8985 | 2024-11-07 00:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| ccc13949-3452-3b37-8b5c-2fbf0bb6f9d9 | -2.8722 | -48.6636 | 2024-11-07 00:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 386af160-c445-387c-8bfb-f38930e83326 | -2.8536 | -48.6856 | 2024-11-07 00:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 460f7f63-f8bb-39ea-ab77-a6bcf679b7d1 | -3.7033 | -48.9986 | 2024-11-07 00:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 22aa6bf6-8101-3d28-8eee-3ad561c679e0 | -3.9485 | -48.1508 | 2024-11-07 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| d6a037e8-bfbe-3144-be9b-442f3ca5b556 | -4.5031 | -42.8854 | 2024-11-07 00:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 009920d2-32b8-358b-918a-98a919dd440f | -6.0782 | -44.719 | 2024-11-07 00:50:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 70c46c5b-670f-3ff2-9896-4bef64bd38f2 | -3.967 | -48.15 | 2024-11-07 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| cd1d4e41-bceb-3e92-90a3-039b348ce3d1 | -2.7639 | -53.2265 | 2024-11-07 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 9b2b083a-c933-3cd5-9e0e-a9047db3db78 | -3.0207 | -53.443 | 2024-11-07 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 7b511cb3-46ed-3d17-969a-af1b65baec22 | -2.82 | -52.9613 | 2024-11-07 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| fcd1a1fc-8686-3a75-942f-6b089bb76947 | -5.9788 | -45.3621 | 2024-11-07 00:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 130.7 |
| ad914b53-dabf-3b87-8e5f-0441b8ea3952 | -17.293 | -57.5062 | 2024-11-07 00:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.7 |
| 64e9e7df-d31b-3e49-a7e9-aaa12373b7f6 | -5.0154 | -46.8531 | 2024-11-07 00:50:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 9b3810a7-aeb2-333d-85cb-a76221cd927f | -2.8352 | -48.6648 | 2024-11-07 00:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 29dbabd5-45be-3207-ab23-c1dc1d54014a | -1.2014 | -53.8983 | 2024-11-07 00:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 67e716d1-c139-3513-8548-d9ae1d2cec56 | -4.5218 | -42.8843 | 2024-11-07 00:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 42be68e0-d616-3c84-a4ab-cf121f311c74 | -2.82 | -52.9409 | 2024-11-07 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 31e57ac4-65e7-39d1-8896-425de0eff7fe | -2.603 | -51.7589 | 2024-11-07 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 52b4c6ee-a551-339e-aa99-e1e6a5bdd4f4 | -5.0155 | -46.8311 | 2024-11-07 00:50:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 51.1 |
| dc30a6bc-752c-323e-a755-6519a7b7e6bd | -2.8016 | -52.9414 | 2024-11-07 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 14a55817-6640-3bf9-8fbb-6d16467491e4 | -4.6653 | -46.3418 | 2024-11-07 00:50:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| df1110f1-b1f8-3ce0-b3d4-a36a7ceeee13 | -5.034 | -46.8521 | 2024-11-07 00:50:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 92.8 |
| d63b89f5-f4a0-3b78-944f-fbbaa1c5ffe0 | -2.4319 | -53.6584 | 2024-11-07 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 1a5aa3aa-c0fd-345b-9370-0eb340930925 | -5.1581 | -47.6997 | 2024-11-07 00:50:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 81.0 |
| a8fc8714-9db6-33e3-a55d-6aabfa9c3d2c | -3.4564 | -50.3832 | 2024-11-07 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 0e43d7e4-16a8-35ab-930d-bee90e3ada47 | -4.522 | -42.8608 | 2024-11-07 00:50:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| f488bd8b-d422-3d4c-8be5-f57f6638a95a | -3.9669 | -48.1716 | 2024-11-07 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 570e369b-affe-3988-beba-45a89ac4326e | -1.1466 | -53.7379 | 2024-11-07 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 502b5177-3dfc-33bd-bf04-9767ec9e2a23 | -5.1397 | -47.679 | 2024-11-07 00:50:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 61042864-ea61-3eb1-9a37-d2ccf9a17187 | -5.0526 | -46.851 | 2024-11-07 00:50:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 64.0 |
| ad7915cc-0bac-3501-8021-bba69c27f76b | -4.5033 | -42.862 | 2024-11-07 00:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 3d65b9ee-7ae7-3451-be79-225315350dc9 | -2.8537 | -48.6642 | 2024-11-07 00:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 7d05a738-baa9-3f3f-96f9-6773ce50815d | -5.9975 | -45.3607 | 2024-11-07 00:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 149b01e3-3309-3b68-bd0e-83c516c159ce | -5.1394 | -47.7226 | 2024-11-07 00:50:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 53.4 |
| a3ad3766-26b7-3679-b68a-2da691dcf0ef | -5.0342 | -46.83 | 2024-11-07 00:50:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 44c4a02c-6df7-34a2-a7fb-cf7d0b6412db | -1.1466 | -53.7177 | 2024-11-07 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| cc628e3a-df2a-3f08-92ff-a2f7b5594345 | -5.1395 | -47.7008 | 2024-11-07 00:50:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 149.6 |
| bfae1a11-51a1-35c5-ae81-481e3c6208b8 | -3.1617 | -50.2038 | 2024-11-07 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| d0bdd15d-584c-3cf1-8df7-6bb7d341d898 | -2.8351 | -48.6862 | 2024-11-07 00:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 6c12cb56-9752-3abf-8e7e-ae69fb264b9f | -3.7218 | -48.9979 | 2024-11-07 00:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| f15e88d4-f535-32e7-8f4d-d9f79db3e063 | -14.06903 | -44.14759 | 2024-11-07 00:54:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 1cbc3ecf-1e9a-37f2-93c9-907053d985ba | -10.67568 | -49.45105 | 2024-11-07 00:54:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 736673de-107d-36c0-a05b-5794d1005b92 | -8.93619 | -42.60456 | 2024-11-07 00:54:00 | TERRA_M-M | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 25.2 |
| 8fb24906-5d8b-3d0a-95c3-37561a05fa5c | -11.60755 | -44.12987 | 2024-11-07 00:54:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 80b9031d-e2df-38e5-98bd-3a7f16d77da4 | -10.87296 | -49.5482 | 2024-11-07 00:54:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e8c9d783-9d02-35dd-8b93-e4a03f9b5f81 | -10.13706 | -49.14645 | 2024-11-07 00:54:00 | TERRA_M-M | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dbf3f9c0-e211-3b2c-9abb-770c571c6f7c | -10.37056 | -49.17045 | 2024-11-07 00:54:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| efa74140-7c0a-3bdb-b59c-69e48421f4ae | -10.71556 | -49.47847 | 2024-11-07 00:54:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4894ec3c-ced2-37a7-9136-f0c15ad6ce28 | -9.14887 | -43.13604 | 2024-11-07 00:54:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 872dc17d-a358-39ae-bb55-05b45937ed6d | -13.51655 | -43.00838 | 2024-11-07 00:54:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| e711caa9-97c1-320b-b843-fc4e80269999 | -14.41093 | -43.17633 | 2024-11-07 00:54:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 044e242e-7f03-3e5c-b9ff-312de4ee9941 | -8.94341 | -42.609 | 2024-11-07 00:54:00 | TERRA_M-M | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 609c25b8-31d1-3a60-a454-8c6fc02c096f | -9.29718 | -43.13128 | 2024-11-07 00:54:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 23.2 |
| d9899d3f-1c93-3c70-9a5a-7e13fd841cd2 | -10.73243 | -49.53474 | 2024-11-07 00:54:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| a01e75c8-b7bc-37bd-9100-8eea466341a0 | -9.29734 | -43.12185 | 2024-11-07 00:54:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 30.6 |
| 5b025127-3255-37a6-b484-d1736053b7db | -10.73113 | -49.52512 | 2024-11-07 00:54:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b316fc05-0c8e-35ec-8cf8-30c4d200ac8c | -12.9879 | -43.44615 | 2024-11-07 00:54:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4ba33bf8-29c2-3d0d-80c4-c040c53f1cfe | -10.70652 | -48.79753 | 2024-11-07 00:54:00 | TERRA_M-M | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| f0e9c0a7-167f-30a7-b961-924c6b514af0 | -10.70528 | -48.78839 | 2024-11-07 00:54:00 | TERRA_M-M | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 091bc116-88fe-37cb-bdc6-e5f55b64a85b | -10.90919 | -48.93461 | 2024-11-07 00:54:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 853ca123-e069-38d9-97fb-064711d61b10 | -12.28019 | -51.22049 | 2024-11-07 00:54:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 124a4d63-c2c0-3039-9975-079d4f586e72 | -13.71907 | -42.88649 | 2024-11-07 00:54:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 2e3698ef-3137-3b23-9179-a7af2aa7992d | -10.46968 | -48.28117 | 2024-11-07 00:54:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8177428f-adae-3c15-ba71-07d40efc779b | -11.60942 | -44.14203 | 2024-11-07 00:54:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 56069538-bbae-3d9e-bbb5-39d4858d56a0 | -10.95364 | -44.40723 | 2024-11-07 00:54:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6caf18a8-d63a-32c6-823f-9535cc095237 | -8.9334 | -42.58726 | 2024-11-07 00:54:00 | TERRA_M-M | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| a843c7c4-a01c-3da0-836d-1c1167e71e2e | -12.054 | -51.21275 | 2024-11-07 00:54:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9391d8d3-948f-3ea4-ad02-72cf9f522fb9 | -12.45999 | -46.64346 | 2024-11-07 00:54:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 253f364b-f4a2-3e33-9922-c569de27d8ce | -12.27859 | -51.20815 | 2024-11-07 00:54:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1ccfc119-e15e-38bd-a615-8aed35c81e58 | -10.17998 | -48.85297 | 2024-11-07 00:54:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 3d8d63c4-1d7d-3d71-a08e-25bc78541a1c | -10.37181 | -49.17973 | 2024-11-07 00:54:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 96ba1814-0d38-3091-8f56-8b29735f9401 | -14.41295 | -43.18914 | 2024-11-07 00:54:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| aa57fbe6-ed92-3ff3-af45-a521f595bb06 | -8.94076 | -42.59161 | 2024-11-07 00:54:00 | TERRA_M-M | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 25.9 |
| d84638e2-f354-30d9-8067-eb99b0601c39 | -14.07161 | -44.1525 | 2024-11-07 00:54:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9deb69fe-7009-3fd5-b39e-fee79333d5d2 | -14.06984 | -44.14117 | 2024-11-07 00:54:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 8329c1f7-d946-31fc-b36f-d79aa785036d | -12.94029 | -49.1311 | 2024-11-07 00:54:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 59b76e4b-2b03-3973-a06d-0dc37bc13289 | -9.29969 | -43.13738 | 2024-11-07 00:54:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 988a1dbb-96e4-3409-bf90-ab8761d2baa4 | -9.74693 | -43.58643 | 2024-11-07 00:54:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 299bcb14-876e-37e4-bb5d-4f4cf8c95dbe | -12.64156 | -49.02024 | 2024-11-07 00:54:00 | TERRA_M-M | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 84f491fc-9f0f-3357-9d32-e08dfb7e76d9 | -12.46857 | -46.9594 | 2024-11-07 00:54:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 00b5ec46-ca1c-3184-bb61-a9f4b029d7b4 | -10.54725 | -49.04792 | 2024-11-07 00:54:00 | TERRA_M-M | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| df647ebe-aaac-3158-a3e6-e352ea157ed9 | -15.13519 | -43.40852 | 2024-11-07 00:54:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 7be4c63f-8603-3b9d-8abf-21faf619eed7 | -10.67438 | -49.4415 | 2024-11-07 00:54:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 18f5593d-e65c-39fc-91ea-726f81027f54 | -12.99835 | -43.44439 | 2024-11-07 00:54:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e983d3e4-0190-3738-966c-691b2ea198f4 | -12.05556 | -51.22503 | 2024-11-07 00:54:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ddfe68ac-c79e-3668-91c8-ca40337d2623 | -9.2947 | -43.11572 | 2024-11-07 00:54:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| ea7a00a6-c9fc-300f-ba98-c0062ba50bea | -12.46728 | -46.95032 | 2024-11-07 00:54:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| b4672ce5-43fc-331b-9df4-2e4236113f04 | -9.74843 | -43.57985 | 2024-11-07 00:54:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ec06e30c-5291-31b0-9f08-40c0dda96dc9 | -11.00568 | -48.69941 | 2024-11-07 00:54:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c3ed3c8a-e4ba-3f07-8246-24edc69bfaea | -14.07965 | -44.13955 | 2024-11-07 00:54:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b22dd9c1-7946-3b28-9626-4749caf6f858 | -2.66986 | -51.82826 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| d444ecdd-93a2-3e22-a858-0b9a5e6638a9 | -2.60801 | -49.25744 | 2024-11-07 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |


[Clique aqui para ver as próximas entradas](README11.md)
