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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 579ec846-f42e-322f-be0f-4dfcf4c09088 | -6.5515 | -42.99872 | 2025-08-21 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56323239-e8d1-3492-a8d3-9e2b2e249ca8 | -7.45508 | -40.15977 | 2025-08-21 03:49:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2c1d16b6-c67c-31a1-8c79-f0c5b1622a2c | -6.95223 | -42.86587 | 2025-08-21 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| b7484d98-0997-39b4-b076-aea414e6accc | -10.72087 | -48.23393 | 2025-08-21 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2359693d-f0e9-3be6-bab1-2bb5866dd594 | -7.01617 | -44.61989 | 2025-08-21 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| ad428715-9c9d-3522-b41f-764f785e5361 | -12.8871 | -46.0722 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d9504d8-258d-334c-b7a6-779658b997b7 | -11.57253 | -47.00979 | 2025-08-21 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d993dfa-89a3-35ff-8ad4-6a3f579a0554 | -7.6088 | -44.39082 | 2025-08-21 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4b90ee7-53c6-399d-bea0-756dac935f35 | -6.95083 | -43.86091 | 2025-08-21 03:49:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c1207c9-10bd-300a-8602-b22fd13c7c88 | -8.14067 | -47.34411 | 2025-08-21 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d94a2c3f-d334-3253-8395-3364888a12f1 | -13.0312 | -45.1957 | 2025-08-21 03:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| c062b6e5-6f35-30fd-ae72-26e13940d871 | -13.051 | -45.1693 | 2025-08-21 03:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 9ef92437-ab4d-3bbd-b97e-4f5299356f94 | -13.0128 | -45.1523 | 2025-08-21 03:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 144.7 |
| d094217e-28ea-3a72-a955-658963df9099 | -7.0164 | -44.6413 | 2025-08-21 03:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 2bc0554e-669c-302d-8da9-0275d58a7d68 | -13.0123 | -45.1756 | 2025-08-21 03:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 200.5 |
| a3da3eb2-ed5f-35dd-8e48-7c3906a37b18 | -7.0352 | -44.6396 | 2025-08-21 03:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 8a879fd2-95a6-3c30-b149-549b55c0d9e1 | -7.0169 | -44.5954 | 2025-08-21 03:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 64a6f2b1-896d-3f9c-9d55-1047dd7b5571 | -7.0354 | -44.6167 | 2025-08-21 03:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 246.4 |
| 6d129c17-3ff9-36e2-b653-1c0a76b9f7a2 | -8.8737 | -62.3925 | 2025-08-21 03:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 35.8 |
| e5fdd0bd-8f97-3360-b45d-06978f1f7aac | -7.0166 | -44.6184 | 2025-08-21 03:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 321.8 |
| 6af4f0d7-3ae0-31cd-9877-245e61a13158 | -14.6519 | -54.875 | 2025-08-21 03:50:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| e42e3876-d7ff-3c5b-be99-af9e808e6ef9 | -8.8735 | -62.4305 | 2025-08-21 03:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 30.9 |
| f5b489d2-a75d-3a67-abe8-08f470bf562c | -13.0317 | -45.1724 | 2025-08-21 03:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 245.0 |
| cadb6fc0-5c6c-358d-b1eb-c7d3a789aab0 | -8.8736 | -62.4115 | 2025-08-21 03:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 4497a108-0d11-3c4d-804a-4837af799d3a | -13.0321 | -45.1492 | 2025-08-21 03:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 179.8 |
| 6faf8f66-de63-3d3c-970f-65e04fcda5ea | -16.11332 | -46.8229 | 2025-08-21 03:51:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3ed7a55a-758f-3921-b4c0-b51ed6a2e8c6 | -15.88505 | -49.01153 | 2025-08-21 03:51:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e77b2859-4c43-3602-8e77-1ae13affd8a3 | -18.29487 | -45.51817 | 2025-08-21 03:51:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f93faf69-3301-3dc1-9f02-ea4f76e64572 | -15.93963 | -46.92852 | 2025-08-21 03:51:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8442a889-c5c4-3103-bc3a-e11966a2bb60 | -20.0817 | -46.13839 | 2025-08-21 03:51:00 | NOAA-21 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 925b54c9-70e2-3d5e-af42-5264e186c4e0 | -18.66731 | -46.98007 | 2025-08-21 03:51:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3c9a6d4b-b6fd-3d61-834f-7ab962a5ec35 | -18.30157 | -45.52827 | 2025-08-21 03:51:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e887a4ef-3102-34e3-9083-35c94a974dae | -14.46532 | -48.37235 | 2025-08-21 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0cae60b9-eb75-3b16-81b1-35a514e0c5fd | -14.38142 | -52.02213 | 2025-08-21 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b1deb45a-c726-3d80-b19d-d0759f9972dd | -18.29412 | -45.52213 | 2025-08-21 03:51:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5189f3c4-d28c-39a1-b862-edb056147add | -17.82484 | -44.41499 | 2025-08-21 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28ae62d9-bd44-3b8e-a50d-084818694236 | -17.58041 | -42.27505 | 2025-08-21 03:51:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d9313488-c257-3a64-9be5-755605778b33 | -21.7675 | -43.30743 | 2025-08-21 03:51:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cb1e792d-7674-3484-a73a-9e765534d8e6 | -14.85916 | -47.94803 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 28ad1f44-01bb-359a-b972-1c065c821233 | -13.63607 | -46.88379 | 2025-08-21 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ef9b2ac-7bd1-3888-b5c0-800e87cf1d6c | -13.53336 | -47.03695 | 2025-08-21 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b185c31a-67f1-3dc5-906f-b141430f596a | -16.3186 | -47.11761 | 2025-08-21 03:51:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 98a62d31-507f-382d-aee6-afb420cd6c6a | -13.58943 | -47.01406 | 2025-08-21 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c753d6a-fba1-3ca9-9836-2e9f4769d945 | -15.50055 | -48.0384 | 2025-08-21 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c5e8317-b337-3cc3-9e67-6f399405a8fa | -20.50533 | -43.9538 | 2025-08-21 03:51:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5e8c92e8-daa9-331d-ad71-4436628a4b2c | -16.00837 | -43.70935 | 2025-08-21 03:51:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a078ef65-ddb4-3604-bb2d-079534462c4b | -14.12151 | -45.37995 | 2025-08-21 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f22575d-48e5-319b-948e-c8e35a7edca9 | -18.73127 | -39.86728 | 2025-08-21 03:51:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2b9199eb-dc7c-3e25-8f73-0f393dad3931 | -13.56004 | -47.03269 | 2025-08-21 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| edc9305e-4037-3bd6-a0b3-725f5608516a | -15.44778 | -41.68963 | 2025-08-21 03:51:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1b2760ee-3c5d-3dae-93de-fce953dfc30e | -14.36946 | -51.9812 | 2025-08-21 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d356558d-8b8c-3d46-b2fc-7146effb71ab | -15.74822 | -49.96256 | 2025-08-21 03:51:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13b49e21-d563-3718-990f-685662bdbffc | -14.12791 | -45.39508 | 2025-08-21 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60d5a9f7-a199-3ef9-b5d1-560309450baf | -13.57337 | -47.04412 | 2025-08-21 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 702636e3-aec4-362f-8b85-b8b126bb6f05 | -14.12233 | -45.3755 | 2025-08-21 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf12ac69-a861-384d-a46d-de265f2c7b40 | -13.48941 | -47.05087 | 2025-08-21 03:51:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c686a742-00bb-3c3f-a730-b8e0751d2b9c | -15.50637 | -48.03606 | 2025-08-21 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c6667f3-86e9-3abc-be70-33dbdae1ec95 | -14.88583 | -48.06347 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 04c33f8b-ceab-3d1d-8ce0-4086f72e490f | -16.42599 | -41.2577 | 2025-08-21 03:51:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dfe47eb4-7cf7-3640-853c-277eb7cab719 | -14.85726 | -47.95786 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 717133a6-5150-3f0c-96d7-7a60d36cfb50 | -14.84449 | -47.94072 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9592b671-bfe3-312c-832d-81c17510b25d | -17.39859 | -46.697 | 2025-08-21 03:51:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 481415e4-1082-3064-b2ae-a18d0876e4b9 | -17.85106 | -42.51964 | 2025-08-21 03:51:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5bef6ea0-b7e3-3178-a1e9-a13c82fc8c38 | -16.61629 | -49.02205 | 2025-08-21 03:51:00 | NOAA-21 | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 236d6dce-be00-3bb7-9af8-ec79316201f9 | -18.66374 | -46.97436 | 2025-08-21 03:51:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 53e82e10-014b-3cfc-b5a9-db079794a818 | -14.3668 | -51.97666 | 2025-08-21 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 896f5729-d42c-3718-8ffa-fa32687fa568 | -14.92475 | -42.80704 | 2025-08-21 03:51:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7fdd2d94-3caf-3d18-9f32-718dda5a1aee | -14.85779 | -47.9609 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| da06ada4-70bb-35bf-b634-cca7688c5546 | -15.51783 | -48.05876 | 2025-08-21 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a33e93aa-2144-3fd3-a7ba-b0eb2451594e | -18.1277 | -43.95365 | 2025-08-21 03:51:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35dbf640-8769-3e5b-ad8d-30d633819ff1 | -20.22066 | -41.78248 | 2025-08-21 03:51:00 | NOAA-21 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b6ee9573-f702-3b2f-b7f6-65328aa89b23 | -13.53778 | -47.04084 | 2025-08-21 03:51:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5978e282-0208-3db6-996a-f0901ccdb699 | -14.84879 | -47.95221 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 669b91ab-b823-359a-a7f8-5b412d7c2023 | -17.34168 | -47.15686 | 2025-08-21 03:51:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc61f5bd-8dbb-34ab-a850-691a22bb75cc | -14.84581 | -47.93391 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 811f36dc-4479-3ae5-a4b3-916805b359e2 | -17.59926 | -44.43453 | 2025-08-21 03:51:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2c15d5b-200b-392d-b5c5-cdf241d514aa | -20.50613 | -43.94922 | 2025-08-21 03:51:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f8095382-7ebf-33ae-a36d-d137e58871ef | -14.37075 | -51.97533 | 2025-08-21 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 699dea10-6bfd-3823-9e30-5fa45a729bc5 | -15.88971 | -49.01638 | 2025-08-21 03:51:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a595a78a-1f56-3e12-91ab-2878a17f3081 | -16.51492 | -46.73448 | 2025-08-21 03:51:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3d282792-1f9a-3679-b3da-98d43f09d516 | -14.84827 | -47.94888 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2dd605b6-b788-3430-8fbc-55087ec0cd86 | -19.94119 | -42.13181 | 2025-08-21 03:51:00 | NOAA-21 | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c181f1c5-792a-32ca-ae6c-81eae3ec33a9 | -14.85976 | -47.95111 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a6129833-ced6-323c-84bc-bba2443be0ad | -14.36416 | -51.97366 | 2025-08-21 03:51:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f7d2f6b6-1e62-3c19-b091-83630d1c8148 | -14.85292 | -47.93177 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4953c06c-125c-3a26-ab03-8b868e18419b | -17.55144 | -46.61715 | 2025-08-21 03:51:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b1a3ee37-8a2f-352f-9d06-11de30da6263 | -18.72796 | -39.8667 | 2025-08-21 03:51:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ae82b231-e871-30bc-a237-88af75aafcc3 | -18.29261 | -45.53013 | 2025-08-21 03:51:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0080bc9e-68f7-3dc7-9c62-46c066e6c13d | -14.85412 | -47.94635 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2b25cac1-1633-399a-88a4-7bffdf71805f | -14.47084 | -48.37256 | 2025-08-21 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 85cc3541-8a7a-3c4b-ad5d-94dbd3f94081 | -16.51127 | -46.72834 | 2025-08-21 03:51:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 668b5237-3895-30bf-850a-c72500bfb5d3 | -18.29746 | -45.52721 | 2025-08-21 03:51:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 19e6a2d7-d4df-35da-90d6-07192ec80784 | -14.85401 | -47.95298 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b50601c3-4c14-3d6e-882b-19fec67e6ae5 | -20.08664 | -46.13522 | 2025-08-21 03:51:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69ed0a79-984f-3961-80ea-e9fb117cb130 | -14.49778 | -45.95807 | 2025-08-21 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 51f317ef-ee2b-3fdc-990d-d89a6ca778d2 | -14.84963 | -47.94186 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b20a40e7-af71-3047-b860-57e4036debf0 | -14.85846 | -47.9576 | 2025-08-21 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a3e23cb5-d922-3c0e-8aba-a882649e0df8 | -15.5185 | -48.05543 | 2025-08-21 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49c3dd6e-7eea-32c3-b79d-45afa30926f5 | -14.4932 | -45.95726 | 2025-08-21 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 878be10a-4a63-3f37-b391-ca29f51eee90 | -14.12709 | -45.39956 | 2025-08-21 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README18.md)
