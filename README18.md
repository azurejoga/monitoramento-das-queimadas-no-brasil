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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3ad1c0e-9aa7-3c1f-9b1d-bbedc0d25d50 | -3.8036 | -51.1852 | 2024-10-30 00:55:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 1751d478-d9f1-3764-b7ae-a90ea5d742df | -3.8037 | -51.1644 | 2024-10-30 00:55:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 193.0 |
| 12912aeb-8cf4-3df1-95c6-cdb33a390932 | -3.8038 | -51.1436 | 2024-10-30 00:55:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 240a8cd6-6e3b-3fbe-9d56-338b6063441e | -3.9326 | -41.4957 | 2024-10-30 00:55:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 113.2 |
| fffbf933-48f6-31a1-a4a1-be9bcf0638a5 | -3.9327 | -41.4717 | 2024-10-30 00:55:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 63.1 |
| 681da733-2db5-34d4-a5ab-187bcae3d3f0 | -3.8221 | -51.1637 | 2024-10-30 00:55:28 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 9283b5aa-4269-3485-812f-f89e94ee10df | -3.9486 | -48.1291 | 2024-10-30 00:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 5d6ff13b-14c3-324a-93ad-fb5a74c15d79 | -4.0705 | -46.2836 | 2024-10-30 00:55:29 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |
| a9d8e9d6-f17a-371b-9bbe-f1386e055fe4 | -4.2561 | -43.46 | 2024-10-30 00:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 1bc3f186-9369-3f96-8cfc-3cb95ff4b1b9 | -4.2563 | -43.4368 | 2024-10-30 00:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 162.6 |
| 09831567-b6af-3ba6-bb38-3adeb7993e3c | -4.2748 | -43.4589 | 2024-10-30 00:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 070b4807-c0f6-3910-91e8-dd56ffa6c7b4 | -4.2749 | -43.4357 | 2024-10-30 00:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 28c6f8c1-066b-36af-8004-68563ef1e62d | -4.3473 | -43.779 | 2024-10-30 00:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| a3eae20c-1b46-376e-84bf-1f5db1265c3a | -4.2496 | -50.6677 | 2024-10-30 00:55:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 47a2aa67-6f16-3aa9-8c3f-8bf2cee6fbf2 | -4.2679 | -50.6879 | 2024-10-30 00:55:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 8a4c79da-92cb-315f-aaab-48f8d74c16b5 | -4.2681 | -50.6669 | 2024-10-30 00:55:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| f500ef53-1de4-334a-a3a6-c11badcf1803 | -4.4971 | -46.4618 | 2024-10-30 00:55:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 98.2 |
| f5a14267-f86d-3c9c-b05a-871d4cd3fc85 | -4.4972 | -46.4396 | 2024-10-30 00:55:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 8aa440e5-b794-32bf-9d21-68e72f1dceb2 | -4.9311 | -43.1857 | 2024-10-30 00:55:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 1a85d1d8-ec33-3db8-a96e-e8c17e2a6b2a | -4.9498 | -43.1845 | 2024-10-30 00:55:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| de1dca99-8627-3822-b616-8e54f77adf60 | -5.2306 | -47.9566 | 2024-10-30 00:55:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 44c99e05-71dd-3885-a1c3-1d4de0d1c209 | -5.2308 | -47.9349 | 2024-10-30 00:55:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 3781c839-767c-3f0f-b1b6-1e436026df91 | -5.9788 | -45.3621 | 2024-10-30 00:55:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 18efea68-e034-3538-bc59-cfedca53810a | -6.8408 | -59.0519 | 2024-10-30 00:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| c84fa226-383d-34a4-86c4-13dff404442b | -6.8409 | -59.0326 | 2024-10-30 00:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 2198a6f4-19b8-3b83-8fcc-b07c1f57de5b | -6.8592 | -59.0511 | 2024-10-30 00:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.5 |
| e1c3b41b-9422-38fd-a2ac-d13a93f58e84 | -6.8593 | -59.0318 | 2024-10-30 00:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 4775431a-02fc-3da2-9615-36cdfdf3d294 | -7.8736 | -46.9065 | 2024-10-30 00:55:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 82527280-84f4-3188-a564-acc0f0140b3f | -10.7175 | -44.916 | 2024-10-30 00:56:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 0825ccd4-23ff-37c3-abc8-a904af700643 | -12.899 | -45.0549 | 2024-10-30 00:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 1406a91b-13c7-347a-9e60-92421ec75dbe | -13.6891 | -46.1017 | 2024-10-30 00:56:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 8fd4fc7e-b91b-30e2-8fc7-3aab7f587b7f | -15.8211 | -42.4953 | 2024-10-30 00:56:34 | GOES-16 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 105.8 |
| b6e94075-9041-3f90-a965-69a824796af2 | -15.8217 | -42.4706 | 2024-10-30 00:56:34 | GOES-16 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 2d41c6e8-8c09-3db5-949e-1a1141fb5a21 | -18.2454 | -55.9793 | 2024-10-30 00:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.4 |
| 3597bcf6-fced-3929-b090-893dc31399a8 | -18.2652 | -55.9766 | 2024-10-30 00:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.4 |
| 48d4fe27-49a5-3e0d-8c7f-b4b849b34c98 | -19.5862 | -56.7136 | 2024-10-30 00:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 82.4 |
| 4eeffe0f-e8c5-3c7a-b54d-5272a833794b | -19.6063 | -56.7108 | 2024-10-30 00:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 57.6 |
| 839f46cb-a0a8-3e32-b267-eafd07fa3345 | -23.9917 | -54.1329 | 2024-10-30 00:57:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 74.3 |
| 22faa0a2-5869-3948-98ba-7584ed7637ee | -23.9923 | -54.1106 | 2024-10-30 00:57:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 180.4 |
| 5b566fb6-aeaa-30ac-895a-ac1d6b3eb397 | -3.0734 | -54.167 | 2024-10-30 01:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 86e4a91c-26ed-33ab-9bb8-c840e6bb415d | -3.0913 | -54.287 | 2024-10-30 01:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 8c483a3f-8e38-359b-85be-a388617b83af | -3.0914 | -54.2669 | 2024-10-30 01:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 70815866-e274-35c8-94c7-4b2a1db8dc74 | -3.1028 | -51.1041 | 2024-10-30 01:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 5555a2ea-f442-3afb-93f8-ec4db00338a5 | -3.1097 | -54.2865 | 2024-10-30 01:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 0ff3ce44-9240-3501-a517-2d3180f891c0 | -3.1098 | -54.2665 | 2024-10-30 01:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| ea2c6480-bcb5-348d-91ce-fdb60685e1e9 | -3.1213 | -51.1036 | 2024-10-30 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 3afd40ea-0c19-3d1d-ac61-be186e711f18 | -3.16 | -50.6231 | 2024-10-30 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 006da46c-d258-3980-97ad-3bda71bc3300 | -3.1601 | -50.6021 | 2024-10-30 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 15d03559-b032-3af7-a579-13ec441a6736 | -3.1602 | -50.5812 | 2024-10-30 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 28f731bb-a009-3dba-afea-928c81467429 | -3.1786 | -50.6016 | 2024-10-30 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 369a338a-fc0d-30a8-96d0-3d43924d72c2 | -3.1787 | -50.5807 | 2024-10-30 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 4a542a62-3573-38be-accd-71ddba930ee8 | -3.234 | -50.5999 | 2024-10-30 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 1cd1d6e5-f3aa-3fdf-9c96-21f1dc41ffff | -3.234 | -50.5789 | 2024-10-30 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| ab37f406-423c-3ae4-84ed-e7d4c22c38cb | -3.2356 | -50.2015 | 2024-10-30 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| cb8825aa-f2e4-371b-b88b-f22b06eef2b9 | -3.2357 | -50.1805 | 2024-10-30 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 803ec575-b071-3b3a-88e2-26f11fd8e5b2 | -3.2534 | -50.3689 | 2024-10-30 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 18a2794f-969d-36ca-bacf-4d6145eb8fb0 | -3.2535 | -50.3479 | 2024-10-30 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 61977e10-ad58-30e3-a120-311363b6680c | -3.2719 | -50.3473 | 2024-10-30 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| e536b8c0-a04c-3682-8ead-c935f49abf1a | -3.4617 | -41.9983 | 2024-10-30 01:05:25 | GOES-16 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 51.5 |
| 75d907f6-577c-3338-9e33-47feb949afae | -3.3383 | -44.1058 | 2024-10-30 01:05:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 1861413e-a0f0-3dd0-bc64-b319965ecc61 | -3.5631 | -47.3847 | 2024-10-30 01:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 270.7 |
| 3f392cc4-42ef-3a38-bc43-52b53d3f58c1 | -3.5632 | -47.3629 | 2024-10-30 01:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 174.0 |
| 42b7245e-5e91-3c87-961b-eda3ea969a43 | -3.5688 | -50.043 | 2024-10-30 01:05:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 182dffd6-fd3d-3502-b775-964730d90b23 | -3.5817 | -47.384 | 2024-10-30 01:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 268.4 |
| bb6d915d-af69-352e-ac80-e3cc88f5c0ee | -3.5818 | -47.3621 | 2024-10-30 01:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 181.2 |
| 7716fa2e-28b7-3c9e-a889-4dc1e7dd5a48 | -3.8036 | -51.1852 | 2024-10-30 01:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 0368d045-c030-308f-84c7-67a87ca3a144 | -3.8037 | -51.1644 | 2024-10-30 01:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 1464803c-923a-3d9c-8490-5ffd82840e68 | -3.8038 | -51.1436 | 2024-10-30 01:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| e8c43c79-2fd5-3b03-89c1-a0163a3cfbad | -3.9326 | -41.4957 | 2024-10-30 01:05:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 99.5 |
| ea282ed8-1b6a-3e50-984c-7015ee3fe82d | -3.9327 | -41.4717 | 2024-10-30 01:05:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 67.8 |
| 4eccf677-5cf2-3953-903e-a671d71afa53 | -3.8221 | -51.1637 | 2024-10-30 01:05:28 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 99d083a6-340e-386a-86d1-898673a1ee66 | -3.9486 | -48.1291 | 2024-10-30 01:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 3bbcf3ef-0f08-3481-901f-04e2d12792b5 | -4.0705 | -46.2836 | 2024-10-30 01:05:29 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 8bb6effd-3f36-321f-94d0-1d36fbd7852b | -4.2749 | -43.4357 | 2024-10-30 01:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 922b81a4-8888-3165-ba0b-da4c75948af7 | -4.2561 | -43.46 | 2024-10-30 01:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 4d68b18f-25fc-367e-b682-bacfb3a42244 | -4.2563 | -43.4368 | 2024-10-30 01:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 25c5079f-67ac-330c-b98c-d24c4168275b | -4.2748 | -43.4589 | 2024-10-30 01:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 7f09b988-d2ad-3ef0-8ff8-2dc457bce02a | -4.3473 | -43.779 | 2024-10-30 01:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 8d6e07d8-0703-3450-9d06-bd8f94a10c8f | -4.2496 | -50.6677 | 2024-10-30 01:05:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 14b6b251-4549-391a-a1aa-9f364bba9631 | -4.2681 | -50.6669 | 2024-10-30 01:05:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 97d50d1e-ee65-3cc3-8831-de086ba8b606 | -4.4971 | -46.4618 | 2024-10-30 01:05:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 50ae04d4-9480-3804-b09b-2708e3d48b49 | -4.4972 | -46.4396 | 2024-10-30 01:05:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 3469e3c3-5573-30e6-8a8c-2dfb193ddeb5 | -4.9311 | -43.1857 | 2024-10-30 01:05:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 47.3 |
| c7adbbfc-623a-3258-8567-30fe80d50f89 | -5.2306 | -47.9566 | 2024-10-30 01:05:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 53.0 |
| ec8e9109-dbb3-344a-b399-c16004386636 | -5.2308 | -47.9349 | 2024-10-30 01:05:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 8a9a0007-ea27-3bea-ae21-6fc0869bad90 | -5.9788 | -45.3621 | 2024-10-30 01:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| fba346b1-b523-3d69-90e3-7d086fac473f | -6.8408 | -59.0519 | 2024-10-30 01:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 485cb7ec-83a3-36c0-90cf-a34199c739de | -6.8409 | -59.0326 | 2024-10-30 01:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 0e4d7b11-8a40-37e6-94ed-441f28ac01f2 | -6.8592 | -59.0511 | 2024-10-30 01:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 5b0ea69f-f1e9-393a-9aa0-ab050eb81e3e | -6.8593 | -59.0318 | 2024-10-30 01:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 92a688f9-8e34-37ff-a388-d2bc1d34c97e | -7.8736 | -46.9065 | 2024-10-30 01:05:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 282e6a09-6ff6-3626-87b9-c7a1689443a3 | -10.3434 | -49.6536 | 2024-10-30 01:06:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 4c4a9c3d-ae86-39a4-ba50-8871dfc9a221 | -10.6984 | -44.9186 | 2024-10-30 01:06:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 64.7 |
| a38b0602-c0e4-36ee-a2b5-616244bcaec2 | -10.7171 | -44.9391 | 2024-10-30 01:06:06 | GOES-16 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 107.0 |
| f7b93767-671d-3ddd-a326-a469899a1867 | -10.7175 | -44.916 | 2024-10-30 01:06:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 186.4 |
| 31a5fd2a-0b8e-3d29-8bb9-3f1ae937dd36 | -12.899 | -45.0549 | 2024-10-30 01:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| b49f39d8-379a-326a-98f2-e4273696041a | -15.8211 | -42.4953 | 2024-10-30 01:06:34 | GOES-16 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 132.1 |
| d9704d3c-d943-31c9-9ecc-02b434718875 | -15.8217 | -42.4706 | 2024-10-30 01:06:34 | GOES-16 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 7c8fa45c-6b12-303d-8899-0f71349f3d8f | -19.5862 | -56.7136 | 2024-10-30 01:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 69.2 |
| d8ff1b72-b8d7-3160-bd7c-8b2337f85627 | -19.6063 | -56.7108 | 2024-10-30 01:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 70.1 |


[Clique aqui para ver as próximas entradas](README19.md)
