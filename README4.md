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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 906f9cf3-36ff-312b-82f8-9925f1c8cf6d | -8.9371 | -60.747002 | 2025-08-11 00:53:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f94a61d-babf-3beb-acc2-5f4cf880f957 | -8.5528 | -54.682701 | 2025-08-11 00:53:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea2de270-9ce4-3137-bdb3-1a9a5dedc046 | -9.0259 | -59.7383 | 2025-08-11 00:53:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce10fa23-bab0-30d2-a81b-8bb57c44eca3 | -7.082 | -59.179798 | 2025-08-11 00:53:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 296a62d2-70fc-3284-8ccd-9c277ffc4cd0 | -8.5606 | -54.6717 | 2025-08-11 00:53:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b1af4a5-830d-333d-964a-811718efb633 | -7.0737 | -59.1889 | 2025-08-11 00:53:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f02b4755-8b4a-3462-be91-144e5dea175e | -21.234501 | -51.0201 | 2025-08-11 00:53:00 | METOP-B | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| af9962de-d94f-385f-b74f-550e45fd6d8d | -7.0934 | -59.184502 | 2025-08-11 00:53:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9dcb7cd2-0bee-3176-8832-d602cdc4c8f2 | -7.0903 | -59.170601 | 2025-08-11 00:53:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 42a6d7c8-f202-3638-a69c-9e6ba7cf9a8b | -8.9175 | -60.751202 | 2025-08-11 00:53:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0fb9a4dd-0fd4-3e48-8901-d4f552cd2ab4 | -21.236799 | -51.0298 | 2025-08-11 00:53:00 | METOP-B | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bf13c70c-6413-3124-a9a4-2596b5435f6e | -7.0835 | -59.186699 | 2025-08-11 00:53:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a22a28d0-2cab-32fc-a165-b59b7f4278cd | -18.604 | -46.840801 | 2025-08-11 00:53:00 | METOP-B | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2014db19-cd0b-3a8c-9a46-8373addf4798 | 1.1391 | -59.444 | 2025-08-11 00:53:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1dda339b-7c7b-3f5a-b784-123c2f112a8d | -21.246599 | -51.0271 | 2025-08-11 00:53:00 | METOP-B | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3699ff0e-2b9d-321a-8b78-823cde03df29 | -8.9256 | -60.741199 | 2025-08-11 00:53:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8183e533-5955-3ec1-872b-03653cb41972 | -8.9452 | -60.737 | 2025-08-11 00:53:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e355b6f0-d116-3e55-8a84-7ca3402b0120 | -7.0918 | -59.177601 | 2025-08-11 00:53:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2a942de8-cb90-3fb3-9bab-be35dd574c63 | -18.6136 | -46.838001 | 2025-08-11 00:53:00 | METOP-B | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fa95e039-7678-3f78-87be-637c3e8c480c | -7.0593 | -59.1703 | 2025-08-11 00:53:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 836795fa-743d-3ad3-bdd4-522dcd0801f7 | -8.9337 | -60.7313 | 2025-08-11 00:53:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0e1edf0d-c2d8-3b12-adb1-79dd5763d6b1 | -18.829599 | -48.633701 | 2025-08-11 00:53:00 | METOP-B | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 60746057-8c7e-3cb1-ab8e-8bc96f5d750c | -8.9401 | -60.713402 | 2025-08-11 00:53:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98935192-ba81-34e2-8015-a1eceeb5893f | -8.5585 | -54.663101 | 2025-08-11 00:53:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc8f1be8-02b3-3264-8744-8695f4b9d5d1 | -9.3807 | -61.523201 | 2025-08-11 00:53:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 72513583-17d0-3aa6-8c8d-9e85f4cc87d8 | -7.0675 | -59.161201 | 2025-08-11 00:53:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 169144bd-4d2d-3f68-8a43-ad6d666d43e5 | -7.2598 | -59.982101 | 2025-08-11 00:53:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ca5e75cf-5764-316e-8a51-dfe9164242ec | -8.9435 | -60.729099 | 2025-08-11 00:53:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c977d33-7b30-3c25-8a1e-61f4666124a3 | -9.3789 | -61.5145 | 2025-08-11 00:53:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9c8d689-86bb-3204-83db-496d670ba017 | -7.0639 | -59.191101 | 2025-08-11 00:53:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9c55774e-40da-376b-aa71-13da2e087ced | -8.9273 | -60.7491 | 2025-08-11 00:53:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4c3be4e5-4190-35b5-9a1e-e4dc3fd01116 | -21.0427 | -50.027901 | 2025-08-11 00:53:00 | METOP-B | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3a5d33a1-befc-3168-9bcc-287a03981924 | -22.9907 | -47.641701 | 2025-08-11 00:53:00 | METOP-B | MOMBUCA | SÃO PAULO | Brasil | 3530904 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 93d1bf43-20da-36c9-b0e3-54b0530d4389 | -8.5724 | -54.678101 | 2025-08-11 00:53:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b62b6f61-8c8d-3fd5-899c-329a1cfbc6a2 | -21.040001 | -50.0168 | 2025-08-11 00:53:00 | METOP-B | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f81980ea-d95b-3552-8050-4e6b8b24cc8d | -13.0674 | -56.838501 | 2025-08-11 00:53:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 618cec6d-fb97-3b9d-b71e-d6a6628e9d1f | -8.9418 | -60.721199 | 2025-08-11 00:53:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 45ae9363-4892-3943-98dc-c01981572145 | -7.0608 | -59.1772 | 2025-08-11 00:53:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f9cd4728-e106-366f-91d7-9f889994fa6a | -22.987 | -47.627499 | 2025-08-11 00:53:00 | METOP-B | MOMBUCA | SÃO PAULO | Brasil | 3530904 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9a84cc87-09de-356b-a932-6bb05f34028c | -6.1018 | -59.908699 | 2025-08-11 00:53:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 46f5149e-8473-3656-86ba-fffc0e5d4c3c | -9.377 | -61.505901 | 2025-08-11 00:53:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4bbe5c4a-9dec-352f-b3b1-ffff79809def | -21.0497 | -50.014099 | 2025-08-11 00:53:00 | METOP-B | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2bec73b4-e0ed-389c-addb-bfe0016316c0 | -8.9354 | -60.739101 | 2025-08-11 00:53:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 64cfb4e0-7427-3936-98fd-3847732ac22c | -7.0789 | -59.165901 | 2025-08-11 00:53:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ccec507-df50-3882-9f8e-17863ec33de4 | -8.9303 | -60.7155 | 2025-08-11 00:53:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 258faa07-9be3-3b92-99cd-f3292473b378 | -18.1523 | -46.9757 | 2025-08-11 00:53:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d4e18497-8791-39fc-96ee-150832a2b8c0 | -18.1574 | -46.994598 | 2025-08-11 00:53:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9279a3dc-d3e5-3b89-a822-94e0419e478f | -9.3887 | -61.512402 | 2025-08-11 00:53:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e7d46993-be0c-38a6-8dea-07eb4513175b | -7.067 | -59.204899 | 2025-08-11 00:53:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 850c859b-cdf2-3e60-9633-cbbd91eda31f | -8.5646 | -54.689098 | 2025-08-11 00:53:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bc2801e-8eb2-3a2e-b663-b8c25470a4f4 | -7.0613 | -59.2165 | 2025-08-11 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.5 |
| f4d71b03-0c9a-3c9b-b589-8379d29fddbe | -7.0797 | -59.2157 | 2025-08-11 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.6 |
| c4e5670f-c063-33d1-971b-164aedfca87b | -16.2093 | -50.3452 | 2025-08-11 01:00:00 | GOES-19 | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 916a20e9-956d-397a-8c29-daf4cba3fc80 | -8.9401 | -60.7288 | 2025-08-11 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| b52c62c5-97b3-34d5-a1db-0673233a54d6 | -7.0614 | -59.1972 | 2025-08-11 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 6919f1d5-f4b2-3199-b207-6a9f9a6690c6 | -8.9215 | -60.7297 | 2025-08-11 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 045fd778-9c62-3de6-86b5-6faa755c4465 | -9.3806 | -61.5315 | 2025-08-11 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 69d25597-e741-3042-b052-56af63e7fc44 | -18.6293 | -46.8394 | 2025-08-11 01:00:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 33878869-1f3f-3e23-97e4-a07bf947b007 | -8.9213 | -60.7489 | 2025-08-11 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| ede9e19c-f381-3edb-9b16-150088871837 | -8.5604 | -54.6973 | 2025-08-11 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 6468ba68-8e85-33dd-a4fe-58312c7cbb8a | -18.6287 | -46.8629 | 2025-08-11 01:00:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 56.3 |
| fb48d61a-2fd9-3ed2-a8ad-cf6eab0d5d42 | -7.0799 | -59.1964 | 2025-08-11 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 171.9 |
| 487f47a7-0b0a-353e-87fd-7657fa2c2ef8 | -8.9399 | -60.7481 | 2025-08-11 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 3bee72f8-50f3-3530-b88a-0e1a88b849c1 | -8.579 | -54.696 | 2025-08-11 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 6c613d14-6682-3225-904c-102f689d710d | -18.6293 | -46.8394 | 2025-08-11 01:10:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 102.9 |
| c8cc796f-4478-3553-aff0-4aa274ca12be | -7.0614 | -59.1972 | 2025-08-11 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 133.5 |
| 446f0d88-fc0b-3325-b5fe-be15cabef336 | -9.3806 | -61.5315 | 2025-08-11 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 621f1925-a2fa-3306-b47b-43f9c7bec9d2 | -8.9401 | -60.7288 | 2025-08-11 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 6cf12b9b-5ef2-386e-9cbe-ebe3d8ce54df | -8.9399 | -60.7481 | 2025-08-11 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 1701032b-32a6-3a45-9f2d-0d37150245f4 | -8.5604 | -54.6973 | 2025-08-11 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| dd03e19e-33e1-36d8-a733-550cc339877a | -9.457 | -40.3889 | 2025-08-11 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 7fa2d804-85d3-3a6d-a6c4-25be2a573c01 | -8.9213 | -60.7489 | 2025-08-11 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| ed2e6c33-d1b9-3a26-81e6-326f582fdd96 | -8.9215 | -60.7297 | 2025-08-11 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 0320f438-b33e-35be-b59f-b1b66b56feab | -7.0797 | -59.2157 | 2025-08-11 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 7f7e6d56-e331-32d8-a0de-87d683dc81d9 | -7.0613 | -59.2165 | 2025-08-11 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| c42eb182-2b2e-3d31-be55-a43159d4e485 | -9.4574 | -40.3641 | 2025-08-11 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 54.8 |
| 80b9e4c6-5f88-34cb-aec1-e6a3b1c08e9a | -9.4765 | -40.3613 | 2025-08-11 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 69.3 |
| cda37eca-fbe4-3441-bae5-5d4c71b8c9bd | -7.8773 | -44.972 | 2025-08-11 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 51.7 |
| c5963201-5b5a-3a12-98e0-32cf175e23ae | -3.4254 | -49.0517 | 2025-08-11 01:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| eee16d53-8092-3fc4-a359-b3dc43f98a1d | -18.6287 | -46.8629 | 2025-08-11 01:10:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 32478963-a3d7-3660-9032-8e25afdfd1d6 | -7.0799 | -59.1964 | 2025-08-11 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 154.9 |
| e0639b5b-6c9f-3528-9753-e0597cbf0deb | -9.4761 | -40.3862 | 2025-08-11 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 111.6 |
| bf6f6d8a-c436-3464-a866-c5bd184c6ef7 | -7.4564 | -43.9554 | 2025-08-11 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 54.8 |
| f4bed90e-62a2-325a-a6bc-2823ca733a80 | -8.9213 | -60.7489 | 2025-08-11 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 20013c47-0e10-3601-a649-19c36963b494 | -8.9399 | -60.7481 | 2025-08-11 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| c9436ca2-5a52-3f2b-972c-fa6201d24d02 | -9.3806 | -61.5315 | 2025-08-11 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| c34b44b4-4c2f-3c50-87d4-766061d8a664 | -7.0614 | -59.1972 | 2025-08-11 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.2 |
| e694b1be-bd10-3b96-87af-58fd100689b4 | -3.4254 | -49.0517 | 2025-08-11 01:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| d15c0275-7a31-3614-bd7f-807c6460ae89 | -18.6287 | -46.8629 | 2025-08-11 01:20:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 08bba9c8-7b32-3160-9a8a-47117c04de9a | -18.6293 | -46.8394 | 2025-08-11 01:20:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 1b58ec8e-4296-359e-9109-fcb65f45cc31 | -7.4564 | -43.9554 | 2025-08-11 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 59.0 |
| db7a2171-74a7-3053-b30d-a48167b22994 | -7.0797 | -59.2157 | 2025-08-11 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 10cf6d04-ca69-30af-961a-6f52cd15a646 | -21.0536 | -50.0356 | 2025-08-11 01:20:00 | GOES-19 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.5 |
| 9d0a85d1-2f87-3182-8ebe-0091f948fe11 | -8.9401 | -60.7288 | 2025-08-11 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 1525f931-ead3-31dd-b70a-01c550231e3e | -9.4761 | -40.3862 | 2025-08-11 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 51.7 |
| 723af65c-e19b-3dcc-bef1-6ace1f37a7ea | -7.0613 | -59.2165 | 2025-08-11 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 805a5606-d738-3656-8053-fd47b1b07843 | -8.5604 | -54.6973 | 2025-08-11 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| da80c52c-c977-3cba-b108-042de0e73e5c | -7.0799 | -59.1964 | 2025-08-11 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 37764c0d-4395-3836-826b-8a30474161fd | -18.6293 | -46.8394 | 2025-08-11 01:30:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 162.1 |
| 9eac3628-c008-30c6-bdef-d783147a29f1 | -7.0799 | -59.1964 | 2025-08-11 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 135.1 |


[Clique aqui para ver as próximas entradas](README5.md)
