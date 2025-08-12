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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c4d5395-505e-3eaf-8513-127cd9a1fbdc | -3.9711 | -47.87828 | 2025-08-12 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 819469c8-a349-3c69-bf22-c0c6c60d2a64 | -4.06838 | -47.97228 | 2025-08-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c1e59b9-b502-3e5c-8fc1-c880aa34bd62 | -3.05697 | -39.89563 | 2025-08-12 04:06:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| de47a93c-0aa4-36a2-bf81-d917461e009f | -3.83616 | -47.75133 | 2025-08-12 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a433c2b7-26ee-3863-8587-fc24322511a4 | -4.30533 | -48.10331 | 2025-08-12 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a1b9b40b-f43c-3a4b-a93d-7c1471c5bc20 | -3.4256 | -49.04882 | 2025-08-12 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbcc5b8d-16f2-3376-911f-2589a3d5ec85 | -5.48448 | -44.38742 | 2025-08-12 04:06:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| f39ae288-ae5c-3a76-8726-3c998a549532 | -4.80698 | -43.14505 | 2025-08-12 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e9f1b80-8b57-39d2-aefb-b30eb9975099 | -6.57477 | -44.57008 | 2025-08-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ce4bdde8-4180-3faa-b44b-0d3e7252fc56 | -6.57899 | -44.56663 | 2025-08-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c425e5a-8c55-3ce1-b166-002df017a891 | -3.96653 | -47.87772 | 2025-08-12 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| b0248fe7-3b2d-329c-b346-273c8196b847 | -6.58032 | -44.55852 | 2025-08-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 03066eba-b34c-3200-949d-b4180ac66afb | -6.58121 | -44.57537 | 2025-08-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d4068111-bcac-3d08-a4ba-0fe90de00c7f | -6.60251 | -42.76873 | 2025-08-12 04:06:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3156a1ca-ce23-360f-9247-ac5ac5d80fbf | -6.58254 | -44.56725 | 2025-08-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2e8bd13e-d462-39df-ac7f-957a5b970653 | -4.32622 | -48.39856 | 2025-08-12 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98718661-1c18-3b4f-9e7f-db6819f56ea6 | -6.59097 | -44.56041 | 2025-08-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df205d5d-7b0f-3196-82ef-e2c13dea2124 | -6.22266 | -43.329 | 2025-08-12 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e7dfad55-3797-350d-8fd5-7261035026be | -6.21587 | -43.32787 | 2025-08-12 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3c215048-841e-3ff3-a925-32b772292ea9 | -7.12018 | -44.62558 | 2025-08-12 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfb2606e-d110-31e7-8ca1-1b2335dd971a | -7.22029 | -35.76888 | 2025-08-12 04:06:00 | NOAA-20 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 580b6042-0bd8-3897-9bf2-939990cfb599 | -6.46178 | -44.57315 | 2025-08-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8cf3a13e-1346-3117-97d4-342ceacc1800 | -3.43152 | -49.04402 | 2025-08-12 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 20892a4d-bf0b-356f-b20c-faa5686dd326 | -5.4856 | -44.38847 | 2025-08-12 04:06:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bd2280e3-cad2-3f45-a100-0edf8e2780c9 | -7.29954 | -39.64264 | 2025-08-12 04:06:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0ca96923-ea9e-3919-8472-22a26d9188aa | -4.8104 | -43.1456 | 2025-08-12 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14528db9-6d95-33af-ba91-98b2afbda3c8 | -6.61009 | -43.88395 | 2025-08-12 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| f0328f28-0b30-3f4d-a693-9cd718f4b719 | -3.17262 | -48.80738 | 2025-08-12 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e74510d0-2550-3fbb-b424-a84dbe9a445b | -4.28941 | -48.05714 | 2025-08-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd0ab8b6-37eb-33b0-a028-d87554fb32ce | -4.10891 | -48.20537 | 2025-08-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4e38f9d-5199-3cf0-a087-34194591b8ae | -6.58476 | -44.57603 | 2025-08-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b564138-508e-3fe9-b11a-40001aad38d9 | -4.17582 | -42.44702 | 2025-08-12 04:06:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 127e4fe8-850b-3d7b-9188-793cfc6a9247 | -3.06909 | -40.81477 | 2025-08-12 04:06:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2873a6f0-f9df-3f52-b658-f62968789923 | -7.11662 | -44.62506 | 2025-08-12 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb1d31f7-f498-3e16-813b-a87bdcacdb05 | -5.54206 | -42.66578 | 2025-08-12 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a7a00142-ee8d-377b-8999-6e9e6e6da178 | -6.5741 | -44.57413 | 2025-08-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f57e8283-7bd7-39c2-a3d0-1e4abaae36dc | -3.83239 | -47.74598 | 2025-08-12 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| cb3d9db4-9422-3626-bb4d-377fc1630a38 | -5.48625 | -44.38439 | 2025-08-12 04:06:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8c6cacae-d3fe-38a8-b000-8cacf92e3099 | -6.13229 | -43.95074 | 2025-08-12 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c6688cbc-3455-355b-aeab-20b0862337c2 | -6.59231 | -44.55227 | 2025-08-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cde104b9-52db-3f84-a8bc-7fbfbe0b37aa | -3.83691 | -47.74669 | 2025-08-12 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 8edf2804-2e9d-3f7f-81c3-94ecfa333dc4 | -6.72259 | -43.57856 | 2025-08-12 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b41aa540-9084-3730-9afe-f3cdd9be5467 | -4.28863 | -48.06184 | 2025-08-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 544c96e8-8248-36ee-a0d3-12eb04b96416 | -5.53535 | -42.66472 | 2025-08-12 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f0c80420-8974-30a8-a4be-561047046f74 | -6.57965 | -44.56257 | 2025-08-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 657b169a-d97e-337b-88d4-85d5bf7061a0 | -4.10613 | -48.20281 | 2025-08-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 690287a6-3de4-318b-a1d0-dfd5754b3f3e | -6.72319 | -43.57486 | 2025-08-12 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5b249edf-6cf1-3085-8a29-01ab0db3e7c0 | -7.12373 | -44.62614 | 2025-08-12 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| da8e4faf-1a9f-3944-a91a-8c3b44e18c7a | -6.58188 | -44.57132 | 2025-08-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 97fbbad4-d118-396f-b3b4-0170d0963e2a | -3.43648 | -49.04485 | 2025-08-12 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8b6939a7-31f2-3174-b893-c1d5a886c427 | -4.60426 | -43.31577 | 2025-08-12 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0853718-eb9a-36c8-b098-464fe5181545 | -3.97032 | -47.88294 | 2025-08-12 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 9b10b475-2b12-3de4-8771-b3859763fc6e | -6.61232 | -43.89215 | 2025-08-12 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| aeeeb765-86a8-3444-972b-eb7546cc05d1 | -3.07239 | -40.81529 | 2025-08-12 04:06:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a9aa9632-a72e-3cd7-a5b1-07c237b481b3 | -3.10468 | -47.01278 | 2025-08-12 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db8b917d-043f-3eb1-ae34-4b11e2595fee | -6.21926 | -43.32843 | 2025-08-12 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5d9f971b-4927-3282-9a2a-fab372f1ad3d | -4.3061 | -48.09859 | 2025-08-12 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7e9ecd54-9f9e-396f-aeaf-c2d162c837fa | -6.15204 | -41.38549 | 2025-08-12 04:06:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ccc348e9-bc28-3df0-8481-4233b27a004b | -4.59393 | -43.31413 | 2025-08-12 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a740e45d-f45e-30b5-ad53-092bb9e7ce5f | -4.32477 | -40.14927 | 2025-08-12 04:06:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 40f71165-8b72-3ba0-9a8a-8ec5c047c8d7 | -6.70603 | -44.0962 | 2025-08-12 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83ffbd3d-ed9e-30c1-8117-f1415c3ba59a | -6.57543 | -44.56602 | 2025-08-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba87efcf-80dc-354f-9780-d9f25f92abec | -4.29397 | -48.05802 | 2025-08-12 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b0d4bed-57f8-3f05-a407-36f02989c1a2 | -6.30147 | -42.35325 | 2025-08-12 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 161cb6cc-29bb-309e-830f-9b045e769dbd | -6.58743 | -44.55975 | 2025-08-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 75c0afd2-2b78-37b5-a1f6-1a8ff58c944a | -7.23182 | -41.90698 | 2025-08-12 04:06:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 406fce8d-09e1-3c09-8339-e584301ffe78 | -6.3048 | -42.35375 | 2025-08-12 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c8ae7e98-0fe7-3670-9dee-1d6d474d8ab9 | -7.30299 | -39.64316 | 2025-08-12 04:06:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b495065d-af4d-3976-8565-3df0d9fadde0 | -11.47693 | -50.15736 | 2025-08-12 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 230bd253-d92d-3858-a800-fc7de70d799f | -13.96482 | -42.5804 | 2025-08-12 04:08:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f5037284-7ddc-3d62-bfcf-d7ed33075bc5 | -9.71872 | -49.47411 | 2025-08-12 04:08:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62b518e0-e5da-338a-9f59-a7c9c0bb8903 | -12.77365 | -45.45263 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 58ab0bf3-0d4a-3fa1-ba7b-51a377f9d7c2 | -8.51633 | -43.31262 | 2025-08-12 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 97484ca1-27e9-3e57-85c9-c97723922dd9 | -12.66555 | -46.97308 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ca4142b-cf4e-3249-861e-3b2ce9a9fb6d | -9.39203 | -48.2333 | 2025-08-12 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 23b60a4e-e038-35c2-8607-1067f478af6f | -11.45288 | -50.17088 | 2025-08-12 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5a9bf62-2947-32de-8777-d6cd777ba38a | -10.8576 | -45.2202 | 2025-08-12 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1a1c7f7-9207-31e9-a5a0-6d9386cdefd2 | -13.58368 | -46.94438 | 2025-08-12 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 198f5b80-ca14-375d-a291-1ae3f9700075 | -13.11657 | -46.87217 | 2025-08-12 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d4d7a4e-b93f-3fbe-adfd-bcf2271a49de | -7.54165 | -49.54944 | 2025-08-12 04:08:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72437713-eb3c-3ba2-ade5-0d9e1c40bc03 | -11.7776 | -44.93905 | 2025-08-12 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0ef2b779-01e9-3f4f-b12e-ac85838d7b7f | -14.03932 | -47.40923 | 2025-08-12 04:08:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d125d770-1b18-3ec5-a55c-10d782a61d36 | -10.35096 | -50.82616 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 619b7326-7a2c-38b1-9bff-9be07ac95d26 | -8.56178 | -54.69988 | 2025-08-12 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8f85df0-4ff5-3a91-a6f5-a596afc0a209 | -14.10419 | -44.85004 | 2025-08-12 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 106b5ef8-f4b4-33fa-ad2f-82d1cee80c41 | -10.35718 | -50.82027 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 94185222-fe3d-30a2-9fbf-094c49d9759b | -12.66931 | -46.97363 | 2025-08-12 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ef33009-8564-327f-ab3c-4abcaa7f087d | -11.67784 | -51.59615 | 2025-08-12 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2cedf996-7955-32b1-80f6-27a3847524c4 | -12.77647 | -45.45713 | 2025-08-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1dbffe5a-8153-38d0-88ee-c1ebea54e71d | -10.34617 | -50.82422 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f91018c-f591-325f-af2d-fb41fa4370ee | -9.39131 | -48.23751 | 2025-08-12 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76203dcd-6c48-369a-932b-927b9ccd27ad | -8.56759 | -54.6959 | 2025-08-12 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30f77764-27f0-3098-a0a8-0d236dfa3edc | -13.11536 | -46.87035 | 2025-08-12 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0edea31b-4f95-3356-8b62-32ad653b9ce8 | -9.71361 | -49.48101 | 2025-08-12 04:08:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d92f40ec-d30a-3046-ada1-81746b83e672 | -7.21684 | -46.22462 | 2025-08-12 04:08:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2231f7e-d9b0-3344-98bc-7556193cf856 | -14.11693 | -45.39562 | 2025-08-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06bff3e6-bb5d-3215-b952-565b08508d79 | -11.77264 | -49.56625 | 2025-08-12 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 679783ed-77b3-3fcf-8afd-4fdc98b64aea | -9.80848 | -45.95769 | 2025-08-12 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4098f066-be8d-35aa-91cc-c69fc232fbcb | -10.368 | -50.8177 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c7acc6f-84ba-321b-b33e-86582b6d85db | -10.35116 | -50.82514 | 2025-08-12 04:08:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README14.md)
