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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f95b765d-02e0-379e-a39a-8e5b8398c411 | -1.3776 | -47.5106 | 2024-11-08 00:40:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 192.2 |
| 2c3eaaef-96ee-3a4a-934d-2b6b0ed19f06 | -3.7254 | -41.6987 | 2024-11-08 00:40:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 173.6 |
| 6f7e403d-4d70-390d-b593-2412b3969209 | -2.82 | -52.9409 | 2024-11-08 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 093407af-ef58-344c-b52b-0cda7a18acc0 | -3.9485 | -48.1508 | 2024-11-08 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 891f4911-098d-3744-b87f-fddba0960158 | -3.351 | -45.2647 | 2024-11-08 00:40:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 8f2a6de2-e08f-39bc-a997-12c6dd4d129f | -5.9911 | -46.08 | 2024-11-08 00:40:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| ece1c64e-1831-3f99-9015-1fa8fc80c106 | -3.5447 | -47.3636 | 2024-11-08 00:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| f0613812-90f0-3b84-b1c2-8a348a94c0a5 | -3.1641 | -54.4854 | 2024-11-08 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 916a1d39-5afb-386e-a666-b51a98e2e1b7 | -3.1642 | -54.4654 | 2024-11-08 00:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| ba044eb9-e41f-382c-a6c7-c724f01da054 | -4.7018 | -46.4508 | 2024-11-08 00:50:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 696b619d-d4e1-3f65-a8dd-9832d0677eb9 | -4.6646 | -46.4528 | 2024-11-08 00:50:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 9c7da366-4833-388c-a7db-2e418b2dea5b | -1.3776 | -47.4888 | 2024-11-08 00:50:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 2884cb67-5353-3fc3-b592-61b9c6ba9c29 | -2.6764 | -51.8189 | 2024-11-08 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 1464b1c4-12ee-3457-8f7d-0c8addf5dd00 | -3.7255 | -41.6748 | 2024-11-08 00:50:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 126.5 |
| 96c52ff7-bd4a-37ef-92bc-249de05e172b | -2.8016 | -52.9617 | 2024-11-08 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| a0a5f207-641c-3a23-900e-200ab9c489cf | -4.6834 | -46.4296 | 2024-11-08 00:50:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 245.6 |
| bc9c0240-6497-36a7-be4a-b962580a33fc | -6.2642 | -39.3546 | 2024-11-08 00:50:00 | GOES-16 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 6e029df7-e229-380c-84e4-b20555011716 | -3.9669 | -48.1716 | 2024-11-08 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| b696f39b-9e30-3e97-9dc3-3f5b6e808fd3 | -2.8016 | -52.9414 | 2024-11-08 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 305.4 |
| a8f42288-ae50-3fe0-8753-6f257c1e1730 | -3.7066 | -41.6997 | 2024-11-08 00:50:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| c9b3edea-ffe9-32b4-b2cb-12006c25106f | -3.1458 | -54.4659 | 2024-11-08 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 1356bd2c-24ce-3520-9c3a-8b8549432205 | -3.5631 | -47.3847 | 2024-11-08 00:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 934c6ee6-7d9d-3694-9b2f-5adf137a5635 | -2.6214 | -51.7378 | 2024-11-08 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 5ccdec47-9b86-3f6e-9588-ac201da55347 | -3.9485 | -48.1508 | 2024-11-08 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 819f2986-db46-33b2-8b00-73dcaafb7962 | -3.7254 | -41.6987 | 2024-11-08 00:50:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 130.8 |
| 73475e4d-c91d-3dee-aa91-fa8c7ed64df0 | -2.82 | -52.9409 | 2024-11-08 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 142.2 |
| 657793e7-71d9-3f2b-baa5-97e3fadb7aa0 | -3.5632 | -47.3629 | 2024-11-08 00:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| c0c391ac-650a-3a6d-b1d9-38a2cb3bef73 | -3.1458 | -54.4859 | 2024-11-08 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 515828df-d322-3eb9-9be5-555f5bf5594b | -3.0698 | -45.747 | 2024-11-08 00:50:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 6295c227-6f85-30fe-ab2e-45e03d15af5f | -3.9854 | -48.1708 | 2024-11-08 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 8119faa1-bdcf-3f2a-8ae6-6a7ed4eec80b | -3.5446 | -47.3855 | 2024-11-08 00:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 9148aacc-eb7b-31e0-b69a-8bd38e654ccd | -2.6228 | -51.3038 | 2024-11-08 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 22237ed9-0d07-3df6-9477-fe6977f9f16a | -3.068 | -50.5631 | 2024-11-08 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| ec72794e-5280-39d4-ab16-92532e280a09 | -6.264 | -39.3797 | 2024-11-08 00:50:00 | GOES-16 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 89.7 |
| d198e783-7959-3048-a210-9cf7079fa0b2 | -3.4838 | -52.617 | 2024-11-08 00:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 4fae04d4-ab9f-39ae-89ae-e20b501d20f6 | -1.3776 | -47.5106 | 2024-11-08 00:50:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 90c95f25-319b-3008-83ff-9545e7004249 | -2.82 | -52.9613 | 2024-11-08 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 76ce141d-9d59-3740-a2fc-accc239c3894 | -3.5447 | -47.3636 | 2024-11-08 00:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 61c979f9-c66a-311e-a00c-099f46901695 | -4.6832 | -46.4518 | 2024-11-08 00:50:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 434.4 |
| de1e713b-0472-3b3a-9f1a-39bc30955359 | -1.3961 | -47.5103 | 2024-11-08 00:50:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 9683739c-87a4-3c36-8335-1a0b9f5b200e | -3.1642 | -54.4654 | 2024-11-08 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 2a3e02af-c781-3a2f-94b2-968bb04df095 | -2.6214 | -51.7585 | 2024-11-08 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 586c621f-9996-3ee2-8ec0-decf530a6ba9 | -3.9483 | -48.1724 | 2024-11-08 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| d842e5f8-0d7e-3e23-82c3-e027472108e9 | -3.967 | -48.15 | 2024-11-08 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| a0747105-1be2-3350-add5-311e8d71d7ce | -1.3961 | -47.4885 | 2024-11-08 00:50:00 | GOES-16 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 72ba4310-51b9-3f45-9a0b-a5ae172b9654 | -3.351 | -45.2647 | 2024-11-08 00:50:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 0060f71f-0214-3a3e-b742-ff8e726607c8 | -4.6835 | -46.4074 | 2024-11-08 00:50:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 3904cb1d-d793-34ae-856f-4d94e6d858a4 | -4.702 | -46.4286 | 2024-11-08 00:50:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 81.2 |
| ce70288a-566c-3f70-bf98-4983635264c4 | -3.1641 | -54.4854 | 2024-11-08 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 234b7503-f6b6-35b2-9c73-a5e805341277 | -2.7832 | -52.9418 | 2024-11-08 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 24b48ecd-c426-3db6-81cf-719e4265b9cc | -2.8017 | -52.921 | 2024-11-08 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 77043b2d-1ef1-37f9-bcee-75b83b3448af | -1.5079 | -52.157299 | 2024-11-08 00:56:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d917b476-eae4-3574-a20f-768453384a01 | -2.275 | -53.801102 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f03043c9-da92-303a-828a-480c82516d3b | -2.156 | -53.640701 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74e57683-616f-3c8d-925f-0d4d5299d142 | -2.2867 | -53.807301 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebfadc13-b7dc-3f60-83a1-bec103b3f7f6 | -3.027 | -53.2617 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92ecf3fd-c190-3718-af2d-e4d47c4378d6 | -3.9524 | -48.165401 | 2024-11-08 00:56:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ac56960-5e3b-32f4-bbfe-c768154dc2a3 | -1.1503 | -51.986801 | 2024-11-08 00:56:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2693e80e-7e27-37ab-b634-211457e9984d | -2.8304 | -52.899399 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1367c3e4-36d4-3708-98d9-4d4cf53605c2 | -1.2406 | -53.3736 | 2024-11-08 00:56:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ab1ce33-3206-303c-ad99-7b2fe760ab44 | -3.4737 | -51.584801 | 2024-11-08 00:56:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f3846ca-8de4-3886-8155-10b3b16e9ff2 | -2.6164 | -51.746799 | 2024-11-08 00:56:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 077724e8-d168-3b0b-83ae-294886c46fe0 | -3.9621 | -48.163101 | 2024-11-08 00:56:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7956253d-9cf4-3074-873d-a036280f41ce | -3.243 | -53.395199 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30089568-39e1-31b5-9a74-cd863c626bb3 | -1.3362 | -54.6082 | 2024-11-08 00:56:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46b0b60a-b87c-34f9-9239-cf2d51a1736b | -4.5102 | -45.695202 | 2024-11-08 00:56:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6bc47058-a14f-3920-89a6-68c6d1470985 | -1.8249 | -53.6791 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c688765c-98f2-3493-8af5-ec6604281dcd | 0.745 | -59.760899 | 2024-11-08 00:56:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8ad49f46-dc78-3826-ab99-6cfd031e0434 | -2.8075 | -52.933701 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9116e61-ad8e-301b-b0c3-62fe3e09117b | -4.5006 | -45.697498 | 2024-11-08 00:56:00 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4396886e-56f3-3e2c-a9e0-f1a9cf392ecf | -0.3652 | -51.425999 | 2024-11-08 00:56:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 15d0124d-d6ce-3b56-9daf-df5c72d67eae | -2.2558 | -53.7169 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87d097b7-28db-379d-8232-1f5efbc01e94 | -2.6705 | -51.803101 | 2024-11-08 00:56:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26fe9e61-3e76-3c3f-9c91-d8e992a41227 | -2.7998 | -52.945099 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3f6bd3c-67f7-3597-b3e2-8b322d7504a7 | -1.455 | -53.4109 | 2024-11-08 00:56:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68384410-f68e-3f3d-aad8-5ec05b37278f | -5.0759 | -47.935001 | 2024-11-08 00:56:00 | METOP-B | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1b6455fe-8850-3a94-9950-300e6c359335 | -2.8194 | -52.940701 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb5f5100-a74e-38f3-83b0-50397cea2020 | -4.5068 | -45.639599 | 2024-11-08 00:56:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e32cc13-d53e-342e-9838-f60081408ec6 | -2.8117 | -52.952099 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be4dd0ef-1edd-3dc8-bcfb-027d423530e8 | -3.09 | -53.311699 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08424deb-a10b-3afa-9803-7a5ef16273e2 | -2.8215 | -52.949902 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a0eab97-b37b-3db1-88cf-33a124cdacc2 | -2.1541 | -53.632099 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b81b85b1-6bdc-359d-8417-9aed21154d69 | -3.0521 | -45.733002 | 2024-11-08 00:56:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f87def94-5b36-3642-a0d5-4133abd668d1 | -2.8236 | -52.959 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ff8d981-108e-3d3d-9c28-3b7dda7f64c5 | 3.2638 | -60.469501 | 2024-11-08 00:56:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 68e6902f-c270-3da9-999c-2369256289e2 | -2.0522 | -53.2766 | 2024-11-08 00:56:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34d221a2-dc47-332b-8c1e-8c5518c715ef | -3.6735 | -51.2938 | 2024-11-08 00:56:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 343de169-69d0-3eca-93e4-9714b78bff54 | -3.0139 | -53.429001 | 2024-11-08 00:56:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 597900b9-3a23-34ea-bc4f-c60d9bd491bb | -4.6637 | -46.447899 | 2024-11-08 00:56:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9b7c6da8-b232-3141-8aef-f960498db154 | -2.6148 | -51.2953 | 2024-11-08 00:56:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88258522-d38c-3d90-943d-75c36f8772c5 | -1.254 | -53.3419 | 2024-11-08 00:56:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a30d474-943b-31ff-a87c-1222cfb787b2 | -1.5177 | -52.155102 | 2024-11-08 00:56:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24fe7de6-23a4-31b4-abee-9f9e921305ff | -1.4127 | -54.491501 | 2024-11-08 00:56:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 927e4997-1d3a-3723-92fa-79ae7b0fe4a2 | -2.7696 | -54.027199 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23aed441-9c06-3e41-94c8-48a09310fb5c | -4.6075 | -46.511002 | 2024-11-08 00:56:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 15af24ba-afdc-3c53-b2e5-1805e33fc4dd | -1.3326 | -54.5924 | 2024-11-08 00:56:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccd29f26-d69a-327a-809f-9f2d10c47330 | -2.9364 | -52.688499 | 2024-11-08 00:56:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db00222e-f9f2-313d-93fe-09038b566664 | -2.8112 | -53.9837 | 2024-11-08 00:56:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e725c99b-ee76-3c9d-85fb-e9c6f663872f | -4.5037 | -45.668701 | 2024-11-08 00:56:00 | METOP-B | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cd2966ca-5c02-31db-9f85-1c431f008028 | -3.4895 | -54.562302 | 2024-11-08 00:56:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
