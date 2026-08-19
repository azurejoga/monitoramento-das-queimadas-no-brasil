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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66bda405-ce9f-3299-af7e-bafec1107731 | -6.8745 | -59.042999 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6decd33f-a361-3c2c-b086-8c86e53a796f | -3.1032 | -61.196301 | 2026-08-19 00:59:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a93334b9-c247-3cc8-bfae-fa5afcddba55 | -6.346 | -54.901199 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3aaaed17-3bcb-3824-b40c-d78ae166de78 | -8.5635 | -54.752201 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01204e1d-67e0-3bd9-b030-4e5a94ca79b9 | -7.1037 | -59.766499 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6c1ce4ba-c600-340e-94f1-0bcda1a7ffe6 | -9.3971 | -60.553902 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b264d7fd-2455-3da7-9105-64dee308924c | -10.6378 | -51.617802 | 2026-08-19 00:59:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d80749e5-99d9-3c0d-99b9-caa63f4fca77 | -21.5212 | -52.007702 | 2026-08-19 00:59:00 | METOP-B | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 957735ff-4acf-300f-8743-506735080248 | -6.0936 | -57.861099 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37587df4-4ce4-3d1b-89cb-4dedd501db11 | -9.3955 | -60.546902 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74ff0837-d73e-3326-a508-57c9b5b5958d | -8.5246 | -54.761799 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f79e8e3-8a41-3ab6-a791-cb7ee99b776c | -9.2081 | -60.811001 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ef5d1f7e-5cb8-38e7-9bc8-2fa6d568b143 | -8.544 | -54.757 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc226161-a39f-3426-b08e-ef4fd0e7f549 | -8.4997 | -54.870499 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7432a074-762c-3226-a684-8b0d8114fa1e | -15.2734 | -56.485901 | 2026-08-19 00:59:00 | METOP-B | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bcd3bd9d-fe71-32da-a7b9-8a8324b17c0e | -6.8629 | -59.036999 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d96c301-26ae-3e69-851a-63e8c3fce705 | -6.8764 | -59.051102 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5149ec0c-f9a3-3308-a09e-e53f78245af1 | -6.7545 | -59.147701 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 38c19173-7f1b-3f45-badb-3dd12e899af9 | -9.1787 | -60.817699 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 87de9989-7fd3-3bdd-8994-e11c61163aad | -9.3937 | -60.584301 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66e5f01e-b43d-3eae-a803-b83bb94dd929 | -9.0543 | -50.861599 | 2026-08-19 00:59:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bab705f-fc1f-3fcc-ba80-f14dac2a55f8 | -8.5474 | -54.770901 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc89fd82-1780-32f8-8ef4-15658c8a2b84 | -7.0554 | -59.825401 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8c2b5821-f476-3a95-b9f0-7c49b14fe1a6 | -11.9989 | -53.430698 | 2026-08-19 00:59:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7913eadd-6691-3e95-aad0-830849a1cba5 | -8.5657 | -54.677299 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45fec2d9-4678-3da4-a1b2-6440869c0737 | -9.4085 | -60.558701 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e7a25018-e18a-305d-8f9d-a899ae1490ec | -9.422 | -60.436798 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab0a80a5-fd5e-38d4-bdf9-36b872b8b1dc | -19.753 | -57.9422 | 2026-08-19 00:59:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a85e1402-925b-3673-a36b-bf5970e621cf | -7.9105 | -61.724499 | 2026-08-19 00:59:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d8f0d1ca-30e3-32c9-b7c8-f65757cd5668 | -6.8902 | -56.4384 | 2026-08-19 00:59:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6015579-cce9-3941-a9ce-368076e5711d | -6.6091 | -58.390301 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65704dab-ed46-3fa2-acfa-48ec4270c5c1 | -8.6486 | -62.816399 | 2026-08-19 00:59:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9a523549-6e4f-364b-952b-cd823486954b | -8.9044 | -60.563 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7916ac63-ec6b-3f0c-9340-0a892eaf47e9 | -6.0162 | -57.838699 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 986707f6-40b0-3c3c-9a67-f1f85a6adefa | -8.5726 | -54.705502 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7648acd-ec96-34bd-8a4f-240a849b9cfc | -6.0012 | -57.8624 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fc5a2fd-b1d8-30cb-9bf1-e99d40c2bd96 | -6.634 | -59.072899 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2289d100-8b7d-3516-b74b-bc882e04d92e | -6.8941 | -59.038399 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a05f39e4-7234-368f-826e-c6b60dc05bef | -8.5274 | -54.731499 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 849b566f-d6f0-3aac-970e-78d1cf15367c | -9.1191 | -61.604198 | 2026-08-19 00:59:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ee643d26-0a14-3d2b-9297-d1a715996b2c | -6.0951 | -57.911201 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f708ab3-40c5-36a0-91b1-d40ffb0fbb8d | -6.7915 | -59.441002 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| de5ef153-e786-3d84-b8d1-a1dc37d433d8 | -6.0065 | -57.8409 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 117fe173-940f-3556-b25d-2c1ff794dfda | -6.3398 | -54.918201 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a179220-5c25-3622-94bf-ad644f757dc8 | -11.2185 | -55.064301 | 2026-08-19 00:59:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b6a03678-3c86-3644-99ea-91391aa22559 | -9.4301 | -60.427502 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cca01ca3-a2de-30b9-be81-3cc86be5c03f | -16.570101 | -51.622101 | 2026-08-19 00:59:00 | METOP-B | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0304a5d3-3e4f-3862-bb7b-1ee560c81848 | -6.011 | -57.860199 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a766eea-f4db-3ed5-958f-1ffc5956299d | -6.683 | -59.0616 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 434da908-22ac-3186-9c5e-85ed17dfd483 | -8.9599 | -60.580002 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bbf35016-3fb6-3a60-9300-70ac511dec49 | -8.5406 | -54.743 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec92fe04-ddcd-3d1d-94fe-0f343c8afb18 | -19.739901 | -57.929798 | 2026-08-19 00:59:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6793bd81-d575-3c17-90a6-1bc349cd9e10 | -8.5372 | -54.729099 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20eb4398-ae64-3bea-a1ea-cb904ed0a664 | -8.5343 | -54.759399 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0ae5d9c-0dd7-3df1-a7ee-39342bed7dff | -9.3987 | -60.560902 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7522abc2-dbfc-3c4c-8525-897b8a33cbc2 | -21.4466 | -48.506302 | 2026-08-19 00:59:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| aabdd854-ba32-3881-a35f-5daac91fc0c3 | -6.4386 | -52.721699 | 2026-08-19 00:59:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e9326d7-88eb-3d93-b500-75dc54da92ae | -8.6404 | -62.825699 | 2026-08-19 00:59:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f9cf2ffe-2b02-3495-8226-c25262f43c4e | -6.083 | -57.9039 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd4890c1-55c3-37a3-9753-b1fa0cf19d13 | -7.5655 | -55.561401 | 2026-08-19 00:59:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27886d66-e8d3-3c18-a645-2d61e072ccf7 | -8.5377 | -54.7733 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0e061c7-cd59-39c2-9648-99d14f7998ec | -5.498 | -60.1343 | 2026-08-19 00:59:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bbbb4272-ef8a-3899-aa18-61e50eac6630 | -8.5537 | -54.754601 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c58a7b6f-0cd6-3c85-a926-5bc9ed1276f8 | -9.3841 | -60.542 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f2113f08-8f2a-3890-a1c0-36d25a428014 | -9.4252 | -60.451 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c460170-da82-3362-b37c-15bb1e3babfb | -19.7628 | -57.9398 | 2026-08-19 00:59:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5879c9be-8024-39bc-91f4-f376102ad432 | -6.0169 | -57.797699 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1287679-4d23-346b-98f2-8ca8fc4f3b7d | -11.2282 | -55.061798 | 2026-08-19 00:59:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0e19675f-cc17-3a48-a0da-5e6aabef4762 | -6.7398 | -59.039799 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2984a7dc-98e7-3c25-99b9-52e3c19e5730 | -8.5829 | -54.747398 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 442cdf52-6942-37b3-a52c-9ea3bb03e5d8 | -6.1447 | -57.859299 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e01b63b3-0f5b-33f8-9bd2-a089dccc9ec7 | -19.7318 | -57.939701 | 2026-08-19 00:59:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 68534a20-e37d-3df7-83be-c83bf7803d6b | -6.0365 | -57.793098 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f412736b-7d0f-3b25-b497-7ec268c6459f | -7.5363 | -55.568501 | 2026-08-19 00:59:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ee33168-77ac-38b4-b9d9-26ec4ef6beb5 | -8.5698 | -54.735802 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a348a24f-fcf3-39e7-a427-87e40277f0df | -6.3363 | -54.9035 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df85a2a0-1468-3576-b9b2-43304db0e24a | -8.5338 | -54.715099 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9c1c8b5-4973-3286-aa48-59262a5d72dd | -9.1105 | -60.381699 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 36663a9c-60fa-31d3-bdff-22044f3d03b2 | -6.736 | -59.023499 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 98bb4b51-beee-3d63-82cb-38f6037e9fd8 | -6.7541 | -59.457802 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3291d7f-bbf8-3bb1-b13d-7f80520931f4 | -9.0124 | -60.493698 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d5ce7a69-5575-3393-bb01-ca8afbe9196b | -21.517799 | -51.994499 | 2026-08-19 00:59:00 | METOP-B | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 25cc5034-650c-3393-8749-c4996d7a32d4 | -5.4962 | -60.126701 | 2026-08-19 00:59:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 27a4ce2a-d609-3130-bded-f8cb7b1f47c5 | -15.2832 | -56.483398 | 2026-08-19 00:59:00 | METOP-B | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ad41cb3e-f334-3b8c-8a13-23d0851b335a | -7.5266 | -55.570801 | 2026-08-19 00:59:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f311ba97-a660-3a3a-a8f9-1b4ce7073ad9 | -9.1424 | -60.612202 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ef77c6af-381d-3856-a673-ea91a869bb75 | -19.775801 | -57.952202 | 2026-08-19 00:59:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| abade0ab-f650-3fb0-a26a-c709001fd385 | -6.7643 | -59.145401 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 00dbd182-4099-380d-b917-68c65627f2c6 | -9.1408 | -60.605202 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3368f57a-0609-3386-a33b-31605568e0ea | -6.3557 | -54.8988 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f002f06e-909e-3a97-b10b-e33bdbe074b6 | -9.4236 | -60.443901 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d0c9e8d1-f57f-3182-8087-16b8766cdbe9 | -9.4133 | -60.5798 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9cc1eee6-0e57-3ed1-adab-1afd463b164c | -6.8436 | -58.998501 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f81ee07e-3153-3757-8021-8d2d8ed8091e | -6.8862 | -59.048801 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 73f4ddfd-210b-3e20-896c-cd33c3dea240 | -6.9975 | -59.0401 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cdebb8ee-49c4-3008-9765-a0438c7ee691 | -6.0875 | -57.923 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d997c916-cfc3-3e3b-a3f4-5a809d8292fd | -9.2017 | -60.783001 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c7df0298-6d2e-3cb8-b6c8-de05e47892d0 | -6.6954 | -58.937401 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d183791-6c1b-3d16-a01b-e13a1fe727d2 | -6.1425 | -57.849701 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65692763-9c32-3657-9bea-ffe47c21e204 | -3.1048 | -61.203499 | 2026-08-19 00:59:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
