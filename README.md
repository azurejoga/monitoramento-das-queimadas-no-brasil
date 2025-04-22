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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1debe32-b861-3e5d-999e-d45e24078f1c | -9.5734 | -37.035999 | 2025-04-22 00:01:00 | METOP-C | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| c0482251-64f3-3bb1-a7a3-7bce8742f858 | -10.6233 | -44.417 | 2025-04-22 00:01:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 85915eca-a896-3e21-aafc-43d55785cf87 | -10.6202 | -44.401798 | 2025-04-22 00:01:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 79be07ad-9fce-31cf-8e3a-3add5c0afbbd | -9.6734 | -36.976898 | 2025-04-22 00:01:00 | METOP-C | JARAMATAIA | ALAGOAS | Brasil | 2703700 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 9de3e9fd-1944-3624-b0fb-c31f665f4e50 | -9.562 | -37.0313 | 2025-04-22 00:01:00 | METOP-C | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| cab82af1-5118-3b70-9dc9-bfd95a7b36b4 | -9.575 | -37.0429 | 2025-04-22 00:01:00 | METOP-C | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 556930f5-015e-327a-a3ed-2c54ac46dce1 | -13.0814 | -53.253899 | 2025-04-22 00:48:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c98f46f0-e043-30b7-87dd-f4d9c676df0d | -5.4177 | -43.1986 | 2025-04-22 00:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 741513c8-7fbc-334c-b923-2cb9263e3f3e | -5.4177 | -43.1986 | 2025-04-22 01:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| f9b526d7-b0b9-36e5-9b27-14406da4c8d1 | -14.65729 | -50.19167 | 2025-04-22 01:07:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d1337301-c78c-355d-bdba-b08a5c4c92f6 | -18.49924 | -49.8349 | 2025-04-22 01:07:00 | TERRA_M-M | INACIOLÂNDIA | GOIÁS | Brasil | 5209937 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b332d312-723f-3694-b4d8-2f3afe6a8e79 | -13.13208 | -53.25311 | 2025-04-22 01:09:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 464cfce8-811c-30ca-abf6-50f438a63e84 | -9.6196 | -37.03269 | 2025-04-22 03:15:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bca8e28b-c7be-3097-93d0-8c2a289fc78b | -10.2558 | -36.44927 | 2025-04-22 03:17:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 593c941e-9a00-36db-8615-cb1340d8fcae | -10.25499 | -36.44626 | 2025-04-22 03:17:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1cdfad2f-60cc-3090-9b70-418b305fd12a | -10.6961 | -37.05078 | 2025-04-22 03:17:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| da2e22cf-bc13-3037-b55a-a6ddc8876b77 | -20.34893 | -40.36069 | 2025-04-22 03:19:00 | NOAA-21 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 521d2c60-f7b5-3608-a32b-548e3c467ab4 | -5.16875 | -35.88739 | 2025-04-22 03:42:00 | NPP-375D | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 767cced0-28ee-3bc1-8421-ed17c04403a8 | -12.41571 | -39.14542 | 2025-04-22 03:45:00 | NPP-375D | ANTÔNIO CARDOSO | BAHIA | Brasil | 2901700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 42c9651a-99ac-310b-bc1c-a9cc97eac131 | -9.03004 | -36.66618 | 2025-04-22 03:45:00 | NPP-375D | TEREZINHA | PERNAMBUCO | Brasil | 2615102 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e158c9ca-1997-3fd0-8ace-8a39fd970aa4 | -7.615 | -39.06358 | 2025-04-22 03:45:00 | NPP-375D | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8a2dc49c-6c54-3d44-86e5-0dac2baa92b2 | -7.56702 | -45.84505 | 2025-04-22 03:45:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 19ca9519-0d65-3c22-a049-af2cb488b693 | -9.7115 | -36.72575 | 2025-04-22 03:45:00 | NPP-375D | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1b785516-03e4-3187-bc9d-431b291ae8c4 | -11.5827 | -47.62337 | 2025-04-22 03:45:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 682782a9-130a-3081-88e0-309a74bfc9a7 | -7.56774 | -45.84109 | 2025-04-22 03:45:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c18994fd-c359-3da0-9968-1db16cfd0c41 | -9.71864 | -36.9716 | 2025-04-22 03:45:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 91df453e-6195-38d1-b45a-61e581d30676 | -9.61138 | -37.02777 | 2025-04-22 03:45:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ae1f8ab6-5cd5-3013-9374-62f59ffca608 | -9.61753 | -37.03247 | 2025-04-22 03:45:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8e28fb38-7e81-3af2-b47e-b02308c466e5 | -11.57579 | -47.62649 | 2025-04-22 03:45:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4dbbf7a-3686-38f5-8ae9-107084aeb296 | -12.07819 | -40.03498 | 2025-04-22 03:45:00 | NPP-375D | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 07231339-737f-3a75-8830-f6e42bb99daf | -7.56846 | -45.83721 | 2025-04-22 03:45:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b951d40a-01cd-3007-8690-46c937d13bf0 | -10.21158 | -40.51435 | 2025-04-22 03:45:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7fb81977-effb-3881-81d7-2c19751de065 | -10.25296 | -36.44784 | 2025-04-22 03:45:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 45f5a603-8bc4-3f95-8fa8-860e05c2e25a | -23.98404 | -48.91811 | 2025-04-22 03:47:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e24c92a-35ee-3c00-b050-4ca931ce84dc | -17.26993 | -49.01133 | 2025-04-22 03:47:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3209196-c0d7-36c8-9202-935034119345 | -15.26184 | -47.46005 | 2025-04-22 03:47:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7065602d-5a96-37e5-9cde-b3cb8ce54c98 | -17.59453 | -43.19849 | 2025-04-22 03:47:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d298de62-753b-3f16-a6ea-bc99cdadb674 | -16.34868 | -43.69758 | 2025-04-22 03:47:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98b3856b-26a1-314e-bdda-1fc0e7d46cda | -16.68089 | -43.88216 | 2025-04-22 03:47:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b705d5d2-1cd2-36da-8e45-c75b971c6849 | -15.25626 | -47.45885 | 2025-04-22 03:47:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7f50374d-8df9-3730-bf65-05fffabfba0d | -17.09439 | -43.80329 | 2025-04-22 03:47:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68e3c8b9-394e-30c6-9b67-b70b04aac499 | -15.25549 | -47.46262 | 2025-04-22 03:47:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 834fa22b-3c18-3d80-ab15-2e334910e5c0 | -17.26402 | -49.01 | 2025-04-22 03:47:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6c039646-0a12-32a9-a44b-2c3991d0c7bf | -18.23673 | -48.19978 | 2025-04-22 03:47:00 | NPP-375D | CUMARI | GOIÁS | Brasil | 5206602 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| adea7f6e-a435-319d-a076-8267a27b6d9c | -14.98818 | -44.46088 | 2025-04-22 03:47:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f22ae6e5-0329-3683-81ce-262421d32ad7 | -20.25643 | -49.67611 | 2025-04-22 03:47:00 | NPP-375D | AMÉRICO DE CAMPOS | SÃO PAULO | Brasil | 3501806 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d5c30a9-84f8-3a43-8844-1d7f98610d14 | -19.43774 | -44.34109 | 2025-04-22 03:47:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 67656d48-9df2-3f98-bf02-e447f01afd13 | -16.68013 | -43.88618 | 2025-04-22 03:47:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7639a165-d9c1-3b6e-bda9-9339012d0b03 | -21.22447 | -48.61349 | 2025-04-22 03:49:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 63e82808-2a58-3195-b3ff-c3cd3ca06239 | -23.33785 | -46.77346 | 2025-04-22 03:49:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| eae3e842-42e7-3a69-99a4-bb0b0c170f5a | -21.67118 | -49.0549 | 2025-04-22 03:49:00 | NPP-375D | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef71bc69-7b60-3c67-bbcb-380886ba58e0 | -21.21914 | -48.61217 | 2025-04-22 03:49:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 21b4cd7e-ec7d-34f8-aea6-59615cbef1c3 | -23.33625 | -46.77528 | 2025-04-22 03:49:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2ba8db50-e4ed-3a2e-af9c-7f0ab3d1624e | -21.67036 | -49.05856 | 2025-04-22 03:49:00 | NPP-375D | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47212874-d59b-37e8-8981-eb798227196a | -5.67669 | -45.21464 | 2025-04-22 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e431e7b3-bfe4-3608-9b9d-8a1751de987a | -7.5678 | -45.83598 | 2025-04-22 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85ccda25-a27f-30a7-9dcb-0371847dcca4 | -7.56399 | -45.83532 | 2025-04-22 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1c057ab-1d94-3bc7-a346-f3dddb7f0700 | -10.96163 | -45.1093 | 2025-04-22 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40413d5f-7468-3021-8600-5d25e2bde16c | -9.61911 | -37.03079 | 2025-04-22 04:06:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 19a6f688-1d70-3f49-9cda-de49c0594a30 | -7.56624 | -45.84529 | 2025-04-22 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95d3a4d0-530d-3bfa-9b08-eef28cf824d3 | -10.21277 | -40.51179 | 2025-04-22 04:06:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 554b6a1d-1df3-39da-9bb3-3cd31f5e3f89 | -7.56702 | -45.84061 | 2025-04-22 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b826aeb9-8fd1-397c-965b-e6bbd21e2c74 | -11.58098 | -47.6213 | 2025-04-22 04:06:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a638d030-51b6-32f6-99bd-e884fa3b7141 | -9.02839 | -36.66514 | 2025-04-22 04:06:00 | NOAA-20 | TEREZINHA | PERNAMBUCO | Brasil | 2615102 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e824b04f-0a77-3355-8208-7e492fc9a5bb | -11.57174 | -47.62683 | 2025-04-22 04:06:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4c462e1-132f-3e21-b1c9-237b19ebf7df | -7.56321 | -45.83997 | 2025-04-22 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42e028d1-c8ea-3f6d-a283-7b2376c579f2 | -11.57574 | -47.62757 | 2025-04-22 04:06:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5149acc-62f1-3434-95fc-2d78e8db0986 | -9.32712 | -37.79419 | 2025-04-22 04:06:00 | NOAA-20 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d8138908-2d90-3c73-963e-65fd9b4e43bc | -10.96515 | -45.10989 | 2025-04-22 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dabcf502-26de-311b-ac86-fa78d8a0abda | -14.98743 | -44.46087 | 2025-04-22 04:08:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6031df7-093d-30a8-980b-9aa501e52fb7 | -11.26853 | -52.4623 | 2025-04-22 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb2e38e3-cbe3-30ea-aeb9-0a79e5a132fa | -16.34936 | -43.69703 | 2025-04-22 04:08:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 174dcd56-5d4d-39a3-b73f-6416dcca2d95 | -15.07641 | -48.9449 | 2025-04-22 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2da11b80-a1c9-3cf3-89dd-e6bd7e6786cb | -15.25705 | -47.45507 | 2025-04-22 04:08:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 66c8a81a-00f6-3a3b-b598-32bea24f554b | -11.26924 | -52.45859 | 2025-04-22 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd5415bb-5829-3022-9d46-de1038140b01 | -11.27547 | -52.45598 | 2025-04-22 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2afe8886-378a-3954-bdd2-a7fabc49868e | -15.25999 | -47.46039 | 2025-04-22 04:08:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2f3769d0-85ef-3e82-944e-47372b99e860 | -17.09323 | -43.80355 | 2025-04-22 04:08:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44e7645e-9de5-350e-a8a7-e726662320b2 | -11.26081 | -52.47257 | 2025-04-22 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4f5c4b3-6f21-3174-a043-2f002832b50b | -19.05343 | -44.35854 | 2025-04-22 04:08:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 04fc4625-8d91-3775-b358-5adcc00d14e2 | -18.23402 | -48.19825 | 2025-04-22 04:08:00 | NOAA-20 | CUMARI | GOIÁS | Brasil | 5206602 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b5cb18d-d41a-31d8-add1-ea65d9068545 | -15.25625 | -47.45969 | 2025-04-22 04:08:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ef013357-ea7c-3b8c-a580-8f941afcaea6 | -15.56719 | -47.85582 | 2025-04-22 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14dff26b-a4ae-35ab-b074-6e3f5b50b76c | -17.26737 | -49.00933 | 2025-04-22 04:08:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bf68066b-6f1f-30df-a25d-93076237df8d | -17.00845 | -49.78149 | 2025-04-22 04:08:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c750431-b441-37e1-b23e-efd25ac22e5d | -19.70511 | -44.7669 | 2025-04-22 04:08:00 | NOAA-20 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5b1ef67b-6748-37c9-a5c0-faa4033b8cbd | -11.27476 | -52.45971 | 2025-04-22 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f2faf04-48cd-3f3d-b694-49b3f9e2a464 | -16.67981 | -43.88492 | 2025-04-22 04:08:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71cec428-5b56-3df7-8dc5-f5636dace9bd | -11.25526 | -52.47155 | 2025-04-22 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad641997-b5ce-3d46-9d57-777ed34279fe | -13.13337 | -53.25193 | 2025-04-22 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6593dbbf-6615-3f22-bf84-e7cf695b3d06 | -20.9971 | -51.79222 | 2025-04-22 04:10:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e04b4f64-682d-3756-8a67-b3ea1c17b50e | -22.9207 | -47.09749 | 2025-04-22 04:10:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 11bdb26a-4c9a-3c36-8233-2e197861aead | -22.53889 | -48.81211 | 2025-04-22 04:10:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f615a0c5-bbd4-38f5-aece-021888ce72f1 | -21.67027 | -49.05431 | 2025-04-22 04:10:00 | NOAA-20 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 42310d0f-945a-3d42-b345-7b5bf0fad3c8 | -23.06076 | -46.64142 | 2025-04-22 04:10:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 658e9c3c-7fb7-30c0-ab52-af438f1fd445 | -21.9121 | -42.264 | 2025-04-22 04:10:00 | NOAA-20 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d4fe847e-fbe1-33d5-86e6-437c54799b4a | -23.59382 | -47.43723 | 2025-04-22 04:10:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d0b1efdc-85db-3ac0-80ff-a91890892fdf | -21.19614 | -44.93658 | 2025-04-22 04:10:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d04da4cb-65b8-3ef4-a91f-911a01ba3db0 | -20.25661 | -49.67647 | 2025-04-22 04:10:00 | NOAA-20 | AMÉRICO DE CAMPOS | SÃO PAULO | Brasil | 3501806 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c9531c6-407a-3296-8922-4c17e3ad1526 | -23.52036 | -46.9758 | 2025-04-22 04:10:00 | NOAA-20 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README2.md)
