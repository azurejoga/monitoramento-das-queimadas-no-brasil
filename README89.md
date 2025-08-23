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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 562347b7-d5f5-35f1-96c9-cafd14d978b5 | -12.5418 | -45.6189 | 2025-08-23 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 07b15664-e1cd-3599-8cb7-0bc6618f57ad | -6.1229 | -43.9578 | 2025-08-23 13:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| b32cc840-fb47-3398-91a8-93f85a7f2c63 | -15.0343 | -56.3724 | 2025-08-23 13:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| de7265fc-c8af-3878-bc08-ea67563fe5d4 | -6.1416 | -43.9563 | 2025-08-23 13:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| afb7a87e-78db-3342-8307-67dc3b615a7f | -15.0183 | -54.8942 | 2025-08-23 13:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 106.6 |
| e829571b-6734-3cd3-af5d-58f6582f801b | -13.0481 | -46.3183 | 2025-08-23 13:30:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 86.9 |
| fca51549-c126-34b0-8523-3ed6b5de2b62 | -10.4784 | -46.831 | 2025-08-23 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 157.1 |
| d217cf65-943b-38be-9ab2-766d83654aa5 | -6.6044 | -44.5624 | 2025-08-23 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 07684fb6-f4e0-386b-9f77-e761f0bbe45c | -7.6296 | -45.2464 | 2025-08-23 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| f2eb1bf3-16f1-3dcc-8f79-d559fe0857fb | -6.389 | -45.5116 | 2025-08-23 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 54512f5b-70c2-31c1-8bdf-7cb517c78add | -8.3014 | -47.2652 | 2025-08-23 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 0eee1990-31ac-3989-91c3-7d20ff7866ee | -13.0477 | -46.3412 | 2025-08-23 13:30:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 9d7ad23e-aee3-330b-88a2-2f430f8729ef | -7.6296 | -45.2464 | 2025-08-23 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| cab74a35-00b5-3617-850a-6d9054d4d373 | -8.5272 | -48.8393 | 2025-08-23 13:40:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 71.4 |
| cdf62adc-e603-33bf-88f0-df2b067a0ad0 | -6.0972 | -44.6947 | 2025-08-23 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| ada64bdc-9943-3667-bb0b-7d95bee9b379 | -7.6366 | -46.2823 | 2025-08-23 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| fbe4fd3f-55ef-369e-a07e-d802fac4ad59 | -8.9579 | -40.6311 | 2025-08-23 13:40:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 97.5 |
| d61d9d98-a0f6-377c-b93f-5f22eff19d28 | -5.7614 | -57.6002 | 2025-08-23 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| c5a422ea-8ceb-33f3-aa65-a752fad98a68 | -8.5944 | -62.6126 | 2025-08-23 13:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 5b46ca8e-c159-32b8-91bb-e9317722c392 | -10.6201 | -50.1609 | 2025-08-23 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 107.6 |
| a5754ca4-5143-38e2-8a41-94b5dc3b603a | -7.0164 | -44.6413 | 2025-08-23 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 114.9 |
| fde8e41e-0e37-3264-a3d9-7e03b6123a83 | -7.0352 | -44.6396 | 2025-08-23 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| e4e7510b-e956-3cfc-bf12-396188a57650 | -8.3317 | -44.7885 | 2025-08-23 13:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 28b0ccf9-5cb7-32b7-8e75-6e2425475083 | -12.1949 | -50.2397 | 2025-08-23 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 1465ade8-4f10-38ad-84c3-16052cb24658 | -5.7615 | -57.5807 | 2025-08-23 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 5c27d531-1418-312b-bbb0-2e54f6ebcfc0 | -5.8323 | -52.0681 | 2025-08-23 13:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 99034967-b46a-347e-8818-b0f4ff94edcf | -6.1229 | -43.9578 | 2025-08-23 13:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| a47e7abe-bdd6-3796-bb4f-9f393d4d8cc8 | -10.4784 | -46.831 | 2025-08-23 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 88457017-9f10-3549-95d5-90ce8373ec5d | -6.1308 | -43.1432 | 2025-08-23 13:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 71.3 |
| c1dd5331-990b-36cc-81ec-cd1bd81bda96 | -11.1204 | -44.7681 | 2025-08-23 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| d8896e18-fcf7-350c-a9ad-a97a959ef48f | -8.5458 | -48.8592 | 2025-08-23 13:40:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 05cf50b4-e4fc-3d46-baa3-f9bc2a73fa46 | -6.5856 | -44.564 | 2025-08-23 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 148.6 |
| eb2f1118-3e70-35d4-9f42-892ce59810a5 | -8.527 | -48.8609 | 2025-08-23 13:40:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 4d413b3c-bfc3-3157-a268-3be627b6df27 | -5.9062 | -45.1185 | 2025-08-23 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 94fc12a9-54b3-3b74-9321-5d2c6b60d9ab | -14.7521 | -45.4091 | 2025-08-23 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 2752b560-5502-3ef1-883b-60fb46fac52b | -11.1396 | -44.7654 | 2025-08-23 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 115.2 |
| e5b4bf82-4433-3324-a7d8-2a55813bd0f4 | -15.0183 | -54.8942 | 2025-08-23 13:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 4e011f8c-bf3a-3283-9866-303053755314 | -8.0379 | -47.3117 | 2025-08-23 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| e473f664-3ceb-3100-9332-d9ace88cc299 | -6.3698 | -45.5582 | 2025-08-23 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 089af409-7337-35b8-85d6-14e58d3d64f6 | -11.1201 | -44.7913 | 2025-08-23 13:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 2c8faa79-6fcb-3d03-96c0-07dc56b1455e | -5.7429 | -57.6009 | 2025-08-23 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 33cb747d-afca-34e5-b348-814b43ffde2e | -6.6044 | -44.5624 | 2025-08-23 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| a2181a66-900f-3141-9096-d845ca5447d2 | -5.7431 | -57.5814 | 2025-08-23 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 4aca9a20-0a45-3c77-935c-f14009f47d82 | -12.9921 | -45.2252 | 2025-08-23 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| fff8f162-eb27-362c-b078-d25a3e59c9c9 | -10.6393 | -50.1375 | 2025-08-23 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 8a37ba92-a881-3f2c-811e-125525aa96a6 | -6.1416 | -43.9563 | 2025-08-23 13:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 8d10c3e6-81f4-3a48-8f6a-db5e7040c740 | -6.5578 | -45.4757 | 2025-08-23 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 3eccce2d-9818-307a-82f0-0c7755507a47 | -6.37 | -45.5356 | 2025-08-23 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 3db430e9-7802-3291-89c2-1662a2444d66 | -11.6981 | -51.6603 | 2025-08-23 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |
| ea113f68-cfb5-3b18-b5e7-a1faf0b009bb | -9.0494 | -47.6332 | 2025-08-23 13:50:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| fbfd2277-3b00-34f2-a92f-3d82c1769c61 | -14.3704 | -52.0386 | 2025-08-23 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 5fdd3fde-8dc4-3df5-8279-aa33a98ec2c0 | -14.37 | -52.06 | 2025-08-23 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 115.5 |
| c856d9b3-1ada-3f57-9693-7b7eb6589ce2 | -6.1308 | -43.1432 | 2025-08-23 13:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 71.7 |
| 780a93bb-5e11-3d85-a1ef-40806f097c65 | -10.6962 | -50.1314 | 2025-08-23 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 18e87bc4-b0f1-386d-95df-3b79b957c477 | -5.8309 | -45.1693 | 2025-08-23 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 1758dd37-e6a8-3461-ad5c-27f5df382c50 | -15.2288 | -53.8481 | 2025-08-23 13:50:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 588.2 |
| 4a8a41ec-38cf-317e-a0ac-a6622a200fea | -6.8733 | -59.8213 | 2025-08-23 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| d5b96d39-f4d2-3ddb-93ed-a75b5012f78c | -7.6296 | -45.2464 | 2025-08-23 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 101.3 |
| a7a65404-13f6-3e40-b480-12d7cf33d198 | -6.3698 | -45.5582 | 2025-08-23 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 52be9ceb-4c2d-3295-87e9-abee7a57cf93 | -15.2093 | -53.8506 | 2025-08-23 13:50:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 63641813-d047-3ca8-9e2a-556175a82076 | -8.527 | -48.8609 | 2025-08-23 13:50:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 131.4 |
| c4f25600-f87b-3391-8d63-81bfb4707b06 | -8.5272 | -48.8393 | 2025-08-23 13:50:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 190cd3b8-f7c8-3764-82ac-c89341a727e9 | -6.5856 | -44.564 | 2025-08-23 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 175.4 |
| 511edb76-7630-3d21-8641-29f58fe0d36f | -7.0164 | -44.6413 | 2025-08-23 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 2425a7dd-10aa-36e3-a57b-a32f9b55659a | -11.6208 | -50.4361 | 2025-08-23 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 7350cfff-a69c-389d-a587-0e7a5b9d2751 | -15.0183 | -54.8942 | 2025-08-23 13:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 117.2 |
| f354e620-866f-3ebd-8f35-30c024c77a06 | -6.1229 | -43.9578 | 2025-08-23 13:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| a9c56679-ba6d-3402-9d78-956c88cb511e | -6.37 | -45.5356 | 2025-08-23 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| c871ccb9-110b-396f-9193-4bd3c6ba5bc7 | -11.1201 | -44.7913 | 2025-08-23 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 293e7408-2b57-3457-aee0-9833834518d9 | -10.4784 | -46.831 | 2025-08-23 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 26799122-39af-3404-a51f-acb41b85d9c1 | -11.1396 | -44.7654 | 2025-08-23 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 0041b03d-ab60-3a2b-a497-fab7be56e4b4 | -10.5684 | -47.155 | 2025-08-23 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| df2d18cc-b5eb-3ceb-890e-3ca01b72dced | -6.5858 | -44.541 | 2025-08-23 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 5c96229b-c0b0-30a7-9b41-bff3a6a9078f | -5.7431 | -57.5814 | 2025-08-23 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 152.1 |
| 182fb73b-804e-380f-8b1c-00bc3e6b06a2 | -15.2284 | -53.8691 | 2025-08-23 13:50:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 189.5 |
| 4cef43e5-7052-33f6-ac57-05af1b25f2db | -7.9447 | -63.0528 | 2025-08-23 13:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| e6237fdc-bad8-3742-ab1e-8eb15559a50e | -5.7615 | -57.5807 | 2025-08-23 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 27597b23-e2c2-337d-8aeb-5b03eb4cd728 | -5.7429 | -57.6009 | 2025-08-23 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 0a8fac30-2c23-33e3-bcf7-aa4760a55282 | -15.034 | -56.3928 | 2025-08-23 13:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 4fbb19aa-19b3-34e6-8cd4-41385a6265e8 | -6.0972 | -44.6947 | 2025-08-23 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 462ac1a4-9137-3a2b-a5b1-ea7c34e91f2d | -11.902 | -47.1177 | 2025-08-23 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 031db591-c0c9-3587-ba6e-a6e5d5cf20de | -7.0352 | -44.6396 | 2025-08-23 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 7cd96a19-d944-3b59-b5e4-1f463b770cc5 | -11.1204 | -44.7681 | 2025-08-23 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 840063fc-8542-3e16-a827-978b8686826d | -13.4349 | -46.2573 | 2025-08-23 13:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 22d6f0f4-59c0-3557-b495-ed13e4c86bf6 | -7.6366 | -46.2823 | 2025-08-23 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 6c093be9-1920-3c5a-a84c-f5fb0c96d544 | -12.1949 | -50.2397 | 2025-08-23 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| fd10a83f-a4c5-33c3-a054-61a25f6dd21c | -6.6721 | -45.2855 | 2025-08-23 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 3635ae84-dd98-3235-ae24-6f79cc5d46cb | -6.5781 | -59.871 | 2025-08-23 13:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 785e25a2-5b7b-310a-8b3d-e5530eec72ee | -6.1416 | -43.9563 | 2025-08-23 13:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 930216dd-6137-3334-8777-7d9c421ffd97 | -8.3009 | -47.3094 | 2025-08-23 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 2601b7be-43aa-36b8-8fa9-7c0f7a56e536 | -10.6201 | -50.1609 | 2025-08-23 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| d0f78f61-82ec-3f4b-9e46-ef5457ab5a50 | -6.6044 | -44.5624 | 2025-08-23 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 3d5bc367-2479-3ae3-bb20-1885e06fd582 | -5.9062 | -45.1185 | 2025-08-23 13:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 623316aa-946c-3f46-b360-cf80fa0a181b | -7.6296 | -45.2464 | 2025-08-23 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| d4ed1ca0-eb4e-3b46-ba2b-9411972fb72c | -8.527 | -48.8609 | 2025-08-23 14:00:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 140.5 |
| f1f43af5-317d-382c-b602-23345a12c4a8 | -10.6393 | -50.1375 | 2025-08-23 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 1c603783-7879-37c1-b2ed-c67d4f6c555c | -11.902 | -47.1177 | 2025-08-23 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| f7e954d3-4578-3d28-8a3e-4d390ce5e8c6 | -15.5385 | -51.7064 | 2025-08-23 14:00:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 7f45829c-634d-3e28-9ec1-938ab0b3815c | -10.639 | -50.1589 | 2025-08-23 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| aadf2176-d1ce-3e5c-afd7-6a5e08c08d47 | -6.3698 | -45.5582 | 2025-08-23 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |


[Clique aqui para ver as próximas entradas](README90.md)
