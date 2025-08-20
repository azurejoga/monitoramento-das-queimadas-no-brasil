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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02c774ba-43f5-3e20-9a65-1267eb352439 | -13.1555 | -54.9357 | 2025-08-20 02:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 7e3fb469-7c1c-3ee6-8314-cfbb058a51a3 | -8.034 | -47.6639 | 2025-08-20 02:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 4f5bb61d-9630-3f6a-ab92-c5e90011d6a9 | -6.1476 | -57.7215 | 2025-08-20 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 95ae72ed-7230-3f41-b682-7edf0aa9d1c0 | -9.1895 | -59.6364 | 2025-08-20 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| f65b770b-3301-30bb-8def-0c7c4d3c02ee | -13.1367 | -54.9171 | 2025-08-20 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| c7425a8b-117c-3323-a540-f8d7cb0a9cf2 | -15.0002 | -54.8135 | 2025-08-20 02:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 54.8 |
| bfa02351-12db-3c3f-93c9-5932e22f7a6c | -20.339 | -51.7062 | 2025-08-20 02:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 68575d80-5b2a-3a88-91c5-2c1e8ca6054f | -13.1364 | -54.9376 | 2025-08-20 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| de7b1e78-8b80-373f-9cb9-b9c36a68fbc3 | -8.6343 | -62.1367 | 2025-08-20 02:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 4578b465-a7f9-3312-bc7f-fe79f21be43f | -13.1555 | -54.9357 | 2025-08-20 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 05b57ad7-856f-3dd6-9851-7ed03b117556 | -20.3594 | -51.7023 | 2025-08-20 02:20:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 2d37d767-8f37-32f3-bf6c-11d939085493 | -13.1558 | -54.9151 | 2025-08-20 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 6eee9ecc-7fcf-3ebd-8054-ad44a95edc60 | -20.339 | -51.7062 | 2025-08-20 02:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 09064256-fd00-3ca0-95df-b6f6b89d158f | -13.1558 | -54.9151 | 2025-08-20 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 4255c5ee-f9b7-3511-87d9-caecf0c411f9 | -15.0002 | -54.8135 | 2025-08-20 02:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| e0b065ad-55fd-39da-948f-3f56cb34b656 | -21.8746 | -47.2212 | 2025-08-20 02:30:00 | GOES-19 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.7 |
| 6c7b6900-be1c-3884-9af8-4a6628709662 | -6.9605 | -42.8816 | 2025-08-20 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 52.4 |
| b2671f7e-5162-3bd3-b60b-4f98f84a4d82 | -8.034 | -47.6639 | 2025-08-20 02:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 4d42786c-0d9f-39d7-a15c-6088a964ebe4 | -13.1364 | -54.9376 | 2025-08-20 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 883658bc-386a-3602-a1e0-b763694a0cc3 | -9.1895 | -59.6364 | 2025-08-20 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 6f9f91ec-d37d-32b9-a383-ebf66b33ab00 | -4.912 | -43.2337 | 2025-08-20 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 3fe390bb-8a65-3ab9-aa4b-1f7b5febc2f9 | -13.1555 | -54.9357 | 2025-08-20 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 6cfcf066-cd88-38fd-8f96-4ffb03293ca5 | -6.9607 | -42.858 | 2025-08-20 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 49.6 |
| cbdb8123-0800-3828-ae1b-abd46c7d9d77 | -20.3594 | -51.7023 | 2025-08-20 02:30:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 1d9072ac-566d-3140-8a44-b5b4a0b29b4d | -8.6343 | -62.1367 | 2025-08-20 02:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 1e51a340-fc2c-349c-9a79-3ce31264b1b3 | -18.6861 | -46.9667 | 2025-08-20 02:30:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 4b27febe-de06-315f-9525-710bf0f521c7 | -13.5743 | -47.0302 | 2025-08-20 02:30:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 04da2ffd-4ac4-3561-9826-61fcc9a4a64d | -8.6342 | -62.1557 | 2025-08-20 02:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 0ac9af40-6b08-30b9-a55f-7b637477c4b9 | -24.1363 | -49.1179 | 2025-08-20 02:40:00 | GOES-19 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 351da313-4e12-3ef0-b9a3-269a5bdbf0e1 | -9.1895 | -59.6364 | 2025-08-20 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 306108d7-0d2a-3de7-b458-19eea70ccb29 | -4.912 | -43.2337 | 2025-08-20 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| ac9916ac-bcb3-3f64-ac21-959c233ce0a3 | -13.1364 | -54.9376 | 2025-08-20 02:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 9b962507-105b-3616-a64e-e58d2b235a4c | -6.9416 | -42.8834 | 2025-08-20 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 49.1 |
| d3ce51f7-0bba-3f62-bfcd-8af16b4bbc38 | -8.6343 | -62.1367 | 2025-08-20 02:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 521403a9-a1e7-3aac-a57b-f3ecdeddc573 | -20.339 | -51.7062 | 2025-08-20 02:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 93.9 |
| ce86fc55-fdd2-37d9-b6ac-d8cefe3740d2 | -6.9605 | -42.8816 | 2025-08-20 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 57.9 |
| f33a274e-2d86-3da8-b342-db158be6b542 | -13.1558 | -54.9151 | 2025-08-20 02:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 8a407fec-6d0c-31e5-a4b1-0d29a34f5684 | -13.1367 | -54.9171 | 2025-08-20 02:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 79c0731d-c045-3fdf-a57d-3c5daf87cddf | -13.1555 | -54.9357 | 2025-08-20 02:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 816ec2db-a40d-382f-afee-2617daccf1ac | -8.034 | -47.6639 | 2025-08-20 02:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 70c0d23e-1a4e-3029-9264-70408519ad0b | -13.1558 | -54.9151 | 2025-08-20 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 87e503e2-c327-3dde-b368-d41106a3fba1 | -6.9605 | -42.8816 | 2025-08-20 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 60.2 |
| 81a63a6f-c2b0-39ec-83b8-ef922ecbcaec | -8.69 | -62.1153 | 2025-08-20 02:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 0b7346f7-1a56-3cc8-8969-c72c1e5cdfb8 | -8.034 | -47.6639 | 2025-08-20 02:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 1456dcd1-a4ba-3ade-8cc3-081fba768c84 | -11.6002 | -50.5454 | 2025-08-20 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| d6352842-0ac0-348e-b413-8c7bb86e4882 | -11.1616 | -46.9022 | 2025-08-20 02:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| bf3a59d0-e0fe-38fc-a909-ef2e1024cfa5 | -6.9416 | -42.8834 | 2025-08-20 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 56.2 |
| 0dabb802-f8c8-3df7-a32f-39947821d35f | -13.1364 | -54.9376 | 2025-08-20 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 57dd27a1-daeb-3e25-b9e0-a50420008b81 | -22.3603 | -50.4076 | 2025-08-20 02:50:00 | GOES-19 | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Cerrado | 85.5 |
| a8bcf97b-4017-3cc0-bedd-9c095c077c0e | -20.339 | -51.7062 | 2025-08-20 02:50:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 0c48fc44-4a27-3eaf-b309-209da5411e89 | -13.5743 | -47.0302 | 2025-08-20 02:50:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 8e53bb1f-46bf-3e11-8f47-22848ab97b3f | -8.6901 | -62.0963 | 2025-08-20 02:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| bd73d11d-bd79-3917-870f-08bfff994ec9 | -13.1555 | -54.9357 | 2025-08-20 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| b4cdb38d-a7cb-3920-b709-d360513b975a | -9.1895 | -59.6364 | 2025-08-20 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 2c601455-6dbf-3c48-91cd-bd10415e22b6 | -13.1367 | -54.9171 | 2025-08-20 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 3f2aca43-b6d5-36ef-8926-a5efb9b4ed3b | -13.1558 | -54.9151 | 2025-08-20 03:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 2fc39745-2651-3f4c-a918-1d85e20898f2 | -22.3812 | -50.4029 | 2025-08-20 03:00:00 | GOES-19 | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 1a81bece-c85c-359b-8ebd-1a034c408b89 | -6.9605 | -42.8816 | 2025-08-20 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 43.8 |
| 327b2fe6-886f-3726-9aaa-c5b444b87978 | -11.6002 | -50.5454 | 2025-08-20 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| eecef931-bb47-36e8-a141-be73cd1d2441 | -8.034 | -47.6639 | 2025-08-20 03:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| cdee81b5-c449-3c96-8a7c-c3514b227f12 | -11.6006 | -50.524 | 2025-08-20 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 5fb22b52-a98c-3071-a1f2-d257aafc83a2 | -8.6901 | -62.0963 | 2025-08-20 03:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 39cf40b3-e306-382d-8a55-7dc9dfd7029d | -20.339 | -51.7062 | 2025-08-20 03:00:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 90.2 |
| f6a5a353-af64-324c-9264-7460a028ada7 | -13.1367 | -54.9171 | 2025-08-20 03:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 8b4e077e-d46e-3785-b33a-159e1586fa01 | -13.1555 | -54.9357 | 2025-08-20 03:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 17cee8e5-1a08-3294-aafd-c3e633335b7b | -9.1895 | -59.6364 | 2025-08-20 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 745ec648-73d3-3530-a28f-80a5d08c6f89 | -22.3603 | -50.4076 | 2025-08-20 03:00:00 | GOES-19 | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Cerrado | 91.5 |
| a0f35117-a175-349d-b0e2-0183773b9002 | -8.69 | -62.1153 | 2025-08-20 03:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 58d0b23b-55f3-3295-90c5-d64100ce9882 | -13.1364 | -54.9376 | 2025-08-20 03:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 084933be-734c-31e3-827d-82df923ab828 | -11.6002 | -50.5454 | 2025-08-20 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| c9c8df88-df65-32e2-8cc7-5dfe86ede68c | -15.0002 | -54.8135 | 2025-08-20 03:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 9064c76f-740e-3463-9dd4-569b3ae2d962 | -8.6901 | -62.0963 | 2025-08-20 03:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| ea33834b-3f20-3a9e-a797-92216a9a5fa6 | -13.5743 | -47.0302 | 2025-08-20 03:10:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 934b03f0-6204-336a-b826-dcd765585685 | -13.1555 | -54.9357 | 2025-08-20 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 7ebcdf0c-4c61-3d5e-9045-e250b13933d6 | -13.1364 | -54.9376 | 2025-08-20 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| b01c050c-1c9b-3548-a21e-599f9887cbd9 | -13.1558 | -54.9151 | 2025-08-20 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| c7e4f9ea-dfc5-349a-ba05-e9e3494e7989 | -8.034 | -47.6639 | 2025-08-20 03:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 65b7ffc3-91d5-305d-b99f-766db54aec13 | -9.1895 | -59.6364 | 2025-08-20 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 1a6922a5-1728-3314-a8b8-71956c38a7c3 | -8.6716 | -62.0971 | 2025-08-20 03:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 33.7 |
| be2912e3-d02f-3c6d-834b-9dbf0dd7d728 | -4.912 | -43.2337 | 2025-08-20 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 11c2e5ed-0b6c-33c5-ad45-eab0f671e82e | -22.3812 | -50.4029 | 2025-08-20 03:10:00 | GOES-19 | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 1ec530a3-e68e-3788-870c-c38094cd8317 | -13.5936 | -47.0272 | 2025-08-20 03:10:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 03389b97-d70f-32b3-8799-bb725eddb403 | -20.339 | -51.7062 | 2025-08-20 03:10:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 1ea80e02-0334-381d-a7ef-82d7d28f16c0 | -11.5812 | -50.5476 | 2025-08-20 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| a51a39d6-7022-3b77-a78f-c5e1159107fa | -22.3603 | -50.4076 | 2025-08-20 03:10:00 | GOES-19 | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Cerrado | 87.1 |
| b9586bf5-a680-3bd6-b5f9-5696c0f82ce7 | -8.69 | -62.1153 | 2025-08-20 03:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 751b4730-b4b2-39d4-9abb-257d28ad85a5 | -6.12484 | -42.95777 | 2025-08-20 03:15:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 6f7532a0-318e-33de-8931-6583352e6dd9 | -6.94792 | -42.88113 | 2025-08-20 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| d96b66dd-5aae-3017-9cbc-0215e88d6e3d | -6.94919 | -42.87429 | 2025-08-20 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 9b15a021-8c3d-3937-8161-de98fc57a493 | -4.17078 | -42.02441 | 2025-08-20 03:15:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4b405286-d5f4-315f-a002-4cced1bae40c | -6.94208 | -42.87316 | 2025-08-20 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 951c6e4e-1d8a-34aa-ab1e-6e88286f6ea4 | -4.72449 | -38.39887 | 2025-08-20 03:15:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 70f2d28a-dd2d-3514-8388-317465c080e7 | -6.94514 | -42.87863 | 2025-08-20 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 6bd557d7-d468-3f57-bdb0-7e909e970136 | -4.16953 | -42.03128 | 2025-08-20 03:15:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 5ba1ffb4-964e-3cce-baf2-1df880f6cbf3 | -6.96895 | -42.86902 | 2025-08-20 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a8405f1c-1181-37ce-a19a-a21e4aa88e3e | -4.17198 | -42.03212 | 2025-08-20 03:15:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f1c7268f-dd79-39a5-b48b-9c559d221a3d | -3.82011 | -41.57224 | 2025-08-20 03:15:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8682c60d-0a81-3ba4-b444-74830f72725e | -4.1732 | -42.02521 | 2025-08-20 03:15:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9672c250-edc7-35d6-9a5e-97ab7bcd74b7 | -3.81547 | -41.55818 | 2025-08-20 03:15:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8140f6df-b1a9-39a3-8421-16e765fd67f7 | -6.94645 | -42.87181 | 2025-08-20 03:15:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 24.2 |


[Clique aqui para ver as próximas entradas](README9.md)
