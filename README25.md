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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e04ff332-7c6e-3435-9991-c16253208bd5 | -3.36291 | -41.66084 | 2024-11-01 04:29:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 170d016d-b399-369a-9b70-0e179f15e2de | -2.26429 | -50.68883 | 2024-11-01 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae55fefc-9a46-3ae0-b5c1-b6f6801551fd | -6.52351 | -35.2497 | 2024-11-01 04:29:00 | NOAA-20 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 23.4 |
| f486b5ec-1022-3fe7-aa43-17d61af247d8 | -6.52269 | -35.25569 | 2024-11-01 04:29:00 | NOAA-20 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 87887cf8-72fd-3ecf-9678-f4ee6c89fb84 | -6.52012 | -35.24992 | 2024-11-01 04:29:00 | NOAA-20 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 38.1 |
| 7f751cd3-0111-3866-b8f7-2d49d329e6b8 | -6.51935 | -35.25587 | 2024-11-01 04:29:00 | NOAA-20 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 44.5 |
| d78d23f8-d66f-3ed2-8792-832b61af3fa1 | -6.51605 | -35.25448 | 2024-11-01 04:29:00 | NOAA-20 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 3d400723-8986-3a2b-81eb-425c40bac4c5 | -6.52436 | -35.24348 | 2024-11-01 04:29:00 | NOAA-20 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| 9b489222-296a-3f0f-bb97-3b319f3ed7bf | -6.52094 | -35.24366 | 2024-11-01 04:29:00 | NOAA-20 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Mata Atlântica | 38.1 |
| a38e230a-8fca-35de-94ee-05b32e62b81d | -6.51688 | -35.24843 | 2024-11-01 04:29:00 | NOAA-20 | MONTANHAS | RIO GRANDE DO NORTE | Brasil | 2407708 | 24 | 33 | nan | nan | nan | Mata Atlântica | 23.4 |
| d678bb77-e94e-3743-bfc3-ca87eb97de80 | -4.68663 | -37.80731 | 2024-11-01 04:29:00 | NOAA-20 | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2526fec2-8e49-3b59-b66b-f2ea3bb18967 | -4.68609 | -37.81096 | 2024-11-01 04:29:00 | NOAA-20 | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5b600c37-2cac-3c86-a499-89b1c35bf8c6 | -4.68549 | -37.8104 | 2024-11-01 04:29:00 | NOAA-20 | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0e047bec-ec5c-3345-a5b7-b3ed400f37e8 | -6.90609 | -38.46671 | 2024-11-01 04:29:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 109a5eab-6ee5-33d3-b71b-af009328a1ff | -6.90559 | -38.47029 | 2024-11-01 04:29:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9ec1d64f-8a4b-35da-8a04-1c0aac383092 | -4.10706 | -38.74419 | 2024-11-01 04:29:00 | NOAA-20 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c4e6f9b9-b9ad-3e3b-b54e-90fe96f57b70 | -4.10191 | -38.74345 | 2024-11-01 04:29:00 | NOAA-20 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1e2771ec-b8e0-3afb-9b29-4395e540c96e | -5.6722 | -39.86914 | 2024-11-01 04:29:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1937c930-8a61-3e9f-984a-e50393a1af16 | -5.66972 | -39.8685 | 2024-11-01 04:29:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8ac041ac-7e7e-350d-9605-0af803baaa14 | -2.88996 | -39.90617 | 2024-11-01 04:29:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e3bcaccb-18a2-3d2b-95d9-aade854f5e56 | -2.88529 | -39.90546 | 2024-11-01 04:29:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f00d9944-6af4-39de-b98b-61883e1c79eb | -3.03988 | -40.0691 | 2024-11-01 04:29:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3705d687-595c-3ee6-a3cb-6c18d46ae3f7 | -2.96211 | -40.24096 | 2024-11-01 04:29:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| aa6e8c8d-3ba8-3eeb-890c-8400d7c7dc87 | -3.50182 | -40.75428 | 2024-11-01 04:29:00 | NOAA-20 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7e1d7bf6-a412-3b77-b989-96e95afefcf6 | -3.50113 | -40.75874 | 2024-11-01 04:29:00 | NOAA-20 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 56d2bf2f-7d00-3740-8c7d-fdac88ff4dd8 | -3.50102 | -40.75285 | 2024-11-01 04:29:00 | NOAA-20 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ac1dfbe9-5cf1-3939-8364-2c9dd1668026 | -3.50037 | -40.75731 | 2024-11-01 04:29:00 | NOAA-20 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 50f22385-2f8a-3605-842f-0dd1c948f4bf | -3.85414 | -40.70582 | 2024-11-01 04:29:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2c0cd18a-9e91-3183-9c96-b2734d2b2c85 | -3.84966 | -40.7052 | 2024-11-01 04:29:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 096a3df7-ed3b-36e6-b0a6-47254bb6b2d0 | -3.84899 | -40.7097 | 2024-11-01 04:29:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 235cdb28-7d29-39a3-b1ac-19ba45121f78 | -4.54039 | -40.46723 | 2024-11-01 04:29:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2b39e720-0f3f-38f3-8dc5-ab94f722bb19 | -6.04175 | -41.80748 | 2024-11-01 04:29:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9e3b8570-549c-3c85-b9a0-a0c683218d8a | -5.5019 | -41.65918 | 2024-11-01 04:29:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d9f126fa-dd20-362e-938c-2d6433cc8b32 | -6.0423 | -41.80377 | 2024-11-01 04:29:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| db3a8b2b-8dc6-38ee-9800-bde71fc83be5 | -6.04003 | -41.80608 | 2024-11-01 04:29:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e17e6326-0da1-38dd-a9ef-14ee2c225716 | -6.1181 | -41.81261 | 2024-11-01 04:29:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 08485b8e-6713-3f3a-8fd4-462f2f860158 | -6.11749 | -41.81673 | 2024-11-01 04:29:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 294d8279-2cc4-3e1c-8880-61aeda9c3312 | -6.0395 | -41.80981 | 2024-11-01 04:29:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ab8d9cef-01c5-3f11-bfe9-98b1311c5fc0 | -3.39549 | -41.64254 | 2024-11-01 04:29:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 30b03abb-f28c-31f5-b380-609a52d97b45 | -3.39492 | -41.64634 | 2024-11-01 04:29:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f8b44c87-1b25-39ed-b995-a563b5ee9752 | -3.39246 | -41.63424 | 2024-11-01 04:29:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 57f3b26a-3b95-3caf-8154-477512967bf1 | -3.39189 | -41.63806 | 2024-11-01 04:29:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2d692e5a-e5fb-3f43-9276-3b605407f6e1 | -3.94556 | -41.51777 | 2024-11-01 04:29:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ce63629b-9e2b-3f96-9f8c-96eb0243069e | -3.94381 | -42.63576 | 2024-11-01 04:29:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 62be9c68-23ad-33d8-b11e-ca806d3a93d9 | -3.94248 | -41.50924 | 2024-11-01 04:29:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bfa398b7-be74-34ba-a689-c820161597de | -3.9419 | -41.5132 | 2024-11-01 04:29:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 92f148f0-cb2b-3e42-98c5-7ae3333a23a6 | -3.94131 | -41.51713 | 2024-11-01 04:29:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c1f24587-8aa1-367a-8dff-051f31d640b3 | -4.54993 | -43.10217 | 2024-11-01 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65d725bb-7c2f-3c3c-9ef8-8b9c78a87a0e | -4.54798 | -43.09912 | 2024-11-01 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fbbd508-59dc-3a9c-b923-b4a75bdc12d9 | -3.5563 | -42.70408 | 2024-11-01 04:29:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 89bbdeb3-432c-37c3-8a42-9352e9727d70 | -5.65372 | -41.88505 | 2024-11-01 04:29:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ac699771-3b0e-319a-bc58-df2fe1615b11 | -6.18251 | -43.07001 | 2024-11-01 04:29:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 64bea1f0-f56c-31a7-89c8-8c09c6fa8797 | -5.46529 | -43.17919 | 2024-11-01 04:29:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 185e815a-98dc-36f4-9a74-a9e6955a5c0e | -5.46214 | -43.17371 | 2024-11-01 04:29:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cccd704-1053-3b7a-a322-d5d306e93a26 | -5.4614 | -43.17863 | 2024-11-01 04:29:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18107727-47dd-320c-84f9-c9c7ba13233d | -6.31396 | -42.03627 | 2024-11-01 04:29:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9534f3f6-16e6-3c68-877f-ab273bc80ba9 | -6.31339 | -42.04008 | 2024-11-01 04:29:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5d624508-6c8b-367f-aee4-68d6e121cc7d | -6.18378 | -43.06801 | 2024-11-01 04:29:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ee40c54b-df42-33e2-a903-f9fd31c9b79b | -6.69805 | -43.05776 | 2024-11-01 04:29:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8edca729-80b8-3aa3-afd2-3aa9f039ec2d | -6.57986 | -43.58339 | 2024-11-01 04:29:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df0dcf9e-07f6-393e-8d3f-4123ad8e4dc6 | -6.50404 | -42.85324 | 2024-11-01 04:29:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 783cd768-116f-3386-8051-b18bc0d720d3 | -6.50352 | -42.85675 | 2024-11-01 04:29:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5118c1f-862a-3391-a0d7-4409aac79368 | -3.57002 | -43.22887 | 2024-11-01 04:29:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2381081e-a1e5-36c8-9a1c-68eef95b7aed | -3.46017 | -43.18681 | 2024-11-01 04:29:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7957ced-cc73-3085-9ea4-f7008951cae5 | -3.29218 | -43.54206 | 2024-11-01 04:29:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db359cea-f307-3fef-bf23-c6b844d7d4af | -3.29149 | -43.54644 | 2024-11-01 04:29:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91273fdf-3dc4-3051-b4a8-194a3f38eaf1 | -3.2905 | -43.54484 | 2024-11-01 04:29:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 32f07e0a-a6ea-36e3-8e94-9b636a3fa279 | -3.19186 | -44.31773 | 2024-11-01 04:29:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4ab9f891-e032-31b7-b52c-e2baf4ba002b | -3.18831 | -44.31719 | 2024-11-01 04:29:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 66e33820-313e-3635-aaae-fe18458fdd8c | -4.26259 | -43.43266 | 2024-11-01 04:29:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fa16e831-0602-3495-8fec-04cf1725d81c | -4.17862 | -43.78091 | 2024-11-01 04:29:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5026e0a7-b028-34e3-a001-7847023c69a2 | -4.17493 | -43.78037 | 2024-11-01 04:29:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a835d1a-b4d1-38c3-a501-a0017efe217a | -4.08413 | -43.95773 | 2024-11-01 04:29:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3892d6b-660b-3281-b2cb-b6c0664a39d1 | -4.08048 | -43.95715 | 2024-11-01 04:29:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bcd04597-0ee2-3720-a02b-1e57068ae032 | -4.06461 | -43.28532 | 2024-11-01 04:29:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c274ced1-a234-305c-a889-6f00a1916d58 | -3.87555 | -43.95137 | 2024-11-01 04:29:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5177b6a9-8db2-369b-ad1e-a7cd3a49ed35 | -3.8755 | -43.95448 | 2024-11-01 04:29:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55172f84-f120-3de2-8996-35ab3c985542 | -3.87186 | -43.95391 | 2024-11-01 04:29:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c09df4b3-e2be-3eae-ba05-73c448b78041 | -3.87124 | -43.9551 | 2024-11-01 04:29:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bf635bb4-8dd8-3846-98d7-39a1259e4863 | -3.76772 | -43.53229 | 2024-11-01 04:29:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 258a1bca-1244-3345-b382-0533f51962d5 | -3.76635 | -43.54128 | 2024-11-01 04:29:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0fffdff-0d9c-31dd-a1fd-48cef3586607 | -3.76566 | -43.54579 | 2024-11-01 04:29:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bfbf3777-0d8d-3b40-ab2b-609d0fce238c | -3.764 | -43.5317 | 2024-11-01 04:29:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 34c00804-6fae-3c7f-a343-d4383ac47315 | -3.76331 | -43.53619 | 2024-11-01 04:29:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6c87079e-3584-3dff-a179-e2b6e1fac53d | -3.76263 | -43.54068 | 2024-11-01 04:29:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0bda835b-ac4a-3806-b8fd-054dd50e839e | -3.76195 | -43.54518 | 2024-11-01 04:29:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df630889-fa87-3fc2-9852-8735873fde8f | -3.7605 | -43.35176 | 2024-11-01 04:29:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| be990135-cc36-337a-992d-2f3a0427d4bc | -4.93325 | -43.63023 | 2024-11-01 04:29:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc2c2301-da7b-3375-ae6d-16bb829205e3 | -4.43804 | -43.67658 | 2024-11-01 04:29:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2a2352d-9273-3f61-b19f-1ca9d343c0c9 | -4.39998 | -43.47267 | 2024-11-01 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 3af7cc9f-f975-303f-9540-93acc5064765 | -4.3993 | -43.47721 | 2024-11-01 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c12edafb-75de-3cbd-97f2-06f0984ed208 | -4.39689 | -43.46751 | 2024-11-01 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| a85fe918-a7ca-3d7f-b5e0-f3deeb8b1720 | -4.39621 | -43.47209 | 2024-11-01 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| b9d7e1f5-ae5f-35e8-9de1-b75350f90f0a | -4.39553 | -43.47664 | 2024-11-01 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 7ee70a63-015e-3c11-a6c8-46bb5415f2a6 | -4.39312 | -43.46693 | 2024-11-01 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 5dfa32cc-7b7b-3851-86c2-202e578fb0b6 | -4.39244 | -43.47152 | 2024-11-01 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 489de518-d214-3ff7-9fe4-472dfa7f973c | -4.39176 | -43.4761 | 2024-11-01 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b0223430-ab53-3b45-8b92-5f6771e44755 | -4.38935 | -43.46636 | 2024-11-01 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c2669eb6-f4a6-3ac1-87b3-9deb9ceb61f4 | -4.38867 | -43.47095 | 2024-11-01 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 139d87e9-ae19-3eb9-8c34-55ca5f83d463 | -4.38857 | -43.4681 | 2024-11-01 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |


[Clique aqui para ver as próximas entradas](README26.md)
