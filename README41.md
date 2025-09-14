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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f2d15e2-8725-35ad-8f96-c6a43aab62ae | -11.47058 | -50.78964 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61330ab4-dd12-3d86-98a0-e077115bcd1e | -8.41566 | -47.24172 | 2025-09-14 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71b405bd-6888-325f-a2e2-8a038e7166cd | -8.62605 | -40.20153 | 2025-09-14 04:40:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2d6cb03c-8ebf-3560-85ff-4d1fd90d342d | -6.62108 | -46.39357 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b51e4427-a515-32e7-be90-644354876179 | -12.76065 | -47.99878 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f85f58d7-2bfe-3b46-bf33-7ae6358b061b | -12.7873 | -47.99137 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3ba0fe32-2259-3c08-b8da-5c0a0194272b | -11.48375 | -50.74873 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb0842f9-9406-3aa1-9db7-8554c4d83c11 | -11.14037 | -47.65189 | 2025-09-14 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 806b3b8c-6ed9-35df-9ad5-95fc8a8a3650 | -6.66049 | -43.51503 | 2025-09-14 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9425da51-1a71-3ef1-8000-c8444bde19a7 | -11.45846 | -50.78053 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a17aa4b7-e805-31a0-9bdf-930069f04a7c | -13.94911 | -44.83791 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 723f43e6-17da-3370-9f54-537b2482f852 | -9.13777 | -46.96082 | 2025-09-14 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f3cdbca-a134-3864-beca-baf5d2f694ef | -10.06778 | -47.15117 | 2025-09-14 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7d69785-14dd-3cdd-844c-29fa699a6c09 | -12.79795 | -47.13808 | 2025-09-14 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02fe3f67-b0a1-379a-95f0-fa600aee0bb4 | -11.50139 | -50.78742 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f88fee3-80ec-3de6-96af-629144ccadee | -9.02307 | -47.05246 | 2025-09-14 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b505f124-8d6f-3e68-8df7-49c009012efd | -11.1118 | -50.6922 | 2025-09-14 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e46b1cd-deab-3e59-80f1-0606b30366b6 | -11.87642 | -47.54329 | 2025-09-14 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76e5a2d2-98e1-37d9-9b40-16210c4215eb | -12.77253 | -48.01757 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1acd48a2-f784-363f-bdaf-ee471adf76f8 | -11.24539 | -47.62529 | 2025-09-14 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8cede7d3-b393-36ea-9bad-cd6c41bb198b | -11.25183 | -44.77194 | 2025-09-14 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| c32ee404-a5fe-377e-a9ee-66ce8a53d21b | -7.3757 | -44.34193 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e8b91e3-f020-3080-93bb-75ec70c2a267 | -10.90283 | -45.56737 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34e2e63f-2198-3c86-9640-1667e95784e4 | -7.39776 | -49.98553 | 2025-09-14 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33f9f238-74de-3cf3-9b1d-afd35575577c | -12.92847 | -47.94216 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ce0d7417-25ad-3863-ae24-c04a13333bcd | -12.12686 | -44.84084 | 2025-09-14 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fbf4ab97-e870-352a-b41b-02c799c9e2f5 | -6.88931 | -45.63921 | 2025-09-14 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f7f21b25-aca1-35fe-970f-cafd9a12b763 | -8.13639 | -43.66136 | 2025-09-14 04:40:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 501e2b25-5d17-320d-be63-894a29750fd0 | -6.86478 | -44.89627 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ba193a7-88a9-3d07-a8bc-de6f1a81dbc6 | -12.78502 | -48.00694 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37c7ee5d-b2ca-3f7e-b502-3384b6ce7012 | -11.44195 | -50.77788 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39686935-cec5-3560-ac05-8ae8a09f0e14 | -8.17424 | -46.77346 | 2025-09-14 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 81d1658e-84dc-3757-b3bb-43f1fd399cd9 | -6.51043 | -52.22765 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b2d1cdc-aa4b-31a5-8afc-250c95c0af44 | -11.4689 | -50.7571 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f8c7d02-8588-3ad7-9039-b06a51f48f85 | -7.39116 | -49.98449 | 2025-09-14 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e59428f9-2a61-3ce7-8c7f-bfbe012532b3 | -11.48875 | -50.80331 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b1a54050-e12e-3c79-adcf-22743caf6c89 | -15.67484 | -49.90213 | 2025-09-14 04:42:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c2d3e13c-debf-35ff-a132-60bc16b4efc0 | -12.91667 | -54.74494 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5964a323-072a-3960-9693-25eb8b0df01d | -12.69651 | -54.69099 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 14436792-1360-303d-957e-41a9057213ce | -14.45057 | -47.34617 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8c56511c-fef8-3334-b75c-b4a0824678a8 | -14.39595 | -52.91211 | 2025-09-14 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01df6dd0-ed47-38a5-80e2-8b5ca0ea132f | -12.93364 | -54.73424 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b05245aa-481c-35cf-a42d-914672123687 | -15.93356 | -49.97993 | 2025-09-14 04:42:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| df1058d1-ef6f-3b59-ab63-9339ec53ef10 | -15.57504 | -54.73122 | 2025-09-14 04:42:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 539561cd-d6a3-38a8-9162-86464fc1ea55 | -15.68389 | -52.2509 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae8bfce3-a4d9-3722-8072-1a0b3fe1592c | -13.90579 | -48.30266 | 2025-09-14 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 21fd7490-f4d8-36f5-a5b3-fc3b6d522e0f | -15.76543 | -52.23124 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e1033226-8ddb-3f7b-ab6a-cad10a29acb3 | -13.50809 | -50.80991 | 2025-09-14 04:42:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40eed8dc-31da-3930-b7a6-a006e208df3b | -15.78094 | -52.21918 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc7b0e4a-a532-30a6-bf34-570a37ff1cf4 | -17.40721 | -49.26352 | 2025-09-14 04:42:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d3c0802b-ffa5-390c-a405-e6a4cddf431f | -15.65166 | -47.04239 | 2025-09-14 04:42:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 206341e7-9c8c-3ca4-a5b8-3791b8111821 | -13.88561 | -48.29087 | 2025-09-14 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ca0f16f8-1390-3c9b-a418-c8890b60044c | -17.2561 | -49.25938 | 2025-09-14 04:42:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7678a5a-70bb-3453-99da-f98c92ca6b4b | -12.68614 | -54.70736 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0fa448ef-1adf-3636-a2d0-df37d50f4fef | -15.76315 | -52.24558 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7c75fceb-0812-35d0-a2b8-d72a97b9ad91 | -17.56233 | -46.50979 | 2025-09-14 04:42:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47ccf99a-8b16-3145-9259-b2eb87a8e7a6 | -19.99847 | -46.90906 | 2025-09-14 04:42:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46bf3bda-1aa7-3f53-8173-3bd03e8cc5d4 | -12.70086 | -54.71009 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e847bddd-853b-3c7b-94ba-3562951616ee | -15.29369 | -53.78255 | 2025-09-14 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b9b99dfb-6ed1-360d-8651-271440ef7065 | -12.67584 | -54.70096 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fc0859cf-f98e-3639-bfce-e714c416be07 | -14.37549 | -52.93145 | 2025-09-14 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ec55abc-24b2-3641-afc7-e44881e8999a | -14.91318 | -55.95033 | 2025-09-14 04:42:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3779760f-179e-3ad6-bddb-81c11d67efd9 | -12.66706 | -54.68575 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 01fbd7fc-0c81-37fb-874a-0c7f8bac4adb | -12.6583 | -54.67056 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7081dec3-3adc-381e-a8f2-e16fcb16b7cc | -12.70454 | -54.71078 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f5b04217-bbdf-3033-905e-3c1e2a95f875 | -12.68906 | -54.7125 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1adee6c7-bfc7-3ecc-8fa6-62030b00664c | -16.71217 | -54.95348 | 2025-09-14 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 476c097d-1330-3915-806a-526133ad783b | -14.28542 | -46.13126 | 2025-09-14 04:42:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 428ce1bd-a7b7-3342-b327-23cd201ee10c | -15.12088 | -52.47261 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 388cc6c2-60f7-3f9a-8b26-49f638ee520d | -12.94318 | -54.74515 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aee36f6f-662d-3d46-b79d-2ae0b05b6a59 | -17.1405 | -48.51499 | 2025-09-14 04:42:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c93540b2-8c31-37aa-80a8-ff723c203af0 | -17.99683 | -46.9605 | 2025-09-14 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f4d2040c-da01-3f53-b30c-7ac87117207d | -13.87851 | -48.28957 | 2025-09-14 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 527387c0-ffff-3858-b6af-b5b712a4dfe9 | -15.11917 | -52.4833 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9c01ad17-2497-3863-b0dc-b08f6f9991d6 | -14.15836 | -46.24506 | 2025-09-14 04:42:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef9ed80d-31fe-330d-9368-d1dac154adc1 | -15.18695 | -48.71906 | 2025-09-14 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c152c8f5-de8b-31fd-ad40-eade83081301 | -12.69198 | -54.71764 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ac709ad7-23f3-39a7-ac4f-cd910cdecc4c | -16.48642 | -55.12886 | 2025-09-14 04:42:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0340a3f7-fa19-3104-8ae5-da39430e0421 | -15.18719 | -52.31373 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b8d43aab-124f-3e0a-acef-382a29db4169 | -15.29153 | -53.77418 | 2025-09-14 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c730eee1-ad55-3d76-b08e-ae45208d4f97 | -16.54808 | -49.20572 | 2025-09-14 04:42:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f1025338-56fa-3cd4-953f-1df215b4b87d | -15.15527 | -52.47101 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1f2dbfeb-4ab4-3314-a7c0-952527dec329 | -15.01005 | -50.13789 | 2025-09-14 04:42:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e42242b9-28bb-33c0-a2f4-26ba983551c8 | -12.67953 | -54.70161 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1e6789fd-d75c-3b9f-af0c-d9c0b77c0d7f | -17.8364 | -50.42387 | 2025-09-14 04:42:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce07aeb1-748f-37ce-8bda-2700b82c4fbb | -14.17689 | -54.06039 | 2025-09-14 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65763b00-b868-3f67-9f56-671aa90ce8f0 | -12.69642 | -54.71388 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c9ba0697-4d3c-33f1-9c25-6395beface1d | -14.46433 | -47.35808 | 2025-09-14 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 246a6c56-d237-3f69-a247-a772d23e7fc0 | -15.1997 | -52.48991 | 2025-09-14 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f0c7827-7657-33a4-b7fa-e29c028cdd35 | -15.58145 | -54.7366 | 2025-09-14 04:42:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| acddb7c3-d54b-39d2-9246-3f12204b9de5 | -18.14347 | -49.1916 | 2025-09-14 04:42:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ad41f827-a93b-3fa7-a92d-55a6ff40db20 | -12.68178 | -54.68839 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 50c4f898-033e-382d-94ea-b8f20961bcaf | -12.70169 | -54.68282 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 454e1612-98be-3af3-b1ee-893444d30d57 | -15.77827 | -53.48514 | 2025-09-14 04:42:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5413fe4b-3ee6-3054-83fd-18efad602970 | -14.38283 | -52.92891 | 2025-09-14 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4ce7860-444f-3d5e-93d7-3216c88c454d | -16.3622 | -51.76707 | 2025-09-14 04:42:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 21f53372-a0b6-3ebc-9903-5216da7f350c | -13.89864 | -48.3017 | 2025-09-14 04:42:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0e4ce0b2-c38d-3987-8f28-88677a090820 | -17.26477 | -47.24174 | 2025-09-14 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b9f3fbd-a173-3004-bd0a-a1cd077c76cf | -12.67659 | -54.69656 | 2025-09-14 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1e6b15d4-64cf-373b-bd7c-7e0f52b32966 | -17.27881 | -46.10488 | 2025-09-14 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README42.md)
