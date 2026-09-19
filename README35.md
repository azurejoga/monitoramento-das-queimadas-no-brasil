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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6634f4da-6aa4-3884-86e3-68065fdb6155 | -12.9884 | -46.91833 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf25984b-c594-3575-8742-fb891077e439 | -12.3965 | -45.05142 | 2026-09-19 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d7aa406-b8c4-386b-bbd4-b61e42ef361f | -10.79983 | -46.64607 | 2026-09-19 04:04:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf66c62d-f642-31c8-82dc-00032f49f241 | -11.84218 | -47.44871 | 2026-09-19 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 730379a5-eaab-3ec9-b893-6670aec900dd | -11.05494 | -49.74302 | 2026-09-19 04:04:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1e7c9b0-6e44-3a5f-935d-f1eea8afd750 | -15.57605 | -43.13557 | 2026-09-19 04:04:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b0216b3b-53cd-339f-ada5-797b2bb48602 | -12.99294 | -44.83314 | 2026-09-19 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec828a1c-1bfa-3ae5-acde-c8fef52383fe | -16.83446 | -47.63917 | 2026-09-19 04:04:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c45070cc-7fa3-389a-831b-91c5152abdae | -10.79857 | -50.88918 | 2026-09-19 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42bf61af-2405-32d6-87e5-f68ad60ed6e2 | -11.06232 | -49.75997 | 2026-09-19 04:04:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e271c411-3dc3-3761-a296-72e95695571d | -12.14239 | -46.98679 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b1c67fb8-6caa-390b-a036-a5f380d2a308 | -13.68501 | -48.58514 | 2026-09-19 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62d7f17e-6571-34ad-8da2-5264e1a5f16a | -11.33548 | -47.36211 | 2026-09-19 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a7c7f06-68eb-3ac4-874a-a07b6b11d78b | -13.00569 | -46.96209 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f92f6504-c4d5-3de6-877a-93bd0718f5d1 | -14.67185 | -46.65534 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bcce5234-076c-34df-8297-117e3a163077 | -12.13416 | -47.00908 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5aab4c76-3430-393a-92f0-8ffec639cfd1 | -10.8583 | -54.10888 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d6af7be4-f4f6-321d-9c48-89cc836d3974 | -14.68648 | -46.66323 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0df5e109-73a7-34ae-9143-d98eae215eb0 | -14.79618 | -48.54401 | 2026-09-19 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b80b7065-6c44-3bd9-8e6d-5288d6547195 | -14.96106 | -47.53468 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6fb49ca3-7ca4-37b4-a2f6-9a6fb6a056cb | -12.13735 | -45.13816 | 2026-09-19 04:04:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18c4b02a-0a83-3b2b-8ba5-30b9d2a70fbd | -12.14106 | -47.01824 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3d65d196-ff4c-3224-bd03-f01ed6d20911 | -11.79383 | -46.80637 | 2026-09-19 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb035a09-62cf-3aec-b8f7-698cc17c1239 | -11.06511 | -49.76485 | 2026-09-19 04:04:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c37b046-52b8-3068-b6e7-f3aedacf2b14 | -15.58924 | -56.55891 | 2026-09-19 04:04:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3680de0a-cdfd-3a90-b80a-cfbcaa39dd88 | -11.43969 | -51.46838 | 2026-09-19 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f62ee8b6-614f-3ac5-b3ca-bf78e0c6c047 | -14.66706 | -46.65967 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d407b7f2-8729-39e6-a0b5-1ace15b72e9b | -12.38937 | -48.47541 | 2026-09-19 04:04:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| db479b24-efaf-329f-946e-9eec0a010440 | -10.88208 | -54.05873 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| de8a5870-82e5-3ecd-905f-49a6f6f7a9c5 | -11.12696 | -45.28981 | 2026-09-19 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a8bfb3f-1197-3d11-9ab6-df2c002b9dc4 | -11.07647 | -48.31076 | 2026-09-19 04:04:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7cef9fd9-1d78-38ba-a0b2-f9cf1e2b8518 | -11.11459 | -49.443 | 2026-09-19 04:04:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2dc3ad87-14d2-3f64-8e82-21f0be3efd1b | -10.83187 | -50.16317 | 2026-09-19 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3ea2fa2a-1106-3cba-b589-d695ebd12bc1 | -10.86525 | -54.09314 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 37b82f9f-5874-37f4-aa57-a71e4437e274 | -12.59747 | -50.88442 | 2026-09-19 04:04:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 718710ea-5fce-34bd-a69e-253defaf17c3 | -10.80494 | -48.11464 | 2026-09-19 04:04:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 48ade91e-2413-3093-950d-92777151c5ed | -11.37619 | -47.03321 | 2026-09-19 04:04:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76824f35-9ad8-3906-8c7a-9c12ef0c19e3 | -12.2838 | -49.17037 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| dd4f07ee-2f71-38ec-b1f1-27ebba30c4b0 | -11.4898 | -45.73714 | 2026-09-19 04:04:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17122b4f-38c2-348c-8efd-14225c6d0d79 | -15.05651 | -48.58345 | 2026-09-19 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87211b09-f155-359f-afea-ad8fed738da6 | -12.3216 | -47.39865 | 2026-09-19 04:04:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aeb1cec4-86a4-3e8e-bb58-b97aa0cd2c75 | -13.236 | -46.91659 | 2026-09-19 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a70ab676-f81d-3e7f-aedf-a8e052ad6fa2 | -12.54249 | -47.09075 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e7b4b09-f76d-3e03-936f-bb3ea93e284f | -12.97657 | -46.98387 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c099dabe-b818-393d-8ea3-7622322bedb5 | -10.98499 | -48.29419 | 2026-09-19 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 879e1c02-8dc0-3bd2-870d-2ab270cd8d8f | -10.8328 | -50.9183 | 2026-09-19 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a395f3d6-db56-3148-b261-34f90e376f13 | -11.05999 | -49.74398 | 2026-09-19 04:04:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36720870-1090-345a-bd44-cf20913081f3 | -14.676 | -46.67696 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 4def2ce1-899f-3583-9024-545c9b5c7623 | -10.80267 | -50.89746 | 2026-09-19 04:04:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8339f14d-81eb-35de-ba16-815f658ab71e | -11.67461 | -54.44279 | 2026-09-19 04:04:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e1e4d96-a69b-3216-9e47-5679e1961cea | -10.70491 | -50.2638 | 2026-09-19 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 42aa4420-c4f6-3f1a-b9f6-d5c24c2bced4 | -15.6731 | -52.73144 | 2026-09-19 04:04:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c17c3ab-9985-3a56-8a2a-b74fee23ed68 | -16.11956 | -51.94384 | 2026-09-19 04:04:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19ee6361-4ba9-3136-a3ae-be29905f9a99 | -12.12509 | -46.98816 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 582ae7e1-853f-39c3-ba8b-46a748c859de | -14.9317 | -49.9165 | 2026-09-19 04:04:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ed74520f-6eba-3ab7-b513-38e5755a15b4 | -15.02476 | -48.56001 | 2026-09-19 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f5137419-300d-3366-8bc6-95063fdeaed1 | -13.62567 | -46.96075 | 2026-09-19 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01fb3eb1-aaf6-395a-b146-9383d194f746 | -12.84154 | -44.39011 | 2026-09-19 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e6f4939-9978-321e-bcd4-e0fb41cb3aab | -13.2333 | -46.90842 | 2026-09-19 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1056818-2340-33db-9bad-a1efa5124127 | -11.43406 | -51.46733 | 2026-09-19 04:04:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10654dcf-a59a-3d18-ae98-3b26243a7d28 | -14.79299 | -48.58536 | 2026-09-19 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6c39c4f5-f8fa-3b35-84d9-9ba7aa3f1d6f | -16.12023 | -51.94053 | 2026-09-19 04:04:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52a2860d-6e70-3d1e-9dc9-74e67def96bf | -12.9772 | -46.98034 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b95ddb71-68aa-3b37-a31a-2e9474db5114 | -14.66982 | -46.66312 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2e95c285-f6fc-3d3f-b251-39fab600a89c | -14.79474 | -48.57598 | 2026-09-19 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fb620659-ca2d-3742-b673-89976d48f57f | -14.6707 | -46.65807 | 2026-09-19 04:04:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aa46bc04-3e3c-3562-80cd-2794ce121be5 | -11.31713 | -47.26683 | 2026-09-19 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a02f0867-4a6f-3014-8d1c-dc3d3a4d943d | -11.40974 | -47.2844 | 2026-09-19 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88389d57-9d0a-3ec5-b39e-4d7d9ae4ce2e | -11.32895 | -47.68098 | 2026-09-19 04:04:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 228d9a82-6176-39c2-a464-3bc2804c0ea3 | -14.18237 | -47.85516 | 2026-09-19 04:04:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e8d58953-2afa-3d21-8f05-dca62506f4c4 | -10.88568 | -54.06089 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7747b6fe-24ef-3a94-b225-115d98574794 | -13.64726 | -46.93901 | 2026-09-19 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 988aa946-b053-305b-b917-a4918cbd2535 | -15.58552 | -56.54273 | 2026-09-19 04:04:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 82fb4a4f-17bc-3807-a192-d267bb9caf01 | -12.41414 | -45.0362 | 2026-09-19 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adf4387a-b1c9-30f7-b1a4-9220cd291afb | -10.36861 | -48.89703 | 2026-09-19 04:04:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c28b6d2b-cbbb-3b0d-885c-d535f4480450 | -12.13833 | -47.00959 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 27f7e031-73ad-3344-ae5d-1498c569c575 | -13.60838 | -48.31459 | 2026-09-19 04:04:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e4d0ad67-7f24-3b71-ab2d-c30da80f473b | -15.67237 | -52.735 | 2026-09-19 04:04:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cd9ca89d-6114-35ae-8ce9-6bb8c12d1fab | -12.15809 | -46.97026 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49ac5b36-dc71-390b-b29f-17e47dc3ba7f | -12.48619 | -50.04546 | 2026-09-19 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 22b2efaf-5e61-38cd-b749-0a1b1c34349e | -11.87599 | -47.61735 | 2026-09-19 04:04:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72534c83-0041-3600-8795-fd0201a391f2 | -13.8778 | -48.59653 | 2026-09-19 04:04:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f5c1d094-c2f8-38f9-af83-99295671a2f3 | -10.974 | -49.75597 | 2026-09-19 04:04:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8a2b279-4a54-3c5b-9fd8-b835ec7f82fb | -15.02587 | -48.57832 | 2026-09-19 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b61e4069-9556-353f-876d-1c7111d024ef | -12.12651 | -47.00409 | 2026-09-19 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 268f3287-917a-37ee-a076-9d51a80f4bb0 | -10.84914 | -50.1866 | 2026-09-19 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8eab117e-de2b-300c-ad36-1fee149193e8 | -10.99379 | -48.32491 | 2026-09-19 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8d89f236-ff14-31cd-87f5-ac6286935158 | -12.53433 | -38.96655 | 2026-09-19 04:04:00 | NOAA-21 | CONCEIÇÃO DA FEIRA | BAHIA | Brasil | 2908200 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a9eb8ca4-df93-3e61-8776-bf32906bd90c | -10.87978 | -54.0703 | 2026-09-19 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b4325f2d-c96a-3048-af3e-33ce8f0fec32 | -13.59056 | -46.94791 | 2026-09-19 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d54f0297-5932-30d0-bc23-bb3ce92f98f7 | -12.34227 | -50.71928 | 2026-09-19 04:04:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3b020dc-dcfc-3ebe-a6c0-25332d045b72 | -16.88256 | -50.58137 | 2026-09-19 04:04:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 46db3ffd-1b4d-3b5a-b71e-eef7147d1a1f | -16.88844 | -50.57676 | 2026-09-19 04:04:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 3b9d6cdd-de12-3672-86c5-cb02ee9dc385 | -13.63521 | -46.92978 | 2026-09-19 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f137b68-4a1e-33bd-88bb-0a0abe3d48d9 | -11.05781 | -49.756 | 2026-09-19 04:04:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1317e745-7140-3fee-b69b-e5701ae44f41 | -11.419 | -47.28185 | 2026-09-19 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3773df5f-3c60-3ea1-8348-b5d1bd4ddf87 | -12.86302 | -46.33384 | 2026-09-19 04:04:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fe6e7218-563b-3fc6-a962-9ab5c4a273ee | -12.99665 | -46.989 | 2026-09-19 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 60f86614-ab57-3822-98b5-5c9bb2b4a359 | -18.6796 | -44.61319 | 2026-09-19 04:04:00 | NOAA-21 | MORRO DA GARÇA | MINAS GERAIS | Brasil | 3143609 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b95798a-6180-310c-9e30-0a977a993ec3 | -13.62221 | -46.95678 | 2026-09-19 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README36.md)
