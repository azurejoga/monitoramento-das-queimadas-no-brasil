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
| fa174309-f8c9-3755-9e01-1409939bcfce | -5.75513 | -49.3207 | 2025-11-01 00:13:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| babde907-9711-3d8a-8f6c-347afa5bbd1b | -5.30266 | -44.52491 | 2025-11-01 00:13:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8a0452be-7c8e-3da8-9330-ce8c24964266 | -6.53681 | -44.52434 | 2025-11-01 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d73bbaf2-afad-3ef0-9803-ca14a3eead1b | -4.68229 | -40.39574 | 2025-11-01 00:13:00 | TERRA_M-M | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 6a2d0ae8-0e0d-3c8a-8f89-b270814f8be6 | -4.7518 | -44.47502 | 2025-11-01 00:13:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c25a265b-1c89-3026-96c8-ed3124fb276e | -5.7964 | -43.97367 | 2025-11-01 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ce446647-850b-3077-a5fa-d16e5d0fb02a | -5.59386 | -45.03276 | 2025-11-01 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 122d2ce1-ddd4-3074-800d-263389922c98 | -5.25781 | -48.48408 | 2025-11-01 00:13:00 | TERRA_M-M | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 835e91bc-6454-372f-9675-8bc6eaa3df21 | -6.4113 | -49.17645 | 2025-11-01 00:13:00 | TERRA_M-M | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 70e1d4c1-c223-3b1b-81f5-681d38529f1d | -6.54933 | -43.23377 | 2025-11-01 00:13:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 44.1 |
| 47e397d9-bbcb-3c40-8692-ddade56bf322 | -5.23469 | -40.71605 | 2025-11-01 00:13:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 070ea076-e595-30a0-91b4-fdfc1720a964 | -6.20227 | -43.71479 | 2025-11-01 00:13:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 9a91d1f2-d436-3552-9716-0b1a315d71b9 | -5.26338 | -44.3101 | 2025-11-01 00:13:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 4164c842-23c7-3a7f-8228-93cc3312213e | -4.82549 | -45.79811 | 2025-11-01 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5887a97d-f071-32d0-b0c2-f353e8f501c0 | -4.74674 | -44.43893 | 2025-11-01 00:13:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 75f51c25-ac78-3383-8cfb-bfb118fd9965 | -4.92298 | -45.44595 | 2025-11-01 00:13:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 631185ac-c8a8-3f30-84d9-d95dd6ff9c6c | -9.92169 | -36.27935 | 2025-11-01 00:13:00 | TERRA_M-M | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| 6af88021-1c28-3668-bfeb-4e4d61330e52 | -6.62428 | -47.17582 | 2025-11-01 00:13:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a079bfca-53b5-3449-8c44-6a51c9b742d6 | -6.22547 | -42.52468 | 2025-11-01 00:13:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 1dcf00bb-5d0f-3e33-9501-efe697ce2730 | -9.84841 | -44.14899 | 2025-11-01 00:13:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fac557c9-89b1-3f12-bdd6-cface78b19e8 | -8.18259 | -44.75792 | 2025-11-01 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ab44a46f-b055-3d8a-a157-6a3f5128fdb0 | -6.93192 | -42.54683 | 2025-11-01 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 16d13938-db1c-3031-b702-62a3a752d2f0 | -10.06268 | -44.10563 | 2025-11-01 00:13:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4042482b-0db9-3d02-be8d-323f6fd324ee | -11.37558 | -48.93365 | 2025-11-01 00:13:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| fd860e75-3bbc-3818-a49f-3db5aac7c5d2 | -5.21724 | -45.83622 | 2025-11-01 00:13:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| ce0cafdf-8db1-3c37-a0a0-35001913f571 | -6.0487 | -47.9753 | 2025-11-01 00:13:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 05591136-834e-323b-9f2b-e6f75bf0c299 | -8.15504 | -45.43733 | 2025-11-01 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d4dbc265-7ccf-3bc9-90c7-560c110a62c3 | -5.35567 | -45.03373 | 2025-11-01 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 888d5f28-902f-3175-93eb-ec2b0f995103 | -6.3588 | -42.40178 | 2025-11-01 00:13:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 3863258b-4165-3d71-a30d-77be35295cd5 | -6.67873 | -44.68811 | 2025-11-01 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a2a8fe3e-228d-3738-9b6b-863c1c68ef3e | -9.92614 | -36.3056 | 2025-11-01 00:13:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 89.7 |
| 36963801-670b-3330-8c88-b74882901d79 | -11.64038 | -48.57498 | 2025-11-01 00:13:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 5d6ce20e-d626-32bf-94fd-9efd97870091 | -10.4711 | -45.81789 | 2025-11-01 00:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1f606db9-149f-32ee-9914-69853e5e5863 | -7.29575 | -45.07161 | 2025-11-01 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 348f0b27-dd11-3863-b0e2-4cbc5f659de9 | -8.75252 | -44.0895 | 2025-11-01 00:13:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cca00423-eedd-3e6f-a11e-c2dde5ba69f5 | -5.95436 | -45.57537 | 2025-11-01 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| cec3c347-ca03-3b8c-9d6f-95da20259b97 | -9.12309 | -48.44898 | 2025-11-01 00:13:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 7a62191f-c8ec-3ab7-be23-5f2503c9599b | -6.48303 | -44.13906 | 2025-11-01 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 22f77cce-9d8b-3c27-af3b-50981967f60d | -5.4039 | -46.05247 | 2025-11-01 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6aab1e56-c96e-3b51-9a50-1f9da30ec0a4 | -4.61502 | -44.42366 | 2025-11-01 00:13:00 | TERRA_M-M | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 00c1b53d-7874-3835-9bba-5ddf7498bd5c | -8.75127 | -44.08055 | 2025-11-01 00:13:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f258ff34-7976-3716-bb40-353591259c67 | -8.22943 | -46.25332 | 2025-11-01 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| c4aec596-fb82-34fd-b8bb-1b425a26de54 | -5.15056 | -45.82473 | 2025-11-01 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 18.6 |
| ec6d3022-58c4-30a5-82d9-3f570744ed19 | -7.47522 | -46.12062 | 2025-11-01 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 59d54eea-1e3d-35d1-9901-1015a5666546 | -7.43162 | -41.25164 | 2025-11-01 00:13:00 | TERRA_M-M | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| ec924e16-5d97-376f-84f0-3bb0f50fe041 | -11.64394 | -48.60406 | 2025-11-01 00:13:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 49c87f75-6da2-31ae-93da-84bc1cccc7cb | -5.75682 | -49.33379 | 2025-11-01 00:13:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7807415f-ed11-3797-b258-b51f470dfb2e | -6.40763 | -43.99223 | 2025-11-01 00:13:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e5d07ac9-9251-34d1-b874-ef187dfc7cfc | -5.95558 | -45.58424 | 2025-11-01 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 752e8a41-773a-3a35-a9b5-9e46968eaec3 | -6.55069 | -43.2434 | 2025-11-01 00:13:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 38.2 |
| 91620269-efad-37ee-9f8a-d891083b65c7 | -5.54154 | -48.38628 | 2025-11-01 00:13:00 | TERRA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 60ae183c-4e4f-3e47-9e0c-faf8a2d8ab61 | -6.61491 | -47.17713 | 2025-11-01 00:13:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 20150fda-a31c-3a1a-84ad-e0353786ce00 | -6.60287 | -43.67965 | 2025-11-01 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| efbc41df-5409-3697-b42a-2415f64a3862 | -5.67063 | -46.7272 | 2025-11-01 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 23c5e14c-75e3-37ec-8d1b-ba07248601f5 | -5.09461 | -47.71537 | 2025-11-01 00:13:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b35eff5d-e98f-320c-bb9b-0478c2d08fb7 | -6.8547 | -42.27959 | 2025-11-01 00:13:00 | TERRA_M-M | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| ed90c38d-79aa-3e79-9170-c77cec34848b | -8.70877 | -41.58378 | 2025-11-01 00:13:00 | TERRA_M-M | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 41.7 |
| b35f7bf0-f26b-3b6a-b50a-e57c56d0e462 | -6.4573 | -43.56412 | 2025-11-01 00:13:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 453355b4-0947-350c-8345-ceaba6fc2eaf | -5.79432 | -40.8413 | 2025-11-01 00:13:00 | TERRA_M-M | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 5318a4f9-2744-3eee-938e-7c4a099a9b8f | -5.21168 | -45.12931 | 2025-11-01 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ebe1e557-15fc-390e-8b78-41d61e5b08dd | -6.62856 | -44.58675 | 2025-11-01 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| dc0ecdd6-b188-3318-9328-e8cbd1508933 | -5.21931 | -44.79451 | 2025-11-01 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f0b9dc69-e9f6-3970-a310-4550daf57fbc | -5.36888 | -45.20867 | 2025-11-01 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a95fd207-0173-3c6c-8525-ba92b24fc7f3 | -8.88798 | -44.39993 | 2025-11-01 00:13:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b316823d-3a81-3f64-b25f-71e8f5b97c86 | -11.5731 | -47.06232 | 2025-11-01 00:13:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 1a50ca59-71e8-3db0-a777-12f7aec1ea88 | -10.06608 | -44.99614 | 2025-11-01 00:13:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a06c986e-6b63-3a00-bd25-3eaff89aa16f | -5.56985 | -47.33293 | 2025-11-01 00:13:00 | TERRA_M-M | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4c61226f-9395-378f-bd48-c6bb7208af97 | -5.26465 | -44.31916 | 2025-11-01 00:13:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 26e2c87b-f398-3918-b65d-f256314fdadd | -4.63718 | -44.71408 | 2025-11-01 00:13:00 | TERRA_M-M | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8255060d-3fa5-38f4-ad1a-06a95a04aa99 | -5.03537 | -43.60608 | 2025-11-01 00:13:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 6d13e868-23fc-3d2a-b761-72cf83b0e854 | -7.70552 | -45.98559 | 2025-11-01 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 74febb7d-cd97-3651-8c6f-6dbf4d8d9ccf | -5.30653 | -45.34322 | 2025-11-01 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9a5e3d93-e95a-3c23-b8a1-dbe2620877db | -5.06615 | -43.95776 | 2025-11-01 00:13:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4fdd7580-04e5-391f-9f67-964bac623b70 | -5.88269 | -44.52436 | 2025-11-01 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 004cbda7-3805-337e-a538-13292b83d1bc | -10.65924 | -45.16319 | 2025-11-01 00:13:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 24.2 |
| f8d4263b-16a3-3f0d-8c2a-6e8270411d64 | -6.04074 | -40.25563 | 2025-11-01 00:13:00 | TERRA_M-M | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 10.6 |
| d843ca4c-72e3-3d0c-b792-f10ea45fa798 | -6.27347 | -44.15376 | 2025-11-01 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f00e8482-8397-3b1a-af35-70867e350050 | -6.57946 | -48.7392 | 2025-11-01 00:13:00 | TERRA_M-M | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| bdf8727b-ea08-3f26-ac85-87a5079cce75 | -6.54567 | -44.52309 | 2025-11-01 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ba31c10d-5954-33a0-b41b-7a4c5f263732 | -5.25626 | -48.4727 | 2025-11-01 00:13:00 | TERRA_M-M | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 5066aac8-50d0-389d-b71c-9724ae466178 | -6.21296 | -44.37958 | 2025-11-01 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d4c0b810-eccc-38d7-bd1f-40af7157e54b | -8.60216 | -45.47319 | 2025-11-01 00:13:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4083d101-e428-3307-bf53-ee86b712a23a | -6.90154 | -35.01852 | 2025-11-01 00:13:00 | TERRA_M-M | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 101.0 |
| 27f50510-408b-3cc2-99b1-3e7e19ea8259 | -5.14207 | -44.82362 | 2025-11-01 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b7b3eecb-77f0-3bc7-a1bf-0223ae1ca246 | -7.5187 | -45.35394 | 2025-11-01 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 32f1a66b-75ab-34b4-8751-da7548182a58 | -7.92544 | -41.61296 | 2025-11-01 00:13:00 | TERRA_M-M | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| b3468cfc-6fd5-34bb-8efb-93ed786055c8 | -5.94225 | -48.3309 | 2025-11-01 00:13:00 | TERRA_M-M | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 87752fbc-3bad-3548-bc42-7262eb04e88f | -6.89528 | -34.98063 | 2025-11-01 00:13:00 | TERRA_M-M | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 39.8 |
| a04b4a1d-82c3-33d5-b1cd-ec9072c7ce9e | -5.83749 | -44.07051 | 2025-11-01 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| fd5180a7-afbe-3c02-b3e8-b3d06ad447bb | -5.99659 | -45.75054 | 2025-11-01 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dca524a1-d231-38b7-aeab-81bbb23f56d7 | -5.2129 | -45.13813 | 2025-11-01 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0fc33a33-01d1-39c1-85cc-fe00b43048a9 | -4.65554 | -43.45786 | 2025-11-01 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 661f6324-33fd-3bf4-804f-7b49f56f1a47 | -5.59509 | -45.04159 | 2025-11-01 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 888f8a4e-3fec-3e29-af67-eaa6bbeb8585 | -5.88093 | -44.70601 | 2025-11-01 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 37440d67-db83-3d8b-9bb1-5183fc895199 | -6.88794 | -42.84329 | 2025-11-01 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 55.9 |
| 2b610bfd-c85c-3ab8-a8fb-087b985a5c6a | -10.72189 | -46.25033 | 2025-11-01 00:13:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7a6ebf4b-6727-3529-8cd5-7ea4fde144cb | -4.81058 | -45.75518 | 2025-11-01 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8daa17ce-8ce2-362f-9bd4-753a69cad317 | -5.48759 | -43.09476 | 2025-11-01 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| dae257ff-1ed7-3ba4-b5fa-931baa262966 | -6.88939 | -42.85326 | 2025-11-01 00:13:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| befe90bd-20eb-3642-9094-890b7e4df919 | -5.06942 | -45.10773 | 2025-11-01 00:13:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |


[Clique aqui para ver as próximas entradas](README4.md)
