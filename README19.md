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
| cf735575-7841-3e5e-8b0c-371f0178f821 | -3.3969 | -54.490398 | 2024-10-28 01:34:08 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f419588-c9c9-3ecf-bd68-1c4bac3d0b50 | -3.1077 | -54.2635 | 2024-10-28 01:34:12 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad562c41-713b-302b-8211-1cb4b391d132 | -2.2612 | -53.749401 | 2024-10-28 01:34:24 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ede017eb-e713-3a7d-9cd5-6cf37e207bba | -2.2671 | -53.774101 | 2024-10-28 01:34:24 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88bc3330-5cf6-398e-be3f-602ad84e9f26 | -2.2729 | -53.798599 | 2024-10-28 01:34:24 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93d7e81e-5029-3949-80ad-db8cb668a0d3 | -2.2516 | -53.751701 | 2024-10-28 01:34:24 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a95d8754-5220-3d96-9ca1-e819f5b6ef6f | -2.2574 | -53.776299 | 2024-10-28 01:34:24 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d25a4915-bb38-3fb4-be17-5c49b3458001 | -2.2632 | -53.8009 | 2024-10-28 01:34:24 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c426e4c-a376-3158-b0b3-ba94258b1195 | -1.5317 | -52.087002 | 2024-10-28 01:34:29 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c672927-bd15-3d6c-a710-0adb4fde46d2 | -1.1723 | -53.488602 | 2024-10-28 01:34:41 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 604d296e-fadb-38f0-9f17-001a1f075223 | -1.1627 | -53.490898 | 2024-10-28 01:34:41 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be2a0c90-9a4d-30bd-b9af-3862c5e30850 | -1.0684 | -53.652599 | 2024-10-28 01:34:43 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6acb3295-2468-38b4-826b-1ccc85d2dd3d | -1.2838 | -55.715099 | 2024-10-28 01:34:47 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1e5d118-f7e3-3791-846f-5f7df428c40d | -1.1653 | -53.4957 | 2024-10-28 01:35:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| b5f6b79e-863f-35b6-976d-487d04bc6228 | -1.1836 | -53.5158 | 2024-10-28 01:35:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 9577e951-d804-3404-be32-a7f3f843c679 | -1.1836 | -53.4956 | 2024-10-28 01:35:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 3234a3d1-64f6-3bfd-aa61-1c8d4447585d | -1.5349 | -52.0874 | 2024-10-28 01:35:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 29451b77-86a4-3adf-9e2f-3d6950dd89d5 | -1.5532 | -52.1076 | 2024-10-28 01:35:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| b7ba18cf-459e-3974-b17e-501ca9038a1c | -1.5533 | -52.0871 | 2024-10-28 01:35:14 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 0040556e-d0be-3c3b-b07b-aff29b5c5021 | -1.9763 | -52.0804 | 2024-10-28 01:35:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 939ccfd5-39a5-315d-a068-eb0c226f1bf1 | -2.0499 | -52.0791 | 2024-10-28 01:35:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| e2ff67bc-976c-368c-a1d7-8c37516122ca | -2.1826 | -50.6065 | 2024-10-28 01:35:18 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 83661d97-178e-3fd0-8d46-90f069255295 | -2.2662 | -53.8027 | 2024-10-28 01:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| a1ca1a09-506b-3d44-a955-1f03fd6bd030 | -2.2662 | -53.7825 | 2024-10-28 01:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 247.2 |
| 71e14f7c-9f51-33db-aa95-ae2691c43cb9 | -2.2663 | -53.7624 | 2024-10-28 01:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 00003d27-cc21-335b-9bbe-ce93d18afcc1 | -2.2845 | -53.8023 | 2024-10-28 01:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 2cce1087-850b-3a0b-a8c8-6dae5740b86b | -2.2846 | -53.7822 | 2024-10-28 01:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 140.7 |
| e99c6bdd-b44e-3009-99a8-a11baa8a223b | -2.2846 | -53.762 | 2024-10-28 01:35:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 2f5683e5-369d-3a09-a69e-aa34e0c08448 | -2.3919 | -48.5484 | 2024-10-28 01:35:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 7ad53650-771a-33ba-a340-04fcc99b4679 | -2.4104 | -48.5479 | 2024-10-28 01:35:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 7a4e1438-3422-3dba-be2a-4e5cca96c550 | -2.5127 | -51.1821 | 2024-10-28 01:35:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 1e3f1523-6680-390d-852c-2a5c4c067c09 | -2.5251 | -47.442 | 2024-10-28 01:35:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| c72180ff-f0a1-36c3-9271-6ae74f23894a | -2.531 | -51.2024 | 2024-10-28 01:35:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 7c2ebd19-2b13-358a-a26c-e60804959a58 | -2.5311 | -51.1816 | 2024-10-28 01:35:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 41dea912-675b-3837-a432-736de5716dd0 | -2.6399 | -51.7374 | 2024-10-28 01:35:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 57c3f815-aabe-3d61-b3e3-2ae1f0f8b19b | -2.7033 | -49.33 | 2024-10-28 01:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 0ba20ff3-440b-38e1-9bfe-dc63b23ef0ae | -2.7034 | -49.3088 | 2024-10-28 01:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 04a8bbec-889c-31eb-be10-015d2b6b86d3 | -2.7219 | -49.3083 | 2024-10-28 01:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 89d7f8e1-a122-3939-96cd-ece76ce87f59 | -2.8556 | -53.3256 | 2024-10-28 01:35:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 8e7a585c-5a3f-3242-a94f-aa2c2d8862de | -2.9047 | -45.2819 | 2024-10-28 01:35:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 1aa03ccf-4e1e-3da0-8e16-e05e6b6a4aa3 | -2.9048 | -45.2594 | 2024-10-28 01:35:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 200.8 |
| 77836b7b-e7d7-321a-9d3e-4f1417f9dac9 | -3.0317 | -50.4176 | 2024-10-28 01:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| f4db20e2-ba03-3ab5-9559-88239d116d6d | -3.0317 | -50.3967 | 2024-10-28 01:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 096caa91-4c85-3d95-9af2-4955baad5cec | -3.0501 | -50.4171 | 2024-10-28 01:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 45e7d8ac-ae5b-3c4f-be88-ff70c9c30e83 | -3.0538 | -49.4895 | 2024-10-28 01:35:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| be02974e-1b69-3c2c-bddb-10376ddb4720 | -3.4014 | -46.3131 | 2024-10-28 01:35:25 | GOES-16 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |
| f73d1aa8-032d-3436-9892-2be2c476d144 | -3.6911 | -51.5622 | 2024-10-28 01:35:26 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| bf402fc5-ae17-33f1-aaf6-089aa0b8fd54 | -4.0681 | -50.024 | 2024-10-28 01:35:28 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 780f925a-5bff-3a3c-be7e-e33048e6f54c | -4.1771 | -44.1109 | 2024-10-28 01:35:29 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| e291a6b3-90f4-3bd8-ab59-e92e7c75555a | -4.2611 | -45.5372 | 2024-10-28 01:35:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 14a5afb6-c4df-3e7b-bc7a-fa2b69bc0bb9 | -4.2796 | -45.5587 | 2024-10-28 01:35:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 73.5 |
| e0a30666-3be0-36a9-9c34-c41700594913 | -4.2797 | -45.5362 | 2024-10-28 01:35:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 381.5 |
| 9af1f76c-98a0-3d4c-a14e-81e36b434681 | -4.2799 | -45.5138 | 2024-10-28 01:35:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 98.1 |
| f99bb203-c1a9-34ba-a0ea-d464eb769d86 | -4.4093 | -45.6641 | 2024-10-28 01:35:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 941f0fe6-a4c0-3ee7-97a7-45fd1edb4079 | -4.4094 | -45.6416 | 2024-10-28 01:35:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 610175e0-31aa-388f-89a0-ad3c8835295e | -4.4279 | -45.6631 | 2024-10-28 01:35:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 11648d4b-69e3-366d-b335-5fe5a907f245 | -4.428 | -45.6406 | 2024-10-28 01:35:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 155.9 |
| aaa941ce-03ad-370b-ba2e-8a8bfa5fea4c | -4.7766 | -46.4022 | 2024-10-28 01:35:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 0087d138-274f-385e-9173-7656ac9ad305 | -4.7768 | -46.3801 | 2024-10-28 01:35:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 68.8 |
| ca998a35-1c4f-322b-8387-46ae78e62d94 | -1.1836 | -53.5158 | 2024-10-28 01:45:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 230e3262-f7e1-3767-a482-4bfe365bcfa7 | -1.1836 | -53.4956 | 2024-10-28 01:45:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 30c68d04-e37b-3457-9281-71b8d4fab281 | -1.9763 | -52.0804 | 2024-10-28 01:45:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 55ffaf01-236c-3bb9-80f7-f08aa60949aa | -2.0499 | -52.0791 | 2024-10-28 01:45:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 7f2bf54d-161f-3d0c-8425-93fba7f568a3 | -2.1826 | -50.6065 | 2024-10-28 01:45:18 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 7d301634-a8d3-348d-ad84-2a03d6720207 | -2.2662 | -53.8027 | 2024-10-28 01:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 622c4743-41b5-3637-94d5-a6f331648752 | -2.2662 | -53.7825 | 2024-10-28 01:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 207.6 |
| bf481840-fc1b-36d8-a9fd-6099ecb7880f | -2.2663 | -53.7624 | 2024-10-28 01:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| e3d7eab2-c00d-33ad-83e9-20d0fabfc8d0 | -2.2845 | -53.8023 | 2024-10-28 01:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 92ea790d-eb4b-33fe-8bba-5baaf76c4725 | -2.2846 | -53.7822 | 2024-10-28 01:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 175.1 |
| 96cc0308-0e2d-3ab4-8032-446f67f023e1 | -2.2846 | -53.762 | 2024-10-28 01:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| ffa18812-1e63-31e4-9648-cd57188822a6 | -2.3919 | -48.5484 | 2024-10-28 01:45:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 07a53328-6ccd-3605-ae12-96152c19c610 | -2.4104 | -48.5479 | 2024-10-28 01:45:19 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 872aebae-3401-3ef7-a85a-bac0bc22aacc | -2.5311 | -51.1816 | 2024-10-28 01:45:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 63f70b9c-ade2-354b-84e5-0ce255a152e3 | -2.5127 | -51.1821 | 2024-10-28 01:45:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 662c916b-a410-3971-998a-b8b6cad4e574 | -2.6399 | -51.7374 | 2024-10-28 01:45:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 23cdbab1-b5e2-37a1-a830-45d19489cb91 | -2.7219 | -49.3083 | 2024-10-28 01:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| cbcd21c2-2316-3f14-a97a-e7e4d7ed9083 | -2.8054 | -51.7951 | 2024-10-28 01:45:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 93df23a5-918c-3192-86a3-e399815e7df2 | -2.8555 | -53.3459 | 2024-10-28 01:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| b87d0e49-8df5-357c-8da4-813e51966ffe | -2.8556 | -53.3256 | 2024-10-28 01:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 0ae5fe0c-3e3d-3932-8b34-0ebcbfa3ddb6 | -2.8739 | -53.3454 | 2024-10-28 01:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| d327a8cd-ee92-3217-9b88-e0cc89d38160 | -2.8739 | -53.3252 | 2024-10-28 01:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 1a848555-7e15-38cc-aa18-220092ff7049 | -2.9047 | -45.2819 | 2024-10-28 01:45:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 051593b8-1e1f-3396-85e4-610fcab8674c | -2.9048 | -45.2594 | 2024-10-28 01:45:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 9c33992a-c811-309a-9f3f-ecd338da5b4e | -3.0317 | -50.4176 | 2024-10-28 01:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| c0bbabcc-6d33-3e7a-935c-febd0c02ecd9 | -3.0538 | -49.4895 | 2024-10-28 01:45:23 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| fa498f8c-f8a9-33d4-b9f9-d07bde63a90c | -3.272 | -46.2072 | 2024-10-28 01:45:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 7ea5e4ec-15e1-31b9-aaec-f82d40cdca18 | -3.6911 | -51.5622 | 2024-10-28 01:45:26 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| b0f53a1b-c32b-3aee-882c-b24db973e7f5 | -4.1771 | -44.1109 | 2024-10-28 01:45:29 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 19256140-723d-3f6a-8fb0-2eed2100a3f4 | -4.2796 | -45.5587 | 2024-10-28 01:45:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 37d33b92-8b18-3bce-ba39-bbbad0c0d735 | -4.2797 | -45.5362 | 2024-10-28 01:45:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 284.9 |
| 564c7eb3-3f31-3b6d-86ab-3df6bc3a3cd3 | -4.2799 | -45.5138 | 2024-10-28 01:45:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 85.7 |
| efe87c50-240c-3f98-b1e5-18f556702a48 | -4.4094 | -45.6416 | 2024-10-28 01:45:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 28e26b6f-aaed-381d-83ce-8e5812fdb4a8 | -4.4279 | -45.6631 | 2024-10-28 01:45:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 66.0 |
| c3270842-eae5-3bd1-a2b7-1773deaf241d | -4.428 | -45.6406 | 2024-10-28 01:45:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 158.4 |
| 64abb9e7-32c9-3d0e-be53-23e2445dada3 | -4.7766 | -46.4022 | 2024-10-28 01:45:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 993afb5e-c8e3-3787-912e-c7af54bafca3 | -4.7768 | -46.3801 | 2024-10-28 01:45:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 6c58012b-0c4c-3a49-9722-ac5dc48763c4 | -1.1836 | -53.4956 | 2024-10-28 01:55:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 69aec145-6bef-39c1-a941-aee4abd0c442 | -1.9763 | -52.0804 | 2024-10-28 01:55:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 427014cd-e5a2-3118-85d7-27681badb2bd | -2.0499 | -52.0791 | 2024-10-28 01:55:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| a3846a5c-3255-3f0a-8a7a-0f35c2d5557e | -2.2662 | -53.8027 | 2024-10-28 01:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |


[Clique aqui para ver as próximas entradas](README20.md)
