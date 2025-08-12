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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e31e1003-cc83-3ac0-a731-221a5b7dbffc | -8.9401 | -60.7288 | 2025-08-12 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 5d16f2b4-e9ea-35b7-ba66-a8604d8a13e4 | -12.5742 | -47.0006 | 2025-08-12 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 228.8 |
| b9e40b26-0060-3f06-8e04-eeef1e966d3c | -19.2907 | -48.4291 | 2025-08-12 01:30:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 819bfe66-20ad-3393-a6d4-ef97620ecef5 | -23.0038 | -49.0309 | 2025-08-12 01:30:00 | GOES-19 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 53e681cb-f97b-3eb1-b1f2-3e6ecbb7f705 | -12.555 | -47.0034 | 2025-08-12 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 96250447-9489-344a-92d9-4b2d85d9d33f | -3.8394 | -47.7436 | 2025-08-12 01:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 4bcab3f3-9850-36ea-a4ae-d06340f9228b | -16.2961 | -52.9016 | 2025-08-12 01:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 2adba5d7-28ce-3e0f-a281-496fd2cf6d8c | -22.9828 | -49.0361 | 2025-08-12 01:30:00 | GOES-19 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 120.1 |
| d838c20e-b0b9-368f-a26f-d87249840d72 | -16.2957 | -52.923 | 2025-08-12 01:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 983c26ec-3c4b-3649-87ad-9668731c8671 | -9.7041 | -49.4825 | 2025-08-12 01:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 2a829964-79e7-3d40-b94e-97bb95844f7c | -7.1299 | -60.1182 | 2025-08-12 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 2dea0262-fb32-36fa-a0c1-1d34b093d235 | -7.1483 | -60.1174 | 2025-08-12 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 0790e980-1588-3506-be15-efc8defea7e7 | -7.1482 | -60.1366 | 2025-08-12 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| db362581-a53e-3d33-bd6f-60b653572b22 | -22.9828 | -49.0361 | 2025-08-12 01:40:00 | GOES-19 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 0716ccb3-93d3-366b-b917-3eae239f2acd | -23.0038 | -49.0309 | 2025-08-12 01:40:00 | GOES-19 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 744b57ef-4800-3c90-b0e4-5a845fe80389 | -3.8394 | -47.7436 | 2025-08-12 01:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 0a4f8d13-bd6d-3ff0-b1a8-7eba9a6482f0 | -12.555 | -47.0034 | 2025-08-12 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 8b629ff4-02fb-33af-b977-6b9b9018a736 | -7.1298 | -60.1374 | 2025-08-12 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 6b0b7160-73b2-3965-8694-361786b422b3 | -9.723 | -49.4806 | 2025-08-12 01:40:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 826c7833-bfa3-3651-a42a-f81181d25807 | -19.2907 | -48.4291 | 2025-08-12 01:40:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 563ff79c-04be-32bd-9b5b-fca8b5180679 | -17.6549 | -46.6757 | 2025-08-12 01:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 989d7b38-c1fe-35e4-a81c-aab17c6783e3 | -16.2957 | -52.923 | 2025-08-12 01:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 434a10fe-23e3-36b0-808b-0b5e23c291f7 | -7.1299 | -60.1182 | 2025-08-12 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 27baa9f6-2ebd-393f-833b-141ccf019528 | -17.6743 | -46.6948 | 2025-08-12 01:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 839f90c5-8189-3d8d-9091-81d817a1a67d | -17.6749 | -46.6715 | 2025-08-12 01:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 46fbeea5-ff03-3699-a295-738b25e23165 | -12.5742 | -47.0006 | 2025-08-12 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 141.0 |
| d0e33b37-d4d3-3e0a-b98f-357c238e00d4 | -17.6544 | -46.699 | 2025-08-12 01:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 93ecc457-2e70-3ecd-96a0-66831d8f3630 | -16.2961 | -52.9016 | 2025-08-12 01:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| fe6d6275-e503-3e40-a4ab-1d2023213412 | -8.9401 | -60.7288 | 2025-08-12 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 25775cf6-9929-3373-a96b-c278f4d0d079 | -12.7759 | -45.4445 | 2025-08-12 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 0f87c2f4-6a25-3092-baeb-dc52b47152fe | -12.5746 | -46.9781 | 2025-08-12 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| ab752950-6099-3dd6-9840-5e6a86ff032d | -13.0543 | -56.8343 | 2025-08-12 01:40:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 86dde71a-f177-3f8c-90bd-3df355b5de87 | -8.5211 | -43.3063 | 2025-08-12 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 3af1aabe-607d-3d32-86e5-eae2ea5e70aa | -8.5788 | -54.7162 | 2025-08-12 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| f02ac116-ba8b-3dbc-a0ad-6251a8c238ae | -12.555 | -47.0034 | 2025-08-12 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| eef9295b-3bab-34c0-925a-8c920a9ac80b | -12.5742 | -47.0006 | 2025-08-12 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 139.4 |
| a264f9ae-0a3e-383a-8f78-6a0a580d2176 | -7.1299 | -60.1182 | 2025-08-12 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 178.5 |
| 895a7dc5-98eb-341e-b51d-7bf2e52e1227 | -22.9828 | -49.0361 | 2025-08-12 01:50:00 | GOES-19 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 61.8 |
| a84fb5b8-e3b6-361e-9f60-ee19e751e136 | -7.1483 | -60.1174 | 2025-08-12 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 135.5 |
| 84463976-b7f3-3abf-bdbe-9a570324cc58 | -8.9401 | -60.7288 | 2025-08-12 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 44106f64-1f36-3e91-92cf-8b8a5f2f5a29 | -12.5746 | -46.9781 | 2025-08-12 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| e7939a15-f2f8-32b3-bee1-6fcbe71c4526 | -7.0799 | -59.1964 | 2025-08-12 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 1edd0336-8d15-39be-9e7c-1c8d0f295ded | -4.3012 | -48.0917 | 2025-08-12 01:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 5505b770-38c1-3c9b-9c87-0889c3965387 | -8.5788 | -54.7162 | 2025-08-12 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| b8f12af6-fa98-36f8-ad2d-819af73fff66 | -7.1298 | -60.1374 | 2025-08-12 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 4e02f618-7117-3475-a85f-384f45b5699f | -9.723 | -49.4806 | 2025-08-12 01:50:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 3d3b60a5-6240-3b87-a9df-07d40eb07c52 | -16.2957 | -52.923 | 2025-08-12 01:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| cd0d575c-736e-34a6-a0c4-f907d54a5624 | -16.2961 | -52.9016 | 2025-08-12 01:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 7bbb3ffe-591d-326d-80dc-ee296564be58 | -6.5856 | -44.564 | 2025-08-12 01:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 51138a1f-7cbf-36c9-84d4-2f694588b87a | -16.3153 | -52.9201 | 2025-08-12 01:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 690731b5-1cf3-3109-8d5f-a4a290b72b51 | -23.0038 | -49.0309 | 2025-08-12 01:50:00 | GOES-19 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 55.5 |
| e3c2245c-1891-32e2-8073-21399ce58505 | -12.5554 | -46.9809 | 2025-08-12 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 564b743e-72dc-347f-9de1-e51d27ca2fa0 | -7.1482 | -60.1366 | 2025-08-12 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| e521d231-6c39-3370-ac57-1c0df38abc10 | -12.7759 | -45.4445 | 2025-08-12 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| c6b28da0-d9f2-3260-9e5c-0481d227240d | -8.5211 | -43.3063 | 2025-08-12 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 867f2f25-01f1-3388-94b8-75449e969338 | -12.5742 | -47.0006 | 2025-08-12 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 130.4 |
| f8156ed0-779b-3939-a878-80f06fee6628 | -17.6743 | -46.6948 | 2025-08-12 02:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 97.2 |
| bbb9030d-2b77-3f4f-bee6-c3dc1c878bfd | -17.6349 | -46.6799 | 2025-08-12 02:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 2989b943-a06e-3de5-ae13-a9d2c3b63de8 | -12.5746 | -46.9781 | 2025-08-12 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| abc68ee4-3c0e-39fc-9c3d-75121aaefbad | -9.723 | -49.4806 | 2025-08-12 02:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 78fca6b5-d3d0-331d-b6fa-44d3c3521ddd | -8.5211 | -43.3063 | 2025-08-12 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 3b5bc8eb-dc6e-3e7d-ad94-cfa8786d3eff | -23.0038 | -49.0309 | 2025-08-12 02:00:00 | GOES-19 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 68d1bad4-dd7d-30a5-9902-524d1ad55411 | -7.1299 | -60.1182 | 2025-08-12 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 122.4 |
| c2703a8d-ddfb-341c-a15b-280f794daa4f | -12.555 | -47.0034 | 2025-08-12 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 31a84f89-0e28-3d1e-b7c1-a404128686aa | -7.1483 | -60.1174 | 2025-08-12 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.4 |
| e801b529-ed2c-36ef-ba06-47127786d23f | -8.9401 | -60.7288 | 2025-08-12 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 9a03c2d9-f623-32c6-9424-e811a303f9a5 | -17.6544 | -46.699 | 2025-08-12 02:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 243.6 |
| 83cb1318-bcf1-342e-9550-4ea506d9cc58 | -17.6549 | -46.6757 | 2025-08-12 02:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 620.7 |
| 3597fbf1-31f9-314b-abab-c503b9267587 | -16.2957 | -52.923 | 2025-08-12 02:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| abf2c8ae-9c5c-38d2-8fc1-dea79a752c1b | -12.5554 | -46.9809 | 2025-08-12 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| a174e7aa-3a32-3d4f-910c-c31df95f208c | -8.5788 | -54.7162 | 2025-08-12 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| b44f8cd7-4de3-3ec4-b98e-7480adc0b84b | -7.1298 | -60.1374 | 2025-08-12 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 6a4f13ec-41f8-3706-a0e3-cd8ecbed67b9 | -6.5856 | -44.564 | 2025-08-12 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 0d18f8cc-9002-3a69-9c78-232f7efda721 | -16.2961 | -52.9016 | 2025-08-12 02:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| a3b9a5cb-1d29-3809-8358-897407453843 | -12.7759 | -45.4445 | 2025-08-12 02:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 45.7 |
| a9f1f253-2965-32f4-9054-1825c30103b6 | -22.9828 | -49.0361 | 2025-08-12 02:00:00 | GOES-19 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 58.7 |
| a21aeca2-924b-3e37-89e1-edaadc5cd6d1 | -17.6749 | -46.6715 | 2025-08-12 02:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 197.1 |
| 3f54171b-c91c-37ae-8ab2-c2de75094064 | -7.1482 | -60.1366 | 2025-08-12 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 2de58d43-6899-326a-81c4-a24a5c8482a7 | -17.6555 | -46.6523 | 2025-08-12 02:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 0b5f15fd-7a3c-3ec7-a6ac-b7ca5a5c3768 | -9.723 | -49.4806 | 2025-08-12 02:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 29f4d740-6fda-3398-9b6d-9f594c5b4e7d | -16.2961 | -52.9016 | 2025-08-12 02:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 88d45f1f-c2f3-3531-a843-f33237f0632f | -7.1299 | -60.1182 | 2025-08-12 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.8 |
| d9672913-1cad-3da3-b226-b36152aa52ec | -8.5211 | -43.3063 | 2025-08-12 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 9d9b3f33-5e8a-3615-87d0-a3323fd08dfd | -16.2957 | -52.923 | 2025-08-12 02:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 33c403b7-7a4d-382a-b902-d92d1e3ba173 | -12.5746 | -46.9781 | 2025-08-12 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| a5c14c33-4a36-3b98-8d2e-4ce7e740ff88 | -21.7801 | -48.3036 | 2025-08-12 02:10:00 | GOES-19 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 164.3 |
| a4410f6a-f055-3209-bb43-9ae3823cfd2b | -8.5208 | -43.3298 | 2025-08-12 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.6 |
| 502c12b1-b765-3c29-9abc-8d53472bd799 | -8.5788 | -54.7162 | 2025-08-12 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 4f92bb7f-76d0-3a3d-9f51-f8ae5d66d183 | -7.1482 | -60.1366 | 2025-08-12 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 150a307c-f686-3682-9077-c52d1c584e67 | -7.1298 | -60.1374 | 2025-08-12 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| bbbdea09-4581-3610-8929-54a16cbe186b | -22.9828 | -49.0361 | 2025-08-12 02:10:00 | GOES-19 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 3bc77404-11e0-3158-8f89-41d89c636ea8 | -3.8394 | -47.7436 | 2025-08-12 02:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 0a72b110-ebc4-3dc7-bd0e-3372b3b04594 | -21.7593 | -48.3086 | 2025-08-12 02:10:00 | GOES-19 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 10d56210-465b-3e30-b697-dcfbd54b49d8 | -12.5742 | -47.0006 | 2025-08-12 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 162.0 |
| 0602bcab-db7b-3d4c-bfaa-e33dfc05d0dc | -8.9401 | -60.7288 | 2025-08-12 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| ec303af9-4258-3bfe-a593-d8db450dd0d2 | -12.555 | -47.0034 | 2025-08-12 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 1d2f0919-37b4-3304-9495-927ab0a87031 | -6.5856 | -44.564 | 2025-08-12 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| ca385982-7b86-3e8c-be3d-2559886c36e2 | -12.7759 | -45.4445 | 2025-08-12 02:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 20a7d046-f146-3b20-8639-9365154a3412 | -9.7041 | -49.4825 | 2025-08-12 02:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 3de7e088-4120-3313-baf5-2d713a93e3bd | -7.1483 | -60.1174 | 2025-08-12 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.0 |


[Clique aqui para ver as próximas entradas](README6.md)
