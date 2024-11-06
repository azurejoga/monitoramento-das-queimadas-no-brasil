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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87121b03-af5b-325b-8613-ed7c2430d6ae | -3.17077 | -53.07099 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4bb3c96-7867-374e-9209-287388c03641 | -4.37246 | -47.2296 | 2024-11-06 04:36:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78cf0821-c26d-3d3a-ac59-0fd2fa464301 | -3.22654 | -50.92215 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 179ae58c-c563-3f19-a6d2-50e271308417 | -2.81143 | -52.93759 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 307f9755-86f4-31d2-9df7-e918b139417a | -2.91383 | -51.03854 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f54b7127-0fe1-3cb8-8398-23297bae2fe4 | -3.08132 | -50.95821 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 189d46d3-c81c-3a9e-b49b-bf0dd7cd9237 | -2.73031 | -51.73862 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0ac4b407-55eb-3ba4-a45d-80586fd4c2a1 | -3.82951 | -46.50165 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb958356-2844-30db-b809-234b79ef6c90 | -2.80757 | -52.93702 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5ba83dd5-75af-3088-9d90-3df464e42f68 | -2.78619 | -52.87501 | 2024-11-06 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fae77d25-0175-3e0a-bd54-428aa9c89ac1 | -2.35363 | -49.64225 | 2024-11-06 04:36:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5fcdb50f-9d32-373c-b574-1b9167318e2c | -3.06643 | -49.71437 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 56d94e24-20ee-3a0f-9884-55494fd7bfc6 | -3.52972 | -53.00095 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d829a2a-6311-30bf-b692-d716b7eb76c6 | -3.17631 | -50.60147 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 282b4c19-34b2-3d52-b9e5-c3b2319020d1 | -3.6447 | -50.14126 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dccf3cca-6215-3fb1-a8ef-d9588134a525 | -2.9047 | -49.40325 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7bfe8393-9ee6-32a2-bd77-ff660da34909 | -3.72188 | -52.10068 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4af4020-5ff2-38da-baf7-5e6343596de2 | -3.27017 | -50.29537 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82bd6667-e81f-3f9a-99c0-1ada542ab736 | -1.86823 | -54.68979 | 2024-11-06 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e995aec9-2fa4-3d90-9f78-b73b1150f281 | -2.64271 | -46.76697 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0a4acaf-a849-3b03-908d-e7d2b30bd69d | -2.71333 | -46.67512 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 820036ce-9036-3e04-bdc1-294fafb0418d | -4.05453 | -48.24894 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7151a6ea-0472-3f80-8974-c333b2fd2411 | -3.27412 | -50.29231 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a9fe880-4a6e-341a-aaab-f7ca4be67fab | -3.04736 | -49.53238 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ecf24ff-0512-3eee-9dcf-98257a048243 | -2.60327 | -51.3059 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12785c7a-e03a-365e-a6dc-38df18a0e28d | -1.22028 | -51.76955 | 2024-11-06 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1475db0f-584f-3326-897e-d8906f0f16d8 | -3.75462 | -47.59986 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f10cb7a5-83e4-3f74-b761-18652147a139 | -2.15476 | -53.66923 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7ab20b2-cccb-3729-ab24-9a2d84ba656e | -2.83674 | -52.90263 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 3966e62c-4b39-3b51-9d30-091145fbae66 | -3.09606 | -51.12467 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96f32a84-60f8-32c7-8a80-2cc35db71dd4 | -5.02368 | -43.6049 | 2024-11-06 04:36:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e1554d68-3b78-3edc-8492-ad06892b03d1 | -2.3898 | -50.31914 | 2024-11-06 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 216e8550-7078-37de-aad0-5f581c405f45 | -2.72048 | -51.70758 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a544712e-0d00-3153-9e3b-9dd5ed42b8d9 | -3.10517 | -45.9416 | 2024-11-06 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 032cd337-e9f6-3b1c-b31a-1c4d383a27cd | -3.03919 | -51.20316 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 37e6e640-9ae3-3e43-a587-b3049ccaf30b | -2.43476 | -53.92334 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 160046a6-7461-304a-bc31-4c254b31eefb | -2.38711 | -48.57039 | 2024-11-06 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d9cfedf-4c6f-3146-9b3d-4d2f4dcf16c0 | -5.71932 | -43.81519 | 2024-11-06 04:36:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4dc83935-0d50-3ac1-adf8-41c06d3c3441 | -3.01647 | -53.43044 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 50053a3c-e86f-3cb2-9a45-25766682a196 | -3.11655 | -51.10813 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1a533fd9-51e2-32ae-9778-0265d7933bb3 | -3.11716 | -51.1043 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a9e2e078-a9ea-33fa-8da4-db39e66069e8 | -3.71702 | -41.6855 | 2024-11-06 04:36:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cd5e10e8-7dc0-37c2-aeef-6e02a8fd3872 | -3.73207 | -45.59912 | 2024-11-06 04:36:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bdac522d-17ae-3136-8992-a107ca9900e5 | -3.00436 | -51.44733 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8675bb78-db78-3c14-bdcd-2e418fb64bfd | -1.42457 | -52.25458 | 2024-11-06 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68a35b79-0734-3794-b750-5d28bedc6d77 | -1.1991 | -53.65182 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3e174ec1-4208-32bf-91df-f4846cff4bec | -3.29686 | -53.1198 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61378d0c-699a-3727-8b32-afad91ab496f | -2.40725 | -48.87234 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1a5e793-4d53-321e-aa92-4a864dd59c3c | -2.24389 | -50.71076 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d6d3f2e-ffc0-3545-b4d9-32dd31146fe2 | -2.3469 | -48.95454 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcef281b-fac6-3bef-a0e7-24c65253e3b0 | -2.85357 | -49.23175 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11b5b8b5-b998-3c15-b899-3f7a5faf61cd | -3.03765 | -53.27758 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b4a596a2-dbd1-3cab-ad5e-8760108ed7e5 | -2.81988 | -52.90966 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| a38f6efc-856c-321c-8b66-d7055e57d76b | -2.60274 | -49.27071 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f58043a3-2bcd-3087-a695-ccad6a7afb30 | -2.31974 | -48.86592 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6dcb891f-4b13-3c23-b2b2-67b420319db7 | -3.18431 | -50.59518 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec9352d2-c4ef-3c1f-b368-b2b1d0ca85e9 | -2.67572 | -46.71478 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03ca7751-ed3e-37f9-a960-381c8d563a8a | -2.87627 | -51.61828 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a364648-e348-3f68-808c-f44f0cf0ffbe | -2.50896 | -48.91644 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f598560-ecb5-3822-baf8-ef7c11a485a4 | -3.24303 | -49.58415 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01287239-f438-3492-b798-7d316854b75a | -3.76049 | -51.76941 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58c80c6b-fe15-336c-ad2a-c98fe1fcb9c0 | -2.81769 | -49.87004 | 2024-11-06 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03bcdb91-25e0-3a72-80d7-53971835af9b | -2.85239 | -51.78035 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| db3d81e7-57f4-317f-a682-e22e9a289320 | -2.76188 | -53.21882 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 07eaff8f-0afc-3352-b7a2-b7db96c23b76 | -0.3458 | -51.57133 | 2024-11-06 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 414f90ce-02da-3dde-8000-62ff3dc5beb4 | -2.41686 | -46.68748 | 2024-11-06 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 381a22d8-d510-3f22-af78-829b7067f85b | -3.08782 | -54.51719 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52f7a080-7ba1-3675-8a2e-2ae2f4f3a181 | -3.03667 | -50.41915 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1b29d80-2815-3061-afa0-70d1ae0e7a97 | -3.32703 | -49.63335 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1610a17-a09c-387f-b4e8-47209fcf9931 | -1.52214 | -52.2261 | 2024-11-06 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 69cc959b-4c64-3d1e-8181-d117779776c5 | -2.8176 | -52.9482 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| b93c7695-f4bf-3174-982e-027252a9f5b3 | -3.52815 | -50.354 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b1c59287-7e19-3c08-9b45-c77df0ec29db | -3.08619 | -54.50063 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d36f18a0-c986-3911-b8b9-6f94320e5f47 | -3.15975 | -53.97696 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3277727-514b-3da4-b113-47c18201a8b9 | -4.12714 | -43.57658 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 177e12e2-233b-3f7f-bf43-5a8032e64172 | -4.25117 | -50.25763 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 488f00a3-0e51-3ac5-82e5-bb3702efd106 | -2.42908 | -48.45394 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e1a5a68c-0765-3c5c-a7df-162d97c208d4 | -3.97743 | -48.15525 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1892d15-bd8a-3e2d-992e-f1fe58f1c974 | -2.64977 | -48.56257 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e60de3c7-2458-3fff-8adb-246b235bc163 | -2.61202 | -49.19068 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a50d9de-715d-3814-83b6-16a6e429a7a3 | -2.81757 | -52.92394 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9d0b6d0a-74c9-3db3-bbb4-94e2a1f17511 | -2.38272 | -50.40815 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f396f91c-47dc-3ac7-a605-e3de4ff0828d | -1.19638 | -54.07664 | 2024-11-06 04:36:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f4ad930-59b3-340a-b370-3fbeea42621e | -3.06304 | -52.50224 | 2024-11-06 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 50370ee8-3e3c-32ca-8edc-5f8bb639a49c | -2.44016 | -49.18108 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b1fd203-2704-304c-8e89-c426b904391c | -2.53008 | -48.1987 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 338dd263-06ca-3c8e-81b8-a6180ada54eb | -3.29942 | -49.52879 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e69478b-7bf1-3a58-9600-81844f328403 | -4.12827 | -43.58657 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 697279b3-f2a9-30bf-a486-7d389840785d | -2.26869 | -53.76536 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93b68725-ba5c-3720-b7c4-3b2034d20821 | -4.13401 | -43.57617 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 58933073-d6dd-3eac-a1fb-59fe4437b38d | -2.42918 | -50.51328 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07fc9068-d209-3090-9650-fab2e56743fc | -2.82454 | -48.55453 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0011bb12-fbd4-3e4f-83f5-0ac94e16e74e | -3.42082 | -51.53878 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbd61314-dc53-3162-a873-a93a08c8d4d4 | -2.18458 | -48.32069 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9af7b80d-9db0-3785-ba9a-b8d8643034ed | -2.24461 | -50.41666 | 2024-11-06 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 037d9833-7594-3b96-9251-8703253d86f1 | -3.15023 | -46.49866 | 2024-11-06 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a586658-35c7-31a9-b6dc-4f69a35c3ba2 | -2.75013 | -49.13424 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4112fda1-0b83-30b6-a3b2-a2f632fd2769 | -3.83916 | -44.13645 | 2024-11-06 04:36:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a3fade5-2f11-36c2-bc49-946964eb285e | -2.44499 | -48.87128 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18855fa2-9ba4-3dd6-84e6-4f78e5242fc7 | -2.60355 | -54.54225 | 2024-11-06 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README33.md)
