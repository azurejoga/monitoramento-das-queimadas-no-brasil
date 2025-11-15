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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa867d29-a94b-3b56-9f04-d85a486e6c03 | -17.575 | -46.6923 | 2025-11-15 00:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 1272ed1f-ae3c-3cfc-9090-289073cfccf1 | -2.7374 | -45.2877 | 2025-11-15 00:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 486659e5-8b3d-36d8-8288-51d136bfcb0a | -17.5756 | -46.669 | 2025-11-15 00:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 77.4 |
| e9d8925c-f1b6-3345-a2d6-7baf3224d388 | -7.8947 | -48.3963 | 2025-11-15 00:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 8a42b585-7fe2-39fe-9a3b-47a47a59e418 | -4.5567 | -43.2329 | 2025-11-15 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 332.7 |
| 010b88af-36c2-319f-8559-93aac5aab0e5 | -4.5194 | -43.2119 | 2025-11-15 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 473a9e2c-cc49-3a9f-8a96-36569b924b5a | -4.5568 | -43.2096 | 2025-11-15 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 584.2 |
| 82fb0284-9f17-3e27-9bb3-965716813795 | -5.221 | -44.346 | 2025-11-15 00:00:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 129.7 |
| ccad7d6b-62cd-32dd-952f-e4f1452a1cb2 | -11.849 | -49.2 | 2025-11-15 00:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 207.3 |
| 8e348d3c-f1a8-3b2c-9711-db3ad376fc1d | -3.2942 | -45.4695 | 2025-11-15 00:00:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 4652731d-b1f8-3c04-b8b7-14448d399d8e | -2.5053 | -47.812 | 2025-11-15 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 194.4 |
| d434d296-dd73-35eb-b68c-02272bafc51f | -11.8486 | -49.2218 | 2025-11-15 00:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 272.3 |
| 39954fcc-7d69-3a03-8292-eebd23488a97 | -13.8927 | -42.8932 | 2025-11-15 00:00:00 | GOES-19 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 81.7 |
| 4d761f6d-bb55-304a-8222-8db95ba09261 | -6.1606 | -48.0507 | 2025-11-15 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| af5c9464-708e-3344-84c4-8b0212cd25ac | -11.8677 | -49.2195 | 2025-11-15 00:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 6c8d9dd8-2e32-327d-9e96-44fb5525fb02 | -4.5193 | -43.2352 | 2025-11-15 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 972796ce-7034-39c0-9f67-0fbb3a89a845 | -11.8299 | -49.2024 | 2025-11-15 00:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| faf2a0c2-14c4-39f0-9a38-fea2ab0fc510 | -7.8759 | -48.3979 | 2025-11-15 00:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| e0dee3e3-0277-3579-8782-809d73bbed69 | -4.5383 | -43.1874 | 2025-11-15 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 190.2 |
| 2c8b553d-ca0f-3240-8ca3-d31c15dc2ab9 | -11.8681 | -49.1976 | 2025-11-15 00:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| a409143e-ee7d-326e-9c11-7a10a5b9b338 | -3.7103 | -47.6185 | 2025-11-15 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 29cdf70b-76e9-3d47-83d4-dd38d4fff248 | -5.2397 | -44.3448 | 2025-11-15 00:00:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 222.6 |
| 20fa0903-bdcc-3707-a958-141216304d6d | -12.6745 | -46.7605 | 2025-11-15 00:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| be889553-8406-3f03-9db1-8e6bbff76baf | -3.7101 | -47.6403 | 2025-11-15 00:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 2c3e46b1-8d37-3cf7-b02e-1b7608471319 | -3.2756 | -45.4702 | 2025-11-15 00:00:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 102.9 |
| d7526829-08bc-3837-a198-2a20a46ea776 | -2.5238 | -47.8115 | 2025-11-15 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 177.6 |
| 4d490f12-b7f6-3200-bb73-00e0c522c589 | -5.2396 | -44.3677 | 2025-11-15 00:00:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 4169fce6-fbc0-30e3-9136-e5e80a6e4ee6 | -2.7374 | -45.3102 | 2025-11-15 00:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 246f703c-a217-3d40-a4c9-a6fdfa9da27a | -12.7532 | -43.6487 | 2025-11-15 00:00:00 | GOES-19 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| b555f1ea-c354-3843-8016-1fe92238030b | -17.0254 | -43.3703 | 2025-11-15 00:00:00 | GOES-19 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 94.9 |
| ab899b22-2da9-35a4-b492-347057cdfd1e | -11.8295 | -49.2242 | 2025-11-15 00:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 4c5d5e89-3424-3fe8-bd56-3b33e71a9277 | -13.9122 | -42.8895 | 2025-11-15 00:00:00 | GOES-19 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 60c51f52-16c0-3807-ad33-89775c70cdac | -4.557 | -43.1862 | 2025-11-15 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| b6b023f7-9581-3962-af89-703398fa89e8 | -11.1802 | -48.1438 | 2025-11-15 00:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| d009e75d-ef4f-39d3-93f0-4f8421f284a1 | -4.1117 | -45.6122 | 2025-11-15 00:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 40f6cb8b-6a5b-3fc7-bdac-d316ee3a3874 | -5.2209 | -44.369 | 2025-11-15 00:00:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 9987595f-1fdb-3644-8875-9658bf9b58d4 | -4.5381 | -43.2107 | 2025-11-15 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1417.0 |
| 25b71d22-03b5-36a7-9c67-ec70afbf6abb | -4.538 | -43.2341 | 2025-11-15 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 767.3 |
| f8e1607b-0ef9-3346-9717-200be86d7d14 | -13.9122 | -42.8895 | 2025-11-15 00:10:00 | GOES-19 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 6e7ea88c-8b5b-350f-bcf2-233917823ae1 | -8.5792 | -46.0794 | 2025-11-15 00:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 197.6 |
| c00a67db-b825-3948-a488-83d71fbe8042 | -7.8759 | -48.3979 | 2025-11-15 00:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 60500390-622d-3118-93e4-30a5b443b938 | -5.2209 | -44.369 | 2025-11-15 00:10:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 940f3837-17de-3fa2-92a9-603b7cf87ba1 | -5.221 | -44.346 | 2025-11-15 00:10:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 99cd94d2-6f36-3a5f-809c-276a6584cefc | -8.5795 | -46.0568 | 2025-11-15 00:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 6c970cd5-9265-3bef-b84a-1260a48aaab6 | -2.8671 | -45.3732 | 2025-11-15 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 83.7 |
| e96e21b1-b1cd-361a-844d-53905d963f7f | -4.5381 | -43.2107 | 2025-11-15 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1173.3 |
| ade4359d-e532-3d69-838f-8c528c34fd50 | -2.5054 | -47.7904 | 2025-11-15 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 682b4f81-41a4-309b-bc78-c22e94e29e36 | -12.4622 | -43.7447 | 2025-11-15 00:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 42.3 |
| fde6e28f-d280-3b6f-ac18-f904c73c5af7 | -8.5984 | -46.0549 | 2025-11-15 00:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 4564fd6f-1d89-3b46-8ead-3dbd4e2a5225 | -11.8681 | -49.1976 | 2025-11-15 00:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| a4a197d8-9ae6-3fc2-a02f-c9e9c41db4c2 | -4.557 | -43.1862 | 2025-11-15 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 2ce91bc1-0094-3174-a81b-d71c58e4a0af | -11.8677 | -49.2195 | 2025-11-15 00:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 68e17b58-8c9c-3779-bd12-3e6cc1362305 | -3.2942 | -45.4695 | 2025-11-15 00:10:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 6afc9f47-3f90-3833-a563-63fb66c2d854 | -2.5238 | -47.8115 | 2025-11-15 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 148.1 |
| fbd7bebc-5a23-3800-9ef7-1fc9aba0ce86 | -4.5567 | -43.2329 | 2025-11-15 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 242.4 |
| 9edf5e96-4367-33b2-ad9e-81d45400ff2d | -3.2198 | -45.4724 | 2025-11-15 00:10:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 8fe1de10-2af4-38c4-92cc-afd9a5e480f6 | -12.4815 | -43.7415 | 2025-11-15 00:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 5b13976c-bbda-3c93-aa4d-0f6f9a91ac6a | -13.8927 | -42.8932 | 2025-11-15 00:10:00 | GOES-19 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 80.6 |
| c330b5d1-95e3-3971-b31b-fcd6acc86f63 | -11.8486 | -49.2218 | 2025-11-15 00:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 240.5 |
| 5f13d12d-d8e0-35de-9a22-ed81d3a537e5 | -2.8672 | -45.3507 | 2025-11-15 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 6cb45792-310d-3922-90b0-04491156fb23 | -11.8299 | -49.2024 | 2025-11-15 00:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 26580013-a179-36c5-a9de-3bc7fc687c00 | -2.7374 | -45.3102 | 2025-11-15 00:10:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 7064484f-4def-3911-b3a7-be8429042517 | -2.5239 | -47.7899 | 2025-11-15 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 4ff0edde-fa6c-36e2-930a-34142a9253d9 | -7.8947 | -48.3963 | 2025-11-15 00:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 22e17aca-d0d3-3154-bb5e-2edb26d8e4f3 | -5.2396 | -44.3677 | 2025-11-15 00:10:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 47d1b11e-501d-379e-a9c4-f62c20e587e3 | -4.5194 | -43.2119 | 2025-11-15 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 139.5 |
| d2cc1821-8085-3a77-b11f-e3dce7fcf578 | -4.5568 | -43.2096 | 2025-11-15 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 529.8 |
| 86d24eff-162c-3f6d-8bab-8a4c0e253f40 | -2.7374 | -45.2877 | 2025-11-15 00:10:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 112.1 |
| c1f4a359-ad74-3b60-bbfc-2a7004319817 | -8.5981 | -46.0774 | 2025-11-15 00:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 127.7 |
| f967da25-c97d-367b-a057-568a9cb4b4b7 | -4.5383 | -43.1874 | 2025-11-15 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 01c7b9fa-661c-3205-891b-906878fe4935 | -5.2397 | -44.3448 | 2025-11-15 00:10:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 204.7 |
| 144a5a58-ba2f-3763-9294-74192f872d44 | -6.1606 | -48.0507 | 2025-11-15 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 6ebb0127-588f-3ef7-ac53-c16cc552bf78 | -11.8295 | -49.2242 | 2025-11-15 00:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 83319c9c-efc0-35cc-8810-487e362563bb | -17.5756 | -46.669 | 2025-11-15 00:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 1cb4697e-34f7-3d73-b952-052da16af03b | -11.849 | -49.2 | 2025-11-15 00:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 224.5 |
| 14f790a6-6e40-3625-bf2c-db8a4f75f643 | -4.538 | -43.2341 | 2025-11-15 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 589.1 |
| dc5ab1e4-2ed0-3315-8a18-8a7837574cc3 | -2.5053 | -47.812 | 2025-11-15 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 150.2 |
| 99f77f01-f18e-3fd2-9457-e810227882cc | -3.2756 | -45.4702 | 2025-11-15 00:10:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 7a36ef84-47b4-384c-b907-e0e22a8c93d3 | -12.4313 | -43.183998 | 2025-11-15 00:18:00 | METOP-C | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c613ab2d-9e8c-3d90-b133-56c9d2739a4c | -6.1031 | -41.606899 | 2025-11-15 00:18:00 | METOP-C | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 38c0373d-0298-334b-8345-34b2ce41ae70 | -4.662 | -45.055199 | 2025-11-15 00:18:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d30b7fed-eb39-3c44-8334-50c96db52449 | -17.5702 | -46.665501 | 2025-11-15 00:18:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 91970e21-85e2-3c80-b302-d604431c23f8 | -4.3986 | -44.073799 | 2025-11-15 00:18:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 013dd028-ccd1-387b-af5a-cf3c45b21607 | -12.9147 | -43.092999 | 2025-11-15 00:18:00 | METOP-C | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 65eeaca6-3773-3b84-9e67-2d3db6894ef1 | -4.6036 | -43.299099 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69a65648-9391-3dc3-8ca4-2a711e3ba7c0 | -4.5522 | -43.209702 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 67608269-1824-3b91-a831-7178ebb5f441 | -12.2288 | -49.395 | 2025-11-15 00:18:00 | METOP-C | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b03550ab-fe6b-3e20-bb56-f3a2a1ad7638 | -3.2134 | -45.478298 | 2025-11-15 00:18:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cef1077c-ab18-3092-91b8-02cb012e30cd | -4.2708 | -46.837898 | 2025-11-15 00:18:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ddc12fc1-eeb5-3776-8a2c-ca96162cc355 | -5.594 | -45.173199 | 2025-11-15 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e0e8d722-1d86-3f91-b814-86d54e5fbbbc | -3.9964 | -44.162998 | 2025-11-15 00:18:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5959a9aa-0002-36da-b274-3597046cd224 | -2.722 | -45.309898 | 2025-11-15 00:18:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cc90d8f5-86b6-3ff4-8091-1ab79a3d657a | -4.7309 | -47.150902 | 2025-11-15 00:18:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f9520c3f-c612-34c1-baf0-4ffa3862d859 | -11.3138 | -48.518002 | 2025-11-15 00:18:00 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 981c7daf-7658-3897-a197-96f7cdd5a7e7 | -10.7097 | -44.5205 | 2025-11-15 00:18:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 718029d9-b005-33dd-98cb-03ada052196c | -10.3044 | -44.591202 | 2025-11-15 00:18:00 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 66f0234b-6143-34af-b387-f446fd453d92 | -4.2214 | -45.4748 | 2025-11-15 00:18:00 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 18951d26-29e9-3667-be91-9bc0355258a8 | -6.0244 | -45.811501 | 2025-11-15 00:18:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fa3568c2-525a-3ebc-8073-d7f742af1403 | -4.5244 | -43.223099 | 2025-11-15 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28a1e7c6-29a0-3b08-bbbb-0375ac712366 | -15.4521 | -39.2314 | 2025-11-15 00:18:00 | METOP-C | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README2.md)
