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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f43a6fb-98e9-3555-ae2d-9cdb89165779 | -8.8625 | -68.501099 | 2026-09-21 01:18:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8cc97f2f-181f-33b6-9b5a-e5da6e54e120 | -9.0274 | -61.647499 | 2026-09-21 01:18:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d2bfaaa9-8f7d-3550-815c-9a5e62b59b5f | -5.7595 | -57.605099 | 2026-09-21 01:18:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b462185-f17d-36a1-b452-7eaaded5afca | -3.069 | -61.275002 | 2026-09-21 01:18:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7e5a3896-ac53-3fbe-828f-bbb20763735b | -2.8656 | -57.815102 | 2026-09-21 01:18:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 09ca4f99-e27e-3bb9-8c51-464a2f0fc647 | -4.3315 | -55.668598 | 2026-09-21 01:18:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bdb1762-c60e-334a-9ae7-afbe35abd7de | -3.476 | -59.562199 | 2026-09-21 01:18:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 31786f87-2434-3bde-b778-632404596eed | -3.6865 | -60.581501 | 2026-09-21 01:18:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5ec2d5c7-c3de-341c-b162-3f8e0a696f63 | -6.9229 | -62.912601 | 2026-09-21 01:18:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9108eeb1-e185-3ec1-b9b7-f57c89bd9a28 | -6.7298 | -59.429699 | 2026-09-21 01:18:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fad3b3b6-9ab6-318b-9f12-927d5d28b119 | -9.5624 | -66.044899 | 2026-09-21 01:18:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 48dbdbb9-c675-3e18-a89e-a1f3eb42352c | -9.5655 | -66.0588 | 2026-09-21 01:18:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 324522a0-6ad0-3e31-9870-9641890919e3 | -6.9876 | -61.355 | 2026-09-21 01:18:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9d684354-ad36-3469-8aa4-1cba973f663e | -5.7542 | -57.583801 | 2026-09-21 01:18:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8d9c0be-812f-3073-938c-179e9fdf86e4 | -3.48 | -59.579201 | 2026-09-21 01:18:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 43db0d7b-6ae1-3226-8dae-259ccd31088c | -7.5769 | -57.6936 | 2026-09-21 01:18:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6a4588d-5892-36af-a229-88b86ca003fc | -10.1001 | -64.3293 | 2026-09-21 01:18:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dd8c48d7-3746-3470-b293-eaa5d6bf8b19 | -2.856 | -57.817402 | 2026-09-21 01:18:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 016d63df-6a5e-3460-9c97-a2fbbdd117cc | -9.5542 | -66.0541 | 2026-09-21 01:18:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1c2d1778-e721-3541-be6d-bf762906fec2 | -11.019 | -54.165501 | 2026-09-21 01:18:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e10a0d47-8853-382d-ba11-537c22dbb137 | -20.8766 | -57.684502 | 2026-09-21 01:18:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 91602303-4833-32e7-9188-5dfa0a3e6f28 | -3.3903 | -59.546501 | 2026-09-21 01:18:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 34328a1d-22a7-3b11-b8c9-58a70c2884a6 | -9.0298 | -61.6577 | 2026-09-21 01:18:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| efac5dd7-6c16-39af-bf18-a6a509519674 | -6.644 | -59.966599 | 2026-09-21 01:18:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 90dd53a8-8b82-3953-9e70-5ee9223fc3f3 | -6.2753 | -57.743 | 2026-09-21 01:18:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5097357-0be4-3d5c-b24a-343b6c7ede6f | -8.8641 | -68.508598 | 2026-09-21 01:18:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 75214d8a-62b5-358c-8ca1-52030bd9af0a | -3.0495 | -61.279499 | 2026-09-21 01:18:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3a5ac1f8-aabf-3e67-afa2-61ac59ebd200 | -3.0623 | -61.290501 | 2026-09-21 01:18:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7e07e263-2ab2-30c8-988a-42ff2e0cfcfc | -6.3781 | -60.015999 | 2026-09-21 01:18:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0d9316a3-17c4-381c-8d37-9d268fdaf499 | -9.5562 | -66.017197 | 2026-09-21 01:18:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f7e6fc09-5ddb-3ca4-9e23-6de00415aebf | -7.5817 | -57.671501 | 2026-09-21 01:18:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a8cc1fe-a69b-34e0-8f40-b477c8375373 | -5.7639 | -57.581402 | 2026-09-21 01:18:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6720e7f1-1724-3874-9250-69966d349955 | -3.0561 | -61.264198 | 2026-09-21 01:18:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 578591c8-04dd-3d59-a297-3ac25f948b60 | -7.5481 | -61.327702 | 2026-09-21 01:18:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d85fd024-d0e0-3d8d-add9-3daaeeb1a260 | -7.5825 | -63.0425 | 2026-09-21 01:18:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 78615bbe-fef9-3727-953d-aa4e8278c1be | -9.5495 | -66.033401 | 2026-09-21 01:18:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 95642594-b9c3-31ef-a23b-a225ef9d5070 | -6.4427 | -59.985298 | 2026-09-21 01:18:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d89319d9-34d2-33a0-8b5c-134a7ec547fd | -6.449 | -59.9687 | 2026-09-21 01:18:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5e416493-47f6-3380-9eba-8353e54e203a | -9.5722 | -66.042702 | 2026-09-21 01:18:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f84f8355-3000-3e2c-9c00-197e217597b5 | -3.0721 | -61.2882 | 2026-09-21 01:18:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2bbb6476-6741-33f3-83ed-ff37cd955563 | -3.0592 | -61.277302 | 2026-09-21 01:18:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2a21b365-a373-3f83-8325-c79f86109c48 | -11.0442 | -54.9123 | 2026-09-21 01:18:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dcd074c3-804c-3fa1-8d8c-6becffc328e3 | -9.2017 | -64.460403 | 2026-09-21 01:18:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3d978342-ccb6-355c-9dab-ac53cad5defd | -6.3032 | -60.004002 | 2026-09-21 01:18:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d4afd882-a89d-3a9a-baaa-fc373d51de88 | -6.8676 | -63.116402 | 2026-09-21 01:18:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 879b7955-0dd2-3481-8e4a-54da41c868d1 | -9.5578 | -66.0242 | 2026-09-21 01:18:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| affa8e75-ca63-3444-abd2-afce708bb074 | -8.8665 | -68.801498 | 2026-09-21 01:18:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f39d8456-6de2-34c8-837d-73083bda2a22 | -6.8773 | -63.114101 | 2026-09-21 01:18:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 483f86bc-034c-3abe-91cd-8d989581929a | -7.5818 | -57.7131 | 2026-09-21 01:18:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3363b0c5-f5b5-3ea8-9eda-ecc280a528f2 | -6.1366 | -59.952999 | 2026-09-21 01:18:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 84c7c67a-c336-3fc0-8994-f0112c6f9b61 | -9.548 | -66.026497 | 2026-09-21 01:18:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c3fa1483-c387-3efb-98ab-a5963afe5b40 | -11.0381 | -54.160099 | 2026-09-21 01:18:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb3ce600-31df-3aa6-a3ce-f181a2905be1 | -3.4783 | -59.615299 | 2026-09-21 01:18:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3deedfac-0d4b-32ec-b1fa-104abe46ef0c | -6.7255 | -55.094501 | 2026-09-21 01:18:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c6dc85c-0570-32d4-b262-0645a1d20e34 | -8.7816 | -68.836098 | 2026-09-21 01:18:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1265ba6b-1111-38e8-9792-260055cd5959 | -3.6802 | -60.598099 | 2026-09-21 01:18:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 43525f46-3b21-3e5f-85fe-816ddac96456 | -8.2368 | -62.841202 | 2026-09-21 01:18:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 064149e5-7b4a-3ad0-8f24-f9f4570bf69c | -6.8655 | -63.107498 | 2026-09-21 01:18:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e5e5cab1-8cfe-36f2-afbf-4323a41ea71d | -16.028299 | -52.525799 | 2026-09-21 01:18:00 | METOP-B | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ebd140dd-5774-34ae-b783-b381a175507d | -9.5515 | -65.996498 | 2026-09-21 01:18:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b5cac32e-70c8-384b-8b9a-e6007a6c5f95 | -9.5511 | -66.040298 | 2026-09-21 01:18:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c4dfd37a-5146-31e0-a7ca-33aed1d10007 | -3.3862 | -59.5294 | 2026-09-21 01:18:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6fdd7a0e-6c28-3c09-bc7c-47e3416b451c | -8.1677 | -54.781399 | 2026-09-21 01:18:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fd609bc-2ad8-3a7d-9ee1-0c6691eea859 | -6.9849 | -61.343601 | 2026-09-21 01:18:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b46c28cc-8117-340d-aa13-50ebbd86aeba | -3.0765 | -61.175598 | 2026-09-21 01:18:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9fb47e5b-3016-359f-9d25-02c6968ddb46 | -10.5277 | -57.438 | 2026-09-21 01:18:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d60bf6d1-bc18-3f5a-adb4-d0fea3425549 | -5.2096 | -56.127102 | 2026-09-21 01:18:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abf008d4-e6ee-30e6-87fa-dee3eeaf8657 | -8.7833 | -68.843803 | 2026-09-21 01:18:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c8bea9a8-d445-369a-88f2-bca928aa1542 | -4.3486 | -55.696701 | 2026-09-21 01:18:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99e9e26a-962e-397a-a514-351dc599c18b | -7.572 | -57.673901 | 2026-09-21 01:18:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddfc83e1-285f-3e84-aa32-cffb89a5fceb | -6.1934 | -57.785 | 2026-09-21 01:18:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1f68354-c9ee-328f-8740-597d09220ebe | -7.5672 | -57.695999 | 2026-09-21 01:18:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aee1c658-59ce-37ed-8d5e-05cc4955c9a2 | -6.2968 | -60.020599 | 2026-09-21 01:18:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| edf18e66-4725-36df-b55b-d31e3cfad4c3 | -16.018801 | -52.528801 | 2026-09-21 01:18:00 | METOP-B | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ba6b81e4-d364-39fa-82b5-a67782e3a85d | -6.7167 | -63.132801 | 2026-09-21 01:18:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 39d08b78-2c46-3154-baf7-2cb7cd37ff28 | -6.0946 | -57.634102 | 2026-09-21 01:18:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0486d44-89d0-3c7c-acb9-c55a9fe2d239 | -7.2359 | -55.611801 | 2026-09-21 01:18:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35382d0c-ac4f-379a-80c0-9dbf1499ce4b | -7.5122 | -64.694199 | 2026-09-21 01:18:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8e8fbec9-eafe-325f-ae1e-767c49824bdc | -6.4621 | -59.980598 | 2026-09-21 01:18:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 68bcb9f6-fa78-3727-ad35-e7780d99f8ef | -8.9366 | -68.746101 | 2026-09-21 01:18:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 92abb8a4-712d-3e89-a52d-f55c5a021948 | -6.1837 | -57.787399 | 2026-09-21 01:18:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a03c2320-af8d-34d6-a8bc-90f8149b7227 | -3.4251 | -59.2617 | 2026-09-21 01:18:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 49e56672-3ed1-3206-b325-eee3cc2f72ae | -6.7395 | -59.427299 | 2026-09-21 01:18:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3497e6e4-341a-374d-8090-c6722d28071a | -10.4853 | -50.346 | 2026-09-21 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| a53892f7-e48c-384b-b187-ab97962cb1ce | -3.0534 | -61.2767 | 2026-09-21 01:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 03323776-1db6-33c0-b513-6c57ae0e6dfe | -3.753 | -59.419 | 2026-09-21 01:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 26.1 |
| c0fa3650-30fc-3aee-8f78-75de2d740219 | -6.467 | -59.9902 | 2026-09-21 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| a4cc89e5-5f7e-37d8-99f7-fb034fe6266b | -11.8017 | -49.7913 | 2026-09-21 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 7f3dfa51-2dc8-363c-95d0-e65f1f7c93c2 | -7.5889 | -57.6757 | 2026-09-21 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| ec16f81d-8662-3577-9074-55c70853ff60 | -11.8014 | -49.8129 | 2026-09-21 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 238.0 |
| 9865d9e0-95f5-3f2d-80a6-519162ed13fc | -3.0717 | -61.2764 | 2026-09-21 01:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| ee9d76eb-187f-3b44-993b-765ec3820db6 | -11.8204 | -49.8106 | 2026-09-21 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 3899a70d-8d3d-3faf-9084-add6c62653de | -9.5593 | -66.0545 | 2026-09-21 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.9 |
| d82785e2-10d8-358b-ac29-0a8ec94084a9 | -2.8791 | -57.799 | 2026-09-21 01:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 02261516-4cad-3e97-9b07-55a16c4eccd1 | -6.4486 | -59.9717 | 2026-09-21 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 5b7df6fc-b8bb-3959-aecf-eaef830620f2 | -10.0712 | -50.26 | 2026-09-21 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 349a9c68-d420-3d67-b8be-338f2c33e0e8 | -11.3419 | -51.3606 | 2026-09-21 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| bb733873-bc7e-369c-a3a2-c4e83518f2a1 | -11.0509 | -54.9106 | 2026-09-21 01:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| a3365831-73f5-3946-b9e8-101a9094cdc8 | -11.041 | -54.1567 | 2026-09-21 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 4bbe3a16-da42-31ed-af18-7b7ae47fa405 | -6.3195 | -60.0147 | 2026-09-21 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |


[Clique aqui para ver as próximas entradas](README13.md)
