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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd0137fd-f462-35f7-86d4-b761452097c0 | -4.36257 | -47.76086 | 2026-09-02 06:27:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 560f2f1f-5f4b-38e2-a0c8-c051a871dfb9 | -6.09584 | -44.13338 | 2026-09-02 06:27:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 01c4eab0-c35a-3ca6-9188-68c7c239480e | -11.33676 | -50.58982 | 2026-09-02 06:29:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 45.1 |
| a92d7ebf-6d5b-3646-a606-fd5ed86f4e58 | -11.30455 | -45.15255 | 2026-09-02 06:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 8b7131ed-f105-342e-83f3-abd238527838 | -12.13141 | -47.05894 | 2026-09-02 06:29:00 | AQUA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 60db9217-08fc-354d-bb15-a14b2b4bffe7 | -15.36194 | -47.6925 | 2026-09-02 06:29:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b115245b-04ee-3216-b633-d1ddfd0c50c4 | -16.19375 | -47.48338 | 2026-09-02 06:29:00 | AQUA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a528f76a-013d-3188-ba17-4f4b92d6e43b | -12.14013 | -47.12554 | 2026-09-02 06:29:00 | AQUA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| aeee2368-ba8e-3fd4-a308-672017383bac | -10.91632 | -45.32763 | 2026-09-02 06:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 69338e5e-ee1c-37b6-adb1-4046ae30acca | -12.6306 | -45.06879 | 2026-09-02 06:29:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 112120c0-d5ec-3ed9-802f-fa830beefd69 | -10.99115 | -45.07893 | 2026-09-02 06:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 26ccf0ae-a58a-3083-bb23-4f683d476a38 | -16.73214 | -47.0602 | 2026-09-02 06:29:00 | AQUA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| bc155223-a6fd-32a3-bad4-9e73c8c160c2 | -11.31339 | -45.15387 | 2026-09-02 06:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0d1da52d-99ef-311c-9eda-ce38ee862fcc | -16.18455 | -47.48174 | 2026-09-02 06:29:00 | AQUA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 88797d1d-3c8b-3eb3-9f3e-53eef56600c3 | -10.77984 | -44.76133 | 2026-09-02 06:29:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 5e128711-c910-3b5a-9205-4d8b19c0c9e1 | -11.30035 | -45.17958 | 2026-09-02 06:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 07320fe5-0e0c-3358-9f79-f3dad6593bdd | -10.40946 | -49.99907 | 2026-09-02 06:29:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| d2f77c9d-343c-3665-99f1-d7a0633b35b8 | -11.28985 | -45.17214 | 2026-09-02 06:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fdc01eba-84fc-3fa6-8c39-34a5307c53fc | -11.34011 | -50.57082 | 2026-09-02 06:29:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 38.1 |
| f8ad5dcf-ffb7-3502-a552-fd3b68d82ffe | -10.97046 | -50.47514 | 2026-09-02 06:29:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 39155e74-5ba9-33e3-8c77-f08580663841 | -10.97655 | -50.46212 | 2026-09-02 06:29:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| eeabbd4b-e027-399c-90e3-86bf18423f1a | -10.433 | -46.74016 | 2026-09-02 06:29:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c5bf6612-388f-3f92-9cee-5fcb714608a9 | -11.29123 | -45.16319 | 2026-09-02 06:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| aee22f67-4952-384f-a1ae-efb7103d87fd | -11.47784 | -45.09369 | 2026-09-02 06:29:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 87e46188-3bc9-336c-a445-2a80843b42f2 | -15.59701 | -46.57445 | 2026-09-02 06:29:00 | AQUA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 09560deb-e7d3-3a06-ae28-71aa3e2335aa | -10.90742 | -45.32623 | 2026-09-02 06:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 3c7845f4-4af7-3643-8e87-5db92114c5a3 | -11.82837 | -46.05674 | 2026-09-02 06:29:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 43a82748-b8a6-309f-93dc-e240a62baedd | -16.18293 | -47.4919 | 2026-09-02 06:29:00 | AQUA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 73367eb1-0836-362c-819d-728721f5ac61 | -11.32768 | -50.56863 | 2026-09-02 06:29:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| ea0880d9-b5d5-36aa-aa06-582c2f5bcf1c | -11.3217 | -50.58194 | 2026-09-02 06:29:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 9cfccb48-faf0-3fe5-b886-df58101bfdf8 | -10.43638 | -46.7191 | 2026-09-02 06:29:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6f0eedb0-0d13-3914-b493-62a2ab2fa9a5 | -10.91489 | -45.33674 | 2026-09-02 06:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 5d3700ec-f961-3250-a3b8-c38f011e7cf6 | -11.30596 | -45.14346 | 2026-09-02 06:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b9784720-dfe5-3d6a-9be6-d08d5871ead4 | -11.67124 | -50.47611 | 2026-09-02 06:29:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 7fa17831-081a-3d05-8a82-c5c5fdac343d | -12.87351 | -45.8301 | 2026-09-02 06:29:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| fafcd005-56f0-3dce-8a8b-de6ad02acbaa | -10.9732 | -50.48102 | 2026-09-02 06:29:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 8e79fe3f-dae8-3178-81a2-d65458ba6916 | -7.64749 | -45.87686 | 2026-09-02 06:29:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6661a5fd-3555-32e0-9fbc-59363dd2afae | -10.77378 | -44.7421 | 2026-09-02 06:29:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| b9c9ee9a-7007-3ec0-a0c9-557d433f7f89 | -10.96724 | -50.49414 | 2026-09-02 06:29:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 5f90ecc7-0b2e-3634-b38b-ceb52da25aec | -7.65844 | -45.86825 | 2026-09-02 06:29:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 806c6947-3934-31c8-9a23-aba95c305db6 | -15.37308 | -47.68341 | 2026-09-02 06:29:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b5f7de62-dd6c-37d6-821c-dc3a2d57def0 | -11.81782 | -46.0648 | 2026-09-02 06:29:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c33a37c9-28e3-3cfe-897b-d01bdffffe43 | -11.35647 | -45.40941 | 2026-09-02 06:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a8dcc24a-f8d7-3243-890e-5c625c262704 | -16.42967 | -42.39898 | 2026-09-02 06:29:00 | AQUA_M-M | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 61309b7c-2621-32cb-82bb-6164ed3254d3 | -12.05469 | -45.0095 | 2026-09-02 06:29:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ce769e3e-76a5-35be-a5aa-85dd110b11a0 | -11.47922 | -45.08468 | 2026-09-02 06:29:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 23.9 |
| f2a098ab-3b01-3c2c-8894-bd0f9a699907 | -11.33416 | -50.58415 | 2026-09-02 06:29:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 035024de-942d-30d3-ad87-3094f834909a | -11.3466 | -50.58637 | 2026-09-02 06:29:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 86aff3b6-4900-3d6d-8028-df7da2e7f2ee | -12.12718 | -47.14524 | 2026-09-02 06:29:00 | AQUA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 62837116-b302-3924-b4c9-634acbf69325 | -10.906 | -45.33535 | 2026-09-02 06:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| a62b6cce-4e99-3bb4-b9c8-c7295eb23aeb | -15.36366 | -47.68197 | 2026-09-02 06:29:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 7fc4ae98-e249-3143-8709-66ea489fa859 | -15.37134 | -47.6941 | 2026-09-02 06:29:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| d25d882a-8cb8-3ce7-8ee7-33dee68abed4 | -12.87496 | -45.82087 | 2026-09-02 06:29:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 13a786c3-a258-3245-83cd-1d9fc6470270 | -11.34921 | -50.59202 | 2026-09-02 06:29:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 35.1 |
| f16faccf-45d3-3ba8-beec-0cb8e6c737c1 | -15.6754 | -45.8937 | 2026-09-02 06:29:00 | AQUA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 20adc3bf-7e0c-307b-a3ad-2dba3fcbc9f0 | -11.32494 | -50.5629 | 2026-09-02 06:29:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 3abe407e-0152-3196-920b-f289da5629cb | -10.4347 | -46.72956 | 2026-09-02 06:29:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 678d1010-4ad2-3f2c-8f2e-acd6373de5a8 | -10.78121 | -44.75239 | 2026-09-02 06:29:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 23.7 |
| e2785a52-1905-3d3f-80e9-7e292f165118 | -16.43942 | -42.40059 | 2026-09-02 06:29:00 | AQUA_M-M | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d4008366-cf04-3c4c-8c3c-19f41aa2d2c5 | -10.99999 | -45.08029 | 2026-09-02 06:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7d6a5a4f-e42f-316c-b56a-c77964c2f91e | -14.96221 | -48.11087 | 2026-09-02 06:29:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1caa876e-e95d-3ed2-9dee-20d345c29809 | -16.15027 | -46.64468 | 2026-09-02 06:29:00 | AQUA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e92e530c-54c4-35ec-bd6f-92989e6db30d | -11.30314 | -45.16159 | 2026-09-02 06:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 5cff369d-e3a4-35a9-8a94-f90b8e1b8dae | -11.34586 | -50.6111 | 2026-09-02 06:29:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 9c9e5d9b-3648-3fe7-9487-bdd4bf6e98a5 | -13.36952 | -51.78046 | 2026-09-02 06:29:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| a54996ea-f824-3d6c-a4e9-d121e9a5f701 | -12.62922 | -45.07777 | 2026-09-02 06:29:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 10c26ec3-ccd1-309b-8622-5dcc4e523d5d | -12.1367 | -47.1468 | 2026-09-02 06:29:00 | AQUA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 370b0377-ae21-3fe9-953c-207e9ddacca2 | -10.88426 | -45.34489 | 2026-09-02 06:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a4ab8200-37e1-3cab-a7ff-887adc876972 | -11.30175 | -45.17059 | 2026-09-02 06:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 2090aaf8-be33-3bb6-9d40-31556904c423 | -16.15175 | -46.63516 | 2026-09-02 06:29:00 | AQUA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8633a636-4954-3967-9696-49466b30d5b0 | -7.28773 | -49.80355 | 2026-09-02 06:29:00 | AQUA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 3999f235-7df8-3f16-9b7d-72b4d7f148de | -12.13842 | -47.13617 | 2026-09-02 06:29:00 | AQUA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| f57de13e-b0f8-30f3-94fd-f51545da218c | -12.12193 | -47.05743 | 2026-09-02 06:29:00 | AQUA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 91f43938-9686-3b35-9e14-eb450e19a7f8 | -12.12364 | -47.04692 | 2026-09-02 06:29:00 | AQUA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9340caf2-36e5-3cd1-82b7-b87d453c24c6 | -10.9013 | -45.3279 | 2026-09-02 06:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 925fe661-ba40-35ce-8d44-b00ad11cd4a7 | -11.334 | -50.5752 | 2026-09-02 06:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 4c6366b3-5f72-3f4b-88b9-25d2080cb844 | -10.9204 | -45.3253 | 2026-09-02 06:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 95567de8-0356-3209-9c13-0f6b4976dafa | -6.6948 | -58.7678 | 2026-09-02 06:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 521e5c5e-2380-37cf-9c59-06bef0f0dab8 | -9.0046 | -65.42005 | 2026-09-02 06:37:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe0b93eb-d15f-3957-96cf-c9be251229ed | -8.65475 | -70.687 | 2026-09-02 06:37:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fe652b7-7d24-3630-94ad-3347cfb212be | -9.089 | -65.38135 | 2026-09-02 06:37:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 552e5238-cfef-3fcd-b6d4-de0661805931 | -8.56441 | -63.19333 | 2026-09-02 06:37:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9d7e357-218d-32df-be5d-9a07660c974e | -9.01503 | -65.40759 | 2026-09-02 06:37:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ddbce80-3463-3511-98f7-b479cbf70a91 | -7.69619 | -67.12334 | 2026-09-02 06:37:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22041291-103d-3b17-8650-1913a920e9d9 | -9.03523 | -65.39996 | 2026-09-02 06:37:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d3930902-fdf2-394b-8500-803527195835 | -9.00328 | -65.43007 | 2026-09-02 06:37:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4fed689-2d98-3d59-8df7-402e22d77447 | -9.01508 | -65.45837 | 2026-09-02 06:37:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8866038-471e-3db5-90e7-b51da55238f3 | -9.01286 | -65.40601 | 2026-09-02 06:37:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20778dcc-44fb-3e74-8800-e4939e1a5481 | -9.0122 | -65.41101 | 2026-09-02 06:37:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cec0d49-c8c4-327c-9811-e0fcd6046d0d | -8.78392 | -69.01716 | 2026-09-02 06:37:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 891f986d-21cd-3d53-812a-ff834dc1f908 | -7.84693 | -71.7412 | 2026-09-02 06:37:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 342e9c75-f7ca-348d-90fe-e88f0fc8c4fd | -9.01952 | -65.45257 | 2026-09-02 06:37:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 36648a73-dd06-3720-bffb-1172f11b8e31 | -7.69013 | -67.12624 | 2026-09-02 06:37:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f139c5dc-9123-3997-a04a-a74d9f90eadf | -8.33139 | -70.72783 | 2026-09-02 06:37:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e201d94-d48e-3a20-bd07-e90bcbba9e27 | -9.01886 | -65.45753 | 2026-09-02 06:37:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1e99e362-b085-3269-9bb2-da3247249324 | -9.02199 | -65.45425 | 2026-09-02 06:37:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81a5547e-422c-36c2-92bf-4ce7108662c3 | -9.00748 | -65.41669 | 2026-09-02 06:37:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11a24abf-7515-331b-9f1d-591e8811bd44 | -9.02018 | -65.44762 | 2026-09-02 06:37:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eb22d6a5-c826-3a00-a90d-2778fc8511ae | -7.6851 | -67.12178 | 2026-09-02 06:37:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43757370-d94f-3472-bc85-c6a248a6d132 | -8.45683 | -72.53484 | 2026-09-02 06:37:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README66.md)
