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
| 3261741e-618a-3179-a0dd-f45ebabc770f | -10.86853 | -40.42695 | 2025-01-06 03:53:00 | NOAA-20 | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c0b7a58c-d04e-35fb-8ae3-d04eb66f2e57 | -5.74341 | -39.35228 | 2025-01-06 03:53:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 67153209-356b-3ecf-93d7-d307311074f1 | -7.56143 | -39.00896 | 2025-01-06 03:53:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ba1c0c7e-66e6-38ed-9816-5fbb6b7f9100 | -7.81233 | -35.16953 | 2025-01-06 03:53:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ad21c882-6779-3f5f-b4a5-b056aafc455c | -7.55812 | -39.00844 | 2025-01-06 03:53:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4899bd3f-1700-3e82-9746-4bcc409607bf | -5.84893 | -35.4793 | 2025-01-06 03:53:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 853adcd8-d2aa-33da-a7b8-046eb8273c92 | -5.846 | -35.47477 | 2025-01-06 03:53:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e8d69632-dfc1-3723-a1cc-ce656c7112f2 | -2.764 | -41.80121 | 2025-01-06 03:53:00 | NOAA-20 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a690f75-2e5a-3106-a134-a9f2df8242fd | -10.87244 | -40.42396 | 2025-01-06 03:53:00 | NOAA-20 | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bdb86bdb-04d0-354c-8da4-1f8acf896abf | -12.77221 | -38.46001 | 2025-01-06 03:53:00 | NOAA-20 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 015bfe26-4da0-3a4a-afa3-1df4933e90ee | -13.40962 | -41.33307 | 2025-01-06 03:53:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| d9aebe95-e8b9-3812-b539-153210903796 | -12.76885 | -38.45947 | 2025-01-06 03:53:00 | NOAA-20 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4161d98e-14d9-3bd4-804d-d0aa7a4d78f8 | -3.66691 | -39.21689 | 2025-01-06 03:53:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f7d90dfb-1dc7-31b1-bf60-aabb41124dda | -7.5642 | -39.01297 | 2025-01-06 03:53:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4020835d-1f8e-3d00-b8f2-1cf81d42f862 | -7.5653 | -39.006 | 2025-01-06 03:53:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 85159c24-5727-3797-8468-f53ebcb1981c | -5.16417 | -35.53757 | 2025-01-06 03:53:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 228c0243-b7fc-3a0a-977f-31d0d5a1887b | -5.18631 | -37.63648 | 2025-01-06 03:53:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d479e697-945b-35ee-b4ca-ba420701da34 | -2.91407 | -40.45068 | 2025-01-06 03:53:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 997207ce-aa0b-3e8f-9422-50f801049987 | -5.84953 | -35.47533 | 2025-01-06 03:53:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3e5150cc-2672-3cab-970a-30d2fc303589 | -7.56475 | -39.00949 | 2025-01-06 03:53:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 387eb134-a142-31df-ad8a-d03a974beedf | -7.81379 | -35.23598 | 2025-01-06 03:53:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 08047c56-8363-30d7-8675-0250dac15c7d | -10.87187 | -40.42753 | 2025-01-06 03:53:00 | NOAA-20 | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2d980d49-7af6-3560-9a8e-5af0c73802d7 | -6.32079 | -35.05525 | 2025-01-06 03:53:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4b790d6f-955f-3b8f-9fca-1b5dfa17f98c | -2.86288 | -40.40533 | 2025-01-06 03:53:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b54e6d73-5e9f-3bed-a33b-864354e55424 | -7.0751 | -35.27948 | 2025-01-06 03:53:00 | NOAA-20 | MARI | PARAÍBA | Brasil | 2509107 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 605e5653-85cd-3088-b83d-7d1ca8427ac6 | -4.2954 | -39.27826 | 2025-01-06 03:53:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 833bf0e7-d6c0-37bc-aff4-03a9564a6762 | -6.04806 | -39.44404 | 2025-01-06 03:53:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 030f9232-fe13-32f8-9ddd-0424716c0a34 | -7.80865 | -35.16899 | 2025-01-06 03:53:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 2083d6ba-8f8a-3b27-8623-5a703c502f67 | -19.83888 | -40.08152 | 2025-01-06 03:55:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a71c6caf-ecf2-3efc-bc2a-01e86eb902a5 | -10.59669 | -37.01906 | 2025-01-06 03:55:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| e0afe5a2-53c7-35d1-804b-744e284d856e | -20.76192 | -46.77031 | 2025-01-06 03:55:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7d4470ba-d7ba-35c3-a864-4b613f99bf6e | -10.60015 | -37.01963 | 2025-01-06 03:55:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 6f92df85-6e84-34f8-955e-cf4f1e4f3bb2 | -9.70802 | -36.70009 | 2025-01-06 03:55:00 | NOAA-20 | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 37608ad7-912b-320c-991d-9b330dbefaa5 | -10.59727 | -37.01519 | 2025-01-06 03:55:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a57c4955-3263-394b-aa62-d07ad2a6c234 | -19.38169 | -48.3899 | 2025-01-06 03:55:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55354fac-1ecd-31cf-ab06-4dcbadecc5e8 | -10.60073 | -37.01575 | 2025-01-06 03:55:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| f47cc994-ab59-369e-9595-7898a7bf7cdf | -9.12382 | -40.20289 | 2025-01-06 03:55:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| af49892f-0559-3276-ad7d-4530cb8f792d | -10.58977 | -37.06525 | 2025-01-06 03:55:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 88188347-4d6e-367d-872d-83a5ae43bb89 | -18.51152 | -53.40605 | 2025-01-06 03:55:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ab177fe6-edfe-3207-8919-390b6e6bb0b9 | -20.34936 | -40.36136 | 2025-01-06 03:55:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6df1f035-a71f-364a-903b-dc23773985da | -17.03283 | -40.15778 | 2025-01-06 03:55:00 | NOAA-20 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ecb54629-fbf4-3ae5-a803-bbd2dd5bf6ba | -9.1244 | -40.19931 | 2025-01-06 03:55:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d7cd1dbf-ff62-30c9-917f-f809d50b0315 | -9.12718 | -40.20344 | 2025-01-06 03:55:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 86e31ad3-a546-3776-b0c3-eeb5968e25f7 | -9.12775 | -40.19985 | 2025-01-06 03:55:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 399f1419-ee6f-32fd-81d9-25e57ea903f1 | -27.22881 | -50.97529 | 2025-01-06 03:57:00 | NOAA-20 | MONTE CARLO | SANTA CATARINA | Brasil | 4211058 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 30031869-1879-3572-bcfa-2c9d5a1ff795 | -22.67533 | -42.85507 | 2025-01-06 03:57:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 840f2da5-b9b6-32e6-aa74-396ff1aaf58d | -25.57017 | -49.35863 | 2025-01-06 03:57:00 | NOAA-20 | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b0cb1ac2-14c1-31c8-97c9-d1751226d64c | -25.57104 | -49.35436 | 2025-01-06 03:57:00 | NOAA-20 | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4085c971-8076-3b91-b796-ce917143ab44 | -22.5393 | -48.81363 | 2025-01-06 03:57:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f41d61b-2fff-331b-956e-4910bc436b7f | -21.62488 | -43.46829 | 2025-01-06 03:57:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 356c3cc9-9fbf-3fd6-8fdd-c7472502fac5 | -20.99346 | -51.79616 | 2025-01-06 03:57:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e02368d1-89cc-32d3-8c75-6e1d6ff0f6be | -22.67473 | -42.85883 | 2025-01-06 03:57:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b7c6f688-c9f6-350a-8705-cfffd7577fff | -22.67785 | -42.85527 | 2025-01-06 03:57:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| d09dca11-d33d-3496-b6d5-6b97fd776d03 | -29.84933 | -54.93615 | 2025-01-06 03:59:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| fc159b8a-eafa-33ca-afdd-ac7584278b17 | -29.85647 | -54.93021 | 2025-01-06 03:59:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 2d76518d-fd77-3850-a822-4584472134b7 | -30.31961 | -53.41779 | 2025-01-06 03:59:00 | NOAA-20 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| 51812eee-c7e9-3316-a481-b0d2997e846f | -29.85027 | -54.93232 | 2025-01-06 03:59:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 73829d62-aed7-38ac-bb2a-7b661071fb8f | -7.81011 | -35.16956 | 2025-01-06 04:40:00 | AQUA_M-M | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 17c280bb-2316-3eea-8760-3b2e6145197b | -22.67528 | -42.85681 | 2025-01-06 04:42:00 | AQUA_M-M | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| d4ccc5e6-10a9-38df-9262-8326bba83d9c | 1.35325 | -60.03243 | 2025-01-06 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3b0288eb-c8fe-3307-a2f8-05a275d7e249 | 1.35389 | -60.03664 | 2025-01-06 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7cbb4924-ebb9-3b35-9910-b96e28c77de1 | 1.34733 | -60.03316 | 2025-01-06 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c614a92c-26aa-370e-92d4-03b98982fd97 | 3.49518 | -60.80679 | 2025-01-06 04:44:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 253cb951-7c07-39a5-995e-8960b78b8db1 | 3.5008 | -60.80058 | 2025-01-06 04:44:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c8d5a60-9998-3219-aad5-28df92ba0477 | 1.34797 | -60.03738 | 2025-01-06 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ea2eeb15-56fb-3642-ac2d-a7a064720a74 | -13.49944 | -53.61877 | 2025-01-06 04:48:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba3ba682-879e-3452-8305-2b3ce47007db | -21.55544 | -54.19774 | 2025-01-06 04:50:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff5359fa-572e-312b-b083-9e9fe2919d98 | -19.98133 | -44.09837 | 2025-01-06 04:50:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7816d57d-c83b-3e05-b05d-386ea2c9cd62 | -18.51719 | -53.3982 | 2025-01-06 04:50:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48fa63c4-9d02-3bf6-a275-26ac2492366e | -23.10056 | -55.17502 | 2025-01-06 04:50:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4c840255-ff45-3dc5-a882-9bbaba12b6d4 | -18.51331 | -53.40129 | 2025-01-06 04:50:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b609fcd4-2dbf-3977-a7a7-5a88fb0bfff4 | -18.51276 | -53.40493 | 2025-01-06 04:50:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b35745ba-59ef-30d4-8336-ff2c025a1e61 | -18.59362 | -53.16412 | 2025-01-06 04:50:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55005ec5-575e-3db2-adcf-54b848a58f37 | -23.77533 | -53.39166 | 2025-01-06 04:50:00 | NOAA-21 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5f9dc6d1-d21b-3ea4-ba2b-7c015c555a55 | -21.55818 | -54.20203 | 2025-01-06 04:50:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f124f4f-8782-32e1-88c5-5bf60851174a | -20.76323 | -46.77051 | 2025-01-06 04:50:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9c0392e3-7323-3f0f-ba10-5ed44677068d | -19.98094 | -44.10229 | 2025-01-06 04:50:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b772c533-500a-3adc-afff-2acbd1dae9c6 | -18.5903 | -53.16356 | 2025-01-06 04:50:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8b49bb3-ed3c-3637-b440-f09f9f564b70 | -23.10115 | -55.17128 | 2025-01-06 04:50:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8f278341-c28f-3020-a908-fc1deed73b59 | -20.47951 | -53.67633 | 2025-01-06 04:50:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 175cadb1-c355-3ab4-a833-51eb2efe1e64 | -21.56424 | -54.20689 | 2025-01-06 04:50:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c12724d-8de0-370b-8f5f-37125d63b524 | -21.6602 | -41.32617 | 2025-01-06 04:50:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 8017f6d4-304c-3bef-894a-0c8848ba97a1 | -20.9981 | -51.79276 | 2025-01-06 04:50:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 627de2ff-f0f1-3a29-a073-f7c61f7ca2fe | -22.85138 | -47.61964 | 2025-01-06 04:50:00 | NOAA-21 | RIO DAS PEDRAS | SÃO PAULO | Brasil | 3544004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 78e21ed2-ea01-39ac-b2e7-0dbd99a7828a | -23.70405 | -55.25251 | 2025-01-06 04:50:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f20a832e-7ea6-3759-98d0-8cbbbe1a34dc | -23.17591 | -52.40934 | 2025-01-06 04:50:00 | NOAA-21 | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6651dfef-128d-3b2b-9273-b7adad9d7c45 | -22.54194 | -48.81104 | 2025-01-06 04:50:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6c61dca-1e77-35ea-ba2d-0886caf4a26d | -23.17941 | -52.4099 | 2025-01-06 04:50:00 | NOAA-21 | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7a8a1763-9f1e-3626-a51b-50084d3794ee | -21.56093 | -54.20631 | 2025-01-06 04:50:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e64c521-cc55-392c-9709-1154310ca5dd | -22.85131 | -47.62081 | 2025-01-06 04:50:00 | NOAA-21 | RIO DAS PEDRAS | SÃO PAULO | Brasil | 3544004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f25e9dc7-7fa8-391b-b518-f0d00bb84317 | -21.5615 | -54.20261 | 2025-01-06 04:50:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf40c068-d19b-3c84-ba89-809cfc7da5b7 | -23.59635 | -47.43768 | 2025-01-06 04:50:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| af19ffef-d54e-31fa-ad62-f2e5f6868649 | -18.51663 | -53.40184 | 2025-01-06 04:50:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f14de4f5-91ea-3ebe-91db-5903c8048e0a | -30.46585 | -53.49957 | 2025-01-06 04:53:00 | NOAA-21 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 58cb3871-7d3f-359f-9545-9eb996bade72 | -29.74633 | -51.14346 | 2025-01-06 04:53:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| d221358f-8158-3a8e-852f-f2f3e406ec13 | -29.85631 | -54.92818 | 2025-01-06 04:53:00 | NOAA-21 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 2.6 |
| 468d0b97-a445-3d6e-a2e4-82877aaabc2d | -30.32326 | -53.41596 | 2025-01-06 04:53:00 | NOAA-21 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 6449b32c-b7de-30cd-8fe2-5943a1d71eb2 | -29.74587 | -51.14748 | 2025-01-06 04:53:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| a4bc27fd-fe3f-38b1-9c2f-8d5311826727 | -25.73291 | -52.1126 | 2025-01-06 04:53:00 | NOAA-21 | FOZ DO JORDÃO | PARANÁ | Brasil | 4108452 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a1c7cc04-74bd-385b-b8bd-e72f3caa5c91 | -29.85572 | -54.93237 | 2025-01-06 04:53:00 | NOAA-21 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 2.6 |


[Clique aqui para ver as próximas entradas](README3.md)
