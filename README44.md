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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db253a85-8c7e-33c9-a4a0-841dc4a9334c | -7.47528 | -47.11836 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f931d9c1-aec1-317f-be9c-3f075eb6d70f | -7.42502 | -47.37595 | 2024-10-24 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ffca6f7-4274-3979-a474-f005589681de | -7.37648 | -47.22879 | 2024-10-24 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b1280fa-09c0-34ed-870e-fc8ad5d380c8 | -7.37316 | -47.22827 | 2024-10-24 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1a8c1e5-74e8-3391-be73-475c31292f1e | -7.37262 | -47.23177 | 2024-10-24 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4fbfcd9d-ea3a-3c52-83df-2c6e0e75a6bb | -7.36991 | -47.22783 | 2024-10-24 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1fdae400-0b44-3bc0-816e-26fb246dcc75 | -7.6809 | -47.30535 | 2024-10-24 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf769e32-ff68-3e4f-ae07-bba12dd2ffde | -7.67981 | -47.31236 | 2024-10-24 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4f4c470-eb5d-3019-86e7-5a26cf47f441 | -9.24337 | -48.32347 | 2024-10-24 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38b71e95-5b1c-3d45-b201-44ef507fe485 | -9.24115 | -48.316 | 2024-10-24 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cc586b7-9ec8-34be-a8dc-e3f6d8598819 | -9.24061 | -48.31947 | 2024-10-24 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27c48241-4cb1-3ff8-aac1-e0f7d1d1b9d5 | -9.23785 | -48.31548 | 2024-10-24 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f89dddeb-b40d-3b5a-b674-b3bdf513fdd6 | -9.23509 | -48.31148 | 2024-10-24 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5da58af7-e9e5-3a6c-b348-37049c5a0e4f | -9.23179 | -48.31096 | 2024-10-24 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97e1122b-d9ac-3124-86f0-1e5bdfdb7285 | -9.12396 | -48.76004 | 2024-10-24 04:34:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41e8c097-68e9-3246-935f-90265c900104 | -9.12066 | -48.75951 | 2024-10-24 04:34:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 430274e9-ca58-362b-a0b2-8c8e77595f91 | -9.03597 | -48.71389 | 2024-10-24 04:34:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eacae753-29be-3139-ae33-ff283971b849 | -8.74818 | -48.2943 | 2024-10-24 04:34:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8414e50-5911-341c-bf02-aae0ee069266 | -8.26821 | -48.49052 | 2024-10-24 04:34:00 | NOAA-21 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7704910-6cdf-3cd1-a210-b0390c924941 | -9.21027 | -47.94748 | 2024-10-24 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3b5a231c-78eb-3470-a13c-16abcd5a0437 | -9.20972 | -47.95097 | 2024-10-24 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8a9560d4-cf31-36ca-bb0b-692481d0f8a9 | -9.20918 | -47.95445 | 2024-10-24 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bf71edda-cc55-3a86-8e8a-389b074f3272 | -9.20642 | -47.95044 | 2024-10-24 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 974ffbc0-a0f9-3705-a40f-f3085a6dc7d6 | -9.13617 | -48.07502 | 2024-10-24 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 797bff77-fd90-3cb8-b0e1-4e4e5e95b20d | -8.42651 | -48.10733 | 2024-10-24 04:34:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4aa2aa8-e875-393e-96a7-771342edfc39 | -8.41469 | -47.98829 | 2024-10-24 04:34:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5bb01933-f0a7-309c-8c65-1945347da668 | -9.20587 | -47.95393 | 2024-10-24 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9562c81b-db84-3993-9651-c67efa2ebe9e | -9.20311 | -47.94992 | 2024-10-24 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f65c4ff2-06b3-3ce2-acdc-1e1d97dad6ba | -9.20256 | -47.95341 | 2024-10-24 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a1e5773-9096-393d-9381-f7ca0913b2bf | -9.14003 | -47.72104 | 2024-10-24 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8925872d-fca7-3c2f-8430-53d264b04ef0 | -9.02234 | -47.75644 | 2024-10-24 04:34:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 600ada3d-350f-3a22-a2e5-f2e3775aa156 | -9.01903 | -47.75591 | 2024-10-24 04:34:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ab45d9f-7beb-3dbc-86ed-fa56c86263c5 | -8.91682 | -47.91155 | 2024-10-24 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3122b468-20c6-32cf-80e3-6ae0026c6f2e | -8.9069 | -47.90998 | 2024-10-24 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a253d82e-2302-3d02-892e-d328c5ef42d8 | -8.82056 | -47.9393 | 2024-10-24 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8c3f5b27-b5a3-3b2b-9c09-2ab98a3e7edc | -8.41139 | -47.98777 | 2024-10-24 04:34:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0060a32-ba23-3995-a21e-e6f0a2811f13 | -8.23946 | -47.67245 | 2024-10-24 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2161a993-5186-374d-876d-da7ea4765502 | -10.69243 | -49.10717 | 2024-10-24 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3cee0525-9b8c-3fe5-83e8-d810df47f2db | -10.69188 | -49.11067 | 2024-10-24 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e9413fce-1d43-39bb-9b2d-6e8a50acec42 | -10.68858 | -49.11013 | 2024-10-24 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 275cdb7b-c2d7-3e5d-9943-34c797f235a4 | -10.68802 | -49.11363 | 2024-10-24 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1645b92-fc5b-3b79-8417-9c7daad77ec1 | -10.68527 | -49.10961 | 2024-10-24 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d6ec24cb-a012-3dd6-b8b0-d51460b0463a | -9.99429 | -48.85107 | 2024-10-24 04:34:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc4037a7-c5f8-3c26-92e4-7a2dbe6d7707 | -9.99374 | -48.85455 | 2024-10-24 04:34:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b32d52e5-b3a5-3920-b91e-526e35d98d3d | -9.99043 | -48.85402 | 2024-10-24 04:34:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e8c97b3-d62b-35dc-a046-0909a3c081cf | -9.92622 | -48.11137 | 2024-10-24 04:34:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87d4463f-f5f3-3de5-b8c7-bb1bcc2a0a25 | -9.87249 | -48.56347 | 2024-10-24 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad55cd3b-d7ce-3fcd-9a65-2f8b5b3449d3 | -9.86919 | -48.56294 | 2024-10-24 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fe1c49ee-e264-3e30-8948-1673425cf838 | -9.85104 | -48.57075 | 2024-10-24 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a5ccb9d-967b-3ebf-b80e-8dc47eb3af8e | -9.8505 | -48.57423 | 2024-10-24 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8816a9b-4ebd-308c-a064-96db10104a1b | -9.84987 | -48.5135 | 2024-10-24 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51b90be6-de5d-360c-bd09-7f1c80abfeff | -9.72537 | -48.37607 | 2024-10-24 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| edd9e38b-9953-3d69-a06f-4b6d7f4959b5 | -10.14493 | -48.30375 | 2024-10-24 04:34:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38debdb3-450e-3d9c-8a23-3b441e9528bf | -10.07802 | -48.86074 | 2024-10-24 04:34:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d5f18099-0b03-3aad-ad59-4c50e26dbd75 | -10.07747 | -48.86423 | 2024-10-24 04:34:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c80fabb-a87d-30ce-b5b4-be5d5d4d7f4e | -10.04642 | -48.21281 | 2024-10-24 04:34:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2a75198-6e5a-3a7d-b248-a880cc93f2f9 | -10.04588 | -48.2163 | 2024-10-24 04:34:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1ee09f5-740e-3986-b9c8-5066bae79edc | -10.66379 | -48.28957 | 2024-10-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ccc1e504-cac8-3ff6-b45d-4b9769d80f7c | -10.66325 | -48.29308 | 2024-10-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f8fc7d0-0637-3d2f-8398-d82e13bdb1c1 | -10.64323 | -48.55159 | 2024-10-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a22b2fb-cd0a-3279-b039-f21def851cb4 | -10.63003 | -48.54947 | 2024-10-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ec5f21b-a804-3b32-b422-6f6e00582634 | -10.62858 | -49.01464 | 2024-10-24 04:34:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ebc5f4d-1922-3cff-898d-c7607f510fd3 | -10.5889 | -48.66084 | 2024-10-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fed84af-8a81-3db4-905d-409fe37dbccd | -10.52154 | -48.2205 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dfe6751b-1a81-3852-9eb7-e57211c3376a | -10.48143 | -48.28232 | 2024-10-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31d39ced-5640-3651-9594-95e05ab8939f | -10.47812 | -48.2818 | 2024-10-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 33a9c17c-795f-378f-bcd2-0f638f5d9d44 | -10.47481 | -48.28128 | 2024-10-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| eefc9f77-2b9a-3218-9baf-51a8fb484ad6 | -10.47124 | -48.28073 | 2024-10-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8804bc8-590f-302d-a0c7-d8609d687033 | -10.47069 | -48.28423 | 2024-10-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9b11a74a-8e83-3e56-b2fe-9bee4c14dc88 | -10.45779 | -48.58646 | 2024-10-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 669aeb38-46f2-3832-9f3b-65d11761c9be | -10.45724 | -48.58995 | 2024-10-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97071988-75c7-3ac7-8432-69904fe7dfdc | -10.3255 | -48.82244 | 2024-10-24 04:34:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c5aa2e4-931f-3f7b-803e-88128a8391a6 | -10.32222 | -48.82187 | 2024-10-24 04:34:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7fb78a70-90b2-33cf-b0e7-14e0226f95e7 | -10.31944 | -48.8179 | 2024-10-24 04:34:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 384d6134-2be9-3522-816c-9a7d3a060368 | -10.29088 | -48.89189 | 2024-10-24 04:34:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8550018a-ec2e-39b9-9d1e-3a9c3c6aa6eb | -9.92618 | -47.84878 | 2024-10-24 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59b44be3-a4dc-3047-a0d4-6a2e995d08b9 | -9.62389 | -47.91253 | 2024-10-24 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e992f4fb-0105-323c-8268-f837d7c2fbfc | -9.60977 | -47.60734 | 2024-10-24 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c45d5708-7902-34ed-bc46-4b3ada512ed4 | -10.91543 | -47.8049 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ac55db6-78da-3a49-b6ab-206082a49ec4 | -10.91319 | -47.79721 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31975523-2759-3fb4-ae45-d757658ee214 | -10.90986 | -47.79668 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95b27d64-ca87-3db8-8a06-ba8827b8b1d4 | -10.8999 | -47.81712 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 53b73cb5-3ae8-3131-9455-ae1d87e4b225 | -10.89474 | -47.96194 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9db603c-ae17-39b0-a23a-a7bfd1d96bb8 | -10.89419 | -47.96547 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e5174d1-0dee-3b91-aefe-493bb46d1b31 | -10.89294 | -47.90711 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 094f308b-f10b-3928-afc3-7ae8eef1ecd2 | -10.88961 | -47.90659 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6a832600-6f18-330a-8ae9-bff0bbddf8c7 | -10.88857 | -47.93563 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a617c114-ee6e-3a81-a2bf-68416396ab70 | -10.88802 | -47.93919 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a60e303d-f546-3fd1-a115-dc56281bfd6b | -10.88628 | -47.90607 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ea92c70a-4b19-3243-a499-a93957f4be40 | -10.84549 | -47.95094 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0ec3191-d7c4-3a60-ba00-17049572f141 | -10.84216 | -47.95041 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0740292b-2f2c-3694-abd3-8a2ad9a4e357 | -10.83939 | -47.9463 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6e4c95d-5817-3a64-8df7-ba5927183748 | -10.82511 | -48.01659 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 044e271e-bca0-3c60-a896-cbceddf77a98 | -10.82457 | -48.02009 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72f98697-cadf-3aed-92dd-abef002ca17b | -10.72409 | -48.05444 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4aa1371d-eab6-38b1-b6fa-bf41fd70cb1d | -10.7193 | -48.15133 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4fa12c8-456a-3a7a-b048-8e72c1cbb40f | -10.58901 | -48.02611 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e36a6507-5f6f-355b-b2ca-ed358f5a94c3 | -10.58846 | -48.02966 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 45c0f7c4-641e-3384-b896-af8795849fc3 | -10.58514 | -48.02914 | 2024-10-24 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3961475a-217d-3fc5-ad72-313c44af4065 | -10.53889 | -47.7351 | 2024-10-24 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README45.md)
