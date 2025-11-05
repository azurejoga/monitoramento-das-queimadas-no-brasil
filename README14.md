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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8130b13a-9782-3031-99a2-d6221b536fe3 | -6.12573 | -41.69769 | 2025-11-05 03:51:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d5061f07-bbf9-3b19-bed0-269a7973b017 | -8.96835 | -44.1121 | 2025-11-05 03:51:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0185ee22-f666-39ec-84fb-a13b743d7463 | -4.04507 | -43.48172 | 2025-11-05 03:51:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 859e41dd-5198-34d8-8fd9-f6285bc3e56e | -7.23878 | -45.70149 | 2025-11-05 03:51:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4522e8ea-c0da-3602-848d-ae4c1bbe40bf | -4.58355 | -43.3396 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 71eb1b61-619e-37f2-bcf0-bb9a92c49f03 | -4.30312 | -43.78533 | 2025-11-05 03:51:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9e769cb4-c977-3a27-a42d-1cec01d7a8cb | -4.25048 | -48.58407 | 2025-11-05 03:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f31f9b9d-2062-310c-ab18-f924a18238dd | -3.67078 | -44.80225 | 2025-11-05 03:51:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05783d17-a62c-378f-9e8b-2ed09b484a53 | -5.89066 | -42.91765 | 2025-11-05 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 9ab1e18a-9f0e-3d21-bce5-9ee3b94f9f99 | -5.2426 | -48.50776 | 2025-11-05 03:51:00 | NPP-375D | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 88732030-f2da-3e65-88ee-f305ca4123d2 | -7.28434 | -45.45404 | 2025-11-05 03:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 34790b46-c6ed-385b-b1ec-74f9f18709b1 | -3.23974 | -46.8765 | 2025-11-05 03:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1e8b255e-c8bd-347f-95f0-bdb629f75bd5 | -6.2087 | -43.26803 | 2025-11-05 03:51:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 969e5982-64a5-360c-8770-a05bbbe86b46 | -3.22875 | -43.44634 | 2025-11-05 03:51:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 44b329aa-01d3-366b-8134-25c2b8774c6c | -8.59421 | -44.15621 | 2025-11-05 03:51:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 778f4090-fa22-3df9-a1f2-841d3ae50c3c | -5.0639 | -45.47687 | 2025-11-05 03:51:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a79acb92-cb08-3edd-9b47-85b7da9833b5 | -2.98585 | -48.70548 | 2025-11-05 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9a505938-c93d-392f-84ad-754ac2b5f387 | -6.10668 | -41.71235 | 2025-11-05 03:51:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8ed9739c-2326-3873-ba61-c5b8e89cde5c | -5.47205 | -43.57829 | 2025-11-05 03:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4e0635f3-4013-3700-a0a1-c62c41707f5f | -5.34793 | -45.17163 | 2025-11-05 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9ba5339-8996-3385-ac1e-d3a43bd6db4c | -4.86413 | -44.6226 | 2025-11-05 03:51:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| aedaac7c-62ff-3f1a-bb4c-34e8ec7f9f34 | -4.15498 | -46.79616 | 2025-11-05 03:51:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88c76876-c08c-3355-b483-ee79e449afdb | -2.97814 | -48.71008 | 2025-11-05 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 13adb4ce-2907-3433-93c0-0e3d477d7040 | -6.12952 | -41.62661 | 2025-11-05 03:51:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a0ad1fc6-2055-347c-be04-424550443910 | -5.10904 | -46.22467 | 2025-11-05 03:51:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8274d88c-1dbf-331c-b6cf-e7ea76b25c1d | -3.49365 | -43.62339 | 2025-11-05 03:51:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b21af619-c8dc-3632-946e-1925e550f71c | -4.30549 | -45.37019 | 2025-11-05 03:51:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfe06af4-f735-3e29-930d-3cf0182ff4de | -6.37305 | -42.40347 | 2025-11-05 03:51:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 927e8169-062e-36c9-8cf4-03b5d1ead6e7 | -4.86297 | -44.62325 | 2025-11-05 03:51:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3139d151-96b8-34f0-89b1-000bcfbc1212 | -3.23062 | -43.43827 | 2025-11-05 03:51:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ea05c722-ace9-3d56-9b88-914593c491d3 | -7.32996 | -38.85126 | 2025-11-05 03:51:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| bc0eb9f8-6ea1-3a60-8980-4389f3bc3a95 | -4.1001 | -47.28252 | 2025-11-05 03:51:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34d0a075-8244-3c7d-90c1-15e4261e6441 | -2.97917 | -48.70415 | 2025-11-05 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| da9cf462-07f1-3a7d-aab1-cc84bc326ead | -4.60731 | -42.85423 | 2025-11-05 03:51:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d864a7b4-c526-30a7-9d7f-848525ad4e21 | -4.50289 | -45.43991 | 2025-11-05 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ebca342-2a44-33c1-b391-ade835800000 | -4.82146 | -45.76414 | 2025-11-05 03:51:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bb27aff-36e0-30c5-9e5d-1a978c6d0cfa | -5.26571 | -44.81221 | 2025-11-05 03:51:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 704dda35-09b3-3ca5-8375-c96af9b3f795 | -8.22526 | -49.98806 | 2025-11-05 03:51:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0158f9e9-ed83-3e56-9a46-d0cd7a23218b | -4.51194 | -45.43607 | 2025-11-05 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a6bc970-04c3-30e7-a20e-f69d6da41de0 | -6.26819 | -42.56826 | 2025-11-05 03:51:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4b976a16-f89b-3456-bf6b-7f15318e1694 | -3.6713 | -44.79917 | 2025-11-05 03:51:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94b83c9f-55f3-38ec-b391-74260fc178b5 | -2.84842 | -49.40814 | 2025-11-05 03:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a7086541-0366-33e6-9210-47c9386ad68a | -6.10444 | -41.70116 | 2025-11-05 03:51:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e4870f13-cba7-348f-a24e-a233c6231134 | -4.18528 | -46.41552 | 2025-11-05 03:51:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf37ff1f-24e9-33c8-8545-b81f6e0133fd | -2.83355 | -49.42242 | 2025-11-05 03:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 68d2bce3-c7bb-34a7-be70-0901b59e9d79 | -2.64897 | -48.51543 | 2025-11-05 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 39c1c092-99af-3576-84ff-f3e2659caa29 | -4.46271 | -43.22004 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e438b717-7a20-3f6f-b4ea-3a41eb92ba86 | -7.68468 | -40.86577 | 2025-11-05 03:51:00 | NPP-375D | CARIDADE DO PIAUÍ | PIAUÍ | Brasil | 2202554 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bae46c6b-7d82-3c50-a5c3-a4e63aa7dd7b | -6.43128 | -43.07022 | 2025-11-05 03:51:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 82a744a9-4ba9-31cd-aa26-7a220a4c057a | -8.30933 | -49.65619 | 2025-11-05 03:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72368f1b-76a5-3a7d-99f3-4b73771a17ac | -8.09142 | -42.94877 | 2025-11-05 03:51:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 94c448b7-ec27-308c-9ae8-905096fa6a7e | -7.05908 | -38.96972 | 2025-11-05 03:51:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 96deb451-1ea0-36a4-925a-30f3dcc2bad3 | -7.33203 | -38.85464 | 2025-11-05 03:51:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 786cc334-df87-345a-9a38-5b2a8543c5cb | -6.70057 | -39.68695 | 2025-11-05 03:51:00 | NPP-375D | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8ea8d358-5ebb-37cc-8db1-4d8a235e0e2b | -8.05864 | -49.63844 | 2025-11-05 03:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8075384b-6c0b-3859-ba21-82b24f4ee86a | -7.72657 | -46.5915 | 2025-11-05 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ff7f042-4124-3bb4-9def-4c617a926575 | -6.03933 | -41.04449 | 2025-11-05 03:51:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e2125880-93ae-38dc-bba7-faff2cc4fc28 | -3.67025 | -42.37672 | 2025-11-05 03:51:00 | NPP-375D | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1a2975e5-7162-3c8a-9a69-8e26222e5801 | -5.47937 | -43.58108 | 2025-11-05 03:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| bbb0234e-9904-3983-a390-5b28324b8025 | -4.59752 | -45.62604 | 2025-11-05 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a22c28a-8527-3f73-9cfb-35e3d9a5e3d2 | -3.06712 | -47.77612 | 2025-11-05 03:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59723092-1429-31ec-91d7-548e0e426eaa | -4.47028 | -43.2309 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 8c707e37-c272-316a-a2c9-2e8c0f16aab3 | -6.4778 | -35.25307 | 2025-11-05 03:51:00 | NPP-375D | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 93fdf371-1209-3e9e-8611-a495606d4faf | -5.7779 | -40.80467 | 2025-11-05 03:51:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a5c72551-a576-3530-900f-1a877eb436b8 | -2.39769 | -47.14747 | 2025-11-05 03:51:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 029482c1-11a0-3757-848d-d20a19cebb61 | -4.45463 | -43.21684 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 3986be45-0b6c-3bd4-af5d-1a100f210809 | -3.48238 | -43.63213 | 2025-11-05 03:51:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f56e9304-8f6a-3965-bb2f-d6543d3e2051 | -4.45275 | -43.22317 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 17f33645-6d54-327f-8a8a-ec112df12ed1 | -3.47588 | -43.64172 | 2025-11-05 03:51:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4edc3934-a989-3159-8d4b-c0f78af74f62 | -3.47194 | -43.63577 | 2025-11-05 03:51:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5f5f4a26-1123-3434-9d63-1157221f6030 | -3.22121 | -44.40442 | 2025-11-05 03:51:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a75bd737-863d-352b-b53b-f4b2519afa53 | -7.07566 | -41.58218 | 2025-11-05 03:51:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 750a3167-3582-3cc4-8ddd-407afa7bb202 | -3.13732 | -40.98903 | 2025-11-05 03:51:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c1dd95b0-b8cd-39ba-b2cb-c37e8e75163c | -6.07835 | -41.7803 | 2025-11-05 03:51:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d5c853d1-d781-33d3-8044-2183e0efcd2e | -5.03484 | -43.61839 | 2025-11-05 03:51:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c8cf8848-d30a-36c0-b8b2-54f521897fa6 | -6.09976 | -41.70038 | 2025-11-05 03:51:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 17835184-5c8e-3c77-8f4a-9394da3e828f | -6.12491 | -41.62954 | 2025-11-05 03:51:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e9b7af25-cf83-3022-864b-390036f7339f | -7.04065 | -41.45385 | 2025-11-05 03:51:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d351dc37-7730-3899-a06e-b8ad5a89e51a | -4.42054 | -48.9451 | 2025-11-05 03:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e407e1b1-dd5a-30c5-b46a-566e59728f12 | -4.90042 | -46.8559 | 2025-11-05 03:51:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0534d9cb-c511-3f4d-b204-bf595cf9dd65 | -7.96898 | -43.23571 | 2025-11-05 03:51:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 0cbb1160-0240-3a31-bc81-91c616509e56 | -5.45779 | -45.40547 | 2025-11-05 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| d5d17b62-9f03-347e-b552-d99ab593dea6 | -3.49281 | -43.62853 | 2025-11-05 03:51:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f82207ef-c7c2-3a78-a7af-83361adba4e5 | -4.55256 | -45.58408 | 2025-11-05 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59590261-6bbe-3bcd-8dba-72e28269f1fb | -5.4802 | -43.57627 | 2025-11-05 03:51:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| a0f8cea9-f17d-303a-a5ba-fd55d58db283 | -3.24046 | -46.87229 | 2025-11-05 03:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 19e36870-54a3-3358-bf8a-a14d186e58bc | -3.22678 | -44.40228 | 2025-11-05 03:51:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c41e0aa-e037-3604-9fdf-31bd16848b22 | -3.6599 | -44.8036 | 2025-11-05 03:51:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8a819e6-465d-3b38-969c-436506302415 | -4.47565 | -43.22701 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| ccb23c37-baf5-364a-aab5-1b4c7ad7eb3a | -3.48803 | -43.62772 | 2025-11-05 03:51:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| bf15bfae-5b28-34bf-9c97-de0ce18eb87c | -6.07626 | -43.25148 | 2025-11-05 03:51:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 6da6c4fe-f6e9-3270-8969-249dac1bf25d | -6.73838 | -44.14663 | 2025-11-05 03:51:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 3ac82b4c-42a7-3263-9fd7-1ea6f3a3730f | -4.61023 | -42.85287 | 2025-11-05 03:51:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c6f1838-07d5-32df-ac38-316db4ce4863 | -3.33719 | -44.35593 | 2025-11-05 03:51:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 444662bd-f304-3535-9fe4-4f728fc7a446 | -3.22977 | -43.44329 | 2025-11-05 03:51:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 25fa814e-0974-33b9-ad0b-f852b0920651 | -5.24217 | -48.50716 | 2025-11-05 03:51:00 | NPP-375D | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7fa8da08-e3cc-37f1-9530-9461672ddc85 | -2.42252 | -49.29745 | 2025-11-05 03:51:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 99cd03b8-e6df-3df2-b6de-b5b2f091b358 | -6.04552 | -42.71567 | 2025-11-05 03:51:00 | NPP-375D | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4f5538aa-db65-3973-a59b-80dff981d511 | -4.58817 | -43.34033 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c014231-a086-366a-957d-69230e377239 | -4.45892 | -43.21461 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |


[Clique aqui para ver as próximas entradas](README15.md)
