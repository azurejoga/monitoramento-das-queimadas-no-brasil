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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f89e01f9-cbce-3a73-a339-e3ef6b95188e | -15.70828 | -41.92836 | 2025-08-23 04:53:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 5a318f8b-34e7-3ebe-a8b5-c09fba31a70c | -12.50263 | -53.82262 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6e1ed09-d779-3d49-8786-5a1f53980476 | -13.41717 | -46.25871 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cbba6d95-4865-3ea3-b2f6-be87b318d939 | -14.57674 | -54.50036 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8641d35d-785b-38ef-82ed-0505035bfb66 | -10.46679 | -59.1346 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ef36e92-1424-30dc-abfa-6510452d9b1d | -13.37696 | -46.2065 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 823032cc-9dd2-3817-a30a-8892ad64b9b8 | -14.60917 | -54.79364 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ecccd5f8-4295-305d-a92c-ff04040091af | -11.78541 | -46.41207 | 2025-08-23 04:53:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae5b67f7-85e9-3e76-ae0b-3b5e22072108 | -14.56902 | -54.50637 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb552212-b771-347b-b02f-740afcbbb948 | -15.07082 | -48.49183 | 2025-08-23 04:53:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3bdcda30-752b-3cec-a82a-af04b644ed57 | -13.42126 | -51.79481 | 2025-08-23 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50a671bf-a865-37c4-be66-45f242c8b22d | -14.28416 | -60.38837 | 2025-08-23 04:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| df001080-c2b1-3267-959a-5c68203412cc | -14.27055 | -58.52967 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| debc0a34-1dab-3086-a731-119e7ccf2858 | -15.03595 | -56.38015 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a4062cf6-940f-32ed-ab36-be6713a28622 | -15.02628 | -54.88806 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1ac58366-8bac-3b0b-bafa-13e144c7b695 | -15.54391 | -55.01399 | 2025-08-23 04:53:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a24d2f2e-2e52-3efb-933f-24baa5f4c7f3 | -14.65811 | -56.6062 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba55c044-a215-369e-a2bd-7478675f36fb | -17.2732 | -46.76177 | 2025-08-23 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef3697c4-8716-3971-8ed2-e68be78b2996 | -12.70476 | -48.10512 | 2025-08-23 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dae1562c-ff65-36c9-9e2f-9b8d116eae8e | -9.95289 | -60.1738 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3ce426b1-bbfe-35dd-a860-887fa77eaeae | -13.44193 | -57.17008 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8aca4596-2be3-34ab-a6d0-daf3e08d06f5 | -11.18768 | -55.01989 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6c15bac-c5b5-3974-bb71-2f722f9dd518 | -16.61841 | -49.41612 | 2025-08-23 04:53:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3383f5ae-f198-3340-8b6a-9d6d3530198d | -15.03564 | -54.89324 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2479ef99-2ea7-36aa-bd06-0a244a74b840 | -14.94401 | -48.00916 | 2025-08-23 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6595ee1-da12-35d4-8575-de17305f34c1 | -14.62563 | -54.84003 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a7688af-8ac5-3870-aa1b-a3e02fd90eb4 | -10.46177 | -59.1333 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51827063-824e-346c-bebb-a62100ee1040 | -13.38145 | -47.51363 | 2025-08-23 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 28032202-74da-34f2-8c5f-62245c4e458e | -11.65397 | -51.5844 | 2025-08-23 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58208a8e-0294-32db-bf7d-bf04bb2bccde | -9.51137 | -60.52254 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b9d9155-bf15-3b11-8f96-4ab699b36927 | -13.00186 | -45.22989 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9707aeae-88c9-3996-88de-ba29d1e86a39 | -9.24119 | -60.47573 | 2025-08-23 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f2aa22cf-f422-3a6b-84db-b923c44a9cb8 | -12.58638 | -60.35326 | 2025-08-23 04:53:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f86ae413-3cd3-3588-8f2d-5ccf628b2d67 | -13.37527 | -47.48998 | 2025-08-23 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 51fbe6ee-52c6-3fcc-a420-d716c6f7d25d | -16.42195 | -48.89941 | 2025-08-23 04:53:00 | NOAA-21 | LEOPOLDO DE BULHÕES | GOIÁS | Brasil | 5212303 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7527510e-c105-3815-ba65-5264bc06b6aa | -14.7664 | -45.38439 | 2025-08-23 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a7e67690-3d85-39c1-993b-436c68d027b8 | -8.69721 | -62.88047 | 2025-08-23 04:53:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2aed9039-52db-3504-afb2-20296c03bdf1 | -13.42782 | -57.16769 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1291612-8d81-3ae1-a6d5-5b783cf3d419 | -9.95664 | -60.18513 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 5f42ce3b-0f5b-3da1-9667-0de5e83c16e2 | -11.31848 | -55.20444 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23267dd7-f13a-3df2-8f22-3133b33da870 | -11.18537 | -55.03423 | 2025-08-23 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 867116c0-b7da-3133-895f-c3d4508fea56 | -14.41234 | -50.41466 | 2025-08-23 04:53:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eed8c01b-f2b9-3dd2-b674-575aa504d604 | -14.61244 | -54.81602 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e981cb48-07ee-3017-929c-379bb70ee098 | -13.03097 | -56.86401 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 240f0f3c-6d40-3242-83fa-5a5a8e10d071 | -13.3702 | -47.49355 | 2025-08-23 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8c22c77d-3d3d-3bcc-84bf-ceaefd71342a | -12.70712 | -48.10318 | 2025-08-23 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 64865aa1-9392-3105-b912-76b199d4b6bd | -13.18754 | -59.17313 | 2025-08-23 04:53:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42f7fc17-9926-345f-8472-7b82779b9f7e | -15.06982 | -56.39322 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a1f5335-1b4d-31a5-a72d-02db06a0e935 | -14.97295 | -54.55498 | 2025-08-23 04:53:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5065b9d2-7e0d-379c-aa1e-c256213e36ef | -12.49987 | -53.81857 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 321130d2-aee7-3753-8d17-ee51b17d1704 | -14.61687 | -54.80946 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 64cd7aad-d982-3de6-92db-7bd70ad283c5 | -14.66472 | -56.58733 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 24c719b2-4dae-30d9-abeb-1751db07fb28 | -13.43134 | -57.16827 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8f2959d-6777-3005-a3df-eaacd65dd003 | -14.77321 | -59.6585 | 2025-08-23 04:53:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ea03211-2a14-338a-ac8a-082359dbe1a2 | -14.61467 | -54.80183 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7efefe9e-0ebf-3a55-95a0-1d42d9d223a7 | -8.87091 | -62.42519 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bd32981-0f18-3506-8097-80de4cd935ec | -14.8569 | -59.61785 | 2025-08-23 04:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce6567e2-1309-3a73-9fb4-f6255280e927 | -13.43702 | -57.17764 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 953341e8-b6ef-3aab-93cd-00281024487d | -12.54707 | -45.62682 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d5b6b85b-4ac7-3be1-a4b9-9e112e7c84de | -13.17594 | -46.91606 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f4241bee-9246-3f7d-ba11-090d3012886b | -14.61136 | -54.80128 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c862d11-3b08-39e7-a0cb-8565a1d2b9c1 | -13.42331 | -46.24957 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c06fde51-7d2c-3c48-a547-07b27b0f5bec | -14.64754 | -54.91654 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d97858f-91b8-3e44-b0f2-484ce1232dc8 | -14.67458 | -56.61274 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 20a847a3-7207-3acf-aa05-80ea936f84e0 | -14.75377 | -55.40617 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51034eb2-bbac-33d7-ba45-c059aeb850f3 | -14.26153 | -58.53747 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d794d6c-82e3-345a-bbd3-d3ffc488d10e | -14.88194 | -47.95877 | 2025-08-23 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71ced30e-b94c-3807-a11d-381b5aa25a2e | -12.99543 | -45.23901 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a81819cf-267b-3876-9f27-796cfb9d8483 | -9.52381 | -60.55904 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 72f5ada1-4423-3c6d-a40e-fbf14393baa7 | -9.95337 | -60.1965 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 222.7 |
| 17ae6231-393e-3bde-a325-b2262ae39b52 | -8.89665 | -62.43056 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cbb9d8a8-c34a-34d8-be90-5ba45bd05385 | -15.20326 | -48.25936 | 2025-08-23 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ebbabcb2-8e8a-3b9e-bcd2-2da59b0fb540 | -8.90185 | -62.43419 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7d315606-945d-3e69-aee5-948acc904cd2 | -12.85593 | -60.16233 | 2025-08-23 04:53:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a75b55ac-a9f8-3182-a588-4a82272bea45 | -11.18156 | -55.01522 | 2025-08-23 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 046879cc-db82-3ed3-aa22-2120930e5811 | -13.14127 | -57.12075 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2b320aa-bd89-32de-99d0-807d049be51a | -9.95257 | -60.20092 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5c136352-0c00-32ef-ab5b-dc4cbccd8b61 | -11.30704 | -55.14697 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 689a0b80-42bc-30da-ad2c-65e08195782a | -12.18607 | -47.21203 | 2025-08-23 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5db4b5c-ff4d-3ef3-8b92-236b6fb5fe7e | -13.02552 | -56.87532 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e36b4b9c-77a6-3876-aaf6-501cafc6b423 | -12.94171 | -46.29621 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 27304829-67db-35f6-8de5-453c4efb4c80 | -12.94037 | -46.30662 | 2025-08-23 04:53:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 21364170-6658-3ffc-a492-7fd004ed947a | -13.33168 | -54.39466 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a74341e-111e-38e3-ba7c-a710d8bb40b0 | -12.49875 | -53.80392 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1679712a-dc07-397a-a6d4-205fc5681aef | -13.80255 | -52.86913 | 2025-08-23 04:53:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c668988-8e33-3400-ba65-4446a8ddb1e5 | -14.6609 | -56.61057 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dd317b43-21b0-3af2-bdda-51c9361cf287 | -15.6502 | -52.68451 | 2025-08-23 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31502ba9-dbcf-339b-b40f-83975404eaa8 | -11.32566 | -55.22416 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f72f12a-caf5-3be9-92bd-9a9b6ddd2a66 | -14.38395 | -52.05971 | 2025-08-23 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd7acb53-7663-377d-93e4-971ee06bba75 | -17.26696 | -46.77354 | 2025-08-23 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 8d4c1f5b-885b-3746-9df6-d705c8fea75a | -17.268 | -46.76463 | 2025-08-23 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52acc52d-846e-36f4-9a93-f0d8c4d383c2 | -14.38277 | -52.04317 | 2025-08-23 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 763a6636-cc52-32f8-ad09-ec4f2feb4352 | -14.66287 | -54.86418 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51f796e8-4039-3c8a-8274-17b637d78b1c | -14.29872 | -58.55243 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76e63a2e-847e-3122-8f53-aefec70ab4db | -14.65336 | -54.92456 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 087a6914-44a3-3eef-810c-d04495aab14c | -16.51373 | -46.73464 | 2025-08-23 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a916e33-973b-305d-b29f-720a395895ce | -13.4207 | -46.27082 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| c6f17c5f-3bd8-346a-9d56-b90a1367764d | -14.29499 | -58.55176 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89498bdd-b89d-3fba-9664-4cd586064b48 | -12.95851 | -46.3026 | 2025-08-23 04:53:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aa1f1afc-9db0-37b9-b37d-86d7faad3bb3 | -11.19656 | -55.02868 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README51.md)
