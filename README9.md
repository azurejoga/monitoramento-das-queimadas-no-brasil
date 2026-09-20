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
| c55ba835-2b19-3fda-a07a-60649e2aabfd | -11.2307 | -54.078 | 2026-09-20 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 151db3c3-f894-3011-bb7a-f0bdc3ec4481 | -6.3133 | -47.648 | 2026-09-20 02:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 20fbfe16-a160-3cd7-a739-953470dc5bdb | -11.8735 | -47.6793 | 2026-09-20 02:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 80e0faa7-1e2c-34c8-823a-8f13dd2c09df | -6.3134 | -47.6261 | 2026-09-20 02:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 158.7 |
| a714f7ad-8846-3de1-87b3-2b82fe57105d | -9.2603 | -45.939 | 2026-09-20 02:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 2f74b66d-e10a-3718-a3af-da45c4b32e87 | -11.0802 | -54.0302 | 2026-09-20 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 1ed5e6dc-bb71-3b76-96b6-e0c2873e87ca | -6.295 | -47.6055 | 2026-09-20 02:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 127.1 |
| a6012f7c-7bff-340e-a181-bdd323730d31 | -11.8547 | -47.6596 | 2026-09-20 02:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| c580bc5c-406d-310c-b5e1-b03b1d8b884f | -7.5334 | -45.4367 | 2026-09-20 02:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 514d7d9c-630d-38e8-a65d-ec467ac30316 | -11.3793 | -51.3989 | 2026-09-20 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 97f26e8e-7c46-33c8-aecb-90a0db62afdc | -10.9308 | -61.4128 | 2026-09-20 02:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 98585428-282d-398a-b97d-c36c9e2ade65 | -11.118 | -54.0268 | 2026-09-20 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 36291280-c405-3980-a5b9-382ee5ad2962 | -3.7454 | -51.8082 | 2026-09-20 02:50:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 5229428e-a5fb-301d-9063-c7a2a07f909b | -13.037 | -46.9096 | 2026-09-20 02:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 149.3 |
| be4ad62c-dc3c-312c-a481-192b0bbb38fb | -10.2787 | -50.2605 | 2026-09-20 02:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 771f6b48-54b3-3862-aa6b-0d8897317b8f | -13.0366 | -46.9322 | 2026-09-20 02:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| bb09dd7a-a703-3501-bab0-87111c6e7703 | -6.3136 | -47.6042 | 2026-09-20 02:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 87d455e1-0950-3bb4-86f6-136e42cde4fa | -2.8791 | -57.8184 | 2026-09-20 02:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 4da046df-c21d-3e1a-aabc-9da0bf3b0046 | -7.5522 | -45.435 | 2026-09-20 02:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 0013efd6-7827-3a6e-bafa-f3b9f336ffbc | -11.8739 | -47.657 | 2026-09-20 02:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 0d89efc1-af7e-32a0-abd4-3166da842b8b | -14.7051 | -46.6852 | 2026-09-20 02:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 9db55135-e958-3fb0-9f61-de103cd9bdcd | -7.5337 | -45.4141 | 2026-09-20 02:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| f67ebbeb-9c3a-3416-ab17-92ae29f0542a | -8.8097 | -60.7926 | 2026-09-20 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 4e0a6f74-0ca4-3d61-9858-6277092cddfe | -11.8544 | -47.6819 | 2026-09-20 02:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 223d77f8-8c9a-30cb-b9dc-9b693fa9518f | -11.0991 | -54.0285 | 2026-09-20 02:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 155.5 |
| ca09cee2-ea9b-3e78-97da-3e604858c955 | -7.5525 | -45.4123 | 2026-09-20 02:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 2b6dd4c4-c194-3011-81d4-25604b1ac362 | -3.7453 | -51.8288 | 2026-09-20 02:50:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 604d54d2-4589-325f-a34e-eb55ef708ce2 | -8.1686 | -54.7634 | 2026-09-20 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 14b3d077-a3b0-38f9-bd38-8228666081b0 | -8.7546 | -48.6669 | 2026-09-20 02:50:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 65.6 |
| e11fd626-9829-37da-ae41-92db9184dcef | -2.8974 | -57.8181 | 2026-09-20 02:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 948ec22f-1149-3a14-bcbc-7da7e14078c3 | -13.0177 | -46.9125 | 2026-09-20 02:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| ab15211a-e746-3c0e-80b4-b91d037e6273 | -5.8408 | -53.5408 | 2026-09-20 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| a44b5e94-c08f-3248-835f-4df92154888d | -14.6856 | -46.6886 | 2026-09-20 02:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 122.1 |
| ded7458c-13df-399c-a8d4-4077f40f6425 | -6.2948 | -47.6274 | 2026-09-20 02:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 160.8 |
| b8669765-5b08-3bdc-a2f5-b678b0280b80 | -5.92837 | -35.62492 | 2026-09-20 02:58:00 | NOAA-20 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 4.6 |
| ae56c0ff-f352-3ae5-b340-cb4edf12f144 | -13.0177 | -46.9125 | 2026-09-20 03:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 094fd61f-9569-3cd4-922a-680c5f753f0e | -11.0991 | -54.0285 | 2026-09-20 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 149.4 |
| ccba4489-20f0-346b-a4d7-d689a33c7687 | -3.7454 | -51.8082 | 2026-09-20 03:00:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| c4278ab1-26fd-3f74-b0ca-4c353b41b976 | -7.5525 | -45.4123 | 2026-09-20 03:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 95ff0909-3799-3436-931b-936a94089caf | -7.5522 | -45.435 | 2026-09-20 03:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 5f022a02-d018-384e-b4e7-8f9713916681 | -11.118 | -54.0268 | 2026-09-20 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 5d4b826e-fd3b-3973-a01c-568246ba5d20 | -11.8739 | -47.657 | 2026-09-20 03:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 0c74f280-8b9c-3df5-bde4-729729297dd6 | -11.8544 | -47.6819 | 2026-09-20 03:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 6cc8fd5d-d40c-34e8-8187-726b548a2191 | -17.9645 | -50.332 | 2026-09-20 03:00:00 | GOES-19 | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| e4d02d5e-c35f-369d-906e-74fdd35d2b33 | -2.8791 | -57.799 | 2026-09-20 03:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 11445d48-e3ce-3008-98ff-8720b01ea3d3 | -6.295 | -47.6055 | 2026-09-20 03:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 0a028540-a098-36eb-b228-ab488bb08aad | -8.7734 | -48.6651 | 2026-09-20 03:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 66.0 |
| a1ed19d4-3603-3177-9596-879c4ab0a37f | -13.037 | -46.9096 | 2026-09-20 03:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| d2506190-8333-35dd-a18f-adb344b1ac79 | -6.2946 | -47.6493 | 2026-09-20 03:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 8d8ca0b1-3048-3676-b58f-53b512739b39 | -3.7453 | -51.8288 | 2026-09-20 03:00:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 40338496-9d88-30d5-afc4-6f4c25fd2802 | -10.2787 | -50.2605 | 2026-09-20 03:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 37bbaf4c-9132-3ca0-badd-2840c2c965ac | -6.3134 | -47.6261 | 2026-09-20 03:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 338.9 |
| 9d484c89-ed41-3e62-b50a-d4c9e27ea119 | -2.8791 | -57.8184 | 2026-09-20 03:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 1c12f525-128c-39b5-b146-6a24cb9a3457 | -11.2307 | -54.078 | 2026-09-20 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| f5d40bff-d11a-309c-aed8-88bc1061510f | -11.8547 | -47.6596 | 2026-09-20 03:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| ce04f6ea-278e-3c69-9dc8-09237ed1ccd4 | -6.3136 | -47.6042 | 2026-09-20 03:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 32c3cb99-442b-3c59-83af-5d5117737fc2 | -2.6125 | -54.7577 | 2026-09-20 03:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 9706ed1c-439b-380f-a4ce-5413b194bf08 | -12.7629 | -46.1343 | 2026-09-20 03:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 2123eea5-64ad-3ffa-93c3-5a724646c018 | -9.2603 | -45.939 | 2026-09-20 03:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 85f17e97-dc52-3353-bdef-a4aaf919ec49 | -11.0802 | -54.0302 | 2026-09-20 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 0e4d3ff2-7cad-3876-8c44-8241d3d2120e | -14.6856 | -46.6886 | 2026-09-20 03:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 76.0 |
| dd344877-4e78-30be-9011-ff69fa3ac196 | -9.131 | -45.7273 | 2026-09-20 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 3a1af294-217e-3af2-9fef-a2f184820efd | -17.964 | -50.3543 | 2026-09-20 03:00:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 108.2 |
| c6539a4e-7c46-3b3d-8a59-62cb8349e34b | -7.5334 | -45.4367 | 2026-09-20 03:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 149.5 |
| dea6ef36-63ba-3edf-bc5e-ecb21c8c5704 | -6.3133 | -47.648 | 2026-09-20 03:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 67bbbdfd-f73b-3bad-b0bd-80a278b44ae0 | -6.2948 | -47.6274 | 2026-09-20 03:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 282.0 |
| ed0678b5-98ed-3f32-82e2-d8693908413a | -11.8547 | -47.6596 | 2026-09-20 03:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 7df39e89-109e-3f35-8efb-2a21f7b177e3 | -2.8974 | -57.8181 | 2026-09-20 03:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 9a68167c-2fcb-325d-be0f-0fbae1527154 | -14.6856 | -46.6886 | 2026-09-20 03:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 23ab2a62-12c8-39b7-9ea6-40e4ba3e7490 | -6.295 | -47.6055 | 2026-09-20 03:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 386af0b6-d7c8-3684-b485-0d5461897494 | -2.8791 | -57.8184 | 2026-09-20 03:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 6727b256-0af2-35b9-88a4-ce3ece5f466a | -6.3133 | -47.648 | 2026-09-20 03:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 7c077b87-f999-3772-8115-4aeda4c9428c | -7.5525 | -45.4123 | 2026-09-20 03:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 2333b0f3-9e82-3979-a802-1a197979d622 | -11.2307 | -54.078 | 2026-09-20 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 3b902dc3-7644-3eab-931a-e96006f49640 | -7.5522 | -45.435 | 2026-09-20 03:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 5c894f8d-e3ab-3815-97a8-a0ffe7dbd462 | -3.7453 | -51.8288 | 2026-09-20 03:10:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| a3b07785-6ad9-339f-ab4e-b9505a401d5b | -2.6125 | -54.7577 | 2026-09-20 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| be1d2938-25c7-3e5f-b81b-73fd442592d6 | -6.2948 | -47.6274 | 2026-09-20 03:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 1358e419-8029-3e14-9bbd-41bf74b42dbe | -13.037 | -46.9096 | 2026-09-20 03:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 35488cac-99e1-3cb2-9261-d181ad909963 | -8.7734 | -48.6651 | 2026-09-20 03:10:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 66.1 |
| a578ebf2-1b32-380e-a3ab-72b54f246675 | -9.2567 | -46.2098 | 2026-09-20 03:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| a6ad1b41-899d-31b1-80a8-83e5c97b4ff7 | -10.2787 | -50.2605 | 2026-09-20 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| e1920ee9-22c6-3d4f-8322-d4e737716fbc | -11.0802 | -54.0302 | 2026-09-20 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| cd105706-d22b-3a6b-8999-d616e8616f51 | -6.3321 | -47.6248 | 2026-09-20 03:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| f8a07549-fd06-3bb9-85c8-9ea5bc5c8884 | -6.3136 | -47.6042 | 2026-09-20 03:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| d2d2dd88-ff4f-3ea8-b8fc-e5b6be346d86 | -7.3259 | -55.6153 | 2026-09-20 03:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| f10dce26-2244-3f3c-a1f0-b48aa8a9feea | -7.5334 | -45.4367 | 2026-09-20 03:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 2799933d-313d-37ec-9507-a627d351d7c0 | -11.8544 | -47.6819 | 2026-09-20 03:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 862d933c-b17c-3462-8647-7f6401365477 | -6.3134 | -47.6261 | 2026-09-20 03:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 298.1 |
| 22d7d856-6abe-3fb7-a149-5bd83ccdb09e | -11.0991 | -54.0285 | 2026-09-20 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 24a8b092-8f3c-3e2f-ae85-96b118da1573 | -11.118 | -54.0268 | 2026-09-20 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 01c22887-81fd-36c5-a515-346c39bd8d19 | -2.8791 | -57.799 | 2026-09-20 03:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 54688d74-7cf0-347b-be94-e78b03579e85 | -6.29 | -47.63 | 2026-09-20 03:15:00 | MSG-03 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 34175e55-8e5c-3fb4-ab2d-7dd92408debc | -7.5522 | -45.435 | 2026-09-20 03:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 12617438-2207-38d4-9c0f-34579ad4b82e | -7.5525 | -45.4123 | 2026-09-20 03:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| dceab2f2-43f7-34ec-aa2b-61a3dd000d2f | -7.5334 | -45.4367 | 2026-09-20 03:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 41c68a76-7140-31fb-b049-103d1bb456f4 | -11.118 | -54.0268 | 2026-09-20 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 9cd0c7c9-193a-30c6-97ff-b6fbcda60e9e | -6.3134 | -47.6261 | 2026-09-20 03:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 273.7 |
| ad675ebe-fd86-3565-8544-e60ce151b802 | -6.295 | -47.6055 | 2026-09-20 03:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 8f412b98-9989-3a1b-afcf-e6e7bc26db8e | -13.037 | -46.9096 | 2026-09-20 03:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |


[Clique aqui para ver as próximas entradas](README10.md)
