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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 567c0a21-8cac-3a45-9c04-aad3444f9eac | -14.19173 | -51.24441 | 2026-09-04 03:47:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a027d72c-de71-3c11-b8e5-3fa2fca3f7a3 | -21.04305 | -48.47129 | 2026-09-04 03:47:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ab60f75-2328-34cc-a74b-61bf1addba92 | -18.13977 | -51.80826 | 2026-09-04 03:47:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 16e47a58-1345-3d37-8c7d-4b78e9c1bcd3 | -18.51906 | -48.19118 | 2026-09-04 03:47:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 54e187de-c632-3d9a-bc64-4f162e4e5c21 | -14.91007 | -44.67737 | 2026-09-04 03:47:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 77b8654b-660c-30bc-89be-33aeebc14d86 | -21.41469 | -45.11014 | 2026-09-04 03:47:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2aad1906-471a-34fa-aab7-654a56f1e579 | -15.63096 | -45.90864 | 2026-09-04 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76f4be2d-5821-3c36-b035-7b5f5a62cff0 | -19.31446 | -47.09746 | 2026-09-04 03:47:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c9c3197b-65ad-385f-8eb1-bfe584e0a23f | -13.58227 | -47.8872 | 2026-09-04 03:47:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e97d73d-1e19-3df0-a658-5dba8becf15d | -18.14286 | -51.80377 | 2026-09-04 03:47:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bafa5b3c-41be-3551-b15b-0b0afb6585d4 | -17.24908 | -44.86321 | 2026-09-04 03:47:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bdbcf38-7212-36ae-bedf-7b0812121fd5 | -13.58397 | -47.88389 | 2026-09-04 03:47:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 51afcf8f-4267-31a9-934d-31c4e8aaf8e6 | -15.06811 | -45.32189 | 2026-09-04 03:47:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7281489-1e41-3743-9f34-a46baccdad71 | -16.65884 | -43.63417 | 2026-09-04 03:47:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| cd1db6b5-126e-378b-b711-520681ef8ca3 | -19.31508 | -47.09452 | 2026-09-04 03:47:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1dfc7b0f-1067-3386-9347-6371d9723a85 | -13.58334 | -47.88201 | 2026-09-04 03:47:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd6ccf5d-7bb6-3d13-bc63-7a6130da2858 | -13.58035 | -47.87162 | 2026-09-04 03:47:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 470e63e8-f180-3bb5-9f01-f10cf3f63a25 | -14.79342 | -47.13654 | 2026-09-04 03:47:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c437cd50-77b2-32f4-8ac0-bf36f4d61728 | -15.63593 | -45.9096 | 2026-09-04 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f55b9266-f80a-3035-b46c-36d80db1ceb4 | -14.19581 | -51.23723 | 2026-09-04 03:47:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b0f22dab-0a36-337c-8e37-6dafbd75b498 | -14.19327 | -51.23749 | 2026-09-04 03:47:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 317b2b97-7396-3789-af00-ae444b70e6b4 | -14.18734 | -51.24253 | 2026-09-04 03:47:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24d16f9e-20ed-353a-9b51-def51f220390 | -15.82842 | -46.03678 | 2026-09-04 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ef648eb-3bb4-3963-8969-bd647ed74444 | -18.52017 | -48.19153 | 2026-09-04 03:47:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1afa1e4e-05ee-3c54-8a65-6be43463c384 | -20.8674 | -43.38911 | 2026-09-04 03:47:00 | NOAA-21 | RIO ESPERA | MINAS GERAIS | Brasil | 3155207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4f7b1bee-992d-3571-81aa-8e330b871e8d | -15.83196 | -46.01903 | 2026-09-04 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f5c69662-94fd-3d2e-a742-e71971685ac4 | -16.66228 | -43.63912 | 2026-09-04 03:47:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff1ff240-d78e-3526-9c10-6895768f6fea | -13.58432 | -47.87729 | 2026-09-04 03:47:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4f8e2379-b3f6-378f-a5ab-bc0c0e66859b | -18.13302 | -51.8068 | 2026-09-04 03:47:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 549037b7-486d-3db3-bf28-1a3fa021cd63 | -20.91539 | -48.47958 | 2026-09-04 03:47:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df580737-c0c7-3b5c-a343-2849ca710274 | -15.84013 | -46.02997 | 2026-09-04 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4dbdb549-1513-3835-ac68-f081d2bda25a | -21.63934 | -43.98805 | 2026-09-04 03:47:00 | NOAA-21 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| dd787848-2700-3913-ab4e-d104b13a397b | -18.80458 | -47.54952 | 2026-09-04 03:47:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0016c56d-5cef-3ba5-921f-72d1eb35b7af | -23.32599 | -52.31067 | 2026-09-04 03:47:00 | NOAA-21 | FLORAÍ | PARANÁ | Brasil | 4107801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c1c16ef5-2992-34f4-b4a4-96e777f2829d | -15.62723 | -45.90155 | 2026-09-04 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c18dcc29-d9a0-3aa3-89fe-838100c21674 | -19.35307 | -47.08693 | 2026-09-04 03:47:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34df0ed6-da29-32b8-9b00-c3aed9070088 | -16.66302 | -43.63509 | 2026-09-04 03:47:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c50f033-11aa-3ec6-aa14-64e498c45916 | -18.14128 | -51.80173 | 2026-09-04 03:47:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 16422423-28d0-3b81-acc2-6f5789622b7a | -15.83339 | -46.03783 | 2026-09-04 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5f3ad18-36ff-3077-9e49-f18144b78bba | -19.06962 | -46.99907 | 2026-09-04 03:47:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ad7d698-d9d5-3784-bf92-5d0d015b0940 | -16.57352 | -51.62654 | 2026-09-04 03:47:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 29be72cc-b53c-318b-83f3-726bb23ea18d | -15.76659 | -43.31559 | 2026-09-04 03:47:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 467d17a7-12cf-346f-94d0-43340a9a0bcd | -21.25847 | -47.35554 | 2026-09-04 03:47:00 | NOAA-21 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e5944b0b-b3af-38c6-98fc-32c89f4c41dd | -17.52481 | -44.61408 | 2026-09-04 03:47:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 587a0931-cbe8-3a8c-932d-729a730acaf4 | -14.91102 | -44.67239 | 2026-09-04 03:47:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2928ab37-0399-3247-93dc-c94bdd983829 | -19.35246 | -47.08987 | 2026-09-04 03:47:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 197ec96b-0dae-3b4c-bdfa-0e9358ca6e30 | -14.90545 | -44.67643 | 2026-09-04 03:47:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 7ddf7b73-e29c-3f01-aae1-56821949dba8 | -17.32239 | -49.61727 | 2026-09-04 03:47:00 | NOAA-21 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c447a7c4-e73f-3ddc-8acb-291669a61406 | -22.59565 | -44.9779 | 2026-09-04 03:49:00 | NOAA-21 | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d3db1a29-596a-3c98-b4a5-2e7ff0998f7a | -21.4579 | -48.67613 | 2026-09-04 03:49:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8737c7cd-1c17-36fc-9771-1c9486b28f0e | -27.56237 | -48.66155 | 2026-09-04 03:49:00 | NOAA-21 | SÃO JOSÉ | SANTA CATARINA | Brasil | 4216602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3e78ff08-a20d-3b65-aca8-0d29907a70b7 | -21.06164 | -48.46151 | 2026-09-04 03:49:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 51332d19-2031-37d2-9ca7-2a2072761b12 | -22.02216 | -49.56725 | 2026-09-04 03:49:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| d8d7e219-91a1-395e-9e98-edaaa4a73d2c | -21.72111 | -47.16275 | 2026-09-04 03:49:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8f486a3e-caf6-3442-9d43-d55a03a4d473 | -21.72215 | -47.1339 | 2026-09-04 03:49:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73b41edf-993f-395f-a8f6-b67a2580b711 | -21.06091 | -48.46493 | 2026-09-04 03:49:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 59c4ae17-3146-3427-8904-e9bf615193d9 | -23.27917 | -46.60318 | 2026-09-04 03:49:00 | NOAA-21 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 5942eb40-6e19-3805-a7fb-423b68ca2276 | -28.28079 | -48.69682 | 2026-09-04 03:49:00 | NOAA-21 | IMBITUBA | SANTA CATARINA | Brasil | 4207304 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 232472cd-a67f-368f-9f9e-9668f1b765fe | -21.72334 | -47.12822 | 2026-09-04 03:49:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14d5292b-adfb-3230-9758-75e9dfc40f1a | -21.58241 | -48.65603 | 2026-09-04 03:49:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0562028-c160-31a5-9297-ede0f9285a95 | -23.0847 | -48.61263 | 2026-09-04 03:49:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbcffa69-3562-38cf-af0f-15676d04902a | -21.45864 | -48.67267 | 2026-09-04 03:49:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38cbaf0a-bfe4-3166-a0a4-637912866978 | -23.08398 | -48.6159 | 2026-09-04 03:49:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72794904-ee6e-3f25-92a1-b8fec0ce987f | -22.02133 | -49.571 | 2026-09-04 03:49:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| aac4c10e-449d-3f17-b363-179966a3af62 | -22.70209 | -43.36299 | 2026-09-04 03:49:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4dcff5e2-97ae-328c-afc1-dce5d11923d5 | -6.6882 | -59.9628 | 2026-09-04 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.7 |
| eed62a3a-940f-391d-a6c8-d843a89c5f55 | -8.6101 | -67.1783 | 2026-09-04 03:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| ba08f43e-3192-3937-a5d9-c22cbb0dc077 | -14.1361 | -58.8776 | 2026-09-04 03:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 5a42d99a-f5e7-3ca9-89fa-3948df31680a | -6.6881 | -59.982 | 2026-09-04 03:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| bf72699a-1fd7-322e-8cdc-89f3afaeab40 | -14.1169 | -58.8793 | 2026-09-04 03:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 062d5ef1-fd84-3e8a-821e-fce8f3c19dfc | -6.688 | -60.0012 | 2026-09-04 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 64544dd1-98bf-3731-817c-6d1993061849 | -6.7065 | -59.9813 | 2026-09-04 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 62e3d612-2344-367f-96c5-6d76e5bee319 | -7.5476 | -61.3437 | 2026-09-04 04:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 592abeb1-64e7-39bd-b4d3-5f69e36de5d9 | -5.565 | -60.1739 | 2026-09-04 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 4cdc19c8-e407-39db-beb2-a097dc33279a | -6.6696 | -59.9827 | 2026-09-04 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 4dce864a-33ee-3af4-8231-145a073793c9 | -6.6881 | -59.982 | 2026-09-04 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 048d9541-93ac-3150-9d24-658c1364dfe2 | -6.6697 | -59.9635 | 2026-09-04 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 28f6576e-b5c1-3db9-9532-5ed398db41a8 | -6.6882 | -59.9628 | 2026-09-04 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 3f7e9e78-3950-3fb0-bc3b-37226c133ba3 | -6.6882 | -59.9628 | 2026-09-04 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 4d8543c6-2667-39eb-a96d-676022ef3d6a | -5.565 | -60.1739 | 2026-09-04 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| e6042333-ca27-3a70-85f3-97a942a0640a | -6.688 | -60.0012 | 2026-09-04 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 9f3706a9-10ae-31f4-92ab-f2db5a917877 | -6.6697 | -59.9635 | 2026-09-04 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| c57b011e-1e36-3e45-baff-bb14a26a0c03 | -6.6881 | -59.982 | 2026-09-04 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 143.3 |
| 58abf010-f957-3028-bc00-9a138d9fe7c7 | -6.6696 | -59.9827 | 2026-09-04 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 3b0e4f2d-de40-3b31-8cac-5a1dde8e78f6 | -6.7065 | -59.9813 | 2026-09-04 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 3e27f223-c5d9-3f48-8934-e74757a82d01 | -2.894 | -39.96593 | 2026-09-04 04:17:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9fa83bad-2942-379e-99bb-9091e0f7308d | -5.38819 | -42.8593 | 2026-09-04 04:17:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c8946aac-c32a-3fa8-ad08-d695ec24305d | -5.38141 | -42.85822 | 2026-09-04 04:17:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 84d320f4-980f-303e-8d8c-d6e392b0d2b2 | -3.2452 | -47.91111 | 2026-09-04 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 50e45c27-d75d-3905-8f46-45ba15d318b5 | -1.24771 | -54.5377 | 2026-09-04 04:17:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c870bd2b-9645-35cf-a09e-56ad9d6a540b | -2.83077 | -46.72351 | 2026-09-04 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c96a8c50-d8db-3662-b646-34df78638524 | -2.32781 | -47.19496 | 2026-09-04 04:17:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ddb1070-3af7-3d2b-886b-a976ee72e2a8 | -4.02875 | -38.23305 | 2026-09-04 04:17:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 087b02ac-2029-322f-b3e5-170f7f460f60 | -3.24705 | -47.25303 | 2026-09-04 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e1ab6bf8-5098-39a5-ac18-e5b95073e4b0 | -3.76868 | -47.55166 | 2026-09-04 04:17:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1bf64238-d530-384d-a147-3d5f7359416a | -2.48148 | -46.85614 | 2026-09-04 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 467735a7-711a-394c-90be-54d73665ec93 | -2.75762 | -49.47594 | 2026-09-04 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bc6393e-7bc8-3286-a80f-21bf9f557f9d | -4.31017 | -46.77879 | 2026-09-04 04:17:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7ee2862-60a6-3399-9a16-c3d41fc8b244 | -3.93481 | -42.98882 | 2026-09-04 04:17:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b23c5247-38a2-383d-a497-db43027a81ad | -4.2967 | -38.52727 | 2026-09-04 04:17:00 | NPP-375D | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README11.md)
