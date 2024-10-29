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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55ac6897-958c-32cf-88a9-2d75f493d9e3 | -7.3341 | -43.574799 | 2024-10-29 00:27:14 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 985a9abc-b10e-3749-8b63-f5b581ac1962 | -7.3143 | -43.261101 | 2024-10-29 00:27:14 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 341af972-c8af-3240-91b5-6be803a8519e | -5.4287 | -35.560299 | 2024-10-29 00:27:15 | METOP-C | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| e5541bf3-6b17-31c9-a5ca-da76698d578b | -5.4327 | -35.576599 | 2024-10-29 00:27:15 | METOP-C | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 7770507b-621b-3bd9-b55a-4828850f189f | -7.3075 | -43.638802 | 2024-10-29 00:27:15 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 911d8e8d-c47e-3274-97a2-4c4c188307f2 | -7.8705 | -46.247299 | 2024-10-29 00:27:15 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 92bd6c29-ead4-30fe-94f7-81f00aecf9ed | -7.8724 | -46.255699 | 2024-10-29 00:27:15 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd1d53ed-95db-3c17-acb3-6f2bff4ba41b | -7.0232 | -42.619598 | 2024-10-29 00:27:16 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a6f0765d-575e-3dc2-bf3d-0177a0b8ac44 | -7.0247 | -42.626499 | 2024-10-29 00:27:16 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7e3f3ea5-0582-3430-a50f-3436814866bb | -6.9111 | -42.222401 | 2024-10-29 00:27:16 | METOP-C | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6f8812ea-85a2-391f-b334-46b83f3c0c21 | -6.9127 | -42.229301 | 2024-10-29 00:27:16 | METOP-C | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1bbd325d-6dd0-348c-9975-c1d37203f076 | -7.62 | -45.256401 | 2024-10-29 00:27:16 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2e0f08e0-bf24-30f1-a09d-928103bc417f | -7.6217 | -45.264 | 2024-10-29 00:27:16 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8308db17-e603-3d32-9fb7-2c8758ac437e | -7.6234 | -45.271599 | 2024-10-29 00:27:16 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3e90dd5f-6c71-3e14-9939-9a46efeeb35e | -7.4237 | -44.7925 | 2024-10-29 00:27:17 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5ee2ec75-3a50-301f-b009-587150f4da89 | -6.9453 | -42.7747 | 2024-10-29 00:27:18 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 10a4fd56-7aa5-36cf-bbd2-d6cde5698fdd | -6.9468 | -42.781502 | 2024-10-29 00:27:18 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e65fcea2-f091-3b30-a56c-7bb380fa8415 | -7.4155 | -44.801998 | 2024-10-29 00:27:18 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a7f6bd8e-c961-3c42-af07-5b74bf3e9974 | -7.4139 | -44.794701 | 2024-10-29 00:27:18 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 17fcd928-4a47-3bbf-99e8-920ffbb25ae2 | -6.8075 | -42.399502 | 2024-10-29 00:27:19 | METOP-C | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d7b2cb16-388b-36b1-9db2-f1a45cc908ca | -6.2792 | -40.613899 | 2024-10-29 00:27:20 | METOP-C | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d3fb22a4-939b-37c1-bb9f-ea9fb5a537c3 | -6.281 | -40.621799 | 2024-10-29 00:27:20 | METOP-C | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 34474c8f-7e39-3912-80e9-b24da6759ed4 | -6.6029 | -42.049301 | 2024-10-29 00:27:21 | METOP-C | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6d45e607-5ad3-3835-b562-edb9e72af3ed | -6.6045 | -42.056301 | 2024-10-29 00:27:21 | METOP-C | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 83c0d5f6-6cc1-326d-838c-230eb7393bd2 | -6.508 | -41.8624 | 2024-10-29 00:27:21 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 62077e69-5fa3-3b16-90d6-3c44660396a3 | -6.5097 | -41.869499 | 2024-10-29 00:27:21 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| db2c4670-68cf-31c2-ac3b-87205ac1bfdc | -6.8413 | -43.266701 | 2024-10-29 00:27:21 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c0e80f18-1f19-3cc2-8fd5-09ce1145477c | -6.8429 | -43.273602 | 2024-10-29 00:27:21 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 63346bbd-1639-353c-ad1d-001731a8e454 | -7.4049 | -45.6759 | 2024-10-29 00:27:21 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ac8c2a5-995e-3cd1-8200-2d647023b4a0 | -7.4067 | -45.683701 | 2024-10-29 00:27:21 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89d79ee7-6233-3563-9d4c-0112eabfecc4 | -7.3951 | -45.678101 | 2024-10-29 00:27:21 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a02a039d-f357-32d0-8261-44eceec3a06a | -7.3969 | -45.685902 | 2024-10-29 00:27:21 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a9c3f9c-5605-3f16-b71f-63e1258abdd2 | -5.936 | -39.463402 | 2024-10-29 00:27:22 | METOP-C | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b8d542ba-00e4-3962-866d-58a124405b35 | -5.9381 | -39.472401 | 2024-10-29 00:27:22 | METOP-C | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 0f9c8e52-b828-3165-bf4d-1b6413ed76b8 | -6.5926 | -42.2729 | 2024-10-29 00:27:22 | METOP-C | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 91dec03b-7030-33fe-9b9a-c1c2a1d5469a | -7.6151 | -46.859501 | 2024-10-29 00:27:22 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fb3d0d6a-094e-35dd-bf27-585283eecfbd | -7.6171 | -46.8685 | 2024-10-29 00:27:22 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2a781a4-7e05-304a-9f91-10e897d63f7c | -6.3678 | -41.569401 | 2024-10-29 00:27:23 | METOP-C | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 48150f09-fad7-3bed-af6e-e1575136f488 | -6.3695 | -41.576599 | 2024-10-29 00:27:23 | METOP-C | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 391b2f92-74c1-3c60-8708-38e193528491 | -6.358 | -41.571602 | 2024-10-29 00:27:23 | METOP-C | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3e48a157-1017-32fa-ba43-4d016cf99524 | -6.3597 | -41.5788 | 2024-10-29 00:27:23 | METOP-C | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4192fc42-f407-39c5-85c7-f41b94bd6ee1 | -6.49 | -42.185902 | 2024-10-29 00:27:23 | METOP-C | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fb3efafb-1254-3c6a-b7b7-659e67b5ac6f | -6.6338 | -42.765701 | 2024-10-29 00:27:23 | METOP-C | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c698c67c-d75d-34b9-8b46-51eb7917b48f | -6.6353 | -42.772598 | 2024-10-29 00:27:23 | METOP-C | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c6ece43f-7b55-30a6-b5e0-e57c2f713bd4 | -6.6369 | -42.779499 | 2024-10-29 00:27:23 | METOP-C | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ed1ee45b-fcc3-3370-b193-43e48685bfdc | -6.6385 | -42.786301 | 2024-10-29 00:27:23 | METOP-C | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d3ec3d1d-455d-3d8c-a65e-cb8b846a51d9 | -6.6401 | -42.793201 | 2024-10-29 00:27:23 | METOP-C | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 40151647-2e2b-3d6d-b396-dfae912441c2 | -6.6416 | -42.800098 | 2024-10-29 00:27:23 | METOP-C | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fc7e0103-47e1-3fef-b762-7a976a90e3b5 | -6.624 | -42.767899 | 2024-10-29 00:27:23 | METOP-C | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 180db8f4-3eac-3908-9657-86f81b2a8bac | -7.2261 | -45.519501 | 2024-10-29 00:27:23 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a19078c1-8eee-3e15-b63f-edc1afa5a2f8 | -6.3136 | -41.914299 | 2024-10-29 00:27:25 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cfee3c63-5a18-3b59-8e28-fdb76eea269c | -6.294 | -41.918701 | 2024-10-29 00:27:25 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a16449cc-5184-3d50-8224-38bf38fff3cc | -6.2957 | -41.9258 | 2024-10-29 00:27:25 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fe9e5248-b599-30b3-8505-8bde02d999ce | -6.2973 | -41.932899 | 2024-10-29 00:27:25 | METOP-C | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4bef349d-c2cc-3c16-b3c7-bbd815e4cc15 | -7.2656 | -46.066601 | 2024-10-29 00:27:25 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 369d82ac-43d4-378a-b0a4-caac77ca697e | -7.2674 | -46.074699 | 2024-10-29 00:27:25 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a6154505-b767-38e0-b726-47ac7400396a | -6.1648 | -41.8507 | 2024-10-29 00:27:27 | METOP-C | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c86c528c-5bd7-31a7-9b56-9611a5ac191d | -6.1665 | -41.8578 | 2024-10-29 00:27:27 | METOP-C | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ecdcc935-9eba-38e5-bfa6-7b0475441ede | -6.1681 | -41.865002 | 2024-10-29 00:27:27 | METOP-C | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9e6a5fd0-9981-398e-bd9b-f2c5bf166ba2 | -6.1567 | -41.8601 | 2024-10-29 00:27:27 | METOP-C | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 21519399-fdc5-38c5-95d4-a58b49385746 | -6.1583 | -41.867298 | 2024-10-29 00:27:27 | METOP-C | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 83956f79-f3ba-3dc0-84b1-d5e8b8ef5753 | -7.1874 | -46.316799 | 2024-10-29 00:27:27 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c2ed53b5-003b-34fc-84ac-e24efa9c2c39 | -7.1893 | -46.3251 | 2024-10-29 00:27:27 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 68929692-442b-3e5e-a656-1f7f03d910bc | -6.9545 | -46.100498 | 2024-10-29 00:27:30 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 021fefed-5a23-3df9-95ff-459f7138d2f2 | -6.9563 | -46.108601 | 2024-10-29 00:27:30 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26a5b5bd-2cc0-33ce-bfa5-826639c24424 | -6.8788 | -45.898701 | 2024-10-29 00:27:30 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b58c332b-c461-3a91-823b-534d102676e3 | -6.8805 | -45.906601 | 2024-10-29 00:27:30 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65db323a-8f0a-3232-b998-10dfa6b9960b | -6.4511 | -44.179798 | 2024-10-29 00:27:31 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d8e1ef0-630e-3877-94d6-83bc55f90905 | -6.4527 | -44.186798 | 2024-10-29 00:27:31 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f17696f0-003d-3ba7-8b86-ced616fab9d4 | -6.8386 | -45.9491 | 2024-10-29 00:27:31 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5542da01-981b-3faa-817b-4eb223ad52ed | -6.8288 | -45.951199 | 2024-10-29 00:27:31 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 430393fb-7602-3b13-8cc0-045cb3a5d940 | -6.0231 | -42.577599 | 2024-10-29 00:27:32 | METOP-C | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3ff4eb1e-1dfe-3ff6-b6cc-2fd00d561a93 | -6.2594 | -43.563202 | 2024-10-29 00:27:32 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| efa928f8-2a53-3921-93e1-c8d006a83c14 | -6.261 | -43.570099 | 2024-10-29 00:27:32 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6631ff4c-b86a-314b-b667-dae9b878b3cc | -6.8002 | -46.007599 | 2024-10-29 00:27:32 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 324c31a3-8250-3111-8df2-6f36ce1334b0 | -6.802 | -46.015598 | 2024-10-29 00:27:32 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e28eae67-ebb8-33b0-9b7b-fa16a7ddbe13 | -6.8038 | -46.023602 | 2024-10-29 00:27:32 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8158918a-7993-3682-aa48-227c05da4556 | -6.7904 | -46.0098 | 2024-10-29 00:27:32 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1bbd65e1-d047-38a7-b2ba-238bb49d2180 | -6.7922 | -46.017799 | 2024-10-29 00:27:32 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98e25099-de94-3ed2-abb9-cf2a90cd360a | -6.794 | -46.025799 | 2024-10-29 00:27:32 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1386fab9-dd13-35c5-9ac6-94da2cb8337b | -6.468 | -44.663898 | 2024-10-29 00:27:32 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a1e98b6-33e1-3cf2-961d-eb6b16431734 | -6.4696 | -44.671101 | 2024-10-29 00:27:32 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1cecb1c-41f0-3a81-ad90-c7add2e9b0e2 | -6.4712 | -44.6782 | 2024-10-29 00:27:32 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7e6502f7-0229-3e05-a682-e8507cc3dca5 | -5.8903 | -42.314899 | 2024-10-29 00:27:33 | METOP-C | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0066c367-0d30-3603-9e9a-612c9166d259 | -5.892 | -42.321899 | 2024-10-29 00:27:33 | METOP-C | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 72211a60-f541-32c6-9540-b5e4a4b76466 | -6.4582 | -44.6661 | 2024-10-29 00:27:33 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4326bca8-5bca-338f-bf4d-a31ebb9de4a7 | -6.4598 | -44.673302 | 2024-10-29 00:27:33 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a109e8b-7170-3fd6-9abc-29993f4b3cc6 | -6.4614 | -44.680401 | 2024-10-29 00:27:33 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c91e5ddd-85b5-38c7-9515-f36d29a24d2f | -6.9964 | -47.078701 | 2024-10-29 00:27:33 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f80eba54-1cd2-34ab-9cad-b8115c2cf81f | -5.4731 | -40.874001 | 2024-10-29 00:27:34 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| fd31da0c-7ec6-3f86-a031-456e48b1ced3 | -5.4749 | -40.881802 | 2024-10-29 00:27:34 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d1752bfc-6a5d-3612-b6e1-49bd4dfb024b | -5.9331 | -42.859001 | 2024-10-29 00:27:34 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cc6e31c4-3f34-3124-9d5f-682e9dd558ae | -5.6098 | -41.727402 | 2024-10-29 00:27:35 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2afbf67c-0d03-32d4-8683-05310abdc33f | -6.6668 | -46.377998 | 2024-10-29 00:27:35 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 95925b59-b67c-37cd-8007-d3e3a4256ae4 | -7.1061 | -48.375702 | 2024-10-29 00:27:35 | METOP-C | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6385821b-5980-32e7-bbc8-094983154d00 | -6.2008 | -44.5298 | 2024-10-29 00:27:36 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7251ad17-9071-33f8-9124-8c5403f77709 | -6.1369 | -44.293701 | 2024-10-29 00:27:36 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f31cf41c-0448-301b-a2b5-4030ee5e0068 | -6.1385 | -44.300701 | 2024-10-29 00:27:36 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d8073bb6-6f1d-3820-9359-be96b5920353 | -5.4138 | -41.416599 | 2024-10-29 00:27:37 | METOP-C | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c9118ddf-8139-33b7-915a-2d55bc9de13e | -5.9486 | -43.647301 | 2024-10-29 00:27:37 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
