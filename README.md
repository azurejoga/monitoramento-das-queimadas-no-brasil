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
| 0e9af060-442d-323b-8599-4e730ce2cf3d | -15.3626 | -46.935 | 2025-03-19 00:00:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 110.0 |
| c45c94eb-9953-3169-a15b-d6798c5cc8c8 | -13.2783 | -54.3469 | 2025-03-19 00:00:00 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| d6f5eea0-71c2-325f-a9fa-c592635e778a | -15.343 | -46.9385 | 2025-03-19 00:00:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 613c9846-2292-318f-9292-a9d796a813da | -15.3425 | -46.9614 | 2025-03-19 00:00:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 192.8 |
| 236f7baa-b241-3450-bfa1-c0a68fd8bad9 | -15.3621 | -46.958 | 2025-03-19 00:00:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 185.9 |
| c80580bc-4cab-3067-8ce6-37aaff743a76 | -15.38 | -46.97 | 2025-03-19 00:00:00 | MSG-03 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cb985d0d-8d39-3e89-a63c-7f8b67811aca | -15.35 | -46.95 | 2025-03-19 00:00:00 | MSG-03 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 40f34d07-3cd5-3945-82e2-0c13d799b944 | -15.32 | -46.94 | 2025-03-19 00:00:00 | MSG-03 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a293c44f-8cf0-3b0f-9579-45fd467c4557 | -8.98378 | -36.52781 | 2025-03-19 00:01:00 | TERRA_M-M | BREJÃO | PERNAMBUCO | Brasil | 2602407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 8a0824d5-0503-3590-a1ff-3ea5cfb7460e | -10.24677 | -37.27605 | 2025-03-19 00:01:00 | TERRA_M-M | CUMBE | SERGIPE | Brasil | 2801900 | 28 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| e5088c8e-c1e9-34a8-b0c1-6513323c4b99 | -13.8951 | -41.637001 | 2025-03-19 00:05:00 | METOP-C | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 16b6a245-c3c3-38d9-bb23-a2da0f0845e6 | -12.2955 | -43.5331 | 2025-03-19 00:05:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8fed97f4-a7c2-3363-8918-e83e69df2e75 | -15.3642 | -46.975201 | 2025-03-19 00:05:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e4a4f5de-bd3d-3492-9836-d9067b928b20 | -11.8679 | -37.590698 | 2025-03-19 00:05:00 | METOP-C | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 07646bd5-0d34-3ac9-b40e-34ac1d4dbe8d | -12.1554 | -40.286999 | 2025-03-19 00:05:00 | METOP-C | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7e1f5d61-89a7-3ff6-b627-0b3a023f9f84 | -15.3406 | -46.955399 | 2025-03-19 00:05:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2eb4f578-fca1-3c2b-afc0-2ac5bb666245 | -12.467 | -43.5746 | 2025-03-19 00:05:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3665de32-9025-3d5b-b16a-111c53f715d3 | -16.0902 | -40.886398 | 2025-03-19 00:05:00 | METOP-C | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 44ce7a93-fd59-31ed-a3c0-09d910de5851 | -12.1571 | -40.294998 | 2025-03-19 00:05:00 | METOP-C | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 11caad1b-41df-3806-90d2-56b23fdfcaa5 | -10.6609 | -44.398399 | 2025-03-19 00:05:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b3385398-5dd9-38f9-b3d4-89a556b595aa | -12.096 | -45.6199 | 2025-03-19 00:05:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d915ff9e-d3d2-310c-8031-b8443735db02 | -12.2931 | -43.520901 | 2025-03-19 00:05:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b3c42a90-385a-3794-a997-c5658b582830 | -12.4645 | -43.562302 | 2025-03-19 00:05:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 61b8ac28-756c-382e-a876-2c6826b0bf33 | -13.8972 | -41.6469 | 2025-03-19 00:05:00 | METOP-C | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 756077e0-32c6-34c3-917d-c4738ba6d3cc | -15.3364 | -46.932201 | 2025-03-19 00:05:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8cf8cc40-2506-3de6-a249-0571a6d3d761 | -15.3503 | -46.953602 | 2025-03-19 00:05:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1165e014-cd42-35f3-b887-27d741229da5 | -15.3545 | -46.976898 | 2025-03-19 00:05:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5ac38949-3283-3646-9a78-dc78e97e3d6f | -12.462 | -43.5499 | 2025-03-19 00:05:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3282326c-fc7b-32d2-a938-0fdd0b9b2306 | -15.2581 | -43.6614 | 2025-03-19 00:05:00 | METOP-C | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 99a2da1d-a613-359d-92a3-843b0eb96c78 | -9.78 | -37.6609 | 2025-03-19 00:05:00 | METOP-C | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | nan |
| 59ca9b3c-1357-32b1-b335-3b3b72bafbf6 | -15.3558 | -46.9286 | 2025-03-19 00:05:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8dd9e5d7-df2c-3d96-b794-81aa1f75bc61 | -15.3461 | -46.930401 | 2025-03-19 00:05:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 43a8f5b2-c018-3131-b2e0-db18011ccaa8 | -10.6582 | -44.3853 | 2025-03-19 00:05:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6c84d3a9-518c-3d0a-8e90-cb95662c23fa | -15.36 | -46.9519 | 2025-03-19 00:05:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 296edf65-3785-3b35-b2df-a38d6cd0ba19 | -10.2586 | -37.272701 | 2025-03-19 00:05:00 | METOP-C | CUMBE | SERGIPE | Brasil | 2801900 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8d2205ec-240e-3a1f-8fa5-2eb80ae83c67 | -11.8663 | -37.583801 | 2025-03-19 00:05:00 | METOP-C | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| face04e8-ddec-3393-8089-f19284e4200a | -13.8992 | -41.656799 | 2025-03-19 00:05:00 | METOP-C | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2f8204e1-7323-3b1d-8654-1ded00f82238 | -12.0862 | -45.621799 | 2025-03-19 00:05:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a623db0a-8edb-316c-8d18-a5b052e32ba4 | -15.3448 | -46.978699 | 2025-03-19 00:05:00 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e259308b-19aa-350a-9401-f262ea7edaf6 | -15.3425 | -46.9614 | 2025-03-19 00:20:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 8e0b9159-9eaf-3927-9de8-c3c3bd9d286a | -15.343 | -46.9385 | 2025-03-19 00:30:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 79.5 |
| af3317f1-147f-3e70-8e1d-e789e44056e6 | -15.3621 | -46.958 | 2025-03-19 00:30:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 103.3 |
| d87732e9-4c2a-3472-b616-bffd8c3bc048 | -15.3425 | -46.9614 | 2025-03-19 00:30:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 136.9 |
| a68570b1-2266-329a-9d1f-3010912976e6 | -15.3621 | -46.958 | 2025-03-19 00:40:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 97.7 |
| d839d694-a742-37cb-ae91-9044f6653ebc | -15.343 | -46.9385 | 2025-03-19 00:40:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 88.7 |
| ec3263d8-b108-33a3-b20e-b2845c3b8557 | -15.3626 | -46.935 | 2025-03-19 00:40:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 2b41bb68-fbd0-3771-af14-a019bf145200 | -15.3425 | -46.9614 | 2025-03-19 00:40:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 627acefa-efc1-3af2-800b-06b17d26e68d | -29.376301 | -49.764702 | 2025-03-19 00:47:00 | METOP-B | TORRES | RIO GRANDE DO SUL | Brasil | 4321501 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 2c0ecf9f-1083-36b2-84cf-29af2250cc05 | -12.1032 | -45.6129 | 2025-03-19 00:47:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 85ada93d-2d8e-370a-9cf7-313d7a589945 | -15.3595 | -46.936199 | 2025-03-19 00:47:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b876dae4-06e7-30d7-9914-1122cdcce3c3 | -13.2843 | -54.334702 | 2025-03-19 00:47:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e8fbd6be-bd3d-3fe4-b50f-58a41c315967 | -15.3656 | -46.919399 | 2025-03-19 00:47:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2366afba-f9b1-3fba-9c63-a116dceaf1c5 | -13.2957 | -54.3395 | 2025-03-19 00:47:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5179240d-5297-3743-8a97-6f8fec573295 | -13.2926 | -54.325401 | 2025-03-19 00:47:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec809a0a-1e90-3d75-a57f-84b9ab650595 | -15.3498 | -46.9389 | 2025-03-19 00:47:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 640f4531-c89f-3d29-8653-9825ab2dfbde | -15.3729 | -46.9478 | 2025-03-19 00:47:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 88093aa9-c218-3e96-9e43-67a190388efd | -13.0667 | -53.319 | 2025-03-19 00:47:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8b5b6de3-f616-32e8-b91a-669893dcec1c | -15.3535 | -46.953098 | 2025-03-19 00:47:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b1f1da2d-8454-3553-b06f-96a533309f00 | -13.2941 | -54.3325 | 2025-03-19 00:47:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4aeddf21-1c62-3576-8953-120b27b69355 | -15.3559 | -46.922001 | 2025-03-19 00:47:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f6b3d44d-7c94-3691-a12f-415dcf1135a3 | -13.2859 | -54.341702 | 2025-03-19 00:47:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4152086d-9347-3342-96e0-0433b9020e97 | -15.3692 | -46.933601 | 2025-03-19 00:47:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d87858cf-989e-3167-8b02-1140585397bb | -13.0683 | -53.326199 | 2025-03-19 00:47:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa5d4a32-f254-35a8-8fae-503488ff4b1c | -15.3621 | -46.958 | 2025-03-19 00:50:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 169.4 |
| ff37fa26-f5bc-3f0a-8942-9fb435472ef8 | -15.3425 | -46.9614 | 2025-03-19 00:50:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 820b041c-0528-3a7c-a716-50ebda086b4b | -15.343 | -46.9385 | 2025-03-19 00:50:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 6aefc69a-be0b-36b1-b885-2aaef2623d51 | -15.3626 | -46.935 | 2025-03-19 00:50:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 115.7 |
| ac2b7ab3-a2d5-3d77-aeb7-dfa4eca32944 | -15.343 | -46.9385 | 2025-03-19 01:00:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 31d9ee14-b0de-305f-8504-ee9535bd3a96 | -15.3621 | -46.958 | 2025-03-19 01:00:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 171.5 |
| 917719cc-5828-3c25-8c0c-6b1d6bc0bfcf | -15.3626 | -46.935 | 2025-03-19 01:00:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 7d003812-84bd-377d-89b6-d8e7a329cdbd | -15.3425 | -46.9614 | 2025-03-19 01:00:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 152.5 |
| e8275d1b-e271-3600-9d7c-d92a07c596bd | -13.2783 | -54.3469 | 2025-03-19 01:00:00 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 921b5f82-d55f-3c8d-a211-c8aa564f61ca | -15.35 | -46.95 | 2025-03-19 01:00:00 | MSG-03 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2df776fc-4284-309e-8f01-7c2c53555b0e | -15.34 | -46.9 | 2025-03-19 01:00:00 | MSG-03 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7f9480ec-379e-3af3-8f6d-c9b2c8d2e37f | -15.3425 | -46.9614 | 2025-03-19 01:10:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 8303fd46-312b-3c66-acac-55051e52108f | -15.3626 | -46.935 | 2025-03-19 01:10:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 104.0 |
| d715673b-e25e-3967-8fb2-f6d4f48846af | -15.343 | -46.9385 | 2025-03-19 01:10:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 3804924c-2bbb-3307-b128-78e105691a4a | -15.3621 | -46.958 | 2025-03-19 01:10:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 147.6 |
| d245137b-26a3-368c-be1d-f69381c29952 | -15.3425 | -46.9614 | 2025-03-19 01:20:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 86676e80-aded-3a85-9edb-1177f1ed7622 | -15.3621 | -46.958 | 2025-03-19 01:20:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 3e2a5c4b-7291-3c12-ad1c-1890af8e3288 | -15.343 | -46.9385 | 2025-03-19 01:20:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 104.6 |
| c11d7259-09d2-3e61-9b35-f6a928c6b2c3 | -15.3626 | -46.935 | 2025-03-19 01:20:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 0cd53546-6252-3213-a341-eb52801e7462 | -15.3425 | -46.9614 | 2025-03-19 01:30:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 8386b228-3d47-30da-88e4-c2a13611b584 | -15.3621 | -46.958 | 2025-03-19 01:30:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 150.4 |
| e003dad3-9688-3734-82e6-2af11f8c5e91 | -15.343 | -46.9385 | 2025-03-19 01:30:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 120.2 |
| a2723ce2-abe6-3437-8e49-cb0218208b61 | -15.3626 | -46.935 | 2025-03-19 01:30:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 2929b7b4-12dc-39d5-bafb-8cd4f5348eec | -30.35444 | -54.29248 | 2025-03-19 01:34:00 | TERRA_M-M | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 20.0 |
| e7bae23e-04b3-3986-a0f0-5c37438cdc13 | -29.76178 | -55.86366 | 2025-03-19 01:34:00 | TERRA_M-M | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 6.2 |
| bd0a441b-43d4-38e7-8995-3e3ce56b30ef | -15.59655 | -57.33928 | 2025-03-19 01:37:00 | TERRA_M-M | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 112c0d37-bb4e-3887-a394-de593d881dfd | -15.59488 | -57.32815 | 2025-03-19 01:37:00 | TERRA_M-M | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c53c53e8-e962-30be-ab45-7ba2f6328a5e | -13.26892 | -54.34014 | 2025-03-19 01:39:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 39.9 |
| f3cdaa8d-3fdc-3bac-a8c8-85876ced4641 | -13.28144 | -54.33789 | 2025-03-19 01:39:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 40b45f92-ce79-328a-9bc1-ccb42f274cb6 | -13.27212 | -54.35965 | 2025-03-19 01:39:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2d28da9f-5ac6-3169-9f83-4b6f3b04a5b0 | -15.3621 | -46.958 | 2025-03-19 01:40:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 673d959f-f461-3866-acf8-4156667347b8 | -15.3425 | -46.9614 | 2025-03-19 01:40:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 191.9 |
| 36bf9bfa-4516-32b5-93ad-9eed6b9f4b2f | -15.3626 | -46.935 | 2025-03-19 01:40:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 131fe8c0-c604-3dc7-9c6e-e971e58de39f | -15.343 | -46.9385 | 2025-03-19 01:40:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 381fc479-61fc-394e-b2cc-929ac34d21e4 | -30.3729 | -54.293301 | 2025-03-19 01:42:00 | METOP-C | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | nan |
| d30cbb71-2ef6-3920-9674-d58c507e035c | -30.370501 | -54.283401 | 2025-03-19 01:42:00 | METOP-C | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | nan |
| a668f368-6bc1-34ba-871d-52b166dfd16d | -15.3621 | -46.958 | 2025-03-19 01:50:00 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 164.8 |


[Clique aqui para ver as próximas entradas](README2.md)
