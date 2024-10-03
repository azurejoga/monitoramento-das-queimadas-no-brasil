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

## Dados Diários - Página 186

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7cb95e48-efa3-3f1b-a756-00f30aac9a58 | -9.16708 | -61.67077 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 16b576a8-6879-33f0-be16-ecf6af87f1b5 | -9.16709 | -61.66566 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7d1de68a-835c-3a04-9f12-22c733f23bc5 | -9.16763 | -61.66655 | 2024-10-03 06:08:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f0c75106-4155-346a-b52c-7ae50d4f3d76 | -7.75714 | -61.12639 | 2024-10-03 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01f85938-2251-3ca5-89f2-e28f268cfbd9 | -7.75769 | -61.12211 | 2024-10-03 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3af2f3e-40eb-3aaf-bcb9-61be933fd9cd | -7.90093 | -61.47768 | 2024-10-03 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b648da09-159a-3051-9c41-d6e0be94e73c | -7.9011 | -61.47823 | 2024-10-03 06:08:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ce84171-55d0-35ef-bb9d-38316138aacc | -10.37814 | -61.21797 | 2024-10-03 06:08:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 771a6991-d81b-3962-bce2-90f6cd5b3b8c | -10.3782 | -61.21295 | 2024-10-03 06:08:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c5c1dbce-b290-321f-a865-eb1275938ff3 | -10.37869 | -61.21325 | 2024-10-03 06:08:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bc1e95ef-b36d-32c9-b0c9-74b4dee862e4 | -10.38434 | -61.21356 | 2024-10-03 06:08:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b42df6d6-36bf-3493-b8fe-66ee24735870 | -10.38483 | -61.21387 | 2024-10-03 06:08:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26f4c0ae-bd85-3faa-bfc4-899c85de823d | -9.38603 | -61.05571 | 2024-10-03 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b68e3e8c-02e3-31c4-a481-c14b5b2cc7d9 | -9.38663 | -61.05092 | 2024-10-03 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 90e317c4-1990-34cb-889f-895aa390b3ce | -9.39213 | -61.05656 | 2024-10-03 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0a530b61-60a0-3b42-9ae0-8861c3578c50 | -9.39272 | -61.0518 | 2024-10-03 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d823934a-0e90-3888-8bf4-dd2a5c6875fc | -9.39331 | -61.04709 | 2024-10-03 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2a8f9d0-3ac2-32cc-80ca-497a82308126 | -9.77553 | -60.4757 | 2024-10-03 06:08:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47196911-99a4-30bf-8480-b147ff46a95a | -9.78187 | -60.4766 | 2024-10-03 06:08:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 873e5790-42e6-3a47-9cbd-62e71dce4182 | -9.78822 | -60.47753 | 2024-10-03 06:08:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b174603-6bd0-37ce-aa80-13d7277202a8 | -6.64721 | -60.04749 | 2024-10-03 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5267ef8d-ed43-38aa-8994-3ee18fed0bd6 | -6.70752 | -59.13182 | 2024-10-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 284ede5c-7e48-3d7c-965f-d4a5fa53bf4e | -6.70972 | -59.13271 | 2024-10-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| aa05af06-b50c-3113-944e-ac72111ea996 | -6.71418 | -59.13258 | 2024-10-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 25e46816-57a4-3657-8b37-f8de95a961a0 | -6.71491 | -59.12681 | 2024-10-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c42834ef-373b-3d09-9fbb-89a2cec32197 | -6.71637 | -59.13348 | 2024-10-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1c328fe5-b4f9-3ca3-a44f-8759356c1ab8 | -6.71715 | -59.1277 | 2024-10-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e12f2fc0-94f0-32c4-904d-e3ccb7cdd9c3 | -7.01936 | -59.38747 | 2024-10-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8c22c40-4550-39c1-b512-1753a0658669 | -7.02011 | -59.38167 | 2024-10-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d735fb3e-bf7d-3a6e-aae4-05bbe8d17275 | -7.02073 | -59.38277 | 2024-10-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b11fa305-5e39-3f26-ae74-ae90ebd7be54 | -7.19817 | -59.79772 | 2024-10-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6305e7ec-f184-390e-bed0-1efaa3f569ed | -7.19884 | -59.79255 | 2024-10-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3041def1-3371-3abc-b8b1-3871347c6059 | -9.46295 | -58.9762 | 2024-10-03 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 26545667-4f35-30ae-a05f-82057c8013bf | -9.16808 | -59.38358 | 2024-10-03 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bfd3fba6-98d1-300a-8e45-67e847b31279 | -9.16957 | -59.37129 | 2024-10-03 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f84cc927-7e53-3885-9504-1e7f6d12e31c | -6.8712 | -59.05201 | 2024-10-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99845811-11d5-3e77-b196-d596ae34f27f | -6.87271 | -59.04035 | 2024-10-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 377bd259-9771-394b-bf4f-517f2c9f61df | -6.87346 | -59.03459 | 2024-10-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbebc798-46a2-3baf-ba54-07bd456dcecc | -6.87787 | -59.05298 | 2024-10-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0587ca2-d9f7-33a7-a0b1-c4ca1a33723f | -6.87863 | -59.04715 | 2024-10-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 418b2916-5041-3c8b-9631-9716612ca98a | -6.87938 | -59.04135 | 2024-10-03 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79b5b800-2faa-3756-8860-c8429f46fe2e | -9.32649 | -68.75763 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb80d1d6-a516-3daa-8e99-f23850e1bee5 | -9.35298 | -68.90981 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7e7239d-2090-3ec6-9823-7bc1ce2b2e40 | -9.35361 | -68.90549 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db18f0d6-025f-3ffe-98b1-4cb2194cb190 | -9.35434 | -68.79737 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1629b8c6-ecdd-31c8-945a-8f1bfce89e77 | -9.35801 | -68.79793 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f166f3a1-d056-315e-9ab3-b6ad627efa69 | -9.35817 | -68.7958 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7c9f7b5a-b4eb-39e6-a394-119aeed11eae | -9.36167 | -68.79848 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6adf4533-cece-3a1d-a567-f33535dae4fd | -9.36184 | -68.79634 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e8ef5b69-b0ee-3d1b-bf3b-7c4eea42d53f | -9.36533 | -68.79906 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c81d9fd5-54ad-3c62-a418-31d9f4bd979d | -9.3655 | -68.79691 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 135f7335-366f-31de-b2a9-12ef250e826a | -9.36598 | -68.7947 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8fbf4801-9574-3834-9a5c-2a50ae299179 | -9.36667 | -68.81485 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff01a314-fffb-3181-b680-42de76db40b0 | -9.37554 | -68.3444 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f08baaec-4bab-347e-a774-9475008df99d | -9.38065 | -68.33572 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7257519a-9788-3a25-9d85-54e878547015 | -9.38132 | -68.33109 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ca54db10-0b73-3c0f-b58f-6da1954fbaf0 | -9.38306 | -68.34551 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7584d33b-63f4-3bcb-9842-7bd24cf4fd14 | -9.38374 | -68.34089 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c80d792-78b2-31a3-9fdc-e852de91dfee | -9.38413 | -68.87489 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de64ab41-a8dd-3a0e-bd84-dc6b055dc3bb | -9.38441 | -68.33627 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98d8395c-c51b-3b23-ba13-81b140855ac1 | -9.38508 | -68.33165 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 14.5 |
| e9fbce8f-6242-344d-ad11-f0661a1b90f6 | -9.38801 | -68.82251 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41e3063f-caf9-3cff-b474-7faa6e17c861 | -9.39194 | -68.33736 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d0a52f80-56ab-3e9b-b3dc-a93d625c2bf8 | -9.39208 | -68.25703 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0fc604e8-2ed3-3429-8fea-def86d8d4dc8 | -9.39289 | -68.30447 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33cd1fc1-c925-3ec0-88b6-c4c8c9a2308a | -9.39519 | -68.26226 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58326c80-1cbf-3a62-9868-6e4ca9e2d56a | -9.3957 | -68.33791 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3e465652-9125-3de0-bd8d-9732f8a28371 | -9.39586 | -68.25762 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47c83a52-760b-3e97-be0d-7405d2492bdb | -9.39638 | -68.33328 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e855f5e9-2beb-3af9-aae2-711e6d43414e | -9.39654 | -68.25297 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f013b13-24e2-32cd-893d-2ce2da8c264b | -9.39666 | -68.30503 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5afe5611-56dd-3efb-830a-dd861e25feaf | -9.39896 | -68.26282 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8ca3e97-db13-328d-bde6-025d94da40d0 | -9.39944 | -68.15275 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38137fe0-cb45-3724-8dbd-26fed3449790 | -9.51432 | -67.43602 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e141c3f-5385-3f8a-b41c-5fc7139a3245 | -9.8982 | -67.33696 | 2024-10-03 06:08:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9d9ac322-4325-3439-9df1-0c5b47a6a93a | -9.89769 | -67.34052 | 2024-10-03 06:08:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3f685ed3-0f7b-3a87-b1f3-1db413ff2d44 | -9.62537 | -67.47304 | 2024-10-03 06:08:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 47e4f647-ef1b-3cfa-b3e3-74f983e6970e | -9.62587 | -67.46957 | 2024-10-03 06:08:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| eac64c01-d80c-3552-9123-e632074d654a | -9.62935 | -67.47365 | 2024-10-03 06:08:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f20db90b-2ea3-3a9d-bb0c-3eda6e2bb11f | -9.62984 | -67.4702 | 2024-10-03 06:08:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 268140f2-243e-313b-a188-aee816a8651a | -9.63034 | -67.46671 | 2024-10-03 06:08:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aebe528b-d500-3287-8d51-8a3da06fe952 | -9.63084 | -67.46323 | 2024-10-03 06:08:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b08a5db9-54e6-3d7e-b854-e0ea102900fb | -9.63433 | -68.64473 | 2024-10-03 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e5d8917-d265-37b2-bfcc-1561971b952d | -9.63562 | -68.63583 | 2024-10-03 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ab628dc6-9f4b-37c6-a4c6-76269f949454 | -9.64674 | -68.63754 | 2024-10-03 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3c2ce0db-c7b3-329f-b636-bad10410c95b | -9.67382 | -68.813 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3fdb41a-8b15-3df3-9499-9bc11a9657c7 | -9.68182 | -68.80973 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8be450d-770b-38f9-a01f-b73f25e53329 | -9.68248 | -68.80532 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffb77686-f5ed-3c89-8a06-cb75e4d363b6 | -9.73321 | -68.43764 | 2024-10-03 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fd408014-f136-35ce-9b20-f1e15e7f30a8 | -9.73389 | -68.43305 | 2024-10-03 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b7c041b-d1d8-31f9-867c-58d18436fb2e | -9.73813 | -68.43579 | 2024-10-03 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 08d2991c-7fb8-3905-ace2-998bcc2aca97 | -9.73901 | -68.42442 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1f3f7031-bfed-3c74-b9b9-1e441d9931dd | -9.74277 | -68.42497 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 01da8b50-c470-394b-9563-b7ee62ee0a73 | -9.74653 | -68.42552 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fbef4d48-f300-3b27-80c7-4a2bb8394f38 | -9.41651 | -68.2748 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20de26a0-6060-3fd4-be82-b8e89556fcad | -9.43225 | -68.59552 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ce87604-3da8-32e8-8fdb-cc08125dfd25 | -9.43595 | -68.59609 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1fc08734-3648-31f4-a1e3-d06be3ec3d7e | -9.43954 | -68.33215 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e556fe03-3670-3a44-bb31-8891bbe8f655 | -9.44571 | -68.2602 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b40b8fc3-5259-39e6-be4f-09c2b18619af | -9.44629 | -68.25745 | 2024-10-03 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README187.md)
