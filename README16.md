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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96adc224-ca76-32b3-b84e-0162bda22c22 | -8.9261 | -46.9602 | 2026-06-18 16:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 166.7 |
| 1b23e360-6257-3060-aab8-4ef1a8a69328 | -12.1952 | -52.7821 | 2026-06-18 16:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| ea2a15cc-651c-3a6a-8cd4-2bb867fd4bfe | -20.2537 | -55.4959 | 2026-06-18 16:00:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 88.0 |
| eac64605-c786-3a45-87ef-9c233d5aedf6 | -13.9412 | -53.5667 | 2026-06-18 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 3d4bdefc-60fc-3104-a003-33963622824c | -10.7838 | -53.5846 | 2026-06-18 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 08989371-966a-34f0-bfbe-a54c47061ec1 | -14.7457 | -52.6683 | 2026-06-18 16:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 132.1 |
| f63d92fe-a104-3671-a150-1fa70536fc12 | -10.7841 | -53.564 | 2026-06-18 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 7988333f-1233-3a95-b2a9-8bfbb22b683e | -8.9449 | -46.9582 | 2026-06-18 16:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 4974f1b1-8055-33e5-9cb1-69d3fe77e542 | -12.2143 | -52.7801 | 2026-06-18 16:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 0e5a803c-37f9-373a-8372-2618e415d877 | -20.2335 | -55.4991 | 2026-06-18 16:00:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 112.9 |
| a378781f-3b43-3807-bbbc-c30a65595d6d | -8.9261 | -46.9602 | 2026-06-18 16:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 354.5 |
| 2586e647-af78-3650-95fa-7efafc4a4a2a | -20.2537 | -55.4959 | 2026-06-18 16:10:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 04b7c287-25ee-3c11-993d-8215416adcdf | -13.9412 | -53.5667 | 2026-06-18 16:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 2b6cc837-3202-3d23-b1b0-1a80ed1278cf | -8.9449 | -46.9582 | 2026-06-18 16:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 357.6 |
| 8976b71b-f588-31b7-a583-312935c37747 | -20.2335 | -55.4991 | 2026-06-18 16:10:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 0c72f070-e154-320b-b0f1-bdcba872ea31 | -10.7841 | -53.564 | 2026-06-18 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| e0995793-e3b2-3c41-903b-cae5e8dd5a8e | -8.9069 | -46.9843 | 2026-06-18 16:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 7ec9aba9-c783-316a-a2d1-14ccd3edbca0 | -10.1227 | -52.1741 | 2026-06-18 16:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 2359717e-df94-3910-8335-75a0fbbc00e5 | -12.2143 | -52.7801 | 2026-06-18 16:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 162cf71b-ebaa-3264-abf2-df2b29b8023b | -10.7838 | -53.5846 | 2026-06-18 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| f2cb30b6-a16f-3a89-b744-07b3a5b7626a | -12.1952 | -52.7821 | 2026-06-18 16:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 07e722c2-4cf8-317f-bc40-ab956d1b4302 | -14.7457 | -52.6683 | 2026-06-18 16:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 22a9d089-4f00-39c7-9ea1-18cff87515c0 | -10.7838 | -53.5846 | 2026-06-18 16:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 112930c5-02c5-37d9-a842-3c6bf03b8def | -14.7457 | -52.6683 | 2026-06-18 16:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 82d6d045-b05c-3dff-b634-57171bf7dcd1 | -10.716 | -56.2494 | 2026-06-18 16:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 3bb057c0-0f35-3ba5-858c-aa446a435d10 | -10.9164 | -56.8536 | 2026-06-18 16:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| c7d51682-b25c-316c-8d03-f9f73b1323db | -20.2335 | -55.4991 | 2026-06-18 16:20:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 41ea9959-ca35-32ae-af1d-e43aab57e6b8 | -20.2537 | -55.4959 | 2026-06-18 16:20:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 86c26805-ae96-3ad5-b9b9-784a4023fbfe | -12.2143 | -52.7801 | 2026-06-18 16:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 00079657-ec33-3256-b52a-22301fff74e1 | -8.9072 | -46.9621 | 2026-06-18 16:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 30c35c0f-997e-393c-89f4-b2f812179e69 | -12.1952 | -52.7821 | 2026-06-18 16:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| ba76260f-d779-3a3d-bb5b-0847e954d71d | -12.1952 | -52.7821 | 2026-06-18 16:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 44a86142-c343-30f6-afff-cf5a37195fd0 | -13.9412 | -53.5667 | 2026-06-18 16:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 47.9 |
| b3224023-2f30-3878-bb06-7d4633d1e658 | -10.9164 | -56.8536 | 2026-06-18 16:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 107.7 |
| c8ec8c92-df3c-3c84-ae1f-56dd7eea0ce7 | -12.2143 | -52.7801 | 2026-06-18 16:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 784db5e8-c8e7-3972-bc18-039afa1b236b | -20.2537 | -55.4959 | 2026-06-18 16:30:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 383d5c48-8304-39cc-810a-738e1886fb3f | -14.7457 | -52.6683 | 2026-06-18 16:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 199.9 |
| ac0223e9-3f24-3167-a465-4cd76aaefcc6 | -9.5319 | -48.2202 | 2026-06-18 16:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 9909f222-a98a-3d06-a66f-f7bedc4b608d | -20.2335 | -55.4991 | 2026-06-18 16:30:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 102.1 |
| c315ef28-8fa8-34b9-b90a-11083b33b86d | -10.1227 | -52.1741 | 2026-06-18 16:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 0b60d459-445e-3773-902f-780dce9d0b29 | -14.7457 | -52.6683 | 2026-06-18 16:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 273.5 |
| 6fe78fab-fd19-3edc-a51a-f8981a0055ea | -10.7838 | -53.5846 | 2026-06-18 16:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 00f77379-918e-3d0c-999b-d8f1d751a347 | -11.2711 | -49.6808 | 2026-06-18 16:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 121.4 |
| a7e94b9e-f7d6-38d8-98ed-ba7dcb1d38cb | -12.2143 | -52.7801 | 2026-06-18 16:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 1c7e0d75-5da3-3ae8-b9dd-c28e8683a7cb | -8.9261 | -46.9602 | 2026-06-18 16:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 37d6cbb8-0c17-32d0-990a-09e45f1df13a | -20.2335 | -55.4991 | 2026-06-18 16:40:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 90.7 |
| b3e1ab7f-dacf-37c9-8cca-2cd445b1a9d7 | -20.2537 | -55.4959 | 2026-06-18 16:40:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 92.5 |


