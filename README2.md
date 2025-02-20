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
| 035596b1-57f7-3ec2-b020-842abcdca20f | -19.94308 | -40.73877 | 2025-02-20 03:12:00 | NOAA-20 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d8eb87f5-d80c-332e-b8ca-89f382858a20 | -19.94227 | -40.74253 | 2025-02-20 03:12:00 | NOAA-20 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 587b7ad5-4148-39d1-9130-22e1daf68521 | -18.58318 | -39.83766 | 2025-02-20 03:12:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| aa7cc305-2d12-3292-93d9-26ec9516bc6d | -20.56736 | -42.39473 | 2025-02-20 03:14:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 83894314-4ef4-3aac-9544-22a339ff303b | -22.67601 | -42.85731 | 2025-02-20 03:14:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3f3b9da6-7d7a-303e-8a92-14bd15f79284 | -22.88906 | -42.44074 | 2025-02-20 03:14:00 | NOAA-20 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 607beed3-8b3c-396a-b368-4645ca060668 | -22.67492 | -42.8619 | 2025-02-20 03:14:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7dcd4938-cd6a-3d85-8858-5437a64d4537 | -22.89003 | -42.43646 | 2025-02-20 03:14:00 | NOAA-20 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5f9638b1-5065-3d5f-a867-a9181802560a | -20.56643 | -42.39879 | 2025-02-20 03:14:00 | NOAA-20 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dee284b2-ded8-3353-94c6-f20464449c38 | -21.41331 | -42.21605 | 2025-02-20 03:14:00 | NOAA-20 | MIRACEMA | RIO DE JANEIRO | Brasil | 3303005 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 74752731-197e-3bc5-bcb4-ce73b4b7ce65 | -4.91438 | -37.48847 | 2025-02-20 03:59:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 422324a4-1bfe-39c8-b441-7b25ef22c27e | -4.534 | -38.14412 | 2025-02-20 03:59:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 99441c2f-9460-31ad-9263-f43855c2341a | -4.86919 | -38.37729 | 2025-02-20 03:59:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| e2e78b4e-adae-3212-8197-827037794571 | -4.44539 | -38.05753 | 2025-02-20 03:59:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0a844384-6a24-35d4-bde4-eb05cc495656 | -4.91495 | -37.48472 | 2025-02-20 03:59:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ab13c989-38ca-3f07-9280-c8597eb51aa3 | -9.29767 | -43.17776 | 2025-02-20 04:01:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2b99e64f-03e4-3934-b96d-3bf8b76fc212 | -8.12737 | -43.13678 | 2025-02-20 04:01:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3bca21f0-33c1-3a50-96bd-52f231ac764b | -12.7964 | -45.01113 | 2025-02-20 04:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1387cc89-a8bc-3690-b355-c6a159c888e3 | -10.69622 | -37.05138 | 2025-02-20 04:01:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a449b4cb-2aba-349b-aae5-43e5a6fadcfb | -10.75373 | -37.17974 | 2025-02-20 04:01:00 | NOAA-21 | RIACHUELO | SERGIPE | Brasil | 2805901 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 63614e3d-dc1b-3cf9-a4cc-2b4efa643b61 | -12.79764 | -45.00772 | 2025-02-20 04:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 053f233a-10d9-34be-a1f5-35a7e7718bac | -10.75796 | -37.04669 | 2025-02-20 04:01:00 | NOAA-21 | SANTO AMARO DAS BROTAS | SERGIPE | Brasil | 2806602 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| ed9b75f1-d34c-3881-af14-c79f89299166 | -12.7969 | -45.01215 | 2025-02-20 04:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6caca7b3-d237-3382-82bd-2716b0233f0f | -12.20288 | -40.28075 | 2025-02-20 04:01:00 | NOAA-21 | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 841a1905-d364-3633-aab5-acc7d742d99f | -12.79716 | -45.00671 | 2025-02-20 04:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c3770f5f-19ec-3189-91f4-6db1e616da80 | -10.54204 | -45.2154 | 2025-02-20 04:01:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| afc5581e-5c22-3043-9a7e-427783c65f4b | -11.03165 | -45.05695 | 2025-02-20 04:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c2bd178-d13f-309f-a8ba-b3adeb4afd3a | -12.79349 | -45.00606 | 2025-02-20 04:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 49647095-b1de-3e22-b911-7a40780f6c31 | -8.12671 | -43.14078 | 2025-02-20 04:01:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9b9b0e1a-2e6b-30a7-a4c1-ef29b3cc5a77 | -11.57319 | -47.63711 | 2025-02-20 04:01:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08575654-d474-3e95-acf5-5f188ba05656 | -10.43406 | -44.88794 | 2025-02-20 04:01:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0d82e7d-70c5-368c-84ca-44e61e2ca722 | -10.54588 | -45.21603 | 2025-02-20 04:01:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d9524410-3aac-307b-88f0-03fe58f6ffe2 | -11.11033 | -45.12078 | 2025-02-20 04:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4959f761-4cb3-37eb-a940-1d75fbd9a62f | -12.80006 | -45.01179 | 2025-02-20 04:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b296e51c-87c9-37cc-a672-19af10770d77 | -12.49962 | -44.32623 | 2025-02-20 04:01:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11897399-f564-3988-a21d-0c6f9f370aea | -11.15662 | -38.05025 | 2025-02-20 04:01:00 | NOAA-21 | TOBIAS BARRETO | SERGIPE | Brasil | 2807402 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 79f336de-cc2f-319f-84b7-c412ad3105a2 | -12.79792 | -45.00229 | 2025-02-20 04:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f342435-065c-368c-b49e-b3049b4ddb9c | -11.9196 | -43.12173 | 2025-02-20 04:01:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 62e654c3-0c57-3ef1-afa9-83485538c88f | -8.90481 | -43.88682 | 2025-02-20 04:01:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86128d10-a491-3c12-b8ec-cd3a85fa916a | -11.57829 | -47.63523 | 2025-02-20 04:01:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88e7b371-d90c-309a-a5bf-b778be0f27c1 | -11.57998 | -47.62481 | 2025-02-20 04:01:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13059da6-9c49-3718-a8ee-04c85d8ebbbe | -12.79398 | -45.00706 | 2025-02-20 04:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4749808-588a-3afc-854c-261a85b254ec | -9.22471 | -40.5169 | 2025-02-20 04:01:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1b866034-023c-3b34-8ab6-9a0f05153202 | -11.57758 | -47.63793 | 2025-02-20 04:01:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 678a91a2-0d08-3e6a-b37b-b90a98e49f2f | -11.57751 | -47.63968 | 2025-02-20 04:01:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7d67477-1a74-3973-b8f7-9439e0abc46d | -10.75743 | -37.18032 | 2025-02-20 04:01:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 06cfda0d-3809-3bd2-996e-50a10688743e | -12.79838 | -45.00329 | 2025-02-20 04:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e5b01e4-23f7-3379-80db-6c59d216c4c5 | -11.69318 | -47.80143 | 2025-02-20 04:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be7aeae2-f1f5-3afd-aad9-e22e811ac37c | -11.92022 | -43.11798 | 2025-02-20 04:01:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d600411e-682c-369c-9eab-0a86b265778d | -12.80296 | -45.01688 | 2025-02-20 04:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d434efbb-a450-3197-ad8f-85900595114d | -11.96473 | -44.66409 | 2025-02-20 04:01:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f4cbc771-715c-3537-a807-eb90efde3a64 | -9.16099 | -43.1206 | 2025-02-20 04:01:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| faf721d8-9d66-3116-9932-6d5b0e0e9f45 | -12.79471 | -45.00264 | 2025-02-20 04:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de8883e2-97ea-3685-9da6-3443a3ddcac3 | -10.75616 | -37.1778 | 2025-02-20 04:01:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9cf52483-8f47-3e8a-941e-ad6a8652e84e | -10.75731 | -37.05116 | 2025-02-20 04:01:00 | NOAA-21 | SANTO AMARO DAS BROTAS | SERGIPE | Brasil | 2806602 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| edf09957-a661-3b37-bbc6-1f6c4b845b5d | -8.72598 | -44.01381 | 2025-02-20 04:01:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 57cdc4e5-a4e0-339b-a9b0-b35d6f7d2885 | -8.72523 | -44.01822 | 2025-02-20 04:01:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 68c1f127-e6cf-35bd-a2b2-19447e9eba31 | -10.54507 | -45.22084 | 2025-02-20 04:01:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dafe5b98-0f1b-3e67-a27f-bfc13681b6b8 | -12.8611 | -38.36555 | 2025-02-20 04:01:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 741b1562-c724-3ec7-9d0b-0ee03e6f9acc | -11.57389 | -47.6344 | 2025-02-20 04:01:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2691a277-e489-356e-925b-381bbb5a758a | -12.7993 | -45.01622 | 2025-02-20 04:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 47b630bc-b37f-31c4-a0a0-eae2f889adfd | -11.57982 | -47.62647 | 2025-02-20 04:01:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70f40e32-ee35-3bc8-8257-f0cbf50328c5 | -8.72964 | -44.01442 | 2025-02-20 04:01:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 931b8d62-0e87-3dbb-b0ba-1ba568802d64 | -11.03087 | -45.06157 | 2025-02-20 04:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 221b6c8c-8198-39d3-bb6a-a1b150f95e5b | -12.55063 | -43.10729 | 2025-02-20 04:01:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| de569c76-7dbb-3683-9f1b-706a50f0ba41 | -8.72305 | -44.00878 | 2025-02-20 04:01:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c5bdbc6-bb65-3403-a80b-430120d550b4 | -12.80586 | -45.022 | 2025-02-20 04:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c60907c2-aec6-3e1a-91d7-431a3d1a622f | -12.79426 | -45.00164 | 2025-02-20 04:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe3b68c1-0ec8-37ef-a709-feb5d1d3528a | -10.76349 | -37.2064 | 2025-02-20 04:01:00 | NOAA-21 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8b02f2ca-a8bb-39d6-91e6-b9271f4ae0cc | -11.574 | -47.63269 | 2025-02-20 04:01:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d757f1b5-81bc-3232-82a8-256b882af75e | -10.54123 | -45.22022 | 2025-02-20 04:01:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8ef9251-d34d-3b5e-93f9-cfafb59f8599 | -20.8057 | -44.12703 | 2025-02-20 04:04:00 | NOAA-21 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 905ad94f-a695-3f3a-9655-60a69de43b5e | -20.29575 | -46.50946 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f9b4345-bc23-30ed-ab36-69e901e8a074 | -20.24399 | -46.47791 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a7a7fe0e-dd25-375b-a9a9-488cedd45a14 | -17.27779 | -46.91071 | 2025-02-20 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f9543997-8515-3346-8b3b-d77799d5af27 | -14.41238 | -45.63464 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e286e2ef-849e-3d6a-870d-bd46d2b9ea70 | -19.82682 | -45.67132 | 2025-02-20 04:04:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c8409ac-660c-3762-aef6-46ee9e7004f5 | -20.31077 | -46.50849 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 148e5cbb-3dae-3aed-8d53-b57d10075620 | -15.55565 | -46.27473 | 2025-02-20 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d5d83ea-698b-38e6-96a8-a38d4d330c39 | -20.20713 | -46.49765 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e0d83a0-d9e0-3ba2-be13-0a9be994029e | -17.46409 | -47.01129 | 2025-02-20 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fea0f7b7-4918-37d5-a5a9-32cba672c487 | -14.42609 | -45.65397 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb67f5c2-638d-36fe-a9d4-a1cb2b6f2129 | -17.46025 | -47.01057 | 2025-02-20 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8f12fb71-1d36-30bf-b285-984889a32b8e | -16.61549 | -43.33929 | 2025-02-20 04:04:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 97b233d8-b069-39d0-b523-44b54dbd05fb | -20.21396 | -46.52206 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20fa6a30-5431-30ee-bdd6-75355a078bf5 | -20.21194 | -46.51248 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 134793de-853c-37d8-b26a-2c9b0cca6b38 | -14.42568 | -45.64646 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d16687be-0a9c-3788-91f4-5450a144de34 | -20.16802 | -47.28293 | 2025-02-20 04:04:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9b292c6-d910-3171-be7c-72ddaaabdb97 | -20.22396 | -46.52861 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 285639ec-e2e6-3d54-bec9-f71958c8d46a | -20.23914 | -46.46327 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a2d78d0f-b24c-3c32-b47d-45d818b0df11 | -16.63088 | -39.86798 | 2025-02-20 04:04:00 | NOAA-21 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a56360e9-97da-3106-920f-adec9d58fcd1 | -14.47497 | -45.81506 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ac22daa-20e1-392a-994a-dd551abc9b3e | -20.29218 | -46.50867 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8944fa89-0820-3b66-98e3-d6787344a524 | -20.21306 | -46.48508 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91e197ac-13d6-3adc-81df-622f717a8f76 | -20.23762 | -46.53559 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d662d050-1996-3f9c-9b02-10c8161207e8 | -14.43311 | -45.6478 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbf085a1-2333-388b-ba95-3a10452dd05f | -20.20915 | -46.50722 | 2025-02-20 04:04:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b8f3bab-b483-3924-9a07-6bd8bf3efc3e | -20.02202 | -47.18098 | 2025-02-20 04:04:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c83fcb9c-7a1e-3168-9068-2eedb5482b89 | -14.42689 | -45.64941 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ad8cd4b-e317-3cf3-a208-ebb1736f34ea | -14.4513 | -45.66321 | 2025-02-20 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README3.md)
