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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 491e2829-4305-3f64-8ac1-a531e3155c32 | -5.9362 | -43.34108 | 2024-09-28 00:26:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7876904e-b5c8-332e-b0eb-775423161373 | -5.89014 | -42.78662 | 2024-09-28 00:26:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| ea00c9c2-ba28-3f8f-b25d-1b2511a7f2a8 | -5.83516 | -43.66295 | 2024-09-28 00:26:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f0bc2cfa-6d15-3273-99f8-bb8dbdaefc83 | -5.83367 | -43.652 | 2024-09-28 00:26:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| ad84c7da-97f7-36ee-ac03-eb1a161a1202 | -5.80673 | -43.98107 | 2024-09-28 00:26:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 207154ea-3d29-3571-98dc-3112d49a2f6a | -5.71931 | -43.9351 | 2024-09-28 00:26:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| decf6e98-379f-3eae-95c5-de96a4a9cd35 | -5.70762 | -43.15247 | 2024-09-28 00:26:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 8129ce94-3ef5-33c7-a0f2-dd9f1952c903 | -5.702 | -43.14898 | 2024-09-28 00:26:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 12.2 |
| eb7f5c4c-7c87-330d-a587-3ad90c038fdd | -5.31626 | -39.78054 | 2024-09-28 00:26:00 | TERRA_M-M | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| ca77f088-10e9-34e8-a570-425c544fd3bd | -5.30406 | -43.07318 | 2024-09-28 00:26:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0a1dfce1-b29a-3ba3-8f8c-c1e0830db2d6 | -5.2289 | -42.73256 | 2024-09-28 00:26:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| e480637b-399b-306d-a950-a634a0c2d7e7 | -5.17645 | -37.98227 | 2024-09-28 00:26:00 | TERRA_M-M | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 048b6ebd-cd02-3a0e-bec1-c6d161f094ed | -5.14078 | -42.89971 | 2024-09-28 00:26:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| d2d290a9-bc30-3ac1-9749-1532337a3544 | -5.13945 | -42.8899 | 2024-09-28 00:26:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| aef49b4c-b499-3ae4-a4bc-6c77d6cf7575 | -5.07746 | -37.72832 | 2024-09-28 00:26:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 0af52fd6-0c44-3245-8297-306b48c34318 | -5.0758 | -37.71688 | 2024-09-28 00:26:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 6.0 |
| c625a932-877d-399d-bbf6-cc092b3ae2a4 | -5.06748 | -37.72979 | 2024-09-28 00:26:00 | TERRA_M-M | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 31.5 |
| 260ef9f4-28bf-3053-976a-59aa2e234ba1 | -5.06581 | -37.71835 | 2024-09-28 00:26:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 13.4 |
| f89fd938-98b8-36a9-b7fd-0e5c24e70816 | -4.73899 | -43.25999 | 2024-09-28 00:26:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 787b921f-302a-3a1a-8c4d-b2f945750484 | -4.73762 | -43.24991 | 2024-09-28 00:26:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 03154a1d-7d6b-3bc8-825a-2a17b04397de | -4.44453 | -43.05496 | 2024-09-28 00:26:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a2b5fa8d-f76e-3d5c-83b2-f2965b873454 | -4.25745 | -43.03323 | 2024-09-28 00:26:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 301dc105-081b-3cb7-88d9-970357ce9210 | -4.0291 | -43.24371 | 2024-09-28 00:26:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 05a3e1a7-f9e7-33e6-9b41-f18a114eb5cf | -4.02773 | -43.23383 | 2024-09-28 00:26:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cf4070b7-b6a7-381b-85b7-f50ed2116385 | -3.92125 | -42.26578 | 2024-09-28 00:26:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 7a29d6c6-3ed4-3b54-a80c-f77888985378 | -3.51603 | -43.06657 | 2024-09-28 00:26:00 | TERRA_M-M | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 894f492a-3cd9-35ac-9a15-0be896bb1637 | -3.30266 | -43.52554 | 2024-09-28 00:26:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 36db528c-36e3-394e-b2db-52dcd4f86e95 | -3.30128 | -43.5155 | 2024-09-28 00:26:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7cfe4f2b-d47c-3d02-a14e-dd620454506d | -3.25656 | -43.05275 | 2024-09-28 00:26:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 476de7f6-282a-3859-a744-b8de409e10d9 | -7.21022 | -42.48302 | 2024-09-28 00:26:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 7f655c67-9b43-39d6-8d5b-6e4e1dccf8e0 | -8.75196 | -49.80395 | 2024-09-28 00:26:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 54035443-d610-31ed-9cbb-af9cfeb13e45 | -8.55524 | -49.59621 | 2024-09-28 00:26:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| ba858941-25c0-3d54-bddf-cf6d8519b087 | -8.5503 | -49.62472 | 2024-09-28 00:26:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| e7e31653-45fd-38db-b9d3-4a7b3ed365e8 | -8.23981 | -49.37777 | 2024-09-28 00:26:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| c34e2354-4b96-33d2-95f2-b2f9ac5d31cf | -8.23703 | -49.40664 | 2024-09-28 00:26:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 0d764407-6409-39d6-8cbc-c99047d13748 | -8.23314 | -49.37304 | 2024-09-28 00:26:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| e365d027-0c87-32cb-b4a9-ff40907fae68 | -7.81951 | -45.55007 | 2024-09-28 00:26:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 3ebf7961-32f7-317f-8883-1a891e3d05ca | -7.81754 | -45.53485 | 2024-09-28 00:26:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 7fc0b6f5-8a98-3a1a-b6af-bf4341cb565c | -7.565 | -45.79972 | 2024-09-28 00:26:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 77d28abe-3f42-3046-b927-db95ca6036fc | -7.5157 | -45.7894 | 2024-09-28 00:26:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| c34ed28a-bc8f-3360-9e7d-8e95a77c67dd | -7.48517 | -47.55176 | 2024-09-28 00:26:00 | TERRA_M-M | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 91e80397-d4df-3b8a-a996-95c3c8bc2353 | -7.47772 | -47.55817 | 2024-09-28 00:26:00 | TERRA_M-M | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| abc29436-9581-35c0-904f-77665ffdbcce | -7.41284 | -47.18268 | 2024-09-28 00:26:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 71a30696-645e-3520-b613-bf3d8c5c10e0 | -7.31239 | -46.6874 | 2024-09-28 00:26:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 2a47fdcb-44cf-3306-a317-2e8cc46eb716 | -7.30994 | -46.66817 | 2024-09-28 00:26:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e544e5aa-5009-3e5e-9d1d-0a48f6d73853 | -7.2857 | -46.14718 | 2024-09-28 00:26:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 608a37c0-e6b6-3195-b80d-ea10ec80b733 | -7.27389 | -44.96638 | 2024-09-28 00:26:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 91b6688e-f097-39bf-84fe-39180b679320 | -7.26485 | -46.61502 | 2024-09-28 00:26:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 54afb81b-4039-300f-bc38-7f632b050825 | -7.26377 | -46.62183 | 2024-09-28 00:26:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 5e985f75-0836-3050-b804-07d86e2f8b45 | -7.25579 | -46.85823 | 2024-09-28 00:26:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 5b6b05fa-cfa4-3703-afaf-ec14a9491ca3 | -7.15247 | -45.44293 | 2024-09-28 00:26:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| a33de4f5-8082-3a08-ba4c-48294669e382 | -7.01359 | -45.34428 | 2024-09-28 00:26:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a6b72f16-6ce6-3c0c-8cdc-c5cca8fd6570 | -6.6466 | -44.71145 | 2024-09-28 00:26:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 455b6b13-ce44-3737-8c16-d455957ef89a | -6.64248 | -44.7183 | 2024-09-28 00:26:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3f32fcb3-9166-35d3-b1cd-3d73958090c7 | -6.64073 | -44.70536 | 2024-09-28 00:26:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3e720581-4f70-3e4b-8110-3654e94fc9ef | -6.607 | -45.72847 | 2024-09-28 00:26:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 237b0f37-1a10-348d-a340-8b75895d4806 | -6.60584 | -45.73858 | 2024-09-28 00:26:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 8f990eac-80da-3a8a-9e89-73d472abb23d | -6.60377 | -45.72233 | 2024-09-28 00:26:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| a37b5be1-abfd-36f8-8e78-cf067ba7bc1c | -6.59547 | -45.7302 | 2024-09-28 00:26:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 21ae0984-261d-3bd3-a370-8f57cd219c36 | -6.59224 | -45.72402 | 2024-09-28 00:26:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 8e4973d4-ce60-338c-af27-f2c3020ba931 | -6.58824 | -44.17879 | 2024-09-28 00:26:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| a1919982-c8f9-35e0-84fd-aab35a070147 | -6.58391 | -45.73166 | 2024-09-28 00:26:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 3d6c913c-1b9c-3af8-89e4-e603a6db3377 | -6.5818 | -45.71582 | 2024-09-28 00:26:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| ed7286b6-d181-357a-8460-7476b07c0fe6 | -6.5807 | -44.18607 | 2024-09-28 00:26:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| aa2a2be7-3bb0-340a-8af1-6692145c9bc1 | -6.57902 | -44.17383 | 2024-09-28 00:26:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 61973498-c362-3d7c-9009-72163ab294e0 | -6.57797 | -44.17998 | 2024-09-28 00:26:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 981332e8-6ee2-3657-9b56-ac0e6dbfdb60 | -6.57638 | -44.16776 | 2024-09-28 00:26:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 20d2f9b9-23be-3dcf-9156-c2f99698164a | -6.56876 | -44.17505 | 2024-09-28 00:26:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 0f1a2db5-7ff8-325f-9adb-78985dad921e | -6.3924 | -44.79029 | 2024-09-28 00:26:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e526883b-6679-33be-8810-2ededb9bc00e | -6.38668 | -44.78333 | 2024-09-28 00:26:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f87c1e77-3fb8-3d44-af18-f53806ac8022 | -6.17781 | -45.44016 | 2024-09-28 00:26:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 34.3 |
| ff0a76b4-082a-3937-b55a-da0c874fd808 | -6.17586 | -45.42566 | 2024-09-28 00:26:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 78ea2cb0-dbc6-31a6-9b45-eed2747bac20 | -6.16664 | -45.44191 | 2024-09-28 00:26:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 54cd682b-1aac-3e7b-9d76-92c08617c38a | -6.12071 | -47.2701 | 2024-09-28 00:26:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 8dbae67c-e8c8-3aa5-baab-2401442be624 | -6.10559 | -44.70141 | 2024-09-28 00:26:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 58163daa-04ef-3881-8cf7-5c628759911f | -6.10068 | -44.70847 | 2024-09-28 00:26:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 0ea06508-5f34-31be-9ef0-bbbb78e43441 | -6.09502 | -44.70284 | 2024-09-28 00:26:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7cece4c3-a6b2-33f3-aeb2-5ba297fdf1a6 | -5.98564 | -44.56812 | 2024-09-28 00:26:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| a925aa21-564a-3dcc-8b24-8a429d4b0611 | -5.97989 | -44.57458 | 2024-09-28 00:26:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| b5f7e513-6455-3e11-a90a-0a179ae05b72 | -5.97819 | -44.5621 | 2024-09-28 00:26:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 97f78922-97a4-39d9-b7f2-210b6ad489ee | -5.97272 | -47.13739 | 2024-09-28 00:26:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| e8d8c91c-773a-3dc6-9f70-fabbc7f0c817 | -5.97201 | -47.132 | 2024-09-28 00:26:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 5b213cce-9de9-320c-8cfc-347a328eced5 | -5.94895 | -46.56193 | 2024-09-28 00:26:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a6ecf288-9e7b-3327-80ef-9efd959841f7 | -5.94707 | -49.21999 | 2024-09-28 00:26:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| f201460b-a11d-38a4-b03f-3a1e368c1be3 | -5.94484 | -49.21379 | 2024-09-28 00:26:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 6885a1dc-ba6c-3d8b-9ce3-b984dcca4e31 | -5.94328 | -49.19094 | 2024-09-28 00:26:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 4baf1820-03cb-396c-9a45-34d4999bf680 | -5.94126 | -49.18472 | 2024-09-28 00:26:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 7e81387c-525b-39eb-9608-b616d4f2b379 | -5.79707 | -44.13583 | 2024-09-28 00:26:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 0af982fd-f36f-3b5f-87db-822286bb8575 | -5.79176 | -44.86071 | 2024-09-28 00:26:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 03406c3a-ac39-3bd1-8230-2371809b35e4 | -5.79001 | -44.84759 | 2024-09-28 00:26:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6906c781-506a-3835-b861-d226c367678d | -5.7719 | -44.4749 | 2024-09-28 00:26:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| e9cc48f0-c4ef-3b9c-95ce-9418222545a7 | -5.77031 | -45.56474 | 2024-09-28 00:26:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 2b3a5751-fa2c-33bf-88e9-96d9678dcf5c | -5.77023 | -44.4626 | 2024-09-28 00:26:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 14d350d1-eba1-38f5-b5f1-1144e271d55a | -5.76838 | -45.54992 | 2024-09-28 00:26:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 8fdd31d4-4a92-31a7-a77d-4927749ec740 | -5.76645 | -45.53513 | 2024-09-28 00:26:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 28ec001b-9ead-375e-bcfc-2e970f9a4b37 | -5.76155 | -44.47624 | 2024-09-28 00:26:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c015ecce-d5f7-3267-bd47-f56b2bdf6269 | -5.7599 | -44.46401 | 2024-09-28 00:26:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 001be47a-cc77-304b-a169-6d4a334a64cc | -5.75566 | -47.07748 | 2024-09-28 00:26:00 | TERRA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 08a86233-788d-3a2f-9566-85dfd3ff52fa | -5.71572 | -46.46277 | 2024-09-28 00:26:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| dc45f750-756c-3ea4-8329-0b70bd3e365f | -5.7148 | -44.81094 | 2024-09-28 00:26:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |


[Clique aqui para ver as próximas entradas](README15.md)
