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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa217d1c-f469-3f5e-b010-4befa3852ced | -17.30915 | -46.74999 | 2025-09-10 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 212ca5dd-1683-3a41-b31a-b68c264de6f0 | -22.54307 | -43.55521 | 2025-09-10 04:17:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9d80ef74-dc52-39d3-a7d9-32061e38b57e | -17.74689 | -44.47635 | 2025-09-10 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27bafdb1-b43d-30d5-8553-b6722dae951e | -15.95434 | -48.10728 | 2025-09-10 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c06fdccb-2b53-3f8d-8a1e-a5f159bbb5d9 | -17.23987 | -46.07592 | 2025-09-10 04:17:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b5c8484-9c01-31c1-ac0d-7248b4701beb | -14.39495 | -48.57236 | 2025-09-10 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 251ef55f-36f9-38d2-98db-9d81f2ea8848 | -14.65646 | -44.04973 | 2025-09-10 04:17:00 | NOAA-21 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 669826f7-9282-38a5-ba2b-efe1e9e46a87 | -11.45041 | -43.61586 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 45715444-5f8e-3299-846f-47051eead281 | -21.30874 | -43.88406 | 2025-09-10 04:17:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 004dd373-26d4-3402-ba2c-d14e2585de32 | -21.31109 | -43.89317 | 2025-09-10 04:17:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 6d892694-d9e5-3ff4-8b1d-ca7960629d57 | -11.76668 | -50.58055 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e407a784-5239-36b5-bb59-d6903e1f3c61 | -12.20297 | -53.86514 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 13fb6d9f-3738-35df-8500-7dd8e98eeab7 | -13.94783 | -48.25882 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1d36baa3-43c7-3ca2-9faf-17afa39b694c | -21.40071 | -43.87167 | 2025-09-10 04:17:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 83c918ea-b02e-3fe1-b4f9-3dcc9c5ab214 | -12.00672 | -50.98819 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc4bf85b-6e82-3584-a0d5-a41f4c10ed6b | -16.39628 | -46.87578 | 2025-09-10 04:17:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3a3b0592-7c37-3969-ae56-32b1190e1da4 | -13.32676 | -44.4555 | 2025-09-10 04:17:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5212ebf7-5489-39f7-9f71-482ac6c4543f | -11.49245 | -50.41037 | 2025-09-10 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51e96042-0538-37df-9f92-40d163947272 | -20.51893 | -47.63947 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b420dbbf-6127-3854-a963-d38694fb005d | -16.57635 | -49.73695 | 2025-09-10 04:17:00 | NOAA-21 | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dc616b96-4aa2-3b48-ab97-e1e2e38647e5 | -11.46538 | -43.62909 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2117a092-c6de-36b0-90e5-923020d1b134 | -11.44533 | -43.60445 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04c5f9f5-6210-3530-a036-382bc27b7176 | -11.21111 | -54.99413 | 2025-09-10 04:17:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd805f6e-7bc4-3703-ba2a-f155eb65a013 | -11.42814 | -43.58358 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed79fe70-0acc-3000-8b58-647e2359c452 | -16.11401 | -48.34153 | 2025-09-10 04:17:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb3611bc-f302-37ca-97ff-5cb8488f095c | -15.47941 | -49.36965 | 2025-09-10 04:17:00 | NOAA-21 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8bad7a5-16d3-332f-b08f-0190f5ae1cb6 | -11.43486 | -43.62814 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1dbd8797-e831-3771-9efc-2f190e7db19e | -15.93864 | -50.22689 | 2025-09-10 04:17:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c97fb3c2-d478-3407-9bd8-33f6e13321c4 | -20.53254 | -47.66125 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e33a6a5-aef3-3ae6-ae4f-4439ebc0d687 | -15.86104 | -51.82721 | 2025-09-10 04:17:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4323e646-b4cc-3c47-b3b6-816e5686cb7d | -11.68085 | -46.90344 | 2025-09-10 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 92d61025-5c12-3ec8-ab66-bcdcbe3fdeaa | -13.04419 | -47.16082 | 2025-09-10 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1fcb9ab-663a-37d2-8478-723132de0f26 | -16.48792 | -51.97423 | 2025-09-10 04:17:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b0a1cb6-f9b3-32b1-ace1-679f1d03e8ea | -12.1924 | -53.86311 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 864ae8c3-fd4a-366e-a7d1-94465b2b148f | -11.94084 | -51.07537 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 07745179-d981-3581-9071-4932bb69cd28 | -15.94553 | -50.23348 | 2025-09-10 04:17:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9d2725b-aa0d-3834-bc22-fc95ee284862 | -10.29889 | -48.824 | 2025-09-10 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a2e90e5-2404-391b-aab3-56b6bb0c0d75 | -15.08431 | -50.07797 | 2025-09-10 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 88e942ba-abbc-3049-9b9b-5fd09b29af61 | -20.70401 | -46.0621 | 2025-09-10 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0e047a0f-43d0-3190-8c8c-c08279739879 | -11.57413 | -44.65715 | 2025-09-10 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ccbb2f18-1801-3bfb-aff6-efbf755dff37 | -11.29352 | -53.96449 | 2025-09-10 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52d763b0-d169-398c-83cb-b9d177af385f | -12.84595 | -52.94464 | 2025-09-10 04:17:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b3041019-c02a-3338-8227-59bef8f439cb | -12.6793 | -44.96405 | 2025-09-10 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0355fc74-f60c-3705-bd2b-3d6c36e639a5 | -13.97978 | -46.66233 | 2025-09-10 04:17:00 | NOAA-21 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87df1ed6-f921-3a9d-99aa-4d0a0f15e421 | -13.76033 | -43.61839 | 2025-09-10 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b42f17d-e748-3b34-8cab-07ffb1d17953 | -12.06083 | -51.06432 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da7dd303-4812-347e-ba2d-6bf99ab24591 | -11.1101 | -48.45312 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec103ebc-b0bb-3b46-be70-8b244dac26b4 | -13.90264 | -47.98198 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1053f02-7c02-3a1d-8f5c-4a43ede14f96 | -17.307 | -46.7421 | 2025-09-10 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7cdc9a7-d016-338a-aed2-9d8fd9e02259 | -15.72731 | -48.93729 | 2025-09-10 04:17:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acd21145-bb1d-3e38-a461-05560e3ab25f | -14.07068 | -43.72291 | 2025-09-10 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd1c5f1a-8888-34d3-ab19-fc7eb1c25233 | -15.80387 | -52.2496 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2de56b19-1c6b-3b0d-83db-00b1edb55397 | -21.1208 | -47.73277 | 2025-09-10 04:17:00 | NOAA-21 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 07477455-0f7d-31f5-90f6-62e5d8a252c8 | -11.99954 | -50.9779 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ba593fb1-fac9-3368-9df4-a25396b00b4a | -17.24203 | -46.08374 | 2025-09-10 04:17:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 065aead8-d4c2-3483-8e06-0be85f9d5f3e | -17.31033 | -46.74268 | 2025-09-10 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6736c01f-67ca-33d7-9676-f649ed889edd | -11.94003 | -51.07976 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38916bd3-5d90-3b3e-86de-dbc2097ac748 | -18.05736 | -44.33632 | 2025-09-10 04:17:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e53bf37d-5b92-374c-b324-ae9be0e68848 | -11.10928 | -48.45787 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03d6b7db-2b1d-3d5e-99f5-919fe49a97c1 | -17.31484 | -46.73595 | 2025-09-10 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c5817f34-a517-3b8c-b93e-1fc68d7e7367 | -11.57358 | -44.66066 | 2025-09-10 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c049355e-b9e0-3c68-93e2-fbcb8a6e2f0b | -15.1221 | -47.02946 | 2025-09-10 04:17:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae5940e3-b971-3d2e-98ec-346cc465b0e3 | -12.92899 | -54.79097 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0f5a329d-a125-30c3-abb9-d0a3c812c17f | -15.22926 | -48.24267 | 2025-09-10 04:17:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60aa3645-c453-3df5-a3d6-b3c7b26ccdd3 | -16.48353 | -51.97379 | 2025-09-10 04:17:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48f0df20-43bb-3fcb-953a-419ad40169be | -11.12013 | -48.44016 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19edcb76-c567-3dff-967e-5f98a3d1e09f | -23.35494 | -47.21104 | 2025-09-10 04:17:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 55cfb8e6-51a5-3cb7-b01b-300ac11d662b | -15.95387 | -48.10397 | 2025-09-10 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a91a33ca-760f-382a-a5c5-0156b6677bf7 | -14.93052 | -50.10445 | 2025-09-10 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d1e0e86a-ce05-3502-8e62-afb9901e71e4 | -19.94952 | -49.26436 | 2025-09-10 04:17:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5668ce50-06f5-3600-8bd6-1cec83d02c05 | -16.74116 | -43.78665 | 2025-09-10 04:17:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91ebf221-8a22-38b5-9af6-d8bacd5d454d | -11.85337 | -46.76795 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 342ecfd6-e68b-3dd1-8e8e-6e108d3e0a33 | -11.66914 | -46.90952 | 2025-09-10 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9cde6e95-1ec2-31f7-9792-c6c34b1f9bfb | -15.64603 | -41.82968 | 2025-09-10 04:17:00 | NOAA-21 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0df0f92a-489a-36f5-ad0d-6a8aa37ce1de | -23.35669 | -47.19981 | 2025-09-10 04:17:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4d22b6ac-4fdd-3406-87f1-fd3f16911ba1 | -13.82529 | -43.86314 | 2025-09-10 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 126ce7a9-acad-354c-a7bd-26dec5fe0b94 | -14.3886 | -47.31993 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2049a524-ba29-32a4-8e19-c17493bd0d93 | -11.66633 | -46.90485 | 2025-09-10 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 528c9ac7-a1ee-3391-99e9-e2063ab56b47 | -15.95914 | -50.22517 | 2025-09-10 04:17:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1f5de8f8-3eb4-328b-891c-3a5d5f355ab7 | -13.19147 | -45.27583 | 2025-09-10 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2649a9a2-25bb-321a-b166-41fcfe088c84 | -21.39956 | -43.88012 | 2025-09-10 04:17:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 49388b4b-eab0-37d2-8322-69179c85aa8d | -15.14216 | -44.02994 | 2025-09-10 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1832022-4b4c-3f24-8cd8-bba5048c68b4 | -11.4643 | -43.63616 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 68a70fe8-816d-3d7b-b2de-2f235622e7a8 | -10.01325 | -51.68172 | 2025-09-10 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d4e0461f-a653-3443-8c50-d2c0e64b13e6 | -13.17589 | -47.25036 | 2025-09-10 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0ab84bd-1e2a-382a-b321-438f4f867b3d | -20.3765 | -46.63882 | 2025-09-10 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46d7d844-0930-36d7-8f5e-6132ade478f2 | -13.15228 | -45.28756 | 2025-09-10 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e96d43ea-4409-3be6-80f3-93dac0620829 | -17.57395 | -44.54772 | 2025-09-10 04:17:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 62e0fb48-442f-3b54-a90f-b42d00be1184 | -23.55931 | -49.92099 | 2025-09-10 04:17:00 | NOAA-21 | QUATIGUÁ | PARANÁ | Brasil | 4120705 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 27c78579-4518-34cd-9364-1fd60aa01067 | -10.03016 | -47.84872 | 2025-09-10 04:17:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9caefcad-1280-3990-978c-b7fe7fb27a84 | -16.59739 | -40.64794 | 2025-09-10 04:17:00 | NOAA-21 | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0b8e3841-a50e-3ff8-bf03-ba2fa468ca32 | -11.44478 | -43.60799 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cc42fdc-b68f-3bd4-8415-00ee75b3afb1 | -14.58011 | -51.40533 | 2025-09-10 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4677fe61-73af-3b52-927b-aad41f646a95 | -15.91325 | -50.18763 | 2025-09-10 04:17:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6fa705f9-a58d-38c4-b3fa-add8fed8489b | -13.19752 | -45.28046 | 2025-09-10 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 66908553-0d02-3c47-b374-e1929428dff9 | -10.65137 | -48.60735 | 2025-09-10 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bacdb36a-8647-3fe3-a531-b4bac56de0e0 | -12.93629 | -54.81229 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1e7d08f-61cc-33b1-8870-ba25caa8d285 | -10.02244 | -48.09949 | 2025-09-10 04:17:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72c175a4-af70-30d0-8da8-4960057cd6a9 | -12.42313 | -47.81237 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bae71d2c-6ac0-3b31-bb1a-00d713a2bbb7 | -12.18712 | -53.86209 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README39.md)
