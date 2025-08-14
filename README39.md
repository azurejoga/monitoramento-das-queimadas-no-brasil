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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc3f23d4-e7a5-37a8-9297-4a15d11cd910 | -6.8956 | -59.1462 | 2025-08-14 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| d475c807-0df6-3390-9763-9ca111761293 | -6.914 | -59.1455 | 2025-08-14 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 60089fcc-541b-3e51-b9e7-f9f9f340c072 | -6.8956 | -59.1462 | 2025-08-14 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 7542c5a9-2530-3068-93a6-c41c69dc668f | -6.914 | -59.1455 | 2025-08-14 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| bd0f1aa1-9ac4-38e4-a6ee-e657c06f4582 | -6.89207 | -59.15284 | 2025-08-14 07:01:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| c2a9cf52-2ddb-3aab-9795-e82bf30d3ba3 | -6.08367 | -59.93942 | 2025-08-14 07:01:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| e1677d64-7835-31da-976d-a3cd7387d981 | -6.09054 | -59.93466 | 2025-08-14 07:01:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 31.0 |
| a8fdced6-106b-3025-b8a8-a28537074405 | -6.09442 | -59.94095 | 2025-08-14 07:01:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 2be9c79f-0ca2-3193-b03b-fb5f298bbcf3 | -6.08858 | -59.94815 | 2025-08-14 07:01:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 7d7dd036-6bf5-30ce-9481-b076f51811b7 | -7.22919 | -57.63634 | 2025-08-14 07:01:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 03e649e9-8724-38fc-be3c-77e5dddadd21 | -7.12522 | -59.62617 | 2025-08-14 07:01:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 48556ffe-b839-3bca-b0bb-aebc09bc3d29 | -6.10894 | -59.91547 | 2025-08-14 07:01:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 3a7846e2-70be-3eca-9f64-0c925598683b | -7.23343 | -57.62975 | 2025-08-14 07:01:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| bfcbfde5-0f73-3dbb-9607-dcde5d2ad46e | -6.88045 | -59.15128 | 2025-08-14 07:01:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| cc6c4ab3-78df-3f96-b8c4-3a8c50a67df9 | -7.86751 | -61.81737 | 2025-08-14 07:03:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| ab23e99a-268d-3645-b2e4-b3567209e631 | -7.87718 | -61.81875 | 2025-08-14 07:03:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| b0a079ba-f178-36a0-a727-9b9034912179 | -7.86904 | -61.80654 | 2025-08-14 07:03:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| bbed4095-0bc0-3b80-a7f5-5a06aa9e2b6e | -7.61318 | -63.51616 | 2025-08-14 07:03:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 69746217-51c7-3f0c-a415-72245f995ffd | -9.15173 | -59.65152 | 2025-08-14 07:03:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.3 |
| c2aabbca-2b05-3697-8b2c-b750bf961cad | -9.15359 | -59.66104 | 2025-08-14 07:03:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 47dc9337-0fcc-3ab8-b35e-20a94eed9cfe | -8.09905 | -61.18808 | 2025-08-14 07:03:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 35a9d667-3c4a-3f9c-8882-208fc2c2f06d | -9.15579 | -59.64509 | 2025-08-14 07:03:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 7bc2c5d6-e1c0-39ed-a1a7-56271b279d3b | -7.87872 | -61.80793 | 2025-08-14 07:03:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 8656308f-1c78-379f-b396-87c1ee3bf98f | -9.14966 | -59.66742 | 2025-08-14 07:03:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| fd787785-b940-3b22-8646-526e228d6462 | -7.62209 | -63.51746 | 2025-08-14 07:03:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 8a4fe6a3-9d7f-3615-97c7-d2e466adbdef | -8.10746 | -61.20136 | 2025-08-14 07:03:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 23.1 |
| fbf6e467-5eae-3daf-bf5f-ae6ed66f9747 | -8.10916 | -61.1895 | 2025-08-14 07:03:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 32803ea0-7c8b-344b-a0b6-933309f0d7a0 | -7.60427 | -63.51485 | 2025-08-14 07:03:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 13.9 |
| c0d09b8a-b89f-3d1c-81a3-dcd995f9b0bc | -6.8771 | -59.147 | 2025-08-14 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| efe9bbc4-b925-34cf-bbbc-64198536bc56 | -6.8956 | -59.1462 | 2025-08-14 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 1dd49afe-5d63-39f8-8d85-8d128c48790c | -6.8955 | -59.1655 | 2025-08-14 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 1bb52070-ed4b-3038-9d8e-218bcc869692 | -23.6978 | -51.7916 | 2025-08-14 07:10:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 60.0 |
| 6942bdcc-300c-31af-94f7-58290488cccf | -6.914 | -59.1455 | 2025-08-14 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 2d435e26-4c9f-335b-babf-b9ba0d4a00cc | -23.6985 | -51.7687 | 2025-08-14 07:10:00 | GOES-19 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 49.3 |
| 397af378-b171-3e4e-a466-827725ebb3f0 | -6.914 | -59.1455 | 2025-08-14 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 68aef9c8-b6f0-347d-bd63-51b30f58d666 | -6.8955 | -59.1655 | 2025-08-14 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| c4d7527e-ee1c-311f-9bdf-b26bed5294c0 | -6.8771 | -59.147 | 2025-08-14 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| c8cd0ba1-fca3-3ae5-a6fc-1ac38fcaa91c | -6.8956 | -59.1462 | 2025-08-14 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 3b1e9354-c4c7-3364-95aa-daaef9269227 | -6.914 | -59.1455 | 2025-08-14 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| a85c0fab-7d7c-3a66-960c-d3416caf3144 | -6.8956 | -59.1462 | 2025-08-14 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 454de5e1-b900-3e8e-9e8a-d0a8fde338f2 | -6.8956 | -59.1462 | 2025-08-14 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 71b96aff-12dd-3051-9635-895f20a4f31d | -6.914 | -59.1455 | 2025-08-14 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 7af5de16-90fd-3ea2-be6c-948a8b77aaaa | -6.8956 | -59.1462 | 2025-08-14 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 12204473-b243-3c61-b2b6-692c742b0077 | -6.914 | -59.1455 | 2025-08-14 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 41d97fe3-86f9-3871-9c6d-3867a859e3f6 | -6.914 | -59.1455 | 2025-08-14 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| cbf98739-53c1-34f1-a9e6-4938166e657e | -6.8956 | -59.1462 | 2025-08-14 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| ad2c396f-a9dc-3398-8fca-e2b49baf9c3c | -6.914 | -59.1455 | 2025-08-14 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 6d646d27-edc6-3eb3-8c59-ade9a7a22fa9 | -6.8955 | -59.1655 | 2025-08-14 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| e3650999-2e8c-356d-a1a6-28cb97259625 | -6.8956 | -59.1462 | 2025-08-14 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| d112d994-47dc-319b-842e-ce391f79d9d9 | -6.914 | -59.1455 | 2025-08-14 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| ccf09083-a9c4-3ac2-8d07-48bd3369588a | -6.8956 | -59.1462 | 2025-08-14 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 563ec261-755f-3e6c-a3c1-0d7a4df23f2f | -6.8771 | -59.147 | 2025-08-14 08:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 470682a7-080b-3fb3-a4f0-a411bdaa1bff | -6.914 | -59.1455 | 2025-08-14 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 51d2aa07-268e-3b72-8897-e39460e1313e | -6.8956 | -59.1462 | 2025-08-14 08:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 8d158e14-8feb-3546-af91-cf4d55bb7474 | -6.8956 | -59.1462 | 2025-08-14 08:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 9accdb73-6cc4-31a6-99d3-07e5f630c729 | -6.914 | -59.1455 | 2025-08-14 08:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| c2fda93f-bf1a-33dd-a696-22cd96fb60fc | -6.914 | -59.1455 | 2025-08-14 08:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 9e4cc88c-90d5-3410-bc40-f2f8dbd79443 | -6.8956 | -59.1462 | 2025-08-14 08:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 32eb5cf0-fc93-3d50-a364-f3a5e5597019 | -6.8956 | -59.1462 | 2025-08-14 09:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 918ef867-4805-3de7-9fe9-ecac2e3798ce | -6.914 | -59.1455 | 2025-08-14 09:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| dba596ac-16a1-3f94-92f1-daf33fb58077 | -6.914 | -59.1455 | 2025-08-14 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 31253fb5-10e4-3dcc-a620-428f8fd233d7 | -6.8955 | -59.1655 | 2025-08-14 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 8d7c065e-3270-3e44-afbc-0ea59aecfd0f | -6.8956 | -59.1462 | 2025-08-14 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| b7c6597a-9639-33ff-8ed1-c085bebcfeff | -6.914 | -59.1455 | 2025-08-14 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 7a1bb6e1-880c-335f-9118-c795f784466e | -6.8956 | -59.1462 | 2025-08-14 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 355a3a34-2484-3de3-a061-12cfeda3e657 | -6.8956 | -59.1462 | 2025-08-14 11:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| a7d9458b-a2dc-3454-8a93-4dfe18d7bed2 | -6.8956 | -59.1462 | 2025-08-14 11:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 9c752162-1f2f-33b5-91fb-94aa7d624f91 | -6.78498 | -39.18639 | 2025-08-14 11:34:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 452f8d8a-e19b-316a-9872-0b4f0806535f | -4.3851 | -38.23204 | 2025-08-14 11:34:00 | TERRA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 6f783011-82d1-3b20-9aff-0c530c1e8e07 | -8.10547 | -36.22445 | 2025-08-14 11:34:00 | TERRA_M-M | BREJO DA MADRE DE DEUS | PERNAMBUCO | Brasil | 2602605 | 26 | 33 | nan | nan | nan | Caatinga | 10.2 |
| cd9dd199-d1ca-351c-9a58-d8ac3e75f2d3 | -7.39132 | -39.69217 | 2025-08-14 11:34:00 | TERRA_M-M | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 9.8 |
| bf27ff28-dd60-32af-bb4e-887328b0c0cc | -9.44866 | -42.32761 | 2025-08-14 11:34:00 | TERRA_M-M | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 9b5d25b2-83c5-3e73-9a1c-d6fda8211bd6 | -8.91049 | -40.37758 | 2025-08-14 11:34:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 22ccaf55-4d9f-32b5-9c0d-733dead55c18 | -4.38331 | -38.24405 | 2025-08-14 11:34:00 | TERRA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 27f9d0fc-e6f7-3abf-a92a-419bf9e13c24 | -7.39344 | -39.67843 | 2025-08-14 11:34:00 | TERRA_M-M | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 9.9 |
| a4945fc1-3299-3167-810d-b81a5e5b6f17 | -6.78306 | -39.19933 | 2025-08-14 11:34:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| f31708e8-2bb7-3532-bb15-90a721a05483 | -5.33346 | -36.81213 | 2025-08-14 11:34:00 | TERRA_M-M | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 0e1ea467-5554-34e6-858e-305426b45b4c | -7.83107 | -37.39787 | 2025-08-14 11:34:00 | TERRA_M-M | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 6.9 |
| f5cf9666-67df-3d01-8705-02ba982c8115 | -12.05097 | -43.37208 | 2025-08-14 11:34:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 34.6 |
| a935f9d7-d842-3309-9b1a-600d29bc3314 | -8.62799 | -40.78199 | 2025-08-14 11:34:00 | TERRA_M-M | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 13.1 |
| ebc4e90c-756f-37a9-b1d0-e79474737291 | -9.88063 | -40.65374 | 2025-08-14 11:34:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 2a0908aa-9ff9-35b2-9f9b-130d6b880334 | -11.46493 | -42.22064 | 2025-08-14 11:34:00 | TERRA_M-M | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| d9a27c3e-9140-3c8d-8cd0-3ffebf48415f | -11.45507 | -42.22614 | 2025-08-14 11:34:00 | TERRA_M-M | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 24.0 |
| a4728342-32f0-3fa1-8c22-7d826f878f32 | -6.77922 | -39.19225 | 2025-08-14 11:34:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 1b4cac4d-10fa-33ef-a1c5-707bf3b93eae | -8.75195 | -44.02588 | 2025-08-14 11:34:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| d376053d-86a4-3931-b427-075be0d5ae44 | -4.98548 | -37.78115 | 2025-08-14 11:34:00 | TERRA_M-M | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 14.0 |
| d0b31916-8dee-36a1-a0db-ad7cb225595f | -8.7487 | -44.0481 | 2025-08-14 11:34:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 1f256525-0cb5-3d36-8a47-58be06acced1 | -13.81856 | -41.97485 | 2025-08-14 11:36:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 3e5869f1-c98b-326c-8018-014cbbaed320 | -18.02576 | -44.40953 | 2025-08-14 11:36:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 24.8 |
| c984447e-7407-3f15-82a2-39ab6e394469 | -18.02687 | -44.40391 | 2025-08-14 11:36:00 | TERRA_M-M | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 22.0 |
| e5e86e86-f6c7-36ca-b190-a044ae0746db | -13.81913 | -41.98578 | 2025-08-14 11:36:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 15.2 |
| f526b4d0-9d8b-3485-9a18-6e1409ada427 | -19.27469 | -39.93284 | 2025-08-14 11:36:00 | TERRA_M-M | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 3b0d5ec9-fca4-3069-aa15-8eef4460d97e | -19.67724 | -40.77466 | 2025-08-14 11:36:00 | TERRA_M-M | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| d6662bea-01ea-3140-98bc-3657a68716b7 | -14.035 | -41.21228 | 2025-08-14 11:36:00 | TERRA_M-M | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 14.0 |
| ec74b43e-a21c-374c-8f1d-f6bb215d66e1 | -19.26346 | -41.17271 | 2025-08-14 11:36:00 | TERRA_M-M | RESPLENDOR | MINAS GERAIS | Brasil | 3154309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 4bf8c0ba-759b-3584-9415-bf8d3e0d954a | -19.77979 | -40.77362 | 2025-08-14 11:36:00 | TERRA_M-M | SÃO ROQUE DO CANAÃ | ESPÍRITO SANTO | Brasil | 3204955 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| c9b3e3a7-acbe-315a-8d93-62335105e4a2 | -13.55254 | -41.85009 | 2025-08-14 11:36:00 | TERRA_M-M | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| e47bd889-898f-397c-aedb-e03b45fa69fa | -20.18538 | -40.85734 | 2025-08-14 11:36:00 | TERRA_M-M | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| a432d31d-ab7c-392c-9836-64b524e80f1f | -12.68651 | -44.92763 | 2025-08-14 11:36:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 2aed7bd8-db3f-3a7c-b7ef-5db39dd998a6 | -12.68539 | -44.93464 | 2025-08-14 11:36:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |


[Clique aqui para ver as próximas entradas](README40.md)
