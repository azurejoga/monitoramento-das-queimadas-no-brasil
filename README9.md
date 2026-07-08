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
| 51076924-55ae-3ea8-abc7-bdaf7113a34e | -4.83489 | -44.06158 | 2026-07-08 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eba34225-bee1-3871-a381-6a71e7b5f8f7 | -3.5127 | -48.04564 | 2026-07-08 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 30f34cd6-4341-3e38-91d9-c2ead088b722 | -4.28559 | -48.35915 | 2026-07-08 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec2be91b-729d-334c-a05a-1f386b10c25a | -4.34716 | -47.76609 | 2026-07-08 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 31bccf7f-1508-30c7-ba65-f163c35f6e6a | -4.83316 | -44.05962 | 2026-07-08 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3885e14-86da-374d-b873-78abbab290cf | -4.57639 | -48.02827 | 2026-07-08 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2481742-3b7b-31af-8e65-4680d372970d | -3.65997 | -48.96391 | 2026-07-08 04:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e851ddb-2e48-3b16-b3f6-3300ede5f16f | -3.51369 | -48.04387 | 2026-07-08 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e84ebca0-7bc5-3f18-8b16-8e6fff6f4c2b | -4.26009 | -48.61321 | 2026-07-08 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a45c175-a442-3001-9fc9-dfa84cbaa995 | -5.47962 | -44.10334 | 2026-07-08 04:04:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| babf8227-b39a-324f-91a7-6059a592480b | -3.50798 | -48.04287 | 2026-07-08 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e8bfaae-952a-3450-b5a2-e762010acedd | -2.98326 | -48.59816 | 2026-07-08 04:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94929ee4-e595-391d-9080-34fd66e93718 | -4.34653 | -47.76968 | 2026-07-08 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d8ce72b4-75d2-3486-b4a6-6bb232597345 | -2.98402 | -48.59377 | 2026-07-08 04:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9683baf1-9ed3-3ff3-96a0-06e4696f857c | -4.34161 | -47.76515 | 2026-07-08 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 317516bf-9a53-3d15-bb39-857d80f7d921 | -5.33422 | -44.71184 | 2026-07-08 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d1e4aef4-edf2-3a05-85c4-573aee21ea14 | -5.47986 | -44.07531 | 2026-07-08 04:04:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c94043dd-1ad6-3f06-a021-0436271438e1 | -9.22581 | -48.57743 | 2026-07-08 04:06:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d790d87f-3cb8-3a18-9b49-23ea279522a9 | -5.80028 | -43.6339 | 2026-07-08 04:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d404fc0-7fcf-372d-a259-1c2f35b8ba21 | -6.64374 | -43.90974 | 2026-07-08 04:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8374e2c3-7541-32c3-9061-d86441f47048 | -9.2201 | -48.58614 | 2026-07-08 04:06:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c5949f62-73fd-3a58-9919-5a05485135ff | -9.3339 | -47.91843 | 2026-07-08 04:06:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc47b469-eb42-363c-8ad3-720f541bb913 | -5.3428 | -45.35657 | 2026-07-08 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2465f1a7-2c0f-34e7-9c0a-381f2223be9c | -5.66897 | -44.30339 | 2026-07-08 04:06:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4056734b-0b93-31b5-b9d3-5bf4ff3adbf5 | -9.84767 | -38.9632 | 2026-07-08 04:06:00 | NPP-375D | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| ec807b7c-28c2-3419-b4b1-3a47955b6c13 | -9.36477 | -48.80969 | 2026-07-08 04:06:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5fa1dbc-f918-376d-8c4d-695064a45780 | -11.12502 | -38.62807 | 2026-07-08 04:06:00 | NPP-375D | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2fe2db06-c783-3310-9430-8f73d666da07 | -5.65834 | -44.31388 | 2026-07-08 04:06:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| bad65685-7e61-321b-806b-60586f9ad60b | -9.21469 | -48.58526 | 2026-07-08 04:06:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9d1bf59a-3b68-3aa6-9730-f3f45903ca81 | -5.80661 | -43.79737 | 2026-07-08 04:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ccb1c31-504b-31b1-9d9f-ab171aac6220 | -6.91171 | -43.7023 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 857e5265-e4a5-3ae9-94c9-604e39544996 | -10.94075 | -43.05224 | 2026-07-08 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 192f9a52-a475-378f-b4b1-0f62f09dcf54 | -5.79646 | -43.80724 | 2026-07-08 04:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b6faa43-e9c5-33fc-a6f6-6ffd36511b62 | -9.37103 | -44.72844 | 2026-07-08 04:06:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53f0919e-ed41-3152-8ef3-71f954684d75 | -7.63994 | -50.0196 | 2026-07-08 04:06:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9bc32850-4b45-3831-ba5d-ebe7a2c30da6 | -10.92681 | -43.0453 | 2026-07-08 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1f381200-1742-32af-8ad8-071dde3926b8 | -6.93593 | -43.70649 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93421069-7756-3fe7-a217-77bf4c739c43 | -10.92828 | -43.05902 | 2026-07-08 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03de6f5e-c566-3001-9d59-dbb1d4aa834f | -5.98234 | -43.61943 | 2026-07-08 04:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e28e4d5f-4b28-3295-b212-cf6a22c0ec5a | -6.89839 | -43.70736 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f439b69-f02e-3aa0-aaa4-3d01c6255d0b | -9.33445 | -47.91538 | 2026-07-08 04:06:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbc2320e-5a56-38c7-b6d3-4d33557d1b67 | -7.2582 | -45.10854 | 2026-07-08 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15b1fa59-8aba-398a-8c9a-0c19822f4053 | -7.40882 | -49.77471 | 2026-07-08 04:06:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 29ff1a20-54e6-32c1-8d54-575f0fee651f | -9.335 | -47.91233 | 2026-07-08 04:06:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c60af0b5-7cca-31d0-982a-7517e7f0d410 | -10.94441 | -43.05289 | 2026-07-08 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4b7a52bc-b5b9-3d9a-81ea-db91045ec536 | -9.23189 | -50.14478 | 2026-07-08 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9e606e8-f546-32ff-bfd1-dba4824256f1 | -6.95906 | -42.06879 | 2026-07-08 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 78de180f-9367-36b0-a10b-a4a110659411 | -6.9417 | -43.6967 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 024cc6f3-0573-386f-9801-363afef1cbc0 | -6.92264 | -43.71145 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71076309-872b-3973-ad9d-a66905e265e1 | -7.64514 | -50.02546 | 2026-07-08 04:06:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee656ea6-7b5e-31d0-bd9d-4e251b206c5d | -6.92382 | -43.70442 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b92bee0-aa48-3f80-9d87-b030fc453010 | -5.66115 | -44.31175 | 2026-07-08 04:06:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e4047035-0785-3b3b-ba58-af1e663be023 | -5.80185 | -43.80045 | 2026-07-08 04:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26e9cee6-3a8c-309a-b9b0-40adb96747b3 | -6.9443 | -43.70885 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e824566-431a-38d8-8777-b60d3085cda7 | -6.90244 | -43.70802 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10e20b90-1b7e-3bff-88c5-bb6002b30586 | -6.94458 | -43.70442 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 00b56fca-ca0a-3a34-8568-a3185cd4a9f0 | -10.03684 | -49.6282 | 2026-07-08 04:06:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c49f74a-49cc-3be4-ac8b-f228b528d339 | -6.93651 | -43.70297 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d77356fa-f3e3-31e4-85f7-7629edb322aa | -9.22205 | -48.57585 | 2026-07-08 04:06:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0f03f51a-fcf5-3ae7-a81b-879c5be1a05c | -9.22735 | -48.57725 | 2026-07-08 04:06:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 191dddfc-d03c-3008-a0f8-8d7eaea82997 | -5.66468 | -44.30267 | 2026-07-08 04:06:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f446aea1-52fb-325c-be72-0d8edec7d351 | -5.79771 | -43.79977 | 2026-07-08 04:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb87de56-29ef-3a48-aeb6-16b88bca412f | -9.37455 | -44.71688 | 2026-07-08 04:06:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 598e1627-3d4a-32d5-9621-5b35fc748d39 | -6.84978 | -50.65251 | 2026-07-08 04:06:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7da1c28b-e0e5-37bb-9320-8e22b3913274 | -9.21923 | -48.58296 | 2026-07-08 04:06:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a06c1d26-d245-3860-b162-e76623da5439 | -9.22075 | -48.5827 | 2026-07-08 04:06:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3ce6eb5a-c5d3-39de-8156-fd5795af0fed | -7.00762 | -42.77548 | 2026-07-08 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 301daea8-f526-329d-b4f4-7e90dc687666 | -7.00842 | -42.77078 | 2026-07-08 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e4a4d6a2-7ee1-3842-a3d6-2eec4bb37119 | -8.11817 | -47.88455 | 2026-07-08 04:06:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9ff88961-a955-335d-ab56-a1e2ac8bc722 | -6.94611 | -43.69833 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6199f579-470b-39bf-a9ec-5fb1fa179280 | -9.56796 | -49.11229 | 2026-07-08 04:06:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 122a2588-059b-396b-b7c3-55d3283b6197 | -8.04373 | -37.73489 | 2026-07-08 04:06:00 | NPP-375D | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 16c41d62-8b88-31d9-85b1-ffc28e7feb33 | -8.59676 | -48.00611 | 2026-07-08 04:06:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a176f609-0693-3c9d-a097-360a33be63a6 | -6.90708 | -43.70514 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2d375e0b-c663-34f7-8295-60d46950a6da | -6.90635 | -44.90743 | 2026-07-08 04:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 579671dd-8f2f-366a-a53e-f52cf2687350 | -7.6391 | -50.0242 | 2026-07-08 04:06:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| feddc765-b7be-3540-837c-5f7abb1b90ad | -9.56867 | -49.10859 | 2026-07-08 04:06:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be457d81-0469-3e8a-b5c9-25ea48b070c3 | -9.23398 | -50.152 | 2026-07-08 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70896957-5b1d-31aa-bb47-5c8f6b6621cd | -8.59735 | -48.00288 | 2026-07-08 04:06:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce53d51c-178f-3064-bd1c-e1484ac56acc | -7.01365 | -42.78614 | 2026-07-08 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 21aaa3cc-cb73-383a-a370-f0ec8fc447bc | -9.74245 | -49.03196 | 2026-07-08 04:06:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43367e44-b325-3d4d-8b6d-4d0f9c1f7c5a | -9.37323 | -44.72433 | 2026-07-08 04:06:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 98dbdbaf-e3ae-3494-a494-56b6033104f7 | -8.4508 | -45.82904 | 2026-07-08 04:06:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37e1772c-22ae-37db-b1de-77af71c27d80 | -9.21795 | -48.59002 | 2026-07-08 04:06:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 22a796b9-a17e-3c6c-9fde-c93aa72e6dc1 | -11.04651 | -45.82865 | 2026-07-08 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a169c441-9284-3895-9134-4785ad70fccf | -9.37167 | -44.7247 | 2026-07-08 04:06:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3c37059-39ce-3a3b-a710-240a27ebd39a | -5.46532 | -45.42719 | 2026-07-08 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1bd5bb3-ee9e-37a9-89af-af9f794a3793 | -4.94632 | -48.24976 | 2026-07-08 04:06:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2347f464-fd3c-3701-8c9a-e9b2201d4ede | -6.91397 | -43.7136 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a90a4b7c-1cde-3408-b592-4234ea7420e4 | -6.94112 | -43.7002 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7a9b195-2f94-31ad-921c-108f464906ed | -6.90304 | -43.70447 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6f47c1f5-bd2a-3992-a4da-a1ab93f2fa34 | -5.66311 | -44.29982 | 2026-07-08 04:06:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 791d41f5-c553-3e7b-81a0-856c1b8f78ab | -9.74176 | -49.03564 | 2026-07-08 04:06:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fef20007-e789-37e4-9771-3334c4b89b50 | -8.12471 | -47.1054 | 2026-07-08 04:06:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 8d822865-8d20-3da2-81da-d6ce24aa8d18 | -7.08753 | -41.35324 | 2026-07-08 04:06:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 47c94c5d-0fc7-3e7e-a6cb-101074971e65 | -6.92205 | -43.71499 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| babdf7cb-5186-316d-ac27-e839eb2ac702 | -9.3723 | -44.72097 | 2026-07-08 04:06:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 502b1208-df22-354c-a1c3-c80a9bf88a57 | -5.30757 | -47.24326 | 2026-07-08 04:06:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b5a54a4-12a3-3595-b0c1-dcbbb7372f75 | -6.64723 | -43.91409 | 2026-07-08 04:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbbf468f-aead-33f1-90d8-1d524b29a4e5 | -7.2975 | -46.2453 | 2026-07-08 04:06:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README10.md)
