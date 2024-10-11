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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6edc658-db57-3a0f-890c-7809f29c09be | -4.1333 | -48.2507 | 2024-10-11 02:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| ee59a0c8-c254-3927-8834-be6ff8fd420c | -5.3265 | -60.1239 | 2024-10-11 02:05:37 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 6dfd3266-19e0-3e0d-bd40-2756e8e9e24b | -6.5589 | -60.0252 | 2024-10-11 02:05:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 8c755904-981c-3f70-a633-237efccfe381 | -8.4231 | -55.4704 | 2024-10-11 02:05:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 1317d96c-860d-30c1-a398-dee949314110 | -8.4417 | -55.4692 | 2024-10-11 02:05:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 77efa19c-3182-38b1-9fcd-f0a2b68394d0 | -10.46 | -46.7885 | 2024-10-11 02:06:05 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 3fd8eb1b-2425-381e-bc3e-b98f666cc034 | -10.6965 | -53.0147 | 2024-10-11 02:06:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 4c190ce4-17cc-3213-9cbe-496dde915190 | -10.6962 | -53.0354 | 2024-10-11 02:06:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 6abfa9a4-6639-395e-a6b8-58fdbe1c5d8d | -10.7059 | -64.1138 | 2024-10-11 02:06:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 85d3aeb0-2e0a-35c5-b81d-dffd05b2d3e3 | -12.8708 | -53.4799 | 2024-10-11 02:06:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| d754ca18-cbf3-31e3-898a-a6da1226a3fd | -12.8705 | -53.5007 | 2024-10-11 02:06:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 90a803a9-844f-36f6-9dda-97815e3de22c | -13.0401 | -53.6483 | 2024-10-11 02:06:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 56d666be-80f4-3dc8-86a4-7a4f58348751 | -13.021 | -53.6504 | 2024-10-11 02:06:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| d87a78eb-5a9e-377f-9bfb-c2bd251bc6e0 | -13.7348 | -60.5883 | 2024-10-11 02:06:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 912c5b08-42fc-3762-a4fe-248327871bcb | -13.7346 | -60.6079 | 2024-10-11 02:06:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| a1bd521c-dbe2-3bea-bd4a-09ae75415c5f | -13.9663 | -45.8025 | 2024-10-11 02:06:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 76fef94a-f57c-39fc-87f1-44d15805adf9 | -2.6533 | -53.3506 | 2024-10-11 02:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 322e3375-ab08-3f7f-9e47-029b280c3c22 | -2.6716 | -53.3502 | 2024-10-11 02:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 2642b54b-5bb4-3a6d-9efe-c89ee79d8c75 | -2.7847 | -52.4933 | 2024-10-11 02:15:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 05794e23-303c-3285-b446-a5e8323c09ab | -2.7848 | -52.4728 | 2024-10-11 02:15:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 38536583-d72e-32ee-9683-c6c19e023bfa | -2.8081 | -51.0084 | 2024-10-11 02:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 3f2a7f0d-81b4-3792-ba28-11e6e2a6c3c1 | -2.9673 | -52.9169 | 2024-10-11 02:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| bea008f3-a8d8-3641-8d91-90484e2b2353 | -2.9673 | -52.8966 | 2024-10-11 02:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 9e5158fa-7d49-3c9f-aba2-5078f0687d3a | -2.9857 | -52.9164 | 2024-10-11 02:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 63dff601-b0c0-3b3d-8633-b7d9ac4f019f | -2.9857 | -52.8961 | 2024-10-11 02:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 128.9 |
| 46c2710e-8685-3492-b514-1bb695f75dd0 | -3.1422 | -50.4562 | 2024-10-11 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 8f390783-2854-3904-9f29-8ffcfb563fb4 | -3.1423 | -50.4352 | 2024-10-11 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| cf153dda-7579-320e-b9c9-685b2707f73d | -3.1607 | -50.4556 | 2024-10-11 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 05f28002-ee08-3237-84fd-d7478de65113 | -3.1608 | -50.4347 | 2024-10-11 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 136.7 |
| 4ee5857a-49e4-3940-93ca-4a1f2fc1b498 | -3.3096 | -50.1781 | 2024-10-11 02:15:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 9befdd75-d446-3d4c-93e7-39dfc6c93fc0 | -4.0962 | -48.2523 | 2024-10-11 02:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| a69d031c-602e-3fed-89cd-580527ba8bd7 | -4.1146 | -48.2731 | 2024-10-11 02:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 8e0a8cda-9c84-33ed-8be5-41e51ac3f336 | -4.1148 | -48.2515 | 2024-10-11 02:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 156.1 |
| f9760b61-6dd5-3c67-bbf7-5d85bbdae115 | -4.1149 | -48.2299 | 2024-10-11 02:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| e01d78a2-3f9f-3ad9-9d12-e8484a09ca4e | -4.1333 | -48.2507 | 2024-10-11 02:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 13965eaf-986f-35e1-bf90-3f10328daf9d | -5.3265 | -60.1239 | 2024-10-11 02:15:37 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 0d47a8b0-8cc3-3136-bcfe-2c20534c634b | -6.5589 | -60.0252 | 2024-10-11 02:15:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 4ca7b53e-2840-3262-89aa-27600b6b6fb6 | -7.936 | -61.271 | 2024-10-11 02:15:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 4d8fc0c6-b160-3394-9db3-5b226251de44 | -8.4231 | -55.4704 | 2024-10-11 02:15:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 7dfaaf7a-febb-3658-92cc-7703165b83a0 | -8.4417 | -55.4692 | 2024-10-11 02:15:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| ab3974fb-618b-3507-8179-28490557a22c | -10.6962 | -53.0354 | 2024-10-11 02:16:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| e357d8ba-0bb3-33fd-8287-22f02bc56589 | -10.6965 | -53.0147 | 2024-10-11 02:16:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| a55e87a0-24c5-3fa0-8c28-56ded09235db | -10.7059 | -64.1138 | 2024-10-11 02:16:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 9376770d-945c-3b5e-b6a2-856b608152a4 | -11.2909 | -50.9421 | 2024-10-11 02:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 830a2d35-c081-38ab-ba5b-b41fc6ab5de9 | -11.2912 | -50.9208 | 2024-10-11 02:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 890b57d9-f522-3477-9054-3fb3b8761852 | -12.7673 | -44.8904 | 2024-10-11 02:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 1b3d0a18-c46f-34bf-ae04-a6107d9568dc | -12.7678 | -44.8671 | 2024-10-11 02:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 214.1 |
| a978289c-9b8d-3419-bdc4-006964de712f | -12.7682 | -44.8437 | 2024-10-11 02:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 7bdc0e8f-fcf9-37cf-95b2-56f8411f9ea8 | -12.7866 | -44.8873 | 2024-10-11 02:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| f288d7ee-c685-3c87-aa25-b4c10ec5cf2f | -12.7871 | -44.8639 | 2024-10-11 02:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 172.7 |
| dd1d0087-2853-38e2-aed5-b59293f81af2 | -12.8899 | -53.4778 | 2024-10-11 02:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 70b3bfca-413a-38a2-88ce-dda523c8a5ea | -12.8517 | -53.4819 | 2024-10-11 02:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 213.1 |
| c08dd405-ee83-3e0c-83d4-997ee4139cb0 | -12.8708 | -53.4799 | 2024-10-11 02:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 236.1 |
| c400b57d-048d-3cab-a0ab-991bc156e69a | -12.852 | -53.4611 | 2024-10-11 02:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 226.5 |
| 4855dbcb-d518-362a-b073-8b8802166b51 | -12.8705 | -53.5007 | 2024-10-11 02:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 4a96fa6c-028c-3e11-a542-2287316246d0 | -12.8711 | -53.459 | 2024-10-11 02:16:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 187.0 |
| 188f0163-336b-39f3-8212-0de204097b27 | -13.7348 | -60.5883 | 2024-10-11 02:16:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 9adf11a3-5e5d-3ec8-84f4-1756ec4bb231 | -13.7346 | -60.6079 | 2024-10-11 02:16:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 94fee1ff-5d5f-3eed-9061-bf6f15647998 | -13.9663 | -45.8025 | 2024-10-11 02:16:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| dc485cd4-612c-32a3-8fa7-3c9c88a73fcd | -9.6165 | -64.944901 | 2024-10-11 02:25:04 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 522e48f7-564c-349f-b0b8-72d0f6170c93 | -9.6231 | -64.970398 | 2024-10-11 02:25:04 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d2b4c735-6439-368e-8775-650ae589a96f | -2.6533 | -53.3506 | 2024-10-11 02:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 8d0f33af-0bca-3b15-aeb1-c79d0f96c811 | -2.6716 | -53.3502 | 2024-10-11 02:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| ee16d58f-142c-3302-a94a-68e12e0ad103 | -2.7395 | -49.5412 | 2024-10-11 02:25:22 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| cb354a0f-ddb6-33e8-a4a4-acf73d77c05d | -2.7847 | -52.4933 | 2024-10-11 02:25:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| abacf175-7448-3fb6-b999-8f11995f0d88 | -2.7848 | -52.4728 | 2024-10-11 02:25:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 3d1cf938-c765-340d-bf1b-4763a8c18e51 | -2.9673 | -52.9169 | 2024-10-11 02:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| b00aa0c3-3d5f-3e24-9e40-885e95edc158 | -2.9673 | -52.8966 | 2024-10-11 02:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 120.1 |
| b2eb28d8-6ce3-3bbf-98bf-93aececab73d | -2.9857 | -52.9164 | 2024-10-11 02:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 133.7 |
| 384d35a3-f961-351b-9b74-70f993e5c18b | -2.9857 | -52.8961 | 2024-10-11 02:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 144.5 |
| 5da2dfc3-244a-3dd6-9bef-cfc439f11121 | -3.0343 | -61.673 | 2024-10-11 02:25:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 2ef3cad2-5f43-3d30-a38e-c88245040e4f | -3.0525 | -61.6727 | 2024-10-11 02:25:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 4f107e88-4275-3fb8-bed4-47e6c17b9410 | -3.1422 | -50.4562 | 2024-10-11 02:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 0e06a56d-61ce-3346-92a0-bc94977b0c07 | -3.1423 | -50.4352 | 2024-10-11 02:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 9fd428e5-52d9-34c4-a31e-1c471ee97b25 | -3.1607 | -50.4556 | 2024-10-11 02:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 6561bf3d-4553-35cf-99d0-5806ff1b2a96 | -3.1608 | -50.4347 | 2024-10-11 02:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 2e98a9f9-f4ef-33d3-a2e0-3238aa4c79d3 | -3.3096 | -50.1781 | 2024-10-11 02:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 162b3215-bf08-346f-b3bf-7154f6719b24 | -4.0962 | -48.2523 | 2024-10-11 02:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 70df912e-9535-3957-8237-a71215d4b1cf | -4.0963 | -48.2307 | 2024-10-11 02:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 9e98d7d2-6292-32de-ac2e-f0ec9632661c | -4.1146 | -48.2731 | 2024-10-11 02:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 78232c2c-f7c9-3ab4-af6b-ad1d9471d98a | -4.1148 | -48.2515 | 2024-10-11 02:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 390.1 |
| 11304534-fe5e-398b-b9bf-9f8fe6767f6a | -4.1149 | -48.2299 | 2024-10-11 02:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 138.2 |
| 43a5ac68-14d7-3c61-b9c8-aa17ea09c011 | -6.1301 | -47.2664 | 2024-10-11 02:25:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 25849cdf-b531-3130-8d0e-b4ee076d50fd | -6.5589 | -60.0252 | 2024-10-11 02:25:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 30af54f6-574c-3bcf-ade8-f11151d02813 | -8.4231 | -55.4704 | 2024-10-11 02:25:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| aa7bed54-905d-38be-a1ad-7d3633a6c9aa | -8.4417 | -55.4692 | 2024-10-11 02:25:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 05ac5359-a177-3391-a1e8-411ba210e915 | -10.6962 | -53.0354 | 2024-10-11 02:26:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 62e88971-e20e-31a9-afdf-746adb252458 | -10.6965 | -53.0147 | 2024-10-11 02:26:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 0c1414b9-45ad-3abe-b7e1-33ae780f40fb | -10.7059 | -64.1138 | 2024-10-11 02:26:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 890b86a5-a4cd-31c9-a038-72a123095bab | -11.2909 | -50.9421 | 2024-10-11 02:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 63df691f-535f-3f1b-aab0-80f95e7a7072 | -11.2912 | -50.9208 | 2024-10-11 02:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 1976c928-a217-3826-9f87-91b959f80b13 | -12.7875 | -44.8406 | 2024-10-11 02:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| fcdcbb0c-4375-30d8-9b21-96a56661c7e3 | -12.7871 | -44.8639 | 2024-10-11 02:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 261.6 |
| e349d8a7-e078-3358-b88e-b2518ba0095e | -12.7866 | -44.8873 | 2024-10-11 02:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 18f52201-6356-3067-921b-fa6986ad6b3a | -12.7682 | -44.8437 | 2024-10-11 02:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 39b44317-20b9-39f0-b580-66947f711d1c | -12.7678 | -44.8671 | 2024-10-11 02:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 329.4 |
| 7b416837-995f-340a-b42a-4288125e693c | -12.7673 | -44.8904 | 2024-10-11 02:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 784288f7-4a62-3e6b-8f87-25832a793861 | -13.9857 | -45.7992 | 2024-10-11 02:26:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 48d87a30-0e04-3a9f-9160-5fe8bba0f883 | -13.7346 | -60.6079 | 2024-10-11 02:26:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 6ad3e893-4f65-3163-a89b-fd44cfe43117 | -13.9663 | -45.8025 | 2024-10-11 02:26:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |


[Clique aqui para ver as próximas entradas](README28.md)
