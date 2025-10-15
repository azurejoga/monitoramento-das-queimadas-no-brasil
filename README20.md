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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3f60ec8-484e-3c31-8bad-145ec75fb8b8 | -13.38734 | -43.65945 | 2025-10-15 03:49:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| c30a34ab-b5b1-3a29-9399-253f94dbaf7e | -18.19815 | -50.74833 | 2025-10-15 03:49:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 12bc3b8a-74fd-31fd-8ec1-451fec12c92e | -12.2165 | -50.42456 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6cb284c0-039b-31f6-abca-c2f9f91759cf | -12.21244 | -50.40948 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 915f4eea-ecc9-3291-a9d5-f17c70d39cb7 | -12.23885 | -50.42253 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 99cf6acd-d55d-357e-baef-00c1c8515931 | -12.2303 | -50.40798 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 8162ce1f-0fb1-34a5-a1f3-3303dc65f9ad | -12.19834 | -50.38651 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fd09cda2-5544-3275-a284-b1fca1fd334d | -12.23623 | -50.4007 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| c93f38fd-1825-3b39-93fd-f16b494ecbac | -12.2317 | -50.40122 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| f4f6b222-a79f-3777-81b1-915eb737a95f | -12.94056 | -42.433 | 2025-10-15 03:49:00 | NPP-375D | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| de8f34dd-4089-3c40-9288-561b3b996721 | -14.83435 | -40.98324 | 2025-10-15 03:49:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| f8ff5ac3-9603-373b-9ade-d9e7d0d2b27b | -12.21225 | -50.38968 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| df05d9d1-68f3-3a75-8d39-8d874486b9fd | -14.28015 | -42.3341 | 2025-10-15 03:49:00 | NPP-375D | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cc398748-23e0-3147-bac2-a99f213fecb3 | -13.93418 | -42.3561 | 2025-10-15 03:49:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| c84bb885-362d-3b8e-a0e4-d7b031dcfd7a | -12.22475 | -50.39963 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f3a1e472-a776-3c04-9f91-bc81aa647283 | -14.123 | -42.65162 | 2025-10-15 03:49:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0fa0ebb0-6f57-3efb-a25a-ba5057c1bd94 | -12.22616 | -50.39286 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f7040f88-e903-3002-9fdd-15d206bcfb0f | -12.21941 | -50.41106 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 347a29aa-4492-376b-9e0a-f3092d09516b | -12.20529 | -50.3881 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 154156d2-c2e0-3db9-9aab-72469ab32fda | -12.2792 | -43.82703 | 2025-10-15 03:49:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2250fa2b-623e-39bd-aefa-c6490033e18d | -12.04419 | -44.24943 | 2025-10-15 03:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 78dd7d16-7ff1-360e-9e6c-9aab6e6044bd | -12.22231 | -50.39757 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 6f7b0879-3691-3bdd-99e2-54a458616a40 | -18.26226 | -48.24818 | 2025-10-15 03:49:00 | NPP-375D | CUMARI | GOIÁS | Brasil | 5206602 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| accb8f6b-480b-3215-b6dd-adeea6387dc5 | -12.20985 | -50.3877 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a4fd426e-782d-30e6-a7b1-e224f3562349 | -11.51987 | -49.14658 | 2025-10-15 03:49:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| abaac41e-6bf1-3a5b-87e0-a3cd10a65bf6 | -12.23445 | -50.42311 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 3795782a-11bc-3b29-bffe-a8760672ac69 | -12.22193 | -50.41314 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b2f8e00e-c4f1-344f-be28-553b63f27fb7 | -12.21084 | -50.39643 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0f641ebb-5e40-3043-b099-7dfe80b2593c | -18.67698 | -44.03978 | 2025-10-15 03:49:00 | NPP-375D | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74b91ae1-dd1f-3d1d-93d4-1c00170acfd3 | -12.19593 | -50.38459 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a41e0e10-f1cd-3b4a-9636-b32b1f0e6d04 | -5.4463 | -44.2388 | 2025-10-15 03:50:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 8f1526dc-5736-3abd-98ce-7318b310fb24 | -4.9104 | -43.4434 | 2025-10-15 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 7fdb846b-a5b0-331c-9ef5-ac24e98f8be6 | -4.9102 | -43.4666 | 2025-10-15 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 230.6 |
| b5ea825f-6a02-3189-ab0d-b5eca1023351 | -5.4465 | -44.2159 | 2025-10-15 03:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| d72f75f0-458e-3732-bad9-4498856ec648 | -4.8916 | -43.4446 | 2025-10-15 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| fede2c08-3ddb-3a62-b0aa-089b89660908 | -4.6509 | -43.1337 | 2025-10-15 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 7ce69124-8ab7-375c-a3ea-2c49ec83e3d4 | -5.4278 | -44.2172 | 2025-10-15 03:50:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 97fb00d4-af4e-3658-9e79-2436c890250e | -5.4276 | -44.2402 | 2025-10-15 03:50:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 2075b426-b024-329f-be09-c6d9b002f2d8 | -4.8915 | -43.4678 | 2025-10-15 03:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 165.8 |
| 62b93c7b-b71d-352d-b6fb-4ca41c144f71 | -28.24898 | -48.78446 | 2025-10-15 03:51:00 | NPP-375D | IMARUÍ | SANTA CATARINA | Brasil | 4207205 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 48c90368-8c6c-34a0-b4e7-a8c2db211c0b | -5.4278 | -44.2172 | 2025-10-15 04:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 114.8 |
| ab06eed9-ba44-3511-bba2-f47a1419b1bc | -4.9104 | -43.4434 | 2025-10-15 04:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 134.8 |
| f2c75f6f-cc7b-32f2-814c-99dc2d504a92 | -5.8802 | -43.8613 | 2025-10-15 04:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 7e3d476a-2f30-34df-bf06-ea5c09e4b324 | -4.8915 | -43.4678 | 2025-10-15 04:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 229.3 |
| 903eb335-12d9-3488-aa6f-76f7152166b4 | -5.4465 | -44.2159 | 2025-10-15 04:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 58c4cc35-c0b7-3afb-ab84-f34cc244ca15 | -4.6509 | -43.1337 | 2025-10-15 04:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| a3b2a18e-69a7-3451-ae6a-99ffad135b19 | -5.4276 | -44.2402 | 2025-10-15 04:00:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 493bc7a3-75e0-352a-852e-154d18f00d3b | -7.9439 | -44.1381 | 2025-10-15 04:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 42.2 |
| f35cb620-5c43-35fd-892f-114407a91ab2 | -4.9102 | -43.4666 | 2025-10-15 04:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 280.8 |
| ff9b252f-894a-3bba-9064-6bc8c2117cbf | -6.4543 | -44.5749 | 2025-10-15 04:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 699b6d08-74e4-3ac3-99b1-64e729783af2 | -5.4463 | -44.2388 | 2025-10-15 04:00:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| b5259715-118f-3b72-b5b9-e7b5b345a124 | -4.8916 | -43.4446 | 2025-10-15 04:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 126.6 |
| f03ff005-2aec-3fd7-a8c7-875d4b3ae360 | -0.89592 | -47.54729 | 2025-10-15 04:04:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| ceee69e5-538f-34b3-a413-fb1c10b6dd1d | -3.95581 | -40.76516 | 2025-10-15 04:04:00 | NOAA-20 | GRAÇA | CEARÁ | Brasil | 2304657 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 16d3669c-cebc-32ef-a6f6-33164a2753f0 | -3.60956 | -41.57904 | 2025-10-15 04:04:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ce9460a1-00b7-373e-94ba-00fca18fdfaa | -3.56123 | -41.62521 | 2025-10-15 04:04:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fa31c682-6924-384e-a247-cbc3dfaf4d11 | -3.53337 | -44.0239 | 2025-10-15 04:04:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 91dbca24-991c-37fe-b8b7-72b295c0296c | -2.71476 | -48.33603 | 2025-10-15 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d800f4b8-cc99-331a-a1aa-545fc7b64885 | -0.8951 | -47.55236 | 2025-10-15 04:04:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe30ec09-3ddd-3951-bce8-6b4651b83032 | 1.07547 | -51.04989 | 2025-10-15 04:04:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5973c368-e499-3f46-b69b-0e2e1a707427 | -3.12922 | -45.6151 | 2025-10-15 04:04:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 107ffcb6-6f82-3d8f-863a-67198bb3aa8d | 1.01354 | -51.09131 | 2025-10-15 04:04:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f4bf34c-bdea-3f8e-9294-8f7488118f1d | -2.53014 | -47.81525 | 2025-10-15 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82a846f2-be68-39cf-be03-090c2a81fd57 | -3.05032 | -44.46794 | 2025-10-15 04:04:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1262a223-1b1d-3ca6-92ad-a9f5737d87cc | 1.34277 | -50.74466 | 2025-10-15 04:04:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 882c8d43-19ec-3496-9b62-8437b4cc3384 | 1.33583 | -50.73775 | 2025-10-15 04:04:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b65b1d8e-1e1e-3c57-8ccb-19ec577aca07 | 1.33375 | -50.72704 | 2025-10-15 04:04:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22890adf-20a7-38d9-9564-51fc872a94ec | 1.08197 | -51.04048 | 2025-10-15 04:04:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c60ecff-a49b-3be1-af19-0167d5250794 | -2.02266 | -46.43294 | 2025-10-15 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 732b6886-bdc3-307f-a0fb-6baa90848943 | 1.34204 | -50.73997 | 2025-10-15 04:04:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 236fb9c8-e8b9-353c-9874-5e0c74344012 | -3.05335 | -44.47309 | 2025-10-15 04:04:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08fe5663-303e-3f8c-8d37-78b8cd6e21d2 | -0.89987 | -47.55316 | 2025-10-15 04:04:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 519d4a19-36b9-383e-9ee8-f4856e8350dd | 1.30284 | -51.25195 | 2025-10-15 04:04:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad20279e-7999-3109-b768-4e755b7dc1e4 | -2.44148 | -49.00294 | 2025-10-15 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c79be4f-8cc8-3ebe-9885-3dec016a4357 | -3.17678 | -41.17914 | 2025-10-15 04:04:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d38d0cac-bf33-3fb3-9200-1aef5b9e598f | 1.0773 | -51.05119 | 2025-10-15 04:04:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 184da425-c449-3ecd-a8cb-91b0850355ee | -2.24525 | -47.87922 | 2025-10-15 04:04:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 87961329-cef9-354c-a9d1-5b4ee8e7bdb0 | -4.02838 | -38.35184 | 2025-10-15 04:04:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 75dd7899-1666-36ee-9334-447b8ce24c14 | -3.56568 | -41.61874 | 2025-10-15 04:04:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ab7ca301-f25c-3329-82b5-005fcc88a96e | -3.09881 | -45.33928 | 2025-10-15 04:04:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4564ede1-fc8e-3386-91e9-bcc599dbee9f | -3.56623 | -43.50911 | 2025-10-15 04:04:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 110b9340-624d-33d9-9e7e-efb0e371a229 | -0.90069 | -47.54804 | 2025-10-15 04:04:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 4ea046d8-0da8-311d-a1fb-657b1e3ea40e | -3.59567 | -41.62347 | 2025-10-15 04:04:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a49c9113-20df-32f4-8d97-3cd349a9c7bb | -2.29547 | -47.99445 | 2025-10-15 04:04:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7316c8dd-e071-3736-bebf-04ebede49f2e | 1.07577 | -51.04152 | 2025-10-15 04:04:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 343808a2-d036-33f6-bad5-3813a00ab51c | -3.6556 | -43.4239 | 2025-10-15 04:04:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49a7275a-2a04-3a26-98f2-d4da40e157da | -3.11072 | -45.04188 | 2025-10-15 04:04:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b587f92a-1487-3126-90ca-95e59f5afe80 | -3.05639 | -44.47826 | 2025-10-15 04:04:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b4faeb7f-163f-3990-974b-9b5d891cb7ab | 1.30204 | -51.2468 | 2025-10-15 04:04:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3ee5677-6067-3339-b061-413cbff0d438 | -3.94736 | -40.92572 | 2025-10-15 04:04:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c6dfcbf6-d23c-3bb9-9225-2fef63bea782 | 1.34263 | -50.74138 | 2025-10-15 04:04:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 327cecf3-a692-3b38-b9ec-b62368b47f0a | -4.08316 | -39.82467 | 2025-10-15 04:04:00 | NOAA-20 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ba4a11f7-3108-3334-ac90-cb24660ddcd0 | -3.28288 | -40.8956 | 2025-10-15 04:04:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 04d849a3-5379-3952-b683-b46132e400da | -2.44662 | -49.00378 | 2025-10-15 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eda2c206-e93f-3895-afc7-e9f141f75430 | -3.28619 | -40.89612 | 2025-10-15 04:04:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bc318d9c-42e1-394d-8158-0c9f1c1a4ad1 | -3.26811 | -41.2684 | 2025-10-15 04:04:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c99c91f0-a673-3dd3-8b58-237c42c2bbff | 1.33375 | -50.72379 | 2025-10-15 04:04:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5851d545-a8af-34c0-837b-7938da832f33 | -3.05408 | -44.46855 | 2025-10-15 04:04:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 32531a7c-2d0b-350b-9b1b-54b93ba3ec2c | -3.76785 | -41.69333 | 2025-10-15 04:04:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 33d45dd0-af99-3011-8143-38b82c2dadac | -3.75909 | -39.96374 | 2025-10-15 04:04:00 | NOAA-20 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README21.md)
