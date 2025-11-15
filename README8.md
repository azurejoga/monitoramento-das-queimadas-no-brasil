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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94a5b7e2-021a-392f-9cb4-350a98bbf569 | -9.4884 | -47.277599 | 2025-11-15 00:18:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5bd017fb-9e7b-3c0e-80f1-041db8430623 | -8.8931 | -47.888199 | 2025-11-15 00:18:00 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 975a6c82-561a-3989-82cb-a32e71b9b109 | -4.0717 | -44.131599 | 2025-11-15 00:18:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c5b2d7a2-3ebd-3ac6-83eb-50d006866989 | -5.5279 | -43.194 | 2025-11-15 00:18:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8e468412-88f2-3325-9e71-75a6f65cdbaa | -9.8556 | -44.181702 | 2025-11-15 00:18:00 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 93a1d888-576c-3bc2-9ccf-93f86d2241d2 | -3.3736 | -47.188499 | 2025-11-15 00:18:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02dc90f7-00db-3030-8855-ea1d32fe5fe7 | -4.2611 | -46.840099 | 2025-11-15 00:18:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4d2c5bef-71d8-3658-9f29-2df15fcc3834 | -7.868 | -48.393101 | 2025-11-15 00:18:00 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32104eca-c1fc-3a2b-89ac-bbb31c134346 | -4.5742 | -45.122299 | 2025-11-15 00:18:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 89eb1b8b-d97c-31a4-b221-b60d5e329179 | -3.1181 | -45.285099 | 2025-11-15 00:18:00 | METOP-C | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 53a1907c-bd2c-34bd-968d-48b933d40261 | -7.8735 | -48.4189 | 2025-11-15 00:18:00 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a776e366-8612-3f31-81e6-c1b528d66cae | -10.3484 | -48.7145 | 2025-11-15 00:18:00 | METOP-C | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0a3369a1-fbda-30d7-a269-c25ee132a078 | -4.7528 | -44.955898 | 2025-11-15 00:18:00 | METOP-C | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 12426f80-151b-32e7-bf2e-42a0239633dc | -7.9799 | -35.219299 | 2025-11-15 00:18:00 | METOP-C | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6aa01f93-14ad-325a-9132-d0bd4b55357a | -12.6176 | -42.392502 | 2025-11-15 00:18:00 | METOP-C | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 361ce7dc-df2a-3bb0-88e1-dcb5c8166af9 | -4.0993 | -47.999298 | 2025-11-15 00:18:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4cc7964-5f01-3c3b-b624-35a0db892d38 | -4.5193 | -43.2352 | 2025-11-15 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 05295b99-391e-3406-afa9-b67e5b040fac | -11.8677 | -49.2195 | 2025-11-15 00:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 1b6d551a-b6df-3d3a-a556-944595b07030 | -6.1606 | -48.0507 | 2025-11-15 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| d82d5952-ec4e-3e85-a9be-88a07fcc5a3c | -2.5239 | -47.7899 | 2025-11-15 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 68764437-aa69-3544-8f18-2b154203d05e | -2.7374 | -45.2877 | 2025-11-15 00:20:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 83.0 |
| b365c035-7ae1-330d-9a50-65cb40c4e9de | -11.8299 | -49.2024 | 2025-11-15 00:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 7d44b3c2-3509-35d1-b9a0-6a9e34981af7 | -2.5238 | -47.8115 | 2025-11-15 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 149.7 |
| 7e322039-4589-3ff4-a0fb-ad1318ef43dd | -4.5383 | -43.1874 | 2025-11-15 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 24cbeb7b-f368-379e-ad10-e1da7840ced6 | -11.8486 | -49.2218 | 2025-11-15 00:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 203.6 |
| 371cbf50-2f7a-36c4-a54a-041c51020dba | -3.2198 | -45.4724 | 2025-11-15 00:20:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 5d129007-0bf1-3265-9140-4ded0b044f6a | -2.5054 | -47.7904 | 2025-11-15 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 53ed0a8a-c22c-35b6-89d2-8117f9b114b4 | -12.7532 | -43.6487 | 2025-11-15 00:20:00 | GOES-19 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 3e5871e6-d228-31af-bb2f-ba651a1c03a9 | -3.2756 | -45.4702 | 2025-11-15 00:20:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 67fa3183-f766-3b66-9fda-052adeb8bad7 | -11.8681 | -49.1976 | 2025-11-15 00:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 4d088b90-bd31-3539-ac19-b709b471cc2c | -11.8295 | -49.2242 | 2025-11-15 00:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 976ccc52-2236-362d-a7ef-518e23de2d5c | -5.221 | -44.346 | 2025-11-15 00:20:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| b6f93a10-4e5a-3b91-ac71-25667cb7c8cd | -4.5567 | -43.2329 | 2025-11-15 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 292.2 |
| c82337e6-17ca-3e87-84b6-0151a16a5bfc | -8.5792 | -46.0794 | 2025-11-15 00:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 253.8 |
| dd960cb3-2654-3881-990a-4b1b7bbfc327 | -2.5053 | -47.812 | 2025-11-15 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 143.7 |
| c1f6abee-0992-3357-bebe-868eba5a6659 | -8.5984 | -46.0549 | 2025-11-15 00:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 6a709c3e-3f36-3a95-b280-b262966fdca5 | -2.7374 | -45.3102 | 2025-11-15 00:20:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 1e565986-9e65-384e-8d45-17e05c90c856 | -8.5981 | -46.0774 | 2025-11-15 00:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 384.6 |
| 179ee715-c1a1-3ec6-aabf-9edbf9a77540 | -4.5568 | -43.2096 | 2025-11-15 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 674.3 |
| 9ce9a779-08eb-3cd3-b58e-97fccc4614c3 | -4.5194 | -43.2119 | 2025-11-15 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 164.4 |
| 1fded349-6553-325c-8653-6ee54adf8e45 | -4.557 | -43.1862 | 2025-11-15 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| cab28309-26af-30f3-b083-f52e433ee9ad | -8.5795 | -46.0568 | 2025-11-15 00:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 411f476c-bd03-3317-964c-86567e7a51bc | -13.8927 | -42.8932 | 2025-11-15 00:20:00 | GOES-19 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 107.6 |
| 96b9646b-80de-375c-a4b2-74a95632c393 | -7.9913 | -35.2159 | 2025-11-15 00:20:00 | GOES-19 | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 62.6 |
| 6cd79c0b-bba2-3405-9868-35dca893e710 | -5.2397 | -44.3448 | 2025-11-15 00:20:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 239.9 |
| cca6259f-8a4f-32d7-9866-07658d940dcc | -7.8947 | -48.3963 | 2025-11-15 00:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| a4efc7e9-d35b-3029-8ba1-9d7bd561f79c | -5.2396 | -44.3677 | 2025-11-15 00:20:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 57ec3477-1182-381c-99b5-78d3ca1473e1 | -12.6745 | -46.7605 | 2025-11-15 00:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 19e5769a-1552-3d0e-9e29-ed35a6d5ba56 | -7.8759 | -48.3979 | 2025-11-15 00:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 6e62d008-6de7-336b-a1f8-254d32da19b0 | -4.5862 | -44.3172 | 2025-11-15 00:20:00 | GOES-19 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 998359ab-5457-32be-907a-3cacab0f917a | -4.538 | -43.2341 | 2025-11-15 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 411.3 |
| f3a2e91b-98de-34de-9359-00c4624b1ae3 | -11.849 | -49.2 | 2025-11-15 00:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 218.0 |
| 73b33bca-c57c-357f-97f6-272e9f285308 | -4.5381 | -43.2107 | 2025-11-15 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1027.4 |
| ee2c4610-c81b-3243-aad0-738a77935374 | -8.5792 | -46.0794 | 2025-11-15 00:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 369.5 |
| 2495b97f-5b71-321f-bf04-c50590218d55 | -12.7532 | -43.6487 | 2025-11-15 00:30:00 | GOES-19 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| ba97ca4a-48f1-3c5c-803d-8809d32907e5 | -8.5978 | -46.0999 | 2025-11-15 00:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 539f75ee-9089-3b15-8873-a06c6db47076 | -8.5984 | -46.0549 | 2025-11-15 00:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 161.7 |
| b4b407ff-870d-3a1c-b60e-3be80715e424 | -5.2397 | -44.3448 | 2025-11-15 00:30:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 217.2 |
| 0bdafc63-79e8-3ee6-bfaa-a098119bbc96 | -8.579 | -46.1019 | 2025-11-15 00:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 39c1ecad-6100-306a-87ae-2a408f832562 | -8.5981 | -46.0774 | 2025-11-15 00:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 399.2 |
| 921b2de0-c303-308a-8d09-2a79948456cf | -13.8927 | -42.8932 | 2025-11-15 00:30:00 | GOES-19 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 82.2 |
| 849fda55-0dc4-3c69-b9fb-086630f5579d | -2.5238 | -47.8115 | 2025-11-15 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 943021cb-df0e-3f24-86c8-232833c919a6 | -3.2756 | -45.4702 | 2025-11-15 00:30:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| d346ecde-4e4a-397f-9ece-53d22835a763 | -5.2396 | -44.3677 | 2025-11-15 00:30:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 2565bf7e-5aa3-37ed-9065-6df4e5ef9e30 | -11.8677 | -49.2195 | 2025-11-15 00:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 16365188-c44a-32c1-aae8-96708781dcea | -11.8295 | -49.2242 | 2025-11-15 00:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 69cbcc0f-7ee8-389b-a4b7-1c27b6e2c2eb | -4.5568 | -43.2096 | 2025-11-15 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 392.7 |
| 528aec18-8e65-3ac2-88e7-d92e297bd99a | -2.7374 | -45.2877 | 2025-11-15 00:30:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 92.6 |
| f0ad2cfa-4b03-37b8-9b4a-8e88e963daec | -4.5381 | -43.2107 | 2025-11-15 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 956.5 |
| 95b25325-3d49-3fab-9b1d-c5f466cf242b | -2.5053 | -47.8337 | 2025-11-15 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| d17106fe-6f41-36c4-9367-0f016cbcaa14 | -4.557 | -43.1862 | 2025-11-15 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 948a18c6-0934-39ee-8baa-d90e78799823 | -6.1606 | -48.0507 | 2025-11-15 00:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| c02122fb-f5a9-3614-bbb2-0422ed06c436 | -2.7374 | -45.3102 | 2025-11-15 00:30:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 76fe344c-dc36-3ff7-985f-59a91c08ead5 | -7.8759 | -48.3979 | 2025-11-15 00:30:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 9f030f01-d47d-3f29-8869-0bd2b2d588d2 | -4.538 | -43.2341 | 2025-11-15 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 472.8 |
| 0749152d-6792-3546-ad0a-7f90138d9d38 | -7.8947 | -48.3963 | 2025-11-15 00:30:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 85147dc4-3129-38aa-826f-e106058c8af9 | -12.4815 | -43.7415 | 2025-11-15 00:30:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 35ce4e0a-6a18-3313-be19-2d8aa6b9edd5 | -8.5795 | -46.0568 | 2025-11-15 00:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 158.3 |
| 7293dad6-06e7-3fa5-a47e-53f668a45521 | -4.5567 | -43.2329 | 2025-11-15 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 195.4 |
| fa35cb70-4cb7-31c2-9a2c-abf73784c181 | -11.8299 | -49.2024 | 2025-11-15 00:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 96ef7931-974f-3bec-9ea6-0e615d467d22 | -5.221 | -44.346 | 2025-11-15 00:30:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 35a4c5f3-dd20-3e55-ae37-2f310fd840d8 | -4.5383 | -43.1874 | 2025-11-15 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 141.5 |
| d4a24618-e859-34d2-8a8c-0c253391bd9a | -4.5194 | -43.2119 | 2025-11-15 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| b9f26832-fd79-3654-b63a-6674f78fe160 | -3.2198 | -45.4724 | 2025-11-15 00:30:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 72ff1bfd-780e-35d6-a693-81d21ed89928 | -12.6745 | -46.7605 | 2025-11-15 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 154e8ed7-5732-3b07-a40e-27bd07941852 | -11.849 | -49.2 | 2025-11-15 00:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 58de083c-d25f-36e9-8375-94b070a243d0 | -2.5053 | -47.812 | 2025-11-15 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 169.7 |
| c1d75c3e-b3af-34aa-a252-95af37fe64a9 | -11.8486 | -49.2218 | 2025-11-15 00:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 229.4 |
| 90d474ac-9840-3fc5-a65a-d0660b05dc27 | -11.8486 | -49.2218 | 2025-11-15 00:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 233.8 |
| 625bf1e4-2eff-3192-9d26-a7f6cd255cdd | -4.5383 | -43.1874 | 2025-11-15 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 883d5444-0b92-3c51-a626-8999d4ee5efd | -4.5381 | -43.2107 | 2025-11-15 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 784.6 |
| 8a57db2a-ac59-3921-bcab-ed51596f25fd | -8.5795 | -46.0568 | 2025-11-15 00:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| fbaeb7f8-3d0a-30f9-9e6f-61922b243302 | -4.5568 | -43.2096 | 2025-11-15 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 273.5 |
| 0a41612d-2323-3518-a1b9-1c3c3c502b79 | -11.849 | -49.2 | 2025-11-15 00:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 181.1 |
| dfcf33a9-7837-3cb9-9e58-fd6da158e432 | -3.2198 | -45.4724 | 2025-11-15 00:40:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 2e905372-9d0f-3c49-8f8a-fc5bb3d9b4ad | -8.5792 | -46.0794 | 2025-11-15 00:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 203.6 |
| 2576f192-83fa-3956-8580-3104a6a6e1c4 | -4.5567 | -43.2329 | 2025-11-15 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 2d74ca61-44b7-33c9-a64e-26db45f4875c | -11.8295 | -49.2242 | 2025-11-15 00:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| b24c74c8-d6d5-343e-8c99-4d5bbf6ba337 | -12.6745 | -46.7605 | 2025-11-15 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 583094ee-9dc5-301e-a231-d50ac4951779 | -6.5631 | -51.1126 | 2025-11-15 00:40:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |


[Clique aqui para ver as próximas entradas](README9.md)
