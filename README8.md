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
| 5ac33444-32a6-37ea-ac6c-027bdd04ee6c | -2.7603 | -54.4149 | 2024-11-03 00:45:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 168.9 |
| 50005c28-ddb4-3bbc-ace3-512262bde1cb | -2.7876 | -51.6099 | 2024-11-03 00:45:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 834e3e18-6c63-397f-9f5f-a8e03f3dfffe | -3.0365 | -54.2081 | 2024-11-03 00:45:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| acd3a4db-c369-3738-b05f-adc91aa54f5d | -3.0397 | -53.2603 | 2024-11-03 00:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| f10d2674-1636-3672-a353-a4316b5716e7 | -3.055 | -54.1675 | 2024-11-03 00:45:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 6fabad63-92d4-301d-9013-9fe0ab71fa5a | -3.055 | -54.1474 | 2024-11-03 00:45:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 03327a5a-265a-398e-91a6-4ae0d5ca8dfc | -3.0734 | -54.167 | 2024-11-03 00:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 590aa13b-30ea-3884-a0dd-06fe6f45a030 | -3.0734 | -54.147 | 2024-11-03 00:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 190.0 |
| 56a20173-2d55-329b-8841-8724554ca9de | -3.0918 | -54.1465 | 2024-11-03 00:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 32dfa588-9cdc-3cd1-ac49-736c6e8a64f9 | -3.1213 | -51.1036 | 2024-11-03 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 991a264f-6c4c-3daf-9000-f7389fc0261f | -3.2047 | -53.4179 | 2024-11-03 00:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| f3a5a178-3c90-3a92-a7db-5b915997ec68 | -3.2415 | -53.4169 | 2024-11-03 00:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 64c9a7da-1820-32df-8777-cdc5469afc6f | -3.2415 | -53.3967 | 2024-11-03 00:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 84126456-10aa-36d9-9428-0e97e031702c | -3.2599 | -53.4164 | 2024-11-03 00:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| a9c27278-d6d5-31bb-910c-63d31c44bb6b | -3.2624 | -52.746 | 2024-11-03 00:45:25 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 463080ba-54c1-3e58-932c-a033f02758b3 | -3.2624 | -52.7256 | 2024-11-03 00:45:25 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 694c69e3-1a3e-3781-84f9-682feac374e0 | -3.2808 | -52.7251 | 2024-11-03 00:45:25 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 3687c5fd-709f-3aa0-acae-1f4d1816b008 | -3.3276 | -50.2825 | 2024-11-03 00:45:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 488204ca-db72-3142-9aae-3d74e3037080 | -3.3277 | -50.2615 | 2024-11-03 00:45:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 7fc416cd-8b59-330b-95cf-748ca2a666f0 | -3.4749 | -50.3826 | 2024-11-03 00:45:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| b769a8da-d564-3b8d-98f1-91989f00d7fb | -3.5466 | -50.8611 | 2024-11-03 00:45:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 28b01dd8-520e-3bcf-8ba0-cf195170ef4c | -3.9473 | -48.3666 | 2024-11-03 00:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 695aad72-186a-3089-be76-c664b849bce5 | -3.9474 | -48.3451 | 2024-11-03 00:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| ed9d72d6-0c26-302a-a3fe-4c4ecc568f93 | -4.4054 | -43.4746 | 2024-11-03 00:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 141.9 |
| b28a9dfa-3ab5-3c56-bfc6-a0d3fb3fec57 | -4.4056 | -43.4514 | 2024-11-03 00:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 171.9 |
| 816acf40-2a18-3ff0-9e18-5b2d73647e89 | -4.4241 | -43.4735 | 2024-11-03 00:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 37.1 |
| cf06a2a5-82e5-3253-a4b0-0f6502ec05f0 | -4.4243 | -43.4503 | 2024-11-03 00:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 543ae2df-2ada-3cc8-a233-bf918c96edd2 | -4.8723 | -48.7318 | 2024-11-03 00:45:34 | GOES-16 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 35034efa-a5ac-3322-9d9e-58acec363ec4 | -8.7059 | -48.0181 | 2024-11-03 00:45:55 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 6f89d020-28c6-3aa3-9830-b0797f6b3d7a | -8.7062 | -47.9962 | 2024-11-03 00:45:55 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 29c7ef99-ff4e-359d-82aa-b8b1944054fa | -8.7247 | -48.0163 | 2024-11-03 00:45:55 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 6671bf64-14ae-372b-a18f-447668e5eb90 | -1.2572 | -53.3938 | 2024-11-03 00:55:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 61de6006-f72f-3e2a-b8a8-1c02c35e9250 | -1.2755 | -53.4138 | 2024-11-03 00:55:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| b56e0e56-f7d4-3447-a6e4-7417c9326ddb | -1.2755 | -53.3936 | 2024-11-03 00:55:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 147.2 |
| ecc246d8-2e6e-3333-8d20-6a2138ab4b8d | -1.2756 | -53.3734 | 2024-11-03 00:55:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| ecca01b2-b1bd-308d-9508-04ca55e87cd3 | -2.0409 | -56.0751 | 2024-11-03 00:55:18 | GOES-16 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 65d4cb0c-bad1-3613-8dbe-37d5c9b01284 | -2.1746 | -53.6834 | 2024-11-03 00:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| d0b8cc23-9dc5-32b4-ade4-ae12ccf71421 | -2.2802 | -48.8082 | 2024-11-03 00:55:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 132.3 |
| 8c12e7c0-fb55-399a-bc07-ba49564ffaee | -2.2986 | -48.8078 | 2024-11-03 00:55:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 233.2 |
| a6007cfd-9b13-3939-bfa2-87041c91e0b6 | -2.2987 | -48.7864 | 2024-11-03 00:55:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| eb3ed6fa-42ce-3631-b7fb-f2ce95ef57d4 | -2.6507 | -48.5629 | 2024-11-03 00:55:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 33d20ac8-c1bc-3509-871f-21f245935ef1 | -2.7218 | -49.3295 | 2024-11-03 00:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 8a1e692b-2246-3c8b-94e9-fc3440392fbf | -2.5796 | -53.3927 | 2024-11-03 00:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 14a14e10-b4e7-31a4-9496-f40db2fe3f39 | -2.5797 | -53.3724 | 2024-11-03 00:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 8b8e0d9e-35e2-3692-a36a-60dd8d3f13ec | -2.6321 | -48.5849 | 2024-11-03 00:55:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| fea812c8-73d1-3b60-8a82-9844ce49407a | -2.6322 | -48.5634 | 2024-11-03 00:55:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 54d841c2-a9d4-37f5-a935-0d3d09641019 | -2.6506 | -48.5844 | 2024-11-03 00:55:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 8d708dea-2a0f-3bd8-9668-e4392e2b196c | -2.7419 | -54.4353 | 2024-11-03 00:55:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 207.3 |
| 24fcfea9-e9fa-322e-9fb6-831e2c545388 | -2.7419 | -54.4153 | 2024-11-03 00:55:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 190.6 |
| 42029e1c-da24-3e6a-8213-92346f052462 | -2.7602 | -54.4349 | 2024-11-03 00:55:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 157.8 |
| d2269daa-4386-318d-a9de-2fb628e70730 | -2.7603 | -54.4149 | 2024-11-03 00:55:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 145.2 |
| bbd8f19e-8700-3f87-baf8-94b898af2b17 | -2.7876 | -51.6099 | 2024-11-03 00:55:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 43231f8c-6c63-3a37-b14b-c441734652dc | -3.0397 | -53.2603 | 2024-11-03 00:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 7607ee51-69b7-328b-bace-829bb13d6998 | -3.055 | -54.1675 | 2024-11-03 00:55:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 62f81487-a082-302a-8e51-d57c6cae70b3 | -3.055 | -54.1474 | 2024-11-03 00:55:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 7610172f-b7a5-3ebf-a7f1-1a0f525fbe5d | -3.0734 | -54.167 | 2024-11-03 00:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 13486636-000f-3205-8669-18110f513c90 | -3.0734 | -54.147 | 2024-11-03 00:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 158.4 |
| 4859b015-09ec-39a3-a682-14a9c7f32715 | -3.0918 | -54.1465 | 2024-11-03 00:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 5f96fc23-6842-3c0b-910d-ce0fae778e08 | -3.1059 | -50.3105 | 2024-11-03 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 8744ecb4-d4b2-3625-bf34-3148beea2677 | -3.106 | -50.2896 | 2024-11-03 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 150.2 |
| fe9e47bd-b8cd-3ead-99ec-ec08ad9ee92d | -3.1061 | -50.2686 | 2024-11-03 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| a163648d-1768-3456-9551-92833027e5b6 | -3.1245 | -50.289 | 2024-11-03 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 43c0fe8c-63cf-3157-864e-8178d540d623 | -3.1282 | -54.2459 | 2024-11-03 00:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| e3cbb691-0e9e-30f6-a2cc-7132703a2dd2 | -3.2415 | -53.3967 | 2024-11-03 00:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 562e3504-b5ca-3fb2-a330-ce8cef88d6d6 | -3.2599 | -53.4164 | 2024-11-03 00:55:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| b1fb1086-3762-3ae4-91b6-a6ec431b95ac | -3.2808 | -52.7251 | 2024-11-03 00:55:25 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 9d1aed60-5674-32c4-a20f-31544a85d8d5 | -3.3276 | -50.2825 | 2024-11-03 00:55:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 497aa8a9-6e59-3e04-9ba0-e71cdc70e203 | -3.3277 | -50.2615 | 2024-11-03 00:55:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| c41e6973-03c8-3930-9e32-b77fc96f53e2 | -3.4749 | -50.3826 | 2024-11-03 00:55:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 130.3 |
| a91e877c-54d2-3958-b69d-5e01c90ff778 | -3.475 | -50.3616 | 2024-11-03 00:55:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| d38a72ae-c6c9-3035-a076-83aefc852275 | -3.9473 | -48.3666 | 2024-11-03 00:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| d2ca647e-185d-3054-8b23-d71a776806cd | -3.9474 | -48.3451 | 2024-11-03 00:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 243789d6-cbd9-3897-a22f-ea630304949d | -3.967 | -48.15 | 2024-11-03 00:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 15080800-6480-320f-91fe-c89d47f9945e | -8.7059 | -48.0181 | 2024-11-03 00:55:55 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| efacb315-ee25-3662-bf51-5e0f3071dc13 | -8.7247 | -48.0163 | 2024-11-03 00:55:55 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 8ced6fac-4e7a-3c7b-a089-9f12a547379e | -11.2819 | -56.144 | 2024-11-03 00:56:10 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 1281f475-aba1-3509-b866-b7d99f33d671 | -22.0936 | -43.0741 | 2024-11-03 00:57:07 | GOES-16 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 77.7 |
| c919839a-8b73-3165-a794-3eea31c58722 | -22.0945 | -43.0486 | 2024-11-03 00:57:07 | GOES-16 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 82.3 |
| 06e9c0d0-e8f4-3e40-bc8d-a276f41c7038 | -4.41 | -43.49 | 2024-11-03 01:05:02 | MSG-03 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 01ef00ce-0d84-34d0-ac14-34902758f12a | -4.41 | -43.44 | 2024-11-03 01:05:02 | MSG-03 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4704fac1-ccd9-38cb-b1aa-03f0ee5b2e6b | -1.2572 | -53.3938 | 2024-11-03 01:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| ca14a764-2338-39fa-aeed-1484bcdfcb7e | -1.2755 | -53.4138 | 2024-11-03 01:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| acf1fe66-935b-3d06-9401-8eb6250f209f | -1.2755 | -53.3936 | 2024-11-03 01:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 133.5 |
| 4fac3e7d-1b00-36ba-be4e-c2fb2b913f59 | -1.2756 | -53.3734 | 2024-11-03 01:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| c78131d1-8ba0-34af-9266-b14c936c1c1e | -2.1746 | -53.6834 | 2024-11-03 01:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| f816cb64-a8d8-33db-b4d6-d3c319085590 | -2.1747 | -53.6633 | 2024-11-03 01:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| f5316978-07e7-3c41-b089-2efdf7b5579f | -2.2802 | -48.8082 | 2024-11-03 01:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 139.4 |
| b5cb35f4-e77b-3139-a73d-bfbec492a500 | -2.2802 | -48.7868 | 2024-11-03 01:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 5e65919b-13b1-32b0-b968-2efedc8f4a84 | -2.2986 | -48.8078 | 2024-11-03 01:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 144.6 |
| c56c6e61-3b6b-3406-bc5e-c8d266c5e962 | -2.2987 | -48.7864 | 2024-11-03 01:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| af9826f2-45e7-3696-b936-557926861a6b | -2.5796 | -53.3927 | 2024-11-03 01:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| e1bd2eab-fbc8-37e0-bc04-527262305d83 | -2.5797 | -53.3724 | 2024-11-03 01:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 224a78f3-8bd4-314a-85f8-06528d74a955 | -2.6321 | -48.5849 | 2024-11-03 01:05:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| b3747713-1b0c-3622-b251-76d689664611 | -2.6322 | -48.5634 | 2024-11-03 01:05:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 112682a1-5530-3d02-973d-3896750d03f0 | -2.6506 | -48.5844 | 2024-11-03 01:05:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 68f9dc5a-6248-3102-a2d5-301df544c900 | -2.6507 | -48.5629 | 2024-11-03 01:05:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 495c1672-0517-3fb8-890f-c0c5d52818f2 | -2.7033 | -49.33 | 2024-11-03 01:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 28709408-0067-31e3-a049-7594018bccdd | -2.7218 | -49.3295 | 2024-11-03 01:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 5e348bc7-7cdd-331a-990e-3b13b71de42c | -2.7419 | -54.4353 | 2024-11-03 01:05:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 208.0 |
| c59c46fd-5d7c-3f44-b2c0-582e9a08ac3a | -2.7419 | -54.4153 | 2024-11-03 01:05:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 156.9 |


[Clique aqui para ver as próximas entradas](README9.md)
