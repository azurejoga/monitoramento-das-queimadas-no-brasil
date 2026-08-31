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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9298f6f2-c936-3ca6-a1cf-531537f4caf8 | -14.22033 | -52.84735 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 822045f9-d771-353e-9c4d-5bde619efb0e | -10.74419 | -54.01754 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0d8b723-c5e3-354a-b119-a52147dc291f | -11.93285 | -45.05881 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 072b5e3d-8370-3bc6-b54c-4c41f1ee27a4 | -10.75209 | -54.03358 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dcc01dc-4c73-3681-921c-79390e8e20b6 | -8.62233 | -54.69228 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d772ec3d-0dfe-37da-af0f-fcb5e3eb9eca | -8.95038 | -62.36852 | 2026-08-31 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a9188566-2f9a-3963-8f1d-48f87fd26481 | -14.41131 | -52.52976 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 071a0554-4e5c-3006-9349-cf1158b25d35 | -9.4137 | -51.69162 | 2026-08-31 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 363ba797-533d-325f-a3d2-69617b66b5cf | -10.50622 | -59.62006 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1082f5a0-0ecf-3423-8cbe-e3f65324c6e1 | -9.89723 | -60.28404 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13e6ed46-2534-33db-abd9-5526294e44d3 | -7.55787 | -61.31936 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5663471e-6672-308e-9b23-2d5f623aeb2e | -9.85572 | -64.98846 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f987e0c-4cfc-3e94-a3ec-7de3cde71706 | -12.10705 | -45.03466 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d3a7d9fb-319f-3a7f-a644-08024965bc0e | -9.86125 | -64.98949 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3617efa-fe4b-3f83-b828-22e887f03d8a | -7.61127 | -61.36993 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| ab031b07-c81d-3539-981c-736cd0a38cad | -14.39339 | -52.54984 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe6c2dfd-b204-359c-a636-9f39199e1681 | -10.15363 | -45.70079 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e98b4b1-6264-3f76-8656-e4323d53c183 | -8.96654 | -62.38708 | 2026-08-31 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8fc58862-a2c0-3d26-b6fb-2f8df95db726 | -13.36374 | -46.91793 | 2026-08-31 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ab93284b-e954-311d-8983-f4369382b093 | -9.85055 | -64.98775 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5213f4f9-5223-396e-a71c-5df8e3c2550e | -14.19712 | -44.58436 | 2026-08-31 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11d15418-29ab-3a46-8f53-4e0b3947ad14 | -9.93961 | -60.52442 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ad06e79-7a7e-362e-b4d8-aa74ba8c286c | -10.15515 | -45.7333 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 985a2509-f8c8-3e67-bba2-65401b92bbfa | -8.55649 | -54.78862 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 786a95c0-f0d1-3152-8b6c-cd493ac2078f | -7.91068 | -61.31974 | 2026-08-31 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f79b6e15-32c2-3d4b-9e51-f8d0475dd46d | -12.77853 | -46.4576 | 2026-08-31 04:59:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d8b33b54-2314-3ec2-b612-14e7508b01a7 | -12.39004 | -46.45362 | 2026-08-31 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e51eacea-d995-3946-bd34-91a8675229ae | -9.07031 | -60.49511 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ecf82157-fa4e-3fba-b228-646a1056b203 | -13.45819 | -57.04634 | 2026-08-31 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0112ec6-8364-38b3-92b1-77b222f0b6b0 | -7.57841 | -61.34563 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f271ec55-f13b-317c-b6f2-051356b7f699 | -9.16006 | -59.54407 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a134b0c4-fcc2-3f31-be81-b59742e3ba92 | -11.33702 | -45.19958 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e1ce106-6b07-3d36-b067-d3d7275dffa6 | -11.22022 | -45.09292 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8bea7c8d-aec4-3641-99c7-7b69ccf76f42 | -11.49318 | -60.58927 | 2026-08-31 04:59:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 57be2e1f-73d7-3298-a8f8-681cc967e4a0 | -12.07683 | -44.98904 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0eef428f-644b-39ab-ad80-60a2aacf6fc3 | -11.03499 | -57.23755 | 2026-08-31 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17748fa9-c8a5-3274-a11e-11f3ff8aa071 | -8.59221 | -54.7551 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2bfd592-cf9d-3671-b1c9-86195790c538 | -10.799 | -50.65536 | 2026-08-31 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 65eba174-8395-35d6-96d2-342bacedb036 | -9.16196 | -59.5087 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed11a943-dd4f-35ef-bfb4-963eeabba31e | -14.39212 | -52.55873 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aae57250-8921-3b45-92e4-5bdde651c16c | -14.15773 | -52.78725 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9121c258-a212-3371-a862-ddaad36b4784 | -10.7745 | -54.04447 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25dbdcd2-559b-3468-8f21-233f00cbd0d9 | -14.20132 | -46.56392 | 2026-08-31 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3822df65-0713-3155-8bbf-5fbf618aacd2 | -11.6791 | -47.60363 | 2026-08-31 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d267b85-45f5-3f94-8e35-ef270faa450c | -11.21116 | -45.12 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79acdf82-f0ed-3563-acde-e21483a73aef | -12.09535 | -47.25912 | 2026-08-31 04:59:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| abc2cc93-f587-3bcc-b55c-d5a4fe2f5cd0 | -8.67808 | -66.52676 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ec3eecc4-dcf9-382d-b6d8-dd0fde15ce44 | -10.75045 | -54.04442 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ddb56f26-1b1e-31ba-ac90-71f4efd7ce32 | -10.83892 | -45.32183 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40e45bcd-1e13-3f08-a2c5-cf92a7a2654c | -8.26096 | -62.75595 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a48dfdbb-8f62-38cf-b09a-6296a129c818 | -10.83676 | -45.31188 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01d50a82-1ed4-3f3f-bd04-b98cf4364e11 | -10.98086 | -48.41491 | 2026-08-31 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6e19f737-b1c7-3692-afc5-77c92160943f | -9.93525 | -60.50084 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1b87b7b-6804-3ded-82b2-6c483e23e81f | -14.98134 | -48.15337 | 2026-08-31 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6070e6fa-0e7d-3523-9278-a7a9a82dff22 | -10.16101 | -45.73057 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a35b501f-a171-36cc-b36f-e7f187c9ef08 | -9.14835 | -59.54213 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e0e58ff7-8bad-334f-ab80-02517d0eeecd | -8.62179 | -54.69575 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 037dabc4-51e0-38b1-88d4-c23a1bc6dcb4 | -10.75388 | -54.06713 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c2c3092b-366c-3324-8df6-9f50cf97abb1 | -11.87854 | -45.81972 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a80d51ff-d966-34ea-9675-eea9b0499c43 | -10.57771 | -57.50128 | 2026-08-31 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c69bc5f-c3a7-3421-8aea-556e4e0410a0 | -10.80363 | -50.65087 | 2026-08-31 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1a1e1823-2e58-3b29-8a0b-81e10bc5e261 | -10.05346 | -48.69288 | 2026-08-31 04:59:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8fb571f-dbbc-3e76-a1c6-b49fa8011cb0 | -14.60294 | -54.09512 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 698b627c-7f03-3908-9462-558c53719b96 | -11.08507 | -51.50897 | 2026-08-31 04:59:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dee1d8aa-540e-3476-b00c-cd22847a8994 | -14.60009 | -54.1144 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b94329fd-242b-3009-a7a2-b39bd545bde9 | -11.37053 | -45.16288 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58fcc654-7f6b-3462-a0a8-43743934fb65 | -10.48402 | -59.61131 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa025212-ed7e-3e8a-b36c-f2f5619f8a40 | -9.22452 | -59.56845 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8ae9b7d-9d91-35fa-b1da-5f8447102715 | -7.4417 | -61.42647 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa6d86c9-c61d-36b7-8564-1e422245b508 | -10.76202 | -50.8574 | 2026-08-31 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74fe4b42-d5af-350b-8067-e01c0a47c831 | -14.22999 | -52.85742 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d2f09cd8-738c-3bc8-8cd0-7d9ee89b4e0d | -9.00078 | -65.44009 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f70ee344-cf5d-3c54-a940-c940f71e3bd6 | -15.19105 | -46.24459 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d5bfbf0-16d2-3aa0-9f6c-5509f6bab5b0 | -9.08362 | -53.03429 | 2026-08-31 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 302d4088-66ea-37e9-bec0-0b7ddb84b3cf | -10.75107 | -54.06302 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8987b33-c79d-32f8-8641-2c1eaa570cb0 | -10.446 | -46.76202 | 2026-08-31 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e0d5c4c4-d6e7-3f57-a96d-982f26500cdf | -9.17295 | -59.61127 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9e6cc5e2-7303-34cb-b3b4-71907ec2507f | -10.15242 | -45.74032 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 80c7df8b-3bf6-3610-ba39-965c31f38633 | -15.65982 | -45.91295 | 2026-08-31 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46e8a3f1-c349-3a28-ad15-793a320bdf1d | -12.95693 | -45.94556 | 2026-08-31 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d82d93a7-73e3-397b-8305-323384035ac0 | -10.14744 | -45.69381 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd65d38a-de4e-3da7-8e24-83d7c1ea58db | -12.78319 | -46.46404 | 2026-08-31 04:59:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee9c8e25-8951-35f0-886c-aa76923e2ca4 | -9.85123 | -64.98405 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3cfe301-66ff-3aed-ab59-18bb1ebd45e0 | -11.18854 | -55.11168 | 2026-08-31 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e20432f6-261b-31f0-8881-308d994ff66c | -11.1746 | -51.31685 | 2026-08-31 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f4b4bb5-454f-30b8-bbde-65bafedb51f1 | -10.14637 | -45.75969 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 29973f3e-3930-3d76-bc69-566fabd38ece | -7.79237 | -61.57711 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37979284-8e42-3770-87b9-c378cb4f7e2e | -9.94025 | -60.52071 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8de3bd3-5583-354d-970b-f9b64f53c357 | -8.55741 | -54.71767 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 074ced89-e2e4-35c0-8e70-2f2b29da4b33 | -12.40032 | -46.4581 | 2026-08-31 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f8b0a16-62ce-3c24-891f-00fdd3c95f6e | -10.44341 | -64.4623 | 2026-08-31 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc0d17f4-c64c-3199-892f-eff8aeb482b5 | -15.19628 | -46.24856 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 396f9984-2cce-368f-b417-8dab434a9c52 | -13.47387 | -57.03413 | 2026-08-31 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca786e88-ca6a-36c0-86ad-9ae29a7f593f | -9.02724 | -65.39746 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e018e798-be9f-3450-8737-cbbfb244a533 | -14.46725 | -52.19458 | 2026-08-31 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15313f88-8a36-3722-93c2-1901412b1dd0 | -11.3266 | -45.18969 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2edbcb9b-ed7b-3b1e-9855-4d48ce17698f | -7.40287 | -60.58477 | 2026-08-31 04:59:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df757b74-e51b-318d-aec4-375f4d7d88bb | -9.03298 | -65.39855 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cd267eb-d374-3a82-9b5a-cbbd12a167b3 | -10.80035 | -50.50782 | 2026-08-31 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3542420a-da6b-3186-9e56-b6056f9163f0 | -14.20277 | -44.58999 | 2026-08-31 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README46.md)
