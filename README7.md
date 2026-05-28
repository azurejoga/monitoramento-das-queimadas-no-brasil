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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56f99fc9-7a9a-301b-b6fa-efae9a5b7fc6 | -9.94647 | -48.01674 | 2026-05-28 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9cc7c350-4a63-3416-b46a-37cfd6e124db | -8.72802 | -48.33474 | 2026-05-28 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 060fad03-35b6-317d-a579-689a7ccd2c5d | -6.99408 | -42.8844 | 2026-05-28 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 252f179d-9e24-38c6-91af-6ac0c6ec245e | -10.63335 | -46.90281 | 2026-05-28 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 282c52b5-bc8d-37bc-a8ae-739eb818e515 | -9.28127 | -48.58916 | 2026-05-28 04:40:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bac73480-988a-318c-bc88-9c8154748201 | -10.77815 | -46.91171 | 2026-05-28 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0f609b30-57ce-3cb6-8e38-917f5131f931 | -5.95962 | -43.49097 | 2026-05-28 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 27804603-dd33-38f2-865f-2e41a9bc1cb7 | -10.62972 | -46.90224 | 2026-05-28 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1949fade-6f5a-3fc4-959a-958aacc228d2 | -8.68185 | -48.30893 | 2026-05-28 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2cd81c2d-65d2-3ad2-9677-ae1fc684b1ca | -12.32808 | -47.89979 | 2026-05-28 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| dfb7ed81-fdbc-3a1e-a3ab-f7935effe20b | -9.22187 | -47.51812 | 2026-05-28 04:40:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7eef4e3-c7f0-31f6-b37e-16478460296f | -9.35718 | -45.4634 | 2026-05-28 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| aca17e82-4d5b-3be0-a551-1ad430885487 | -6.99473 | -42.87991 | 2026-05-28 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| bd2c03cc-4386-3b00-b4d9-e4c1c51e36fb | -6.54244 | -44.68882 | 2026-05-28 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b58aeb5b-966d-3d28-84e6-63f76e414ad9 | -9.1429 | -51.28543 | 2026-05-28 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f6dec6e9-13a8-3e5c-9fce-bf745e461cb0 | -10.44538 | -59.43329 | 2026-05-28 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03ef9764-017f-3ba3-be18-de03a80870d0 | -11.16671 | -46.80865 | 2026-05-28 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 245e12c7-4df8-319f-b92c-46e67ba0396f | -8.43582 | -51.55208 | 2026-05-28 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4248480-43da-3217-a36b-698589971236 | -11.37941 | -47.93593 | 2026-05-28 04:40:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 882f9752-ec27-3e7b-b8ca-297136756591 | -11.64596 | -52.86101 | 2026-05-28 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cdf737fa-424e-329f-a17b-099bb8571dc3 | -8.7101 | -47.79899 | 2026-05-28 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48d93b00-a7f1-307b-bc3e-32404b53b343 | -12.32454 | -47.89927 | 2026-05-28 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 660eaec2-9a1f-347b-8ddc-563b912cdfb2 | -8.72911 | -48.32747 | 2026-05-28 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 083e7800-cb46-36e9-a946-787cd5cdfed1 | -10.62481 | -46.91033 | 2026-05-28 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 290e232f-1183-39ee-b752-97c45b7fec95 | -11.59354 | -47.4538 | 2026-05-28 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 1142f592-45b2-3d24-b676-889a59ec8276 | -9.34093 | -48.40134 | 2026-05-28 04:40:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c32f3821-b500-38f3-bdc7-a071f53dc5d6 | -9.38537 | -48.43813 | 2026-05-28 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a520e60-acd1-3ee5-a5a6-de1d77aeb3fd | -11.46899 | -52.91595 | 2026-05-28 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d7df7215-a1a0-3c7b-9a6d-fdd38f613649 | -9.39495 | -48.44336 | 2026-05-28 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00975c94-5f95-3a62-9ebe-34b65b16dd5a | -5.95539 | -43.49043 | 2026-05-28 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 32e0c625-c0c9-38c7-82c6-f14f58bc5fd7 | -10.95338 | -44.17667 | 2026-05-28 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c8a7621-2067-3c23-84ac-081a1333436c | -8.71353 | -47.79953 | 2026-05-28 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e99c92cb-570f-3c97-9418-1c4b6a863ac8 | -9.14625 | -51.28598 | 2026-05-28 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 15abd88a-44a1-3b6f-a384-cf7b87914580 | -10.48289 | -48.90615 | 2026-05-28 04:40:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7f70b422-2767-31ee-ba70-30c68e16fe18 | -9.35405 | -45.46439 | 2026-05-28 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b78b06f0-7a3a-31c3-90c2-dba56fb7ebd0 | -8.11824 | -49.56358 | 2026-05-28 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| effb1a8f-a742-3e65-8369-866e60dbe906 | -9.3955 | -48.43972 | 2026-05-28 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0a123ad2-7477-339c-b44a-6919f2f8427e | -11.16242 | -46.81234 | 2026-05-28 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d072b705-0b3f-34c2-b307-766d3bfa54ec | -10.14294 | -52.3992 | 2026-05-28 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eca89e67-bee8-3cdb-9ffb-297cdb8c121c | -9.34488 | -45.47322 | 2026-05-28 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c502b45e-8ce8-354b-b3bc-4fdeb82da5a4 | -9.15167 | -46.86423 | 2026-05-28 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e42b9aee-4f5f-3537-a932-b4df209c1712 | -10.05269 | -51.6813 | 2026-05-28 04:40:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9799620c-0221-385c-9a32-10a48b9d7bb8 | -9.34946 | -45.46881 | 2026-05-28 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bc42db0e-213b-3071-853c-b7b3fea48925 | -10.13613 | -52.40253 | 2026-05-28 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6210d8c0-e21c-3a24-b822-9f823d77bc71 | -8.90711 | -51.85168 | 2026-05-28 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f08f8da7-59b0-35ba-b1bd-733d1ee4c62f | -10.87298 | -53.73849 | 2026-05-28 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c63f8e82-5145-3303-93be-1587ec6ef974 | -11.82648 | -48.21286 | 2026-05-28 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d9b0f62a-70b6-35b5-9aab-6c48cb4dddd8 | -11.59116 | -47.44492 | 2026-05-28 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e50e2040-af30-36f6-8984-4f87bfca3983 | -9.99025 | -53.62619 | 2026-05-28 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 237187cf-2466-3102-8068-870c94da1490 | -8.72857 | -48.33111 | 2026-05-28 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4cddb48e-8a1b-3caa-9602-08701f0f50b6 | -11.47037 | -52.91938 | 2026-05-28 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1216978d-df0e-3b36-806c-9e4e5f895c4f | -9.13783 | -46.86814 | 2026-05-28 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df2e91d7-0d79-3934-b252-b46f2c6d9dd5 | -11.5929 | -47.45829 | 2026-05-28 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 458b94f4-cbf9-3149-9114-3fe95981b9ed | -10.77937 | -46.90307 | 2026-05-28 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 075d4328-51e7-3b3e-8c7f-1ee5b71a85dc | -9.39158 | -48.44283 | 2026-05-28 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8704caae-36fa-3f4a-8b4a-426651b8d44f | -11.28121 | -53.97171 | 2026-05-28 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23f20ee0-f67d-37ad-93e5-b204937ad98a | -11.58996 | -47.45328 | 2026-05-28 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| c5b9622f-c008-353a-a7fe-cf427d4d4fd2 | -5.9371 | -43.46538 | 2026-05-28 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 694296ea-c170-3791-8ba7-16729089ac78 | -12.60295 | -44.52359 | 2026-05-28 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31fba4c0-f42d-3dfc-849e-dbce2f978e2e | -10.8007 | -46.88424 | 2026-05-28 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c358e09-c7cc-3660-bb9c-53cfd25e80b9 | -11.81151 | -52.51552 | 2026-05-28 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c508f45b-4609-342b-8d2a-f4e83ab93f96 | -6.54638 | -44.68939 | 2026-05-28 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 135b8b7b-ac1a-3e43-8536-1a94c92eecc3 | -11.6425 | -52.86042 | 2026-05-28 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| bf78238f-179a-3cc5-8196-5002bca9eaba | -9.29245 | -48.58349 | 2026-05-28 04:40:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4087b054-8224-39a3-855a-f04b5d6b753f | -6.54579 | -44.69171 | 2026-05-28 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3db64b8d-818c-38c6-9f1e-7fbd6bc93121 | -9.35336 | -45.46938 | 2026-05-28 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 72364e21-4667-34d0-9489-dc309e8f948c | -10.56518 | -48.02633 | 2026-05-28 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d782a6fd-a3e8-3fc5-a789-09243dbcbbbf | -6.53923 | -44.68342 | 2026-05-28 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 83c7b055-eb36-3e65-949b-098567498b08 | -10.47899 | -48.90924 | 2026-05-28 04:40:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e095e89c-81d7-32df-ad91-feaa0274233f | -10.1445 | -52.13208 | 2026-05-28 04:40:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bed9c16d-67c6-31f1-85ca-abf5fc0bba7b | -10.63762 | -46.89909 | 2026-05-28 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee7756bb-8cd0-39f9-9b2f-785da9422396 | -9.05688 | -46.30318 | 2026-05-28 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa81761b-83cc-3229-aabe-ada607acdab5 | -5.10492 | -46.94818 | 2026-05-28 04:40:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e302953-dba1-317b-8011-fdb97fc30167 | -5.80615 | -45.12761 | 2026-05-28 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0162d29-0d67-3e4b-9498-87f1d3a4c022 | -10.70918 | -56.04611 | 2026-05-28 04:40:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 410e8483-0cae-34f5-81ee-78c79fac5876 | -11.27463 | -53.96605 | 2026-05-28 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3818af08-7241-3670-8329-c28934e23f5b | -10.04081 | -48.69074 | 2026-05-28 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 726789b0-91c6-3fe7-b670-0b7c25dcc198 | -5.79787 | -45.13115 | 2026-05-28 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 97af8a00-fe85-3d77-9611-36320cd1ad8a | -7.35299 | -46.21619 | 2026-05-28 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9165ea76-d7d9-32b7-bcb5-482aac37d62a | -6.99985 | -42.87602 | 2026-05-28 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| ce8fa118-b9b5-3bee-9de0-10f306058487 | -8.34059 | -51.92284 | 2026-05-28 04:40:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cf90d3b1-81b0-350b-9e24-5ab2d293e0fe | -5.95531 | -43.48811 | 2026-05-28 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7c82e7a7-202e-3134-95f9-7b3b02016689 | -7.71219 | -45.93666 | 2026-05-28 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a1ff9f19-24a5-3bc7-8300-76da7326d03b | -5.80684 | -45.12304 | 2026-05-28 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 406b9891-03ea-3d9d-87ab-4df30a82011b | -11.27756 | -53.97108 | 2026-05-28 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8683aa45-b6a6-3404-9805-957093c357c0 | -11.60191 | -47.44648 | 2026-05-28 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 68e2ce80-9d3d-3363-90fa-2f4c6e9cd5f7 | -8.68295 | -48.30167 | 2026-05-28 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ce729a1-a704-32f9-996f-a90a59253284 | -12.69179 | -44.78565 | 2026-05-28 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ceaa736e-ac7a-343c-a911-c91bbf48403d | -10.80133 | -46.87987 | 2026-05-28 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98a1d769-abed-3b92-a619-d0ce14d0bd3b | -12.69606 | -44.78625 | 2026-05-28 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c73b84d7-be5c-3902-a429-c573ab6857f4 | -10.62839 | -48.32946 | 2026-05-28 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c7e6d19-d38e-3ad8-8764-737bd8cf2b31 | -8.72629 | -48.32329 | 2026-05-28 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 53470263-2ebf-34c5-a280-9354b024bb0b | -7.40793 | -45.50384 | 2026-05-28 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebda3854-eaf9-374b-9762-e069d49ed959 | -12.60433 | -44.52594 | 2026-05-28 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5128d64-0ace-3e94-9219-5a2f92d65f09 | -11.47449 | -52.91607 | 2026-05-28 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d5177c58-4cd0-31e2-9b16-bba7f4693e78 | -9.05256 | -46.30698 | 2026-05-28 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 006d4775-30fe-3224-8dbc-ca2ed383e8e5 | -11.47247 | -52.91653 | 2026-05-28 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1b0bed17-88b5-32f3-8b4f-af9532ec8432 | -9.35645 | -45.46839 | 2026-05-28 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f267661d-fae6-33a3-aec0-a2bf0c048d2f | -8.72966 | -48.32382 | 2026-05-28 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6d031048-f250-37cf-8cc4-7ff2ae4ef274 | -9.35865 | -45.45992 | 2026-05-28 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README8.md)
