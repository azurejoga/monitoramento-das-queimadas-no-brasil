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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a09989b-75c3-3b6c-9272-fc27119cb33c | -22.1213 | -47.2765 | 2025-09-09 00:20:00 | GOES-19 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.7 |
| 81814d61-c17e-35f5-8ffc-5ebf0415a0ac | -12.2178 | -53.9005 | 2025-09-09 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 614ef7db-e95f-34cc-9e05-95d25efce085 | -9.9498 | -60.1367 | 2025-09-09 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 0669bb64-0748-394e-a052-8ab204b4d6f4 | -12.1991 | -53.8817 | 2025-09-09 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 102.8 |
| c282905a-4b0a-33d5-881f-3d8f2d2a0e1c | -10.9815 | -45.0874 | 2025-09-09 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 4912e706-d3bd-3888-a7db-76e422b6e33c | -5.6925 | -43.8986 | 2025-09-09 00:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 7d21fe42-0c19-3499-88a7-fd7fdbb3a930 | -5.6931 | -45.9891 | 2025-09-09 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 2aa594a7-d269-3413-88fd-af4a32a5a866 | -10.011 | -64.9339 | 2025-09-09 00:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 1982f63f-0c6e-315a-a2ab-1474c9c2b725 | -5.5705 | -45.0291 | 2025-09-09 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 917142e4-7abb-3608-833f-6840e73e50bd | -8.0609 | -48.6206 | 2025-09-09 00:20:00 | GOES-19 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 86039ec7-88ea-31d5-803f-185a5595f12f | -18.4607 | -49.5485 | 2025-09-09 00:20:00 | GOES-19 | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 54ff4d43-3fd0-3138-acc0-b1d89ccd42ae | -10.9808 | -45.1335 | 2025-09-09 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 02447c5d-a9b4-3125-8b72-217844ad7c7e | -12.6153 | -56.9742 | 2025-09-09 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| e76372b0-bd15-372b-9f68-ca8b11faf27d | -12.1988 | -53.9024 | 2025-09-09 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 116.3 |
| c9bc100e-1c5e-3217-bda1-27d3721d6bad | -10.962 | -45.113 | 2025-09-09 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 524.8 |
| bdfb69ac-3aee-3952-b2f1-cd5fbb52eee1 | -18.15 | -51.8156 | 2025-09-09 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 5c4ea9ee-933d-3db6-9ae8-c6799c1d36c9 | -11.4277 | -43.6017 | 2025-09-09 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| ba230abc-66c5-3422-8455-e5162e03a3c0 | -5.5703 | -45.0518 | 2025-09-09 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 411.1 |
| 4b2a51fa-ea0b-373b-819e-9355302d8208 | -12.1991 | -53.8817 | 2025-09-09 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 110.8 |
| ce3060dc-4871-342e-b458-308d2775baf0 | -5.6925 | -43.8986 | 2025-09-09 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| c0f76a67-dda6-312c-a23e-970da9cb8ca8 | -12.1988 | -53.9024 | 2025-09-09 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 0eb1942a-0407-3e08-9f3e-b2af045853d8 | -12.2178 | -53.9005 | 2025-09-09 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 1aff4d44-5333-309b-bf4a-035f103b7e14 | -10.9815 | -45.0874 | 2025-09-09 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| f6c0a56e-4e4a-325e-bc6e-0719c80db893 | -12.9482 | -54.7519 | 2025-09-09 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 95472e2c-487b-3dc6-947f-f1aa76042899 | -11.4277 | -43.6017 | 2025-09-09 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 0c7ff04f-1aba-3b27-b1b0-f6d80bc266ed | -9.2182 | -60.8113 | 2025-09-09 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 3c95d637-0faf-3d88-b8aa-8e9e4a383071 | -10.962 | -45.113 | 2025-09-09 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 340.6 |
| 25174ff5-ce55-3703-bb70-e759487fe8a7 | -5.6738 | -43.9 | 2025-09-09 00:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| de36f8bc-df59-3a12-8db7-2dd9b7830a76 | -5.5892 | -45.0278 | 2025-09-09 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 133.8 |
| b80b7b60-c2ba-39c2-bd31-6839a5c718e9 | -10.011 | -64.9339 | 2025-09-09 00:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 76.9 |
| e9cac964-48fe-35bd-955a-76570be34d44 | -5.5506 | -45.1664 | 2025-09-09 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 3081699f-2cd8-35ea-af46-f424faaef273 | -8.0606 | -48.6423 | 2025-09-09 00:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 67.8 |
| bdf0e9ea-32d0-3d66-964a-b098b9a41354 | -9.0802 | -65.3789 | 2025-09-09 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| ea61b520-392a-3753-ada0-549bcc9f21b2 | -22.3261 | -50.8934 | 2025-09-09 00:30:00 | GOES-19 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 96.5 |
| f02e7e56-ca0b-3a27-b4c3-d7e0c8215dc5 | -9.9498 | -60.1367 | 2025-09-09 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| bdc529d6-3359-3e9e-ab4e-832860d071ec | -12.9673 | -54.7499 | 2025-09-09 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| d2c76fbc-354c-3772-8ee7-5e5457778bac | -22.3463 | -50.9117 | 2025-09-09 00:30:00 | GOES-19 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 181b5026-d7cf-310f-ada5-7ff99ebbab75 | -22.3469 | -50.8888 | 2025-09-09 00:30:00 | GOES-19 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 278.0 |
| 5a28b774-c9ed-3ec7-a069-687aa93c78c9 | -10.0111 | -64.9151 | 2025-09-09 00:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 57d7b2a1-8249-3037-b738-3db4d38f09ab | -10.9808 | -45.1335 | 2025-09-09 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.4 |
| d9f14463-e95f-3ba5-9307-ef121505bcad | -11.2007 | -54.9992 | 2025-09-09 00:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| cf1aa776-44c6-3b4f-a9f3-3fa7562b680e | -10.9811 | -45.1104 | 2025-09-09 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 566.9 |
| 335bb26d-ffb3-3457-939f-9d425e91ebb5 | -12.967 | -54.7705 | 2025-09-09 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| a33479bd-9492-3ecf-a0de-b371b120ae05 | -22.3678 | -50.8842 | 2025-09-09 00:30:00 | GOES-19 | JOÃO RAMALHO | SÃO PAULO | Brasil | 3525607 | 35 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 27c0a54f-9a7e-3abd-bd14-5b9319f9d8bb | -5.589 | -45.0505 | 2025-09-09 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 372.1 |
| 6b54e7ba-b264-3893-b0f9-379d8ba2354c | -12.948 | -54.7724 | 2025-09-09 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 218802ff-94a1-3bcd-bf0a-4230402fa049 | -10.9624 | -45.09 | 2025-09-09 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| a61358c8-46fd-3dae-8446-3d3c55dc3d63 | -5.5703 | -45.0518 | 2025-09-09 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 308.1 |
| 1eabdd5f-867d-3f29-886c-8ef18e0cd784 | -5.5705 | -45.0291 | 2025-09-09 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| f6c1a491-eb0d-306c-9b26-ec478594e00b | -10.9616 | -45.1361 | 2025-09-09 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 49b0cbfa-0e7f-31e2-9ef0-efc865ccb50b | -12.6343 | -56.9725 | 2025-09-09 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| c503e1ad-3afa-3f6f-9c65-35be1f348855 | -9.2181 | -60.8305 | 2025-09-09 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 4dea8a0b-3458-391e-8ac0-c8f5661ea317 | -8.0606 | -48.6423 | 2025-09-09 00:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 445ea306-650f-340f-ac06-24b57c16bcb0 | -22.3261 | -50.8934 | 2025-09-09 00:40:00 | GOES-19 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 632c84b7-91db-3e8e-a16a-8e533006409a | -5.5892 | -45.0278 | 2025-09-09 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 0f5039b8-e1a5-3f06-ab40-3446fb54eb11 | -11.3018 | -46.4792 | 2025-09-09 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 20d14f7a-25d1-323e-b0e6-54b23bf292ed | -9.2181 | -60.8305 | 2025-09-09 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 49c7bc29-e638-3fff-8c9e-ecd7b628655e | -5.6925 | -43.8986 | 2025-09-09 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| aafb8ba0-0c9c-3fe1-9a0b-7ee05d230ed0 | -12.2178 | -53.9005 | 2025-09-09 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ed2f4e66-ad1f-37b6-b460-7791d68de75f | -16.3136 | -50.0427 | 2025-09-09 00:40:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 9aee6df9-87a9-39ca-9ceb-d7235b19b668 | -12.1991 | -53.8817 | 2025-09-09 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 64e35905-7de1-3ca8-b238-d7f51dbd9d87 | -5.5703 | -45.0518 | 2025-09-09 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 339.3 |
| ebf89665-a8b7-3fb7-b545-58aed1948bea | -5.6738 | -43.9 | 2025-09-09 00:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 1a2a9374-081d-3825-9ae5-0d6b0840d037 | -5.589 | -45.0505 | 2025-09-09 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 186.0 |
| b25ae8cc-3904-31c1-aa1a-2b604ae40040 | -5.5705 | -45.0291 | 2025-09-09 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 192.0 |
| 222c7a69-811c-360c-9230-6e3f0264c9a2 | -12.6343 | -56.9725 | 2025-09-09 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 8dfa9442-4144-3b0f-871d-33ad14066c02 | -20.5473 | -51.4882 | 2025-09-09 00:40:00 | GOES-19 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.0 |
| 03bad5ed-03e0-3247-bd28-1f74836bf6a0 | -9.0802 | -65.3789 | 2025-09-09 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| ddb19b08-86d4-3c6a-a2a5-0f8f98395a4b | -17.2757 | -46.7538 | 2025-09-09 00:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 460bbf78-a7d5-36dc-a4d1-b47f401da29b | -10.0111 | -64.9151 | 2025-09-09 00:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 89.1 |
| a9a879e3-81bb-39ff-8918-75446439925c | -12.948 | -54.7724 | 2025-09-09 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 35a51162-824d-3804-bf46-2c8d30bc1a9a | -12.9482 | -54.7519 | 2025-09-09 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 7283d17c-75c0-349e-81df-adc41d216beb | -22.3671 | -50.9071 | 2025-09-09 00:40:00 | GOES-19 | JOÃO RAMALHO | SÃO PAULO | Brasil | 3525607 | 35 | 33 | nan | nan | nan | Cerrado | 80.3 |
| d938c126-ae1c-3308-be16-56545f4484d1 | -5.5701 | -45.0745 | 2025-09-09 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| d2d5597f-9520-3973-b8b5-cf7d822ab0a5 | -22.3463 | -50.9117 | 2025-09-09 00:40:00 | GOES-19 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 2b62b9ac-9f9f-3410-802c-f058890c6b75 | -11.4277 | -43.6017 | 2025-09-09 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| de2f325b-e77e-36dd-b5a2-830d9a276841 | -9.0987 | -65.3783 | 2025-09-09 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 805ec65a-5bd6-3aa7-8cd6-b95bc126e18e | -22.3469 | -50.8888 | 2025-09-09 00:40:00 | GOES-19 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 216.5 |
| 427222dd-5313-36b0-8c4f-c9502740ccd1 | -10.011 | -64.9339 | 2025-09-09 00:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| a6e8cc1a-c0ad-325e-840a-c4ad30659a93 | -22.3678 | -50.8842 | 2025-09-09 00:40:00 | GOES-19 | JOÃO RAMALHO | SÃO PAULO | Brasil | 3525607 | 35 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 9ade8992-f253-3632-b2fa-daef794c93f6 | -11.3905 | -43.5365 | 2025-09-09 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| ec30995b-6218-3d0c-9f24-ff4c410d7da5 | -12.1988 | -53.9024 | 2025-09-09 00:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 72c42bff-2d48-39f9-abc6-9dc378bce23a | -12.1991 | -53.8817 | 2025-09-09 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 9fd27609-4703-320d-95d0-d015acf97333 | -11.3014 | -46.5018 | 2025-09-09 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 7ce0b401-ad45-3463-97e5-4da2d2619cb6 | -5.6925 | -43.8986 | 2025-09-09 00:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 809e2fcb-9078-3178-a14d-a132fbf8581b | -12.1988 | -53.9024 | 2025-09-09 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 127.9 |
| acafabe6-49f7-3f91-bc14-b0ea05b957ad | -20.5677 | -51.4842 | 2025-09-09 00:50:00 | GOES-19 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 109.6 |
| b85b31f1-5bd0-3130-914b-d107e3f3da57 | -10.011 | -64.9339 | 2025-09-09 00:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 53bba5fe-934a-35a6-a6f6-e7b50d6ea74b | -5.5703 | -45.0518 | 2025-09-09 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 280.9 |
| 99b474a2-55ed-302c-9f7c-33acb1145b3e | -15.8703 | -54.9358 | 2025-09-09 00:50:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 56.9 |
| a75ad439-5b5d-3533-836a-fca15d389e67 | -20.5479 | -51.4659 | 2025-09-09 00:50:00 | GOES-19 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 174.2 |
| ed519281-30c6-3c7d-94d3-9130b8a57fff | -20.5473 | -51.4882 | 2025-09-09 00:50:00 | GOES-19 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 238.0 |
| 468eff65-9b07-3fb5-8209-6f51fefeccfd | -5.5892 | -45.0278 | 2025-09-09 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| cbfa7dfe-bd6a-3eff-bcfa-e2f851e064a0 | -17.2757 | -46.7538 | 2025-09-09 00:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 715edb64-e697-3a7f-9e0b-684e8eebbc21 | -20.5683 | -51.4619 | 2025-09-09 00:50:00 | GOES-19 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.0 |
| a392fe9a-d28c-3f87-a578-83d355975b35 | -9.0802 | -65.3789 | 2025-09-09 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 4408de90-cb7c-3b6b-b162-6ee00ba38db6 | -5.5705 | -45.0291 | 2025-09-09 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 1f8a3880-70cf-37cd-8711-69e5b2ea74fc | -12.9482 | -54.7519 | 2025-09-09 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 5fb82862-0d6f-3147-857a-c9292785d5a7 | -12.948 | -54.7724 | 2025-09-09 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 7d68c3a6-7674-3879-9de6-fef43dbf943d | -11.4277 | -43.6017 | 2025-09-09 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |


[Clique aqui para ver as próximas entradas](README3.md)
