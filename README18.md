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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77ac56a9-ab23-3760-8db7-5fc2f8931f73 | -8.92588 | -63.87479 | 2025-07-12 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.2 |
| a339bef0-6367-398e-8006-1e11134e1634 | -13.65361 | -53.94002 | 2025-07-12 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 930eb520-2095-35f9-854e-29e7cd3e7056 | -9.02102 | -61.22639 | 2025-07-12 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d112a6e6-777d-35e6-8a02-def9d80332e6 | -11.87943 | -58.71043 | 2025-07-12 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a838035c-2584-3c05-a168-9c1f92712927 | -11.87824 | -58.71164 | 2025-07-12 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6b2e46b-b831-3313-83fe-9fefccc6cc77 | -11.86242 | -58.70921 | 2025-07-12 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 765e749f-c487-3543-aa67-90bafdcb3638 | -13.65559 | -53.9374 | 2025-07-12 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b45286fc-5854-34ee-8759-0ab4135628ab | -9.01664 | -59.54505 | 2025-07-12 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1989b998-11f8-3dd5-b8d9-2c7c79d10fd1 | -7.90021 | -61.52288 | 2025-07-12 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab541051-dc3e-3c91-a158-cd639d061b7b | -9.96472 | -64.95087 | 2025-07-12 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfab5b0d-c9f6-3934-bcfd-ed8e8410ea14 | -9.62632 | -61.46056 | 2025-07-12 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a342dc4-725f-3069-87a7-a66c10085219 | -10.13171 | -57.78166 | 2025-07-12 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84f5b950-7119-3ca1-a1a0-8a843ec85021 | -10.22505 | -56.76761 | 2025-07-12 05:29:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fd8b1c0-c1b8-367f-8c5d-132fd43ad7e2 | -10.31937 | -67.34447 | 2025-07-12 05:29:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c9009bf-525b-39aa-9447-d6c797171afd | -7.80683 | -66.93388 | 2025-07-12 05:29:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4349596d-44cb-3bb6-a02f-3af0de4ea750 | -11.87473 | -58.715 | 2025-07-12 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fd3e93a-b56a-36c9-8cc1-2e12d61fe011 | -8.80478 | -67.27187 | 2025-07-12 05:29:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b465ad1b-2a6c-365c-8d88-8da868beec31 | -9.45501 | -65.55316 | 2025-07-12 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e95d4fdf-7730-313c-a72f-3f072d119581 | -10.13224 | -57.77796 | 2025-07-12 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4b2b9389-cb85-3cd9-98e9-2ede1fc16bfe | -9.88385 | -63.10903 | 2025-07-12 05:29:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a4f0268-322a-3c31-9e89-1f0ddefc43b5 | -7.59363 | -63.47148 | 2025-07-12 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30da098a-bd82-35d3-a661-81782943fc43 | -9.02496 | -61.22323 | 2025-07-12 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8162c301-054e-3568-815b-687cbc5b9de6 | -10.05166 | -59.11083 | 2025-07-12 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97c2bd09-b323-39c3-950a-fcdc3799c1f8 | -10.66929 | -49.50912 | 2025-07-12 05:29:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5bd14c52-e231-3a90-aa37-c88b386048b5 | -13.64399 | -53.9395 | 2025-07-12 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11797e40-9e0a-3b81-abcc-36856024e047 | -9.01707 | -61.22952 | 2025-07-12 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48047a1a-093d-331d-a103-e3220cf2116e | -7.84797 | -56.66657 | 2025-07-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba397916-db1e-36d3-83eb-b3a07747831f | -13.65514 | -53.94114 | 2025-07-12 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7393a943-9364-3852-9030-ee18126731f1 | -10.22019 | -55.45311 | 2025-07-12 05:29:00 | NOAA-20 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aed36f9d-122c-3366-a426-75b541591fc1 | -9.96874 | -64.9477 | 2025-07-12 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64057b07-9ca9-30a1-8b3c-aab50b646b6f | -9.61714 | -67.27339 | 2025-07-12 05:29:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7650da63-0e32-30b9-b2ee-bcd7aba5e545 | -8.52932 | -54.76903 | 2025-07-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a4cc6caa-adc3-393c-8133-73aad319a1ef | -10.04722 | -59.11486 | 2025-07-12 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2007507b-a7fa-304a-8c5a-9229ead71813 | -9.65299 | -62.91469 | 2025-07-12 05:29:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0af36f21-ce09-33e8-9762-9f38441f8fe9 | -10.04789 | -59.11026 | 2025-07-12 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40513151-eb1e-3136-be84-21b952b8d022 | -13.64956 | -53.94034 | 2025-07-12 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c12b2480-702d-3392-9688-8a905b051c2f | -10.36623 | -57.49793 | 2025-07-12 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3836f465-b42f-3181-b1b9-91c0607d27e0 | -10.05488 | -59.36068 | 2025-07-12 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 480fb611-c4de-3a3d-bffd-96045dd98487 | -7.59696 | -63.472 | 2025-07-12 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39aab3fa-8542-30ef-a9c4-5b9f31dc57bf | -10.22947 | -56.76808 | 2025-07-12 05:29:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af34aed7-ca29-3e0b-973e-cce094e08e49 | -13.65001 | -53.93659 | 2025-07-12 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92d0372d-ca3f-3430-86ce-4f8281ef59df | -9.64547 | -65.73895 | 2025-07-12 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 45e7728c-702c-3975-9e0f-5d58e0b4ec4f | -7.91976 | -61.55133 | 2025-07-12 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35976459-47c9-3f85-b7bb-b6117763d41c | -12.57942 | -56.98396 | 2025-07-12 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb2096d4-3737-31e4-8d2a-f2e848457e59 | -12.06697 | -63.22344 | 2025-07-12 05:29:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 38b3f01a-0d72-3e6d-a92c-0165e46f38d0 | -8.52855 | -54.77452 | 2025-07-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bb909eaa-9db6-3e1f-aec3-18ae33fa6cb5 | -9.71808 | -61.29063 | 2025-07-12 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8340471a-25b8-3309-80b7-000b031763f1 | -10.66483 | -49.50757 | 2025-07-12 05:29:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 773d025c-cb60-3fae-adec-986ebc15a5fd | -13.6592 | -53.94075 | 2025-07-12 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ebd68d8-fcac-3c0b-9698-ca203025c0f1 | -8.52611 | -54.77055 | 2025-07-12 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d7aa4977-84a6-3f93-b69d-798d8ea9e7d3 | -7.84472 | -56.66684 | 2025-07-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d2e9470-5cbb-3cb5-80c5-5455c3a862ee | -11.1011 | -60.84905 | 2025-07-12 05:29:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 579a26e7-8498-3451-aa91-dbe199412a53 | -11.88149 | -58.71742 | 2025-07-12 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29c3d7a7-9f66-37d5-a6c0-adf4197db6e7 | -7.86709 | -56.62373 | 2025-07-12 05:29:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc0b149a-3e79-3455-8c1f-f34bbcf2eced | -11.86656 | -52.25871 | 2025-07-12 05:29:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61226439-12b8-3de7-90bc-0eaaf22f2546 | -9.97215 | -64.94827 | 2025-07-12 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 130d334a-2eae-318f-8a88-c45ba543302f | -11.4897 | -61.77413 | 2025-07-12 05:29:00 | NOAA-20 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c958e7f-f386-355f-abf1-0d185edc899a | -12.5833 | -56.98912 | 2025-07-12 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f76412e-504a-3715-9345-773ca3d621ba | -9.65629 | -62.91521 | 2025-07-12 05:29:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 046991b7-70af-36e6-9ab7-29c3dc09f961 | -11.87868 | -58.71563 | 2025-07-12 05:29:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f536b68-d174-3fde-ac98-bb2e418f1450 | -10.66562 | -49.50084 | 2025-07-12 05:29:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 48480de8-7843-3222-9604-8bfa6326c136 | -10.21608 | -55.4472 | 2025-07-12 05:29:00 | NOAA-20 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c68f1ed6-9888-3d2d-b0f9-1f513b326265 | -9.78478 | -62.485 | 2025-07-12 05:29:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03d9ad12-329b-352e-8161-3e36f5477d2e | -9.65353 | -62.91121 | 2025-07-12 05:29:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a88ac068-fcaa-30ef-a4e3-0d82b7be456b | -13.66073 | -53.94183 | 2025-07-12 05:29:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 303fb7e5-bdfe-3aae-884a-42c07179cad8 | -10.0959 | -60.49438 | 2025-07-12 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1cd64a3-7225-3922-811e-a2c4190b6786 | -5.8413 | -48.3748 | 2025-07-12 05:30:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| c6b2a9e0-215b-36a0-96a8-322fbf8fcfa4 | -5.8412 | -48.3964 | 2025-07-12 05:30:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| cba1b6eb-d691-3f60-8475-1378674ee4f9 | -10.8986 | -49.204 | 2025-07-12 05:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| ecf6ca3a-a770-3ea4-89ea-54f26c23b170 | -19.08456 | -56.04436 | 2025-07-12 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c2540c73-0ab7-3078-b6b5-a339391d1a13 | -14.35121 | -58.69029 | 2025-07-12 05:31:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f09d2c0b-b7a7-3f60-a5ce-dd5485c5439a | -14.31736 | -58.70132 | 2025-07-12 05:31:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4b01d3c-ab52-3344-94c9-3fe45113d383 | -18.66147 | -55.72731 | 2025-07-12 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 817edcb0-431c-3a87-91fa-62d3754f0789 | -19.08979 | -56.04499 | 2025-07-12 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a02002d2-e881-3e17-9578-698c46c15dde | -14.35218 | -58.69117 | 2025-07-12 05:31:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 066fd6f4-554c-3b57-b6e8-a46362f0083a | -18.42209 | -53.03385 | 2025-07-12 05:31:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6576a4f-8217-39fd-a98b-37bac67c11d9 | -19.09014 | -56.04165 | 2025-07-12 05:31:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b3e9a0e2-b503-3b9b-9992-4c70b4060944 | -5.8413 | -48.3748 | 2025-07-12 05:40:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 87a3853c-b3c9-3db4-b63f-fa6c2a98f1ed | -5.8412 | -48.3964 | 2025-07-12 05:40:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| cfb1b189-0d02-3cc5-8bf4-06af4053be2c | -10.8986 | -49.204 | 2025-07-12 05:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 94c53a95-2830-3be0-a108-fdeb35e10e26 | -10.8986 | -49.204 | 2025-07-12 05:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| bd128ea6-9553-3e8c-828e-1953c1e99f34 | -5.8412 | -48.3964 | 2025-07-12 05:50:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 182944bc-e9ad-3379-8c4d-f5339a2800ad | -5.8412 | -48.3964 | 2025-07-12 06:00:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| a3616ace-5bbb-3bea-a1fc-73fae11b804a | -10.8986 | -49.204 | 2025-07-12 06:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| d28d8f38-9d72-3e0d-b8da-9560df76fd7c | -5.8598 | -48.3953 | 2025-07-12 06:10:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| f82f1d51-1c8c-3c6b-adc5-c3f571b54d92 | -5.8413 | -48.3748 | 2025-07-12 06:10:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| b019b0ce-8cc0-3797-a5e0-a7042c7a2665 | -5.8412 | -48.3964 | 2025-07-12 06:10:00 | GOES-19 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| e45f19c7-2901-3cd9-aafd-d3211333c001 | -10.8986 | -49.204 | 2025-07-12 06:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 9bde6bfa-a054-33d0-b58a-2565af039866 | -7.41729 | -72.67548 | 2025-07-12 06:20:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 109d2e6b-2cfd-38a2-8df8-b9cacf7fd1c4 | -7.59477 | -63.47122 | 2025-07-12 06:20:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a7c6160-1a7a-35e9-a859-bb79bb4cfd39 | -8.9142 | -72.80876 | 2025-07-12 06:22:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 374efe57-e187-3512-852c-f912795f633d | -9.96866 | -64.9482 | 2025-07-12 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e73927fd-494f-3657-a2d4-d4afa1b80d86 | -9.61801 | -67.2711 | 2025-07-12 06:22:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b707af5-b52f-3c9c-b17d-3e7cd6e0134a | -9.96812 | -64.95255 | 2025-07-12 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c66b1b95-36a9-3ee2-91cd-54f9b0d4fc1a | -9.96757 | -64.95689 | 2025-07-12 06:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 94d66a05-d450-3a4d-942c-b048aeb6f1b8 | -7.81111 | -72.99022 | 2025-07-12 06:22:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 911c2fec-9c17-3b5c-9209-f30f3d9a17cb | -10.3183 | -67.34667 | 2025-07-12 06:22:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a96e8dd7-9896-3760-9b67-0ef5f80405f2 | -7.81009 | -72.98959 | 2025-07-12 06:48:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb28b861-5f29-3be0-8379-3b5d3d3ed377 | -12.8813 | -49.1758 | 2025-07-12 07:40:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 17d72e15-3f3f-35a5-9423-66eb97748619 | -12.8809 | -49.1977 | 2025-07-12 07:40:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 44.7 |


[Clique aqui para ver as próximas entradas](README19.md)
