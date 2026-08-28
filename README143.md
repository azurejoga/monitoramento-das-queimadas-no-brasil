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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e493ee6-092d-39de-a50a-43cd7874b45b | -14.89008 | -52.62432 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 8042bfd5-f193-3715-ba41-b37d0d7b4ad6 | -13.55464 | -52.61563 | 2026-08-28 17:45:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 96076875-7a15-3913-96f6-e2bfe3e8a183 | -13.46182 | -57.04523 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 04d3e5ee-4195-3718-ba72-3795cc416192 | -14.65726 | -56.99218 | 2026-08-28 17:45:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 670f7d9a-f913-3fc5-b42a-918a65b3f581 | -13.42266 | -51.7695 | 2026-08-28 17:45:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0a8de9bf-0bce-3fb6-af7d-7d1ca6457a0f | -10.51515 | -59.63071 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 354f116f-dd1f-3a7f-b76f-abdd14b402f1 | -9.43452 | -51.69903 | 2026-08-28 17:45:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c5ba3bda-741a-3700-b8ef-dbac479c64ae | -8.66863 | -49.54539 | 2026-08-28 17:45:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 72eef854-5bea-3f44-abbd-5d3ecc62ba52 | -10.72297 | -69.65363 | 2026-08-28 17:45:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 04bfb8ae-1dc2-3f06-94f7-61596512d1b8 | -14.91772 | -56.31893 | 2026-08-28 17:45:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| c8da3544-7916-307a-a395-345d146b1be1 | -9.10321 | -60.31497 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c4e5a00d-3a88-350f-9713-25a798aa84f8 | -9.39843 | -60.56919 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6d0b7a2b-2e62-336b-b3ed-e740365d9aaf | -14.44066 | -52.59944 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7b280bba-7bd6-3eeb-9b60-15df76c8f977 | -14.64183 | -57.0027 | 2026-08-28 17:45:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 9223094c-2ad5-35b4-ae46-bb9f39cbf569 | -14.18599 | -48.76689 | 2026-08-28 17:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 7c527709-eb2d-3f45-9c4d-5660d8b44cae | -10.48312 | -49.95088 | 2026-08-28 17:45:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5865b29f-6c7f-3b88-ae5c-6c82ce0c25d1 | -14.44005 | -52.59632 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 58937ab1-3f09-31ca-a574-2d28d33c8ffa | -9.10732 | -60.31834 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| c2d85bf3-7ba6-321f-9411-06eeda18a122 | -10.71978 | -69.62916 | 2026-08-28 17:45:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| acec8a1f-421c-38b3-a325-0ad1abe04f78 | -8.21227 | -54.95474 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 35bccdeb-f892-30fa-986e-76f0ff63d9e1 | -14.46584 | -58.51455 | 2026-08-28 17:45:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| ea219555-11ad-3d24-a74c-167f870ec130 | -9.2527 | -57.07847 | 2026-08-28 17:45:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| d851425c-fa13-3e50-a7e8-70a0d5b25fea | -9.19507 | -61.07794 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 98a52da2-e76e-3842-8d0b-207551fd7604 | -9.87145 | -60.2642 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5c1aa034-886a-32b4-8e58-d765dbfc070c | -11.00906 | -49.63041 | 2026-08-28 17:45:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b7b5f499-6bab-3510-816b-d548e28329a1 | -14.46482 | -58.52237 | 2026-08-28 17:45:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 79bb6714-7eef-3c3d-8d1f-24042730284f | -10.50928 | -64.51515 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 9311106f-4f3e-3292-8567-3a4f726dd1e0 | -9.88597 | -60.2658 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 778a64c6-a3cd-3c37-bcf9-16ab12f3553d | -11.2281 | -53.98018 | 2026-08-28 17:45:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 33683341-99f6-350b-b780-6aff98919a59 | -10.7577 | -53.97538 | 2026-08-28 17:45:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 45015f7a-f649-3e11-b442-f9a3501ed431 | -14.91035 | -56.32402 | 2026-08-28 17:45:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a36db893-b571-3b86-bc94-e45a76c1f0b1 | -10.48887 | -61.49093 | 2026-08-28 17:45:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 422b6305-6d25-36c0-b34e-0b1cbcf312d6 | -14.47654 | -53.26805 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6b4aa6cb-ab70-36ec-b78c-18ce6bddd182 | -8.76526 | -50.49596 | 2026-08-28 17:45:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 671e67af-6d6a-373c-99d1-cb2909a13e99 | -15.57245 | -56.28398 | 2026-08-28 17:45:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 221171d8-ba7d-34c1-8efd-e3b8ccbd4fe4 | -10.51698 | -59.62276 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 6875d35a-e494-3236-a5fa-33ba1e8f8cbb | -9.69935 | -65.07027 | 2026-08-28 17:45:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 35e1a678-a502-33a7-969e-e8992778d9f9 | -9.68598 | -65.07626 | 2026-08-28 17:45:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 1d68fd82-0167-3ea4-aec3-b8ce30b10fd7 | -11.35621 | -48.39466 | 2026-08-28 17:45:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 035c6cf7-0d3b-36df-ba79-845d0f7e57b4 | -9.10259 | -60.31105 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 930887e8-d6a1-3cd8-89f6-828f9311db04 | -10.25528 | -55.88074 | 2026-08-28 17:45:00 | NOAA-20 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 7d004e16-2442-3841-9b47-7a522d082149 | -15.57736 | -56.28855 | 2026-08-28 17:45:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 94e101d1-fe07-316d-886e-116280e990cc | -14.91646 | -56.31176 | 2026-08-28 17:45:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 9d25bf76-3926-388d-99dd-b3b46dcd0ce6 | -8.21873 | -54.95241 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3dacdef0-dacb-3ca6-b786-067ca42a4283 | -10.50386 | -59.62841 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 17e8065e-1a6e-3c07-b547-7f746a5d2e19 | -9.19461 | -59.569 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 56248ef4-af5b-329a-93cb-59d181331745 | -9.23178 | -59.40269 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e77c7c50-efdf-3abb-88a9-7a1e6091755d | -14.90835 | -52.60939 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 52513be5-f1e8-3ca6-9a24-753aa3db2340 | -14.46771 | -58.51759 | 2026-08-28 17:45:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 102511c5-9893-3d9a-8a7b-12c3797aec71 | -8.76486 | -50.49503 | 2026-08-28 17:45:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0dae3ad1-b606-3eb4-ba5b-5d1cf50b0bc5 | -9.92072 | -60.43772 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 5459b2ab-87a5-36c6-b1fd-40cf382c9fe9 | -13.87135 | -54.1179 | 2026-08-28 17:45:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 0898967e-fce8-3828-8518-5bf136df1e91 | -10.89404 | -50.49999 | 2026-08-28 17:45:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 372b747b-925c-373f-af1d-628c7d819ef2 | -14.86794 | -52.61934 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 996bdbd9-7b59-3ba7-9f09-37e50f064ae7 | -11.6906 | -54.59576 | 2026-08-28 17:45:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 9e887841-9a0a-3eab-8c04-115cc76cb656 | -12.92015 | -59.87827 | 2026-08-28 17:45:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a764281e-c12b-3787-b035-e7a83a28ad47 | -8.16583 | -54.95011 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| eefdb9cc-ece4-3812-ab2d-867f4131d6d1 | -10.90653 | -50.49757 | 2026-08-28 17:45:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 227e2e2d-61b9-3927-b17a-7646be62e261 | -14.65515 | -57.00282 | 2026-08-28 17:45:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| d935b54d-5933-3d38-803e-b091cbe20d3b | -10.05507 | -68.83222 | 2026-08-28 17:45:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 22.8 |
| db2f0d28-78e8-36be-9be2-8a4db8ffe53d | -12.14243 | -50.62589 | 2026-08-28 17:45:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d7f686a5-caad-3ba7-8b46-53f4f922aa9d | -8.24115 | -54.96447 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e7cdc4c9-850b-3999-868e-e55d36d717c9 | -10.20447 | -68.77876 | 2026-08-28 17:45:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ce82d4bb-88f0-3423-8f6b-3845c5c5c44c | -9.91666 | -60.43446 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 684e13a6-aedd-3222-bbdf-005564122e48 | -14.1899 | -52.84823 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c229d7cf-178f-3e9e-8736-1639f2cf584b | -9.01896 | -57.54193 | 2026-08-28 17:45:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 28.3 |
| f93e72a0-6e79-3efa-936d-d0b4f7ea8806 | -11.19901 | -55.09041 | 2026-08-28 17:45:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 98b6bbf8-bd94-3761-b8b4-c1965a27e3be | -15.57338 | -56.28928 | 2026-08-28 17:45:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 25ec5c23-8242-3540-bb40-4eed863e7e20 | -10.51254 | -69.0767 | 2026-08-28 17:45:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7e80dc5b-8cdf-399c-94dd-558ae237739e | -11.19932 | -53.99159 | 2026-08-28 17:45:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| f69345ca-4f85-312f-aa3e-19824b3abcd0 | -14.19049 | -52.85129 | 2026-08-28 17:45:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6ff71e18-9a87-3763-9f18-95b98b8b6e15 | -11.2462 | -53.99465 | 2026-08-28 17:45:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| ed93690e-04ff-32d8-8f8f-586eff243f6e | -10.50964 | -59.61903 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| a37d6cd8-9faa-3020-abb7-8d2a6ec463d9 | -14.87753 | -52.61424 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e2e7c174-401a-3550-be44-27c9d58492b5 | -9.86291 | -60.26555 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fde8669b-cad9-365f-a69b-3848b68b090f | -11.27989 | -54.03442 | 2026-08-28 17:45:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 7a23d695-9b50-3c43-9585-6b70bbb57368 | -9.87998 | -60.25081 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 497e167b-4a68-31d2-9cd4-7ed62a19e888 | -11.28543 | -54.04108 | 2026-08-28 17:45:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| d0ca7c67-cd2f-316e-9ddc-d07055433e9a | -13.8831 | -53.24541 | 2026-08-28 17:45:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 6eaabe1f-3791-38d1-ab0b-860facbdf4eb | -10.76171 | -50.63682 | 2026-08-28 17:45:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ea232811-ae51-3889-afe8-b8a7796b7f60 | -10.5064 | -64.51945 | 2026-08-28 17:45:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 1c42faed-a579-3d34-9205-2b10c6fa4be5 | -13.4219 | -51.76564 | 2026-08-28 17:45:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| acc17144-1193-3e76-846b-00515766994e | -14.87927 | -52.62316 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 1d4a9d6c-d622-31dd-9362-13935c1d51f2 | -10.5074 | -59.6278 | 2026-08-28 17:45:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 31287c56-efaf-3835-9b77-8555f43e7db8 | -10.2352 | -69.31381 | 2026-08-28 17:45:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f565d358-ecc0-3c00-a04a-f6e34e254583 | -10.83255 | -50.51704 | 2026-08-28 17:45:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3ed78ff1-ae8e-3b11-b823-c490a3f21fc9 | -14.8697 | -52.62833 | 2026-08-28 17:45:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 29eff5c9-5eb4-311b-b2b2-871e801910e7 | -9.26452 | -56.8943 | 2026-08-28 17:45:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a9a0289e-564e-372d-abd0-ef89f9c25245 | -13.26294 | -51.56615 | 2026-08-28 17:45:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c275e1d3-854c-31ed-a678-3ecc5f51c8a8 | -12.91292 | -59.89904 | 2026-08-28 17:45:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| f811b0e9-5dd4-387e-97ed-62fca954957d | -9.85574 | -65.02325 | 2026-08-28 17:45:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 77383465-6f21-33b5-aa5f-d16ad0755398 | -9.22231 | -59.7654 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 617ee6d1-d53b-3dce-a555-e4e45e6bd1ba | -10.31646 | -68.45978 | 2026-08-28 17:45:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 701ac96d-d84a-30ab-9cca-e2027b8a8b37 | -9.22429 | -59.77779 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 21f6c10f-53f8-3b00-b1f4-90dfef34fbef | -9.224 | -59.67245 | 2026-08-28 17:45:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 42ac8582-aaeb-3a5b-a87a-9d6f4823b24c | -8.2163 | -54.94869 | 2026-08-28 17:45:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9adefdc6-ee3c-3722-82a9-f635ef1aff32 | -11.86039 | -51.67101 | 2026-08-28 17:45:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| efc89b2b-0864-3fa1-a6e1-eed63fa61f0c | -9.21086 | -51.55315 | 2026-08-28 17:45:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1da9fd2d-fbfa-3bd4-96d4-7d4dbc0b21ea | -14.65427 | -56.99787 | 2026-08-28 17:45:00 | NOAA-20 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 18507571-db86-350b-9820-60cb21ea19c4 | -9.65672 | -53.64314 | 2026-08-28 17:45:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README144.md)
