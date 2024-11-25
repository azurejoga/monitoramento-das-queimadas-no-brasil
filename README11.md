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
| 038e4188-48e4-3c1f-ba35-471908c49922 | -4.29094 | -59.71602 | 2024-11-25 01:28:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ba6cdf60-4302-3404-8df6-9d754cfc4332 | -3.93608 | -47.98859 | 2024-11-25 01:28:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| bb8261d3-9970-3d3b-9524-03f15a00056b | -3.9493 | -47.9993 | 2024-11-25 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 06a1a6e2-0e8c-3f16-b2c3-9754e9652e10 | -2.3211 | -53.862 | 2024-11-25 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 7924d4be-4dcc-3305-a303-36b4e698c1c7 | -3.9494 | -47.9776 | 2024-11-25 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| b0a1e9f0-33b6-3f10-a945-1fc18915e084 | -3.2872 | -51.1194 | 2024-11-25 01:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 7732c99e-91f2-3ac4-b9bc-2dcc12483a83 | -4.023 | -48.0827 | 2024-11-25 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| c39ca22d-c2f8-3b06-84df-feae72985181 | 1.3637 | -55.9063 | 2024-11-25 01:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 02870080-ad90-3402-871a-055c42b5e22c | -2.3395 | -53.8617 | 2024-11-25 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| a1549247-bc32-32e5-a173-eecf0baa06f0 | -3.2928 | -45.7384 | 2024-11-25 01:30:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 48.4 |
| f2e98fa3-29d5-3b54-988e-29db3b453fda | 1.83651 | -55.93436 | 2024-11-25 01:30:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| c2e3e559-ecd0-3566-9cc0-92b1f5ebbfda | 1.37076 | -55.90355 | 2024-11-25 01:30:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 0e2a48e7-9607-3027-b730-45feb8979a8e | 1.85446 | -55.89958 | 2024-11-25 01:30:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 18aa5e94-a221-3094-b9d5-cde17d2536bf | 1.83801 | -55.92369 | 2024-11-25 01:30:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d4d0bd32-e48b-3f09-b518-d3f12d161e93 | 1.38039 | -55.90491 | 2024-11-25 01:30:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 35f0cb50-bb11-3116-85a7-431bd16f27fb | 1.84102 | -55.90231 | 2024-11-25 01:30:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 3a06e24a-1f82-3d3a-b32d-22ebcd914323 | 1.85071 | -55.90363 | 2024-11-25 01:30:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 42fc7721-8664-3411-b9d9-d941d39c7df8 | 1.82387 | -55.95425 | 2024-11-25 01:30:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b4cdc67b-6cdb-3719-8abb-b8623007a4df | 1.38188 | -55.89434 | 2024-11-25 01:30:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 636434b2-b54e-38d9-8dea-2eebd77a9171 | 1.41496 | -55.89406 | 2024-11-25 01:30:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 78f563c7-0f0f-3cc1-adc4-d59c274c7b60 | 1.7121 | -55.81255 | 2024-11-25 01:30:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1f0d77dd-91b3-3f89-b860-7b33cbf34ea5 | 1.36782 | -55.92455 | 2024-11-25 01:30:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 298ddaa4-021c-3141-81f2-6ca8928f8829 | 1.36929 | -55.91406 | 2024-11-25 01:30:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| b7dcf3a9-faf7-3779-8156-01a6839a6ed4 | 4.81494 | -60.59845 | 2024-11-25 01:32:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 087646a7-78b1-36dd-b477-17bd356dd671 | -3.2928 | -45.7384 | 2024-11-25 01:40:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 47.9 |
| e297bf88-8ea8-3f80-a8d7-d77c9f949c0f | -2.3395 | -53.8617 | 2024-11-25 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 0337d7d9-d044-3333-bfe0-63bf1c8c28db | -3.9494 | -47.9776 | 2024-11-25 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 04d10703-1efe-344d-b3de-2e03ac253165 | -3.2872 | -51.1194 | 2024-11-25 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 856deb96-3f44-38eb-a779-53cb679be322 | -3.9493 | -47.9993 | 2024-11-25 01:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| d88426cf-8076-336c-bb66-33ebdc6c8846 | -2.3211 | -53.862 | 2024-11-25 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 109542a9-5192-3efe-94b1-bae6fcc424eb | -0.6918 | -68.353897 | 2024-11-25 01:43:00 | METOP-B | SÃO GABRIEL DA CACHOEIRA | AMAZONAS | Brasil | 1303809 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b718ec06-818e-3f06-b021-8759e3e34979 | -3.4581 | -50.0047 | 2024-11-25 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| dd4696a8-4cab-38e8-bca0-b659fedb9249 | -3.9494 | -47.9776 | 2024-11-25 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| e5aa1832-730f-35c6-8de9-d21d10adc096 | -2.9043 | -45.3719 | 2024-11-25 01:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |
| b14f8d95-2321-33e6-899c-0376dbd7f4be | -3.9493 | -47.9993 | 2024-11-25 01:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 78fa6c3c-2cc6-316d-8cf7-8870fa7ff04f | -3.4396 | -50.0053 | 2024-11-25 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 5a9c0f64-4800-39c9-acc2-2204b448c2b2 | -2.3395 | -53.8617 | 2024-11-25 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| dce4a1e4-7504-3f8a-afaa-8c77b36e3641 | -2.3395 | -53.8617 | 2024-11-25 02:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| cde123e0-2697-314d-8590-b3e435790cb9 | -3.9494 | -47.9776 | 2024-11-25 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 866333e7-8766-3cfa-afee-8665304610a6 | -3.4396 | -50.0053 | 2024-11-25 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 4def6d1c-079e-3815-8c20-62890c1d5dd8 | -3.4581 | -50.0047 | 2024-11-25 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| d734800a-3f95-33ed-9ca4-bb4099c55ef2 | -3.2872 | -51.1194 | 2024-11-25 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 9fc7857a-bb42-368d-8d97-b21b09a86b11 | -2.5887 | -45.3151 | 2024-11-25 02:10:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 3037fbbe-2914-31a1-a64d-1d9d1ba4128f | -3.9494 | -47.9776 | 2024-11-25 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 66992ae1-3461-367b-80c0-f7da538375cf | -2.3395 | -53.8617 | 2024-11-25 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| b3791378-0cf1-3eca-90a5-5677923e101d | -3.4396 | -50.0053 | 2024-11-25 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| cf3dc1a1-fbb6-39ea-8a97-2ebb24401378 | -2.5886 | -45.3376 | 2024-11-25 02:10:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 346f1298-818e-3a73-b78f-3ef8ca531274 | -3.4581 | -50.0047 | 2024-11-25 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| c1b2e6b3-2dd6-34ac-97c3-0845d56438ba | -2.9043 | -45.3719 | 2024-11-25 02:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 136.2 |
| 9d433324-79a1-3a14-9649-d8977626e35b | -3.2872 | -51.1194 | 2024-11-25 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 60a2a1eb-ca7b-3ba8-a232-ca1057b46c12 | -2.5886 | -45.3376 | 2024-11-25 02:20:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 46.4 |
| e55dc6c3-2a3b-38e1-aa4c-0fa051928706 | -2.9043 | -45.3719 | 2024-11-25 02:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 6dc07f61-0b07-3a90-bb65-7268becc73b5 | -2.3395 | -53.8617 | 2024-11-25 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 3ae09f69-dfa6-3e71-a33f-e8d0dc597ef4 | -2.5887 | -45.3151 | 2024-11-25 02:20:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 48cd902b-f588-3ef1-945f-35f0b6645cc1 | -1.9431 | -50.5695 | 2024-11-25 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 3c32e27a-482e-3530-ad38-19f0dde15d89 | -2.3395 | -53.8617 | 2024-11-25 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 8f62ddae-637d-379b-978a-9c0a13d1fd76 | -2.3395 | -53.8617 | 2024-11-25 02:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| f752d1bf-73aa-3d0f-bd2e-5162315e33d1 | -1.9431 | -50.5695 | 2024-11-25 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 1d0b3b5a-128f-3267-a543-bf73730bbcd7 | -2.3395 | -53.8617 | 2024-11-25 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 664a19ea-0e89-385d-81b1-5cf98407602f | -10.82831 | -37.4193 | 2024-11-25 02:53:00 | NOAA-21 | ITABAIANA | SERGIPE | Brasil | 2802908 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 38bfe427-8cde-310c-a304-19d0cf43aea6 | -10.8299 | -37.40839 | 2024-11-25 02:53:00 | NOAA-21 | CAMPO DO BRITO | SERGIPE | Brasil | 2801009 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| aae61047-170e-332d-990e-4e7360d5fea0 | -10.82833 | -37.41582 | 2024-11-25 02:53:00 | NOAA-21 | CAMPO DO BRITO | SERGIPE | Brasil | 2801009 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 2e541fd6-41a8-34f4-abbd-4f9d2ce4b5e5 | -10.82142 | -37.41776 | 2024-11-25 02:53:00 | NOAA-21 | ITABAIANA | SERGIPE | Brasil | 2802908 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 1d34d3ff-0c75-309a-88e1-100569f471cc | -7.59214 | -35.03353 | 2024-11-25 02:53:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| bc451833-0f88-3765-bb9a-13a7e2ca7762 | -7.59116 | -35.03867 | 2024-11-25 02:53:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 599e27e5-4bac-3414-8bdb-11109c753c80 | -7.59851 | -35.03461 | 2024-11-25 02:53:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| a7ae7b0f-a173-3529-b447-66d4ea3fd5de | -7.59751 | -35.03991 | 2024-11-25 02:53:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d3a50ad0-ccc0-36de-9e29-1fd1cbdd5b6b | -3.2928 | -45.7384 | 2024-11-25 03:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 61.1 |
| e9683a04-8be0-394b-bd20-8749bb6c46be | -2.3395 | -53.8617 | 2024-11-25 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 5fb684d5-8434-3f88-83f8-e185232c49e6 | -3.2928 | -45.7384 | 2024-11-25 03:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 986b8fd3-5373-33d9-a37a-6dbd835540a0 | -10.47811 | -36.82585 | 2024-11-25 03:17:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| efe2bcfc-1b4d-37a4-b18e-992318a0a87f | -6.73478 | -34.97448 | 2024-11-25 03:17:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| c499db0f-df18-3a26-ab3c-7cab560c4743 | -10.47097 | -36.83912 | 2024-11-25 03:17:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8ccc7631-b688-3f0f-8728-d6f1b2ae5c45 | -8.27133 | -35.4873 | 2024-11-25 03:17:00 | NPP-375D | CHÃ GRANDE | PERNAMBUCO | Brasil | 2604502 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 56576c72-d123-3d53-8bf5-ccb5a5fc1467 | -10.48273 | -36.82683 | 2024-11-25 03:17:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 38e9bc52-ecc0-3fc9-9fea-bfaac8752bf1 | -10.48014 | -36.82774 | 2024-11-25 03:17:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8823728d-7014-3e57-81c3-5067f783a135 | -10.48102 | -36.82299 | 2024-11-25 03:17:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 20bf8302-0c1a-3fc9-be46-afeab56373ae | -4.86497 | -38.37927 | 2024-11-25 03:17:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3d130bb6-10a2-3eaf-a5b1-1cf93f2a9604 | -7.13964 | -35.18661 | 2024-11-25 03:17:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b1fcaf8c-121a-3ead-a12a-036b890a9fc8 | -6.77953 | -35.37117 | 2024-11-25 03:17:00 | NPP-375D | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6d5a9315-1e80-3167-ad20-025c14b70be9 | -4.85933 | -38.37818 | 2024-11-25 03:17:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2836377d-a9e9-3243-b6e5-e8cb4df9571a | -22.90231 | -43.75293 | 2024-11-25 03:19:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e0099934-6519-36e3-8043-d8ed3e814a7d | -1.9247 | -50.5908 | 2024-11-25 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| cdab8406-955f-3c4f-a2c4-04a6754c876b | -1.9248 | -50.549 | 2024-11-25 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| e67a652a-45ab-3078-94ca-6b75aa1cb95e | -1.9247 | -50.5699 | 2024-11-25 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 68427721-b820-3aa4-8193-9ca1cdb72203 | -3.2928 | -45.7384 | 2024-11-25 03:20:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 2ce64dd3-bda4-3b7f-910b-2a50ddaf94af | -1.9431 | -50.5695 | 2024-11-25 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 8e4c05d2-9cba-3db3-9e91-29534c9081a7 | -3.2928 | -45.7384 | 2024-11-25 03:30:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 102.1 |
| c22274fd-8a77-3ce8-9bda-996915ccc8ff | -1.7726 | -52.7379 | 2024-11-25 03:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 9dbc384e-5049-3779-8315-2e01c3ecd580 | -1.9431 | -50.5904 | 2024-11-25 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 5f695779-199f-3820-a6bb-705cc1cc2b28 | -1.9431 | -50.5695 | 2024-11-25 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| ae0ecfa0-c2f7-3ed3-883b-140d22d99e1b | -4.023 | -48.0827 | 2024-11-25 03:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 061828a2-d8a3-3f88-969c-3f01aceb088d | -1.9431 | -50.5904 | 2024-11-25 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 5efe6a09-8158-39d9-903a-0b6b5143a28d | -1.7726 | -52.7379 | 2024-11-25 03:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| dee8fa9a-17a3-309e-9618-b268ed43c18d | -1.9431 | -50.5695 | 2024-11-25 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| c6c82468-fc68-3cc4-bd64-f1be190715fc | -3.2928 | -45.7384 | 2024-11-25 03:40:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 5d2b7f48-0ca0-34e5-b9d2-265ec90b3cae | -8.8436 | -35.17122 | 2024-11-25 03:40:00 | NOAA-20 | SÃO JOSÉ DA COROA GRANDE | PERNAMBUCO | Brasil | 2613404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 08236363-f4de-35bc-ad9b-10a67a321e38 | -8.90007 | -35.52668 | 2024-11-25 03:40:00 | NOAA-20 | CAMPESTRE | ALAGOAS | Brasil | 2701357 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| fd51f443-5fa2-3b26-8e9a-419871aeac69 | -4.86401 | -38.38036 | 2024-11-25 03:40:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d38c1257-451a-3b95-871b-19b537de6e0d | -4.54005 | -42.88747 | 2024-11-25 03:40:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README12.md)
