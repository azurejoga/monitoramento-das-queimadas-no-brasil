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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37b1e9a7-b73e-3b1d-9720-b334b4c3780a | -3.3871 | -59.4075 | 2026-09-02 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 05573cce-c5db-3713-a64f-c1f6d36ca1f0 | -3.6216 | -60.547 | 2026-09-02 15:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 91.1 |
| b4f94fd6-da53-37e1-b985-a195cde8135e | -10.4142 | -50.0112 | 2026-09-02 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 2d2b7a3f-35d9-3282-b53e-08350b3d6a0f | -13.5531 | -59.7574 | 2026-09-02 15:00:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 2a7aaf1b-5b15-372a-a92c-9780c80762a8 | -8.4089 | -62.6767 | 2026-09-02 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 0f67714d-f313-3bbd-ac5b-1417bb2f775a | -10.5788 | -47.7306 | 2026-09-02 15:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 376cd77b-7cb1-3544-bc91-8d5d0fa6d64e | -6.6542 | -59.426 | 2026-09-02 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 51cf8ec1-3641-31f4-b450-2d2a2cab9326 | -9.0244 | -65.4367 | 2026-09-02 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 302d1469-1447-382d-bb5b-6454d0d516fc | -9.4349 | -45.625 | 2026-09-02 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 4af6bdf0-7767-3876-a8b7-ab813ac43ff9 | -7.2536 | -61.1074 | 2026-09-02 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 9e669052-1be0-3e7e-82d1-bcc6c9d68daa | -12.1128 | -47.0886 | 2026-09-02 15:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 127.5 |
| e3196fe4-8996-39d3-8c91-17e98dd9d165 | -7.2006 | -60.6706 | 2026-09-02 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 228.8 |
| 41143ddc-450a-38c9-bcf4-e700ac7386bd | -8.7631 | -46.4418 | 2026-09-02 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 94b2d90f-196f-3c68-8988-4aeae7a6f5f4 | -3.2361 | -61.2359 | 2026-09-02 15:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 0c97d860-77c4-32c2-a4a6-c22cd0dab73d | -0.3046 | -48.6854 | 2026-09-02 15:00:00 | GOES-19 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| b5a5e18b-8df0-3672-b44c-a199f942f976 | -15.2866 | -53.8617 | 2026-09-02 15:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| daa0bf6b-a86a-393a-b050-63c5f14a614b | -6.8018 | -59.4201 | 2026-09-02 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| f62a3bc7-bb44-3cee-8652-5d28a6f1e8b1 | -8.7628 | -46.4642 | 2026-09-02 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 2fb53e1b-eed6-3a9e-a243-aa29a3abaf81 | -6.93 | -45.7157 | 2026-09-02 15:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 906d66e8-c992-35b2-b2fb-53e5ee604b40 | -6.8757 | -59.3978 | 2026-09-02 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| f4a33b5e-735a-37b5-96e9-6cb4a9885f61 | -12.1704 | -47.0806 | 2026-09-02 15:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| ce524f2f-5d5d-329f-b19c-19ddbe1ef4e9 | -4.9604 | -55.8424 | 2026-09-02 15:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 114b10f4-b072-3bc5-9c92-747380c1fc48 | -9.1721 | -59.4823 | 2026-09-02 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 4179a78a-21d3-3531-a38f-94e92505085c | -10.0818 | -46.7217 | 2026-09-02 15:00:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| f72c189d-99cf-3252-80de-2e07f629e7a5 | -12.3622 | -48.1681 | 2026-09-02 15:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| c76b2903-85dc-335c-b267-72d230e4c183 | -3.7533 | -59.3231 | 2026-09-02 15:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| d5a66ff8-a631-3740-8f8d-ad622cf923a0 | -7.3118 | -60.5897 | 2026-09-02 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| de269bcb-d535-3e25-a208-a0ddda909aa4 | -10.8428 | -50.4792 | 2026-09-02 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| edeaa648-6797-3bf0-96e2-2bea20980f3b | -7.3487 | -60.5883 | 2026-09-02 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 322d7115-0c60-3349-a4b1-72f88609fdc7 | -7.0242 | -59.2374 | 2026-09-02 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 2145d48e-9995-313c-b7da-aca0b59e0bcd | -9.8433 | -64.9965 | 2026-09-02 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.1 |
| e5fce39e-9c82-3781-9f36-bd9e74c404ea | -9.8619 | -64.9958 | 2026-09-02 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 625c2174-cb38-39ae-a809-09f55abe21c7 | -4.9788 | -55.8417 | 2026-09-02 15:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 28bb9208-13d8-3307-b0e4-bdc1662a6b37 | -7.0427 | -59.2366 | 2026-09-02 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 0d632ff8-3d97-32a3-ba13-396821344bdb | -3.3688 | -59.3887 | 2026-09-02 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 29469f08-e4af-31dc-8a48-73872b629ea0 | -12.01 | -60.5345 | 2026-09-02 15:00:00 | GOES-19 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| d55d4261-62c6-3086-9bcf-cb9b73e48f5e | -5.5833 | -60.1924 | 2026-09-02 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 131.1 |
| e4d73313-ff31-3025-b47d-ee2c9856e988 | -13.5724 | -59.7362 | 2026-09-02 15:00:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 221bcb72-b443-383c-9040-ba74dcb10f29 | -6.7648 | -59.4408 | 2026-09-02 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 2cca6d49-00c7-3e8c-b1e5-19284f041952 | -9.0243 | -65.4554 | 2026-09-02 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 9059b3ed-744b-3d41-be41-b7ddb4ecb788 | -10.8627 | -45.356 | 2026-09-02 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 84e8fe3c-3a6b-395d-8846-5211d4bb4e36 | -14.6145 | -53.59 | 2026-09-02 15:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 125173db-dd53-33b5-8b51-0be325cea15e | -7.2005 | -60.6897 | 2026-09-02 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 165.6 |
| 26f4c099-96b1-3efd-aa89-1bedf441fe16 | -12.3818 | -48.1433 | 2026-09-02 15:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 8577f7f3-8404-3ceb-9d62-e8dfc27e3f88 | -9.4156 | -45.6499 | 2026-09-02 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 72abb49d-a739-32d3-b49e-bf45d6cd2953 | -7.1123 | -42.7727 | 2026-09-02 15:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 61.8 |
| c56fa020-1536-3163-a417-360b69929572 | -7.2007 | -60.6515 | 2026-09-02 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 6d552090-4042-3fcd-ad55-8bb0944e0e58 | -6.7692 | -58.6679 | 2026-09-02 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| fb915e13-7fbb-34c8-b275-66537c5fcd7a | -11.0437 | -49.6635 | 2026-09-02 15:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| dc94077b-fe1e-3948-87bd-52dcd196a53f | -7.571 | -60.4643 | 2026-09-02 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 128eb0eb-dbb7-3347-9cd2-dca4ecb7fc53 | -7.566 | -61.343 | 2026-09-02 15:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 5b0ec675-dbdc-3ebe-993b-f93f5a7dd1aa | -2.9447 | -60.9002 | 2026-09-02 15:00:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 3e1fbfb4-f026-32ee-ba3f-4fec17e427fa | -13.9853 | -58.6919 | 2026-09-02 15:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 09e46de0-09d2-35f6-a7c7-0026582f8b1f | -7.3117 | -60.6089 | 2026-09-02 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 3ea071f1-6da9-380a-8270-b0a061065d75 | -12.1312 | -47.1309 | 2026-09-02 15:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 25666c6c-ccf1-3fa6-a63c-43193489fcdc | -12.0933 | -47.1138 | 2026-09-02 15:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 136.3 |
| feaf25aa-855a-3ecb-80a2-6297b787db7e | -3.0347 | -61.4846 | 2026-09-02 15:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| ed6824d8-021c-32fa-9a8b-f45554fe5025 | -9.4159 | -45.6271 | 2026-09-02 15:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| f486d86e-6e6a-360c-9d8b-ed6388336171 | -3.3688 | -59.4079 | 2026-09-02 15:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| ed516f68-250b-3332-b27d-ac905ba942e4 | -15.2672 | -53.8642 | 2026-09-02 15:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| b6cc03df-9ac5-39d9-b610-53f448fbd14a | -7.2191 | -60.6699 | 2026-09-02 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 247.0 |
| 28572714-d891-3330-973b-057261e48763 | -12.1508 | -47.1058 | 2026-09-02 15:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 27126e37-1b84-36aa-ba83-413d6d076614 | -1.9776 | -44.7678 | 2026-09-02 15:00:00 | GOES-19 | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 0ac3832f-d00d-3157-8be7-3774cb3adad1 | -1.0182 | -53.7189 | 2026-09-02 15:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| c8028193-ae20-3f6e-bf95-1c508c1f1fef | -3.2455 | -47.9187 | 2026-09-02 15:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| a1188615-99f6-3801-a89c-9ebeaba7b780 | -9.8806 | -64.9764 | 2026-09-02 15:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 3782a935-1039-3603-9b21-8178b7aa2b8b | -8.8925 | -62.3538 | 2026-09-02 15:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 5bdf445b-d076-3039-8c3e-93286679079c | -5.9635 | -57.6899 | 2026-09-02 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 95f93aba-ff75-36a6-be34-081f4f9970c6 | -6.8419 | -41.7032 | 2026-09-02 15:00:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 77.7 |
| 1e60f293-3586-3213-b62f-b1ab90042a9c | -8.7817 | -46.4623 | 2026-09-02 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 3f362b0c-1c62-3285-9783-356db3c1f6ad | -1.959 | -44.7682 | 2026-09-02 15:00:00 | GOES-19 | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 5aaf8df3-4add-37e5-85d3-8cb3b71c6fe9 | -11.0376 | -51.4559 | 2026-09-02 15:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 2c5a7219-ef28-351f-b030-147329fe6b12 | -12.1504 | -47.1283 | 2026-09-02 15:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 175.6 |
| 899c7d40-3542-3c9c-8831-7d991e9a383d | -9.1711 | -49.9835 | 2026-09-02 15:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 5aa8b40d-5948-33a6-a772-83869d8e3a30 | -6.7649 | -59.4216 | 2026-09-02 15:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| b4a4e6df-cdb1-3d60-bbec-9da80c69d075 | -3.2361 | -61.217 | 2026-09-02 15:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 101.9 |
| adc0fc69-d5aa-3025-be0e-2ea60d300ecf | -10.7856 | -50.5066 | 2026-09-02 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 7e86f61f-2e09-32b0-b2fb-e77e4cfa0350 | -3.3452 | -42.8067 | 2026-09-02 15:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 65445e1d-e089-3831-bd5c-e4f75f0926b8 | -11.3806 | -45.1928 | 2026-09-02 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 5ec5f3bd-7f9c-39f6-8551-aa03aac2752b | -10.3959 | -49.9703 | 2026-09-02 15:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 132.3 |
| a387700c-6b98-35f2-b783-43cf778d0078 | -10.3953 | -50.0132 | 2026-09-02 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| b6f7e1c0-5b07-3117-ab99-0e36df44d593 | -5.9635 | -57.6899 | 2026-09-02 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 525f43b0-4301-3efa-8d0d-e0030c7542ec | -9.8433 | -64.9965 | 2026-09-02 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 9508616f-214c-33fb-8cd9-4064f8793771 | -12.1504 | -47.1283 | 2026-09-02 15:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 170.0 |
| d8e27bff-74a5-33f9-8df7-2d7860acc066 | -8.3718 | -62.697 | 2026-09-02 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 7ec2eac9-c2f7-3495-ba92-03d91aaa55d9 | -7.3672 | -60.5875 | 2026-09-02 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| f2318f34-9a02-3c67-af64-44c65fff658c | -9.862 | -64.9771 | 2026-09-02 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 13e385eb-51ea-3746-9494-3674bb4f0f9f | -9.8806 | -64.9764 | 2026-09-02 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.8 |
| ae236731-a68f-3af7-9394-cd8bd2120afe | -6.9872 | -59.2582 | 2026-09-02 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| a1b95029-1343-3a94-8069-ab307d6f4691 | -11.0814 | -47.1585 | 2026-09-02 15:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 57718264-eba1-3e1f-b8c5-3b684dfcb123 | -8.7814 | -46.4847 | 2026-09-02 15:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| aabdc024-6ba2-3b9e-882a-853a6533d578 | -3.2455 | -47.9187 | 2026-09-02 15:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 8d757444-77fa-38e1-84e5-79f27666d9e7 | -7.2007 | -60.6515 | 2026-09-02 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| e0d2984a-f9eb-3952-a134-8fb2042ebc87 | -10.4142 | -50.0112 | 2026-09-02 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 2fd3815b-d61f-3163-b19d-709cec7fb03b | -10.7009 | -47.1835 | 2026-09-02 15:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| ce312dc9-1a76-34bc-805a-aa2143ba929e | -1.0182 | -53.7189 | 2026-09-02 15:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 5f8b6acf-7a74-3047-b9ec-e1128cd5ea90 | -12.1293 | -47.2432 | 2026-09-02 15:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 9f923983-bdbb-340a-94ca-b15a709d2008 | -10.4634 | -46.5638 | 2026-09-02 15:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| a40981bc-5d23-327b-966c-33dfb6bfc5ed | -8.8925 | -62.3538 | 2026-09-02 15:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 7920dafb-95a6-3578-82ca-b28774ebfe6e | -3.2361 | -61.217 | 2026-09-02 15:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |


[Clique aqui para ver as próximas entradas](README83.md)
