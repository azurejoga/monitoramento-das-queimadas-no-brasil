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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 528e5161-16be-3698-a526-64993a6bfa14 | -11.0972 | -49.6025 | 2024-10-02 03:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1d819aba-d87e-3a18-b361-41c3d84b9bec | -11.09383 | -49.58964 | 2024-10-02 03:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8deeae58-b309-3334-b6aa-3bdc2decd1b6 | -11.09307 | -49.59355 | 2024-10-02 03:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f51b358c-7d30-39eb-ad3c-73baf6e02dab | -11.09231 | -49.59746 | 2024-10-02 03:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e3b83551-3ed5-3de1-ae22-4728f33f2c0f | -11.09155 | -49.60139 | 2024-10-02 03:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ddb0841-501e-3148-ab20-f2358d086e09 | -11.08742 | -49.59243 | 2024-10-02 03:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7179ad9-f157-3cbd-b9aa-e03c625ca63a | -10.91115 | -50.12845 | 2024-10-02 03:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bcfb936-7ba5-391b-b7ef-5c241209375c | -10.91031 | -50.13276 | 2024-10-02 03:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ac19939-51ba-397e-9f56-4ffda5d906a2 | -10.90948 | -50.13707 | 2024-10-02 03:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87adc180-6e3c-3bb9-a694-65b3424b91b2 | -10.89943 | -50.09486 | 2024-10-02 03:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aac8af0e-8a7b-3610-939a-dd619a70d8da | -10.8986 | -50.09913 | 2024-10-02 03:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fa5db55-1572-35b0-9f4f-2c21c802f374 | -10.89777 | -50.13465 | 2024-10-02 03:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 01d678d8-e6bc-3d0d-ab3c-a8d7b4bba0b0 | -10.89693 | -50.13895 | 2024-10-02 03:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 095c4238-f946-3c69-9fc0-c36ab8265f50 | -10.89609 | -50.14325 | 2024-10-02 03:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 91f69512-bbfe-33f4-b70b-79f8e9cdf555 | -10.89359 | -50.09365 | 2024-10-02 03:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d547a36-e72b-3a93-92fc-562fada7cff6 | -10.89275 | -50.09794 | 2024-10-02 03:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8f5d542-9919-3ac3-8c7a-470a74732b2a | -10.89191 | -50.10222 | 2024-10-02 03:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e56cb70e-3dad-3dfe-9cdc-8fecef203b49 | -10.51522 | -51.08714 | 2024-10-02 03:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1fb664a6-eec4-3e90-adba-c7f088b5e2c2 | -10.51419 | -51.0924 | 2024-10-02 03:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d98037b-1f19-3d15-8515-166de1c50e35 | -8.38495 | -46.38569 | 2024-10-02 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 399f6d73-8653-3d53-b4c3-ac466e229af0 | -8.03413 | -46.0611 | 2024-10-02 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd0e3c58-7381-3104-bef7-1b12c48f02c1 | -8.02081 | -46.04625 | 2024-10-02 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75833062-cb73-3382-9d9a-a2b0ab0e315c | -7.25331 | -46.84906 | 2024-10-02 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c8b4d2b-ea4d-35a2-9f2a-5ae3ff1cf0cb | -7.24965 | -46.84683 | 2024-10-02 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ba5f8110-6cfb-3f1e-b62f-bb2d39398f03 | -7.20477 | -47.70066 | 2024-10-02 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 49dd5857-0f29-3e18-a00a-7b4d458a36e2 | -7.20227 | -47.70003 | 2024-10-02 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e6c4f888-d98b-3750-975a-a92242f785bc | -7.17867 | -46.95473 | 2024-10-02 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 40120103-e620-3c43-b401-28487622af15 | -7.17758 | -46.96092 | 2024-10-02 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 788a0044-7426-30f3-b67e-c73e32830793 | -7.1745 | -46.94861 | 2024-10-02 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2ca5ef09-73aa-3b6d-9b63-4561ece02653 | -7.09686 | -47.87115 | 2024-10-02 03:53:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ce2de8a-3324-3536-b70d-f8dde900bed5 | -7.09623 | -47.87465 | 2024-10-02 03:53:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 859e9a1d-2ca9-306d-9b25-afc59426b65e | -6.94651 | -47.66047 | 2024-10-02 03:53:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e9771ee-61c4-33e3-8cbe-51301aabed7d | -7.25384 | -46.84615 | 2024-10-02 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 03583e4d-0184-3d44-a420-9c4164749c29 | -7.25015 | -46.84392 | 2024-10-02 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5cbe5aa5-b57e-3289-8388-66c4bd288b0e | -7.17968 | -46.94898 | 2024-10-02 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c5c43551-4e21-3f71-bb51-2b008bde9068 | -7.17918 | -46.95183 | 2024-10-02 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 560d88f7-c02b-3200-8bb3-75b790988dd1 | -7.17813 | -46.95778 | 2024-10-02 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cd352a8b-a262-3ae5-a03f-6ef8eea9ed07 | -8.96676 | -48.15242 | 2024-10-02 03:53:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32d3e90d-9c47-3c1a-bd16-4a0ec56bb30e | -8.96612 | -48.15588 | 2024-10-02 03:53:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69b69c3a-c4b5-37fc-bd86-7b8061e1e6c4 | -8.96269 | -48.15796 | 2024-10-02 03:53:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8534531d-7230-313e-a7a5-ef62d7faef94 | -8.52806 | -47.32698 | 2024-10-02 03:53:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69279968-b8d7-3d18-a729-06cf6ec10205 | -8.52296 | -47.32602 | 2024-10-02 03:53:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee6d5fd4-8ced-38d2-b75a-d1ea7b133528 | -8.5173 | -47.32823 | 2024-10-02 03:53:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59a3534a-2564-3a62-bf93-f7336a3d6202 | -8.96331 | -48.15453 | 2024-10-02 03:53:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae5e6741-140b-3c92-921d-c85710c243e5 | -8.96078 | -48.15485 | 2024-10-02 03:53:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bf4cc8f-5813-363d-a2e8-e7fec0bee092 | -8.96014 | -48.15828 | 2024-10-02 03:53:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02cf4471-7bf3-3986-8103-1eb239249f86 | -10.4736 | -37.87479 | 2024-10-02 03:53:00 | NOAA-20 | PARIPIRANGA | BAHIA | Brasil | 2923803 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7b328985-01ef-307a-bf46-59e2eebce72d | -8.63789 | -40.28837 | 2024-10-02 03:53:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9774705c-3e0c-38d4-86fb-a9ef9f47e647 | -8.64186 | -40.28527 | 2024-10-02 03:53:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ee88fa3c-7b49-399b-8367-2182d272f527 | -8.63848 | -40.28473 | 2024-10-02 03:53:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 761450c0-60e2-3c4c-bc41-1bcb007e2e39 | -8.77237 | -40.37295 | 2024-10-02 03:53:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7cee9f82-6ecf-3a7f-a8c9-5327d23c0500 | -8.63731 | -40.29201 | 2024-10-02 03:53:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9b647ccb-7fc0-3a9a-abd4-1b9cffafdb9f | -8.27326 | -40.592 | 2024-10-02 03:53:00 | NOAA-20 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ee698abe-0a74-3a33-ba32-038cd96335bf | -8.77108 | -40.37336 | 2024-10-02 03:53:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c147eed2-bdf8-39d6-8092-a80f585c2ac4 | -8.34492 | -40.43258 | 2024-10-02 03:53:00 | NOAA-20 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 630b34d1-8252-3368-9658-9da2ef9a9eb1 | -9.57333 | -40.34196 | 2024-10-02 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 83e06a1b-8aa5-33d6-a3b6-df0faf5ef1f3 | -9.46097 | -40.36478 | 2024-10-02 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 838be2a7-4015-350f-abed-eefccc023db4 | -9.43203 | -40.31918 | 2024-10-02 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f16be711-846a-3f68-8702-23d20d21ebd7 | -9.46039 | -40.3684 | 2024-10-02 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5a9cecc5-4827-35f4-941d-75fc393d1939 | -9.43376 | -40.31949 | 2024-10-02 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4ac40a5c-6820-36a8-845c-39b9ba39a90f | -8.43417 | -41.93657 | 2024-10-02 03:53:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bf00f86e-29b6-3340-877d-76f643b429d3 | -8.43058 | -41.93579 | 2024-10-02 03:53:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1bd12b43-96fd-3fc6-a59e-c764cc59dbd6 | -8.42987 | -41.94006 | 2024-10-02 03:53:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 062155ce-8cfe-3c65-b268-0cc7d2fe80ac | -7.90429 | -43.17096 | 2024-10-02 03:53:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a3c3b0d1-a05b-3caf-b8ba-df2074557f6b | -7.87641 | -42.66914 | 2024-10-02 03:53:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 54ee5bfb-cf83-3bec-991e-2798d3e3ecbd | -7.84362 | -43.07595 | 2024-10-02 03:53:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 14029c91-858d-3234-bcb8-c590fa9ee6a8 | -7.83501 | -43.0796 | 2024-10-02 03:53:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a55d4512-5e18-3a39-a304-5567d96bede5 | -7.83249 | -43.09467 | 2024-10-02 03:53:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 338d2518-c692-395a-865f-7bf0f5471d82 | -7.83029 | -43.08394 | 2024-10-02 03:53:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 91417305-e493-3143-9e84-cd64636a0374 | -7.8264 | -43.08329 | 2024-10-02 03:53:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f88fddae-c3df-3818-a708-d6fcc98dcd8a | -7.82554 | -43.08834 | 2024-10-02 03:53:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 042c3d8a-60c3-32b9-abe7-da4e0e5445d0 | -7.8225 | -43.08264 | 2024-10-02 03:53:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 64d69b58-18e9-33d6-a534-9dbd5124ff92 | -7.70936 | -42.9916 | 2024-10-02 03:53:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 1f240815-40f8-3fc2-ac33-48a34d94b5bd | -7.70854 | -42.99643 | 2024-10-02 03:53:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 1a54b12d-e43d-33d4-b71a-1bd15d389d0d | -7.86883 | -42.66783 | 2024-10-02 03:53:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c96e40ef-89ae-30f1-a2fc-e0ce8af9e374 | -7.84751 | -43.07661 | 2024-10-02 03:53:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8deaa8a7-cf8d-308b-9b35-5965e0802f5a | -7.76324 | -43.05102 | 2024-10-02 03:53:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 778c705f-9465-38bf-8d00-837644efa073 | -7.70549 | -42.9909 | 2024-10-02 03:53:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| c94008cf-29ff-3343-a887-88db99623d41 | -7.86804 | -42.67249 | 2024-10-02 03:53:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a6c336e5-c3c3-30d0-8dd1-190b594cc471 | -7.85444 | -43.08294 | 2024-10-02 03:53:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7fd50198-a500-393d-a7a6-86367bd36f59 | -7.83723 | -43.09026 | 2024-10-02 03:53:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ace1d8c4-7b4e-35d1-873c-48c84ee68604 | -7.82859 | -43.09406 | 2024-10-02 03:53:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f6e2dbff-ace9-3e20-ace2-e1e2f041d950 | -7.75935 | -43.05036 | 2024-10-02 03:53:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 34652689-d72a-3e71-b5ae-9d031219cd93 | -7.70466 | -42.99577 | 2024-10-02 03:53:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| d14af304-7665-3a61-8c70-ce8189130c40 | -7.87261 | -42.6685 | 2024-10-02 03:53:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3e492812-aa27-3347-99ac-360fd5412d2b | -7.87183 | -42.67315 | 2024-10-02 03:53:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1d4a3a6a-174e-3dc4-9406-a9e2b79c6300 | -7.85749 | -43.08866 | 2024-10-02 03:53:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c1307d09-d226-31f9-a548-b1ec5c968c29 | -7.85278 | -43.09295 | 2024-10-02 03:53:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e0c80c2f-8b01-3e60-a407-720b2546df67 | -7.85139 | -43.07728 | 2024-10-02 03:53:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 19839408-37db-38a5-ae24-5caafecab351 | -7.83113 | -43.07892 | 2024-10-02 03:53:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a257a194-3371-354c-8251-4d538b350eab | -7.82944 | -43.08898 | 2024-10-02 03:53:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 92a2c9f9-803b-3875-9aea-c7fdb2c4fb46 | -7.77101 | -43.05233 | 2024-10-02 03:53:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 20eb2965-f6d0-33bd-9587-eb88c72fdf18 | -7.76242 | -43.05596 | 2024-10-02 03:53:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 72eb3f44-e0a2-38dd-bf97-c0d1f1cb68b3 | -7.79165 | -43.8317 | 2024-10-02 03:53:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd6a4743-645f-3afe-9eff-212c90bb0f9d | -9.27541 | -43.46317 | 2024-10-02 03:53:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ec48af06-9cbc-3d33-b299-860bb48f7389 | -8.5035 | -43.91995 | 2024-10-02 03:53:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ae58546e-2373-36f5-966b-f29a333fff82 | -8.31776 | -42.81588 | 2024-10-02 03:53:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b6a7b67e-e271-3c56-a8a3-c3d5f03b9be9 | -8.14973 | -42.91216 | 2024-10-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2f4ac576-a678-3f72-9a69-9a7749ff51d0 | -8.1429 | -42.90597 | 2024-10-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e47581de-c1f6-3d1d-94ab-0978f6ca4c74 | -8.15055 | -42.90736 | 2024-10-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |


[Clique aqui para ver as próximas entradas](README66.md)
