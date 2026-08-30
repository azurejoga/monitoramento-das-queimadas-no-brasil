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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 785275d9-0e35-3338-884f-7402b16681a5 | -9.58924 | -61.0297 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cfa7ade-1fe1-34c7-9700-d242d01b3e70 | -7.23901 | -60.62699 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4a648575-1013-361a-880a-5c807536d58e | -6.78841 | -55.68314 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cd409db-6aea-34b0-8b33-165fec695ddb | -8.58935 | -66.96217 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1b385a5-af18-3ef2-8a5e-c648561becd2 | -7.29747 | -60.59921 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7eb6fa1e-7879-3d8f-a127-32d318b367ef | -9.09261 | -65.48539 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c8f053b7-c715-3dab-915e-e8904049573d | -7.56287 | -61.31787 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 131f6317-7d4d-3522-8985-f333d2713aa9 | -9.0027 | -65.45701 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05e43a99-c095-30e9-88d5-8e99fa6989df | -7.56675 | -61.31845 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8e95f465-3e3d-31ac-8b7a-267537666909 | -9.22019 | -59.76081 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b900226-0452-3643-98f5-e4868e216db0 | -6.78996 | -55.6722 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7493761e-d2ed-336d-85b4-61cfa65efc62 | -9.00268 | -65.43542 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ecd687b5-3196-3f1c-bc60-007d99318570 | -8.17817 | -54.93988 | 2026-08-30 05:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8fa3db4f-7c01-3d37-8eef-b1f94ec02f5b | -3.48924 | -54.66254 | 2026-08-30 05:53:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d92c8e3f-f460-3108-a70e-035d7770a638 | -7.24303 | -60.62764 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 833c5f4c-2495-3546-8e54-cf3d5b21fd07 | -8.99992 | -65.45297 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a12c2c62-7fd6-3ae7-9c03-711189f87bfd | -8.58657 | -66.95805 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 189e1156-b818-3701-bf67-da3f39df1020 | -7.23497 | -60.62642 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 770659c6-dec3-365e-91d5-34678072d383 | -8.15543 | -63.99926 | 2026-08-30 05:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d825261-8a63-3c20-9c2c-49bd7b7c3bf2 | -9.06033 | -65.40826 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4cd9f14-99b3-3d08-a811-89a07b253b61 | -8.50672 | -55.28866 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d21d024c-7243-3e5e-8951-c36960759491 | -9.78921 | -59.43493 | 2026-08-30 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 202373f4-4e7f-3fbb-90f5-899293d99cdc | -9.8898 | -60.26725 | 2026-08-30 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0e07042-15e1-389d-9de7-064b8ecea23e | -9.89458 | -60.28308 | 2026-08-30 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 95522d3d-826b-3db8-8029-4cd9f7d7bfba | -9.71184 | -60.72828 | 2026-08-30 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25d77ca9-c6e6-3f97-a94f-5a9ebbc9b4ce | -9.15854 | -59.5052 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a91ac30e-cdb9-3c60-a2f6-a1083952d02b | -9.01886 | -57.54016 | 2026-08-30 05:53:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f80258d-a561-3891-914f-e7c863c9ef13 | -9.1496 | -59.50393 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5402f929-0106-30f8-87a4-e3e19cdc3991 | -8.46984 | -62.71207 | 2026-08-30 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de8f2ce7-4dbb-399a-bb71-d3f57af86a53 | -9.14079 | -61.10196 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89b75a4c-3219-38d8-b645-ba16a2f10b4b | -7.00358 | -59.65538 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dec7f17b-3ca1-3a4c-af4a-274887bd2c48 | -7.2985 | -60.59218 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2017186d-6e50-3ed8-9220-f70cfeb9cc13 | -6.90587 | -59.79669 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25f5443b-744b-3729-8131-1ff7438b7b8c | -7.5527 | -61.30641 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 43dbfa65-b8b4-31a4-ae98-a2d988b4a869 | 0.1386 | -60.40648 | 2026-08-30 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4e2c4bd-b5ed-3b76-ae4c-5188265f79ee | -9.05922 | -65.41529 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86dd959a-6287-3c48-88b5-7050396ca974 | -6.77878 | -55.6704 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40304afa-c70c-323d-9f55-8d1d5aaf5a9f | -9.05867 | -65.41881 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fe388f3f-0675-346d-803f-fb5727081083 | -7.48371 | -61.39949 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1eb433ea-3707-3907-929f-5aca1dd3116c | -8.94864 | -62.37477 | 2026-08-30 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f6aa71a9-6e43-3a5b-ba21-8493430816a0 | -7.70316 | -61.15546 | 2026-08-30 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2be94728-0a55-3e3c-82d1-9841564b450f | -9.14981 | -61.09616 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5596fda-64ea-3e59-b21e-56bd50aec237 | -9.88864 | -60.27535 | 2026-08-30 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 071d7d2b-04b8-350e-b109-45abfb86619d | -1.25304 | -55.70417 | 2026-08-30 05:53:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3c1c032-c452-3504-beac-f1175ee49485 | -7.30908 | -60.60455 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbb0fc71-b72d-3289-95df-0d8c18f5f8aa | 0.14685 | -60.39843 | 2026-08-30 05:53:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1c79fe2-b211-3902-84fe-d7700f90c7c8 | -7.8407 | -62.31467 | 2026-08-30 05:53:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| def02a05-251e-3eb3-a4a5-100442214559 | -7.30203 | -60.59629 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6bbc4866-f44e-3c6b-82f9-1aa89a965a91 | -6.93567 | -55.70287 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31a5732f-a6a7-35a7-8be4-fd6e673f1d81 | -9.0976 | -65.47539 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8f0ac26-57c5-305e-b1cb-993478897d2f | -9.05644 | -65.41125 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bcd8c1ba-951c-3be6-a559-fc5e8c9d1b3c | -8.63331 | -66.54108 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ebd390db-6b52-3a19-b433-346b78e029d5 | -7.30607 | -60.59689 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a171ae8-84f7-36c0-abe3-bbc97e953dc8 | -8.95606 | -62.3759 | 2026-08-30 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1921325e-9255-349c-b345-7b77541a68d2 | 1.16159 | -60.67054 | 2026-08-30 05:53:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a07d067d-2599-36c4-a258-969f4bbfb6d8 | -9.05033 | -65.40668 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cd4b46e6-7d33-3017-bec9-9b5ff0ceee6d | -8.25016 | -62.75524 | 2026-08-30 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9789dec3-f64c-30ba-94d1-a0e63746649d | -9.71323 | -60.74784 | 2026-08-30 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6572a845-caff-31b3-ac0d-d41d0ac13cac | -7.69849 | -61.15985 | 2026-08-30 05:53:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9a8d0eef-29eb-3418-80af-420681e5cdda | -8.95235 | -62.37533 | 2026-08-30 05:53:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 043a85db-7c46-3895-9c3f-3e539fdcb009 | -9.05366 | -65.4072 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 95394dc6-562a-3204-b982-f7af8453e449 | -9.64978 | -58.93696 | 2026-08-30 05:53:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7338e5cc-5c0b-3574-a821-30e44b96bc5e | -9.6472 | -58.93824 | 2026-08-30 05:53:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aee94a06-85ac-3422-8bc6-e5006ef9e557 | -7.48301 | -61.40428 | 2026-08-30 05:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e58990c7-7ae0-3500-bdf4-19b2802c3960 | -9.01043 | -65.40787 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2ae543e-b626-373d-98ac-cc5b5e9748b0 | -8.62799 | -66.5399 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cb85e96-12d0-37f5-82da-7198dd64fbca | -7.009 | -59.64806 | 2026-08-30 05:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ca384ba-2020-34f3-98ab-20e3639b63ee | -9.04923 | -65.4137 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2f449670-122f-372e-8534-d22eaee8f404 | -9.2191 | -59.76402 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b91379b7-03cc-3d8e-9d13-434063c4547f | -9.84523 | -60.2731 | 2026-08-30 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 25bea34f-0dce-3961-ad38-cf0a2622517b | -9.01765 | -65.40541 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7b295c7-2f3c-33c6-8a90-c83dd037c462 | -9.24148 | -60.41341 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f541114-60c2-32ce-a7e1-79500c35ad23 | -9.09316 | -65.48188 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ce5560f6-5345-37ac-ad59-055131fba46b | -9.16089 | -59.50775 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc80c75c-db2d-3256-8fb2-45b94b7a1ee0 | -8.49972 | -55.29627 | 2026-08-30 05:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 750859e5-df12-3526-bf8f-6172c967cb6a | -9.65191 | -58.93874 | 2026-08-30 05:53:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcea938e-8d02-308a-84b0-e376e355207d | -9.05534 | -65.41828 | 2026-08-30 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2339fc74-82c4-35d6-9bc9-d239fca660fb | -9.2235 | -59.76465 | 2026-08-30 05:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3715f8d5-c07f-3175-aa1b-2285d21ff187 | -4.95797 | -55.84579 | 2026-08-30 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 897598f1-3bbf-368a-b269-8bebc9f71d86 | -9.38301 | -66.51445 | 2026-08-30 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75f0dbaa-c7a4-30fc-8f39-7fd3d4fc6667 | -9.54213 | -67.16437 | 2026-08-30 05:55:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0eb9de24-b564-34b0-a66b-76a4ce7984b5 | -8.60427 | -70.21489 | 2026-08-30 05:55:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2467e2b1-d433-3d20-a774-18956ed2b384 | -9.93894 | -60.52462 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ac0057b9-6333-3cc5-b5a3-92e89a0ff9b2 | -8.93315 | -67.36069 | 2026-08-30 05:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 9e358f3a-6940-3e29-b0a0-ff68a9f09de7 | -5.8891 | -57.76255 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 345ba0ff-dfec-3eb2-bf4a-c28a20a41274 | -3.63363 | -60.5516 | 2026-08-30 05:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b015ec2f-bc4d-3707-98b6-e12a83eca35c | -10.50468 | -64.52808 | 2026-08-30 05:55:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eafc4415-7034-33a2-9495-38c3f1da171c | -3.7678 | -59.33667 | 2026-08-30 05:55:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2fe0087f-a547-3f64-a2e3-2472503ba70b | -4.15871 | -60.69583 | 2026-08-30 05:55:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0ab18765-c773-31b6-ae16-464f58a116e4 | -3.62665 | -60.54568 | 2026-08-30 05:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 931826ae-7a77-399a-b9d5-2dd79fd8561d | -6.12034 | -53.55643 | 2026-08-30 05:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d171346e-8901-3eed-84aa-1a63ee658f6c | -10.4834 | -59.60584 | 2026-08-30 05:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0df193c-edf9-3dad-ab08-5f4b12db6cdc | -11.62999 | -54.59372 | 2026-08-30 05:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0cc6dbf-efe3-3746-bfbf-3309f016fe12 | -3.63676 | -60.55691 | 2026-08-30 05:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9e22a76e-fd2d-362b-a19b-e06764faa13b | -3.6305 | -60.54626 | 2026-08-30 05:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5bfcfc41-e912-32bd-984f-6d65c6e654d1 | -8.93198 | -67.36794 | 2026-08-30 05:55:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2f54224c-6c02-3a42-9472-93bb41a1516f | -11.23792 | -54.00596 | 2026-08-30 05:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e7894367-193f-3b44-9127-442c67f74763 | -4.4771 | -55.7634 | 2026-08-30 05:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 73ebed1e-637a-38f9-aead-bb346e516e2b | -5.89543 | -57.75256 | 2026-08-30 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8443f6f9-00c8-34b2-abe9-f263c55aa401 | -3.62593 | -60.55043 | 2026-08-30 05:55:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README68.md)
