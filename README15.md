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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40ffa47b-b5d1-3ebb-9d15-92c6162baedd | -12.01452 | -49.53086 | 2025-05-31 04:53:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c654af1a-f175-3080-aa23-54e9e3527fc0 | -8.31801 | -47.91985 | 2025-05-31 04:53:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03e9a6db-e959-3b12-9df3-b499b25210ba | -11.90938 | -54.82831 | 2025-05-31 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 807ac183-e6b5-3862-afc3-8235f682b65e | -10.69068 | -57.64723 | 2025-05-31 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38f0e457-8052-358b-bbce-e3e0f5746f31 | -11.89792 | -47.43913 | 2025-05-31 04:53:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e6a5293e-3af0-3685-8b62-9c1aac36038e | -12.46434 | -54.91647 | 2025-05-31 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4bc97513-2b94-3f7c-82ac-f275427da163 | -13.10501 | -52.28544 | 2025-05-31 04:53:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd27aaae-b4b7-3de6-94b6-c357023095c0 | -10.30154 | -57.14072 | 2025-05-31 04:53:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cea440ec-4064-35b4-a2dd-19718a385319 | -10.3302 | -57.49072 | 2025-05-31 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 453770bc-0b37-3160-b613-8d99daddb4de | -10.63834 | -49.43518 | 2025-05-31 04:53:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2a05ebff-e607-3fad-951d-00891c67354e | -9.60877 | -49.02572 | 2025-05-31 04:53:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f801f39-4af8-3b52-ac07-9650173f166d | -13.09781 | -45.28724 | 2025-05-31 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb6c6c5c-0cf5-3efb-8c3f-bb551c446b61 | -8.47906 | -49.60839 | 2025-05-31 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea24dfda-38b0-38f3-9375-ca393302aeb8 | -11.63993 | -55.36933 | 2025-05-31 04:53:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7335d0c-b580-3043-91b3-25ac55cf6d03 | -11.87944 | -55.53011 | 2025-05-31 04:53:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7978b2a6-53b4-33f9-9e68-7b02b450ab05 | -11.83963 | -51.27021 | 2025-05-31 04:53:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 95b963ca-6257-3ea3-96bc-56a16faa0860 | -10.73454 | -49.28662 | 2025-05-31 04:53:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c249c7a3-bc31-32d8-8266-c2b9ae6ed3ef | -11.44978 | -49.09842 | 2025-05-31 04:53:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87249716-845a-3a48-9526-517d2f4e349a | -10.50627 | -53.66013 | 2025-05-31 04:53:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85c41135-25d1-3738-a870-2688dc85e9bb | -10.64985 | -49.437 | 2025-05-31 04:53:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9794213d-a0b9-3ccf-85c8-ba0bbb38b91b | -12.45371 | -54.91838 | 2025-05-31 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea0075f6-7d49-3b85-ae5d-fc2b1368ed7c | -10.82115 | -56.94309 | 2025-05-31 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d5e9b942-7f33-3c24-81d0-8cf97770b267 | -9.30103 | -49.67436 | 2025-05-31 04:53:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c68a000-42ce-3288-a78a-7d0de048eedd | -12.10395 | -54.66604 | 2025-05-31 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cc2d074-72ef-3617-bf8d-a11834d25e62 | -13.10386 | -52.29305 | 2025-05-31 04:53:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad1b868f-4fee-33bd-91fd-43aa6c4eb164 | -8.81332 | -49.83892 | 2025-05-31 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 969a9f97-5379-33a0-bfe4-03a7d519bd9c | -11.91139 | -54.41939 | 2025-05-31 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23ec0d70-0899-3d44-8253-f8a53264c1ed | -13.09338 | -45.2801 | 2025-05-31 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34f72e80-620d-3132-9f1f-bdd0c23d0d5d | -13.09822 | -45.28399 | 2025-05-31 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c3a1ad6-541c-39d7-85e8-addf5efcee6b | -12.01998 | -49.51987 | 2025-05-31 04:53:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| b602179c-84bf-3088-83ed-488dae0d2602 | -10.73913 | -49.28231 | 2025-05-31 04:53:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c73a4eb8-f561-3900-aeea-7b2597333fb1 | -7.31146 | -55.30975 | 2025-05-31 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 62fc5863-9c74-359d-8f33-6dda8272d37d | -11.14316 | -53.92517 | 2025-05-31 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ece70289-b4f0-361f-8fcf-a38531c81e2b | -9.31196 | -49.4896 | 2025-05-31 04:53:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d98a3a94-2b56-3a32-81aa-a586b9ca2347 | -12.01063 | -49.53029 | 2025-05-31 04:53:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2380ae59-9ece-33fc-9abd-53bc06f0973e | -11.90176 | -54.79023 | 2025-05-31 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e70a372c-f34c-3846-ac62-6e108f1c3d0c | -10.65122 | -49.42736 | 2025-05-31 04:53:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| fb613cc0-65b0-3cbf-885f-9c19da071876 | -10.55847 | -59.21112 | 2025-05-31 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa585890-7f6b-33a9-9638-d959eadb145a | -12.02827 | -49.51764 | 2025-05-31 04:53:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5315dcdd-7bbe-3b6a-858d-01c54c7e6206 | -10.46278 | -47.94552 | 2025-05-31 04:53:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7d63a838-2cae-3a34-899b-abd1b0286364 | -10.61173 | -44.76935 | 2025-05-31 04:53:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c5d89b0-637f-3724-9906-934825f11623 | -11.02752 | -54.83905 | 2025-05-31 04:53:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bcb7dc10-e2e2-38e2-a0f6-d864786707a3 | -12.02387 | -49.52042 | 2025-05-31 04:53:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| dd7d34fc-84b1-3296-a2a8-4340ea1c4987 | -8.31854 | -47.91619 | 2025-05-31 04:53:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc36f850-0a6c-3619-b439-85ee1907c04d | -11.83669 | -51.26563 | 2025-05-31 04:53:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 692d123c-a389-3377-bb9f-a15827ffc969 | -8.47971 | -49.60403 | 2025-05-31 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 305829bb-82a1-389d-906f-6eeeaf1d8eae | -12.02315 | -49.52541 | 2025-05-31 04:53:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a5cd2f61-1f60-3b29-b8eb-2f4ab2ddaf5a | -13.09816 | -52.04873 | 2025-05-31 04:53:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9bdb723f-c9c1-326e-ab16-a73cccb748f0 | -12.12734 | -54.6699 | 2025-05-31 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 596a49bc-ecf4-31fd-a5ab-70bdf47b4327 | -11.90178 | -47.44423 | 2025-05-31 04:53:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92b25d04-fc2b-331f-bba9-24db53ebfaed | -11.6336 | -58.01514 | 2025-05-31 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d692c7c-db18-3468-a13b-67ea0ad4da48 | -6.63581 | -55.00908 | 2025-05-31 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74bbc22b-faa2-322f-872a-dee56e4b731f | -11.14426 | -53.9398 | 2025-05-31 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c911151-9a05-3ecf-9ff9-6c1dcb286328 | -7.8797 | -45.99005 | 2025-05-31 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bb3d48e0-167e-36a9-a823-000d2623d788 | -11.83256 | -51.26911 | 2025-05-31 04:53:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 941c2b1b-ffb7-3d4e-bc67-faa8744632e6 | -13.10264 | -45.29114 | 2025-05-31 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3d48a95f-97df-3fd7-a9e8-5daad035a2d3 | -11.82842 | -51.27257 | 2025-05-31 04:53:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| fea27c58-4762-39f3-926f-525261b2d919 | -7.87477 | -46.48542 | 2025-05-31 04:53:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2280c83-47e9-3f8b-908e-58f5d1570187 | -8.81203 | -49.84754 | 2025-05-31 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7b85052-eb52-30cb-83ea-f47859a9b858 | -8.67878 | -48.28752 | 2025-05-31 04:53:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 688beba4-69a1-39bf-a730-ce31e00dea5f | -11.91528 | -54.4164 | 2025-05-31 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ccd23e7-60f0-3d29-8c30-bfffaee7d0cf | -13.12686 | -53.52954 | 2025-05-31 04:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd97c34f-c9cc-32f5-801e-3e0c3c327fc0 | -13.78439 | -54.31076 | 2025-05-31 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf327086-2b0a-39a6-b9d7-279880f40907 | -15.37079 | -45.67868 | 2025-05-31 04:55:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6bf4af0-77f1-3623-bd41-3a1b199f10ae | -13.63937 | -52.17998 | 2025-05-31 04:55:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0db5ad5-3031-3a3f-9752-23b9ceea3e23 | -13.12352 | -53.52901 | 2025-05-31 04:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c29bcb5-c774-39d6-b7c7-72b908e8be0b | -17.2615 | -50.87473 | 2025-05-31 04:55:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2a37b8d-51ec-37b7-9af6-680a8017188b | -21.10089 | -48.50291 | 2025-05-31 04:55:00 | NPP-375D | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1a5bad69-12ba-35ea-8620-025a712722b1 | -19.17855 | -53.9566 | 2025-05-31 04:55:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2c81637b-7184-374f-893b-391bca32ae73 | -19.02292 | -57.62244 | 2025-05-31 04:55:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 01d141a9-2b9d-3448-8c03-d57d5e071478 | -13.04568 | -53.72132 | 2025-05-31 04:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9dee9723-20dc-3773-b342-7ac3f2ed1005 | -14.58745 | -58.76079 | 2025-05-31 04:55:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb090e3c-358c-3fc4-ab73-ccd4d3d84a12 | -15.8898 | -43.45206 | 2025-05-31 04:55:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 285c6816-32d9-30c0-bb62-4df7db6051d3 | -13.63879 | -52.18385 | 2025-05-31 04:55:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| caa8a742-2c79-3bd1-a816-8fb64bbe3791 | -17.11248 | -49.14163 | 2025-05-31 04:55:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c03cb4c8-a6e9-323f-8063-1d63101b6ca1 | -19.19198 | -52.08888 | 2025-05-31 04:55:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6c05810-e46a-3bfb-9953-36ff812c0ba9 | -20.5463 | -54.11814 | 2025-05-31 04:55:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5e12534-6332-3e58-ab35-0bff6bfee900 | -14.61888 | -47.96581 | 2025-05-31 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df3d5f09-1290-3e12-868c-fcf47a6f5611 | -16.34344 | -56.83572 | 2025-05-31 04:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 465ac831-babc-3000-a0e3-fb96e76d9c48 | -20.47815 | -53.67546 | 2025-05-31 04:55:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11a3072c-9726-3aac-9852-d045b3016f0b | -20.60983 | -48.86755 | 2025-05-31 04:55:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e06d1674-505a-3254-a0c0-a8499997fff0 | -14.01671 | -55.12564 | 2025-05-31 04:55:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 629fdc11-78f5-344d-8742-f396dbbd7b03 | -19.59513 | -53.84412 | 2025-05-31 04:55:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 515e3373-0b96-3800-af68-d6955cfa158e | -14.02616 | -55.13091 | 2025-05-31 04:55:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 33a06c70-49fd-31fe-adca-a20476c24266 | -15.37118 | -45.67536 | 2025-05-31 04:55:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6cea7171-9798-30a9-9446-f639b9ded53f | -13.93916 | -54.49003 | 2025-05-31 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 120672a2-55c1-396d-b8aa-62e510ee3753 | -19.19935 | -52.09003 | 2025-05-31 04:55:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1e5c2cd-3e95-3b61-b636-913b05cba1f9 | -13.95028 | -54.48457 | 2025-05-31 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07212997-f77c-33e7-a1c0-3e7eed924ef4 | -20.54973 | -54.11871 | 2025-05-31 04:55:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4377f0c-c0c8-3375-84ce-95c5e0170d45 | -18.83849 | -53.59857 | 2025-05-31 04:55:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28947fa9-1a6d-3d91-a770-f280ed9de5a6 | -19.19627 | -52.08495 | 2025-05-31 04:55:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e03b2cf4-822b-353d-b5e2-6e090685170f | -13.95638 | -54.48923 | 2025-05-31 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c793169b-86ea-3a44-8cdd-14d5ca74bd2b | -14.0295 | -55.13148 | 2025-05-31 04:55:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f8a7aa76-9aff-36b9-9cc4-b116b1e1d6fc | -14.44389 | -50.64787 | 2025-05-31 04:55:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 388fab91-050c-3d4d-a021-901981638c52 | -13.95305 | -54.48868 | 2025-05-31 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e0b1951-9e89-3ac5-be12-d997e57ad3a3 | -14.03169 | -55.13922 | 2025-05-31 04:55:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 785b4171-25c2-3589-b3be-f242ca7ed2c5 | -14.03226 | -55.13563 | 2025-05-31 04:55:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2602a31f-987c-3941-a69f-4e218e4a8641 | -16.12356 | -46.82481 | 2025-05-31 04:55:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ee606572-cac3-3d81-a2bc-9560e6b61be8 | -15.88932 | -43.45675 | 2025-05-31 04:55:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3d8ae9ec-43f7-392b-8ec2-11d155589dbf | -17.02709 | -52.54165 | 2025-05-31 04:55:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README16.md)
