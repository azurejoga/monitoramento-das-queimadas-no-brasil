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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1774a704-f934-3b7f-9cf8-b4e14db775c0 | -4.4241 | -43.4735 | 2024-11-03 02:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| a327600a-bfdf-344f-8968-6b1ced59bdd6 | -4.4056 | -43.4514 | 2024-11-03 02:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 4096e5ed-601c-30fc-83d6-73ed693bbc87 | -4.4054 | -43.4746 | 2024-11-03 02:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| f461c409-62d2-39e2-ad22-faf7e1be7565 | -6.5239 | -41.4929 | 2024-11-03 02:45:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 79.6 |
| 230ab20b-7eac-3b5c-a292-119bc5afe25c | -1.2755 | -53.4138 | 2024-11-03 02:55:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| f46ada6c-ce6d-3692-9783-223886f02a85 | -1.2755 | -53.3936 | 2024-11-03 02:55:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| ae1385b0-c79b-3895-ba9d-8b480925a4af | -1.2756 | -53.3734 | 2024-11-03 02:55:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 2e1cb299-6bdb-3c7a-9cce-d81712c30f46 | -1.2939 | -53.4136 | 2024-11-03 02:55:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 4b69f788-5f5c-35bb-a0d2-10db5f486746 | -1.2939 | -53.3934 | 2024-11-03 02:55:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 2e420703-963c-394a-8fd7-bb6075a52436 | -2.1746 | -53.6834 | 2024-11-03 02:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 541bc6d0-5ded-3d12-b6ba-b926f7ed1bd6 | -2.2802 | -48.8082 | 2024-11-03 02:55:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 99fbf7d9-bbde-33e1-8874-8dc677631113 | -2.5796 | -53.3927 | 2024-11-03 02:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 5fca62f9-4ea5-39f4-a318-7658d7e06f5e | -2.5797 | -53.3724 | 2024-11-03 02:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 9f1c6682-a452-3281-8a94-a30e2191706a | -2.6321 | -48.5849 | 2024-11-03 02:55:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 3f30988a-fa32-38a2-94f2-001fddab0e95 | -2.6322 | -48.5634 | 2024-11-03 02:55:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 4dab3585-77e1-30c3-bc64-8b97a065512a | -2.7033 | -49.33 | 2024-11-03 02:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 453405ea-26f8-3f14-973d-e53474ddaf99 | -2.7218 | -49.3295 | 2024-11-03 02:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 50cb7406-02f3-3e40-8020-63d7142fb739 | -2.7419 | -54.4153 | 2024-11-03 02:55:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 01ccb269-ed36-3539-8538-177c00081da0 | -2.7603 | -54.4149 | 2024-11-03 02:55:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 135.0 |
| 27e1fd84-0634-3698-84f7-79916f7cd1f2 | -2.8148 | -49.1567 | 2024-11-03 02:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 122.7 |
| e607427f-7d22-34ed-955d-0a30a3147c78 | -2.8333 | -49.1562 | 2024-11-03 02:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 42953128-693b-370f-ace2-ad391483c6dd | -2.7419 | -54.4353 | 2024-11-03 02:55:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 573d29d7-7d3c-3638-9e2f-e4882de57866 | -2.7602 | -54.4349 | 2024-11-03 02:55:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 166.5 |
| e2ace62a-aa6e-3032-a8c2-f9a890640d58 | -3.055 | -54.1474 | 2024-11-03 02:55:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| b42c7fa6-7a38-391e-82f1-02b996f0048b | -3.0734 | -54.167 | 2024-11-03 02:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| ff1c03cb-fd0d-3e21-9481-c02f4e080fc3 | -3.0734 | -54.147 | 2024-11-03 02:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| e17bd4c6-f1ca-3095-96e0-ef20d0c693f6 | -3.1059 | -50.3105 | 2024-11-03 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| fac69373-9c6f-3378-8f6b-315c93c439ba | -3.106 | -50.2896 | 2024-11-03 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 93828c4d-e3d2-38b3-9aa9-638e8ec0172e | -3.1061 | -50.2686 | 2024-11-03 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 991459e4-03cc-3811-9871-6a0e85f484b0 | -3.1212 | -51.1244 | 2024-11-03 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 0c3a86b9-a441-3fcf-9eef-95a529ad39bf | -3.1213 | -51.1036 | 2024-11-03 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 2b7d007c-cc27-343c-8d1d-cd4e3a2cb982 | -3.1501 | -48.5689 | 2024-11-03 02:55:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 1a2fee80-de58-336c-9400-c28f84e1d23c | -3.3276 | -50.2825 | 2024-11-03 02:55:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 5a898996-f69a-3663-875d-e591b441a0e4 | -3.4564 | -50.3832 | 2024-11-03 02:55:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 37be0f9d-4bbc-3d09-89ac-4b76fcf6a134 | -3.4749 | -50.3826 | 2024-11-03 02:55:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 465eabaf-a023-3cd8-945b-0f2ebeebb764 | -3.4934 | -50.3819 | 2024-11-03 02:55:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| bee895bf-ea4e-3f82-bd86-ff305738c15b | -3.9473 | -48.3666 | 2024-11-03 02:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| b39fa9f0-492c-334b-ab63-1b0c86e8fa66 | -3.9474 | -48.3451 | 2024-11-03 02:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| b889257b-f5d6-37e3-b024-3b6570492216 | -3.967 | -48.15 | 2024-11-03 02:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 0cf48bdd-a0e0-3e92-bfb0-702404004cf5 | -4.4054 | -43.4746 | 2024-11-03 02:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| de8b923a-9a6b-31d8-a652-8b2864ef5aa5 | -4.4056 | -43.4514 | 2024-11-03 02:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 5d42c8a6-431c-30e4-b0fc-90257e5f7bd4 | -4.4241 | -43.4735 | 2024-11-03 02:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 97dbdcf4-121c-3296-b1a4-73b2795c8eeb | -4.4243 | -43.4503 | 2024-11-03 02:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 73ea267f-d6e7-33fa-bf54-4b6e5f5f770a | -6.5239 | -41.4929 | 2024-11-03 02:55:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 101.2 |
| 14ee2c30-63a5-3c9a-bb32-8faa25e06b7f | -8.7247 | -48.0163 | 2024-11-03 02:55:55 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 1500db02-ab2e-3c88-95f0-01771c50e073 | -5.68901 | -38.04344 | 2024-11-03 03:04:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 151e7f7c-14bf-3fa5-b3fc-1a25c55a7987 | -1.2572 | -53.3938 | 2024-11-03 03:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 11697dfa-ecc1-3fa5-ac27-10f597132b4f | -1.2755 | -53.4138 | 2024-11-03 03:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 135.0 |
| 56f15345-3b38-3e9c-a850-521b2be36ee6 | -1.2755 | -53.3936 | 2024-11-03 03:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 151.0 |
| 1ca85a98-6787-3b11-804b-4a529410299c | -1.2756 | -53.3734 | 2024-11-03 03:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| d895a2b4-98dd-3b66-ac1f-388f1b169051 | -1.2939 | -53.4136 | 2024-11-03 03:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 1426eb25-2ffb-3cef-90e1-35a512de1e11 | -1.2939 | -53.3934 | 2024-11-03 03:05:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| a93aa0dd-849d-3900-9898-8fd229ded055 | -2.1746 | -53.6834 | 2024-11-03 03:05:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 5e406e26-7cd4-36e0-80de-239a9a681a66 | -2.2802 | -48.8082 | 2024-11-03 03:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 840ce7aa-ecbd-3bbf-bdd1-07b1a43acc83 | -2.5796 | -53.3927 | 2024-11-03 03:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 8cad246e-d898-336d-acd1-c380cca3a0b3 | -2.5797 | -53.3724 | 2024-11-03 03:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 00836e21-d9c7-3188-bf82-b2996a4a6180 | -2.6321 | -48.5849 | 2024-11-03 03:05:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 145842eb-1bee-3e1d-bcfb-14738c8cb3ca | -2.7218 | -49.3295 | 2024-11-03 03:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 222acd14-066a-3b60-926b-7a856438a838 | -2.7419 | -54.4353 | 2024-11-03 03:05:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 16be2927-3826-3052-8100-d55227e0a6fa | -2.7419 | -54.4153 | 2024-11-03 03:05:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 341cab51-be52-3190-aeb7-5d203dd54eee | -2.7602 | -54.4349 | 2024-11-03 03:05:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 143.8 |
| b9d2bcbe-55d5-38a5-b14f-00688e99fabe | -2.7603 | -54.4149 | 2024-11-03 03:05:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 5360e02f-38b9-3d80-b4f7-84db8c36b6b2 | -2.8148 | -49.1567 | 2024-11-03 03:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 133.8 |
| 2d2506fb-78ea-337d-b8e0-27f675ceaef7 | -2.8149 | -49.1354 | 2024-11-03 03:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 3f2c6b95-85a3-34ce-851a-c4fd4acba57b | -2.8333 | -49.1562 | 2024-11-03 03:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| a2e890e3-2bcf-3374-abc4-d76922c40221 | -3.055 | -54.1474 | 2024-11-03 03:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| c6178436-bcf6-386d-b00e-cc89af66a021 | -3.0734 | -54.167 | 2024-11-03 03:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| bb0391f0-3a53-386b-8c41-a3bc940213da | -3.0734 | -54.147 | 2024-11-03 03:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| c429b8a3-95cb-3336-af24-0664820b4c86 | -3.1059 | -50.3105 | 2024-11-03 03:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 0a61b289-c621-3184-84df-0b1cb014a285 | -3.106 | -50.2896 | 2024-11-03 03:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 55f0a345-75cc-3a7b-9c39-9dc2c455216f | -3.1061 | -50.2686 | 2024-11-03 03:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| fad87986-3682-3d19-a3f8-caea43a5a2e2 | -3.1212 | -51.1244 | 2024-11-03 03:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| a8daadbc-f701-3d25-8fce-abb3a27902ee | -3.1213 | -51.1036 | 2024-11-03 03:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| c6f09ccd-178c-3462-9057-91a62d0ebcf4 | -3.1245 | -50.289 | 2024-11-03 03:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| e25ecc16-8228-38a0-b348-18644a1281c4 | -3.1501 | -48.5689 | 2024-11-03 03:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| dfea4c4d-c939-3886-ba02-8335161a466c | -3.3276 | -50.2825 | 2024-11-03 03:05:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 3c8aef38-a68a-3643-85f3-afa9e60f478e | -3.4564 | -50.3832 | 2024-11-03 03:05:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| e26d8d42-63c4-3831-8c1e-c11788a2e13b | -3.4749 | -50.3826 | 2024-11-03 03:05:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 8c4674e8-2fc8-3fb4-98ed-3c00012f942c | -3.4934 | -50.3819 | 2024-11-03 03:05:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 4dceba85-28a5-3a11-8643-14ed698e5d19 | -3.967 | -48.15 | 2024-11-03 03:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 0e2a2810-2e82-3914-a0e2-53403c5abeba | -3.9473 | -48.3666 | 2024-11-03 03:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 4807deec-071c-3fe7-bc6f-deb6f6192228 | -3.9474 | -48.3451 | 2024-11-03 03:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 12d908c3-3148-377b-b090-fc7e02bc2a39 | -4.4054 | -43.4746 | 2024-11-03 03:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 37b5f430-afef-31f5-8804-e856d8251a2a | -4.4056 | -43.4514 | 2024-11-03 03:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 587914e2-c26e-36f8-b06c-fbf240d55b31 | -4.4241 | -43.4735 | 2024-11-03 03:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 1c7db095-3b4f-3da7-90de-7d4df2eb7897 | -4.4243 | -43.4503 | 2024-11-03 03:05:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| d3922703-ba97-3e9f-b6a7-0bb2556fe8c0 | -6.5239 | -41.4929 | 2024-11-03 03:05:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 97.6 |
| 273adfcb-9068-330a-8f01-457a08df9bf7 | -6.5241 | -41.4688 | 2024-11-03 03:05:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 66.3 |
| bfcb3140-9c79-311c-a0ab-0e00439a1885 | -7.52694 | -35.13161 | 2024-11-03 03:06:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1aa7bddb-563b-341d-ad6b-dd676d265015 | -7.52635 | -35.13492 | 2024-11-03 03:06:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fd7eb74a-bf91-37ea-9ec3-0f9c3cc372ca | -8.15938 | -35.31306 | 2024-11-03 03:06:00 | NOAA-21 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 610828c5-1f91-3b3c-b072-c700b7ec84df | -6.85508 | -38.46832 | 2024-11-03 03:06:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d8f813c3-b9f3-391d-a554-1c52c93f6201 | -6.77169 | -37.53958 | 2024-11-03 03:06:00 | NOAA-21 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 27db89f4-0336-3211-a20a-6357f87b98c0 | -6.76545 | -37.53828 | 2024-11-03 03:06:00 | NOAA-21 | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 52754759-ebd5-3434-b65a-56b064244d50 | -6.70679 | -37.48431 | 2024-11-03 03:06:00 | NOAA-21 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7fece9b5-bfee-36ba-ac0f-cefb3f520262 | -6.70401 | -37.48547 | 2024-11-03 03:06:00 | NOAA-21 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f506deac-5c03-323c-953f-c410ab871cb3 | -6.70069 | -37.48229 | 2024-11-03 03:06:00 | NOAA-21 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ed05ddb0-52c4-3603-8234-88ea4aaf26e6 | -6.69884 | -37.47856 | 2024-11-03 03:06:00 | NOAA-21 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2221a333-51bf-3053-8fb8-5b7dd780b01c | -11.23683 | -39.40838 | 2024-11-03 03:06:00 | NOAA-21 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 36fff043-452d-3850-878c-dd4a3fcab626 | -1.2756 | -53.3734 | 2024-11-03 03:15:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |


[Clique aqui para ver as próximas entradas](README20.md)
