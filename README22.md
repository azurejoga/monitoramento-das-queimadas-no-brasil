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
| 541b9bfc-e4d8-3e8d-891c-1c38fa792e98 | -4.73737 | -46.66827 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6118fe99-bbb5-3c85-bfdd-707c0b3378cb | -4.73653 | -46.6732 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8a7dc67a-639e-351a-9cb3-b4c0946d590b | -4.73446 | -46.6657 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 87af0790-dcc6-32d6-a75c-e028aca232ff | -4.73367 | -46.67056 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 642b02cb-ef07-37ae-b234-f8718769ccb5 | -4.73287 | -46.67548 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7bb52c1f-7754-30c9-a500-7d6c1ac5d174 | -4.73275 | -46.66745 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 78368435-ba2d-39e8-9b65-24a9805f03f8 | -4.73208 | -46.68036 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a94df4e5-8784-3e02-9706-2b306e939738 | -4.73191 | -46.67231 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9c3d2e8b-4fcc-3d47-a740-cba959857945 | -4.73108 | -46.67719 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 18adfa23-b025-3372-b708-0b189f9dbec3 | -4.73026 | -46.68201 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9a9f0b85-676a-3ff0-b1b0-df075f641be5 | -4.72746 | -46.67943 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 55b7b9ea-1c09-3ea0-ba03-248aa93bbf54 | -4.63344 | -46.53476 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea650ac7-715f-3843-b703-8b3b8284433a | -4.63282 | -46.53615 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 505071bc-b1c3-3b78-b66d-a841f653751f | -4.55117 | -46.65848 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d8d0d926-acab-36e6-8eb5-e825de9f5ba3 | -4.55032 | -46.66352 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 668aa308-1ea4-3365-ab80-b8bf35921c59 | -4.52394 | -46.73468 | 2024-10-23 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb23a63c-8e2a-327d-afe9-0e56c9801f04 | -4.30408 | -46.69833 | 2024-10-23 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| efeea4f7-df52-329b-9019-22aa9165b8d1 | -4.30327 | -46.70312 | 2024-10-23 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7c85f74b-4b89-3a14-b6ad-95aa374dcdaf | -4.25624 | -46.53921 | 2024-10-23 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c1356280-80b5-3a5e-8564-36b109a469a1 | -4.18231 | -46.86518 | 2024-10-23 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87a1f577-0c62-309a-8d9d-5f7a6d12dfc8 | -4.16724 | -46.86782 | 2024-10-23 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e19a90c5-1f88-3f41-a833-c0783f9cc4cb | -4.16586 | -46.87036 | 2024-10-23 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 16a65521-6069-354b-9c0d-74db5d279c8d | -4.16248 | -46.8672 | 2024-10-23 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34092fef-56ac-3079-b83c-1d833b9df6d1 | -4.01164 | -46.53707 | 2024-10-23 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36725d96-e169-36b8-bc49-15047f11cd7c | -3.98111 | -46.47068 | 2024-10-23 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c918a0d3-4eee-39ee-ac9c-827625045f60 | -3.97652 | -46.46969 | 2024-10-23 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74e5562b-fa98-3371-bf44-6b9203089bc8 | -3.9757 | -46.47471 | 2024-10-23 03:57:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ed3ec62-6634-30b0-bd6f-9e4b6b2f694b | -3.90339 | -46.14244 | 2024-10-23 03:57:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c16bd84-846c-3b5b-959a-6ae3a0045813 | -2.13943 | -47.91999 | 2024-10-23 03:57:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f9bd17ba-db31-31c6-9847-43fde458cb8e | -2.13891 | -47.92323 | 2024-10-23 03:57:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c9f77643-be7d-3769-a31f-d0ad18676f30 | -2.13879 | -47.92003 | 2024-10-23 03:57:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0fe27b41-3f37-323d-a078-ad243c63842a | -2.13824 | -47.92326 | 2024-10-23 03:57:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7fea7b56-1ee8-3789-ae2b-7281b4991c0f | -2.13415 | -47.91919 | 2024-10-23 03:57:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 84f61b9c-5866-3ce5-b4dd-26bc306c74c5 | -2.13363 | -47.92241 | 2024-10-23 03:57:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 66409b20-f49f-3d0c-8a46-6bc13b80ab35 | -1.97655 | -48.68816 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4681248e-f90c-3dc1-a84b-468b54ab3fdb | -1.97594 | -48.69187 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c97256e-b207-3bef-8151-bc0488fcee70 | -1.97099 | -48.68724 | 2024-10-23 03:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d759674c-a75c-3f75-91c8-a655685d6e5c | -1.69476 | -48.16555 | 2024-10-23 03:57:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9a4c70d-5eef-3dc5-9ab2-6c6d14957a6e | -1.38025 | -47.82458 | 2024-10-23 03:57:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 624efc90-c6c1-3df7-86bb-7fa6ac4ffd79 | -1.37973 | -47.82787 | 2024-10-23 03:57:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3868587-0f6d-32a2-9a27-d22caf1928f0 | -1.27546 | -48.0514 | 2024-10-23 03:57:00 | NOAA-20 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48d66a47-2cad-3884-b89b-2386337a6b8b | -1.27492 | -48.05485 | 2024-10-23 03:57:00 | NOAA-20 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d2a4702-5644-39a4-ac34-ae0c1cacaece | -1.2724 | -48.05059 | 2024-10-23 03:57:00 | NOAA-20 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 959bf5b1-d2a5-3155-80d7-e5d6deeb85ec | -1.27183 | -48.05402 | 2024-10-23 03:57:00 | NOAA-20 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e3171947-ba1f-32de-a8eb-0b4a6f3559dc | -1.27007 | -48.05054 | 2024-10-23 03:57:00 | NOAA-20 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2bd21c0a-d4db-3078-967b-28629278b9e0 | -1.26953 | -48.05398 | 2024-10-23 03:57:00 | NOAA-20 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba2c49c7-9272-3587-b3ac-572e70d48073 | -3.4612 | -47.66998 | 2024-10-23 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7a31e50-85e2-32ca-b6d8-6407214ee1f1 | -3.4607 | -47.67301 | 2024-10-23 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7b51674-7f16-30dd-9497-7f8138124d0a | -3.46021 | -47.67605 | 2024-10-23 03:57:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d4aec2f-fe67-30f4-b859-d6bc05607f0c | -3.16633 | -48.37636 | 2024-10-23 03:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31147dfd-4b36-36e5-b194-06020ffc9bce | -3.16577 | -48.37967 | 2024-10-23 03:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b866fdc-1d62-39d6-a78d-6422eda39ff8 | -2.96498 | -48.00471 | 2024-10-23 03:57:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| dcde71c8-3e66-3a50-8d88-b46286ecbc67 | -2.96446 | -48.00789 | 2024-10-23 03:57:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 7e5c0e9a-4534-38af-bb8c-52cb3cb7a3cc | -2.95924 | -48.00697 | 2024-10-23 03:57:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b491e8fa-f532-3b8a-a9f6-dc864d766ced | -2.89604 | -48.29178 | 2024-10-23 03:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b1baf82-d818-316a-a0d8-ebc94a32f92e | -2.8907 | -48.2909 | 2024-10-23 03:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ef05944-7392-3dc5-a58d-77a1a8e7c201 | -2.79219 | -48.57307 | 2024-10-23 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46154ae4-a579-3d4f-80e2-3c5571b7349b | -2.78796 | -48.57303 | 2024-10-23 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 516f6a58-22f1-340d-8369-90fe0d6ca84e | -2.78735 | -48.57657 | 2024-10-23 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae2a226a-ee69-3c6a-b13d-3dd1ace6c311 | -2.78676 | -48.57208 | 2024-10-23 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc09d232-64be-3fe9-9f63-72540fe8d9f4 | -2.78619 | -48.57562 | 2024-10-23 03:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5707ee1e-7a0e-3b16-80c2-b4ad21e2ce72 | -2.27962 | -47.91641 | 2024-10-23 03:57:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 164c727b-a6d1-3bc9-84ef-805c0626dbd1 | -2.27907 | -47.9197 | 2024-10-23 03:57:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f9af45be-57fb-3cae-9fec-daf3274cb5bc | -2.25617 | -47.66318 | 2024-10-23 03:57:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb73f08b-4f41-34ac-9855-7ac1311a6bdb | -2.25566 | -47.66634 | 2024-10-23 03:57:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e18ab39-d634-3875-bec1-9cf10ad470e9 | -4.54408 | -48.83357 | 2024-10-23 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbb81a23-25fa-34ad-860a-7c19df3396b2 | -4.40252 | -48.83638 | 2024-10-23 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4ed80f0-dbc5-3b2a-8539-0339851504a2 | -4.40192 | -48.83989 | 2024-10-23 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5484ee8-0257-3ea9-b7a7-a648695a36de | -3.9792 | -49.02583 | 2024-10-23 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dfa943d2-387b-3e3d-89ee-cffd91d25a42 | -3.97433 | -49.02113 | 2024-10-23 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 04725881-dc38-3a58-b760-83db663225c6 | -3.97373 | -49.02472 | 2024-10-23 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d395c1f7-1fb4-3d4d-aca4-b8456ac18547 | -3.82407 | -48.87466 | 2024-10-23 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9b03936-cf54-38f5-aec6-a7528a2bded1 | -3.82346 | -48.87822 | 2024-10-23 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e1bcb31-fbe6-3dda-812f-af08e576568b | -3.82328 | -48.87394 | 2024-10-23 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fdaef3ff-6724-3f5e-9cb5-be6b27e8853a | -3.8227 | -48.87751 | 2024-10-23 03:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3820b998-9428-3d3d-9e3e-10e3329db28f | -4.1816 | -47.98816 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| dc78d7f9-e4ac-35ba-805d-c2fe30b76341 | -4.18108 | -47.99121 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2e74e1b9-de16-3e9c-97ff-f952e75dc257 | -4.18055 | -47.99426 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b75e111d-d14f-3faa-b366-d0fd73ead4c2 | -4.17925 | -47.98608 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 07031d77-b374-3248-8641-3b4f5875a57b | -4.17875 | -47.98914 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a431df98-6af8-333e-a930-6f80cb5d383f | -4.17824 | -47.99218 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d421c268-b3cd-35c3-b835-7ada650755ae | -4.17774 | -47.99523 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e05ffeda-ee63-35c3-86d0-b0dfbd3b12b9 | -4.17724 | -47.99827 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa77c7d8-48c0-3712-a4b3-52fd47b98561 | -4.17699 | -47.98436 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 88d05542-42b9-3e8e-988a-66f1f52e1b02 | -4.17647 | -47.98742 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f028a321-7061-38b7-932c-59b7b93fcdd5 | -4.17594 | -47.99046 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 59b09935-f5d3-368f-9d3d-ca8bd3347017 | -4.17542 | -47.99348 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 198fe2f0-83b9-3bc6-b7ae-7fe033819249 | -4.1749 | -47.99649 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3b84addb-94c4-34a3-b9c8-5caf17980889 | -4.17435 | -48.60215 | 2024-10-23 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f304dcaf-abd2-3b56-8b2a-cbf2aebf6a77 | -4.1741 | -47.98539 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 42f7ee9b-d3f5-367f-bfea-a2f48582f143 | -4.17378 | -48.60558 | 2024-10-23 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da0a34c0-6e2b-3e0e-b608-f7aec7f559c2 | -4.1736 | -47.98845 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 473e61f4-7008-30f1-b9af-f5b7c143d053 | -4.17323 | -48.60891 | 2024-10-23 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f84435e-8cbb-3a14-827b-706f3be2e6a9 | -4.1731 | -47.99146 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b98f03a1-cf14-3fbe-9f46-2227a6e0e60c | -4.17261 | -47.99446 | 2024-10-23 03:57:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a78881ed-9533-31e0-a23b-5c3008fa974c | -4.17016 | -48.59439 | 2024-10-23 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05043dfc-f4a6-33a7-bd69-01cec89c18e5 | -4.16959 | -48.5978 | 2024-10-23 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de16b088-44b5-347d-be51-f08a88ade662 | -4.16902 | -48.60126 | 2024-10-23 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f9edd20-a579-3bf6-94ca-b7459c83b26b | -4.16845 | -48.60469 | 2024-10-23 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 408cfa69-fae8-315d-aefa-7cfb3489d7ca | -4.11164 | -48.48785 | 2024-10-23 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README23.md)
