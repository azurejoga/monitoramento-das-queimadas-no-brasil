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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e404265-2975-3964-9f96-55ac94a47d3b | -15.80205 | -52.27667 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 943f7b13-1c17-31dc-af4b-56af71f30b04 | -12.87223 | -62.12222 | 2025-09-11 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c73748b-e26f-306f-b13c-b27357f6c97b | -15.13586 | -52.44864 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0ef4379b-135c-3990-8b85-0bfe4bb580f4 | -12.60025 | -56.96452 | 2025-09-11 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e32387a8-1266-3184-8e69-b5eafc489b37 | -9.74918 | -65.06644 | 2025-09-11 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cb343eb0-4b2f-3ff5-8b36-84fdb7600133 | -11.88292 | -58.81888 | 2025-09-11 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 64e64ce3-195d-37b7-adce-bbbf83d5c010 | -12.35162 | -63.64454 | 2025-09-11 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5951efe9-2bff-39ef-a8c6-802333a76e11 | -12.93534 | -54.75114 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bfbc1428-de9b-3940-bbc2-f8f2ae579c08 | -15.55799 | -54.74738 | 2025-09-11 05:38:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a166d920-35f1-3945-8b4e-69193439643c | -15.82113 | -52.22363 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3067e12-0526-3fed-b558-d023af4e3e62 | -12.38077 | -54.17315 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 671a1a16-5f1b-34da-ba4c-2c30b23dac19 | -12.85641 | -52.94717 | 2025-09-11 05:38:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d38fb1f1-c24c-39bc-8f1c-e0fc86f0ec01 | -11.16038 | -52.03569 | 2025-09-11 05:38:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9b0415f-1d4c-30f3-ac46-a7ad365d4a5d | -15.14672 | -52.40767 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4c10e980-d234-3328-8407-98ae26b9ab6d | -12.86862 | -62.12169 | 2025-09-11 05:38:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 036726c5-04d2-3d04-95e0-69114da30f74 | -9.93257 | -65.00263 | 2025-09-11 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5b88c72-e6fd-3ad4-ad40-3676ea818a2f | -9.03515 | -63.55869 | 2025-09-11 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20fef257-0d5c-369a-97f3-c165e5f11996 | -15.11869 | -52.40262 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 51ae5037-9099-3c8c-b229-82048ccb2308 | -11.20857 | -54.99149 | 2025-09-11 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 20deafbd-d317-3f64-b06b-c7119b38fdf6 | -9.92924 | -66.87725 | 2025-09-11 05:38:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8505583b-339b-3d3b-98fd-235b0af588f2 | -12.61096 | -56.96008 | 2025-09-11 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 002bc006-53d6-3cce-891d-47b076a47413 | -11.87853 | -58.81847 | 2025-09-11 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 905070a2-7063-30c1-b30c-49cde79f48c3 | -12.94541 | -54.81556 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fea313e-dc63-3e63-9209-851e84cf98ec | -14.5181 | -53.93026 | 2025-09-11 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| afd9c6d2-033b-36b6-be1a-4f634d579589 | -14.9289 | -55.9103 | 2025-09-11 05:38:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f57887e4-e909-3041-a14b-c9158505b13a | -15.60347 | -52.73853 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88b62223-de17-380f-b788-0cc250d08fb7 | -12.06544 | -64.16758 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 93ad4fb0-2285-38cc-8f3d-2544159874d5 | -12.41072 | -63.81464 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ff74b40-a237-34ff-806f-194c85606b50 | -15.80615 | -52.23256 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e096c8ec-f5d6-3966-999f-a8b5d47d9ba6 | -12.92514 | -54.7879 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3bbb324-8ae8-3a07-bcba-b38bc2b2a54d | -10.16625 | -68.15734 | 2025-09-11 05:38:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17bc8345-d31c-3627-b369-c9533c92acf1 | -14.3047 | -54.74406 | 2025-09-11 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1027c7e-a279-3808-829a-bc07f20d2dc2 | -9.45954 | -63.03117 | 2025-09-11 05:38:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9521029-438b-33f9-b29e-91f41d6b3d31 | -10.64408 | -69.30428 | 2025-09-11 05:38:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e62a2352-a471-3b20-974e-269513fc2f7e | -15.5615 | -54.77187 | 2025-09-11 05:38:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fdd57d69-d89d-30d6-999e-3c88fde35bde | -14.93647 | -55.94211 | 2025-09-11 05:38:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7aabfe23-3854-3700-9108-d45d520a8630 | -9.15345 | -60.25697 | 2025-09-11 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15a8a9ed-9fb3-3b29-b80a-4537d973d757 | -10.33907 | -54.55207 | 2025-09-11 05:38:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3f8ae506-d2c7-3512-9f94-6b90924babd0 | -12.39521 | -63.8128 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b6248a2-d23d-3ea1-abd9-0a8a607d0f71 | -10.05298 | -59.35775 | 2025-09-11 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4d90e1b-ab77-34e8-9cb7-ac4ce2941fde | -8.89318 | -64.23402 | 2025-09-11 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 731ee734-40c1-3bfd-9f7d-11a74afe772f | -12.93528 | -54.80179 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c0f155db-0fb9-3068-86c2-fcfe1806e93d | -15.12584 | -52.40783 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 6cd73991-e533-3bf7-b8c2-d04e3590b9fb | -12.41354 | -63.81881 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 277fd8b6-51f5-3754-952c-557669e8ad48 | -12.60561 | -56.96227 | 2025-09-11 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51aee2dc-b91f-3950-a3e7-be3ccb8bd56c | -15.11966 | -52.39957 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7d29913c-9471-3800-8228-018d5e74ad52 | -8.82085 | -64.17297 | 2025-09-11 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 868408f6-ec20-39aa-9cef-3e42df74959f | -12.96448 | -54.75551 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dbadc627-933f-3ae9-8f6f-45250684226a | -12.39329 | -54.16988 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2560d037-06d5-3026-a3a2-fb4e4080fb07 | -11.22537 | -54.99368 | 2025-09-11 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 931de44f-a5f4-33fb-8097-65df0ed96740 | -9.79681 | -61.51712 | 2025-09-11 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ad4d37c8-82f5-3fff-995a-c24e205ab4ea | -14.51866 | -53.925 | 2025-09-11 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 19b9f929-6c9c-35f1-8ee3-313b9bbae2d0 | -10.06489 | -66.98983 | 2025-09-11 05:38:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e004b880-9f14-3cf8-b828-58c5d92aa4ce | -12.41299 | -63.82246 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f1f3768-f8da-35fc-8c94-dd08ca39bfc4 | -9.75248 | -65.06698 | 2025-09-11 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 32aa88cc-1c69-3aa4-8d7c-2e4643830b81 | -9.28825 | -63.72463 | 2025-09-11 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d8b7184-29c7-3332-9436-221d884761c2 | -9.03859 | -65.405 | 2025-09-11 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e5f2035-e541-3654-a14d-008537bbcdf2 | -12.07102 | -64.17577 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9cd6540-4225-3fb9-964d-53a0d6313225 | -12.8629 | -52.94804 | 2025-09-11 05:38:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5cede96b-6284-3f6a-81a8-f4a35d4badc4 | -12.97079 | -54.75184 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9b4d02c-12c1-382f-a267-d8f51344148b | -10.05246 | -59.3615 | 2025-09-11 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99526bf8-5350-3845-bfcc-d3897392cc4c | -10.46461 | -67.83932 | 2025-09-11 05:38:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e10c5f1f-6049-32ae-8e8c-8747ad6e4631 | -15.80842 | -52.284 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 763a36e6-43e0-3389-a612-0fedc45f1ad3 | -9.80696 | -61.52291 | 2025-09-11 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5c0fc1f8-c563-3c77-8aa9-5eb7e684c612 | -10.37631 | -67.82519 | 2025-09-11 05:38:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a4b11ae-bcf4-37d2-a956-b2ed71b74011 | -12.38728 | -54.16926 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfa9f22b-fb94-3192-8871-eec9ab0771f2 | -14.28646 | -54.74636 | 2025-09-11 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f1056606-93da-3c73-a076-f07fc9d78dc3 | -15.13037 | -52.43336 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d622777c-72e0-3c6d-a6d7-b4c9b5543e8a | -15.79984 | -52.22434 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6d14c971-4b3d-3981-ad17-37777a77b298 | -14.90463 | -55.87659 | 2025-09-11 05:38:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e7f13f83-d8fd-3c77-b19a-2006b43f6eb9 | -11.22338 | -54.99875 | 2025-09-11 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2f462ce9-9708-39a6-b410-c2edbd1a6269 | -11.8797 | -58.80974 | 2025-09-11 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5c97976c-86a2-34ad-83e0-ac59a9558254 | -12.40681 | -63.81777 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3147c6d6-f670-3a6f-b5b2-1e08aaf02875 | -11.16082 | -57.18183 | 2025-09-11 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7e32f2e-a041-397d-9b6e-f9d1284deb68 | -15.14266 | -52.45004 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4110b41b-ec55-3f37-bc10-20542afbeb9d | -11.78829 | -64.92691 | 2025-09-11 05:38:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7497d069-4fcc-387d-85e4-7edcfef14874 | -11.22488 | -54.99751 | 2025-09-11 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9ac72f19-a5d1-38fb-9a28-b5fccb26ea65 | -12.39676 | -54.16754 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4f2fbb70-232a-35a9-9fd7-8f0e5a9daa87 | -11.15967 | -52.04178 | 2025-09-11 05:38:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ecd6a214-c22b-3708-9dae-935dd40e0f86 | -14.89218 | -55.83683 | 2025-09-11 05:38:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3baadd56-c883-3ea1-9590-77535087454e | -14.89357 | -55.87497 | 2025-09-11 05:38:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c7795c9-ab86-341d-b4b2-cbf30f0f55e3 | -11.22383 | -54.99493 | 2025-09-11 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a523486-b7ab-33f8-9ac2-2c68fad2f8b0 | -15.15979 | -52.41637 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2ff65e85-a9f4-3143-b8c5-aaf71edc572b | -15.13051 | -52.42327 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f0563fe0-ed6c-3070-b35b-2a908b984968 | -12.35217 | -63.64086 | 2025-09-11 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31e13ecd-13a6-3dd1-8cb5-129a9d30d24e | -15.13643 | -52.44261 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 639f6e51-074c-3730-a57f-85efa58f4994 | -12.35555 | -63.64138 | 2025-09-11 05:38:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b48ee75b-8f0c-3ce0-8bc7-1c4209d445cb | -12.40344 | -63.81726 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f1f3703-24f2-33ef-af1a-2baf72c9708c | -15.13708 | -52.43584 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| faa9bddf-56b3-3df1-98f5-6e12199864e4 | -12.40735 | -63.81412 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d21edeac-3360-3606-b1a7-1f9f5b15f2c5 | -8.97998 | -61.43309 | 2025-09-11 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee0c2613-54a9-3baf-a21e-feb3aa605baa | -15.13658 | -52.43187 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cef65179-a28f-39e5-8520-8b0a6114b22c | -12.96974 | -54.75954 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a7ebc8b-e7f0-3091-9bda-3f5799a16e65 | -14.51655 | -53.92983 | 2025-09-11 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 070bbe0f-d1e6-37c7-a832-892ad9d1f781 | -11.21822 | -54.99427 | 2025-09-11 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d080a89d-a808-3a0b-97e7-0ac433fe9b51 | -11.05742 | -51.34556 | 2025-09-11 05:38:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 5ea0209e-c002-39c7-adb8-d4a8c4fb0443 | -12.4079 | -63.81047 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9a38bb6-1a92-30ba-ae44-6d05eaf786c3 | -17.37684 | -52.94078 | 2025-09-11 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 94e76351-62d9-37db-a08c-e578435bb225 | -17.38476 | -52.92879 | 2025-09-11 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7a91b387-3b3e-3a38-9479-1616b390e72f | -17.37791 | -52.92828 | 2025-09-11 05:40:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |


[Clique aqui para ver as próximas entradas](README129.md)
