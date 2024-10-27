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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81250754-f004-3aed-bcc8-6759f371de45 | -2.4786 | -50.2858 | 2024-10-27 02:25:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 172ebd12-5f98-3aa7-a55a-a26a1b970e44 | -2.5045 | -48.0502 | 2024-10-27 02:25:19 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| a0e5fc44-21c8-3760-b36b-ca861e0fd9a0 | -2.6297 | -49.247 | 2024-10-27 02:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| e2a751f9-e503-3c43-9f82-a2ea4afad3c8 | -2.6321 | -54.2975 | 2024-10-27 02:25:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 1b9b9c41-7c25-3bbf-bd76-1103bed0d4ab | -2.6505 | -54.2971 | 2024-10-27 02:25:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 702f67af-ca64-35e4-a98b-707cd3b069f1 | -2.6849 | -49.3305 | 2024-10-27 02:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 3c2ac212-cbe2-308c-a66d-604cf95fbcc1 | -2.7033 | -49.33 | 2024-10-27 02:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| ff6555e2-5eb2-3779-876d-ac456ca52887 | -2.7034 | -49.3088 | 2024-10-27 02:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 3662a66f-3a60-3373-8f83-e94ffa66e0c0 | -2.8144 | -49.2631 | 2024-10-27 02:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 0a767f40-efd7-32ef-85df-94dbba0cdba2 | -2.8145 | -49.2418 | 2024-10-27 02:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 13c3cfb5-a2f6-3dc6-af91-8879af0a4ca1 | -2.8329 | -49.2626 | 2024-10-27 02:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 79fbbe3c-1998-3717-81b4-69649e59cd1c | -2.833 | -49.2413 | 2024-10-27 02:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 79bfac65-3e39-35af-abd9-f4dd575ca38e | -2.8397 | -52.5532 | 2024-10-27 02:25:21 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 0f1b740d-bf98-3056-be31-90f5ab4932d1 | -2.8422 | -51.8148 | 2024-10-27 02:25:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| aa923c22-14d3-3828-b8ed-825cd533776d | -2.8514 | -49.262 | 2024-10-27 02:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 129a01c6-81d1-39f3-83b4-2185af0a6a87 | -2.8515 | -49.2408 | 2024-10-27 02:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| e34ca237-f7ab-3ba6-a3d3-77e5f30f8478 | -2.916 | -51.7716 | 2024-10-27 02:25:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| d34833d9-ccca-356c-983b-3697bb9acf0c | -2.9161 | -51.751 | 2024-10-27 02:25:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 5c8157e4-a369-3c9f-b9ce-a74f2e90266c | -2.9214 | -50.295 | 2024-10-27 02:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 07fa2009-ecfc-3105-a005-356c80cabad1 | -2.9215 | -50.274 | 2024-10-27 02:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| a110a5c6-2d14-33c5-b150-1cd655d3e47b | -2.9345 | -51.7711 | 2024-10-27 02:25:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 754c1557-2a12-30f4-b0ae-6a051255653b | -2.9345 | -51.7505 | 2024-10-27 02:25:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| c6a616fc-9a15-3012-9379-181b761626ca | -2.9399 | -50.2735 | 2024-10-27 02:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 9675a06e-0783-3c72-9c5f-5f3282b9019a | -2.9669 | -53.0389 | 2024-10-27 02:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 9bfc1c65-30bf-36ef-a253-a1b39e3b6f1c | -2.9984 | -45.1207 | 2024-10-27 02:25:22 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 8a3313bf-e7fe-33be-8eaf-0f5cba009860 | -3.1242 | -50.3519 | 2024-10-27 02:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 4afff106-9138-3cd6-8f94-057efe497f99 | -3.344 | -50.7635 | 2024-10-27 02:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 6b7bf08b-3980-31b8-8e91-d8afeb4dd588 | -3.4762 | -54.5772 | 2024-10-27 02:25:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 0d143d29-6f60-34af-a704-4ee3302ef70d | -5.6945 | -41.638 | 2024-10-27 02:25:37 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 116.1 |
| 27ffe5e6-20f4-3711-b3a0-e14ce9ae0047 | -5.5543 | -46.9967 | 2024-10-27 02:25:37 | GOES-16 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| ce7b1d3e-f3f3-3392-b266-8e4c79401c86 | -7.8533 | -45.4066 | 2024-10-27 02:25:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| f148ab92-f66b-30f2-9a42-02e63537b819 | -0.9815 | -53.7192 | 2024-10-27 02:35:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| a6c19551-83f8-3fbf-9f6c-ef9c7d86ab1b | -0.9815 | -53.699 | 2024-10-27 02:35:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 185.9 |
| 0b202064-0887-3719-ab74-bf34b922912b | -0.9815 | -53.6789 | 2024-10-27 02:35:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| c2981d2a-d8fd-37d1-8ecd-76862b4c8952 | -0.9998 | -53.719 | 2024-10-27 02:35:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 1a479f4d-68cd-3533-9d72-554328f67a41 | -0.9998 | -53.6989 | 2024-10-27 02:35:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 133.2 |
| 3d23b6d7-e053-3345-831c-27e5a085cb07 | -1.1831 | -53.8985 | 2024-10-27 02:35:12 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 37c4c04f-58ff-33d9-bc1c-1e654a833058 | -2.5045 | -48.0502 | 2024-10-27 02:35:19 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| c20a6c86-0265-3d30-bde0-e5c918e1584e | -2.4753 | -45.8561 | 2024-10-27 02:35:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 0af9bfd2-fb96-323b-ab18-fb6f5b6a6130 | -2.4753 | -45.8338 | 2024-10-27 02:35:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 42.2 |
| d00794bf-eab5-360e-9e89-d888a97b9ecc | -2.4786 | -50.2858 | 2024-10-27 02:35:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 40eb16d6-d522-3edc-9581-1593f82f6058 | -2.6297 | -49.247 | 2024-10-27 02:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 6b330e69-d4b8-3902-bce0-bf99597d21b8 | -2.6321 | -54.2975 | 2024-10-27 02:35:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| edef330c-6a86-36f6-ab82-8a3f7c59389b | -2.6522 | -48.1324 | 2024-10-27 02:35:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 3c33db1d-050a-3360-9e51-b081e4a047dc | -2.6505 | -54.2971 | 2024-10-27 02:35:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| c5e03a8b-bcfc-300f-8854-141a0786432e | -2.8422 | -51.8148 | 2024-10-27 02:35:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| d0cdde2a-51db-3a6e-b2e4-c666859ebf11 | -2.7033 | -49.33 | 2024-10-27 02:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| a1c27ef2-2e9c-321c-be85-081b26822273 | -2.7034 | -49.3088 | 2024-10-27 02:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| ba6744e4-e011-3e35-a49a-dbf4fddb3cdc | -2.8145 | -49.2418 | 2024-10-27 02:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| deb19a33-710c-32e5-a91d-85915eca2dc1 | -2.8514 | -49.262 | 2024-10-27 02:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 35ba000d-eb2e-35bb-be2c-d81f561b1857 | -2.8329 | -49.2626 | 2024-10-27 02:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 8392efc9-a574-3a99-b0d3-e63110fd23c4 | -2.8515 | -49.2408 | 2024-10-27 02:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 10ada2d3-2c25-3d1a-adb2-cf422c6865b3 | -2.833 | -49.2413 | 2024-10-27 02:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 8c04ee9f-d06f-3e33-99b5-dde0f7b93831 | -2.9399 | -50.2735 | 2024-10-27 02:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| b5f499eb-fab4-3d1c-b9d4-0f6161fde35f | -2.916 | -51.7716 | 2024-10-27 02:35:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| c4ef75f7-338e-3698-b18c-ea513bc994cf | -2.9161 | -51.751 | 2024-10-27 02:35:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 04668e95-4626-31af-8773-de283ef78093 | -2.9345 | -51.7505 | 2024-10-27 02:35:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 112f3535-05b0-3183-a3e9-c5d76a345483 | -2.9669 | -53.0389 | 2024-10-27 02:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| b7114fc5-31c7-33bb-ad42-060ff2aaf909 | -2.9214 | -50.295 | 2024-10-27 02:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 1633fed5-26a7-3ab4-97d1-948cda4713e7 | -2.9345 | -51.7711 | 2024-10-27 02:35:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| c38660b0-75ec-3aa2-8cfe-4585ea77cf15 | -2.9984 | -45.1207 | 2024-10-27 02:35:22 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 5dc081f5-a09b-3978-bc51-e3d367336c73 | -2.9215 | -50.274 | 2024-10-27 02:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| e8d71ec8-977a-328f-8ec8-e5d0031f00b2 | -3.1242 | -50.3519 | 2024-10-27 02:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 13a6d8c7-1edf-3f14-be80-11d839e7a1f2 | -3.344 | -50.7635 | 2024-10-27 02:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| a3d37bc4-20b8-3488-a1f9-292bcaa1d395 | -3.4762 | -54.5772 | 2024-10-27 02:35:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 77d8aec0-b59b-368e-a55b-2c7f823a8705 | -7.8533 | -45.4066 | 2024-10-27 02:35:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| fb6e1490-f010-3740-adab-c43404cc5dbc | -12.8883 | -44.6143 | 2024-10-27 02:36:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 3c3dcd4c-b300-3741-b0d6-13f58f164c67 | -0.9815 | -53.7192 | 2024-10-27 02:45:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 71b0a20f-bf6d-375b-a9f3-57b61753c2e0 | -0.9815 | -53.699 | 2024-10-27 02:45:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 193.2 |
| 625d467b-998e-30e6-aa6b-b12d90796874 | -0.9815 | -53.6789 | 2024-10-27 02:45:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 9655d5f8-55ae-3281-9f87-9263e21864d0 | -0.9998 | -53.719 | 2024-10-27 02:45:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 13967df3-5f79-33d5-b48a-0a33264f9677 | -0.9998 | -53.6989 | 2024-10-27 02:45:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 9bcdf72c-9668-348d-8d0a-96212a9c90e1 | -2.4753 | -45.8561 | 2024-10-27 02:45:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 4f5ebbd8-e103-3987-a6b3-76b5e40904e9 | -2.4753 | -45.8338 | 2024-10-27 02:45:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 41.1 |
| d9439a1f-47ea-3d4b-b679-7033ed6bb8a1 | -2.4786 | -50.2858 | 2024-10-27 02:45:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| db4c1eca-2cf6-3d59-a959-698f52de48b7 | -2.6522 | -48.1324 | 2024-10-27 02:45:20 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| e4b61bf7-2de8-3f24-b8e7-cf4dff10cdd1 | -2.6505 | -54.2971 | 2024-10-27 02:45:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| cf24a868-d400-3ad6-b0f7-054d150c1098 | -2.6297 | -49.247 | 2024-10-27 02:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 30b2d8ef-04ef-36d4-b167-fd0af2fe97c8 | -2.6321 | -54.2975 | 2024-10-27 02:45:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 03c30a1b-fb0c-3319-a600-d83a1415c463 | -2.7033 | -49.33 | 2024-10-27 02:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 0e773d00-c9e1-396e-96c3-84e6acec706c | -2.7034 | -49.3088 | 2024-10-27 02:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| fff37881-d523-3873-8b89-fd7f6945aa39 | -2.8145 | -49.2418 | 2024-10-27 02:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 933119db-db28-3b54-b0cd-642db74d9bb5 | -2.8329 | -49.2626 | 2024-10-27 02:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 389a6695-e6f9-34ab-9dd4-db82a746e7c0 | -2.833 | -49.2413 | 2024-10-27 02:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 5a0b85be-ff28-31b0-a7e6-d890ae21c1d7 | -2.8422 | -51.8148 | 2024-10-27 02:45:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 87d15c6f-ac40-3c9b-bc5a-db77c8697064 | -2.8514 | -49.262 | 2024-10-27 02:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 2d764bf9-5604-3953-9720-7e28353fb5a8 | -2.8515 | -49.2408 | 2024-10-27 02:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| d04627cd-a596-3363-a0a4-17da2270eb5d | -2.9215 | -50.274 | 2024-10-27 02:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| fb062112-5e92-3d5c-b02f-f396af713a2f | -2.9345 | -51.7711 | 2024-10-27 02:45:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 473371f6-24b6-3bd4-8b66-c127a013d191 | -2.9345 | -51.7505 | 2024-10-27 02:45:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| c2ad435a-e0d2-3082-87ed-401487f627e5 | -2.9399 | -50.2735 | 2024-10-27 02:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| a0dbd8d9-4a3c-3ef0-ba4f-a4b03beb0c49 | -2.9983 | -45.1433 | 2024-10-27 02:45:22 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 44.1 |
| cd909506-c908-3914-a74e-84307b7eed06 | -3.017 | -45.12 | 2024-10-27 02:45:22 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 65.7 |
| aa616b59-edad-3498-998f-bfccf7847c46 | -2.9669 | -53.0389 | 2024-10-27 02:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| bb5cadf9-d251-3ee8-b799-699f3b417e80 | -2.916 | -51.7716 | 2024-10-27 02:45:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| fbda17ae-17bd-3dd2-97ab-025ac83f0a8c | -2.9161 | -51.751 | 2024-10-27 02:45:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| e18dc77b-2b89-31ef-9203-11bbc19432e8 | -2.9214 | -50.295 | 2024-10-27 02:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 2869c6f5-b001-3f72-837c-bd22cda2264e | -2.9984 | -45.1207 | 2024-10-27 02:45:22 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 85.2 |
| f1cdd27f-52fd-36f3-b8c3-3595e2d06c0a | -3.1242 | -50.3519 | 2024-10-27 02:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| f39f1cf2-113f-3b5f-827c-0247e9077e47 | -3.344 | -50.7635 | 2024-10-27 02:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |


[Clique aqui para ver as próximas entradas](README25.md)
