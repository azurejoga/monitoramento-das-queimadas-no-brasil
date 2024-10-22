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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f219f908-2d7a-390d-b2d4-0441f22e5c1e | -3.45209 | -49.15414 | 2024-10-22 04:19:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd6731d2-6044-38d8-b71e-37b603f14b81 | -3.45169 | -44.27218 | 2024-10-22 04:19:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8517889-5fa3-313d-be1e-7813ba7d8092 | -3.33679 | -49.0185 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b727d434-88d4-3136-9871-913fc5a36291 | -3.31178 | -44.14479 | 2024-10-22 04:19:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cf796358-8714-330a-80df-d1a446ca1207 | -3.31124 | -44.14822 | 2024-10-22 04:19:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 236799cb-e43c-3257-8283-a46f6d4c226f | -3.29876 | -45.83052 | 2024-10-22 04:19:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 22cc6ac2-ce5f-34af-b7e4-24253a9b8209 | -3.29825 | -45.83048 | 2024-10-22 04:19:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6c54e3cf-a530-3f55-bce7-5f3ebb16104d | -3.29352 | -46.9874 | 2024-10-22 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 290d0a21-e026-3be4-95e2-ec80bf4b2bf9 | -3.29287 | -46.99149 | 2024-10-22 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79e7d624-f748-30b6-9096-e314954d8710 | -3.21805 | -46.5307 | 2024-10-22 04:19:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f791b6e-883d-37dc-8169-37d8be4ec0c0 | -3.21661 | -44.3836 | 2024-10-22 04:19:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed968ae2-259f-32f8-8de5-7218bb13f787 | -3.15974 | -45.64477 | 2024-10-22 04:19:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 06314d27-0991-3f1e-b6c9-5ceef5e18912 | -3.11802 | -49.52176 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b105b240-597e-3b39-8fe1-1fb6609c4fb6 | -3.11384 | -49.52111 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68f773a7-da2d-30b7-85b7-bfeeb0f72c25 | -3.11322 | -49.52498 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2fcbe0cf-2aa5-3163-9db0-8fa989195763 | -3.08389 | -46.5541 | 2024-10-22 04:19:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c58476b0-a9bf-3845-99af-8cb323438cb2 | -3.08326 | -46.55803 | 2024-10-22 04:19:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47f06e5a-ba93-3743-b767-683d89ac5f81 | -3.08218 | -45.93379 | 2024-10-22 04:19:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15c0544a-432a-3a27-a9f7-859bb6c374ab | -3.08038 | -46.55355 | 2024-10-22 04:19:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d706d5a4-1080-33ad-a1bd-2c8bb6b79de0 | -3.04426 | -48.01746 | 2024-10-22 04:19:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87759c81-c3a2-3e81-baff-77dd39d29e32 | -2.99279 | -45.61127 | 2024-10-22 04:19:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41fc1e40-9549-3dd7-b81f-8a92aee8ae05 | -2.99222 | -45.61491 | 2024-10-22 04:19:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de3b2013-2041-39a4-93f7-de4270314572 | -2.9894 | -45.61074 | 2024-10-22 04:19:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7af2f6f-b731-37bd-b3fd-543e9bd5d98c | -2.98883 | -45.61438 | 2024-10-22 04:19:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7544f12-6210-3eee-a35b-d07c2f842256 | -2.98601 | -45.61021 | 2024-10-22 04:19:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 803337c2-2447-35f0-9bf0-d6063beb7e39 | -2.98544 | -45.61385 | 2024-10-22 04:19:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76f45324-0421-3281-8081-ddf7cd418029 | -2.98486 | -45.61748 | 2024-10-22 04:19:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 85ce7683-8b51-3397-9875-8bc3b250a2e2 | -2.98429 | -45.62112 | 2024-10-22 04:19:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9868af38-b77a-310e-a03d-7b67526e510d | -2.98205 | -45.61331 | 2024-10-22 04:19:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d17b19a2-f77a-3594-a361-f0df512f53e7 | -2.98147 | -45.61695 | 2024-10-22 04:19:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a96dce0f-4bc4-366d-8295-b642a005ac50 | -2.96603 | -47.9954 | 2024-10-22 04:19:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75044fcd-5ea7-3ee5-88f8-d859a22c82d3 | -2.96453 | -48.00461 | 2024-10-22 04:19:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 132ee7eb-2591-3550-9ac0-4417d56be453 | -2.96073 | -48.004 | 2024-10-22 04:19:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7749a158-3349-399e-bd7e-439de9e46279 | -2.95998 | -48.00863 | 2024-10-22 04:19:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cb35515-5392-3f2e-bc80-ae7198e8a419 | -2.9208 | -48.95908 | 2024-10-22 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 603e5195-68a0-3c70-9a5c-2ebec19e5c4b | -2.92022 | -48.96261 | 2024-10-22 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cb51e6c7-fd07-3abb-ba52-04c6a84fa679 | -2.89891 | -50.40542 | 2024-10-22 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e322208-9d6f-32d2-82a6-819092af2110 | -2.89819 | -50.40981 | 2024-10-22 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62b38f9e-7ed9-3b44-aa85-bd0df20a7b05 | -2.89564 | -50.40696 | 2024-10-22 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ed5486f-45a7-3255-b4d2-111a933282ba | -2.87131 | -54.47888 | 2024-10-22 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5db2f453-7a09-3e3a-b337-9fb79a4c4096 | -2.87063 | -54.48288 | 2024-10-22 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35deb03e-773e-3113-b4b1-46b5b1056c08 | -2.86688 | -54.47775 | 2024-10-22 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0127ed21-d6f6-389f-8293-4aaceeba6a81 | -2.86621 | -54.48185 | 2024-10-22 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfa88d37-bd24-3e03-8256-4140ed26fcc9 | -2.86548 | -54.47771 | 2024-10-22 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1cc2088-53fd-3cd2-a6bc-c4f7522a7b68 | -2.85871 | -45.46394 | 2024-10-22 04:19:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a33041ce-5852-3bdd-be6c-ec8bcbbcac26 | -2.85533 | -45.46341 | 2024-10-22 04:19:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 16ce70a5-4ad8-34ca-b0bc-754a3a8f4c69 | -2.85475 | -45.46702 | 2024-10-22 04:19:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e95ce1f2-2f38-3c64-88f5-00ffdc034b04 | -2.85195 | -45.46288 | 2024-10-22 04:19:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3945c27a-0654-3989-bae2-e8883af21941 | -2.85137 | -45.46649 | 2024-10-22 04:19:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9ab557e4-894b-3ccf-8111-1dd44c606e32 | -2.79347 | -45.78644 | 2024-10-22 04:19:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b3d78b9-fe45-3cff-a155-b2eceeaca4e0 | -2.76725 | -45.97279 | 2024-10-22 04:19:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22d2f4d7-6f96-3c9a-bbeb-8100855bc251 | -2.76548 | -49.32265 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 330cdb16-8984-3ab1-a833-cc429a4f8c07 | -2.76486 | -49.32642 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 1e769317-3a86-3515-9598-b7da41c7ce14 | -2.76363 | -49.33393 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c80b15f7-b316-36a9-ba22-1da31d66a640 | -2.76302 | -49.33769 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce3ee4fe-db85-383a-b8f6-ad7db3e2cbab | -2.76241 | -49.34143 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1379eca4-53ae-392f-bea6-ff8e10bfa28d | -2.76196 | -49.31818 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| aab3866b-0a40-3211-85ff-2d699e1009b0 | -2.76134 | -49.32195 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 85124725-9054-38a5-94bf-cd203bc8751d | -2.75826 | -49.34075 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a69f56c8-97c0-322f-8fab-48f8a285acd6 | -2.75412 | -49.34008 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 146228f8-f3f6-34b9-971f-08d26cc0cf98 | -2.7535 | -49.34382 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 160895f3-e287-3fbb-8fe0-9b042d388c2c | -2.74997 | -49.33939 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ffaa725d-0213-3e0b-bfbc-0c497b74c306 | -2.72291 | -47.74696 | 2024-10-22 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abde1dd0-d1dc-3bf8-81f0-608878261a61 | -2.63633 | -48.43788 | 2024-10-22 04:19:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84cd866b-2653-388c-9b87-7c4ca7599bb6 | -2.63554 | -48.44284 | 2024-10-22 04:19:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b73bf0e6-8988-3a66-b66b-98c3b68f3048 | -2.63242 | -48.43721 | 2024-10-22 04:19:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0bac0bea-cf15-32f1-86a2-7c1f0a08422a | -2.63163 | -48.4422 | 2024-10-22 04:19:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08379b83-bc02-3e92-bd8f-839c2c120f1c | -2.63083 | -48.44719 | 2024-10-22 04:19:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09940fd6-931c-32f9-9fc7-aaea5613396f | -2.59993 | -46.12614 | 2024-10-22 04:19:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1b4c1ba-b793-3012-9d35-46fc77f7b6cf | -2.59934 | -46.12995 | 2024-10-22 04:19:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf1ba4cc-1500-31fd-bab2-bc9e66e221f0 | -2.59819 | -46.12875 | 2024-10-22 04:19:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3bec6d01-91c1-3c8f-ad58-f4867ce1d0ce | -2.47778 | -49.11766 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6d547802-25fe-3ec5-b96b-56a08b1c6cde | -2.59758 | -46.13255 | 2024-10-22 04:19:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2513615f-a2ed-3687-8216-76fc1526d6a3 | -2.59587 | -46.12941 | 2024-10-22 04:19:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51b31ad3-d0b9-3a9e-ad39-1118b75caa24 | -2.47488 | -49.10966 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3cb3df14-bffd-3c50-b1cd-13360602e986 | -2.58081 | -46.1348 | 2024-10-22 04:19:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0dff525-0a96-307e-add7-22dfa8e2874d | -2.57819 | -49.14161 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 86f727c0-ec9f-3ee9-b1bc-4c0c06c77c09 | -2.57794 | -46.13045 | 2024-10-22 04:19:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f2aee1f-cbfd-3489-8795-664f987995a3 | -2.57734 | -46.13426 | 2024-10-22 04:19:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7dba010c-4935-34ff-99f7-d48cf4a4fb34 | -2.57408 | -49.14094 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1a8048ce-4b16-39fe-a29e-9e87e5987d6e | -2.56778 | -45.99299 | 2024-10-22 04:19:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9eb4d4c-e9a4-31dc-974d-e753ff846cf0 | -2.56702 | -47.2694 | 2024-10-22 04:19:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60bb0433-3888-35e7-900c-a513e1e56f64 | -2.56433 | -45.99245 | 2024-10-22 04:19:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44d25eea-8114-3fb9-9efb-63ee2c6810ce | -2.56373 | -45.99621 | 2024-10-22 04:19:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fff1888b-4830-3a14-acc4-91c587a9f8d5 | -2.56088 | -45.99191 | 2024-10-22 04:19:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8be6538e-bb4d-3ef1-92b0-5499ca6b46fb | -2.56029 | -45.99567 | 2024-10-22 04:19:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e876a7e2-7299-3e00-bf8b-fa9140dbd246 | -2.53664 | -49.66378 | 2024-10-22 04:19:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 410518ff-3d7f-35ce-9720-f6f05d417888 | -2.53554 | -45.99565 | 2024-10-22 04:19:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fe6f5c4-739f-3c80-9e0e-863b42eadbf0 | -2.53209 | -45.99511 | 2024-10-22 04:19:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26beab38-b449-3de9-8992-3db50d86daa2 | -2.51095 | -45.88857 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 584e1e61-e9b5-38ee-b596-e34ac107cf82 | -2.50752 | -45.88802 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71d39fd3-490b-3e39-899a-4911b2472c8a | -2.49898 | -45.87517 | 2024-10-22 04:19:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 747fe460-35f4-3029-b39f-8032fa0d7590 | -2.48659 | -49.11531 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78a50c11-caf9-3273-8464-410b46860194 | -2.48308 | -49.11098 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 698623be-c4c0-39e5-b144-c7895a846b40 | -2.48248 | -49.11466 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4ec35663-e96b-31c1-9a50-7dbadd3c47c0 | -2.48189 | -49.11832 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 727e95fd-229c-337a-855d-00d273b6debe | -2.48129 | -49.122 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c8c2c3b2-6994-3a29-a0c1-b6f0cdfd717e | -2.47898 | -49.11032 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b1c4d8c3-d0b3-3a91-bbcb-6cc0c788e8dd | -2.47838 | -49.11399 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6d2827ab-7891-3521-b914-aa294aa7d29a | -2.47719 | -49.12133 | 2024-10-22 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |


[Clique aqui para ver as próximas entradas](README23.md)
