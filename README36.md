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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cb8d6e7-64d7-301a-8eb2-66841e381990 | -5.6566 | -60.2284 | 2026-09-06 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 118.8 |
| ed847cda-fd4b-33bf-b982-e3a51e4ca680 | -11.2955 | -45.7087 | 2026-09-06 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 19e5ab2c-d588-3fbd-bb4a-e610bf7faace | -5.3462 | -56.0256 | 2026-09-06 13:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 74de2819-bf0b-3cd9-a5c3-982f8023702d | -7.1372 | -42.2484 | 2026-09-06 13:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 88.0 |
| d568de0d-4616-30c4-81b5-e9a51148cfb5 | -5.6565 | -60.2475 | 2026-09-06 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 151.3 |
| 488316e7-b78c-34c9-a1b9-ef80f76dff16 | -5.1439 | -55.9543 | 2026-09-06 13:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| c0df9b83-ce3b-34bc-899b-df8f1fae7d07 | -5.3645 | -56.0447 | 2026-09-06 13:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 06b807ce-97e3-3ee1-988f-43c2e4b506d1 | -7.137 | -42.2722 | 2026-09-06 13:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 79.6 |
| 3eae6a1f-86a6-392a-8058-b99991877a67 | -10.6731 | -50.4331 | 2026-09-06 13:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 4a7279fa-00d1-3cc1-b4cb-16c3ed63400b | -5.1623 | -55.9536 | 2026-09-06 13:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 2c67846b-1289-3707-a82a-584b40533f2e | -5.3645 | -56.0447 | 2026-09-06 13:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 6acb73e4-3381-3fc9-8f02-3e30cce60e2e | -5.3462 | -56.0256 | 2026-09-06 13:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 40ccb322-96b9-3f40-b51a-f556a7a83b1d | -5.1438 | -55.9741 | 2026-09-06 13:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| fbf1ef87-e4e9-30fb-b08d-a0b1e6440f96 | -7.1372 | -42.2484 | 2026-09-06 13:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| e2cf3f9f-5a8e-362a-9d97-60ac32049d66 | -11.3056 | -45.1113 | 2026-09-06 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| cc6a4bc3-f97e-3976-89db-68e173e2c03d | -11.2955 | -45.7087 | 2026-09-06 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 6223e9e4-1bb4-3480-a1d8-a5b5350b5f2b | -5.1439 | -55.9543 | 2026-09-06 13:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 2422f22f-6b32-3d67-96c0-91fe4ea7844c | -5.6565 | -60.2475 | 2026-09-06 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 141.2 |
| dff1ddda-8faa-3e62-a162-f43515293879 | -5.3646 | -56.0249 | 2026-09-06 13:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 337.5 |
| b3d7a0cb-5e08-31bf-a57b-647edb0ba543 | -11.2764 | -45.7113 | 2026-09-06 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| e3b8e976-4505-3738-b127-4ced5391cc7b | -11.2959 | -45.6858 | 2026-09-06 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| df09f4f5-b2f2-306a-be04-70bdfcb718ca | -5.6566 | -60.2284 | 2026-09-06 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| c704d38a-f596-3378-a42e-578d45b7af04 | -5.3647 | -56.0051 | 2026-09-06 13:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| f049ec27-0407-3d17-8aa3-905d83eef340 | -5.3462 | -56.0256 | 2026-09-06 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 54e2e434-56a3-3686-ae0a-95dd9a309a34 | -11.2864 | -45.114 | 2026-09-06 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| d3517dc3-fede-3b7c-b788-0d62fc04d717 | -5.1438 | -55.9741 | 2026-09-06 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 5124099b-71f3-34d7-aae1-3e3b1882d83a | -10.4023 | -46.8402 | 2026-09-06 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 2287b90f-4eb3-362c-8fe3-01e41dfa0e42 | -5.6565 | -60.2475 | 2026-09-06 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 169.0 |
| f3303f89-7054-3825-a564-494df0df6cf2 | -7.1372 | -42.2484 | 2026-09-06 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| b3c651d6-0ba2-3174-becb-db174243962c | -4.6651 | -56.0307 | 2026-09-06 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 36657cb5-6000-3e29-bd30-6c1a76c5e2f4 | -5.1439 | -55.9543 | 2026-09-06 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 38649c1e-45af-3506-9adb-c0a974124f59 | -5.6566 | -60.2284 | 2026-09-06 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 9ab00a57-5dd5-3408-9082-7cf9f3441b1d | -5.3647 | -56.0051 | 2026-09-06 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 787ff11e-9c42-3c78-bfb8-7c8d30f4f1df | -5.3645 | -56.0447 | 2026-09-06 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| c25fad13-1cb3-3b94-bb49-38cd206ae1a6 | -11.3056 | -45.1113 | 2026-09-06 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 3adbc594-eead-30d3-91a7-ed0f26ca2d98 | -5.1623 | -55.9536 | 2026-09-06 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 95ceb4ac-b7b3-381d-97e9-e55b6779a024 | -5.1423 | -56.2703 | 2026-09-06 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 2bec9f02-cf50-3e97-8d70-f04c50b92f18 | -5.6566 | -60.2284 | 2026-09-06 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 27dded8f-fe6a-3029-b880-5c00d231f464 | -5.4914 | -60.1953 | 2026-09-06 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| b9b79973-de5e-3bc2-9ac6-bfe21fcec94d | -5.1623 | -55.9536 | 2026-09-06 13:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 0c4bfa31-6904-3e55-b1f5-95abf4175df1 | -11.2864 | -45.114 | 2026-09-06 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 5482b3ea-6065-35ba-a27b-052d353e94ac | -7.137 | -42.2722 | 2026-09-06 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 78.5 |
| 1c49d5f8-77a9-3655-964e-7f6bac6e470d | -7.1372 | -42.2484 | 2026-09-06 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 94.9 |
| da1cc9de-6ace-3a76-9b0a-6e18133fcf11 | -11.3056 | -45.1113 | 2026-09-06 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 657ba529-2c84-33ea-ab86-fd7d31751ad9 | -5.5098 | -60.1947 | 2026-09-06 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| a755d109-888f-30fe-88b9-4f5d10b989ba | -5.3462 | -56.0256 | 2026-09-06 13:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 068e8c78-eaee-32e3-aae5-24da225cb43b | -5.3647 | -56.0051 | 2026-09-06 13:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| d352983c-cf92-382b-8d43-ab5038d51f7a | -5.1439 | -55.9543 | 2026-09-06 13:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 5f9b6cef-7d80-3b54-bac0-d2eff94f45c5 | -5.1438 | -55.9741 | 2026-09-06 13:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 65fccf97-68c5-3a69-8697-075edec9ad47 | -5.6565 | -60.2475 | 2026-09-06 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 186.7 |
| 0277040b-d10d-3f8a-82ec-701928692429 | -5.6566 | -60.2284 | 2026-09-06 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 141.0 |
| 7db915d6-0db3-3bbe-94e4-c3b6169fc24e | -6.6514 | -59.945 | 2026-09-06 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 4fb40438-e1dc-38e5-b422-7b4599203409 | -5.1423 | -56.2703 | 2026-09-06 13:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 44541cde-6844-3ffe-9cac-3420db1de491 | -5.6565 | -60.2475 | 2026-09-06 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 199.3 |
| c86816af-d736-3e09-ab59-8f271eea1807 | -5.3647 | -56.0051 | 2026-09-06 13:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| d137bc93-b13a-310a-b356-132b77c95e65 | -5.1439 | -55.9543 | 2026-09-06 13:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 123.6 |
| f8124c46-78d5-340f-9ddf-49d9e41115e7 | -11.2864 | -45.114 | 2026-09-06 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| bcaa6b06-54bb-3bc7-bc55-1446d0d3fa05 | -5.3462 | -56.0256 | 2026-09-06 13:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| e673897b-b9bc-37bd-abd0-ccdf7d92ddd6 | -5.1438 | -55.9741 | 2026-09-06 13:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 153.8 |
| 51223ac9-b066-39c8-afca-84e5f8d8c0ab | -5.4914 | -60.1953 | 2026-09-06 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 111.2 |
| e3f99756-3160-3b7a-b1b6-983de34a9a4f | -5.5098 | -60.1947 | 2026-09-06 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 4ff9fb5b-4f33-3859-b26f-770d5c43ed76 | -11.3056 | -45.1113 | 2026-09-06 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 2ff77099-ebe9-3814-84da-00c4731d148e | -5.6382 | -60.2289 | 2026-09-06 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| bb0f1bc4-a0c9-3a9a-a36e-f2828d4083d3 | -5.6566 | -60.2284 | 2026-09-06 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 77e262a6-8e5a-3457-8ff0-8d6d1efa8250 | -5.1623 | -55.9536 | 2026-09-06 14:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 8cf85b07-5664-36c0-a2ed-028109660c8e | -5.5098 | -60.1947 | 2026-09-06 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 4ec2ef52-98a7-336c-bd79-c3ef2fd71053 | -5.3462 | -56.0256 | 2026-09-06 14:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 2920b117-9b1d-3807-ab7e-475bb386585a | -5.4914 | -60.1953 | 2026-09-06 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 283.4 |
| e0937790-8b95-3578-b6d8-895c37d73d6d | -11.2864 | -45.114 | 2026-09-06 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| a41e2457-e311-3128-87ba-7c3fe964d27d | -5.3647 | -56.0051 | 2026-09-06 14:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| f0cd0274-9507-3754-9c81-8cc534b75fe1 | -3.7197 | -39.6278 | 2026-09-06 14:00:00 | GOES-19 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 94.0 |
| 075f3664-3798-3f95-93b1-144b38a1e547 | -11.3056 | -45.1113 | 2026-09-06 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 4aff84f4-8005-3319-8915-4f177cf66cd5 | -5.6565 | -60.2475 | 2026-09-06 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 51de49d2-d41e-306c-b1ff-12fcb80bdf9f | -12.1504 | -47.1283 | 2026-09-06 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| db1fcb07-83f8-387b-a620-2c39d140eed4 | -5.1439 | -55.9543 | 2026-09-06 14:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 69f075d6-7615-33c6-814a-1c7a0e263ed5 | -5.5098 | -60.1947 | 2026-09-06 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 140.1 |
| d938729a-30bf-369b-ac79-33a753912fe8 | -5.3647 | -56.0051 | 2026-09-06 14:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| bd3f8780-1c30-3031-82f9-db3e2c16602b | -8.9787 | -44.4183 | 2026-09-06 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 1c236283-4546-3a35-a001-7975d7d8a6b5 | -11.2864 | -45.114 | 2026-09-06 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| a42714f0-1380-3160-9f69-459603055c06 | -7.1372 | -42.2484 | 2026-09-06 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 100.9 |
| 70439d38-52c7-3fce-a608-642efd9a256a | -3.7645 | -61.7548 | 2026-09-06 14:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 7c9d4afb-6a5a-3b1c-9b23-aa4657e28be2 | -11.286 | -45.1371 | 2026-09-06 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 34dd5dd7-0539-3824-a691-f21f2adb9590 | -5.4914 | -60.1953 | 2026-09-06 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 260.5 |
| bca6a29c-2d11-3806-8432-f694dc779324 | -5.1439 | -55.9543 | 2026-09-06 14:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 5710ad42-0f30-32d7-940b-36eeddc9f7b3 | -3.7197 | -39.6278 | 2026-09-06 14:10:00 | GOES-19 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 134.5 |
| 814043d9-f95a-3e81-b884-13a81b1433aa | -11.3056 | -45.1113 | 2026-09-06 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 9ce7d0fa-7aec-370b-92a0-fe5319e2dbac | -5.1623 | -55.9536 | 2026-09-06 14:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 858bca4c-4445-31ce-a595-718229552b2c | -7.137 | -42.2722 | 2026-09-06 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 99.0 |
| e71672ab-68ba-380c-aded-e8eebcce1a31 | -3.6215 | -60.585 | 2026-09-06 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 27f5962c-e078-3116-b474-6da6a3c00a6f | -5.5097 | -60.2138 | 2026-09-06 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| f62a71f7-91ab-380b-b017-624022d4ef98 | -5.6566 | -60.2284 | 2026-09-06 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 100.4 |
| ca454e50-3649-3a70-af38-96ba82a32913 | -3.1462 | -60.6317 | 2026-09-06 14:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| f17616cb-8092-3b57-8618-30155e82afa3 | -5.6565 | -60.2475 | 2026-09-06 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 8d838a44-f484-3ad9-9066-69513bf59f8d | -5.6566 | -60.2284 | 2026-09-06 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 009cbf65-1c98-30b8-b41b-5ce3794b3b18 | -11.286 | -45.1371 | 2026-09-06 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| ddbe2b9d-4ff6-3d76-8eac-bbdfcfce0d5e | -3.6215 | -60.585 | 2026-09-06 14:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| e14ea774-1fcc-39b1-8471-d57c50bb82ae | -5.3647 | -56.0051 | 2026-09-06 14:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 31040866-9a9f-339d-919f-a165c459ee02 | -5.5098 | -60.1947 | 2026-09-06 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 45e42854-36e7-3b8e-824f-0bdad55d7ba4 | -5.4731 | -60.1959 | 2026-09-06 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 2c41b03c-51dd-394b-afeb-cc7ad64c8c52 | -10.2028 | -50.2895 | 2026-09-06 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |


[Clique aqui para ver as próximas entradas](README37.md)
