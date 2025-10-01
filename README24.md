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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 253026b8-cac6-3093-8c0b-95a8b5775954 | -20.68709 | -43.37533 | 2025-10-01 03:32:00 | NOAA-20 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fe5dace8-5783-3731-bdc1-f2be6f836c78 | -17.40189 | -47.16805 | 2025-10-01 03:32:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69234b90-a38b-3339-bb42-a13cab217483 | -15.41336 | -47.05374 | 2025-10-01 03:32:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9f266082-3dc0-3a61-9cf5-e8e856f8b903 | -19.89247 | -42.62854 | 2025-10-01 03:32:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| feee5c14-7bf8-32fb-92a1-9bdaf742b31f | -19.83528 | -46.71788 | 2025-10-01 03:32:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f05ad15a-868a-3c48-82b0-721b844ff4d4 | -19.93081 | -43.89764 | 2025-10-01 03:32:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| c3cf2bd9-903e-3304-a051-c929fdb1ea8f | -14.68562 | -45.28962 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82cebfb4-75b0-326d-b060-ca7ce1f659d5 | -18.43285 | -43.80059 | 2025-10-01 03:32:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1df2164-6558-3a54-bc20-fc00be8e4edc | -15.48839 | -45.91727 | 2025-10-01 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2eafbbac-5332-311e-9f28-6d20a50609c8 | -14.66414 | -48.1396 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 468a0eca-428a-3310-ad1e-050b11cfb0c9 | -13.92127 | -48.09924 | 2025-10-01 03:32:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4f91dd8-0a9c-376d-ac07-d6bcb203b820 | -16.49507 | -43.73154 | 2025-10-01 03:32:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea2de8ee-a078-3ba7-9668-5146ec295a38 | -15.60741 | -46.91004 | 2025-10-01 03:32:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f526293-2fed-3360-b5ff-2acb92c26966 | -20.83772 | -43.02479 | 2025-10-01 03:32:00 | NOAA-20 | PAULA CÂNDIDO | MINAS GERAIS | Brasil | 3148301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 71000734-7a04-3692-94bb-db3828263ebe | -20.12831 | -44.02007 | 2025-10-01 03:32:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d36ce1f0-09cd-3b2b-a99c-3a14536237a2 | -15.28265 | -47.83787 | 2025-10-01 03:32:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e55a2935-e903-37bd-bfad-b70d76f37a8b | -17.86728 | -47.14534 | 2025-10-01 03:32:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e40c66b1-97bc-3217-8b89-64f84efc0405 | -16.37464 | -47.07256 | 2025-10-01 03:32:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 60575759-805a-384a-b777-1f18d865c855 | -14.36055 | -47.14183 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 90dc1801-30a0-3d2e-91f6-f6d16928ea42 | -14.89795 | -48.12109 | 2025-10-01 03:32:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0c1eb9cf-a6eb-3d4b-a05a-3209ed51dba0 | -17.95596 | -45.03149 | 2025-10-01 03:32:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 953d657e-9b25-3aa5-84bc-d63af488f0b4 | -16.24264 | -44.06253 | 2025-10-01 03:32:00 | NOAA-20 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82df8c87-5202-37ee-8e60-fc73c9ebfaaa | -14.52761 | -48.37194 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86afc4f1-8c13-3b59-a261-9974f5575350 | -14.96412 | -46.883 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 96d8a623-bb56-3b36-af23-8b5a7e5cd57c | -15.44265 | -43.64625 | 2025-10-01 03:32:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e3662cbc-74c3-397d-9c74-cfec440145c2 | -15.35433 | -47.08351 | 2025-10-01 03:32:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 210807e4-9c71-3975-afd8-d86ee84441c3 | -14.912 | -47.82711 | 2025-10-01 03:32:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 426e3dd8-eed3-3f05-b0d1-fbdbc647e151 | -18.4239 | -39.79618 | 2025-10-01 03:32:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| eb97b923-aa90-3846-a319-4d1cb0974e35 | -13.93398 | -48.10955 | 2025-10-01 03:32:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0863999d-4eaf-38b6-8355-71cb4f90b851 | -17.53818 | -43.45085 | 2025-10-01 03:32:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 997d2f5c-aca2-39bd-b45d-49fc231998da | -17.49272 | -43.47842 | 2025-10-01 03:32:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a528f55-c5f1-33d5-964e-fb7ffbd4924c | -14.43774 | -46.35903 | 2025-10-01 03:32:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a13d5215-74b7-372e-8048-7fff494cccf9 | -15.0739 | -45.07579 | 2025-10-01 03:32:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be2d2a2b-1240-3a6f-8d8b-67fda0543168 | -15.29162 | -46.40734 | 2025-10-01 03:32:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d722004-adf9-3222-8c15-126c1ce4a7de | -20.63391 | -46.18182 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10e40c7f-a438-3115-9e8b-d876a60c799e | -14.35353 | -45.93016 | 2025-10-01 03:32:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 886fec7c-3151-370c-9aa7-8ce162df6bb0 | -22.40824 | -43.16993 | 2025-10-01 03:32:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| de1e5b22-dbc1-3796-92dd-ffa4dd5bb400 | -17.95601 | -45.02114 | 2025-10-01 03:32:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bafcbab9-bc11-3939-be2e-ee9534617cad | -14.79311 | -45.80317 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 49bd1300-90eb-375a-9b8d-f1454bc0ea74 | -21.57347 | -44.21806 | 2025-10-01 03:32:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f4329245-73d9-3471-8ae9-bd5363ce0ce8 | -14.63241 | -46.98248 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 938a2953-4502-37e7-a500-55ebaa2c99e4 | -20.62192 | -46.20822 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b10de56e-9457-3005-8ae8-31bc0172485f | -20.18772 | -40.23744 | 2025-10-01 03:32:00 | NOAA-20 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4f041bc7-1c2a-31bd-9b63-41f737abb987 | -14.9584 | -46.88785 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06715efc-32ca-31ea-9e50-3e79b95a9863 | -19.93553 | -43.90397 | 2025-10-01 03:32:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| be79d3c5-461f-3063-880b-5e8fd4b0e532 | -20.42895 | -43.59697 | 2025-10-01 03:32:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5b0fa301-eba3-3cb2-afe6-faec05d98d47 | -18.89428 | -47.21027 | 2025-10-01 03:32:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69987ef3-83ea-3e3e-b600-16727b8e3d42 | -15.75959 | -43.71732 | 2025-10-01 03:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fc4c72f-e61a-3654-8076-79783ae674e6 | -17.79127 | -48.63504 | 2025-10-01 03:32:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 79b256cc-8ae9-36f1-b838-c3c67fbddd6b | -18.70322 | -44.33666 | 2025-10-01 03:32:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4487b3bf-17fa-3cab-951c-52338663cfe4 | -20.62498 | -46.2139 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cc535b4b-53a3-3991-90eb-2df7fd97e3d2 | -16.39837 | -47.05562 | 2025-10-01 03:32:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d49be8f0-d2f6-3e33-b39d-291ddb47f4ac | -15.27523 | -47.84068 | 2025-10-01 03:32:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5f8cac65-119e-34ee-9393-ba6c3b9a27b6 | -21.21776 | -43.92951 | 2025-10-01 03:32:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 06305425-701f-3101-82bf-73f820811b57 | -15.94383 | -48.12111 | 2025-10-01 03:32:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6ae5d49-ef9d-3c8e-a92d-d8805ffb9d7c | -15.33915 | -47.84338 | 2025-10-01 03:32:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5e7e3152-b5e1-3ca0-9ed5-81f9ba6f0c8b | -14.78897 | -45.79227 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| ac585b5c-07bf-3d94-be7d-aaf6ff7cfaac | -15.73435 | -45.25916 | 2025-10-01 03:32:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f994eaf-d2ac-3a14-851f-dcf7977886ee | -20.96506 | -45.8121 | 2025-10-01 03:32:00 | NOAA-20 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 709db306-daf6-303a-971a-cedc05098d9a | -13.93184 | -48.11937 | 2025-10-01 03:32:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9ebf5dbc-55f7-390a-ae2a-1a83b8664e95 | -15.77705 | -43.71373 | 2025-10-01 03:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83a8b3ae-396d-3f81-a933-03fd3b0b4682 | -15.48044 | -45.86372 | 2025-10-01 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17346795-1196-3753-8cd0-918dd7edd014 | -14.58316 | -48.30213 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4e450364-8b3e-3b48-911b-acf96378793f | -14.89587 | -47.21117 | 2025-10-01 03:32:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ebf00b2-2b47-3593-b232-c94875df34b1 | -20.02237 | -44.53807 | 2025-10-01 03:32:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c902ae68-6c91-35b4-a811-d73a3557c4d2 | -15.75669 | -43.73145 | 2025-10-01 03:32:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb07a0ed-c69c-3d5d-8a54-8cb005f36a5a | -14.59188 | -48.23014 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b3fefc3-d3b6-348a-9c96-5b4c1486cca2 | -15.2817 | -46.41547 | 2025-10-01 03:32:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa0020cd-42bb-38f7-aa46-c58755c77837 | -20.22168 | -43.44508 | 2025-10-01 03:32:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c93bdb3c-ae00-3fb1-95f5-59a1608b5289 | -19.31694 | -43.87917 | 2025-10-01 03:32:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 36d3bd54-af64-32f8-8177-6bc77e61ba8d | -16.24342 | -44.05875 | 2025-10-01 03:32:00 | NOAA-20 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e79d6db-62e3-3d27-9803-d4ec5098f326 | -19.85452 | -42.58519 | 2025-10-01 03:32:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 28f0af47-41d2-375c-b131-a30e145009bb | -15.84149 | -46.24784 | 2025-10-01 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acd5a3f0-11cf-334a-8498-8484e642046f | -15.00949 | -46.97927 | 2025-10-01 03:32:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| debfb4b0-652a-3892-bc65-4abb86734add | -14.68111 | -45.19234 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40987976-8ee8-3065-b7eb-ab40555273c7 | -14.79513 | -45.79369 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2367a720-db86-33af-a0ff-b21270f2610e | -21.04169 | -45.67437 | 2025-10-01 03:32:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc0f4d61-f367-32e0-a271-7af31febb98b | -18.71441 | -43.1795 | 2025-10-01 03:32:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f4696d9b-ca10-3b21-bc16-59b7800d9d51 | -15.3048 | -46.40788 | 2025-10-01 03:32:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1929c766-b8e4-33af-a6fc-693168210be0 | -15.78202 | -43.68937 | 2025-10-01 03:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b66a389e-4a56-35e4-994c-0d2593e5fee7 | -14.71814 | -48.14627 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0561f9c0-5a7a-37e8-a280-c9856f994690 | -17.40069 | -47.17335 | 2025-10-01 03:32:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1e7473af-e75a-3a07-852e-3bb98b97ff98 | -15.72914 | -41.74381 | 2025-10-01 03:32:00 | NOAA-20 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2665e47d-f7c2-33cc-9fc8-50336291d5e0 | -14.35129 | -45.94075 | 2025-10-01 03:32:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 10531293-5910-38a7-bf1e-2d5b5c0b8ddc | -14.60384 | -48.32099 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8c8fb961-51e6-3c05-9f54-a11487e5a2d1 | -18.60762 | -43.26904 | 2025-10-01 03:32:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 3800debb-f8ab-3d8a-9917-4012e4b7bf4a | -14.69975 | -46.97681 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 961f7e3d-2a64-3721-a930-86016a947e5e | -14.67865 | -45.29291 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a5e22e8c-1ab6-3d4b-9590-cef44e6549fc | -14.54374 | -48.24483 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bcbb69be-3a52-307f-8b8c-ac914b687d64 | -22.11102 | -44.69726 | 2025-10-01 03:32:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| acc2e476-eb17-36d8-bb9c-1ccb0689a69f | -17.96346 | -45.01368 | 2025-10-01 03:32:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c09d56ce-58a6-3392-96c2-5a114d465b94 | -14.74693 | -45.7774 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54718d3b-b69a-3c92-8a0e-82fc335df6f6 | -19.8949 | -44.49564 | 2025-10-01 03:32:00 | NOAA-20 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a7e056ac-ff9a-36db-847e-38be587bbc80 | -15.2657 | -47.8511 | 2025-10-01 03:32:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 215d7785-71da-3ad6-90c8-a4433d497eec | -14.7059 | -48.13478 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6cb960a2-844b-3326-b854-e6f1378653dc | -13.93732 | -48.12858 | 2025-10-01 03:32:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 4c095d38-c21d-34f3-acaf-bd844c918b30 | -18.95829 | -43.71016 | 2025-10-01 03:32:00 | NOAA-20 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd44da5a-c874-32a4-a38c-5bb770f7e49a | -18.32462 | -44.775 | 2025-10-01 03:32:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b7599bb-577b-3677-ac20-641550722ae3 | -20.02835 | -44.5356 | 2025-10-01 03:32:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2b2bc208-3de1-38a4-a313-23c0de58fb7e | -20.96595 | -45.80812 | 2025-10-01 03:32:00 | NOAA-20 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README25.md)
