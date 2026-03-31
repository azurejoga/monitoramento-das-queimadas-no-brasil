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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a66012e7-e670-3c4b-811c-2dac7d687dc4 | -13.54217 | -43.68628 | 2026-03-31 00:01:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| ab7001e8-e1c6-3063-83cd-dafff2692370 | -12.48574 | -43.64871 | 2026-03-31 00:01:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 684e3d8a-753b-3759-9f9b-fb2cfd2dcd83 | -13.14866 | -53.25781 | 2026-03-31 00:01:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 23.7 |
| ebb831b2-b535-39db-a0bf-70f2977123cc | -12.83694 | -43.84887 | 2026-03-31 00:01:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 905863dc-d8ef-323f-be38-614a5e1e5815 | -14.3353 | -57.7187 | 2026-03-31 01:40:00 | METOP-C | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ba6fd7cd-fe1e-35fb-b176-21571e1f730b | -4.93814 | -37.36862 | 2026-03-31 03:38:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f74517e2-aa2c-3e6f-8014-0c34c63f9f9b | -4.93436 | -37.36798 | 2026-03-31 03:38:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f4470508-953d-3954-9230-df9f75371974 | -4.93889 | -37.36403 | 2026-03-31 03:38:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2cefa4ba-5396-378e-8500-10b835c312c3 | -5.84891 | -35.51704 | 2026-03-31 03:38:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c207aca4-2594-37a8-83fd-8396b7a930e7 | -15.1644 | -43.98665 | 2026-03-31 03:40:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b214fc01-7b99-309f-89fe-524f33f6f008 | -13.54109 | -43.68722 | 2026-03-31 03:40:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6fbe24ce-0204-3735-8fa2-626a1f9cc60b | -13.54244 | -43.68248 | 2026-03-31 03:40:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f6e43f5-1c06-3b46-98f6-6488c01e2029 | -13.54132 | -43.68824 | 2026-03-31 03:40:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4908f99f-edd9-31b9-bf8c-16fd089a4bdf | -16.92312 | -43.59854 | 2026-03-31 03:40:00 | NOAA-20 | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26944aa2-5702-3fdb-b9c4-64a3ccf1d3d0 | -16.92502 | -43.59759 | 2026-03-31 03:40:00 | NOAA-20 | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 184bd100-29da-3ef1-b824-203b938bb643 | -12.48427 | -43.64701 | 2026-03-31 03:40:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d0b72aa-bca2-3aac-958c-b972c890210f | -12.83407 | -43.84907 | 2026-03-31 03:40:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3b5730c-cdb6-3591-8fc6-6bc3a6c480f1 | -15.52884 | -41.67768 | 2026-03-31 03:40:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| af7f950e-8643-39a5-8d9a-7627a9ec6e4b | -16.92402 | -43.60282 | 2026-03-31 03:40:00 | NOAA-20 | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7832fdaf-e14c-3de3-8995-2504cfd7834a | -20.20473 | -46.43448 | 2026-03-31 03:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 07521db4-9f33-34ff-9ef2-37550ea3008e | -21.334 | -47.07024 | 2026-03-31 03:42:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f1f0e30-474b-3507-be66-44c2545f4cf2 | -20.2033 | -46.4411 | 2026-03-31 03:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ed2bd5e-17c8-3c06-8457-35135b9b2069 | -17.90438 | -42.85948 | 2026-03-31 03:42:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68f10e24-c1fd-39b7-aa15-15de192a8caf | -20.20261 | -46.44436 | 2026-03-31 03:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a1ccea0c-5c55-39ad-86d3-07e3ee8367d2 | -20.20401 | -46.43782 | 2026-03-31 03:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 360dbde5-42d1-3455-8963-a16b967c6113 | -21.33207 | -47.06936 | 2026-03-31 03:42:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c55c518-bddc-33f4-bca5-94495abc15cd | -22.77679 | -43.5549 | 2026-03-31 03:42:00 | NOAA-20 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b0e3b6be-f8e0-3929-9830-0067b5a17f1c | -12.45152 | -48.72609 | 2026-03-31 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 526b0740-ef91-3649-a76d-2b68d84b2245 | -12.48981 | -43.64542 | 2026-03-31 04:27:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 73db0779-f74b-371d-a18a-b5df26b7e52d | -14.3328 | -57.72723 | 2026-03-31 04:29:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3633f4b-6bd7-3ad3-9772-9dfcba97e24b | -15.16638 | -43.9847 | 2026-03-31 04:29:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aa19b954-3f8f-329c-8118-0ded4cb341b9 | -14.32746 | -57.72599 | 2026-03-31 04:29:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35fd4ba5-6242-36e4-aec4-7f932735b201 | -17.13427 | -47.59591 | 2026-03-31 04:29:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b32b4c2-fb07-34a2-a45a-f6b1946624ff | -13.15615 | -53.25725 | 2026-03-31 04:29:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f7e1d0a-79f8-3634-931b-c5e7c47be191 | -13.15206 | -53.25647 | 2026-03-31 04:29:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f2be536-86b6-3fbe-ad26-f3e25eecb44c | -17.88054 | -49.86596 | 2026-03-31 04:29:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9215ad62-e0bf-3dab-87c0-e8c3f1f28373 | -17.40657 | -52.65275 | 2026-03-31 04:29:00 | NOAA-21 | PORTELÂNDIA | GOIÁS | Brasil | 5218102 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6dc955bc-c14c-3ade-b0a6-e3c33dc430cc | -15.2391 | -50.83236 | 2026-03-31 04:29:00 | NOAA-21 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d14bc9ef-3a43-3819-b61d-576d57d86665 | -14.32676 | -57.72952 | 2026-03-31 04:29:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9fe013d-ca20-36ac-8623-efc73a873de4 | -16.26845 | -47.96944 | 2026-03-31 04:29:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e45ee920-9991-3750-985d-b1629c27d206 | -17.90666 | -42.85907 | 2026-03-31 04:29:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a36fab2-d27c-39a4-8807-6eaeb212aaa2 | -16.04021 | -48.47534 | 2026-03-31 04:29:00 | NOAA-21 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73233b94-4b67-346b-a24f-be4ac855a6a7 | -16.92699 | -43.60091 | 2026-03-31 04:29:00 | NOAA-21 | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 201df53a-9051-31b8-8c65-b18b708354e2 | -17.90612 | -42.86325 | 2026-03-31 04:29:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15581ce8-628e-32b7-b472-ce44249c4060 | -13.54325 | -43.68415 | 2026-03-31 04:29:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abb0fe54-076a-3c0a-9db9-848defcf6e74 | -13.54258 | -43.68893 | 2026-03-31 04:29:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac7d6660-5d6a-3e77-ad29-ac8d9be2a041 | -20.14373 | -52.83655 | 2026-03-31 04:32:00 | NOAA-21 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ad77867-1712-3dfd-8e5f-17565535043c | -20.13489 | -50.76357 | 2026-03-31 04:32:00 | NOAA-21 | SANTA RITA D'OESTE | SÃO PAULO | Brasil | 3547403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2677023d-234d-3ad2-bbe1-573ec600f0a1 | -22.07322 | -55.49287 | 2026-03-31 04:32:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07451c94-4bfb-340e-99eb-8be47dc476b0 | -21.52836 | -53.39289 | 2026-03-31 04:32:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 873747b3-c65f-3f48-8d24-4deaa00e770a | -21.33508 | -47.07261 | 2026-03-31 04:32:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f252684b-9c43-3a73-a351-83fff6453912 | -19.18099 | -49.1326 | 2026-03-31 04:32:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d1a26f6-9c6a-353c-a87c-a25c23ee0504 | -21.52473 | -53.39213 | 2026-03-31 04:32:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0910c69a-b658-3220-a896-83af185a37a2 | -21.33568 | -47.06842 | 2026-03-31 04:32:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 063f6d0e-5831-3898-83b7-c04e1cc0c97a | -19.29425 | -55.16208 | 2026-03-31 04:32:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0bd738b7-00aa-3aa5-9a55-ccfbd6f00538 | -22.07398 | -55.48894 | 2026-03-31 04:32:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11641d1d-6be6-3041-9a43-e5cb56832efa | -19.18487 | -49.12953 | 2026-03-31 04:32:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48546842-63f4-32bd-b68d-2df2d530f898 | -18.84078 | -53.4234 | 2026-03-31 04:32:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1681294d-ff8a-371c-a118-83ac1af3b868 | -22.72208 | -48.05542 | 2026-03-31 04:32:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5d60711-0fa3-39de-922a-0743ad6d2c54 | -19.69609 | -51.35647 | 2026-03-31 04:32:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a1f0405f-a376-3994-b806-38a2314072bf | -20.04344 | -54.51423 | 2026-03-31 04:32:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cd48d45d-67fe-3ed4-9f65-aefc8ed65589 | -18.8437 | -53.42893 | 2026-03-31 04:32:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7802b4d-2404-37c4-9f6a-42caf652400d | -20.20508 | -46.43268 | 2026-03-31 04:32:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79a83e25-8d54-3693-a977-7bc87158cd5e | -20.20388 | -46.4413 | 2026-03-31 04:32:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa7d37f7-bb41-34b0-9544-13f04f010560 | -23.50885 | -52.95344 | 2026-03-31 04:32:00 | NOAA-21 | CIDADE GAÚCHA | PARANÁ | Brasil | 4105607 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 51f97986-aed4-33a1-bcd5-1d93016385a0 | -22.06313 | -56.22028 | 2026-03-31 04:32:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee13828b-3b62-3ddb-94f7-e8587044a655 | -21.3263 | -55.78186 | 2026-03-31 04:32:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8bbf7ed-7a66-3dcf-a4f4-bef1dd039e5e | -20.80496 | -49.81295 | 2026-03-31 04:32:00 | NOAA-21 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| d0a0a9e3-4ca3-3add-8ac9-fdcc1faa26f0 | -20.56511 | -47.87093 | 2026-03-31 04:32:00 | NOAA-21 | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4799f528-8012-31f8-9e54-0198d497cfaf | -20.91837 | -49.52315 | 2026-03-31 04:32:00 | NOAA-21 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 51b46b77-242b-3df3-817e-81fcb7011c38 | -20.20448 | -46.43698 | 2026-03-31 04:32:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c654701a-6ca2-3d3b-a43a-2a5af4e37436 | -22.72156 | -48.03489 | 2026-03-31 04:32:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7cda3085-0dbb-3505-9e75-c53ca2069212 | -23.23331 | -52.16275 | 2026-03-31 04:32:00 | NOAA-21 | PRESIDENTE CASTELO BRANCO | PARANÁ | Brasil | 4120408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9e2748e0-fcd1-3103-9b1b-79e78709cfa6 | -28.57065 | -51.02789 | 2026-03-31 04:34:00 | NOAA-21 | VACARIA | RIO GRANDE DO SUL | Brasil | 4322509 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 84a5ff12-83d6-3d45-b520-905857410a2f | -30.02999 | -50.16299 | 2026-03-31 04:34:00 | NOAA-21 | TRAMANDAÍ | RIO GRANDE DO SUL | Brasil | 4321600 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| c2cd5351-b956-348f-a409-ef93dd51f7b6 | -29.98021 | -51.20159 | 2026-03-31 04:34:00 | NOAA-21 | PORTO ALEGRE | RIO GRANDE DO SUL | Brasil | 4314902 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| d1ea5424-b621-3f29-b61b-55f156400ca0 | -27.48896 | -50.99055 | 2026-03-31 04:34:00 | NOAA-21 | VARGEM | SANTA CATARINA | Brasil | 4219150 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a537ba2a-73d0-3682-adb6-55dd82dbc370 | -27.26656 | -51.45525 | 2026-03-31 04:34:00 | NOAA-21 | ERVAL VELHO | SANTA CATARINA | Brasil | 4205209 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 215069b1-43c8-38b7-b258-f4345622ec03 | -12.29837 | -57.40484 | 2026-03-31 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29e3cc98-f2fa-320d-a6f4-00bad3103966 | -13.15565 | -53.25712 | 2026-03-31 04:59:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edc27ac9-2a04-3243-8fd0-3ca7ff583a3f | -13.1523 | -53.25659 | 2026-03-31 04:59:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9844e22-34bc-345b-9982-013dd90a060d | -13.22964 | -53.3245 | 2026-03-31 04:59:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ee143b1-1044-39e8-89ba-1316d8f94af7 | -12.44946 | -48.7256 | 2026-03-31 04:59:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75ed4e86-c487-384e-a521-948aaee6f430 | -12.29826 | -57.40295 | 2026-03-31 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3acd66d7-0720-3f56-b034-4c8e24d1b2a8 | -20.04124 | -54.51181 | 2026-03-31 05:01:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d9c5c49-6a68-3bb8-ae59-55f5fb2f94de | -22.07488 | -55.49314 | 2026-03-31 05:01:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87f06422-e226-3c90-a522-7a78ce2186d6 | -21.32456 | -55.78283 | 2026-03-31 05:01:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e053dd7c-939c-3124-9916-d58828e107cb | -20.20207 | -46.43765 | 2026-03-31 05:01:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cdc108c8-b7fa-36ce-9b18-cb5f82bbab95 | -14.32962 | -57.72682 | 2026-03-31 05:01:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d63a07c-9b17-3198-bde4-2f51e75f7b41 | -19.29372 | -55.15929 | 2026-03-31 05:01:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec3784d7-33b2-3987-99bb-bd8dac60e15b | -20.04068 | -54.51559 | 2026-03-31 05:01:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 381e6752-857d-3712-81e7-d77c31e264ca | -14.326 | -57.72615 | 2026-03-31 05:01:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc78d34c-6186-3748-8c25-0f836d6db823 | -21.52306 | -53.39205 | 2026-03-31 05:01:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23c1cc22-9d70-35ea-b242-8609afd6e8dd | -18.84058 | -53.42648 | 2026-03-31 05:01:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad8a5921-e36f-359b-8937-b206252fc556 | -22.07211 | -55.4888 | 2026-03-31 05:01:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07fb1a48-92c2-3cfd-983d-dac5837abde1 | -19.29315 | -55.16293 | 2026-03-31 05:01:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79ad255d-453a-3283-818a-335754831ffc | -20.91831 | -49.5271 | 2026-03-31 05:01:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| eaec3d5d-b084-3195-8bde-ebbcd9728cea | -20.91884 | -49.52256 | 2026-03-31 05:01:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| cc8aa680-43ae-31bf-af3d-71a1416a8d12 | -20.14396 | -52.83832 | 2026-03-31 05:01:00 | NPP-375D | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36d7ecc1-3e03-3b3b-880b-316dc689014a | -19.18168 | -49.13427 | 2026-03-31 05:01:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README2.md)
