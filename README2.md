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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77714a70-42f3-3606-85d6-b70e3dc42abc | -10.7728 | -50.254799 | 2026-06-23 00:36:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 22e8ff0b-20bf-33d0-9819-b20370507a26 | -12.4961 | -48.252899 | 2026-06-23 00:36:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b2ce88d1-93d0-34fa-a86a-8c369b90d8d7 | -9.2141 | -45.3153 | 2026-06-23 00:36:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| aab8ab1c-da0b-3ebc-92ca-2889cf04104b | -12.8746 | -44.3357 | 2026-06-23 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 6ce05f61-52e2-3154-ae1c-963ce6d7f586 | -5.8319 | -45.0559 | 2026-06-23 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 12a2ab61-b157-3b4e-8d39-7847374571ef | -12.8548 | -44.3625 | 2026-06-23 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 295.6 |
| eb642ae7-6b49-308c-ba8f-eebf1bfce3a6 | -12.8741 | -44.3593 | 2026-06-23 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 282.2 |
| f7ea5ee6-bf10-3f13-a216-f3fd559ea9bf | -12.4283 | -58.4048 | 2026-06-23 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| b88e3063-c6f7-397a-a70c-e2cbd5881737 | -12.8552 | -44.3389 | 2026-06-23 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 3dcf9b4d-34db-37bd-965d-4cd31a0cc55b | -11.81095 | -47.3501 | 2026-06-23 00:41:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 6f1dd8c5-5d9b-3084-9097-fbdb497aaafb | -12.6554 | -47.68559 | 2026-06-23 00:41:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 40.4 |
| e2b924ff-b076-356c-9c17-e7c5c972f3f9 | -11.80421 | -52.52235 | 2026-06-23 00:41:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 4838f60c-8397-31cf-8d42-2dbac06e3ef1 | -12.51944 | -48.29415 | 2026-06-23 00:41:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 3548cc66-8b10-3672-98e3-41cc7c2d2373 | -12.49931 | -48.26759 | 2026-06-23 00:41:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 5fa960c7-6e35-3372-852c-58f6ea825e12 | -12.54793 | -57.18742 | 2026-06-23 00:41:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7221f1ed-c3a5-305c-9f37-f29b1253da66 | -12.50132 | -48.27398 | 2026-06-23 00:41:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 38.6 |
| afde2ca3-7bd4-3383-83de-d4296e90a314 | -13.50378 | -56.5752 | 2026-06-23 00:41:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 27.0 |
| f1f9dbf8-d093-3d46-bb96-56e8111df996 | -12.92263 | -49.48313 | 2026-06-23 00:41:00 | TERRA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 5b01fdac-f2a3-3f45-97e7-7d63ca853ffb | -11.80113 | -47.3451 | 2026-06-23 00:41:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| de9691a4-4596-3f91-9285-b6e022d03cc5 | -11.57655 | -47.44275 | 2026-06-23 00:41:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 7c187cb3-cad9-3ffb-b54f-0c0b26c80d5c | -11.80644 | -52.53642 | 2026-06-23 00:41:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 7c0311ef-48e4-3521-a9c6-f3d6dcc7ca7d | -11.80249 | -52.5285 | 2026-06-23 00:41:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| de6b3f0f-3b03-30a7-abad-d4e4391881d8 | -11.8134 | -52.52673 | 2026-06-23 00:41:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 64223ce3-a31f-31f7-ac9d-196883ab7f4e | -12.5212 | -48.3004 | 2026-06-23 00:41:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 5077eaff-33a4-3f44-8bc6-58cc14c639b0 | -12.54917 | -57.19644 | 2026-06-23 00:41:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c05082d6-d2af-3965-b578-373abda7bf92 | -12.87751 | -49.84349 | 2026-06-23 00:41:00 | TERRA_M-M | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 16e7b7a9-30fb-3587-9dbf-c2f89ba22dba | -12.47133 | -55.12775 | 2026-06-23 00:41:00 | TERRA_M-M | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 741268cb-f089-39c8-99e1-5418ae9365ed | -11.29799 | -54.72321 | 2026-06-23 00:43:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6cee629d-0b6a-37f8-9622-51f22cb7d385 | -12.28842 | -57.5752 | 2026-06-23 00:43:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 5d6b27ea-d9f0-388c-873b-08931271a4b3 | -10.77055 | -54.11763 | 2026-06-23 00:43:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c3bd9624-90c6-3370-ac8d-c1c157ad194d | -10.11723 | -52.20355 | 2026-06-23 00:43:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| ff5eee8f-996b-392f-b939-5ce00a9c2c17 | -12.43761 | -58.41611 | 2026-06-23 00:43:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 48c0e59d-db5b-3eda-8b11-21c111ae170b | -9.93223 | -55.1705 | 2026-06-23 00:43:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8ea2b5be-4983-3fe5-be68-2ca763b1311c | -11.27483 | -55.7864 | 2026-06-23 00:43:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b16b5ff9-013a-3d13-a602-16efec5db8f8 | -12.42724 | -58.40781 | 2026-06-23 00:43:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 25.9 |
| d071c582-8e44-3bd4-8d39-b56226d1ead8 | -10.27724 | -60.54929 | 2026-06-23 00:43:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 323f276f-6256-3336-9ac1-1532970a8a50 | -10.93555 | -56.84786 | 2026-06-23 00:43:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 39c341fa-25e3-36f9-aaa1-5c4c46ccae14 | -10.57789 | -57.31652 | 2026-06-23 00:43:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7bc37274-851f-30c9-acdc-31ba699ceed7 | -9.90415 | -58.5306 | 2026-06-23 00:43:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 30e2db5c-294b-305f-988d-1b4084b51ac8 | -9.17695 | -58.05746 | 2026-06-23 00:43:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 1967d73b-54c5-3690-9efc-b2737208a50f | -11.05608 | -52.46415 | 2026-06-23 00:43:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| d37cc6de-c7cb-34dd-bb80-529f4b6cc790 | -11.48023 | -57.11595 | 2026-06-23 00:43:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 49e11939-ea0e-3f2a-9807-c9adae5381d9 | -9.45354 | -49.83583 | 2026-06-23 00:43:00 | TERRA_M-M | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 3fb22ba1-3fa5-3dcd-b8ff-1dd0218529c0 | -12.43634 | -58.40654 | 2026-06-23 00:43:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 2fc8e24a-a5ca-3e0e-9519-84c705dbea04 | -10.92671 | -56.84915 | 2026-06-23 00:43:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3005e9af-2ec2-3240-a574-684592c36029 | -10.02195 | -59.3505 | 2026-06-23 00:43:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ee7ce4bd-4d08-37c8-af98-7f3f2cdb2078 | -11.04497 | -52.46586 | 2026-06-23 00:43:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| dbf65cee-d00e-32dd-b7a5-91daf74a89d5 | -11.31306 | -54.72518 | 2026-06-23 00:43:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 46f76f9e-299f-3605-9ae4-73501fb01883 | -10.87518 | -49.54417 | 2026-06-23 00:43:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| bb86ec69-c5bc-34d5-be20-13439f757da6 | -11.31151 | -54.71478 | 2026-06-23 00:43:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 50edd67c-2ad5-3c4a-96b9-6148652b3a7c | -11.94674 | -57.70408 | 2026-06-23 00:43:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0876f69c-6f84-3685-b860-5802fed159de | -11.30747 | -54.72179 | 2026-06-23 00:43:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 93bc42b9-4197-30cb-9184-d878479030b1 | -11.28562 | -55.79778 | 2026-06-23 00:43:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eb204981-2b75-36ad-bb07-b446c5b5101a | -11.872 | -57.83263 | 2026-06-23 00:43:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 3ee467df-a0d4-354c-b239-8109d483b020 | -12.42851 | -58.41738 | 2026-06-23 00:43:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 24b8cee5-4655-3f55-822d-cd839e018d8f | -11.28426 | -55.78835 | 2026-06-23 00:43:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7b843645-d4e0-39c0-b6d8-aeccea8d7ac5 | -11.87323 | -57.84177 | 2026-06-23 00:43:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d5e6f818-6550-3675-909b-44210e6cce1d | -10.90616 | -54.13656 | 2026-06-23 00:43:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 94da5627-6a55-3ad4-95e5-92aec59d240c | -12.43506 | -58.39696 | 2026-06-23 00:43:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 1b6954c0-f9a2-3250-a478-39a44bcd078e | -12.29731 | -57.57394 | 2026-06-23 00:43:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 159551c8-b499-3f0f-afa6-972bc0fbbbd3 | -11.51753 | -56.13021 | 2026-06-23 00:43:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 6ad447d5-7bf8-36f1-b2c4-27cf09f8cbbe | -11.51622 | -56.12101 | 2026-06-23 00:43:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d59bcfc1-5cf9-3342-9b63-5e355e3a8425 | -11.27615 | -55.79582 | 2026-06-23 00:43:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f64a4107-069d-3238-800a-1bc2a0cb669a | -10.77966 | -50.26583 | 2026-06-23 00:43:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| d5409989-7ade-3c9c-9448-0f0d71686747 | -12.28965 | -57.5843 | 2026-06-23 00:43:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c25c3bf4-33e6-3bb8-83b2-6de463843241 | -9.4574 | -40.3641 | 2026-06-23 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 73.9 |
| 6bab98d4-5c0c-33be-89be-0e6c1bc10154 | -12.8746 | -44.3357 | 2026-06-23 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 157.1 |
| c26271a4-a1d7-3c1e-a8ff-3799c2d310ad | -12.8548 | -44.3625 | 2026-06-23 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 247.0 |
| 64150b80-930d-3dd8-8863-7b39e913d245 | -5.8319 | -45.0559 | 2026-06-23 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 5cceb02f-88db-34bb-9061-c24765c9f7d9 | -4.822 | -42.7712 | 2026-06-23 00:50:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 60.5 |
| bf3adeaf-9d53-350b-bf3c-11209fb2b604 | -12.4283 | -58.4048 | 2026-06-23 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| c87d0f47-97f7-3f96-8df6-a9348e26c24e | -9.457 | -40.3889 | 2026-06-23 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 101.7 |
| 43f0bf52-3ab7-3794-98a1-d6e74c68fb31 | -12.8552 | -44.3389 | 2026-06-23 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 155.3 |
| f6070208-36ea-37f1-868c-d0300a7910b1 | -4.8222 | -42.7477 | 2026-06-23 00:50:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| ce63c529-de4b-3c8d-bcdb-01ff08eb58a9 | -12.8741 | -44.3593 | 2026-06-23 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 238.4 |
| 4039d9ce-b185-3c6a-9f70-a3f0d52b274a | -12.8552 | -44.3389 | 2026-06-23 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 8534e63e-4c8e-32e3-a8aa-21830e95ae4c | -12.8548 | -44.3625 | 2026-06-23 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 261.0 |
| 48d9572f-682b-342d-86da-6bb4f1dee6ae | -12.4283 | -58.4048 | 2026-06-23 01:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| c3d0b9af-7884-3a9c-b5c4-7a0f365bb519 | -12.8746 | -44.3357 | 2026-06-23 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 44607e78-1f3f-3fc8-8a2a-3618de793e32 | -12.8741 | -44.3593 | 2026-06-23 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 241.4 |
| ce61f1b1-79de-3fd8-a486-0b728e500572 | -10.9051 | -54.128201 | 2026-06-23 01:03:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ef9b3083-72a2-3a5b-8315-45e6b73563ff | -11.0527 | -52.4631 | 2026-06-23 01:03:00 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1b7a4b00-2352-3295-aabd-3329e5c7c998 | -12.2896 | -57.571499 | 2026-06-23 01:03:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2a9d231b-b466-3a81-80c1-89fc9aba72c3 | -9.4646 | -49.832802 | 2026-06-23 01:03:00 | METOP-C | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eb07f93f-7912-3e2f-a4bd-4910d61107bd | -11.3049 | -54.720901 | 2026-06-23 01:03:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2e38d9cc-04c6-333e-9145-d9a08f0a7f88 | -11.8119 | -47.3424 | 2026-06-23 01:03:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 27b50f8d-4d7e-31a2-a70b-9e57d05a3b43 | -12.9136 | -49.479198 | 2026-06-23 01:03:00 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c9084b0f-ae70-3448-a3a5-bbb7079fcd27 | -11.4798 | -46.6763 | 2026-06-23 01:03:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5cba414d-da06-3c67-a3d0-fe53fffdadd8 | -12.8638 | -44.340599 | 2026-06-23 01:03:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| faf90cbb-f53a-3be8-868a-4368b8443d99 | -12.9114 | -49.470402 | 2026-06-23 01:03:00 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 75305e67-0105-3bf1-bf4e-5e7d5d71f78e | -11.8088 | -47.3302 | 2026-06-23 01:03:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1d652212-768c-3aa2-9cf5-f124e27b46f2 | -11.8113 | -52.532902 | 2026-06-23 01:03:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b58e6c55-e936-345e-ba00-ab615e4996b8 | -16.3146 | -51.4762 | 2026-06-23 01:03:00 | METOP-C | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 32c28997-5302-3b8e-95db-857bd0a5321f | -12.4325 | -58.405201 | 2026-06-23 01:03:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 70db2674-c3b8-3b92-a9ca-25db4a3a9ab3 | -12.8734 | -44.338001 | 2026-06-23 01:03:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3885a755-9c82-3f96-be89-d4874900bd1a | -12.8589 | -44.322102 | 2026-06-23 01:03:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 29b58c12-8964-323c-8d4e-26366844bfaf | -5.8335 | -45.064701 | 2026-06-23 01:03:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0ee21b84-a506-3cd9-8adb-05939c147522 | -16.313 | -51.469002 | 2026-06-23 01:03:00 | METOP-C | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a4a189ae-19a2-3488-9642-03361428cae4 | -12.8849 | -49.8344 | 2026-06-23 01:03:00 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f1ba70b5-ec20-3136-a6b5-22126ca511eb | -10.1242 | -52.195301 | 2026-06-23 01:03:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
