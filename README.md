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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b50493f4-eff8-3878-9f55-ad26a1f50170 | -6.90507 | -34.89962 | 2025-03-14 00:01:00 | TERRA_M-M | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 34.4 |
| 2edb3336-fc1b-381d-8536-6e54b8f35350 | -7.22427 | -35.78236 | 2025-03-14 00:01:00 | TERRA_M-M | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 99276445-61c9-34b2-b70e-b716ea546362 | -7.2401 | -44.77922 | 2025-03-14 00:01:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 44e437e5-fc78-35a2-b932-d6ea797e193d | -7.24126 | -44.77376 | 2025-03-14 00:01:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 4dbd6db2-9815-36c9-8f66-80a00d045b10 | -6.1633 | -43.7057 | 2025-03-14 00:01:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 30.8 |
| d631ce29-66d8-3cc8-8d53-ea2ece55467b | -6.89579 | -34.90094 | 2025-03-14 00:01:00 | TERRA_M-M | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 21.0 |
| 6d19dcc4-396a-37d3-887e-4654c5a0c234 | -7.69631 | -35.1466 | 2025-03-14 00:01:00 | TERRA_M-M | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| eff8e53e-1f26-39ed-8775-48aef0f3e9ce | -6.90365 | -34.88969 | 2025-03-14 00:01:00 | TERRA_M-M | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 05bdff1a-073f-3fac-8568-610e533e7461 | -5.97121 | -39.67361 | 2025-03-14 00:01:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 61a65783-3cf5-36f9-827f-5ad102e3b56c | -6.89437 | -34.89104 | 2025-03-14 00:01:00 | TERRA_M-M | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 049ef953-bbea-322e-beaf-5be9a3bcac25 | -11.8089 | -38.461899 | 2025-03-14 00:03:00 | METOP-C | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5af35c6a-caae-362a-816d-9c35a42f256e | -10.1836 | -37.446201 | 2025-03-14 00:03:00 | METOP-C | NOSSA SENHORA DA GLÓRIA | SERGIPE | Brasil | 2804508 | 28 | 33 | nan | nan | nan | Caatinga | nan |
| e8e8934e-e382-302b-aa70-aef4a89b1337 | -6.1549 | -43.6991 | 2025-03-14 00:03:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec0efb3b-0597-3184-9705-1d619a3f29e8 | -10.1403 | -42.169601 | 2025-03-14 00:03:00 | METOP-C | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d73942b1-5a84-36b4-bb22-bad3a3eb6894 | -7.2424 | -44.779301 | 2025-03-14 00:03:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 840b79ba-26cf-3515-af3a-8d8e7245dc36 | -9.7677 | -37.6563 | 2025-03-14 00:03:00 | METOP-C | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | nan |
| 4e896bc0-3b30-37b8-91aa-61db41565c3c | -6.1569 | -43.708199 | 2025-03-14 00:03:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 61f74831-682e-3cc8-a4b9-9682ca67e6ab | -9.0292 | -40.577999 | 2025-03-14 00:03:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| e5257865-3a27-3ae1-9bab-806a23bc7d7a | -9.0308 | -40.585201 | 2025-03-14 00:03:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 73cadbc0-e705-3fb4-8fb7-7b88b2efdd5e | -18.3412 | -40.009602 | 2025-03-14 00:03:00 | METOP-C | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4fd928c9-cde5-3ec1-bc09-dbf8b2da44fe | -12.8418 | -43.824001 | 2025-03-14 00:03:00 | METOP-C | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 46b6d9e6-bdf5-3151-885e-896907766860 | -12.8818 | -44.8741 | 2025-03-14 00:03:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1f407f77-5269-32f0-89c4-c3c53ca10150 | -20.052299 | -40.333599 | 2025-03-14 00:03:00 | METOP-C | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 42c15fd3-1675-3761-8e5a-190d44335aab | -10.1421 | -42.178001 | 2025-03-14 00:03:00 | METOP-C | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b5d560d2-c5f5-3c27-a493-4d0ba577ca18 | -9.8311 | -40.574299 | 2025-03-14 00:03:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 890ef94e-7f1d-39fe-b8a4-c975f6f2bbfd | -6.2227 | -48.049999 | 2025-03-14 00:03:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1caad77f-2cf7-3025-9df7-4e5e20a6cefd | -10.3066 | -38.747601 | 2025-03-14 00:03:00 | METOP-C | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0d67481f-7eab-3fde-8b64-3cb6d5a8bbbb | -6.1667 | -43.706001 | 2025-03-14 00:03:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3bd31e91-1c95-322e-be11-f45b5ea2c296 | -6.1647 | -43.696999 | 2025-03-14 00:03:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2bbb544e-9075-3ea6-bad3-397fc2993fca | -12.8747 | -44.8895 | 2025-03-14 00:03:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 59eca165-3bcd-37d4-841b-a52c19406542 | -7.24 | -44.768398 | 2025-03-14 00:03:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec5b3a5d-0d2c-3654-86cc-85284c7503ae | -16.4832 | -39.074902 | 2025-03-14 00:03:00 | METOP-C | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c0ca0d6f-809b-3a53-9d0e-9fdcb3d2e67d | -12.872 | -44.876099 | 2025-03-14 00:03:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c2804197-f96c-3d9b-a6bf-56f91462e2f9 | -9.7693 | -37.663399 | 2025-03-14 00:03:00 | METOP-C | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | nan |
| a1561747-da40-3abf-b17e-616cf495da93 | -10.3082 | -38.754501 | 2025-03-14 00:03:00 | METOP-C | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| fb6863b3-c2fe-319c-947a-759f98b72d1f | -9.6547 | -38.151299 | 2025-03-14 00:03:00 | METOP-C | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c1461d70-9f92-3153-8f26-2a1b7755078d | -9.8295 | -40.567001 | 2025-03-14 00:03:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e2cf61c2-51c5-3a45-930a-6ae37f143ea5 | -10.1384 | -42.161098 | 2025-03-14 00:03:00 | METOP-C | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c56c4b2b-42d7-357d-9114-bcb8e0fa7350 | -12.8442 | -43.835499 | 2025-03-14 00:03:00 | METOP-C | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e7581b90-47a7-37a1-809e-90c48b841021 | -12.8845 | -44.887501 | 2025-03-14 00:03:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5508771b-c41e-3127-88f9-66ab4be3acb3 | -12.8915 | -44.872101 | 2025-03-14 00:03:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4626092b-bf39-315b-9eeb-0a44c00cf3c9 | -18.3314 | -40.011799 | 2025-03-14 00:03:00 | METOP-C | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f33aaba1-21dd-3d90-b6dd-c08533bd467a | -12.8833 | -44.8716 | 2025-03-14 00:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 319adfc0-32f3-30f6-a2fd-f0b905f631cc | -7.4565 | -35.1826 | 2025-03-14 00:30:00 | GOES-16 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 79.4 |
| 00a1894c-9675-3450-8971-992bc915462f | -18.538601 | -56.1702 | 2025-03-14 00:54:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3917d991-d934-339b-86a9-a4b614292bc0 | -27.868799 | -55.2118 | 2025-03-14 00:54:00 | METOP-B | PORTO XAVIER | RIO GRANDE DO SUL | Brasil | 4315107 | 43 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 05891ade-9a13-3211-91d4-fc1bae9a73fd | 3.1668 | -61.002201 | 2025-03-14 00:54:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ab110fa4-c216-34ee-98b2-5d5b617f944f | -12.8866 | -44.8466 | 2025-03-14 00:54:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ac364bb0-3bdc-3e6c-9967-a6275469fba2 | -18.5403 | -56.178101 | 2025-03-14 00:54:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9874ab1e-8659-3c36-a74c-f53fffc83291 | -12.8931 | -44.870701 | 2025-03-14 00:54:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0c09a921-eae5-3669-8f42-fbf198c5836e | -7.0177 | -35.1592 | 2025-03-14 01:00:00 | GOES-16 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 90.5 |
| 8155e9ea-6831-339b-97f8-d8d010768e75 | -7.0 | -35.16 | 2025-03-14 01:00:00 | MSG-03 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4693ef6a-b83c-3494-a25c-a070722347cf | -18.53536 | -56.18202 | 2025-03-14 01:34:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.5 |
| d2702444-7dfd-359c-8b8c-076bc4dabfc2 | 3.1724 | -61.01464 | 2025-03-14 01:41:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3f12e69b-91e1-32fb-86fc-101f803b4a96 | -15.56501 | -40.63882 | 2025-03-14 02:58:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 1fc4b8a5-8ef9-3878-9cb0-ca81a68fffaf | -15.56652 | -40.63207 | 2025-03-14 02:58:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| bbf84656-c35d-3de0-9182-95837531bc40 | -15.56096 | -40.63717 | 2025-03-14 02:58:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 57bad056-d0a2-3477-9cf5-cfbbbc81cc52 | -15.56256 | -40.63023 | 2025-03-14 02:58:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 279b6fd8-1b43-325d-9936-9c6a2bda6738 | -18.3349 | -40.0139 | 2025-03-14 03:00:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| c390fce0-67fd-3e20-bac2-987df8752b0c | -7.24291 | -44.77969 | 2025-03-14 03:47:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7bb57516-2591-313e-87ad-b98a58f57dfe | -6.16248 | -43.70274 | 2025-03-14 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c21589b3-4615-35c9-b34b-cd874070b50a | -6.22759 | -48.04867 | 2025-03-14 03:47:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6acef92-ca5e-3a71-952b-2eea84d1306b | -6.22672 | -48.05342 | 2025-03-14 03:47:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b9eb006-c5d8-36de-b76c-d7c407f08b38 | -6.23845 | -42.79493 | 2025-03-14 03:47:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 49d5b772-8fb5-3fcf-8f48-b2d93535dd12 | -8.07358 | -34.97784 | 2025-03-14 03:47:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8c4012a3-51cc-38e2-a66c-b04b56567cb2 | -7.22314 | -35.77782 | 2025-03-14 03:47:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3da73ec6-3fb0-35fb-bc95-34c58ba21e2a | -6.22647 | -48.05103 | 2025-03-14 03:47:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f0b8a6d-44c4-31de-84c5-8bdbfb299648 | -7.22259 | -35.78138 | 2025-03-14 03:47:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 17ca118f-375d-3374-bf44-f42847fb92b8 | -7.24384 | -44.77443 | 2025-03-14 03:47:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a6ded3bd-15a4-3901-9c29-748bd9cbacd7 | -6.74631 | -37.98085 | 2025-03-14 03:47:00 | NOAA-21 | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 74d9a8d6-3e7e-3d1b-9176-937422aa246f | -7.2215 | -35.7885 | 2025-03-14 03:47:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 233f32b7-e6ac-35bc-b8fe-cac900720834 | -7.24868 | -44.77519 | 2025-03-14 03:47:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 65a0d6df-2433-39ab-8fbe-dc3365f9aae6 | -6.23251 | -48.05241 | 2025-03-14 03:47:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5354c55b-6357-35bc-b2aa-7b782405fe16 | -6.16705 | -43.70354 | 2025-03-14 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4450a7bc-df15-3f15-9bb8-0775a4329981 | -7.24961 | -44.76994 | 2025-03-14 03:47:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 577fd5ca-a66e-3123-b194-4dcf275bba0a | -13.696 | -44.32766 | 2025-03-14 03:49:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22e2340f-af94-3c3c-a13c-c8540b4c4060 | -12.71791 | -43.18546 | 2025-03-14 03:49:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| af5299a8-8d81-3e39-8d25-e237673eed21 | -12.88883 | -44.88264 | 2025-03-14 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b16027c3-dcd2-3e70-a15e-1a97fa51c6a5 | -11.57136 | -47.61601 | 2025-03-14 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27f7e645-e9dc-332b-9818-349b8cfc315a | -10.18092 | -37.44897 | 2025-03-14 03:49:00 | NOAA-21 | NOSSA SENHORA DA GLÓRIA | SERGIPE | Brasil | 2804508 | 28 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c1ccd9ec-f394-3443-a931-0f79d0349568 | -12.89487 | -44.87461 | 2025-03-14 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 81b6652e-a68a-3d65-bcea-1fb6bb087173 | -12.28897 | -38.43217 | 2025-03-14 03:49:00 | NOAA-21 | CATU | BAHIA | Brasil | 2907509 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 1b6a4db6-2079-3a0b-8777-17f680a06d92 | -12.71569 | -43.18317 | 2025-03-14 03:49:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| af1b179b-955f-318e-a583-28ede66293c7 | -11.57216 | -47.62023 | 2025-03-14 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e67a01b-6087-3883-af9a-4b1b9396992c | -9.82816 | -40.57305 | 2025-03-14 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fbc96c6b-db3e-3180-88f8-876f235677f6 | -9.82885 | -40.56895 | 2025-03-14 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 61a905db-9621-39ef-ba43-9b22ad0b300f | -9.83241 | -40.56955 | 2025-03-14 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 30d15ead-5634-36c4-8c4f-d70da1eba7ca | -11.57148 | -47.62373 | 2025-03-14 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a0d7176-7a57-3374-9ac3-d37424d6d3e8 | -15.07234 | -44.1041 | 2025-03-14 03:49:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee5a49a3-2d44-3945-882e-794ad8f831d6 | -12.80398 | -40.3903 | 2025-03-14 03:49:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 185a0a12-5026-3bd7-b5c3-eb817a18db9c | -12.84956 | -43.82875 | 2025-03-14 03:49:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 550c9c5a-ded4-343f-ae16-e62e12822a21 | -11.88753 | -46.9431 | 2025-03-14 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5d6d786-de10-37e1-a7d1-2ed81dae114d | -12.87721 | -44.87142 | 2025-03-14 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9323cade-8146-322c-8070-e8cfea7b9778 | -12.88964 | -44.87822 | 2025-03-14 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| c4bc6483-a62d-35a9-bff4-c58f7e163abf | -9.02696 | -40.58351 | 2025-03-14 03:49:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 11.7 |
| d5fcffc0-02ca-30b4-9f23-5c79eba66cef | -14.21017 | -47.02196 | 2025-03-14 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1e2d360-ee48-38c8-b682-d01e02ac5c27 | -11.34942 | -47.55524 | 2025-03-14 03:49:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 497ae029-c054-360f-9875-4ece908c9831 | -8.6329 | -40.44447 | 2025-03-14 03:49:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 78b27e82-4b46-387f-8718-4be83323d081 | -11.57003 | -47.62309 | 2025-03-14 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0363de9e-64f8-36fb-8309-dc8c73f1d6c9 | -12.89567 | -44.87021 | 2025-03-14 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README2.md)
