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
| 1b4a8603-ec20-3579-a00a-952c7dda381e | -9.7474 | -49.0465 | 2026-07-15 00:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 8205829c-469e-38af-a1f5-ce584275e14a | -12.3753 | -47.4103 | 2026-07-15 00:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| c40ca8dc-d35e-3752-bc45-732727c4010f | -12.3561 | -47.413 | 2026-07-15 00:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 2fd99382-f573-3443-96cf-abffc1a6426e | -9.7474 | -49.0465 | 2026-07-15 00:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 36615c4e-866e-3a17-8acc-a4337b67c7ac | -12.3561 | -47.413 | 2026-07-15 00:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 13c35813-6953-36c1-8a39-db78e74c4bdf | -5.8265 | -43.5872 | 2026-07-15 00:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| c7d8480a-b289-3c15-a889-f8ec243d5306 | -14.1943 | -58.8128 | 2026-07-15 00:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 27.0 |
| af8e71e2-e25a-378b-ad38-f2f3530c81ac | -9.7474 | -49.0465 | 2026-07-15 00:50:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| b3167eb3-4b99-361a-a1e3-70fa9c923f2e | -12.3561 | -47.413 | 2026-07-15 00:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| ad891d13-dddb-3518-92c6-38991fefd764 | -9.7474 | -49.0465 | 2026-07-15 01:00:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 15d9ac21-5c7c-371c-a111-1f0e1f7ae19a | -12.3561 | -47.413 | 2026-07-15 01:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 7f31118f-4fd3-3a98-a2d6-4b3e1a47b9dd | -9.6442 | -40.6095 | 2026-07-15 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 73.4 |
| cdc03df4-b0c3-3ec1-ac6f-995adf8898d9 | -9.6446 | -40.5847 | 2026-07-15 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 81.0 |
| 64b5c8a2-498a-3bdd-929d-e1b031858dc4 | -9.7474 | -49.0465 | 2026-07-15 01:10:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 055079ee-936c-37d1-ac81-67726fe451a1 | -9.6442 | -40.6095 | 2026-07-15 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 55.1 |
| 9aac4c8b-2784-3757-a8d6-da70e9ab9efc | -5.0166 | -37.557 | 2026-07-15 01:20:00 | GOES-19 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 57.3 |
| 255689e1-74d8-3628-be49-c8091af35ca4 | -9.7474 | -49.0465 | 2026-07-15 01:20:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 2ef5b42f-46dc-3193-9f2e-fc5bbda6cd17 | -14.1771 | -58.801899 | 2026-07-15 01:22:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ee2c9225-1cdb-30c3-aee6-06396d7383bd | -9.7474 | -49.0465 | 2026-07-15 01:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 52e951be-5dd1-31e6-b39f-4ce422ab66f1 | -5.0166 | -37.557 | 2026-07-15 01:40:00 | GOES-19 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 40.8 |
| fd67c836-15dc-3f73-8370-eafae6ad4bcc | -14.1577 | -58.820499 | 2026-07-15 01:48:00 | METOP-C | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 820f7724-bdcc-308b-8f04-4eeaaafc4cad | -14.1674 | -58.818001 | 2026-07-15 01:48:00 | METOP-C | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0f263187-30b0-3102-95c5-1f0b2508b4f1 | -10.7392 | -43.6089 | 2026-07-15 01:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 809e0a68-39b9-3b7b-b1b1-96adf61f9b1d | -10.7392 | -43.6089 | 2026-07-15 02:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 883aad0c-dbb4-380c-81c7-f795e4eb3a54 | -8.7452 | -49.4658 | 2026-07-15 02:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 084ed94a-b2fc-3d72-afa4-5d4627541057 | -21.4789 | -47.3446 | 2026-07-15 02:00:00 | GOES-19 | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 3b597574-ddfe-328b-ab30-c00c965ade9d | -9.7474 | -49.0465 | 2026-07-15 02:00:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| f8dd8560-b91e-3196-bd15-d8887d396e1f | -10.7392 | -43.6089 | 2026-07-15 02:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 360c494d-d05c-3b4c-8069-bb6c3dc829d5 | -10.7583 | -43.6062 | 2026-07-15 02:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 9b1cf732-b83b-3b05-96a4-1c64fc1ae49e | -8.7452 | -49.4658 | 2026-07-15 02:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 30be29f5-c68e-3971-af23-57d4e391ccf6 | -10.7392 | -43.6089 | 2026-07-15 02:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 3ef721eb-b227-3c38-b7af-f9210eb1a16f | -10.7392 | -43.6089 | 2026-07-15 02:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| e4420b8f-9fc8-3973-bc42-c126c06dde9e | -9.625 | -40.6122 | 2026-07-15 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 69.6 |
| 594f910c-278c-3be0-ad52-237c11cda5c9 | -9.6254 | -40.5875 | 2026-07-15 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 72.8 |
| 1f2d82bf-1359-3188-a11f-fb0a6b935ecf | -10.7392 | -43.6089 | 2026-07-15 02:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 96bef9ab-d45b-3c86-9925-5fb86648ce91 | -5.82961 | -43.5966 | 2026-07-15 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b5aa1570-205d-38d0-a85e-b3c2e200cb3f | -6.47812 | -42.22609 | 2026-07-15 03:51:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| bd8d69e6-3e24-3ee3-9a31-0009cf05677c | -5.82588 | -43.59107 | 2026-07-15 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4f6d7a51-0810-3234-a48c-276334ca57e1 | -6.50169 | -42.21106 | 2026-07-15 03:51:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| aaac331f-4335-3d93-a551-93e5aada27b6 | -5.34238 | -45.18184 | 2026-07-15 03:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 79c67177-a35d-3e7d-9173-86109aa018d9 | -5.83041 | -43.59188 | 2026-07-15 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9d15ec08-d493-3188-bc77-af149d339c0a | -2.95316 | -39.92759 | 2026-07-15 03:51:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 4b701bfa-e535-3125-b28b-b8510717b645 | -5.34696 | -45.18575 | 2026-07-15 03:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 335e28a9-7b57-3f11-978f-ba7d7e3ffe9d | -6.48282 | -42.22315 | 2026-07-15 03:51:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 46b52603-fcd6-38d5-9930-e53e8347cd00 | -6.4822 | -42.22682 | 2026-07-15 03:51:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 143940ed-550b-385e-a63e-53f55c1e56f8 | -3.15366 | -48.58551 | 2026-07-15 03:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfe7b622-412f-302e-b0fb-8df13a62d5e5 | -5.08945 | -37.33601 | 2026-07-15 03:51:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2b8c927d-8286-3e6a-89cd-829c33df178a | -3.15463 | -48.57982 | 2026-07-15 03:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0aed9a4a-12cd-30aa-bf28-c7a41b600a39 | -2.96883 | -39.92553 | 2026-07-15 03:51:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 580b3cac-a19a-32e5-bb65-e6b8b01b63dd | -5.48406 | -37.31314 | 2026-07-15 03:51:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0e92611d-45f6-3b42-8c75-123a429236be | -5.82507 | -43.59582 | 2026-07-15 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cbd81fa4-0a3a-3127-b672-5c1838c83fcc | -5.33476 | -45.34964 | 2026-07-15 03:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bbadde5a-e4a4-3d35-8d96-54df5d4c8835 | -5.348 | -45.17975 | 2026-07-15 03:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3b46c22-dc46-337a-8936-7f41a69f2347 | -5.33992 | -45.35059 | 2026-07-15 03:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 650ff332-0669-3633-89e6-4c367307faf0 | -6.47872 | -42.2225 | 2026-07-15 03:51:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 182300ab-1f93-305c-926d-c8fb2515edbb | -5.01543 | -37.54645 | 2026-07-15 03:51:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 44f4ae78-6deb-3361-a001-23c879b0126d | -5.30705 | -43.05791 | 2026-07-15 03:51:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62c9c17a-7a48-3e68-88d8-5fb3842e56b2 | -5.34748 | -45.18275 | 2026-07-15 03:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9df3f30f-d166-3e0a-9f26-1db010b63055 | -5.51303 | -45.97106 | 2026-07-15 03:51:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c150ae6-4be5-3457-806f-0042eb34d886 | -5.01599 | -37.54294 | 2026-07-15 03:51:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 10.1 |
| e97f9fd2-06cf-36a4-ae1f-b52b15495841 | -5.35257 | -45.18368 | 2026-07-15 03:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8359170-4f60-3ef5-834b-0674ad24f8d0 | -5.48075 | -37.31261 | 2026-07-15 03:51:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 926f6bba-f8a8-34be-b1de-fc179760f8e6 | -6.49164 | -42.22079 | 2026-07-15 03:51:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4c23ba39-c713-3589-8304-7cab2d851e8d | -5.83494 | -43.59271 | 2026-07-15 03:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d43bac91-a474-332b-9976-74d59f397226 | -6.49101 | -42.22456 | 2026-07-15 03:51:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 34abaff1-2912-3b0d-a816-dc5daa12dce9 | -10.73898 | -43.61396 | 2026-07-15 03:53:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 348275c4-0d7c-3712-a614-2c38327cdad6 | -10.71621 | -45.15188 | 2026-07-15 03:53:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 977eefd9-a581-35b0-8595-254c9f6103de | -9.7385 | -49.04174 | 2026-07-15 03:53:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 54f45c7b-26f1-3166-9580-6780f37df9bd | -8.94709 | -47.60983 | 2026-07-15 03:53:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62c2a85d-7214-348f-9e95-1ceb7e577735 | -9.76262 | -37.7612 | 2026-07-15 03:53:00 | NOAA-20 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 469fbf3d-31f1-36df-937a-c7d9d4367108 | -9.74415 | -49.04333 | 2026-07-15 03:53:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b1f17902-3658-38dd-b17f-15288cd24aad | -9.73758 | -49.04635 | 2026-07-15 03:53:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a75f507f-0223-37b5-80b4-537f1a81f679 | -9.74367 | -49.04748 | 2026-07-15 03:53:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 8db47a21-68ae-345b-8772-eb7cd41b1201 | -9.88008 | -49.98252 | 2026-07-15 03:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2301b798-456f-3c76-8f57-306983c6c8bb | -8.50255 | -48.07426 | 2026-07-15 03:53:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 741315a3-0e67-3dbc-9b9d-d2efb2f9681a | -11.40377 | -47.54042 | 2026-07-15 03:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20514a52-e1d2-352e-9bd9-fe9c9f3b13b5 | -9.74327 | -49.04795 | 2026-07-15 03:53:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0204c0dd-68ef-3a73-9c01-e096371fd53f | -11.09713 | -47.80455 | 2026-07-15 03:53:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2fa467f4-1cec-3216-a724-ea0531b2696e | -11.86763 | -43.79704 | 2026-07-15 03:53:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aad608cd-2861-33b3-8392-06c641a5603a | -8.94404 | -47.61002 | 2026-07-15 03:53:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7321b1e3-2370-3121-a745-05cf50045e62 | -8.74207 | -49.4483 | 2026-07-15 03:53:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad0b7c0f-d581-33df-a476-d74b29363516 | -11.40846 | -47.54504 | 2026-07-15 03:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8b4ce7e-a2b7-3c28-86a6-490a690cbf6f | -9.87866 | -49.98501 | 2026-07-15 03:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8b3ac613-545a-330c-a75e-2f8672da9e2d | -9.73718 | -49.0468 | 2026-07-15 03:53:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1f03b29d-3f7a-3d79-baff-1634bcd473c3 | -8.94638 | -47.61373 | 2026-07-15 03:53:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c5f7d26b-f2ce-38ea-b28b-379432790e7f | -12.3805 | -43.8985 | 2026-07-15 03:53:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e3eeabc-d5c4-3374-b3f5-4481900d0487 | -11.87178 | -43.79781 | 2026-07-15 03:53:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 202f8546-b0a6-3a50-905a-20986d979ea8 | -8.9433 | -47.6139 | 2026-07-15 03:53:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95899caa-56dd-30f8-b264-5b7474de9807 | -8.50334 | -48.07001 | 2026-07-15 03:53:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4782e114-66c5-3565-8285-a162db24240a | -9.73807 | -49.04216 | 2026-07-15 03:53:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 66f5a794-e0d6-36c3-bfb5-8f356ace550c | -11.40305 | -47.54418 | 2026-07-15 03:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08bcf2c0-243b-3c5e-8cc6-c57a5464c478 | -8.73573 | -49.44712 | 2026-07-15 03:53:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| adc49098-81c4-3135-b3f7-e947076f53ea | -10.74315 | -43.61481 | 2026-07-15 03:53:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| bc39d565-2ca8-3369-8bb8-733d6e876aa9 | -7.86287 | -36.06137 | 2026-07-15 03:53:00 | NOAA-20 | TAQUARITINGA DO NORTE | PERNAMBUCO | Brasil | 2615003 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b9ca04f4-6c15-35ba-8b8b-857d4437ebaa | -9.74458 | -49.04288 | 2026-07-15 03:53:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 317d1610-9e46-3fcb-a40c-967d07e028a1 | -9.87971 | -49.97962 | 2026-07-15 03:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| af3f770c-4da6-3020-8cfe-251a3559e4f9 | -11.86694 | -43.80089 | 2026-07-15 03:53:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 887f3255-5779-3cb4-94f4-4b8b334604d5 | -14.30462 | -47.16706 | 2026-07-15 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54d97948-b4ea-3190-b17a-316d04b320e9 | -18.71044 | -39.86691 | 2026-07-15 03:55:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bb4e3ec0-359d-39e5-9f40-f83b1f00c2a6 | -13.439 | -43.85367 | 2026-07-15 03:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |


[Clique aqui para ver as próximas entradas](README3.md)
