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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6cd0da75-1abd-3a0c-8d54-7983ea9b3ec8 | -3.04146 | -50.37281 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c41c7405-dabd-33db-ba27-feeb323594a3 | -4.64946 | -46.02312 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8c6c549-ef06-3181-ba75-0fbddb6aae42 | -3.01131 | -53.43553 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd6a0c75-5cf7-310f-9bf7-5733c2872fbb | -3.09334 | -50.22971 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7745239c-2679-3544-9c90-f806ed38ad87 | -11.09891 | -43.33981 | 2024-11-09 04:33:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 7a91422e-b639-3e64-91e3-708f9768827a | -3.97026 | -48.16578 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba5c7417-6842-3d9e-ad69-0d1018b12314 | -3.29431 | -46.41371 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 5e4468c8-c765-3d5a-bc1b-714459598b46 | -3.97139 | -48.18018 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 69b2f608-afa5-33de-8ed8-44e30720627b | -5.27321 | -44.76935 | 2024-11-09 04:33:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 792868a1-8b1b-3dbb-adac-e4d4bb982b19 | -3.01697 | -47.95204 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4eb4656d-45ba-340a-99e5-e459ad986649 | -2.9406 | -51.49887 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1df52d70-c639-3dc8-a372-f69db54e95bc | -4.1156 | -46.90762 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 896d5e85-bbff-3ca4-a3e8-13a3c0be4d70 | -5.73789 | -41.99573 | 2024-11-09 04:33:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f8a46435-5351-3b61-b9ae-c5875a8be98b | -3.16852 | -49.09732 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe6281c4-235f-3b78-a973-8b68620a5312 | -2.85894 | -49.83066 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1b2215ad-cbed-36ba-bc41-be07f9bfa820 | -3.25264 | -48.74611 | 2024-11-09 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88c77677-a806-343c-a1fd-087c4c5bd178 | -4.77954 | -48.6871 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 608b27ff-9913-38f7-af15-3a51420b9bb4 | -3.34827 | -47.11584 | 2024-11-09 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67eb47b9-aacb-36ee-8557-16e11be7729b | -2.8303 | -49.43881 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00457e01-060a-3b54-b462-9a16ea7338ed | -4.62568 | -48.90609 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f315f1cd-dd65-3a91-95fb-09d692f259f6 | -4.37016 | -48.15385 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4d8ea38-5b36-3927-b2bc-7dbe00e77a2d | -3.03426 | -50.37169 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47749ffe-5fb0-3a2d-af6c-178c19f6c0d7 | -3.76442 | -50.77983 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 49490b02-f4c9-3e5a-95b5-a3c2cf0fe2c7 | -3.78512 | -47.73985 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 401b7d0d-bae7-3e73-8397-e374a8734602 | -2.86933 | -50.31889 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ef6054a3-4047-3ee8-bce2-7d26d2687a11 | -3.19261 | -50.44168 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0b5b9f40-f3ba-3a25-b41f-00bb34097e67 | -2.6197 | -51.29556 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c3a6512d-dd74-3b6d-940a-a35cc35f23f4 | -8.85586 | -47.67461 | 2024-11-09 04:33:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fbf1ebf2-3a25-332d-a563-bec2907d8c1b | -3.02543 | -54.20496 | 2024-11-09 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5cf6bd5-b40a-363f-abfb-376fc86cfc87 | -4.40635 | -43.37784 | 2024-11-09 04:33:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8462ba5-a969-3c19-a4e9-a80f417e3e61 | -4.19814 | -48.55608 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 76f3e217-7055-32a4-a094-502241c4f039 | -3.24314 | -51.30658 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61f6ac7e-9e86-3056-99b1-d95d1ae87afd | -4.07799 | -54.97475 | 2024-11-09 04:33:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18579032-936c-3f2f-9308-a754893a2ff5 | -3.98076 | -48.16387 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c651e632-3efe-3b73-ab68-1cc632c56123 | -10.86573 | -44.90922 | 2024-11-09 04:33:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f41323b3-bff2-3930-a79d-44144918ad03 | -3.11138 | -53.71122 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a1226ef-cdc2-38f4-b29f-fb39f08020a0 | -6.18717 | -41.87931 | 2024-11-09 04:33:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 92bdd37c-497a-34a6-b78b-ff08f934c933 | -3.75451 | -47.15118 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2110257f-1fd6-33f6-979e-fdc28b7395a3 | -4.24482 | -47.86921 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0433f62e-2071-3b71-bc76-0491ab086bc1 | -4.49077 | -48.49063 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3ab81e45-1d68-39b8-869f-a22cd0cae08c | -3.04571 | -50.36924 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2c8504e9-7ebd-32cd-a478-d652da372424 | -3.06775 | -48.06311 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 584cc46b-eb84-347d-b4d3-a03b182b950d | -3.08982 | -51.29417 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a7acafe-881b-36ea-b207-ffe91ee9cee5 | -4.38664 | -46.80432 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1bb5178-75cc-38b0-b246-e1fc47f61d3b | -2.36413 | -54.75465 | 2024-11-09 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| afe0ebee-1fbe-3882-bc40-f91d9e3c5b81 | -4.24021 | -46.01275 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b306823-a8eb-3a48-87c9-931960cdd0d2 | -8.85199 | -47.67762 | 2024-11-09 04:33:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 99910426-a656-310a-93ab-feed9c340599 | -3.96582 | -48.1721 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| adefe5f8-550e-377b-94dc-b13eb324ed32 | -3.10784 | -51.13334 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a984441-bea4-36c7-9c7a-f1dcc48a1dcf | -5.76555 | -45.29942 | 2024-11-09 04:33:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e1b570b-fb3e-302b-a71f-cd62e68ed4b3 | -3.04931 | -54.46716 | 2024-11-09 04:33:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a4995a4-a3be-32d2-abd2-9e164c53b7f0 | -4.61021 | -49.57435 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1846f012-bdec-3aa2-b025-d1f994c74862 | -4.23547 | -47.55765 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a93686b6-c4f2-3a2d-89c4-fad9b0d62103 | -4.39051 | -50.97016 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c39e840d-d8cc-3d56-8d12-d64bb2d703e2 | -5.13845 | -48.24369 | 2024-11-09 04:33:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b847859-4830-31b0-a48a-975f716dea2e | -3.27133 | -46.32098 | 2024-11-09 04:33:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e270f7a-d68c-31a2-a1d8-0d90e7b206ae | -3.33728 | -50.08383 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2604c662-1a54-3147-bcda-8887de549717 | -4.14754 | -46.8984 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b67804e5-4347-3516-8572-074866f0d405 | -3.04276 | -50.36454 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 398a7b52-64a4-35d1-9ef9-65c5f97125b6 | -2.15905 | -53.65559 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a796037e-b6f5-36bd-a204-d6889df3e77a | -4.95334 | -48.44884 | 2024-11-09 04:33:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1d06f094-6cef-3ca6-8e5c-67921cdabcba | -4.9554 | -49.49923 | 2024-11-09 04:33:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8953b3f-ece5-3d04-b550-6465e3f663a2 | -2.97861 | -50.2924 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dabc516c-b0cb-329e-abb5-09508f403354 | -2.92712 | -51.04797 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abba1506-a994-3582-a9db-d96608a15b40 | -4.11605 | -46.88288 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c75d49b1-c901-3d7a-9939-5f546d005b2c | -4.25206 | -47.58132 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 4c52e334-5df9-3ae5-80f1-5365022a3a20 | -4.40534 | -46.28663 | 2024-11-09 04:33:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aecbb745-2765-398f-924d-fb5135c491a7 | -5.66054 | -45.20433 | 2024-11-09 04:33:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01cf308a-e745-3d73-97dd-3fd4bd6332bc | -4.42663 | -45.61946 | 2024-11-09 04:33:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fa0256e-b13c-3fa6-b6db-d6116f4c0546 | -4.37727 | -48.58437 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81d8dc01-cb97-374f-bd8f-5f1d93f63dfb | -3.77071 | -51.38044 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 288072a3-6b1d-3b52-b8e5-1e02deffcee7 | -4.03513 | -47.14235 | 2024-11-09 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a51dd12f-9e6d-30b7-8517-72934c31c8e0 | -4.13247 | -48.23774 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c23b3186-aac3-3b25-9140-edfa088fca6e | -3.88105 | -53.38974 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b9bd928-f541-376b-b6ea-dcf72ca20633 | -6.27383 | -41.65508 | 2024-11-09 04:33:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 47b898a5-cd5e-3172-b85e-231dbfb61fd6 | -3.23506 | -50.15506 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f3e3cbed-7389-384d-b630-29852039a60c | -3.73004 | -50.16775 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcd9c10d-3308-3dec-90a2-d2a2cfa2de88 | -3.84186 | -50.03507 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6921022b-3475-3ec9-8cd3-620853d2c107 | -4.84785 | -48.6438 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c31a32b8-66f2-3f0f-a526-2f763df74754 | -3.02128 | -48.0773 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 338e990f-9c67-3a1f-b22c-b3065b4a6a9d | -4.09609 | -48.31779 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4cda975-ba44-395d-9c45-950a4b772c12 | -9.12544 | -43.17974 | 2024-11-09 04:33:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6483a525-d47d-3435-a230-cbfccaa4005b | -3.02018 | -48.08426 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f8bb809-4e11-3c49-9172-d7cce3954bbc | -4.50981 | -48.21889 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ab5a861-5b69-3d95-9c02-3af4e2b73f10 | -4.08969 | -48.51035 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2ab1cc4d-eb4f-32f0-bb61-d9c52bb320da | -3.2349 | -46.53288 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59abb2b4-7d1c-3da1-b8f0-c9372f1aafb9 | -3.24251 | -50.26819 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 13aa19d6-81ba-33df-807e-19b6829bb06e | -3.83647 | -50.04632 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65bd2ffb-aed4-3301-b2b8-3073307a0e84 | -2.87109 | -49.22565 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5c8f06f-995c-372a-8835-7aecb9b62699 | -5.45077 | -44.82 | 2024-11-09 04:33:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 973d9f7c-dfa5-3a1f-bd00-e80b12151d7f | -2.6969 | -51.6885 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0359ad9-8a0f-36ef-b8ad-e8ff94e49c20 | -3.03726 | -48.04057 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc2992c4-f493-3487-8503-44d943190cf0 | -2.66738 | -49.87052 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a5d51fce-86b2-3681-98be-3fb2e257f31a | -4.24653 | -47.57343 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 13c4e1a9-c31d-3155-b74f-697d54dc5ce1 | -5.02663 | -42.95397 | 2024-11-09 04:33:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6c528b9-dc67-3af1-a539-57f0fde5e5b6 | -3.63731 | -45.89136 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55ce89ae-784c-32c1-b9e7-af6f6cd3fc97 | -4.59854 | -49.49268 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c6f18c62-0268-3aa2-8ab1-c2dbceef9ff3 | -3.58699 | -50.26963 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1915cf62-5151-328d-b770-26c1c329cade | -3.16959 | -48.36973 | 2024-11-09 04:33:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a3a9624-b68e-3c3a-8c35-ba40f6c17e2d | -2.18276 | -53.73786 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README64.md)
