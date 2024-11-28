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
| f6fb6620-a163-305f-ab95-f6fb0279d3a0 | -9.77425 | -48.20822 | 2024-11-28 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b59cff9f-0e18-3bf4-9e3d-c7beeddbcbfe | -3.49167 | -50.08288 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 78161179-0a31-3b59-a6fd-4c7ee5ad01a9 | -3.8278 | -46.54501 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d66fc08-94af-3db2-b430-e13d2e64a651 | -4.32961 | -50.76413 | 2024-11-28 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bac5f4c-ba97-37ff-b3c6-7931cee60963 | -3.24882 | -50.77008 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f20981c4-7880-3857-a625-441e4f11d2f8 | -3.0355 | -48.50435 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6da31c51-06de-3b50-9d53-edeb08f1dc79 | -2.81011 | -54.07765 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e024e828-ae56-3415-b968-f35e43056cb3 | -2.83968 | -46.83665 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99b749f0-fb45-3ab0-a306-008938641ecb | -3.10754 | -53.25657 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b40b5234-6aa6-3ada-83ea-a363930a1688 | -2.86436 | -46.85517 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 54205a55-ee87-3428-adef-24227b3e3ad8 | -4.45359 | -45.895 | 2024-11-28 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9429394a-63be-3d4f-b75e-8cd734445766 | -4.19858 | -48.56911 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e86768e3-3d3d-3e64-9618-e1d83c94eb47 | -4.77834 | -44.4253 | 2024-11-28 04:25:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 18f1ce04-2f10-370e-b4f2-d5e0a33573db | -2.84214 | -54.07672 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28383645-9f30-3e93-b47e-d93c4fdd80c7 | -4.10669 | -50.9827 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 02c320f7-fccf-341d-b4f4-17c6dcbd2201 | -4.08291 | -48.81569 | 2024-11-28 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 49071766-2470-31c7-8e75-6401064bfe90 | -3.81116 | -47.47139 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae8e63ed-7c0b-3784-b1e3-47fb01bfd4bc | -3.91013 | -47.2025 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5802dcc0-1aa3-34ad-8d62-439aa2c55027 | -3.77726 | -46.69166 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3051346b-4f07-3b0b-bb2e-9b997db39d44 | -3.43338 | -54.53928 | 2024-11-28 04:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f108ae99-3e34-35de-94f6-2d453ed33dd2 | -3.97043 | -46.73669 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6edbf63b-1019-3bb2-9c66-c8fba50d2920 | -3.93256 | -47.0181 | 2024-11-28 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1ad385f-24a3-3718-b3dc-c586723303ca | -3.05214 | -48.51543 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a795ef90-a487-3da8-831d-647ff7806519 | -4.30805 | -48.1816 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f399ac9f-d19a-370a-80ed-6b4e0d39382c | -3.44068 | -50.12546 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4926cd9-0ccf-3fde-a4fd-36c5f2d55fe7 | -3.39293 | -50.31956 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7665d045-fd81-3a64-a800-f71fc2ab8206 | -2.25343 | -53.75432 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a641faeb-7559-3f1b-8856-befed7036a00 | -3.10491 | -50.36764 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfd84802-e037-387f-89ef-1e7b8fa8187a | -3.31884 | -50.25868 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 408be1ce-7313-3581-998c-412fb4feba3f | -3.6214 | -44.04764 | 2024-11-28 04:25:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| f2ca83f5-3912-3ef4-ae39-100be35243ee | -3.49853 | -50.46348 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 66d0687f-fb40-3d5f-8d7c-780df7591c26 | -2.90089 | -54.1813 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83a4b834-70cc-31c3-a8a4-ad106f39dc66 | -4.21125 | -50.9017 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62bf5312-130a-3389-9767-5bca522bdcfa | -3.74333 | -47.58974 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 040d6dc3-b28d-3c9c-8f49-03dc23d02e69 | -2.74742 | -48.66357 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4dd81d2d-a1a7-35e6-8149-70fa3d126344 | -3.56955 | -52.28484 | 2024-11-28 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b222da9-6de6-3816-aed8-b910ca502ba7 | -4.04971 | -46.83623 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3446c56-3ec4-3d74-97f2-84ba0dd4c78f | -3.03716 | -50.97833 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c0c105d2-a9a1-3f9a-af78-14bb19682eff | -3.80676 | -46.67823 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8bae2ce0-1fca-3a4a-960e-8505aa8a970b | -3.32457 | -50.22318 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30879ee7-deec-396c-b2c0-fc877f3f9ba5 | -3.93899 | -46.89119 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5521b50d-2585-3bc3-9f0a-546e35faacb7 | -2.5428 | -53.99725 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bd0db64-32ba-3123-8ac3-91c1e785f9cd | -2.69472 | -51.99373 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99a99b37-d584-3600-961a-140c83563fbf | -2.83236 | -51.84185 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f04b7e04-5a7d-3637-8dc2-7139b1c0bac5 | -3.11788 | -53.76291 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f344e2a0-28b6-31c5-96a2-d811fdf75c89 | -2.97995 | -53.89111 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| febfc19f-192e-3705-839b-3563b453ae9d | -3.96766 | -46.73263 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32f4070b-1342-3881-bbc7-89d2ea2e3b84 | -4.01133 | -46.99046 | 2024-11-28 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c33888b-c1a7-378b-935a-45f07e405b4c | -3.96633 | -48.07792 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b4995b17-7afb-3f84-a7d6-578d4b785591 | -3.96271 | -49.93658 | 2024-11-28 04:25:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb65912c-4454-3304-ba49-83ba38479917 | -3.78918 | -50.13234 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0702a41f-f895-32c0-9a9e-0744fcb0e82d | -3.38551 | -50.11984 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 715d9d7c-9723-31cb-ab64-33f08250299c | -2.2343 | -55.90652 | 2024-11-28 04:25:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7811d8b0-b004-3e6d-886b-2206be15830e | -2.86269 | -46.84391 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95f7071c-2827-3ac8-9e30-ccbc40bc5430 | -2.69847 | -51.99896 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47f21022-92f7-3a4e-ad6b-55bcd8518fee | -3.20442 | -46.59565 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f38dbc6f-4748-3be2-9196-5bee2acd3841 | -4.08842 | -49.3366 | 2024-11-28 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a471c47e-4d0b-33e8-aec9-1491f94c7cb8 | -2.82687 | -46.84224 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| add15746-632b-3639-a7a1-b917324f05b0 | -5.21667 | -41.28376 | 2024-11-28 04:25:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 47b379b0-ffcd-3751-a509-d26d2b94f0de | -2.88543 | -48.73919 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| effd7042-f2a6-34cd-983d-dd57e8a06b1f | -3.11605 | -53.11039 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 48412cac-7cfd-32fa-9592-f729f91e33d7 | -4.34184 | -45.8707 | 2024-11-28 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d06162c7-0ae9-342c-9514-3c2688bdd875 | -3.11365 | -53.76202 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9203c8e2-1af3-3dc3-85f7-6788cd027485 | -3.70298 | -43.4271 | 2024-11-28 04:25:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 257d94af-da5c-3b37-8f62-1025e89586f8 | -3.14676 | -51.13593 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c524701b-6673-3d5d-8330-1d9f186dbeef | -4.02142 | -46.32945 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4767e995-d833-3725-9cf1-31f34b38db08 | -3.4396 | -50.00882 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6e63f64-6c43-3e2e-9567-8fb4b9549a6d | -4.68743 | -45.81213 | 2024-11-28 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98390523-342e-3b68-b907-2ce834c64ac7 | -2.8531 | -46.86081 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d52dbe3-e00b-3711-bdf3-ff5e0421e725 | -4.91364 | -47.85847 | 2024-11-28 04:25:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ef333c7-b158-39d4-adda-56a35915e686 | -3.34767 | -50.52079 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e560d9da-fb82-3845-b56b-d7c9287ad0e7 | -2.93929 | -48.33636 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2170489-8b9a-303c-a911-6623236faafd | -3.93872 | -46.72084 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 787cd00b-1253-3133-9d6f-360d5b382b03 | -3.20386 | -46.59917 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6002d08b-2e61-3c5d-99ae-5791bbc1adcb | -4.00629 | -48.30024 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 974568f4-eece-3332-aa50-b75590a6f94f | -2.86487 | -46.87368 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0b8ce165-b863-365f-b7d1-e87659e956f3 | -3.40944 | -50.98607 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3dc189a-0877-324c-bb55-ee64419167c0 | -4.38202 | -49.747 | 2024-11-28 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 734db7c0-6560-3c73-9240-7f3871cfa450 | -1.50074 | -54.46714 | 2024-11-28 04:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c78c3843-b956-3005-8133-79454cb496b4 | -3.27098 | -48.76123 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 609dc7a7-a049-3f09-aaee-584dd578d809 | -3.26679 | -46.43983 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27fa6a8c-21d0-3051-aba3-0f40e2640e02 | -3.56168 | -46.33561 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aed64a79-fcd8-396a-af7d-263d8ef00823 | -3.94265 | -46.6962 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f7bd8f2-0a9e-36a3-a2de-cddef263e7fe | -3.38662 | -50.1117 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 93c0bec9-bbad-3236-b569-7f28ddfab7e0 | -4.35112 | -48.56777 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1d28a0a-189f-37bf-8034-0c9ce5b2cbbe | -3.09683 | -53.73816 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55b540be-2bc9-3cac-8363-c55c777b9590 | -3.3827 | -50.11109 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 2f26e532-174e-34bf-a893-cfd48b7d87dd | -3.39469 | -54.28924 | 2024-11-28 04:25:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6be974fd-fd2b-3304-9c5e-b57c5be43195 | -4.21299 | -50.89091 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1155c8a5-17ad-37b3-b2fe-7d613fa2f6af | -3.22274 | -45.64179 | 2024-11-28 04:25:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f258083d-d7e2-3c4e-ab72-1d9083d78cd5 | -4.21357 | -50.88732 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d9c1a00-d4c9-3299-8c51-f8ff31e1fbf8 | -3.9157 | -49.34408 | 2024-11-28 04:25:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb47caf8-ffaf-3a38-ad00-4b2f4b50af38 | -3.44109 | -50.02423 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c92abbc8-23f2-3d59-be42-7febc38e3f6f | -4.31305 | -48.08341 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 419e927c-7bd0-3c62-9c74-77f9485be0c2 | -2.71635 | -48.67158 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6c8f402-2c59-36b7-be79-c04d21bd5f42 | -2.14862 | -50.61129 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93afc75f-e4c0-30bf-aa19-eae40bebed33 | -3.24833 | -50.61788 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f6f6f75c-c1f3-3d83-8685-f1b8191f4d34 | -3.77838 | -46.6846 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5caa0cea-ac43-33ee-bd51-209b4f5ee486 | -3.29972 | -45.52012 | 2024-11-28 04:25:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 75361893-66fa-3be9-98b6-6f24b4fe5f83 | -2.60552 | -51.79439 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README53.md)
