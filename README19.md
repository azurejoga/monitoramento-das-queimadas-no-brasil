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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1248df48-ca18-31cb-9d24-df58d0a35f17 | -11.8275 | -44.8044 | 2026-08-20 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 7286d7fc-bf8e-3e67-a6a9-38a5cfe34fc0 | -7.3603 | -45.8136 | 2026-08-20 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 194.4 |
| efeb688a-0621-3d45-8ad6-96c6778b0e71 | -11.1936 | -54.0199 | 2026-08-20 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 16bd67ff-49bf-35ac-b57d-f58e19fef34e | -8.6727 | -54.6492 | 2026-08-20 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 128.2 |
| d5d34e15-2553-346d-befd-2e416cd9febf | -23.0831 | -49.1746 | 2026-08-20 01:40:00 | GOES-19 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 9adbb07b-fa0b-355a-bdec-e33975473ea4 | -17.3365 | -43.6383 | 2026-08-20 01:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 97.9 |
| d673ef77-78b3-37fd-9215-a4398570be18 | -11.1939 | -53.9993 | 2026-08-20 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 87a14acb-1ca9-3d4d-b9ff-136a82ee557c | -9.2071 | -59.771 | 2026-08-20 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| dddeabaa-138c-3ee4-a1d2-ca077177117a | -6.3863 | -54.9451 | 2026-08-20 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 36b0649c-9df9-36e0-ad98-8b0f0d711afc | -6.5829 | -58.9851 | 2026-08-20 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| f3457ca0-f63a-3ce9-ae3b-56d32f085af1 | -9.12 | -61.6011 | 2026-08-20 01:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 779894e9-2631-3a60-a0b3-7f2b642bc32c | -11.8083 | -44.8072 | 2026-08-20 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| e65b5f1e-063f-39be-8978-105846b12e8f | -17.3372 | -43.6139 | 2026-08-20 01:40:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 01b0bda8-4571-3ca1-ad8f-c8565bb1ec52 | -6.6938 | -58.942 | 2026-08-20 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| d29c6ed4-f791-39df-811a-f55e3d4bd3c5 | -9.4256 | -60.4353 | 2026-08-20 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| ac819858-add4-38ac-a8a4-e6ceb3244bb7 | -9.2258 | -59.77 | 2026-08-20 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 0e0b5953-9dc9-384e-99cd-613d6fb7f281 | -9.4071 | -60.417 | 2026-08-20 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 551cf702-50a0-3c44-9b5a-94e9facf2610 | -9.4069 | -60.4362 | 2026-08-20 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 5c74118a-6740-363f-9445-54e946f61aa6 | -9.2256 | -59.7894 | 2026-08-20 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| bb08bcfd-6b6d-33a1-89e6-fecba7a9b7bd | -7.7551 | -49.2067 | 2026-08-20 01:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 52c713db-0ad6-3420-9b10-1863ffd3c1a7 | -11.2189 | -55.0585 | 2026-08-20 01:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 8a067ce2-84ee-332b-8ac3-11825e3c1063 | -11.8377 | -58.8445 | 2026-08-20 01:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 06e4b622-dd01-3f55-9124-03db2b97762b | -7.3413 | -45.8377 | 2026-08-20 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 9e3d74f7-9ac5-37a8-ab62-d651e8361a15 | -8.654 | -54.6505 | 2026-08-20 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 12947511-3303-3185-8945-d7fcd4cb43d2 | -7.36 | -45.8361 | 2026-08-20 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 169.6 |
| f69c343b-a836-3251-84e0-0ff05b3ba67c | -6.583 | -58.9658 | 2026-08-20 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 4140fabb-9f99-3949-b546-50e83f39481f | -9.4257 | -60.416 | 2026-08-20 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| a824359e-b291-304c-8e64-44970788aaf7 | -17.3372 | -43.6139 | 2026-08-20 01:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 159.4 |
| 91e35fb1-ac59-3994-8f63-87f56f963638 | -17.3572 | -43.6092 | 2026-08-20 01:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 67807b97-5da0-3ce3-bec4-579250cfc897 | -7.3415 | -45.8152 | 2026-08-20 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 177.3 |
| da0e3bb1-5771-36ee-b97f-557a01ea5d18 | -9.12 | -61.6011 | 2026-08-20 01:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 45984cbc-9fde-3a47-a1c2-203aad716462 | -17.3365 | -43.6383 | 2026-08-20 01:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 9823aa6b-461f-3780-a21d-61bae4c55c36 | -7.3603 | -45.8136 | 2026-08-20 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 65a9c31b-0108-3e34-8d35-b59316096790 | -11.2191 | -55.0382 | 2026-08-20 01:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| df60e00c-4808-3c02-9734-9aeafddc0353 | -11.8083 | -44.8072 | 2026-08-20 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| acf6a163-0e81-3d38-8761-6a898b526a0e | -6.3863 | -54.9451 | 2026-08-20 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| c1d49ed3-7ef8-3177-87b4-5cedfa07929c | -9.2258 | -59.77 | 2026-08-20 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 8090f61d-e336-3045-b660-bea00bcf3e72 | -6.5829 | -58.9851 | 2026-08-20 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 2565c02e-5ef4-3dcb-a41c-8b6636dcc958 | -9.4071 | -60.417 | 2026-08-20 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 27a2ac14-6f19-31a7-bbee-7d17b956b8cb | -12.4919 | -54.7158 | 2026-08-20 01:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| ba57fd6e-2fc2-3712-ab7e-e8a66bf0d689 | -6.7123 | -58.9412 | 2026-08-20 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 96a6b837-6e04-3b90-880b-24787d422291 | -12.4916 | -54.7364 | 2026-08-20 01:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| c16a1034-1a53-3056-b6ca-ee9b0de27d56 | -9.2071 | -59.771 | 2026-08-20 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 91352031-500e-3755-929e-bb88580798eb | -7.9751 | -44.6648 | 2026-08-20 01:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 60.2 |
| a848125e-fe5e-3b9e-8452-447370e81401 | -8.654 | -54.6505 | 2026-08-20 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 85b27a25-d70d-3cf7-ba1c-fa8c05b51036 | -8.6727 | -54.6492 | 2026-08-20 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 02529556-53c2-3a58-a43b-b915ba9fe479 | -7.3413 | -45.8377 | 2026-08-20 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 4d7c0f16-6d4b-343b-822d-5f7c479bb403 | -9.4069 | -60.4362 | 2026-08-20 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| a5a147a6-c12c-3a09-b68c-31f2e464338d | -14.4559 | -45.6019 | 2026-08-20 01:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 18ee62d3-1db7-3346-8a51-1b038ddfd215 | -6.6938 | -58.942 | 2026-08-20 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 1e605214-e9d5-35ac-ae7d-62161d633567 | -12.4914 | -54.7569 | 2026-08-20 01:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 3906999a-d9ca-3c88-b845-bef51c2446a4 | -9.2256 | -59.7894 | 2026-08-20 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 31a74a6f-ec42-3b5d-aab6-b2fcd0072b7e | -7.36 | -45.8361 | 2026-08-20 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 132.8 |
| ca97e3b5-4082-3623-be16-5f8a0c6bd4f3 | -11.1939 | -53.9993 | 2026-08-20 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 3058a4c2-7528-33b3-845c-e7fe76b0d485 | -11.1936 | -54.0199 | 2026-08-20 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| aae7ab0b-356f-36f0-91b1-42e8231acbb6 | -11.2189 | -55.0585 | 2026-08-20 01:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| e5715772-046e-31df-8cf3-d76d3b2cd55e | -9.4256 | -60.4353 | 2026-08-20 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 8ed03f91-c216-3281-a877-485e1a3553ce | -6.5829 | -58.9851 | 2026-08-20 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| f79f917a-44a4-3be7-b6ac-d8db0c4a263f | -11.1939 | -53.9993 | 2026-08-20 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 7df9f655-9bda-3bba-80c5-f93fff09564b | -11.2191 | -55.0382 | 2026-08-20 02:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 19171236-5b26-3cf0-8ec6-60542a7a1624 | -6.3863 | -54.9451 | 2026-08-20 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 127deb3e-d8e0-3683-a0d1-5da514078365 | -8.6729 | -54.629 | 2026-08-20 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 77ab61e8-b2ae-3c1f-80a7-c483655b8882 | -7.9751 | -44.6648 | 2026-08-20 02:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 369a5ee8-10c3-39aa-8d7f-6f21c4b21e58 | -17.3372 | -43.6139 | 2026-08-20 02:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 146.5 |
| 634cbc5a-aaa2-359d-a533-cec5279a25cd | -7.3415 | -45.8152 | 2026-08-20 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 159.4 |
| d3ec485c-4e4f-34b9-8443-cb745d24e99d | -7.3603 | -45.8136 | 2026-08-20 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 154.5 |
| be1e2ed9-9c16-32b4-b9aa-ea6f128634bd | -9.4256 | -60.4353 | 2026-08-20 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 7f5d61ac-4214-35e8-be1c-338a14db8875 | -7.36 | -45.8361 | 2026-08-20 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 24d0bbe1-3fed-300d-92a6-02ff0df7e5a3 | -8.6727 | -54.6492 | 2026-08-20 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 139.9 |
| fccecdfe-190f-345e-aa5e-7b6401630df1 | -9.2258 | -59.77 | 2026-08-20 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 15a5bfd5-dc6d-385f-8e22-58c090450729 | -8.6725 | -54.6695 | 2026-08-20 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| fbdda21d-1d41-362e-ba8d-aba9ad1a3874 | -7.3413 | -45.8377 | 2026-08-20 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 627dcad4-6993-3639-a648-42ded7fdafe2 | -11.1936 | -54.0199 | 2026-08-20 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 0fbddca2-dba9-3716-99bc-0885a38f3429 | -11.2189 | -55.0585 | 2026-08-20 02:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| d1082284-2d7e-30eb-b351-bea1a24da41c | -17.3572 | -43.6092 | 2026-08-20 02:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 60.1 |
| b898d4ff-f3ac-3670-a08a-d5ac5fc297fa | -9.4257 | -60.416 | 2026-08-20 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| bdf2ecc7-509d-3ecd-be86-8cdefc84a440 | -6.4391 | -52.7343 | 2026-08-20 02:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 721ebfc3-5464-37df-b5ec-13769c65db76 | -14.2213 | -52.883 | 2026-08-20 02:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 8e411d78-4770-37fb-b8b9-377d5800f6b0 | -17.3365 | -43.6383 | 2026-08-20 02:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 78.5 |
| b468685a-40a6-30d0-9ed4-190394040b2d | -6.6938 | -58.942 | 2026-08-20 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 8780e027-7e12-38d3-b499-9668ceec7eda | -8.654 | -54.6505 | 2026-08-20 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| d2f670d0-700a-39eb-9558-642814e1e6d9 | -12.4916 | -54.7364 | 2026-08-20 02:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 991ce7d8-b8bf-39ef-a8e8-11e5712c7ed1 | -9.12 | -61.6011 | 2026-08-20 02:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 673cb275-ef93-3226-a495-81172d20b16e | -6.7123 | -58.9412 | 2026-08-20 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 695ea2d8-923f-3f00-a7b2-a7d8719fab47 | -9.2071 | -59.771 | 2026-08-20 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 11468aa9-3290-3220-9530-5b193986e57a | -13.5683 | -51.6739 | 2026-08-20 02:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 5ce62c74-6d58-36a2-bf85-c7179f147853 | -11.2189 | -55.0585 | 2026-08-20 02:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 142.8 |
| e936d684-c361-3c03-9364-6f33e85aff74 | -11.8377 | -58.8445 | 2026-08-20 02:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 1f81de17-60e6-3ce9-9b79-a4711e3629f9 | -7.3603 | -45.8136 | 2026-08-20 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 124.1 |
| a5e6c0f7-c441-38fc-ae44-669422ea5a4d | -11.8083 | -44.8072 | 2026-08-20 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 2b4655a0-51e1-3fa8-bb39-f1913b2b506e | -11.2 | -55.0601 | 2026-08-20 02:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| b66365e5-db8e-3a75-aad1-69efe7709682 | -11.1936 | -54.0199 | 2026-08-20 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| e3e876ff-bacf-3969-a9fc-f0072533c01f | -6.4391 | -52.7343 | 2026-08-20 02:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 1a0a7eb7-a6e0-3846-8b63-efc6e71b8f0c | -8.6729 | -54.629 | 2026-08-20 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 6667e446-bf31-31f5-ad3d-a664aa25548c | -6.3863 | -54.9451 | 2026-08-20 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 7f812bfd-3b43-30f8-820f-37a2b5e8ca92 | -9.2256 | -59.7894 | 2026-08-20 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| d51bd98c-3eb2-3b80-ab88-f16d99026660 | -7.36 | -45.8361 | 2026-08-20 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 123.6 |
| dbd6f7d6-312f-3eed-a9f5-62ae9e0182b4 | -8.6725 | -54.6695 | 2026-08-20 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 92f2b71b-bd6f-3655-b712-8c0a29821f33 | -8.6727 | -54.6492 | 2026-08-20 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 162.3 |
| 568a7cfa-c84e-3862-86a5-d024e65d27ea | -6.6938 | -58.942 | 2026-08-20 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |


[Clique aqui para ver as próximas entradas](README20.md)
