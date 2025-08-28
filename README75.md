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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d77391b-15c8-3812-961b-271dc7d9729a | -6.15463 | -55.80391 | 2025-08-28 05:25:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f63cc4d5-5da1-3196-af01-dead42fac47e | -8.9279 | -65.92735 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd043334-38ea-341b-a5c9-e7548eabc9d0 | -10.25712 | -64.50471 | 2025-08-28 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b90ea76-735b-30db-bbe6-f24cfe77aa0b | -9.12853 | -65.77306 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1786e106-86f6-35b7-b176-3373b7949aeb | -8.95797 | -65.94424 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df3e2432-033b-39b6-9a9a-1f47190830b9 | -10.79054 | -60.79797 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 76eae0fb-296b-3b9b-af18-bb185ba6112f | -8.34364 | -62.93512 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0c7980c-9424-3929-91af-f5a23ecddb3d | -12.85742 | -48.12233 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 759616ac-2c5c-3b5d-88d4-9731d017aa58 | -8.87807 | -60.7686 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a3f7fa7-7b21-3eaa-9b32-8511b4d0fa47 | -9.51257 | -62.78865 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6efbe249-0c5e-3018-8f1d-fde4fc4bbd32 | -8.8742 | -60.77156 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75da85e8-9456-385f-8baa-766382561fe3 | -11.23026 | -55.05774 | 2025-08-28 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 146f47c6-b494-3a1a-84b2-2b9dbc29c79e | -9.19129 | -60.79697 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86892534-2c5a-3666-8ccf-6dffb7ad01af | -12.78996 | -48.14817 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b40a4f17-0327-3438-b1ad-d8de547a5b61 | -7.46943 | -61.39599 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91549ac2-8444-3ca2-8f5b-85020a90be7d | -10.25132 | -64.49503 | 2025-08-28 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 161b7139-35bf-38bd-8941-178949736a87 | -9.14268 | -62.3545 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b36ee923-929c-37e0-9335-760e44bdd2a0 | -10.46782 | -57.95098 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e04110c-1203-3c92-8392-2ba7330c0260 | -9.46896 | -57.84266 | 2025-08-28 05:25:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ade7872-2005-3492-8bab-a8d519029606 | -8.8814 | -62.48015 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23c8a97e-f70f-3f9a-ab12-d568c07f3a66 | -8.07281 | -61.53611 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 87825465-b917-3116-8eb1-fc9d33bed461 | -13.62204 | -48.23775 | 2025-08-28 05:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2d705bfa-a36b-31f8-ac0e-7b93a8307c93 | -13.63115 | -48.21935 | 2025-08-28 05:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b1d4400a-adcf-3096-8523-7b36f53692eb | -8.34425 | -62.93134 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| edb3b447-5c8d-3202-ab91-23800eb3b7a6 | -9.16552 | -59.57246 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e1028f7-4ca5-3f9d-ba2f-c628b74bdf96 | -10.8094 | -60.76469 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 8d8ec566-2f03-3fbf-9506-a7cf74dee81d | -10.47022 | -57.96021 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0e327e11-4d78-3c54-a487-7566b65b2d52 | -13.37777 | -51.75444 | 2025-08-28 05:25:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f784d94-907a-3e76-8a02-d4ea6595f200 | -10.15432 | -64.2457 | 2025-08-28 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ec2b196f-3198-39d2-a485-f1d150763221 | -7.41355 | -60.61846 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d7b5cae-7c14-3fc6-9252-f71f5dc0c076 | -9.54761 | -65.68855 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0bb05536-597f-3711-b4f7-0e81858bb766 | -9.24104 | -59.78518 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a40cd5cc-d39b-3ad9-bbbd-6b5f35b93ca2 | -13.14159 | -54.92525 | 2025-08-28 05:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47481584-b7b1-3129-a2db-c7e0615ae351 | -9.0221 | -65.6897 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ea1f4fc5-6e7d-3929-8150-1a7c05c90c38 | -9.07044 | -66.06516 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f3a013a-d16c-34c8-be66-ec9f03e4e2f8 | -13.00961 | -56.8978 | 2025-08-28 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b97ea48-ced9-31e9-9d1b-d4fec10b1207 | -9.27083 | -59.77148 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c3310223-b685-3084-b3e1-dc1d7dc60514 | -10.83671 | -60.80897 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 65da3d40-dbd3-33f7-b2eb-7c1153c872a5 | -6.89054 | -62.92941 | 2025-08-28 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0997b999-7552-34d0-b0d5-28d86e561b15 | -9.16269 | -59.56829 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45f85c0b-19f2-30f8-a47b-8994538c89d8 | -9.40924 | -60.52556 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2aaa8696-44ba-3c84-a142-6e8e5e63e9ac | -7.34917 | -59.65104 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 182376bd-a08e-3a78-823f-987b6871186c | -8.74091 | -71.00176 | 2025-08-28 05:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa03f4c2-1f93-38f1-8d6f-32a0b8d23654 | -10.7916 | -60.76912 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 944739c3-7b2a-3a2f-bd7a-98e8c28b5d22 | -13.01415 | -56.89479 | 2025-08-28 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 297dd786-3144-3c1a-bc09-96398aa726b6 | -10.25161 | -64.49252 | 2025-08-28 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b24c9e1-74fd-3731-9c97-a1df9aa89de7 | -9.40599 | -60.56833 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc88df09-0b24-3b1d-bb25-a5da2cb4dabc | -9.48776 | -62.38095 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef1dfeb2-2f7e-37b2-a410-8d05f27d3225 | -8.95434 | -65.96529 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 89a04817-8f39-31dd-94f8-0d8ce702b7b7 | -9.18134 | -59.51493 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e9812a2-cbd5-3c35-985e-ccdf5f272959 | -7.28117 | -60.29451 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa5ca057-d299-3a97-a0f6-fbbc61faf642 | -9.48381 | -62.38402 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e7a299e-bc75-3adb-a8b3-5123df08ac96 | -9.54333 | -68.57874 | 2025-08-28 05:25:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6d2f0d15-7f07-39d4-bb0c-d63948b24f6f | -9.18578 | -60.81038 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8a69936-c3e8-391f-a1e2-a7f46cc5c609 | -9.40869 | -60.52908 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1685073b-274e-3b50-8cf7-a42601101b0c | -8.96435 | -62.15995 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8f2a368-4a93-3268-96af-d6fc26bd8062 | -8.87695 | -60.7541 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b376a83-9d6d-3ad6-b32c-c5fb4bc6548e | -8.90292 | -62.47619 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27c1ba85-275f-3a11-ad2f-3e5f4d12c8c8 | -6.13476 | -57.93523 | 2025-08-28 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa04065b-f282-3852-9b94-f71624c3f1db | -10.08291 | -62.89246 | 2025-08-28 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7efd1af8-06dc-3c16-8f3a-2f2aea0c514e | -9.1299 | -65.78898 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a3e738be-7cd6-342c-bf8f-a9986989f192 | -6.91439 | -62.93731 | 2025-08-28 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d67ab19a-3ba5-39f8-bc17-2bf686d371db | -6.01482 | -57.84952 | 2025-08-28 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd20ea7e-290e-31f5-b0ff-35302bf5b043 | -7.56678 | -63.86329 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fc67602-8f0b-328b-b2b9-20d874f23071 | -9.15001 | -62.35199 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fff49313-53ba-3f6a-a4ac-54400f8e4b27 | -9.46579 | -62.38844 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70aa99a9-fdb8-335d-98af-2d3726f3e4c1 | -9.47765 | -62.37931 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0688e3f2-dafb-322b-b36b-dad5f4ecd913 | -9.46057 | -60.30567 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 888f64b0-24a0-3874-9b87-9b2373fc49fe | -8.56066 | -64.22079 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc45af24-1722-3187-adaf-77955c54a9b1 | -10.79105 | -60.77265 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 3b400815-5e66-31df-9f4e-908c4f27c9e5 | -13.63605 | -48.24137 | 2025-08-28 05:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55731483-a5d2-3b72-b825-0bff33ffbd09 | -9.46112 | -60.30212 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7601eab-2560-35cb-9bd0-d5d4eece5933 | -9.40865 | -60.50742 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6953df86-ad2a-3122-8f5c-3347acf68c91 | -9.10831 | -65.74857 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6342730c-2788-3ef3-93ca-175aba1f91ba | -9.18911 | -60.81092 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 344971b3-958c-3eae-a93a-31f556a3168a | -8.23447 | -61.45724 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f05578c7-c139-3287-9005-796cd7bc97ab | -9.41599 | -60.56991 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15a0224f-650b-3d0c-8a0e-8a48bcb06da8 | -9.17677 | -59.45406 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48b861f6-f2f2-35a7-8513-fdf2e7995a52 | -9.16521 | -60.76771 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a6c6ad9-4b71-35fc-b1de-4825e53392bf | -9.11976 | -65.77673 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 42f97358-b236-382d-b82e-8dff42ec1265 | -9.17398 | -59.51752 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c51e42bd-07c5-378a-b1bc-107149abc49f | -9.15222 | -62.35976 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1c1242f-d082-383a-9269-2ee8deefbace | -8.93152 | -65.92567 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28c82b17-0d97-32e1-a295-e78678449f29 | -7.35853 | -57.62601 | 2025-08-28 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8978cd47-58d0-3d2f-b320-3d54aa775b6c | -6.62536 | -60.01631 | 2025-08-28 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2a5a52c-9310-3a65-82c4-0283e6bfef2a | -8.05932 | -61.59903 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e7c4afc-72a0-39fe-b4af-0a7c6698a836 | -9.53013 | -62.40219 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfb1656c-491f-31d4-9fa2-c2fce020e0d5 | -9.80834 | -63.07722 | 2025-08-28 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c07c5ea-7bde-3da6-bec1-9c40509796b0 | -9.48265 | -62.39122 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8cfcc8c5-bb40-3742-86a6-d581112c7174 | -9.41427 | -60.53717 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c330dc39-4c56-314d-b4b0-7b918e6dbb52 | -9.4667 | -60.31028 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 135e31ba-45a1-3472-9287-e7ae0c0602b9 | -9.13558 | -65.77951 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91d9c34f-d73b-3f85-8a23-93331cd68e18 | -8.88747 | -60.75219 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f53ef11-edc8-3454-b0b5-bc4d24235f30 | -8.89773 | -60.55658 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff5f7fc1-c211-359a-893a-2ff3b27b1f30 | -9.73112 | -64.90598 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4e8baded-86d9-3888-b1ae-0f19cfe2d18a | -9.12062 | -65.7717 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 4243b859-4195-3f61-8ff5-51b8211b6c51 | -13.60189 | -48.22366 | 2025-08-28 05:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c6b7e8c9-eb3d-3935-baae-57e31e352972 | -9.41368 | -60.51905 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76e84640-cdac-3477-bab6-ac8e1ddf2f61 | -9.41646 | -60.52309 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f71b860-f909-34aa-9325-c00044967ed8 | -10.94027 | -63.63644 | 2025-08-28 05:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README76.md)
