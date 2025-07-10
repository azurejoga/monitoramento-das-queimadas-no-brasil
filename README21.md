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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32075bb6-8d95-3e2b-af5f-3146946091b8 | -13.03553 | -46.30703 | 2025-07-10 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1f669182-378f-3d58-81de-b43ba4f6842e | -13.38117 | -47.88111 | 2025-07-10 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 253b4883-1d74-3b00-8ea0-d290bae4d6df | -11.82983 | -48.2163 | 2025-07-10 04:27:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1b3afba2-ad77-3080-bed7-4735989982fe | -11.32644 | -55.21441 | 2025-07-10 04:27:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5da45d0f-14c4-321f-b6b8-c481fc15f364 | -11.95717 | -46.35469 | 2025-07-10 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d02075f-3e8f-349c-ab15-06991a5d9b44 | -14.7324 | -41.72987 | 2025-07-10 04:27:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| de5edd52-987d-3254-bb23-7836fbc59917 | -10.87363 | -54.04778 | 2025-07-10 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b9e759b-0a7e-32de-b100-f365a81c5872 | -12.47243 | -46.91408 | 2025-07-10 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54d9760e-9f81-3ae7-b410-053fce76f752 | -12.03464 | -48.76082 | 2025-07-10 04:27:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d16020c3-80e1-3aa1-8897-6cd49ec07774 | -13.87346 | -45.84295 | 2025-07-10 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| befb2fee-5105-3461-90d3-de189719d11c | -17.65296 | -46.83841 | 2025-07-10 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5422dcd8-c8a7-3158-9f11-f8cfe0eb0902 | -17.78047 | -52.43303 | 2025-07-10 04:27:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a6bb4f4-3d72-36ed-983d-35701f45c564 | -13.16204 | -47.28378 | 2025-07-10 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e6cba14f-557c-3d38-b73e-88a7a3f202e3 | -11.87786 | -46.76538 | 2025-07-10 04:27:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d806837-11d5-3d95-b582-d0cd94041b07 | -12.09923 | -44.73756 | 2025-07-10 04:27:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36e7da04-ca1a-3795-b7a1-50ba17467cbe | -13.33256 | -52.91875 | 2025-07-10 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5bbd667-a6f6-30a2-98c8-06a95fbc8ee8 | -16.06461 | -51.55748 | 2025-07-10 04:27:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 170f322b-d32f-3b4e-ab8c-e7a05f65f05d | -16.58536 | -43.6487 | 2025-07-10 04:27:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78c763ac-efb2-36ba-b1dc-d02afeadbd1c | -13.34504 | -52.89413 | 2025-07-10 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1b89b8a8-e6ab-3695-8b36-678c8f511a77 | -12.99998 | -46.28247 | 2025-07-10 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfe625da-e319-3dea-a02d-d61493f91b9e | -19.0575 | -48.33236 | 2025-07-10 04:27:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e03b4c97-fe1e-31df-8d7c-c5fbd0633f41 | -13.38889 | -47.87513 | 2025-07-10 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c92c04fa-ff5d-3082-a268-743c3143fb47 | -12.99197 | -47.82859 | 2025-07-10 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2734adef-e658-36dc-8bfb-e86b2161d77b | -18.79861 | -47.9586 | 2025-07-10 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2dcac2e8-44c6-3069-a3a9-01061e59b8e4 | -15.92263 | -43.51569 | 2025-07-10 04:27:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15ecf2c3-aaab-3d01-a795-3eb90e37c101 | -15.30144 | -46.45033 | 2025-07-10 04:27:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8604e96d-4317-3174-b97b-a50c5b74d74e | -13.03438 | -46.307 | 2025-07-10 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3da0824-690e-30c4-8ecb-a9f9b17e7d16 | -13.34352 | -52.92618 | 2025-07-10 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a263b3de-c337-37e9-95ec-ff8560e87bd0 | -12.56912 | -48.88224 | 2025-07-10 04:27:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f0267796-85a9-3683-a5fc-f6bd80149b85 | -13.15595 | -47.27921 | 2025-07-10 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f5b90ed-693b-39fc-bfc6-d319100efc40 | -13.03495 | -46.3033 | 2025-07-10 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b540f241-dd99-3e4d-b6fc-70c9d2290de1 | -12.42604 | -43.72056 | 2025-07-10 04:27:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 53406cf2-82aa-39df-89dc-6178a26f5a15 | -14.72227 | -48.40268 | 2025-07-10 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b0aba049-9e79-3eaf-a54d-f47f8c396cdf | -12.43361 | -43.72166 | 2025-07-10 04:27:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c32a57a-3d2e-3b89-9b29-87072fd9b438 | -13.349 | -52.89482 | 2025-07-10 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d793cb0-0be0-3841-873a-a462a2f5ba13 | -13.37017 | -43.75785 | 2025-07-10 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 124b9d74-e1c1-39b2-9b65-8521f6d73cb6 | -15.92406 | -43.51465 | 2025-07-10 04:27:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8aad09c4-3663-3eb8-990b-59093e754093 | -10.87262 | -54.04613 | 2025-07-10 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a931c78-6d72-3e2c-8b6a-13c43e945b5e | -15.81743 | -43.34497 | 2025-07-10 04:27:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8110b2c0-92d6-377b-bede-aefaf62793ae | -10.23184 | -56.76859 | 2025-07-10 04:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6551d94f-6593-3e51-ae8f-21fbf769909a | -12.99942 | -46.28615 | 2025-07-10 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c34d322a-f5f7-3de5-a35f-80c217b81d3d | -12.13371 | -44.99609 | 2025-07-10 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f1729aff-4a3b-3392-8ef8-0e868ebeb188 | -11.33253 | -51.44777 | 2025-07-10 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6299f9e2-4290-3ebd-ae3e-4ff2014f29bd | -14.63098 | -46.8401 | 2025-07-10 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e1b1c41-7fac-34fc-8141-64e0714f9929 | -13.60533 | -47.53358 | 2025-07-10 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 06c9301b-1ee3-3968-b620-8b775c5748a2 | -17.09525 | -43.80494 | 2025-07-10 04:27:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c535d51-a79a-3101-bf6a-a91e75a4c0e5 | -13.01743 | -46.2817 | 2025-07-10 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b86adca-d48a-3077-9f0e-d2b4392b076f | -13.1565 | -47.27566 | 2025-07-10 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d25e25e2-2776-3a4d-b10f-18c5a30f56b8 | -13.34017 | -52.89863 | 2025-07-10 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f852bec7-6528-3a94-9d41-7d3d876b1a35 | -11.3333 | -51.4432 | 2025-07-10 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2573b16a-ead0-3b34-bbd9-22754822dbdd | -10.22649 | -56.76738 | 2025-07-10 04:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2ec44fc-b4b3-304e-9c70-bb25dd905a25 | -17.65698 | -46.83503 | 2025-07-10 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85b54592-c628-3c5c-9aed-424ad4568a19 | -13.34413 | -52.89933 | 2025-07-10 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5390aaf6-947f-3ce6-9b2e-84cb0959c833 | -16.74398 | -52.84278 | 2025-07-10 04:27:00 | NOAA-20 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3415ba8a-f1d9-3b4b-92fc-3e001b09af4f | -12.57246 | -48.8828 | 2025-07-10 04:27:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 52b3aad0-cf7d-3b1c-b00e-9327a22b92b9 | -11.83315 | -48.21684 | 2025-07-10 04:27:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a2d055d-62da-323f-b493-94b4efe6be70 | -13.02136 | -46.27867 | 2025-07-10 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36f38c97-5167-3cab-b9ea-bd900f9801fd | -12.87982 | -49.83736 | 2025-07-10 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 739c43ad-4be3-384a-b2ec-f4fa69d2cb7b | -15.81793 | -43.34127 | 2025-07-10 04:27:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa9103ea-078c-3aa0-9bbe-3632eba9b747 | -12.2211 | -44.20345 | 2025-07-10 04:27:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97651ada-68d2-38f9-a377-0cff3516be02 | -11.94935 | -46.36084 | 2025-07-10 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7663b5a-f4ba-3ca3-8cc3-cc2f3637340e | -17.86785 | -50.71328 | 2025-07-10 04:27:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 083866e0-041c-34e6-97d1-64a9b8d1eb58 | -15.03159 | -57.19148 | 2025-07-10 04:27:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce6913cf-7799-3a40-8f4a-1ac6f8db263f | -11.33099 | -55.21766 | 2025-07-10 04:27:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7444280e-132f-3dbd-9064-a943f5208df1 | -11.82708 | -48.21222 | 2025-07-10 04:27:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ae554149-ccd3-39bf-a717-b47fdf026f3f | -12.5758 | -48.88337 | 2025-07-10 04:27:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 306231e1-8fff-37d5-918c-184a4d84e766 | -12.57304 | -48.87922 | 2025-07-10 04:27:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 28625c2e-a17c-3a27-9d4c-91bfbfe3a501 | -11.33012 | -51.44548 | 2025-07-10 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9777834-6990-3299-8c7e-05376fa7efdc | -16.06391 | -51.56157 | 2025-07-10 04:27:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9141238b-8095-3636-9391-bc324f5bcb47 | -16.07884 | -53.74634 | 2025-07-10 04:27:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f462eb8-229a-3814-affa-863cba2ff1e5 | -14.86084 | -45.12564 | 2025-07-10 04:27:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fb9cb5a-1d80-3165-85fa-21521bbea78f | -11.33386 | -51.44614 | 2025-07-10 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d188bc13-d058-314e-b6b8-90316dc69550 | -13.34109 | -52.89343 | 2025-07-10 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 32fc559f-2c56-3535-a140-2d6eb9426d88 | -13.16314 | -47.2767 | 2025-07-10 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d926ded-6540-3fcf-9289-66c41d5e0310 | -13.35589 | -47.78294 | 2025-07-10 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7dae114-e72a-3482-ba22-4f29e1cf1a71 | -15.68743 | -53.32577 | 2025-07-10 04:27:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ce4edd7-fa0b-3ff5-8b4a-57e596cf66f4 | -13.63686 | -44.41803 | 2025-07-10 04:27:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ff972ad4-3e64-3eb4-9537-ea1a6e5545b0 | -13.16259 | -47.28024 | 2025-07-10 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f3f8756-2b16-37f6-bf81-d1a0c64dc773 | -11.73554 | -48.52812 | 2025-07-10 04:27:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5baef045-dfa7-3515-9e2e-3924bc0bbc7b | -18.08373 | -54.28661 | 2025-07-10 04:27:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73fa03d9-88f8-3192-b3a1-98b2110eb0fa | -13.01351 | -46.28473 | 2025-07-10 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81866da6-2157-391d-83c3-2ab8692a8817 | -12.46965 | -46.90998 | 2025-07-10 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 781764d0-22a7-30e2-804b-ce159950632b | -13.33561 | -52.92471 | 2025-07-10 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 884092bd-9f99-3709-9c8d-eafa2821d7a0 | -13.0242 | -46.28279 | 2025-07-10 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b427a46-a26f-39c2-8fb2-57d3cded2c38 | -13.03946 | -46.30392 | 2025-07-10 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b47700a4-d190-31a4-8be7-149e409282a1 | -15.47314 | -45.19585 | 2025-07-10 04:27:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5da8c702-0959-3216-b814-f5b2da05d301 | -12.1028 | -44.73812 | 2025-07-10 04:27:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 96a515c1-043e-345e-80a8-59624d02af30 | -13.15872 | -47.28326 | 2025-07-10 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3c33497f-d41f-3848-b3d4-e9f6507b3fcd | -13.1493 | -47.27816 | 2025-07-10 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0cb50eb3-1901-36e5-b59f-a00e80abed91 | -13.37234 | -47.89415 | 2025-07-10 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7afac619-0424-36b7-bc6b-ab977440f277 | -14.6644 | -53.11259 | 2025-07-10 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43d73669-4914-38ae-92c6-dfe8f4a8cf23 | -13.15263 | -47.27868 | 2025-07-10 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac3b1a08-1f8d-3038-bcaa-9623af33ea3e | -11.95271 | -46.36137 | 2025-07-10 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 775dc288-318d-3a25-a39a-9ab531e421f6 | -16.33585 | -48.96128 | 2025-07-10 04:27:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 603afd73-dd27-3f99-82ea-a42bbf4f1fdd | -12.98866 | -47.82805 | 2025-07-10 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47db1065-ac31-34fc-be8a-deb7575cf17a | -11.87841 | -46.76183 | 2025-07-10 04:27:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ceddbf73-8fac-3679-8158-5863871b4e3c | -12.98591 | -47.82398 | 2025-07-10 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 416d387d-a6ad-391d-bf31-9ab204fa8b6a | -13.342 | -52.88822 | 2025-07-10 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8ea9885d-2ae0-38e4-94a9-c68126fb77ad | -11.95662 | -46.3583 | 2025-07-10 04:27:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1a49481b-a8ed-36ea-9da3-3259066cf98e | -12.56421 | -52.21905 | 2025-07-10 04:27:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README22.md)
