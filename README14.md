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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3dced25-bca9-318f-9e59-ac9e82d73c6b | -16.52887 | -52.77454 | 2025-10-23 04:10:00 | NOAA-21 | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32950b4e-916f-3076-b929-48b7b6fed9fb | -16.08403 | -51.40814 | 2025-10-23 04:10:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b54c9993-28f9-33b8-85ee-9168c863e36d | -17.6032 | -46.60393 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac5db2bb-85db-3af0-9704-a491ec4e17e3 | -18.69357 | -47.05217 | 2025-10-23 04:10:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7c58a5a-30c6-3d1f-a833-7bbc86728828 | -17.62061 | -46.60714 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3c7fcccf-fcde-3b87-acb2-1429269ab69a | -17.60948 | -46.60923 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c17ed9d4-b120-336b-85c7-43f2d363e0e8 | -16.49972 | -49.74227 | 2025-10-23 04:10:00 | NOAA-21 | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e3d492fd-7be2-3b0f-8cf2-54238b506a4a | -19.95607 | -45.60161 | 2025-10-23 04:10:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc40cd12-2678-32e8-9e3a-025e641eecce | -19.20673 | -46.49138 | 2025-10-23 04:10:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7ddd189-3209-34c9-8214-23eaf17b8527 | -17.61434 | -46.60182 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12bf9cdc-8fdd-33eb-abea-80687e9b76ef | -18.13768 | -52.97461 | 2025-10-23 04:10:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 744f2a6b-4713-3040-b88c-585f918c74f6 | -18.23009 | -47.41685 | 2025-10-23 04:10:00 | NOAA-21 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 700639d8-0a66-3075-be83-ab793d0abcdf | -17.61234 | -48.58235 | 2025-10-23 04:10:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0a143b4-3c21-371d-8698-53777f02bdb2 | -17.59904 | -46.60729 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15372b3f-714c-3d12-bce1-90017cef8889 | -13.90713 | -48.37003 | 2025-10-23 04:10:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f10aece2-09af-3c6d-84a7-2658ebf91dd9 | -13.89751 | -48.37085 | 2025-10-23 04:10:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21ff648b-53f2-3574-80c2-e07b34dcdcdd | -17.61928 | -46.63596 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67fe0481-caf2-300d-8770-16f72a853666 | -13.79472 | -52.77517 | 2025-10-23 04:10:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5cf2396f-58e5-39bc-923a-7598588ee149 | -17.59837 | -46.63212 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60659bae-ef34-314a-8cfb-60b847511a21 | -18.71984 | -46.83358 | 2025-10-23 04:10:00 | NOAA-21 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6d4b477-3402-33f9-b804-61fbe50e99d0 | -20.26317 | -47.90783 | 2025-10-23 04:10:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ff1ea01-6ab3-3361-9638-91596b3a4996 | -17.60252 | -46.60794 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 413b5f08-949c-3d18-8345-b1a5e714341a | -19.64789 | -46.08611 | 2025-10-23 04:10:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 075888a0-a9f0-3fa8-8292-0045735074bb | -20.54308 | -46.22048 | 2025-10-23 04:10:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e283525e-af01-3757-9c1b-335ce16dcf5c | -15.5666 | -46.49538 | 2025-10-23 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6e933a96-928b-3433-939c-86b70b2dffc4 | -17.61227 | -46.61388 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77956f91-59e0-3748-a116-ec97b9f72a97 | -21.42581 | -46.58644 | 2025-10-23 04:10:00 | NOAA-21 | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9fa9ec5a-cf90-3520-a0b7-c0774f2e2405 | -17.61296 | -46.60987 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e8b471c0-d6c1-3641-8423-e91237ce6e56 | -17.61016 | -46.60522 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77ad4872-ea97-3598-85c2-de5e815fbb58 | -20.07263 | -45.49234 | 2025-10-23 04:10:00 | NOAA-21 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73527db7-e209-3678-bc87-4d05503d047e | -14.83479 | -48.31612 | 2025-10-23 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43f95a07-adc1-3341-b07d-d7bc2fb2f1f7 | -21.84491 | -43.71383 | 2025-10-23 04:10:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a65f7fd2-d5e9-3e66-a5da-aef5d8d6f37e | -15.51616 | -45.96089 | 2025-10-23 04:10:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c3629d6-a992-37e6-8b38-010d721af884 | -20.33508 | -43.8604 | 2025-10-23 04:10:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e2b95585-02af-324f-8698-0498aee86cc4 | -17.62276 | -46.6366 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e444fa3-66d8-388d-821e-6a206399fb88 | -15.58511 | -49.06532 | 2025-10-23 04:10:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| efcefefc-1ed7-3b25-9e2b-b47f4b7cd324 | -18.72399 | -46.8302 | 2025-10-23 04:10:00 | NOAA-21 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ff62ab52-e970-3cbe-b94d-2d9f42e1f078 | -19.26702 | -49.3583 | 2025-10-23 04:10:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 96eca5d6-0648-30e3-8b6e-1fb388e8712b | -19.70942 | -46.07021 | 2025-10-23 04:10:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eae68d0f-1571-3f68-baef-5595a6fd7bce | -16.30488 | -45.87629 | 2025-10-23 04:10:00 | NOAA-21 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 190cce43-df10-3281-ae2f-5fd6b5175e8f | -18.14015 | -44.46344 | 2025-10-23 04:10:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b0a1b1a-ad18-3176-8970-72e866044c35 | -20.63669 | -42.71433 | 2025-10-23 04:10:00 | NOAA-21 | PEDRA DO ANTA | MINAS GERAIS | Brasil | 3148806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 51a4c057-74b1-3cf3-bac3-c7613eb47872 | -17.60114 | -46.61597 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5dd812e8-373a-31cd-b063-f7dfbd3df01c | -17.60255 | -46.62871 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 48018165-a422-34b7-9ab7-765b7ce1b6cb | -14.20991 | -44.51835 | 2025-10-23 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 65509152-6f43-3521-a0d9-cf77deac84ff | -17.61507 | -46.61854 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 23.0 |
| a5f23907-5267-36b0-8738-04781bf696b1 | -17.60744 | -46.64214 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f51a5c76-b420-370e-8f20-168312be3a28 | -14.51812 | -46.94648 | 2025-10-23 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b919b578-a830-3b59-b96c-d41ab5d79ca9 | -19.26312 | -49.35748 | 2025-10-23 04:10:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f2b5bae8-0c8a-3108-8ebb-3f0b8c3ce3e7 | -17.606 | -46.60858 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b8e03f1d-b03c-332a-b76f-a5db9b6fbfd7 | -17.61369 | -46.6266 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 88ebf0b3-005f-34ce-a9ea-c41cb68a3844 | -17.60534 | -46.6334 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 271cea2c-3a2e-3e8d-908d-ae9790507975 | -20.93366 | -49.45386 | 2025-10-23 04:10:00 | NOAA-21 | BADY BASSITT | SÃO PAULO | Brasil | 3504602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fcb14001-4765-31ae-a64d-5cdc93582ec0 | -18.23368 | -47.41751 | 2025-10-23 04:10:00 | NOAA-21 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9bc4efb-1840-3146-b176-fe795a8f793a | -15.59658 | -45.90637 | 2025-10-23 04:10:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dadd94cc-5fd2-39d5-abd1-9cb09e4c2060 | -13.89809 | -48.36753 | 2025-10-23 04:10:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0317889-dc86-3008-9046-c85c15e643f0 | -14.84233 | -54.22293 | 2025-10-23 04:10:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| edd29e23-1009-3c5d-abcb-c30de35547fb | -18.14179 | -52.51391 | 2025-10-23 04:10:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f717c23-7dee-3cdd-a0d0-e99a501b2d08 | -17.60742 | -46.62128 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bfd1798c-5e02-31d2-b7e6-80835a8857be | -17.61364 | -46.60585 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 540cf20f-07ac-3a9f-9a94-98bdb8b74f3a | -18.72467 | -46.82614 | 2025-10-23 04:10:00 | NOAA-21 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5dbc92e-0bc6-382b-bb20-760235418bbe | -15.33873 | -47.98035 | 2025-10-23 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00ddf6ce-4ce8-3d6c-a77b-05c84daee16e | -16.47573 | -46.47349 | 2025-10-23 04:10:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5b79c56b-d0b3-3383-8c75-0a2d34923cf1 | -17.60952 | -46.63 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 427b059e-5d0e-3830-b4fe-8ccf2cb84976 | -17.60464 | -46.63746 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f95b032a-0e19-3e53-929f-66c3bb30f93c | -21.69793 | -43.96987 | 2025-10-23 04:10:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4d4d669f-e16f-306c-b49b-5beb112ba36b | -14.84203 | -54.2238 | 2025-10-23 04:10:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 647b73c2-c44b-347f-baaf-019939aba213 | -15.52567 | -50.13011 | 2025-10-23 04:10:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cd0c3baf-b46d-3283-9fff-bda4c6df962d | -13.89506 | -48.36785 | 2025-10-23 04:10:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8f2cda6-463f-38e8-9680-fd73f7f1a4b8 | -13.89445 | -48.37121 | 2025-10-23 04:10:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d99c62b3-8bee-3220-bc72-2a73f646451d | -17.60668 | -46.60457 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1d47208-1bcb-3ab8-8938-15c55ff1ceae | -15.52484 | -50.13458 | 2025-10-23 04:10:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6af52521-9fe7-3709-9848-3e4cbeb8160f | -17.21247 | -47.65687 | 2025-10-23 04:10:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50cf0c6b-befc-36df-8a0c-3bf5d22cbd04 | -17.60938 | -48.57669 | 2025-10-23 04:10:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15866047-290d-3d77-8af9-0b8d3a6d4c7c | -18.22651 | -47.41621 | 2025-10-23 04:10:00 | NOAA-21 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1520db79-d5c6-30b5-9558-9062459874bd | -20.57308 | -45.89148 | 2025-10-23 04:10:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a08d0a7b-4e0e-3d6d-b4a9-28a6bca8ddb4 | -18.18621 | -46.19738 | 2025-10-23 04:10:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 726affae-260c-3d20-85ff-ff9750209bc8 | -17.55065 | -51.04425 | 2025-10-23 04:10:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7337798-7eb8-3f0c-b382-af84bf893e1b | -18.91714 | -47.02063 | 2025-10-23 04:10:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a8109b25-90f7-348c-b691-5376ba424eaf | -20.23732 | -47.38617 | 2025-10-23 04:10:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 236a0bf9-d1a6-3cd6-b337-c28b64053497 | -20.64068 | -42.71089 | 2025-10-23 04:10:00 | NOAA-21 | PEDRA DO ANTA | MINAS GERAIS | Brasil | 3148806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6a260579-7f90-3f8d-b4ac-08dd4e9d7796 | -19.34077 | -44.22654 | 2025-10-23 04:10:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 384a1a60-d11b-33c7-ae28-b2d09ec82a6a | -20.97635 | -47.3652 | 2025-10-23 04:10:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14473aba-6863-3c06-a1db-a6ff99dac475 | -17.61644 | -46.61052 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bce84500-7cab-3c08-b4c4-b904b3fbb81d | -21.48543 | -46.02289 | 2025-10-23 04:10:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f3fe727b-7397-3048-995b-dd295d637601 | -18.71637 | -46.8329 | 2025-10-23 04:10:00 | NOAA-21 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f58812f1-fc8e-3611-8612-069695f72564 | -17.40286 | -47.51624 | 2025-10-23 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d1f0a4a-388c-36d7-831a-091910e62ce4 | -19.15528 | -49.12894 | 2025-10-23 04:10:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| defca5cc-f335-360b-b619-a69e226b3970 | -17.52165 | -49.21548 | 2025-10-23 04:10:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 424b3efc-17fc-3fba-852a-c5b0a96aba6e | -14.27957 | -48.07513 | 2025-10-23 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1212c9a-6b92-3fb0-898a-cd2a3af543d1 | -17.60879 | -46.61324 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 49e31d4e-cf42-3095-8bad-ed1b9a798f1c | -17.6032 | -46.60392 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0856bdd4-e79f-35fe-80e1-918d21acf2ac | -17.61781 | -46.60246 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a7ebdde-ccb3-323d-8186-a97bf12e39f7 | -17.60675 | -46.64618 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6adfe4e-1bab-3dc8-b383-11bbb33e8893 | -13.90835 | -48.36329 | 2025-10-23 04:10:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 15a3a35d-18ea-30e1-8860-2ea8607b549f | -17.60882 | -46.63405 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a41ec57-dcdf-313f-9ac0-1298693c455f | -17.62551 | -46.62049 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b4bc77c9-0c65-3c07-8e98-283ca3034809 | -17.62482 | -46.62451 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a01e23ab-f324-31e7-af26-851e1a99eec7 | -15.32712 | -46.81363 | 2025-10-23 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6b6a8b6-5734-3e90-9baf-fa0333103d12 | -17.60395 | -46.6415 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README15.md)
