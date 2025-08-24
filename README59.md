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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49610da5-97d1-34df-9d58-cd56aa1654b3 | -5.7957 | -59.2131 | 2025-08-24 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53d02e38-5928-345d-9556-cf08f7a6a945 | -8.63227 | -62.63489 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9eb856f1-b631-31bb-8bf2-56d48bc9a7e7 | -9.18073 | -59.46711 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 87d032f2-a2d0-3c9a-94e8-d3d5ef1aa2af | -9.18146 | -59.65339 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a374910-084d-3cc9-a965-94c1ca908a94 | -8.71558 | -51.13656 | 2025-08-24 04:59:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9990f943-581a-35b1-966d-8fdc4c9c643a | -8.61373 | -62.59684 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| fd490e52-402b-33db-83ba-1ff1ebb6347d | -9.15669 | -60.81285 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b872443-462e-3f74-99c8-ac1d7040bbbf | -7.29659 | -59.62655 | 2025-08-24 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c81ae277-0319-3763-877c-71a03ef26def | -8.90667 | -62.44994 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 160b0a7c-9a34-37e3-83bd-337a03000747 | -6.87841 | -59.81757 | 2025-08-24 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ae41cb6-b13a-3b8f-9365-b890963466d2 | -9.15569 | -59.50813 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ce569341-e8aa-3bc0-a5f9-7ea567515060 | -8.83985 | -49.90805 | 2025-08-24 04:59:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13694357-0f26-3fa6-aa7d-9d62b9f9acf7 | -9.14946 | -59.49643 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0b0873b0-24d8-39fc-bb81-43154881645e | -9.14758 | -59.45905 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b14c95a2-f31d-382e-8353-348ef09e736a | -7.91584 | -45.90459 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d38e8a11-414c-3786-b0fb-df48bcdc0d05 | -9.15966 | -59.50881 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 03cec005-470c-3e08-a6cc-49774d128c3f | -9.24927 | -60.92689 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca95f7de-d31f-3207-890c-0bf11486f38e | -10.63423 | -51.61775 | 2025-08-24 04:59:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e99189e-254a-317b-8bd3-4ce326ec45fc | -9.16278 | -59.51466 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c2a37b5f-86bc-3343-b475-585ad1e5a981 | -8.7513 | -46.75524 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d706537f-2dfe-310d-bc20-a330d1643841 | -7.92447 | -45.91807 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e66b0f22-2bf1-36b2-b83f-36c70f81d3f0 | -9.15516 | -59.48686 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 80c263b8-c5fa-3aed-b52d-a99438a6c850 | -8.90376 | -62.43828 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 99ce0b0b-715b-349a-8c90-e9ba30a5f255 | -9.53069 | -58.87581 | 2025-08-24 04:59:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7a01bae-efe7-33ac-a74f-3686c6f5a5d1 | -9.1825 | -59.4569 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05ba79dd-2477-3353-a8e5-affaea4dea43 | -7.91895 | -45.92026 | 2025-08-24 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9be736d9-5d09-3af1-8d1f-8323e35267c4 | -9.16487 | -59.46439 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cd98e391-b34a-3e57-8df9-b6b6fec22d6a | -9.19878 | -59.48088 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4440e07d-c5f7-310a-b4f3-9e00c98544fc | -6.55725 | -60.059 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e0f66de-7d65-369b-b5fb-ceac689a9401 | -8.70324 | -51.14362 | 2025-08-24 04:59:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b81cd7eb-05e8-3693-af63-f72e24d51e84 | -7.55018 | -63.84605 | 2025-08-24 04:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f515473-b5d3-35bf-962c-ef2e2016e815 | -9.19999 | -60.79492 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 93caf8a1-f5ff-3c9e-b2a4-6bbe9c323ec6 | -9.23175 | -60.92127 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef8d4991-f6e7-3c67-a281-c2ff5be26545 | -9.15948 | -59.46109 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 91adf5e9-209a-35ac-ad2a-9ae72a4df7df | -8.61341 | -62.59467 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 313c6c0f-f29c-31c9-ae92-81eb499c9706 | -9.15689 | -59.47648 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6222eed3-8509-36ab-9df5-1a1200fff9f2 | -11.10544 | -44.77966 | 2025-08-24 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c09fb40b-9d0a-3d36-96e8-8905ea613215 | -6.87421 | -59.81681 | 2025-08-24 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e990ed8-f71c-3835-85fe-2452e15820e2 | -6.31365 | -59.88353 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c1b7ee2-7152-3b8a-9494-f291c9069692 | -9.16794 | -59.48373 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0b8c3b99-82dd-3093-bcbd-c31adb31e789 | -9.16053 | -59.50365 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f4e0990-d4eb-3fd6-9e0d-07c687608629 | -5.79796 | -59.22486 | 2025-08-24 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86053d6c-1f2d-3744-a362-f53df8b3f149 | -10.40429 | -47.19075 | 2025-08-24 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f7e6165-9d3b-3ec3-9a24-5c624504a37f | -9.15425 | -59.47839 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dca89989-b4b3-390a-aa03-155a262ff2b9 | -9.24999 | -60.48348 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77b2c7d1-7066-3ad9-99d6-b901d8bfd120 | -9.16966 | -59.47342 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 80be5d47-9ad4-3419-8e60-b40f824711bd | -9.19783 | -60.78183 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9eed29cf-c167-3994-be03-7a8a2ded5b9a | -8.21744 | -45.11671 | 2025-08-24 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9d273a5-7388-3dac-8253-1cfd70cacd4e | -9.16033 | -59.45598 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0ed94ebc-02ee-38ed-9d99-0db8f0805d15 | -10.81048 | -46.41652 | 2025-08-24 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4bb7537a-47e6-3f7d-a7ee-f697049a89e5 | -8.60849 | -62.59375 | 2025-08-24 04:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 9e0eb0e1-b4d2-3895-9b78-89a570d199af | -8.90182 | -62.44904 | 2025-08-24 04:59:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e34fb81a-2013-347d-98be-40c8e21fb0ab | -9.19026 | -59.62614 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 683cc94f-9c9d-381b-be15-f713eff3175a | -5.80619 | -59.22622 | 2025-08-24 04:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93c293f6-b1c5-3414-bd1e-502bb206dd30 | -9.10202 | -61.43157 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 58a96800-ebb3-32fc-990c-c742d571e1e0 | -9.16176 | -60.80946 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f88aafcd-4aeb-3d0c-9f73-78c84d9c385c | -9.14257 | -60.78635 | 2025-08-24 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eaf3ae9e-450a-3fd3-a85c-b55d459e6242 | -6.87356 | -59.82062 | 2025-08-24 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89e11157-8ec7-316e-bace-cd7d1bebc180 | -6.43697 | -53.37855 | 2025-08-24 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45ea7571-39d6-323e-821d-3dfa64e319ca | -5.74184 | -57.60442 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ecea02c0-8367-39a0-ad3e-064a79c2ce4f | -7.25716 | -43.67118 | 2025-08-24 04:59:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1245bafa-7827-3604-ad53-0204eb0a6cc2 | -5.74247 | -57.57724 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8a71bfa5-3203-3d68-a6f7-67c757afc6df | -7.61171 | -45.24116 | 2025-08-24 04:59:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4219f8a9-3141-3b4b-8972-1292946c7070 | -6.61403 | -48.04392 | 2025-08-24 04:59:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57836ecd-a6d7-30aa-9ff0-b10ca2235589 | -5.64516 | -51.84682 | 2025-08-24 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77e8316d-4e0d-3d6e-beae-72d51efafb2e | -6.72163 | -43.19538 | 2025-08-24 04:59:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 38ca0ef7-6ae3-3933-8e5d-93a35fc226c6 | -5.66146 | -45.15521 | 2025-08-24 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a70a6866-5791-3e5a-a274-5790124f91ca | -5.44779 | -60.18873 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a371f20d-580e-376f-b5ce-a835da1e411d | -5.50398 | -45.3219 | 2025-08-24 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4c862d03-e06f-3de8-bf9e-46e1d74c6789 | -5.66253 | -45.15067 | 2025-08-24 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d3aedf0-2629-3b0f-a9f0-887b32cdb986 | -6.43642 | -53.38205 | 2025-08-24 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dffe0f58-6317-3e62-abbe-238e416fdf59 | -7.6219 | -45.24631 | 2025-08-24 04:59:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a129499-13fe-376e-8265-2f433054a4ac | -7.26023 | -43.66769 | 2025-08-24 04:59:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c18b4ba-98a6-3804-9c4d-3471095e5355 | -4.95573 | -55.82304 | 2025-08-24 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9310d2b6-6bd1-31e8-96f7-25862a9a769b | -5.49876 | -45.32159 | 2025-08-24 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ec5cdceb-66e5-3458-a1d1-85d0f0b9bb6e | -4.95755 | -55.81171 | 2025-08-24 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05cbe886-a34b-3f8f-8da3-bb65250d099e | -7.18069 | -44.6645 | 2025-08-24 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f49f315-9a09-3103-87f9-2360d0e41525 | -6.19235 | -45.4377 | 2025-08-24 04:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5b07873f-893b-3b17-9637-0c05d29a7c2a | -5.7433 | -57.59552 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e0e42a0-212a-3ea6-a947-e99be1cf9e6f | -5.67995 | -52.21289 | 2025-08-24 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c8a115c-1fbf-311c-ab47-6c42a6e19096 | -6.88442 | -45.68507 | 2025-08-24 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fdc1cb94-fca3-3ca1-b9df-b050f92061da | -7.02026 | -44.65122 | 2025-08-24 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2568d7dd-213f-389c-bf82-d29ff4512649 | -5.8742 | -57.76433 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e743d2f-b617-330c-9cf2-ce944c0551b9 | -5.01068 | -56.04243 | 2025-08-24 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a56366d9-3d79-356b-8566-02b6e2c7e20b | -4.93846 | -55.82021 | 2025-08-24 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 021eaeb6-8e69-3572-ac4e-4328bb7a2926 | -6.95607 | -44.42079 | 2025-08-24 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1aedcf9f-0fca-353f-917d-ddbc86dc5d82 | -5.4522 | -60.18949 | 2025-08-24 04:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e63a7f07-fe05-3784-8ce4-3d4d0cfa2298 | -6.89203 | -45.6679 | 2025-08-24 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fffef36c-d208-3cbf-a077-282745d6f9d8 | -5.75292 | -57.58346 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 82ce3572-f3ab-3ad5-b4b8-65fc30b72bfa | -6.58982 | -44.56328 | 2025-08-24 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 590e43ac-b9cb-344e-95e9-f82a4780923a | -4.96955 | -55.8253 | 2025-08-24 04:59:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 23b91c71-d5a6-33d7-a8c4-0b96c2b6e6b4 | -6.19624 | -42.98706 | 2025-08-24 04:59:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62a6f4a6-bd7a-3920-9d61-6b8015b1b675 | -5.87863 | -57.75799 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57059cbc-a07d-32f2-bdb4-17b933dc92fd | -6.11911 | -53.78509 | 2025-08-24 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b7e0ffdd-747a-3d09-b92e-9ca311fc558a | -6.19277 | -45.43467 | 2025-08-24 04:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d9d3764-e6e3-39e4-b647-358e0a6143f1 | -6.42587 | -53.38399 | 2025-08-24 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 33fe7139-1fca-3931-a0cc-9ebb16ca8b8b | -5.58844 | -51.32035 | 2025-08-24 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b086e368-62f4-3599-939a-ac2b91185c40 | -5.74402 | -57.5911 | 2025-08-24 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc0b6e2b-c241-380a-9e7a-8ba69b2b2be8 | -6.90027 | -45.68393 | 2025-08-24 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29ec31ac-4ec6-3b26-a60e-8a88d49e0c24 | -7.08016 | -44.62476 | 2025-08-24 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README60.md)
