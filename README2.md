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
| 1c32063a-abae-3aa9-8923-c558dba08a14 | -10.2398 | -50.3497 | 2026-08-22 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 477d3cce-4e08-3845-8204-79b76506f2cd | -11.449 | -44.5587 | 2026-08-22 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 22e5dec5-8be7-3a3c-a28d-ce3bede0cc03 | -10.2776 | -50.3459 | 2026-08-22 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| fa1cb701-5a95-3492-867c-2e1aa8822d52 | -10.2395 | -50.3711 | 2026-08-22 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| ea689561-afc8-325d-8001-b65de0dbfbf6 | -8.5404 | -54.8398 | 2026-08-22 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 247.9 |
| 022e8a18-a571-3577-81f1-5281ae99853c | -8.522 | -54.8209 | 2026-08-22 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 273.1 |
| 1d51a6ee-cef3-3ac0-861e-f0d9a29af19e | -13.997 | -53.6853 | 2026-08-22 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 6a476b28-1434-37b5-b7fb-89082ee7fafe | -6.8593 | -59.0318 | 2026-08-22 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| f88171a6-dfc2-31e5-9e97-db91478770f0 | -5.7985 | -57.5402 | 2026-08-22 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 82a79dcc-cd8c-3fac-928a-3a46c4021fe8 | -10.2773 | -50.3673 | 2026-08-22 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 471df0f0-4ee4-36a3-a945-c824bc09995c | -8.5406 | -54.8197 | 2026-08-22 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 279.2 |
| d2230493-61f5-3cdf-9286-aaadc1a551cd | -10.2584 | -50.3692 | 2026-08-22 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 550cbe2c-3464-3ce8-9fc3-aed23f0a14fb | -5.9997 | -57.8054 | 2026-08-22 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| c9b942a1-b9ba-3743-a258-cea70140d18a | -6.8188 | -59.6696 | 2026-08-22 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 8a18d7bb-5e8f-3847-9d9f-12b702d391c5 | -11.4298 | -44.5615 | 2026-08-22 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| a68dd2f0-63c6-3da2-9421-6a95788c9f1b | -10.2587 | -50.3478 | 2026-08-22 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 245.7 |
| 04c225b9-f824-33fa-9485-b16eec10f5f7 | -6.3863 | -54.9451 | 2026-08-22 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 844b6159-d474-37fc-b203-f3922a82285f | -6.3678 | -54.946 | 2026-08-22 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| a8da0c4f-5ce2-3190-9bbb-88a60ca31b18 | -6.8778 | -59.031 | 2026-08-22 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 2aea13ed-1c90-3c89-a8fe-967aeaf22b0f | -7.344 | -55.6741 | 2026-08-22 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| a1c1fb3f-f2d4-3a0d-b727-b35d686ca0fa | -4.9153 | -45.2527 | 2026-08-22 00:20:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| a367ba0d-ebe5-36e5-81f4-c8f409fbd343 | -8.8856 | -60.5394 | 2026-08-22 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 5cccf363-1740-3011-9236-2bc47eee93ac | -16.4773 | -47.9381 | 2026-08-22 00:20:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 2e16d919-f0bc-3670-8ba2-a186a6fcee9e | -6.2528 | -62.5236 | 2026-08-22 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| d06d378f-009b-3b80-8aae-28eb64b3d0e4 | -6.2712 | -62.5231 | 2026-08-22 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 0e13032a-1af4-3872-a96f-6a68c00f3420 | -8.9934 | -50.7427 | 2026-08-22 00:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 5380b249-bcc3-3fd4-b3f6-1a5984f6314f | -8.5218 | -54.8411 | 2026-08-22 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 235.4 |
| 32affce4-4d30-383c-8e5a-3822ed61b3fe | -22.01534 | -45.325 | 2026-08-22 00:24:00 | TERRA_M-M | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.0 |
| db89585a-6c32-3e06-996e-c2c458b0ef40 | -23.52196 | -47.32848 | 2026-08-22 00:24:00 | TERRA_M-M | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.6 |
| 07eee321-de6c-3b22-b182-f32f79235319 | -23.53292 | -47.32676 | 2026-08-22 00:24:00 | TERRA_M-M | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 9cc50422-d8c2-3f44-8ff3-5aa387288034 | -22.38556 | -48.40282 | 2026-08-22 00:24:00 | TERRA_M-M | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| aa16a64e-f5a1-37a4-9e22-e2af54db995b | -20.98188 | -47.34941 | 2026-08-22 00:24:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 576ae212-b2dd-31f6-b76e-59fb102a7611 | -23.82452 | -48.71463 | 2026-08-22 00:24:00 | TERRA_M-M | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 09f51320-ff98-3025-8ee1-ceb471f4ac02 | -22.01234 | -45.32008 | 2026-08-22 00:24:00 | TERRA_M-M | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.9 |
| 0b595dad-5bcd-3ad9-9836-466f286ab381 | -17.92429 | -44.41248 | 2026-08-22 00:26:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 62.8 |
| d9283ec4-9dc2-3921-afa5-1e61bc9f2751 | -12.00098 | -53.42546 | 2026-08-22 00:26:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 468436e9-a5bb-3729-ae44-fdf9d02afd27 | -14.98229 | -52.66909 | 2026-08-22 00:26:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 29c0eb4b-aaa9-378c-bb10-2787f6517f28 | -15.20296 | -52.79131 | 2026-08-22 00:26:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c6a78fcc-2d59-3393-afc0-412965446bd4 | -14.31965 | -52.99897 | 2026-08-22 00:26:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 9a4c4dff-e2dc-3262-bd77-45ddd7fd5fc8 | -15.51764 | -45.87552 | 2026-08-22 00:26:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 39f99c90-a4b9-3953-a6b0-beb64ce14599 | -11.60466 | -46.56515 | 2026-08-22 00:26:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 582ffdc5-5d03-3e25-98c6-b26f50c20e8b | -13.38877 | -54.37176 | 2026-08-22 00:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8b13471d-800b-308c-b908-8ad4ace184fe | -13.94088 | -53.84731 | 2026-08-22 00:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3fd13d7f-1035-32e5-a1b0-e3f4d21096d6 | -14.12871 | -48.06814 | 2026-08-22 00:26:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 05c3b218-9e4e-3b01-b84f-39e8dc18bae7 | -11.5994 | -46.54409 | 2026-08-22 00:26:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 579bdc5e-e21e-346e-8793-cab54480a237 | -14.18443 | -53.02248 | 2026-08-22 00:26:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 46fe2b70-cf41-3307-a180-ae272f333602 | -14.00495 | -53.71113 | 2026-08-22 00:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 05a35447-735c-3175-93c6-293eabf6ada7 | -18.71162 | -47.58219 | 2026-08-22 00:26:00 | TERRA_M-M | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 8bc6488e-a67f-3607-b592-cb66d622da68 | -16.48415 | -47.95258 | 2026-08-22 00:26:00 | TERRA_M-M | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 25703b7c-5689-35f4-98bc-3894a875c387 | -13.991 | -53.67603 | 2026-08-22 00:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 3a0af2f8-1a44-31b0-903b-3aaa3325cdd4 | -14.14103 | -48.06554 | 2026-08-22 00:26:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 86f5ff4f-7f6c-3864-b56e-d145f75142be | -16.4932 | -47.93337 | 2026-08-22 00:26:00 | TERRA_M-M | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 55b459bd-af11-3679-8b26-cad7a9b568e2 | -16.49952 | -55.18808 | 2026-08-22 00:26:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 1c08f7bc-62f7-34b3-9e53-79d0e436bcfe | -13.83377 | -53.99919 | 2026-08-22 00:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 37519471-30eb-3145-b16b-404912d36881 | -17.96606 | -42.71577 | 2026-08-22 00:26:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.2 |
| 49d61a29-df44-3f8b-aea7-f55c7e695d5c | -14.40804 | -43.79546 | 2026-08-22 00:26:00 | TERRA_M-M | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 40d16ba7-751f-30b7-bfcf-8a243f3f968c | -15.74561 | -56.5403 | 2026-08-22 00:26:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9d1a438d-0f27-3fe6-bfdc-2037a365401e | -13.95097 | -53.85507 | 2026-08-22 00:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ca4634e2-ee08-3f9f-b145-b381f528eb41 | -11.62901 | -46.53156 | 2026-08-22 00:26:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 37ce32b7-fad9-3fc1-aa56-023a6ddef3f7 | -16.48125 | -47.93554 | 2026-08-22 00:26:00 | TERRA_M-M | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 33.1 |
| b9ed192c-b10e-3864-8d29-bedea341e9bf | -13.99985 | -53.67471 | 2026-08-22 00:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 4978affc-00e3-3320-8290-247fba5c7d68 | -16.57762 | -48.50694 | 2026-08-22 00:26:00 | TERRA_M-M | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e3192b3e-f56c-31fc-8f2b-b049f2dee3c1 | -17.6861 | -44.45064 | 2026-08-22 00:26:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 6fe56c35-3967-39c2-a18f-8556f2f5e831 | -11.44377 | -44.54456 | 2026-08-22 00:26:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 95f2c24f-0798-3cd1-8903-24f8b1254c57 | -17.56131 | -47.88177 | 2026-08-22 00:26:00 | TERRA_M-M | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 99ce098d-e01d-3a93-a162-0c789d69b379 | -14.00113 | -53.68382 | 2026-08-22 00:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5fa292a8-eb93-3903-a8af-966167cce465 | -11.62868 | -46.5386 | 2026-08-22 00:26:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 236aa2b2-bfdf-33f9-b1b0-b6527d434f9f | -18.53229 | -48.24482 | 2026-08-22 00:26:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| e0a30ae8-0e02-37eb-9509-141c3602959f | -14.01252 | -53.70069 | 2026-08-22 00:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c9b761c8-7403-36ea-9f62-66168d4a447a | -14.32027 | -51.87671 | 2026-08-22 00:26:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a7a73e8c-edad-38df-bb4a-672032932e59 | -15.33188 | -52.91925 | 2026-08-22 00:26:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| be102539-4cfe-3ac9-9ccd-6342d2ca26c4 | -13.98343 | -53.68646 | 2026-08-22 00:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cb81cba8-b120-3504-9bc0-c2177788bb9f | -18.07973 | -46.95365 | 2026-08-22 00:26:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 2befa711-ed8d-399a-9805-c1a683e16f2e | -12.77461 | -48.39994 | 2026-08-22 00:26:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 767552cc-51de-3775-a81a-968745792f55 | -13.99228 | -53.68513 | 2026-08-22 00:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 97d8e7a0-a900-39f0-8ec4-0f152a302fe5 | -14.17545 | -53.02385 | 2026-08-22 00:26:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 5690ca9c-d2b0-3393-a570-b570800d11e8 | -17.5705 | -47.89095 | 2026-08-22 00:26:00 | TERRA_M-M | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 48b1c1e4-4136-361b-96ba-3cd340d90d6e | -11.59972 | -46.53699 | 2026-08-22 00:26:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 48.6 |
| dc7d2067-ce5a-355e-b8dc-61aef97b75ed | -15.21196 | -52.79001 | 2026-08-22 00:26:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 80ef9a98-8e6b-3738-bfdd-58c623ca8a87 | -14.31068 | -53.00036 | 2026-08-22 00:26:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 50385a93-ca8a-37a4-992a-27ae7fc84f3a | -11.45096 | -44.58406 | 2026-08-22 00:26:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 18a767a9-67e0-363c-aa46-662d21093834 | -12.54855 | -54.76669 | 2026-08-22 00:26:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5ae7e4c0-a352-3cdc-8a64-5dd4eb303099 | -14.55134 | -53.00891 | 2026-08-22 00:26:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b3c25867-fb60-37ef-bf0f-96aa78503c25 | -12.00998 | -53.4241 | 2026-08-22 00:26:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 13145bde-427e-3980-b8c7-843911cc9898 | -14.00368 | -53.70203 | 2026-08-22 00:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0479da2d-a124-31d5-b3e0-c2fa054a9e0c | -18.53486 | -48.26047 | 2026-08-22 00:26:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| d81e33e3-b08b-343f-845b-24b77e00b060 | -15.33322 | -52.92861 | 2026-08-22 00:26:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8f3584f8-4637-3ef5-bdbb-1ea3417d8574 | -13.82495 | -54.00048 | 2026-08-22 00:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 99eec079-f1c2-323b-83bc-d4dcb390d2ec | -12.01131 | -53.43349 | 2026-08-22 00:26:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 43be7cf6-aef8-3b66-9af0-fa88ae7264c3 | -18.07626 | -46.93387 | 2026-08-22 00:26:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 90fcbb3e-3b1f-3e2e-8066-feb6849f89db | -16.48713 | -47.97006 | 2026-08-22 00:26:00 | TERRA_M-M | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b82592bc-b26e-3086-809d-851de211239b | -13.52704 | -58.13036 | 2026-08-22 00:26:00 | TERRA_M-M | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 484a03c7-5065-3dde-a601-9908dc62e180 | -13.82369 | -53.99142 | 2026-08-22 00:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 84f3767f-4de5-3acd-8a99-d8e18e0588e6 | -11.44818 | -44.59159 | 2026-08-22 00:26:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 4217a31d-fac2-38a2-9042-48b8603a8aac | -13.84259 | -53.99785 | 2026-08-22 00:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5c30f6c4-f27d-3a49-ad44-f944cbd1adc9 | -12.77277 | -48.40631 | 2026-08-22 00:26:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 1e15b10e-47a2-39d1-823e-de258e5cf8f3 | -13.99355 | -53.69424 | 2026-08-22 00:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 28074c96-83cb-3f0e-869f-d875aca6ce55 | -13.98215 | -53.67735 | 2026-08-22 00:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 2546e232-6b91-3871-8ffb-6371d12704da | -14.32101 | -53.0084 | 2026-08-22 00:26:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 0e8465db-e391-3768-bf61-c271e7d9671b | -11.44124 | -44.55202 | 2026-08-22 00:26:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 161.5 |


[Clique aqui para ver as próximas entradas](README3.md)
