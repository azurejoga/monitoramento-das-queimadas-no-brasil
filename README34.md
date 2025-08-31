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
| 3d27225d-636a-3463-8874-eed6cb7769fc | -7.88748 | -45.17233 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d07c698-739e-3f4d-9129-ed554c28655a | -7.58602 | -42.71516 | 2025-08-31 04:27:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8b0a1b27-6705-3175-ad8a-742d0fa88fd3 | -6.29819 | -43.54519 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe1c44f3-39a8-3ead-a985-b58e4fed7356 | -6.27987 | -43.54673 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d673d37-bcfb-37db-b969-93d2ed0fa778 | -7.40561 | -49.51345 | 2025-08-31 04:27:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc38c110-8dae-3605-991b-6e65d3b0547c | -6.21717 | -42.76582 | 2025-08-31 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| db1f169a-4a7a-34da-aafc-bf07adb22434 | -5.58502 | -46.32763 | 2025-08-31 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5a713b0-7698-37fb-91c0-a7f4425bfa48 | -7.19401 | -43.71257 | 2025-08-31 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb3f2e64-5b83-319e-b19a-24f48c46c8ad | -6.81821 | -43.3422 | 2025-08-31 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8e2226da-5c6f-3525-a907-aa4c786796a6 | -5.48209 | -44.39839 | 2025-08-31 04:27:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4c2e06d6-11b8-33c2-8b40-a9be3c094367 | -6.17156 | -43.9965 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f38985ae-af36-36f8-9fb2-a1770e6586f8 | -5.80158 | -43.86821 | 2025-08-31 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b19c1dda-2981-3d8f-8ebd-a71324b3fd8e | -6.33796 | -53.43503 | 2025-08-31 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f4afc8f0-8fcc-3055-afcb-b3eb21211982 | -6.53981 | -44.43789 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7765c961-df95-3803-9ae4-3e0570e7bdb9 | -5.80793 | -43.87309 | 2025-08-31 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bdad81f8-74c1-398a-9f10-ecbd82b0adfe | -6.50619 | -43.55098 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5554212e-35ed-3ef5-859d-667893e3ffe9 | -8.29375 | -46.31089 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bbba204c-99bd-3b3c-af0b-5a2f1600ffbe | -4.73706 | -44.45103 | 2025-08-31 04:27:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cdf287a8-f286-3973-a393-7340b628fb9d | -6.17673 | -43.32297 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 703c8719-6d67-3db9-9702-2b7090791884 | -5.78657 | -50.20621 | 2025-08-31 04:27:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5ea69f6-8c3c-375d-8439-46d0af2fb6d4 | -7.3674 | -43.40264 | 2025-08-31 04:27:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36e8e9a9-de62-3747-838c-443f5ed21ada | -7.49121 | -45.05581 | 2025-08-31 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6801ee8-f0d6-3da4-9523-ca58085ff10a | -6.44995 | -42.40702 | 2025-08-31 04:27:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4b19121f-cbe3-393f-a5e2-962264bd68bc | -7.40938 | -42.05529 | 2025-08-31 04:27:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 83a2c65a-5cd5-3b53-9210-5a4083b664f2 | -6.44376 | -42.39716 | 2025-08-31 04:27:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ef7b3209-ba13-3974-81c9-2980fc1a18dd | -4.22518 | -47.20836 | 2025-08-31 04:27:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8ba42227-d9e2-36d3-a615-6e76b818eb79 | -2.26527 | -47.85677 | 2025-08-31 04:27:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 1c1feb87-eff8-3b77-b4f7-7be93e765f31 | -4.91728 | -42.09209 | 2025-08-31 04:27:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6feb072f-fcbb-344b-9550-ff745be48f50 | -3.84977 | -49.28843 | 2025-08-31 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4231e36a-1b55-32b2-9023-dcf46a0b5a40 | -9.05178 | -46.86821 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5930a98d-a721-3340-8802-07fb0c5995b1 | -6.8696 | -45.14822 | 2025-08-31 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca0fcc5c-d99b-3978-a4be-b312a9e0ea81 | -6.30937 | -43.61041 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9768a851-6cda-34e9-be99-d1e3eed7ef9a | -6.1691 | -44.12776 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8541316b-b572-3a60-8eff-31f1fd05af72 | -6.95539 | -44.30177 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa7c5638-811e-358f-8f87-5d5a0bbc0468 | -8.11902 | -45.00719 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a083ebf8-baf4-3168-acbe-5db06f3441d1 | -5.53556 | -36.85218 | 2025-08-31 04:27:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 255b612f-29de-3b0f-952f-cb539e2340be | -6.494 | -44.16847 | 2025-08-31 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05c39659-081b-347f-876a-e02e226b9377 | -6.94722 | -44.05629 | 2025-08-31 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 18431ed3-e70e-3eec-9413-d42bafb80b2d | -6.54157 | -44.58497 | 2025-08-31 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1b6bb56-61c0-3de7-8389-beb537d1b412 | -7.08332 | -44.32403 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d2453d6-98aa-350c-891a-1490bb79e272 | -7.21068 | -45.43718 | 2025-08-31 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 636d2246-b217-325b-aa88-7b9f04ecb869 | -5.80505 | -43.86876 | 2025-08-31 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c228a63-9d98-3b4b-8eb0-6d2123464095 | -7.63395 | -42.65555 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 34d11c4d-695b-3715-86e2-a5dfd00ee31a | -5.13947 | -45.03241 | 2025-08-31 04:27:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a1e36f4-36d1-3f77-92bf-e84e5c526796 | -6.41229 | -45.58979 | 2025-08-31 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a287676-df15-33ae-8a25-c833d2e1da9f | -7.7165 | -50.30525 | 2025-08-31 04:27:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84fdd878-464d-312e-a289-4b3f4690698f | -8.87938 | -45.09962 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 292272da-1231-3855-b86d-41a5ba7bdb91 | -7.58478 | -45.1222 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3416d124-54fc-36df-881f-ec1971d2d14c | -5.70028 | -49.1472 | 2025-08-31 04:27:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e8d3006-390f-3cf2-ae53-9abdbfa7a2c3 | -8.97178 | -46.73388 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53da9224-b4f9-3993-bbc4-e0f15fc9c449 | -9.25669 | -47.06973 | 2025-08-31 04:27:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77de523c-2d65-3ec4-9e54-1ab291c4a047 | -6.61849 | -43.73477 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8dea3c2-6070-3703-9146-cfea1260cd2a | -7.85587 | -46.9636 | 2025-08-31 04:27:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a57af714-4633-3479-914e-c2e864d54e6a | -6.46224 | -42.4271 | 2025-08-31 04:27:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 80069338-2e5e-39d1-81f4-13a7b06537d8 | -7.12548 | -44.59712 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2fc322d-7c6f-314e-9565-dd3f0f7b355d | -6.54665 | -42.75276 | 2025-08-31 04:27:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a47f694e-54ae-3093-935a-3a29e3356e4b | -6.16959 | -43.32195 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| ffd000d2-4122-359a-871b-ee4e649274ac | -6.94617 | -44.31568 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6938b5c-329a-3148-9219-072fd6c042c1 | -8.25637 | -47.1893 | 2025-08-31 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0dc7336-b52e-36be-bdac-8bc56d617ebf | -5.19677 | -46.08849 | 2025-08-31 04:27:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6e537396-5be4-31f5-a11c-d06ac3f72537 | -5.78581 | -50.2109 | 2025-08-31 04:27:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a887644b-f3a7-3fd4-80eb-22b8f09beef6 | -7.43441 | -50.25914 | 2025-08-31 04:27:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e7fdaa5-8dbd-35f0-aca2-33079d3169ac | -9.59395 | -40.35604 | 2025-08-31 04:27:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 29dfb1ff-ae62-3b72-8e93-44b67402b658 | -7.09884 | -44.3149 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 408ed1be-9761-34ac-9807-ce835fa0cc15 | -5.44026 | -42.8271 | 2025-08-31 04:27:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bbd9a028-4016-32d7-af85-06190956046e | -5.46046 | -42.57492 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 759f42fb-2084-3e10-bf6d-e84128c1ad11 | -6.1536 | -44.13683 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c2b8498-90ee-33f8-9bc4-a799dd40fb27 | -6.35243 | -43.56433 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e098cbea-0c38-3c4e-bb5e-13af3cf3a16c | -8.55661 | -51.30219 | 2025-08-31 04:27:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab845530-e2a7-3b57-ac7e-07e25e7f55f5 | -6.50145 | -43.55824 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3cbfbc08-8e9a-3769-b030-461ea5407f60 | -6.5495 | -43.68941 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eddfc6a4-8d24-3ba7-bfc7-c1ed1ef01d6a | -7.96246 | -46.4197 | 2025-08-31 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89f4e0ae-6817-376f-af1d-fb947d634572 | -6.53638 | -44.4374 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6091da7b-a4af-3129-a445-e8925a29636b | -7.7841 | -45.46054 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f9d5a54-f5d9-33c6-ab26-17b3d76deac9 | -6.17243 | -43.35128 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a2a123cb-cdc5-33d9-b3bf-dc3a369971a0 | -7.08621 | -44.32828 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73d8463d-af44-3958-a7b8-4f509c768278 | -6.95657 | -42.01217 | 2025-08-31 04:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 550381fe-78d9-31c0-bae5-04156aead56e | -7.65358 | -42.70478 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 75a214bf-cdcc-31eb-a6a7-aa0b26026e06 | -6.42461 | -43.96447 | 2025-08-31 04:27:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| efcf1ccb-8ac9-3b64-bc03-4d3423fecb5a | -8.00262 | -44.05505 | 2025-08-31 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59d1f94b-5e94-3b0f-ac41-0c69eef7fb8c | -7.78691 | -45.46458 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f863e03-aa20-32d9-83a7-6de7dd2586c8 | -7.88354 | -45.17541 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49b8ba67-69df-394e-8263-ca4defbe01ff | -4.59857 | -40.61587 | 2025-08-31 04:27:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 925dab73-678c-3a82-bc04-5ad6ef1e10e2 | -8.73341 | -50.37697 | 2025-08-31 04:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| dbf446a4-81c1-3faa-979e-687c432c5af2 | -6.28341 | -43.54725 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d4ae093-03ce-3f84-aac2-0b84d01d20c1 | -8.56053 | -51.30293 | 2025-08-31 04:27:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a776216-df65-31ce-a919-2359c3476921 | -7.96411 | -46.40925 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5aa6563-b6a5-36fd-9834-6f134b2b217c | -7.10048 | -44.5785 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62c46e87-8888-33e4-bedd-afc789327897 | -7.38641 | -46.65984 | 2025-08-31 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a96a5edc-b6f5-32bd-aced-821338662774 | -5.81317 | -43.86225 | 2025-08-31 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a0f898c4-5da9-3d8b-b51c-b8a1101b8388 | -4.22493 | -47.20883 | 2025-08-31 04:27:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8c7ca8a9-ed62-3085-873f-72144d0dc8be | -7.45562 | -49.59785 | 2025-08-31 04:27:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd9f875a-64c3-3459-b7f7-f151e77f78e2 | -7.40367 | -44.08407 | 2025-08-31 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35c3b219-9b25-389f-a18b-a877baa7c09a | -6.19515 | -42.76254 | 2025-08-31 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 190d7f06-a357-37a9-9e2d-aa9e29f16690 | -3.59135 | -47.52462 | 2025-08-31 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac4c8fb0-a43e-3a2e-997e-1b6ae33bed7b | -6.54296 | -42.75226 | 2025-08-31 04:27:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3b5a34a8-d9cd-3690-9228-9c131b566445 | -6.65137 | -43.94223 | 2025-08-31 04:27:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba78ec06-ece2-3c9d-9ccb-b379f344dc6b | -6.53477 | -44.58383 | 2025-08-31 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e4fa11a-49a3-3427-a7fe-be7b26538c84 | -7.96524 | -46.42371 | 2025-08-31 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e944d54-a6d9-3a29-9b06-2c9cc8e86abb | -4.14404 | -46.44969 | 2025-08-31 04:27:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README35.md)
