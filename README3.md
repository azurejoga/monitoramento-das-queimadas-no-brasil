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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13eb9637-2947-33e7-bb22-a868fc715cd8 | -5.5213 | -39.198299 | 2024-11-27 00:17:00 | METOP-C | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 0f535f38-2b9a-3105-ac90-90353d32da3b | -22.882099 | -43.726101 | 2024-11-27 00:17:00 | METOP-C | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 95c8cb06-346d-3739-a907-5748699f47a8 | -20.3517 | -47.479 | 2024-11-27 00:17:00 | METOP-C | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b272a5cc-6147-3744-9c35-25f6ac3c89b3 | -1.9872 | -46.041199 | 2024-11-27 00:17:00 | METOP-C | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dc89f619-111b-30d9-ab85-8afa39060612 | -3.4737 | -50.481701 | 2024-11-27 00:17:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bddf0fd2-3f41-3c7a-88c9-be44ca6dc9f6 | -19.1805 | -45.378799 | 2024-11-27 00:17:00 | METOP-C | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| edd2ac36-7e90-3c7c-9d7f-af23f95e7100 | -3.4824 | -52.126202 | 2024-11-27 00:17:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91458df9-e328-3bcb-aa11-b5f1e18ca6b4 | -3.9453 | -46.7262 | 2024-11-27 00:17:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f03b6a27-114c-3825-ab30-12cb9a4a8adc | -3.9577 | -48.060699 | 2024-11-27 00:17:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a37c46a2-b0ff-307b-8874-3285ed5b62b5 | -20.218901 | -40.240501 | 2024-11-27 00:17:00 | METOP-C | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| efa199d4-6cf7-329b-8c0e-15e2ade6ffd3 | -2.3202 | -47.639599 | 2024-11-27 00:17:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75dc7dd3-9d5c-3565-8a1b-478fe6a19ad0 | -2.6925 | -46.287102 | 2024-11-27 00:17:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6c171ed0-8ce0-356c-9b5a-63472cb02ce3 | -3.3636 | -44.167702 | 2024-11-27 00:17:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d69cdfe-d98c-3bc9-83d5-85a76fdca092 | -4.6941 | -46.578602 | 2024-11-27 00:17:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 122bc989-3ec2-3756-9fc4-67eb6b5a211f | -2.6908 | -46.279701 | 2024-11-27 00:17:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 75417636-db35-3e92-bc6e-eb915de9bc3d | -2.684 | -46.249802 | 2024-11-27 00:17:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a8ee03b2-6a50-3ec0-886f-19dd63931753 | -2.7817 | -46.815498 | 2024-11-27 00:17:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d606882e-3f16-3a69-9b5c-de1d3793fd25 | -2.076 | -46.566101 | 2024-11-27 00:17:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b14e92e5-3c4e-3319-a441-ba3d2c113002 | -3.6942 | -42.285301 | 2024-11-27 00:17:00 | METOP-C | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b4cbd03d-a74b-348f-a95b-e310a5603453 | -2.9716 | -45.476101 | 2024-11-27 00:17:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3d379cab-46b2-3ba1-8522-7c248891515d | -1.9151 | -45.725601 | 2024-11-27 00:17:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a32ee2c8-144a-33cc-a99b-ef244b146e54 | -4.6789 | -47.9333 | 2024-11-27 00:17:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a079ebe-517e-338a-877e-10e48243fc7b | -4.1893 | -50.8955 | 2024-11-27 00:17:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6869d21-503d-3196-8820-b97a8db9a2e6 | -2.5768 | -48.363098 | 2024-11-27 00:17:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32788b49-af9e-31fd-9c0b-cfeffa0908ed | -2.9684 | -45.461899 | 2024-11-27 00:17:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 773506ef-50ed-376c-872c-b24eef1768fa | -1.9168 | -45.7327 | 2024-11-27 00:17:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2d36d78b-2802-3df5-b50a-3fa24d942a29 | -2.5176 | -45.384102 | 2024-11-27 00:17:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aefb346b-be11-3196-b7f0-00fed5437271 | -3.9471 | -46.7342 | 2024-11-27 00:17:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fcd299ac-db83-39e4-893d-e58a693d6969 | -5.5235 | -39.207699 | 2024-11-27 00:17:00 | METOP-C | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7a4e2b5e-a1ed-3e1b-b44b-620669cec123 | -4.1148 | -43.799301 | 2024-11-27 00:17:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4b475508-c02e-3345-86b3-9ca14283dbda | -3.3652 | -44.1745 | 2024-11-27 00:17:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71ad824c-775a-320b-b063-6e35b48014a6 | -3.1367 | -48.430698 | 2024-11-27 00:17:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74f6ea1e-0d02-37f9-bfaf-514dfc6fbcc0 | -5.5557 | -42.93 | 2024-11-27 00:17:00 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7ffcaa86-f63e-30ec-b4d6-fc320a7ce5f8 | -11.9919 | -49.5257 | 2024-11-27 00:17:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 658daf91-0f77-3225-9350-403b59c078e0 | -2.7951 | -46.829201 | 2024-11-27 00:17:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b796727-3ee9-3cb9-88ba-ad4921fbffe7 | -3.95 | -48.0723 | 2024-11-27 00:17:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3458b68b-8847-3045-bd3c-37e97cb4dc00 | -3.1345 | -48.421001 | 2024-11-27 00:17:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa952d6d-2378-31b8-8f3c-d66bf6b86495 | -19.1784 | -45.368 | 2024-11-27 00:17:00 | METOP-C | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 82b9388b-93ab-37d7-9acf-cb64d34b3ead | -20.220501 | -40.247799 | 2024-11-27 00:17:00 | METOP-C | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8c8f974e-3db1-37fd-94de-a783fadf4c2f | -1.8586 | -45.523201 | 2024-11-27 00:17:00 | METOP-C | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 23fa5c15-5458-3080-ad71-9204bb870036 | -16.816799 | -46.6609 | 2024-11-27 00:17:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5c2f7c13-301a-3356-9a30-e38f98974eaf | -3.1465 | -48.428501 | 2024-11-27 00:17:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6976194-27bf-3bbc-ab34-7df8a64f9125 | -4.1796 | -50.897598 | 2024-11-27 00:17:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83c11bf4-829d-3c68-a88a-e9b246113835 | -3.4863 | -52.1436 | 2024-11-27 00:17:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b3104f3-bef7-33e7-827f-403042308480 | -3.1389 | -48.440399 | 2024-11-27 00:17:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 749725f1-b86d-31fc-827d-2bc84a2236c9 | -2.757 | -49.2062 | 2024-11-27 00:17:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e127f30-c9d7-35e0-bbcd-b35030a57442 | -4.2115 | -50.8782 | 2024-11-27 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| f13e0eb6-ae1a-33b0-a492-f74b18dba379 | -2.6988 | -45.6481 | 2024-11-27 00:20:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 825a7600-945c-3fc3-9379-c060add26f33 | -3.5226 | -52.1448 | 2024-11-27 00:20:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 193.9 |
| 1a9511f4-5393-3174-970e-2e02d14e4796 | -1.6444 | -52.4951 | 2024-11-27 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| f0b4b377-7aea-339d-b5af-f089a941ae15 | -9.3986 | -35.9196 | 2024-11-27 00:20:00 | GOES-16 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 77.9 |
| 4751109c-51ee-3ebc-83cf-f6c5311500f6 | -2.8346 | -54.1326 | 2024-11-27 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| e27285ff-4788-3262-a678-7c8dfc99b5f9 | -1.6629 | -52.4336 | 2024-11-27 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 8c20a5ba-00fd-3f46-89da-c78088391d27 | -2.6987 | -45.6705 | 2024-11-27 00:20:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 131.2 |
| d390e1c5-fe98-348b-8e7d-8b53c168b92a | -2.8424 | -46.8413 | 2024-11-27 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| fb939b93-644d-3baf-8942-d461230fb5cd | -4.2114 | -50.899 | 2024-11-27 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 4b73974c-bf75-3bfa-8ef3-446da51a70fa | -2.8347 | -54.1125 | 2024-11-27 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 9fb1f5e1-47c8-30d6-941d-39afc214e655 | -3.0154 | -45.4577 | 2024-11-27 00:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 229.5 |
| 72ff6359-4e84-3153-95cf-e65dbee751f7 | -2.8425 | -46.8193 | 2024-11-27 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| bac4049f-4fee-3d5b-9813-f972f8e51a71 | -3.5226 | -52.1653 | 2024-11-27 00:20:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 151.8 |
| 2e80440f-5d03-3f5a-91a4-11573c2f8a9f | -1.9562 | -45.7137 | 2024-11-27 00:20:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 73.7 |
| b3820683-93e1-390f-a47a-ce9416694b6d | -4.7383 | -46.5595 | 2024-11-27 00:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 0a39fc26-f318-35be-8bd6-06240a88bd4f | -2.6802 | -45.6711 | 2024-11-27 00:20:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 9ca59661-8e61-30b1-92ec-bf49d94f5e37 | -4.1417 | -43.8135 | 2024-11-27 00:20:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| be092c49-dc0a-3ff3-b6c7-f6ed2d30bc0f | -1.9561 | -45.7361 | 2024-11-27 00:20:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 9c7a463e-0fd9-33d5-b33c-64bbc2ed1d4c | -3.0393 | -48.5082 | 2024-11-27 00:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 94cd0ed2-f343-3faf-84cf-43a24325a942 | -5.9788 | -45.3621 | 2024-11-27 00:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 67ceb345-72d3-3fa0-b185-c130d942a8b6 | -3.9674 | -48.0851 | 2024-11-27 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 9a6dcf15-9b92-3a19-9949-31098b37cc60 | -2.6803 | -45.6487 | 2024-11-27 00:20:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 3a470ec2-ed28-3fb3-831a-9e96bddbccba | -3.9859 | -48.0843 | 2024-11-27 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 00768ca7-9491-3392-99e3-284a09943a14 | -2.824 | -46.8199 | 2024-11-27 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 7a1203e0-6e9f-3d3a-a201-3f4ed270ac9b | -1.6629 | -52.454 | 2024-11-27 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 42fd3646-7379-3d19-9d75-e501c1b6a58e | -3.0153 | -45.4802 | 2024-11-27 00:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 148.5 |
| 31ee2a71-0d31-3616-93b6-8a3ec6acad75 | -3.5411 | -52.1442 | 2024-11-27 00:20:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| a5d26a72-9f7d-3b7e-99fa-83a92328981c | -2.8163 | -54.133 | 2024-11-27 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 31c04073-329a-321d-bc72-989026012323 | -4.7197 | -46.5605 | 2024-11-27 00:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 107.1 |
| f54a55b3-6a44-32f8-9e62-449e28f5246a | -1.6624 | -52.7192 | 2024-11-27 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 4fbf5314-b2a6-3034-ba19-ab7d49341eac | -2.8611 | -46.8186 | 2024-11-27 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 721c699c-5397-3c3a-9c09-7311c7e18e0b | -2.9967 | -45.4809 | 2024-11-27 00:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 201.4 |
| 325e7715-0c7e-3dd2-a6dd-691c6f7d3b1f | -2.9968 | -45.4584 | 2024-11-27 00:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 322.5 |
| 9afb8343-bea6-3eae-83bf-8f5533f481f9 | -3.7796 | -52.403 | 2024-11-27 00:20:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 760b2382-2c07-39e5-a052-4540c227b550 | -4.7381 | -46.5816 | 2024-11-27 00:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 4f03304d-de55-3267-9c8b-b291381b3c08 | -3.9675 | -48.0634 | 2024-11-27 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| ce4dbee9-fbae-3191-a295-3e863d0dc361 | -3.541 | -52.1647 | 2024-11-27 00:20:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| f841192b-fb54-36ef-828f-190f3655828d | -2.8239 | -46.8419 | 2024-11-27 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 7a6920d1-5664-3e9f-87ad-c6ba715c83d9 | -4.7195 | -46.5827 | 2024-11-27 00:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 99.5 |
| bf2c8069-54f9-3fe3-b962-dbd10be9832e | -1.4205 | -47.125 | 2024-11-27 00:21:00 | METOP-C | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bf79f61-d515-3381-9801-7d7b95c0c3e8 | -2.9226 | -45.487 | 2024-11-27 00:21:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f92d8290-9622-321b-8572-caca3eb6594e | -3.3564 | -46.306801 | 2024-11-27 00:21:00 | METOP-C | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 13af81b8-dda2-3d17-be04-1bb794c02cf5 | -2.5234 | -46.4035 | 2024-11-27 00:21:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 41e867cb-eb18-3126-bf5b-d769c4c3f2f9 | -2.805 | -46.827 | 2024-11-27 00:21:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bfc4a45-f5a2-32b0-a956-55c052ce7d80 | -5.2984 | -43.067299 | 2024-11-27 00:21:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b1774809-360a-360d-bb9a-c4862d8f6571 | -3.5485 | -41.967602 | 2024-11-27 00:21:00 | METOP-C | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f9cae182-8f88-320b-87da-3a5aadd595df | -9.3692 | -35.912701 | 2024-11-27 00:21:00 | METOP-C | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f40d2062-1a26-3381-a63e-76b0b7935097 | -1.1174 | -53.662998 | 2024-11-27 00:21:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbb92fc0-8b9a-33d5-bce5-f73a368d62af | -3.7438 | -52.385899 | 2024-11-27 00:21:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21f59280-b9ed-382d-89a4-a34306271d61 | -6.1668 | -44.433201 | 2024-11-27 00:21:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94f2b1d6-2978-391c-bef9-9a38e6204ba0 | -2.8772 | -45.378101 | 2024-11-27 00:21:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5da26ab5-0fd9-38c5-90ea-2702df3017d0 | -1.603 | -52.480999 | 2024-11-27 00:21:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7524c22b-d728-36b2-a5a6-23ba97717473 | -2.0629 | -46.553001 | 2024-11-27 00:21:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
