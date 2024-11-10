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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40bc4822-1901-3bec-b5fc-3ac474bab45f | -2.7771 | -49.3704 | 2024-11-10 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 0b2d5ee4-b847-38e8-b8c4-39b4ed752442 | -17.2933 | -57.4857 | 2024-11-10 01:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 165.1 |
| b1f1147a-6494-328f-8fb6-136e5392e22a | -2.7772 | -49.3492 | 2024-11-10 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| ab98be99-74dd-3663-ae27-50b733a0ba84 | -2.4182 | -51.9689 | 2024-11-10 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| d8e16679-ea14-37d6-8313-c512c068d5d0 | -3.4383 | -50.2999 | 2024-11-10 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| a0b3c7de-c22b-3f60-99bb-be23ac8e7630 | -3.9669 | -48.1716 | 2024-11-10 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 168.0 |
| 5503cd40-9f50-3120-a50b-3914430164db | -2.0768 | -48.8342 | 2024-11-10 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 610e73e3-c1b3-3032-89b8-ff87977e9806 | -17.313 | -57.4834 | 2024-11-10 01:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.4 |
| 55cad23c-48a9-3ec4-b623-c4e2f27493d4 | -2.0316 | -52.0589 | 2024-11-10 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| b01c4f20-a2d4-3792-a0f3-9f6bbe518d6a | -17.293 | -57.5062 | 2024-11-10 01:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.5 |
| 90c789a9-8045-383f-a9bd-7bac55fffd6b | -2.4366 | -51.9685 | 2024-11-10 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 8ed19613-4571-3e8b-8f1a-b5dcacec0a6b | -2.5696 | -50.6812 | 2024-11-10 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 0c2864f4-b5cd-3bef-9f9b-d719c7047b84 | -3.6923 | -51.2929 | 2024-11-10 01:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 2d66c411-1f43-3c05-ab4d-efa9fbe970c7 | -2.2095 | -47.733 | 2024-11-10 01:30:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 1a6f6886-0667-3b41-9f1b-4a335e32718e | -2.5512 | -45.4062 | 2024-11-10 01:30:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 8eb183b3-a117-3bdf-8ef4-59ccc4db0196 | -3.1239 | -50.4358 | 2024-11-10 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 162.5 |
| d738b275-82b8-3aef-b1c9-9d230dfb8b85 | -3.1238 | -50.4568 | 2024-11-10 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 92e80331-37a9-3c98-a9c8-a796d620d147 | -3.967 | -48.15 | 2024-11-10 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| eb21b7e0-4acd-30eb-b453-920d4c596a4d | -3.2352 | -50.2855 | 2024-11-10 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 250.3 |
| 15e15cff-03ed-3c53-a1be-250fafde85ca | -8.3967 | -44.1365 | 2024-11-10 01:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 718ad4bc-8f47-3cfc-885c-44e6f8a4a3a6 | -3.1096 | -49.4029 | 2024-11-10 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 4c559fc1-2e94-3f34-8fd4-f0428c42e3be | -3.9671 | -48.1283 | 2024-11-10 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| f35c56d1-f818-39a5-bb09-6e07d10e3cf5 | -3.5064 | -44.0294 | 2024-11-10 01:30:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 5d73c93e-3dfa-3d8d-b0f2-7a52eea39536 | -4.8471 | -46.9728 | 2024-11-10 01:30:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 228.0 |
| b80deb12-9fde-3fae-9477-6882307918a6 | -3.2353 | -50.2645 | 2024-11-10 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 115.4 |
| a9dd09d1-1f22-38c1-8f13-c91ebad6aef9 | -1.5347 | -52.2104 | 2024-11-10 01:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 205.8 |
| 30f20c65-a107-3f03-96e9-5c9587b591b3 | -2.4367 | -51.948 | 2024-11-10 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 8b2d1ac3-a7e9-3b8a-bb63-9046eb0ac408 | -2.7587 | -49.3497 | 2024-11-10 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| f5da91e9-affb-3807-9b72-90f42acc1657 | -3.1091 | -45.2968 | 2024-11-10 01:30:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 8ce08712-5d9a-3af9-8a93-80037c1da2c5 | -3.2948 | -45.3346 | 2024-11-10 01:30:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 597cde03-68c2-3208-8359-b14dd378b022 | -3.0213 | -53.2607 | 2024-11-10 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 8aaa089d-dcf8-32bd-8e0e-2eda1f7513ba | -1.5163 | -52.1901 | 2024-11-10 01:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 90795b86-200e-3813-86a2-35be63d6570e | -5.0533 | -44.2883 | 2024-11-10 01:30:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 009a6253-2956-3479-b0e3-a6cf1a667f59 | -17.627 | -57.5075 | 2024-11-10 01:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 402.9 |
| 945660ff-a102-3fb8-b036-6c2eba01f82e | -2.7586 | -49.371 | 2024-11-10 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 15eb2ea3-2bd9-3f63-99bd-734ebff0b2b1 | -17.6066 | -57.551 | 2024-11-10 01:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.5 |
| 614dd151-eea6-3009-9dfc-59acad51cff2 | -17.6273 | -57.487 | 2024-11-10 01:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.4 |
| c6090a1b-9ec8-3df3-b9b7-04122d8e7f14 | -2.2076 | -48.3596 | 2024-11-10 01:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| b6d35ed9-6b18-36d9-9141-c0ac640b5128 | -3.1095 | -49.4241 | 2024-11-10 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 0d897ee2-67c7-3ae9-a560-0db51574a772 | -1.5347 | -52.1899 | 2024-11-10 01:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| c508b517-6959-3d4c-a9b9-b3cc161efa22 | -3.9668 | -48.1932 | 2024-11-10 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| ff3e04fc-e257-39d5-92ab-fcf1a8bb5099 | -2.8857 | -45.3726 | 2024-11-10 01:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 792a5beb-f4fd-3b0c-9b45-f62fafec3a40 | -3.2244 | -53.0524 | 2024-11-10 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| d59b2bae-3b36-34e3-a321-38649194e345 | -5.0535 | -44.2654 | 2024-11-10 01:30:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| e2722d88-4228-3e6b-9390-bd5a9ab8b35e | -2.4183 | -51.9484 | 2024-11-10 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| f3e9b0c2-98b9-39f2-b71c-a351345e899f | -4.8655 | -46.9938 | 2024-11-10 01:30:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 8a8a3cc2-41dd-30b8-a821-936df13e7592 | -2.9171 | -51.4825 | 2024-11-10 01:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 4cf8d9fb-5df2-3bb0-b306-a7988896ba64 | -3.525 | -44.0286 | 2024-11-10 01:30:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| f80a62ea-f9cd-3fe2-af1e-1458fb00a84b | -2.7772 | -49.3492 | 2024-11-10 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| ca8dab1b-df96-3af6-86cb-158ea2947da7 | -17.2933 | -57.4857 | 2024-11-10 01:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 182.6 |
| ef0bb46b-7254-3f33-a80c-14618a6832d4 | -2.8803 | -51.4628 | 2024-11-10 01:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 42419fb3-c4e1-3b0d-ab0b-b7eb9f4e819c | -3.3117 | -45.6706 | 2024-11-10 01:40:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 68eca4bc-98bc-3c71-82ad-3685cdae8f06 | -3.6004 | -47.3395 | 2024-11-10 01:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 153.3 |
| 0aa1fdfe-336d-30b2-80b6-1fa404bfe2bc | -1.5347 | -52.1899 | 2024-11-10 01:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| b688ce55-3c5f-3d28-8fa1-95851fe16dd7 | -3.0213 | -53.2607 | 2024-11-10 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 6321a07d-b913-3c38-a3df-7c6016120878 | -4.8657 | -46.9718 | 2024-11-10 01:40:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 3374c6ec-4871-3373-9bf8-8ad1429fc640 | -5.0533 | -44.2883 | 2024-11-10 01:40:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| be663f1e-3067-3c7e-814f-49d9b0f28559 | -3.1095 | -49.4241 | 2024-11-10 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 61e7f5c2-05b7-30c7-bb8e-a90a7708baff | -2.8857 | -45.3726 | 2024-11-10 01:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 022886ef-6e55-366d-85e6-80fee66848d4 | -2.7586 | -49.371 | 2024-11-10 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 002f9c49-3517-3b22-98d0-1fa47e66d598 | -3.5819 | -47.3403 | 2024-11-10 01:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| accde017-65e4-35de-b7bc-ca88817e9bd8 | -3.4383 | -50.2999 | 2024-11-10 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 2104db59-cdec-3320-986a-83357c137bb3 | -11.0877 | -43.3456 | 2024-11-10 01:40:00 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 0ad82a6e-634b-3372-aadb-f0b70e3a4e98 | -3.2244 | -53.0524 | 2024-11-10 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 0054836c-7b78-3a67-9d9c-fa4dc9013442 | -2.5513 | -45.3837 | 2024-11-10 01:40:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 46b6cf7a-5d77-31f2-90ab-fbed5c4bed75 | -1.5163 | -52.2106 | 2024-11-10 01:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 8ee79c15-74ed-33a1-8f9a-d76aea1df69a | -4.8469 | -46.9948 | 2024-11-10 01:40:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 52.6 |
| d64ba35a-5916-314d-bbcb-ad5996b9e65b | -2.7771 | -49.3704 | 2024-11-10 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| b68e9869-2dc1-39bb-aeac-4ecd165e4a5c | -2.8802 | -51.4835 | 2024-11-10 01:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 2f284ab1-3553-3065-a868-8b802ee0b0fa | -2.9171 | -51.4825 | 2024-11-10 01:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| e6bdd764-3b19-3120-8ad8-3375b162dfc5 | -2.4367 | -51.948 | 2024-11-10 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| f0e829d0-437b-3761-8641-3233d13aadb3 | -2.418 | -46.3024 | 2024-11-10 01:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 95463f0f-2689-3f41-a4dc-1e8186134450 | -3.619 | -47.3388 | 2024-11-10 01:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| ed5eceff-f19d-3732-989e-26bc99948350 | -5.0535 | -44.2654 | 2024-11-10 01:40:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 9c33e1c8-078e-3c82-9a6e-7095a59bb3a6 | -3.5064 | -44.0294 | 2024-11-10 01:40:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 8b8246b8-9ed4-3a5e-9072-75b589a24d73 | -3.9624 | -49.0096 | 2024-11-10 01:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| af1a8622-a66d-3d63-9c79-b58ac7da41fa | -3.6003 | -47.3614 | 2024-11-10 01:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 4a26b47e-062f-3eb2-978f-fd13ab60892a | -3.2428 | -53.0519 | 2024-11-10 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| b9e562c0-1a11-3952-9909-55442b658a1f | -3.1422 | -50.4562 | 2024-11-10 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| f8ba1b7c-0e61-36de-84db-1e1e8121a813 | -4.8471 | -46.9728 | 2024-11-10 01:40:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 82.4 |
| b1685acd-b18f-3723-a683-d12d1172bb6d | -2.0954 | -48.8125 | 2024-11-10 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 584f2bc1-0c9c-30d8-9a59-31cb6ce02e96 | -8.3967 | -44.1365 | 2024-11-10 01:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 108.4 |
| f304b4d9-744d-3d6e-a61e-cec98564365a | -2.2076 | -48.3596 | 2024-11-10 01:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 7b7c9fb2-e9f3-3cb4-a30e-f6b7e6d6fbea | -3.1239 | -50.4358 | 2024-11-10 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 2fa4f374-cc2b-3a1b-bf18-90001ad710a9 | -2.7587 | -49.3497 | 2024-11-10 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| c9ab61dd-afa8-38ea-8663-92c04b30ff43 | 2.8552 | -60.0853 | 2024-11-10 01:40:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 27.9 |
| d5792fcf-0e96-31bf-a137-b8bc1566d5e1 | -3.525 | -44.0286 | 2024-11-10 01:40:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 35083460-c6a9-382d-a191-0800ac548bf1 | -2.8858 | -45.3501 | 2024-11-10 01:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 89d8e4d4-3968-3639-a769-3b86ae1d42b9 | -2.2075 | -48.3811 | 2024-11-10 01:40:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 12fa37ac-f1ca-33e2-9e75-d2e55d9411bb | -2.4183 | -51.9484 | 2024-11-10 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| d5e41d4c-fbc4-39f3-ba86-da7f9e213b26 | -2.0953 | -48.8338 | 2024-11-10 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 193.8 |
| c2df4004-e06b-359b-a5c0-078c05fba862 | -2.2095 | -47.733 | 2024-11-10 01:40:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 29dc9663-3559-3536-b462-a3ef574f263c | -2.9355 | -51.482 | 2024-11-10 01:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| b8bf9ee9-8e2e-3b8a-b48b-a5bd69e71421 | -1.5347 | -52.2104 | 2024-11-10 01:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 207.5 |
| 3d9bec98-c172-3b6e-834d-3e61db6866bb | -3.5818 | -47.3621 | 2024-11-10 01:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 222b18a2-9156-3d87-8cf1-7f0e30a7e0b8 | -2.4366 | -51.9685 | 2024-11-10 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| d5449bf0-3e3a-365c-ab82-fcf6dbcea90f | -3.1096 | -49.4029 | 2024-11-10 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 8699c0d6-269d-39f6-8274-82c8e8c20db9 | -3.2427 | -53.0722 | 2024-11-10 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| be755349-3a8c-397c-9226-d14172ce714e | -17.293 | -57.5062 | 2024-11-10 01:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.8 |
| b9bdab5b-0e54-329e-b9f6-51c7d42906b8 | -3.1238 | -50.4568 | 2024-11-10 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |


[Clique aqui para ver as próximas entradas](README17.md)
