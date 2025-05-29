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
| 35123379-56d3-3dc1-b372-2fa954a15eb2 | -10.9521 | -48.1493 | 2025-05-29 00:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 0592c077-d06c-3fb4-b601-bd16241423a0 | -10.9711 | -48.1471 | 2025-05-29 00:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 23c995a2-ae06-3cd4-a440-85b7ef6f837c | -10.7458 | -49.2862 | 2025-05-29 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| d1c8bdf2-9093-38f8-8317-4833edc3b545 | -7.2405 | -43.0899 | 2025-05-29 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.9 |
| 7be049b1-3b2b-3f2b-a272-dfa2c5d76d9b | -9.2149 | -49.4655 | 2025-05-29 00:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 0abdb31f-872d-3639-a139-b58fa4c26e01 | -6.2226 | -43.3459 | 2025-05-29 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| aac6c3ee-796a-30a3-b1d1-b87ed8b5ceeb | -7.6406 | -45.9232 | 2025-05-29 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| fa7ad016-ab67-3252-803b-3b92ae3ee53e | -7.6762 | -46.0995 | 2025-05-29 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| ddb15787-a68d-3893-8969-641cba5fb6e1 | -11.818 | -44.2703 | 2025-05-29 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 2ff6cd7f-980c-36de-a2b9-9c0049edae63 | -10.9518 | -48.1714 | 2025-05-29 00:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 678d8819-549e-36a4-9e8d-21e530f297ee | -10.9521 | -48.1493 | 2025-05-29 00:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 134.5 |
| a1ddf4c4-d6fe-3cf6-b618-91abd9c35859 | -10.7269 | -49.2883 | 2025-05-29 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 27c9bd7a-bb77-30b8-98b2-a81f1363bade | -7.0695 | -44.9335 | 2025-05-29 00:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| bda87076-b770-3977-8007-988283094fed | -6.2226 | -43.3459 | 2025-05-29 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 310209a7-fc74-30b9-bd9f-9484ac5561a7 | -11.818 | -44.2703 | 2025-05-29 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| f41159db-e4a4-347a-b37e-6fb80e2a8816 | -7.2405 | -43.0899 | 2025-05-29 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 54.0 |
| 1d8aa9c9-94aa-34e1-9cd9-acb12068252e | -10.9518 | -48.1714 | 2025-05-29 00:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 2ab7b63d-dfb7-3750-9a21-42a908981dca | -10.6391 | -48.7987 | 2025-05-29 00:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 766ef9b2-b0a8-3603-ae70-3a27f1cffdf1 | -6.2226 | -43.3459 | 2025-05-29 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 18fe48a8-29cf-3d94-b305-b023577e0ae8 | -10.9521 | -48.1493 | 2025-05-29 00:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| c3f68177-f5e2-37ca-a214-2fc554eade9c | -9.2149 | -49.4655 | 2025-05-29 00:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| a21601ef-8492-3310-a45c-60f72fe7a52d | -7.6762 | -46.0995 | 2025-05-29 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| f3386d1b-afdc-38e5-b197-7ecb4b3eda36 | -7.0695 | -44.9335 | 2025-05-29 00:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| b7149d01-7f1b-3435-afd1-66ca338777ad | -7.2405 | -43.0899 | 2025-05-29 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 63.1 |
| cdc4ebf5-eaa6-389e-8591-fffd9a7b2760 | -11.818 | -44.2703 | 2025-05-29 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 71a50aa9-c6e1-3a4c-9034-71f5bf4408f7 | -10.9711 | -48.1471 | 2025-05-29 00:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 78d77e06-06c7-3856-a6a3-6345442fa3cb | -11.818 | -44.2703 | 2025-05-29 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| ea959a55-0416-30be-be29-a52c04b02ea5 | -7.6762 | -46.0995 | 2025-05-29 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| ef9a44c3-bd85-3a34-87f5-d7ca41c435ee | -6.2226 | -43.3459 | 2025-05-29 00:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 75ed827a-e818-3629-8856-9c51e67e2916 | -9.2149 | -49.4655 | 2025-05-29 00:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| c9213d20-2555-3aa4-bc61-f9575a346803 | -10.9521 | -48.1493 | 2025-05-29 00:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 8a173abd-1a19-367e-b0a6-4dc1e2d13e18 | -11.818 | -44.2703 | 2025-05-29 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 0f005330-6410-39ee-8967-8853b6955493 | -9.5725 | -40.3227 | 2025-05-29 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 58.1 |
| 92d18921-e48c-37e7-8c75-593937d63cc2 | -6.2226 | -43.3459 | 2025-05-29 00:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 1f6bf74a-dabd-317c-9973-bd3999f2d4f6 | -9.2149 | -49.4655 | 2025-05-29 00:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 52d8335e-b3ba-3679-88c1-747d8399ad85 | -10.9521 | -48.1493 | 2025-05-29 00:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 1e6462fe-cda2-32da-b708-9b08df9b4e62 | -7.2405 | -43.0899 | 2025-05-29 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.9 |
| 53425ec5-1652-3234-a20c-0aa87d7a8c00 | -7.2403 | -43.1134 | 2025-05-29 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 47.5 |
| e339c12d-38a9-3328-95ff-0cbc18423729 | -6.8285 | -44.6578 | 2025-05-29 00:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| fc0019ef-aae8-3d78-8e8b-1fa94d53ad19 | -10.9521 | -48.1493 | 2025-05-29 00:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 8c6d3c97-c4d8-3daa-8ed9-c27629175596 | -11.818 | -44.2703 | 2025-05-29 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 9a96ec11-b759-3055-a1a0-3159d8d9e749 | -9.5725 | -40.3227 | 2025-05-29 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 40.7 |
| e4627bf2-ad90-3449-a3e8-2b0818330ad0 | -9.2149 | -49.4655 | 2025-05-29 00:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 22293eeb-1ecf-3cb8-8f43-e2a2f003908d | -7.2405 | -43.0899 | 2025-05-29 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 106.8 |
| 7d6e8e03-47c5-38cd-bef6-478aec2b7947 | -7.6762 | -46.0995 | 2025-05-29 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 01b7729d-b7b9-3e1a-a616-b3d455cf4220 | -14.66752 | -45.08334 | 2025-05-29 00:54:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| fd84e117-2b60-3b19-87da-e18cf5e513b3 | -18.38371 | -44.51843 | 2025-05-29 00:54:00 | TERRA_M-M | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 7a43e1ff-fd92-32dd-a910-79b6979e7add | -14.66376 | -45.09 | 2025-05-29 00:54:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| bd78984f-be00-34bf-ba22-0bc29d582b63 | -10.6499 | -48.8054 | 2025-05-29 00:56:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4665b5fa-e7f4-3c23-987e-8b6523aa21e5 | -8.75137 | -49.76673 | 2025-05-29 00:56:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 08fa27df-ec37-3ce7-9c59-0bd833caa0b5 | -11.29553 | -46.45019 | 2025-05-29 00:56:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| b1780fdb-d07d-3f25-be3f-abd4e3db6713 | -9.21318 | -49.47548 | 2025-05-29 00:56:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 33.0 |
| abfa0f82-075f-3973-ae3a-59bea93091a9 | -8.78853 | -47.95065 | 2025-05-29 00:56:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3b6e3146-501a-3c70-aba6-4e3d6b8ae403 | -12.30247 | -47.27211 | 2025-05-29 00:56:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 386fa07e-c92e-3ced-b11e-7b863e303c74 | -7.68434 | -46.10728 | 2025-05-29 00:56:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |
| a4315ef1-418e-3da1-8bc5-055251b1457a | -10.95059 | -48.14629 | 2025-05-29 00:56:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 707bc2c1-edb0-3180-8635-e2369d31491e | -10.95249 | -48.15866 | 2025-05-29 00:56:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 2379f5c4-f271-3956-8571-00a08f253e35 | -9.39256 | -48.41998 | 2025-05-29 00:56:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 10942c79-20b1-3702-8dc6-46b7d9c59da3 | -7.67157 | -46.10929 | 2025-05-29 00:56:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| cacf3c55-916a-349b-a7ee-1967502aa86f | -7.18167 | -43.09763 | 2025-05-29 00:56:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 44.4 |
| 232df352-a382-32b6-a65b-3bb6cf51efd4 | -7.23628 | -43.12473 | 2025-05-29 00:56:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.6 |
| 2a7a19e3-79be-38f2-bb37-4e12bb6141d8 | -10.19086 | -52.65103 | 2025-05-29 00:56:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d94e2a3b-28bd-37e6-a285-1c2231def469 | -7.06836 | -44.93714 | 2025-05-29 00:56:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 6f7808b8-e1e6-33e2-84c4-c1c545aab844 | -10.71865 | -49.54434 | 2025-05-29 00:56:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6f1b9543-2f81-3d26-b250-c90b36df61fa | -11.13392 | -53.9206 | 2025-05-29 00:56:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d32101fc-bbbb-33c3-ab23-a5a4081f712b | -10.96273 | -48.15695 | 2025-05-29 00:56:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 3e2ba5fd-08ee-3ee5-9fa9-65192db3bf0c | -7.62988 | -45.93046 | 2025-05-29 00:56:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 0eb3fa5f-3f3d-35b0-b64b-37b0a3cae04b | -10.73443 | -49.29041 | 2025-05-29 00:56:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| c63d77a1-dc77-3849-9529-2e29fb0a2e1e | -11.81336 | -44.25481 | 2025-05-29 00:56:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 18a78546-cc1e-39f3-8b3e-7b0f620cc1f3 | -11.14591 | -53.93945 | 2025-05-29 00:56:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c8b3de65-ee22-3389-9ec1-b61c0c575f12 | -8.6657 | -48.28284 | 2025-05-29 00:56:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e1b5db0c-da49-346d-bfc0-018233cddad9 | -8.19506 | -49.81221 | 2025-05-29 00:56:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 7806e2e6-0d4f-3aa0-8fd6-4ec74969d2b6 | -8.19659 | -49.8228 | 2025-05-29 00:56:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 612ae4be-25a4-3529-8768-13bacc93e43b | -10.63838 | -48.7957 | 2025-05-29 00:56:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 27a5df05-b03c-33f6-870e-c7b98b3215a5 | -7.19139 | -43.10126 | 2025-05-29 00:56:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| f9f0a461-c5e3-3587-ab59-5e25793b3bc1 | -8.75288 | -49.77724 | 2025-05-29 00:56:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 03354b4c-82bc-3606-9ea5-7d64ce8e137f | -12.27526 | -49.53143 | 2025-05-29 00:56:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 980d2e67-201e-365f-b0f5-d3d056333ef1 | -8.01635 | -49.69269 | 2025-05-29 00:56:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 22a9edcd-2560-3f3f-896a-5b2ab378f56b | -7.23716 | -43.08141 | 2025-05-29 00:56:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| 85bb913e-b304-3a31-bf30-86f5e2163b89 | -7.5802 | -45.85961 | 2025-05-29 00:56:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 3918e955-1f63-3fc9-b0c9-88ee5eded40e | -12.32256 | -49.98341 | 2025-05-29 00:56:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3bdfd548-1bff-31b2-bc3f-c6c17a70a45d | -13.19472 | -49.31653 | 2025-05-29 00:56:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f4d84feb-66b2-343e-a53f-d532d39d6d2f | -11.92871 | -44.55628 | 2025-05-29 00:56:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 49184966-aa15-3caa-b99b-0142dda8d17f | -6.82369 | -44.64337 | 2025-05-29 00:56:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 1845bb64-5619-30bf-8c79-eca0257d6b48 | -5.21497 | -43.30601 | 2025-05-29 00:56:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 14ee087c-d77f-30a9-938f-7c7d981c0a1f | -11.92004 | -44.5643 | 2025-05-29 00:56:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 56bfd9f7-7027-39c8-b6fd-c17fcda4fd8a | -10.72808 | -49.54292 | 2025-05-29 00:56:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 7a1a5a10-7bd2-35d0-88cc-d2e2422853de | -12.38619 | -49.97372 | 2025-05-29 00:56:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| dfb9a32f-f6ed-36a0-9ec5-48f4eb26c863 | -10.72016 | -49.55466 | 2025-05-29 00:56:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c02df5e5-8af3-3c61-9443-2fb0370b36ff | -10.46917 | -47.9436 | 2025-05-29 00:56:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| fdf0dc4f-4208-3a3d-8e76-14044c7c1639 | -7.94527 | -44.86075 | 2025-05-29 00:56:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 74e84640-3f74-386a-abbc-95d149493182 | -7.24309 | -43.11642 | 2025-05-29 00:56:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 127.7 |
| 2e1f2a48-1108-3db4-afec-51d2b0322081 | -8.74183 | -49.76814 | 2025-05-29 00:56:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 7e7927e7-1d49-3a4d-9dc5-30d3c4d95e9b | -13.0785 | -45.28829 | 2025-05-29 00:56:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| bd2e4224-16a3-32c4-91dc-953f5baba7c9 | -7.68122 | -46.08745 | 2025-05-29 00:56:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 35eb856e-949d-3ba3-9cbc-d62d7921236f | -11.8173 | -44.27826 | 2025-05-29 00:56:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 93e08538-d87f-3df8-beba-10b470d72042 | -12.32396 | -49.99298 | 2025-05-29 00:56:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| d1feae17-bed8-32e0-9724-5057a6a62631 | -10.64004 | -48.80699 | 2025-05-29 00:56:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 88808e27-71f2-3f7e-a8d9-8d7c405eda6f | -13.09079 | -45.28613 | 2025-05-29 00:56:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 41267414-bc7e-345f-b3ed-b0fd874a6a72 | -10.65453 | -49.43777 | 2025-05-29 00:56:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |


[Clique aqui para ver as próximas entradas](README2.md)
