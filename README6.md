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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ed5b2eb-aef7-3b6e-ad9d-53917592b02d | -3.3957 | -47.5003 | 2025-07-18 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 9a4b9f25-604f-3ddf-abcc-e3803aa77757 | -5.6567 | -43.7161 | 2025-07-18 03:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 217.5 |
| 310988e1-eaa0-389e-b53e-26c6437db4b2 | -5.6569 | -43.6929 | 2025-07-18 03:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 776eefb2-f6df-30df-b712-a6d5979666f6 | -5.6379 | -43.7175 | 2025-07-18 03:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| e0fddd9a-5aef-3cca-b8d5-54738a171c0d | -11.7317 | -48.1849 | 2025-07-18 03:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 93d38361-0156-3bbc-b0f2-9666b30a9e61 | -3.3958 | -47.4785 | 2025-07-18 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 132.8 |
| 4cfc2f6d-5154-35c4-8b02-60a5b38cc7bf | -9.48774 | -40.39358 | 2025-07-18 03:15:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| d1a16c6c-79c8-3559-8e94-35b3a5a01dda | -9.48911 | -40.39223 | 2025-07-18 03:15:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 69e57158-883d-3312-857d-094c0c1d7a3f | -9.53551 | -40.32655 | 2025-07-18 03:15:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 65c69bff-fd75-3f88-98ce-70b25492d83e | -9.48801 | -40.3979 | 2025-07-18 03:15:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| b94c760e-2bbd-38d3-9045-40a6d5b1a09b | -9.54113 | -40.32921 | 2025-07-18 03:15:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 8ceab4df-c4ef-3d97-a69a-1fa7e7055295 | -9.53574 | -40.32242 | 2025-07-18 03:15:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| e18b4d51-adad-3ebd-a5e6-41ce27357b03 | -9.53465 | -40.32791 | 2025-07-18 03:15:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 3c92ff48-f15b-3019-a50c-44af616c7197 | -11.87938 | -40.9531 | 2025-07-18 03:15:00 | NPP-375D | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7853ba59-24e8-3ca4-b047-e3369c12d465 | -9.54199 | -40.32788 | 2025-07-18 03:15:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 88d74c4e-f272-302b-bf48-c5fd83f3bb37 | -9.48661 | -40.39923 | 2025-07-18 03:15:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 25997e17-4e37-3f98-805b-0e07ef8b794b | -15.18526 | -43.53826 | 2025-07-18 03:17:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d7256fbf-85bf-362a-98e3-44ac8b652f4b | -15.63634 | -41.26047 | 2025-07-18 03:17:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e6339b47-56bb-3daa-a892-250824edd707 | -20.04407 | -41.66949 | 2025-07-18 03:17:00 | NPP-375D | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 4657a774-e02b-3714-a4c4-cc7bd66beb56 | -20.0394 | -41.66307 | 2025-07-18 03:17:00 | NPP-375D | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 9dfb2778-96cd-3969-b5d6-78d7d59db9db | -15.64247 | -41.26196 | 2025-07-18 03:17:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6e1bfd09-9b9f-38c4-99cf-1c4324dd5705 | -15.6413 | -41.25761 | 2025-07-18 03:17:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6bc496ad-ff12-3d76-8d71-cd2a283d7037 | -18.60942 | -44.26596 | 2025-07-18 03:17:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 263f4661-da45-3769-9f48-37f063e1c92d | -15.63746 | -41.2552 | 2025-07-18 03:17:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 78999f1b-fe28-3716-82db-fdc420949c8c | -18.61323 | -44.2728 | 2025-07-18 03:17:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 32914fd7-e955-3888-b271-454279aa5bbf | -20.03836 | -41.6677 | 2025-07-18 03:17:00 | NPP-375D | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 1654b291-ee10-3f67-89ee-7ef1ee2d5990 | -18.61627 | -44.26778 | 2025-07-18 03:17:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f17728d-4dd1-3bd6-9783-bd4995d358bb | -15.64017 | -41.26272 | 2025-07-18 03:17:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 041f927a-5086-3e4f-9ca9-6586b2782ac6 | -18.6149 | -44.26598 | 2025-07-18 03:17:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c078c3bf-286e-36dc-a32f-f53c0ad795e0 | -22.58419 | -44.08488 | 2025-07-18 03:19:00 | NPP-375D | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3968fda4-df5a-3938-a559-93d893e4916d | -22.57854 | -44.08361 | 2025-07-18 03:19:00 | NPP-375D | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b04f7c87-ad6a-3bbf-b50a-b4fb61a1faa1 | -22.57793 | -44.08299 | 2025-07-18 03:19:00 | NPP-375D | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2cfe44a6-0e4d-38b7-b98c-8cc9826d441a | -5.6379 | -43.7175 | 2025-07-18 03:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| f175a901-5e9c-3df6-a0af-f53d8eb9f855 | -3.3957 | -47.5003 | 2025-07-18 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 00da02d4-4482-3e56-a54d-bdaf20dd644a | -5.6569 | -43.6929 | 2025-07-18 03:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 84552fad-6b23-3696-9c22-09fabb911346 | -3.3958 | -47.4785 | 2025-07-18 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 73b13bb2-23d2-307f-8532-11b046b87caa | -11.7317 | -48.1849 | 2025-07-18 03:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 24db82dc-7ba5-383a-8602-98281d8f493f | -5.6567 | -43.7161 | 2025-07-18 03:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 244.0 |
| 91822552-4679-3100-a54d-7ff6023dda80 | -8.0886 | -43.1431 | 2025-07-18 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| 01e1eacc-e236-3a6f-88d8-8a0aa4dea429 | -5.6569 | -43.6929 | 2025-07-18 03:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 54c444ab-b38f-35e1-a11f-e069137ee489 | -9.5343 | -40.3282 | 2025-07-18 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 82.3 |
| a64b818f-1a31-31a9-b8bf-64b9fb1e42a4 | -3.3957 | -47.5003 | 2025-07-18 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 3002dc43-9071-36c0-a0ac-64730d012eb3 | -11.7508 | -48.1825 | 2025-07-18 03:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 1af89c03-4b77-3ab2-9ad8-09c4f8686f56 | -8.0886 | -43.1431 | 2025-07-18 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 4a72636f-561a-360e-81fb-059382f51ae5 | -23.7017 | -51.6543 | 2025-07-18 03:30:00 | GOES-19 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 75.3 |
| 567fd0c6-7f4f-3420-8529-cfefb54d16ac | -3.3958 | -47.4785 | 2025-07-18 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 123.5 |
| e7183cd2-a98e-3857-ae4e-b56f3ca204e4 | -5.6567 | -43.7161 | 2025-07-18 03:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 186.0 |
| dc21d953-91b5-36a1-aa86-848bf31512c3 | -5.6379 | -43.7175 | 2025-07-18 03:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| fb587fe4-5fa9-3886-8108-3a868e8ecb5b | -4.48046 | -46.07949 | 2025-07-18 03:34:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76bd5ed2-8644-3531-9667-0b6cff8e2737 | -5.75722 | -43.40195 | 2025-07-18 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42ae0c40-53c0-3f47-b383-c163a9483ed6 | -4.52231 | -42.06936 | 2025-07-18 03:34:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f4bf1001-9b41-3739-b55a-c7fc08443f93 | -5.64656 | -43.71879 | 2025-07-18 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| bf06817d-35f6-375b-9a41-fe3dad2a9f85 | -4.4815 | -46.0735 | 2025-07-18 03:34:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a60e2205-935c-303c-92f0-0619f3696fe2 | -5.52771 | -43.887 | 2025-07-18 03:34:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 16d00e08-ac23-3d64-9dc4-5de85a59ddee | -5.48544 | -43.07814 | 2025-07-18 03:34:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e6ba5503-7ca8-303e-9de1-9ed8bf9ee723 | -4.7965 | -43.22528 | 2025-07-18 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c5a20a73-d07f-393b-b33e-b82839f7ce06 | -5.68683 | -39.28479 | 2025-07-18 03:34:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 62e00ba0-3791-3df0-8bbb-db31d4b3edec | -4.48417 | -46.07672 | 2025-07-18 03:34:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8017a533-894f-3e47-94dd-92a519afcef3 | -5.64834 | -43.72001 | 2025-07-18 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 48694d96-5515-39b9-b653-cdd45a7434d7 | -5.65863 | -43.71668 | 2025-07-18 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 4bec9b6b-2c93-321c-ac99-40c5ad6ce409 | -5.48481 | -43.08173 | 2025-07-18 03:34:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3e9abef1-1fef-3d27-8d68-80dd4d207294 | -5.75787 | -43.39824 | 2025-07-18 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57d7765e-1960-38c6-ace7-d622ba6332b0 | -4.47757 | -46.07504 | 2025-07-18 03:34:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fedaa0cb-d36b-30b9-a7e8-44ddd1f52f1f | -5.64906 | -43.71603 | 2025-07-18 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 5223a37c-68be-314f-a552-ff257980d3bc | -5.65362 | -43.71181 | 2025-07-18 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 5907ee72-df6d-3a1b-ad05-8d6246a137d2 | -5.65294 | -43.71572 | 2025-07-18 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 21c03dc5-1f6b-3a7e-b249-6c3f555d5e9c | -5.66114 | -43.71404 | 2025-07-18 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 1231ddb0-8c1c-3d91-aef0-5ce8158cf66f | -5.52854 | -43.88673 | 2025-07-18 03:34:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 488fa343-f21f-3ae5-ad04-fef7dc53a2f7 | -5.65476 | -43.71694 | 2025-07-18 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 2df06352-d11d-3102-919d-c98be0e54b01 | -5.65226 | -43.71968 | 2025-07-18 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 8ca0b06c-08d3-3ea5-9c4c-6ae8278f7993 | -3.60634 | -43.54362 | 2025-07-18 03:34:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a863ff4b-aa18-3fad-bef7-845ad6b87a51 | -5.66045 | -43.71785 | 2025-07-18 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 3a62cfbd-e5b8-3976-8aa6-b276ad0aeb1f | -5.78986 | -43.62989 | 2025-07-18 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 571a922d-da53-31d6-bd01-19d74e179cb6 | -5.79551 | -43.63082 | 2025-07-18 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 06d6217f-e13d-3aad-88ef-9a53c140dd89 | -5.65157 | -43.72371 | 2025-07-18 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 68ef7f14-4c1f-3424-b7c5-d8cdce2cd665 | -5.65975 | -43.72173 | 2025-07-18 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 31229368-4145-3f02-849d-d7b1a36a0d80 | -3.80466 | -43.22665 | 2025-07-18 03:34:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ccdb5e1-2988-3114-9d14-edfd0921ed1e | -3.80227 | -43.22736 | 2025-07-18 03:34:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67e64260-737c-3f1f-afeb-6abe8de9041c | -5.1975 | -45.49162 | 2025-07-18 03:34:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a6c39091-7273-371d-91ae-53dad5b3585f | -4.52284 | -42.06622 | 2025-07-18 03:34:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dc020520-0970-3c83-a7b4-c193dce5ad82 | -3.60563 | -43.54786 | 2025-07-18 03:34:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 768da6a3-e3e4-388a-a942-fce16f22a354 | -4.80273 | -43.22253 | 2025-07-18 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e4dc7bf1-bcfb-34df-b1bf-8e0827d559a7 | -4.90609 | -37.29602 | 2025-07-18 03:34:00 | NOAA-20 | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9807adb4-ed9f-368a-a36b-a19c9c9a4f18 | -6.9512 | -35.81159 | 2025-07-18 03:34:00 | NOAA-20 | REMÍGIO | PARAÍBA | Brasil | 2512705 | 25 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a56621c4-7479-3cb9-a5c5-d9c68a8b9a66 | -5.47967 | -42.14697 | 2025-07-18 03:34:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8d260ff3-6365-3e94-96b7-0c0718025f08 | -3.61215 | -43.54463 | 2025-07-18 03:34:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43834790-7d76-3066-9cc6-6a9d344dec9e | -5.65546 | -43.71304 | 2025-07-18 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 735c6eb9-8bc8-3cb5-b7d2-d82d92af0f10 | -4.80208 | -43.2263 | 2025-07-18 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8ea9d2c2-0011-3baa-9649-95757b1fca47 | -5.65614 | -43.70924 | 2025-07-18 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 95b2f05e-2233-3a35-ba6d-43cc0f733c97 | -5.64793 | -43.71088 | 2025-07-18 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 2671e292-5146-3d29-8579-b12d9a53747a | -4.58866 | -43.31578 | 2025-07-18 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37ec449c-fa6b-3c96-9043-cbb36117f56a | -5.64725 | -43.71479 | 2025-07-18 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 8ecf36e5-22b5-379c-a628-82d4a1749f38 | -5.36285 | -45.12716 | 2025-07-18 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0024322d-16f9-3560-8e1f-dda81cb6f7ab | -5.75166 | -43.40102 | 2025-07-18 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fcd3ae8-ee08-35f0-9364-809afa31f348 | -5.65428 | -43.708 | 2025-07-18 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 019052a0-92b8-30fd-9c72-d5c203f525f6 | -4.58799 | -43.31968 | 2025-07-18 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb9eb367-0f5f-318e-ac36-a97f93838b72 | -5.79187 | -43.63407 | 2025-07-18 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 216f2f75-a277-3863-b7ae-1c146c1461d2 | -5.64977 | -43.7121 | 2025-07-18 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| b07dc4c7-efef-314a-8fba-6874274272b8 | -4.58933 | -43.31194 | 2025-07-18 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 413b36ba-417e-3029-9a13-06796b2b547e | -5.19851 | -45.48595 | 2025-07-18 03:34:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |


[Clique aqui para ver as próximas entradas](README7.md)
