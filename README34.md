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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0464213-9246-32e0-aa92-9ad0474a12d2 | -4.39953 | -49.41046 | 2024-11-08 04:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 228af27b-e273-3b97-93ad-478f90faff68 | -2.01667 | -52.33234 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 54af4888-cf34-343d-90d0-832affc97e8d | -3.0776 | -53.8789 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5de634d-1733-31c1-a36d-b3e0b4ced0a2 | -2.81574 | -52.94545 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfc291c4-c2ca-3bb3-9ad2-f6ef92a8e481 | -2.79519 | -52.94592 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a3cc8496-a9b1-3613-9ce4-76acb79bff0d | -4.5157 | -45.69424 | 2024-11-08 04:53:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 092c5613-30e9-3279-8ecc-8d9c9e915bf4 | -4.86943 | -42.9493 | 2024-11-08 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| de25147d-1bc5-38ab-bbe9-fd3522394732 | -3.24755 | -51.55064 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d437448e-c714-3072-accc-75a649f10c5a | -3.16721 | -51.08348 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24164c9b-0965-3a10-8d24-e6251c1e7a5d | -4.3665 | -49.10605 | 2024-11-08 04:53:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e22ac1b7-b4be-3850-8423-5686dae4c3ac | -2.85555 | -51.77468 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad63f4b9-923a-33d8-9baf-64475caa8756 | -4.23322 | -46.90655 | 2024-11-08 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23db30d1-7b8d-3c9f-baf4-17ee00269697 | -1.23182 | -47.42342 | 2024-11-08 04:53:00 | NOAA-21 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 303fe1c7-b71c-381d-a5bb-b99d28f67966 | -3.25041 | -53.33904 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5abe7ff3-294e-3890-a28a-41d856029072 | -4.52087 | -45.6902 | 2024-11-08 04:53:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 6983a130-4f30-346f-97a8-058c7c9c18de | -3.38946 | -51.42767 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c226684-4530-358d-a188-59de7a125ba7 | -4.24287 | -48.54347 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b917906d-90c9-3e4e-8bc6-de6cc6e7394d | -1.41784 | -51.50721 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b22707df-fe57-3a8f-87ab-9624b4e6373f | -2.76225 | -53.22272 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9eb5502c-16e8-3c56-a9cc-a271e51d35a2 | -1.50991 | -54.76566 | 2024-11-08 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30dd9228-f89d-3a05-9f71-d6cf5cf83524 | -3.62416 | -50.19344 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5470c3e-5d0a-3f37-8416-a08da98ea646 | -2.04874 | -52.08344 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dc5e4a7d-1efb-31ce-a804-d852a428de7d | -3.60159 | -44.91419 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9ab1362a-f7ac-3ae9-8887-15e916a1ecc5 | -5.70412 | -49.30235 | 2024-11-08 04:53:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b214963-074e-3e11-82ce-23e686c51a56 | -1.42358 | -46.80307 | 2024-11-08 04:53:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba1a9aeb-4379-3dd0-af2e-027fc06e4c92 | -2.65257 | -48.56004 | 2024-11-08 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa805768-730b-3e9e-bc51-7cb04845c16a | -2.28382 | -53.81419 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ece1ea4b-1c06-3920-b08b-aa966da7db07 | -4.28587 | -48.6517 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92c87682-110b-3639-91e9-fd46d976449c | -1.42581 | -54.53907 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c31da6a-6a89-3dc2-82a4-72f6563e7d38 | -2.97021 | -49.28328 | 2024-11-08 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b26123f9-f03c-383a-983e-2da8171359b0 | -3.24893 | -46.47715 | 2024-11-08 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d322396-2ee1-34b1-8ca0-c539a779a302 | -1.15025 | -51.99963 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f25268e4-6e3c-365b-b2d5-10efb397e593 | -5.44126 | -46.35799 | 2024-11-08 04:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 82b6af82-ad74-371f-b515-820e86143048 | -1.55961 | -52.2753 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddedc293-1af9-3fc8-8e4c-36b101cdb1e3 | -4.78284 | -48.67706 | 2024-11-08 04:53:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abc47f3e-1701-34a5-9b77-b0a5534521dc | -2.80077 | -52.95392 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87817297-e2f2-3734-ba46-67b29f4e0bca | -3.08152 | -53.37078 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39f61c1a-57d1-3fb1-b768-2256b4a00f84 | -4.78591 | -45.64928 | 2024-11-08 04:53:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c75fa76-2ce0-3862-bdfe-41a05d970266 | -10.73262 | -49.53801 | 2024-11-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04588e8f-017c-3c91-b300-99e8d4959f73 | -2.6112 | -51.75032 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a5e0223a-c737-368e-bd0c-2727162d8b6e | -1.56916 | -51.29941 | 2024-11-08 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6c22035-0087-3438-a736-f6910fc40659 | -2.70978 | -45.69638 | 2024-11-08 04:53:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e820e96-c2aa-32bc-838e-5b522790f0b5 | -2.0551 | -53.30364 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dcb2d6ea-52b8-3102-8a68-542d78fc38d8 | -2.83129 | -48.46796 | 2024-11-08 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1424ae2-5c86-356d-8f27-76f3a54b4aba | -3.91062 | -45.83054 | 2024-11-08 04:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d401a12-b818-3d80-8a31-e4830c120b4d | -2.64155 | -46.77119 | 2024-11-08 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e186319-c1a1-3e3e-98ab-79a824cba458 | -3.3843 | -50.22554 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7f9f777-b3ed-3454-a618-49ad71e1ce65 | -1.61907 | -47.35473 | 2024-11-08 04:53:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2a34f12e-bd4c-3243-bfdd-5b1bb68e30d3 | -2.88895 | -48.29042 | 2024-11-08 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db92bad7-2418-3302-a147-865e666b93f0 | -2.62164 | -51.74842 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b095333b-4436-3c76-a61c-5153697b795d | -2.68814 | -51.82544 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| faaac4cc-35a9-35d1-b69f-ec8cd8abf13b | -4.88623 | -45.4356 | 2024-11-08 04:53:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e5e5aad-e0fa-38a0-abfa-bfa84a4e6245 | -3.23472 | -53.39504 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 733f0039-ce53-3fa7-bf4d-b32244ba80b1 | -3.68365 | -50.19498 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 502f7bab-c15e-3b01-8036-55727a34d764 | -2.96961 | -49.28722 | 2024-11-08 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eea43c71-8e34-32d3-a6cb-16b6256d7106 | -3.54299 | -44.96876 | 2024-11-08 04:53:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b418f9b-c4f4-3ae9-b414-e76643d681de | -4.21607 | -45.74477 | 2024-11-08 04:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a26fead0-1bd8-3f5e-8f03-b657fee49aef | -2.6329 | -46.77356 | 2024-11-08 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f19e693-4405-3518-a02d-2b247ca0a353 | -2.20696 | -46.36271 | 2024-11-08 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d979b2f-caf7-35ac-bdcf-5ec5c5e8779a | -3.72989 | -53.40264 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba2b2a49-f237-345e-8c55-8194c328d54f | -1.46126 | -53.42003 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5aae997e-66c1-3016-a058-5daf3fa6b882 | -2.28725 | -53.81469 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86022abd-3638-3d89-a5a8-22c5dc42a00e | -2.23669 | -53.66701 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b0f2ebe-1fb0-307f-9bf5-6eff3d2b573d | -4.38178 | -48.58352 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c41746a4-7e22-32ca-91a5-f7dac5c4d310 | -1.34248 | -51.42189 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d907451-ace4-3311-8bc7-8d9c71afafe2 | -2.95684 | -53.28238 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2d1ccf2-6cf0-3479-975f-22e97ce0156c | -3.02952 | -54.07306 | 2024-11-08 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15c07a68-41aa-3dbd-9909-1447e451276a | -3.02356 | -54.48246 | 2024-11-08 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 368ff94a-65e0-3f84-b7d8-f249bcc64c0f | -3.02906 | -51.53398 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c63f050c-99b8-38ae-a3ff-90b9452ecc6b | -3.24704 | -53.40427 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 371c427b-810f-3015-a9e2-2eba29b721de | -2.97066 | -53.86633 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f875fa7-40e5-3cec-8a7d-e02410eb4b21 | -2.17768 | -50.97294 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5aeba383-9131-377e-b6ff-9109c9d92da1 | -4.23719 | -47.87096 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 35337b53-2b5c-3afe-ae8e-46ef44e937ee | -3.03237 | -51.53449 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4735c471-502c-3876-9b42-6d6291a97e43 | -2.96253 | -53.91821 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 30f8c2ba-82ed-344d-9c9f-e370d66d615f | -6.74698 | -47.1451 | 2024-11-08 04:53:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 25c5ea40-f4ca-3b27-9f88-efe29c0e201d | -12.33236 | -48.00889 | 2024-11-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be5e37b8-0e04-3cb8-a077-61262067712f | -3.39178 | -54.26752 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d94b320-844e-347a-a030-0d84a3352412 | -2.81186 | -52.94845 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebc96368-f04e-3b83-8871-10b912f31b04 | -2.84841 | -51.7771 | 2024-11-08 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6b52acc-84e7-3187-8f13-c8c582cc81d7 | -1.70351 | -52.33302 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8033f68a-1ba3-3c9b-84bd-8bed9daf83da | -2.11931 | -46.36561 | 2024-11-08 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3df68dec-f9d5-3e95-9c15-d0a96c38825a | -3.08385 | -53.88364 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e20adea-84a5-34d2-8816-c4997c4e24cc | -2.8286 | -52.90443 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09a3f9c1-4b41-3552-b1aa-d0f2a1ed50f2 | -1.12903 | -54.19004 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c8265d3-17f2-3f3d-b5a5-4ff6a063203f | -2.59223 | -47.01459 | 2024-11-08 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f77398e8-7e9f-35c2-bbcc-d0b329918985 | -1.61852 | -52.24545 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9e6c992-daee-3a8d-8554-c350ddd516ca | -2.29953 | -48.58456 | 2024-11-08 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8152d7ad-3c9f-30ef-a835-c8b73ecf2100 | -1.47591 | -47.22232 | 2024-11-08 04:53:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0778eaf3-f80a-32ca-b9e8-0d38f945de2f | -2.64775 | -49.23664 | 2024-11-08 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| add48231-6a8d-38d0-a801-6aace910bd87 | -2.23601 | -46.53331 | 2024-11-08 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c614c06-61fe-31f0-8d81-0d1869c0640f | -2.88689 | -53.97491 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e091c58d-1ce9-316b-9248-cae672d841bd | -1.19473 | -53.64012 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 530334e0-3998-3165-a1f1-cfa8e780087e | -3.37691 | -52.35938 | 2024-11-08 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1adc668e-c948-3477-9f7a-78f61855d153 | -2.22611 | -48.48322 | 2024-11-08 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35c96d0c-7fa7-3784-861c-f7e9c4419c37 | -1.93467 | -47.8441 | 2024-11-08 04:53:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| feaca213-508b-38de-9725-ffb3a4a12984 | -4.22163 | -48.55835 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 28f3679f-e667-38e7-afed-20b25014e3e6 | -2.16223 | -53.65179 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 587a73c4-a516-3b30-a0ca-ed067a1f2fb5 | -3.11086 | -53.71113 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef3a52af-570b-337e-b4d7-08926b1c7349 | -1.38267 | -47.50137 | 2024-11-08 04:53:00 | NOAA-21 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README35.md)
