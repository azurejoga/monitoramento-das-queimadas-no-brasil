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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d43ab538-3492-3879-9e61-b86ca1f3fa2e | -2.4753 | -45.8561 | 2024-10-27 01:45:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 116.1 |
| c4a7b62a-98e5-39c4-949f-61bc92f12e51 | -2.4753 | -45.8338 | 2024-10-27 01:45:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 105.0 |
| ab90cc5a-b592-3916-a51e-0311795ff2a9 | -2.4786 | -50.2858 | 2024-10-27 01:45:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| ed8c28ea-9273-372e-ab4f-9fe7d766a6e4 | -2.486 | -48.0507 | 2024-10-27 01:45:19 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 6aa245d8-4516-3e49-bf85-0361b75ee3b8 | -2.5045 | -48.0502 | 2024-10-27 01:45:19 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| fa6478fb-a8c4-30d4-88ab-36215de6225c | -2.6482 | -49.2465 | 2024-10-27 01:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 6f7db41c-501f-343f-ab92-37f4e503a5b2 | -2.6505 | -54.2971 | 2024-10-27 01:45:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| c9f1f7b7-7145-38ee-abdb-fd06bfb82ec9 | -2.7033 | -49.33 | 2024-10-27 01:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| c550ad43-a34d-38a4-8ae0-54cf0d4abb3b | -2.7034 | -49.3088 | 2024-10-27 01:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 61e1365d-234e-3139-a5d8-3d459aadd01d | -2.8329 | -49.2626 | 2024-10-27 01:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| aa3d9423-d591-3e7e-bbce-84a8fcfaded5 | -2.833 | -49.2413 | 2024-10-27 01:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 0cfcedbf-ec53-391f-856b-70751133a8a4 | -2.8397 | -52.5532 | 2024-10-27 01:45:21 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| ee8cbb6c-19ac-31df-93a0-3778004ab820 | -2.8422 | -51.8148 | 2024-10-27 01:45:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 27937537-0a10-3025-91fc-4b061f86aeb9 | -2.8423 | -51.7942 | 2024-10-27 01:45:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 0576f8a5-07d8-398a-a6b0-6595b0058d5d | -2.8515 | -49.2408 | 2024-10-27 01:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| ce08046f-3922-34cc-a35f-6bc4cf70f28b | -2.916 | -51.7716 | 2024-10-27 01:45:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| bd509aef-ea1e-3b5f-804a-8e290e5d3983 | -2.9161 | -51.751 | 2024-10-27 01:45:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 9171ece4-d780-3e93-baa4-d3369e5e83e9 | -2.9214 | -50.295 | 2024-10-27 01:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| c1de52c5-831d-31eb-b02f-637cfb0b954b | -2.9215 | -50.274 | 2024-10-27 01:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 14bce638-289b-327b-90c1-99a10a1a7235 | -2.9345 | -51.7711 | 2024-10-27 01:45:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 88e195cb-b114-3894-be8b-93754ab51f67 | -2.9345 | -51.7505 | 2024-10-27 01:45:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 5ea562d6-e662-3fe4-913a-253b0f767f81 | -2.9399 | -50.2735 | 2024-10-27 01:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 73194486-c831-3cfc-b597-7c0ed874f189 | -2.9669 | -53.0389 | 2024-10-27 01:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| b76c273b-b4dd-32d7-994f-5a0c47ec57b9 | -2.9845 | -53.2617 | 2024-10-27 01:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 049bd3a9-5d73-3a0e-ba0d-c6c7eab6a403 | -3.1242 | -50.3519 | 2024-10-27 01:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| cc0ca849-93e4-3f0e-bd96-0b0a66bbd4cf | -3.3256 | -50.7641 | 2024-10-27 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 1ab26a06-8b2c-3e7e-8e4d-2a141ec6202f | -3.344 | -50.7635 | 2024-10-27 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 89455926-c998-3c2d-bb4e-4da951ada257 | -3.3441 | -50.7426 | 2024-10-27 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 7cc41658-6b3d-3c04-86bb-518a22e8d788 | -3.4762 | -54.5772 | 2024-10-27 01:45:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 488499f7-01cc-3c0f-b4f2-7a6e448651aa | -4.254 | -63.153 | 2024-10-27 01:45:30 | GOES-16 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 58630768-f5c3-3cc4-8b05-141a8b086149 | -4.3522 | -45.8462 | 2024-10-27 01:45:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 44.3 |
| c19f0acd-4bfe-3a8c-8b50-67ce93532acf | -7.2264 | -46.0498 | 2024-10-27 01:45:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| e7854b8a-c23a-316b-92f8-a7e8ea0bfd19 | -7.2452 | -46.0482 | 2024-10-27 01:45:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 4a2e0fbd-af78-35c1-ad13-1b216f7cbad2 | -12.8883 | -44.6143 | 2024-10-27 01:46:17 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.3 |
| b4c452ff-f610-3c95-af98-a006c979631d | 2.71793 | -61.49492 | 2024-10-27 01:49:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e9d4a86a-7ad2-3599-9f89-94a1380baa6d | 2.30556 | -61.33311 | 2024-10-27 01:49:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 66846612-a59e-3d23-aeb5-f60aae45e844 | 2.29831 | -61.33582 | 2024-10-27 01:49:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cecf7484-d182-3929-aaaa-088f8b250aa1 | 0.11172 | -62.54721 | 2024-10-27 01:49:00 | TERRA_M-M | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9b738beb-b8be-3ec5-bd18-b9ac4e9276b9 | -4.25927 | -63.15524 | 2024-10-27 01:49:00 | TERRA_M-M | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 26.6 |
| a4af24d3-a4e3-3d15-b68f-644762274dcb | -4.25801 | -63.1461 | 2024-10-27 01:49:00 | TERRA_M-M | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 3b0b8118-c9ad-3524-8892-8cd380f2f07d | -4.01588 | -59.82859 | 2024-10-27 01:49:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 65163ab1-6727-3676-af42-a0b50b308a50 | -3.4689 | -54.58051 | 2024-10-27 01:49:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| b24fc27e-2821-3fd9-b70c-d782aaa1ee05 | -3.42405 | -59.2506 | 2024-10-27 01:49:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| bda065fb-9ea7-30d1-82b5-e1477678d1bd | -3.18675 | -58.95359 | 2024-10-27 01:49:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 489a2c11-a60f-3fdd-8e85-16a1e3b7723d | -3.05757 | -61.67249 | 2024-10-27 01:49:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 58c1bee2-060f-322d-ab68-fa6d7ba19e33 | -3.0386 | -61.66614 | 2024-10-27 01:49:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d01ad1ef-8209-321e-b704-e54ad2dce8c7 | -3.01698 | -61.70538 | 2024-10-27 01:49:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2a241e26-0d8d-3e34-8272-c2e51c7189e5 | -3.01573 | -61.69651 | 2024-10-27 01:49:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 646ad286-9155-339e-bae9-d21e46995833 | -2.89185 | -61.87057 | 2024-10-27 01:49:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 16d58240-df8e-3732-944d-b7ff69a2c140 | -2.89106 | -54.90738 | 2024-10-27 01:49:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 415b40a4-ab44-3f79-ac20-de05c0c49703 | -2.84293 | -51.81204 | 2024-10-27 01:49:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 7ff2ee76-7f74-35c6-a6f8-3d10869c795c | -2.84283 | -51.80706 | 2024-10-27 01:49:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| cb6fcbc9-17f3-348e-9991-5449962ddb80 | -2.6827 | -59.42922 | 2024-10-27 01:49:00 | TERRA_M-M | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b99ac6c1-3a49-3666-9132-cb33c79de926 | -2.68137 | -59.43542 | 2024-10-27 01:49:00 | TERRA_M-M | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| eabdb663-5079-3ef7-9c6a-b469b3bbf8a8 | -2.6349 | -54.31774 | 2024-10-27 01:49:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 6c1f16f4-cba7-3b8f-8185-ae067dcec510 | -2.63095 | -54.29103 | 2024-10-27 01:49:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 2606dc6c-3716-3d55-8640-61a3a1088f70 | -2.59039 | -57.54872 | 2024-10-27 01:49:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 12ff2ac0-d21a-3c08-953b-31bb91c34798 | -2.58953 | -57.543 | 2024-10-27 01:49:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 3b22fdc6-46f6-3eec-922c-99f2fe12a000 | -2.5883 | -57.53391 | 2024-10-27 01:49:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 576b8ba4-2987-3923-ae4d-a1d49a4fa9c2 | -2.53492 | -54.65556 | 2024-10-27 01:49:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 8e293a89-f669-3223-a36b-7ccdd5848d1c | -2.21779 | -54.49074 | 2024-10-27 01:49:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| fabac8b6-25b1-347d-8785-6abca7e0998d | -2.12902 | -55.86536 | 2024-10-27 01:49:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 699c6926-b8a7-3c9a-ba2d-26fdd2c19f22 | -1.92003 | -59.99083 | 2024-10-27 01:49:00 | TERRA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 853bd700-d359-3cf3-9650-b39c276827a6 | -1.9186 | -59.9805 | 2024-10-27 01:49:00 | TERRA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e3b0be6e-0d36-3201-a592-1426eb1460ce | -1.90906 | -59.98192 | 2024-10-27 01:49:00 | TERRA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 707ee0bf-ad77-30b8-93ef-5b57dbd43173 | -1.89132 | -59.55329 | 2024-10-27 01:49:00 | TERRA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5c9cf259-36fe-3af0-bfb7-1e7f9727af25 | -1.43976 | -53.42083 | 2024-10-27 01:49:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 0ec22de1-32e5-3ef6-aae7-dd6442313aed | -1.43218 | -53.41669 | 2024-10-27 01:49:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 8c8e3ea9-7734-3e31-930d-2383bcda554b | -1.34412 | -55.882 | 2024-10-27 01:49:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| eb33ea9f-c0bd-3e25-bdec-0ad1da7a1d16 | -1.27053 | -53.06157 | 2024-10-27 01:49:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| def814b2-fd09-3b2d-9cf5-411bc4b44aa8 | -1.26462 | -53.06953 | 2024-10-27 01:49:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| a9f2ee43-445f-334a-b26c-fa3b7933b7f3 | -1.25947 | -53.03429 | 2024-10-27 01:49:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 1a911290-c5a7-3be4-bdf1-e647eef76a05 | -1.17677 | -53.91143 | 2024-10-27 01:49:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 5d6b497a-dd75-37ee-a67b-e828c089e5f0 | -1.17241 | -53.88023 | 2024-10-27 01:49:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 93137e35-b5b4-32ae-ad13-f560ee468c16 | -1.17236 | -53.90697 | 2024-10-27 01:49:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 01fb131c-6d53-3782-94b2-8c262d05f58b | -0.99487 | -53.72304 | 2024-10-27 01:49:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 679d99d6-f0b5-30c0-b261-eb7dcd17caa1 | -0.99023 | -53.69096 | 2024-10-27 01:49:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 134.5 |
| 7c0bb627-226c-3dca-9292-8bf9d56de8ac | -0.97942 | -53.72729 | 2024-10-27 01:49:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| bf87789c-089f-310d-8a86-4d0d0571b1fa | -0.97452 | -53.69368 | 2024-10-27 01:49:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| b656740c-5e58-33ef-8f1c-712da10e8787 | 4.93348 | -60.26833 | 2024-10-27 01:52:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 681860ba-53ea-37d5-bc01-40b931cd579f | -0.9815 | -53.7192 | 2024-10-27 01:55:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| a9306350-0573-3ce5-88c6-01baf1c79f9f | -0.9815 | -53.699 | 2024-10-27 01:55:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 214.8 |
| 12538397-b98c-37ab-95e5-05ce87d753ba | -0.9815 | -53.6789 | 2024-10-27 01:55:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| d51055d3-bca8-3b70-8534-b27ed74d81a0 | -0.9998 | -53.719 | 2024-10-27 01:55:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| ef74e0a9-b9e1-3b08-be5f-d7c583b76636 | -0.9998 | -53.6989 | 2024-10-27 01:55:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 42d0ff76-6f2d-3e12-8b52-a785d9dc4cc1 | -4.2531 | -63.137001 | 2024-10-27 01:55:16 | METOP-B | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8c5ce0cf-d97e-3605-817a-381c9a4e30fc | -2.4598 | -50.412 | 2024-10-27 01:55:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| dc9e762e-b753-3074-861a-82b8cc9fe0b4 | -2.4753 | -45.8561 | 2024-10-27 01:55:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 81.6 |
| bd7ae47b-5f39-33f5-abea-bb81024d88a9 | -2.4753 | -45.8338 | 2024-10-27 01:55:19 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 107.9 |
| cb983706-b147-3f4f-b78d-a78537052a1a | -2.4786 | -50.2858 | 2024-10-27 01:55:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| e2e9c480-feaa-3f48-ab88-4a31473335f6 | -2.4824 | -49.102 | 2024-10-27 01:55:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 28439d8b-3e7b-3e61-ab2f-106e4b9573e6 | -2.5045 | -48.0502 | 2024-10-27 01:55:19 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 14a7b295-0d7a-360c-8a16-8e2f606616aa | -2.6297 | -49.247 | 2024-10-27 01:55:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 0d2182fb-03a5-38bb-9907-2987571a8eb3 | -2.6321 | -54.2975 | 2024-10-27 01:55:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| dcef51b3-cfc5-3301-b919-f2622ee789c6 | -2.6505 | -54.2971 | 2024-10-27 01:55:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 76b193c8-d9ee-34c0-bd15-056018b37cc1 | -2.7033 | -49.33 | 2024-10-27 01:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 38d17039-4adf-3110-a702-494ee1d3759c | -2.7034 | -49.3088 | 2024-10-27 01:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 309733b4-0b70-3753-9c54-cd96a3bf2101 | -2.8329 | -49.2626 | 2024-10-27 01:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 43061cfe-609e-3194-9ae7-14f60f60636c | -2.833 | -49.2413 | 2024-10-27 01:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 6a576b68-3c98-3d70-a385-a7f1e15cfcd0 | -2.8422 | -51.8148 | 2024-10-27 01:55:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |


[Clique aqui para ver as próximas entradas](README23.md)
