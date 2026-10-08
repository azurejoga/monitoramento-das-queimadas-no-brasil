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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97e080cb-08c9-339b-ae83-cc9506d480d3 | -1.10844 | -54.16583 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| afc530ca-ac5d-322f-bb4f-48c29a030d32 | -3.19576 | -50.5691 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9da70a8-d783-3662-8497-a38afd0b0873 | -1.10992 | -54.15653 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e58781e4-104a-346f-9906-ef5a619830cc | -1.99041 | -56.0003 | 2026-10-08 04:44:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0bb73a83-f457-33cf-b897-10ec69318a39 | -2.83401 | -48.5717 | 2026-10-08 04:44:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b64b8d6e-0928-3d56-b732-88f4039c8521 | -3.10139 | -50.31876 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a51391a1-f0d4-3c61-91f5-8f1b59067852 | -3.27962 | -50.13947 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ece2bf7-b436-37af-b7c1-65f470a66533 | 3.54429 | -51.28327 | 2026-10-08 04:44:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0a618a89-c628-3b44-8410-e1ea87a5f8a7 | -1.83124 | -54.93309 | 2026-10-08 04:44:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 96eca38c-aa68-3ec8-afee-809cb03d44ca | -2.27596 | -48.75524 | 2026-10-08 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46dfe333-30fc-3727-abf4-96b5cf245f82 | -3.1687 | -50.45601 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a1a2eb64-aec8-3f34-b023-6bb74970668f | -3.00391 | -51.12018 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6c43464-99c7-39bc-994d-b9c71b185220 | -3.27862 | -50.03713 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b684f204-cc4f-33fa-945c-26fb73925738 | -3.18904 | -49.2523 | 2026-10-08 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd0a4148-2135-31b8-90f8-0e62dcfe7714 | -3.15882 | -50.82682 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00bd0571-58ac-3c9d-a41f-52a6c6af50ac | -2.86126 | -49.54708 | 2026-10-08 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 965a02e8-a840-367c-9234-29bca9820a0b | -1.53035 | -54.54366 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 63a9cd83-b17f-3616-8be5-ff1f351f6726 | -1.12416 | -54.11596 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 031ea623-800d-3bd0-a905-61364fa2e6eb | -3.19354 | -50.56174 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9b65d5e5-5f8c-3b66-8a3a-d8e348711ef4 | -1.2669 | -55.39511 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9cd98c2-0e4d-37d9-8c36-58bb96a741ff | -1.28399 | -55.42005 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 520b3de6-53d0-36c3-b9f2-377a705f1452 | -1.50411 | -54.83875 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 934c4c04-2889-3513-8663-49dfdf4842d4 | -0.08808 | -49.48208 | 2026-10-08 04:44:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 90b52f5d-22fd-3795-90ef-822968bd5e11 | -1.60527 | -55.15897 | 2026-10-08 04:44:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1a0643e3-f28d-3034-bceb-780665ab3c67 | -3.15712 | -50.4437 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de923b9e-75dc-3d95-8c7b-3d301a9a244c | -3.19523 | -50.57253 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c998db7-0002-3762-8aff-637af4dfc920 | -1.3271 | -55.43398 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0dc49c46-9083-361a-abf1-d3931950fe0b | -3.26323 | -50.41808 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db5fae7e-d1e5-3c12-bb4b-514e55a18903 | 1.33712 | -50.83035 | 2026-10-08 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63fccfd3-071f-382c-b945-5ab7ef58212a | -1.18885 | -55.67074 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6586e9e8-48d0-3296-ac6a-832259c95315 | -3.20779 | -50.55692 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d12860f8-1840-3adb-95b3-3b3e4f5bdebb | -1.52256 | -54.51775 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 64b169a4-3494-3946-b3c3-aaf5336a4b41 | 0.53991 | -50.77697 | 2026-10-08 04:44:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e90f3a81-ad19-3ba8-ab67-df253e27a575 | -3.1703 | -50.44573 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ff732b98-19ca-3b02-aeac-5b18124d3ad2 | -1.28592 | -54.56474 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eabe79e5-f98d-3564-a434-dcfdabcdf664 | -3.172 | -50.45652 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4d80e168-766d-3186-9c39-b7793d2c8f5f | -1.71439 | -55.44257 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8774054-630b-3542-91ef-baa487407752 | -2.96976 | -51.51034 | 2026-10-08 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 229da244-6687-39a7-8e50-92a22f9efdec | -1.52458 | -54.81086 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9671e326-af23-3108-bb90-63bf75252756 | -3.1914 | -50.57545 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 426982ba-cc77-389c-87ff-ce66ddcba1a7 | -2.85793 | -49.54657 | 2026-10-08 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6a64251f-c0ef-3984-81bf-311002810d39 | -2.27161 | -47.87412 | 2026-10-08 04:44:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a063fc69-d5dc-3653-83c8-87f533342e88 | -1.1077 | -54.17046 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dc7e3acd-94c0-3916-b5d2-30a5a48eec2d | -3.18971 | -50.56466 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6433ec91-114c-36a2-bf85-e805f3b280a7 | -1.18947 | -55.66689 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d4e1679-f367-3046-87d1-355a1c9ba71d | 1.31738 | -50.8521 | 2026-10-08 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2f5de1e-c4f8-3718-89e7-d5a7470535cc | -2.10905 | -52.06859 | 2026-10-08 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af6ae115-19de-3fbe-af07-3990831e60e0 | 2.43752 | -50.81906 | 2026-10-08 04:44:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 90c71551-637c-3ae1-afcd-2548f6871429 | -1.08613 | -54.11136 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2c43d7d-e30c-313d-9e0f-5d71d92925f7 | -2.16719 | -53.66682 | 2026-10-08 04:44:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 883fd4b6-e885-3c50-97af-4ca9d053ac4e | -3.24942 | -46.96043 | 2026-10-08 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6eb399dc-0a88-3b05-a005-c17cafbc60d8 | -2.49048 | -49.41482 | 2026-10-08 04:44:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f3fa01d-dfef-3910-a0f3-acfd718fcdda | -0.59714 | -52.05727 | 2026-10-08 04:44:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6fb4cd23-a787-3a95-93b6-3ea3c7158de7 | -2.66064 | -52.57779 | 2026-10-08 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4bd24cba-0686-36c4-bf70-079d86697a04 | -1.37648 | -56.89429 | 2026-10-08 04:44:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 632f081c-f95f-3d73-a5a4-650a6dc9ae41 | -3.19238 | -50.54753 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 265d0c57-052a-3915-9dee-f93d8bb4f861 | 1.34383 | -50.82932 | 2026-10-08 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56830b98-f493-324f-a88b-53cb4b0335c8 | -1.53346 | -54.5491 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| d90d5012-7dbe-306b-9951-1525dad74e04 | -3.17191 | -50.43546 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31f48be6-7356-3254-968c-7159098e3656 | 1.63324 | -55.77813 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10ecc93f-624f-3699-9cee-07cd093ecee4 | -1.52773 | -54.8165 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 266262b4-1d96-3728-bd15-5af066b7eeb7 | -1.71848 | -55.4432 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 56ffdeb2-1585-35e3-b153-688098224a47 | -2.39889 | -51.30981 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 72ae59e4-3c36-3c0e-8e0e-1da323a3f0bc | -3.18641 | -50.56415 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80a5b44b-e582-3743-960b-563a5abb56a1 | -3.29097 | -49.12609 | 2026-10-08 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a6d6c01-e207-3092-ae77-64cf83064868 | 1.34438 | -50.83287 | 2026-10-08 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e060355d-5cbd-361f-be42-5c0820aae426 | -1.52801 | -54.81367 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1f930812-f526-3191-a3bf-97b10cc3858f | -3.17091 | -50.5932 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 8c373dc5-84df-3094-bb3e-89eb0c200e19 | -3.01356 | -51.01565 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c66449a-8bca-39ca-afbc-b4dc08edfcbb | -1.7432 | -55.02803 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0f331c6-62e2-31ae-b416-773d32c03e58 | -2.78779 | -51.66926 | 2026-10-08 04:44:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44b82ef9-890b-35bb-bcb2-1934cdad64d9 | -3.18196 | -50.54943 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2edd5d8c-0717-3b7b-b901-4f3cb2e2a494 | -3.19292 | -50.5441 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67006fe4-79c6-3afd-9ced-97b23f39e7d8 | 1.61827 | -51.06244 | 2026-10-08 04:44:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e29cb442-9d57-3ace-b09d-84786c8f7faf | -2.68616 | -49.05191 | 2026-10-08 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1f5cd001-5eb1-3438-acfa-d8c1475dc911 | -2.88101 | -51.03328 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d8048df-969b-31ed-b080-fcf38eaf2b57 | -3.18258 | -50.56707 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80e2b134-f652-35ed-befd-02e7cd409c19 | -0.99936 | -47.65897 | 2026-10-08 04:44:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 119d3d24-1464-35a3-ae3d-5d1408ec8606 | 0.95061 | -50.20377 | 2026-10-08 04:44:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 989096cc-bc63-385c-ac07-19b8ceafb815 | -3.13414 | -51.02735 | 2026-10-08 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43f87bbe-25bc-332d-bcac-a638943c5eb5 | -3.1784 | -50.54524 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32c9d10a-7704-3997-bfbc-7f800d625c3a | -1.528 | -54.53343 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 981966bc-e06b-3a06-93d6-d07cf4be5437 | -1.1001 | -54.16927 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97ab2852-40fa-3d8f-9052-1dba398d02b6 | -0.84754 | -51.8489 | 2026-10-08 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e20d493-7939-324b-9aba-a8fb34d57db0 | -1.8273 | -54.93247 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 188ee803-963b-3c9f-bea3-2c94ba8c77a3 | -1.44933 | -54.4689 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 115275a4-48ea-3b7b-a3ae-2b2f52038505 | -1.10613 | -54.15589 | 2026-10-08 04:44:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c33ff274-6ed7-378d-8ccd-21bb64168b5d | -1.18823 | -55.67461 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2281870d-78f5-3716-94cb-bada8ebf31e2 | -3.18802 | -50.55387 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| caaf8c68-3232-3fe8-b342-3468476341a6 | -1.52414 | -54.53277 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b866e473-f51a-3203-9cbf-c9e3e06469d2 | -3.13352 | -49.24026 | 2026-10-08 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1c6b94c-6506-3470-ae1e-d8f25ca9b41c | -2.56919 | -50.67782 | 2026-10-08 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 709aa99e-51ac-31e1-8aba-32dea12d4995 | -1.47461 | -54.64439 | 2026-10-08 04:44:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 63df182f-0337-3c17-a506-d5c4b28cb3a1 | -1.63053 | -55.41854 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 099d7ea5-2541-309b-91dc-fb820b55a664 | 4.43625 | -60.93018 | 2026-10-08 04:44:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f72b461-2726-346d-95ca-72e396817342 | 3.5437 | -51.27947 | 2026-10-08 04:44:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6b5e09b0-c4a7-3c40-8401-8445d5616d2b | 3.5235 | -51.2631 | 2026-10-08 04:44:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2156bf9-da8f-313c-9c8b-cbb1730b2798 | -1.33119 | -55.43469 | 2026-10-08 04:44:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ad0e809-6585-3dc2-aaee-ee6e0ed67182 | 3.6891 | -51.72664 | 2026-10-08 04:44:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ff9df48-5bc2-3f89-8dd6-d0e2a6d5f789 | 1.32797 | -50.8978 | 2026-10-08 04:44:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README76.md)
