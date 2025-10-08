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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce96eeaf-c651-3af1-b3ad-945e4d6910b7 | -17.25907 | -46.90774 | 2025-10-08 04:40:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c0e3da76-d5df-3065-8313-c7f2719d989c | -15.64237 | -52.57339 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5eaa25b-21b9-3d52-b87d-b01412d34726 | -15.38918 | -48.03069 | 2025-10-08 04:40:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 273f8469-c2a3-3758-b01f-3c2e75b702f1 | -11.73911 | -50.93626 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4188426-cec8-3406-a29a-b75edb011337 | -11.16094 | -54.88249 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5983e994-d0b4-3108-8abb-319ade5bc657 | -15.63746 | -52.56125 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3894206c-ebd7-3199-827c-79471d151891 | -12.29788 | -55.10411 | 2025-10-08 04:40:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71eef996-5651-3bc6-aa8b-4da5e17d5482 | -12.50646 | -54.72235 | 2025-10-08 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bea4d47e-42c7-36c5-81de-53387af58c75 | -12.32703 | -50.26699 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6f17290-72ef-3bc5-9c0a-016e1a0242e0 | -17.56543 | -46.08017 | 2025-10-08 04:40:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cdbe86e9-d3ad-3a90-b64f-f4e410d782b3 | -11.14844 | -54.8854 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5af5bc63-1a48-3cbd-abf4-34d132193dd7 | -15.99228 | -50.83878 | 2025-10-08 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8eb429f6-06fc-3490-bcac-c90940145f66 | -18.50543 | -43.89885 | 2025-10-08 04:40:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71c2e1ee-6c82-3042-a5b4-e9aaf97ce33d | -14.39512 | -46.03475 | 2025-10-08 04:40:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2c375c4-85ff-3441-99a1-cb5e4addacae | -14.68034 | -51.90116 | 2025-10-08 04:40:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4ea7627a-75a0-3e10-b643-58020e598bc3 | -15.24674 | -46.35427 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c60fdbae-a32c-30b1-b39f-5ff77c7882b8 | -11.46047 | -50.20642 | 2025-10-08 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e75198eb-5ccb-37ad-8e12-0d5891babe2a | -11.16568 | -54.87822 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4aefb5fa-36b0-38a8-978b-15906173b22c | -13.80641 | -45.79002 | 2025-10-08 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d800b1af-a1b4-34a0-92e0-5e51c8a68b9d | -14.79556 | -41.62894 | 2025-10-08 04:40:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f5fcfa09-2547-35a3-be4f-e80dc34ef11d | -14.9462 | -46.79949 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8581215d-5bcb-320c-aaa0-a1bc7870ca86 | -13.0892 | -47.80636 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 545fc009-948f-30ef-a717-c5930e4b805a | -15.63806 | -52.55753 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98c77096-c1ba-34c0-9be6-5c9d280dd80f | -19.51476 | -44.08142 | 2025-10-08 04:40:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bdb8d1f-0153-3b9e-b1e4-565532286ca9 | -11.14307 | -54.88789 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f9d94b4-9d80-307a-9db2-bfb223d596d1 | -18.02162 | -51.14411 | 2025-10-08 04:40:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e014993d-4303-3268-8159-d79093e5263a | -15.3062 | -46.15872 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2bc69b3f-9700-384b-8804-d34f9add116b | -15.42415 | -41.27261 | 2025-10-08 04:40:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 76628b46-372d-36a3-a5d1-66546084770d | -15.3676 | -47.29525 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 22.5 |
| d241dbde-88a5-39a0-a0f7-d76f0e47eaac | -12.4361 | -54.21943 | 2025-10-08 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acc26fc9-79bc-3422-9549-3ea3db4586d5 | -16.33722 | -47.0575 | 2025-10-08 04:40:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f56a10b6-5bbe-343f-88b3-432c8dabc796 | -16.27444 | -50.98795 | 2025-10-08 04:40:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42a3e4a9-81af-3ea9-a44d-ceff67e3102f | -12.37507 | -50.30755 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90b4ca6f-edea-3eb4-b21d-2b08891b55c3 | -11.1717 | -54.88951 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 4d6d8baa-4994-3804-9240-bcd8754787a7 | -12.32537 | -50.27757 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b53383a8-f7f4-36cc-ac69-4a624f2a9289 | -17.1597 | -56.611 | 2025-10-08 04:40:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 110dbbfe-2235-39fb-acf9-f8f7d28c0074 | -19.30659 | -43.76764 | 2025-10-08 04:40:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| db96769a-f7cf-3081-a9e5-7f102a103688 | -11.73248 | -50.93517 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| deb728e9-1871-3788-b9b7-af80bef1d9ca | -11.11189 | -54.04049 | 2025-10-08 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 47704058-3e17-3d11-baaa-558bda5453d7 | -15.36691 | -47.30039 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 22.5 |
| ab442c6e-54f4-35af-8ea8-d36dc503687a | -12.38954 | -51.1402 | 2025-10-08 04:40:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94b10a36-bef8-3d1f-9291-ce7e428f947b | -17.96745 | -44.97932 | 2025-10-08 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47060151-f7b3-31a3-bd8b-de2458edbf09 | -17.37855 | -45.05908 | 2025-10-08 04:40:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69fec284-39c6-3cb7-ab75-87bd7ad75f92 | -13.07909 | -47.92505 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2ea19bb-8894-3d37-97f0-4867fbd1bc57 | -11.74518 | -50.94086 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b87d1b15-4dca-3522-8ebe-aea15e097ecb | -19.13123 | -43.51915 | 2025-10-08 04:40:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5428b905-1579-3310-bfda-6a2a3a8b0599 | -13.30906 | -48.03152 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8ea39dfd-91a8-3dea-8c0e-868577789358 | -17.48704 | -43.33316 | 2025-10-08 04:40:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b78a62c2-8021-3030-b941-b08c56262950 | -11.74135 | -50.92218 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 2c845725-9dd0-3630-a7b6-3ebc2e790966 | -13.28699 | -48.47727 | 2025-10-08 04:40:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 039f87f4-9ca3-365c-8975-9666c914adb6 | -13.74018 | -45.75913 | 2025-10-08 04:40:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| acda4561-05c4-3c3e-86eb-8e980755475e | -15.94328 | -42.59666 | 2025-10-08 04:40:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 0b484eeb-fdb5-3c60-8edb-a3f7bd121e77 | -16.06529 | -47.77545 | 2025-10-08 04:40:00 | NOAA-20 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5de8818-5764-3446-9e22-939eecf7aeaa | -13.0323 | -47.89684 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb2ac2f3-d024-3656-b2a0-64e5462e72e5 | -13.01634 | -47.91256 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02d66689-6a2e-3460-92a4-5ab3247c3367 | -11.33098 | -56.20512 | 2025-10-08 04:40:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8e762e1-2232-326d-b99b-3b85b7a7c8cf | -12.24611 | -47.86923 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6df445f9-aec3-3659-804e-fd0efeed7977 | -11.9997 | -46.7712 | 2025-10-08 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 29aad5b3-3a39-3511-beb4-68a26bbed1ef | -11.42384 | -56.29589 | 2025-10-08 04:40:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ffa781c-50f3-32ff-9e17-4e03e6184eb4 | -13.30251 | -48.02673 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e71a4773-a124-3cfe-b1f6-451de5e8845f | -18.51146 | -43.93377 | 2025-10-08 04:40:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fde78942-bb86-3362-b3a5-f667f34bc52c | -18.03715 | -51.15421 | 2025-10-08 04:40:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ac758234-32f7-30db-a489-ff398a2d2101 | -18.30312 | -42.23172 | 2025-10-08 04:40:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 968e2a5a-9cdb-3d10-8cc2-cccae0256436 | -13.10958 | -47.7921 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d05f54ce-07ac-3641-882a-4e88670dea0a | -18.30011 | -45.44489 | 2025-10-08 04:40:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06b19324-36d4-3f15-ae30-279e02a4e3dd | -11.14155 | -54.87915 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 64485569-079c-3fb8-85b7-a8fbd5c528c3 | -11.74023 | -50.92922 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 7cbebc47-3076-3e85-97cd-1fd77e1285a0 | -11.15016 | -54.87559 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48632e80-a067-3de3-b152-de7204824121 | -14.96028 | -46.8117 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 000ba70a-9e9d-33e6-865b-fa1b3d05252b | -18.54841 | -41.57892 | 2025-10-08 04:40:00 | NOAA-20 | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 9677bd5a-3726-30fd-8551-8802d47f4c84 | -15.38887 | -46.28313 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11a6730b-2ddc-3909-a4f0-9f95d7182985 | -12.9444 | -46.85895 | 2025-10-08 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f55c4827-fdb5-3e91-9893-99425b0e5652 | -14.23987 | -60.17194 | 2025-10-08 04:40:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 66750c42-3444-3276-8205-aec9cc104f97 | -15.62111 | -52.57721 | 2025-10-08 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2dfeb4be-ce5d-3c20-b5ad-1cbe2e74f077 | -12.23256 | -47.8631 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7001f1b-a0f5-37c9-a825-98334878db1f | -14.389 | -46.01927 | 2025-10-08 04:40:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 25195a1b-001f-321c-9e55-d2d2f4721e9a | -11.33517 | -56.20597 | 2025-10-08 04:40:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26adcdc5-5bd7-3fb7-9d64-8f538fc9a1c3 | -11.14555 | -54.87318 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab2a6ca7-cdc6-3f96-a3d3-1486b19f5254 | -11.9139 | -55.90412 | 2025-10-08 04:40:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acc4e152-0a4b-342a-a27e-f46dfca781b4 | -14.09762 | -44.30933 | 2025-10-08 04:40:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc7560ba-fd39-37a0-8d7e-339ba64819fc | -15.98784 | -50.84541 | 2025-10-08 04:40:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cc58a175-5d99-3262-86e9-7005babf3e1d | -19.46635 | -45.95615 | 2025-10-08 04:40:00 | NOAA-20 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1073ffff-8737-33d4-82b2-a4098904f950 | -18.19353 | -43.04846 | 2025-10-08 04:40:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 45c1473f-c8b6-38bc-8d78-df493fefbb69 | -11.17296 | -54.90525 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f37c103-1d26-3c21-a155-c231df522b4a | -11.01701 | -52.32191 | 2025-10-08 04:40:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d5cb80b-fb47-3ebf-a7fe-9e6bff83b5cd | -13.0701 | -47.83709 | 2025-10-08 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c21e4ad4-ee44-31e2-a7ca-6b746f04676e | -11.13681 | -54.88338 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d388766-c6f4-3e39-b8f1-467359956866 | -11.72917 | -50.93463 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 511a79d4-cdff-38df-9f74-d3262bc87c17 | -17.48672 | -43.33605 | 2025-10-08 04:40:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d19fecfa-0a95-3768-bb2e-fae68b33d60d | -11.74742 | -50.92678 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 50931221-05b5-3dc0-a651-143772b81ed8 | -14.90573 | -46.82486 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c36dbfa5-e580-3dc2-9ee2-d956b394f875 | -14.36342 | -45.23645 | 2025-10-08 04:40:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42b24962-8e6f-323a-8e20-b660c6d20210 | -11.1439 | -54.88296 | 2025-10-08 04:40:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f5da6ea8-10a8-3d25-9e90-1779c0526a4b | -11.74574 | -50.93735 | 2025-10-08 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5de7f433-6348-3645-83a7-4279d92976cf | -11.90599 | -46.74963 | 2025-10-08 04:40:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9f5606b-3ba3-36da-a8d8-4b46cf43f31c | -13.3377 | -47.56045 | 2025-10-08 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 49d54b27-440c-30b2-a03a-f03c1e69d822 | -15.30882 | -46.16962 | 2025-10-08 04:40:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cf079271-cd7d-3b7a-b0c1-0e5eccb7150c | -14.93851 | -46.79808 | 2025-10-08 04:40:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 42e45c02-03a1-38d7-9230-18d46fdf49eb | -12.24132 | -47.87706 | 2025-10-08 04:40:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 383b6852-76ce-3ed5-8383-054897ab945a | -14.79515 | -41.63241 | 2025-10-08 04:40:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README81.md)
