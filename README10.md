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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8ffdea9-cd01-3728-a6df-c8e2922a8c25 | -17.13486 | -51.66595 | 2026-08-11 03:51:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e19e4af0-6e50-30c2-aba6-fac50a223fa7 | -18.92761 | -43.75595 | 2026-08-11 03:51:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ac5b499-aa22-33de-b7d5-529ea41c614e | -22.18842 | -43.24198 | 2026-08-11 03:51:00 | NOAA-20 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0397b311-2c4f-3fba-80f3-8df646667cc6 | -20.04484 | -43.75331 | 2026-08-11 03:51:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d285df48-a49e-342f-ad99-24a4e2a8c023 | -20.04877 | -43.75435 | 2026-08-11 03:51:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| baa50137-0950-305e-9364-09e6d3ba90c1 | -22.18562 | -43.23623 | 2026-08-11 03:51:00 | NOAA-20 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8d750ec1-f076-35e0-a864-1dc0e24351a8 | -22.1846 | -43.23848 | 2026-08-11 03:51:00 | NOAA-20 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8badf613-3820-32e8-b697-3662639a43a6 | -21.46744 | -48.61699 | 2026-08-11 03:51:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32ad4863-a5aa-3528-b2c7-9d152389c555 | -22.34555 | -43.04625 | 2026-08-11 03:51:00 | NOAA-20 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b0dac4c5-552d-3665-bc6d-33b265dc3973 | -20.4609 | -52.91835 | 2026-08-11 03:51:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2eeb0c44-4093-350c-809f-eef77f68662e | -17.1377 | -51.65392 | 2026-08-11 03:51:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 494d8c99-0add-3a64-8400-fb0b24174734 | -18.92787 | -43.75675 | 2026-08-11 03:51:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1732e375-53b2-35a2-a79f-5147041c1ebd | -21.46297 | -48.61232 | 2026-08-11 03:51:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a87132fb-12ee-3b8e-bc62-6fbfac356101 | -19.70624 | -45.26413 | 2026-08-11 03:51:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7aeb8ee7-a559-3a96-ae23-de9ec2ccceeb | -19.16992 | -43.46878 | 2026-08-11 03:51:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4491538-a58e-3306-a6d0-93cce2e8453d | -20.39043 | -49.30902 | 2026-08-11 03:51:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 4374b120-961a-3069-82ab-744ad9e220b5 | -20.09321 | -44.31715 | 2026-08-11 03:51:00 | NOAA-20 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d6805edf-cb75-3eef-8cb9-51f91be7f47b | -22.18743 | -43.24428 | 2026-08-11 03:51:00 | NOAA-20 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a704f849-f99f-3a19-a589-c929ab7e7c43 | -22.18371 | -43.2434 | 2026-08-11 03:51:00 | NOAA-20 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a79fe1d5-fdfb-377c-a84d-278e5d69e88f | -14.4539 | -45.6948 | 2026-08-11 04:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 6eca2a46-1250-3b04-836b-00d9fcaef75f | -4.2635 | -48.1799 | 2026-08-11 04:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| a7eaf301-396c-31c2-abf3-a93890b2672b | -12.4708 | -45.3077 | 2026-08-11 04:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| b50de096-cef2-3a65-b9a8-e3a8e7a54c4a | -14.6268 | -47.6506 | 2026-08-11 04:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 00692362-f66e-39af-8699-08c59be67501 | -12.4896 | -45.3278 | 2026-08-11 04:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 83295ea9-ad12-30ef-9298-5f78b8c7f565 | -4.2634 | -48.2016 | 2026-08-11 04:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| b2a259c7-e184-3425-991b-437149cdab3c | -14.1249 | -45.6368 | 2026-08-11 04:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| bdc6922e-86d4-3ce4-91c1-3eccf5242862 | -12.4905 | -45.2816 | 2026-08-11 04:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 64af7af6-a2e3-35ec-ba80-f173ebec2dec | -12.4703 | -45.3308 | 2026-08-11 04:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| b29440bd-a764-3654-8e63-e80b2f2f3074 | -12.49 | -45.3047 | 2026-08-11 04:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| b03ea65c-e282-3701-98e5-85a380a77f34 | -12.4703 | -45.3308 | 2026-08-11 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 5aba9ec9-f6a1-32b2-aed2-559025743b82 | -14.6263 | -47.6732 | 2026-08-11 04:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 3a9a7bce-316b-3069-8733-65f4c4257a99 | -14.6073 | -47.6538 | 2026-08-11 04:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 123.3 |
| dd3726fd-71e0-3ecb-be61-69661b58e097 | -13.5696 | -46.2813 | 2026-08-11 04:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 369.2 |
| 347fbe30-a5b6-3cfb-8e3a-1d4aec26ee30 | -12.49 | -45.3047 | 2026-08-11 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| b81839ac-ffa1-3afd-9a6e-604d66086c55 | -11.4514 | -46.662 | 2026-08-11 04:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| d561c4fe-a732-31a2-9661-2f7857147335 | -14.1249 | -45.6368 | 2026-08-11 04:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 95a2a48d-7121-3f8c-9efa-52f76c510ac0 | -13.5701 | -46.2584 | 2026-08-11 04:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 171.9 |
| 0ae1d0ef-ba66-3c85-8dcc-74bc49142788 | -13.5894 | -46.2553 | 2026-08-11 04:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| bcec701a-57de-3339-83c1-e8b18d422dad | -4.2634 | -48.2016 | 2026-08-11 04:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 1ab02e5c-305c-3eb9-94dc-86aadcd6d75b | -4.2635 | -48.1799 | 2026-08-11 04:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| a5c28530-2686-38dc-a0d4-232f0b2734ca | -14.6268 | -47.6506 | 2026-08-11 04:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 209.6 |
| 978959d8-4b31-3333-b02d-985e90d6e27e | -13.589 | -46.2782 | 2026-08-11 04:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 98.6 |
| bdb26671-5af3-317e-91a0-2ba44893fb10 | -13.5691 | -46.3042 | 2026-08-11 04:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 4a682673-183b-38ad-b9f2-b99c976f8be5 | -11.451 | -46.6846 | 2026-08-11 04:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 21591630-a1c5-3bba-883d-e6322fd1a322 | -12.4896 | -45.3278 | 2026-08-11 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| b7a65990-7846-3a7b-8036-a95059420e56 | -14.6272 | -47.628 | 2026-08-11 04:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 49.2 |
| a3ffbdc0-bf33-3e5d-8305-cb0761fcae88 | -13.55 | -46.28 | 2026-08-11 04:15:00 | MSG-03 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cece29e7-1be9-3b57-8afd-4fdd199c3528 | -13.58 | -46.29 | 2026-08-11 04:15:00 | MSG-03 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 72928a2e-fe49-3411-8152-2e0b372a31bd | -13.58 | -46.34 | 2026-08-11 04:15:00 | MSG-03 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b6b01489-156c-31a5-88d6-fdd60edd1503 | -13.5701 | -46.2584 | 2026-08-11 04:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 616288dc-e069-3b2d-bfaf-3a572f32ba7e | -13.5696 | -46.2813 | 2026-08-11 04:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 191.4 |
| 46323e52-aac9-3bb9-9cfc-437d3e4b9858 | -13.5691 | -46.3042 | 2026-08-11 04:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 74.7 |
| d7fe4ef5-cf21-390c-b831-59450d1033bd | -4.2634 | -48.2016 | 2026-08-11 04:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 270d3a5f-3511-3fff-8761-8c9a4073dd2a | -13.5502 | -46.2844 | 2026-08-11 04:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 23adb43b-9bea-3882-84b3-b07ef5960395 | -4.2635 | -48.1799 | 2026-08-11 04:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| b104c5c2-6ac6-319c-b245-74a9cd1c3610 | -13.5691 | -46.3042 | 2026-08-11 04:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 88160ec5-f391-3448-9845-0898f7b92d6f | -13.5701 | -46.2584 | 2026-08-11 04:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 138.5 |
| f632b8f8-2173-3314-8558-f8421c57d9a5 | -13.5696 | -46.2813 | 2026-08-11 04:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 269.0 |
| c5137b7c-f8fe-375a-8560-60056d4ec82e | -4.2635 | -48.1799 | 2026-08-11 04:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 5ee63f53-e794-381e-865e-00d9a0f4719e | -13.5502 | -46.2844 | 2026-08-11 04:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 477cc525-8d60-3bea-aaac-0bb1e50666fd | -1.74344 | -47.12907 | 2026-08-11 04:32:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 74af7764-9732-372c-a730-4c3fa6901134 | -4.39341 | -50.96899 | 2026-08-11 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 297c753b-530c-3aa4-b6eb-bba83ae4e9e4 | -4.26447 | -48.1897 | 2026-08-11 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 034254e6-20cf-32cc-99ac-4304fd8baf4f | -5.34339 | -45.16623 | 2026-08-11 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c63b630-3e78-3a24-bb28-08e517fc8fb0 | -4.3941 | -50.96474 | 2026-08-11 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be62af4f-7b09-3bcf-9d80-d2d513918485 | -3.02779 | -54.52632 | 2026-08-11 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4764ffbd-7496-3745-bea6-6479a7bd60be | -4.83825 | -49.8534 | 2026-08-11 04:32:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a67600b0-29c6-36dc-a6ca-b2f21e943cd6 | -3.0259 | -39.97894 | 2026-08-11 04:32:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 51e3b587-ee3d-3a94-af39-7f1842a72e05 | -4.40511 | -50.96652 | 2026-08-11 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 732d5b3b-cbfe-324d-802b-c5bb61b2584f | -3.00789 | -49.55066 | 2026-08-11 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 227ee00d-7d26-3e9f-9c25-f1d58c4ca3cd | -4.39638 | -50.9739 | 2026-08-11 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ee167cc-9ef9-3525-8dbc-b06842e9efbb | -2.50811 | -51.81675 | 2026-08-11 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a1a9f3e-0362-3ad0-abf2-070d79d147c8 | -4.40441 | -50.9708 | 2026-08-11 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ea021c3-6e59-3de2-b7db-4d50be9425ab | -2.49216 | -49.10789 | 2026-08-11 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f242d90-2eb9-3056-9677-6d6208e27da7 | -5.7392 | -44.50329 | 2026-08-11 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 035cdd54-8b58-3b4b-af91-0f20a4aadd30 | -4.45408 | -47.91407 | 2026-08-11 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 038c62dc-05ad-3c44-9b17-d5c7ee824540 | -2.9651 | -52.15214 | 2026-08-11 04:32:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1b8963d2-cc79-308d-a4f5-6ac559e3d400 | -4.26779 | -48.19022 | 2026-08-11 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 44f59a01-86a4-3ff2-a534-93b08c351c63 | -2.95899 | -49.26287 | 2026-08-11 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28daf699-c332-3674-acb7-88f0edd79ca7 | -4.26393 | -48.19318 | 2026-08-11 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 66524696-46ed-314d-9087-9f6b5c08cd6a | -4.21089 | -46.439 | 2026-08-11 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a146a202-d4c6-34c0-8887-a8be3af881da | -4.45354 | -47.91752 | 2026-08-11 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d898136f-712a-3a93-b805-555dd6dfb9c0 | -6.06853 | -45.44575 | 2026-08-11 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d371838-6afe-3648-8c55-66b57e43d8ff | -2.65324 | -54.62568 | 2026-08-11 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 641a37b6-6ab0-3b28-a0a3-5d4d1ead8185 | -4.21034 | -46.4425 | 2026-08-11 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 50ed9d7b-fb96-33b8-8aab-3a37adc42a26 | -2.96124 | -49.2709 | 2026-08-11 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d7ed32f1-5ae3-395e-b499-f4d0bde34bf3 | -2.96857 | -52.15629 | 2026-08-11 04:32:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac54a299-fb51-3abb-984e-3babaf4cadbe | -6.09792 | -44.32876 | 2026-08-11 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 861f4c4c-e311-38f2-a14d-6880ec7c25d0 | -4.26888 | -48.18327 | 2026-08-11 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 94a8e454-4df0-30d6-b209-dfaa408ed143 | -4.38975 | -50.96838 | 2026-08-11 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e510643-2d93-3672-afad-b8b72e42412d | -3.48956 | -50.05542 | 2026-08-11 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9294787a-adcd-33d9-b753-996f79dd12fc | -2.68942 | -48.70475 | 2026-08-11 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1f3e9b1-e4a5-32bf-bdb3-eb2510b900a2 | -5.50735 | -47.44098 | 2026-08-11 04:32:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6057a6f4-beb6-3175-ae0f-f135e0a1c5f6 | -7.1402 | -37.78115 | 2026-08-11 04:32:00 | NOAA-21 | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4dbf4b9a-69d9-351f-8bcb-7b8c69137465 | -4.26502 | -48.18623 | 2026-08-11 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 2cfb2c32-0c73-3386-8352-9ce10707688a | -4.97949 | -37.23556 | 2026-08-11 04:32:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d1639560-8988-3407-b38d-8b05f3d18eda | -4.21368 | -46.44302 | 2026-08-11 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 191b70d8-8ca9-3009-8e2a-172841c99a7d | -4.45739 | -47.91458 | 2026-08-11 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0a92b526-a613-3940-a0be-8aad892ce17c | -2.68884 | -48.70837 | 2026-08-11 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fce2f77a-614a-30b1-92aa-a187b670a14e | -4.5257 | -49.29993 | 2026-08-11 04:32:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |


[Clique aqui para ver as próximas entradas](README11.md)
