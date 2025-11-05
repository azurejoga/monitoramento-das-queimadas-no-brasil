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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e387ded8-7f6e-3e53-aabe-2b892e01396d | -1.27337 | -49.14471 | 2025-11-05 03:49:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b1958099-ed2d-3937-acf3-b619193bff26 | -1.29339 | -49.15513 | 2025-11-05 03:49:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9067dee3-3832-366c-92a9-e20ee805d13f | -1.26521 | -49.15023 | 2025-11-05 03:49:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ce8f1361-cfc5-3424-9986-12e79863ec75 | -1.2793 | -49.15268 | 2025-11-05 03:49:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4fa8b1ed-88a6-3b74-a884-e9da67d645f2 | -1.25111 | -49.14782 | 2025-11-05 03:49:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0e7e021-270e-3fc1-abb8-a88bede74698 | -1.25224 | -49.14108 | 2025-11-05 03:49:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 695601b1-0370-3dd8-bf7e-417fc9bbced0 | -1.29933 | -49.16311 | 2025-11-05 03:49:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a4a40703-5801-36d6-9f40-963dfceb848c | -1.24407 | -49.14661 | 2025-11-05 03:49:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0946143-3295-334b-a801-00fbd1006ad5 | -4.4073 | -48.9474 | 2025-11-05 03:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 156.4 |
| a8244b03-502a-35e6-a8e7-14df708e599e | -4.7668 | -42.6572 | 2025-11-05 03:50:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| b4582fcd-dc8e-36a7-9b1e-8e43e2e4f8a4 | -5.4707 | -43.5674 | 2025-11-05 03:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 39870bc0-b252-3a05-9d82-52d25cd2fc22 | -4.4633 | -43.2152 | 2025-11-05 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 908a7328-e66d-3271-bf88-ee82e284736d | -4.4446 | -43.2164 | 2025-11-05 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 5e74ba5a-9768-3c30-89a2-e13a63ac42df | -4.4075 | -48.926 | 2025-11-05 03:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| a2906c10-3c88-3576-a420-360d7e1115ff | -2.6508 | -48.52 | 2025-11-05 03:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 0cce4665-18ca-3540-af12-61b81514e8eb | -4.4632 | -43.2386 | 2025-11-05 03:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 5a93cb19-18f8-30b3-a63b-c016ef8f3bfb | -5.0399 | -43.6205 | 2025-11-05 03:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 6ef4322a-2fc7-303a-9c35-af0f5dec6d0a | -5.4705 | -43.5906 | 2025-11-05 03:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| d7be1fc7-5297-3001-b149-40cfef239b64 | -4.4259 | -48.9465 | 2025-11-05 03:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 7d6a1634-eb02-37ba-9fa5-11efd3b62f96 | -5.45314 | -45.40119 | 2025-11-05 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 7b0a268d-eb55-3b0e-bbbd-e535552099ea | -5.03558 | -43.6253 | 2025-11-05 03:51:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 8e3927cf-c14f-3f77-93fb-b24a63d957d3 | -5.45834 | -45.40224 | 2025-11-05 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 2fffccdc-d5cd-34bc-b622-3d9a5753b95f | -5.1093 | -46.21675 | 2025-11-05 03:51:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d89fdb9-a993-3e98-a893-0e0540b632c8 | -5.51627 | -41.15379 | 2025-11-05 03:51:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a8b9bb43-1daa-3f09-a0ae-ed03b3fa2e33 | -7.52071 | -45.34813 | 2025-11-05 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdb74e87-f57f-348e-8a42-b9986cccc832 | -5.46048 | -47.41224 | 2025-11-05 03:51:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0732a1c7-fe20-31d0-847c-508a08f65578 | -6.11508 | -41.6388 | 2025-11-05 03:51:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 862a8f03-64c0-3142-905e-669b712a9fdd | -4.57433 | -43.33807 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9384aa30-2307-3810-8b3f-80617ab73e88 | -5.03642 | -43.62044 | 2025-11-05 03:51:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| f435cfc3-6e0c-3d51-9519-082f123f9185 | -6.10788 | -41.70528 | 2025-11-05 03:51:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 46d3877b-6db0-36a6-8dce-ff1018179463 | -3.6656 | -44.80138 | 2025-11-05 03:51:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b762cfda-1156-3b8d-b426-3e0e50d0181c | -4.85901 | -44.61639 | 2025-11-05 03:51:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| dead77fe-de06-3573-9c85-96d0e960c6fe | -7.8363 | -38.2416 | 2025-11-05 03:51:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 90eb4c4f-d10a-3f7b-8bb4-cfe81f09bd7d | -4.41731 | -48.94528 | 2025-11-05 03:51:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b23afebf-bb34-3df2-b5f0-42c9d48967e4 | -5.7841 | -40.81477 | 2025-11-05 03:51:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 7b8656ac-ebe0-366a-a6f4-a147c1d3d9f0 | -5.78026 | -40.81422 | 2025-11-05 03:51:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 271cf061-a507-322e-9812-5e23c91258d9 | -3.81797 | -48.66651 | 2025-11-05 03:51:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8164697-5cdb-30ac-81bf-3695fe2aec04 | -6.05158 | -43.0298 | 2025-11-05 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a01ff291-d2e2-3c88-8edc-de088306ac1e | -3.79473 | -44.041 | 2025-11-05 03:51:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c00c2f15-f0aa-34df-905f-82789ea15671 | -5.3213 | -41.23939 | 2025-11-05 03:51:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b09fadb7-4ca0-3431-9636-94bf0b64f1d4 | -5.92105 | -41.29751 | 2025-11-05 03:51:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8f3ed463-a429-3f17-906d-ca4c21360af0 | -6.10378 | -41.70109 | 2025-11-05 03:51:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 66aeedbe-89e2-3573-9a7f-eb9ec3a17729 | -4.86513 | -42.54171 | 2025-11-05 03:51:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9d35bff4-685b-3b0b-ae21-4ff6f895de82 | -4.30218 | -45.37563 | 2025-11-05 03:51:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa16b838-2ce9-3b79-a604-9565d7eb9887 | -7.28996 | -45.45197 | 2025-11-05 03:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ecc94d7d-b7c2-3bdd-b90c-0305c069c864 | -4.47186 | -43.22158 | 2025-11-05 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| f1d51717-602e-32f6-89b4-62a738c6c8d8 | -3.48632 | -43.63814 | 2025-11-05 03:51:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0d436cd5-b8fa-3aef-ac5a-ec27e58402f5 | -5.57618 | -37.89311 | 2025-11-05 03:51:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 628d2db1-215b-3a22-ac1e-64063c00b8ac | -5.03288 | -44.7938 | 2025-11-05 03:51:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 268da865-2aa6-35e8-af15-e3b01d0953ae | -4.82094 | -45.76715 | 2025-11-05 03:51:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d7e781f-dd2d-3039-b96f-c234ed66602c | -3.47759 | -43.63137 | 2025-11-05 03:51:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 534259b9-a567-3140-b473-41f900b3592e | -4.89337 | -46.85623 | 2025-11-05 03:51:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9e0897d5-0563-3ffc-9863-149ac7b1a662 | -6.12431 | -41.63306 | 2025-11-05 03:51:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5d49f5a4-a940-337e-80e9-cba6d02465db | -9.77607 | -43.61649 | 2025-11-05 03:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b287641e-63ea-3307-a856-ab7a41a17963 | -6.59115 | -44.6248 | 2025-11-05 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 02e75f05-39f7-3e9a-9eba-6774cb56fcb9 | -6.09516 | -41.70316 | 2025-11-05 03:51:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 325c4865-7ba8-3fe2-829d-5db2a0c53817 | -6.37177 | -42.41105 | 2025-11-05 03:51:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c7954854-1007-3433-b728-0280cbb9dc2d | -6.58593 | -35.25494 | 2025-11-05 03:51:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| caa4d144-fc32-356a-b0d5-bacee81fdb89 | -7.67339 | -47.42093 | 2025-11-05 03:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8bfb8ca-e05e-3613-ac9e-aa9c3de4cfa9 | -5.67761 | -44.74411 | 2025-11-05 03:51:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09d8ba18-c799-3769-aa70-e0833b5aa0a4 | -6.27536 | -42.56828 | 2025-11-05 03:51:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1a6aba77-dcca-33f2-a80b-af66b15f9b55 | -2.8498 | -49.41164 | 2025-11-05 03:51:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f31938e-d7c1-38ce-9ae0-0b5c68486e6a | -4.1158 | -48.02103 | 2025-11-05 03:51:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2e801aeb-1697-3892-9c30-3aeb5d7431fc | -5.07427 | -41.21341 | 2025-11-05 03:51:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 838dffe9-d679-3b32-b62a-2d60264e7d67 | -5.14944 | -41.21691 | 2025-11-05 03:51:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 0da50b9a-5b43-3c68-b23b-f6532e2eb1f7 | -7.78768 | -42.22457 | 2025-11-05 03:51:00 | NPP-375D | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7310a59c-f68d-3b78-8a38-83682aa840c4 | -4.63067 | -40.76746 | 2025-11-05 03:51:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 31d74462-70c8-38a2-80eb-177f5f86b48b | -3.23234 | -44.4002 | 2025-11-05 03:51:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a919df7f-b12f-3eaa-bf92-2b50728e05b5 | -7.28379 | -45.45705 | 2025-11-05 03:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4e69d017-c5f2-3bb0-b105-f104a9832ef2 | -5.24356 | -48.50254 | 2025-11-05 03:51:00 | NPP-375D | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e2607a37-5188-3aa3-8595-2e777a2eb5c5 | -7.54598 | -45.85133 | 2025-11-05 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 08d03267-6ea1-36a6-96c2-86db451babf0 | -2.6576 | -48.50494 | 2025-11-05 03:51:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c3dffc6d-de2e-3516-8e94-6c709874e63f | -8.94947 | -40.83626 | 2025-11-05 03:51:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b9088699-ce86-37d6-8865-3cb730735807 | -4.864 | -44.61732 | 2025-11-05 03:51:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5c4dcdf7-8e8e-3c62-b1b7-080bbe0ade95 | -6.13873 | -39.7645 | 2025-11-05 03:51:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4fb19ee4-49e1-31b4-b3ba-0559df86bde3 | -6.1754 | -40.66573 | 2025-11-05 03:51:00 | NPP-375D | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2982a871-29c2-31b8-8a87-f70e0772d218 | -7.93972 | -49.73911 | 2025-11-05 03:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88c62ae7-5802-3a7c-9dd5-411d9a180b0e | -3.23905 | -46.88059 | 2025-11-05 03:51:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 0d313e87-aea6-3623-bc3f-4e5d04b43e11 | -7.72364 | -45.81791 | 2025-11-05 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ac90cd5-50e0-33f3-85ed-8ecb94ee6ac8 | -6.45147 | -39.11215 | 2025-11-05 03:51:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 409b520f-e258-3299-8ff2-4c229507a29c | -2.81888 | -45.15386 | 2025-11-05 03:51:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| f29e7626-7bd9-32d9-b1c3-d15fac76393b | -6.52733 | -39.69069 | 2025-11-05 03:51:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2e8c83cc-3bf3-3a35-b262-3741c85062be | -2.81942 | -45.15051 | 2025-11-05 03:51:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| e77932ed-c88c-3149-ad39-1dcb9e0db180 | -6.73285 | -44.15063 | 2025-11-05 03:51:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 15749ec4-2fb7-3ea1-8088-e23053263304 | -6.11449 | -41.64225 | 2025-11-05 03:51:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| df40d13c-8dc4-38c3-b2b7-712574cab29b | -8.67758 | -36.68867 | 2025-11-05 03:51:00 | NPP-375D | CAPOEIRAS | PERNAMBUCO | Brasil | 2603801 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 39caf8ce-c13a-3993-a40b-097e4844953b | -2.82148 | -45.15032 | 2025-11-05 03:51:00 | NPP-375D | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 19.9 |
| f9c2fb51-140b-3c17-9eb0-b29774b82bb6 | -7.54772 | -45.84179 | 2025-11-05 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed9ab46e-5aa4-33cb-bb22-b9cdd0f8082a | -4.63064 | -40.76931 | 2025-11-05 03:51:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 36cc1135-0075-38fb-9175-741e1893b26b | -6.74051 | -44.16246 | 2025-11-05 03:51:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c4afaf3-22b2-3c14-ad4e-3a01bb1b5b3d | -5.04109 | -43.62115 | 2025-11-05 03:51:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 877c2b19-e8b4-31f6-8ab2-46b5df33decb | -5.26939 | -44.14494 | 2025-11-05 03:51:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| daff7859-8e0b-3ef4-b99e-87161f82e13e | -8.67704 | -36.69218 | 2025-11-05 03:51:00 | NPP-375D | VENTUROSA | PERNAMBUCO | Brasil | 2616001 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6de94053-d507-3ca0-8bea-ee526bed00ee | -4.59691 | -45.62955 | 2025-11-05 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 390fe3ea-2862-39b3-9db3-9ae75b8d6bb7 | -2.73308 | -47.38556 | 2025-11-05 03:51:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84beffa5-34e8-362d-85cd-946df91e0cc0 | -4.552 | -45.58736 | 2025-11-05 03:51:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c953d60-1b18-32d5-963b-96f6127671ff | -4.81051 | -38.56773 | 2025-11-05 03:51:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 585df2d3-1a2a-3e59-ace7-16067f6a414c | -3.41492 | -44.43896 | 2025-11-05 03:51:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b39676c-d281-3f83-9c60-6306e59102f1 | -8.95335 | -42.66019 | 2025-11-05 03:51:00 | NPP-375D | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e1ad17ae-6993-35fb-bc9b-3baa63fee5fb | -5.5171 | -41.14877 | 2025-11-05 03:51:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |


[Clique aqui para ver as próximas entradas](README10.md)
