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
| c179fa8d-4d81-33b2-9bc1-b0aedb569b2c | -11.8939 | -57.1155 | 2026-06-29 00:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 38.1 |
| eb0e4672-816a-37ea-b9ec-d40f09c486f5 | -9.3327 | -58.0298 | 2026-06-29 00:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| e6744662-cdfa-3432-aae3-ec3fd689c748 | -8.774 | -63.6446 | 2026-06-29 00:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| eedc9382-2432-38da-a3ba-2adda41d96f7 | -9.314 | -58.0309 | 2026-06-29 00:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 722a6256-892d-39ad-a105-ceb54aa19a72 | -9.0796 | -59.4098 | 2026-06-29 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| af26c34c-cb95-3cfe-a1fd-0a7886fb975e | -9.0795 | -59.4292 | 2026-06-29 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 3c9a1939-0497-3e71-93d2-bd7f43279eea | -8.0127 | -46.2475 | 2026-06-29 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 5591b559-c76f-30e5-9b97-956e433d7fa3 | -11.2148 | -53.833 | 2026-06-29 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| ef132892-41ae-3691-ba5a-d863eceb786e | -11.8937 | -57.1355 | 2026-06-29 00:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 85ea8b7e-cb06-3dfc-a1be-f449d557fc63 | -9.0798 | -59.3904 | 2026-06-29 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 3c395de4-90a6-3db4-b8fb-e8533b717950 | -10.4821 | -46.584 | 2026-06-29 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 40ff776e-3f80-3ecd-a20c-2b86df2d8807 | -9.0798 | -59.3904 | 2026-06-29 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 7445e3d7-03b5-3722-81f1-5ec00f2213b3 | -9.314 | -58.0309 | 2026-06-29 00:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| aa5773c3-0850-3a79-a0b7-19448420a303 | -10.4631 | -46.5863 | 2026-06-29 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 147.8 |
| ad53233d-2dbc-32fe-a035-5e463d1bbe00 | -9.3327 | -58.0298 | 2026-06-29 00:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 5ad8a251-3b1c-3812-a237-c72954958393 | -11.209 | -54.3053 | 2026-06-29 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 86e05abb-4f37-3f37-8344-31cf1c3b0399 | -9.0796 | -59.4098 | 2026-06-29 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 240037b3-de0d-3321-a2ef-275d5ef01932 | -9.0795 | -59.4292 | 2026-06-29 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 85e406ce-dcc2-3338-ae2e-078aea5d6eb1 | -10.4634 | -46.5638 | 2026-06-29 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| d834d6f8-0cdd-3469-830f-2400acaaaecb | -9.0798 | -59.3904 | 2026-06-29 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| cbd2d825-4e1e-3622-a7f3-8321436f4977 | -9.0796 | -59.4098 | 2026-06-29 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 4370afcb-9b1b-386e-acc1-48f2af9115ae | -10.4631 | -46.5863 | 2026-06-29 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 46111982-506f-3962-8d56-537dc784c388 | -9.0795 | -59.4292 | 2026-06-29 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| c80d48a8-4e48-3659-922b-103bf1316199 | -9.3327 | -58.0298 | 2026-06-29 00:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| c3bdfe36-9e9b-384e-b7f7-32604cb735de | -11.209 | -54.3053 | 2026-06-29 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 84748ca3-1bde-392e-b7df-6225d5fdcf28 | -9.3327 | -58.0298 | 2026-06-29 00:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 38dc9de8-a500-32a2-9e26-47e15627d776 | -9.0796 | -59.4098 | 2026-06-29 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| cd7b1dff-4d9e-307c-8e07-7e50872112b6 | -9.0798 | -59.3904 | 2026-06-29 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 38f6725f-085c-3dbd-8ee1-5e9c94666e07 | -10.4631 | -46.5863 | 2026-06-29 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 8f10ed43-d9f9-3e52-80ed-57eb3cada1ba | -9.0795 | -59.4292 | 2026-06-29 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| ba19bcac-91c8-3d76-bf94-d11153fa8834 | -11.209 | -54.3053 | 2026-06-29 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 52314d42-cb9e-3a60-af68-f475b24b8efd | -9.0798 | -59.3904 | 2026-06-29 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| f5fd3edc-b4d1-3f56-b4e5-f68c42fa6a17 | -9.3327 | -58.0298 | 2026-06-29 00:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 7ba911e4-3fe7-30f4-8575-f2538dcff516 | -9.0796 | -59.4098 | 2026-06-29 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| afc33957-ea71-34b2-937b-5ee1e3f8b1f5 | -11.209 | -54.3053 | 2026-06-29 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 21dcddec-91c4-35df-849f-0afc49611e80 | -11.8937 | -57.1355 | 2026-06-29 00:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 6950410e-3364-3759-b671-2742aee80dd2 | -9.0795 | -59.4292 | 2026-06-29 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 3bfa0702-23c5-3dc0-a3b4-a0514643c2e3 | -10.4631 | -46.5863 | 2026-06-29 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| aa7f30a5-fd67-3698-af3f-4dd3d7116403 | -11.2279 | -54.3036 | 2026-06-29 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 41534aed-7a02-38f8-b59a-9d1e72b3e135 | -9.0795 | -59.4292 | 2026-06-29 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 364c76f8-0e98-3473-b683-44963bafe0ea | -11.2279 | -54.3036 | 2026-06-29 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 64f535a2-55b2-36c0-bd17-00b5ce985429 | -11.209 | -54.3053 | 2026-06-29 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| e20b70be-13a1-3c47-9355-6636ca153a64 | -9.0796 | -59.4098 | 2026-06-29 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 05182f25-b734-3cf2-aa3d-6b49d04a1596 | -9.3327 | -58.0298 | 2026-06-29 00:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| cfd48433-5de6-344a-8a80-26a0c03606db | -9.0798 | -59.3904 | 2026-06-29 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| ebfb3690-3893-367f-9447-d0078a642c2f | -10.4631 | -46.5863 | 2026-06-29 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 44c295b6-3720-3aff-add6-568d12f6d6de | -10.4631 | -46.5863 | 2026-06-29 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 5a84212f-0c4a-371c-ba44-0c644f819f4d | -9.0982 | -59.4088 | 2026-06-29 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 54b9261b-5fd6-35a7-bcca-46592ff67416 | -11.209 | -54.3053 | 2026-06-29 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| aea3398d-4177-3225-af36-fe8de5504c83 | -10.4627 | -46.6088 | 2026-06-29 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 2c0b5629-282d-37fe-8dd4-23e6200e247b | -9.0795 | -59.4292 | 2026-06-29 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| b94b83a5-dc05-3066-aef0-6d0e1174ebe2 | -9.3327 | -58.0298 | 2026-06-29 01:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 3671f2a0-d783-3c70-be39-510947f0993c | -9.0796 | -59.4098 | 2026-06-29 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| a735efe7-be6d-3419-b654-26b234d1810a | -9.0796 | -59.4098 | 2026-06-29 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 388dddbb-bb29-317c-bdb7-cf5ae8cd832c | -10.4631 | -46.5863 | 2026-06-29 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| fbba3bbd-1d4d-344b-9303-d69cebe888b8 | -9.0798 | -59.3904 | 2026-06-29 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 594d13b4-97cf-3be1-a6ca-c7db9c10feab | -9.0796 | -59.4098 | 2026-06-29 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| ffdf9bba-6de8-399a-b033-869aa69e2aed | -9.0795 | -59.4292 | 2026-06-29 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 37e01320-602a-3ece-852b-d5f6ce1cb93d | -18.78353 | -57.37633 | 2026-06-29 01:20:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.6 |
| 10ed607f-1366-3bec-8633-477e7eeb1058 | -8.76703 | -63.63395 | 2026-06-29 01:22:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2e6bc503-25fa-3a71-b17c-339c9e8b4577 | -9.31406 | -58.02153 | 2026-06-29 01:22:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 40.0 |
| c49bd91d-d413-3241-b48c-f261d63937ad | -5.40333 | -65.43433 | 2026-06-29 01:22:00 | TERRA_M-M | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 172e21f5-c09b-3781-a5ab-bb66d7123da6 | -9.32297 | -58.01293 | 2026-06-29 01:22:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 2ca57977-a74d-32fe-bcd4-eeb95f85a1da | -9.32984 | -58.01851 | 2026-06-29 01:22:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 75677f20-93ed-3871-ba91-3e0f85be7afb | -9.32859 | -58.04541 | 2026-06-29 01:22:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| d28b7b8b-2dc8-304e-92c6-84a05a682d3c | -9.10994 | -64.44068 | 2026-06-29 01:22:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6e8e3d09-0c3f-3ddc-b879-7882581a2d89 | -8.76532 | -63.6404 | 2026-06-29 01:22:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a219e68a-6518-31ee-a53e-4b80bd5c2ce4 | -9.0796 | -59.4098 | 2026-06-29 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 849fc1c2-0f8c-333e-93a7-085c9f340825 | -9.0795 | -59.4292 | 2026-06-29 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 21d2262d-5637-3665-9b22-053e322f9d86 | -9.0796 | -59.4098 | 2026-06-29 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 056d5eb2-3812-3a94-98a8-6dea5e80931a | -9.0796 | -59.4098 | 2026-06-29 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 03909810-aa0b-3a33-9cf3-8e51dde406d8 | -10.9882 | -49.5618 | 2026-06-29 02:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 8455011d-225a-3caf-9689-b35ebe20f80d | -10.2177 | -46.5038 | 2026-06-29 02:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| fc163d71-96fd-3af3-9fd8-24bd3b618da1 | -7.74356 | -44.18065 | 2026-06-29 03:34:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 811fd976-9521-3b3d-acf3-c8a9136598e2 | -4.8472 | -42.92934 | 2026-06-29 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e8bb2a77-bb68-3f2a-ba7d-be63a6ddb98e | -7.75025 | -44.18278 | 2026-06-29 03:34:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c95570f-2c88-3728-a356-14d9baff2c9b | -7.74235 | -44.1869 | 2026-06-29 03:34:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99464b31-67f4-3c1b-b425-028d6522fd68 | -13.85775 | -44.75504 | 2026-06-29 03:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e03e7b06-f13b-3cfe-a310-a28197e20a4e | -17.70571 | -46.78469 | 2026-06-29 03:38:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d02ea063-83de-368a-a6b9-373d2bc3efd1 | -19.8148 | -42.87759 | 2026-06-29 03:38:00 | NPP-375D | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2deb77d9-d709-3b76-a491-cc5a69297cd4 | -19.91766 | -42.32698 | 2026-06-29 03:38:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bc5f6b80-e3f0-3ddd-acae-862adfd269a8 | -17.61248 | -46.69026 | 2026-06-29 03:38:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f39c43c-9f55-34c1-a35a-0ab260882f02 | -20.47224 | -40.49797 | 2026-06-29 03:38:00 | NPP-375D | VIANA | ESPÍRITO SANTO | Brasil | 3205101 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8138a329-bc03-387a-adb3-0e526c9ae2a0 | -19.81718 | -42.87553 | 2026-06-29 03:38:00 | NPP-375D | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2b9d7f22-6538-3b6b-a36a-35a6c18d5aae | -19.81139 | -42.87762 | 2026-06-29 03:38:00 | NPP-375D | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 03ae3be7-f470-354d-8ba2-862255e2daeb | -19.81544 | -42.87453 | 2026-06-29 03:38:00 | NPP-375D | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a85b883b-11f3-3a39-91ae-63eed4d67b67 | -19.91814 | -42.32837 | 2026-06-29 03:38:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ba5d26ad-825c-352b-a9f6-f885b7117dd8 | -20.18845 | -40.23721 | 2026-06-29 03:38:00 | NPP-375D | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 20cc69b1-d4e8-3efb-95ac-b9f058c078d4 | -17.70043 | -46.77709 | 2026-06-29 03:38:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 589b1a26-5d78-3503-bc10-67720f8245c3 | -17.61106 | -46.69638 | 2026-06-29 03:38:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1dd3341b-e654-3461-872d-f9716785cb51 | -17.70717 | -46.77839 | 2026-06-29 03:38:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 235bdbc7-b1eb-3799-b5cc-236cb915de0f | -19.81205 | -42.87457 | 2026-06-29 03:38:00 | NPP-375D | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5bd03433-fd45-31c2-8666-44da010b8d29 | -19.80969 | -42.8765 | 2026-06-29 03:38:00 | NPP-375D | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c1e273f3-79b4-3ffe-a392-c24338040429 | -7.30291 | -46.29098 | 2026-06-29 03:51:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed4b0adc-b628-3922-a649-53eea8b36d9b | -7.74306 | -44.18475 | 2026-06-29 03:51:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| afd3e6a0-1d85-3227-817b-75c25d458fec | -7.7447 | -44.17556 | 2026-06-29 03:51:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 313e74e3-bfcf-3be9-bf74-c047e190da64 | -7.26612 | -43.22532 | 2026-06-29 03:51:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4c167313-8958-3aaf-aca6-38af7890194e | -4.84531 | -42.92846 | 2026-06-29 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b7eda6d-e598-3e37-955a-e021b027aaf0 | -7.74444 | -44.17861 | 2026-06-29 03:51:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4a3452c3-b064-3944-80e4-5867b6c0b83f | -7.74364 | -44.18329 | 2026-06-29 03:51:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README2.md)
