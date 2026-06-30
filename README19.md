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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| faec6f4d-c29e-3077-b806-74e83262bb6c | -10.9593 | -43.0326 | 2026-06-30 06:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 46961f0a-e465-34e2-b03e-20811066976a | -10.9397 | -43.0593 | 2026-06-30 06:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 61b85448-10ac-3f3f-a151-fc7958a7f386 | -10.9209 | -43.0384 | 2026-06-30 06:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 6c0ea5bc-d5bc-36a9-ac6e-de73f1aa92ce | -10.9593 | -43.0326 | 2026-06-30 06:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 6d57cd4e-81fc-373b-b7f2-6437617d7140 | -10.9397 | -43.0593 | 2026-06-30 06:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 6fbcce7e-61ed-3e5b-8278-f7a63604ae3b | -10.9401 | -43.0355 | 2026-06-30 06:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 325.5 |
| 00c9adc1-ab78-3294-8698-98ee49e5e3d0 | -10.9401 | -43.0355 | 2026-06-30 06:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 289.7 |
| 858da5d0-3e7b-3f46-8ec6-f9a41d279c11 | -10.9397 | -43.0593 | 2026-06-30 06:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 9812b987-44df-3dd5-b67f-f308ab6a08c2 | -10.9405 | -43.0117 | 2026-06-30 06:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 166dca5b-e5a6-333e-8dc2-b27126fda970 | -10.9209 | -43.0384 | 2026-06-30 06:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| c8edf7d4-7ed4-37be-981e-c84cacff5325 | -10.9401 | -43.0355 | 2026-06-30 06:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 295.1 |
| bdf28c33-ceb1-3438-8110-8017b9339e8c | -10.9397 | -43.0593 | 2026-06-30 06:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| fa7f72e5-2554-3272-a11c-ff3cbc41d5aa | -10.9593 | -43.0326 | 2026-06-30 06:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| c388bb57-9d2b-3f4c-9e76-56b172037ea9 | -10.9405 | -43.0117 | 2026-06-30 06:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 1bdcb30f-e093-3ccd-a011-6702c7262dc4 | -10.92536 | -43.03229 | 2026-06-30 06:52:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 01ff60f3-607f-3796-a61f-7dc91fdcb936 | -12.22017 | -56.55232 | 2026-06-30 06:52:00 | AQUA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| dc62f8aa-d05c-360b-b44c-993b27f6afc8 | -12.20254 | -52.86697 | 2026-06-30 06:52:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4bab4048-a46c-3696-98d2-cb8dbe74eda6 | -7.63724 | -50.02263 | 2026-06-30 06:52:00 | AQUA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 328cbad5-838c-3776-b5fa-1bd4249b2a92 | -14.62929 | -54.45793 | 2026-06-30 06:52:00 | AQUA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5afa371e-8f53-326b-9550-2e0dd220ae0e | -7.42809 | -49.8753 | 2026-06-30 06:52:00 | AQUA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a964e471-b682-31ca-9f75-3b18b669a397 | -10.93575 | -43.03846 | 2026-06-30 06:52:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 436.8 |
| bd442045-4b57-3a91-b813-dba7ef19f547 | -12.45154 | -58.49663 | 2026-06-30 06:52:00 | AQUA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 201d4652-8fff-3d65-9216-2602bfed8c44 | -13.2625 | -56.79985 | 2026-06-30 06:52:00 | AQUA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 28c83455-7f72-3150-9930-076f40709354 | -12.21368 | -56.55779 | 2026-06-30 06:52:00 | AQUA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| b53ad0be-06d4-39ba-a670-78dfb37c6167 | -10.12726 | -52.40511 | 2026-06-30 06:52:00 | AQUA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c3ad0950-f285-36bc-a8df-b13c0342fc05 | -12.44261 | -58.47647 | 2026-06-30 06:52:00 | AQUA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 1406c3bd-cbdc-322c-a947-72096dd9b4d4 | -9.6009 | -56.91996 | 2026-06-30 06:52:00 | AQUA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 25.6 |
| db703ebf-06b2-3b63-98c5-b1572f371d68 | -12.45474 | -58.4785 | 2026-06-30 06:52:00 | AQUA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 54d30d3b-6114-3b96-a44b-da818bf9d017 | -10.93966 | -43.00545 | 2026-06-30 06:52:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 96271b15-fab1-3133-84be-c83294572651 | -12.44885 | -58.48902 | 2026-06-30 06:52:00 | AQUA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 0a5387a5-0a74-3589-922e-0814a93909cd | -11.22857 | -54.3117 | 2026-06-30 06:52:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c4631dae-1947-3dfa-a84d-d4ae2a25b81e | -11.89064 | -57.12767 | 2026-06-30 06:52:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 03e117c6-349b-379f-96a5-661c7143a694 | -10.69497 | -49.60558 | 2026-06-30 06:52:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 11209a05-ef1a-3c08-9a2b-0a6d198defda | -14.2016 | -57.42914 | 2026-06-30 06:54:00 | AQUA_M-M | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 652e81a1-aeb8-3d5a-84a9-44351fc16c78 | -10.9209 | -43.0384 | 2026-06-30 07:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| fba9bfa1-6b01-314b-a347-b7295c8b77d5 | -10.9397 | -43.0593 | 2026-06-30 07:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 82b57bf3-856f-3929-8c19-6d892784f7cf | -10.9401 | -43.0355 | 2026-06-30 07:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 293.0 |
| 4a8d474b-a482-3eae-ab67-50d1fbd6ea1d | -10.9593 | -43.0326 | 2026-06-30 07:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 4c75d0f8-0341-39fd-aae7-dde8fbedc4d9 | -10.9397 | -43.0593 | 2026-06-30 07:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 8bd62277-3736-3ca0-8e06-1fac1f017aa6 | -10.9401 | -43.0355 | 2026-06-30 07:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 295.2 |
| 52831968-0127-3026-8698-37f8ec905695 | -10.9209 | -43.0384 | 2026-06-30 07:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 20f9c1e1-80f9-3923-8548-39b61a2d35c7 | -10.9593 | -43.0326 | 2026-06-30 07:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 3449e995-3af5-33fc-968b-7c6439a565f2 | -10.9397 | -43.0593 | 2026-06-30 07:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| d2c6bcee-861f-3919-abd3-37d397dcf633 | -10.9593 | -43.0326 | 2026-06-30 07:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 49dbefc4-1169-3180-9f5b-4335d1710a0f | -10.9405 | -43.0117 | 2026-06-30 07:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| b0f3b010-1d0a-3fa6-b10a-f190b3b2b749 | -10.9401 | -43.0355 | 2026-06-30 07:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 269.6 |
| a6402aec-cb10-3b27-9cd0-179a37f07c13 | -10.9593 | -43.0326 | 2026-06-30 07:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| cb1396e4-e2f2-3e0c-9b74-0718b855129c | -10.9401 | -43.0355 | 2026-06-30 07:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 296.4 |
| e70d36a3-87aa-3cdb-a05f-5bcb28249649 | -10.9397 | -43.0593 | 2026-06-30 07:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 6cb272fc-38b4-3c56-a4a5-e2f576ce0ae9 | -10.9401 | -43.0355 | 2026-06-30 07:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 244.2 |
| 4500c2ab-e511-34c0-b599-997ece40c513 | -10.9397 | -43.0593 | 2026-06-30 07:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 82e16c54-effb-34db-a6f2-98c07ae0d8b0 | -10.9401 | -43.0355 | 2026-06-30 07:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 225.6 |
| 86aaa53c-740e-32c3-8c34-6006ef115235 | -10.9397 | -43.0593 | 2026-06-30 07:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| ff0ed073-5f77-36a0-9f09-1a284dc77b04 | -10.9397 | -43.0593 | 2026-06-30 08:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 70141c8c-00f8-35c4-8cdb-664a78f35f8e | -10.9209 | -43.0384 | 2026-06-30 08:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| b29f288f-40c4-3979-a6c7-8ed079d6bd3f | -10.9401 | -43.0355 | 2026-06-30 08:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 224.6 |
| eaa55f00-9995-3a2d-96c0-f10fe12138b1 | -10.9397 | -43.0593 | 2026-06-30 08:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 8350f55d-65a0-3e58-b00a-fd2bc443a5c8 | -10.9401 | -43.0355 | 2026-06-30 08:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 195.5 |
| b4bd5cad-ce3e-3796-b4dd-fd01492622a2 | -10.9397 | -43.0593 | 2026-06-30 08:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 3f3437ca-8824-359e-b56b-8d3f3a7f3ca6 | -10.9401 | -43.0355 | 2026-06-30 08:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 7741d099-226d-377d-ab88-0ef1cec3adca | -10.9401 | -43.0355 | 2026-06-30 08:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 162.7 |
| b44a04c4-cf35-3a2f-9efd-f6a0cb22bee4 | -10.9397 | -43.0593 | 2026-06-30 08:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| d7dffbc2-1c74-3279-bce3-8e3fd738b2a2 | -8.9989 | -45.7191 | 2026-06-30 11:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 0f756004-5eef-3fdb-85b8-cc980b5cefc4 | -8.61725 | -36.8998 | 2026-06-30 11:08:00 | TERRA_M-M | VENTUROSA | PERNAMBUCO | Brasil | 2616001 | 26 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 3788459b-a5aa-3fb1-8834-648f2eb86249 | -11.85668 | -45.50471 | 2026-06-30 11:08:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 55f76262-37a1-3ebf-a59a-90a1ad112e75 | -9.07612 | -44.73487 | 2026-06-30 11:08:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 3aa2d3ea-0f70-32f5-b961-35581bca3dce | -8.9799 | -45.7212 | 2026-06-30 11:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |
| b0196805-fb88-3eaa-95e6-a7e1b6aeff7f | -8.9989 | -45.7191 | 2026-06-30 11:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 223.2 |
| 468eb15c-1c89-3259-8a1f-f8c2c0b6ee0d | -8.943 | -45.6573 | 2026-06-30 11:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 08ef0ebd-195b-37a0-97e5-6df2811cdb54 | -13.84295 | -44.765 | 2026-06-30 11:10:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 61cc173f-042c-30c1-bb12-591f3724fdd6 | -8.9989 | -45.7191 | 2026-06-30 11:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 236.3 |
| 475373d5-902b-36f8-899c-a034f3d89821 | -8.9619 | -45.6552 | 2026-06-30 11:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 7b426523-1616-3ff4-a547-35b0a4332c3d | -8.943 | -45.6573 | 2026-06-30 11:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 30ce98c5-7ac4-3e92-9dcc-ab5dabf40176 | -8.9799 | -45.7212 | 2026-06-30 11:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 153.5 |
| d0ee6c2d-671f-394a-9e62-be15205ec13c | -17.712 | -46.7798 | 2026-06-30 11:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 21ece081-cd11-3764-ab07-0ae4e9487066 | -8.9619 | -45.6552 | 2026-06-30 11:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 111.6 |
| e7a1b077-0979-34e6-87c5-f3cc420db26e | -8.9799 | -45.7212 | 2026-06-30 11:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 156.1 |
| af98a1e3-5577-37e3-97ab-6a3293c9bcb8 | -8.943 | -45.6573 | 2026-06-30 11:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 185.0 |
| 547ca12d-6794-352d-ab1f-040ad13ce1e8 | -8.9989 | -45.7191 | 2026-06-30 11:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 288.7 |
| afd8180f-aec8-374f-90e0-a8b7748d0266 | -17.712 | -46.7798 | 2026-06-30 11:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 1f9468dc-9297-3b62-abfc-ee2f2dcedf22 | -8.943 | -45.6573 | 2026-06-30 11:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 130.1 |
| b74f1167-2720-360c-ae42-e47813644474 | -8.9989 | -45.7191 | 2026-06-30 11:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 232.4 |
| 8e97a3a2-2206-3009-b450-fdf668fb546f | -8.9799 | -45.7212 | 2026-06-30 11:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 271.8 |
| d637c9fb-ab34-3f51-818b-671934ca5c1c | -17.712 | -46.7798 | 2026-06-30 11:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 3b6b6f8a-07d4-3a68-9e40-d64bdefde7ba | -8.9619 | -45.6552 | 2026-06-30 11:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 119ed688-e0d0-38d4-b927-a0e37591aefc | -8.943 | -45.6573 | 2026-06-30 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 164.1 |
| cf8a8296-a4ce-39c1-9cf2-4b647e0c23c5 | -8.9619 | -45.6552 | 2026-06-30 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 758498a7-9b20-336d-bccc-c270effc29cd | -8.9989 | -45.7191 | 2026-06-30 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 339.5 |
| e711f03d-b77f-30b0-9a99-d9a009a6e09a | -8.9799 | -45.7212 | 2026-06-30 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 249.8 |
| c4d92ca7-3680-3a2e-bfa3-fc56c95d819b | -17.712 | -46.7798 | 2026-06-30 11:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 377af473-7365-3199-bbcc-cc6312683010 | -8.943 | -45.6573 | 2026-06-30 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 150.3 |
| f6c09ba9-dbfd-3dca-ac2d-9d9494a996f2 | -8.9619 | -45.6552 | 2026-06-30 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 2849593c-89c0-3880-a32e-bd0241c8251c | -17.712 | -46.7798 | 2026-06-30 12:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 1fe4c73e-f9ca-32d8-b437-2e5303c70b5b | -8.9799 | -45.7212 | 2026-06-30 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 279.2 |
| d720c160-55c3-38d0-b82c-14b41958c0d5 | -8.9989 | -45.7191 | 2026-06-30 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 326.9 |
| aff6efab-6659-3df0-bede-1a68ba5819a7 | -8.9985 | -45.7418 | 2026-06-30 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 117.2 |
| eb2185b0-d125-3927-adc8-3eb71533aa08 | -8.9619 | -45.6552 | 2026-06-30 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 643b1c37-2903-3bce-ae9f-669c02bbda51 | -8.9989 | -45.7191 | 2026-06-30 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 372.2 |
| fc9a3c92-8946-320d-832f-142caa99a82f | -8.9799 | -45.7212 | 2026-06-30 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 191.6 |
| 10a74cc0-3594-3c93-a52f-9e8a2e191bc2 | -8.943 | -45.6573 | 2026-06-30 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 150.6 |


[Clique aqui para ver as próximas entradas](README20.md)
