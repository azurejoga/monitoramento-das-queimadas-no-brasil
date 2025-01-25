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
| b16b3382-45ac-36ca-913f-47f4ac71fefb | -11.65168 | -43.91919 | 2025-01-25 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0069c37e-d86c-3b35-8b56-22bba49e1584 | -11.27823 | -38.50605 | 2025-01-25 03:49:00 | NOAA-21 | NOVA SOURE | BAHIA | Brasil | 2922904 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a6c4eb70-0a7a-3d57-9cbc-fde490b89aa8 | -10.50828 | -42.42498 | 2025-01-25 03:49:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| ce6f6725-0d35-3cfd-9394-b76e7e0a5050 | -10.62263 | -37.04126 | 2025-01-25 03:49:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4719336c-42ad-3c5b-a3e0-2542bb9632ef | -10.17258 | -36.49666 | 2025-01-25 03:49:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 54259227-ff68-3bef-8668-b3a917323499 | -4.8178 | -37.75373 | 2025-01-25 03:49:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ef07f383-3021-37d0-843c-8e8af65ea2d4 | -10.50348 | -42.4294 | 2025-01-25 03:49:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 9dcfab02-282e-3af2-88e7-cc3dfc317bf0 | -9.56012 | -42.85545 | 2025-01-25 03:49:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c992db6f-8596-35a1-8757-402bcecbd1f8 | -10.17312 | -36.49311 | 2025-01-25 03:49:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0cbd500b-858b-37ba-8190-c5ff686fe12d | -10.54376 | -42.43096 | 2025-01-25 03:49:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5fc43ddc-56da-3afb-b817-ad39a78f57c4 | -10.50434 | -42.4243 | 2025-01-25 03:49:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 6785920e-1a0f-3c26-967b-fc702305b75a | -12.53581 | -48.3219 | 2025-01-25 03:49:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a9573cf-c656-3b9d-b1a1-79d663698168 | -16.60158 | -46.78945 | 2025-01-25 03:51:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6117a83-9734-3d8c-92ac-d0e265618290 | -22.74582 | -42.95369 | 2025-01-25 03:51:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3ac8af65-a9ea-3233-84be-ec9791ad4a54 | -18.42859 | -40.0333 | 2025-01-25 03:51:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9326dfa1-8abd-371f-9fe5-39434d7b182c | -19.32589 | -40.062 | 2025-01-25 03:51:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fa6f5168-d0cf-31e6-afac-627622134321 | -22.67867 | -42.85303 | 2025-01-25 03:51:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| d8042c13-1fe1-32de-b962-3c670cdce7ea | -22.73751 | -42.96055 | 2025-01-25 03:51:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5248e49a-6e93-3132-aba9-7de540ce7548 | -16.63868 | -39.64475 | 2025-01-25 03:51:00 | NOAA-21 | ITABELA | BAHIA | Brasil | 2914653 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 07380e01-8ab7-3329-b517-1afad1e25e43 | -16.59961 | -46.79242 | 2025-01-25 03:51:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78b7a3eb-45c1-34d3-b785-3143b7a073e0 | -21.18711 | -48.63433 | 2025-01-25 03:51:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0935a277-b8c0-37fd-af64-2ad71299bf67 | -21.98327 | -42.13314 | 2025-01-25 03:51:00 | NOAA-21 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ff788d10-c746-39a6-a38f-134dc4071344 | -15.07672 | -48.94656 | 2025-01-25 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37012159-16d2-3c33-a40e-3df8d55dbccb | -17.48995 | -45.25882 | 2025-01-25 03:51:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54429c2a-f635-3728-97e9-dd3d06205c41 | -18.59442 | -39.95388 | 2025-01-25 03:51:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 514a7e7d-a621-3166-bc0d-ddbf6c3b9dc0 | -21.16985 | -41.92404 | 2025-01-25 03:51:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 895b5a7a-e688-38a3-887c-563d69da5773 | -15.07837 | -48.94545 | 2025-01-25 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b376a37c-906c-3c23-bbc1-cc8d11c88642 | -18.0407 | -39.92547 | 2025-01-25 03:51:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5893f543-d0de-3c68-9051-c9cf66937b3e | -20.90026 | -43.81978 | 2025-01-25 03:51:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 02100adc-fab5-3784-bfc4-7c6808bc1a44 | -15.56773 | -47.8548 | 2025-01-25 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18c8858c-4e01-35e4-8e8d-ce1f81502050 | -16.67967 | -43.88476 | 2025-01-25 03:51:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b45ff104-512d-3086-aa72-f9180766fe6d | -22.27978 | -48.57316 | 2025-01-25 03:51:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.5 |
| 25c3130e-9b04-3c91-a363-aa857b866019 | -22.78214 | -43.04479 | 2025-01-25 03:51:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e226258c-2652-301d-a3c2-9783be680d9a | -22.28094 | -48.56765 | 2025-01-25 03:51:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.5 |
| b17f0e7d-a51d-3f60-b4b2-a37a4c42ea20 | -16.39926 | -49.19597 | 2025-01-25 03:51:00 | NOAA-21 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c8aecf1e-8190-3b90-8625-895a5e9a04e6 | -22.67455 | -42.85641 | 2025-01-25 03:51:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0336bf9c-e1e8-3dc3-99d8-1e673a261516 | -22.6996 | -43.34903 | 2025-01-25 03:51:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7623d9fd-d651-3c21-937e-b48318074483 | -21.98264 | -42.13692 | 2025-01-25 03:51:00 | NOAA-21 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 03b1323e-dd51-3009-be87-b2bc02d33544 | -16.421 | -40.49315 | 2025-01-25 03:51:00 | NOAA-21 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b868f0b5-271a-3d4a-9177-e0e56a6d8711 | -20.97295 | -43.85798 | 2025-01-25 03:51:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4fd7380e-99c7-3565-abf1-22da78019552 | -22.67799 | -42.8571 | 2025-01-25 03:51:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9211bf6d-e2e2-3fcd-88b7-f2c45de5dcea | -17.43875 | -39.49238 | 2025-01-25 03:51:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ad89ef24-a602-316d-86d2-36a121e3000a | -20.41692 | -43.55207 | 2025-01-25 03:51:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a9b36a35-2066-3b5e-b476-a513db95d19e | -21.97989 | -42.13248 | 2025-01-25 03:51:00 | NOAA-21 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6e107e20-7271-3964-bbc5-b884a3b7911a | -21.98665 | -42.1338 | 2025-01-25 03:51:00 | NOAA-21 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d4c2539a-57bd-3e33-8197-0e57c7d86bb9 | -16.26207 | -44.04456 | 2025-01-25 03:51:00 | NOAA-21 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c027d71-b961-3e74-9675-b2f8ad2352da | -21.97926 | -42.13627 | 2025-01-25 03:51:00 | NOAA-21 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2f5c57c3-f139-38ca-90a3-83243564e143 | -19.10001 | -43.88843 | 2025-01-25 03:51:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cda1c8bc-99ae-3f53-b51f-9123ac3a66e2 | -21.18229 | -48.63308 | 2025-01-25 03:51:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ecb5a45a-f708-3378-8d29-b2c1677f90ba | -8.49813 | -43.28696 | 2025-01-25 04:14:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 28506fac-8f94-3660-b3ff-bb8b2af4d886 | -7.69542 | -41.66647 | 2025-01-25 04:14:00 | NPP-375D | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f5d65d57-5db6-32e7-bd19-9e98100e3f67 | -2.88372 | -48.27251 | 2025-01-25 04:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be2ba734-2629-3935-89b7-09df5322328a | -8.46447 | -37.816 | 2025-01-25 04:14:00 | NPP-375D | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e1cf2ac2-6e91-31e4-a41a-c055420df28e | -8.46877 | -37.81665 | 2025-01-25 04:14:00 | NPP-375D | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5a25cd32-8aa7-39a7-8ff2-5d7b6591d3b5 | -3.24736 | -48.07412 | 2025-01-25 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9974db8a-5c60-3951-afd8-70bde4ba8a14 | -7.69198 | -41.66595 | 2025-01-25 04:14:00 | NPP-375D | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 894de080-51c3-3956-a7ec-313b8e22a960 | -4.81424 | -37.75225 | 2025-01-25 04:14:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 50343d0d-1556-3c83-8418-271f35aa7a41 | -9.55878 | -42.85786 | 2025-01-25 04:14:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7a8e6a67-a3ad-377d-831d-1915b9fc6e2d | -8.11716 | -43.13025 | 2025-01-25 04:14:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 3adec267-c0f9-3c60-b251-1bca359e9945 | -1.87778 | -48.71664 | 2025-01-25 04:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd64a2f3-7955-362f-8319-2ce000158485 | -2.88435 | -48.26857 | 2025-01-25 04:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2bee034f-9ca3-3cee-86fc-9242261d068a | -7.39146 | -42.77238 | 2025-01-25 04:14:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 142d6406-3212-302c-a826-d02ae099e167 | -8.46018 | -37.81536 | 2025-01-25 04:14:00 | NPP-375D | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8223a341-baa5-39bc-b765-51ead4e70373 | -8.50146 | -43.28749 | 2025-01-25 04:14:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d0799836-4826-38ad-986c-81faa4989f9b | -8.46934 | -37.81262 | 2025-01-25 04:14:00 | NPP-375D | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 31632c5f-ca8c-3492-ac8c-17b6e5a13b21 | -4.81833 | -37.75286 | 2025-01-25 04:14:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c2cce617-adc8-3e04-b551-c544df41275a | -3.1766 | -48.03236 | 2025-01-25 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f37e7443-12f8-3db9-848a-5b70dfc8f859 | -7.39201 | -42.76886 | 2025-01-25 04:14:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e711c0c8-6600-30ed-a563-b9ca508cf6a1 | -8.12049 | -43.13077 | 2025-01-25 04:14:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1bd644db-468f-3927-b6ed-d748d7740861 | -9.29511 | -43.27217 | 2025-01-25 04:14:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 289673fe-00f1-39b0-9751-7b546537c636 | -2.8825 | -48.27134 | 2025-01-25 04:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 51cc9dfb-0590-39bc-9eee-0185377662ac | -10.50784 | -42.42258 | 2025-01-25 04:16:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 193e2210-ee1b-3c6d-82b8-a494419182a8 | -15.07838 | -48.94706 | 2025-01-25 04:16:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1039014-f5b3-3a87-931d-d70e323edb95 | -15.17821 | -43.4264 | 2025-01-25 04:16:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 69442891-9323-33f8-a3f0-519198cbbcf4 | -11.05771 | -45.37959 | 2025-01-25 04:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ada62aa4-5e52-3879-aec6-1d3efbc6c9cb | -10.50042 | -42.42525 | 2025-01-25 04:16:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 048e27ad-9a31-3828-bba7-42d6aebec79f | -15.07913 | -48.94269 | 2025-01-25 04:16:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a12ae7cb-296d-3821-aef0-24d28628e7fc | -11.65171 | -43.91942 | 2025-01-25 04:16:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c74f6691-0311-3fa0-a3e0-55cffa63470b | -12.91045 | -45.09823 | 2025-01-25 04:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f049ffe-ada7-3c85-b385-dfcb468c09b8 | -10.62226 | -37.04021 | 2025-01-25 04:16:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d6e860c0-fb8b-3d06-ba5c-530150fabcf0 | -12.50726 | -54.57717 | 2025-01-25 04:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9250bd22-12b3-33f2-aeb8-7088820555ce | -9.5972 | -47.69363 | 2025-01-25 04:16:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13105c5e-469d-344d-b078-c918eca89188 | -10.94429 | -48.07667 | 2025-01-25 04:16:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 711c6d5d-2b30-3552-a986-c05b269a5049 | -14.03589 | -45.51013 | 2025-01-25 04:16:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e857f090-0ccc-3949-9db7-46e6a20d4a6a | -12.53504 | -48.32226 | 2025-01-25 04:16:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 924715e9-6280-3715-8c8d-ec3cc0413161 | -10.62158 | -37.04522 | 2025-01-25 04:16:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 488d50e6-faf1-329e-84da-25eeaa71d7bf | -12.11409 | -43.63798 | 2025-01-25 04:16:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f525fff5-6e94-3316-979f-a0b28fb742c5 | -9.5244 | -47.7806 | 2025-01-25 04:16:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c176bd1-53c1-33e0-b1a6-42284f8be814 | -17.09318 | -43.80345 | 2025-01-25 04:16:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6cdd207d-488a-3d58-8ab4-e22fe0501798 | -9.52815 | -47.78122 | 2025-01-25 04:16:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cffdb0ad-dca6-3f7e-a82b-f576eeaeab0d | -11.03576 | -46.11493 | 2025-01-25 04:16:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 661b0132-c52f-3e7d-bd2a-fc5f1dda2977 | -11.28146 | -44.44917 | 2025-01-25 04:16:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4b3dc4d-8146-371b-8530-97488e7b98e4 | -12.46524 | -43.59645 | 2025-01-25 04:16:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4058ba8-034c-314a-97a3-a799a5f80155 | -11.27813 | -44.44864 | 2025-01-25 04:16:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4f040f3-dec1-3787-b296-8aff4e6a5000 | -10.50385 | -42.42578 | 2025-01-25 04:16:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 9e9b4c1b-9211-38f6-8bbb-8f046a6bf5d4 | -16.60006 | -46.79225 | 2025-01-25 04:16:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb7896d7-6cbd-34c9-9ec7-79e885a16cd6 | -16.68006 | -43.88496 | 2025-01-25 04:16:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 702d667b-5fdd-37e2-aaec-056f35de462a | -12.11354 | -43.64157 | 2025-01-25 04:16:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67791bb8-6dd0-31e4-b63f-bb0db1443ab6 | -10.50727 | -42.42632 | 2025-01-25 04:16:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eed8dcbd-f861-3300-8fec-6bb02c67da71 | -19.09848 | -43.88665 | 2025-01-25 04:18:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README4.md)
