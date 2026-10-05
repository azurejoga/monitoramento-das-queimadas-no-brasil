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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2913274f-23f8-3dec-bb08-3dd0faafb5c7 | -3.01985 | -57.91764 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b3797b6b-1465-321b-bc1b-64bae960007c | -2.88895 | -56.75072 | 2026-10-05 17:34:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 64d0acfe-019a-3e81-89cc-72542b591239 | -3.71594 | -54.2321 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 870d3f66-4f45-3df2-b839-095a661c86cf | -3.57442 | -55.41573 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8704ff2d-6a23-3ab1-b005-190be3937725 | -3.55786 | -59.08941 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9c493973-32f3-3a61-85a7-27df1e295a0c | -3.70834 | -58.93014 | 2026-10-05 17:34:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| f4ef73b3-68f6-3cd8-882b-a685c098e4ad | -3.27928 | -54.17474 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 9d416a15-84db-3791-bac2-f94023169c45 | -3.47201 | -59.5029 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13b5a932-2593-3a56-a2b1-d1d8b5b3b600 | -2.95913 | -54.10878 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ee22df5a-07bc-3409-8de9-5f40d8908e5e | -3.37977 | -58.20229 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 0f10d268-486d-31e7-bb95-56d1968a3c0b | -8.05913 | -72.39235 | 2026-10-05 17:34:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 50.3 |
| ed59ed5f-3cf3-388d-9fe7-bfad8d8e624e | -3.89933 | -58.74036 | 2026-10-05 17:34:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 110.4 |
| a19c2e73-a221-35e4-b8bc-828a45656186 | -3.82615 | -55.61241 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bb97d905-9962-3344-8481-8df8fe971243 | -3.23906 | -53.86722 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0447bb1e-319a-3ec9-be6a-394a7386badf | -4.341 | -63.45881 | 2026-10-05 17:34:00 | NOAA-20 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 30df693c-a925-33ac-9f5a-2388fdac37d5 | -6.91448 | -59.26021 | 2026-10-05 17:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e91c382a-1de3-30ea-8d2f-8801342c9def | -2.9853 | -57.89677 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 49094be7-dc4e-3e4b-b055-4a6e2c4a28d0 | -3.12575 | -56.97615 | 2026-10-05 17:34:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d2ffba36-d6c3-35ff-9210-74438035f3d3 | -3.6509 | -54.0573 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 47d95592-7b9f-3067-b8f1-8e373e793237 | -6.38687 | -60.04353 | 2026-10-05 17:34:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5f609636-9d75-3118-a47e-47ebf41c5079 | -7.78864 | -70.01653 | 2026-10-05 17:34:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 870b2470-6bd1-3472-8de3-d795325bff13 | -3.518 | -54.62986 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 073225e5-e289-3e1a-b0a6-6c5cea760413 | -5.25001 | -60.17849 | 2026-10-05 17:34:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 809e0666-513d-3bc3-ae76-fc8dc818cfff | -3.75226 | -61.01601 | 2026-10-05 17:34:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 8e70eec4-de13-3cd8-8964-dcc190c7318a | -2.99575 | -54.10321 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 134d44dd-042b-367c-802d-da5bea00e34a | -7.63342 | -72.31569 | 2026-10-05 17:34:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 900be940-b005-3f1c-a385-ef6bb382c771 | -3.0658 | -54.15602 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 0411f463-f7a2-3b29-964b-8512f75f7ebb | -3.22604 | -54.3042 | 2026-10-05 17:34:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 71f60ef9-96fc-35c7-b3ca-2490371d091a | -7.37563 | -73.15708 | 2026-10-05 17:34:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 12cf9b72-1f75-3677-a810-4cb8c3721686 | -4.12457 | -63.41328 | 2026-10-05 17:34:00 | NOAA-20 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 88afff57-089d-3f08-8cf4-63a258f29e60 | -3.06963 | -54.17917 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 79103c6c-261c-3669-867f-6ab20d403654 | -10.19603 | -52.55948 | 2026-10-05 17:34:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3e1d1bd8-05df-310f-887c-2057e114d1b7 | -4.13167 | -54.15672 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 46669c87-9cc8-3e70-9da5-1ccc06c7cbc5 | -3.59676 | -61.7135 | 2026-10-05 17:34:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b343065d-2715-34a6-969e-d5887f9cd17d | -11.39863 | -50.84625 | 2026-10-05 17:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 1611db91-b251-3daa-87f2-5e53c24806fc | -3.69113 | -59.1357 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| af8b05fe-f791-38aa-bbac-b2379459cbe1 | -3.30056 | -59.3975 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f133b0f7-8bd7-3639-a9dd-7941c5719e59 | -4.05435 | -54.04956 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| c9b68cca-7fac-3bdb-aba5-4b146db055b9 | -3.84562 | -59.61139 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2c2cb5b0-9c3d-351d-a9af-923ab8dbb94e | -6.78967 | -66.66972 | 2026-10-05 17:34:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 2a6f3576-9886-3cd1-982c-2fc484466d60 | -3.85241 | -55.80568 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9e4c991f-4bdf-39b5-a0b3-907fd0b7ceaa | -2.99327 | -56.59884 | 2026-10-05 17:34:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 97f94c40-6d34-3eef-bd5b-9120625700cc | -3.70822 | -59.04325 | 2026-10-05 17:34:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c613e900-93ca-3277-8603-adee0f84ef0d | -12.87961 | -62.15097 | 2026-10-05 17:34:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 17.1 |
| e889f38d-1423-3907-b981-94c4cd89108c | -4.05812 | -54.04428 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| ea5fc2c6-e657-383d-873b-f4c58289c204 | -3.47699 | -55.43108 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 63fa54de-ee85-3f38-84e3-ffd8cd5df3c4 | -3.75235 | -59.30815 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4bcab2cf-0939-386e-81a0-1dd8d3ebc108 | -11.20449 | -47.13328 | 2026-10-05 17:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| ded9cf29-b86c-30a5-9f11-bdc8de246829 | -3.50834 | -59.55946 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 6c688df1-34ae-3f19-99fb-10253f53e36a | -3.68326 | -58.90362 | 2026-10-05 17:34:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 8993dcd3-3e6d-32a0-a9b0-b73371e39ac8 | -3.07331 | -58.42132 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ccb4515b-87db-3e75-8068-724e96b70111 | -13.50585 | -61.13539 | 2026-10-05 17:34:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 28.6 |
| c4957146-5e5b-3282-9af0-f95f5fdd3fde | -3.25035 | -57.90873 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| deaf5651-8a68-3de2-888d-553dd11e0eda | -3.51594 | -54.61713 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d82e5556-ac56-37c8-8822-5870bbe05af7 | -7.89725 | -73.17185 | 2026-10-05 17:34:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 26a33370-cd4b-34da-baeb-5c1239cadd2e | -3.5845 | -58.35567 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9f3d8fbb-e93a-317b-a5b6-5c5aa337a014 | -3.59343 | -61.714 | 2026-10-05 17:34:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6901d7ec-d141-34cb-9162-cef4bef4269e | -10.51288 | -46.04754 | 2026-10-05 17:34:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| b53c215e-8777-3fca-9209-720f90dc99c3 | -2.96013 | -54.14543 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 38833e06-a801-3221-b5a3-8b5522cb40e8 | -6.59909 | -61.85294 | 2026-10-05 17:34:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2535fc47-17b0-3510-af8b-0b0c0b2284a6 | -5.81838 | -53.83826 | 2026-10-05 17:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 5433042f-d419-3480-aec0-a0f0eb0d59bd | -5.81562 | -53.84167 | 2026-10-05 17:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| ac58a182-3842-38ca-8249-eb765ec0a024 | -4.42627 | -63.16074 | 2026-10-05 17:34:00 | NOAA-20 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| fc84eb89-b80e-35a3-b3bb-d89c02fdf03d | -3.09236 | -54.17567 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 5e142413-d5a7-3192-a7f9-9fdd49a7877e | -3.67063 | -54.54193 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| ae9dfdf8-380d-3be3-af4a-0685c86c5673 | -2.90015 | -54.12173 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bedeede5-3cbd-3309-9eb6-53863687ba8a | -8.82328 | -49.30831 | 2026-10-05 17:34:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9d0b7916-e299-3e3e-b77f-41c83c62d850 | -3.59027 | -55.29171 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ea9b6f09-5fa3-396f-b1c5-4ffc703630fe | -3.53174 | -59.3984 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 2557a449-121e-3bf2-aff0-2663a8e13320 | -14.3242 | -59.57571 | 2026-10-05 17:34:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 634bb2a7-ab86-313d-8cab-0a9fd68e047f | -2.9594 | -54.14081 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0232f482-b0ab-375f-9cd1-5435c6d79329 | -3.65264 | -59.15649 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8a880a6d-300c-3762-8818-b623c9dd5625 | -2.99313 | -57.8998 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| fe28d775-5ca0-3202-aca4-6d943ae6bebf | -8.34353 | -70.10622 | 2026-10-05 17:34:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 0d20880b-c814-30b1-9d92-ee8988bc6fab | -3.37502 | -58.19503 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 100.0 |
| e39ecbad-4fcb-3f19-9d36-0a07280ab43b | -9.58686 | -59.26648 | 2026-10-05 17:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c2a15e24-1853-3805-a0ff-af7452a98840 | -3.89589 | -58.74089 | 2026-10-05 17:34:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 110.4 |
| beb6066a-c5ef-37f4-9953-f3d97cbd6266 | -7.2423 | -73.09705 | 2026-10-05 17:34:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 24a70afa-a78d-30d2-96d1-b4dc174e9e8b | -2.93549 | -54.10777 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c5931edc-60b2-3464-8031-3043d34e003b | -3.65421 | -55.31701 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ee495e6c-97a1-335c-aa45-0f779f28dd5c | -8.27055 | -71.11806 | 2026-10-05 17:34:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 18bae139-4279-3eec-828a-0942a0f3c83f | -12.42988 | -62.45169 | 2026-10-05 17:34:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6f274485-396f-3824-bdcc-51063654dcea | -2.70721 | -56.53885 | 2026-10-05 17:34:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3df8ee86-bc60-31b7-8c54-5a7d8996014c | -7.94743 | -69.93039 | 2026-10-05 17:34:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| cb28a950-b294-3c81-a0b5-a45015f3cd5b | -3.37725 | -54.10549 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 40eb1181-4b1e-3bb2-b0ae-8ed39e4a4f22 | -10.88038 | -61.4066 | 2026-10-05 17:34:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e28735d6-4ab4-3868-b782-e8a21258cb02 | -2.94867 | -54.16175 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| d567e5f2-fdfa-3b81-840a-78435241c467 | -7.94699 | -72.28693 | 2026-10-05 17:34:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 8.5 |
| de8e9157-aec1-32ec-933e-782938b2de3d | -2.97745 | -54.10606 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fea27c18-dea7-3980-9edb-2acbab9560c0 | -6.17649 | -55.35118 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 40cbaf59-124f-3ad2-87c6-c459664929a1 | -7.69372 | -72.46971 | 2026-10-05 17:34:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bb832f0e-0570-37e8-b31d-9706b77dc69b | -10.53589 | -65.2793 | 2026-10-05 17:34:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b27a253c-aa09-3d36-bb94-df22d83c5832 | -2.99651 | -54.1079 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| ac684180-e833-3dd2-8c19-4373093284b9 | -3.91514 | -59.66232 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 181c0418-d8f0-3b60-aced-e28306e8a117 | -8.81755 | -49.30931 | 2026-10-05 17:34:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9037c51a-5fda-3a2d-b2e4-088170ef67ce | -7.84767 | -72.83888 | 2026-10-05 17:34:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 11.1 |
| fb54a759-523a-3b7d-9874-ff7f5913e27c | -3.36268 | -59.89025 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 71e99bb7-5d1c-3ec2-bc23-80ae1d578419 | -3.37792 | -58.19052 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 308e334c-ac69-333a-b73c-bae6642efdcf | -7.94078 | -72.85157 | 2026-10-05 17:34:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 10c848c8-abc8-3e3a-a4e8-83dd27e50d61 | -3.71721 | -59.68232 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |


[Clique aqui para ver as próximas entradas](README141.md)
