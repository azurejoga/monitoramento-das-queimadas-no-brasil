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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14fc8169-a904-37f4-a3c8-3c690dc6309a | -6.06821 | -39.18764 | 2026-01-08 03:53:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b6f023f9-ed2e-3af6-8b3b-cfd8fb89ad41 | -6.66747 | -35.11772 | 2026-01-08 03:53:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 02715f50-fd50-38d5-9b4c-84dff1e7e5f7 | -7.55966 | -45.62598 | 2026-01-08 03:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fcc4e710-1d25-38fc-b2f6-38ee861fc054 | -4.27456 | -43.78903 | 2026-01-08 03:53:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad6245af-2af6-3d89-90c0-abb8c0a740d1 | -6.07626 | -37.31235 | 2026-01-08 03:53:00 | NPP-375D | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1e7dcedf-60b4-3802-90c1-03c098dda5ce | -3.65984 | -44.81338 | 2026-01-08 03:53:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3989c95f-79de-3795-ac20-584cf8f7a751 | -4.26896 | -43.79322 | 2026-01-08 03:53:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6091b801-31eb-3240-b278-d74e1e1d51c6 | -5.28506 | -45.82901 | 2026-01-08 03:53:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 989bd098-c7b0-329a-9735-38a6cce0162b | -9.65202 | -42.95813 | 2026-01-08 03:53:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0fd65a24-eda9-3d0d-b574-3e58561f5071 | -5.0113 | -38.13606 | 2026-01-08 03:53:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b01ccc87-f1cf-3b23-85f2-9b6bf77477f4 | -11.88137 | -44.20729 | 2026-01-08 03:55:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b537df0-178f-349c-aebb-59eb2e065ec0 | -11.88566 | -44.20812 | 2026-01-08 03:55:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48005c0b-569d-3bde-8f26-a55da2809593 | -11.95812 | -44.2118 | 2026-01-08 03:55:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52a3c3d5-a7d3-3767-bccd-f8b4a026b876 | -15.14283 | -45.27328 | 2026-01-08 03:55:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21b82f22-9dd7-3652-926e-09ee4a980f9c | -9.98818 | -44.7495 | 2026-01-08 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e59bfbc-79ee-3703-953c-5439de935ad5 | -9.98734 | -44.75425 | 2026-01-08 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 849e07b0-a19e-311c-b10f-d14c7dc545fc | -15.82935 | -39.33615 | 2026-01-08 03:55:00 | NPP-375D | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 384c4ace-bc0c-3a2c-bfb4-c234904867c6 | -15.14716 | -45.27422 | 2026-01-08 03:55:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6085c3d5-9d1e-38ed-a2cb-45ad4b915bdd | -12.29886 | -38.20494 | 2026-01-08 03:55:00 | NPP-375D | POJUCA | BAHIA | Brasil | 2925204 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| abbf3246-925a-3433-8985-7ff5cc0e666c | -9.99362 | -44.74554 | 2026-01-08 03:55:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fae2bf9e-ebff-3414-99ea-3475a789ca13 | -20.89013 | -52.33835 | 2026-01-08 03:57:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 49823a07-5005-3c6e-8457-b280d14a4730 | -20.88754 | -52.35028 | 2026-01-08 03:57:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6cee99af-c6f0-3aa5-9305-382d57b55295 | -20.89466 | -52.34721 | 2026-01-08 03:57:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5cf337fa-2aaf-37f1-a900-9cd0857ecb3a | -22.82483 | -49.29118 | 2026-01-08 03:57:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 640d0d11-e456-398c-8071-04daf7a25e62 | -22.82844 | -49.29815 | 2026-01-08 03:57:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7312f83b-9fef-3ae3-9be7-0c470ee2aeb7 | -20.88898 | -52.34333 | 2026-01-08 03:57:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 611260fb-983f-3b38-ba5d-8988b0d6183a | -21.61725 | -48.94696 | 2026-01-08 03:57:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b28729c-bfcc-3253-a114-046db79fe15b | -20.7176 | -49.83091 | 2026-01-08 03:57:00 | NPP-375D | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dbef89e7-3e44-395e-adc5-67a543996ef2 | -20.88874 | -52.34521 | 2026-01-08 03:57:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b00a9651-89f1-3366-b883-ca3a2da66caa | -20.88665 | -52.35349 | 2026-01-08 03:57:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b3b0e493-9b24-34ef-b707-0d13e09e06dd | -23.61545 | -48.34925 | 2026-01-08 03:57:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 69ac53c7-01dc-3166-8e9f-5021219ab675 | -23.61515 | -48.35075 | 2026-01-08 03:57:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab1e12fa-7ae6-3bb7-ab78-6a53237ec0a2 | -20.89377 | -52.35035 | 2026-01-08 03:57:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c0e625b-1e9f-3ea5-9385-de032cb57d7b | -20.88992 | -52.34026 | 2026-01-08 03:57:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 16282379-7b37-3552-8533-1669798665a4 | -20.89491 | -52.34535 | 2026-01-08 03:57:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54fea64a-5ddc-3455-b00b-666569c200ed | -20.71238 | -49.82962 | 2026-01-08 03:57:00 | NPP-375D | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1d2263c0-b13e-3ad0-9e0c-c1b14c5f3664 | -24.34664 | -49.42571 | 2026-01-08 03:57:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 52b52d5c-001a-3959-a3a0-ca1a505c1fa4 | -20.88783 | -52.34837 | 2026-01-08 03:57:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 760fe755-5fb8-386a-b3ae-7ff89a2f33e9 | -21.75833 | -50.17036 | 2026-01-08 03:57:00 | NPP-375D | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 78da23cb-a2f0-322e-9df1-0b6ef440a86f | -22.82361 | -49.2969 | 2026-01-08 03:57:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 72ace68b-8882-3452-b9c0-c704f1a866b5 | -23.61095 | -48.34818 | 2026-01-08 03:57:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c270bb3f-3266-3641-a61a-3a75de85e70e | -22.82965 | -49.29248 | 2026-01-08 03:57:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8ef9cfdf-54ba-3e59-a449-d66f45f5950e | -26.11418 | -51.55124 | 2026-01-08 03:59:00 | NPP-375D | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| be66d18b-05cf-37c7-8ec6-75492b2c5991 | -24.88952 | -49.27637 | 2026-01-08 03:59:00 | NPP-375D | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 81814266-d999-3ce0-b7cf-dc5434e674e8 | -28.04169 | -48.89554 | 2026-01-08 03:59:00 | NPP-375D | SÃO BONIFÁCIO | SANTA CATARINA | Brasil | 4215901 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1b39d50e-26d4-38a3-977e-1edcefd92e5f | -4.2728 | -43.7601 | 2026-01-08 04:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 6f284638-1479-39c6-92e6-1f8f245126a3 | -4.2726 | -43.7832 | 2026-01-08 04:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 87ae9038-859d-38dd-a8d0-4d848ea25cfa | -4.2914 | -43.7591 | 2026-01-08 04:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 31a8ed29-cadb-3021-8d97-1a317c48fb6e | -4.2913 | -43.7822 | 2026-01-08 04:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| f6227d50-bd8f-3917-be46-70a8d91f2e27 | -4.2726 | -43.7832 | 2026-01-08 04:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 48e779a2-7b13-3f70-b67e-36e6593274fb | -4.2914 | -43.7591 | 2026-01-08 04:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| b8f02e77-e0a6-3763-ae62-d6f8bef80404 | -4.2728 | -43.7601 | 2026-01-08 04:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| e5cb91de-7fdd-3759-a174-465d32f9c761 | -5.13204 | -43.81321 | 2026-01-08 04:14:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f5b98f1a-0795-34d3-a53f-30ad84aed000 | -4.51584 | -43.69392 | 2026-01-08 04:14:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77cde712-e9e8-3bcb-9eaf-cf66b0a138e2 | -5.75194 | -45.11106 | 2026-01-08 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81d9caa7-a786-3189-996d-13757f326c8f | -4.27254 | -43.77081 | 2026-01-08 04:14:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 6e6b58dc-7ada-3f86-a39b-bb23eda7a3e8 | -2.66368 | -42.73322 | 2026-01-08 04:14:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 37bf0095-4826-3e8b-87d6-4aae9e596aca | -4.37153 | -46.38302 | 2026-01-08 04:14:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66640685-e5df-37e0-81d3-3d2dfd0529c9 | -4.27532 | -43.77485 | 2026-01-08 04:14:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 875d3deb-a89a-3f69-9c8c-dce321f11d9f | -5.38785 | -45.38886 | 2026-01-08 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4fd2c401-1ad5-3cb3-be60-f95baa7c44fd | -3.55824 | -47.18011 | 2026-01-08 04:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a98d54cb-4b12-33de-a003-716a82d9dab5 | -6.63983 | -41.71805 | 2026-01-08 04:14:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d3a47e19-9b44-3e00-90bd-aa86c86286ae | -4.26698 | -43.76271 | 2026-01-08 04:14:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99795e54-2b0f-304b-86ea-73e142031603 | -3.6391 | -39.99562 | 2026-01-08 04:14:00 | NOAA-20 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0a628374-0928-3420-9d8e-b9b689f946b8 | -4.26586 | -43.76973 | 2026-01-08 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 61ed78c0-3cee-3208-8d1f-6077cce81ae7 | -6.34186 | -43.38285 | 2026-01-08 04:14:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1c055cf4-8eb4-3343-b311-f01cb26fd9d1 | -2.87879 | -45.22399 | 2026-01-08 04:14:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b804eec6-fbc2-3484-8289-802c8789eb74 | -4.2692 | -43.77028 | 2026-01-08 04:14:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c48a9eef-7dd5-3495-b1be-87cc54cddc6d | -4.26808 | -43.77731 | 2026-01-08 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a3c1753-a956-336f-8f8b-fefeb8f08362 | -3.89356 | -42.56068 | 2026-01-08 04:14:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4bf37ccf-f679-31aa-bd9f-0a6b31afb9c6 | -5.86405 | -42.42682 | 2026-01-08 04:14:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 85010623-4d18-3492-a088-94331441d6c6 | -5.94022 | -44.44873 | 2026-01-08 04:14:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2f79ba2a-44a0-3b65-b4cc-70c76f78258f | -3.93416 | -41.89329 | 2026-01-08 04:14:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3398f598-42e7-3dcc-b9b4-a32caff70df7 | -3.18847 | -39.75249 | 2026-01-08 04:14:00 | NOAA-20 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 32481e6d-13db-3eef-a807-3c20a9a2eb16 | -4.282 | -43.77591 | 2026-01-08 04:14:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4ec8d654-09d3-3c71-aba6-f3565f633c23 | -5.28709 | -45.82847 | 2026-01-08 04:14:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57b6a159-ccc9-3b4a-a1f8-1d1ee31c3df1 | -2.9217 | -40.37613 | 2026-01-08 04:14:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 8ebcccba-b127-3033-90a6-97ef00d1a9d3 | -3.23518 | -41.80199 | 2026-01-08 04:14:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 049439d1-f5fe-3d79-8972-d6cc3b97511b | -6.6963 | -39.65327 | 2026-01-08 04:14:00 | NOAA-20 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7dc2ca52-8bbb-3404-b744-8aa1f16a514a | -3.82606 | -44.48399 | 2026-01-08 04:14:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8986a4d-301c-3549-9814-6dc60ac4c169 | -5.74852 | -45.11047 | 2026-01-08 04:14:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 431fb43f-cd1e-3422-bdb4-95a0b12f3c7a | -3.87415 | -42.51178 | 2026-01-08 04:14:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6321a789-e3d5-31cf-af82-598c4a5d0bfc | -4.28255 | -43.7724 | 2026-01-08 04:14:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 85c0de01-51f2-3d6d-a220-971b5350b95d | -4.28589 | -43.77293 | 2026-01-08 04:14:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7de8fac4-bc21-37e6-9f5f-ee3d98039db7 | -4.2614 | -43.77626 | 2026-01-08 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 835d879a-f85c-32b0-b8db-27e8a62f9e0c | -3.91206 | -44.90672 | 2026-01-08 04:14:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d78f205d-b5d5-3608-97f6-2dd3efcfa0c1 | -4.26084 | -43.77979 | 2026-01-08 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a5b901a-9dc4-3eca-a6df-1bfc9f195143 | -3.46051 | -42.07539 | 2026-01-08 04:14:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 452e1e8f-1e7a-339c-bb84-bb02c970f1a5 | -3.20154 | -46.82893 | 2026-01-08 04:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 78b9be62-d1b2-314a-8930-085694c5398f | -4.27866 | -43.77538 | 2026-01-08 04:14:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 524b07d5-02b3-3904-bf3c-5e05a0d1f300 | -4.83324 | -45.3464 | 2026-01-08 04:14:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 28bd3822-5063-3537-afe3-f1501237ef74 | -2.92228 | -40.37239 | 2026-01-08 04:14:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 63852e00-5bdf-34c4-979e-b7dd12508155 | -6.585 | -44.62459 | 2026-01-08 04:14:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 846f98da-3445-3912-87f1-adbc7eb6ce9d | -6.61512 | -39.38827 | 2026-01-08 04:14:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 5ea41889-0536-3ba6-a582-6711eddf50d6 | -3.86976 | -42.51815 | 2026-01-08 04:14:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e2c0cdcf-fcbb-349e-8783-90f6ae51fcbf | -3.87084 | -42.51126 | 2026-01-08 04:14:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b6bfc441-9449-34b6-88c5-5acae9e32e73 | -2.93756 | -41.79501 | 2026-01-08 04:14:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bbdfef66-39d1-3b5e-b0ad-152dec4ce04b | -4.45643 | -44.13348 | 2026-01-08 04:14:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a6b46733-1c1b-3adf-8d41-f14b74dc333a | -4.26474 | -43.77679 | 2026-01-08 04:14:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd140962-bedf-3da5-a730-cf12c46361f7 | -4.26976 | -43.76677 | 2026-01-08 04:14:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README5.md)
