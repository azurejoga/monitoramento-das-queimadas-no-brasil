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
| 6b8da2af-56d5-362d-971f-5ee07b2e5414 | -5.16454 | -45.10875 | 2025-04-10 04:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 942bd1b3-5bca-344a-8b9d-63936a732598 | -9.91378 | -37.08742 | 2025-04-10 04:08:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4df45015-0ca6-3e68-ab4d-0e0976e54289 | -8.09984 | -43.12529 | 2025-04-10 04:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 2d99b085-df00-3354-8b16-89456d2bb506 | -6.23218 | -43.37793 | 2025-04-10 04:08:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d112659e-dc80-3137-94e0-048373003543 | -10.97835 | -38.27088 | 2025-04-10 04:08:00 | NPP-375D | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 24b8b46e-875a-3c58-8c3e-12cc7bc964a2 | -6.69365 | -42.1352 | 2025-04-10 04:08:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9f5757f2-33c8-3fce-9c71-4e6debf6958c | -5.93344 | -44.35358 | 2025-04-10 04:08:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f3f7fa5-61b9-32e0-9d50-574002798013 | -9.62721 | -36.81448 | 2025-04-10 04:08:00 | NPP-375D | CRAÍBAS | ALAGOAS | Brasil | 2702355 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 006b11ee-eaeb-3548-b62b-f026ea378107 | -7.24958 | -44.7782 | 2025-04-10 04:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e591f9e6-129b-34ea-bf82-87e6a45c492e | -7.43614 | -45.42481 | 2025-04-10 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| effd4eab-331a-3f3e-952d-f8b131f5b592 | -10.53604 | -44.66728 | 2025-04-10 04:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e2cfd7a-656f-3fec-87e4-1005fea2ccab | -10.54016 | -44.66401 | 2025-04-10 04:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d8de9da-ee70-39f7-8156-361c95f6851f | -6.66477 | -47.59673 | 2025-04-10 04:08:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14cebc5c-a951-3e22-b57b-181ec5c2af18 | -7.07567 | -45.21766 | 2025-04-10 04:08:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36ee7d3c-8e31-3cdf-a977-676f1571ead4 | -9.9143 | -37.08386 | 2025-04-10 04:08:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a43bec5a-6bbb-3194-9204-557ee9c89b50 | -6.23562 | -43.37848 | 2025-04-10 04:08:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8129eccd-3254-35ca-bc1e-8502ac788d4e | -7.07097 | -44.37777 | 2025-04-10 04:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e69a25a-b55d-3ee1-9229-c11545b005a2 | -10.62106 | -40.50943 | 2025-04-10 04:08:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6e2727ab-54eb-322a-bea4-6ca41a931ba3 | -6.6794 | -41.71582 | 2025-04-10 04:08:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 88756a63-ae94-3f29-afdf-c1ad4f154ae9 | -7.48859 | -41.25935 | 2025-04-10 04:08:00 | NPP-375D | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3dfaa5d7-be38-3976-83f3-2866bcde5c79 | -10.14881 | -47.65847 | 2025-04-10 04:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95885a8d-f16e-3b14-8175-c505ab1f14a9 | -10.98219 | -38.27147 | 2025-04-10 04:08:00 | NPP-375D | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ef81f641-0d29-343a-9cf9-8fbd0b4ea69e | -6.67885 | -41.71929 | 2025-04-10 04:08:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a71858f1-e01b-3d7c-a63c-042dc49bed65 | -9.61597 | -37.02732 | 2025-04-10 04:08:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 65ff3ec9-baf6-317d-a561-c0628d4cc1b4 | -8.11784 | -43.12082 | 2025-04-10 04:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| bc84fe00-1b6f-34e6-b751-6448f9e9bb28 | -8.37434 | -41.8241 | 2025-04-10 04:08:00 | NPP-375D | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c06cf702-1c1f-3550-8ad0-95332f2e630b | -7.24528 | -44.78177 | 2025-04-10 04:08:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84dc1198-0461-35c3-82d6-0bfaf925589d | -8.11447 | -43.12027 | 2025-04-10 04:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 01f0a96d-4a6c-3293-850c-029188959e3e | -8.10378 | -43.12224 | 2025-04-10 04:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| f330a157-e1d8-3e43-b8de-b96de542e5b9 | -6.68217 | -41.71981 | 2025-04-10 04:08:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a54821e8-a8b7-332c-af62-3ac3bf2bb596 | -5.63262 | -44.32088 | 2025-04-10 04:08:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f6ab509-9966-32c1-a5b5-c135b38e06f1 | -12.36038 | -39.09497 | 2025-04-10 04:10:00 | NPP-375D | ANTÔNIO CARDOSO | BAHIA | Brasil | 2901700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cec7289d-a877-3fab-80d8-207beaf0210d | -11.27431 | -52.4546 | 2025-04-10 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aeedc243-d049-395d-a64c-3b82443622cd | -11.6963 | -44.6241 | 2025-04-10 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d047d63-a533-3405-89e3-46e0d518e453 | -13.02186 | -45.06517 | 2025-04-10 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 785f5168-3e7d-3210-ab1d-834901a36e79 | -15.65494 | -39.18676 | 2025-04-10 04:10:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2d3763fa-6a3b-321c-b46d-d1464c122ddb | -16.42112 | -42.51471 | 2025-04-10 04:10:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d43dbe8-9720-3578-aa73-f1c111ffee6e | -11.27359 | -52.45828 | 2025-04-10 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fc76abf-ed52-3d7b-ad12-2733d3963f0a | -11.27452 | -52.45665 | 2025-04-10 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57996f1e-92dd-3168-af3e-df62afba510b | -14.8867 | -42.26871 | 2025-04-10 04:10:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| dffb2254-e563-3159-a227-4ed3658afc6e | -13.28971 | -39.86687 | 2025-04-10 04:10:00 | NPP-375D | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d44cfae5-8fca-3b6a-82bd-5fb2daf986f0 | -11.27983 | -52.4557 | 2025-04-10 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7eefc4e-784d-3654-94cc-9ac8a8f561e7 | -11.57793 | -47.63572 | 2025-04-10 04:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74a6286f-c02f-373a-b7a3-146ccf857149 | -13.02337 | -45.06595 | 2025-04-10 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9de88d8d-5239-3873-a1fc-84f1b9f241de | -12.43612 | -39.24181 | 2025-04-10 04:10:00 | NPP-375D | SANTO ESTÊVÃO | BAHIA | Brasil | 2928802 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 58cd6651-fa5c-379d-8b08-40befca8ef11 | -12.40343 | -39.24325 | 2025-04-10 04:10:00 | NPP-375D | SANTO ESTÊVÃO | BAHIA | Brasil | 2928802 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f5120848-8706-3642-ba24-749c48065313 | -16.61311 | -43.33231 | 2025-04-10 04:10:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 10703221-4231-3384-ada8-f4c3049ee94e | -11.26899 | -52.45555 | 2025-04-10 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5eed60c-b344-3ed6-bd8f-ba229b69f95b | -16.61367 | -43.32869 | 2025-04-10 04:10:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d6725612-f4b9-30aa-b4f9-4e4117fa7e99 | -11.40336 | -52.95766 | 2025-04-10 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74e0de99-09f1-3ced-9d51-f787e3ee92fa | -16.09397 | -42.28439 | 2025-04-10 04:10:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6ae10f3a-4408-3047-91ab-75456694a045 | -13.02553 | -45.08556 | 2025-04-10 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7527decc-024c-327e-8539-8efc75db9f1d | -16.35012 | -43.69546 | 2025-04-10 04:10:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f00c4b4-4cfc-377f-8267-b5172af58b40 | -15.7106 | -42.25918 | 2025-04-10 04:10:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 862085a0-7353-3107-9ab6-de4f50d16442 | -16.61034 | -43.32813 | 2025-04-10 04:10:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cec181c0-7731-38d0-bd16-011c4936a4ce | -15.65331 | -39.18983 | 2025-04-10 04:10:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ae21844d-dccb-33ef-a2d8-b86ac29a61aa | -12.62819 | -48.14815 | 2025-04-10 04:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67ca10a8-8d0b-3c77-9555-3f2d76b87d25 | -13.02106 | -44.03153 | 2025-04-10 04:10:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d988238f-5e30-3bac-8f40-46c02e9f8f7c | -14.88334 | -42.26817 | 2025-04-10 04:10:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4587b8aa-f48f-3956-a5cd-67663b3949d3 | -11.39659 | -52.9539 | 2025-04-10 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f29c05c0-0bcc-3929-b7b8-64480ef52284 | -11.39768 | -52.95642 | 2025-04-10 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c9f4e015-4d69-3bc8-9702-280d088c805b | -11.39848 | -52.95238 | 2025-04-10 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7b6eb76a-5ed5-39f9-9e37-9e38056e6c6b | -11.26829 | -52.45924 | 2025-04-10 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edefc104-3d7d-3c06-b94b-0864e4dcd6bb | -13.89231 | -44.01849 | 2025-04-10 04:10:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b60a52d-9870-387a-82f4-e4e984ad1fd0 | -22.21174 | -49.85217 | 2025-04-10 04:12:00 | NPP-375D | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 0b1d8794-9b61-3412-880b-e34be96a7dd3 | -20.58638 | -56.05181 | 2025-04-10 04:12:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 60b3abf2-80e0-35b6-9974-a68e386f9b0e | -21.09331 | -48.69573 | 2025-04-10 04:12:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 37e7c6f5-5dea-3258-aeff-c677a1088174 | -20.98433 | -43.03162 | 2025-04-10 04:12:00 | NPP-375D | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7ad76aae-1a78-346a-ade7-6336bebf620f | -22.26012 | -53.17727 | 2025-04-10 04:12:00 | NPP-375D | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0db682c8-f428-3217-81f1-976f03febc0c | -23.59314 | -47.43975 | 2025-04-10 04:12:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a570b8dd-0b88-38ae-af8f-e8b64cbcc75e | -20.99123 | -43.0086 | 2025-04-10 04:12:00 | NPP-375D | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3df6d15f-380d-353e-8363-e1be7414cc63 | -20.59212 | -56.05342 | 2025-04-10 04:12:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab244a49-ac36-3073-ba20-70353f068461 | -20.98375 | -43.03557 | 2025-04-10 04:12:00 | NPP-375D | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ba65423c-7008-3cfb-8602-77aa4ba65af1 | -22.20789 | -49.85134 | 2025-04-10 04:12:00 | NPP-375D | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f60c02f8-6071-3a22-b7b1-ed613da03389 | -22.26073 | -53.1742 | 2025-04-10 04:12:00 | NPP-375D | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2b93e330-afff-3877-aa26-83313c9a99a0 | -5.16494 | -45.109 | 2025-04-10 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5296e56d-a953-318a-9340-33fd330d525e | -6.23141 | -43.37438 | 2025-04-10 04:29:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ca1ac820-5a57-3163-aabd-8bb994a136da | -6.69639 | -42.13608 | 2025-04-10 04:29:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8bf502a1-7a63-3610-bb2b-dcd76fdd2413 | -6.19391 | -48.04352 | 2025-04-10 04:29:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd7773af-7764-37e2-aac1-35dccba9d45f | -6.23377 | -43.37205 | 2025-04-10 04:29:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a70e55c7-9c91-34bf-8032-52bbfee11aa6 | -6.23525 | -43.37494 | 2025-04-10 04:29:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0b702ea0-b0ab-383d-a589-a6f4ae803a7d | -8.11514 | -43.12102 | 2025-04-10 04:29:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| a8a33e66-53ea-3580-b0eb-29d057df0305 | -5.63 | -44.32072 | 2025-04-10 04:29:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3b36a49-98dd-3b2b-886e-b76b3acefcb1 | -6.59259 | -44.78305 | 2025-04-10 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6242753e-1658-3ba5-b90c-2dc5371fe484 | -7.07602 | -45.21958 | 2025-04-10 04:29:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 249c2f6b-267b-3751-96f3-c40a082e7697 | -7.24736 | -44.77763 | 2025-04-10 04:29:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f0e143d-bb56-3df3-9b4b-b55f1824f243 | -8.11564 | -43.1175 | 2025-04-10 04:29:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 41e0a46e-3981-3cac-98bf-6ed986786529 | -6.60039 | -44.18264 | 2025-04-10 04:29:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5800569c-3d3b-339e-8b12-064254629842 | -8.37277 | -41.8254 | 2025-04-10 04:29:00 | NOAA-20 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a41a6726-ba16-358e-9ad2-b4b24b6c5605 | -6.28936 | -43.39458 | 2025-04-10 04:29:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc923e2d-e0b3-30ce-adc2-9aede905be52 | -8.10034 | -43.12644 | 2025-04-10 04:29:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 577c4817-8ed7-38ff-a599-3e2dce62c397 | -7.43496 | -45.42409 | 2025-04-10 04:29:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40b15b90-b54c-3974-8dfa-2ccbd86719af | -8.10262 | -43.1227 | 2025-04-10 04:29:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| ec765cb3-5054-30d7-a61c-d861bddaf318 | -7.24674 | -44.7818 | 2025-04-10 04:29:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a792695-622f-352d-878c-63a9f5f90bcf | -6.68074 | -41.71768 | 2025-04-10 04:29:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3a8247d2-454e-393c-9ad1-68c5f86ff569 | -6.6651 | -47.5974 | 2025-04-10 04:29:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 807ef947-b336-3fc2-bac4-018792774601 | -7.07167 | -44.37753 | 2025-04-10 04:29:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e41c099-d218-3f74-ae5b-e1166da975d7 | -7.079 | -44.3786 | 2025-04-10 04:29:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02e6acb5-ecaa-38bb-9601-31ed8befa38b | -5.93537 | -44.35369 | 2025-04-10 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29f43768-c4fb-3836-bdf6-88b37cc0d734 | -7.43606 | -45.42336 | 2025-04-10 04:29:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README3.md)
