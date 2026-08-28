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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05527af4-d4e2-3036-9c48-c1c5c53ea04b | -11.6603 | -46.7239 | 2026-08-28 02:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 47ac8fe7-02ad-37a7-b3f5-f1b55a332da6 | -4.8397 | -45.3926 | 2026-08-28 02:30:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| b2860b0f-50ee-3cd0-867b-fd291814671b | -12.4305 | -43.3944 | 2026-08-28 02:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 60bab7d1-e2a6-31bb-9134-df876f92d920 | -10.4082 | -61.23 | 2026-08-28 02:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| ef821606-9846-3450-a829-56116fc6c61f | -16.1641 | -58.5851 | 2026-08-28 02:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 270.0 |
| 335a1a7d-6054-37a0-a66c-d05c522886ee | -10.3895 | -61.231 | 2026-08-28 02:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 174.0 |
| 9dd384e7-3fcd-378c-aa6c-9b60ab3710ef | -10.3894 | -61.2502 | 2026-08-28 02:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 220.0 |
| 288e794f-f98f-3148-afc2-c5acfb714c0e | -7.2661 | -45.8443 | 2026-08-28 02:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 4ab556a5-88b5-3649-bf57-6fd54085bc8d | -16.1447 | -58.5871 | 2026-08-28 02:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 162.1 |
| 780b3936-71a4-37c4-bac6-a7e311a940a6 | -15.5403 | -41.9175 | 2026-08-28 02:30:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.5 |
| 83e738fa-0c31-3ce1-a6a2-e019895cd855 | -14.8627 | -52.6106 | 2026-08-28 02:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 163.9 |
| cf94ea80-9250-31c2-824e-d5ac21ce8f10 | -12.4305 | -43.3944 | 2026-08-28 02:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 8a979431-0924-3d66-9b59-624edffeff87 | -16.1447 | -58.5871 | 2026-08-28 02:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 149.1 |
| cf7fbddc-845c-3d23-8a86-f3091319e3a5 | -10.3894 | -61.2502 | 2026-08-28 02:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| a80801fc-5be2-3319-b662-1ec224bc9f79 | -7.2659 | -45.8668 | 2026-08-28 02:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 170.0 |
| 5017b209-63fe-3bf6-99df-7d31d9ef9654 | -11.585 | -45.5311 | 2026-08-28 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 154.0 |
| fcac2a41-02a0-3b7b-97ad-9235d26ca494 | -16.1444 | -58.6073 | 2026-08-28 02:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.6 |
| 9c9f0756-39e6-3a49-b935-9e76f45c97c1 | -7.8828 | -46.1028 | 2026-08-28 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 00ec097c-c2c0-3fc4-94d2-c1ece06e1b49 | -10.7596 | -54.0384 | 2026-08-28 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| d2e37308-afd8-38a7-93f1-f335f7538d4c | -11.2882 | -54.0111 | 2026-08-28 02:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 47854e90-ed65-39ce-877f-c376e078e8e6 | -11.2317 | -53.9958 | 2026-08-28 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 36aa17d7-269a-373e-bc2e-37bb7075fc92 | -11.8239 | -47.2178 | 2026-08-28 02:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 67a2a5fb-756f-3e39-aca3-2444a6e26047 | -6.184 | -57.7981 | 2026-08-28 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| c2535321-9864-3df6-afd3-48405dbcd092 | -10.3895 | -61.231 | 2026-08-28 02:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 8fa12708-e637-3cc1-b2b4-551aa56edccd | -6.1656 | -57.7988 | 2026-08-28 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 015d3b59-cc75-33a6-a9f6-25f7fec8da87 | -11.5659 | -45.5338 | 2026-08-28 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 87561f2a-7166-3dd0-88d0-f2b60471e0ec | -4.8397 | -45.3926 | 2026-08-28 02:40:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 6bf4e583-90b5-39c5-9879-b39572449e4c | -7.2661 | -45.8443 | 2026-08-28 02:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| bd457be3-f20d-3731-b9e6-745306b3e13f | -6.1657 | -57.7793 | 2026-08-28 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| e7b51d78-4728-3117-bf5b-575e8d0dddf8 | -7.2474 | -45.846 | 2026-08-28 02:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 128.2 |
| c81aa43a-18d3-3032-87f2-f5449a9a84fd | -16.1638 | -58.6053 | 2026-08-28 02:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 122.3 |
| 764e23b8-6d59-38e5-bef0-e220819b62d3 | -11.2879 | -54.0317 | 2026-08-28 02:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| f93c123f-fb2c-31b6-8726-379a1e032671 | -8.5969 | -54.7755 | 2026-08-28 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 132552aa-ef38-3d61-9a1e-998c0dc22bf6 | -10.4981 | -64.5005 | 2026-08-28 02:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 0603801d-44f8-3526-a557-3049495017c0 | -12.43 | -43.4182 | 2026-08-28 02:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 6bbda69c-c3cd-3849-9bf4-08f62310b8ca | -15.5403 | -41.9175 | 2026-08-28 02:40:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 75.3 |
| 9b69ad50-c6be-3006-b660-996c5ccec697 | -6.1841 | -57.7786 | 2026-08-28 02:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 7e3f01ae-f118-39a6-a0e4-92257da35f8c | -4.8583 | -45.3915 | 2026-08-28 02:40:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| ee33e417-d8c2-3ae9-9135-2b3f1362af96 | -7.2471 | -45.8685 | 2026-08-28 02:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 211.3 |
| bf6f340e-31ba-39b8-918d-2d81efe4456c | -16.1641 | -58.5851 | 2026-08-28 02:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 203.5 |
| 63c31bbf-53e4-30f0-8d8a-67ad8526a17d | -12.4305 | -43.3944 | 2026-08-28 02:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 3d1d8c3c-c2ed-352d-91a6-bac00495b90e | -7.8831 | -46.0804 | 2026-08-28 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 1e58f9e2-1165-38df-8602-bc49e7eeccd4 | -16.1644 | -58.565 | 2026-08-28 02:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.3 |
| 02d4d51c-fecd-3859-b5b5-605b9d7e83fc | -4.8397 | -45.3926 | 2026-08-28 02:50:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| afaab2c9-71ae-39cc-b637-e06d6cf2aab9 | -10.3895 | -61.231 | 2026-08-28 02:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 241e382e-62ec-3948-8875-b579c03b49ab | -16.1447 | -58.5871 | 2026-08-28 02:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 173.9 |
| c01a1014-2f47-3992-b5c5-7f134275d7b3 | -10.4981 | -64.5005 | 2026-08-28 02:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 71.7 |
| bdb48c31-5756-3f4b-8e75-95af2492db8f | -6.1472 | -57.7995 | 2026-08-28 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 30af4570-afa2-39b4-ab98-9ea15ae9e45d | -16.1638 | -58.6053 | 2026-08-28 02:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.4 |
| a1072070-8f93-3533-bf81-f83442778e54 | -8.5969 | -54.7755 | 2026-08-28 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| ffe87eae-279d-356b-a656-be1e4d924b43 | -6.1473 | -57.78 | 2026-08-28 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| feaacfff-cd56-34cf-aa98-78cd908c7a45 | -16.1444 | -58.6073 | 2026-08-28 02:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.3 |
| 0b57fae3-dcb6-39a7-84f4-e7adbad9aba8 | -6.1656 | -57.7988 | 2026-08-28 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 136.4 |
| 46bb3079-9f35-38ee-b100-a4aa14f99246 | -10.3894 | -61.2502 | 2026-08-28 02:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| add47fc3-95e1-30b4-935f-c208b5900403 | -4.8583 | -45.3915 | 2026-08-28 02:50:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 483636d2-d189-33c8-8485-80cb2a0c946b | -11.269 | -54.0334 | 2026-08-28 02:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| f9aa3e1d-db2d-3de3-ba79-1c4c10ef792a | -11.8239 | -47.2178 | 2026-08-28 02:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 558fb316-f1e7-3e37-bea7-8562ddca8d9b | -7.2471 | -45.8685 | 2026-08-28 02:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 183.7 |
| 8bd10887-7132-3a6e-96d2-c8e7b862e3ba | -14.8627 | -52.6106 | 2026-08-28 02:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| c90cbfc4-0150-3e18-8ec2-280de836a9fe | -6.1657 | -57.7793 | 2026-08-28 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 88e28695-aa75-349b-8dbe-681f2685388c | -7.8828 | -46.1028 | 2026-08-28 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 4d7d011c-1cd8-3f23-8a9e-14f8b478ccbe | -11.585 | -45.5311 | 2026-08-28 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 05059a90-2d81-368c-8639-5d5b212c82bd | -11.8243 | -47.1954 | 2026-08-28 02:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 1c7f3a22-847a-30f4-9c02-ff2dc25a6908 | -14.8825 | -52.5868 | 2026-08-28 02:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 274.8 |
| e2b2d5f2-42cd-3802-89f2-f2e020978387 | -10.7596 | -54.0384 | 2026-08-28 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 1bb00866-5967-382c-8a2e-8eb1ed314649 | -7.2659 | -45.8668 | 2026-08-28 02:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 6b8f6e59-c22c-356b-955f-a4a9015b14fa | -7.2661 | -45.8443 | 2026-08-28 02:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 4857363f-3f5c-3e9a-afd1-061ed357ee95 | -14.9019 | -52.5842 | 2026-08-28 02:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 287.7 |
| fa6206bd-21a7-3a57-9597-bf3e7acbbc0c | -15.5403 | -41.9175 | 2026-08-28 02:50:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 62.6 |
| 98816a99-501a-308e-9089-caf0edeb7921 | -11.2879 | -54.0317 | 2026-08-28 02:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 3dc6bb6f-fa6e-3c09-be61-3b2cfe3ca085 | -12.43 | -43.4182 | 2026-08-28 02:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 5c7f1bd8-56c2-3467-b7b7-9ced8a1f0c7f | -14.8821 | -52.608 | 2026-08-28 02:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 2bca6d9c-7243-38a9-951e-4dc01e7eb481 | -7.2474 | -45.846 | 2026-08-28 02:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 8159a8a5-96cd-3735-8b49-d314026c9f74 | -14.8631 | -52.5893 | 2026-08-28 02:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 883307c7-08b7-3115-af1d-a2bd8f5efc0e | -11.2882 | -54.0111 | 2026-08-28 02:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 296e602f-d707-3842-b814-07840a5b4dfa | -16.1641 | -58.5851 | 2026-08-28 02:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 274.8 |
| 65b56ce5-ffcf-37b3-99ed-ae4911818484 | -14.9015 | -52.6055 | 2026-08-28 02:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 190.8 |
| f2b47c1e-0942-3782-937e-5c4900f0ec4e | -10.7596 | -54.0384 | 2026-08-28 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 9bb1bd9d-4b65-3419-8e6f-b242ea847f98 | -6.1472 | -57.7995 | 2026-08-28 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| bf0ddd3e-f456-3b3b-a025-577fc82199e6 | -6.1657 | -57.7793 | 2026-08-28 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| ace91ecf-0da2-3bb9-95c1-8a94968779e9 | -12.4305 | -43.3944 | 2026-08-28 03:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 7bacd5bb-6d96-3d17-b33e-6f82dca3b806 | -7.2471 | -45.8685 | 2026-08-28 03:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 4bf7a273-9cf0-3b77-8051-b111cf945df5 | -16.1641 | -58.5851 | 2026-08-28 03:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 333.8 |
| 30ef1c21-1a95-3e4b-a94d-91a430ce106a | -7.2474 | -45.846 | 2026-08-28 03:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 107.1 |
| bb49bddf-b8b1-305d-9425-4a8413dbf869 | -14.8825 | -52.5868 | 2026-08-28 03:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 0416ea4b-6af9-354b-88a4-c3ac36565459 | -6.1304 | -47.2224 | 2026-08-28 03:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 8f665592-7437-3371-a06a-6290e90472f9 | -4.8583 | -45.3915 | 2026-08-28 03:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| ecae9731-504c-391b-af8c-5f48b058796e | -7.2661 | -45.8443 | 2026-08-28 03:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| a78e0c0c-e067-3310-b2ec-3eab53147828 | -14.9015 | -52.6055 | 2026-08-28 03:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 456096a1-75d9-3556-b71d-e043fd402f6c | -12.2656 | -50.5961 | 2026-08-28 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| b4d41197-b58d-31eb-9128-42239e35f5c1 | -4.8397 | -45.3926 | 2026-08-28 03:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| e82dee05-f701-3350-b01a-ddaa25c249f2 | -16.1836 | -58.5831 | 2026-08-28 03:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.7 |
| d53042c6-7b13-350c-8dbb-aeabebf1e93d | -16.1644 | -58.565 | 2026-08-28 03:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 361fe2b8-0682-368b-8fdf-b0a16d116b1b | -16.1447 | -58.5871 | 2026-08-28 03:00:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 197.1 |
| 35c5440c-96b1-3bfb-bcc9-63dddc4c2acc | -12.43 | -43.4182 | 2026-08-28 03:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 4aa36ab0-95c7-379f-83f1-a876301ba8f3 | -7.8831 | -46.0804 | 2026-08-28 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| ab44a34d-81a1-3ff8-9fd2-0b9040c4f935 | -11.2879 | -54.0317 | 2026-08-28 03:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 6a980f78-b02a-3739-afb7-5863d851029d | -10.4981 | -64.5005 | 2026-08-28 03:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 83.8 |
| fc60f9ba-2368-3749-bdb4-f1f9e5634ad0 | -8.5969 | -54.7755 | 2026-08-28 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 9a7f6cab-8899-3626-9564-6911140dc148 | -11.585 | -45.5311 | 2026-08-28 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |


[Clique aqui para ver as próximas entradas](README12.md)
