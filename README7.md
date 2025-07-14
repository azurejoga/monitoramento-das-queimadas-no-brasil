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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed19d055-1fac-35a7-acce-f0c725f0d7de | -28.58703 | -49.44331 | 2025-07-14 04:08:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d17521e6-224a-37c7-a9e6-00b5fa700e25 | -28.5996 | -51.25563 | 2025-07-14 04:08:00 | NOAA-21 | IPÊ | RIO GRANDE DO SUL | Brasil | 4310439 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0cc9c526-0aad-3e88-ac32-12a3b43e537b | -27.21403 | -50.66576 | 2025-07-14 04:08:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 337daa33-696d-3646-acdf-50c99bc7748b | -8.5211 | -43.3063 | 2025-07-14 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| d07dbac6-ca43-3f93-a3a9-0e65b3eb944d | -8.5211 | -43.3063 | 2025-07-14 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 435be0b1-8a66-3759-827b-eb99148f85cd | -2.29323 | -48.57514 | 2025-07-14 04:25:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17f49c23-9c24-358f-a9bb-414ffa5c86d9 | -3.58599 | -47.51896 | 2025-07-14 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c4975a7e-b8ad-32da-a2ef-567be064d5ca | -7.02022 | -44.38475 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d6e0790-831d-3608-8687-bc37a1487674 | -8.04807 | -50.09203 | 2025-07-14 04:27:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31e35086-ad8f-32e5-a4b3-9803187ef6b3 | -8.91511 | -47.34344 | 2025-07-14 04:27:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49eb347a-2b35-3986-9c68-bf0d3f582e28 | -3.57972 | -47.51417 | 2025-07-14 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8e8b9c23-1123-3d30-8243-3738424d7c4a | -6.83478 | -42.86571 | 2025-07-14 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| eb2a807c-f934-3f3e-b6ce-00bec2520260 | -6.4634 | -45.36106 | 2025-07-14 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76247e78-e766-30d6-a638-3b6da0ae18b1 | -9.49863 | -47.56695 | 2025-07-14 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b153afd6-f666-3993-995b-1da3441e6ebb | -7.0243 | -44.35825 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d1a8c5b5-eced-31a9-8190-db3cecba4463 | -6.82676 | -42.86889 | 2025-07-14 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f6b305a2-abcd-39c5-a23f-5fac1007fc77 | -5.44889 | -43.58772 | 2025-07-14 04:27:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3a91937-9342-3f57-9306-97cf25f0c8f4 | -7.02832 | -44.35506 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b4780dab-3592-34f4-90aa-2bc37c50b47d | -7.03176 | -44.35566 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 053e99ce-8f2b-3df0-ba41-aa431721a797 | -6.2604 | -43.36718 | 2025-07-14 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 800c7255-653d-361f-b31a-a712ee77d448 | -7.05324 | -43.95926 | 2025-07-14 04:27:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe9c5527-3a45-3cb4-9bb1-969474eb05a2 | -3.58256 | -47.51841 | 2025-07-14 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3e8bed54-7b50-3263-8b23-31c9cbdae0aa | -5.15506 | -37.68343 | 2025-07-14 04:27:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 628bb910-db22-373e-be26-9b2194461cd6 | -8.91011 | -47.35342 | 2025-07-14 04:27:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da1cdebe-4423-382a-b85c-ba4519719c2c | -7.29643 | -44.62824 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 10d9e12b-4fc9-381d-834e-91eb7b6086fd | -7.26778 | -45.31482 | 2025-07-14 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 04e97c0c-0062-37b8-ba37-48772e6d4eb7 | -7.58136 | -44.72733 | 2025-07-14 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6a714b1a-f57d-38fb-a815-75446c32ed7b | -7.02256 | -44.36958 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4293cf7-b2ce-33a2-b21a-35c961604170 | -6.76209 | -47.36657 | 2025-07-14 04:27:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1e1b998-135b-3206-b1e2-46d16c787bfa | -6.14064 | -44.0885 | 2025-07-14 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e91592c7-5e56-3c05-a5c2-7ff2ca857d2e | -7.01679 | -44.38416 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d550c59-c921-3e78-8418-d3086d33df7f | -8.04811 | -50.11459 | 2025-07-14 04:27:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c2646319-366c-3f90-b335-ef38995f7e07 | -8.5102 | -43.3079 | 2025-07-14 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| e03c1326-74db-3b96-bb05-ba80f0795be8 | -4.51493 | -38.5513 | 2025-07-14 04:27:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| c886dc45-d070-33a3-9630-80348e2dce19 | -8.5203 | -43.30736 | 2025-07-14 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 34.9 |
| fce530b2-ea31-30a9-b1db-61bb4a4a8830 | -7.62919 | -56.76573 | 2025-07-14 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3086ca46-a1c9-395c-b57c-6730db77f62f | -7.27059 | -45.31892 | 2025-07-14 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca10aac1-4a1b-3296-a363-d0b56f4a6e63 | -8.91178 | -47.34291 | 2025-07-14 04:27:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 840dd83e-7295-3b49-9c31-75642f8aa7ac | -6.46619 | -45.3651 | 2025-07-14 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17b407ca-e199-3e91-ab2c-aa976f596ffe | -7.5882 | -44.7284 | 2025-07-14 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8881e19d-23ce-3f4c-9c5e-c499b6a2126c | -6.12008 | -44.22359 | 2025-07-14 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a99c64d-4ce0-3d73-a897-b3daefc41d73 | -4.30391 | -48.10468 | 2025-07-14 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| eee8ac6d-77c0-39c1-ab56-1f7534e6c7c9 | -3.58196 | -47.52212 | 2025-07-14 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 58826b51-fdd1-346a-b846-a533ed46dbcd | -7.26162 | -45.3102 | 2025-07-14 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b15e0e1b-7a55-34b4-996c-344d9eb37af4 | -8.87634 | -46.904 | 2025-07-14 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 299b00cb-df47-3fb6-8831-41477a7df1dc | -5.44539 | -43.58718 | 2025-07-14 04:27:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65298ce8-8c96-3c5e-9e84-aa3052999882 | -8.91122 | -47.34641 | 2025-07-14 04:27:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8af290c9-5977-3e47-ac68-b325829ee800 | -4.5846 | -47.26339 | 2025-07-14 04:27:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d220d83-60da-3f4d-bdf8-baf9dd243bdc | -7.26834 | -45.31126 | 2025-07-14 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d93bf5bf-8d21-38ec-a58d-20877532d34a | -7.27114 | -45.31535 | 2025-07-14 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0dba321b-ab6c-3cc8-b605-e2a320337c10 | -7.58079 | -44.73103 | 2025-07-14 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 64264805-b8ac-349f-ad02-1b4bf8a7554d | -7.04262 | -44.37673 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77b40a0b-7031-3334-98b8-7c197195412d | -7.297 | -44.62449 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73ff503c-3a5d-3f46-8f12-fa98f275a350 | -4.86697 | -43.22195 | 2025-07-14 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d8d43eaf-8f2d-3c81-b871-53d5dfab000e | -7.0214 | -44.37714 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 996a8287-4238-330b-8a64-c15969258b57 | -10.55606 | -45.11323 | 2025-07-14 04:27:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f33d576-e6dd-33bd-9870-244c0b2d6f74 | -5.28571 | -44.8815 | 2025-07-14 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7500cae9-aed4-3634-a17b-6ffbc14504b6 | -4.01401 | -49.47004 | 2025-07-14 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99c063fa-5dd7-348a-92ed-22e880992e86 | -9.4894 | -40.38528 | 2025-07-14 04:27:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9a2fef27-fc30-3356-82fc-e7bbd597ebd2 | -7.16852 | -42.97273 | 2025-07-14 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 11654ef5-fdf9-3d36-b096-c4e165d72bfb | -8.91455 | -47.34694 | 2025-07-14 04:27:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ab3f6d2c-4cb3-3347-a3d1-501bdbf669a8 | -6.7056 | -43.89754 | 2025-07-14 04:27:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 33d12b45-572a-3af0-81bb-1ca350809a35 | -3.78721 | -47.0909 | 2025-07-14 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9a28118-6d64-3924-b0df-3a1d61571e3b | -7.0508 | -44.32384 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9382aae-0278-3a06-92cb-4b8784ccb2ed | -3.58137 | -47.52583 | 2025-07-14 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fc36d99a-ea83-3196-a717-bb0fc302ea76 | -5.27119 | -45.12857 | 2025-07-14 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88304c42-ec70-35e3-97d2-ca93027a2850 | -4.58798 | -47.26392 | 2025-07-14 04:27:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cef8d6f0-20ad-32fb-ac8a-60b9c9731ecd | -9.49919 | -47.56343 | 2025-07-14 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6182517a-0903-3288-b42f-fc7da171c160 | -8.91399 | -47.35045 | 2025-07-14 04:27:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e954301b-55d1-33e5-be02-d7a7ca41c858 | -3.78778 | -47.08731 | 2025-07-14 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a2e783f-3870-37b9-9709-b21f25a05dfa | -5.25208 | -44.46931 | 2025-07-14 04:27:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| acee170f-271a-3efe-a80f-7ddb119465c7 | -8.0407 | -50.11365 | 2025-07-14 04:27:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7be3cb0-e526-350e-aa7d-14aafee5096d | -8.87357 | -46.89999 | 2025-07-14 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7e82296c-4a16-3e87-8583-6283a38b302f | -8.50653 | -43.30735 | 2025-07-14 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| fb5b0a8d-41b2-3c71-9c18-dc59055d27d9 | -3.58078 | -47.52954 | 2025-07-14 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b4d4cafb-7156-3e72-abf4-1be1dd7b6d39 | -8.04668 | -50.10041 | 2025-07-14 04:27:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b0487070-bf3d-3360-8d8b-8beeb2e1f71b | -5.28235 | -44.88099 | 2025-07-14 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 555848ec-2092-3016-85f3-71e746f18240 | -4.77915 | -45.33142 | 2025-07-14 04:27:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6d6d58ec-0fc6-3a30-8203-3e4cb97c59f8 | -4.51566 | -38.54629 | 2025-07-14 04:27:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| f554f5ae-691b-393a-b5e7-3af93c11940d | -4.24857 | -46.63295 | 2025-07-14 04:27:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf49b079-69c5-3c4d-8885-708213f0d595 | -3.58421 | -47.5301 | 2025-07-14 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 62453b3f-7709-3298-ac37-ca64ae1ff626 | -7.87722 | -46.13441 | 2025-07-14 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 217b1007-80e2-3248-9c50-01c5bb5bf9f8 | -6.94811 | -42.72815 | 2025-07-14 04:27:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1de1769d-9296-31c9-90d5-9f2198e3b97b | -6.63136 | -56.2869 | 2025-07-14 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a11124c-8dc7-35f4-b211-8eedf94fa309 | -6.26162 | -43.35908 | 2025-07-14 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d4ac846-7211-3540-b231-49dc879671ad | -7.0352 | -44.35626 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29e109dc-4111-3c3c-bd78-8ef3e5c1223b | -8.5182 | -43.30468 | 2025-07-14 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 25.6 |
| d24d2df2-e7d1-3bd1-a295-dbd5afea8a40 | -9.39049 | -47.97049 | 2025-07-14 04:27:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 899d5f48-45fd-30da-8b22-b1e4c6d61b05 | -6.81291 | -42.83569 | 2025-07-14 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5dfbaafa-74d4-3a68-b081-c4f6a12f44b0 | -2.91491 | -48.23966 | 2025-07-14 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d77b88a5-ebbb-38dd-9d7e-57a9b9b466d5 | -6.66839 | -43.12584 | 2025-07-14 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c7ea6fc-97a5-3b1e-ad52-938406ff90f2 | -5.7471 | -44.98551 | 2025-07-14 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 107e2120-c8bf-31a4-913e-37901f895fc1 | -7.05674 | -43.9598 | 2025-07-14 04:27:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98850b0b-a2fd-3d81-b87c-d398ef774653 | -7.04736 | -44.32328 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8f7b09c-9e72-34ca-b754-e6b572c22817 | -6.8803 | -44.72443 | 2025-07-14 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df6b1a71-1cc6-31f9-87fb-32ce6cd82bec | -4.47804 | -42.93672 | 2025-07-14 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ccf89617-c1d5-3fc6-8949-e9d2b31d8cf6 | -9.49586 | -47.5629 | 2025-07-14 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f6b55e4-bff4-32e0-aa05-e915b5d17b88 | -8.04064 | -50.0913 | 2025-07-14 04:27:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 856aefc9-f548-30c6-9621-9278f25e8d78 | -8.04735 | -50.09636 | 2025-07-14 04:27:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0faac1b-1a80-351e-8605-a1be058d06cd | -9.4867 | -40.38757 | 2025-07-14 04:27:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |


[Clique aqui para ver as próximas entradas](README8.md)
