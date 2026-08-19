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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81dfafb3-7295-3450-a703-f61665e32b0a | -7.04969 | -59.84182 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 869ebb57-35dc-3f93-bf08-7a442941c4d1 | -7.55344 | -61.18065 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3f8fb1d-8952-3cc1-acc3-21e53d8c8913 | -8.56164 | -54.72823 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a930d6c4-c56f-31c1-820b-98ac3b799811 | -7.4343 | -59.80281 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e2f25dcc-caa6-3645-8a98-187ec012a76f | -8.57515 | -54.75145 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5eb61f8a-9fce-3b76-88db-550b16a5abb5 | -8.58643 | -54.77094 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5fc95e1a-dd96-363e-afbf-03e93c9752fb | -8.22029 | -55.03152 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6030f8be-3ed4-309c-a093-6ef9794ea5b0 | -8.57995 | -54.69295 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0e492c2-63a5-3866-a61a-f3485fc42252 | -9.1802 | -60.82876 | 2026-08-19 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f7427eba-061d-3c46-b232-d1c16ec48f6c | -8.53681 | -54.76142 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 76fc19da-bc4f-3814-94a1-89541d372f05 | -6.0438 | -57.79708 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e65f8e77-1e1a-30a6-991c-26a217510a2d | -6.88523 | -59.04416 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1c39b49-e0a5-3db9-943a-6feb5bc7f9ce | -6.13991 | -57.87254 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3a8db45-0dbb-3e8e-bfc7-d08c4e259ead | -8.54536 | -54.77115 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 450bf3de-365b-35e2-a35a-98c6597693f8 | -6.14283 | -57.88995 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1bcffa6f-91b2-385e-8f5d-bc440ecfc689 | -8.56686 | -54.74091 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| de226dd3-b2cf-37a3-90df-c5263ead6af0 | -8.64189 | -62.83279 | 2026-08-19 05:59:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13bcb19a-f252-3ec5-93eb-565be16a5576 | -6.89259 | -56.43978 | 2026-08-19 05:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5642ca12-6f3b-392a-988e-40f7be3a1bd1 | -6.1242 | -57.71523 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2273689f-470c-3eb6-b809-dfc3690154fc | -9.42752 | -60.41075 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5dfd296-c884-305b-9717-6ff15b0456e4 | -6.10252 | -57.86717 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 491e863a-7978-399b-ab7b-e0a699ea1c2f | -6.74692 | -59.16123 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6d1f609-39a8-3670-951c-a6c72fba2aff | -8.50982 | -54.86588 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a89588b-5ed5-3cb5-9ded-a58f7c7992df | -8.53088 | -54.75425 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3983685e-83af-3750-99b8-1914f82746fc | -9.01643 | -60.49684 | 2026-08-19 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| baa8eccd-ac84-3a92-833f-b80a919f0997 | -6.14667 | -57.86363 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93cf50cf-c151-3b8b-b813-ac4701b99030 | -9.39489 | -60.56618 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c37116dc-8c60-3ede-b30c-ef4fc7dbee3a | -8.58156 | -54.68049 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ce44a8b2-71e5-3c5e-8b11-4a074ef5a392 | -6.78858 | -59.44564 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df1a0942-4d9a-3791-8c85-ea5ae79f9e7f | -9.44315 | -60.29412 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a5cd2b2-1c18-32a9-ada2-a4dc2af4ddff | -6.86605 | -59.03579 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6fa54457-15ad-3026-9972-ce53cb216c0a | -9.39022 | -60.56556 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b9dbb482-1cfd-3d74-84ab-e12622ce4deb | -6.84842 | -59.01619 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 558aaede-8023-3b10-b8ff-33e25b1ee3fe | -6.00683 | -57.86379 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5c2840e0-cecc-32f0-b484-8868ea7d9b89 | -8.54748 | -54.75371 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8cfc6a16-b6d8-3448-9a32-ecb67bb40962 | -6.09051 | -57.91312 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 07d6442b-658a-39ae-b47c-62e00fc2a1b1 | -5.49289 | -60.13295 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d532c79-7aed-3ed3-aa01-3b6c742a5da3 | -6.70638 | -58.94194 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fcdd07c9-1ee4-307f-a40d-77cdae9ba5e9 | -6.60902 | -58.39683 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5410e16-08c7-3e35-9553-66d6a3ca5632 | -8.21791 | -55.03056 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f308c5fc-efab-3421-b7e7-e4bba717da80 | -6.35129 | -54.90506 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3c20e57e-a979-3654-b825-99f5ca5a6474 | -8.58568 | -54.72178 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10dcac7e-7330-31b8-9616-7fa3133e453f | -6.00388 | -57.84642 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5108097d-1b65-3d00-8953-7717dd03ff9d | -6.84652 | -58.99752 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1db3818-8a36-330c-82e9-100d81412a54 | -6.60944 | -58.39375 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ccbb98f-cb1e-3f67-8a24-a9fa12f3d837 | -6.1438 | -57.88327 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16db4297-17aa-36de-bf90-d2ee340c4891 | -6.99681 | -59.04951 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c436f069-6a80-3c51-bb19-e8063b938fb0 | -6.63654 | -59.07569 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 702d4780-1a42-3796-8143-0328f001f307 | -6.80234 | -59.45318 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a615c47a-689e-36eb-b18d-7e872bb4efa2 | -6.00197 | -57.85976 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 633d25b0-f95b-36b9-ba0e-e3bcef16957f | -8.56087 | -54.75624 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 869217b3-5a02-39b7-9ef5-0282bbe70e18 | -9.39757 | -60.56281 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1330acec-d94d-328a-95fd-917773f05f42 | -9.40826 | -60.58917 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a3d18f54-5252-3c28-935e-b791cb55d37c | -6.80718 | -59.45391 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa7aef27-228e-3d84-9db7-20cdc4b77131 | -7.60794 | -60.95995 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b1190e36-2a65-3361-9157-b3830e2a1fa8 | -9.42243 | -60.43933 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d96b3fe-31b1-326a-939b-eeccc197e0eb | -6.74948 | -59.17873 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cbb98a56-73f6-31fc-844a-f743fa7dce94 | -8.56973 | -54.77155 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c9e97add-a67b-3187-aaa6-331e72043d19 | -8.5692 | -54.72282 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b4d261e9-941d-3e74-8ed3-9b4b98b56a10 | -6.74285 | -59.04615 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5803910d-5cf4-35ba-a6b3-fd38055174f0 | -8.54823 | -54.74756 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4976b96d-00c4-32a3-964f-ac3029e5443d | -6.03465 | -57.80603 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d44f0033-500c-35c3-8b7b-49fb7efe2bc8 | -9.42685 | -60.41573 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 604d4b9d-bb80-3b88-b9fc-7d2922edc98d | -9.42351 | -60.44058 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6ce50950-6e8d-3ada-bd85-a51d461529c6 | -9.10793 | -60.3885 | 2026-08-19 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f76af880-dce7-3d12-831e-fa8dbe295f3b | -8.55716 | -54.73056 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 71a8333c-5153-36cb-9be4-a8739876d237 | -4.45894 | -55.4567 | 2026-08-19 05:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47680240-b5a9-3208-86af-ed1024cbbec1 | -8.53319 | -54.73613 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9487759c-d5d2-3deb-a7e7-ce9ef5068403 | -8.95809 | -60.58978 | 2026-08-19 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7db36ce9-db75-3c99-b458-2eb8ee9b8a78 | -6.13857 | -57.86189 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb19482c-059c-37c8-8d04-bce21cd4de29 | -8.50308 | -54.86541 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| db994ffb-2b74-3b49-becc-6233b945ec37 | -9.40609 | -60.58757 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b3b51fa-c409-3cf4-b5fd-eddd609ba5a0 | -6.84081 | -58.99748 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 43ca49db-aa2a-363d-b925-265ff5b97c69 | -9.3929 | -60.56217 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 962d9ed0-c9ea-3068-9753-05066a4ad397 | -7.47525 | -64.26289 | 2026-08-19 05:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 062e9aab-7c21-3e2c-b977-24270b7310f5 | -9.12132 | -61.60106 | 2026-08-19 05:59:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 354c42e4-3827-3e7f-a86f-995aa8365421 | -6.08375 | -57.92251 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c6df7818-df16-3e66-9142-856b242a48d5 | -8.57597 | -54.72357 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d8f8ed41-9d37-3d4f-9843-08c89a6e5fa7 | -9.39955 | -60.56684 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e27a17c7-f8b1-3b27-b131-dc5000eee954 | -6.33906 | -54.89756 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14f28967-fa96-3720-9bbb-cebc9dfb843f | -6.00488 | -57.83945 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f1538a3-1f20-3f81-90b1-729ca19a2a60 | -6.34544 | -54.90435 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fe2fc8e1-42fa-3d90-a31d-59d4699424af | -6.00875 | -57.85047 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 150cedd2-8c4c-370b-8008-e30373e0e443 | -6.35267 | -54.89999 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2090e159-5ddc-3fc5-9ebb-25861c048d4a | -6.04094 | -57.80007 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ad987f1-7c46-330f-89c8-6557610957bc | -6.01505 | -57.84455 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36a7f829-f8af-3643-bd99-113c3da3aa1f | -8.55571 | -54.72099 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f0ee04de-0cf3-30d7-9ea9-d610f623b873 | -6.01556 | -57.84103 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f222e17-5288-34a3-980c-1fa2c16bb70c | -8.5797 | -54.77001 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c1b1fd3a-5783-33c5-a24f-248f68081160 | -7.60919 | -60.95138 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d5c30ca-c90e-327c-a1e4-280ccf284d17 | -6.73945 | -59.03415 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bc9277b-3191-3e65-84e3-63c1458cb0ee | -6.84152 | -58.9968 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d8c958e7-e94c-3e42-a25e-c8072d483d7d | -8.56764 | -54.75681 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8c38b294-2279-3e8f-9c1a-7c701efb411a | -8.56917 | -54.74438 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c3620c79-f003-3638-ae7d-c7cc72316977 | -8.56238 | -54.68779 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4164d23a-6d70-31bf-9cb0-4ceecd98166c | -6.85082 | -58.99889 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6d333bf-458d-394b-8df5-00a34fab2cbc | -6.00437 | -57.84297 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55d104d2-e35a-39f0-a3c2-28fc098f654c | -8.56373 | -54.76498 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bde768a0-a173-37b5-a015-11b8e2e5e524 | -6.10392 | -57.85736 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89f5d0ec-1c70-3d77-a932-f6d9d1070a59 | -6.14182 | -57.85946 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README69.md)
