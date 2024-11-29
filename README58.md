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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46850563-45bd-3591-81bb-44c1bff683df | -2.80514 | -54.06747 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 337e2b08-def3-3330-83fb-b3c76461ff4e | -0.87812 | -51.7203 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3b4f11a-39bb-3c38-aba0-9398dd476138 | -4.21641 | -54.76439 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57324583-c8bf-30f9-8034-a62d1ba2c57f | -3.26779 | -49.89582 | 2024-11-29 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 205283ea-159c-30d6-937d-3bdbbf69fde3 | -2.54395 | -54.06159 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 647a010e-54bd-3a97-813c-eb8bf2b25329 | -2.54171 | -54.05418 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7b72e15-ad95-320d-8ff5-edd30283c73f | -1.0892 | -53.64291 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 168b74d9-6df0-3603-872d-11e901e22a1a | -3.0964 | -53.81335 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1fdfb99-1373-3317-a004-7d9f4d88e4cf | -3.11068 | -53.80851 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61d04dc0-2c02-3e2b-8b4b-56932b321a45 | -1.53259 | -52.69538 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bd31ed3-62e5-3ad6-bc2e-8bea464538a2 | -1.39286 | -53.63422 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df8b9620-535f-3c0d-8a00-f23c87d20122 | -2.37017 | -56.11432 | 2024-11-29 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8dd905f8-989d-36a5-a250-bb0a61240504 | -1.73044 | -52.0369 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 629833aa-1de5-3b14-a328-98eab3e82ba9 | -3.39111 | -54.27972 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74a7f6a2-f5f3-3674-a307-1e97fb82c7ad | -1.72591 | -52.48024 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18d0653f-2884-3ff7-9f71-e8cd3ad1c332 | -1.58237 | -53.83677 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 4fbda385-51fe-31a6-814a-e731860d99fc | -3.32199 | -53.6977 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51593079-a22e-337e-ab38-4d182cab9554 | -2.25875 | -53.75261 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23e54eb5-82a4-3df7-9b07-77c777fd49a6 | -1.15548 | -52.23447 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbe847a9-d11f-31e5-898e-ee36e7a53196 | -2.58638 | -53.96593 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 24f865f6-1ac2-310c-918b-334ba2d68c76 | -4.07852 | -47.02744 | 2024-11-29 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2738d48-068b-3123-83bd-a431661a2da6 | -2.36529 | -54.35623 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c3b17e04-5c19-3041-899a-899a7d14506d | -2.14653 | -50.61521 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a8664c4-c339-3890-bd9a-e226aa6f9c38 | -2.77429 | -54.06977 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 515a2e9a-ebce-3e4b-86e4-47ec24ed19ca | -1.59003 | -52.28336 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f5b32dcf-a622-3d10-889a-dbb804f593d1 | -2.50155 | -54.52792 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30c8bafd-d6c3-3f32-aee2-cc74f789c66b | -4.02334 | -49.12843 | 2024-11-29 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 629d66b3-9185-3626-b983-67b9fab27207 | -1.88446 | -53.31754 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aec5ab9c-98f4-30e8-a127-045a36296907 | -1.57202 | -51.18298 | 2024-11-29 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4eced39b-e6cd-3c89-a30f-fadad8d54fec | -1.06615 | -53.37574 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 553c059f-7d2c-3c8d-be8e-ad8eb3e78f56 | -3.7292 | -49.86907 | 2024-11-29 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 01c1cdc4-166e-37d1-8041-8919c9fc7b21 | -1.22615 | -51.80296 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 803275ab-fd2b-3746-89ed-f72cc1e99089 | -1.8817 | -53.3136 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15769cfd-1511-3bc9-b4dc-a7410f21230c | -2.24982 | -53.4631 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4705d635-b223-3bab-ab10-2a5cd9e07704 | -1.16861 | -53.67622 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d0789d2-7a9f-382f-9588-8ac753bf73bc | -1.55319 | -52.07903 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3a12994-94ac-3bb2-b9a4-a43180e37a9e | -2.77415 | -54.02744 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 25f512aa-b823-394a-b5bc-79270129777f | -2.63804 | -52.54204 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54b40054-7f7e-32a1-a5bf-e69e4c8ebf1b | -0.84128 | -51.80248 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 653f6217-2dab-3b89-8781-d8283cd42b03 | -1.75986 | -53.63908 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3006dab-7078-30f3-94ff-70fc054897b2 | -3.68818 | -50.22679 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fea6fa63-6233-375f-bee6-10cbd3115c58 | -3.3525 | -50.51773 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b99bda9-25b5-3662-9c94-545cdcb3b16a | -2.53676 | -47.32492 | 2024-11-29 04:57:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7de82b9-0316-3d17-9dd5-299bb931ba23 | -1.5463 | -51.93242 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 528689af-9a3e-3934-8ea5-2801b954baba | -3.90024 | -49.81501 | 2024-11-29 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5c3934ed-a1d3-3550-8bbb-86545cf3a85c | -3.46629 | -51.59149 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 738b76d6-ee7e-3d03-b840-8ad42dfaf2a1 | -2.10463 | -50.34758 | 2024-11-29 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b88051c3-2424-3ecd-b891-222b93a44a46 | 1.45981 | -55.9271 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d9463d9-630f-3c1d-9e02-53275da309f5 | -2.77316 | -53.98772 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07fccc18-a26a-3349-90a3-d7d37ca4318c | -3.05106 | -54.0386 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51b8487f-3cbe-3327-ad3b-4d676c17e1a8 | -1.34609 | -51.98886 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f972a0a7-188d-3c87-84d5-d446cfe85192 | -1.10086 | -53.3916 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 28efae25-3acd-339f-9e57-9ba1504237ac | -3.66403 | -51.04075 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c2fb5a1c-6af8-3def-aec4-6d436b8a4abf | -1.01692 | -48.06941 | 2024-11-29 04:57:00 | NOAA-21 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29ed7697-1e7e-3459-84c7-3ed5a6651416 | -1.60514 | -55.42509 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1444a673-ff1f-35fb-9147-3aaa459e299d | -1.52932 | -55.3713 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 183b2844-82f0-3e2d-bf1d-281c85fc5716 | -2.98522 | -53.2825 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 13e1f763-9582-3bd0-9a7a-c928640827c4 | -1.57066 | -51.23662 | 2024-11-29 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f853a271-6119-3f19-90f1-cb7063c423c2 | -1.82655 | -52.07395 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f091ff40-b5b9-322d-ac24-49459f2fdbfb | -3.68972 | -52.42088 | 2024-11-29 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 673281a1-4095-3732-8393-13785949bfd8 | -2.45668 | -53.70597 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 26e77e34-089b-395f-8361-ad04b9d4763d | -1.95227 | -53.34264 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 62e266b9-cef7-36af-a13c-6999dd710e09 | -2.44659 | -53.66224 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b600916-5ee0-36fa-b45b-2edb37f91fe0 | -3.5269 | -51.24747 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aed0b181-8c73-35bc-8ba6-9271f8a98104 | -2.90352 | -54.17806 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b40190f-701f-30d9-b7ca-87fde4c660d7 | -2.97448 | -53.35133 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61f50065-8b60-342e-aef9-be3ab5bcc5c4 | -3.04323 | -50.98026 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87670588-22c4-3e80-b4a7-24da0074d976 | -1.99002 | -53.29575 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9faa3ee7-5717-3f95-89ce-d346c69dd083 | 0.97953 | -50.25684 | 2024-11-29 04:57:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4234294b-bf4a-33db-ad8b-ab90269f0daf | -1.32011 | -51.74347 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8692ca74-bb0e-3bce-ad74-54441156b1a8 | -1.43032 | -53.3941 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f5f27c7-1e86-317d-86c2-aaacf8df794b | -5.27968 | -45.12323 | 2024-11-29 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| baaaad64-1b50-3567-96d8-11268bd5605d | -2.97625 | -53.88615 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74d6b8e5-a883-3e78-802b-71af05f690d6 | -3.20413 | -46.56462 | 2024-11-29 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 180e1608-e73f-3502-bc17-5a54db121117 | -1.59222 | -52.2693 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6c318265-31bd-345e-9c5d-57d82cf9bb75 | -1.31143 | -51.95463 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fff788b3-a85e-350e-a928-83909e33ebe3 | -5.2225 | -44.90903 | 2024-11-29 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ff57843-4a6a-3451-98b5-b8099a268bba | -1.06603 | -51.75589 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01763120-d8e6-3a45-94fc-c9a7239f0972 | -1.10189 | -54.12613 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 102e5852-04c7-3148-a8e7-9814ed1ef58a | -2.59853 | -53.97485 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3987d9c3-6c8b-3697-a50d-172d81d9e6f6 | -2.39233 | -48.55788 | 2024-11-29 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2badafc-ec8f-357a-87c9-a57bc544923b | -3.11465 | -53.98209 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87f7852a-888a-360e-a8d0-57edde04c587 | -3.10132 | -53.25808 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52487e9f-e2da-3522-b500-20d148f2ce77 | -1.4023 | -53.40033 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68ab167e-324e-3692-8127-bf5918f2773e | -2.245 | -53.62395 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c432bda2-71df-3fe7-aa16-f68352139dfb | 0.58844 | -50.79061 | 2024-11-29 04:57:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9bce7dc-cec0-394a-bbc6-022d0b4be432 | -2.25136 | -51.11612 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40b55bc0-707c-3da5-85c7-e8291633023f | -1.33379 | -51.92163 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d13075d-bc5f-3a5d-a570-d26449015971 | -2.60563 | -54.27645 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21560177-39c5-32ca-8df1-aaf656cf4064 | -1.15763 | -53.68151 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98a590a2-3ce5-34a6-83ae-31863cef7f0a | -4.26206 | -53.53839 | 2024-11-29 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5bc74585-0b65-3c51-bece-4f3e02e5725a | -3.07177 | -54.40676 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5aa5a535-22de-39ba-8371-4042de8ae679 | -3.05295 | -52.76083 | 2024-11-29 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b7ad88a4-c962-38c9-b2a9-269b0ef546ee | -1.18677 | -51.76751 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 17808057-3aca-368b-b476-97818c235825 | -1.96151 | -52.1053 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67b5f07a-40c9-3fc4-b379-b2fa99175c98 | -3.54478 | -50.5349 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34868486-1acc-367e-8c9b-9c52f3d5df2a | -1.66001 | -52.72907 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7ff2c4e9-0c36-357a-a353-79953abb44ac | -4.78255 | -46.11904 | 2024-11-29 04:57:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7de8caf8-891e-3810-9ec7-e8d36382d66d | -2.8378 | -49.84334 | 2024-11-29 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a086a20-7a18-374b-bade-c1fdc5f25013 | -2.05979 | -52.03989 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README59.md)
