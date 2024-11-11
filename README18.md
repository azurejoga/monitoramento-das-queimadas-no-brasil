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
| 653210fb-b678-3d42-96ac-d56061de8d4f | -2.189 | -48.3815 | 2024-11-11 01:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 74171ffe-e94c-392c-9b82-51c480a30665 | -17.2936 | -57.4652 | 2024-11-11 01:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.4 |
| 17a34f3d-8a81-3496-8b4d-a827f50a8d8e | -3.0296 | -50.9607 | 2024-11-11 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 7d23eec6-cea9-33df-adf6-522e1eecf7d1 | -17.6086 | -57.4276 | 2024-11-11 01:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 93.2 |
| 186b3aa9-1f7f-36a7-a8c8-9ea3f9eedc29 | -4.0294 | -46.9484 | 2024-11-11 01:20:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 55.6 |
| cdda1d88-0f24-30e5-ac6f-bf3a507ee0d9 | -17.2933 | -57.4857 | 2024-11-11 01:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 161.7 |
| 3339afac-bb5f-3c4b-88f5-688a4822c9db | -3.2773 | -53.6787 | 2024-11-11 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 64665125-a5df-382e-a353-2668d86bbeaa | -3.6217 | -50.587 | 2024-11-11 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 96d836fa-9df6-387c-9445-05d994113ed8 | -3.0295 | -50.9815 | 2024-11-11 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 4cf62033-3671-3cba-835a-0c645c03c84b | -4.11 | -49.1102 | 2024-11-11 01:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| ce5418e0-783a-3b93-a04f-186d51b25051 | -3.1458 | -54.4659 | 2024-11-11 01:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 572f3c01-0dbf-3f94-a963-b23eb65fae30 | -3.0214 | -53.2404 | 2024-11-11 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| e021eb7a-02fc-3dbe-b5d9-78322814ed83 | -17.2933 | -57.4857 | 2024-11-11 01:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 149.7 |
| 2d2dc776-06bd-3bf0-bd05-36a4d893e989 | -3.6954 | -50.6262 | 2024-11-11 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 7001593b-ad35-37a4-a324-ebd459cbe2a3 | -2.8508 | -49.4108 | 2024-11-11 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 4bd48390-7dbc-3098-ba29-4fbfa35d90f6 | -2.1891 | -48.36 | 2024-11-11 01:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 66066546-49f3-3385-92ce-44037b80cd1e | -3.0295 | -50.9815 | 2024-11-11 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| b3d8746e-b41f-36b6-b9c7-13526b06a2e8 | -3.0296 | -50.9607 | 2024-11-11 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| e2251489-3cde-3e21-9eb1-25eddbf4815e | -3.2427 | -53.0722 | 2024-11-11 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| e7929a70-68d1-3fff-a8a3-dfbe6ad47133 | -3.3836 | -50.1336 | 2024-11-11 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 0d4e3607-7c40-3cc9-a34f-fdf6d7db92de | -3.0138 | -45.8161 | 2024-11-11 01:30:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 3bc3106f-a855-373f-8a9d-9415f07b0287 | -2.189 | -48.3815 | 2024-11-11 01:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| c441f6ab-3fe3-3997-a912-46d339bbffec | -3.1458 | -54.4859 | 2024-11-11 01:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 799369b0-a198-38ba-b48e-eca63882609b | -2.8508 | -49.432 | 2024-11-11 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 129.4 |
| 04b06d42-ca76-34c2-9047-a3e6397c9985 | -2.2504 | -46.5061 | 2024-11-11 01:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| a65f5e6f-0bf1-3b0d-90e8-74957493ad12 | -1.4057 | -52.3758 | 2024-11-11 01:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 327a08ac-fefe-358e-ab83-1ed38167c378 | -3.4021 | -50.1329 | 2024-11-11 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 28227611-dbf4-3949-9096-b2bf51e8b58b | -1.4057 | -52.3553 | 2024-11-11 01:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 86b075f0-01a6-3793-b6ec-8ec356b81255 | -3.2428 | -53.0519 | 2024-11-11 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| be6d2328-c1b1-3f46-94a8-ff59db4dbc1a | -3.2588 | -53.6994 | 2024-11-11 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 2251bf02-53a2-3c24-82d3-c997b87ad85f | -17.2936 | -57.4652 | 2024-11-11 01:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.1 |
| b46710e9-7c37-360d-b14a-68ab1de513f7 | -3.2772 | -53.6989 | 2024-11-11 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 24eda819-1b10-396c-a74c-a9b666157450 | -4.6835 | -46.4074 | 2024-11-11 01:30:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 6e53aaaf-be8e-333f-9316-9ee6f70c84cc | -2.4367 | -51.948 | 2024-11-11 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| dd9a0755-45ad-3f54-8336-5ffff0c28757 | -3.6218 | -50.5661 | 2024-11-11 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 96b29a07-d792-3578-a39f-1f59d765a173 | -9.7745 | -36.395 | 2024-11-11 01:30:00 | GOES-16 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 85.3 |
| 52d92425-5b9e-3de2-8840-b0011719f646 | -2.2075 | -48.3811 | 2024-11-11 01:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 212a7cf6-a9c3-3344-9450-405fe2bbe76e | -3.2773 | -53.6787 | 2024-11-11 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 4592ca17-b90c-3823-bc50-7b0e18384344 | -17.313 | -57.4834 | 2024-11-11 01:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.3 |
| 01625104-9987-3c6b-a476-616dc640d548 | -3.0324 | -45.8154 | 2024-11-11 01:30:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 79.9 |
| a5315d58-421e-322f-8e8c-2f1c765f4c10 | -2.3863 | -50.3299 | 2024-11-11 01:30:00 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 55963aa0-bc42-3e86-a93f-74d52f45241e | -17.6086 | -57.4276 | 2024-11-11 01:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.8 |
| d3758344-e9ad-3553-92e8-b8b9b29054ff | -3.5346 | -45.7061 | 2024-11-11 01:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |
| e7f10d63-a97c-36f4-ab15-a9ca2d38e4a2 | -3.2774 | -53.6585 | 2024-11-11 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 5e2fa23c-caba-3571-979f-b9f709589aff | -2.9355 | -51.482 | 2024-11-11 01:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 761a6793-c04e-3b7c-bcc4-e4977819445d | -3.6217 | -50.587 | 2024-11-11 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 929a3513-defc-3ccb-ab46-789ef8d36fd8 | -3.2243 | -53.0727 | 2024-11-11 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| e63e2b9a-84ae-35ca-9ccc-87cab1f39258 | -3.0213 | -53.2607 | 2024-11-11 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| e78afc9e-1c44-35d9-8753-2d945b700d09 | -2.8323 | -49.4325 | 2024-11-11 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 514f6200-b1cc-3bb1-b18c-b7fdcfa021e8 | -3.2244 | -53.0524 | 2024-11-11 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| b00c1fd2-6e3c-3572-b042-f1e9942669a1 | -3.0111 | -50.982 | 2024-11-11 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 19c412e3-dfa6-3380-a58c-6257bb6cb313 | -3.1097 | -54.2865 | 2024-11-11 01:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 17620180-a2aa-362c-8305-42645b87b00c | -1.3873 | -52.376 | 2024-11-11 01:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| dfdaf9ff-73a0-39e4-9898-dd22e05bc11f | -17.677099 | -57.507801 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 90d1fc08-85d2-3557-bb53-219320089d49 | -17.2761 | -57.48 | 2024-11-11 01:33:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 27afa5e2-3748-310e-8a1c-7f17b8fc5fff | -17.692101 | -54.090698 | 2024-11-11 01:33:00 | METOP-B | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 23a03ed7-f232-3028-8951-3bce182d2f75 | -17.6091 | -57.526402 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a605f13c-44c8-3c60-bbf1-edade1e8a992 | -17.5839 | -57.508499 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6a208a2c-1f39-3906-bb8c-2cd1574bddaf | -17.6052 | -57.428001 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fc9af5bf-effb-3c74-963b-6349dbac0969 | -17.2955 | -57.4748 | 2024-11-11 01:33:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 22c57618-38d1-38a9-a944-0b8208d9917a | -17.237301 | -57.490601 | 2024-11-11 01:33:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a35639c3-a579-38da-8454-c84f45332212 | -17.592501 | -57.543201 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 85c1bbc5-032a-37d0-a383-c94d70f17d27 | -17.282801 | -57.299999 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6971ce2f-bad2-3c94-a714-9b1e8d550833 | -17.301399 | -57.498299 | 2024-11-11 01:33:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ae570147-039a-35ba-b033-2b8251ac2039 | -15.9729 | -59.343201 | 2024-11-11 01:33:00 | METOP-B | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| def7e471-e370-3286-9f57-6d93cbc54068 | -16.0814 | -60.098999 | 2024-11-11 01:33:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 010b4b6d-c56c-336e-8847-33df7b583018 | -13.4841 | -60.6567 | 2024-11-11 01:33:00 | METOP-B | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 949e1b4f-6c2e-3ac2-81b1-8da1aa4dd859 | -17.627501 | -57.434399 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8548d2e3-687e-3884-8641-835260d06151 | -17.618799 | -57.523701 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7ada92bf-f44c-3185-94b0-fa06ed27ccfd | -17.5828 | -57.421501 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 651fbc05-d2db-380e-aad0-937e0e20358a | -17.614901 | -57.425301 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a4bf921b-46d8-3a3e-a94a-cd521c8f6dd3 | -17.588699 | -57.445 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4fe6381d-8e3f-3d7a-a959-21ca860c02fe | -17.6285 | -57.521099 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 656514f5-51b8-30ce-a5cc-a733a76a0200 | -17.5994 | -57.528999 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4f4cabb0-0683-3151-a721-5e6c1a130e66 | -17.5965 | -57.517399 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 69549514-ca7c-3fe2-a40c-83b4f67c734a | -17.612 | -57.537998 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b12430bf-14de-3e41-85a1-dc6875563744 | -17.6178 | -57.437 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9ccd53bb-927b-38cd-be76-3f43a9784a7f | -17.682501 | -54.093498 | 2024-11-11 01:33:00 | METOP-B | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 443624a6-f3f0-302a-b218-55717dbcc67e | -17.282801 | -57.465698 | 2024-11-11 01:33:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| caa7a3e6-94d8-325c-9a6e-aaba9c8fdcde | -17.686899 | -54.071602 | 2024-11-11 01:33:00 | METOP-B | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 32a8224a-1b50-3e97-99c5-0b839181ee15 | -15.9683 | -59.3241 | 2024-11-11 01:33:00 | METOP-B | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e2324b96-2b79-3dff-aa5c-8ed6654691cd | -15.9752 | -59.352798 | 2024-11-11 01:33:00 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 76cda646-b50f-3344-89a3-77a797b38549 | -15.3107 | -56.512699 | 2024-11-11 01:33:00 | METOP-B | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 83b2747b-23cd-37e6-8b50-fac2212dfc3a | -17.278999 | -57.491798 | 2024-11-11 01:33:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a10a72e8-785f-37de-9024-5463641d4dd4 | -17.234301 | -57.478901 | 2024-11-11 01:33:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 97bf8378-a00b-3702-a8a9-3b124cd9ce57 | -17.3081 | -57.483898 | 2024-11-11 01:33:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e21ab267-a08d-3088-b619-d187898925d4 | -15.301 | -56.5154 | 2024-11-11 01:33:00 | METOP-B | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8077d0c2-37fa-3137-b925-1bac4b5baec5 | -23.9167 | -54.0443 | 2024-11-11 01:33:00 | METOP-B | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8880c9f9-a14a-3817-ad5d-184ff939086b | -17.6022 | -57.416199 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 77572c1b-2394-3f5d-b74e-e428d5368974 | -17.5984 | -57.442299 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 384205a1-682c-3512-adb2-c264861b6b28 | -17.247 | -57.4879 | 2024-11-11 01:33:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1231c633-3b4d-39b0-9fe2-644c0fb9cf06 | -17.638201 | -57.518398 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 586319ce-e6e3-3830-b1f5-3bfbf3e65942 | -17.285801 | -57.477402 | 2024-11-11 01:33:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 70b7ed79-df94-3384-9d1e-63f263da5630 | -17.6022 | -57.5406 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 96c7bccf-8408-3337-94bc-02656cfe85b0 | -17.606199 | -57.514801 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d500f648-09a1-3955-963c-8f4b68a34fb9 | -17.608101 | -57.439701 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 075ca710-3ee0-341e-90ef-d927880f142f | -17.595501 | -57.430599 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c1a61c0f-b0a1-35be-840b-2a1a0d3efc19 | -23.912701 | -54.029202 | 2024-11-11 01:33:00 | METOP-B | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 71f86e20-b85d-38c3-980a-3d9351234be5 | -17.589701 | -57.5317 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1d6022c6-fa55-30fd-a2f1-526bc610dcff | -17.6217 | -57.535301 | 2024-11-11 01:33:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README19.md)
