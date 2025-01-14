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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0ac4361-0114-3430-9b98-4e99914480cc | -28.77857 | -55.61547 | 2025-01-14 04:01:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 10.7 |
| f8c75eef-6509-3fad-92b3-108aed3b1f55 | -28.77411 | -55.60918 | 2025-01-14 04:01:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 10.7 |
| 07b5a86b-2b4a-3193-a238-c1d5c2393f87 | -30.36315 | -52.30837 | 2025-01-14 04:01:00 | NOAA-21 | DOM FELICIANO | RIO GRANDE DO SUL | Brasil | 4306502 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 65cb7e93-8e72-346e-8a47-92396f4a4c50 | -28.77967 | -55.61103 | 2025-01-14 04:01:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 10.7 |
| 9296cec7-fe6e-3719-85f9-4658fce65fd8 | -29.70003 | -51.35945 | 2025-01-14 04:01:00 | NOAA-21 | CAPELA DE SANTANA | RIO GRANDE DO SUL | Brasil | 4304689 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 515c329e-90e6-3b18-8fc7-9cb171ceea0c | -29.73637 | -53.87352 | 2025-01-14 04:01:00 | NOAA-21 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 4.4 |
| 4ceba2c8-8d66-3b7c-96c6-0cc6fa5f7692 | -27.44752 | -48.44315 | 2025-01-14 04:01:00 | NOAA-21 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 73f6377d-9735-34bf-abbd-bfc13ccbb3cd | -28.77521 | -55.60478 | 2025-01-14 04:01:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 10.0 |
| c6cab22e-cec7-34e9-ac15-5f3c03ad937a | -28.77859 | -55.63955 | 2025-01-14 04:01:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 7.1 |
| 40a5d40a-4293-3a3a-b79f-e23f49195c3b | -28.77969 | -55.63513 | 2025-01-14 04:01:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 7.1 |
| b0556dcb-5e1d-3962-9b82-03261ff940e3 | -29.7356 | -53.87677 | 2025-01-14 04:01:00 | NOAA-21 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| 78162e9e-9c22-3404-beaf-513f0a2f3bd8 | -28.77633 | -55.6244 | 2025-01-14 04:01:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 12.5 |
| a59ca4ec-3843-3cd1-8389-e06793b339db | -28.77522 | -55.62886 | 2025-01-14 04:01:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 9.6 |
| 4535aa36-8840-311b-aa54-b815c4874714 | -27.44962 | -48.44764 | 2025-01-14 04:01:00 | NOAA-21 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e43658d8-a171-3f39-b9ea-a06010e6190e | 1.3403 | -60.0461 | 2025-01-14 04:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 37e2be27-e56f-31e7-946d-a2f3eaef38f4 | -28.7817 | -55.6294 | 2025-01-14 04:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 72.5 |
| 97644299-8331-330b-80e3-d2ffa1851ffa | 1.3221 | -60.0463 | 2025-01-14 04:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 00230d5f-1f92-3bbd-b52d-81a0323c9ae8 | 1.3221 | -60.0272 | 2025-01-14 04:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 123.8 |
| cdfe46f0-c573-31a8-96d8-1985fa54ffe3 | 2.9463 | -60.179 | 2025-01-14 04:10:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 795f384e-3357-3a91-b1aa-6153be90a311 | -28.7824 | -55.6063 | 2025-01-14 04:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 78.6 |
| f2c40000-dd54-3772-9bd5-c3e0679fbffc | 1.3403 | -60.0271 | 2025-01-14 04:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 859a539c-6921-309f-ac39-b508d0be1297 | 1.3403 | -60.0461 | 2025-01-14 04:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.5 |
| d712777c-1f9e-3a9c-8734-3fb6c0fb2b53 | 1.3403 | -60.0271 | 2025-01-14 04:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 53135f1b-808b-3bb3-a63f-b43b1ff93c8f | 1.3221 | -60.0272 | 2025-01-14 04:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 100.3 |
| fb949191-99fb-33c4-902b-32119bc30d51 | 1.3221 | -60.0463 | 2025-01-14 04:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 131cc3ac-edcd-3523-9059-f5b5fe7f7b33 | -6.53853 | -35.27544 | 2025-01-14 04:21:00 | NPP-375D | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fd6ab324-0056-39d1-aed9-d3ea82238f63 | -6.54406 | -35.2763 | 2025-01-14 04:21:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4e08584e-90e0-32e3-943d-addb1fd7a0b3 | -21.45084 | -48.60803 | 2025-01-14 04:23:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 39c93fa6-5e8c-3081-871a-53fa602bec6f | -21.74492 | -48.45323 | 2025-01-14 04:23:00 | NPP-375D | NOVA EUROPA | SÃO PAULO | Brasil | 3532900 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32a41766-74d6-338c-9356-a40f35d2a047 | -21.74433 | -48.45696 | 2025-01-14 04:23:00 | NPP-375D | NOVA EUROPA | SÃO PAULO | Brasil | 3532900 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3651dc42-a0ad-3e7a-adbe-e8112c559a4d | -21.741 | -48.45636 | 2025-01-14 04:23:00 | NPP-375D | NOVA EUROPA | SÃO PAULO | Brasil | 3532900 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b33d93b-dca4-3219-954b-e22bec82f12e | -21.44751 | -48.60743 | 2025-01-14 04:23:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 4713365e-4f26-3406-89c4-85a8b5e8f595 | -22.11769 | -51.46436 | 2025-01-14 04:25:00 | NPP-375D | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7d9040a1-2439-33a5-9f19-c143635e0631 | -27.44858 | -48.44629 | 2025-01-14 04:25:00 | NPP-375D | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f26ac12d-637d-34df-b116-84dbdfe83d92 | -23.75119 | -55.41277 | 2025-01-14 04:25:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c1bd13f3-2adf-35b2-af11-227fa53c0471 | -23.40464 | -46.55474 | 2025-01-14 04:25:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 309d8e44-fad6-3625-8b85-fad3339a8984 | -29.00526 | -52.30883 | 2025-01-14 04:25:00 | NPP-375D | FONTOURA XAVIER | RIO GRANDE DO SUL | Brasil | 4308300 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c02503f0-a30e-308f-87c4-9501b78153b9 | -25.96897 | -52.60209 | 2025-01-14 04:25:00 | NPP-375D | CORONEL VIVIDA | PARANÁ | Brasil | 4106506 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cff4bed1-21a1-376e-983e-0646950f4537 | -24.82785 | -53.6201 | 2025-01-14 04:25:00 | NPP-375D | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 83a0059b-5445-3d98-92c6-5366cb9005ee | -25.97252 | -52.60285 | 2025-01-14 04:25:00 | NPP-375D | CORONEL VIVIDA | PARANÁ | Brasil | 4106506 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3884777c-c3fe-34bc-8d8d-b8d2f24d8d02 | -23.32548 | -46.70234 | 2025-01-14 04:25:00 | NPP-375D | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 46642a96-26bc-33bd-957f-189a085586b0 | -23.63072 | -46.42757 | 2025-01-14 04:25:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4b9a0cdc-9e18-34b4-82d2-4f623a90121c | -25.56678 | -49.36691 | 2025-01-14 04:25:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3bf0ce3c-d4f5-333f-a373-72da1053e268 | -23.71829 | -46.77182 | 2025-01-14 04:25:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2ce26f83-736a-379b-b9f3-9676a563d246 | -23.34026 | -46.77158 | 2025-01-14 04:25:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bc69f5f3-0e44-3772-b241-bd69edc79bd8 | -23.33681 | -46.77098 | 2025-01-14 04:25:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 84628fa6-9193-3cc7-8d76-83f5d727bfcd | -23.75546 | -55.41369 | 2025-01-14 04:25:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 983f3b6c-b942-39a0-9cb1-8e3c990d8bab | -22.54015 | -48.8124 | 2025-01-14 04:25:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e8c0567-e1a9-3e9a-a00d-fbf479cf6e19 | -23.73078 | -50.07187 | 2025-01-14 04:25:00 | NPP-375D | JABOTI | PARANÁ | Brasil | 4111704 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4dbfa568-4a7f-3bbf-99ea-724a9059fdbe | -27.7976 | -50.38138 | 2025-01-14 04:25:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5b959801-7eb5-3e52-a45b-1ed51217df02 | -24.15994 | -51.46069 | 2025-01-14 04:25:00 | NPP-375D | GRANDES RIOS | PARANÁ | Brasil | 4108700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0acee6c3-9c05-37e2-b655-8a0422cfc2ed | -23.9855 | -48.91652 | 2025-01-14 04:25:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4dfbc52-7a10-3489-9a27-2d38356d5d8f | -24.82828 | -53.62357 | 2025-01-14 04:25:00 | NPP-375D | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6516d06d-2605-3cab-bd45-837679468b43 | -28.76851 | -55.59703 | 2025-01-14 04:27:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| 13f655dd-3edd-33b9-a0d7-90ce20f3eb32 | -30.1172 | -52.07544 | 2025-01-14 04:27:00 | NPP-375D | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| d12d6f9f-f50d-3d2e-9276-ffdfbc02f242 | -29.69769 | -51.35735 | 2025-01-14 04:27:00 | NPP-375D | CAPELA DE SANTANA | RIO GRANDE DO SUL | Brasil | 4304689 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| e9985c8b-db0b-32ea-8e52-6fd38f727209 | -29.87361 | -51.15682 | 2025-01-14 04:27:00 | NPP-375D | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 4c0a3d5a-93a9-3fba-a37c-d94680b4a8bc | -28.77969 | -55.62406 | 2025-01-14 04:27:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 14.8 |
| a9a6bf4e-486b-368f-b894-c9b8808bc38e | -30.50717 | -54.04097 | 2025-01-14 04:27:00 | NPP-375D | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| cd1dfbf4-32f4-3408-bf0a-257f73bdfee8 | -30.36168 | -52.30749 | 2025-01-14 04:27:00 | NPP-375D | DOM FELICIANO | RIO GRANDE DO SUL | Brasil | 4306502 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 90e1a17c-1e0f-3e85-8fca-35ac9a58e163 | -28.77802 | -55.61158 | 2025-01-14 04:27:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 12.7 |
| 7c62366a-8447-366c-b063-a205a239212b | -28.78081 | -55.61834 | 2025-01-14 04:27:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 9.3 |
| 0a4a1959-9658-3076-a8a0-23125c96ea55 | -29.73397 | -53.87519 | 2025-01-14 04:27:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 3.6 |
| ab1c27fa-c7f1-3e41-b3b6-39180d1dbd93 | -28.77913 | -55.6059 | 2025-01-14 04:27:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 7.6 |
| 04c03d46-5a6f-3766-9010-6031653340b6 | -29.51517 | -51.94951 | 2025-01-14 04:27:00 | NPP-375D | ESTRELA | RIO GRANDE DO SUL | Brasil | 4307807 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4ff41527-1e18-3bef-add6-a1e5ebb5ec87 | -28.77409 | -55.61055 | 2025-01-14 04:27:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 12.7 |
| 4569a0ce-f450-3956-903b-4b149174469e | -28.77856 | -55.6298 | 2025-01-14 04:27:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 14.8 |
| 86559272-61b5-3479-ba2e-b9d98b70afe8 | -28.77689 | -55.61729 | 2025-01-14 04:27:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 12.7 |
| 067a798b-40f7-3690-86e9-59917be1fe81 | -28.7713 | -55.60379 | 2025-01-14 04:27:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| 100c6fa9-a10e-3354-8a2d-2f028a3de6fa | -28.77521 | -55.60485 | 2025-01-14 04:27:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 7.6 |
| 3464aa4d-a01b-3378-b3ce-72b4e2194d4c | -28.77633 | -55.64122 | 2025-01-14 04:27:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 4.9 |
| 10972b6e-60a7-3184-8a55-7a668ee2a885 | -31.42401 | -53.33561 | 2025-01-14 04:27:00 | NPP-375D | PINHEIRO MACHADO | RIO GRANDE DO SUL | Brasil | 4314506 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| a1c74635-e178-3575-8895-29130aa96314 | -28.77744 | -55.63551 | 2025-01-14 04:27:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 4.9 |
| 2a1291c6-8c1e-31ef-afa9-3380ba246dfb | -29.73482 | -53.87057 | 2025-01-14 04:27:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 4.6 |
| 23d3590d-77ad-350a-ab33-c26859b16e51 | 2.9463 | -60.179 | 2025-01-14 04:30:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 07734f69-3444-3883-954c-acf7e5eccee4 | -28.7824 | -55.6063 | 2025-01-14 04:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 78.7 |
| ab0dd86f-fa36-3a1e-842b-f9085b8d017f | 1.3221 | -60.0272 | 2025-01-14 04:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 19cb1c47-ede2-3e51-8aad-cfd4b0726da0 | 1.3221 | -60.0463 | 2025-01-14 04:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 104.3 |
| cecde567-374c-3a84-a769-25f108c4d010 | -28.7817 | -55.6294 | 2025-01-14 04:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 72.5 |
| cf2c25c2-4f3a-3809-a8f9-91ded496e5b4 | -28.7824 | -55.6063 | 2025-01-14 04:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 85.1 |
| 7ead5962-378c-33d7-a7d8-df747bc03203 | 1.3221 | -60.0272 | 2025-01-14 04:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 106.8 |
| f40d1b5d-e362-3f7a-bfc0-37d99a62e097 | 1.3221 | -60.0463 | 2025-01-14 04:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 109.5 |
| f9c97b24-3df7-365c-8d13-0ce509b955ce | 3.69234 | -60.06649 | 2025-01-14 04:40:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce4013e2-f9af-3c65-9c0a-6d07fea10020 | 3.69223 | -60.06811 | 2025-01-14 04:40:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dccc7cbf-5d09-38ad-96bf-d2b6a718845f | 3.69156 | -60.06339 | 2025-01-14 04:40:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47bfeb2e-9544-361c-9a2c-2ed02458e70a | 3.69163 | -60.06177 | 2025-01-14 04:40:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7486625e-e635-30fd-978a-3fa964b7fc33 | 1.31978 | -60.04293 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e70406e4-bdb8-359e-a4eb-695b71d92fdc | 1.32636 | -60.04626 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 442f04ea-852e-3792-bcac-cdc429aaaa7c | 2.18923 | -61.81639 | 2025-01-14 04:42:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a076ac65-f792-3dfa-aeb2-34dd74f66c3f | 1.31847 | -60.03418 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ecc614d5-386c-3cd8-a76b-c132463682ab | 1.32874 | -60.04492 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| de0954ac-d4ad-3259-b3f0-92b1cf02d71e | 2.95798 | -60.18625 | 2025-01-14 04:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c9a17fa2-43d7-3521-b42f-634d7da3adaf | 2.95183 | -60.18712 | 2025-01-14 04:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a16733c1-1a90-3383-ab0f-8fa7bbea744d | 1.18083 | -60.50092 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5adbfde0-275d-3bd5-8e0f-9d653fd41f28 | 1.31414 | -60.42725 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 66011453-05d1-3dd6-8f50-c781c4804b39 | 3.59817 | -60.94519 | 2025-01-14 04:42:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 349858ad-da21-3037-95bb-74047d713f3a | 1.17937 | -60.49167 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7220b3dd-10bf-36ad-927d-285be96e775f | 0.05547 | -51.62131 | 2025-01-14 04:42:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 286e5d46-946c-36b1-9c10-23938d0c54d8 | 2.95113 | -60.1823 | 2025-01-14 04:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ed04b89d-9925-39d7-9592-19dff8924a17 | 1.32282 | -60.04597 | 2025-01-14 04:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |


[Clique aqui para ver as próximas entradas](README4.md)
