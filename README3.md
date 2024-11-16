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
| ecf4e2b7-e9da-3394-9193-0bae9faa5ca5 | -3.79511 | -40.99151 | 2024-11-16 00:24:00 | TERRA_M-M | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 1663d5b8-57dc-32f4-96b7-3bf124728638 | -2.55648 | -46.90287 | 2024-11-16 00:24:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 27778076-dea4-36dc-82cd-9d3cbf5399ac | -3.76722 | -50.78846 | 2024-11-16 00:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 265.0 |
| 5fdb944b-5129-3b13-833e-006125a79e96 | -4.22293 | -47.22706 | 2024-11-16 00:24:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 37.1 |
| c6b2346f-6722-39c8-a4d3-e5e11c93f7e6 | -3.73181 | -45.67443 | 2024-11-16 00:24:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 3f606dda-bdf5-344a-aa2f-56bfd20a2edf | -2.46006 | -45.44735 | 2024-11-16 00:24:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 0932a3da-41da-3005-b8c9-dc1d608a4377 | -4.03286 | -44.10656 | 2024-11-16 00:24:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 84af2980-eb86-3789-90b5-22d595bfc110 | -2.58957 | -45.64009 | 2024-11-16 00:24:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 34.3 |
| a0b385c2-c304-3115-af4c-1cd46fb36306 | -5.71842 | -44.81747 | 2024-11-16 00:24:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ed36115d-51f4-3d0e-8561-8b689758e076 | -5.00608 | -37.53096 | 2024-11-16 00:24:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 7.0 |
| a10af1fc-a9c2-3cc8-a744-0237e4516047 | -4.55667 | -45.75818 | 2024-11-16 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 17.4 |
| db2a3333-1a66-3eac-915c-e0765d915650 | -5.91242 | -46.23821 | 2024-11-16 00:24:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 44.4 |
| f11fa337-389a-3903-9f8c-d73971f7067b | -4.36648 | -45.61742 | 2024-11-16 00:24:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 55cdeaef-358d-35f2-ab57-2384db260d73 | -5.95848 | -44.46497 | 2024-11-16 00:24:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 12ee2004-1968-3c5f-9557-dd4aa4effb1d | -3.492 | -45.44206 | 2024-11-16 00:24:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ad10aa9c-5d56-32c9-861a-a818bd7d5988 | -5.95099 | -44.45893 | 2024-11-16 00:24:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| dbff6a7a-34a4-34b9-b2d8-eec174ca16c9 | -2.15337 | -46.55175 | 2024-11-16 00:24:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| d2c13fce-12ec-3116-8902-0f44d9ace6e7 | -4.37763 | -45.61601 | 2024-11-16 00:24:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| ac08cc5f-fe25-39a7-a2fa-5e2554a62f71 | -5.01069 | -44.31761 | 2024-11-16 00:24:00 | TERRA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b6eda590-4543-387a-b2fa-b9190b28d2aa | -5.92884 | -43.77659 | 2024-11-16 00:24:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4ac68a6a-4469-3341-85b6-92972d2f53b9 | -3.9804 | -43.725 | 2024-11-16 00:24:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 2cfdb2cd-c634-3e91-9344-9bbb29ceafe9 | -3.01331 | -42.99296 | 2024-11-16 00:24:00 | TERRA_M-M | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 64bcf4ed-b6ea-3f6f-aaa9-f551ac53987d | -2.10327 | -46.5968 | 2024-11-16 00:24:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 2c73b487-bef6-332c-9a9d-6769ab3e7b56 | -5.00283 | -44.32442 | 2024-11-16 00:24:00 | TERRA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 32.7 |
| d5871f11-4e3e-3839-a1f1-4a06801e02f4 | -4.23544 | -43.18209 | 2024-11-16 00:24:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ff8507f6-9ec2-3ac7-b411-68dff450fb6c | -5.94033 | -43.78648 | 2024-11-16 00:24:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ffa33852-61b9-31c4-9016-76b7601d6b4f | -5.21679 | -43.79065 | 2024-11-16 00:24:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 778af025-66f8-3dd0-8947-104261d2530f | -3.29291 | -44.07707 | 2024-11-16 00:24:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e286cff8-ca14-3746-8024-7a29b3ae772b | -3.79142 | -43.90525 | 2024-11-16 00:24:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 5a41e272-bf65-3ca0-a911-cf8c697765e7 | -3.02297 | -45.37341 | 2024-11-16 00:24:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 2ce49d6d-70bb-33df-a5a8-10e15371fc91 | -4.37766 | -48.09631 | 2024-11-16 00:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 96b3cea4-f7d4-3d22-94b6-a845821b1501 | -1.76445 | -46.23009 | 2024-11-16 00:24:00 | TERRA_M-M | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 26.8 |
| dce9317b-e211-3390-bec7-dc239fb8acaf | -5.32977 | -40.89514 | 2024-11-16 00:24:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| a7064ac7-f1c6-3c42-918b-88f4921f5240 | -4.3607 | -45.48807 | 2024-11-16 00:24:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 19.4 |
| ec27bba8-e799-326c-ad7b-e28a46e7084d | -3.50282 | -45.44056 | 2024-11-16 00:24:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e96c5994-ce7b-38a9-a7df-d5a8ee188cc7 | -3.57526 | -50.53186 | 2024-11-16 00:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 2ca477cf-01cb-3808-84a6-b6385d4d8b77 | -3.211 | -46.67997 | 2024-11-16 00:24:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ed5b479b-4fa6-3c60-989d-8c0afec6a289 | -3.46788 | -43.41539 | 2024-11-16 00:24:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| b70d9159-41a1-3047-9c09-a39abed5e220 | -4.85212 | -42.7032 | 2024-11-16 00:24:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 014e44f6-c532-32b5-90ed-4ed58c3a3ffb | -3.74483 | -50.19161 | 2024-11-16 00:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 491d9c8b-4279-3328-a297-be1a80b7858e | -1.24267 | -47.7192 | 2024-11-16 00:24:00 | TERRA_M-M | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 39f11bbd-fe1b-36ba-b495-be120bc4fb83 | -4.37456 | -48.07307 | 2024-11-16 00:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| b02d5305-3c45-3283-8d83-a12ea40f2c15 | -5.29957 | -43.07061 | 2024-11-16 00:24:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f3d6354e-4816-387f-a050-7825b5b39411 | -3.50399 | -42.00542 | 2024-11-16 00:24:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| c731b63b-7880-3dd0-aeab-0465121f08a1 | -3.28722 | -46.20708 | 2024-11-16 00:24:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a7910cf9-e12a-36de-bdf1-06c004138250 | -2.63838 | -45.17529 | 2024-11-16 00:24:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 0cd17754-df6c-3785-923b-4d7ef1e2da83 | -4.40248 | -43.81188 | 2024-11-16 00:24:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 359153fb-4ff1-3822-aaae-3e15b85ffe39 | -3.50281 | -47.21978 | 2024-11-16 00:24:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 025938ab-e784-3210-9aaa-1b26f331b41a | -5.78329 | -48.15712 | 2024-11-16 00:24:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 8c4bbe39-ee29-3248-a9b3-e51ac3a9a017 | -6.16895 | -41.16403 | 2024-11-16 00:24:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| faaacc7d-4726-3717-bc20-56f16d620f74 | -6.20791 | -41.65211 | 2024-11-16 00:24:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| d62afcbe-0182-3b52-bc8b-44dc148e5729 | -2.98659 | -43.92963 | 2024-11-16 00:24:00 | TERRA_M-M | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 83d3723b-656c-383c-8efb-018ddc840876 | -3.99757 | -45.86259 | 2024-11-16 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 3f53df97-32ef-329e-91a3-9955f6fa3d55 | -4.22136 | -46.42543 | 2024-11-16 00:24:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 0e66b1d2-f5cd-365d-a1ed-1453416a025d | -4.54036 | -43.56807 | 2024-11-16 00:24:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 54f677f4-6066-32ad-88c6-dbd58e526bdf | -4.9055 | -43.23277 | 2024-11-16 00:24:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d4959e2c-eec8-37cc-a2d9-c54e0bad74cc | -1.24135 | -47.725 | 2024-11-16 00:24:00 | TERRA_M-M | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 0124e39c-334a-36af-a929-bb029c9ed2f5 | -3.91755 | -45.86418 | 2024-11-16 00:24:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a98b5e18-86a6-39b0-a4d4-bc305de52c9a | -4.37949 | -45.63011 | 2024-11-16 00:24:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 45.8 |
| a888f825-6b6a-346d-89b9-301954e63b98 | -4.61746 | -45.34972 | 2024-11-16 00:24:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ffa2dc0d-63aa-3521-8d11-99b7807ab64b | -4.53889 | -43.5575 | 2024-11-16 00:24:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 07f03ce3-4f95-35e6-ac06-b3dadcae2df9 | -6.30354 | -39.49285 | 2024-11-16 00:24:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 7a647246-4931-3c97-a9f9-cde4d726fb56 | -1.18122 | -47.08174 | 2024-11-16 00:24:00 | TERRA_M-M | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| dcd6c38f-28f9-3832-bf0c-e9dfdd0f4181 | -3.97895 | -43.71442 | 2024-11-16 00:24:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 3dec35d6-312c-35b1-b0a5-0446d723bc7a | -5.90719 | -46.24517 | 2024-11-16 00:24:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 279eb5d6-5857-37ad-a239-7c02a55f274d | -4.54303 | -43.5619 | 2024-11-16 00:24:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 533a43cc-7597-3b8b-9151-c24a0fd3cd1b | -5.23385 | -44.90612 | 2024-11-16 00:24:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 2e4f2445-8707-31cb-9012-0157c4663002 | -2.1456 | -46.41124 | 2024-11-16 00:24:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2ad8575b-d349-3289-8e5d-64de22be12f1 | -2.28875 | -46.45763 | 2024-11-16 00:24:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2779e38d-15bf-3992-b1dd-1e0a198e42a2 | -3.50035 | -47.20132 | 2024-11-16 00:24:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 41df3b0e-d97e-3179-b66b-304c80276b43 | -5.90489 | -46.22811 | 2024-11-16 00:24:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| fc2d2813-51e0-3985-b7aa-1f576a0e2995 | -4.54946 | -48.0147 | 2024-11-16 00:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 1db83d41-0e13-3b83-b3e3-88ae106d61b6 | -5.4895 | -43.76907 | 2024-11-16 00:24:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b6909ac2-5572-3f76-90c4-1bcd2a7c0a47 | -2.15918 | -46.42498 | 2024-11-16 00:24:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| f3f46865-a175-35ee-b2b0-63dfda1e1f5d | -4.991 | -44.31393 | 2024-11-16 00:24:00 | TERRA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| e0b60657-c510-3f71-9210-59878674c449 | -4.8273 | -44.38503 | 2024-11-16 00:24:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| df9727c4-c487-3e77-91f3-0dd1b1b83b39 | -3.5382 | -51.50179 | 2024-11-16 00:24:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 5f48b583-d8de-384b-9db4-25f517ad8ed2 | -3.39694 | -45.22486 | 2024-11-16 00:24:00 | TERRA_M-M | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5f2e3c13-3ea1-338f-a760-c1f1272e39cd | -5.93878 | -43.77517 | 2024-11-16 00:24:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 56f12dae-f252-3472-bbbe-83edf8ee6026 | -5.43891 | -42.88554 | 2024-11-16 00:24:00 | TERRA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 9d961089-a4cd-39dc-958c-8e3ab2f19b29 | -4.36833 | -45.63154 | 2024-11-16 00:24:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 1dc61f48-25bb-3668-88ce-ff73e86cc9a3 | -5.75299 | -49.46536 | 2024-11-16 00:24:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 0270429e-1bd8-3a2b-b87c-cfb604ed25ba | -3.12385 | -45.16253 | 2024-11-16 00:24:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 15.0 |
| bd35885a-98d8-3c13-9c72-cfbbf6b6a102 | -2.34422 | -47.45646 | 2024-11-16 00:24:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 8ae912cc-033f-3c37-9e48-4b7d3d07ac81 | -3.72917 | -45.66604 | 2024-11-16 00:24:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 72993d34-9fad-3c1a-ba38-55be1c884d1f | -5.94802 | -44.46636 | 2024-11-16 00:24:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| c37a4984-c078-33e2-9fee-e19caeb6ee1b | -3.77226 | -50.78104 | 2024-11-16 00:24:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 664b664e-f3c6-3105-a8c3-7591b0c6040c | -1.99806 | -46.58539 | 2024-11-16 00:24:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 5b096db3-a9ae-3076-a30e-4ecc62b79c45 | -4.99263 | -44.3258 | 2024-11-16 00:24:00 | TERRA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 38.3 |
| c20043b9-21bd-38d3-980a-e51c84a622da | -2.22074 | -47.22057 | 2024-11-16 00:24:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b161f77c-ccc8-3e5d-bcf6-85907e491cb9 | -1.89822 | -47.00786 | 2024-11-16 00:24:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| d3813096-edd4-35ab-ae3d-ef20ec120d4c | -2.63663 | -45.16278 | 2024-11-16 00:24:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 1eb16b60-0d07-3ef6-a4bf-27336f01a3f4 | -3.33048 | -43.82529 | 2024-11-16 00:24:00 | TERRA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4a4aface-36e6-3737-b108-2a22125bc8fb | -2.89588 | -40.02702 | 2024-11-16 00:24:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 12.0 |
| caafbe9e-dd9d-33e9-a779-506febff3405 | -1.23532 | -47.47803 | 2024-11-16 00:24:00 | TERRA_M-M | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 596ea71f-e082-31e4-bda8-ee7f54eeaa11 | -4.29923 | -48.08979 | 2024-11-16 00:24:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| a9a18240-cae9-34b1-be78-1fdd3088fe32 | -1.70975 | -46.16389 | 2024-11-16 00:24:00 | TERRA_M-M | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 76c7ab67-ac17-3f19-80a1-c4dd6c5cc2b0 | -4.66289 | -44.08125 | 2024-11-16 00:24:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9ced16c5-0a98-3370-b8e5-e5a752e7ca7f | -6.04214 | -42.25663 | 2024-11-16 00:24:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| c8297b40-a194-3d53-afa6-d332a89fd7d4 | -2.12387 | -46.50819 | 2024-11-16 00:24:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |


[Clique aqui para ver as próximas entradas](README4.md)
