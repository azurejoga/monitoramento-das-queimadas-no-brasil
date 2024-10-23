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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9dbf6968-5c27-3424-8cc9-27050594f61a | -4.10443 | -48.24495 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bed79cba-0b9f-390b-aa7e-2cf4c6a581bc | -4.09918 | -48.24429 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be05d26f-30bd-37e3-8210-99a44bdd8ee4 | -4.0776 | -48.27686 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e01440d0-6e6a-3fd6-9e55-7e235e6bfeb9 | -4.07706 | -48.28003 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8133884-27a3-3a1d-bc2a-488fafec8b1d | -4.04785 | -48.10656 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 70d6fe1c-b099-3155-8631-a2ec3509392c | -4.04734 | -48.10951 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 922ade36-9546-3330-912f-3b6aac023a08 | -4.04682 | -48.11248 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ae726c4a-d62c-32f7-bc7e-2c3dda3bd3f9 | -4.0466 | -48.10585 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0bea7b31-3749-3fd7-80f9-290582dc1d63 | -4.04611 | -48.10881 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8c388305-9770-3329-93e6-806d25b82b60 | -4.04561 | -48.1118 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d1241fa6-dde3-36e2-ba20-6271c4b6fb86 | -4.04511 | -48.11485 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d3b0db7f-777f-3ae3-93df-a011996ceb48 | -3.9119 | -48.3678 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03b383d5-1fa5-30ba-b490-92548efc6964 | -3.91135 | -48.37113 | 2024-10-23 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f110ba3a-7ca2-36f5-92c8-6daaa6b1120c | -3.91107 | -48.36874 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1dd42150-c642-3189-8db4-b2a187a4b426 | -3.90621 | -48.33397 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e14aa05b-7bec-38aa-b750-de5467240c53 | -3.89676 | -48.3281 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2c62b3e-5db0-3eda-96dd-27323a5caa01 | -3.89624 | -48.33125 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 409cd0e9-23e3-3ba6-845e-4b1c56e780ce | -3.80298 | -47.80054 | 2024-10-23 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e487370e-48c6-3651-8608-37a487eb6a05 | -3.80247 | -47.80359 | 2024-10-23 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1129bd4-d90d-39dd-9b46-341e6a836928 | -3.79841 | -47.79666 | 2024-10-23 03:57:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 225c3556-3304-3a8a-ab67-3037fd6ca878 | -4.48943 | -48.111 | 2024-10-23 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f534ed73-de97-368b-af31-5807dd8ec2b7 | -4.48377 | -48.1132 | 2024-10-23 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fbd866ca-72a0-38e3-82de-cb2f8d142d60 | -4.48181 | -48.1123 | 2024-10-23 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83a7e537-76a6-3dc1-870f-0d632e8e2ac2 | -4.4813 | -48.11539 | 2024-10-23 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1afca77-888e-3200-ae4e-d2b338c2f991 | -4.47 | -48.11979 | 2024-10-23 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 322da28a-b815-3529-9d55-70be7a9656ba | -4.46435 | -48.12202 | 2024-10-23 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1437171b-55d9-30f1-a8bf-1c284a1e41bd | -4.34292 | -48.61962 | 2024-10-23 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 426cda55-03af-34a8-9e0d-942d9bb03ea7 | -4.34237 | -48.62289 | 2024-10-23 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f32f7ba3-5b8c-340a-99b5-1904219d4ec4 | -4.33706 | -48.62188 | 2024-10-23 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4fcc84fa-5e1f-35ec-870c-1829468b5443 | -4.24302 | -48.3503 | 2024-10-23 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52060c53-c24c-335d-b7a2-ea44fed919d6 | -4.23776 | -48.34956 | 2024-10-23 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bb08c70-7189-3881-a986-28676db24e7c | -4.23633 | -48.13298 | 2024-10-23 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d22e3fca-1cdc-308f-869a-d96e348f15bd | -4.23582 | -48.13609 | 2024-10-23 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ab3c9b3-9726-3e86-b024-d81e2750e8cb | -4.19028 | -47.95099 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99188251-ecf5-35f5-9432-26386b126766 | -4.18979 | -47.95392 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ceb3feb7-df33-3360-8477-3f150c53447d | -4.1893 | -47.95691 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be095bca-4773-32d1-9a7d-a764b6367a37 | -4.18832 | -47.9492 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0df8ba7-3841-3154-92e8-014edb6cc644 | -4.18731 | -47.95504 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bc8569d-26da-3c0b-a6e1-539aa93b5b5f | -4.18679 | -47.95807 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c5b48f2-af35-366c-b7d6-8da2f0e09477 | -1.18003 | -48.86018 | 2024-10-23 03:57:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0961cfe2-e605-3cd9-aa33-9f5db4d96bcb | -1.17433 | -48.85927 | 2024-10-23 03:57:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e8ae1e2-6c59-3fae-bca1-1f9fd7bd8eca | -3.45168 | -49.82681 | 2024-10-23 03:57:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b1ca364-5b86-3dc6-b429-31ab961c6358 | -3.44581 | -49.82597 | 2024-10-23 03:57:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cd9f1445-2727-32cd-ab9e-e0d810cfee57 | -3.3469 | -50.32038 | 2024-10-23 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 658b2b45-91b9-36cd-bd5b-faaabf9d4671 | -3.34609 | -50.32504 | 2024-10-23 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0173551-d3ba-3890-a22a-59f3a466f043 | -3.34524 | -50.32124 | 2024-10-23 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0935dfed-b259-3225-9c69-9c40bf188e30 | -3.26456 | -49.13376 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79044c8b-96bc-3a9f-8c96-de3e4903af3f | -3.26392 | -49.13753 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dea53e18-a512-33c9-828b-b6632644cd2e | -3.06894 | -50.50579 | 2024-10-23 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| de2baa67-585f-36f5-8a27-187320496162 | -3.06815 | -50.51049 | 2024-10-23 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e1a2e9c-b922-306c-92c1-47d0e43b309a | -2.81888 | -50.49458 | 2024-10-23 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0c6be3b-95fd-3554-9b41-5cf1c0db7c2f | -2.81809 | -50.49918 | 2024-10-23 03:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36dcf4d9-42ca-32f0-a56f-126595494ee1 | -2.76511 | -49.30311 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da6171d7-9f4b-307f-874a-be85d81753dc | -2.76443 | -49.30706 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fde1c082-81d4-3ac4-bc07-f8168a82a981 | -2.76409 | -49.30019 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ae77e89-caa2-3d17-aa54-f479105ebdae | -2.76375 | -49.31101 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db2197d4-558e-330f-bdad-e92500286c72 | -2.76344 | -49.30415 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ba59d1e-e44f-36de-8f08-f4e5444169d1 | -2.76308 | -49.31495 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8a95b01-fb4b-39b8-be96-6c9f4ba73bc8 | -2.7628 | -49.30811 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec063575-ecfc-390c-ba4f-ad0097a4c676 | -2.76215 | -49.31206 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 951258a8-d898-300d-8889-fd58c9a9bbe8 | -2.7615 | -49.31602 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c0c1b6ed-5d27-3c00-9190-e511a78023df | -2.76019 | -49.32402 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7277f7bf-fec6-341f-98ec-69c2fa649ad9 | -2.75953 | -49.32808 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8817f09f-ee38-3b27-878c-cd15446ff12a | -2.75773 | -49.30318 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8e24d356-0baf-3c51-97e4-2a42dd5c2820 | -2.75708 | -49.30715 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f2fcfea9-31eb-3e9f-b9a7-ed7d7053b0a0 | -2.75643 | -49.31111 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 500811cf-9789-34d7-b70b-a06bace51da2 | -2.75578 | -49.31508 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 68bee7a0-7d75-3a82-b8da-14bce37147ac | -2.75512 | -49.31905 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84ff40f5-2a8b-3b89-9017-1fbd578c80ab | -2.75447 | -49.32306 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bba3e023-a0f4-32da-b961-b2fb6afc8f4c | -2.75381 | -49.32703 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d2c2e6d-1079-349a-8882-7b1536b3ff09 | -2.7507 | -49.31021 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 770a66b2-3c12-3bab-9f6f-6d1b2279d798 | -2.74939 | -49.31818 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d0c5b77-e25d-3805-bfe7-99bb41345624 | -2.74874 | -49.32214 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 612bf01d-65ef-3d10-a064-7241569aa162 | -2.65753 | -49.51395 | 2024-10-23 03:57:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b923932a-6eeb-3c42-86fa-e985c4873d7b | -2.65173 | -49.51296 | 2024-10-23 03:57:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ca9d03a5-e6c1-39eb-9ca6-2fec2e5273ee | -2.65168 | -49.51336 | 2024-10-23 03:57:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 94440bdd-b115-30ee-945f-653dfa9c6034 | -2.62098 | -49.98532 | 2024-10-23 03:57:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3970e1e-4baf-3a93-9a6d-b920117d7f4d | -2.62023 | -49.98981 | 2024-10-23 03:57:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 51fc479c-8f45-38e7-8d71-ce4013b08ecb | -2.61599 | -49.1224 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d0a616a-a096-3074-8218-80564d03c4a3 | -2.61533 | -49.1263 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21fabb3c-e103-3c0b-a58e-28a8da4ba589 | -2.5426 | -49.66595 | 2024-10-23 03:57:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c834cc0-50ef-3b41-acd4-11dbd29a20df | -2.4802 | -49.11847 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 643acd0c-625e-3444-b100-9e13b5249ee3 | -2.47954 | -49.12234 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86957982-497e-3819-af13-901d451bcdae | -2.47837 | -49.11403 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbdb0036-0b81-3ad8-a9b5-09a86109c385 | -2.47774 | -49.11791 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 74c56379-0d66-3baf-a267-a06564ec50a8 | -2.47711 | -49.12179 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8f4e61ab-40b1-3f56-bc43-e09a79be026a | -2.47585 | -49.10976 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1313b339-8de3-36d2-9331-989ec18bc2d8 | -6.44798 | -49.92022 | 2024-10-23 04:00:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93c24636-d395-3817-b39c-fbd2232031d6 | -6.44596 | -49.91991 | 2024-10-23 04:00:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a7b2b7e-454a-38d6-b59d-7a8a0e5ac065 | -5.85248 | -50.05268 | 2024-10-23 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1edb290d-07c4-34c1-b7f5-8bc64109ca83 | -5.7572 | -50.22339 | 2024-10-23 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8db71eb-8d0b-3504-b0e9-699ad857981d | -5.75644 | -50.22763 | 2024-10-23 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c11fd81-d706-3cf9-9dea-b5bea3ef5b7e | -5.7514 | -50.22246 | 2024-10-23 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c0a9f19f-38d6-3ebe-98f1-c1766f2ca96f | -5.75107 | -50.22268 | 2024-10-23 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 371ae927-46ff-39d7-b19e-ca841343e6a7 | -5.75065 | -50.22667 | 2024-10-23 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d98c701-b520-35db-8371-ccc2be697f8d | -5.75035 | -50.22691 | 2024-10-23 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62f5db60-bd50-3b03-91ce-b89494f273a7 | -5.74991 | -50.23079 | 2024-10-23 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e1b6341-f17b-30d0-94d3-f4f461756c3e | -5.74964 | -50.23101 | 2024-10-23 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c4d9f84-b803-3669-bd5c-67c1648787fb | -5.24128 | -50.88076 | 2024-10-23 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c5811cc-cc76-33bb-a5b6-f00e9267b32f | -5.24047 | -50.88531 | 2024-10-23 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README24.md)
