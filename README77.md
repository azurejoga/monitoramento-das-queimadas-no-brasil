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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3aead40-1679-329d-8e06-0f5b1a45ebde | -5.25489 | -47.23879 | 2025-10-18 04:49:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9cd6bdd-7cbf-3b0f-9551-5e9972d6df58 | -8.3005 | -43.39777 | 2025-10-18 04:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1520425a-5aab-35e4-81a4-a5cc1375e49c | -7.34361 | -43.85899 | 2025-10-18 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ff857c4c-a4da-3bce-9371-2def52bc8303 | -3.60324 | -49.34844 | 2025-10-18 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b83ce1e7-bd5f-370c-9947-ff5d0f0c8d91 | -6.7641 | -56.86111 | 2025-10-18 04:49:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 386b277a-c6a8-3247-929c-ace71fbdb4fc | -6.36811 | -45.76741 | 2025-10-18 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3cd9ab12-9e65-3e47-95fa-bf92bd4ed3b5 | -4.49869 | -46.48665 | 2025-10-18 04:49:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b14e88e3-ef1c-38ea-a9b2-ddde84c4dfc7 | -3.13289 | -50.21558 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f231358-12c8-3ce3-821c-9b107919c09f | -7.86938 | -55.37545 | 2025-10-18 04:49:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f9346741-1493-359c-bca4-c3047c8c2d4a | 4.41738 | -60.38934 | 2025-10-18 04:49:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f32324e3-fda5-31f4-b253-ea81f56b346c | -8.22458 | -47.84726 | 2025-10-18 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f98e6804-4e11-34e2-98b3-4746bf76d456 | -3.41503 | -52.82751 | 2025-10-18 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e574be04-f757-3fc4-843e-24c7e8864764 | -2.33104 | -57.02612 | 2025-10-18 04:49:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca2426f5-503a-3056-b528-73494133ede9 | -8.41835 | -44.72549 | 2025-10-18 04:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e066d4b-424d-3a02-9e48-6d5cc9db3dcc | -9.75296 | -43.96236 | 2025-10-18 04:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c236e295-a16d-3146-81da-46a952a0752d | -6.59369 | -46.69127 | 2025-10-18 04:49:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b307d544-a22e-3ab0-8896-31e64382a7c6 | -9.75072 | -43.96219 | 2025-10-18 04:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be5342d1-49db-37e1-aebc-a057652adaaf | -6.64106 | -47.88243 | 2025-10-18 04:49:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c260509-9010-315e-94e0-632b9f0c26fd | -8.81252 | -49.68586 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b923c126-12cd-3484-a8af-77162113a4ca | -7.71381 | -47.85344 | 2025-10-18 04:49:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97c968f2-a56d-3a02-be14-3121507230d6 | -3.85179 | -41.58042 | 2025-10-18 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a229c831-226e-3198-bdd8-0754b301fce2 | -2.57224 | -49.11037 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e95600f7-e468-3f5a-8731-a27c7055dfdf | -8.31559 | -43.41935 | 2025-10-18 04:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1643cf82-2c95-3e7d-afcf-161d18627c59 | -9.04224 | -46.97121 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e44d78a-24c2-3bd7-b998-c2fca0468932 | -5.01258 | -46.02715 | 2025-10-18 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ddcbe2d5-a7f8-33f2-889b-806de3465e6d | -8.78957 | -47.9397 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc5c4885-7ada-3fd1-b6ea-1533ccbc7366 | -8.8343 | -49.68912 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 923ea4b5-28a5-3b0a-b296-3afce2cdb940 | -6.98889 | -42.79612 | 2025-10-18 04:49:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e3217d4d-6139-31a7-9865-0c9476de3e00 | -5.06068 | -45.85483 | 2025-10-18 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 213c184f-2820-32cc-b6b4-47a67d904395 | -3.05443 | -43.21649 | 2025-10-18 04:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 099aa02a-57b1-3d43-b24f-d65b8aee740d | -1.4204 | -60.40358 | 2025-10-18 04:49:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ea51545c-b72d-378d-a13a-174f444c2149 | -2.81311 | -54.37756 | 2025-10-18 04:49:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c609f60b-fdd4-3c92-896d-12764b5bf64a | -4.96349 | -44.6107 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67360a8c-3414-3a2e-8940-f5d799191baa | -6.36494 | -45.7578 | 2025-10-18 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b8aa162-e542-337b-96ec-b0107aa3c60d | -5.01317 | -46.02315 | 2025-10-18 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7d91f13a-04da-38cb-82a1-2f4ff018c191 | -7.39209 | -44.74929 | 2025-10-18 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdf5787b-3f98-3150-b315-9695e983bd94 | -4.43616 | -50.55129 | 2025-10-18 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e8d41d0-9e18-308d-9d05-2f30538834fa | -6.95304 | -44.87498 | 2025-10-18 04:49:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ec2dfda-86c3-3f11-811c-212fde35df2f | -2.5993 | -51.94761 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 121092a4-4070-3375-b770-bf573091eceb | -2.8779 | -50.74121 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d064179-eb9a-3457-8a9f-674a1acc4fd8 | -8.11652 | -55.08741 | 2025-10-18 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99ab091e-7b5f-30ea-b9dd-15e8a9361cfc | -6.14482 | -44.45877 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9fe1c8c5-8c33-358b-b976-4c223dee8ed0 | -5.07343 | -49.85443 | 2025-10-18 04:49:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5740b39-85cf-38bf-8e34-ccd55e51089c | -6.69041 | -46.70958 | 2025-10-18 04:49:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65efaadf-f6c3-31a0-bedd-8a1609471e55 | -5.10097 | -56.15254 | 2025-10-18 04:49:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44c20939-f4da-31b6-b145-374cc81bf262 | -3.2411 | -45.96805 | 2025-10-18 04:49:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9568853-6305-3619-85c8-95d2334517e7 | -5.21519 | -47.50288 | 2025-10-18 04:49:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d4accf9-c41c-387f-b1d0-dfe16fccc9b8 | -6.67507 | -58.75034 | 2025-10-18 04:49:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9431ede5-a773-3ca2-9abf-34871f42f862 | -8.82341 | -49.68748 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 25934a14-20d3-3d01-a588-76cd488d1855 | -3.78649 | -51.76856 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65f2528f-958b-35ee-8119-914f6f0d2cb0 | -4.87701 | -46.70612 | 2025-10-18 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0dd4823e-3d63-30f2-8861-514484c6eafd | -3.24475 | -45.97261 | 2025-10-18 04:49:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a0e9946-08c2-36c8-b412-170276f4cbbb | -10.4941 | -43.4315 | 2025-10-18 04:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| b547aa96-beb2-3469-ad98-832925b2cc14 | -5.0215 | -46.0097 | 2025-10-18 04:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 6b499242-bc17-3528-bba9-4b508f5976e4 | -4.4445 | -43.2397 | 2025-10-18 04:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 4567a953-fb2f-3562-a07c-75bbfbbfce7c | -4.4632 | -43.2386 | 2025-10-18 04:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 080b2e74-c014-350e-bda5-da723908fcea | -10.23906 | -44.07699 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5d0a98d-c513-3c6e-834f-a5ac104362c1 | -10.61324 | -47.3867 | 2025-10-18 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a9ac55a-ad30-3964-bbca-f6687dc66f45 | -10.8101 | -43.93061 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 876180a3-1b36-3447-9e9c-061e00e2cc0c | -13.77174 | -48.2303 | 2025-10-18 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b23f417a-2a13-341f-9956-57394e397336 | -14.44765 | -52.89472 | 2025-10-18 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a4ea7f5-6474-3c4d-ab13-5613b0e8282a | -10.43486 | -45.02082 | 2025-10-18 04:51:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e32b1642-ea24-3a43-b3fa-8d104e223f4b | -10.82642 | -43.93279 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d2acfc2-af4d-3a7d-93cb-1bcdadf5b8e8 | -13.51346 | -47.99941 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3b71538-65a9-30fc-93b3-aeafcf869d62 | -11.37558 | -44.28716 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3300d1d5-1830-3b34-a924-fae1e9641c8b | -13.19995 | -48.31868 | 2025-10-18 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8446756a-d9e6-3258-a3b8-cbe5514ea3af | -11.3615 | -45.26126 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 795c50e6-a455-36ed-820f-693909e79a61 | -10.431 | -47.74152 | 2025-10-18 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57bc1f17-2c83-39bc-a0e9-9ea910771d50 | -16.81297 | -41.2276 | 2025-10-18 04:51:00 | NOAA-20 | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1249dd6b-0c59-38a0-b8de-3babf9d49c87 | -11.35246 | -44.21106 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d51c4e94-3994-34ba-8e2e-6ce7bc6ab377 | -10.53107 | -49.55141 | 2025-10-18 04:51:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80379472-1e2d-3f8e-865c-feda80dd45aa | -10.48499 | -43.43386 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0e025f5f-42c8-3dbc-a034-5e9162f7af6b | -10.96343 | -45.46446 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1b3d327c-c063-33f7-84dd-8662f3f0d733 | -12.93336 | -48.60062 | 2025-10-18 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd4e128a-22a2-3baf-8b5e-bac3d45efe64 | -10.69969 | -44.55784 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1832a79-87a7-30d5-b95b-f3be957bb91a | -14.90499 | -52.38595 | 2025-10-18 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df53f68a-4321-3685-8df9-39d0f387580c | -10.53346 | -43.3665 | 2025-10-18 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77834b62-a7a7-306d-b014-3d7b3b1e4ad1 | -13.44665 | -47.98925 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce3f4e85-aafc-3b58-917d-f8cc48ac0707 | -15.04182 | -46.61674 | 2025-10-18 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 488aaa91-32fb-3583-b944-e05416096fb4 | -10.24434 | -44.0369 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9eeb36d8-a7de-3d28-9089-faa071b75140 | -13.04493 | -48.18985 | 2025-10-18 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a44a876-a3fd-3abd-9df6-80dbb0fdb913 | -15.05285 | -47.30583 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49b84aeb-01b3-3c65-b123-8c3a01b24089 | -9.61729 | -55.11744 | 2025-10-18 04:51:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5f002fd-e344-360f-8a17-2789f19ace83 | -10.93091 | -47.55355 | 2025-10-18 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8331630c-bb3f-3e6b-9340-f29da9637bd4 | -10.61982 | -45.23989 | 2025-10-18 04:51:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5a4d6b7-de5c-317e-bdd6-447bcd8c71c0 | -15.04801 | -46.60633 | 2025-10-18 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7a188d9-711d-31e7-b42e-3a964b81c09b | -14.90211 | -52.40518 | 2025-10-18 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d92b24a6-b906-36b9-ac0e-a00a98d77e8f | -9.66187 | -48.52812 | 2025-10-18 04:51:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0a97624c-e4c0-3f5b-9626-ea2804bde89e | -14.81188 | -48.40241 | 2025-10-18 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84a78bc1-765f-3ec8-a074-832cc89d48c8 | -13.26756 | -46.44019 | 2025-10-18 04:51:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25fc416c-62a2-3afb-b5ab-35a65685b7e1 | -15.79125 | -43.64918 | 2025-10-18 04:51:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 058b0ba5-23c5-3e63-a259-0cb8e53916d9 | -12.46619 | -45.46702 | 2025-10-18 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cdfeba4e-93b3-32ee-b9e5-b5b232074abc | -11.43625 | -54.0953 | 2025-10-18 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab96af12-1b2c-3de1-918a-ed076b4f011c | -11.21074 | -47.83498 | 2025-10-18 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0bd3ba5f-2602-333c-89ac-def10d7dce09 | -10.81299 | -54.60894 | 2025-10-18 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d345caa-fbc1-3621-b90f-dfecffffefe4 | -12.04431 | -54.24514 | 2025-10-18 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97c66df1-7ca5-36a1-a442-279dbd5280b5 | -10.29792 | -44.02734 | 2025-10-18 04:51:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad2ec3aa-3019-3f08-b9c9-d1ab1b037c43 | -15.05232 | -47.30996 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf437949-a42d-34d6-a321-3df49bff2490 | -12.46656 | -45.46407 | 2025-10-18 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 38de7ec2-5b31-31bc-84bb-9baf2927034e | -12.15613 | -45.08888 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README78.md)
