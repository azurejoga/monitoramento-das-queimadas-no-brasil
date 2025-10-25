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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c452b2e2-18f2-3a42-8ef6-8c38526a3383 | -13.85143 | -46.89762 | 2025-10-25 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b23e10a8-52be-342f-8ad9-94218a3ad39c | -18.16764 | -51.76156 | 2025-10-25 04:21:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ab649701-7cf8-35ba-b3e1-b3c05ab4ae91 | -15.23596 | -47.93653 | 2025-10-25 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e288f8c7-7cdc-31b3-a956-dc8c489dcdfe | -14.46887 | -47.90553 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41d8096d-f169-3b78-b04a-c92a2347abbf | -15.76648 | -46.10356 | 2025-10-25 04:21:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d2040c5-066b-3303-b5d3-26a170f65638 | -14.89215 | -47.86292 | 2025-10-25 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6607d2ff-6d91-3524-8df0-02205c232b39 | -16.21729 | -46.47976 | 2025-10-25 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a00bda11-a091-3d1c-8fe8-009223e506b2 | -14.20103 | -47.30171 | 2025-10-25 04:21:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7267e04-b434-38dd-aa9b-fd73d98a08c5 | -15.18906 | -44.07687 | 2025-10-25 04:21:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8603dab-c8ed-3dd9-9a00-17e2c6429ad2 | -17.46248 | -48.40076 | 2025-10-25 04:21:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8c35d22-c1d6-3604-a3f7-5b1dd42553ed | -13.83136 | -48.50518 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5c741b7-af9a-33c0-a248-6e29109c7f85 | -14.38182 | -51.52395 | 2025-10-25 04:21:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9af2c52-7d19-36c9-aa25-bff2dbf920f4 | -14.8695 | -48.09475 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c0526fe5-e752-3739-ba71-898bdb7e1bbf | -14.9518 | -47.70021 | 2025-10-25 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d333e22d-f7a0-3e49-a8b2-a551ef895e83 | -19.86723 | -48.33411 | 2025-10-25 04:21:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6327a62-0d1d-3f30-8692-13c2a9a9de73 | -18.15927 | -44.25018 | 2025-10-25 04:21:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d434c328-b698-380c-b512-3ea15f4241dd | -14.09722 | -47.20708 | 2025-10-25 04:21:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b136e7e8-bdf7-3879-9066-d3d580414474 | -19.76229 | -48.28865 | 2025-10-25 04:21:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f239c636-91df-36a2-a16e-15c7265491ac | -19.76561 | -48.28924 | 2025-10-25 04:21:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6e05c839-141d-3b2e-b4ec-c2dd602a3fdc | -15.78925 | -52.84349 | 2025-10-25 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 155ff1d6-1f75-3edb-aa47-0b373b00abfb | -19.76833 | -48.29353 | 2025-10-25 04:21:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 043f09de-aa7e-33fd-b25b-12c38af7cd14 | -17.29141 | -49.23495 | 2025-10-25 04:21:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d9b7e82-87c2-3ffb-aee9-88e51ef536ea | -13.8767 | -48.38266 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 921564ca-0485-35b7-9117-d009ec29ea13 | -13.64681 | -48.64752 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5267e17a-cfe1-3c03-86f8-d0b924c34240 | -19.75897 | -48.28805 | 2025-10-25 04:21:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6181bbbd-caff-333a-9670-c8382a0fcf55 | -21.56648 | -45.77591 | 2025-10-25 04:21:00 | NOAA-20 | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a9e248c6-2c73-3255-8877-b8481c9fa75e | -14.7219 | -46.61592 | 2025-10-25 04:21:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19c98f6a-6444-3087-944d-32bfc71a0eee | -17.34128 | -55.02051 | 2025-10-25 04:21:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ab855897-4ee2-3f3b-9965-d9fd3fbfc3b2 | -18.16566 | -51.75077 | 2025-10-25 04:21:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b7da45f3-2285-3973-9eb0-d06f4464263b | -14.56229 | -54.18151 | 2025-10-25 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79373816-8831-368c-b6df-8c73fa51766e | -15.24328 | -47.93403 | 2025-10-25 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fbb88217-5663-33bd-bdc0-a44780e93455 | -14.74511 | -46.5979 | 2025-10-25 04:21:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d83afed4-8440-3e19-919e-931169e2e710 | -14.1916 | -48.20053 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1dad6d2f-cab0-3471-837d-27cd4943a30a | -13.88061 | -49.04981 | 2025-10-25 04:21:00 | NOAA-20 | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f766fcd0-86b7-3607-9723-07414daca065 | -14.47809 | -47.93369 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd6a44f6-2354-34f6-8fee-cf2f483912bf | -14.84053 | -52.44224 | 2025-10-25 04:21:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 74ef93fe-ffc6-3c5b-a5eb-fb11b71d3790 | -17.37154 | -45.49508 | 2025-10-25 04:21:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 270a120c-e60c-3484-ab41-86a1635a3d38 | -13.91885 | -48.40551 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fdec11ea-0ce0-3f7c-b9f5-0156c64ac2ba | -14.56332 | -49.84291 | 2025-10-25 04:21:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0f15248d-9870-365e-9bf7-cb531db952de | -13.88448 | -48.39959 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 707423ab-cfa5-30b0-afee-e0f6b86fb30f | -17.51298 | -45.1062 | 2025-10-25 04:21:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e71194c3-a3fc-3fa8-b182-fd65c8b2fd6e | -14.89443 | -52.45595 | 2025-10-25 04:21:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4205a40a-4c25-35b2-80e8-f4966a34db7c | -18.27841 | -45.91224 | 2025-10-25 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 603e9680-3cd7-36aa-83dd-3be1e10ffc6d | -15.22376 | -47.9268 | 2025-10-25 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 201b643d-6562-3ca7-8bbc-8fd3f948bae1 | -15.00083 | -49.98536 | 2025-10-25 04:21:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3c5e4810-ef3f-37bd-945e-10788f87d8d2 | -19.33215 | -49.09017 | 2025-10-25 04:21:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 84da6267-4eb0-38b0-9787-98d5e0b20e56 | -14.76796 | -43.0844 | 2025-10-25 04:21:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 3e141b34-2bb5-3d2c-a6d5-cad17578ccf5 | -16.21673 | -46.48335 | 2025-10-25 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a1ba61a1-73c9-3bfe-81f0-18e558ca0602 | -21.37238 | -45.03104 | 2025-10-25 04:21:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4433ae21-6cb8-3a12-bf13-e0ac13651303 | -14.17539 | -47.31221 | 2025-10-25 04:21:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 29568c55-2fcf-3e59-9c86-9513b43697f3 | -19.63108 | -46.13219 | 2025-10-25 04:21:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 70132977-a206-376c-bbee-e565cb46b9c1 | -19.8772 | -46.97718 | 2025-10-25 04:21:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a29b55c5-c57a-3b69-8be5-e3c86eeea99a | -15.83007 | -49.09061 | 2025-10-25 04:21:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8817405b-d98e-3543-b1af-e90c44f2adfd | -17.58717 | -49.10763 | 2025-10-25 04:21:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2f9a1fb2-084a-3c6c-859f-54b89863142d | -15.98261 | -43.90501 | 2025-10-25 04:21:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 5.2 |
| be264d7d-af83-398e-ab1c-80a4421c75d7 | -16.84142 | -50.52509 | 2025-10-25 04:21:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a81d022-9e91-3f9c-af2b-e01586bb731a | -14.76798 | -43.08139 | 2025-10-25 04:21:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 3.6 |
| af6f24ec-2d0c-3fec-8be2-12d3ae4096ed | -13.87606 | -48.38649 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9135b59-177a-3687-b63f-6ea6bb2aec57 | -20.44213 | -46.58123 | 2025-10-25 04:21:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da484d06-0eb0-3cf4-b2af-f3e4e2d8f3bf | -13.90258 | -48.41834 | 2025-10-25 04:21:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f74d20a5-f547-30dd-8580-f8bde9bee58f | -17.05964 | -48.0352 | 2025-10-25 04:21:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfbb1e00-ef48-3ac0-a9ff-5b0b91c4338b | -14.8882 | -47.86602 | 2025-10-25 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74228205-89fc-3122-ba98-20385ef730be | -20.10907 | -45.85183 | 2025-10-25 04:21:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca26a73b-dd79-3e2d-aba2-25975a3857de | -13.64947 | -48.18651 | 2025-10-25 04:21:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebef13f2-98b6-352b-89af-0e73219abbac | -15.45984 | -43.09544 | 2025-10-25 04:21:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6bbafc84-ab73-3253-82bd-3285c1eafd02 | -19.6828 | -46.13308 | 2025-10-25 04:21:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6daedcdd-6159-38a6-b180-22e19c225e33 | -14.81098 | -48.4451 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 576dd23e-606b-3d96-9178-4b283b4dd9db | -16.17259 | -45.0888 | 2025-10-25 04:21:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a4920cb-d1b9-36a7-ae89-e4413354bbd9 | -17.41681 | -46.88589 | 2025-10-25 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| da1b3d4e-5b23-3233-ba34-67568a0b5501 | -19.6013 | -43.69242 | 2025-10-25 04:21:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3647292f-2e73-3f72-9c95-0cfca2f812d2 | -19.87565 | -48.32425 | 2025-10-25 04:21:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c516f37-ca4d-3c4f-8ead-5b75b6cb83d3 | -14.86487 | -48.10165 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a75489e9-affb-3dfb-bf94-f8e7be33a4b0 | -20.8287 | -45.00171 | 2025-10-25 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| d03aee50-5a54-3665-8431-6e176e0fc6b2 | -17.41334 | -49.68338 | 2025-10-25 04:21:00 | NOAA-20 | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1aaaea54-addc-37d7-a7ff-b21edce54c7c | -19.02887 | -47.51918 | 2025-10-25 04:21:00 | NOAA-20 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27eab077-0b25-3860-afbb-de77084f9d8c | -14.39632 | -51.54124 | 2025-10-25 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1927551f-844a-3def-9eac-02e64c4a8fee | -14.43771 | -48.07244 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8b07e2e-7f91-3d8f-a755-4eb6f19723be | -21.50083 | -44.26277 | 2025-10-25 04:21:00 | NOAA-20 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2268cdf9-2f68-3ec5-93c7-ceecd07032ac | -14.44571 | -48.06625 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3fb9a540-5c81-3a82-bf83-ede9aa050929 | -14.8888 | -47.86232 | 2025-10-25 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2237592-d2f8-3422-87e2-48a77300808c | -14.87225 | -48.09908 | 2025-10-25 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4f735658-907b-3552-b9d7-84848f743bb3 | -19.27802 | -43.29196 | 2025-10-25 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3160504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 01ff30af-fa30-3e05-b85a-b6fb7511a6df | -19.08318 | -46.75813 | 2025-10-25 04:21:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 702e4c3f-b943-3ac7-93e5-e558bfb662b9 | -16.58363 | -43.50611 | 2025-10-25 04:21:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 24.6 |
| baf4cedb-190f-3923-8a4a-ec2cd0a57fd2 | -14.72133 | -46.61948 | 2025-10-25 04:21:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 016fb906-200b-3037-91ce-fb04398e4382 | -14.91268 | -52.4516 | 2025-10-25 04:21:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7dfe4991-6d03-31f4-b730-0d6a253d9e98 | -16.21398 | -46.47921 | 2025-10-25 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1355643-5e04-3d14-9821-e002e5c3190e | -14.47629 | -47.9026 | 2025-10-25 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 579150d3-3294-354a-8b28-2c309620ea44 | -14.38119 | -51.52755 | 2025-10-25 04:21:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8eb79ea5-69ad-3d79-93fd-92f52417a452 | -21.0974 | -45.34476 | 2025-10-25 04:21:00 | NOAA-20 | COQUEIRAL | MINAS GERAIS | Brasil | 3118700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| db4800b9-a943-3125-b029-3b2e3641a56f | -21.37178 | -45.03534 | 2025-10-25 04:21:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5fcbccda-5e70-3d61-8b13-b6f8a3471621 | -19.8594 | -44.30826 | 2025-10-25 04:21:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb2bfe76-e2a0-389e-91b5-7c13462052f9 | -25.04024 | -49.71069 | 2025-10-25 04:23:00 | NOAA-20 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 033331d8-cb48-38c6-910f-a815b0c6217a | -25.04294 | -49.71518 | 2025-10-25 04:23:00 | NOAA-20 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0f66bf5e-1a43-3ea1-9162-5590cf6cc1d4 | -22.88254 | -47.26461 | 2025-10-25 04:23:00 | NOAA-20 | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| de378f73-0f5a-31ae-923c-69935e4e737a | -22.22878 | -53.35218 | 2025-10-25 04:23:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 55c81935-1de8-3e52-9d60-7bea29139bf9 | -23.41282 | -49.68059 | 2025-10-25 04:23:00 | NOAA-20 | CARLÓPOLIS | PARANÁ | Brasil | 4104709 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 937af829-0581-3be3-a676-c6871128141b | -25.09328 | -52.32331 | 2025-10-25 04:23:00 | NOAA-20 | MARQUINHO | PARANÁ | Brasil | 4115457 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 40e1661b-783b-3f3e-a5eb-e4f4a7a63623 | -23.39065 | -51.13017 | 2025-10-25 04:23:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b80c3b97-3f2c-3f46-bbeb-e64d33ff976a | -22.8313 | -51.35815 | 2025-10-25 04:23:00 | NOAA-20 | FLORESTÓPOLIS | PARANÁ | Brasil | 4108007 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |


[Clique aqui para ver as próximas entradas](README48.md)
