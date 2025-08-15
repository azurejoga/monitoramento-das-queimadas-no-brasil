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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca2e5cbc-2b8d-3d2a-b313-9059e8fd753c | -9.518 | -60.5268 | 2025-08-15 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 6a053541-0c17-3915-b243-9714dc50dc56 | -7.5477 | -61.3247 | 2025-08-15 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 7cc89ac1-70f2-33af-9add-6c65aef25523 | -11.3468 | -55.4124 | 2025-08-15 01:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 195.8 |
| 743bd299-4218-3c5c-8b66-a5098ea45453 | -5.762 | -46.6741 | 2025-08-15 01:20:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 79094371-007a-38d9-afa5-e8278c643241 | -9.4992 | -60.547 | 2025-08-15 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |
| d0b83dca-e843-3807-b6ef-5c7eb934c6d3 | -9.4995 | -60.5085 | 2025-08-15 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| fa20278a-5008-3215-807d-1837a5960afc | -11.328 | -55.414 | 2025-08-15 01:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 5a7acd45-3c16-3359-a004-10ecae7b9a78 | -7.0797 | -59.2157 | 2025-08-15 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 27f69807-a7e5-3d48-89c7-e04edbaa0490 | -14.2449 | -44.5661 | 2025-08-15 01:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 0d9cef00-fe73-36ac-8229-2c5d1cb02a8f | -14.2444 | -44.5897 | 2025-08-15 01:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 6e75fdb4-ff9f-35cd-8510-58bdaf727c77 | -7.6104 | -63.4972 | 2025-08-15 01:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 2c61a2e6-db81-38a7-b638-3d7a77d6f202 | -9.3875 | -60.5528 | 2025-08-15 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 35585861-5dfa-3d1a-9383-957830ccd0a1 | -11.3466 | -55.4326 | 2025-08-15 01:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 92f0e1b2-ea2f-389a-8469-f76e2c4edb7b | -5.455 | -60.12 | 2025-08-15 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 2cf0309b-fd47-3236-992b-77fc7e41cbf7 | -7.5291 | -61.3444 | 2025-08-15 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| a8bfde8d-fab2-3609-97c3-ad433ada5266 | -11.3655 | -55.431 | 2025-08-15 01:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 952d3ee4-c107-3a6c-8a66-7c63fc081961 | -7.0982 | -59.215 | 2025-08-15 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 2b3ea33e-3e94-3b13-b7b3-872601dde098 | -16.30986 | -52.93459 | 2025-08-15 01:24:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 4b83c0cb-9afc-3e39-a651-a18c022358c7 | -16.30639 | -52.92881 | 2025-08-15 01:24:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| e1ae5fce-81e5-338c-afd3-47111ccad6d4 | -16.30629 | -52.91366 | 2025-08-15 01:24:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 35.2 |
| f314c20e-2b64-3f0b-a950-859ef1fd5395 | -10.11383 | -57.7718 | 2025-08-15 01:26:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 06cb4bbd-5def-3ce3-806c-60247ff759c7 | -15.6699 | -56.38136 | 2025-08-15 01:26:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 38b2073f-f763-3c87-80be-8487e04ab01d | -9.92309 | -60.43449 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 848598d7-61f6-3e74-9b0e-148eb7345035 | -9.78569 | -61.5044 | 2025-08-15 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 410c8bb9-5e8f-37d4-bb58-5a6fa2da2797 | -15.38327 | -59.82645 | 2025-08-15 01:26:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 977c0e6d-7d84-3d8a-95d8-c944d1213826 | -9.92038 | -60.48765 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 23.9 |
| b96426ab-3c7b-35e2-8447-69d77bed2502 | -10.32904 | -64.45524 | 2025-08-15 01:26:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 14.7 |
| afeb57f9-9fc9-347b-912f-ff05acb67a52 | -10.05464 | -59.36601 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 19356fad-9695-3185-9d87-ded964458d97 | -10.32217 | -63.62768 | 2025-08-15 01:26:00 | TERRA_M-M | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 81268602-3ae0-3e35-bee9-4b3609d94729 | -11.74049 | -64.89892 | 2025-08-15 01:26:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 1e9cdf7c-043e-3d61-9fd3-b6c3e6131f6b | -9.50143 | -60.51792 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 0455e04f-348a-3f8f-b998-6116a29cf549 | -9.51293 | -60.5348 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| a7de42ab-0081-3016-ac11-105a2fab9bab | -9.504 | -60.53611 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 133.7 |
| 28e94f2f-a090-3223-a220-d8e333158d09 | -9.39418 | -60.53961 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 40667f7d-916d-328f-acbb-0c22cdef17a1 | -9.50657 | -60.55429 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 36.5 |
| a7e80b99-bcd0-310c-a36f-afb9003c399f | -9.90378 | -60.43433 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4a5bb8fd-d18b-352f-98e8-88c44a4f89ed | -9.17544 | -59.65931 | 2025-08-15 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 6570516d-1b44-39b2-a526-a51236e0f828 | -10.47123 | -61.32948 | 2025-08-15 01:26:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 5eadf264-3081-3b31-bf12-f9b221643aa7 | -13.13566 | -57.16566 | 2025-08-15 01:26:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| fac018ed-0dd4-30e9-9d94-96f189c884c9 | -11.35324 | -55.43782 | 2025-08-15 01:26:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| d7c60a9b-540e-36cf-ba4d-5bc1d831ee34 | -10.00735 | -59.21656 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 097f5708-d5a8-37d5-8f60-5eb2b69f8641 | -9.18467 | -59.65799 | 2025-08-15 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 37.4 |
| aaa52948-813e-3de5-bbbe-686a98448f0b | -9.50272 | -60.52703 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 160.2 |
| c8e710b3-5da5-3ed8-b329-b7aeacd02dac | -9.21369 | -59.66347 | 2025-08-15 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 5a4cd112-c77c-3d64-885c-55a2a774dad5 | -9.9191 | -60.47855 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 215aa276-3115-30d8-87f4-9bba788efee5 | -9.49636 | -60.54653 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a48135bb-9bc5-34f6-85c0-07520c63842e | -9.50014 | -60.50881 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 21bf7e19-1455-376e-9d46-b4ad8482364b | -9.20448 | -59.66488 | 2025-08-15 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 1a2ea911-7fc5-3e65-8393-86b45ce1a75b | -10.04761 | -59.12242 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 351f5593-18bd-3ea9-a017-08c54b55a924 | -9.51164 | -60.5257 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| ecbc1a0a-cb75-3fd8-87ce-336c4c0f3d3a | -9.17827 | -59.67875 | 2025-08-15 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 12286244-6da1-3dd6-b07c-7f987078227e | -10.00879 | -59.22655 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cdfbdd93-b331-3846-83b6-c72cb7cc21a0 | -11.31775 | -55.21342 | 2025-08-15 01:26:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 7c1e18fd-c588-37a6-af5d-92f4e6f3aae8 | -13.06952 | -57.13371 | 2025-08-15 01:26:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 705cf1a8-1290-348e-a721-56c38b033d03 | -9.50529 | -60.54521 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 33a8536f-70fb-3970-b1dd-f85657a17083 | -9.38654 | -60.55003 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 4b77cb09-1d04-332c-8439-8d120ac2322b | -10.85774 | -62.00077 | 2025-08-15 01:26:00 | TERRA_M-M | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 5a29e162-89aa-38e9-b6d7-2daed21f4845 | -9.18109 | -59.69815 | 2025-08-15 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 13bd0731-e79c-3710-aa32-430acfc600b6 | -9.20308 | -59.65518 | 2025-08-15 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 979dd3b2-093e-3a07-a675-b7f197d164d1 | -9.18888 | -59.68707 | 2025-08-15 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| dbacf916-6a33-3ede-8ddb-818ccffaf9e6 | -9.39547 | -60.54871 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 93922e48-0661-3b96-b063-d32c9ff8f789 | -9.21508 | -59.67317 | 2025-08-15 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| c95747e4-03e8-3ebc-a40f-a440aaee06db | -9.15031 | -59.42171 | 2025-08-15 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 754fbfd5-b072-37ef-b476-3be491633776 | -10.112 | -57.75972 | 2025-08-15 01:26:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 0c399e9b-181a-3fcd-acd0-ae8b9b7a1c78 | -11.36511 | -55.43584 | 2025-08-15 01:26:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 1e58592a-9c12-3315-b363-62152373afc5 | -9.93848 | -60.47867 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 8bb97d0d-07db-3d68-a824-2149335e8add | -10.85899 | -62.00991 | 2025-08-15 01:26:00 | TERRA_M-M | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 38ebcc8b-fda1-3457-bd39-ae7c57a099bc | -9.89485 | -60.43563 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| db5c3808-a2bf-30c4-8d5e-aee9eedbf13d | -9.79679 | -61.50607 | 2025-08-15 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 64f95e6e-ea41-393c-a529-205f623afba0 | -9.49765 | -60.55561 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f763e195-ec20-355e-a099-3a324551757d | -9.38525 | -60.54092 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| e37376c3-7a09-3d54-b36a-70cc174b53ec | -9.51421 | -60.54389 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 0aeca86e-d9f9-303e-b358-10370c187cdb | -9.51036 | -60.5166 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| af2d285a-a482-364b-8757-7964445d5252 | -15.68014 | -56.37969 | 2025-08-15 01:26:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 04a07ca4-5367-3721-80b9-e6ba3e9460ea | -9.17686 | -59.66904 | 2025-08-15 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 7b549ef8-df1f-3fa2-bcb1-5402a5a6bed4 | -11.9409 | -58.76552 | 2025-08-15 01:26:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7ccdb33a-7ffe-3022-b58c-f3437437c41c | -11.34791 | -55.40406 | 2025-08-15 01:26:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 103cc5be-ba2a-3e74-bf34-9b40db3d5f78 | -11.36246 | -55.41899 | 2025-08-15 01:26:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| c03f5fe1-6529-3ee0-9c63-8721683c5de4 | -11.33868 | -55.42285 | 2025-08-15 01:26:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 484c6a09-6d08-39d6-900e-57ac2f06c1d8 | -9.83092 | -60.76515 | 2025-08-15 01:26:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0268135f-4b67-3f61-8754-8b0649e8e507 | -9.17968 | -59.68845 | 2025-08-15 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 341d660a-af04-3c76-92a2-6d9bd8c828a8 | -15.67894 | -56.38686 | 2025-08-15 01:26:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0c6ccb31-410d-396e-b0ea-e8bef3fa65cd | -9.91399 | -60.44212 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| bdb64a26-f3f9-3584-a5b8-3faf246862f8 | -10.35901 | -64.45123 | 2025-08-15 01:26:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 90048f79-d365-3289-8599-b91bad029296 | -10.05319 | -59.35609 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0af4fa51-d3e9-3d67-8a9a-3db050312b9c | -9.93977 | -60.48776 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d6c32c74-2f1d-36d8-a2a6-f178e89a97cf | -11.3506 | -55.42107 | 2025-08-15 01:26:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 152.0 |
| a7dbf0a6-388f-3f04-863a-3e1e2c8672a3 | -15.38199 | -59.8173 | 2025-08-15 01:26:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 373b65ea-4b29-3af2-9247-6a09f31e5469 | -9.92439 | -60.4436 | 2025-08-15 01:26:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 1292d840-5d71-3300-a32c-788534a0de60 | -11.40829 | -58.54241 | 2025-08-15 01:26:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 8a13d76e-598d-35f3-ad74-8374d55eeaa5 | -9.18607 | -59.66771 | 2025-08-15 01:26:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| f66872db-2622-31bd-9332-5e6fd9e1123e | -8.91371 | -60.72997 | 2025-08-15 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b4880e06-e10a-34c7-b8fe-41c86d83d231 | -9.15338 | -59.68828 | 2025-08-15 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 90e9609f-0877-30eb-a733-8eaf76193bee | -6.93147 | -59.54353 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.2 |
| e75ea340-75ab-3e51-9eb5-44f60a968297 | -6.1088 | -59.92778 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 949be869-d75e-3f3c-bb10-e92024dd7ab8 | -8.11464 | -61.20399 | 2025-08-15 01:28:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 34a6f89f-1bc0-377f-a134-8bc4aba24ac2 | -7.07387 | -59.22554 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 924b40d5-cc74-3957-be9e-6e5f934a92f1 | -6.0756 | -59.96328 | 2025-08-15 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 918aa76c-28df-379c-951a-0da8048085d5 | -7.05871 | -59.21182 | 2025-08-15 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 9d491084-0a18-3dbd-925f-78f670a1fe2f | -7.95442 | -63.46556 | 2025-08-15 01:28:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |


[Clique aqui para ver as próximas entradas](README11.md)
