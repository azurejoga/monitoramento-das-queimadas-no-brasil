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
| 2ba5128a-2611-36f8-9206-33c93101d309 | -6.978 | -42.9977 | 2025-02-09 00:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 115.6 |
| 8111f7d7-4089-3714-a7ee-75fbb72b2561 | -6.978 | -42.9977 | 2025-02-09 00:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| ec231ebb-7801-3711-9d9f-6282b6210de6 | -6.9968 | -42.9959 | 2025-02-09 00:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.5 |
| 1b6dc29e-e300-366b-a2ef-788a6c5c7b09 | -6.978 | -42.9977 | 2025-02-09 00:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.5 |
| 4cb2e0dc-3d70-311a-b69d-f62ff41108ba | -6.978 | -42.9977 | 2025-02-09 00:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 578412f7-495b-350e-9145-5eb4c4578095 | -6.9968 | -42.9959 | 2025-02-09 00:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.3 |
| cb853958-c5a4-3f39-8f7d-f866b80a5a44 | -6.978 | -42.9977 | 2025-02-09 00:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.5 |
| cbd789d8-6f14-3b02-aa1d-2e29d229094b | -6.9968 | -42.9959 | 2025-02-09 00:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.0 |
| 55fa1e61-11b2-3db7-bf2c-704bf7568105 | -6.978 | -42.9977 | 2025-02-09 00:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.6 |
| e77a0f6b-2e19-377a-84c5-ebcf8fdedd94 | -6.978 | -42.9977 | 2025-02-09 01:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.1 |
| cae37c19-b728-362f-84d3-3d4d87a255fb | -20.28014 | -49.92207 | 2025-02-09 01:04:00 | TERRA_M-M | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e56e5de4-1447-33c9-9c41-5f1ea96f3480 | -19.5163 | -49.28639 | 2025-02-09 01:04:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b79de88b-ea04-361b-aaf9-8654ff10ef6b | -16.4359 | -52.11484 | 2025-02-09 01:04:00 | TERRA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e567492b-57e0-3b92-a386-67c993e2d2d0 | -20.28898 | -49.92065 | 2025-02-09 01:04:00 | TERRA_M-M | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 247e51c6-9e01-3b63-abe7-12c0d0ac3574 | -12.34499 | -52.48893 | 2025-02-09 01:04:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 3fed975d-1ed7-3578-ae92-20972e86fe72 | -12.21041 | -50.92702 | 2025-02-09 01:04:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 6b414123-2807-3056-aac6-5cb0db601b3a | -12.35388 | -52.48764 | 2025-02-09 01:04:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7e3ced2b-b364-32bd-abc0-097a32e35a0f | -6.98468 | -42.98355 | 2025-02-09 01:06:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.2 |
| 434a2898-063f-3976-bc4a-4e188af852f9 | -6.98022 | -42.99151 | 2025-02-09 01:06:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.4 |
| 45ac918d-09f1-3ba7-aba8-25ff71ba63ad | -6.978 | -42.9977 | 2025-02-09 01:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.4 |
| af915624-45c7-3e2b-b0e2-3644bf524a4a | -6.978 | -42.9977 | 2025-02-09 01:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| 6624c976-a432-360d-beb9-9147f4d3c911 | -6.978 | -42.9977 | 2025-02-09 01:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.8 |
| d834d962-2174-35f9-97cb-bee5d1a3cb34 | -6.978 | -42.9977 | 2025-02-09 01:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.7 |
| 327742b2-3b5b-3594-86c0-6490fc4e4e99 | -6.978 | -42.9977 | 2025-02-09 01:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.9 |
| a7341601-b38e-3eff-a773-2c68cec49fe3 | -6.978 | -42.9977 | 2025-02-09 02:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.3 |
| ce83e2aa-2286-30a6-9a6b-618224329f79 | -6.978 | -42.9977 | 2025-02-09 02:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 114.3 |
| 230d009e-0906-3ed6-914a-cd2a58e5931e | -6.9968 | -42.9959 | 2025-02-09 02:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| abafc092-5afe-35aa-8604-71db0b23dfef | -6.978 | -42.9977 | 2025-02-09 02:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| a382c86c-a901-36a2-b1c9-d16d21dc1c16 | -6.978 | -42.9977 | 2025-02-09 02:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.9 |
| 51721ab1-3d33-3bb9-8c1a-ab87056bfe3c | -6.978 | -42.9977 | 2025-02-09 02:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 121.7 |
| 7ae435ea-98f0-3a44-b3f4-1bfa0c242a61 | -6.978 | -42.9977 | 2025-02-09 02:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.5 |
| ffb367ea-e23d-3f03-bdc7-07f2f0670a93 | -19.82513 | -40.10348 | 2025-02-09 02:55:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| a71e124b-a2c4-3cd9-8194-57352603fb90 | -6.978 | -42.9977 | 2025-02-09 03:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 108.2 |
| 00737c58-f94f-30d0-b020-cf9cee7aeda6 | -7.47476 | -34.84531 | 2025-02-09 03:17:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d911ba27-610a-387d-8149-be82d9ef9040 | -7.22493 | -35.78531 | 2025-02-09 03:17:00 | NOAA-20 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d29855cd-28e1-31fa-b58a-f01e4c1de183 | -18.71242 | -40.00537 | 2025-02-09 03:17:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 2e73cb76-2d0e-3671-84f7-b1f5a77f2ff7 | -7.47513 | -34.84432 | 2025-02-09 03:17:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 07421637-954e-336d-be60-c0639ed0605f | -6.97706 | -42.9991 | 2025-02-09 03:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 85ae67c5-62bb-341c-bffb-cb1219353be5 | -15.0264 | -43.38143 | 2025-02-09 03:17:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5f75db37-e0b2-3071-8f9b-a9ee8312fda9 | -15.02754 | -43.37613 | 2025-02-09 03:17:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 917b9ea7-ec3b-3822-9964-193f220e21f8 | -7.13689 | -34.99226 | 2025-02-09 03:17:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| a65c9d17-2853-3de7-a78a-ca262984b4b8 | -6.97569 | -43.00649 | 2025-02-09 03:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8b2d2f10-0f69-3e8a-84f3-d8c9a6baac7a | -21.88519 | -41.09212 | 2025-02-09 03:19:00 | NOAA-20 | SÃO JOÃO DA BARRA | RIO DE JANEIRO | Brasil | 3305000 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9bb3542c-ae17-311a-9049-3c93264d2b7a | -19.82355 | -40.1013 | 2025-02-09 03:19:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 1b801665-0918-3d74-b113-fe949949f6cd | -21.88396 | -41.09795 | 2025-02-09 03:19:00 | NOAA-20 | SÃO JOÃO DA BARRA | RIO DE JANEIRO | Brasil | 3305000 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7d2f391c-3d23-3955-bafb-b9e37ea6692a | -22.67655 | -42.85992 | 2025-02-09 03:19:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 2a99679e-2eba-389d-a594-3c7791c0d612 | -22.67354 | -42.85835 | 2025-02-09 03:19:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 05d66037-5bbf-397e-af66-40e44f6ea5c3 | -22.67437 | -42.85469 | 2025-02-09 03:19:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2fd167bc-3ead-30de-b7a1-e14855f4bd0f | -20.62029 | -40.49707 | 2025-02-09 03:19:00 | NOAA-20 | GUARAPARI | ESPÍRITO SANTO | Brasil | 3202405 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 8a166cb1-edf1-30b2-8170-d142116aea9b | -6.978 | -42.9977 | 2025-02-09 03:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.5 |
| 9b0a0dd2-340d-33e1-8ecf-91c984ebd533 | -6.978 | -42.9977 | 2025-02-09 03:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.5 |
| 45da16d2-3ff3-31f2-97c2-2b167102dab6 | -6.978 | -42.9977 | 2025-02-09 03:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 109.0 |
| fc1b8c39-c366-30ca-93a7-d4906eff96c1 | -6.978 | -42.9977 | 2025-02-09 03:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.7 |
| 9d4c38e5-52ea-3bf4-a023-d7a6ddfc5cee | -6.978 | -42.9977 | 2025-02-09 04:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| 671b092f-503c-3904-ad81-49ebd80d31e5 | -5.00115 | -37.30686 | 2025-02-09 04:06:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 08478bb3-ee4f-36c7-849c-b66586d1c7c5 | -6.60026 | -44.19721 | 2025-02-09 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1c577627-86d1-3b9f-b58c-4386da93253b | -6.62746 | -43.03278 | 2025-02-09 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a54113f-a1de-3a14-9314-188e1e53b776 | -12.41756 | -43.80519 | 2025-02-09 04:08:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 484acf36-b9af-3cb0-adae-c540f65dce08 | -6.98348 | -43.00069 | 2025-02-09 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| adf961f4-d529-382f-bdf8-ec56eebb1212 | -6.63192 | -44.11758 | 2025-02-09 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57c5f7a7-6c52-3bb9-9631-bcb8816a870b | -6.98183 | -42.98938 | 2025-02-09 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 7ef07c24-7809-3cf2-aa1b-db7887686fff | -6.60089 | -44.1972 | 2025-02-09 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51679045-7c1d-335f-9166-8a9f34c78f57 | -6.98126 | -42.99297 | 2025-02-09 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| c021265c-804a-3f46-8941-4fa6b60e3438 | -7.23208 | -44.71298 | 2025-02-09 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b2ce213-c2d6-38c1-9f74-44a938aef13c | -6.97733 | -42.99603 | 2025-02-09 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 4df5a645-24bd-3d08-b867-96e8951c3995 | -6.98405 | -42.99709 | 2025-02-09 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| d470ffbd-447d-32b6-be60-f6ed84a81e4c | -6.97676 | -42.99962 | 2025-02-09 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| fd6fa0cc-bf23-3a31-ae08-a23ec65eb790 | -6.98012 | -43.00015 | 2025-02-09 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 04b7e9d3-e9cd-3342-a7b8-6e128362a32c | -7.24215 | -44.71882 | 2025-02-09 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77dd3607-7f8e-391a-97b2-7d189b5b6978 | -7.89832 | -43.91817 | 2025-02-09 04:08:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba1d58db-9ee5-3f49-acbe-e9bdfd50ee3f | -7.24573 | -44.71938 | 2025-02-09 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d47a4576-8cea-3644-933e-ec880a753d84 | -7.4755 | -46.22959 | 2025-02-09 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 203eee07-f6e4-3b67-95f0-88dba01c6b76 | -6.98069 | -42.99655 | 2025-02-09 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| ba4ff0c5-6856-3b3b-9b9f-91ab36639197 | -7.13662 | -34.99103 | 2025-02-09 04:08:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 0a5bb41d-c743-3940-ac15-7d65c49fa0b5 | -6.98462 | -42.9935 | 2025-02-09 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| a1022334-9a11-3bd7-974a-0e0a4dd5f553 | -7.26969 | -42.15949 | 2025-02-09 04:08:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4aaca335-872c-3e84-bd79-a77cb87762ea | -6.9779 | -42.99244 | 2025-02-09 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 2b92a722-62e8-3cd7-b937-b994be12ab6a | -6.63083 | -43.03331 | 2025-02-09 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6083a85f-160a-3c66-bc46-1fd77599bc13 | -6.59738 | -44.19658 | 2025-02-09 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2598faa0-23cb-3477-b4df-037a50b79317 | -9.81744 | -39.15046 | 2025-02-09 04:08:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e780591c-029b-3325-91ba-9567fb225a33 | -7.2285 | -44.7124 | 2025-02-09 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f576cbe-238b-3c01-bec0-db25a362c032 | -6.978 | -42.9977 | 2025-02-09 04:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.9 |
| 09b686c2-e21a-3f89-9a77-811e66f4fc23 | -15.46618 | -51.95354 | 2025-02-09 04:10:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0e6eeb63-9775-372b-b179-1226c9aa376f | -20.52794 | -45.26745 | 2025-02-09 04:10:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ae070d6c-3ad4-34e3-9176-30d0939ca49f | -19.52205 | -49.28882 | 2025-02-09 04:10:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 738755bd-e248-311f-a02d-ad2de657e27f | -17.67706 | -42.74245 | 2025-02-09 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72307f8d-6dd3-3fef-a614-5773282c27de | -12.20901 | -50.92646 | 2025-02-09 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cbf52b7-b72d-3586-aff6-0799c7bc0880 | -17.75871 | -42.94489 | 2025-02-09 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| deb6ed73-07b5-3851-bbb4-f68db91f359b | -20.62181 | -40.4934 | 2025-02-09 04:10:00 | NOAA-21 | GUARAPARI | ESPÍRITO SANTO | Brasil | 3202405 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c1352a15-dd7f-3e7d-99d9-266ff46d2cf5 | -15.03127 | -43.37484 | 2025-02-09 04:10:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1295684f-e3e8-3946-a1af-3bf79ef9a13c | -20.57858 | -44.57557 | 2025-02-09 04:10:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 941053c2-c1cc-3ece-91e1-5910c019c622 | -13.62648 | -55.45266 | 2025-02-09 04:10:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 947f7938-88a1-30ae-927c-46249f0e2279 | -12.34934 | -52.48378 | 2025-02-09 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cf57ea38-a2dd-35cd-aad4-90713bcd399d | -18.59906 | -53.15585 | 2025-02-09 04:10:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1013bfb-5e97-3996-b15b-33ead18a537b | -12.34864 | -52.48732 | 2025-02-09 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 32f7f671-0f10-32b9-a841-73795ab3a2b2 | -18.59841 | -53.15895 | 2025-02-09 04:10:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2af4735d-119b-3c22-9edb-8c62baaab344 | -18.71515 | -40.00466 | 2025-02-09 04:10:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3f092847-2fbd-34c8-9507-b0cdcf0bf213 | -19.82551 | -40.1011 | 2025-02-09 04:10:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| e810e657-4324-3bc5-92f1-0376fa07d723 | -12.2139 | -50.92739 | 2025-02-09 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 260d8cb3-bed4-3ca7-b091-9ca77bbe3337 | -12.35404 | -52.48839 | 2025-02-09 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README2.md)
