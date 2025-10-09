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
| 8bffdccd-5e84-3cdf-957f-245b42d749cd | -13.3913 | -42.70035 | 2025-10-09 04:00:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| bcd37d33-673a-3360-8754-6be38be02483 | -15.74968 | -48.72547 | 2025-10-09 04:00:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bfb450a4-9f82-3e7d-b959-7a9a07c033f7 | -15.3825 | -47.30415 | 2025-10-09 04:00:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f1ebb73-1a11-3ba4-8924-b026a8a3becf | -15.78244 | -46.24572 | 2025-10-09 04:00:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b1572b9-0f67-3a16-beac-d1a349c16661 | -11.87347 | -45.53452 | 2025-10-09 04:00:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c321a9c-b512-31c3-b564-ee8bc22b2097 | -11.86473 | -44.924 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2e6d2a1-b7fd-3be7-898f-988c796add18 | -13.33834 | -43.07469 | 2025-10-09 04:00:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| df9be632-b777-3947-a2c7-480af2143943 | -15.49738 | -45.34803 | 2025-10-09 04:00:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| adee02f9-c3e1-38a7-9c1a-630b74fad622 | -11.98296 | -45.21399 | 2025-10-09 04:00:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9390c6c-e2a8-35fc-8c0b-346149e7cadb | -11.79245 | -45.04493 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71725c80-dbce-33b0-862a-d2027ac530cf | -11.24442 | -40.33612 | 2025-10-09 04:00:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| adf4a44b-cd2e-369b-95f4-ecf9fab6424a | -11.24107 | -40.33558 | 2025-10-09 04:00:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3e814912-2356-3ab1-b96d-56a3bd01c519 | -11.06031 | -40.9366 | 2025-10-09 04:00:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 46e6674d-c816-3cda-ad8f-57c5bdb85a75 | -10.79972 | -44.08242 | 2025-10-09 04:00:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67ebe135-82a3-32dc-b0b7-fad7b3c62462 | -12.06667 | -45.74008 | 2025-10-09 04:00:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08607f67-1099-3c1c-839b-366ab9afab82 | -13.82318 | -45.81985 | 2025-10-09 04:00:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5e290ce6-58f0-355e-b9d5-b5d79ccc4152 | -15.75111 | -49.0022 | 2025-10-09 04:00:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3af1871e-26ad-35be-85f2-efebfc7eceb0 | -15.071 | -46.61544 | 2025-10-09 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a985c261-533b-36c5-b229-d09ba55562c5 | -14.4241 | -43.98147 | 2025-10-09 04:00:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d5f78a9-56ee-3420-b491-48f026c03da9 | -15.06539 | -48.07559 | 2025-10-09 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 250fbec1-f09b-32db-be14-f79ab0ee6dc6 | -11.86992 | -45.5298 | 2025-10-09 04:00:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fcadce5f-4dcc-34b4-b0be-56d1aaa9b869 | -11.78769 | -45.04777 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 703db4a0-58c8-39c3-a463-e6acd039dd13 | -10.55567 | -50.04313 | 2025-10-09 04:00:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f28e7ec9-3a29-3b47-b9b5-fa8a6a277277 | -10.55595 | -51.46097 | 2025-10-09 04:00:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 013f7f2a-f518-3f70-b6fd-d0abee7dc128 | -13.78353 | -44.34609 | 2025-10-09 04:00:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4194b63e-40a5-352e-8e9d-4afc0a5e6bab | -13.82955 | -45.80873 | 2025-10-09 04:00:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b80cd31-ab32-354c-a1ca-21ada3774276 | -11.78297 | -45.05033 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ade61299-71f7-39d8-ac00-749dfa87376f | -13.93742 | -42.35458 | 2025-10-09 04:00:00 | NPP-375D | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 025e25b0-ff4c-3c46-be5c-cde6f03d2db9 | -10.3562 | -50.21631 | 2025-10-09 04:00:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3df8c29-6069-3545-aa10-0e2197335ef3 | -13.79228 | -45.84604 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4509e3f9-6304-348c-ab86-d9e5cf0d4cd2 | -12.42468 | -45.71473 | 2025-10-09 04:00:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6a7c6a3a-2477-3a85-a035-8f0fa511a575 | -15.74857 | -48.72441 | 2025-10-09 04:00:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 82e1cf8c-6ca2-3817-bbc9-118088532851 | -15.08145 | -46.6074 | 2025-10-09 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 048d3275-2eec-3029-ad4c-90c86c5140f1 | -13.81609 | -45.83486 | 2025-10-09 04:00:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 593635e0-d0ae-30dc-bbea-fb2da972e97e | -13.79939 | -45.83142 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5c07220-fb2e-3858-adc2-b888454dae57 | -14.91155 | -46.81516 | 2025-10-09 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 09c4c323-8127-377c-80ca-6ae81c6522a7 | -14.79312 | -46.08477 | 2025-10-09 04:00:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1bcd82a-3d80-3799-8e06-107f33dab8c5 | -11.66106 | -47.53201 | 2025-10-09 04:00:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3f16458e-15d4-3e7a-aee4-d707b2019a58 | -13.79289 | -45.86648 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90b7a2c2-013c-39ec-be24-d0f2030e5ebf | -11.24328 | -40.3432 | 2025-10-09 04:00:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 77cb8897-b642-3707-8621-8191c1ae56c9 | -10.35029 | -50.21509 | 2025-10-09 04:00:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d70dbfb-117d-33a1-9dfd-072f4b37b2a4 | -13.81263 | -45.83015 | 2025-10-09 04:00:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33a6d18f-ebd0-3efb-a323-00f1da904f46 | -11.66744 | -47.53533 | 2025-10-09 04:00:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 302d4b7a-dfec-3131-ad97-73b3cb8225c1 | -11.24997 | -40.3443 | 2025-10-09 04:00:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a2df83cb-53c5-30aa-9219-e8b697703cb7 | -14.73154 | -46.0895 | 2025-10-09 04:00:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f03e2ad-ed89-3ec1-83f5-9f25266c519a | -14.77966 | -46.11092 | 2025-10-09 04:00:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d58e0fd1-2305-3844-8c38-6f700b4ab090 | -13.8014 | -45.84401 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 222e98c4-c411-3e4e-9a68-ff43e43b296f | -11.65413 | -47.54241 | 2025-10-09 04:00:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 463824dd-8b80-3c16-bcfd-c74f12ba9dd9 | -15.40349 | -46.27838 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e9917cac-7141-3eb8-9e31-2784a1885be1 | -11.13429 | -47.74616 | 2025-10-09 04:00:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 73b7e2c3-0adb-39df-b512-fa015c86a49b | -14.73573 | -46.09028 | 2025-10-09 04:00:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16e304bb-3a0b-39b1-bf7e-48470404ab71 | -12.42541 | -45.71072 | 2025-10-09 04:00:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 4176c425-bf8c-3be0-9664-8e02686210d6 | -11.75122 | -45.14732 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2a26701-e21e-38f4-9ef5-f699285bfa07 | -11.66488 | -44.25364 | 2025-10-09 04:00:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22876b00-04ea-3d3d-8ffa-f3ad1ec154ce | -11.24271 | -40.34673 | 2025-10-09 04:00:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 017d9dc6-c7f6-3bb0-93ea-06668e8e107f | -16.38014 | -46.3695 | 2025-10-09 04:00:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b03f61ba-dae2-3ce6-a40b-8893a7a06ec0 | -13.79368 | -45.86252 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46b09562-1664-3e70-9ea0-60344ea70995 | -15.05872 | -42.33326 | 2025-10-09 04:00:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| d89559fe-cf53-3fd3-b434-c1caeb5a87b7 | -15.06969 | -46.61718 | 2025-10-09 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9e3a068-d91e-3e17-83e4-cc29ed8db7c7 | -10.53112 | -50.02333 | 2025-10-09 04:00:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 45041c44-79ea-3b52-9c3a-0423be4de5b8 | -15.63724 | -46.44744 | 2025-10-09 04:00:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7a99542-fcfe-3840-b2ab-bb11cc091165 | -13.79924 | -45.83126 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c25d9ea7-6635-3eb0-b43d-5ba18aed4737 | -10.86849 | -44.28734 | 2025-10-09 04:00:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fcc6bd37-452c-38fa-83d5-f3756056a9f1 | -13.81989 | -45.79075 | 2025-10-09 04:00:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24e64eb0-b213-3e77-a08a-2032e12eed67 | -11.23715 | -40.33859 | 2025-10-09 04:00:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bdb2c19c-96d1-39a4-9888-f938c7f562de | -15.79738 | -39.73242 | 2025-10-09 04:00:00 | NPP-375D | ITAPEBI | BAHIA | Brasil | 2916302 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 54bf92aa-bb3b-3223-bf52-9a4897548412 | -15.47626 | -47.96517 | 2025-10-09 04:00:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 07be33a4-b45d-3403-9fef-e8a1b569ea8b | -11.51326 | -41.43787 | 2025-10-09 04:00:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 71fd34f3-5bc6-3083-80f7-1e55fbd65399 | -15.21928 | -46.38812 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 26b00c6c-b40b-33a7-9b76-0ce5ca3d79be | -10.93527 | -42.8378 | 2025-10-09 04:00:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 697af1ac-f519-3e93-bb49-0a45bc51e998 | -15.78602 | -46.24968 | 2025-10-09 04:00:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4dda946-7a0e-323d-8b08-8dfaf519e653 | -15.2292 | -46.37643 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d2c8839-9a86-316b-8bf9-68066955c704 | -14.40243 | -46.01619 | 2025-10-09 04:00:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71adce2c-9ff1-3d3b-a47d-68718719dc7e | -13.61505 | -44.43968 | 2025-10-09 04:00:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1b6687a9-889b-38a8-9433-5f25fe93325e | -15.78551 | -46.25547 | 2025-10-09 04:00:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75ceb9b2-1733-331f-a7d3-1e5adb674913 | -13.61832 | -44.43746 | 2025-10-09 04:00:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7070e744-cb77-3eca-8da6-479d24ed91e9 | -11.79737 | -41.19673 | 2025-10-09 04:00:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b52070d3-c193-3170-8a5f-4f8ad9244bb3 | -13.79089 | -45.85389 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e540cb0-2f56-3458-87ed-d8cf4b0bac58 | -15.22423 | -46.37954 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 16f424c9-3b6b-3b3b-bdd6-c438ad049c67 | -15.4796 | -46.86673 | 2025-10-09 04:00:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8b57eda-242b-3a68-8cfd-24595ac60961 | -13.48494 | -42.01979 | 2025-10-09 04:00:00 | NPP-375D | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 83e3607c-4fac-395d-8676-e5436881891a | -15.32183 | -41.73752 | 2025-10-09 04:00:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 64ff992c-fa49-3328-a84e-fca4bd46b365 | -14.41216 | -43.98396 | 2025-10-09 04:00:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6eb0f186-2396-3deb-a08b-1cd962e646f7 | -11.24499 | -40.33257 | 2025-10-09 04:00:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ae7dcca4-31f4-3d50-96fa-fb405cfce41e | -13.58455 | -48.67005 | 2025-10-09 04:00:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13f408d4-b5fa-37d7-8342-0a5ff4f94a41 | -12.22892 | -43.78327 | 2025-10-09 04:00:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bc3b0940-353c-3dc8-85a9-2e624ffb8bd8 | -12.24428 | -43.78477 | 2025-10-09 04:00:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68695f19-5dd5-3ede-a3fe-d0a12d171551 | -15.48467 | -46.8638 | 2025-10-09 04:00:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72ca4e20-63c5-3ff7-b59e-1dc070d413eb | -15.07264 | -46.60677 | 2025-10-09 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a97ac58-fec2-3fb2-96fc-c78eef1c71d5 | -14.93428 | -46.78951 | 2025-10-09 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce5ce4bc-9cc1-3a6f-9f41-663b60f7b4ff | -11.65663 | -47.53914 | 2025-10-09 04:00:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23fe4e3a-adc8-303a-8d17-84734f2cbb37 | -15.13155 | -43.67136 | 2025-10-09 04:00:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c2535136-8640-399d-bd7e-6ae83f09eaee | -13.78323 | -45.84816 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ff5346d-2329-3eac-b552-4c84a5c8f64e | -15.91152 | -44.28753 | 2025-10-09 04:00:00 | NPP-375D | LONTRA | MINAS GERAIS | Brasil | 3138658 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a083376-6db0-3918-ab2a-4cb6f7d8fafe | -13.77696 | -45.83476 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90c88815-07fd-3229-848b-7b7dce80562a | -13.79855 | -45.83517 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe1d5f5d-c73f-3483-99f1-9c8ae3f57b96 | -15.49121 | -47.96317 | 2025-10-09 04:00:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7f18046-ec24-3d04-b353-7a8ceb87b6cd | -15.06909 | -48.08199 | 2025-10-09 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c6b13e4-ba02-3061-b374-f47fe127036e | -14.41823 | -43.97105 | 2025-10-09 04:00:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 96af6c5a-311c-372f-a85b-adce84207e64 | -15.08065 | -46.61163 | 2025-10-09 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README26.md)
