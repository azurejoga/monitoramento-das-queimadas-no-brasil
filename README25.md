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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5e96f00-a2dd-3bc5-a6dc-771b3a94aa2a | -14.50955 | -44.8365 | 2025-09-16 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5388489-7e53-3952-8359-88816cbd75de | -12.70187 | -47.74358 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0f83e93-cc7b-361f-8936-2026ca14d918 | -15.82374 | -53.46709 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d2fe412-119a-3b36-9419-9fd6d5565f02 | -15.83723 | -53.47199 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 913fc956-ee19-3c89-9465-05a049214b9d | -12.66719 | -48.01594 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05ca1c7a-08e5-32c6-9876-b2c12eadf4c7 | -12.61855 | -47.95833 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f6414c5-15b5-31aa-bf9b-d67d6f03502d | -12.76095 | -47.97342 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| fa15aa5a-5261-3ec6-84f0-d2edd3cc6eb3 | -12.74596 | -47.2008 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1e6a2f3-8b3b-33b0-ae19-30606b11d372 | -14.54425 | -47.36392 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c970a1d5-e3a3-3e2e-9ced-4b28e9805180 | -15.41184 | -47.34698 | 2025-09-16 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 754aa946-441c-3137-a4b6-9423c191e7b1 | -14.84785 | -45.50776 | 2025-09-16 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34fde15f-fb93-367a-aa55-8886e7767662 | -12.77698 | -47.96201 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e808123f-9b5b-3d78-aba2-935f12b67361 | -15.53318 | -44.32475 | 2025-09-16 04:04:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d01f77de-0951-3db2-8001-a4b3ceface65 | -16.68269 | -49.76042 | 2025-09-16 04:04:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f0252ca6-9908-37a2-8acf-cbdea9da91ce | -14.54774 | -47.36786 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d6559ee5-2b04-3b52-9116-1b093693011d | -14.59973 | -46.38197 | 2025-09-16 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cbb553b4-eec4-375c-b7e9-78bf39f4bade | -14.55124 | -47.3718 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 75d1d4b8-d8df-3704-a531-b72061ceca76 | -19.01251 | -49.93056 | 2025-09-16 04:04:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29caea33-6383-37ab-bbf0-23ed71fa9162 | -12.7726 | -47.96124 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 95c2affc-b6bb-352b-86ea-aacace390ed6 | -12.28757 | -46.41176 | 2025-09-16 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 63e3f0ee-c812-315c-bdff-aad3ab57b12d | -14.51182 | -47.38287 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f2f257af-b7ce-369c-b59c-b9232dfb0ec0 | -17.73498 | -46.77072 | 2025-09-16 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2136754-cb16-36b2-aaab-dc1640837c3b | -14.86529 | -51.61694 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82e3b3dc-88b6-369c-af18-814986ace345 | -19.82994 | -45.90375 | 2025-09-16 04:04:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ce29517a-8226-39ce-b7d3-45c14979f060 | -13.8252 | -43.23261 | 2025-09-16 04:04:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 12eb2eb2-c8f4-3111-8086-5c60fb3b9307 | -14.84267 | -51.67427 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b274c6e9-f26b-3032-bfb0-2d2f2830e3b7 | -12.63341 | -48.00159 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 195d8e7a-6afa-3278-b883-007e919a46e7 | -16.42507 | -45.67301 | 2025-09-16 04:04:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79590cd5-59f2-3340-a291-ad79070c8c3b | -16.4863 | -55.10579 | 2025-09-16 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| a8e461a6-4f53-30a0-803e-ab8948895b8a | -15.84449 | -42.68156 | 2025-09-16 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d198c61d-1086-3eb8-909d-38372f997a79 | -17.60615 | -46.68567 | 2025-09-16 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58524a00-880f-3688-8127-1c3031acfd13 | -12.68878 | -47.99721 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6720fae5-13b8-383f-8eb3-e04a9928bbeb | -14.90679 | -51.67367 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 671966a2-26ce-3852-a4a0-9708cbb3fc84 | -12.76533 | -47.97423 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cf62a886-8e52-3156-98e5-9aca62851add | -12.76608 | -47.97 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 03950112-0099-394b-8833-c58a7ee763fe | -14.27182 | -46.14617 | 2025-09-16 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 850e0ec4-0fbc-3a0c-be9f-98415bbef60d | -18.21468 | -44.36242 | 2025-09-16 04:04:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5fe1bf67-8ae2-336b-bfd6-a86892349a17 | -14.88158 | -51.6751 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef859abc-f160-37d0-bd10-4ab38e602031 | -17.67531 | -44.2125 | 2025-09-16 04:04:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88fcb433-12f5-3b89-a984-c77a0f36d35b | -12.80941 | -47.23962 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0ef8e9d7-2395-376b-9aa0-25100e173a96 | -12.62877 | -47.51682 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44501f6d-21e8-333b-98e1-27dd29333d95 | -18.17402 | -45.18885 | 2025-09-16 04:04:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 987f4a9d-31e5-3da2-b68a-132b3953d9e8 | -15.8188 | -53.46148 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a317904a-4efa-3ca7-9e37-e3fdb2d8d919 | -16.68997 | -49.77008 | 2025-09-16 04:04:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bc5199d2-a388-324e-a800-62ea52afd8e1 | -18.01379 | -43.93044 | 2025-09-16 04:04:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b17010c9-d4db-346b-8de3-3d4884f3d08a | -13.21458 | -47.30508 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e5d64186-3aff-3f6c-a233-656a7d4fe29c | -16.43177 | -43.73276 | 2025-09-16 04:04:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2a49cc0-3cca-31b2-8f58-7f3503327350 | -12.29282 | -46.40538 | 2025-09-16 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 78fdec2f-dab2-3070-8d38-1a401f7e8eae | -14.93033 | -51.66762 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48260a5b-58ab-334b-bd3a-bf7538c1a7d6 | -14.81194 | -51.66055 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 74e722a6-9c51-395b-979f-de04f87a6212 | -17.8339 | -40.3503 | 2025-09-16 04:04:00 | NOAA-21 | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7c6057f6-ff9f-3684-accb-6d9c6e9be52d | -14.52517 | -47.33117 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c7cfdd1-1e4d-3f68-8966-ad033efd4c13 | -15.7705 | -43.86389 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8dc47814-9f1c-3762-aeb6-9c6402b9b234 | -17.07577 | -45.8251 | 2025-09-16 04:04:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cb7aafcd-371e-3365-923e-f320a0deb820 | -12.65906 | -47.93408 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 977d20d4-2510-3d95-ae13-3a4fad0501c1 | -13.28659 | -54.23721 | 2025-09-16 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 59db3b46-0ff2-3fce-b6fd-f3dc6684b675 | -15.4125 | -47.34338 | 2025-09-16 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 956af58f-4a6f-3905-b03a-74c6702f1ada | -14.52927 | -47.35368 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ecceadbc-f155-3149-ab66-596d4ac84135 | -12.66776 | -47.93949 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 00656b31-74d4-310b-85f1-afd63736f42f | -19.97716 | -44.95514 | 2025-09-16 04:04:00 | NOAA-21 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a746582c-7365-3ea6-8791-a137b7a5c697 | -14.9182 | -51.67241 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c38c53a-d797-38bd-a0ec-64ea6fc46017 | -14.81051 | -51.66758 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 81c26498-19bf-35cb-8fb1-1e06afeb163e | -14.34493 | -47.09349 | 2025-09-16 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e6c29d1-4aea-383e-894d-e2f9e1718433 | -15.15783 | -52.46418 | 2025-09-16 04:04:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 177ad1f9-f1af-37ff-8b26-d1671cbe9eb4 | -12.86088 | -47.14417 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2540f438-ab3c-3eb3-b20e-9b032e21f595 | -15.40845 | -47.3428 | 2025-09-16 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 838a3326-2d7d-348b-887c-6505a71f75de | -12.80162 | -47.25881 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 37d725d8-5da0-3aa6-9e89-12d37b2dbc03 | -15.62649 | -44.37638 | 2025-09-16 04:04:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f34b48a-4292-3e7c-85f4-3582799efdc1 | -12.84472 | -47.13906 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6e178f10-57f5-33ed-8ba0-c4ba75e7774b | -12.8489 | -47.13954 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f764032-6f43-35fa-9268-42b5ee78114a | -14.533 | -47.37941 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b1595c0b-3c37-3373-87cb-acd9c2d6ecc4 | -18.16117 | -49.20074 | 2025-09-16 04:04:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 3f7730e9-30f6-3e0d-9d65-a635ee7b103c | -14.63357 | -46.39213 | 2025-09-16 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b3bf6bbe-0de5-3a5b-a8d5-765884326b64 | -12.6633 | -47.71043 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9af1b794-6210-30f2-9cdb-df33b381ef8f | -15.59973 | -42.38033 | 2025-09-16 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2f729b57-0cee-38f0-81e1-f4ac6bf435e5 | -15.77356 | -53.45304 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ce2cb57f-52b8-3b6a-9cd6-c49614445ca0 | -14.80729 | -51.65591 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d313c245-9353-31f2-b121-1f6a332a4618 | -12.60036 | -45.70397 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0a9e47b-6f6c-393e-b192-e0406aea3211 | -12.79823 | -47.25378 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e51a1f13-3dc0-3e0e-8d5e-bc08addee445 | -12.77798 | -47.92849 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d0c1c67-f3a0-3629-8f4b-e053bd792115 | -12.65748 | -47.71805 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 0997c68f-def0-39dd-85d2-d048c1c6fc42 | -19.14736 | -44.65636 | 2025-09-16 04:04:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dcdd9e43-cfda-35fa-8875-4e51aea234ef | -16.48513 | -55.11103 | 2025-09-16 04:04:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| b6b21255-f4d6-3a7e-aa8d-0f66f239a67e | -13.19361 | -47.30243 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6cbb5fc4-8044-3066-bd29-77f601057ac1 | -15.84213 | -53.47799 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c2caf77-c84a-311e-98c1-09ad5d3b8924 | -18.8659 | -43.35062 | 2025-09-16 04:04:00 | NOAA-21 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b02f0a90-fa18-3729-b336-347e48c94a31 | -15.41113 | -47.35084 | 2025-09-16 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e629cfb-ea09-395a-a3d0-784a94dfbe5b | -18.56018 | -49.25859 | 2025-09-16 04:04:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 83691109-c6b7-38d2-aba0-f98f730435fa | -12.77706 | -47.95902 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c2aae55b-2308-3cd5-9607-33c0cf96a914 | -12.44172 | -49.70869 | 2025-09-16 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4873eccc-35d5-396e-9ae2-67372af2dafd | -12.80722 | -47.25167 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ebefdd9a-c10e-3999-b83b-6383d63a11d2 | -14.97006 | -46.56519 | 2025-09-16 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b8e72b3f-4d5d-322f-a7d9-4c87d6ca886f | -12.54298 | -45.87732 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.5 |
| f2b765ae-1402-3ef4-8699-9ce5c8ed2e6f | -12.24685 | -46.75551 | 2025-09-16 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f78af361-d521-3228-bd5f-7e8e9a479b51 | -14.52391 | -47.33828 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c36b58e0-d302-39ea-b53f-b837d6bd0e10 | -17.43749 | -45.80763 | 2025-09-16 04:04:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9a54a84-6b64-3ed7-b1d1-901ae7620eb9 | -16.69318 | -46.94782 | 2025-09-16 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 101b1db7-e6b3-3366-bd16-d1ec188274a3 | -12.62047 | -45.74691 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3a1c9d94-f77c-386a-bf0d-4e5360b70271 | -12.7865 | -47.95937 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25ff48c1-db9a-3070-9624-8c2860697e2c | -16.59538 | -42.90504 | 2025-09-16 04:04:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README26.md)
