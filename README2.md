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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23687469-0a79-3569-a3d9-c58d0a0e255d | -4.5375 | -43.304 | 2024-12-01 00:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| ff5c7a36-cee3-351a-a229-bf5e9209871f | -2.1352 | -54.8662 | 2024-12-01 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 135.5 |
| 908e75dd-2948-3aff-acde-8197339782e5 | -3.2183 | -45.7861 | 2024-12-01 00:10:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 89.6 |
| ecbe8898-3238-346f-8408-b662c7ca533b | -1.9558 | -45.8477 | 2024-12-01 00:10:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 74.2 |
| dd492c2c-51ee-31a6-88c3-bb7d1c5e1307 | -3.2058 | -53.1138 | 2024-12-01 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 18d939da-debc-36cf-8bc6-b370696872ab | -4.5562 | -43.3028 | 2024-12-01 00:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 299.9 |
| f26d1e84-d781-3ca9-9a23-05a9f17b2909 | -3.4569 | -50.2782 | 2024-12-01 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 16fbb787-8c51-376a-946a-bd7e71746f05 | -3.237 | -45.763 | 2024-12-01 00:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 176.4 |
| 7d0fd057-beff-3a4d-b828-98f04c6a1679 | -6.9344 | -43.5401 | 2024-12-01 00:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 235.2 |
| 7d852200-eaed-364f-8845-986870b52b9c | -2.8197 | -53.0425 | 2024-12-01 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 5c0a8dc1-62e9-32e7-ac71-5694c4f2d292 | -4.8899 | -41.3143 | 2024-12-01 00:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 1230040d-c0dc-3f23-bd14-4b4376687503 | -6.9346 | -43.5168 | 2024-12-01 00:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 0b0a947e-26d9-3f59-a937-1ee79a088db4 | -10.6483 | -44.4861 | 2024-12-01 00:10:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 37410847-38f7-3ad5-be2d-aabf6137bf31 | -3.2184 | -45.7637 | 2024-12-01 00:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 225.2 |
| 5d6dc0d2-c55d-350f-b3ac-aeebe8c49d2a | -3.69 | -51.8101 | 2024-12-01 00:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| b632f0c0-dd62-3cd1-a981-2464a7945339 | -6.9341 | -43.5634 | 2024-12-01 00:10:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 1c02d7b8-4a45-39cf-9ad1-37641c5b5701 | -3.2775 | -53.6181 | 2024-12-01 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| f7789a56-ae08-3c8a-9d52-ea915128a9fb | -3.2057 | -53.1341 | 2024-12-01 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 9dda45c6-262e-36ce-abd5-69cf8f2bcb95 | -4.9087 | -41.313 | 2024-12-01 00:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 73.5 |
| 93552548-8380-3ac5-9b1a-6216753319f3 | -3.1456 | -54.5259 | 2024-12-01 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| db50d0e3-7185-3e81-8505-d101ec540031 | -3.4974 | -53.8339 | 2024-12-01 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 0bd3180e-e16c-3bb5-9a16-8f3f55fc094b | -3.69 | -51.8101 | 2024-12-01 00:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 270132e5-9501-357f-9c5f-84a6d6adb13c | -3.2774 | -53.6383 | 2024-12-01 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| dad2621a-0fa1-3262-827e-60da82a15f92 | -3.1272 | -54.5464 | 2024-12-01 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 058dbc84-24f4-311c-94d9-88c566947da5 | -2.1535 | -54.8858 | 2024-12-01 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| ce0d9d9e-96f0-3991-a33c-3e226462cb6c | -2.6579 | -51.8606 | 2024-12-01 00:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 2f216c93-ab01-33a3-a2da-3732bca07c9e | -3.457 | -50.2572 | 2024-12-01 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 0a69a047-dc79-3209-86b5-5f14ac20b229 | -2.8491 | -49.8763 | 2024-12-01 00:20:00 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 4be605e9-c176-3cb2-80f7-95753861874b | -4.5562 | -43.3028 | 2024-12-01 00:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 209.2 |
| f78071f8-1950-35c3-8794-fbc04ec0a628 | -2.1352 | -54.8662 | 2024-12-01 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 6f9b924f-7514-3de5-ade5-c7aa2aef0680 | -4.5578 | -45.7232 | 2024-12-01 00:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 206.1 |
| 737bacf7-ac16-3b5b-aa77-cc4548df793d | -10.6674 | -44.4835 | 2024-12-01 00:20:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| a96eb891-5ead-3c0d-822a-4374ae03815e | -2.8197 | -53.0425 | 2024-12-01 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| d17db9a2-ef0e-358e-898a-adb83f6beaa6 | -4.556 | -43.3261 | 2024-12-01 00:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| deaffb0c-bf00-3147-9638-ccafb0c83f19 | -3.5158 | -53.8333 | 2024-12-01 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| a7351cda-f895-3421-a99f-708279a0d1f6 | -4.9087 | -41.313 | 2024-12-01 00:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 114.4 |
| 4791f8ab-4f23-3414-aebc-472484723843 | -4.8899 | -41.3143 | 2024-12-01 00:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 107.7 |
| 05548fdc-d736-3e65-b527-23d6153c9d9d | -4.5375 | -43.304 | 2024-12-01 00:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 7415d61b-d931-3d86-b201-0e475f21e508 | -3.1273 | -54.5264 | 2024-12-01 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 144d7548-7c94-3a62-8d3a-1ef2fafce7ad | -2.1535 | -54.8659 | 2024-12-01 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| c72d6eff-addb-34c7-bb25-9d3ddc6cb2db | -4.5749 | -43.3017 | 2024-12-01 00:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 658d536f-6c7c-3d38-86c0-4eda10395995 | -3.4754 | -50.2776 | 2024-12-01 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 3da81303-5fc1-3847-80a0-3038d6cbecda | -4.5563 | -43.2795 | 2024-12-01 00:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| bc378f71-60e8-31a7-8847-bc8ebc7968e6 | -3.2775 | -53.6181 | 2024-12-01 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 6975210d-deee-39bc-9f0d-7d04a52f71b0 | -3.4569 | -50.2782 | 2024-12-01 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 126.8 |
| be020c92-cb2d-3403-a869-d7856daef30b | -2.8013 | -53.043 | 2024-12-01 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 7fad4ed2-73b5-3d8b-85c5-66e2be04207a | -3.2242 | -53.1133 | 2024-12-01 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| e78e9d4e-c36a-3901-aeba-701d5bd68c09 | -3.2057 | -53.1341 | 2024-12-01 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 2eee0941-d421-3aaa-8a0d-e76835a494c2 | -4.5394 | -45.7019 | 2024-12-01 00:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 145.5 |
| 295dd83c-dd16-3efc-8b1a-9bc42ce969f8 | -4.558 | -45.7008 | 2024-12-01 00:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 135.9 |
| 80181292-07f2-3326-b22a-e235121b37f0 | -3.2183 | -45.7861 | 2024-12-01 00:20:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 073bd0d7-11e7-3d27-90f8-4cc986baa53e | -2.8012 | -53.0633 | 2024-12-01 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 9dac1a82-3fa9-3d96-8cf9-5e0ff3e966bb | -4.5395 | -45.6794 | 2024-12-01 00:20:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 72cc6e91-af50-3ba3-bd03-6d88508ce2a8 | -1.0022 | -51.7235 | 2024-12-01 00:20:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 3bd25b0e-91b5-3ff6-b848-793e1d907df8 | -3.259 | -53.6388 | 2024-12-01 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 194.9 |
| 0bc15839-4758-3b3e-81a1-3d64f4b4c76a | -2.6578 | -51.8811 | 2024-12-01 00:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 9d07ea3a-9c4d-3550-9f42-7be7f0427452 | -3.2184 | -45.7637 | 2024-12-01 00:20:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 157.3 |
| 153fb270-a826-3bc6-9628-005d3eb7adb2 | -2.849 | -49.8974 | 2024-12-01 00:20:00 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| bf64be57-0222-3c15-855a-719058a50c74 | -2.1351 | -54.8861 | 2024-12-01 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 44367050-8273-30d9-9661-c7820e48a3cd | -3.2058 | -53.1138 | 2024-12-01 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| d9c4e95d-19c3-339e-a625-ea71d3e11cbd | -2.7503 | -51.7553 | 2024-12-01 00:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| be4b7e6f-d3f7-3b76-9579-cdb79ef3354f | -3.4755 | -50.2566 | 2024-12-01 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 313163fd-ca14-30c5-899e-794b664a973b | -3.2591 | -53.6186 | 2024-12-01 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 154.5 |
| dc926221-8ff6-3dde-83d4-0fb068c7f452 | -4.5392 | -45.7243 | 2024-12-01 00:20:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 68.5 |
| ac176393-2002-39ce-93e7-42808f6f9052 | -3.4974 | -53.8339 | 2024-12-01 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| b0ddc552-0b8d-3316-82db-95ace64314d1 | -2.6068 | -45.4269 | 2024-12-01 00:30:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| d999a3b7-bbca-33fc-8c69-126ff70b58d1 | -4.5562 | -43.3028 | 2024-12-01 00:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 269.9 |
| 6d2b3929-e6d8-3994-92f2-fc4e19a04c0f | -3.3134 | -53.8592 | 2024-12-01 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 49b3077c-1c2a-30a8-be0d-21a31e4a0294 | -4.8899 | -41.3143 | 2024-12-01 00:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 95.1 |
| e2dbf042-72b2-3064-b927-a29def29a17d | -2.8197 | -53.0425 | 2024-12-01 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 4e64115a-b906-35b5-a3cb-19a100ddf0f4 | -3.1456 | -54.5259 | 2024-12-01 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 67154f73-895c-3a32-b60f-46a296620a6c | -3.2774 | -53.6383 | 2024-12-01 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| a841202c-3718-34bf-a746-25ba10eb9042 | -2.1535 | -54.8659 | 2024-12-01 00:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 0bf4f7a5-33fe-3502-881f-c7b67cef9f9b | -3.4754 | -50.2776 | 2024-12-01 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 164.9 |
| c01e858c-af7c-3e80-9e3d-b7bc4e476463 | -3.69 | -51.8101 | 2024-12-01 00:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| ee5abdfb-69b7-3101-b434-bfb9130e82da | -4.5392 | -45.7243 | 2024-12-01 00:30:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 991ee42a-bd54-372e-b2ad-ac2a6fbac044 | -2.3376 | -54.6034 | 2024-12-01 00:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 170.3 |
| 7c790c23-e80b-3a78-83c1-cedd7bf7bd11 | -2.8306 | -49.8768 | 2024-12-01 00:30:00 | GOES-16 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| f27223b5-52bf-3af7-8116-9ea1a31e888a | -6.9156 | -43.5418 | 2024-12-01 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 214.4 |
| 9b653eb7-abae-369b-ade1-d7622c4f7854 | -3.2184 | -45.7637 | 2024-12-01 00:30:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 1d23b2be-8b75-3237-976d-d3e454c5755b | -6.9153 | -43.5652 | 2024-12-01 00:30:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 6ab97ddb-82a3-35d7-b7fd-65440b29bc02 | -2.1215 | -46.2439 | 2024-12-01 00:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 18246152-74da-37a2-abd0-4c29b37ab420 | -3.4569 | -50.2782 | 2024-12-01 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| df204055-9f22-385d-b1ba-8865b54ca7fc | -6.9341 | -43.5634 | 2024-12-01 00:30:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 146.7 |
| b67c7296-8abb-3423-b1d6-1a300d5c0ce4 | -2.1535 | -54.8858 | 2024-12-01 00:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 019fffee-c82a-3e9c-8d5d-6b7994b8b5a8 | -3.4974 | -53.8339 | 2024-12-01 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 1ef5e94a-feab-350a-ac77-7103d938ab75 | -4.9087 | -41.313 | 2024-12-01 00:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 62.0 |
| 82332e45-a572-328f-8e0d-56f27fea81e2 | -2.8491 | -49.8763 | 2024-12-01 00:30:00 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| ef2e0a5c-e5e5-39b4-887b-5d2bc82263c8 | -1.6954 | -46.1426 | 2024-12-01 00:30:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 59.9 |
| d811307e-da7b-3b43-9831-4013b941e6af | -3.2058 | -53.1138 | 2024-12-01 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| aa4d1a7b-0ea4-3ff0-9dd6-6ef6eb9b57a4 | -4.5563 | -43.2795 | 2024-12-01 00:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| f579ee12-82fe-3273-9503-a9cd89827a71 | -3.259 | -53.6388 | 2024-12-01 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 174.9 |
| 43300b4e-a74d-3610-9ebf-c6a538462a19 | -4.5395 | -45.6794 | 2024-12-01 00:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 42e7b2f4-ab56-3a5c-b2e0-40e456174989 | -10.6674 | -44.4835 | 2024-12-01 00:30:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 03d582a6-bb1b-38c6-83be-2d4c89c667f7 | -6.9344 | -43.5401 | 2024-12-01 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 474.3 |
| ab0094dd-7864-3450-8b6f-4ffcc128ced3 | -2.8013 | -53.043 | 2024-12-01 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| d62652e8-fcbe-3489-9f59-28795f9030de | -6.9346 | -43.5168 | 2024-12-01 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 9449a858-2eb8-306a-8748-f9560679240d | -3.1273 | -54.5264 | 2024-12-01 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 72d00288-5634-3cca-8066-ac96f7c20757 | -3.4755 | -50.2566 | 2024-12-01 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 148.6 |
| 69bc5456-5b12-3db8-bae6-1efcafdeeb57 | -4.5578 | -45.7232 | 2024-12-01 00:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 169.6 |


[Clique aqui para ver as próximas entradas](README3.md)
