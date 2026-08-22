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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 481a3149-8a1f-31bd-b818-d523b00acf0e | -13.44613 | -51.76303 | 2026-08-22 05:23:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fc5a114b-dffa-388c-b05e-59611a07a8e9 | -6.91616 | -59.35633 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0b42a600-0054-3b5b-b8c9-f033e265257a | -14.13918 | -48.06755 | 2026-08-22 05:23:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80e16590-5792-3770-8cef-9e80bdc30444 | -6.78106 | -59.4377 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b238d57-6dd7-3852-ab8d-b7395150b8c1 | -7.05146 | -56.61031 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1c0305a-1b66-3de9-961c-9ebf492c7486 | -6.75776 | -58.65979 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| bd37dcb9-917a-3e11-a88a-47ae05524c8e | -6.76554 | -58.69667 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4aa749cc-8d7c-3a60-bede-911a919318f3 | -8.03139 | -54.00616 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 661b4587-1a06-3166-8db0-2a5241c68b47 | -6.85715 | -59.44979 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fec91b6c-2837-3e3c-a415-0f671ca074f7 | -5.99544 | -57.80288 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d20fce9-0a7a-385a-8823-b46f39d89275 | -7.34363 | -55.67181 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbd231d1-8e99-356d-a8bb-3f3f07cea0c1 | -5.74918 | -53.58653 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbfabbad-4e84-300e-95b7-a2a40c53356a | -6.7987 | -59.4334 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 85c3aa9c-efbf-3cbc-9daf-ad045605922b | -6.01615 | -57.82433 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19145b47-6c39-3ee5-96d4-5d9a6a34d639 | -6.90681 | -47.47486 | 2026-08-22 05:23:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e68ecdb-7988-3755-9dd9-672ff78f0041 | -8.58828 | -54.74473 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6a12cc77-9b58-39d4-b6a1-f1f703d3c5bf | -8.49851 | -54.87074 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 518f0679-5eb2-3329-aca1-e9eb44fdc16a | -8.5873 | -54.72297 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9fa21569-3a8d-3165-ab7d-beb333a6636a | -6.77489 | -58.65891 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 278a5bda-972c-31c3-a5d0-d2e680d46ee5 | -7.53228 | -57.65187 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1c292b1-460f-3713-a064-f4f2a08d195b | -9.87645 | -62.92881 | 2026-08-22 05:23:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9606a653-5f78-37c3-bbdc-c55c82f7bfc5 | -6.09377 | -59.95531 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15799415-c7f4-352f-a374-099f0103b390 | -6.76938 | -58.67231 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 221e231b-5029-3955-a56b-9942bda494fb | -6.88701 | -59.04669 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef1ad1d9-177a-3ffb-87d3-a337056e6650 | -7.36315 | -55.68204 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2cc8d0f5-d2a6-3fa5-8483-7b51aac19f6e | -12.06791 | -56.29256 | 2026-08-22 05:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79485f4a-bc37-36fb-a91e-a7dde6252ac1 | -6.67283 | -58.74619 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7c940f5-beb6-3b65-b004-1e7c3364ea13 | -1.42158 | -55.72336 | 2026-08-22 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3fe5cee4-99fd-39de-9a03-8380ec6cc42d | -6.94698 | -59.31159 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| affe9d39-40cf-302a-ba78-ed18a5bfcd35 | -6.76442 | -58.68224 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 878afa5a-c285-34b2-8c65-e5e537cc3849 | -6.7622 | -58.67476 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b1869b05-fe29-3cd9-9f55-61a86f4b6730 | -6.91285 | -59.35581 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 17bcceb2-f5b2-32a0-bbcb-991ef6f601c4 | -6.77814 | -55.70364 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34e1e3b9-913c-3664-b9f5-c5c70cbf3be4 | -6.76664 | -58.68971 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d11787d-8884-3655-a13f-b59298ea1959 | -6.80806 | -59.41715 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1293d403-d842-3412-a227-9b5778c71f10 | -7.6021 | -60.95673 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e76082c9-b826-3b8f-a888-ca310acae48c | -6.88559 | -56.72703 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a75c227c-23c8-3889-88f2-6e91dd745720 | -8.02139 | -51.80076 | 2026-08-22 05:23:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28ec6960-b4b6-35ca-a4b3-35a307b4b5cf | -9.00584 | -50.75089 | 2026-08-22 05:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d63e9047-959f-3b68-8060-e2e2da2262a0 | -6.67357 | -56.33939 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 085f21f3-c008-3d74-bfca-965c37a43a6f | -6.65577 | -56.33673 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db55f927-e53c-3405-8bef-74edc8474f83 | -7.60025 | -61.18914 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fb5d850-3c47-3c97-853c-25e72f02843b | -6.38967 | -54.94482 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 187f4b6c-d62d-3b52-b563-5c6426629e61 | -6.72235 | -48.115 | 2026-08-22 05:23:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d9ad3596-c7bc-34aa-a9f2-2456450237d7 | -14.13187 | -48.07256 | 2026-08-22 05:23:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e7d04d1-65bb-3306-95d9-adf0c65d6509 | -8.59228 | -54.74528 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7db452d-01bf-34ba-8933-80dd6453fd9b | -14.01441 | -53.70177 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 02856519-b119-3fcd-a655-91147699563e | -5.80442 | -57.54575 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc6ac3a6-f34f-35ca-b01d-24a38898d7c1 | -12.01193 | -53.42852 | 2026-08-22 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 136f3d15-2cf0-373c-8062-9c822e8718e4 | -12.14014 | -63.92415 | 2026-08-22 05:23:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59ca3b41-b5b8-39f0-8bad-174874cbcb42 | -6.77659 | -58.69128 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| fc1474cb-a2d9-3024-9c67-3fcb39dba2eb | -6.20251 | -53.09108 | 2026-08-22 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bc7f594-4c16-3719-aa93-5a72a5961a84 | -6.96069 | -60.14481 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89d82db4-a673-3c24-a682-54001fa02492 | -6.56876 | -58.97502 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f7400ff-22bd-38a0-ab04-08adc76d45e0 | -7.34734 | -55.67237 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d771a037-26da-35a6-a7f2-cd64ba89d3b6 | -6.60755 | -56.36686 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b8672d3-dbf0-32aa-9b2a-db6ee095080a | -14.31819 | -51.86924 | 2026-08-22 05:23:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 123cbf0d-64a8-308b-aade-b4ff81157d12 | -6.26623 | -62.52392 | 2026-08-22 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77edfce1-563c-3c80-9c69-3157b1bcf290 | -6.79042 | -59.42144 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 26cf660c-4579-3ca1-8135-111c50474b60 | -6.55649 | -58.51426 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e79bbe4c-5a5a-385a-9bff-c48a37b65d34 | -6.84114 | -59.4224 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6f98f8b-142f-361f-bc9b-5e720c384bbd | -12.09943 | -56.31664 | 2026-08-22 05:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f4d2cef5-2bc6-3fcb-b419-33579923fa32 | -7.59768 | -60.94113 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb1d3ce7-720b-324d-9940-0d686378e4bc | -14.55831 | -53.00931 | 2026-08-22 05:23:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c373c80a-4c03-3b4e-ab44-45c771b42184 | -8.18696 | -54.97587 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 943dfce4-c49b-3ac5-b4e8-1f3ee3251659 | -6.86209 | -59.41863 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6a73d72-e178-337f-8560-2289686ca4b9 | -13.69174 | -51.85078 | 2026-08-22 05:23:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c96531c-3a84-32e7-b136-9116865fbc96 | -7.68073 | -46.1652 | 2026-08-22 05:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 24a16f6a-1a0a-35ac-b8f2-d03291742441 | -6.96705 | -59.05583 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 82a19fcb-7dbc-358d-a89a-98c414cacfa2 | -6.72189 | -59.46691 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19ef7a54-9a7a-3bb1-b8bb-ac3919f55d5e | -6.79049 | -59.59181 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c3bdf61-9a3b-3ca3-90c1-690c6ccc1898 | -6.80127 | -58.98665 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d50e01e3-5071-37ec-881b-b395fd238b9c | -6.43633 | -54.94691 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce41b8e2-73fc-3cc6-8afe-c54c3078342a | -3.54157 | -48.18159 | 2026-08-22 05:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61be7332-c035-3396-8d9a-6cb98fa0e975 | -8.16928 | -54.98727 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d7b57d7a-a0ba-3b98-be74-1f22d85952d8 | -14.56254 | -53.01537 | 2026-08-22 05:23:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7684b802-9ad4-3985-94da-941135a53c3a | -11.21009 | -54.00078 | 2026-08-22 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46d2a26d-7a5b-3d9f-b466-6673396f961f | -6.82239 | -59.41233 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 68ba5b2a-4c69-35d7-9c4f-fd55ce945496 | -6.5421 | -58.51919 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 2fc70020-463a-3103-b960-438d85701ee6 | -6.80144 | -59.4161 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 2d5b5266-ae3e-3723-81af-c1ababfdcc5d | -6.89726 | -56.43752 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 950ad15e-9636-355d-9453-4240666bda03 | -6.86101 | -59.44685 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee0aae52-8dc7-3daf-afc3-c8b298489bc6 | -6.37817 | -54.94316 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 14ba1b67-e50d-3338-9dd0-be327c1c9d94 | -6.00052 | -57.83644 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f1c7e3f-35bf-32e7-8e8a-c5ea863c913a | -14.12943 | -48.06898 | 2026-08-22 05:23:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a175bb55-fed7-3d8b-b110-1084ee460647 | -6.13378 | -59.89701 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcf9b33d-0f7b-3b07-9ea9-c88aa2200d67 | -6.78601 | -59.42784 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e0fff4b2-f256-3bef-82ed-a9c6e1f6224d | -6.08599 | -59.96127 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53ca057d-1fb5-3041-904c-66b79b95be19 | -7.41604 | -59.99506 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4e52e46-1558-3142-a2ab-addcd9e18a41 | -13.9995 | -53.67026 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 47343b6c-e0f8-301b-b1f9-3f9eb2134f02 | -6.85273 | -59.43489 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a0c6ea6-bdb7-3f1a-b0fd-9cec8a3c8ad6 | -6.00053 | -57.85833 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d15f8945-f4c3-3bf7-97ee-3e204947b87f | -6.817 | -59.66002 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8ee9650e-feb0-313f-ad2c-5650fa3cee74 | -6.00444 | -57.85529 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51959c36-4cef-3f55-a74e-c6e86f369525 | -6.80407 | -59.01192 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6aea3397-bc98-30f6-a673-967b55d78d0e | -4.47002 | -55.39497 | 2026-08-22 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2adfb108-d468-3d90-ba4f-0592cfd5b27e | -6.77228 | -59.14875 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44c55aca-54ae-32d0-a913-1bc03e6bde4e | -6.66877 | -56.34697 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9835a139-1695-37c9-99e8-bd28b826309f | -13.45137 | -51.76376 | 2026-08-22 05:23:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1959f00d-497e-38e1-9f61-80ed378865d9 | -5.75028 | -53.57905 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README70.md)
