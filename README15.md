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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee4541f6-f052-30ec-b6b6-ed3034126ae0 | -7.2384 | -42.290401 | 2024-10-09 00:40:54 | METOP-C | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3ae15b44-4a72-386b-83f1-7552bd208eaf | -7.2263 | -42.283298 | 2024-10-09 00:40:54 | METOP-C | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 504fa6d7-28fd-3590-a990-b49d71ddd83c | -7.2286 | -42.292702 | 2024-10-09 00:40:54 | METOP-C | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| efc063e3-058f-3530-bdce-1b11a12d9a3f | -8.2601 | -46.855202 | 2024-10-09 00:40:55 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 080a99d4-fab7-35ce-b931-37a153ce1186 | -8.2617 | -46.862202 | 2024-10-09 00:40:55 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 40828803-1f9d-349e-8180-74b83e57782e | -8.2632 | -46.869099 | 2024-10-09 00:40:55 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a5d4541-f726-3aec-b91f-6d237d60c389 | -8.2503 | -46.857399 | 2024-10-09 00:40:55 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c92864a-3ce2-3a9d-8a40-83eb371c3fdd | -8.2375 | -47.028099 | 2024-10-09 00:40:56 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d87f334-4062-3309-aeac-b1000f937984 | -8.6008 | -48.835999 | 2024-10-09 00:40:56 | METOP-C | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 12fa9be1-4702-3167-ac6c-5f23f901d513 | -8.6025 | -48.843899 | 2024-10-09 00:40:56 | METOP-C | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 3a998027-8b63-35fc-859d-d801335230db | -8.492 | -48.6236 | 2024-10-09 00:40:57 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| be3e1ada-6f8c-37f0-a349-e6e95b964e23 | -8.4938 | -48.631302 | 2024-10-09 00:40:57 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 7029ee14-6e82-3bae-8b0a-e52fdb88290f | -8.4955 | -48.638901 | 2024-10-09 00:40:57 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 8305d6f5-af4c-3622-ab77-24718b6d0eb9 | -8.4972 | -48.646599 | 2024-10-09 00:40:57 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 0a7d85f8-b6af-3b7d-8509-46c7ff5ebc95 | -8.5247 | -48.770599 | 2024-10-09 00:40:57 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 61e5960f-45c7-3c4c-8851-4488cbc22843 | -8.5264 | -48.7784 | 2024-10-09 00:40:57 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| de21e050-5514-3638-ae03-86047752acb3 | -7.1352 | -42.636902 | 2024-10-09 00:40:57 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0c375261-71fe-3ad8-87a2-65bcf6a6c827 | -7.1374 | -42.646 | 2024-10-09 00:40:57 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a4abf119-57f0-344f-883c-bb4521d85ad2 | -7.1254 | -42.639198 | 2024-10-09 00:40:57 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| da8a37bd-be2a-3770-a5aa-4897f9039ac6 | -7.1156 | -42.641499 | 2024-10-09 00:40:57 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fcc0c5b1-0702-354c-9772-db610a1bfb0e | -7.6344 | -44.803699 | 2024-10-09 00:40:57 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f8b62281-2379-3b47-9303-0a8e8e6e9815 | -7.6361 | -44.811001 | 2024-10-09 00:40:57 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2782f430-db9d-3a0e-b1f7-274ec5500b65 | -7.6378 | -44.818199 | 2024-10-09 00:40:57 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fa6a4ba6-d19b-3d15-a5e8-652dbad173ac | -7.6213 | -44.7915 | 2024-10-09 00:40:57 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ee975896-70e1-3a7e-84f8-62890c22a201 | -7.623 | -44.798801 | 2024-10-09 00:40:57 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b39a6fb7-9219-33e7-874c-6f07c00eb40c | -7.6263 | -44.813202 | 2024-10-09 00:40:57 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 99025e39-58bb-3e2e-b168-22331bdce3b6 | -7.628 | -44.820499 | 2024-10-09 00:40:57 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dabd1378-138b-3716-8186-56c8421c4586 | -8.484 | -48.6334 | 2024-10-09 00:40:58 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 495e553a-cfc1-3180-9412-ce595de1e6f5 | -8.4857 | -48.640999 | 2024-10-09 00:40:58 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| f5c67148-a479-3b2c-b725-4eadca7bcd39 | -8.4874 | -48.6488 | 2024-10-09 00:40:58 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 9875ea91-3600-3f1c-ac2e-8436bbd47148 | -7.0994 | -42.6166 | 2024-10-09 00:40:58 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e97225e6-7649-3e35-83b3-9d51cbec5405 | -7.1015 | -42.625702 | 2024-10-09 00:40:58 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6544ba4e-1414-389e-b206-23275e624c16 | -7.1037 | -42.6348 | 2024-10-09 00:40:58 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7c792a11-28db-33bf-a71c-348710c4b810 | -7.1058 | -42.643799 | 2024-10-09 00:40:58 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 65e850a2-6dcf-33a8-ac4d-9dbd062869e4 | -7.3469 | -43.662601 | 2024-10-09 00:40:58 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 75dbe2f5-9fce-3847-ba71-abff09d3d887 | -7.3488 | -43.670601 | 2024-10-09 00:40:58 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e84ae8f3-6d5f-37fb-8b48-0f70b84223ed | -7.5885 | -44.783699 | 2024-10-09 00:40:58 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| daf5479d-be3d-3a7b-8326-d382ebfd61f1 | -8.5217 | -50.0173 | 2024-10-09 00:41:02 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ede1d5cf-9802-3928-b368-e1d81ec752e7 | -7.744 | -46.5798 | 2024-10-09 00:41:02 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a7f961d7-166e-34a4-8453-e663ee576112 | -7.3117 | -44.969299 | 2024-10-09 00:41:03 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2e6421ad-ffa9-30f7-8929-911f2e3c3327 | -7.3134 | -44.976501 | 2024-10-09 00:41:03 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 847f8994-8f6c-3bc5-900d-8d9d8d0720b1 | -8.5596 | -50.521099 | 2024-10-09 00:41:03 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b90a29f3-cb6e-3854-9139-1e13373d7638 | -7.3019 | -44.9715 | 2024-10-09 00:41:03 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e08bfd85-a0e4-3154-8ee0-e8527d36051b | -7.3036 | -44.978699 | 2024-10-09 00:41:03 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c321e18a-4eaa-32b0-b600-05885402bcd9 | -7.3052 | -44.985901 | 2024-10-09 00:41:03 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a389f632-ad5a-3e79-85d9-ad9b3ff71474 | -7.2921 | -44.973801 | 2024-10-09 00:41:03 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| daf6f5bf-8398-3bfe-a3f9-7de6632ca72c | -7.2938 | -44.980999 | 2024-10-09 00:41:03 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af4d5bf5-15c9-36b5-bbf8-eff034a4503a | -7.766 | -47.039001 | 2024-10-09 00:41:03 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2fa5e2d8-adcd-34d0-8b0c-0d3aa75f5e6f | -7.7676 | -47.045898 | 2024-10-09 00:41:03 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bbe8c636-70d3-3890-bd44-79753c424d04 | -6.6519 | -42.124401 | 2024-10-09 00:41:03 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b4315d33-f309-3ee6-b98f-e8ce510f3f2b | -8.3379 | -49.6464 | 2024-10-09 00:41:04 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bec37ae0-2d3b-3d4b-80d1-7e9b1ef85069 | -8.3397 | -49.6549 | 2024-10-09 00:41:04 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1426161-a2ba-3a59-b7b2-fcbf3845d47a | -7.3919 | -45.673 | 2024-10-09 00:41:04 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e92c80e6-d64d-3ac7-8b88-6574ce87043b | -7.3935 | -45.679901 | 2024-10-09 00:41:04 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f3dcc325-d13f-38ea-b687-aac4a6779585 | -7.3951 | -45.686901 | 2024-10-09 00:41:04 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 59ef603b-16fb-3dbe-aca1-14edbf59e542 | -7.0989 | -44.454102 | 2024-10-09 00:41:05 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b0ac9859-0e0d-3810-8b26-89b164d0a7f6 | -7.1007 | -44.461601 | 2024-10-09 00:41:05 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96d7b2f3-4a68-36d5-ac04-ebdaeae542b0 | -9.3003 | -54.5079 | 2024-10-09 00:41:05 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82571056-06e5-3df3-9aa4-6d08b170f23f | -7.1342 | -44.827 | 2024-10-09 00:41:05 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3d9520d-a895-3f23-9dce-796e3272086e | -7.1359 | -44.834301 | 2024-10-09 00:41:05 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98e92a1b-4fdd-39ab-9229-c3253a80d0dc | -6.4847 | -41.943001 | 2024-10-09 00:41:05 | METOP-C | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 47b067e1-e8e9-3f54-8824-914fbeaa6b40 | -6.4871 | -41.953098 | 2024-10-09 00:41:05 | METOP-C | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 66038457-8b84-3d13-91c0-15fc342b536d | -6.4749 | -41.945301 | 2024-10-09 00:41:05 | METOP-C | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fe20f0fc-b527-348f-b757-8d4597934e87 | -6.4774 | -41.955399 | 2024-10-09 00:41:05 | METOP-C | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 100cc9c5-3753-3129-a20e-fe1d25548ab3 | -7.6824 | -47.306198 | 2024-10-09 00:41:06 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 526f90cd-8537-3d4a-9d4c-e63a65db9585 | -7.684 | -47.313202 | 2024-10-09 00:41:06 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b8cd709-e263-3782-81db-4e0b639df7ab | -7.6725 | -47.308399 | 2024-10-09 00:41:06 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 475e336b-af8e-36e8-a650-a427e4d89c36 | -7.6741 | -47.315399 | 2024-10-09 00:41:06 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 63fccee0-5ad4-33d6-88d6-44f556285083 | -7.4994 | -46.591702 | 2024-10-09 00:41:06 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c5d256e4-2b46-38fc-aef9-80e04c66a323 | -7.501 | -46.598499 | 2024-10-09 00:41:06 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 428ec45f-1c35-3675-abdc-5d860ecac505 | -7.5026 | -46.6054 | 2024-10-09 00:41:06 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 21331f98-28ec-30f2-971d-46682970ae0b | -7.3701 | -46.0714 | 2024-10-09 00:41:06 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0c895c58-906f-3cb9-9668-679eebfd031c | -7.3717 | -46.0783 | 2024-10-09 00:41:06 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f3c5834-96e2-3c1a-b401-f01fd7683350 | -7.4841 | -46.660099 | 2024-10-09 00:41:07 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a98b606e-341c-39f8-a0f9-cb86a39c4706 | -7.4857 | -46.667 | 2024-10-09 00:41:07 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 653a83e0-933e-37cc-af91-7211460504b7 | -7.4873 | -46.673901 | 2024-10-09 00:41:07 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e010d2c-2a21-3612-bc84-ab193e011020 | -6.7832 | -43.810799 | 2024-10-09 00:41:07 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0d7534f3-83b7-3f46-ad1a-6d5c3654104f | -6.9286 | -44.564201 | 2024-10-09 00:41:08 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00b7ffc7-7f09-393b-a6c1-0c88bdee3465 | -8.0738 | -49.659302 | 2024-10-09 00:41:08 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4df840d9-401a-3456-acd2-9650e427bb19 | -8.064 | -49.6614 | 2024-10-09 00:41:08 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1ffc5b8-8b74-36d9-98fb-d2344afe2c95 | -6.6656 | -43.486599 | 2024-10-09 00:41:08 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a32ce571-8458-3ae1-a2cb-a0ffc46e91a5 | -7.0087 | -45.219799 | 2024-10-09 00:41:09 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 50096917-0813-3ef9-8b3e-2c37b1832b8a | -7.0104 | -45.227001 | 2024-10-09 00:41:09 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3618af55-4455-3fca-bcca-3aa11fe32342 | -6.9989 | -45.222099 | 2024-10-09 00:41:09 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28237ae7-156b-3079-ac63-b6337c8290ab | -7.0154 | -45.382599 | 2024-10-09 00:41:09 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb7b3a9b-84e5-3ccd-a392-a6cdaa593db1 | -7.2539 | -46.3293 | 2024-10-09 00:41:09 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f61ced1-660a-3ab7-93eb-8a25689f6a32 | -7.2554 | -46.336102 | 2024-10-09 00:41:09 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3caa0c87-f2d4-3484-b5d0-3604361054d3 | -6.9467 | -45.219002 | 2024-10-09 00:41:10 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c277bfd2-ed0c-30d8-9097-1f78c8c56cfb | -6.9483 | -45.2262 | 2024-10-09 00:41:10 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd560a90-3713-36c5-ba00-b3ee708fa42c | -6.9582 | -45.268902 | 2024-10-09 00:41:10 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7edeb57b-50b0-304a-b133-b0221189d980 | -6.9598 | -45.276001 | 2024-10-09 00:41:10 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 641616cf-85ac-3bd9-9eaa-a7ebae6658bb | -7.4864 | -47.5783 | 2024-10-09 00:41:10 | METOP-C | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aaa705e9-ca40-3604-b305-d9848db4ee21 | -7.488 | -47.5853 | 2024-10-09 00:41:10 | METOP-C | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a870e138-8765-31b7-bf7e-4162486d2ed1 | -7.4782 | -47.587502 | 2024-10-09 00:41:10 | METOP-C | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f78f5c21-9ae9-38ed-83d2-288d00130918 | -7.4572 | -47.540501 | 2024-10-09 00:41:10 | METOP-C | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 494292bb-ad94-355d-b1df-8ab2ca36be7b | -7.348 | -47.103699 | 2024-10-09 00:41:10 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ddac0dc8-86ff-37ca-8c6c-a6369bd6aa40 | -7.3496 | -47.1106 | 2024-10-09 00:41:10 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ceda3955-b9c3-31f4-a5c4-acceaf726c14 | -6.7291 | -44.284401 | 2024-10-09 00:41:10 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 85bf3bca-66e6-3cfc-a18d-da8de8513e20 | -7.4341 | -47.347099 | 2024-10-09 00:41:10 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 19569ee0-cc13-3ec8-903f-2a8eae0d6010 | -6.6722 | -43.9538 | 2024-10-09 00:41:10 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README16.md)
