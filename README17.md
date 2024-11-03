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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0bc9ef34-bddf-30f1-a8f8-3520b841df14 | 2.5498 | -51.0981 | 2024-11-03 02:04:51 | GOES-16 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 38.3 |
| f4eb6534-1b2b-3677-8072-49bdcdd689ad | -1.2755 | -53.3936 | 2024-11-03 02:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| d5296b24-afec-37ea-a15f-4741cfac395a | -1.2572 | -53.3938 | 2024-11-03 02:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| e24559d3-cb7f-33e0-a162-e99bd071f7a8 | -1.2756 | -53.3734 | 2024-11-03 02:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| eb2be5a3-4a4f-34c5-8c78-9dbd6e037560 | -1.2755 | -53.4138 | 2024-11-03 02:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| f369ee99-4a1c-3d95-84d2-b402b65f961f | -2.1746 | -53.6834 | 2024-11-03 02:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 24d2af8a-9aa5-3b7b-b8d2-23a3030a2f2e | -2.2802 | -48.8082 | 2024-11-03 02:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| c8749d99-9a02-301d-b980-18ef084c262b | -2.2986 | -48.8078 | 2024-11-03 02:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| e442b530-e889-3079-9f54-94149d028044 | -2.5796 | -53.3927 | 2024-11-03 02:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| b09e1dd8-0d9e-3381-8392-8e78ee6eabc1 | -2.5797 | -53.3724 | 2024-11-03 02:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| d2fecaa2-5c71-37c8-af17-5a555995776e | -2.6506 | -48.5844 | 2024-11-03 02:05:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| d9ed00f9-7e5a-3d36-9e4f-0806f6adb4e0 | -2.6507 | -48.5629 | 2024-11-03 02:05:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| fa768234-e46b-39e5-b2cc-ed76cc6bff67 | -2.7033 | -49.33 | 2024-11-03 02:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 2a8a5221-1f28-35c9-a7a5-9309962a50bb | -2.7218 | -49.3295 | 2024-11-03 02:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 26ae61f0-e48e-36f1-8895-7334b1eadb16 | -2.7419 | -54.4153 | 2024-11-03 02:05:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 5b0b6633-6762-3618-8411-734e6ba3964b | -2.7602 | -54.4349 | 2024-11-03 02:05:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 25fe08fb-c647-33e7-b514-b5e1f962bee0 | -2.7603 | -54.4149 | 2024-11-03 02:05:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| e90a8956-f758-366d-ae13-9d346bda1ac4 | -2.7876 | -51.6099 | 2024-11-03 02:05:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 99e6669e-ca4c-3377-9268-a7603407a35f | -2.8245 | -57.7031 | 2024-11-03 02:05:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 9518acae-3517-39e8-8097-4b2adc9a54fd | -2.7419 | -54.4353 | 2024-11-03 02:05:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 9aabb239-34aa-3e6c-8a59-d229c8327811 | -3.055 | -54.1675 | 2024-11-03 02:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| cb026a39-4fe1-3e16-8350-bfb97d65701e | -3.055 | -54.1474 | 2024-11-03 02:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 5f9ace94-0887-328e-99a0-fae7a8f1652d | -3.0734 | -54.167 | 2024-11-03 02:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| fcf1ff78-08c7-335e-bd3a-4a97b16bc774 | -3.0734 | -54.147 | 2024-11-03 02:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 126.1 |
| f04f2953-1e3e-3606-987b-71e0dbdb9616 | -3.0875 | -50.2901 | 2024-11-03 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| c5e1d843-5853-3ccc-b270-045d983d91aa | -3.1059 | -50.3105 | 2024-11-03 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 837474a5-b8e5-328d-bca9-c984fa6caa8c | -3.2168 | -50.2861 | 2024-11-03 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 8fe85f05-d9f8-38af-89d8-fe71064c7027 | -3.1245 | -50.289 | 2024-11-03 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 7039c69e-6ba1-3882-a3c6-8ea91acf2a42 | -3.106 | -50.2896 | 2024-11-03 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 165.7 |
| e571e7a5-ae03-3cfe-b11a-2001d5197348 | -3.1061 | -50.2686 | 2024-11-03 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 14f96660-51ea-37be-9f54-3bc0811b030b | -3.2415 | -53.3967 | 2024-11-03 02:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 135514a3-af3e-3c21-8fec-2aad7181948a | -3.6092 | -49.3219 | 2024-11-03 02:05:26 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 7f09688f-c25f-351a-9151-7f7e771aab8a | -3.4749 | -50.3826 | 2024-11-03 02:05:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 730afa81-f711-3bd2-99cb-db95b74fc9df | -3.475 | -50.3616 | 2024-11-03 02:05:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 4b0c6727-3c63-351d-be2f-4fe73a5631db | -3.967 | -48.15 | 2024-11-03 02:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 72201774-dce6-3b3b-8e29-00b284d69a87 | -3.9474 | -48.3451 | 2024-11-03 02:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| feb66656-b71f-3f30-bbf7-4bbcfb000c8d | -3.9473 | -48.3666 | 2024-11-03 02:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 7e6a469a-bd6b-3549-a44b-08305de46e07 | -4.4054 | -43.4746 | 2024-11-03 02:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| c927b2e0-b03d-3a06-85df-3a7ec0a043e9 | -4.4056 | -43.4514 | 2024-11-03 02:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| ef43e416-5114-3e95-838b-ecfbcdd65f15 | -4.4241 | -43.4735 | 2024-11-03 02:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| ef1fe21a-378b-3807-856c-c59db4ed6348 | -4.4243 | -43.4503 | 2024-11-03 02:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| dd2d2e15-9381-386c-b2f3-fd778ec82b57 | -5.3507 | -46.8331 | 2024-11-03 02:05:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 1b9afc98-e836-30c8-b81e-53616d3ada0a | -5.3321 | -46.8343 | 2024-11-03 02:05:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 87a36167-8989-3f3f-8665-8be587f4c811 | -6.5239 | -41.4929 | 2024-11-03 02:05:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| b7907dc3-34c0-3e52-afa1-a6243ee4dea0 | -1.2572 | -53.3938 | 2024-11-03 02:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 3f959816-12e2-349d-b73f-ff1f1817fe15 | -1.2755 | -53.4138 | 2024-11-03 02:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 3174ac0d-27ba-34e1-99c3-c390c454ac24 | -1.2756 | -53.3734 | 2024-11-03 02:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| f4cd865b-6ff1-3bd8-aeaf-204d614d368e | -1.2755 | -53.3936 | 2024-11-03 02:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 140.7 |
| d31b27c9-5c83-383f-87c7-613a34aa6594 | -2.1746 | -53.6834 | 2024-11-03 02:15:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| e88d213d-6820-3e28-8133-ac5b51773ea3 | -2.2986 | -48.8078 | 2024-11-03 02:15:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 72be5466-5dbd-3bd9-ad8d-35d90b78aa04 | -2.2802 | -48.8082 | 2024-11-03 02:15:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 03a68098-cec4-3759-896c-8e66b102e5a9 | -2.5796 | -53.3927 | 2024-11-03 02:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 0f9eaf6d-1103-3a4a-a3a6-88a4bf63409a | -2.5797 | -53.3724 | 2024-11-03 02:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 242aeb63-702f-35a6-8aff-d80c00400e25 | -2.6321 | -48.5849 | 2024-11-03 02:15:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| cf206e92-c432-3856-ae64-e67dc33d6412 | -2.6506 | -48.5844 | 2024-11-03 02:15:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| a0c5792f-c65b-3734-972a-def6a99de6f8 | -2.6507 | -48.5629 | 2024-11-03 02:15:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 4764246e-35c9-3136-8e46-5d21798ff52c | -2.7218 | -49.3295 | 2024-11-03 02:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 7fde0b5c-394c-396e-89bd-17501deb5261 | -2.7876 | -51.6099 | 2024-11-03 02:15:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 95e1b238-d86f-349f-9a75-9e69e3da17e4 | -2.8148 | -49.1567 | 2024-11-03 02:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| de2b02ca-c71c-3112-808f-e2d960b4b30c | -2.8245 | -57.7031 | 2024-11-03 02:15:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 12297d45-8923-3673-bcdc-52a19cff2f52 | -2.7419 | -54.4353 | 2024-11-03 02:15:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 163.5 |
| 6a7972cb-8bab-3673-ac6c-7089fcbfb93c | -2.7419 | -54.4153 | 2024-11-03 02:15:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 27e4ddac-f2e3-30f5-8ef7-24691ba2f32d | -2.7602 | -54.4349 | 2024-11-03 02:15:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 3c4c9e5c-fa37-32be-8894-80fc89782c92 | -2.7603 | -54.4149 | 2024-11-03 02:15:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 0d8c1a89-2d8d-362f-a371-49364d522550 | -3.055 | -54.1474 | 2024-11-03 02:15:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 4774eadc-f1ef-38f2-a17d-22736e2c29d8 | -3.0734 | -54.167 | 2024-11-03 02:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| c7b8531b-2e7b-3d7d-bc47-4e2fe74490e9 | -3.0734 | -54.147 | 2024-11-03 02:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 0779f89c-7503-39de-900f-2ddf21952417 | -3.0875 | -50.2901 | 2024-11-03 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 056ac3f4-c88b-39fa-8ffb-940c08cb6581 | -3.1059 | -50.3105 | 2024-11-03 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 30f04196-6df5-3912-a45f-33c06b7c069c | -3.106 | -50.2896 | 2024-11-03 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 163.2 |
| 0c97bdbe-ddaf-3574-b310-596626090d83 | -3.1061 | -50.2686 | 2024-11-03 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 09995935-a268-3a7e-96db-aa0c39c57e61 | -3.1213 | -51.1036 | 2024-11-03 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| bbaf9bd8-4f60-3ecb-afcc-f3f6b6eee9c6 | -3.1245 | -50.289 | 2024-11-03 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 98507e2f-560e-3a2c-aca1-f79b0fa82e68 | -3.2415 | -53.3967 | 2024-11-03 02:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| cead1a77-20d4-37db-bde1-dd38dfb57841 | -3.4749 | -50.3826 | 2024-11-03 02:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 6f67025d-5bd5-3434-9aa1-f03c51b8ad1f | -3.475 | -50.3616 | 2024-11-03 02:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 57343e73-9517-3f8d-ab43-36d0feadb463 | -3.6092 | -49.3219 | 2024-11-03 02:15:26 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| ddfe48f3-d718-3e0a-a5f6-42a2417f9751 | -3.9473 | -48.3666 | 2024-11-03 02:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 1dce5b26-d673-3319-9dda-fffce3b2eedd | -3.9474 | -48.3451 | 2024-11-03 02:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 52f713f5-4268-37ec-8553-86712b6883fc | -3.967 | -48.15 | 2024-11-03 02:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 2a221685-e0aa-36bc-bb55-ef18097c3105 | -4.4054 | -43.4746 | 2024-11-03 02:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| d652be76-8836-36a6-85c2-23f5424055ea | -4.4056 | -43.4514 | 2024-11-03 02:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 3e7313b8-42a8-3664-a636-d03f0713eda9 | -4.4241 | -43.4735 | 2024-11-03 02:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| fabb6258-8aed-395f-a96a-f2e5689d0edb | -4.4243 | -43.4503 | 2024-11-03 02:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 52f0e018-832c-3893-9d0f-70aab601cf84 | -6.5239 | -41.4929 | 2024-11-03 02:15:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 74.8 |
| d4ff3df2-b032-394c-a7e1-8eb9ecec9c12 | -6.5241 | -41.4688 | 2024-11-03 02:15:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 64.1 |
| 07b2b8fa-8c3b-3ebd-8f28-7c1780e8f5cf | -1.2756 | -53.3734 | 2024-11-03 02:25:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| d028a85d-3182-3818-ae74-1c11f114062c | -1.2755 | -53.3936 | 2024-11-03 02:25:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 119.6 |
| a037ae54-8b33-3a3f-b9d0-b184673f32bf | -1.2755 | -53.4138 | 2024-11-03 02:25:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| ccbf381f-2fc9-3ca1-8c1a-3b5054597d07 | -2.1746 | -53.6834 | 2024-11-03 02:25:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| b85b97e7-9095-3c1f-910b-b757f2db7562 | -2.2986 | -48.8078 | 2024-11-03 02:25:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 9139394e-8f25-3af0-b5c3-19576b9e516c | -2.2802 | -48.8082 | 2024-11-03 02:25:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 6b1d5efb-5f6a-3c4a-82a7-39266fdeaee8 | -2.5796 | -53.3927 | 2024-11-03 02:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| d16382e3-3b8a-3e76-bfa0-0f0c2a246e84 | -2.5696 | -57.1242 | 2024-11-03 02:25:21 | GOES-16 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 38.2 |
| c5394688-77cc-3e25-9789-812af9ceb3f0 | -2.6507 | -48.5629 | 2024-11-03 02:25:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| a7341423-32da-3b5b-ade4-cab3c101421e | -2.6506 | -48.5844 | 2024-11-03 02:25:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| fd2ae797-f2a2-3609-8749-91da4c434237 | -2.6322 | -48.5634 | 2024-11-03 02:25:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 3b4909fd-f3fb-37e4-89d1-0043fe83abc9 | -2.6321 | -48.5849 | 2024-11-03 02:25:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 3b867a36-17a7-380e-a61d-8d606f83124f | -2.5797 | -53.3724 | 2024-11-03 02:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| a150f917-6b0c-3f4e-b97c-30a4fa1f7d35 | -2.7218 | -49.3295 | 2024-11-03 02:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |


[Clique aqui para ver as próximas entradas](README18.md)
