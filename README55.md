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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72d55208-294a-330e-89c5-8861fce2695d | -1.80905 | -52.16711 | 2024-11-14 05:35:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 82bf3817-70d3-3119-be70-d8ccffe27dd2 | -1.40225 | -51.13497 | 2024-11-14 05:35:00 | AQUA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a0ef4bef-d7d3-3f50-9fac-e978009582cf | -2.67057 | -46.98252 | 2024-11-14 05:35:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f634831c-e296-3974-b0ee-a6d72ba0285c | -2.37731 | -48.5229 | 2024-11-14 05:35:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f59422d3-6d02-3f65-b3c1-60f26e92e9b2 | -2.9017 | -46.859 | 2024-11-14 05:35:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 0131d935-774a-36f2-adf6-818087afc996 | -2.64561 | -46.16408 | 2024-11-14 05:35:00 | AQUA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 23ffa343-525b-33b3-a0a1-a03254ddcfea | -2.40923 | -45.34293 | 2024-11-14 05:35:00 | AQUA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 77e1a852-eaa6-3e0c-a81f-3f98d6df1ca8 | -3.2594 | -45.1344 | 2024-11-14 05:35:00 | AQUA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 0e9e8d61-94da-3212-8d91-1acd79c3a682 | -2.66699 | -46.81301 | 2024-11-14 05:35:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1fdc8e98-3b6c-3ee7-a512-3c89554ce539 | -2.82199 | -46.64851 | 2024-11-14 05:35:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fd20426e-c93c-35d4-befd-6769f27e5322 | -2.6346 | -49.51905 | 2024-11-14 05:35:00 | AQUA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 5f490f99-13af-330c-92a9-5c370fdd68d4 | -2.36714 | -48.84197 | 2024-11-14 05:35:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 94bf1fc9-99d3-3c9a-83c8-093e10e28ed8 | -1.55768 | -51.86022 | 2024-11-14 05:35:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| fca25daf-1305-34f9-85e1-4fd054007ff4 | -2.68357 | -49.25461 | 2024-11-14 05:35:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 34f61760-a1b0-380d-9b7d-535496e74469 | -2.92524 | -48.06389 | 2024-11-14 05:35:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7087172c-7a4c-3507-87ee-634fd40a05b5 | -2.73272 | -49.28885 | 2024-11-14 05:35:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 19845127-fa11-3dba-bbcb-91b58e80b090 | -3.20229 | -44.42355 | 2024-11-14 05:35:00 | AQUA_M-M | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| af68b672-cedc-3ec7-b70e-64fa5dd6e88d | -2.15104 | -48.80047 | 2024-11-14 05:35:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d541fd04-26fc-3580-b014-5f3c1458a11f | -0.20755 | -51.50373 | 2024-11-14 05:35:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 90951aac-1782-3526-8924-61d8f472729b | -1.40384 | -51.12453 | 2024-11-14 05:35:00 | AQUA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| b9858c14-eb15-3554-b574-09a4a142bdd5 | -3.20282 | -44.43046 | 2024-11-14 05:35:00 | AQUA_M-M | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 01715fae-5eda-329b-8e23-c801f45e1cf3 | -2.08984 | -47.73075 | 2024-11-14 05:35:00 | AQUA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 79e5102d-3dd9-3932-af52-72a4457a39f8 | -1.55944 | -51.8487 | 2024-11-14 05:35:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 451d2d96-43ba-3f33-9279-7edaedbdbff4 | -2.42586 | -46.26988 | 2024-11-14 05:35:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a3daf2b1-cf18-3327-a363-2a75b520d060 | -2.64403 | -46.17466 | 2024-11-14 05:35:00 | AQUA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| bd7f4eeb-c54c-38c2-acd4-e9bba97bbe30 | -2.66915 | -46.99214 | 2024-11-14 05:35:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 98bf2e48-34c9-3726-925a-53f69d99b47a | -3.95318 | -46.41125 | 2024-11-14 05:37:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f973dc12-6f02-3ec3-8cc6-46e268648d75 | -3.46665 | -50.30379 | 2024-11-14 05:37:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 84ac715e-ab3d-356c-a901-6d3817b0f373 | -4.0568 | -47.22451 | 2024-11-14 05:37:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b0d199e0-081f-38ba-abc8-8bc729021191 | -3.49788 | -50.83375 | 2024-11-14 05:37:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 91189026-8acf-3a89-9e7d-19a1bbbe2a79 | -3.41129 | -50.30795 | 2024-11-14 05:37:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 4a88bbd0-4039-3747-bf26-1ee7ddaab159 | -4.40028 | -47.2692 | 2024-11-14 05:37:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e40b2ac2-cd5c-3826-8206-b56be90763bd | -3.27718 | -51.26287 | 2024-11-14 05:37:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 80ea4b1e-aa15-3f6c-b213-0a7121d41271 | -4.55872 | -48.00497 | 2024-11-14 05:37:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c07aa353-122e-32b2-9e9b-1cb06538b3ab | -3.75003 | -50.44905 | 2024-11-14 05:37:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3a476afb-f50d-35e4-a289-ce316482f475 | -5.9194 | -42.96907 | 2024-11-14 05:37:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 189851f1-3482-3851-a92c-f6019580059e | -3.41267 | -50.29875 | 2024-11-14 05:37:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2f802347-3e18-365c-ba15-42e928f6748e | -3.40225 | -50.30662 | 2024-11-14 05:37:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 6999f9f5-e0ef-3f04-92fa-6deab9de6d32 | -4.94131 | -44.96131 | 2024-11-14 05:37:00 | AQUA_M-M | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| fede7b18-9dcd-37da-a7bf-ea43860db27e | -5.07357 | -45.5089 | 2024-11-14 05:37:00 | AQUA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d810688f-bdf1-37f7-bd12-4e75595097db | -4.52324 | -48.93015 | 2024-11-14 05:37:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ec9d00d2-1ad0-38af-a3c3-a8b124c3417c | -3.74238 | -50.4384 | 2024-11-14 05:37:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b522f08b-e017-3f4d-a4f4-1cf549397897 | -3.636 | -50.58858 | 2024-11-14 05:37:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 4c1d4e0f-8f22-3a4c-9e2d-47748a7fa041 | -3.49642 | -50.84338 | 2024-11-14 05:37:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3f82197e-6fc9-30d1-bb96-df3a1334b4fa | -3.64511 | -50.58995 | 2024-11-14 05:37:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9d1d82e4-8faf-3a96-a612-d01987bb0f3a | -4.94331 | -44.94746 | 2024-11-14 05:37:00 | AQUA_M-M | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| aebcb3b1-38aa-3877-811a-b7fc60e94add | -4.21063 | -50.69745 | 2024-11-14 05:37:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bbfacea5-17ae-34b7-a223-36bef6678536 | -4.15188 | -46.24215 | 2024-11-14 05:37:00 | AQUA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8aede593-ec97-3de6-93b2-f4d41a85fef7 | -4.59514 | -47.06746 | 2024-11-14 05:37:00 | AQUA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1eb83b67-9743-3613-9189-51b8d2caf794 | -3.71554 | -50.6158 | 2024-11-14 05:37:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f1934fde-6ffa-3614-a0f9-5ba3bd1ebc9e | -3.81389 | -47.80059 | 2024-11-14 05:37:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5a410fc2-1002-3da3-bdc0-7fa81645fed4 | -3.96923 | -46.70129 | 2024-11-14 05:37:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 968fdaed-bed1-3879-8780-29fa1beaf16c | -3.71695 | -50.60645 | 2024-11-14 05:37:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 6c6607ea-0497-3f67-83b0-c85cd3f04208 | -17.71266 | -57.52345 | 2024-11-14 05:40:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.8 |
| 18c2ddab-fc88-3d77-ab40-98b7f9e32510 | -17.23999 | -57.46226 | 2024-11-14 05:40:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.1 |
| af09a8fc-bda5-3e64-adea-69a11f878d92 | -17.2464 | -57.47062 | 2024-11-14 05:40:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.5 |
| b521f478-ed27-311b-853f-391db893ae2b | -17.58487 | -57.53677 | 2024-11-14 05:40:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.9 |
| 854f5162-586d-3999-a48b-417b8a872001 | -17.70973 | -57.53973 | 2024-11-14 05:40:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.3 |
| fba7a7bb-2528-3fcd-bd9c-f3b946602542 | -17.24936 | -57.45424 | 2024-11-14 05:40:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.3 |
| 0c30673a-c41f-3bd7-a627-795609eafbba | -17.62896 | -57.53532 | 2024-11-14 05:40:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 62a81e09-17d6-30a6-a343-cc536f6a4401 | -17.57333 | -57.53454 | 2024-11-14 05:40:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 38.8 |
| 0d67cbbc-aef4-3743-bd25-94a35fc24545 | -17.60618 | -57.46365 | 2024-11-14 05:40:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 5e50a9e4-ceb8-30ee-bf8f-50eb1605e7b3 | -16.9518 | -57.63665 | 2024-11-14 05:40:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| f0b75ecd-2ef2-3525-9591-586e2de454c0 | -17.62603 | -57.55169 | 2024-11-14 05:40:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 47f005bb-3da2-3e86-8005-7ed5a853929f | -17.59344 | -57.48778 | 2024-11-14 05:40:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.8 |
| 122841e1-6de9-3d17-a348-3e00a3cb9dfb | -17.59628 | -57.47153 | 2024-11-14 05:40:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.8 |
| 6c43cd4b-03dd-3073-a29c-b50415f3d51a | -4.5616 | -47.9925 | 2024-11-14 06:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| cc511f59-9347-3cbe-b095-462bc6bfd906 | -4.5614 | -48.0141 | 2024-11-14 06:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| f085a0dd-bc0a-3e9b-80a7-060301830dcc | -4.5614 | -48.0141 | 2024-11-14 06:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 77b3e7ed-928e-37b0-9ea0-9cd6f36602e0 | -3.714 | -50.6046 | 2024-11-14 06:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| f3ca1e41-1a22-3c0d-90da-68d7ac640fe1 | -4.5616 | -47.9925 | 2024-11-14 06:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 81857643-593f-32d3-87a7-45be33a7a2ea | -4.5614 | -48.0141 | 2024-11-14 06:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 525b5490-37bd-38d6-96ec-431efde35675 | -4.5614 | -48.0141 | 2024-11-14 06:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| fc7f45ba-3bf6-3a85-bab4-fe9e4d11f07e | -3.332 | -45.333 | 2024-11-14 07:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 3a03c689-a026-34e3-a6b0-a9d4301dd125 | -3.3878 | -45.3307 | 2024-11-14 07:00:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 514048cc-8c4a-3a09-b7ce-090b34202e0a | -3.3878 | -45.3307 | 2024-11-14 07:10:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 2ea95b4b-43cd-3b8c-bc1e-3d36abe7f622 | -3.3506 | -45.3323 | 2024-11-14 07:10:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 403a0275-2230-3dc5-9d1d-0b2a9c194cad | -3.3877 | -45.3532 | 2024-11-14 07:10:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 50.5 |
| adb3f707-0c3a-32c0-b7ec-b76e4626199a | -3.332 | -45.333 | 2024-11-14 07:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 3e5d9050-6bf0-34e6-990a-6e7b5872b55d | -3.4064 | -45.33 | 2024-11-14 07:10:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 39.7 |
| dcc73796-3377-368f-a383-6db0cadc8f02 | -3.332 | -45.333 | 2024-11-14 07:20:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 64.1 |
| edf0bd8c-5dbc-3ae6-a15c-548715d86f7d | -1.643 | -53.2677 | 2024-11-14 07:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 9b1b0bf5-664c-34f6-89de-ade4faaa8207 | -3.3506 | -45.3323 | 2024-11-14 07:20:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 848a4723-81eb-3f0e-b01c-7a2c68f97ed6 | -3.3319 | -45.3555 | 2024-11-14 07:20:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 81d75a62-92b4-3ae0-aa58-d464b0d93614 | -3.3319 | -45.3555 | 2024-11-14 07:30:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 8f01fbae-70f8-3594-8182-657bc9ef1f63 | -3.3321 | -45.3105 | 2024-11-14 07:30:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 5b7ef127-9c85-31a2-8ac8-da7263177800 | -3.3507 | -45.3098 | 2024-11-14 07:30:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 40.9 |
| f07049d5-3e39-39c0-9d93-927ad228c0fe | -3.3505 | -45.3548 | 2024-11-14 07:30:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 6441ccc5-563e-3496-abc1-fb4ad96b93cb | -3.332 | -45.333 | 2024-11-14 07:30:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 176.4 |
| e89bf115-b033-3d4e-987a-856155d6da5a | -3.3506 | -45.3323 | 2024-11-14 07:30:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 162.3 |
| e9847855-ef89-3248-81b7-6f9c2e989252 | -17.5869 | -57.5533 | 2024-11-14 07:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.9 |
| e218fe90-5c51-332f-b68b-c7a019362fbe | -17.5869 | -57.5533 | 2024-11-14 08:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.2 |
| a4cea2d1-8c02-3c28-bbf2-945fda5ec7f2 | -17.5869 | -57.5533 | 2024-11-14 08:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.2 |
| 7840c8c0-a9ed-3e8d-adba-5a85d6f27625 | -17.5869 | -57.5533 | 2024-11-14 08:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.0 |
| 9ab7f9d7-6169-3e5c-89fb-fecf3a8fcef4 | -8.13897 | -38.27553 | 2024-11-14 11:27:00 | TERRA_M-M | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 57.4 |
| fbfc6841-11bc-34ef-83e4-b4f3bfc71036 | -8.14404 | -38.28426 | 2024-11-14 11:27:00 | TERRA_M-M | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 63.5 |
| cb482d67-86dd-3b75-bd6f-a362632ce545 | -9.60969 | -38.38681 | 2024-11-14 11:27:00 | TERRA_M-M | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 79.1 |
| 22fa64e0-c2ea-3eff-a673-46abcbc91a72 | -9.60359 | -38.42112 | 2024-11-14 11:27:00 | TERRA_M-M | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 52.3 |
| caf6b08e-1003-355e-85f7-a8a3bd4afec3 | -9.61358 | -38.41544 | 2024-11-14 11:27:00 | TERRA_M-M | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 89.9 |
| bec755fc-27fc-367a-b88d-50a930a15552 | -9.61944 | -38.38099 | 2024-11-14 11:27:00 | TERRA_M-M | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 64.9 |


[Clique aqui para ver as próximas entradas](README56.md)
