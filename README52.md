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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5053e31-ad9c-3539-a7fb-ee7047f415da | -3.14939 | -48.53424 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7263b3c-e396-3a64-b0eb-a94fe417f4de | -3.58411 | -50.60164 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 58a6841e-c64a-39c9-bfc9-58a532d3fb6c | -1.23887 | -51.61125 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54a8143b-4a7f-3b6b-b41a-2745500e657e | -1.63357 | -52.49562 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e22b5486-0fc6-3ae0-aacb-72aa09aa4dbc | -2.9989 | -45.4627 | 2024-11-27 04:42:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f0472b5d-1ed8-3d21-a43e-2e4db40458c5 | -4.24186 | -48.67286 | 2024-11-27 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a27bc951-69f7-38e2-8920-d88d5087ab95 | -2.22672 | -47.84317 | 2024-11-27 04:42:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d85067f-e75f-3880-aa71-5d44570f686a | -3.24507 | -50.14342 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c4a0052-b1fd-3e75-8358-371645a1999a | -2.5792 | -48.07556 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cafcc4a2-1ba6-3e2b-a4ce-4f93a621afb4 | -1.66594 | -52.72401 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0abea1a9-82f1-34f3-a49e-521498ca23b3 | -4.04505 | -48.31273 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44390412-f072-3625-877d-872fe9576d50 | -1.4546 | -53.4235 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13e8d30c-0e13-31c6-b6ac-16dc8d09976f | -1.29117 | -51.37001 | 2024-11-27 04:42:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee06cfd4-00b9-3eb4-93ed-5c74322aa068 | -1.93908 | -50.64725 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d2de7654-a7a9-331f-8554-a38b8b09bea4 | -3.28426 | -51.12225 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d50f2eb6-4a77-3a15-a790-8f160ebdbc2d | -3.10713 | -53.24776 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8923af9e-eec3-3f15-b4f0-52a22b1478fb | 0.90106 | -50.23671 | 2024-11-27 04:42:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0877e27c-b3df-3987-9e99-00c6b4b5649a | -3.12885 | -50.25513 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68cccd12-5c7b-3ebf-bde0-9e20956c5ca0 | -3.2854 | -41.77354 | 2024-11-27 04:42:00 | NOAA-20 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 04874cf5-18c8-3e4e-9afd-d448091f229e | -2.2735 | -51.23756 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aee2a671-c27d-3b5c-81ba-9b6460ee1578 | -4.32541 | -45.88953 | 2024-11-27 04:42:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee66dbf9-a80f-3c0e-b517-af1ae6708a02 | -3.083 | -53.26072 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70be2fad-e07c-31f3-b6ca-cc87dfbafb01 | -4.27274 | -42.44287 | 2024-11-27 04:42:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4551ca34-1f87-38fc-a3ca-8f92ba2374a7 | -1.87908 | -47.98227 | 2024-11-27 04:42:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6e48be8-b71e-37e5-bc45-7877269176a2 | -3.24228 | -53.41465 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2585fa6-6b31-3389-bdd3-a80cb622709e | -2.18072 | -53.2598 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a87bb0a-2c61-3622-a1df-c55211225c5e | -1.63709 | -52.49617 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 454bbf0e-58fb-3603-ad9b-dca8fd5d2bae | -1.46567 | -52.47937 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9608a70d-402c-3e33-afa6-44094e7cb48a | -0.99283 | -51.72515 | 2024-11-27 04:42:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5b42aa7-f5c9-3810-8c07-501c554b779f | -2.43721 | -53.97484 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02cc09bb-6043-3acd-835c-100e8d6194fc | -4.04916 | -46.85445 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e8706ee-cde0-3e5b-b085-0d70822d466d | -3.96855 | -48.08054 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 609999a1-9c0f-3662-b32f-877bf7e849de | -5.75624 | -46.26443 | 2024-11-27 04:42:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9bfd2fe5-6d8b-3ed7-88ea-f33faa6abaa5 | -3.27325 | -50.17949 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3dd4b1db-d5ba-3cf1-9e75-3946e574d5fd | -3.431 | -49.9963 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9751b2ea-c7cf-3322-bdc0-530b33b10175 | -2.36389 | -50.43134 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3756cb13-9a31-3cb7-b839-30dd94ee43b7 | -0.55054 | -49.51783 | 2024-11-27 04:42:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea0a608b-1d55-3074-9a54-f77d896c7cca | -2.6173 | -48.16884 | 2024-11-27 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50876da8-0f1c-392d-a4f8-d98d4bb16157 | -3.28218 | -53.83799 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b90c157-46d2-3a05-887c-90affed03783 | -4.18153 | -53.52962 | 2024-11-27 04:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bd2b77a-6ef0-34b4-8417-1ce27e807cb8 | -0.16002 | -51.46978 | 2024-11-27 04:42:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bb1526f-65b7-396f-bdf8-e587a29c0dd6 | -4.18172 | -49.41251 | 2024-11-27 04:42:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8b8e23d-969d-3af1-8fde-4fed81eb3b2f | -1.73161 | -52.03949 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36c3180f-344e-3083-bed4-b167d48b51cf | -3.22944 | -45.92698 | 2024-11-27 04:42:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 301fea37-0b78-3f11-9429-d5b13f77ee9d | -3.91041 | -50.60025 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c733a30b-842b-31e4-8a1e-f1637205119c | -2.86306 | -46.81483 | 2024-11-27 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b466963f-b171-34a2-8c72-cdfc8ca3c909 | -2.6958 | -48.65778 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8db86df6-8a0d-3798-94fe-9574fbe7c4fa | -3.07546 | -53.2848 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9d3c1df6-5cca-31a9-a3fa-b292b27d62d2 | -0.98941 | -51.72461 | 2024-11-27 04:42:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 937476f6-a39d-3bca-a803-bef8599f83a8 | -3.05762 | -51.33082 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa33bd40-9308-35eb-872b-70fd560383a6 | -2.93692 | -54.79397 | 2024-11-27 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c667c4a5-7429-3547-abbc-aed6c278545e | -3.51076 | -50.31209 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 79938aa3-e4c8-36ff-a69d-f3d1d3b6c69b | -3.17316 | -48.62708 | 2024-11-27 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bc3e903-ff32-3943-80f4-2af2839f9992 | -3.89709 | -50.08007 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a23e77b0-f4ea-3320-a64d-1ced257bc592 | -3.90015 | -47.74538 | 2024-11-27 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1d84ac2-9045-3608-81b5-0efdc7b3bc8b | -2.83311 | -54.11736 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 10e0e125-ee61-3668-8e5f-478f509c82b7 | -1.3604 | -54.63278 | 2024-11-27 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb4bf339-7ed3-335d-b1fb-4e8f0b7b4027 | -3.51958 | -53.78408 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1cc7280e-9ff7-304f-8e0e-3f8bb59b3107 | -2.59782 | -53.96732 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9c233d2b-646c-3f10-a154-a6b4d14268ca | -2.94477 | -54.79526 | 2024-11-27 04:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1346910a-a517-3bea-a829-90f790b9dd79 | -3.26358 | -46.442 | 2024-11-27 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd4d0183-8bf7-384e-afb6-594dec5eea73 | -2.7692 | -51.64722 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19bf7936-fcda-3bff-a07c-f6d474f10042 | -3.27842 | -50.55717 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b42279d-fce7-3008-9329-d4a7ef250035 | -5.65007 | -46.64946 | 2024-11-27 04:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ea50168-2749-3b10-a838-9ebfa2bc3bc4 | -1.59158 | -52.2364 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1c43a65-741e-3dca-a006-49640a067acb | -2.83615 | -54.12254 | 2024-11-27 04:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 8f802b54-a116-313a-915a-60ada9c2025c | -3.70609 | -51.80004 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43c7f255-2442-3610-956b-65952ac0097e | -3.96567 | -48.07613 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a323d277-50b1-3bba-b820-c8d1f198f7ab | -3.3117 | -50.23838 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df78abc3-e682-3574-88a1-f9b335f32a2a | -1.45337 | -52.71766 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e623c2f5-0604-3a57-80e9-fa7c849d672e | -4.96136 | -47.5932 | 2024-11-27 04:42:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f1eed45-4958-3e64-967c-bef4800325ce | 0.9422 | -50.73996 | 2024-11-27 04:42:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 082aa7c6-f217-3dfd-bfa8-0bd549d2da44 | -4.05384 | -46.68594 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86321852-f6ad-31da-8b23-4d38da127f57 | -2.97545 | -51.57587 | 2024-11-27 04:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d4d8b593-99aa-3e36-9ff0-e38b7632a9c6 | -1.64411 | -52.49728 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8c3c445f-c15a-350f-a494-96934ef144be | -3.9391 | -47.98256 | 2024-11-27 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ccb1ef30-1d38-3000-b29c-f9a66b6f1a68 | -3.44878 | -50.29531 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 36ac9d38-78b4-34c3-942a-301c09fa49a7 | -1.10757 | -53.39082 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04b840fa-226a-32f9-9f42-058ae17b5fef | -1.63997 | -52.50064 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d712dea-3523-3189-ae95-5ef3877e405b | -3.49519 | -50.454 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b47c0dc-8741-3b7e-88b9-8245d1e11bdb | -2.9241 | -51.77046 | 2024-11-27 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41b90b82-bc02-3056-b42f-12962a07f652 | -3.28119 | -50.56113 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82e2af1c-1897-323f-b364-61d511249f2a | -3.11724 | -53.25353 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62e3c4ca-e602-3c84-a250-3e6375213da3 | -2.61966 | -52.53705 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 733ed9fe-ac1a-3989-b54c-6e3731591810 | -3.90933 | -50.60712 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3366df1d-ec8a-3637-a403-39101432e7bf | -3.70838 | -50.43789 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fd2cacb8-eef0-3185-94a1-8b47d71288a7 | -3.94998 | -46.69284 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8415247-95dc-3768-99d2-8abfc64a7c76 | -3.39243 | -44.17384 | 2024-11-27 04:42:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9950c2f-1b4c-3a12-aea2-486fbc372bf4 | -6.07434 | -44.70153 | 2024-11-27 04:42:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3aeb3c87-2a64-380b-a80a-396f519c421c | -3.9951 | -50.55709 | 2024-11-27 04:42:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e916a26-7193-3f61-8345-ec2e1f3f7c77 | -3.21289 | -49.45912 | 2024-11-27 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e45f0c8d-9043-387e-a6a3-5bbe71a2d64f | -3.10453 | -53.26411 | 2024-11-27 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d7c93a26-cd27-34de-968c-83153bc1e77d | -3.28715 | -50.75984 | 2024-11-27 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61727aec-e1f8-323c-b81e-4fd17156b204 | -3.80862 | -46.59766 | 2024-11-27 04:42:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e556e69-8d47-32f1-b2a7-fb70c2f2954b | -1.76602 | -53.63369 | 2024-11-27 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40ed0633-c1bb-3744-b662-4931f907ccac | -3.5146 | -50.30917 | 2024-11-27 04:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f15ba7d0-334d-3081-a866-26e3833c75ad | -1.44233 | -52.58074 | 2024-11-27 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 501f90c5-609f-3067-9f5d-89c4d93bde24 | -3.50214 | -53.79871 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6735c2b8-84a9-373a-a217-809db2b59185 | -2.05306 | -53.23449 | 2024-11-27 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4508c574-266e-3b46-9de6-04abd5b77ebc | -3.51889 | -53.78833 | 2024-11-27 04:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README53.md)
