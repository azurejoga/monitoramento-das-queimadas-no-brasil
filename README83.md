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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9c44042-69b1-31b2-a94a-bf60ad0aef70 | -7.69412 | -61.09908 | 2025-09-02 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a4ceaf7-ce3e-3aab-93ba-057743f7d823 | -8.65449 | -62.60988 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f432722b-6ef9-3395-a0f3-5a0da8324d9f | -8.73627 | -62.4189 | 2025-09-02 05:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd351d81-e96b-36a5-861b-5b7ad5b4e661 | -9.08927 | -58.89141 | 2025-09-02 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 75beff4e-cdd2-396e-a1cb-b71f00a17456 | -6.33804 | -58.1768 | 2025-09-02 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e0e34241-72de-323d-9488-edb31e57df1e | -7.67143 | -61.08488 | 2025-09-02 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 88fbf9be-3960-35f9-913e-a97d17c6c356 | -7.48008 | -63.82693 | 2025-09-02 05:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c677eba-69cb-3202-a37f-ef9ec85e9319 | -9.11812 | -61.4898 | 2025-09-02 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d00eaf5-e0cc-3d69-b6db-9f9c0cd951ea | -8.85851 | -64.22942 | 2025-09-02 05:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92dae164-d216-37b9-a857-f0f2fa44b79e | -8.6551 | -62.60551 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 523ce4a9-2242-35ba-9b99-2dd539d40128 | -8.72672 | -62.40661 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a00365d-642c-321d-a052-14b6b59f3126 | -8.50624 | -63.90726 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4c2cf7c3-99ba-3219-94a6-719dbe09d985 | -7.78554 | -61.56684 | 2025-09-02 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b41b106f-8824-3a7a-90a4-9ff55aad300f | -8.64636 | -67.2446 | 2025-09-02 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a44cc80-fe89-31f7-8e9c-48d68034b4e4 | -7.08846 | -63.18167 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ecf9bdc-eb29-35a9-be16-656139a45119 | -8.6585 | -62.83288 | 2025-09-02 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6b1997f8-579a-3f9c-b3cd-78434e6ffd0f | -7.54395 | -61.33209 | 2025-09-02 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 2cb8baf8-23f3-390e-836d-f3ba0a7a7a5d | -6.27596 | -62.53978 | 2025-09-02 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec50f563-000a-351b-bfc5-961a288a9049 | -6.75488 | -56.40004 | 2025-09-02 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cdc7fd8-3b49-3628-9aa3-e7ac05f7c871 | -7.60254 | -61.61187 | 2025-09-02 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| df8068bf-5a4b-30f1-bd3f-31d47bf81ce2 | -7.5998 | -61.63126 | 2025-09-02 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47d63156-3fdc-311a-99d4-82271a4a1a5b | -8.66793 | -62.83751 | 2025-09-02 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bc30e45b-ee2c-3b4f-9a6f-12265695b993 | -7.70229 | -61.11109 | 2025-09-02 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b17a9bab-0db0-3cfb-8282-741ee6a28fab | -7.53919 | -61.33149 | 2025-09-02 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c046b00b-6e53-3b5d-84cf-978fada1087c | -8.66021 | -62.92588 | 2025-09-02 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db8af3a1-5dc9-345a-9c2f-23eaa2c3874c | -7.55718 | -63.84174 | 2025-09-02 05:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 586f3fda-0cec-3b36-9409-cec4babf8960 | -6.92318 | -63.13892 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77efc2b4-11fc-3ebf-8bd1-a6acd86a72ba | -7.47657 | -63.82286 | 2025-09-02 05:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8aeb28d-d3c8-355b-95e9-3279c38a8ac0 | -8.66721 | -62.83412 | 2025-09-02 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fa8add86-812f-380e-8bdc-42719e2ba53d | -7.59855 | -61.60641 | 2025-09-02 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bab14544-20d2-3318-8f4b-a69f13fc6e54 | -6.40306 | -62.91413 | 2025-09-02 05:53:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83ce0d02-74a9-34be-aaea-a37b395107c3 | -9.08834 | -58.8885 | 2025-09-02 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4cf73f77-558d-3f4d-9f68-c5174c017bea | -8.72549 | -62.41568 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 150b733d-8db1-3399-95a7-d66b7713783d | -7.54871 | -61.3327 | 2025-09-02 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d9507e05-deb3-315f-932e-f3d7f2304d08 | -9.25899 | -59.75578 | 2025-09-02 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b8d44ee-2727-347e-b1a5-041cdd6d2edc | -7.28172 | -60.65574 | 2025-09-02 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3eea2039-6541-3693-90e2-366b0c025b6f | -8.75117 | -62.42855 | 2025-09-02 05:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30493457-7718-3dc0-a8e6-5c7710a69475 | -7.41588 | -64.35023 | 2025-09-02 05:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b618974-dc03-3fca-bf45-ad656edb2a75 | -8.71772 | -62.42065 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cbc7c2e7-eae7-3ed4-a8f2-cc67dfcf4c15 | -7.60321 | -61.60709 | 2025-09-02 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee83af39-3cbe-3f3f-a76e-8e279a299b50 | -8.70554 | -62.40976 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b9cd650-7833-3de7-a465-c4d465839679 | -6.90806 | -62.94106 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2c21189-1f68-3711-aea0-04489fc6b4c9 | -9.44988 | -60.57538 | 2025-09-02 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd5531c5-383b-3f80-9edc-946c7d95bca7 | -9.26438 | -59.75674 | 2025-09-02 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13dc3b60-d4cd-3d1c-bdb5-d74bfa4ef095 | -8.69655 | -62.4086 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 595758aa-9631-31f4-92fd-676599151424 | -8.67027 | -62.40024 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbf1fd1c-18ce-35a9-8ebc-09ae1d35a50f | -8.72732 | -62.41752 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d3c1c05d-afa9-37c6-aaaf-3b3e79714c71 | -7.54468 | -61.32693 | 2025-09-02 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d6290ec6-4831-318a-bc48-cc9c9dc33ae5 | -9.25192 | -60.49456 | 2025-09-02 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74871272-0fb3-34c0-b0b8-e0e25376ba07 | -8.63741 | -62.60302 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bca9c7f8-9887-33d1-969d-161c3876145e | -7.50344 | -63.49075 | 2025-09-02 05:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12b2103e-8f76-3010-9481-a4cf1e475790 | -7.09518 | -63.1362 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5eac97f0-2fab-37e3-b270-479b4faafbb6 | -7.54798 | -61.33784 | 2025-09-02 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 2b6b1744-e9a3-3446-a8d1-bc56170c87a4 | -8.73323 | -62.42598 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3010b0b4-1869-332a-a2a6-7b81414031fa | -9.25233 | -60.49143 | 2025-09-02 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b982cf28-b143-3500-b510-aa7d6abd8610 | -8.73384 | -62.42154 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b4c6577-803a-3804-938d-438993d4384f | -8.72875 | -62.42533 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c6add38-52f0-3127-9b56-f5ddfe809d18 | -7.25497 | -57.54443 | 2025-09-02 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a7d4c8b-1028-3410-81f3-afccc05df170 | -8.66415 | -62.83268 | 2025-09-02 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d0b10cd-0498-3727-87f5-d371804635e7 | -8.63619 | -62.61171 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 708fda13-2a53-3e93-8095-744d47d699d8 | -7.63548 | -70.57111 | 2025-09-02 05:53:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46971cb2-0e1c-34c3-b772-5539ed2cfc45 | -7.67552 | -61.091 | 2025-09-02 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f19e42f3-cf66-3a2c-b334-dcbb23e8d8d7 | -7.06452 | -62.99436 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b89ba8f-91e4-3798-bec7-65ef0a80d424 | -7.06032 | -62.99376 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5843eedd-90eb-3938-ac70-cf98bba8821d | -6.92372 | -63.13515 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec5ae21a-e276-3972-b72e-f5301ad006a7 | -7.56286 | -63.07048 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b30e761f-62de-3499-8a9b-c395d65eed63 | -7.45121 | -63.15756 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a81a074-c1c4-3ccd-b8b0-bdc7da30f44d | -7.3756 | -64.37148 | 2025-09-02 05:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9fbd113-09bc-3980-818b-cfc6bcf6c64f | -7.67627 | -61.08561 | 2025-09-02 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9f4073ee-8f95-38d6-9c73-71fd1f95b36b | -8.75565 | -62.42922 | 2025-09-02 05:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c8cc4b59-93de-330d-aeb6-a46f6c59300c | -8.64122 | -62.608 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 943272eb-0670-3555-98aa-aa72e50ca743 | -8.73832 | -62.42221 | 2025-09-02 05:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcc145fb-582d-36f9-8c3c-130ae9fb13f7 | -8.6492 | -67.24881 | 2025-09-02 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56e8e774-bc33-327b-b371-43fa9787b408 | -8.75178 | -62.42408 | 2025-09-02 05:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4cfa483-d28e-3a7d-86d4-a1c8f93a9ec8 | -8.65068 | -62.60489 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b69e0028-986e-3668-99c5-23603d33c413 | -7.6072 | -61.61256 | 2025-09-02 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46ba5516-4e43-37d5-93c1-88800f1dce68 | -8.67539 | -62.39633 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c881c101-7b91-3df5-ba8d-048fff140145 | -8.68884 | -62.39841 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4c2884c-6491-30b4-a667-f8eeb12cf9c7 | -9.16417 | -58.8984 | 2025-09-02 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5f4af67-8fb5-3f2e-8b7a-e33abd01e923 | -9.43957 | -60.5741 | 2025-09-02 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e696fde6-77ae-3216-abb9-5fdee6af3577 | -9.08887 | -58.88451 | 2025-09-02 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4db6a5f6-872b-3dc4-a1ef-c45bc6073e3e | -8.7524 | -62.41959 | 2025-09-02 05:53:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa1dd599-904d-377a-93c9-629693a21ceb | -8.64977 | -67.24512 | 2025-09-02 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b180b1b-fb68-3a1a-8df3-3cab6861c4e2 | -9.09027 | -58.88346 | 2025-09-02 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2a6661d-331f-31ec-837d-86482f242671 | -7.07852 | -63.07527 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9c4c461-0922-3d51-b761-56756aa8b3e3 | -7.55864 | -63.06986 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1ff0649d-972e-3cda-9547-8f630ed7cdc9 | -8.73115 | -62.42267 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68e6e082-4200-3471-9fea-2e5b701a35c7 | -8.66974 | -62.84734 | 2025-09-02 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60cdd9aa-0bca-3b4c-accd-8c0c2a137a9b | -6.39821 | -58.21001 | 2025-09-02 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9f0eba49-a81b-3f2a-ae2c-74f98fffde51 | -7.6651 | -61.09495 | 2025-09-02 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4880167-eaa0-3183-98b7-1760d70df666 | -8.65318 | -67.24564 | 2025-09-02 05:53:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cd6e2bb-8db9-3fc0-b023-f7b374a2c053 | -9.44432 | -60.57779 | 2025-09-02 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da99d662-bd44-347e-bd25-c2a8474e4885 | -8.67112 | -62.84657 | 2025-09-02 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b711cff4-097d-3acf-8510-4cd5f4f512e0 | -7.55823 | -63.07027 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4a944274-92cf-3e6e-95c6-afaca6c5dedb | -8.66357 | -62.83688 | 2025-09-02 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2fbebc17-662c-39f0-8a32-785c14a6c8ac | -8.64564 | -62.60863 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c6e8884-1d8c-3f02-ba36-fe0430ed29b3 | -7.16447 | -71.50111 | 2025-09-02 05:53:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e25e5b4e-02c1-3d19-af63-66521afee35e | -8.68821 | -62.40285 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce33807a-13cf-3763-8274-4ffa20c40ed3 | -8.65824 | -62.92649 | 2025-09-02 05:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bf9fbf3-abe9-3ff0-94ca-9e31e44ec7bf | -7.27676 | -60.65503 | 2025-09-02 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README84.md)
