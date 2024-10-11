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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffb129db-1656-3880-bbe6-6749392db6e3 | -6.5437 | -59.991199 | 2024-10-11 00:46:44 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ff6d45e-e92f-3be5-8742-f9e53d354964 | -6.5478 | -60.010601 | 2024-10-11 00:46:44 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6facc674-f612-316f-93ed-697400bc4307 | -3.8064 | -47.7808 | 2024-10-11 00:46:44 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa063465-8811-3054-a5f0-32fbbb3ef8fa | -3.8085 | -47.789902 | 2024-10-11 00:46:44 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 388f86ec-1e21-3d3a-98a4-4fd821566c3d | -4.4363 | -50.533298 | 2024-10-11 00:46:44 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9954eb3a-f5e0-3086-a01f-238f870b8881 | -4.4379 | -50.540298 | 2024-10-11 00:46:44 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b3a56c3-1f80-3d44-a706-58cbd66452ef | -3.7967 | -47.783001 | 2024-10-11 00:46:44 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e565c5a-9a66-37fd-b505-f284e18ce337 | -3.9115 | -48.326 | 2024-10-11 00:46:45 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 162e53c4-2e71-3caa-8302-44257fda8ba1 | -3.9134 | -48.3344 | 2024-10-11 00:46:45 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b032dea-0462-3ebe-9815-f22f4a94a8e5 | -3.9153 | -48.3428 | 2024-10-11 00:46:45 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35c7d32d-00fd-390d-ad7d-9337619baa08 | -3.9036 | -48.3367 | 2024-10-11 00:46:45 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52e586f5-71b9-3ba8-b111-ad2422fd7d26 | -3.9055 | -48.3451 | 2024-10-11 00:46:45 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fda85779-01cb-3b9e-8a78-f3fad956a517 | -3.886 | -48.349499 | 2024-10-11 00:46:45 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ae8070b-6ee0-3d93-b011-839386905769 | -3.8879 | -48.357899 | 2024-10-11 00:46:45 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b2c4815-5acc-31e6-86fd-1be717fb80fe | -3.6991 | -47.5835 | 2024-10-11 00:46:45 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 464e4d11-4a93-3e0f-a985-55c1641f4284 | -3.7013 | -47.5928 | 2024-10-11 00:46:45 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48017904-daa7-3e73-aaee-6d1844571972 | -4.3452 | -50.494999 | 2024-10-11 00:46:46 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9dd8b48b-3497-3f21-9428-c229b885c269 | -4.3468 | -50.501999 | 2024-10-11 00:46:46 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c258c05-ecc1-39b6-b05a-db4d0137b982 | -4.3484 | -50.508999 | 2024-10-11 00:46:46 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ec9e3c6-90d1-3baa-8dc5-8f1c2575326c | -3.294 | -46.058498 | 2024-10-11 00:46:46 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b77674c1-9dee-3c85-877c-08638ac2ff97 | -3.2967 | -46.070202 | 2024-10-11 00:46:46 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f918d99d-c4fb-30dd-a10a-161e92b63eba | -3.2995 | -46.081902 | 2024-10-11 00:46:46 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d48bc5e5-e97e-3dae-98ad-5e71b72f629b | -3.3022 | -46.093498 | 2024-10-11 00:46:46 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9e92728b-c7b5-3067-9c8d-9059ca4d2131 | -3.7663 | -48.097801 | 2024-10-11 00:46:46 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06a1d70f-85c9-3a11-949f-03072c4fc792 | -3.287 | -46.072498 | 2024-10-11 00:46:46 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b63411db-911f-367b-be4c-04c40ff82bcc | -3.2897 | -46.084099 | 2024-10-11 00:46:46 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ccdaac31-6ecb-3362-a4e1-233d66d5e7ee | -3.9501 | -48.942799 | 2024-10-11 00:46:46 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73be6a23-5139-3d34-b08f-9e4892b96916 | -4.2727 | -50.948399 | 2024-10-11 00:46:48 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2447e5d-dd30-3095-84d6-d597a365d9b8 | -4.2743 | -50.955299 | 2024-10-11 00:46:48 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c3f21c9-299c-31f7-89fb-c14e9a349bca | -4.2758 | -50.9622 | 2024-10-11 00:46:48 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab255bf8-1d4e-3bb1-b973-a5c54bd59cbc | -4.2629 | -50.9506 | 2024-10-11 00:46:49 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddf02f86-ae10-3b79-b8ea-0b775565c33b | -4.2645 | -50.9575 | 2024-10-11 00:46:49 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98deac18-b901-35f5-b64b-cf09a9b50705 | -3.9314 | -49.853699 | 2024-10-11 00:46:50 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ea20151-643f-3b48-9397-f3cbc6378157 | -4.0828 | -51.019699 | 2024-10-11 00:46:52 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee15fd2a-fd59-32c3-8a77-1d5f03f4acfc | -5.1875 | -55.986401 | 2024-10-11 00:46:52 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a1e223d-752b-3fc7-b231-cd3fe6dfc0ad | -5.1756 | -55.9785 | 2024-10-11 00:46:52 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db5a916b-d7bf-334f-8c71-c0e75be7d1fd | -5.1777 | -55.988499 | 2024-10-11 00:46:52 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64ef86a5-8fbf-3a97-8ff7-d3350b232df4 | -4.0606 | -51.104 | 2024-10-11 00:46:52 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3bd4286-590e-348f-a319-94f767fafdea | -4.0622 | -51.110901 | 2024-10-11 00:46:52 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b3bb350-dcaa-3c50-932d-c8c5a761e72d | -4.0146 | -50.9916 | 2024-10-11 00:46:53 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 915113a5-1197-376b-8b4c-48ee5f470dc0 | -4.0161 | -50.998402 | 2024-10-11 00:46:53 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1811af25-3957-348e-a65f-74d0971d0fce | -3.6899 | -50.105801 | 2024-10-11 00:46:55 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f1a331c-334a-3e77-8477-520f921b6364 | -3.6916 | -50.112999 | 2024-10-11 00:46:55 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9912d31b-b123-378a-b197-a33720b72f5d | -3.6801 | -50.108002 | 2024-10-11 00:46:55 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fcc69a8-d8de-39e3-a3f2-ab57cb61f402 | -3.6818 | -50.1152 | 2024-10-11 00:46:55 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed7c5e2f-f563-3d7e-bf9c-465c03fe6000 | -3.9208 | -51.2145 | 2024-10-11 00:46:55 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ead86149-c202-38aa-99e8-61d9fafa210b | -3.9223 | -51.221401 | 2024-10-11 00:46:55 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 661bd6e7-1487-3800-811d-605add6b4b74 | -3.8454 | -51.245701 | 2024-10-11 00:46:56 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d078b70c-597c-3d2d-82e9-086e6f678b06 | -3.8469 | -51.252602 | 2024-10-11 00:46:56 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe11a860-4b20-3308-86a2-69a64bc76b7e | -3.2839 | -49.093399 | 2024-10-11 00:46:58 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bb59c6c-e2cc-308d-8876-2a6a39ddb564 | -3.2856 | -49.1012 | 2024-10-11 00:46:58 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fd86a47-418d-3be2-ba98-08df8b79a3d4 | -3.2722 | -49.0877 | 2024-10-11 00:46:58 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04e815c1-614f-30eb-b5e9-4ea57a71ee6d | -3.2741 | -49.0956 | 2024-10-11 00:46:58 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fce9a30-bd3d-3f0b-a030-eb771437244a | -3.2624 | -49.089901 | 2024-10-11 00:46:58 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7991fe2-21aa-3a52-b3d0-490d00644f59 | -3.2643 | -49.097801 | 2024-10-11 00:46:58 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65a20c05-c1ea-38c8-96a7-84ba8a252540 | -3.6795 | -51.059101 | 2024-10-11 00:46:58 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b99f67da-7666-3ebd-a0a7-c8063d90809c | -3.6811 | -51.066002 | 2024-10-11 00:46:58 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 321c3bb4-5f23-31d6-bec5-e4dd0f665f51 | -3.6826 | -51.072899 | 2024-10-11 00:46:58 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6b49a53-e180-3056-b8fb-436fc235ad3f | -3.6904 | -51.1073 | 2024-10-11 00:46:58 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57cbafbb-92d5-34fc-86d8-cc212239d611 | -3.692 | -51.114101 | 2024-10-11 00:46:58 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 450a6a1c-b3c0-3d90-9c47-bc66ab4ae719 | -4.2689 | -53.684299 | 2024-10-11 00:46:58 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed887cd9-39fc-331c-b4ec-bd94b9091252 | -2.9691 | -47.990398 | 2024-10-11 00:46:59 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61b6308b-3292-39b2-a7c0-9ff2f605e16f | -3.6805 | -51.109501 | 2024-10-11 00:46:59 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b355b0cd-474a-37e8-82de-2e4a4423a2cd | -3.6821 | -51.116299 | 2024-10-11 00:46:59 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef0a3fd3-1f58-336b-b049-969f7946c75c | -3.6723 | -51.1185 | 2024-10-11 00:46:59 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3ebf954-cd57-30af-bc9d-8624acd911e1 | -4.8049 | -56.204899 | 2024-10-11 00:46:59 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd1f7d34-5b28-3d82-a513-774d6aaf6825 | -4.7951 | -56.2071 | 2024-10-11 00:46:59 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbefb857-5b61-3a80-b914-0ac6e96efd53 | -3.4317 | -50.148602 | 2024-10-11 00:46:59 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 131f1377-be18-3a7f-9472-b95c4bf6b44b | -3.4334 | -50.1558 | 2024-10-11 00:46:59 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b440a1a9-61e0-3220-9d49-6e700c97e443 | -3.4236 | -50.158001 | 2024-10-11 00:46:59 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4853591-407b-3398-9793-c9120d4d52a8 | -3.8989 | -52.260399 | 2024-10-11 00:46:59 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08b1c49f-3641-3cbe-8d0e-9ad6a3a31306 | -3.9004 | -52.2672 | 2024-10-11 00:46:59 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecd01298-9ecd-39c7-983d-575cf67ec5f7 | -3.5396 | -50.8508 | 2024-10-11 00:47:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2193ff43-609e-3fd4-a289-4a1ca1c5b844 | -3.8627 | -52.2827 | 2024-10-11 00:47:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7427afb-454f-35f5-bbc0-d5c1ace72bc6 | -4.4749 | -55.077 | 2024-10-11 00:47:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d5e15a1-6f8a-3f3b-bd5c-560c84fd836f | -3.4615 | -50.597099 | 2024-10-11 00:47:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bf22fe0-b98b-3db4-b3bf-7a2e6099fadb | -3.7353 | -51.808201 | 2024-10-11 00:47:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd281a78-a38d-3aba-b8df-97cd49061b07 | -3.496 | -50.794899 | 2024-10-11 00:47:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47b27787-f007-3698-8caf-ac928d52ea20 | -3.8044 | -52.252399 | 2024-10-11 00:47:01 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e22771c-39be-3182-b982-ac52be326ea3 | -3.806 | -52.2593 | 2024-10-11 00:47:01 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b798385-c11d-3492-a9d8-46464c55153f | -3.3124 | -50.167801 | 2024-10-11 00:47:01 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8935b044-ad12-3301-b6b0-a6d5226382fa | -3.314 | -50.174999 | 2024-10-11 00:47:01 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4f9bc92-d442-3455-a266-05ce4c8a90ae | -3.2683 | -50.154999 | 2024-10-11 00:47:02 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc62d1c8-bb74-3cf8-90b3-6fedec1c9f36 | -3.2699 | -50.162201 | 2024-10-11 00:47:02 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98899de5-5a36-35d5-a057-5fb8c88ecf46 | -3.1264 | -49.6222 | 2024-10-11 00:47:02 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29aaf266-f162-3d3d-9e20-2124accf36a0 | -3.0575 | -49.365501 | 2024-10-11 00:47:02 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99a00817-86cc-3379-aa1f-79b1b393d764 | -3.5097 | -51.3564 | 2024-10-11 00:47:02 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 648d922c-4f2b-3f2c-af14-a6a0145919ab | -3.5112 | -51.363201 | 2024-10-11 00:47:02 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42776cc8-aaaa-34f7-abc4-764989710f28 | -3.5523 | -51.5909 | 2024-10-11 00:47:02 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 653b8b88-efb0-30bb-8dae-6b8e2b400490 | -3.7248 | -52.356602 | 2024-10-11 00:47:02 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40163925-84f6-3cd4-96eb-bd1259288e9c | -2.5315 | -47.206402 | 2024-10-11 00:47:03 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe500ba0-1533-37e0-a3d2-42cd5e5c76ae | -2.5338 | -47.216499 | 2024-10-11 00:47:03 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf7e6396-2c55-35d9-8567-7f6bd49109b6 | -2.5361 | -47.226601 | 2024-10-11 00:47:03 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d941cea-9e74-30fe-9d70-18d5ab3c72e5 | -3.472 | -51.372002 | 2024-10-11 00:47:03 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf73277d-6b51-39a1-9f09-cbc7bc7759ef | -3.3312 | -50.7952 | 2024-10-11 00:47:03 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d126aab8-b4c1-3df3-90c0-17871be15ac5 | -3.3327 | -50.802101 | 2024-10-11 00:47:03 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 489c86b8-b39f-3ffe-8404-b83ec9b2690b | -2.956 | -49.192001 | 2024-10-11 00:47:03 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bab9634c-f8bf-383d-9f0a-4a64542fa968 | -2.9578 | -49.199902 | 2024-10-11 00:47:03 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfc94e50-cbec-39f5-a9b7-6bec82f52630 | -2.9596 | -49.207699 | 2024-10-11 00:47:03 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5accaea-9ccd-3a96-b501-1bd0bb24d6f3 | -2.8788 | -48.898998 | 2024-10-11 00:47:03 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README12.md)
