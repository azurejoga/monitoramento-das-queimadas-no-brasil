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
| e28e6a25-66d3-30ff-8450-a2f5aeb89d4c | -2.87449 | -51.47382 | 2025-11-12 05:22:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ea4c7237-8500-3479-9da9-7ed859f85af7 | -4.10928 | -48.02211 | 2025-11-12 05:22:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2ae2213-d69b-349f-b33f-9b439c236f23 | -3.84083 | -50.06086 | 2025-11-12 05:22:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9fd60f03-c81c-3707-b6b6-c478b687f74c | -1.75124 | -53.88079 | 2025-11-12 05:22:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2266a17-cbd6-3e91-a1b2-0b7e670e7302 | -2.0228 | -57.03566 | 2025-11-12 05:22:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75682441-e222-37e7-be38-4e50c57ede5d | -2.87452 | -51.47873 | 2025-11-12 05:22:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2dbaa603-93d8-3ce7-a36c-d50caacb2755 | -2.8686 | -51.48374 | 2025-11-12 05:22:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16b9fed1-981c-3e57-a3c5-a2e10eae5e87 | -2.48683 | -50.2622 | 2025-11-12 05:22:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 424b4833-90b0-30c3-86e6-59b02d13e909 | -2.49226 | -50.26305 | 2025-11-12 05:22:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d30cad0-f893-3faa-abc6-e34caf8676f5 | -4.43511 | -50.54822 | 2025-11-12 05:22:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2ebbfc1-3e6f-3946-912f-9453d6b73365 | -4.1139 | -47.99848 | 2025-11-12 05:22:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da3e4932-8369-3bf1-b64d-ea97d8976b50 | -4.10285 | -48.02123 | 2025-11-12 05:22:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7876151e-cb38-312f-b7d6-e5936091452c | -5.21763 | -60.05344 | 2025-11-12 05:22:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1bffc70-e87a-356b-acb9-909403792006 | -3.78137 | -52.22729 | 2025-11-12 05:22:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee996141-d8ad-3338-a8dc-166883d91519 | -4.11465 | -47.99307 | 2025-11-12 05:22:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5aef8123-54ea-3648-9bd9-33e353abbb51 | -2.86949 | -51.47793 | 2025-11-12 05:22:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e323b650-5606-3c37-9285-3b707ce36213 | -2.87406 | -51.47675 | 2025-11-12 05:22:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8dadde3a-b2a0-3f16-ba9f-4f826d658b3b | -3.84286 | -50.06098 | 2025-11-12 05:22:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7ba1318f-7e21-3d90-b203-09fcfad6876a | -2.46409 | -55.36791 | 2025-11-12 05:22:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24c87152-169e-344e-a75c-2884cf30b465 | -3.7667 | -51.80756 | 2025-11-12 05:22:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 138d1903-83fb-32a1-a0de-0ebe16c01867 | -2.63681 | -49.19865 | 2025-11-12 05:22:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1f53b40a-3d3b-33f3-a5b4-e5fc840fcd0c | -4.27822 | -50.54023 | 2025-11-12 05:22:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e716e1c2-e7ed-3291-9fa8-6cc8cb584729 | -2.64201 | -49.20377 | 2025-11-12 05:22:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc83b756-32a3-3cf2-b318-8aa579c418f8 | -2.86903 | -51.47594 | 2025-11-12 05:22:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b62c7a28-1be4-3aed-ace2-0c823fdaa603 | -2.63618 | -49.20279 | 2025-11-12 05:22:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1a3d3b31-9f05-3921-8b26-461b615b19bd | -3.49234 | -55.41809 | 2025-11-12 05:22:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 109ce7a7-d1e9-3833-b092-4ef3193e4917 | -2.64264 | -49.19963 | 2025-11-12 05:22:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed492942-1657-305e-aa53-18f496046f0d | -4.09806 | -48.00904 | 2025-11-12 05:22:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fd3e7a4-3ac6-337d-a367-7a7286f8af21 | -4.11094 | -48.01978 | 2025-11-12 05:22:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce5e0e3f-6e72-3743-bc1c-8b18f9b3ef74 | -2.48245 | -50.25443 | 2025-11-12 05:22:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5446e97b-cf87-3cb1-81aa-2d0e0759e767 | -2.87497 | -51.47581 | 2025-11-12 05:22:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6270145d-80de-33be-b6fe-9b963ebee6a2 | -3.77653 | -52.22654 | 2025-11-12 05:22:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b49882a5-8f5a-384c-95fe-f3f6ee428e3c | -2.8704 | -51.47208 | 2025-11-12 05:22:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a9ff9ba0-6d76-34fb-8e6e-d9de51611592 | -4.1116 | -48.00626 | 2025-11-12 05:22:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 909bd8f4-b7c9-3e4d-a473-7b3145141416 | -1.75293 | -53.87681 | 2025-11-12 05:22:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8d6e436-1df3-3b13-9c1d-d1b038749b9d | -11.84118 | -57.85054 | 2025-11-12 05:22:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c72f39d1-8334-3911-8a93-3292075e98f7 | -4.11317 | -48.00374 | 2025-11-12 05:22:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d51d5f8-9537-3dc3-a9fb-406830622ae1 | -4.10441 | -48.0105 | 2025-11-12 05:22:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d55bc44-314c-306c-84f6-74b480d9d9e2 | -1.75185 | -53.87693 | 2025-11-12 05:22:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9ab169c-4159-3a2c-85f5-a23e130ad3b1 | -2.63743 | -49.19452 | 2025-11-12 05:22:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1f55e51-9ea3-3947-a994-45e03b400dc6 | -4.27331 | -50.53556 | 2025-11-12 05:22:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ec55232-2080-324e-837b-22b32a9dd2ee | -4.10522 | -48.00494 | 2025-11-12 05:22:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4534df14-4160-3064-951f-369b7a9f0fe0 | -2.87363 | -51.47967 | 2025-11-12 05:22:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 29d11f58-b36f-3d5d-bd88-3a5a24e48337 | -3.84591 | -50.06552 | 2025-11-12 05:22:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c28890b2-c575-3a33-b28f-e498d1f5ff6b | -2.79407 | -51.36164 | 2025-11-12 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3d53c0d-09b6-3547-a303-8eb48f77b63e | -4.24223 | -50.05939 | 2025-11-12 05:22:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 872f3e0e-14cf-3435-a40e-a771f61bb467 | -2.78953 | -51.36528 | 2025-11-12 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 753ed339-c193-3374-b7b9-bb06d6e3a042 | -2.86491 | -51.47425 | 2025-11-12 05:22:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d2540323-60a1-3874-a589-65c36e0e73b5 | -2.8686 | -51.47888 | 2025-11-12 05:22:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 61502cd0-684e-34fc-97f1-5677e6093e4e | -3.03467 | -51.03391 | 2025-11-12 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6184c66-bcb0-3b45-9a98-d147e1728149 | -11.84493 | -57.85113 | 2025-11-12 05:22:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c9bb4719-c90d-32d6-b5f7-c473bbbf5d36 | -3.98218 | -47.29972 | 2025-11-12 05:22:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c5e15d08-bce8-3e06-bea5-62aaff4e86f5 | -2.86946 | -51.47301 | 2025-11-12 05:22:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8456fc15-c357-38f5-832b-51b6dd67cab6 | -4.75253 | -48.84279 | 2025-11-12 05:22:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc807099-cc35-38ae-a1f3-0c1cc7a7f061 | -3.49623 | -55.41867 | 2025-11-12 05:22:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6cecfa1d-a201-3d7c-a0e4-bed99b28ccf0 | -2.81148 | -51.34918 | 2025-11-12 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9b2005b-ad78-31ac-8a62-c2f07cb83388 | -2.48736 | -50.25871 | 2025-11-12 05:22:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11cf3ec3-ae8b-312a-963a-003475964a4e | -4.09722 | -48.01479 | 2025-11-12 05:22:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ebd679dc-df6f-3bce-8255-eca1f9386957 | -4.09642 | -48.02034 | 2025-11-12 05:22:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b5a307a7-5923-35a2-950a-60a3cbddf1e3 | -4.10362 | -48.01595 | 2025-11-12 05:22:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1134964b-c578-321e-887a-664c2adb58e7 | -2.78999 | -51.36234 | 2025-11-12 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7818be5c-72fc-3543-944d-871283e54910 | -2.63556 | -49.20692 | 2025-11-12 05:22:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 436269d2-59da-39e9-8cdf-5e02ce3f657b | -4.10215 | -48.02605 | 2025-11-12 05:22:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 253b9191-5372-31c5-855e-b477edbbfdf2 | -2.87543 | -51.47287 | 2025-11-12 05:22:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be5524d2-6276-3ec3-8957-5c7324eb4bf1 | -4.27875 | -50.53665 | 2025-11-12 05:22:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 252514c2-a115-30f3-a5df-fed577d139bf | -3.76713 | -51.8047 | 2025-11-12 05:22:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c2d9cab4-5542-3013-a2fe-05bc59614670 | -4.11242 | -48.00914 | 2025-11-12 05:22:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1cf9679-5092-3cd7-955b-d99283a51b81 | -3.84028 | -50.06469 | 2025-11-12 05:22:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 39fec286-6c03-33ab-bf6b-d8f4695ad069 | -2.86905 | -51.48084 | 2025-11-12 05:22:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9eee72c8-9d80-3af0-bd41-c1294311e504 | -2.86995 | -51.475 | 2025-11-12 05:22:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9ba56240-ac3e-30bd-8992-663c12b52399 | -3.64402 | -50.17959 | 2025-11-12 05:22:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3e4c7d8-0f65-36af-bfef-ce64c817b24a | -4.11081 | -48.0117 | 2025-11-12 05:22:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4dcf1a47-e5b2-3621-bff7-f3ab86885338 | -4.09566 | -48.02552 | 2025-11-12 05:22:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| bad3568c-1929-32cf-bff1-3963daf76cd1 | -2.64327 | -49.19547 | 2025-11-12 05:22:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d8e36c4-68a2-3ed5-ac67-d26191d891dd | -4.11003 | -48.01701 | 2025-11-12 05:22:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 747809c5-6383-3594-a92f-ec6495452c86 | -4.24279 | -50.05555 | 2025-11-12 05:22:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa7fb61d-66f4-380c-a5f9-164f7b52f400 | -3.63898 | -50.1752 | 2025-11-12 05:22:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ea2f5ec-4015-32ad-817c-a43e1b39f0e1 | -3.84645 | -50.06173 | 2025-11-12 05:22:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d892e655-3cd1-381c-8063-8190838a39c6 | -3.84228 | -50.06479 | 2025-11-12 05:22:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 77dc2fc1-b7c9-3cbf-927c-4d73b43ac8dc | -4.75321 | -48.83783 | 2025-11-12 05:22:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0157d73-430d-3db3-8734-cf4bc4f5f614 | -2.91016 | -51.47642 | 2025-11-12 05:22:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c43e47cb-6a24-313b-9438-38095a0355ec | -4.11167 | -48.01453 | 2025-11-12 05:22:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| af21e36b-2e6c-3b25-a857-15e8c8041759 | -1.11091 | -52.59167 | 2025-11-12 05:22:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8aa55d3a-017a-3d9f-ae82-c14abc77854a | -1.6396 | -52.04974 | 2025-11-12 05:22:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbb5699a-3be4-3b3f-b339-e0aabdba1eeb | -2.79363 | -51.3646 | 2025-11-12 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5329994a-0b92-31db-9b81-da77a2bb2daa | -3.49697 | -55.41381 | 2025-11-12 05:22:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3420c413-3118-39bb-a542-a6f29f8f72d8 | -1.75234 | -53.88068 | 2025-11-12 05:22:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e35e06c8-2234-3457-a12a-63c1b63720c6 | -2.91563 | -51.47424 | 2025-11-12 05:22:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 02fe4ef0-b950-3c7f-a9a7-c90be6c2adf9 | -2.91059 | -51.4735 | 2025-11-12 05:22:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a58650fc-880b-3c07-8e26-5cb29d9a6ef8 | -2.86817 | -51.48179 | 2025-11-12 05:22:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4cd9aed4-b2a7-3964-a0e6-ad7dadf2f5ee | -2.87407 | -51.48163 | 2025-11-12 05:22:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 175c5eaa-0b55-3940-8aca-6f825e24c4de | -2.81192 | -51.34621 | 2025-11-12 05:22:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de0923c0-44f2-3beb-86e4-2d9abea9814a | -1.50555 | -54.24756 | 2025-11-12 05:22:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3b8896b-7c4c-3877-9991-2cdeab38ebe2 | -2.49279 | -50.25956 | 2025-11-12 05:22:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd5bc2d4-df18-36c0-b8d1-065f8bd5808b | -2.86446 | -51.47718 | 2025-11-12 05:22:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 449766ba-7620-3f74-b408-2dbea1d0d3ee | -4.43561 | -50.54469 | 2025-11-12 05:22:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 532de56e-53c2-3c30-bc65-8f3c0b8f5aa4 | -2.48789 | -50.25523 | 2025-11-12 05:22:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8053da12-7025-34ff-bce2-a56a15c9b030 | -19.85453 | -58.00436 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 723c246e-f760-35d1-89c8-7bd9bf7420f6 | -19.80421 | -57.98639 | 2025-11-12 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 5cdf1b8a-5d1f-310f-88d1-7a19b578b911 | -16.46248 | -58.16125 | 2025-11-12 05:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |


[Clique aqui para ver as próximas entradas](README19.md)
