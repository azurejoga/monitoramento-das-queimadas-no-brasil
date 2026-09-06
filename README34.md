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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 519f8865-bcf9-34d2-9c79-e0a9de3c2818 | -5.3646 | -56.0249 | 2026-09-06 06:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 0b132c11-5726-3051-bcb5-73b11e31aac2 | -5.3645 | -56.0447 | 2026-09-06 06:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 0e4b674e-af23-3d38-83e3-ed514b380c70 | -5.3645 | -56.0447 | 2026-09-06 06:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 4cad59e1-03b8-38d9-83a7-6fc36f5f1646 | -14.905 | -44.6782 | 2026-09-06 06:40:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 9143efb0-d158-3dfb-b35c-ac065ea6f737 | -5.3646 | -56.0249 | 2026-09-06 06:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| b79dbee3-f573-3896-9cdb-7be13e124bfe | -5.1423 | -56.2703 | 2026-09-06 06:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 3d6979ec-1973-36d9-91aa-2a16d67a72f2 | -5.3646 | -56.0249 | 2026-09-06 06:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 67dd26f9-34ae-34a0-b7de-a7b8bc2f5877 | -14.9246 | -44.6744 | 2026-09-06 07:00:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 55f4c8a7-e554-3746-ab43-cd58f87a9bc3 | -5.3645 | -56.0447 | 2026-09-06 07:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| ce5d4181-b544-369c-908b-206c4dd1dfd2 | -5.3646 | -56.0249 | 2026-09-06 07:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 992a9eb4-075a-3537-b629-8be1a824cfee | -7.79038 | -70.04694 | 2026-09-06 07:03:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 928063dd-6861-30bf-8207-03ba966f31f0 | -9.13127 | -70.88064 | 2026-09-06 07:03:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| de9ad390-5790-3f9b-8fd3-1136620d5227 | -9.13052 | -70.88641 | 2026-09-06 07:03:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c068e2a1-0c2a-3ffb-a773-7d1289d87733 | -7.78956 | -70.05331 | 2026-09-06 07:03:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56d4cd4d-319b-3445-9505-ea4934d7ea44 | -5.3645 | -56.0447 | 2026-09-06 07:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| bfe96885-53a3-3feb-8e43-632d3fe12a0c | -5.3646 | -56.0249 | 2026-09-06 07:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 85615c3c-4295-34a7-98c1-12d92a3455a0 | -14.9246 | -44.6744 | 2026-09-06 07:20:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 71.2 |
| e0646579-b375-3071-986a-5862a16cfef3 | -5.3646 | -56.0249 | 2026-09-06 07:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| a9974166-326b-3f0b-be5d-98f09c84ecb6 | -4.35654 | -47.78584 | 2026-09-06 07:20:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 245d404c-2319-325d-b07f-b6ef467f5ae8 | -4.35875 | -47.76486 | 2026-09-06 07:20:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 24f4b103-c481-31a6-868b-ffff9e57a022 | -3.55359 | -48.17265 | 2026-09-06 07:20:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 8be96213-fab7-3b14-8c5b-f2a15138637c | -3.54173 | -48.17799 | 2026-09-06 07:20:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 29ca780f-2f41-37a1-8eab-16f7b0befcf1 | -1.39435 | -55.16988 | 2026-09-06 07:20:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f26a81d5-3118-39e3-b37c-a83945d2f952 | -3.12045 | -57.68642 | 2026-09-06 07:20:00 | AQUA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5513c26a-494c-3582-a2f8-f182ec908959 | -4.36064 | -47.75737 | 2026-09-06 07:20:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 0411938b-e57f-30ff-b75a-3e0d3da5edf0 | -2.45823 | -57.91182 | 2026-09-06 07:20:00 | AQUA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 69420685-7600-3fb5-b844-33d9b17a8713 | -3.80923 | -55.88857 | 2026-09-06 07:22:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6d0e29a8-783b-3945-8cc6-3aee1998862f | -5.35995 | -56.03485 | 2026-09-06 07:22:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| ff8cba4b-99bc-303b-9639-eacdf3ee6a70 | -5.36127 | -56.0261 | 2026-09-06 07:22:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 5bd349e4-ec2b-339b-8021-2a348b70a741 | -4.66434 | -55.62308 | 2026-09-06 07:22:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f3e7bb74-53ee-3917-9107-4bb31848b25d | -5.3525 | -56.02481 | 2026-09-06 07:22:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| e80c77c8-8b6a-31bd-8500-d3195ae96433 | -4.67314 | -55.62435 | 2026-09-06 07:22:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 983f6c1b-7515-33e8-823c-ef37f7f0fd47 | -4.46735 | -55.08554 | 2026-09-06 07:22:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0036a399-e9f4-3a59-acd7-30670388aa66 | -5.84333 | -60.25256 | 2026-09-06 07:22:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| edee2dcb-3dd7-3b4d-b48b-45331d6d4d89 | -6.83801 | -59.42584 | 2026-09-06 07:22:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 55663b27-7b32-32e3-be4b-9683b5ea1659 | -5.15109 | -55.95595 | 2026-09-06 07:22:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| e8b3ded9-f3b7-302f-8a23-bf1bcba9f7ea | -10.74475 | -60.70795 | 2026-09-06 07:22:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| aac45334-ccfd-3b12-b940-33ac00d9a2e0 | -10.74439 | -60.71464 | 2026-09-06 07:22:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 65bd89c4-6ede-3c44-9f2c-433a06915f47 | -4.66302 | -55.63186 | 2026-09-06 07:22:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 03130f1c-4301-3b47-b9c8-c6f4e3ea36be | -3.13844 | -60.63186 | 2026-09-06 07:22:00 | AQUA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| bccf2354-6b7a-36e6-ac2f-fc0b43793e55 | -6.12846 | -57.74253 | 2026-09-06 07:22:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9d197739-f995-372a-b4ee-1ef6c8008398 | -5.13117 | -56.26547 | 2026-09-06 07:22:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| d63ddb07-8c60-3f0c-a44b-f01e4b40b7d9 | -5.12985 | -56.2742 | 2026-09-06 07:22:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 759725de-1cfe-3b1d-a37d-101073178491 | -5.65055 | -60.23542 | 2026-09-06 07:22:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c9d31c02-a9da-395f-b61b-c8cf37c39d9e | -6.0642 | -57.79241 | 2026-09-06 07:22:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7ebb212a-8f77-3cff-8490-35a2281fbe45 | -6.87556 | -55.61389 | 2026-09-06 07:22:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6dbe9b88-c24b-3617-8e13-8e0ceba3a6ec | -6.95427 | -59.73539 | 2026-09-06 07:22:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a74c15ea-cabf-3830-b196-09b2612dd3ee | -5.14125 | -56.25804 | 2026-09-06 07:22:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2ada9c7b-1d01-3377-b400-c5184ac3e9f1 | -5.141 | -55.96341 | 2026-09-06 07:22:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| bf3a7b7c-d37f-34fa-b5ca-4ec0b8c2364d | -6.06279 | -57.80159 | 2026-09-06 07:22:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3d9b8d98-e553-365c-a135-eb640e4d21ce | -4.67182 | -55.63311 | 2026-09-06 07:22:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b22716ac-f553-33fb-9a1a-1f2765eb3f2c | -3.79305 | -55.87728 | 2026-09-06 07:22:00 | AQUA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4781e19f-dce6-366f-a019-dd4312f2b361 | -6.05524 | -57.79112 | 2026-09-06 07:22:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 29f772ef-2e55-3e6d-bf4c-3e31c09b18f9 | -5.13993 | -56.26677 | 2026-09-06 07:22:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| a4a8cae4-52bd-35c0-a172-e5071283b5ed | -7.101 | -56.51542 | 2026-09-06 07:22:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4d889b80-6693-3613-b027-a7e7392121ad | -10.74626 | -60.70327 | 2026-09-06 07:22:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 4152882f-085e-36d0-be29-ed2cb99fcacd | -4.47624 | -55.08681 | 2026-09-06 07:22:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ba1d0448-1fa4-3eb7-aee5-b450a7c8e74b | -5.35118 | -56.03356 | 2026-09-06 07:22:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 878ece2d-0cb0-326b-a845-eb7b6c46083d | -4.466 | -55.09455 | 2026-09-06 07:22:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 98e92c46-bb6a-3a1f-b909-72dbac279f25 | -5.14977 | -55.9647 | 2026-09-06 07:22:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| e90ec169-e874-3af2-bf81-308bed11b24b | -5.14232 | -55.95465 | 2026-09-06 07:22:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7e95bf85-4d0c-3076-9da6-1ae33890c838 | -13.76363 | -51.63654 | 2026-09-06 07:24:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 6d085935-fcb6-32f2-a8de-29ac83c5aadb | -5.3646 | -56.0249 | 2026-09-06 07:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| b2dc97c0-21f1-3673-b02b-b1f058b984e8 | -5.3646 | -56.0249 | 2026-09-06 07:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 373fd009-c3fe-3a1e-a438-385d0a4afa9d | -14.9246 | -44.6744 | 2026-09-06 07:40:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 5e772412-693f-33d0-8dae-c247445fddb1 | -6.876 | -62.9566 | 2026-09-06 07:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 705247e8-7bef-3e1e-9c7b-f8f760d705a3 | -5.3646 | -56.0249 | 2026-09-06 07:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 61fae718-79b7-3df2-bae8-c6499972d63d | -6.8944 | -62.956 | 2026-09-06 07:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 09026630-d45c-3eba-a617-52029d3c5cfa | -6.8944 | -62.9748 | 2026-09-06 08:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 81563a05-928f-3881-a6af-0877f749cc3e | -6.876 | -62.9566 | 2026-09-06 08:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 376df9ab-27d4-3f35-9e08-60e7223fbeb4 | -6.8944 | -62.956 | 2026-09-06 08:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 108.6 |
| cbe66d7f-c377-379e-949e-06fe9209eaa5 | -5.3646 | -56.0249 | 2026-09-06 08:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 60cb02ac-6f09-3acb-93a5-aee68cb3b7cf | -6.8945 | -62.9372 | 2026-09-06 08:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| c063cbe0-0c63-3ab3-a367-bf1a710e2cd1 | -6.8944 | -62.956 | 2026-09-06 08:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| b813d4b3-7070-3533-9f92-6ffdaf42ced9 | -14.9246 | -44.6744 | 2026-09-06 08:10:00 | GOES-19 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 062d8a5e-5e1a-30cb-a594-36b28f9b5cf1 | -5.3646 | -56.0249 | 2026-09-06 08:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 6ce867de-b9ab-307a-9efc-5a8201b33d86 | -6.8945 | -62.9372 | 2026-09-06 08:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 441d449a-06dd-3884-94e9-419f9c690560 | -6.876 | -62.9566 | 2026-09-06 08:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 3b493bca-b21c-3eae-816a-dccdcce50b8a | -6.8944 | -62.9748 | 2026-09-06 08:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 2a80f340-03a3-3a08-a79e-a5ec3b50cfcd | -6.8945 | -62.9372 | 2026-09-06 08:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| a6bb4b08-a174-3217-9285-d4ab06d24445 | -5.3646 | -56.0249 | 2026-09-06 08:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| d89ab2ca-6af8-397e-a5d4-41d6c4b230ad | -6.9128 | -62.9554 | 2026-09-06 08:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 544f1615-717e-3cea-bef0-b9385d6c399b | -6.8944 | -62.956 | 2026-09-06 08:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 186.0 |
| 95d69e0a-59b4-3332-bc7a-7a491977370f | -6.876 | -62.9566 | 2026-09-06 08:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 97805280-32ec-3acc-b4dc-e24dfc1b2170 | -6.8944 | -62.9748 | 2026-09-06 08:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| be252826-2f94-3789-a663-3c5a7fcf1c10 | -6.876 | -62.9566 | 2026-09-06 08:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| f8ac4e2d-b082-3c36-af4a-8143e356ce31 | -5.3646 | -56.0249 | 2026-09-06 08:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| ab3bf668-47c9-3d2f-af87-7ab676542a8c | -6.9128 | -62.9554 | 2026-09-06 08:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 37e7bd94-b3d6-35b4-84b3-77a34a62c40b | -6.8944 | -62.956 | 2026-09-06 08:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 9e12f7d4-1db2-3ac1-a807-bec16ccda86e | -6.8944 | -62.9748 | 2026-09-06 08:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 19516ed8-2abf-3b98-9239-630c94f4b965 | -6.8945 | -62.9372 | 2026-09-06 08:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| b7d8e9e2-31de-34c1-a031-579dc2799c57 | -5.3646 | -56.0249 | 2026-09-06 08:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 665e821c-dcc0-34aa-93e8-9134a6952fdb | -6.8945 | -62.9372 | 2026-09-06 08:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 529b609d-0ad1-3652-ab15-e3e33fa4e984 | -5.3646 | -56.0249 | 2026-09-06 08:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 39870207-0576-33f3-8e9b-304e1519906e | -6.8944 | -62.956 | 2026-09-06 08:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 0a8f7e9d-c1e7-3365-a7a7-b68fe3d3cd87 | -5.3646 | -56.0249 | 2026-09-06 09:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 68cc84d6-9f8a-306a-a8df-a542520fb8c4 | -6.8944 | -62.956 | 2026-09-06 09:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 481a1634-455c-3fa2-be7c-1653a8d8d99c | -6.8944 | -62.956 | 2026-09-06 09:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 252fa072-4c97-3610-9ae6-3a7fa2f959f2 | -5.56743 | -37.8211 | 2026-09-06 11:08:00 | TERRA_M-M | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 5f3998c5-0413-3c6c-8549-fc8b3759a3b0 | -9.3415 | -40.60836 | 2026-09-06 11:10:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.7 |


[Clique aqui para ver as próximas entradas](README35.md)
