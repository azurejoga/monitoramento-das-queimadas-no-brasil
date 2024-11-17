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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88e3e9a7-a063-37cf-9214-3069bcbd69e8 | -3.5125 | -50.2343 | 2024-11-17 03:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| d761913d-3c21-33cb-85fa-eeb9a595bd94 | -2.6322 | -48.5634 | 2024-11-17 03:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| a2fafa13-4f0c-37cf-8ef2-87adf333fc6a | -2.8614 | -46.7306 | 2024-11-17 03:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| b085a6a3-c211-397c-9f3d-d538645f455a | -8.4528 | -44.1767 | 2024-11-17 03:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 193.2 |
| 08770d85-1613-39aa-b8a1-99eb57a98ccc | 0.6159 | -51.7676 | 2024-11-17 03:00:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 60963c39-d2e6-306e-8293-bf6e3aa85047 | -2.2111 | -47.2321 | 2024-11-17 03:00:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 3841dcce-4c73-38e4-8dff-640ac236cc79 | -1.9167 | -46.5584 | 2024-11-17 03:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 0366e08a-f6ac-3cda-9871-f58b1a4f61d6 | -2.8615 | -46.7086 | 2024-11-17 03:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 7be6d49a-8721-3615-8135-2ad6a91b9c1c | -3.531 | -50.2337 | 2024-11-17 03:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| c5770ec7-abfd-3262-93a5-58f7c49f0af1 | -8.4339 | -44.1788 | 2024-11-17 03:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 296.1 |
| 290d0b88-c507-3c45-89f0-bc14ced376e0 | -2.2296 | -47.2316 | 2024-11-17 03:00:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| d644c733-e2fd-30c7-a7f3-826f9cb77059 | -3.5309 | -50.2547 | 2024-11-17 03:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 251.6 |
| ac6cb7f9-0e11-3039-903a-48abad0d0fa7 | -8.4333 | -44.2251 | 2024-11-17 03:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 157.4 |
| 2f8a45cb-ba6e-370e-80d6-eb72e66312bf | -2.2296 | -47.2098 | 2024-11-17 03:00:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 9f93f38b-1223-3d97-a7be-3cb423618b48 | -8.4522 | -44.223 | 2024-11-17 03:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 98.3 |
| d7014905-6f85-3afd-8fd7-fb53d916edde | -8.4525 | -44.1999 | 2024-11-17 03:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 418.6 |
| 12d1e378-9846-38a0-a4dc-ab075172e76f | -3.5124 | -50.2553 | 2024-11-17 03:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 02375e6f-2e51-3da3-b2b4-ad2dd1fa0f68 | -8.4336 | -44.2019 | 2024-11-17 03:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 725.1 |
| 62d94a3c-32c9-302c-a5e0-2c442dd06e58 | -2.2111 | -47.2102 | 2024-11-17 03:00:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 7442f074-19b9-3e03-a5ee-2e254acda88c | -3.5308 | -50.2757 | 2024-11-17 03:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 95566cf1-a8dc-3291-b9af-832760bc2d60 | -3.3359 | -52.7847 | 2024-11-17 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| edf48be6-5bb8-3303-84a3-4533b20c3d6d | -1.9166 | -46.5804 | 2024-11-17 03:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 986ed653-8284-3fad-92b0-cacc5ba24acf | -2.8801 | -46.7079 | 2024-11-17 03:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| e92af101-c764-3417-b215-aa6248ab798a | -3.5494 | -50.254 | 2024-11-17 03:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 1ba1a4a3-63c9-3fef-b6e4-5f9e7bf56006 | -2.88 | -46.73 | 2024-11-17 03:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 1178acbb-b469-38af-b90f-347a233db5d7 | -4.5614 | -48.0141 | 2024-11-17 03:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 14af47f6-cf33-38a2-9df1-883cb18b091e | -3.3359 | -52.7643 | 2024-11-17 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| cd52de77-983e-32cf-899d-589c84df3f35 | -8.45 | -44.22 | 2024-11-17 03:00:00 | MSG-03 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 834a03b8-f6d3-3053-9891-64177e795a8e | -8.42 | -44.17 | 2024-11-17 03:00:00 | MSG-03 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 74d09881-cd51-39f6-b2ad-20424b6744ec | -3.52 | -50.24 | 2024-11-17 03:00:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 744a1a9a-722d-3d88-8e49-ce0532016369 | -8.42 | -44.21 | 2024-11-17 03:00:00 | MSG-03 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e916901b-ec20-3bee-ac1f-128bb96ad587 | -8.45 | -44.17 | 2024-11-17 03:00:00 | MSG-03 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6968f8e9-1e07-3995-acfb-8179a535d29d | -8.4333 | -44.2251 | 2024-11-17 03:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 82e34b79-90f4-3533-8507-a2b5a8381552 | -8.4339 | -44.1788 | 2024-11-17 03:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 8042fac3-b94e-3772-94c8-0ab1f0fecafe | -2.6322 | -48.5634 | 2024-11-17 03:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 66d22b1c-3dd5-3b98-992c-3b11676423a1 | -8.4336 | -44.2019 | 2024-11-17 03:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 413.8 |
| 4a6200f8-18d3-317e-9bb0-fe05f5d2b8cc | -2.8614 | -46.7306 | 2024-11-17 03:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| af459be7-399c-33e0-883e-52e7a1bd6b74 | -3.531 | -50.2337 | 2024-11-17 03:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 2f1e0533-92dd-3b0a-a723-becaa46ce2b7 | -3.5308 | -50.2757 | 2024-11-17 03:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| a64e6f07-8a70-3a02-b511-845849cd820c | -2.678 | -46.2059 | 2024-11-17 03:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 61.9 |
| c1df2a00-0eb1-3832-b6b5-26d4a3f5bfc7 | -8.4525 | -44.1999 | 2024-11-17 03:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 631.8 |
| abc160f9-466e-3c3e-980f-b9d409d4648c | -8.4528 | -44.1767 | 2024-11-17 03:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 262.4 |
| 7f02fa83-4fb5-374b-917f-72d1b3da2f9f | -3.5124 | -50.2553 | 2024-11-17 03:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| d03da691-ee6b-37d5-839a-c2e48fc1c525 | -8.4522 | -44.223 | 2024-11-17 03:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 164.7 |
| cd460988-72ea-3574-85ce-7c8e6e491ea8 | -2.2296 | -47.2098 | 2024-11-17 03:10:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| f320af21-b655-3d61-b543-98790684e502 | -3.5309 | -50.2547 | 2024-11-17 03:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 205.6 |
| 917f48ee-5421-3216-b204-c3e1359b35a5 | -3.3359 | -52.7643 | 2024-11-17 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 2de46689-a578-3067-997e-d40d6897fabf | 0.6159 | -51.7676 | 2024-11-17 03:10:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 8b234bb3-2e24-3937-8a36-1f4ef7a7cad7 | 0.6159 | -51.7881 | 2024-11-17 03:10:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 7d0aa92f-09eb-3322-9d12-17a10172e8a3 | -4.5614 | -48.0141 | 2024-11-17 03:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 174e9f1f-93ea-3fbc-a9cc-2347a5d99122 | -17.6059 | -57.5921 | 2024-11-17 03:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.0 |
| b6a70ddb-6dde-39bb-bf85-47cd0c50c6e8 | -2.8615 | -46.7086 | 2024-11-17 03:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 07ef3970-194e-3009-984a-af8cdb5be4f1 | -2.2111 | -47.2102 | 2024-11-17 03:10:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 7e0c2adf-8ba3-3112-bdfe-2874fbb6ded3 | -4.5616 | -47.9925 | 2024-11-17 03:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 4b44fa6c-45d2-3eb2-8e96-311e87fd7ebe | -3.3175 | -52.7648 | 2024-11-17 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| ec13200a-94b5-33e0-bf9b-5813ced13276 | -3.531 | -50.2337 | 2024-11-17 03:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| e15893d7-a250-3cd8-855b-676e2d6d7d31 | -2.6322 | -48.5634 | 2024-11-17 03:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| a07b79b7-e3ca-378a-9c52-725a829d9ee1 | -8.4522 | -44.223 | 2024-11-17 03:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 287a0f2f-7fca-3cfa-aaf8-2b61c21d1588 | -8.4525 | -44.1999 | 2024-11-17 03:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 316.5 |
| 23c58298-5fae-33ab-aa90-1a0d07226c40 | -17.6063 | -57.5715 | 2024-11-17 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.3 |
| 7c40feb9-903f-39bc-9840-bfea766c61df | -3.5125 | -50.2343 | 2024-11-17 03:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 6758cca8-f02c-302d-855a-ccfe63b21679 | 0.6159 | -51.7881 | 2024-11-17 03:20:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 62.6 |
| b91500d3-b9b1-3c8d-ad40-d500e4504283 | -8.4333 | -44.2251 | 2024-11-17 03:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| dae27bb3-f25b-34cd-8e3a-81c8a479f717 | 0.6159 | -51.7676 | 2024-11-17 03:20:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 1b8c6c1b-0911-317e-a299-0974d0a6d108 | -17.6059 | -57.5921 | 2024-11-17 03:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.4 |
| d4e4ff1a-ac8d-3ecb-a15a-b0e35dd5d273 | -3.5851 | -50.5255 | 2024-11-17 03:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 14a6a09d-e554-3f86-8bf3-43f0a66d6e16 | -3.5308 | -50.2757 | 2024-11-17 03:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| bd26e9b4-8c18-317d-be04-d69fcad8194d | -3.5124 | -50.2553 | 2024-11-17 03:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 2a6753ae-3137-32fa-83f2-468bd9a00a2b | -3.5494 | -50.254 | 2024-11-17 03:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| cbc7a40d-930b-37ff-be38-8e00a5793bf4 | -8.4336 | -44.2019 | 2024-11-17 03:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 263.5 |
| 8536519d-1fd2-3ade-ac7f-b6e0db0f1df1 | -4.5614 | -48.0141 | 2024-11-17 03:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| f358d29d-0041-3687-aa5b-fc2ac58568e7 | -2.8615 | -46.7086 | 2024-11-17 03:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| e20e1248-c401-312d-8543-12e432a93bca | -4.5616 | -47.9925 | 2024-11-17 03:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| f4a00daa-f626-3eb9-8d96-f2fed128e6f8 | -8.4528 | -44.1767 | 2024-11-17 03:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 4455058d-e5b0-391c-b602-3c8b18ae1698 | -2.8614 | -46.7306 | 2024-11-17 03:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 3c314011-8ea3-3d04-a91c-9f1f28013e5d | -2.5987 | -47.5705 | 2024-11-17 03:20:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| db368ffa-b1fb-3a36-bfa4-dc1833ff77b3 | -3.3359 | -52.7643 | 2024-11-17 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 5f155628-ae02-3438-834a-9d5a272b022f | -3.5309 | -50.2547 | 2024-11-17 03:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 256.9 |
| 6b251eae-c30b-3f83-b12a-0a2bf93fbce0 | -8.4339 | -44.1788 | 2024-11-17 03:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 53c325f3-419d-3ba7-b426-89926230261f | -2.8614 | -46.7306 | 2024-11-17 03:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| d50f49c1-2e05-3cc8-8fc1-af9a6cf56938 | -3.5308 | -50.2757 | 2024-11-17 03:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 5ba8fbc2-9330-3cb7-94f3-49b80ab99691 | -2.678 | -46.2059 | 2024-11-17 03:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 60.9 |
| ceb3e102-cfc5-3ef9-ad56-ae5eae44faca | -3.5124 | -50.2553 | 2024-11-17 03:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 8cfdfc39-9dfa-3eda-b512-1e3cdeaae468 | -4.5614 | -48.0141 | 2024-11-17 03:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| a7c4cccd-99e7-3b8c-bd2a-23e9a7de48d5 | -4.5616 | -47.9925 | 2024-11-17 03:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| a777f0e4-a873-3d14-81cb-522c78f8c4ea | -3.531 | -50.2337 | 2024-11-17 03:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 5bc97b1a-51fa-39ec-a314-bc1298be1f3e | -8.4528 | -44.1767 | 2024-11-17 03:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 3bfd320c-cc99-3e05-a9f0-30bbae765c0d | -17.6059 | -57.5921 | 2024-11-17 03:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.1 |
| 5c1a06ee-6a18-3896-8191-d4e5700b2871 | -17.6063 | -57.5715 | 2024-11-17 03:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.1 |
| 3f560b44-82bd-3502-8d21-7d1d3cde8e19 | -3.5309 | -50.2547 | 2024-11-17 03:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 324.6 |
| 312f570b-ed36-3f3e-8800-a5d5adebca33 | -2.8615 | -46.7086 | 2024-11-17 03:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| ff5ebb87-e2bf-3a8e-85d2-92ef4a87b114 | -8.4525 | -44.1999 | 2024-11-17 03:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 175.4 |
| 0bbcec23-3a58-3d7c-a572-ff62345e17d6 | 0.6159 | -51.7676 | 2024-11-17 03:30:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 89.9 |
| badf515f-975c-31da-ad00-18b8b7219c39 | -2.6322 | -48.5634 | 2024-11-17 03:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 2959af30-4bb0-3034-a960-62cfd2d76fcd | -3.3359 | -52.7643 | 2024-11-17 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 74538590-d72e-3f6d-9350-d10b334fe67f | -8.4336 | -44.2019 | 2024-11-17 03:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| c847ebaf-4f86-3b26-80ed-7c295e352c83 | 0.6159 | -51.7676 | 2024-11-17 03:40:00 | GOES-16 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 4e9f6dd5-16ff-3f7e-95f2-05297d5345db | -17.5862 | -57.5944 | 2024-11-17 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.7 |
| 60631375-77a7-30a0-b628-4688458f960a | -8.4336 | -44.2019 | 2024-11-17 03:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| ed1fcee5-11e4-30bd-93d8-039d8e2c4861 | -17.6063 | -57.5715 | 2024-11-17 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.3 |


[Clique aqui para ver as próximas entradas](README21.md)
