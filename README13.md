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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ece280e1-271c-3c6d-ae5e-13b05870cff5 | -1.2572 | -53.3938 | 2024-11-03 01:25:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| bf28ecb1-89fe-3e50-8901-a02a05ff7d47 | -1.2755 | -53.4138 | 2024-11-03 01:25:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| d3e2bd70-cfdf-3f9c-8014-085f43dfc9bf | -1.2755 | -53.3936 | 2024-11-03 01:25:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 6e407b24-31d8-3f08-bd15-66d3aaac1c24 | -1.2756 | -53.3734 | 2024-11-03 01:25:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 273d5147-4fbe-37b7-8ef0-05587528874d | -2.1746 | -53.6834 | 2024-11-03 01:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| ca13fd19-e2e7-3b22-b1b0-6e6b856eeffe | -2.2986 | -48.8078 | 2024-11-03 01:25:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| f6eba400-45e1-3938-8816-b5171878572a | -2.2802 | -48.8082 | 2024-11-03 01:25:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 122.7 |
| ac556555-6fad-399a-984c-6d7dabed4ac9 | -2.7033 | -49.33 | 2024-11-03 01:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 8d1277ad-bb9c-3fa6-936f-d1f9d5745c03 | -2.5796 | -53.3927 | 2024-11-03 01:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 168e06dd-3ad9-3708-b1f1-e8201a88fff6 | -2.5797 | -53.3724 | 2024-11-03 01:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 379eae15-e812-3a78-b3e3-e29670698942 | -2.6321 | -48.5849 | 2024-11-03 01:25:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 57d3c7c3-12d8-33b1-852b-9554b72b67d0 | -2.6322 | -48.5634 | 2024-11-03 01:25:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 621897ef-975e-370e-9592-67e8e2cb07d3 | -2.6506 | -48.5844 | 2024-11-03 01:25:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 6978da9c-fde0-3d8f-bac7-5e4ee9730540 | -2.6507 | -48.5629 | 2024-11-03 01:25:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| cdf6ff1f-d8cb-3983-a1c6-1dfbb5c368ec | -2.7218 | -49.3295 | 2024-11-03 01:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| f5449574-004c-3d0b-8ba2-1ae86eefa13b | -2.7419 | -54.4353 | 2024-11-03 01:25:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 144.7 |
| b89ee498-c183-310c-9c47-fccf45fbb5f7 | -2.7419 | -54.4153 | 2024-11-03 01:25:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 463cedf8-1b22-3afa-ac74-54c3b5e08fc2 | -2.7602 | -54.4349 | 2024-11-03 01:25:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 203.0 |
| a2620883-938a-3c63-beca-60dd1491d7c9 | -2.7603 | -54.4149 | 2024-11-03 01:25:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 181.2 |
| 7b0465af-6d0e-36f0-80b6-f5792b514fe0 | -2.7876 | -51.6099 | 2024-11-03 01:25:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 2641ae0d-b3f1-3998-8ad4-032a1b45a84a | -3.0397 | -53.2603 | 2024-11-03 01:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 57d81652-ad9f-33bf-a9a5-411627226a1d | -3.055 | -54.1474 | 2024-11-03 01:25:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 83e5d3e4-33b7-38d8-b8a4-6a7f169e542d | -3.0734 | -54.167 | 2024-11-03 01:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 3f3173b6-ef2f-3ab3-abbf-127d0693024d | -3.0734 | -54.147 | 2024-11-03 01:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 156.2 |
| d3aaff43-2689-3470-9725-9b7d60ca86c1 | -3.0875 | -50.2901 | 2024-11-03 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 68d700b8-89ad-378a-b733-f5ec20ede49f | -3.0918 | -54.1465 | 2024-11-03 01:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| a5a1a083-d8f9-335d-b049-215a20257931 | -3.1059 | -50.3105 | 2024-11-03 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 0575bd99-75bf-33da-8c2b-e96310b8575a | -3.106 | -50.2896 | 2024-11-03 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 196.7 |
| c32ca7aa-10ee-383c-be20-2c276ee2814e | -3.1061 | -50.2686 | 2024-11-03 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 821c8045-bfd0-3298-8dc3-dfd7e7d40c10 | -3.1245 | -50.289 | 2024-11-03 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| d459bf0c-43b5-3403-afb1-dcc8b95b40d4 | -3.1245 | -50.268 | 2024-11-03 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 02ef0506-58a1-304e-a11b-cb5eee6b58ab | -3.2415 | -53.3967 | 2024-11-03 01:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 92fd245f-89a9-3b6a-8747-7d01359f287f | -3.2599 | -53.4164 | 2024-11-03 01:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| d4cf8f8c-6062-3f02-a6c3-cc0ec237155f | -3.3276 | -50.2825 | 2024-11-03 01:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 0f87e43e-156a-33d9-81d5-dc8c74ae2439 | -3.3277 | -50.2615 | 2024-11-03 01:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 43185ade-9e77-3313-8a97-3e6a72852c2c | -3.4749 | -50.3826 | 2024-11-03 01:25:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 2a63a811-367f-3c4a-a9bb-1afa7ce677d6 | -3.5466 | -50.8611 | 2024-11-03 01:25:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 13f9ea41-ef4b-3f9d-8fcd-2aa0260b26fb | -3.9473 | -48.3666 | 2024-11-03 01:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 546e585f-fb43-38be-9403-675c1736c07b | -3.9474 | -48.3451 | 2024-11-03 01:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 0861ac4a-18b6-34a3-9a0a-f17e714c450c | -3.967 | -48.15 | 2024-11-03 01:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| adff2ac3-2ffe-3e3b-9925-e30e1c0026a8 | -3.9671 | -48.1283 | 2024-11-03 01:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 8f49f021-8730-376f-8443-255882f732a8 | -4.3867 | -43.4757 | 2024-11-03 01:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 694d9b51-1bd5-3719-97ea-6892be3f31e6 | -4.3869 | -43.4525 | 2024-11-03 01:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 908a1072-5fba-3ee2-b888-9c34836cc3cb | -4.4054 | -43.4746 | 2024-11-03 01:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 264.0 |
| 79a922fc-1b77-3162-9b01-b900225cf4a0 | -4.4056 | -43.4514 | 2024-11-03 01:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 437.8 |
| 79077dcc-b4e8-34f5-a030-55c0932559e1 | -4.4058 | -43.4282 | 2024-11-03 01:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 7fc8aae3-1b21-31d7-af2f-23f8404619bb | -4.4241 | -43.4735 | 2024-11-03 01:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 223.5 |
| ed4a01fa-ff5b-302d-aad2-54bb5915cc42 | -4.4243 | -43.4503 | 2024-11-03 01:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 450.7 |
| 2a2ff5d4-ddd4-3525-bf06-c8523d8eefcd | -4.4245 | -43.4271 | 2024-11-03 01:25:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 9bb8f74f-a820-3f6b-9134-f9db712fa5f4 | -4.5715 | -46.4578 | 2024-11-03 01:25:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 57.2 |
| c1c5303e-4eef-3aae-af73-74aab4e7cd42 | -6.5239 | -41.4929 | 2024-11-03 01:25:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 59.4 |
| 8db471dc-0f73-3f33-abbb-4f9d20b198dd | -11.2819 | -56.144 | 2024-11-03 01:26:10 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 94cdaf95-31c7-3813-975d-69634c3e7fe4 | -17.64698 | -57.48874 | 2024-11-03 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| ee612fb4-cb92-3b80-873e-8b0fbe3e1e6e | -17.63902 | -57.50027 | 2024-11-03 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 6dc09aed-7261-3def-9ba2-395c63b87c2b | -17.6377 | -57.49007 | 2024-11-03 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 34323dd6-01cd-3519-a278-a148dec610e6 | -17.28279 | -57.51367 | 2024-11-03 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 789b9392-d474-3c7c-bec8-d066df990ff3 | -17.28147 | -57.50355 | 2024-11-03 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 305b20d0-2bd5-382b-adde-3418cb413e4a | -8.7203 | -48.0139 | 2024-11-03 01:32:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| fc789615-c1c7-3085-b699-a77b48270a95 | -8.71145 | -48.00873 | 2024-11-03 01:32:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| a3a261f0-135a-3e43-b37a-d7ee47ea8a3a | -14.59038 | -57.11431 | 2024-11-03 01:32:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0993bd6d-0e05-37ac-954a-a3c56e0ad209 | -14.58911 | -57.105 | 2024-11-03 01:32:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0253aeb9-427f-3fae-849f-adef9452864a | -13.37077 | -61.31599 | 2024-11-03 01:32:00 | TERRA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 83c01d07-308c-3ad5-bba5-2cebc209283a | -11.50691 | -54.84561 | 2024-11-03 01:32:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 14030cc9-25e1-3e55-92cc-89facf709bdf | -11.4922 | -59.12568 | 2024-11-03 01:32:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3b8ab9e9-5e76-34f3-8e1e-1c5d02e7a1a8 | -11.28731 | -56.14211 | 2024-11-03 01:32:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| de16d7ca-c5a3-38b1-b184-ec5937465f25 | -11.2797 | -56.15256 | 2024-11-03 01:32:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 1c6fc5c5-fd94-3260-b969-f1de1fefa66a | -11.27841 | -56.14345 | 2024-11-03 01:32:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 2571d12d-a9e2-3853-a17b-160dbd8fe45a | 2.55379 | -51.08762 | 2024-11-03 01:34:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 40f6a275-42a9-3c9b-9b86-ed712222f083 | 2.54948 | -51.11812 | 2024-11-03 01:34:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 482d334e-aa5b-37d4-b3db-340c0e5b7efc | 2.54945 | -51.09393 | 2024-11-03 01:34:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 613b3f08-f12f-3341-ba66-fe0a733f5a79 | 2.54537 | -51.12444 | 2024-11-03 01:34:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 6a2089cf-e436-348a-b652-d0e528528c02 | 1.1976 | -59.97575 | 2024-11-03 01:34:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 724c64d9-c7b4-3923-8577-98fc9b33192d | 1.12601 | -59.4399 | 2024-11-03 01:34:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 227202d1-bd19-3941-a135-f6bbb57e0731 | 1.11896 | -59.55516 | 2024-11-03 01:34:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 79fbb05a-72c9-3f98-8d97-d1b26791e16d | -4.53832 | -56.1346 | 2024-11-03 01:34:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| eef2ae2b-8950-34d6-95aa-b0df83174eac | -4.53685 | -56.12434 | 2024-11-03 01:34:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| af1542f2-47d4-3140-8c4a-4f3173b46df2 | -4.33782 | -55.3163 | 2024-11-03 01:34:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a36c9193-2787-3860-8b0b-f5df8e6b68fa | -4.27223 | -55.14733 | 2024-11-03 01:34:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f7e1719f-4d9c-3d21-9ebd-1082f51ecc6c | -4.24342 | -55.87104 | 2024-11-03 01:34:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| fabbe6fd-2c44-3499-b94c-b2d4f8cc0bc3 | -4.24193 | -55.86061 | 2024-11-03 01:34:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5c036291-f671-38f6-a11e-d1a5276e3f29 | -4.07401 | -55.54238 | 2024-11-03 01:34:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7b7b3b8e-627a-3693-9a5b-b49ac44f9792 | -4.06422 | -55.54375 | 2024-11-03 01:34:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| d86e646f-c7c9-3ed6-a578-256b346ab211 | -4.01733 | -54.79678 | 2024-11-03 01:34:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9ec7d1e3-68f0-3aa0-9793-93783eea9694 | -3.94723 | -48.37951 | 2024-11-03 01:34:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 2e86ce50-3fbc-336c-a17d-18999eaee36d | -3.94124 | -48.34116 | 2024-11-03 01:34:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| a7437b60-8b7c-3b63-9b8e-0bb57f01a33c | -3.93884 | -48.34639 | 2024-11-03 01:34:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 08e26f77-8d61-3af7-8bd3-0d83efa54400 | -3.86169 | -55.98335 | 2024-11-03 01:34:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1be3ac17-9ce7-3385-b4f2-9b94adee7eab | -3.79943 | -55.64051 | 2024-11-03 01:34:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 5c5f10df-6acc-3124-8f1c-efde6bacb680 | -3.73933 | -54.06525 | 2024-11-03 01:34:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 2f28f3a0-6cf5-3e27-ba86-5bf0c0a47959 | -3.64847 | -50.18966 | 2024-11-03 01:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 3d9065d0-39e2-3f90-9ea1-9fbdcb334c81 | -3.64694 | -50.18446 | 2024-11-03 01:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| fa88f8c6-cdf2-3102-8238-aa623cd0c00e | -3.64434 | -50.16162 | 2024-11-03 01:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 19265f3b-14ff-328c-a360-3702f7e2fb2e | -3.64258 | -50.15631 | 2024-11-03 01:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 97865409-71dc-3c50-959f-ef3fd66d5790 | -3.62733 | -53.52912 | 2024-11-03 01:34:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 7640b97a-1f40-36d6-ac25-7ecec3d70acc | -3.60999 | -49.31285 | 2024-11-03 01:34:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 9ad02448-4868-3495-89a3-3f8f99f31c93 | -3.60742 | -49.3405 | 2024-11-03 01:34:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 14185dc9-bc3f-3596-9b7e-9e75a6daf96e | -3.58359 | -54.56446 | 2024-11-03 01:34:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1049221c-e133-30cc-a17f-cdeae755d8dd | -3.5633 | -54.6458 | 2024-11-03 01:34:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 2699bf97-7d89-368d-976e-a7d528b2f4d2 | -3.56128 | -54.59973 | 2024-11-03 01:34:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c67e5b90-f125-3258-bd33-f8f2a200c6d3 | -3.55573 | -54.59476 | 2024-11-03 01:34:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |


[Clique aqui para ver as próximas entradas](README14.md)
