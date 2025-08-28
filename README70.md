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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd012dcb-827a-3101-8c03-f693a5db067b | -7.56163 | -63.84953 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36aa3fa6-b0da-321b-a115-f0ae50f28ce7 | -10.42144 | -64.37271 | 2025-08-28 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8bf063a-8b35-3d71-bdc8-0ee5367b7693 | -10.80217 | -60.76717 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| f794ded4-7d97-3e88-9616-86696598be8a | -5.42164 | -60.16156 | 2025-08-28 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a733b28-071c-3c94-948d-f37f45b93d0f | -12.81982 | -48.13757 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 803bf3c5-e982-398f-976d-021e42125a78 | -9.13249 | -65.77372 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02585cf7-3f9a-3bd1-9111-7190ee91c47d | -10.28242 | -64.48734 | 2025-08-28 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3732dfb-38d6-3344-9db9-3f4eae47fa53 | -10.47516 | -57.95213 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff6b0bfc-da95-3e06-a792-664e915ef842 | -12.85801 | -48.11703 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2ec98d4-6515-3532-958f-ddf0a181f16d | -9.46706 | -51.94345 | 2025-08-28 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cdba55cb-8b78-36ad-98a2-900e92c534b9 | -5.99621 | -57.85157 | 2025-08-28 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9643fb2-5d6e-3c26-878c-4328f95c0dca | -8.88538 | -62.47706 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d7db1e6-e5ec-3123-9037-127d10263c92 | -9.11099 | -65.7804 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 545fd0c3-5d61-3ec7-9f72-cf59bc061097 | -9.53072 | -62.39859 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56138cf9-5ddc-3d81-adf0-1ab30555eb25 | -9.16155 | -65.79446 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8f296e03-e841-3190-99f4-17bcd5db2c90 | -7.46887 | -61.39949 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae35b6f1-850b-3d5c-bd88-a88535e986a9 | -9.53409 | -62.39914 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cb78023-13c7-3e0c-8a3b-2df084f5be81 | -8.45471 | -64.06892 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5cf5294-5917-3277-8372-80e69f1ac08c | -13.06482 | -56.91983 | 2025-08-28 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df51bd11-c889-3096-9000-c896a36a7bbc | -9.63327 | -59.64034 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2db01e1-e8ff-32f9-b480-404bb5ced1e6 | -9.18191 | -59.51127 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc499f12-8896-3388-a462-f0edacdbd47f | -11.22903 | -55.06664 | 2025-08-28 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| af1386c4-2356-371d-a624-9022674f2119 | -10.79494 | -60.76965 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 81d84a3e-da3a-3e52-9cad-9c1574e53905 | -8.88195 | -60.76564 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52713508-ba91-385c-a5e7-41a36efd06da | -6.01087 | -57.84987 | 2025-08-28 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b5d4c92-1791-3d57-bb27-56dd6b8dc4f8 | -9.15704 | -59.55983 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f3b9ffc-7780-3087-8590-a0609dbe0dd4 | -12.79497 | -48.16825 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 81629a4b-7a16-353c-8583-1d26fc723e8c | -9.31543 | -57.69912 | 2025-08-28 05:25:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 71be0380-6499-3bdf-a7f1-ccf07be39f0a | -9.40705 | -60.53964 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a72ac712-db91-30a7-ae07-d0c33421c761 | -9.5244 | -60.52626 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75c237e7-32ec-3455-a832-6cb6cb68ce58 | -12.67656 | -48.17057 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed904483-62d6-3536-b792-50ffa147120b | -9.4076 | -60.53613 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6dc17ad2-1417-34e4-bd43-8dd3a3c37ad2 | -6.23953 | -60.0131 | 2025-08-28 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cda9c873-ffc9-3d8b-9381-290f66eda2b8 | -9.16722 | -59.56144 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6f0c0136-6ee3-39be-b4a3-05a58390dfc1 | -9.54442 | -68.57508 | 2025-08-28 05:25:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 846ce403-ac04-303d-96ad-52d5a438ab3c | -9.23292 | -60.9182 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f3f64fd-c899-3e03-ab89-3f71c61ab0e9 | -10.26219 | -64.49683 | 2025-08-28 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcd8a800-10e4-363b-83a9-b95136858022 | -8.06891 | -61.53909 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b2984f5-e1b8-3339-b00a-51205e913f01 | -9.10919 | -65.74346 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a7827667-6d26-346a-b840-b48e414148fe | -8.93115 | -65.93241 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 021127e1-45ab-33c2-80c0-4ba0fab77de3 | -8.90271 | -60.5466 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f0cb86f-2507-3ef7-b143-ea384c0629bf | -9.80034 | -64.26592 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e548e67-93c0-3798-b476-07d783e89dd6 | -9.16778 | -59.55777 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4118d784-83df-32f1-a862-303c8741de80 | -8.09906 | -71.25048 | 2025-08-28 05:25:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53df1364-3d2d-3822-be2c-daf8d34300f7 | -10.81887 | -60.76982 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 116a9fd9-5a43-39e6-9d6f-7fd2c0aa337e | -9.45224 | -65.4211 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7e0e12a-fade-310c-a7cb-2fc682b46913 | -9.15934 | -59.59005 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 453223fe-03e4-3406-9c80-0c09fa347212 | -8.9239 | -65.92667 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b073e49-8910-38fd-a5a1-4f9519a4fe22 | -8.23114 | -61.45671 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 456aeaa8-9906-3eed-b589-19e100958988 | -10.07891 | -62.89559 | 2025-08-28 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f145786-0c89-3d2c-9855-17edb3a0e5c8 | -9.13471 | -65.78462 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30c63c60-1518-3cd5-b850-9735b43d46c7 | -6.85531 | -55.11543 | 2025-08-28 05:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 263bb5d9-de02-3794-96e8-1d2283680d0c | -10.84445 | -54.03249 | 2025-08-28 05:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f80b2987-d3a1-362a-9e57-4b47358be970 | -12.70599 | -48.16331 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e43936cd-a7bc-3e33-93ef-78712bec5a96 | -9.65553 | -48.30929 | 2025-08-28 05:25:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d16bfe54-c01f-359c-9936-b322c8c0a48a | -9.12199 | -65.78755 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 02a4cd34-878a-339a-956e-9981ae4249fd | -9.0855 | -65.73938 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 3be59a86-cdc0-3985-b1ee-dcda7aa834e4 | -9.41477 | -60.512 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8c5e32e-195a-3f5a-b251-c24710cee472 | -8.34648 | -62.93948 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fbb6577-6b18-39e0-b4d1-6bc10b2dec67 | -9.52385 | -60.52979 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5dda0851-6de0-329a-bd89-acb7dac8750a | -11.45675 | -57.71452 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c02ceddb-6b1e-351e-a890-0ca299bd9f75 | -9.25469 | -65.89422 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 24828278-049c-32e0-9dab-c94856f68cef | -10.47342 | -57.9384 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b008cc6b-242b-3bfa-a1a8-d29beba7f603 | -8.96377 | -62.16354 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e39600d-e856-3a48-9a16-a66d0fe34ac1 | -8.57067 | -63.9337 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9890a6ca-f1ad-37d7-bed6-549961c3a9db | -9.16212 | -59.57196 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dba6bfae-4799-30a7-9981-0107c62ec4b1 | -8.95373 | -65.96877 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 972f3c81-0fc7-3523-a0de-cbbd20bfc574 | -8.94972 | -65.96808 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 215dd8ea-bf89-3fa4-ac74-30b28611a528 | -5.42496 | -60.16208 | 2025-08-28 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6ecbda7-27e3-35ee-ae78-e2ca037362b4 | -8.95093 | -65.96108 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fe16d470-10b7-32c8-8cda-15d0b7302cc4 | -10.81498 | -60.77284 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be72a5ae-2daf-37db-aeca-70164df83519 | -7.34415 | -59.66114 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f9c0578-dd7f-34a4-9dd9-ce8bac4b7635 | -9.10282 | -60.32254 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b91443d4-65dc-3d70-84c3-98723e1848f1 | -9.48544 | -62.39538 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84178546-df3c-350f-9f40-c1dad78e75ce | -9.4081 | -60.51094 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 425bcf70-9df8-38ad-b908-422911f85576 | -10.25204 | -64.49078 | 2025-08-28 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ac4a4ed-24cf-372d-be0c-520f82625fed | -9.5442 | -62.40079 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3e3ab029-eb8b-386b-94e0-87779289bade | -10.07951 | -62.8919 | 2025-08-28 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c3d54ad-7229-35f0-b127-16ce7afeaf62 | -7.44458 | -60.03031 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3dbf8188-6e49-3252-9b8a-652faea1575e | -13.632 | -48.21124 | 2025-08-28 05:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15cb2fb2-d82d-38ae-bf4f-d7c9ac321692 | -10.46591 | -57.964 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3dbbe965-3e21-30c0-b478-8bb9f20ad916 | -9.12458 | -65.77237 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 1ef142da-538e-3904-8595-1a305771babf | -13.00055 | -56.90373 | 2025-08-28 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1749c524-5a27-3817-b9fa-93dff8308cc3 | -9.13517 | -65.28024 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 90d24e65-87e4-3568-a9ea-ae24742246ba | -8.65948 | -63.85008 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81d56d72-58b8-3182-b379-857021b63a70 | -8.34303 | -62.93892 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a653961f-51c3-3fb2-b9bc-0f36d79dfec5 | -8.94535 | -65.94564 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffe57142-76b5-342c-8542-71ded20d761a | -9.19353 | -60.80445 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86cd0014-b357-35cc-9aae-a5666e26915f | -2.44384 | -47.33057 | 2025-08-28 05:25:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ac1d927-f4ce-30ab-bb01-373101437d25 | -8.71459 | -68.68732 | 2025-08-28 05:25:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2d798d5-ad45-304d-9fde-36ea22d5ffac | -8.88692 | -60.75568 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0d46852-9618-3698-965f-bb4ff8327f06 | -7.44871 | -63.15995 | 2025-08-28 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 44aab240-04cd-3bd0-88df-b6c9531dc7f5 | -8.94352 | -65.95616 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 260ffb7c-4d5b-3803-8014-2b32aa207f98 | -9.41266 | -60.56939 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 251aa411-3d13-30d0-8624-ffb6a30c34c7 | -12.81116 | -48.15121 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 33292928-f9b1-322f-93c1-004826b3b2d6 | -9.2478 | -59.78624 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c1020b5-a65b-39f2-8e4f-015bbb4af530 | -9.14126 | -65.76995 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc1b4a0c-2c6e-356e-b387-71eadc1b7d43 | -9.19407 | -60.80101 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ebeace0-09d5-3f61-8322-012ad12115d9 | -9.48439 | -62.38041 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed69c020-6545-3d45-b223-6a85f7107f26 | -9.08814 | -65.72413 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README71.md)
