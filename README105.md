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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25e78acf-fa12-34e6-97b9-1441840e31ad | -8.6208 | -54.96012 | 2025-10-07 05:48:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 416e60ac-ca0f-3b97-aabd-46310562f28b | -7.4661 | -63.7438 | 2025-10-07 05:48:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b35e3ae4-7dda-379b-83da-cbf044b2977e | -4.56862 | -55.95862 | 2025-10-07 05:48:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99bb381e-3556-3032-af06-b2294f300331 | -7.43569 | -63.74546 | 2025-10-07 05:48:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9f6f8e6d-bca6-3303-8705-2762a072b688 | -6.7688 | -63.02571 | 2025-10-07 05:48:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f688feb0-ce89-37be-98eb-b07509ca77f2 | -7.43205 | -63.74491 | 2025-10-07 05:48:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ed63c2d5-c207-3f80-a1f9-c6cfb9446b6f | -9.40246 | -61.44162 | 2025-10-07 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 501bcfa2-5ae3-3c57-a30d-f46af70a3285 | -9.32658 | -62.4071 | 2025-10-07 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5b350f5-cf85-32e9-a5c4-4fee54c9c56f | -10.52824 | -58.03189 | 2025-10-07 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90deb7ee-01eb-343f-aff9-07ae5cad2c99 | -11.74512 | -54.72502 | 2025-10-07 05:50:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 13512233-d706-3871-97a7-8dc5adf63c92 | -9.76674 | -62.32291 | 2025-10-07 05:50:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 806bcf7c-a423-36ad-b6ba-f64eab842c68 | -4.68561 | -45.83457 | 2025-10-07 05:50:00 | AQUA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 670f2e02-03de-38e3-8717-50e3ab2445b3 | -8.7695 | -72.78605 | 2025-10-07 05:50:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca29d2b1-06e1-3a7a-b40e-3316f035eb8c | -9.56399 | -63.50385 | 2025-10-07 05:50:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ea18a7c-212c-36ea-b1d8-49f48059b930 | -3.08864 | -47.01722 | 2025-10-07 05:50:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| c5925f3f-5ad6-3129-a8c1-6d855802e201 | -3.09839 | -47.01864 | 2025-10-07 05:50:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 125.1 |
| b1b814dc-1d91-33d2-8195-5fa871986475 | -9.00636 | -61.64267 | 2025-10-07 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c69971f-8aed-3460-aa95-b143041a50a9 | -9.83453 | -61.99068 | 2025-10-07 05:50:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d7348a6-a0e4-3ade-b250-3aa264ec50b7 | -12.91534 | -54.73025 | 2025-10-07 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5cdd0d7c-8ba8-3b18-b0c9-aac0e3a97c4d | -10.89714 | -69.56239 | 2025-10-07 05:50:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d33cde79-a5e8-3c28-9ded-f6977ceff74c | -15.1982 | -56.82421 | 2025-10-07 05:50:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b84ee4a6-8d9c-302d-91b9-4213c0307238 | -9.77136 | -62.31983 | 2025-10-07 05:50:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4913d5e4-d830-388f-83ae-b3fe95999064 | -9.40415 | -61.44394 | 2025-10-07 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eef5db24-004c-3acb-b8fe-70450f313144 | -5.49924 | -43.06675 | 2025-10-07 05:50:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 022a90a0-c9b8-3045-9b0d-bd6500254b49 | -8.83228 | -62.36908 | 2025-10-07 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79337bef-fc6b-394b-8b9f-d2a4bf939ea0 | -7.94231 | -63.7108 | 2025-10-07 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24fa85f6-2aec-3be0-9bbe-129a18fc3157 | -9.45064 | -56.65613 | 2025-10-07 05:50:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e517ad9a-b281-30f7-bd99-34e785763a97 | -10.5569 | -56.55474 | 2025-10-07 05:50:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 543cf075-01f7-3630-9532-c6d09bd2a91b | -8.85404 | -62.36873 | 2025-10-07 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54f0668e-c819-3caa-8ebe-2c7b3baf6006 | -11.74582 | -54.71923 | 2025-10-07 05:50:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a641749c-34bb-35fe-a081-f1b45c20008e | -8.86261 | -62.36633 | 2025-10-07 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 956cd649-6713-3885-a2b3-5249b0d1d851 | -12.89912 | -54.74897 | 2025-10-07 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| ca3ce8c4-6176-379b-9327-1dc1f9ddd802 | -12.89707 | -54.75391 | 2025-10-07 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 26aa4e2c-aa96-3c5d-80bb-399cb4cce2f4 | -9.6187 | -57.19822 | 2025-10-07 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8ed4f26-e764-3f9e-b025-dadb7b8c11da | -9.39812 | -61.44106 | 2025-10-07 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea9d12a4-eb40-3997-bc25-b620399e7d6d | -9.36045 | -62.43052 | 2025-10-07 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4183695b-9884-37a0-8912-9d5642c50146 | -9.38812 | -59.42042 | 2025-10-07 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8c280b5-4163-363b-a60c-74a0bb98b03b | -9.12817 | -61.84842 | 2025-10-07 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36f40af4-685d-3672-9751-3048b6793c7e | -12.90615 | -54.73444 | 2025-10-07 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 710a2ab6-3ebc-3bf3-bdf0-58012082278c | -9.25683 | -59.02347 | 2025-10-07 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46aa9f55-9650-386e-a85e-30befd80438f | -10.43844 | -61.33067 | 2025-10-07 05:50:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f486eed-80fd-3ae0-96d3-c924a6701590 | -10.02553 | -64.96521 | 2025-10-07 05:50:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4fc0e79a-8a84-3781-88de-a5b0181f9813 | -9.83873 | -61.99134 | 2025-10-07 05:50:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34733d1b-9380-3a7e-9f68-422df1606d72 | -3.09032 | -47.0064 | 2025-10-07 05:50:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4e38ba8b-8f34-301e-b8e8-c0b3f6b029a5 | -11.15216 | -54.88217 | 2025-10-07 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 64d75467-c3b7-3a21-aaa2-8a0f9bd67173 | -5.75586 | -43.39379 | 2025-10-07 05:50:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3898db63-68ef-3c7b-9231-ec7af4bec390 | -9.20018 | -62.59224 | 2025-10-07 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfa4c86a-beec-3f79-82a5-9f631f8e7ef7 | -8.83739 | -62.36995 | 2025-10-07 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a068ca06-78aa-356e-a07a-2b7d628cc5b3 | -9.60881 | -63.18676 | 2025-10-07 05:50:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec55928e-fa51-37ea-bab5-034b4ef9dfa4 | -9.41659 | -63.20995 | 2025-10-07 05:50:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8f9f479-b9f2-35e2-90fd-4d8990df4e2b | -4.68419 | -45.84386 | 2025-10-07 05:50:00 | AQUA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 0f654976-9007-3285-a299-2aecc2c074c9 | -8.22567 | -61.17832 | 2025-10-07 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08447b49-bfcd-347d-847c-b39fa7258abf | -5.57274 | -43.56888 | 2025-10-07 05:50:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a34ab051-5a6a-3a7e-b8ee-b3a37d902b95 | -7.67091 | -66.99687 | 2025-10-07 05:50:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2997afa4-5ccd-3fb7-9ed3-158bd01c66ea | -7.67145 | -66.99342 | 2025-10-07 05:50:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdfb37e1-b97f-3272-a599-5b220f3dddfe | -9.25212 | -59.01979 | 2025-10-07 05:50:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ec62aba-338a-3d5d-9385-d7ce07f5f6d1 | -11.86589 | -56.88483 | 2025-10-07 05:50:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 82a6c303-330b-3566-997d-ecd6de4b3f38 | -12.90544 | -54.74139 | 2025-10-07 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 633759cf-2e89-3d72-af2f-3446fe62acb1 | -9.9112 | -60.19426 | 2025-10-07 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9369c7e2-0b52-3094-8cc3-9c7bd834f41a | -9.39872 | -61.43684 | 2025-10-07 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4355ecc-ae68-39e6-ac36-ccd21d348074 | -11.15895 | -54.8832 | 2025-10-07 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 59aa63aa-efff-379e-a4e5-999aa740ce5d | -11.15289 | -54.87577 | 2025-10-07 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e7c39ebf-522b-32cf-aec7-b1713b1ac90b | -9.15804 | -62.30495 | 2025-10-07 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf520afc-87c4-314a-a333-0a271757d399 | -4.69461 | -45.83599 | 2025-10-07 05:50:00 | AQUA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 42.8 |
| d5cced23-e71a-393e-9413-23705b5b406e | -9.70967 | -61.92637 | 2025-10-07 05:50:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9246f62f-74bb-370c-9607-8e9381dcc023 | -9.60819 | -57.14175 | 2025-10-07 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d85e7d03-1d76-391e-bc74-a4d875c26f7c | -9.58565 | -63.90966 | 2025-10-07 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46954560-f48d-3bef-b03b-862437d666a4 | -10.1555 | -61.94964 | 2025-10-07 05:50:00 | NOAA-21 | VALE DO PARAÍSO | RONDÔNIA | Brasil | 1101807 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99158c17-2482-3d92-ab18-d18afe9f0072 | -5.67244 | -42.76395 | 2025-10-07 05:50:00 | AQUA_M-M | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c3fc69cf-ba23-304c-accb-adc859f5d83a | -11.15968 | -54.87687 | 2025-10-07 05:50:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 21fd6df8-8186-3826-b523-f0023a9f57a0 | -9.1529 | -60.62218 | 2025-10-07 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 607b1ad7-a965-3f20-b332-a43315b7e7fc | -12.91314 | -54.7355 | 2025-10-07 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 75842371-abf8-339b-b537-b34317a31b4b | -15.30211 | -56.93042 | 2025-10-07 05:50:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 57179cb0-d9cc-31bb-b1e5-604728d58e3a | -15.19421 | -56.82402 | 2025-10-07 05:50:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4df3ff9f-09d3-352a-9b6d-a0e3f5d3b2db | -5.65812 | -43.17838 | 2025-10-07 05:50:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e73889d0-f5e7-33a4-9601-7c48bf4d728a | -10.56301 | -56.55548 | 2025-10-07 05:50:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf3b8e22-65c0-34a2-8612-71641b9b4cdf | -15.03661 | -56.0292 | 2025-10-07 05:50:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 59d06409-0851-3aaf-b96d-bcda31937590 | -10.63122 | -57.61882 | 2025-10-07 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b672171-44f2-3892-b0a6-66f882955ab3 | -9.40185 | -61.44586 | 2025-10-07 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b6aa911-4cd2-3126-86bf-c1d7f1f1195f | -12.91384 | -54.72861 | 2025-10-07 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ae35b42e-5288-3312-970e-574c2b9cfd64 | -9.14458 | -62.36963 | 2025-10-07 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8668be2-485c-38f4-a50e-991e8b28f7c9 | -11.74585 | -54.71861 | 2025-10-07 05:50:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0ba1f763-5fd8-3b7b-a42e-9a7f6e3a3c08 | -11.87144 | -56.89019 | 2025-10-07 05:50:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| efa47226-1132-3b1d-a3c6-ee4d5291e037 | -10.55525 | -54.87178 | 2025-10-07 05:50:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4bcc828c-bca0-38d2-a08e-42a32f6406a5 | -9.00227 | -61.54762 | 2025-10-07 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4180d62-04ab-3bfc-8cb6-bb35b6407c63 | -8.85857 | -62.36575 | 2025-10-07 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2077a24-d6bd-30ec-bec0-e7244340897c | -9.96338 | -58.70173 | 2025-10-07 05:50:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf3b1375-68c5-3a5b-b087-490c7cc46f31 | -5.7572 | -43.38461 | 2025-10-07 05:50:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 67e9ce8d-4cb7-307e-a1a6-be05b57f510a | -12.89774 | -54.74736 | 2025-10-07 05:50:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 86f54282-53da-3a06-b55a-b42d73667e46 | -1.61224 | -46.65914 | 2025-10-07 05:50:00 | AQUA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4af3fc33-7d04-3317-8db0-a89efaeaf731 | -9.9581 | -58.70109 | 2025-10-07 05:50:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d75b4d4f-9ba6-308f-9ed0-8431aa410b6c | -9.65125 | -62.34516 | 2025-10-07 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee5defe4-325f-3529-9a0c-d513292dac57 | -12.08662 | -62.94374 | 2025-10-07 05:50:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d64bd0ce-eaf5-394e-bb64-c42b05217d4c | -10.8413 | -69.14398 | 2025-10-07 05:50:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02473ea5-81a6-3322-85e8-2dd4ad9a9c31 | -10.55599 | -54.86552 | 2025-10-07 05:50:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cc10f766-e3ee-39b1-991e-eb094c6bb828 | -9.96382 | -58.69837 | 2025-10-07 05:50:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02ecbd8f-e60c-3589-84fd-ac9498ef509e | -9.61818 | -57.20234 | 2025-10-07 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fd1f721-951c-35ba-a9eb-419dc95c970c | -9.84065 | -62.23438 | 2025-10-07 05:50:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31324230-7391-3ae6-ab78-c647d50c1b03 | -5.84442 | -42.85073 | 2025-10-07 05:50:00 | AQUA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 6dc1744d-023b-38c9-bd3d-285395bef441 | -9.12894 | -61.85077 | 2025-10-07 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README106.md)
