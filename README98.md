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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7c38b47-6616-32d2-8f09-596363634ec0 | -12.99536 | -53.46137 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1187eb38-7795-369f-8fb1-c9db459291ee | -12.99474 | -53.46618 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44d31836-c890-3a68-833e-7ce40391356b | -12.99079 | -53.46077 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b099db96-13aa-371d-a507-b471257d58ae | -12.99017 | -53.46555 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63d52776-4fa8-32ce-9c99-4a76365510cc | -12.98622 | -53.46013 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ec7e698-10c6-385c-b348-94be1c2fc2df | -12.98561 | -53.46489 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 613352e0-be5b-3ed2-ad37-fc8e93053f2f | -12.985 | -53.46964 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 359eb000-3c28-3d30-9298-aab473d3e5eb | -12.98105 | -53.46418 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e433cbc-7847-3553-80b5-930d21386b33 | -12.98045 | -53.46892 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52d5deca-4c4e-3a27-9a8f-305ee315effa | -12.97649 | -53.4635 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 179b1d68-a425-363a-b25c-c60f1db1ba72 | -12.88251 | -53.46796 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79641705-dee5-3f9d-9d5e-e5826113c58b | -12.87857 | -53.46253 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8729d19-3e0f-31e7-9ba1-678f05bd40ec | -12.87795 | -53.46733 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b24da27-3e90-31b4-88c3-658bae8d1a5b | -12.87523 | -53.45238 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c4ae231a-7c42-3e90-ad4b-4542d785cf68 | -12.87462 | -53.45715 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 32079128-6e0f-387e-b78c-6a499a4337d5 | -12.87401 | -53.46191 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0fd50204-be10-367c-a92f-3415b284cfcb | -12.87339 | -53.46672 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3da570b5-d00c-3eba-a949-60036109d3d3 | -12.87067 | -53.45177 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d0c907ff-5d68-31f0-8ba4-b93115f719b3 | -12.87005 | -53.45657 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 89010b1e-ed66-37cd-a87c-9d1db6d69d48 | -12.86944 | -53.46133 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ff811f9d-fce5-3c00-9a33-397909be16ee | -12.86883 | -53.46612 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a303dbf6-4ea2-394c-b375-ebea5653bbda | -12.8661 | -53.4512 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c1a5afa8-0b29-3429-bea3-fc29c4bc0ff3 | -12.86548 | -53.456 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3af81234-876f-3f52-86e5-8fa5e676aa18 | -12.86487 | -53.46077 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 3251c9bb-0e5c-3ea2-b0f3-5738caafd6d1 | -12.86426 | -53.46553 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| e434545c-424e-37a7-a75f-24463e44fc91 | -12.86152 | -53.45063 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e14ebbfd-ef3f-3c95-b7f0-9665c4858172 | -12.86091 | -53.45541 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3ded7985-8da8-39dc-94d3-d0b126cfe7d9 | -12.86031 | -53.46017 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| a687fa53-0c2b-3279-bed2-b8540089459f | -12.8597 | -53.46492 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 5aaf945c-274b-3ebd-97f8-6eda050978eb | -12.85909 | -53.46967 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 03acc261-32ce-343d-b468-1aa0a976d15c | -12.85635 | -53.45479 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2af40617-0598-3283-95e5-579ca1918dad | -12.85575 | -53.45955 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 8800b085-fca5-315e-b035-f460bae1d7af | -12.85514 | -53.46431 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| df423dcc-8d9a-3dc6-987d-391b3683ece5 | -12.85454 | -53.46906 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| a90e33fe-bca2-3f53-8dbb-97352a2dca56 | -12.85179 | -53.45414 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6590df3d-e762-3d89-bef5-b11961fb8caa | -12.85119 | -53.4589 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 8c95b31f-7990-36f1-aafd-57246e9a09f2 | -12.85058 | -53.46366 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 7d1cf99d-ca04-3b9c-ba06-90af9d6e4649 | -12.84998 | -53.4684 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 18a35ffa-8bfb-3d03-8dc1-e59a19c5e232 | -12.84723 | -53.45346 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3a125778-6a41-39a3-af4e-09deeea5fddf | -12.84663 | -53.45823 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| caf0c864-ab95-3cff-b58a-ad7a000dfc0c | -12.84603 | -53.46299 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77fcd1fb-458e-3afc-b8bb-d67d61c5408f | -12.84543 | -53.46774 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 32.2 |
| ce9e9536-5668-3332-9f44-1bbc0822890b | -12.84268 | -53.45278 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 68c04427-287c-3756-9110-2780de4bf196 | -12.84216 | -53.45027 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2fdaa064-c3f0-3376-b6cb-9b8c399bee15 | -12.84207 | -53.45756 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6088c3b4-d9c2-33f0-9acf-1adb7e281aa5 | -12.84153 | -53.45504 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c14e0bf-3ef9-327b-9dea-214a16a62464 | -12.84147 | -53.46233 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be1baf65-f110-3070-860c-545de28db2a8 | -12.84089 | -53.45981 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 296280ae-deb5-3d9d-83ef-5091c0bfdb82 | -12.84087 | -53.46708 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 32.2 |
| c8145c13-8217-387d-ba3a-5c4d4764f9c4 | -12.84025 | -53.46457 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 100be8a7-7858-3142-b016-8d189b8b87e9 | -12.83961 | -53.4693 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 088cc642-801e-3c0a-9052-838b74944f94 | -12.83812 | -53.45209 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 41abe14e-fa28-37e7-ab4c-dfa1c8259cc1 | -12.83752 | -53.45688 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cfffe02c-5d67-33eb-9d41-0b5fbd964e7d | -12.83697 | -53.45437 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c143c49e-c71d-3c79-b37c-1730910bef7b | -12.83692 | -53.46166 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9348652-750e-33c7-9b14-82467b009508 | -12.83633 | -53.45914 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| be77271a-7e8f-3027-8818-e69c57a96569 | -12.83632 | -53.46641 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 447d140b-03c2-392e-834b-c83894e31a08 | -12.8357 | -53.46391 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b06d2d23-0bf0-3f54-b867-f04e0749de5a | -12.83506 | -53.46864 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fa791fc4-77b1-3d8a-941b-d94d2c5f7cff | -12.83236 | -53.461 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 16f1bfc6-64e4-38db-980f-27be81e4753f | -12.83178 | -53.45851 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc0cb01e-a73a-30c6-8851-faf50d75b231 | -12.83176 | -53.46574 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3024eaf4-01df-3624-a5da-e416bd533c81 | -12.83114 | -53.46325 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f89c619-df3a-310e-8274-6ae38af2ded0 | -12.83051 | -53.46798 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a28becc-d5fc-3f39-9eb2-7ad5616cfd7b | -12.82597 | -53.46729 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8fc317c3-72af-387f-bb2c-9b49f6e2d24a | -12.6395 | -53.1081 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cb462487-6746-393a-8f97-43004c85dbcf | -12.63484 | -53.10746 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f662719f-d7da-3d99-939c-0c0d8832dfd1 | -12.58679 | -53.07549 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36c01502-f56a-396f-aa87-ccd47434e46e | -12.58276 | -53.06982 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b0f4a36-f603-3d92-ac0c-d670247147e3 | -12.5781 | -53.06915 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b551f492-0912-3ce6-8b11-57327bc8175b | -12.57407 | -53.06343 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e07af7d1-1896-3ebc-b42e-1c58756b0f41 | -12.57344 | -53.06849 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9db4888-3d93-3fd0-94ec-58cb99f2d4c9 | -12.57216 | -53.07861 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0bf265f-a8b6-3855-9d5e-43e173992c4d | -12.57096 | -53.06551 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6c9f24f-922a-3d6c-961b-0b9decd736d4 | -12.57028 | -53.0706 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26eb086a-77c9-316f-8d7f-c2080bc60f7a | -12.56961 | -53.07565 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d1766e8-c219-38a1-bd29-6ee3f3fddcd1 | -12.56894 | -53.08067 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09a5dfd3-e59c-384a-802e-c10cf90d7ae4 | -12.56878 | -53.06781 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f734a20-123a-3cdb-a416-027dfe0f463d | -12.56814 | -53.0729 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 232d466f-e5af-39c7-ad23-2abb08c1a1db | -12.5675 | -53.07796 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8eea7724-1aeb-3c8d-9bab-6738bf8e26a0 | -12.56563 | -53.06993 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29d5f145-75e9-31c6-8be5-07c81248d8eb | -12.85849 | -53.47443 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| d86da21c-44d4-39b2-8bce-e3244a6731a7 | -12.85788 | -53.47919 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 46219079-87ea-38ce-8fd1-f50f38c54614 | -12.85728 | -53.48391 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 13338735-21f7-3c82-ae91-a62b44c20ccc | -12.85667 | -53.48863 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f8f33f24-0016-3cf8-819c-ea4ce5387912 | -12.85607 | -53.49335 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a2d3643b-e366-3795-a1d9-68c48a151294 | -12.85393 | -53.4738 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 4e524a9f-8c0d-3cd1-96a1-df717e7a5d4e | -12.85333 | -53.47853 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 1b187ee4-de53-3ed3-bbc0-9b16470e029c | -12.85273 | -53.48326 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 40.8 |
| c56254ac-90f9-3107-968d-99d81f1b977d | -12.85212 | -53.48798 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 8d2ad611-75b6-3337-acd9-2b7883ac36b6 | -12.85152 | -53.4927 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 17e4ec06-6dd0-398d-bf3d-bd5f7a9ff6d9 | -12.84938 | -53.47314 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 05bae11a-fdb9-35fe-b80e-9403f667f438 | -12.84878 | -53.47787 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 40.8 |
| e38cf5a0-16b7-371e-b390-f0b4257fe9ba | -12.84818 | -53.4826 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 40.8 |
| e2bed232-2cd0-383e-97d0-0e19df4139f6 | -12.84758 | -53.48732 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 3f9ae657-e7d9-34c3-90fc-24dd95fcc971 | -12.84697 | -53.49205 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 90629f74-e609-38ba-bd89-6d89087859fb | -12.84482 | -53.47248 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 32.2 |
| ca86c9fb-d883-35b2-8054-8d00a3b46fe1 | -12.84422 | -53.47722 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 9472c021-0cc4-3e3f-adb3-8c97b330a63b | -12.84363 | -53.48195 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| d0390079-d240-3a99-a33f-c955f2ede895 | -12.84303 | -53.48666 | 2024-10-11 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 391.9 |


[Clique aqui para ver as próximas entradas](README99.md)
