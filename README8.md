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
| 0f858260-804a-3826-838f-1ff52dcdbe07 | -2.3632 | -46.526402 | 2024-10-28 00:49:32 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c26e24d4-caed-3acb-96b0-9e7cb2e3ff77 | -2.365 | -46.534401 | 2024-10-28 00:49:32 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b8c8108-b8c3-3079-9d5c-20a271cdaa94 | -2.5533 | -47.347401 | 2024-10-28 00:49:32 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24f23cd7-b0d2-31e8-b540-8c4fedf3f07b | -2.555 | -47.354801 | 2024-10-28 00:49:32 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 354ec2ab-f3ae-3d8b-a2f3-a03b61a748bc | -3.0463 | -49.4888 | 2024-10-28 00:49:32 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4db0fede-d3a6-3a30-8355-baeacff713ea | -3.0478 | -49.495602 | 2024-10-28 00:49:32 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f826275f-975a-30d5-9526-eed27fac207e | -2.3974 | -46.7187 | 2024-10-28 00:49:32 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c41379f3-a12b-3e18-a6a9-9ce4621022f6 | -2.3993 | -46.726501 | 2024-10-28 00:49:32 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9b41961-28e4-3499-ba0f-4e3671060461 | -2.5354 | -47.3592 | 2024-10-28 00:49:33 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8173ec6a-c650-366f-8dfc-a2042e0a9f9b | -2.5372 | -47.366501 | 2024-10-28 00:49:33 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82716cbe-658d-3c9d-8478-04c2fdecb48f | -2.5389 | -47.373901 | 2024-10-28 00:49:33 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9c0529c-65d2-3fc7-adb2-4348a2dab1fa | -2.5214 | -47.432098 | 2024-10-28 00:49:33 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05013b0e-f612-338e-85c9-902b47a3ac19 | -2.5231 | -47.4394 | 2024-10-28 00:49:33 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0699807b-a7a0-3d6e-b687-04f34e4fc4ff | -2.5248 | -47.4468 | 2024-10-28 00:49:33 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b61fdba-e780-3baf-bdd3-60de1b99bb77 | -2.8141 | -48.702 | 2024-10-28 00:49:33 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a73a05c-beba-35df-9ad0-8b45621397cb | -2.3247 | -46.6273 | 2024-10-28 00:49:33 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ceeaa1a9-240d-3745-87ad-313c6ab7fbaa | -2.3265 | -46.635201 | 2024-10-28 00:49:33 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f8c881d-bc4e-3808-88b1-9ef98095d077 | -2.3284 | -46.643101 | 2024-10-28 00:49:33 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69d8dea4-36e9-3311-bd12-3214cb842064 | -2.3204 | -46.653301 | 2024-10-28 00:49:33 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e74fd3e-f9dc-356a-a74f-579f9ffa3942 | -2.3222 | -46.661201 | 2024-10-28 00:49:33 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64ee34d9-918c-3a9d-bef1-102e5e5cb66c | -4.0053 | -46.979698 | 2024-10-28 00:49:34 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cc45c92c-ed93-35c4-a98e-21545a696bc1 | -4.007 | -46.987099 | 2024-10-28 00:49:34 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0b30ad46-642f-3b63-b80b-c236107b40e6 | -2.3088 | -46.647598 | 2024-10-28 00:49:34 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4faed8b-bfff-37f1-9883-ce92c130c6d0 | -2.3106 | -46.655499 | 2024-10-28 00:49:34 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c364b0d-2e77-34b9-9310-72aefd0d5479 | -2.3124 | -46.663399 | 2024-10-28 00:49:34 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8dd73b21-7070-3b0d-b6f1-48ee1b349bf9 | -2.78 | -48.688 | 2024-10-28 00:49:34 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b475416c-53e0-38c5-8c82-3c4e55c219ab | -2.2953 | -46.633999 | 2024-10-28 00:49:34 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19dfb667-a409-3d11-a435-a17674fd651a | -2.2971 | -46.641899 | 2024-10-28 00:49:34 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2312af80-f1cb-3120-9664-5bad58dcd1cb | -2.299 | -46.649799 | 2024-10-28 00:49:34 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8b3a4b9-1f31-3bcc-a078-600dbc6f995e | -2.3008 | -46.6577 | 2024-10-28 00:49:34 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36a70c6c-9478-3474-8cea-c48485764a82 | -2.2855 | -46.6362 | 2024-10-28 00:49:34 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3f33d11-9ff8-3e87-bb9f-fa0486777250 | -2.2873 | -46.6441 | 2024-10-28 00:49:34 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d09d7ff8-b568-32be-84a1-47c63eef861c | -2.7635 | -48.7061 | 2024-10-28 00:49:34 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c10c183d-7ad7-3629-bdd6-a8dfc842179b | -2.7651 | -48.713001 | 2024-10-28 00:49:34 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d403c127-1416-3a87-b82d-d10f112e04ea | -2.7521 | -48.7015 | 2024-10-28 00:49:34 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8265fba9-1a9b-3f72-987f-fcd689b0169e | -2.7536 | -48.708302 | 2024-10-28 00:49:34 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0466b986-13b0-3b5c-8f4b-1dcb7db3a25e | -2.876 | -49.240601 | 2024-10-28 00:49:34 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f498031-2f5a-3add-9734-39d5edc4ade2 | -2.8775 | -49.247398 | 2024-10-28 00:49:34 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e87af2c-0e01-3673-a15f-1b6efd42eb35 | -2.8791 | -49.2542 | 2024-10-28 00:49:34 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afc34dc1-2009-37a5-ba44-7135195d3975 | -2.8807 | -49.261002 | 2024-10-28 00:49:34 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e8e7574-0228-32d3-88a2-bfbe28d30c1b | -2.2878 | -46.735199 | 2024-10-28 00:49:34 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61ceb1b7-7507-3a45-93b3-336976c942a3 | -2.2896 | -46.743099 | 2024-10-28 00:49:34 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7002309-74f1-37f4-b3bc-dc6818f7ab9b | -2.2914 | -46.7509 | 2024-10-28 00:49:34 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74fd05d3-cb33-352b-9c45-872d37c81e55 | -2.2933 | -46.758701 | 2024-10-28 00:49:34 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 336652e2-96f9-3f03-8265-6127cfd5f54b | -2.8645 | -49.236 | 2024-10-28 00:49:34 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e44839dc-b23b-344d-ab70-7490be58e426 | -2.8661 | -49.242802 | 2024-10-28 00:49:34 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5cc0474-53ac-33bd-a920-d5b5de0ba745 | -2.8676 | -49.249599 | 2024-10-28 00:49:34 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 410cba36-2eb7-3566-982d-3c52e632ca8f | -2.8692 | -49.256401 | 2024-10-28 00:49:34 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 769eacb9-6fb7-30a8-924f-b2718778a050 | -2.8708 | -49.263199 | 2024-10-28 00:49:34 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d28d08fe-6477-348c-afdf-c9d723f77332 | -2.9348 | -49.542198 | 2024-10-28 00:49:34 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aec61dd9-59ff-3d86-ba08-25c50edbfcdf | -2.9364 | -49.549 | 2024-10-28 00:49:34 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de91277c-cb85-3537-9afa-bae1f06ab572 | -2.81 | -49.312599 | 2024-10-28 00:49:35 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca0580fe-75c3-39da-b0c0-23355316f149 | -2.8287 | -49.394199 | 2024-10-28 00:49:35 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0a348fe-6c4c-3fa5-92c5-24f244c8c169 | -2.8302 | -49.401001 | 2024-10-28 00:49:35 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e278d670-83c1-3822-ab3c-d223abefe76a | -3.3325 | -51.6031 | 2024-10-28 00:49:35 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35e81fc9-75b4-3514-81b7-f53078eb189d | -3.3343 | -51.610802 | 2024-10-28 00:49:35 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 207ff2f1-bfcc-3a97-a2b0-c882b332c1a1 | -3.336 | -51.618401 | 2024-10-28 00:49:35 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2241da77-7474-36b7-af7b-bb270d31020e | -2.5266 | -48.125099 | 2024-10-28 00:49:36 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53f44337-9aed-3afe-8279-a491bfb6e596 | -2.4989 | -48.0499 | 2024-10-28 00:49:36 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e57abb87-365d-31a0-9ec7-78074271aa7d | -2.5005 | -48.0569 | 2024-10-28 00:49:36 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3493f44-9006-37ba-b023-be53aa6de83a | -2.5021 | -48.063999 | 2024-10-28 00:49:36 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10bb9b65-1c9f-3b30-8683-438a7a5092d4 | -3.0385 | -50.401501 | 2024-10-28 00:49:36 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edb45b87-5533-3e77-b219-4990b5b997d7 | -3.04 | -50.408401 | 2024-10-28 00:49:36 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6294e21-3af2-3c81-ab96-52d64c87153e | -3.0416 | -50.415401 | 2024-10-28 00:49:36 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42ec653c-7efd-30bf-9ec2-b5911c4c8efa | -3.0432 | -50.422401 | 2024-10-28 00:49:36 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39369190-b1ef-30a3-b8a8-9d6d0d90a703 | -3.0271 | -50.396599 | 2024-10-28 00:49:36 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c669f1b-e7bb-3ae9-9d44-a4fb6e50ce06 | -3.0287 | -50.403599 | 2024-10-28 00:49:36 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c28e567-301a-3dc7-bea1-08542fc7da13 | -3.0302 | -50.4105 | 2024-10-28 00:49:36 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d85cdee7-659b-3ee2-ae07-3e24c1d8e5df | -3.0318 | -50.4175 | 2024-10-28 00:49:36 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77fc7941-ae0d-3dec-8df2-3bbaa0794d80 | -2.0444 | -46.307899 | 2024-10-28 00:49:37 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 204e9291-5259-31da-8aff-a7581064c70f | -2.0346 | -46.310101 | 2024-10-28 00:49:37 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fed030c-3795-3c30-b2da-68731efb0583 | -2.7139 | -49.298302 | 2024-10-28 00:49:37 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87f299ea-51ce-3d67-bca3-524031f39e4f | -2.7154 | -49.305099 | 2024-10-28 00:49:37 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 255cec2c-8ec7-3c57-922b-6174fc91f90f | -2.717 | -49.311901 | 2024-10-28 00:49:37 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ae57630-65f4-3bf6-a589-61f478ece68b | -2.7186 | -49.318802 | 2024-10-28 00:49:37 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5508344c-efe7-3d47-8d8f-87edff878d8d | -2.9825 | -50.472599 | 2024-10-28 00:49:37 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06b95a03-f720-3362-a66a-e885ae0cbe6d | -2.0544 | -46.528702 | 2024-10-28 00:49:37 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60c0a63b-6a12-3900-9446-763b66520668 | -2.6957 | -49.309399 | 2024-10-28 00:49:37 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 116c8dfc-4ef6-3699-a2aa-2e68b4579573 | -3.3473 | -52.167999 | 2024-10-28 00:49:37 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8eaf4ac0-591a-3401-94fb-97ef030cfa30 | -4.0315 | -48.2985 | 2024-10-28 00:49:38 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cda8541b-24b1-360a-b721-219c5a537188 | -4.2824 | -49.391899 | 2024-10-28 00:49:38 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4ec505b-7322-3f71-a622-02026271f2b3 | -4.2839 | -49.3988 | 2024-10-28 00:49:38 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a471f9d-0e88-3f45-92a7-b6ce6e84d902 | -2.5721 | -48.9505 | 2024-10-28 00:49:38 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc8a3602-e316-3b2c-8c75-ffc90bbf5cd5 | -2.5736 | -48.957298 | 2024-10-28 00:49:38 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a78840ab-fc3f-3ff7-8d03-92f33b4a8ffd | -2.4581 | -48.4995 | 2024-10-28 00:49:38 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d1caad8-7c68-3af8-99bf-f66fb32c16ee | -2.4597 | -48.506401 | 2024-10-28 00:49:38 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e285c2a-ca7b-3f07-9042-10c72829622f | -2.6327 | -49.259201 | 2024-10-28 00:49:38 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7f5e71d-60ad-394e-a4f0-c3e0235712a9 | -3.1832 | -45.0028 | 2024-10-28 00:49:39 | METOP-C | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 11cd34cd-2606-3122-ac72-96d9fabb9b3e | -3.1854 | -45.0121 | 2024-10-28 00:49:39 | METOP-C | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7c3a86f8-9345-3c99-b07f-e5ee96e78904 | -4.5087 | -50.748798 | 2024-10-28 00:49:39 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| facd726e-4499-336c-820e-a6c2cc9ff836 | -2.5742 | -49.229401 | 2024-10-28 00:49:39 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a804e9f5-44e9-3d81-9712-cf3ebee2a697 | -2.5758 | -49.236198 | 2024-10-28 00:49:39 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29e77a74-f3ca-3358-bae8-f8a70fa7088c | -2.4039 | -48.533501 | 2024-10-28 00:49:39 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 416c814f-5e43-3a65-822c-01ad28d67b36 | -2.4055 | -48.540401 | 2024-10-28 00:49:39 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6fa9232-7689-32fc-bf37-ec0d53131ebd | -2.4071 | -48.547298 | 2024-10-28 00:49:39 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42a62a37-9288-3583-ac02-5f1050b7a4f0 | -2.5644 | -49.231602 | 2024-10-28 00:49:39 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 587a7b95-1b98-3ce1-91d9-ace1433d3ee0 | -3.5968 | -53.7761 | 2024-10-28 00:49:39 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3aa2eb7c-7cdf-3530-96ea-75cca20a43e8 | -2.3941 | -48.535702 | 2024-10-28 00:49:39 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bce214cb-f30e-3c85-844e-7bf14ced1c6b | -2.3957 | -48.542599 | 2024-10-28 00:49:39 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8df570b8-6cbf-3ab0-8788-69c972497a25 | -2.3973 | -48.5495 | 2024-10-28 00:49:39 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
