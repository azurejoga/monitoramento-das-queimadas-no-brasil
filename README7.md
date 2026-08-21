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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 582946fd-30ea-3c22-80e3-67b16c703d46 | -6.1217 | -57.6758 | 2026-08-21 00:14:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e36f12c5-371a-3d29-8901-fc4ac7f3bba8 | -7.2462 | -49.9035 | 2026-08-21 00:14:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79789eb0-bb51-33c0-a48d-6c39d1bbd0fe | -9.2147 | -60.734501 | 2026-08-21 00:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 45088edf-15e6-3ac4-b1b0-f8bf25377539 | -12.845 | -48.420601 | 2026-08-21 00:14:00 | METOP-B | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 585d144e-9cc2-3055-9305-7f919254632a | -6.4276 | -52.752201 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7208478f-8b69-32f9-ab6c-9f00370d6cae | -6.2459 | -48.6493 | 2026-08-21 00:14:00 | METOP-B | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4133c94d-b2e5-3da2-b535-115d884f1215 | -20.188101 | -49.111198 | 2026-08-21 00:14:00 | METOP-B | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c84233ed-aa16-3680-9258-efaa4ee39cd6 | -12.7442 | -48.476101 | 2026-08-21 00:14:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1f0315f3-8825-3705-b1e1-e9608fb6d4dc | -4.0478 | -50.2925 | 2026-08-21 00:14:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8840109-c32e-333a-ab28-90a2f3c64fd5 | -8.0334 | -51.787498 | 2026-08-21 00:14:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bdb6a8b-248b-3c46-877c-68516988bb2a | -8.5702 | -54.648602 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a715213-9c3a-3c00-a0c4-28867b2368b6 | -4.1129 | -56.3521 | 2026-08-21 00:14:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c22c69d4-5aad-36cc-93db-5a0e0eb85fdd | -12.7344 | -48.478401 | 2026-08-21 00:14:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e0473515-3a93-3162-acf4-d0fcf8d7b63d | -3.5331 | -48.1894 | 2026-08-21 00:14:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89d97557-2f77-3799-bbc3-f96e7d651178 | -7.2938 | -52.530602 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3f1bc28-20e1-3c6e-ace2-8205657ae453 | -10.636 | -51.600201 | 2026-08-21 00:14:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6bcda6bd-6af0-3af4-9b22-22596b3c64a0 | -8.581 | -54.745899 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d8486bf-6a1d-30b9-bd51-4fe714c37837 | -9.0569 | -50.888901 | 2026-08-21 00:14:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2e82692-959f-3386-96f1-67431406a26b | -10.778 | -50.2995 | 2026-08-21 00:14:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 278824fb-734f-39f5-b509-26cad483d489 | -6.9605 | -50.412201 | 2026-08-21 00:14:00 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27a4c1e1-1589-3318-818d-017b81eb5306 | -13.9473 | -53.846401 | 2026-08-21 00:14:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| deabfc19-ae14-30df-b60f-4afa1183f101 | -10.9665 | -48.372101 | 2026-08-21 00:14:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8fd69079-d7a6-3205-8908-9dc4424f8c39 | -6.1 | -57.859299 | 2026-08-21 00:14:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 994b0e75-763d-392c-8265-f3e145d5fbf2 | -6.1192 | -57.663799 | 2026-08-21 00:14:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a46a9549-cdaf-31c8-9542-7ae529c550d0 | -11.0833 | -47.589199 | 2026-08-21 00:14:00 | METOP-B | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f19a64e1-c50f-3b54-84ab-0787ccbf463d | -6.0158 | -57.799999 | 2026-08-21 00:14:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c0303a3-9837-32ec-b0d8-e963f40c72b7 | -8.494 | -54.865398 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac28f249-5a80-39f3-9cbc-71ea25854a42 | -6.0105 | -57.775501 | 2026-08-21 00:14:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69fdce73-f598-3eec-be61-f116e16668a5 | -10.8329 | -51.004002 | 2026-08-21 00:14:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 45354800-9982-36e1-81f0-901fd81b4ae1 | -12.5112 | -54.7556 | 2026-08-21 00:14:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8ac9ab5d-3aa3-3b9a-bbbb-fe5a950da1a8 | -9.0636 | -50.872898 | 2026-08-21 00:14:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 205cfdd0-acfa-3160-8f6c-85498a582d68 | -6.9589 | -50.405201 | 2026-08-21 00:14:00 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14a16690-7157-3a90-9d78-13b9a8300330 | -8.6644 | -54.610199 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b85b8714-e060-34cc-8fe8-f15a3b4c2e31 | -8.1066 | -51.6549 | 2026-08-21 00:14:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d92913a8-5be5-3a22-b189-c4861910d7ef | -9.9956 | -48.544399 | 2026-08-21 00:14:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 40be75ca-f842-3ba2-a54b-c067d83e91b8 | -6.873 | -58.999699 | 2026-08-21 00:14:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 67954f48-a517-3908-b447-2f95fb90845b | -7.7732 | -61.137299 | 2026-08-21 00:14:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7a7eec1c-9f38-36a5-9705-96cf9601a5e5 | -12.2396 | -43.166698 | 2026-08-21 00:14:00 | METOP-B | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a52ce1a2-72df-3943-abd9-f0f363e31c3f | -14.4589 | -45.625 | 2026-08-21 00:14:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f96fe03b-4e92-3c30-8c62-1c5b5ff6725a | -10.5242 | -50.774399 | 2026-08-21 00:14:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ac00d981-2eb1-3d87-80ea-f7a54204c0fb | -12.2553 | -43.147099 | 2026-08-21 00:14:00 | METOP-B | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0e2a9dc0-a524-383d-9ef2-c5dca2606292 | -9.4562 | -51.614601 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e02946b-8a8b-3e9b-97cb-420d95b83cf5 | -14.7242 | -47.133701 | 2026-08-21 00:14:00 | METOP-B | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e23c8ffc-95fe-354d-bfb0-615e83f7d136 | -7.3633 | -45.823502 | 2026-08-21 00:14:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a9a9e5d-24d7-306d-a9af-d0971bbaa46c | -8.0546 | -50.103298 | 2026-08-21 00:14:00 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c92952eb-55df-39ed-bf07-dbb9f541ec58 | -13.982 | -49.431801 | 2026-08-21 00:14:00 | METOP-B | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 95465072-4e84-3ce6-86ee-e6275ba2fec3 | -9.4017 | -60.408699 | 2026-08-21 00:14:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aff79ddd-dd5d-36cd-b500-dfef33167b4c | -9.448 | -51.623798 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c7cf412-28cf-3377-b8de-9539bcaacb0d | -8.5987 | -54.732899 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69ed8359-e034-3dfb-81ac-9bd5e7a8939f | -5.6611 | -51.632198 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d46916f7-5c73-39d7-8a03-b57301811f1e | -12.4334 | -43.4035 | 2026-08-21 00:14:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5154b0c2-26cf-3ae1-a8db-b200bcc153b9 | -14.5362 | -52.014801 | 2026-08-21 00:14:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a24b7ef4-3b9d-37c6-8a34-bb9f1eda7cf7 | -7.2446 | -49.896301 | 2026-08-21 00:14:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31530c46-bd01-338d-b097-6f820494573e | -12.8024 | -48.4151 | 2026-08-21 00:14:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6c873a2c-8e58-37a5-9fab-a36610e60f59 | -12.2299 | -43.169201 | 2026-08-21 00:14:00 | METOP-B | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e4b49e7e-7617-35ea-856c-541ee4815b4a | -7.3675 | -45.798 | 2026-08-21 00:14:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 10094bb4-1ab4-3ec0-9da6-9240255e557e | -5.7261 | -53.712601 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| babee5c7-5c09-3302-bbd7-45ac02cbaf4e | -6.0184 | -57.812199 | 2026-08-21 00:14:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b9b4a19-11bd-3be4-b53f-a418d01d284d | -9.9931 | -53.926601 | 2026-08-21 00:14:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0a14a37-e14c-328e-aeec-ea9326dc9dd6 | -6.4342 | -52.736099 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e06c1b5b-04a7-31e4-800a-27bebdda4a01 | -8.587 | -54.726398 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc09968a-84a3-3cdf-a9e5-17db3e7a2e12 | -11.1718 | -54.024502 | 2026-08-21 00:14:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9c150232-7e25-339f-8cd5-2fc1c8a27a95 | -13.2615 | -51.621799 | 2026-08-21 00:14:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1d0015ac-40fc-3895-8223-53cc6ff3ea6f | -14.3354 | -51.890701 | 2026-08-21 00:14:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 06ff9241-19c4-3501-b9ea-c3254e096db6 | -6.2318 | -55.399601 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b76a40f7-eddf-3e53-94be-50c1d353129b | -12.7425 | -48.468601 | 2026-08-21 00:14:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9f35c816-ff50-34c0-a7fd-5c866fe03d4c | -6.8716 | -59.427399 | 2026-08-21 00:14:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ac40ea16-4d0c-371e-9934-a11b461129fc | -14.3371 | -51.898399 | 2026-08-21 00:14:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b84cf3ea-5768-39ac-80f5-bf0e70b3a9aa | -8.1102 | -50.030701 | 2026-08-21 00:14:00 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f979e1e9-0be2-3c1b-9a64-be1ddc180df2 | -12.799 | -48.4002 | 2026-08-21 00:14:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 36251818-40dc-3fac-b5b6-a5640c26d2a8 | -7.6333 | -45.7463 | 2026-08-21 00:14:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be0e5176-4242-3170-a2a7-0c45e2c1506b | -6.6744 | -52.890301 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7eeaf451-bd60-35f0-84f2-c6bb0f279240 | -14.342 | -51.921299 | 2026-08-21 00:14:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c29ad121-57fd-32e1-8c66-42c326c3c2b1 | -9.0703 | -50.8568 | 2026-08-21 00:14:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb39e779-32f3-37bd-bfd2-d7400c770402 | -14.7223 | -47.125702 | 2026-08-21 00:14:00 | METOP-B | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d151446a-817e-3d72-b76b-b11b47946879 | -10.3196 | -50.367802 | 2026-08-21 00:14:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1fc1309f-d8a9-3e2f-8f79-b02b67c24715 | -5.8067 | -55.706299 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 265f73a2-b054-3000-9fbf-1c5979404085 | -19.693701 | -46.9231 | 2026-08-21 00:14:00 | METOP-B | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 17eef28b-a4f6-327e-acc6-31d0400f7356 | -6.169 | -55.440899 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d98c1bce-c00b-3fd3-a0b8-4635d7d94de4 | -12.2165 | -43.1572 | 2026-08-21 00:14:00 | METOP-B | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7376306e-02d7-3797-a0c1-486f2c0c9dab | -4.9469 | -55.761299 | 2026-08-21 00:14:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04933462-81a1-3727-8b13-e6699ef47686 | -6.896 | -56.429501 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 544e37d1-05e4-3bc1-974b-71925b8c3d5e | -10.5227 | -50.767399 | 2026-08-21 00:14:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9ce337bb-5b4a-3040-87e9-c542d860155e | -18.2071 | -50.755798 | 2026-08-21 00:14:00 | METOP-B | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1fe9c10a-11f6-39aa-b7c8-21cedf0dc44b | -16.320101 | -49.435398 | 2026-08-21 00:14:00 | METOP-B | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5f09cec3-152c-3cd8-a9ea-78403bc686f7 | -2.475 | -49.4063 | 2026-08-21 00:14:00 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22a893c4-6307-3080-b974-8c2458d7a40a | -9.1785 | -56.982399 | 2026-08-21 00:14:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac9393ca-49ba-3ef7-9734-055bf4e5e687 | -9.4531 | -51.6007 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6aee4fa-d181-34c1-b7a3-889b7f1bf1bb | -10.2497 | -54.3592 | 2026-08-21 00:14:00 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c527e9b0-1f49-327d-8bc8-5115e0af389f | -7.3578 | -45.8004 | 2026-08-21 00:14:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 21b26a90-924f-39fa-90b4-2acee719876c | -6.9703 | -50.41 | 2026-08-21 00:14:00 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a0aaba3-bf6f-3f08-abe0-ffa63cff956d | -7.0699 | -59.9375 | 2026-08-21 00:14:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 68a12cc6-8d13-3103-813d-40361eb1518d | -11.2121 | -55.040798 | 2026-08-21 00:14:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 671859a0-8a1f-358d-b7f9-b993a4ffc52a | -12.0063 | -53.4207 | 2026-08-21 00:14:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9f2ef9c8-3b42-3edf-9971-6946efdad7e7 | -4.1837 | -49.402401 | 2026-08-21 00:14:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a98ab987-ac9d-3c65-b087-a59e88246749 | -11.2153 | -53.988201 | 2026-08-21 00:14:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0813d612-9d1f-3570-86d2-7301bf244427 | -8.5684 | -54.639999 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f452c09-0a05-3985-a2dd-b629e630e955 | -8.5019 | -54.8545 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 249e2942-87c8-3587-a9b2-5c8b93510268 | -10.6293 | -51.616501 | 2026-08-21 00:14:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c3e9dcf-1858-3472-bebc-b3d96546d86e | -12.5071 | -54.736 | 2026-08-21 00:14:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
