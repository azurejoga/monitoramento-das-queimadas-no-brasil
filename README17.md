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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf113bc2-6dc4-3adf-af32-2cc81b8cf82e | 2.59023 | -60.6954 | 2026-06-23 05:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eac11ca1-4ecd-3268-b5bf-b1322cc3a8fa | -10.27782 | -60.54506 | 2026-06-23 05:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 62447bd3-a6b3-3157-af0a-77144addb128 | -10.27307 | -60.5484 | 2026-06-23 05:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48bdf60c-2ecd-334e-a9c2-664d5769924d | -9.60838 | -56.92727 | 2026-06-23 05:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d008941a-01af-3f34-b302-88bc3ff741be | -11.04508 | -52.46671 | 2026-06-23 05:46:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 839c51b0-160c-308f-ad17-f13da02ad35c | -10.27727 | -60.54905 | 2026-06-23 05:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b9dd4f5-dc2a-3548-afaf-4105433f2aa1 | -10.27362 | -60.54442 | 2026-06-23 05:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3c05ae2-3d91-35bb-8b22-5da30e7c773c | -10.77111 | -54.1112 | 2026-06-23 05:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5eb47f4b-7a92-3135-914c-7007eaf443dd | -10.77682 | -54.11504 | 2026-06-23 05:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57e688b9-78dc-3bad-836c-513efdd1d4ac | -11.05509 | -52.46751 | 2026-06-23 05:46:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 225c228a-4274-3d9b-8b88-ae94cb1dc878 | -10.77034 | -54.11415 | 2026-06-23 05:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fd4c542-6dc5-3f49-bc42-c6f543138cfc | -9.38348 | -58.20506 | 2026-06-23 05:46:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56a36b02-fabc-3ea3-b6f2-9865f2489e0e | -11.04794 | -52.46643 | 2026-06-23 05:46:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 04740135-44bd-3a4b-a9ea-d594877576c4 | -9.37859 | -58.20443 | 2026-06-23 05:46:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66c1f6fb-3f67-3f75-bde1-d1730e3e4cc7 | -9.38052 | -58.20399 | 2026-06-23 05:46:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 92ea472a-dda9-390e-ad9a-e6bb5aedb326 | -11.05222 | -52.46779 | 2026-06-23 05:46:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7cdd4560-37cc-3c65-b426-ad67ace483a8 | -10.77759 | -54.11211 | 2026-06-23 05:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45253e3e-dfbf-3935-a42a-acee767efb50 | -10.93801 | -56.84852 | 2026-06-23 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21d3329b-898b-3964-b2c7-93ca4808b7cb | -11.80267 | -52.53287 | 2026-06-23 05:48:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| af816b49-2ad8-3c2d-9757-e82adec48839 | -12.55021 | -57.19273 | 2026-06-23 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 73f34119-ee1d-33e8-8215-003233d827f1 | -12.28527 | -57.57209 | 2026-06-23 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ca72fd8-e38c-3706-8f83-0c2dbea43013 | -11.87877 | -57.83148 | 2026-06-23 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94c3179b-b52c-3d6f-8a6d-1110ac7bd517 | -11.80721 | -52.53248 | 2026-06-23 05:48:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7ec07b90-8ba6-3aa1-b3d7-bf7515847d3b | -11.51462 | -56.13053 | 2026-06-23 05:48:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd1006dd-30a7-3ac9-ae75-72e9ab7afd69 | -10.93253 | -56.84792 | 2026-06-23 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 743cc8c6-40a9-3c07-9e21-c26cfd89be60 | -11.30796 | -54.72365 | 2026-06-23 05:48:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7feebfea-a997-3cc5-9e30-f24ab0fe7a9c | -11.86799 | -57.83332 | 2026-06-23 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb11dc0c-3503-3293-b1c9-f72e9c469f66 | -11.30431 | -54.72293 | 2026-06-23 05:48:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 571e3d92-a7bc-3bf0-a8b7-17f2636cd8bf | -11.3106 | -54.72372 | 2026-06-23 05:48:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa5422ab-d79a-3c78-8af9-59fa7a1ffb06 | -12.28486 | -57.57546 | 2026-06-23 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e7d08b1-982a-316e-9888-b10ab98258d0 | -12.71947 | -63.04217 | 2026-06-23 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0cb1f79-13d5-33bf-8bba-e6f15be7cd27 | -11.80084 | -52.52441 | 2026-06-23 05:48:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e768776e-bc1b-34ce-aab1-c17acde99170 | -12.29058 | -57.57277 | 2026-06-23 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eaa9334e-1e74-3c2a-852e-89304c0aaca1 | -12.29099 | -57.56942 | 2026-06-23 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0934f89d-c8fa-3588-aeea-f0f98c141c04 | -11.87358 | -57.83081 | 2026-06-23 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fbb51a6-ae76-3b36-8aa2-b28ec0f3a71e | -12.54474 | -57.1921 | 2026-06-23 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7340eba2-49cb-34cb-9914-eff94c15500c | -12.54891 | -57.20347 | 2026-06-23 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81223873-a1c6-3d3a-9280-b668f573b3c6 | -13.50304 | -56.57576 | 2026-06-23 05:48:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b32b0d36-d84e-336e-ade3-87bc2e768251 | -12.29589 | -57.57338 | 2026-06-23 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e08c8c75-bd4d-377e-b87b-eca6de5cbba9 | -11.87276 | -57.83719 | 2026-06-23 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee21e2c6-4382-3d0a-afca-4128dc7b5710 | -12.29016 | -57.57613 | 2026-06-23 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23ce15ee-f73d-30e4-8c31-be340e55d4d0 | -11.80804 | -52.52527 | 2026-06-23 05:48:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a62c20e-93b7-3b53-a033-1fe8a6cccae7 | -12.54344 | -57.2029 | 2026-06-23 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 554d2744-0f48-39a1-bdc0-934feccb6174 | -12.28934 | -57.58279 | 2026-06-23 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f8d9fa6-f05e-361d-a925-819e53f7991c | -10.93209 | -56.85135 | 2026-06-23 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36feb2cb-89d5-319b-830b-aff04ea84113 | -11.87317 | -57.83401 | 2026-06-23 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ea63cfe-a51b-3234-b960-f2bdcdf9cdd8 | -11.30854 | -54.71857 | 2026-06-23 05:48:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cd313f5-2f91-339d-976b-a7ba446a87e6 | -11.81065 | -52.52658 | 2026-06-23 05:48:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2750ea69-abac-3176-b424-e0f0af3d78af | -11.87795 | -57.83784 | 2026-06-23 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a159bc7-61ad-3c2e-9c67-e286ca2d0076 | -11.80345 | -52.5257 | 2026-06-23 05:48:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 60d29407-fdc0-34f8-9eec-ed8f114b6442 | -12.28975 | -57.57949 | 2026-06-23 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88521c05-f4b2-3039-a211-7d06528b1d27 | -13.50353 | -56.57156 | 2026-06-23 05:48:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0cbdbddf-b60d-31d6-9848-73de6218a1ec | -12.8746 | -44.3357 | 2026-06-23 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.2 |
| ac935dcf-5141-3346-bc77-ea490e966e36 | -12.8741 | -44.3593 | 2026-06-23 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 9158fcd3-35cf-301e-9941-3d3d4f337bf8 | -12.8548 | -44.3625 | 2026-06-23 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| af914674-a99d-31df-b2da-ae2c366a4ceb | -12.8552 | -44.3389 | 2026-06-23 05:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| c95d8403-6cd5-3147-bdc6-e8aadd26d69e | -12.8741 | -44.3593 | 2026-06-23 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| db1156ff-e63a-39fb-ad2e-2ac903356342 | -12.8746 | -44.3357 | 2026-06-23 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 51808169-0787-3326-922a-293a690fa0e2 | -12.8552 | -44.3389 | 2026-06-23 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| bc507847-b4b9-3fb0-b001-23217672c662 | -12.8548 | -44.3625 | 2026-06-23 06:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 105.1 |
| bf098ed2-c792-3151-809b-e163c0f27b3c | -12.8548 | -44.3625 | 2026-06-23 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 118.8 |
| ac9eb34f-1d91-3f5f-8ea4-7a59b577acb1 | -12.8552 | -44.3389 | 2026-06-23 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| b2484c5a-8c75-3944-81ab-61c7e8dc53aa | -12.8741 | -44.3593 | 2026-06-23 06:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| f58961f8-2509-3b7d-906a-b64de149d69b | -12.8552 | -44.3389 | 2026-06-23 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 583e1fa9-b469-3be6-8894-d354302bb06c | -12.8548 | -44.3625 | 2026-06-23 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 13cc7d20-ee51-3f66-a654-651420e40fd3 | -12.8741 | -44.3593 | 2026-06-23 06:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 27c7f806-440f-3999-9de2-f841e24352fd | -12.8552 | -44.3389 | 2026-06-23 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| e984f77c-9987-3e44-88c7-a72f72bf4ded | -12.8548 | -44.3625 | 2026-06-23 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 7bb5439b-c820-350f-8b7a-d72a51603a58 | -12.8741 | -44.3593 | 2026-06-23 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 8d53eb3d-e97e-3e15-979e-ffbf62cf73dc | -12.8746 | -44.3357 | 2026-06-23 06:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 649243bf-b793-35fd-bad1-07df75f57341 | -12.8548 | -44.3625 | 2026-06-23 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 128.6 |
| a4ee8681-8207-373d-a97c-2aa6b84a90b6 | -12.8741 | -44.3593 | 2026-06-23 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 134e3f26-64f2-3d10-8d10-47b3971a35f6 | -12.8552 | -44.3389 | 2026-06-23 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 24307f73-2ad2-398c-9c30-c94dccb3092d | -12.8741 | -44.3593 | 2026-06-23 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 22288df9-b6ee-32e1-bd8f-69b62889570d | -12.8552 | -44.3389 | 2026-06-23 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| b92ff49a-a047-32e8-8b50-801b4e6a2dad | -12.8548 | -44.3625 | 2026-06-23 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 4f9aae14-324c-3268-b426-2c7f842ad01e | -12.8552 | -44.3389 | 2026-06-23 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 9d6d6551-2815-302c-8cf8-8b4b793dd190 | -12.8741 | -44.3593 | 2026-06-23 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 28b9f666-4869-3f6d-af56-0fd6aeaeb854 | -12.8548 | -44.3625 | 2026-06-23 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 412707f9-015a-320c-9e50-0743f1231977 | -12.8741 | -44.3593 | 2026-06-23 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.4 |
| f2b29a7a-11b5-32a5-82dd-575516583723 | -12.8548 | -44.3625 | 2026-06-23 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 0e93f792-8310-3291-aa48-cae2d781b276 | -12.8552 | -44.3389 | 2026-06-23 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| b69e97bb-63ae-396f-91c2-6368905fd079 | -12.8741 | -44.3593 | 2026-06-23 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| e06e2895-e410-398e-83f4-0c2d3cd15a05 | -12.8548 | -44.3625 | 2026-06-23 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| f1d45e5a-0616-372d-a3c6-f7c9976ce5e3 | -12.8552 | -44.3389 | 2026-06-23 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 7ec84671-2ba9-3d0c-944f-3f2bc471ae8c | -12.8746 | -44.3357 | 2026-06-23 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 877985b5-57a7-319b-9f65-35c6b5a27c57 | -10.27493 | -60.54559 | 2026-06-23 07:20:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 541623e0-45d4-3e30-b57f-2aebe2d14d96 | -12.43666 | -58.40195 | 2026-06-23 07:22:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c0dbea81-2810-3b0f-97ce-5c8959dcdc62 | -12.42761 | -58.40063 | 2026-06-23 07:22:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9bf44f5d-19e8-30d6-9306-f98a85712e24 | -12.42623 | -58.41012 | 2026-06-23 07:22:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| aa5e944a-577a-3f5c-b9d9-cb34b2efe06b | -12.8548 | -44.3625 | 2026-06-23 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 681a9b75-6f6d-3ac7-b13f-9a1e71fc0764 | -12.8741 | -44.3593 | 2026-06-23 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 6fac699f-2f7e-3a1d-b5ea-123bafd9c2ba | -12.8552 | -44.3389 | 2026-06-23 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 9d607a37-7f9a-3b3a-bf62-b19fe0a815cc | -12.8741 | -44.3593 | 2026-06-23 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| c375c1e8-c83e-3258-aad3-28967e7285c7 | -12.8548 | -44.3625 | 2026-06-23 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 5a70de3b-be50-3507-bef8-1d565d65a28c | -12.8552 | -44.3389 | 2026-06-23 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 1c9881a5-84b3-31f3-afdb-d1a4fe2c4ea6 | -12.8741 | -44.3593 | 2026-06-23 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 977ba0dc-705e-3aaf-8822-dab8108f99dc | -12.8548 | -44.3625 | 2026-06-23 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 836bddc4-7896-383c-8b9a-ecf69a7f029f | -12.8552 | -44.3389 | 2026-06-23 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 3c9f44af-c2ed-3a47-88ac-f6b92682613f | -12.8741 | -44.3593 | 2026-06-23 08:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.8 |


[Clique aqui para ver as próximas entradas](README18.md)
