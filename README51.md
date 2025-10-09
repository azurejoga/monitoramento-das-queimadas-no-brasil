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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc488e16-41c1-310c-a6d0-fa1898413c1f | -16.69999 | -47.59629 | 2025-10-09 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f22e4ba9-1cc5-3977-869d-dce371615c98 | -17.93978 | -57.54037 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d8da82f6-b92e-3da3-ad7e-554f090b4c20 | -21.10384 | -47.84435 | 2025-10-09 04:21:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf7874c6-6acc-3427-9ef6-cf63fc981a63 | -14.97368 | -46.29582 | 2025-10-09 04:21:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| af4b1362-19af-3da4-aced-eab64fffe2f9 | -18.04007 | -57.52544 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fbfa60e1-3bd8-3a23-96a0-7a8a82c0483c | -14.91207 | -46.81507 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e7dc1d5-5241-3a98-8242-b50ef3044ea1 | -16.08364 | -45.791 | 2025-10-09 04:21:00 | NOAA-20 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e21615fb-52c5-3968-bad4-0d8cfbd93d52 | -16.28202 | -47.1291 | 2025-10-09 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4d4a9e84-b1be-3099-bc0a-746c2ddd2224 | -17.24235 | -46.94137 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 699c6e1f-7253-3fc3-abdf-74f171a2db57 | -18.92986 | -51.73575 | 2025-10-09 04:21:00 | NOAA-20 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 25c7fc6b-beb2-3e8e-b576-44734638961a | -21.21071 | -47.76804 | 2025-10-09 04:21:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db4981cd-56e2-39e6-9e23-fc6dcea903b1 | -17.37727 | -46.88303 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dd712a02-8e1f-3858-a126-a926e9f294a5 | -15.99518 | -59.55566 | 2025-10-09 04:21:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ae494e0-d8b1-3c0c-a78b-44bb7a5aa489 | -18.04034 | -44.70554 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f2ef5f88-f906-3c4f-b772-8dd89e154a7e | -16.3966 | -46.35741 | 2025-10-09 04:21:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73cf430e-355e-3063-9d2c-afcb5c50fdcb | -18.39359 | -45.24464 | 2025-10-09 04:21:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d8eb624-2e3a-3bd9-9718-44c26a17f045 | -15.91019 | -48.33264 | 2025-10-09 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00633826-7410-3d6f-92d3-22c4022c5eae | -17.92951 | -44.60123 | 2025-10-09 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ce8c5e7-d8d3-3d71-a226-f5144624bd3b | -16.59756 | -58.16555 | 2025-10-09 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 85bff6da-deea-39b3-a5f8-31d4712cab10 | -15.81806 | -43.78207 | 2025-10-09 04:21:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| baa1d87e-c0ba-319f-9bc4-c1a35e4555c8 | -17.56152 | -43.52208 | 2025-10-09 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71604be0-d842-32c1-b2fc-783878df2196 | -15.47522 | -47.95278 | 2025-10-09 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d29f7bf2-10e8-37c8-badd-f54dca62c32f | -17.53145 | -46.05792 | 2025-10-09 04:21:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 833d99d0-9609-3a0e-9aec-d526fe3e6728 | -15.07779 | -46.60516 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 76b72b4e-55f2-332a-865d-f96f424c43b3 | -17.37277 | -45.0817 | 2025-10-09 04:21:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0852b8f-6f14-393d-b531-e825c03ef729 | -16.71313 | -49.75125 | 2025-10-09 04:21:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20752236-40a1-3531-8851-025b23bae75f | -17.32939 | -46.84158 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86b4c1cc-efdb-342b-b715-35855d4e9aca | -20.30124 | -49.69265 | 2025-10-09 04:21:00 | NOAA-20 | AMÉRICO DE CAMPOS | SÃO PAULO | Brasil | 3501806 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 85fa28fc-4d7d-3d3f-bc0b-876b9e6236ab | -20.55796 | -54.65764 | 2025-10-09 04:21:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45158358-d171-3eb7-8abc-15724bf17307 | -18.03886 | -57.52604 | 2025-10-09 04:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 662eb089-a11d-349a-977f-16e44950e19e | -17.6252 | -47.20555 | 2025-10-09 04:21:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 86ccacf8-2238-3d24-9653-ad8749908d02 | -15.49695 | -45.34542 | 2025-10-09 04:21:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66d5fe5b-2a3e-32eb-a3fb-7e3761659933 | -15.48584 | -46.85967 | 2025-10-09 04:21:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0113e5d4-a833-3967-b82e-a1a6a3524c88 | -22.32654 | -49.86855 | 2025-10-09 04:23:00 | NOAA-20 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| dc1eae1c-5379-3513-98df-9ba900f9a003 | -22.31408 | -49.92237 | 2025-10-09 04:23:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a53e1f86-9455-3465-99f2-fa27cada3290 | -6.6995 | -46.2946 | 2025-10-09 04:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 54cb715a-0c59-3cd7-8a62-badff1adb7f6 | -10.8558 | -44.6199 | 2025-10-09 04:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 53c778e2-5204-30f8-8c37-414e92a43882 | -17.9224 | -57.5128 | 2025-10-09 04:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.9 |
| be9da263-11f0-3332-bb31-7683ce8c1f74 | -6.6808 | -46.2961 | 2025-10-09 04:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| abc626c7-0e18-306c-a4a9-8cadeb416694 | -8.1993 | -43.3424 | 2025-10-09 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| 4aa34716-3c6a-34b8-a4c0-7c90a49f8a85 | -17.2705 | -46.9627 | 2025-10-09 04:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 78a1bdd6-f719-37bc-b5bb-5d917b745a2c | -17.9227 | -57.4922 | 2025-10-09 04:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.6 |
| 9ffd7cf1-79ef-3277-876e-d6e612ec4a58 | -0.04954 | -51.17926 | 2025-10-09 05:08:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8f4cd4e3-6b85-3af9-b6d7-b2adc63d2ab9 | 0.90711 | -51.12203 | 2025-10-09 05:08:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58c53abb-1dd0-308f-95f4-fc8e2a534a9c | 0.90005 | -51.12826 | 2025-10-09 05:08:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 153d522d-9deb-3b8a-8f9e-fadb417703fc | 0.89691 | -51.13385 | 2025-10-09 05:08:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9058c056-d72e-3b95-8303-0607aba42ad8 | 0.88671 | -51.14562 | 2025-10-09 05:08:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1e60424f-daa4-3270-b22d-fe452d324dde | 0.89613 | -51.12886 | 2025-10-09 05:08:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| de3ed01e-d148-3486-b5aa-4dbcb47e972d | -0.9061 | -47.54894 | 2025-10-09 05:08:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a5a8421-c714-3204-be0f-3f891c8d0fa2 | 3.54407 | -51.78082 | 2025-10-09 05:08:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5ba3fbe-7e72-33a2-b2f5-55fac389bf81 | -0.04854 | -51.18044 | 2025-10-09 05:08:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 320bfe42-0a69-3788-bfe5-a45782cf56ac | 0.89608 | -51.15431 | 2025-10-09 05:08:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| baad7ff0-9a2d-3dfb-a064-5a2605e0149c | 0.89286 | -51.21058 | 2025-10-09 05:08:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| aab69ab9-5575-3ec1-bc57-b687d573a5c0 | 0.89999 | -51.1537 | 2025-10-09 05:08:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 28049d6d-f394-3208-a153-5cf213a6b088 | 0.89299 | -51.13446 | 2025-10-09 05:08:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 58e4cc3c-9376-345b-b70a-2989d47bee4e | -5.64775 | -43.60685 | 2025-10-09 05:10:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c9a7f49c-16fa-3b36-947b-b2cee04fc2de | -3.13886 | -49.03424 | 2025-10-09 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b1085697-c59a-36ad-8aac-c0afa7dd2a04 | -3.10769 | -47.79324 | 2025-10-09 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8ab8cfb-a749-33e6-be75-b8fcfc24f2fc | -4.72256 | -43.35295 | 2025-10-09 05:10:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f314218c-f28b-333c-9023-670b04447fbe | -8.22669 | -44.15649 | 2025-10-09 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b53f9926-8bc4-3af1-b9b6-bfa471e1e465 | -2.17114 | -54.47705 | 2025-10-09 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d504c457-6193-3e97-b46f-e954971761ac | -7.78739 | -50.21845 | 2025-10-09 05:10:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8a2bebc-2c25-3011-b053-4da8a80b5634 | -3.16157 | -49.17594 | 2025-10-09 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1094bf7b-d4ab-3571-9319-72470132e570 | -3.38763 | -49.04324 | 2025-10-09 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 588cf91a-e023-3968-82f4-1d6099fca082 | -5.6407 | -43.6058 | 2025-10-09 05:10:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 297a0d50-9e1d-3485-88a2-d28a3b0bf6c8 | -3.39583 | -50.14608 | 2025-10-09 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d264b3f-6665-379e-aeed-90030804caef | -5.45663 | -47.4423 | 2025-10-09 05:10:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 05fb4893-0123-3921-98af-4088c5b492c1 | -4.81467 | -46.8175 | 2025-10-09 05:10:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7eb89ae-3e93-361a-98c7-79ede84b4979 | -4.42934 | -47.75527 | 2025-10-09 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f67774cd-9b1e-3a8e-ab99-a065566e8040 | -2.38349 | -47.70965 | 2025-10-09 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be03f188-6d75-39d2-9d8b-d69e1d1dbbbd | -4.68713 | -45.84145 | 2025-10-09 05:10:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4430e2d-fe6d-3f15-a5d1-71413a06ba66 | -9.68532 | -48.38788 | 2025-10-09 05:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78990aec-6872-3381-be95-5f21684cd3f2 | -5.74026 | -44.3283 | 2025-10-09 05:10:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0d78d9c9-12b6-347e-9bdb-cab78f9f185f | -5.04382 | -56.22721 | 2025-10-09 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e827ae2c-c0fe-3427-b4c7-e51cf5874efc | -2.18367 | -54.46383 | 2025-10-09 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8dffe23e-7e20-38cf-a7f7-be97532daf86 | -3.11245 | -47.79724 | 2025-10-09 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e34a0bdf-711e-3137-960c-33a93a43c692 | -4.8165 | -47.34444 | 2025-10-09 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7fc01e67-daa7-3526-adfd-01986a3f4181 | -5.04436 | -56.22372 | 2025-10-09 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 954387fd-63fe-34eb-97b8-5d175134ef84 | -2.18822 | -54.47967 | 2025-10-09 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 57af879f-423c-3a3f-a1f5-3a79b41df6db | -4.34035 | -49.88693 | 2025-10-09 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| af08f27f-954e-33b5-975b-b1bd668ab601 | -3.39137 | -50.14539 | 2025-10-09 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 52427617-fd7f-396b-906b-9025265495c6 | -10.19779 | -44.56793 | 2025-10-09 05:10:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 30ac4842-ff69-3b6b-8aef-1359174f4289 | -5.33387 | -45.51284 | 2025-10-09 05:10:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 53243418-5ae4-3754-ae59-a79e0ed5e6bd | -4.27431 | -48.88049 | 2025-10-09 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c7422998-d4fb-3821-b16c-000c6a9930bb | -6.68605 | -46.30447 | 2025-10-09 05:10:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 324df717-90f0-3882-b4cd-8b3a723463ab | -2.1905 | -54.46487 | 2025-10-09 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9cf4c246-0e73-38df-98c5-ab0b4cd74d39 | -7.36474 | -47.04902 | 2025-10-09 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eee72281-ec72-320b-9696-bfca377f6162 | -6.16695 | -43.76104 | 2025-10-09 05:10:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9d2e346e-4d88-34b8-a841-48590f77fc2c | -7.17189 | -60.06378 | 2025-10-09 05:10:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40c99ac8-f347-3dae-8ed4-8c7461146957 | -2.38302 | -47.7128 | 2025-10-09 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bba2a32e-2a9d-3e6e-b538-9649eeedf804 | -4.03659 | -49.49454 | 2025-10-09 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37e6e5f2-a569-31c4-9c8d-1d007ce250b6 | -4.23088 | -47.78361 | 2025-10-09 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 28a89ea9-a7e3-325f-bd78-2856ec533cc7 | -3.07375 | -49.10871 | 2025-10-09 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f86cdcc-7e63-3f0c-b71f-7c5516ec8969 | -2.18766 | -54.46064 | 2025-10-09 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95f2d6c2-6793-3b05-affe-b3bb7e2b7f8b | -5.31657 | -45.38108 | 2025-10-09 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 003d6166-ff66-3d3c-b9b9-0cf76f761569 | -7.80623 | -44.20386 | 2025-10-09 05:10:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 375870c0-6e90-3ed9-b401-5db18964b37a | -4.82207 | -47.34502 | 2025-10-09 05:10:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5544a9fa-a17b-3dc0-a0c4-8d5c06b6fd0b | -6.79516 | -50.48846 | 2025-10-09 05:10:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 355db6fb-2152-3df7-8e7f-e345e09a6933 | -3.09857 | -47.01369 | 2025-10-09 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c0f5f84-1071-39a9-ac79-7ab0234e7302 | -3.15681 | -49.17524 | 2025-10-09 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README52.md)
