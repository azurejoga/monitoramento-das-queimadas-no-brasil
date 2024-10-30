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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45cbd2ff-779c-3c84-8400-bc362dfd8acf | -10.50472 | -49.01494 | 2024-10-30 04:46:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 49db8414-1f56-3e8e-83c8-d49f6c544df5 | -10.50115 | -49.01442 | 2024-10-30 04:46:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0893018d-6016-3b93-b33a-ff0b146bcdd2 | -12.07398 | -47.98351 | 2024-10-30 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c1fb035c-d812-36b1-b643-384311dd45c4 | -11.82464 | -48.76065 | 2024-10-30 04:46:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1634ce88-130e-3019-8ae9-33617797feb2 | -11.82097 | -48.7601 | 2024-10-30 04:46:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50f6b011-be50-3f01-ac2e-ef7023a189e7 | -11.82035 | -48.76444 | 2024-10-30 04:46:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8b24939-b3dc-3b26-adb8-dd3e46839b20 | -11.81668 | -48.76387 | 2024-10-30 04:46:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b446382-9897-36d2-b968-0beee15302da | -19.5862 | -56.7136 | 2024-10-30 04:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 129.8 |
| 4a64c0ad-e5f0-331d-bc19-c3e41878e197 | -19.6063 | -56.7108 | 2024-10-30 04:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 122.6 |
| 8b566e5e-53b2-3dcd-81a8-8510cd6c4b13 | -19.6264 | -56.7079 | 2024-10-30 04:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 79.9 |
| 363b8b07-8c3a-3425-aec3-5abc22f68487 | -18.96 | -52.39579 | 2024-10-30 04:49:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6091e7ba-101b-39fd-8ec2-617b236a1db4 | -18.95661 | -52.39525 | 2024-10-30 04:49:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8f5111af-9644-3fa8-8144-298c449b630d | -19.60127 | -52.25229 | 2024-10-30 04:49:00 | NPP-375D | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e1ecead-72bb-3d70-b196-87415ca3c653 | -20.99646 | -51.79397 | 2024-10-30 04:49:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 668f9a84-2032-3482-b871-258654b63daf | -19.48 | -56.64139 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b1eae2b2-68a2-3a8e-946f-daa77a0954ee | -19.47929 | -56.64553 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 382165ee-843b-3485-96b0-e4aa1277f220 | -20.47845 | -53.67486 | 2024-10-30 04:49:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dff76fab-2e4c-31dc-a39f-fb716a47793a | -21.565 | -54.21125 | 2024-10-30 04:49:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4f2db77-bba7-3abb-b685-d2376834532a | -21.56225 | -54.20695 | 2024-10-30 04:49:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 369605d7-a1a0-3fb4-85bf-46b032e02295 | -21.56167 | -54.21066 | 2024-10-30 04:49:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96b38c62-57a5-3f25-957b-588c00c5f4a2 | -21.55983 | -54.20708 | 2024-10-30 04:49:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9865fd1c-c2ec-349c-b369-b111382acd62 | -21.55707 | -54.20278 | 2024-10-30 04:49:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc3d8a61-60d4-3b2d-adda-4db3b1f92b5e | -21.5565 | -54.20649 | 2024-10-30 04:49:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e53ba1ad-f05a-39bb-9a89-06107a12ccd6 | -21.20078 | -54.44112 | 2024-10-30 04:49:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e37c941c-5b92-3d1f-847b-b3a5a2de148a | -19.4772 | -56.63659 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a52c9d78-5440-349c-98a1-8e398e79247b | -19.47649 | -56.64072 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e4f08c1f-7d0d-315f-9627-2c7246ad7090 | -16.1558 | -54.77575 | 2024-10-30 04:49:00 | NPP-375D | JUSCIMEIRA | MATO GROSSO | Brasil | 5105200 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e9fcff3-80ac-389f-aee3-6e17c0ec172b | -17.96491 | -54.48788 | 2024-10-30 04:49:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd229db9-fafa-34c6-9bc2-184867d4d9e5 | -19.11224 | -54.91198 | 2024-10-30 04:49:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a2779c4d-9b7d-3da0-a65d-d2d3c5809d2d | -20.60089 | -55.80785 | 2024-10-30 04:49:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f18eb11d-6383-3ab5-961e-bc41a4e83c34 | -20.03107 | -54.67382 | 2024-10-30 04:49:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec11c6c8-2d1e-3650-9176-6f8a9ad5c2a3 | -16.55653 | -56.23167 | 2024-10-30 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 43e13e4b-5bf7-3cdc-8360-5eb9fbf0ff35 | -16.56009 | -56.23233 | 2024-10-30 04:49:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 89c9bdfe-26ce-37d6-9db7-0697bb11d133 | -19.48213 | -56.62901 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c8f4a47e-f063-3ae0-8447-2d2f12b6f55f | -19.47089 | -56.63112 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 55dcf717-6bf5-3557-85f6-275a2db1ea72 | -19.46809 | -56.62632 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 5e0e30ad-5f67-3a6f-be10-f998d93689a7 | -19.46738 | -56.63045 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 0d551b91-34de-3930-aea1-e78aaf796ca1 | -19.46387 | -56.62977 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 1e92989d-5ee2-3828-8957-e66a12c5e0fd | -18.26258 | -55.97787 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.8 |
| 50273078-1a2a-3240-bccf-7ab6a5a2bffd | -18.25911 | -55.97723 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.8 |
| b4a95fd9-513e-39b3-98e3-4d5f32c560fa | -18.25843 | -55.98121 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.8 |
| a3f846b6-5737-373c-bb1e-0b3a2d880bb4 | -18.25632 | -55.97261 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 58a9c326-d574-39dd-a03f-8874fe4a4e8a | -18.25564 | -55.97659 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 4a05260a-ca7b-3fad-92b9-9c11850540ad | -18.25496 | -55.98056 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 9a1fc73a-2c70-31f2-8d6c-a488fc571d17 | -18.25217 | -55.97594 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 732d74a1-51dd-36e7-a7c0-4319406b4497 | -18.25081 | -55.9839 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 92fd7189-9fbc-37b9-865c-7b74f2c9d1b0 | -18.24592 | -55.97067 | 2024-10-30 04:49:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4cd4747a-81f1-3e04-b8c0-d01da7634bd6 | -19.62638 | -56.69435 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 1485d554-7e7a-3ad2-826b-c68aafe5a6cb | -19.62568 | -56.69849 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| f448663b-87cb-30b5-ad57-1880f21553ca | -19.62287 | -56.69367 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 2a375465-f542-3c08-a818-5cd31c66c20e | -19.62216 | -56.69781 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 59c6a9c2-abea-3588-9f1c-713781fd07f6 | -19.62145 | -56.70196 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 43ceac98-e98e-35f5-99d9-da19237f40b9 | -19.62075 | -56.7061 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 74b9dab5-a944-312f-a1af-2e2d481abcc3 | -19.62004 | -56.71025 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 7cf3b34a-5778-327d-9617-6931d6d94e10 | -19.61864 | -56.69713 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| e5d3abe2-33ea-3aeb-bd6d-576f41b5bb02 | -19.61794 | -56.70127 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| b24f1f44-7230-3dae-a2be-f8bb2a2bf7e4 | -19.61723 | -56.70542 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| c99900a0-0edf-3dfb-9874-2f91b2d102aa | -19.61652 | -56.70957 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 6d5450ee-60e7-3e5e-b956-98a220f3152a | -19.61584 | -56.69231 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 946bf41e-dce5-3147-ba4d-9f0cd7b0c882 | -19.61581 | -56.71371 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| dfb6b44b-3923-3548-b769-49ee8bfe8a88 | -19.61513 | -56.69645 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 867f42c5-5eff-36bb-940e-6ff0462783d2 | -19.6151 | -56.71786 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 06d0bdb3-2f1c-30e4-b18a-7ac5bbb3f4f3 | -19.61442 | -56.7006 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9ce07ae7-0df9-34dc-bd44-612506b4b4a2 | -19.61371 | -56.70474 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 9b8d297b-f296-3a9c-98b4-9f55514a10e6 | -19.613 | -56.70889 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 46a83526-d1f6-310e-8ae2-055ae137fb9d | -19.61229 | -56.71304 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| d55d3511-221e-3111-a439-33d5aa5f4346 | -19.61159 | -56.71718 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 4503719a-ec9c-37b1-a53b-8eaea593e29c | -19.6109 | -56.69992 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9c106293-d79f-33cf-ab31-b42b5caabc84 | -19.6102 | -56.70406 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 61fcd27b-c1b7-37cc-8867-1930fa11bb7b | -19.60949 | -56.70821 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 9d55e28b-5160-377d-be0c-9823924ea52e | -19.60878 | -56.71236 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 459f609f-6c22-3eee-a70b-3084f0f1be15 | -19.6081 | -56.6951 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| a5918ac2-0f4c-39e5-8ddd-3e8c1c7bfab2 | -19.60807 | -56.7165 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 875a26a5-c1db-3ae6-8da7-3bbc2f87bb21 | -19.60739 | -56.69924 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 1776ad7d-ddea-3beb-bdec-c1d2735b1927 | -19.60668 | -56.70338 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 90c96ad3-a498-3ea8-84ba-d2e972e35f6b | -19.60597 | -56.70753 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| be3f30ac-5df6-3e66-8a17-a3179ad09204 | -19.60526 | -56.71167 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.1 |
| 5f106f64-61cc-3ef1-9c21-bf32003c82e3 | -19.60455 | -56.71582 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.1 |
| 0ead469a-20f2-3b3c-9447-34e93e266dd8 | -19.60387 | -56.69856 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 4c17c27a-e011-3eb9-a20a-2624043d0f90 | -19.60384 | -56.71997 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 9431b1bb-d185-3ae5-a070-60ef19e9b965 | -19.60316 | -56.70271 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 68214420-f2d8-3403-823d-7548dff261f4 | -19.60245 | -56.70685 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 119e4061-f25a-3611-bb37-2a8fc13c02e9 | -19.60174 | -56.71099 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.1 |
| b235c3c0-ea99-345a-adfa-f730521e865b | -19.60103 | -56.71514 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.1 |
| f0cb499c-e5d3-3a1f-9e41-1f9600fe7bbb | -19.60036 | -56.69788 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ac0ac6df-d060-3e66-8138-351998d02743 | -19.60032 | -56.7193 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 6c8c06f9-4fab-39e4-86e8-260d9d94b160 | -19.59964 | -56.70202 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 86302f87-08a1-3dc9-8927-46b6f907dfa0 | -19.59893 | -56.70617 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| bd266b9b-13df-33cf-937d-9e19e6708354 | -19.59822 | -56.71032 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| a191ff27-0b69-3aff-805b-15fb82bd2e4d | -19.59751 | -56.71447 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 641ffda0-0383-329c-844d-dd2cc3034fa7 | -19.59684 | -56.6972 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bc019869-07a1-3bfa-b227-01c670b3c8c5 | -19.59613 | -56.70135 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 7842afac-7851-33e6-af78-8987f8652d22 | -19.59542 | -56.7055 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 2c3bcfe3-9d44-30b3-aadd-1f7a2d02fad0 | -19.5919 | -56.70481 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e0221331-8312-33c9-880b-0753d382b68d | -19.59047 | -56.71311 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7b5c8ca3-6bbe-35be-945c-b11b9c029483 | -19.58855 | -56.61884 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5551e5ab-99c2-3c64-8f09-5e0e6badf0f7 | -19.58767 | -56.70828 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 0b7d6eeb-f068-3c86-b412-cc8f1c872dda | -19.58695 | -56.71243 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1b94a7cd-7849-36d0-964c-3b1e55db1e3f | -19.58624 | -56.71658 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 293a7a1c-afbb-3884-a8fa-bdec37a13ae7 | -19.58553 | -56.72073 | 2024-10-30 04:49:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |


[Clique aqui para ver as próximas entradas](README78.md)
