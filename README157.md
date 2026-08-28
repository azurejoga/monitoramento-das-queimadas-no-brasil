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

## Dados Diários - Página 157

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03d9b85c-2c7f-310a-b06d-48c186240dd0 | -8.0551 | -45.839 | 2026-08-28 18:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 46835461-0010-3266-9f55-7ef54a6f2363 | -7.5662 | -61.3049 | 2026-08-28 18:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 3eb70b70-b2a7-3ae5-9615-39311fd11e1b | -13.4132 | -51.7784 | 2026-08-28 18:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 2f734246-3df2-3c2b-9c16-01ceb690f7f3 | -7.4735 | -61.3846 | 2026-08-28 18:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| e4371f98-b284-397d-8880-e1042aad0002 | -7.5478 | -61.3056 | 2026-08-28 18:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| acd76b46-dcb0-35ae-b4ff-e325680453de | -6.7123 | -58.9412 | 2026-08-28 18:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 36fa1c03-f6e5-3546-981e-58c2c4e7ebca | -5.7616 | -57.5612 | 2026-08-28 18:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 13c81b6c-d7b3-3b85-9d9c-8000f1a0c685 | -11.0247 | -49.6656 | 2026-08-28 18:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 3035fff4-62e4-306f-b574-eddb51b9d835 | -9.4329 | -51.6926 | 2026-08-28 18:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 137.7 |
| 2da246f6-fb26-3e1f-a57b-3273449d4266 | -8.0742 | -45.8147 | 2026-08-28 18:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| c702f092-0521-3580-96cf-ceb9ae448907 | -4.3022 | -59.4634 | 2026-08-28 18:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 91.1 |
| cb3e806f-a929-3151-b1fc-f7fe3003b41c | -12.2281 | -50.5578 | 2026-08-28 18:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 62b4861e-8eff-3cfd-af7c-5e1f01ac3bb9 | -10.8422 | -50.5219 | 2026-08-28 18:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 9dfdc23e-eb0b-3373-8a9b-e26b215aac82 | -6.8257 | -55.6218 | 2026-08-28 18:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 7b01d46a-13e7-38d6-8924-763ba977b2df | -8.6311 | -66.5287 | 2026-08-28 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 5057b6fc-f167-3511-af2b-14adb2240fe0 | -11.1998 | -55.0805 | 2026-08-28 18:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 58e64f05-69ad-31ea-b88e-94f131bb7872 | -8.87 | -66.8935 | 2026-08-28 18:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| a2d039c8-e363-3e33-8fe1-0813fc50b3a2 | -6.7267 | -59.654 | 2026-08-28 18:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 641b2b0b-754d-3d02-87ae-283131e13998 | -6.8386 | -59.4379 | 2026-08-28 18:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 965063b6-a10f-30a3-b765-d16497c881bc | -6.8019 | -59.4008 | 2026-08-28 18:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| a6d7ab48-a9f3-34fa-8a76-efafbe979642 | -10.4499 | -46.2052 | 2026-08-28 18:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 212.0 |
| e0b53aeb-8c68-3fe4-b817-81d809bfd415 | -8.826 | -68.9835 | 2026-08-28 18:00:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 135.3 |
| b7e36505-8a7f-32c3-9b9b-5ec401746a9b | -9.1714 | -59.5793 | 2026-08-28 18:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| a01f94f5-201a-3ec4-a82b-446cf34792b8 | 1.4373 | -55.6491 | 2026-08-28 18:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 797ee5b7-5226-34bf-823e-dbd237a3a6eb | -14.8821 | -52.608 | 2026-08-28 18:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 248.7 |
| 5d501e24-c245-392f-a0ad-49be3ba557ab | -6.8755 | -59.4364 | 2026-08-28 18:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 197275bf-06c0-37f4-a117-b1db686cbda2 | -6.7279 | -59.4423 | 2026-08-28 18:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| e6b2f069-7e54-378c-9708-598417695a72 | -5.9995 | -57.8444 | 2026-08-28 18:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 6cfdc1ce-e664-3e60-bbdc-0d9aa797e08a | -8.5783 | -54.7768 | 2026-08-28 18:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 0dfea3b9-99f4-37a9-9059-376bb83e741f | -8.9557 | -68.9072 | 2026-08-28 18:00:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 00c68a36-ed0e-3e3e-8fa7-5dc15c28f3ea | -8.8371 | -62.3181 | 2026-08-28 18:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 3bc9032a-7103-3363-9284-96c765782d89 | -10.76 | -53.9974 | 2026-08-28 18:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 9db8dd03-458a-3825-a288-84ba6cfa6b5e | -6.7698 | -55.6844 | 2026-08-28 18:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| ca6a4952-adbb-3cba-befe-99b8832f2ecd | -6.8571 | -59.4179 | 2026-08-28 18:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.2 |
| d899fcf7-7881-355e-99f8-c115150c39db | -7.6031 | -61.3225 | 2026-08-28 18:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 314d8cce-ce54-3e01-a41e-e8cc2d88a94d | -8.5975 | -54.715 | 2026-08-28 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| cbd50346-9090-306b-9ed9-b1b9f571048e | -8.0742 | -45.8147 | 2026-08-28 18:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| cdf4e1db-5875-3203-aca4-27a4451dba81 | -13.4132 | -51.7784 | 2026-08-28 18:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 9d1e3e01-954c-3dc1-bd6b-68f9fbb7ba58 | -4.3021 | -59.4826 | 2026-08-28 18:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 67ee8a0f-e9f0-3786-bf35-118995d6a272 | -8.5777 | -54.8373 | 2026-08-28 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 642543d0-1485-32c0-a974-62f8f1bf27a1 | -13.4324 | -51.776 | 2026-08-28 18:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 941bd0d0-2e36-3b30-9512-afb31dbc314e | -6.9521 | -58.9506 | 2026-08-28 18:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 215.3 |
| 11c795ce-c90a-30cf-ae0c-93e18caf1275 | -14.8817 | -52.6293 | 2026-08-28 18:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 301.1 |
| b46b0d15-1eae-3a77-9d6e-e93891206848 | -6.8368 | -59.7458 | 2026-08-28 18:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 13c1bc86-6216-30e5-9d2b-4ecb05920a1d | -3.5574 | -64.4488 | 2026-08-28 18:10:00 | GOES-19 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| fa6cd388-1a57-3dc8-89d2-6337319be8bd | -7.5846 | -61.3232 | 2026-08-28 18:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 6d800625-d245-3cf8-888a-c103788c1081 | -8.5977 | -54.6948 | 2026-08-28 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| e1d9c3cd-0ae2-3054-a001-e397f92d408b | -6.5607 | -56.5464 | 2026-08-28 18:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| f090bb96-b14d-3bcb-9ce4-2733eb026f4e | -9.2477 | -57.0697 | 2026-08-28 18:10:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| a10929f2-2a8d-3192-9444-b00592286401 | -6.7647 | -59.4601 | 2026-08-28 18:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| b5f02d49-b500-3d80-929d-835d72c40bf9 | -11.5984 | -65.1338 | 2026-08-28 18:10:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 1cec1009-f7b6-3c32-8668-2e729e1c3953 | -6.7883 | -55.6834 | 2026-08-28 18:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| fdfbe275-ff14-3f2b-8cfe-992714528f72 | -6.7279 | -59.4423 | 2026-08-28 18:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 633cb8fc-d8cc-3302-9c47-209254b1e63f | -12.0733 | -47.1614 | 2026-08-28 18:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| fba8ac86-5e6f-38ac-b0fe-1ef00ab319ad | -6.8542 | -59.9372 | 2026-08-28 18:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.8 |
| dd1b49d9-05b4-3484-97d6-ec19ace6e7ca | -8.0551 | -45.839 | 2026-08-28 18:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 9fa406ee-aa84-3da8-9792-143ec0d6073c | -8.0739 | -45.8372 | 2026-08-28 18:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 175.2 |
| bd968d02-1dcd-320c-ab23-e19d4d5d0c76 | -9.1714 | -59.5793 | 2026-08-28 18:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 615e044c-6a31-3f10-a26c-da31171f2ffe | -11.1998 | -55.0805 | 2026-08-28 18:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 15e08e72-6747-3388-921a-abc44052b610 | -6.1473 | -57.78 | 2026-08-28 18:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 0d93710f-6503-33e5-9eb0-34d04801f102 | -6.7833 | -59.4208 | 2026-08-28 18:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 64b80b7c-59af-3e6e-a7f5-3f060098e94e | -11.0247 | -49.6656 | 2026-08-28 18:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 139.3 |
| bd7bf5fc-2f70-3a72-b3f8-587ba206e474 | -9.8894 | -67.0137 | 2026-08-28 18:10:00 | GOES-19 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 4264fb37-90ac-3f34-b01f-e4bb618bbc95 | -8.0548 | -45.8616 | 2026-08-28 18:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 2601f8b2-c1c6-3e3a-9258-3f155a2c8583 | -8.6311 | -66.5287 | 2026-08-28 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 706e27a3-d818-395d-89ec-903ef06760d0 | -7.5852 | -61.2089 | 2026-08-28 18:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| d69e8b3f-f595-37ec-8226-908f97abdcb6 | -8.87 | -66.9121 | 2026-08-28 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 492dd04b-7878-36e2-afcd-b14d5ad1ea4f | -7.5515 | -57.7363 | 2026-08-28 18:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| e559149c-8edd-3fc3-8352-952bd34febeb | -8.6694 | -49.5369 | 2026-08-28 18:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 3435909a-4ef6-3a7e-a12b-61bee40bca09 | -9.2475 | -57.0894 | 2026-08-28 18:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 04dd9f57-040b-3566-83a9-39868c26b1d7 | -8.5783 | -54.7768 | 2026-08-28 18:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 143.6 |
| 50e7b983-02d0-3cb5-8b82-1485a3e06e77 | -10.498 | -64.5193 | 2026-08-28 18:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 088da312-26de-339b-90e7-aea89397d9fc | -9.7878 | -43.5506 | 2026-08-28 18:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 137.4 |
| b6a5f509-3ec9-3009-b119-0f0d4a04dc7b | -6.1841 | -57.7786 | 2026-08-28 18:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| f6157e8d-8e3b-33a3-bede-972ccf46f3f8 | -6.8569 | -59.4564 | 2026-08-28 18:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.4 |
| e55ead0a-ed19-3e96-8feb-9eb457a4b187 | -7.5845 | -61.3423 | 2026-08-28 18:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 202.1 |
| fd6b01fd-7711-3435-a000-dc410e6109bb | -10.7603 | -53.9769 | 2026-08-28 18:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 6d7d5198-6bb4-3fb9-8ddd-ba3775d242fc | -11.025 | -49.644 | 2026-08-28 18:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 8b335522-caef-3e7b-8178-653743b5657c | -7.9244 | -50.956 | 2026-08-28 18:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| e1898eb3-1cb8-38bb-841f-5aa9016fc395 | -6.5865 | -55.4346 | 2026-08-28 18:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| c20feba5-bca5-3119-9513-39d3d74d1b16 | -8.7947 | -50.06 | 2026-08-28 18:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 4da21e4c-e4d8-32d9-b8fa-98cf217a3da4 | -14.8814 | -52.6505 | 2026-08-28 18:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 633d243c-5626-393f-a1a7-74d1c8b9f50c | -4.3022 | -59.4634 | 2026-08-28 18:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| d04cbdb3-efa9-3539-ad56-33220b8c67fa | -9.8742 | -60.2569 | 2026-08-28 18:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 61e3184a-4ae7-3832-bbea-a20f28db19c7 | -10.5166 | -64.5186 | 2026-08-28 18:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 941e1471-5f72-3084-bc2e-44418caa9dca | -12.9054 | -59.8857 | 2026-08-28 18:10:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 433aa7e2-7de2-3aec-b191-22865a4ab8e5 | -6.2348 | -55.4915 | 2026-08-28 18:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 71d3f7ef-b676-35fe-8c4f-a572e119dbc3 | -8.631 | -66.5473 | 2026-08-28 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 83bf218a-668f-3e05-93a7-9122072974f1 | -9.4331 | -51.6716 | 2026-08-28 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 7f8e40d6-b73c-3e3c-81a8-2566747925d8 | -10.5593 | -50.4663 | 2026-08-28 18:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 346b839e-fab2-393a-b3fd-ad027e5c4086 | -14.8627 | -52.6106 | 2026-08-28 18:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 7e481a05-51db-3321-87c0-13322e4c8842 | -5.9996 | -57.8249 | 2026-08-28 18:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| bce30bba-d73c-374e-94dc-f89a3310ef6b | -9.4329 | -51.6926 | 2026-08-28 18:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 151.7 |
| c9015a34-da0f-383a-ba3c-788b9d3d8b87 | -8.0928 | -45.8354 | 2026-08-28 18:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 115c3ec9-c889-336a-8887-0fc7de2a313f | -9.1895 | -65.7863 | 2026-08-28 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| a9aa816b-149b-30e1-9f47-261efa9a6ab8 | -14.8821 | -52.608 | 2026-08-28 18:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 295.4 |
| b50d985e-0bd5-3bfe-96c7-ba14e7db46d2 | -15.6139 | -56.4103 | 2026-08-28 18:10:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 46c126ed-f0a9-3b99-83f8-5a99e8b6b00b | -14.3997 | -52.5862 | 2026-08-28 18:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 4195c04c-6b00-316a-b51c-e495db45340d | -7.5662 | -61.3049 | 2026-08-28 18:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 14182d1c-a80b-3145-b0ae-ab863d7aaf93 | -8.87 | -66.8935 | 2026-08-28 18:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |


[Clique aqui para ver as próximas entradas](README158.md)
