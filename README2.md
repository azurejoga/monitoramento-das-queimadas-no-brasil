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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f78feeeb-a23b-3202-87f5-439d249ce316 | -8.1996 | -49.804001 | 2025-06-03 00:31:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ea3226f-dd32-302a-9663-1b6363a12c21 | -4.8222 | -45.2668 | 2025-06-03 00:31:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0dac9aa5-8c4c-3a29-8bad-b6cde1369e10 | -13.0144 | -43.796101 | 2025-06-03 00:31:00 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a4f3e743-5986-3f00-97d4-6116c5d1a929 | -8.909 | -50.053101 | 2025-06-03 00:31:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67963058-96d5-37b5-ae4f-2c1695739305 | -8.0881 | -43.1147 | 2025-06-03 00:31:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a5c7b14f-8517-30a6-be1b-a43ece787136 | -11.6803 | -43.781101 | 2025-06-03 00:31:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fc1f07f8-0273-3a3d-b013-37d4f4ee39f8 | -8.9141 | -48.896198 | 2025-06-03 00:31:00 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7f792f72-28ba-366f-90ef-384b03822515 | -9.6084 | -49.024502 | 2025-06-03 00:31:00 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ff1b95c2-7491-3591-b5a4-24a9e27bc2f0 | -22.136801 | -46.8293 | 2025-06-03 00:31:00 | METOP-C | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8fa7cc0e-b287-3d18-a0a1-80eddf1771fc | -13.016 | -43.803101 | 2025-06-03 00:31:00 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4dd6883d-6dab-3825-b275-1265dfc8776a | -18.8612 | -53.6105 | 2025-06-03 00:31:00 | METOP-C | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 493763c5-9f6c-34c6-b908-af3a0657be18 | -7.232 | -43.117901 | 2025-06-03 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7c8928a0-39b8-393e-a32f-f50224058a4c | -7.8735 | -45.982899 | 2025-06-03 00:31:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ba7d18e7-bb92-3ec3-a234-fdbc4d0f9eb0 | -5.9239 | -45.5271 | 2025-06-03 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f4ec344-4119-3666-bca6-80bd573d5797 | -3.0396 | -49.417702 | 2025-06-03 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47e0f6de-4b18-31f1-93a5-10c49e9b115d | -7.0875 | -46.559502 | 2025-06-03 00:31:00 | METOP-C | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f418a65-c7d6-3de8-bdd0-63d1c83386aa | -9.6064 | -49.015499 | 2025-06-03 00:31:00 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5d33fd99-c664-3793-8d9a-88b2e21eadce | -10.3645 | -48.73 | 2025-06-03 00:31:00 | METOP-C | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c653360b-eaa9-39cf-aa3c-4c25be6185df | -6.967 | -42.9123 | 2025-06-03 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0139b13d-2fe7-3bf2-9bce-0d3ef3f2fd6c | -13.6319 | -52.182999 | 2025-06-03 00:31:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d4fabf2f-50ed-3673-887e-127b723845cf | -8.0765 | -43.109299 | 2025-06-03 00:31:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7b154843-40eb-3fb2-9560-31aef0eb00b3 | -9.2013 | -49.700001 | 2025-06-03 00:31:00 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9d81ddb3-8144-3f70-a9c4-e1ea30667b72 | -9.0753 | -47.159 | 2025-06-03 00:31:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e196fe41-08ec-3ecc-87f0-3c43b8a2b79c | -13.6417 | -52.181099 | 2025-06-03 00:31:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8811ab6f-86f7-3959-9cb3-0ebebb9ba9bd | -8.9046 | -50.032902 | 2025-06-03 00:31:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 520e3b0b-f40f-381f-92b7-113daaf9df79 | -7.018 | -44.590599 | 2025-06-03 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cddcad47-9eeb-3b1f-8111-9b87cbe6240c | -6.9787 | -42.917999 | 2025-06-03 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4378a6c2-c159-3bb7-9ccb-bf2bee7c23ce | -6.9749 | -42.902 | 2025-06-03 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 69764bd0-923b-3c60-a2f3-463520485d67 | -11.5864 | -47.458199 | 2025-06-03 00:31:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d4ec5cf-a5e1-3724-a456-5c3871a7d3db | -7.0229 | -44.567101 | 2025-06-03 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54f74530-c01f-3ddf-ac60-01ebb66230b8 | -11.2516 | -49.480499 | 2025-06-03 00:31:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2b6a296a-1929-364e-97e3-25fb8d506656 | -6.7287 | -42.908401 | 2025-06-03 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2e5413fd-c886-32ad-b671-f8714ffb4b13 | -11.9121 | -47.445801 | 2025-06-03 00:31:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b6041891-2ed5-3d03-ab32-b50bb7ddb4eb | -7.8877 | -46.226799 | 2025-06-03 00:31:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 74e9c53e-e3ab-34a3-8aba-a33355175c34 | -10.2431 | -52.2187 | 2025-06-03 00:31:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ba4c7f64-4e55-36a8-8455-a02a5eb9a605 | -9.3996 | -48.442001 | 2025-06-03 00:31:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0102b043-89a1-346b-817b-07408c51b4bc | -11.2538 | -49.490601 | 2025-06-03 00:31:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 051e4697-e2e1-3ea2-a845-e9890f8f6d2a | -7.0098 | -44.599899 | 2025-06-03 00:31:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 307317fa-9c20-3a0d-97af-8d12543ebdae | -11.6819 | -43.7882 | 2025-06-03 00:31:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 055273f3-703d-3e3c-a609-111b3550840e | -7.0744 | -44.924198 | 2025-06-03 00:31:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c7dc8eb3-3478-3372-8458-16820c0e1a6e | -18.865299 | -53.635399 | 2025-06-03 00:31:00 | METOP-C | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0ac53bfe-2c7b-3c31-ae3a-b5c07d852818 | -7.0859 | -46.552502 | 2025-06-03 00:31:00 | METOP-C | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 778564c9-a15f-3e4b-8531-f57a7b873bd2 | -7.076 | -44.931099 | 2025-06-03 00:31:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 62ec5d01-cdfd-3f54-8576-67fcd92c7851 | -20.235001 | -45.719002 | 2025-06-03 00:31:00 | METOP-C | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| da682485-3be1-33b7-8547-f28dfb9ca741 | -11.2359 | -49.4903 | 2025-06-03 00:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 46.4 |
| a124fee7-1320-3d4c-85f8-742d71055015 | -11.2546 | -49.5098 | 2025-06-03 00:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 45a22b69-51e3-3717-984a-2a73569aa9a9 | -18.8679 | -53.6218 | 2025-06-03 00:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 658ba5f7-2bf3-35b0-ba18-1f9779eb0158 | -6.9791 | -42.9034 | 2025-06-03 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 1c717f03-456f-31a3-a620-e6e4f729576c | -7.2214 | -43.1153 | 2025-06-03 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.0 |
| 75923843-0fe0-3755-ad27-49d60aae6477 | -18.888 | -53.6186 | 2025-06-03 00:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 2e95474b-fce9-3e86-ab52-eecbbdee674a | -18.8875 | -53.6402 | 2025-06-03 00:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 159.2 |
| d82e2c1d-c2b5-35d4-a1e5-74a1dffa17dc | -7.2211 | -43.1388 | 2025-06-03 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.1 |
| cf92b4be-ffad-3053-b9f0-0a4d1cca6baf | -11.2549 | -49.4881 | 2025-06-03 00:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| f4fef9c6-0fb2-3985-9ddd-6204592b6f10 | -18.8675 | -53.6434 | 2025-06-03 00:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 205.6 |
| 3f13c742-5285-3df3-9b96-b3d922404647 | -7.2211 | -43.1388 | 2025-06-03 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.8 |
| 6f354a5e-9b99-3fc6-bb6f-5559d943aa8f | -11.2549 | -49.4881 | 2025-06-03 00:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 15b13c02-4481-3abd-b829-3b4019fff83e | -11.2546 | -49.5098 | 2025-06-03 00:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 54a574ed-a8c6-33ea-bc73-dbb4f41a4b63 | -7.2214 | -43.1153 | 2025-06-03 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.8 |
| 4d662f4f-c59f-3b23-a10c-cb1fff27140b | -8.9074 | -50.05 | 2025-06-03 00:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 28ba44aa-21bf-39d3-ac97-dcaf50c3ea96 | -18.88211 | -53.64806 | 2025-06-03 00:54:00 | TERRA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 60a9cd49-23ec-33c2-8057-009b21b9cfd0 | -20.71995 | -56.63993 | 2025-06-03 00:54:00 | TERRA_M-M | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 10953884-93e0-364e-81d7-1a9d835431bb | -18.86087 | -53.63896 | 2025-06-03 00:54:00 | TERRA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 07cbe5fb-f7d1-3d94-8334-aa2f4e8abae1 | -18.83634 | -47.68532 | 2025-06-03 00:54:00 | TERRA_M-M | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 468e1992-962a-3032-a115-c77cdd29126c | -20.71786 | -56.62013 | 2025-06-03 00:54:00 | TERRA_M-M | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 19.9 |
| c87fcc1e-d9fe-30d9-8a3a-a27e391ebe88 | -18.87222 | -53.64947 | 2025-06-03 00:54:00 | TERRA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 1a3bed89-9513-3683-a433-70d283b65b39 | -18.87076 | -53.63753 | 2025-06-03 00:54:00 | TERRA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 62035ece-6079-3607-aaa5-517a737a5c0e | -20.72028 | -56.63345 | 2025-06-03 00:54:00 | TERRA_M-M | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 47.5 |
| ad108cac-7816-3b3b-a6c7-1283bd225d39 | -18.88066 | -53.63621 | 2025-06-03 00:54:00 | TERRA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 25.1 |
| e8a7b786-ee65-350b-8b2a-2c3bc0d0487e | -18.34514 | -53.25209 | 2025-06-03 00:54:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 354445ca-679b-3afe-b0d4-e8ab47b8c79e | -18.86232 | -53.65091 | 2025-06-03 00:54:00 | TERRA_M-M | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 11.0 |
| fda97912-f2da-3e84-b278-c95d6ce0d647 | -14.02102 | -55.12478 | 2025-06-03 00:56:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 32.4 |
| a61f10e1-feea-306b-ad24-60244aa7e937 | -10.44871 | -47.93476 | 2025-06-03 00:56:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0c0147af-6d9c-3951-ad14-95ed6a73f456 | -13.37102 | -54.26801 | 2025-06-03 00:56:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f8e6ca37-ce37-30a9-b722-93faa123ec00 | -12.37608 | -45.92598 | 2025-06-03 00:56:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 33fa7a84-862a-397f-ad38-96cb10fc45e9 | -10.49375 | -53.65926 | 2025-06-03 00:56:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 59df7553-8c5f-3c4f-b92f-9772bde041a7 | -9.07296 | -47.16399 | 2025-06-03 00:56:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| b2dce8ed-46b0-3350-b7d5-b1d6e29fb3c4 | -10.13755 | -52.13633 | 2025-06-03 00:56:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 37.6 |
| c4f9cc4e-a2a5-3770-87af-b30efe15f210 | -12.38461 | -45.93 | 2025-06-03 00:56:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 2396cd8e-37af-3df5-88f9-d637f5e22272 | -12.37249 | -45.93226 | 2025-06-03 00:56:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 937e756b-d7b8-35bc-a2d2-ba081b8096d1 | -11.56134 | -56.42742 | 2025-06-03 00:56:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 5d8b66c6-9237-3aa2-943e-6e2b05df85b4 | -9.19597 | -49.69328 | 2025-06-03 00:56:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 36f06d1e-aa4d-3744-9e6f-bfb1c4e709c5 | -10.24313 | -52.23316 | 2025-06-03 00:56:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a06c0447-d360-3596-a384-52e3799293d8 | -9.06357 | -47.1544 | 2025-06-03 00:56:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 6d011d4b-e777-3109-b751-4e025aac1e90 | -9.39648 | -48.43451 | 2025-06-03 00:56:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| adac26fa-adb6-38a3-84bf-03629e052a3e | -11.67331 | -43.78997 | 2025-06-03 00:56:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 43.1 |
| a7693d99-c444-3771-896e-28b7fe012269 | -10.45081 | -47.94861 | 2025-06-03 00:56:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| e3bbe907-4100-304f-a800-662cd2a57a56 | -9.666 | -48.71859 | 2025-06-03 00:56:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 90f2f47b-a31e-316e-83f6-3ec31dbc0718 | -12.28309 | -50.10734 | 2025-06-03 00:56:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 02c1412b-87a4-34a4-9e4c-6d887ca8f526 | -9.19758 | -49.70411 | 2025-06-03 00:56:00 | TERRA_M-M | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 8b34d97a-5845-3e46-822b-75909c2a2834 | -14.03278 | -55.13565 | 2025-06-03 00:56:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2213d09d-1d54-3c1c-a3ea-d864f0c72665 | -11.5739 | -47.45765 | 2025-06-03 00:56:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 19e9ddf7-452f-38b0-acb4-16324b11c50a | -14.02255 | -55.13704 | 2025-06-03 00:56:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0b445860-1e8d-33a5-a786-691bac258407 | -11.55693 | -56.42027 | 2025-06-03 00:56:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 99da2ea5-dcc4-337e-b0f0-3a6b5a792efc | -11.67249 | -43.79569 | 2025-06-03 00:56:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 9bf93492-9d4f-31ef-91c5-c16bba714e09 | -12.36963 | -45.91424 | 2025-06-03 00:56:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 010d3d63-4073-3e85-b78a-aaa122eeb2cf | -11.55871 | -56.43418 | 2025-06-03 00:56:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 39.8 |
| e7784133-1330-397f-ac6e-b080073d072d | -11.41151 | -52.95329 | 2025-06-03 00:56:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 59171d78-1c5c-3d48-84ec-447ff54b6166 | -10.46156 | -47.94695 | 2025-06-03 00:56:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 0b858207-4c59-3483-a773-80e45efdc88c | -9.0753 | -47.15258 | 2025-06-03 00:56:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 2e9a36ea-db5b-36f4-8a4b-1c1e0ad7c6bc | -10.13879 | -52.14523 | 2025-06-03 00:56:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |


[Clique aqui para ver as próximas entradas](README3.md)
