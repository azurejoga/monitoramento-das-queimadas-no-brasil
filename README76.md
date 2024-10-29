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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1813acf5-0841-3ca0-805d-21dca15b1ce7 | -4.62505 | -50.63853 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3932a406-b109-3d33-acd0-439360152d9d | -4.60558 | -50.56112 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d0bec017-af2f-373f-b0eb-811104b2c39e | -4.60244 | -49.38819 | 2024-10-29 05:01:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c18244b0-6be6-385e-baeb-5dcff2cb3bf5 | -4.59102 | -50.65704 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 907f4430-c142-3cac-9870-7b7cfee63904 | -4.51334 | -49.66104 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86101ba3-09f4-3fe2-949f-a0c22448610f | -4.51162 | -50.49865 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64f74b09-fcaa-34b7-bb30-782833503558 | -4.51086 | -50.50368 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fcac618a-7eb0-3f2e-999f-e16c91d19d17 | -4.50864 | -50.75509 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12b9ee39-50f0-392b-b7a2-ddea9adae2f9 | -4.46222 | -49.71616 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d026f37c-071f-3482-99b1-a86a6dc49f40 | -4.42452 | -50.46785 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23b0d662-8ced-3073-95d6-5eee465c7e00 | -4.42374 | -50.47297 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 275fcd0b-0d97-3524-aa46-b58dd03d33a6 | -4.41275 | -49.78635 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d52c16c2-e026-36bb-b109-95adfcbe9208 | -4.39228 | -49.75245 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddf22e3a-9915-3f37-9cd5-eee0ae2cd64f | -4.38753 | -49.75564 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0dae5df-407a-3262-8afd-6e20baf82b1d | -4.15542 | -50.22426 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a8f139f-fafe-3ea3-ae41-a6ca98ffd80c | -4.13846 | -50.2257 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2c0d384-9473-3c37-8c40-f3965ae87c6b | -4.10408 | -50.52822 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 661788da-8b83-3bf9-860d-19eb5ecfca99 | -4.10303 | -50.52448 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8188151e-ff63-3ad5-93a6-3f739f158718 | -4.10228 | -50.52956 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7a38e540-8ca1-3ccf-9928-d0ed02b5547f | -4.10092 | -50.52251 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8457cd04-f8dc-3ec5-9cd4-070d795f4054 | -4.10014 | -50.52757 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 66bf07df-cf8d-3ca7-aabe-6d8929d54bf0 | -4.09936 | -50.53259 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8de08fd9-f078-351b-a73e-e898c768634a | -4.09908 | -50.52383 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0de50d60-2bb0-3d1b-94e7-e26e93b1df1c | -4.09834 | -50.52888 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3df173b3-fbb2-3a9d-bbba-0c36d784cb49 | -4.0976 | -50.53391 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 46c4f369-4745-3e75-809c-491f4ad3933f | -4.09542 | -50.53196 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66acf0dd-db24-34e4-924d-105f466032be | -4.09513 | -49.98961 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 53684558-7d62-31d5-af86-90e248ea6b01 | -4.09459 | -49.99325 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 673c16dc-b833-3448-87d3-bc83f6709280 | -4.07399 | -50.01958 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57b34762-64ec-35e5-b56d-9c1f88aff510 | -4.06871 | -50.0303 | 2024-10-29 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed5c0428-61ed-30f1-9c25-fe3c9229a425 | -4.06816 | -50.03391 | 2024-10-29 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59bdda81-22e2-3f04-a837-94475473cc27 | -4.06518 | -50.02615 | 2024-10-29 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52df87bd-bcf7-393a-a6fd-a81cff192114 | -4.06462 | -50.02978 | 2024-10-29 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1bc39b2b-bb4e-301e-ae6d-7407399dae7d | -4.04272 | -50.55989 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f698cbc5-2d7c-3576-a21e-6829abc4e1ac | -4.03953 | -50.55428 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e6d7a57e-c029-35a9-a575-7c3f83f9a426 | -3.9375 | -49.96696 | 2024-10-29 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8e74e62-1e4e-3e2e-814a-72a2ad3fb0ec | -3.93395 | -49.96279 | 2024-10-29 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c62684d3-5a4c-3757-9e2c-bf2133a84ca7 | -3.9334 | -49.96638 | 2024-10-29 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62791f3f-935f-3a9a-9cb3-e8fd6272c0f0 | -3.90235 | -49.75144 | 2024-10-29 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dae4283f-59e0-3e8a-8bef-6201738c06cd | -3.90181 | -49.75517 | 2024-10-29 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0cc6805-9fde-3cf1-91bc-f980f9447797 | -3.90051 | -49.75094 | 2024-10-29 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb40e1bf-68c3-3843-a609-6ab34f7e3d60 | -3.89993 | -49.75467 | 2024-10-29 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1468881-d4a5-3f29-89a5-1d6950821fd4 | -3.89136 | -50.0517 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e2a86701-8563-3386-a7bc-c0b5486c7a96 | -3.89082 | -50.0553 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1e63a824-4c9e-3cde-bd9a-c364383da7ea | -3.8767 | -49.95413 | 2024-10-29 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 729df2e4-0237-3e89-a764-9b70bfdb99db | -3.87617 | -49.95773 | 2024-10-29 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d47aff37-bbd9-3c8c-bf02-943b9d433000 | -3.87564 | -49.96133 | 2024-10-29 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7282b09c-3ab2-34ae-95a6-7a4d1ecf5b19 | -3.8673 | -49.99276 | 2024-10-29 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 830282cd-3f96-3f44-b05f-5004af750590 | -3.86677 | -49.99316 | 2024-10-29 05:01:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6481e93f-e445-3f30-a085-dd8562effe19 | -3.73619 | -50.06458 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58d46ef6-40ca-300c-9a30-a737160f6639 | -3.7258 | -49.43122 | 2024-10-29 05:01:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66a5d844-f2c9-3f4a-8303-37bd956a4ff9 | -3.67615 | -50.29471 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85a8d3fb-ef49-3bbd-a814-fbe3c86248d6 | -3.67536 | -50.29987 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3eff76bb-1d8a-38e4-9217-0c8e28ca9464 | -3.67216 | -50.29411 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 785d83b5-33f3-310a-8c46-ed96ee8360ed | -3.67138 | -50.29927 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7ce029c-fa04-384d-83eb-428cd7eb0b8e | -3.66645 | -50.1153 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 01364dc9-c344-3c6c-b4c9-46c53475eefd | -3.66591 | -50.11886 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 25a448d3-ea34-31e2-bc01-1cad3dc7208a | -3.66538 | -50.1224 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0abe9047-35ca-3e38-bd32-4201b352e733 | -3.65662 | -50.15332 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32019a60-9569-37e4-81ba-cf12d075b949 | -3.65609 | -50.15681 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eab85548-b5be-3f4e-8ba4-57b0d05ccce1 | -3.65557 | -50.16032 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e30b0c5-cc79-3042-b501-b01ca846f2cd | -3.6526 | -50.1527 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44acf5c6-f357-3f14-a08c-a09467a6529c | -3.65207 | -50.1562 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05b9462e-2773-39b9-b9d0-98c6cda69ec9 | -3.64968 | -50.44122 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b09c1187-d550-3872-87ed-01263e2ba32c | -4.11626 | -49.26294 | 2024-10-29 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cdfb666-279a-3388-b9fe-6c190a11ddfb | -4.11256 | -49.25827 | 2024-10-29 05:01:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53d55de0-19d0-3197-ada1-aad2ebe9b4e4 | -3.99293 | -49.28279 | 2024-10-29 05:01:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f29b3f6d-0627-3310-85e1-cdab88cf12a4 | -3.98924 | -49.27814 | 2024-10-29 05:01:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c08c202a-b134-3415-91a8-b99eedf6e7c9 | -3.98864 | -49.28217 | 2024-10-29 05:01:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9f5beb11-ca6c-32c3-89c1-46f25aa8fcb6 | -5.66386 | -49.99967 | 2024-10-29 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 03fdd647-a6ea-3cbe-bc99-9a4eef5469a6 | -5.65967 | -49.9991 | 2024-10-29 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 04c3bb5b-5520-3d1a-8924-c2646eef7fb6 | -5.60427 | -50.05652 | 2024-10-29 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5fd9995-0881-3c65-a5a1-cd3bf548310d | -5.60372 | -50.0603 | 2024-10-29 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a23733d2-4cee-37ed-9ff1-2414e62e94a8 | -5.60009 | -50.05596 | 2024-10-29 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83a12a5f-6c6d-30b9-b57a-1042a8bfbbbd | -5.59954 | -50.05974 | 2024-10-29 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d6b3148-8051-31ac-a7b4-a4ba329bc1ab | -5.54005 | -51.01063 | 2024-10-29 05:01:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb8803bd-237b-3094-8d0f-c8ccaff74e79 | -5.52058 | -49.80154 | 2024-10-29 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a50de694-c080-3ee8-a05b-62627be40d04 | -5.52001 | -49.80545 | 2024-10-29 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55e39199-6190-33f3-89cd-77f252bb26ba | -5.51635 | -49.80092 | 2024-10-29 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86b9bf3f-2870-3c28-a960-8fc4d54c5226 | -5.51578 | -49.80483 | 2024-10-29 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b146acb-4938-38c3-9c64-7e1ab27c9b6a | -5.39063 | -50.9662 | 2024-10-29 05:01:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01993d8c-ebfe-3f52-9823-b3070afa67d6 | -5.24434 | -50.69377 | 2024-10-29 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 708328a3-6107-3fbe-8043-143efeb47f02 | -5.02925 | -50.9558 | 2024-10-29 05:01:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 86f54468-c927-3dfd-a165-6e7ade858e84 | 1.80627 | -50.45314 | 2024-10-29 05:01:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1504f51d-f5a7-34e9-946a-2796eeaf32d1 | 1.03527 | -49.96951 | 2024-10-29 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c1a0ac9-c13d-316f-88d9-fcb5c386c2b5 | 0.85096 | -50.73236 | 2024-10-29 05:01:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8317756f-8abc-32ce-ac52-ee7e955d1bc9 | 0.80058 | -51.10081 | 2024-10-29 05:01:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85e9cbb8-fc0a-3185-bf43-4a25c975492f | 0.1718 | -51.01692 | 2024-10-29 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8415eeab-6bb9-3e20-b42f-530875a259d1 | 0.16882 | -51.02166 | 2024-10-29 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02e658ca-ba73-311c-acb5-5185bb4607f2 | -2.20867 | -50.78645 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 824f9681-34c0-3488-b5c4-ce1ed3eb405c | -2.20006 | -50.5903 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4eca2d30-830e-3b86-abca-977048996c23 | -2.19623 | -50.58972 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0f7dcd1c-7857-3e54-bf4e-379875e36607 | -2.19551 | -50.59442 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 618972fa-1496-370d-9b40-7d9729151a55 | -2.19239 | -50.58914 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1530dd23-e0d2-3831-9652-25bdfbe6204b | -2.19168 | -50.59383 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 39fbc18a-3f5b-37b1-af3d-41af4114d7ce | -2.08297 | -51.39836 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c01dac8b-12ad-3f2f-ae00-869bdaf43ac1 | -1.52368 | -50.62493 | 2024-10-29 05:01:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 275be495-c1e1-379a-bc32-5c1abbaf3336 | -1.43419 | -51.54235 | 2024-10-29 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c4c452a-6193-3ad1-ae8c-5a92e26d8665 | -1.35989 | -51.42252 | 2024-10-29 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c891a26-fd9e-3212-ac47-b1327b8e2d8e | -1.35923 | -51.42667 | 2024-10-29 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README77.md)
