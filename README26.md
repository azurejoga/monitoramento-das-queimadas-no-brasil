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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6e76505-b8ed-3ea4-a53e-31eacedd3674 | -8.0129 | -43.1513 | 2025-08-04 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 404ae201-358b-38a5-a340-42140ee2a35b | -7.994 | -43.1534 | 2025-08-04 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.0 |
| 68385b54-ca16-3948-9ac4-85cb389da779 | -8.0132 | -43.1278 | 2025-08-04 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.0 |
| 753f593f-e9b5-3fe8-8479-8bfa6a6aa25f | -7.9429 | -45.7823 | 2025-08-04 06:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 042a4340-a364-39d5-8c7b-860b9a353cf1 | -8.0132 | -43.1278 | 2025-08-04 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.3 |
| 0f8102a3-f720-3a2d-bee1-95e81260325d | -8.0129 | -43.1513 | 2025-08-04 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| b7e60139-4ed6-377c-aad1-762a15745efb | -7.9429 | -45.7823 | 2025-08-04 06:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 3751da81-e3b2-3273-ad03-cdc8fde17737 | -13.0535 | -56.8947 | 2025-08-04 06:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| a4081951-dcf1-3b98-af09-bc023a47939b | -7.994 | -43.1534 | 2025-08-04 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 114.2 |
| afedc238-de98-3c7d-a293-750e3e77148d | -7.9943 | -43.1298 | 2025-08-04 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.1 |
| 402155d8-b077-3216-8930-ac84ee24f8b5 | -13.0726 | -56.893 | 2025-08-04 06:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 4ce91d1f-5275-3732-a6c2-138c0ebb9fbc | -7.994 | -43.1534 | 2025-08-04 07:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 95.5 |
| 32aa38d2-1095-3de3-af93-1b639a1a5d26 | -13.0726 | -56.893 | 2025-08-04 07:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 91b8ebd5-084c-3808-adc9-93419dac3767 | -13.0538 | -56.8746 | 2025-08-04 07:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| acf0e94e-c2b5-309a-9bea-049f52c3e3f5 | -8.0132 | -43.1278 | 2025-08-04 07:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| 498229b1-0018-323c-83f9-3315ef0e6580 | -13.0535 | -56.8947 | 2025-08-04 07:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 74208dd1-f5a2-3f11-9e9c-477f11d5340b | -8.0129 | -43.1513 | 2025-08-04 07:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| ee6dd479-ad4f-3c0c-8b1e-f30d927c58c5 | -7.01481 | -59.8255 | 2025-08-04 07:09:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 7d4fd1bc-4544-3ced-b84f-0229b3961283 | -7.9429 | -45.7823 | 2025-08-04 07:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| c5943328-249f-345e-a74b-004d771afc77 | -7.994 | -43.1534 | 2025-08-04 07:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 40.3 |
| 37303389-b5b6-317a-aefb-04c26344d24c | -7.9429 | -45.7823 | 2025-08-04 07:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 7262cb01-3dc3-330f-b84f-1701cf21824a | -8.0129 | -43.1513 | 2025-08-04 07:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 38.6 |
| ba6f4776-0bee-3faf-aa78-a9a0ff2999b3 | -13.0726 | -56.893 | 2025-08-04 07:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 58413fb8-4e37-3ac2-9c77-21c60ab4aa5e | -7.9429 | -45.7823 | 2025-08-04 07:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| ac875d8d-a667-3b6e-aa19-ac3aae47b530 | -13.0535 | -56.8947 | 2025-08-04 07:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 070e28c0-f78d-3f72-9281-0c60c719cbc9 | -7.994 | -43.1534 | 2025-08-04 07:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 47.2 |
| 97d6dc59-eeca-38fb-8408-c7a79f32847a | -13.0538 | -56.8746 | 2025-08-04 07:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 6fb3556f-3c89-3843-8fdf-e5f611a110aa | -7.9429 | -45.7823 | 2025-08-04 07:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| c776f381-d837-3c7d-9101-db7ab799b4ab | -13.0535 | -56.8947 | 2025-08-04 07:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 5fe04585-1b2a-32aa-8658-59f1972e9f8b | -8.0132 | -43.1278 | 2025-08-04 07:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| 608b12f4-2668-383f-bb50-7566ad9fa084 | -13.0726 | -56.893 | 2025-08-04 07:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 57bf4562-988c-3ff2-820d-51b63bce0e68 | -7.994 | -43.1534 | 2025-08-04 07:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.3 |
| 0143a23d-313b-3b98-a17e-ac779742f444 | -8.0129 | -43.1513 | 2025-08-04 07:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| b224f3fc-7b70-3713-8799-39ea1f869b8c | -7.994 | -43.1534 | 2025-08-04 07:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.0 |
| da6e856c-1e68-3931-b840-d54e7f7763ba | -13.0726 | -56.893 | 2025-08-04 07:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 96d44dd9-be16-3bb3-b284-393a15688255 | -7.9429 | -45.7823 | 2025-08-04 07:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| d4e6b70b-aca7-3222-844a-72d63a87651c | -13.0538 | -56.8746 | 2025-08-04 07:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 5dda9a1e-6166-33a3-b057-eefcffeeb7b8 | -13.0535 | -56.8947 | 2025-08-04 07:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 146.1 |
| d37ce704-1b96-3cbf-87f2-72dae2ceeaf6 | -13.0728 | -56.8729 | 2025-08-04 07:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 249ce5a3-1bc3-3512-b69b-253c600754cb | -13.0726 | -56.893 | 2025-08-04 08:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 638f964e-6bc4-3d49-b58d-66def6e1ec5d | -7.994 | -43.1534 | 2025-08-04 08:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.8 |
| af09924d-f775-35ea-ae1b-59c403fb8966 | -8.0129 | -43.1513 | 2025-08-04 08:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.6 |
| 0ddffc83-15bf-3716-b60e-9747c6cf8106 | -13.0535 | -56.8947 | 2025-08-04 08:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| e89270e2-c6c7-3832-9fdb-595fe33242c7 | -8.0132 | -43.1278 | 2025-08-04 08:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.2 |
| 2958f20e-49c2-365f-af87-2437c33ecb3d | -7.994 | -43.1534 | 2025-08-04 08:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.2 |
| 64cab998-c61c-377a-a60a-fe5c3b8580e8 | -13.0726 | -56.893 | 2025-08-04 08:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| ebdcde57-eb8b-340b-80b8-1a8aea7afa20 | -8.0132 | -43.1278 | 2025-08-04 08:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.9 |
| e39cb5f0-26f7-3d31-958b-7ebf662d345e | -13.0538 | -56.8746 | 2025-08-04 08:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| e884031e-2d85-37a9-8e86-b387839fd3cd | -8.0129 | -43.1513 | 2025-08-04 08:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.1 |
| 2c8dcc76-23c6-3c4d-91f7-57841bcc03c7 | -13.0535 | -56.8947 | 2025-08-04 08:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 38dd7ec8-0be0-3e7c-9ed1-c866810f6611 | -8.0129 | -43.1513 | 2025-08-04 08:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.5 |
| a4d41318-2982-38d9-a0e8-1218f88332d6 | -8.0132 | -43.1278 | 2025-08-04 08:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 47.8 |
| 96d5e01f-fd43-3a88-8fe6-5618e750952a | -13.0535 | -56.8947 | 2025-08-04 08:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 8c3589b3-946c-3cef-9faa-4529558fcb37 | -13.0726 | -56.893 | 2025-08-04 08:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 31abd181-5840-3c1e-bb7a-b456c2fdce28 | -7.994 | -43.1534 | 2025-08-04 08:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.8 |
| 3fba7f07-8735-39fa-a0a2-425529bc76bf | -13.0535 | -56.8947 | 2025-08-04 08:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 38695913-dbf8-32b7-8869-181af59461f0 | -13.0726 | -56.893 | 2025-08-04 08:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| c9af7982-c2c1-315a-a035-b3bb78bec18b | -13.0726 | -56.893 | 2025-08-04 08:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 63e422ae-789d-33e0-863e-a76012aeaf79 | -13.0535 | -56.8947 | 2025-08-04 08:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| d2618dfd-2d1a-3f1a-9bcd-bdd32123891e | -13.0535 | -56.8947 | 2025-08-04 08:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 34d5ddc0-e08c-3149-a96f-1e88d878da03 | -8.0129 | -43.1513 | 2025-08-04 10:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 110.2 |
| b1317bc7-6f64-381c-a7fe-49775adb5a8b | -8.0132 | -43.1278 | 2025-08-04 10:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| 461ab7ea-edb2-3f24-a934-d9e47b368bea | -14.1297 | -45.4043 | 2025-08-04 10:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 120.3 |
| cf1a1e13-ee21-30e4-a6dd-2e85503a9832 | -8.0132 | -43.1278 | 2025-08-04 10:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 111.9 |
| 050c9cc3-0536-358a-a2f5-16e26a775802 | -8.0129 | -43.1513 | 2025-08-04 10:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 106.1 |
| 0ef3e891-63ff-3deb-98f3-2673be9664ac | -8.0132 | -43.1278 | 2025-08-04 11:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 130.2 |
| fe4e0fcf-50b1-3ce5-9bfa-cbfe54feb083 | -8.0129 | -43.1513 | 2025-08-04 11:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 111.7 |
| 50efcc9d-1b4c-34fa-aafa-1bb13658ceab | -8.0132 | -43.1278 | 2025-08-04 11:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 131.4 |
| bdaf3e2c-3233-325f-ba23-d105eac4dbfd | -8.0324 | -43.1022 | 2025-08-04 11:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 107.1 |
| 08d753c2-225f-382b-bc3a-626d8d5d2fb3 | -8.0129 | -43.1513 | 2025-08-04 11:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 118.2 |
| bbdcb147-8887-3780-8023-9969dd822183 | -8.0321 | -43.1257 | 2025-08-04 11:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.7 |
| 559fb2de-1605-3d4c-8a6c-60d0027ea35d | -7.994 | -43.1534 | 2025-08-04 11:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 103.9 |
| e2279b23-4286-3e19-a5c2-32ead899c7d0 | -8.0321 | -43.1257 | 2025-08-04 11:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 118.3 |
| a8cda7ea-28c3-3a60-9ccf-8e7d1953340b | -8.0324 | -43.1022 | 2025-08-04 11:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 111.1 |
| 8880fa79-e4a8-3cc0-b868-57f2778d9eb8 | -8.0132 | -43.1278 | 2025-08-04 11:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.5 |
| 27dd8a45-61dd-3f73-b16e-df5b4b7c6ca5 | -7.994 | -43.1534 | 2025-08-04 11:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |
| acf30dcc-3b9e-3837-a83e-edb731b599e2 | -8.0129 | -43.1513 | 2025-08-04 11:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 105.6 |
| 581aeee5-8c37-3c70-b0a9-84a22104e73a | -7.994 | -43.1534 | 2025-08-04 11:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.2 |
| 7894676f-4090-3f5a-bc4a-3daeb84b1a55 | -8.0129 | -43.1513 | 2025-08-04 11:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 116.4 |
| e6f52e13-dfec-3981-9075-80f20fc39f80 | -8.0132 | -43.1278 | 2025-08-04 11:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 121.1 |
| 0e3e78f1-1959-301a-9e58-e793b3c69426 | -8.0324 | -43.1022 | 2025-08-04 11:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 119.5 |
| 73a867ae-c176-3d9b-bfaf-f1348e29a67a | -8.0321 | -43.1257 | 2025-08-04 11:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 130.9 |
| 7339f76f-fe5a-3fb7-95ae-226072e1888a | -6.06555 | -44.67932 | 2025-08-04 11:34:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| ab474fbd-b40e-3c32-848b-a92b71ed6b1c | -8.01194 | -43.17617 | 2025-08-04 11:34:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| 12bebacb-3aee-3b32-9aa9-0ac615b60510 | -6.06258 | -44.67312 | 2025-08-04 11:34:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 97964f71-6691-3c14-b54d-80623909ed53 | -8.03557 | -43.12359 | 2025-08-04 11:34:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 172.8 |
| 02346580-7a84-3998-9f50-250fc7a79e6a | -8.01646 | -43.1485 | 2025-08-04 11:34:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 50.6 |
| 2afc8afa-20ee-372a-be45-678512024cb1 | -8.03993 | -43.0967 | 2025-08-04 11:34:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 103.6 |
| 36851954-d910-37d2-b5eb-e936997e2e87 | -8.00177 | -43.14625 | 2025-08-04 11:34:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 246.6 |
| 641a85e1-e077-308a-9dcd-5d3e9c3eac79 | -8.04009 | -43.1039 | 2025-08-04 11:34:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 141.2 |
| 0ca75fd2-1b60-39e1-ab0d-b3e92ae59f3d | -8.03551 | -43.13085 | 2025-08-04 11:34:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.1 |
| 17db39bf-e897-3575-9b5f-98d7fcf57962 | -19.77045 | -40.93411 | 2025-08-04 11:36:00 | TERRA_M-M | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 645bf94f-40fa-3262-97c4-231083ac5bd5 | -18.62788 | -40.31161 | 2025-08-04 11:36:00 | TERRA_M-M | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| eaee6cdf-e916-3793-9dcb-535d44f21979 | -8.0129 | -43.1513 | 2025-08-04 11:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 128.1 |
| b4bb4176-9d3b-3e2e-a1b0-0afa914abde3 | -7.9931 | -43.224 | 2025-08-04 11:40:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 154.0 |
| ba981ec5-aeae-3abd-a361-0e8a7c42d594 | -8.0324 | -43.1022 | 2025-08-04 11:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 164.4 |
| de59e53d-6fa1-3166-9d7e-5ecc0bed8b61 | -8.0132 | -43.1278 | 2025-08-04 11:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 125.3 |
| 06495c33-b2d8-35ef-bded-8e787e5f715d | -8.0321 | -43.1257 | 2025-08-04 11:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 129.3 |
| 96f25747-fa71-3a34-a2bc-50b8925266e7 | -7.994 | -43.1534 | 2025-08-04 11:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 127.3 |
| c6c6647e-9ddf-31bd-8986-11b9b78f170d | -8.0321 | -43.1257 | 2025-08-04 11:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 158.0 |


[Clique aqui para ver as próximas entradas](README27.md)
