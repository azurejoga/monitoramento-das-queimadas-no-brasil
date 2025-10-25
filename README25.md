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
| 71e94ca3-19f7-305b-91fa-3c03aa5edab9 | -18.55877 | -50.27529 | 2025-10-25 04:02:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| b6a8a56d-10e2-3fe0-ae75-46138f74d559 | -16.21399 | -46.48075 | 2025-10-25 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 07ae488c-7a03-32e0-af42-44d85dd3019e | -16.36252 | -49.93843 | 2025-10-25 04:02:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2018ba9e-d7fe-38f0-97de-ddf21eee8d84 | -20.28265 | -50.22393 | 2025-10-25 04:02:00 | NPP-375D | FERNANDÓPOLIS | SÃO PAULO | Brasil | 3515509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a1230052-cea9-3b24-96a7-13f8a245bd51 | -18.56323 | -50.27949 | 2025-10-25 04:02:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| 2b1f6a20-86c2-3541-a5c1-40413a0ebebd | -19.17764 | -43.52446 | 2025-10-25 04:02:00 | NPP-375D | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c884c16b-c453-3a44-8b02-81c1215b2102 | -21.95836 | -46.1633 | 2025-10-25 04:02:00 | NPP-375D | SANTA RITA DE CALDAS | MINAS GERAIS | Brasil | 3159209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| eac93b73-2d1f-39ce-8698-f6cc1f3117a9 | -18.23197 | -46.71503 | 2025-10-25 04:02:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2c27c86-b6d1-3fd9-9694-ae01cb725e83 | -15.00029 | -49.99059 | 2025-10-25 04:02:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c76fa710-b591-343c-aeed-e9dcdea0974d | -19.86039 | -44.30704 | 2025-10-25 04:02:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ad4be8d-a8bf-30c7-8511-c4f2ed38baa5 | -14.8967 | -52.45388 | 2025-10-25 04:02:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9092fab3-66d6-33d9-bce7-501fc6d1f006 | -21.08633 | -46.34275 | 2025-10-25 04:02:00 | NPP-375D | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 69799371-484c-3879-adc1-c317ffa16e22 | -19.86794 | -48.33352 | 2025-10-25 04:02:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09575f20-40d3-3c89-856c-4831cb553655 | -15.52987 | -45.70477 | 2025-10-25 04:02:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f20ad21-9fe1-3e36-be4e-9d88e8b67f82 | -19.85687 | -44.30634 | 2025-10-25 04:02:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc5f75d0-4143-309e-bde8-a18061432e10 | -15.56485 | -45.94974 | 2025-10-25 04:02:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db8be25e-6757-3a56-808e-b7c6878efd7e | -15.65777 | -46.1543 | 2025-10-25 04:02:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b03e409f-71d3-36e8-aa0d-4a338284cb49 | -19.87883 | -45.83764 | 2025-10-25 04:02:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9e8b9ae-e9a2-3e40-8172-1cd8267fc7af | -18.1617 | -51.75575 | 2025-10-25 04:02:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f9f0e139-abd1-30b3-962b-3d10ee5cce26 | -18.41729 | -43.28898 | 2025-10-25 04:02:00 | NPP-375D | SANTO ANTÔNIO DO ITAMBÉ | MINAS GERAIS | Brasil | 3160207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d87cece3-7472-32ef-bcc5-22d218a2fc6c | -18.17373 | -51.75489 | 2025-10-25 04:02:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 58007363-2b36-3f12-b219-ff49637968c5 | -18.903 | -44.40605 | 2025-10-25 04:02:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11470bff-6e36-36fc-af20-ad99715088a6 | -20.76023 | -43.23121 | 2025-10-25 04:02:00 | NPP-375D | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.4 |
| f2f83e35-44da-36ca-8fb1-22f726a18907 | -16.21471 | -46.47682 | 2025-10-25 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 168b74b1-9fad-3d7a-a7c5-9ae4f780fe40 | -17.415 | -46.88075 | 2025-10-25 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4943ab8e-9968-3cc3-b665-59947df45778 | -16.17455 | -45.08098 | 2025-10-25 04:02:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c4d9d83a-1cf4-39bc-bfbb-19e313c7b9b8 | -20.33942 | -42.90122 | 2025-10-25 04:02:00 | NPP-375D | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| b9ed6ce3-7e6d-3bca-afee-e9f0afcb460a | -19.76304 | -48.29253 | 2025-10-25 04:02:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 45c471f1-9028-3d42-9da1-4690e79eeaed | -21.15083 | -48.51582 | 2025-10-25 04:02:00 | NPP-375D | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 89118873-f909-3739-8110-aa7bcc3f915d | -21.07358 | -43.63572 | 2025-10-25 04:02:00 | NPP-375D | SENHORA DOS REMÉDIOS | MINAS GERAIS | Brasil | 3166204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0848f14b-9e67-3208-a04c-4dbbdc387f19 | -20.10902 | -45.85334 | 2025-10-25 04:02:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c35b9c8f-4125-3de9-b644-92e5237b1dd3 | -15.2239 | -47.92476 | 2025-10-25 04:02:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 342f42cd-3d7a-34c6-b882-876e01cf6346 | -22.58166 | -44.27961 | 2025-10-25 04:02:00 | NPP-375D | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 11531b68-6be2-3dbd-97e5-86b984d6d63f | -18.55301 | -50.27722 | 2025-10-25 04:02:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 2e5c5f65-e2d3-3dd7-b6e3-9e470bbea12a | -22.58234 | -44.27563 | 2025-10-25 04:02:00 | NPP-375D | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0004c5e9-d569-3f38-9a9a-328f836c9b9c | -19.87971 | -45.83284 | 2025-10-25 04:02:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d5b14cc-8ef1-3c4d-b7a3-f86e74d4c15d | -17.38233 | -45.49543 | 2025-10-25 04:02:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c578ec42-2b09-395e-b4ca-901d2c3513a5 | -19.08455 | -46.75691 | 2025-10-25 04:02:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c04d9163-f1d3-34f1-b50c-0dc1d94c8f6a | -19.62325 | -46.13169 | 2025-10-25 04:02:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 81085573-bf0e-36db-8c77-9cc84bf94298 | -20.41612 | -50.10303 | 2025-10-25 04:02:00 | NPP-375D | VALENTIM GENTIL | SÃO PAULO | Brasil | 3556107 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9bc00680-3fac-3e15-aef0-351492514e6a | -16.58727 | -43.50575 | 2025-10-25 04:02:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 088ab01b-1650-39bf-9ff3-6c2b1f858922 | -14.88529 | -52.44611 | 2025-10-25 04:02:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75ae8607-6e66-356d-afa0-687054a3cba0 | -20.44596 | -44.16126 | 2025-10-25 04:02:00 | NPP-375D | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1ffc2b57-0ad9-3d52-8b2a-9cb93d6af92e | -19.28105 | -43.29074 | 2025-10-25 04:02:00 | NPP-375D | SANTO ANTÔNIO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3160504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fccf6e8c-5fa5-352d-8480-ef5bbae1d6cf | -15.24085 | -47.91262 | 2025-10-25 04:02:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae561aa2-a670-31d5-84af-d79b67b45237 | -18.1655 | -51.76554 | 2025-10-25 04:02:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5682bbe8-59d9-3d62-a863-496ca2d15318 | -18.16901 | -51.74936 | 2025-10-25 04:02:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 41a9fb86-b4e6-3746-aa69-1f21e614dff3 | -21.92369 | -46.51523 | 2025-10-25 04:02:00 | NPP-375D | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 9ee409d6-30ab-3e5c-b0b3-bc64216cde2a | -15.98265 | -43.90619 | 2025-10-25 04:02:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e1f9ab91-bede-3713-bde2-25b539eaa566 | -16.36185 | -49.94169 | 2025-10-25 04:02:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7569eada-aec1-338e-9a17-a766fe0556ec | -18.70124 | -43.72831 | 2025-10-25 04:02:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db3ed975-ca2c-3c55-99b0-4076e21b3d67 | -21.9008 | -46.55259 | 2025-10-25 04:02:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6a3ba2ac-0355-36aa-9d37-fc1ba00fbade | -19.76213 | -48.29717 | 2025-10-25 04:02:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0a324f1e-389e-3b10-b719-edc8f2f83145 | -15.47251 | -50.46518 | 2025-10-25 04:02:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 741d3575-6754-30b1-89b5-e2b26e27bc66 | -21.88598 | -45.26752 | 2025-10-25 04:02:00 | NPP-375D | CAMBUQUIRA | MINAS GERAIS | Brasil | 3110707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fcb2e8a3-0f4a-37b7-aa9b-772643930cb2 | -19.26659 | -45.83739 | 2025-10-25 04:02:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 502b9e75-4e43-3654-9dfb-f6ec943127f6 | -20.43961 | -46.58689 | 2025-10-25 04:02:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32848c4a-6360-34af-8cc8-646a23a55474 | -15.23465 | -47.93599 | 2025-10-25 04:02:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e30b3725-2257-3009-b19d-a7fdf523a08a | -16.06601 | -46.62183 | 2025-10-25 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 94cadeb9-2f65-3f7b-9fb4-4104b671ea80 | -14.84344 | -52.44617 | 2025-10-25 04:02:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 478e4455-bdf4-3922-b4b5-fe72b3d827a2 | -15.53589 | -45.69548 | 2025-10-25 04:02:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9056ed72-f73e-34cf-ac5a-fc10d0aca73a | -15.47308 | -50.46707 | 2025-10-25 04:02:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 14839e10-e5b6-3177-b110-b645555f56ff | -14.56222 | -54.17796 | 2025-10-25 04:02:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87b91978-1829-3151-b6eb-cee09ff040d8 | -19.76743 | -48.29358 | 2025-10-25 04:02:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6627092a-5a73-3f16-8512-2dd85af1845c | -19.86977 | -48.32421 | 2025-10-25 04:02:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39c2156a-1ca5-3b32-992e-2eb03906716f | -15.53455 | -45.70201 | 2025-10-25 04:02:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 165d4ca3-d641-3679-adf8-2ed9df1b1434 | -16.09548 | -46.74829 | 2025-10-25 04:02:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4cf5a8f6-ca8e-3116-96c0-1babb757d893 | -14.84459 | -52.44069 | 2025-10-25 04:02:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64f30bb2-bbd6-38a3-b02f-77f8ffea0cc2 | -18.16728 | -51.75733 | 2025-10-25 04:02:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b7003b4a-143e-351b-96dc-799eb9e41f8d | -15.31171 | -48.07716 | 2025-10-25 04:02:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f939aa64-9368-3110-8f3d-dab36741b44f | -16.17368 | -45.08592 | 2025-10-25 04:02:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a7be84b9-d3f5-39e6-9572-a7814dca0804 | -19.65108 | -44.90321 | 2025-10-25 04:02:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e907ed9e-0852-3ead-a241-227153c76189 | -21.2048 | -46.7196 | 2025-10-25 04:02:00 | NPP-375D | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 36ff7728-d992-35d5-998f-8d7b85ae749c | -19.60432 | -43.69322 | 2025-10-25 04:02:00 | NPP-375D | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5179782-69ce-38ab-a740-ddbe5f0a1019 | -16.58373 | -43.50513 | 2025-10-25 04:02:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 26.7 |
| c1b29d16-0342-372d-a90d-9e8dc18bc19c | -19.1742 | -43.52381 | 2025-10-25 04:02:00 | NPP-375D | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 316ba836-b4fb-3151-89b1-66b6a22d6b44 | -18.08579 | -44.24813 | 2025-10-25 04:02:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd762365-994a-3348-a627-cbf39655f62e | -19.31461 | -42.28711 | 2025-10-25 04:02:00 | NPP-375D | BUGRE | MINAS GERAIS | Brasil | 3109253 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dd8f70ab-450e-3192-b19e-e25f0d541790 | -19.87415 | -48.32528 | 2025-10-25 04:02:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2bf48380-dda9-3a45-b49e-ca3cc0f3af91 | -22.83998 | -43.48845 | 2025-10-25 04:02:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9942cdc0-9307-3942-8565-64b6761a02c5 | -19.60088 | -43.69253 | 2025-10-25 04:02:00 | NPP-375D | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb6a1140-3031-340f-a056-e286d04277d1 | -18.16816 | -51.75327 | 2025-10-25 04:02:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 27e877e5-295c-3227-9bff-67f6b31922d5 | -21.91705 | -46.5295 | 2025-10-25 04:02:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| e3bf29d6-cc30-3b87-8c7a-9ef9e06fb05d | -20.41125 | -50.10192 | 2025-10-25 04:02:00 | NPP-375D | VALENTIM GENTIL | SÃO PAULO | Brasil | 3556107 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8fdb0ecb-8176-330c-9d43-2928988dca84 | -15.56146 | -45.94507 | 2025-10-25 04:02:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 217a1f59-46c5-3f92-88b6-4a743a64ae85 | -15.21926 | -47.92365 | 2025-10-25 04:02:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b5ac742-4010-3cb4-86fa-32549d3c8264 | -19.62743 | -44.76217 | 2025-10-25 04:02:00 | NPP-375D | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dff3b5b8-1c8e-3290-ae9b-9853ce17c819 | -18.79045 | -48.0405 | 2025-10-25 04:02:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 16e4fc0e-9ac8-3c87-b3ab-52a08b49e747 | -14.40383 | -51.52191 | 2025-10-25 04:02:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7c61bd04-c254-3662-8765-afd83f4d2052 | -15.24353 | -47.92377 | 2025-10-25 04:02:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12cc8807-1cc3-3a6a-a664-9e095259f22e | -15.23192 | -47.92463 | 2025-10-25 04:02:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e44c47c5-3dd9-36af-a000-16b27665d923 | -19.95082 | -41.71983 | 2025-10-25 04:02:00 | NPP-375D | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 740f4099-b2eb-30d7-a4e3-b4d48c866925 | -18.24809 | -44.1936 | 2025-10-25 04:02:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e7c470f-9ca1-3a8c-96e0-bdef38e2a149 | -19.32948 | -49.08559 | 2025-10-25 04:02:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4711e56f-5514-359b-b987-77d916dcfdda | -15.21798 | -47.92133 | 2025-10-25 04:02:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 572e3086-b902-368a-9b59-38b508fb5b78 | -17.9509 | -44.54426 | 2025-10-25 04:02:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7b8aa9f-25e6-32b0-a49a-4b028cc3b9ae | -20.69977 | -44.25943 | 2025-10-25 04:02:00 | NPP-375D | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4231590a-efbf-3e44-aa73-c0f86fa5520c | -16.36764 | -49.94003 | 2025-10-25 04:02:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aadaa3b7-2830-3283-b51a-930d672bd9b5 | -15.22626 | -47.92894 | 2025-10-25 04:02:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2b05b16e-04c3-3fe3-9126-074808c4735a | -17.37636 | -45.48415 | 2025-10-25 04:02:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README26.md)
