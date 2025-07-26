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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6d4c6bd-406f-3dee-8efb-98ceac405dd5 | -16.2765 | -49.9387 | 2025-07-26 01:40:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 7472e70a-96dd-3166-b6e8-1ae096718d80 | -8.8686 | -45.5747 | 2025-07-26 01:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 7d142e3a-b43a-35f1-800b-c0d057e4a56f | -16.2564 | -49.964 | 2025-07-26 01:40:00 | GOES-19 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 33b2cc1f-23dd-3e9d-9d04-2ace462be730 | -8.8875 | -45.5727 | 2025-07-26 01:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 6f1d45e1-b4cd-32a4-aa98-108dcb650fba | -16.2569 | -49.9419 | 2025-07-26 01:50:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 19a4c21b-e140-3c91-b4a6-9a7db4f2e8b3 | -16.2765 | -49.9387 | 2025-07-26 01:50:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 03d41f6a-309b-3b92-bff9-ce0f878f3e0d | -16.2564 | -49.964 | 2025-07-26 01:50:00 | GOES-19 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 805fe39a-634d-3145-ba65-3fea8bd78880 | -6.5441 | -56.2508 | 2025-07-26 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| e66dd3dd-9acf-3235-ad63-52907fd540d4 | -6.1549 | -42.6001 | 2025-07-26 01:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 157.4 |
| 8e602090-d531-312e-872e-05de9d35a5d0 | -7.2408 | -43.0664 | 2025-07-26 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.1 |
| 6834748b-8151-38b2-9a10-ffa3f1b5174b | -9.8169 | -46.7076 | 2025-07-26 01:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| bc9c3fdf-50e6-3bdf-9fdb-b332d511adee | -4.0754 | -42.5344 | 2025-07-26 01:50:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 52.1 |
| 29b3a43f-45ef-3df6-a928-3bf4e9e00274 | -3.3957 | -47.5003 | 2025-07-26 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 1f67fa90-ec6e-35d2-bfe4-fb3a3a12089e | -16.2761 | -49.9608 | 2025-07-26 01:50:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 51242991-3eb8-3769-a388-cf93336f9b24 | -6.1551 | -42.5764 | 2025-07-26 02:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 62.7 |
| db533fcf-7643-35be-a2f3-e93620dc701d | -7.2408 | -43.0664 | 2025-07-26 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 111.4 |
| 3b30f388-1de5-3b95-8109-654b7547e8f8 | -6.1549 | -42.6001 | 2025-07-26 02:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 143.9 |
| 7221db84-ea49-3920-aa2c-ea97bd2e2402 | -3.3957 | -47.5003 | 2025-07-26 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 784b0e8a-5a39-327c-8b24-e4c2119328a0 | -4.0754 | -42.5344 | 2025-07-26 02:00:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 60.9 |
| 9f91fc60-ad1b-329f-879f-152648a42bb6 | -6.5441 | -56.2508 | 2025-07-26 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 80bbf3b0-dd70-39d6-beac-21a9f54f7219 | -6.1549 | -42.6001 | 2025-07-26 02:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 112.0 |
| 5ddff17f-5581-36d4-9a1c-d14ab40c6fbf | -9.363 | -40.3031 | 2025-07-26 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 63.4 |
| 6b5c924f-655e-3532-940e-730689f7b99c | -3.3958 | -47.4785 | 2025-07-26 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 239932c0-42cf-3291-a547-fcbae35d2cda | -7.2408 | -43.0664 | 2025-07-26 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.9 |
| e1365697-6c03-35d5-be11-eab684130f93 | -3.3957 | -47.5003 | 2025-07-26 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| fe44c956-506d-30af-890c-6063cb956fed | -6.5441 | -56.2508 | 2025-07-26 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 3d2c83ff-94d2-33d6-9ca6-74251110d85c | -6.1549 | -42.6001 | 2025-07-26 02:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 100.9 |
| cf21e4f6-a5f2-3384-8711-a03578d11d2b | -6.5441 | -56.2508 | 2025-07-26 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 0332d260-b972-319f-abed-94b985be498e | -7.2408 | -43.0664 | 2025-07-26 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 107.5 |
| 4972bd61-75ac-3b3b-a75c-459a913a1af8 | -9.363 | -40.3031 | 2025-07-26 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 915292e9-cefe-34db-abf6-602175640410 | -9.3626 | -40.328 | 2025-07-26 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 60.0 |
| a6031fff-65e3-32f8-a6c0-0282d68e87ea | -6.5441 | -56.2508 | 2025-07-26 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 6bda4c2e-8c5b-39f1-b423-52307685da5a | -9.363 | -40.3031 | 2025-07-26 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 122.7 |
| 802ef4d1-3a20-3753-844f-2dec7bc44b9e | -6.1549 | -42.6001 | 2025-07-26 02:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| 3a663a0b-082f-3988-b801-25fef74d4d3f | -7.2408 | -43.0664 | 2025-07-26 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.3 |
| d843ebe9-ab47-317e-93e1-96554310beee | -13.2443 | -40.587 | 2025-07-26 02:30:00 | GOES-19 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 0bbac752-52d9-313a-8083-6d71da2c01a5 | -6.1549 | -42.6001 | 2025-07-26 02:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 82.7 |
| 7f5cbf96-9220-31a6-afbe-f4ac2a7d390f | -9.363 | -40.3031 | 2025-07-26 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 14df9f2f-2d63-3dab-9987-39d37e78ef29 | -3.3957 | -47.5003 | 2025-07-26 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 642feda6-1ca6-3000-9883-3456f90b2fa8 | -7.2408 | -43.0664 | 2025-07-26 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.5 |
| bf50616a-3fab-3c4e-b407-cf190c8bf72d | -9.3626 | -40.328 | 2025-07-26 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 91.8 |
| f2b12441-2f5f-33e2-87c0-97817d00ae25 | -9.363 | -40.3031 | 2025-07-26 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 184.9 |
| ac8852e5-2e6a-3aee-a94a-0bd25fb78337 | -9.3821 | -40.3004 | 2025-07-26 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 65.2 |
| b2c9c8ba-8149-3d09-a672-eebf6e9388ef | -6.1549 | -42.6001 | 2025-07-26 02:50:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 73.3 |
| 68a75cee-be94-3d67-a08a-e4be3da12778 | -7.2408 | -43.0664 | 2025-07-26 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.2 |
| 08cf1114-1cc8-39e4-974b-138060c0f112 | -3.3957 | -47.5003 | 2025-07-26 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 3adf0ffa-b021-32c1-90df-af3eed9ecd8a | -7.2408 | -43.0664 | 2025-07-26 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| 1aa6362d-941b-3a5f-aeb1-7487c1040e4f | -9.363 | -40.3031 | 2025-07-26 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 229.5 |
| e04399bc-e31d-3e09-b4f1-eb98cb05153b | -6.1549 | -42.6001 | 2025-07-26 03:00:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| 8375eff7-990e-302c-a607-c8be76297f8c | -9.3626 | -40.328 | 2025-07-26 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 107.3 |
| b4cfe759-bad3-3c07-ad51-66a9b1e611a7 | -7.2408 | -43.0664 | 2025-07-26 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| 704a3a05-63ee-3498-835e-579545736582 | -3.3957 | -47.5003 | 2025-07-26 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 8a91981e-8fb4-347d-8cd7-d63fe3d2b4af | -9.363 | -40.3031 | 2025-07-26 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 66.8 |
| d497de4f-c255-3e15-b57f-1ed77dd3b662 | -6.1549 | -42.6001 | 2025-07-26 03:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| fe777a2e-3c81-3995-8686-cca9e1aef253 | -7.2408 | -43.0664 | 2025-07-26 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.6 |
| 2cc0144e-d54c-3cbd-85c9-e6beada08637 | -14.9528 | -46.9388 | 2025-07-26 03:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 57491196-148f-3173-bfc5-3380a6a67847 | -7.2408 | -43.0664 | 2025-07-26 03:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| e00d0443-3412-3d7f-a9e2-ed11a8132470 | -14.9523 | -46.9616 | 2025-07-26 03:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 58fcafc1-0871-33b0-99c3-640b06dd7cce | -7.09951 | -44.38081 | 2025-07-26 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6528e95-7e5e-3195-8cfd-437f1e0652f4 | -6.56804 | -41.49567 | 2025-07-26 03:36:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d4506fa9-4ea0-3b25-8237-cd832e0d33e3 | -8.17158 | -43.21132 | 2025-07-26 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4400b470-5389-362a-ae08-f937875fd8e4 | -7.24073 | -43.06573 | 2025-07-26 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b7382b32-20aa-3026-9980-cb5a3ffbf9e5 | -6.5614 | -41.50549 | 2025-07-26 03:36:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 407fe1da-af8f-393b-8a29-d4f81e467f2a | -7.24487 | -43.07312 | 2025-07-26 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 1e9c36dd-63f7-336a-b8c1-8550a83ebe29 | -6.15603 | -42.59849 | 2025-07-26 03:36:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| b9adf764-7299-33db-87fe-bb208a0a0319 | -6.15714 | -42.59207 | 2025-07-26 03:36:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| d313e46e-5a18-365f-9571-fb8c86d0fe1a | -8.17442 | -43.22548 | 2025-07-26 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 5ecc219d-fc41-38c1-be06-2f01a7f826bc | -7.23603 | -43.06156 | 2025-07-26 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1b22e5bd-25a7-35d8-94ab-3ff82ada7641 | -5.74333 | -43.96307 | 2025-07-26 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c039fab-a601-30e8-baae-4399f413a583 | -6.90548 | -44.29509 | 2025-07-26 03:36:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a6d748e-c67a-3ead-86b2-73c6b5e58e84 | -6.70115 | -43.06174 | 2025-07-26 03:36:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ec61f4c-aa5c-389b-a745-d6d6c2c81dc5 | -6.7854 | -44.10286 | 2025-07-26 03:36:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bc5ddc6-ede5-3d11-b4ea-b025371e2db1 | -5.77501 | -43.64521 | 2025-07-26 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 84b21503-5579-37fc-94f6-1f5fbbfe1c4a | -6.88114 | -43.67922 | 2025-07-26 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66e74e1b-176b-33d9-83bb-58a5eadac7f8 | -7.53539 | -42.42271 | 2025-07-26 03:36:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 601295d7-4189-33e1-9d7e-e163a2883f6c | -8.00166 | -45.04528 | 2025-07-26 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da659635-01c3-3270-a466-1d7bcd5e31c0 | -7.24309 | -43.0831 | 2025-07-26 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 047afcf7-4775-38a5-8e9d-4fedd010ba5f | -6.5276 | -44.59565 | 2025-07-26 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1402c221-1f5a-3449-ab84-b2028216f239 | -6.70175 | -43.05836 | 2025-07-26 03:36:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9bd2459d-5806-3ac8-954b-68c6f1ec975e | -6.87493 | -43.68205 | 2025-07-26 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8717feef-4c11-3428-a703-f6fbdeeb45e2 | -6.70056 | -43.06507 | 2025-07-26 03:36:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 118f3642-ba8d-3708-8cf9-ae805c597629 | -6.86871 | -43.68497 | 2025-07-26 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 07078290-6f33-3f23-ba02-708fe6728adc | -5.73755 | -43.96774 | 2025-07-26 03:36:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae59b009-7796-3a13-ac60-ad5f632164ea | -6.86721 | -43.68883 | 2025-07-26 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9a8a7150-fb1e-3ff9-89ac-264589b5a621 | -7.23368 | -43.07465 | 2025-07-26 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 95608f95-290f-3dab-a654-cc90445033d3 | -5.48173 | -42.15386 | 2025-07-26 03:36:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 71e2988a-3686-3afe-a8bd-75b1b66c4fc1 | -6.78289 | -44.10672 | 2025-07-26 03:36:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07c125d4-4234-3e4b-b7d9-79985cfd8eeb | -6.15547 | -42.6017 | 2025-07-26 03:36:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 2a359df1-83f2-3ecc-a669-65b508950c2e | -7.25016 | -43.07402 | 2025-07-26 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 7aaae7d6-cefe-30a2-8b33-4708b801d1b4 | -4.96392 | -43.22069 | 2025-07-26 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b3d970a-55d9-31c2-b765-868f7424b609 | -4.96456 | -43.21694 | 2025-07-26 03:36:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f061651f-6def-3107-9600-55b1ec8ce517 | -8.17503 | -43.22212 | 2025-07-26 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| cce85361-c8b5-3b6a-ab57-050ed0689a10 | -6.87622 | -43.67466 | 2025-07-26 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b5a0aa72-f3fc-3d7b-bff2-1a1c97cc4036 | -6.15191 | -42.59128 | 2025-07-26 03:36:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 0d72ed11-fe2e-384c-a0b8-0eedadf86c96 | -7.23957 | -43.07222 | 2025-07-26 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 5ebbdc8a-c9d6-329a-996a-59e3c5fbc7d2 | -7.17507 | -43.49453 | 2025-07-26 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 18bc27f6-e29d-3348-9c2d-a274b3c1dc86 | -6.72197 | -37.12435 | 2025-07-26 03:36:00 | NOAA-21 | SÃO JOÃO DO SABUGI | RIO GRANDE DO NORTE | Brasil | 2412104 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c57f41cb-f0ec-3f0b-ad0f-ca10a1884aaa | -4.77736 | -45.33331 | 2025-07-26 03:36:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1bd1ec28-bab0-322f-8bf2-70bd473bc385 | -7.04239 | -40.4092 | 2025-07-26 03:36:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 7d9b8c97-0cd1-3845-905c-27c709ab178f | -6.86378 | -43.68047 | 2025-07-26 03:36:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README4.md)
