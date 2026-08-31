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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99d9feea-8f60-3b8f-8941-49ef45d09eaf | -3.6398 | -60.5656 | 2026-08-31 14:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 88.1 |
| d8a4c497-9bf8-38a3-8d51-39aac29ed864 | -7.5659 | -61.362 | 2026-08-31 14:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 0c97cfc2-b8b0-3b6e-8ef5-a0df942b4464 | -15.2669 | -53.8851 | 2026-08-31 14:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 165.5 |
| fd49026d-7d8d-387f-ae58-fa83d6585c47 | -10.7409 | -54.0196 | 2026-08-31 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| d630f706-ca98-3209-8d92-7ffaa4260695 | -11.0244 | -49.6872 | 2026-08-31 14:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| a83a6501-c1e6-3d9a-a8a2-13b9be54ffa5 | -5.2363 | -55.8914 | 2026-08-31 14:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 12ac9ee0-54b8-38e6-8801-0e132072e7d7 | -14.1263 | -52.8106 | 2026-08-31 14:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 6693294b-9c95-30ec-80e4-044078773659 | -14.4394 | -52.5176 | 2026-08-31 14:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 211.3 |
| 2c7912ad-1dae-34ef-b943-ea6c9d048c60 | -5.8783 | -59.9726 | 2026-08-31 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 9fc0500f-39eb-3d39-b5ab-9028b0d787d1 | -10.7596 | -54.0384 | 2026-08-31 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 167.6 |
| 0d9ddc49-2ecb-3f67-835b-d91635b27c4f | -11.0933 | -51.5345 | 2026-08-31 14:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| e9cfc4f0-2ada-36b6-983c-6f090f33b6f6 | -11.2314 | -54.0164 | 2026-08-31 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| d26cbd93-fa03-36d4-8977-4e9ccc45be5e | -3.6216 | -60.547 | 2026-08-31 14:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| ccd67fec-743d-39ef-8217-2c9f43bea921 | -11.0744 | -51.5365 | 2026-08-31 14:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| d59bcef0-1950-3c0d-95ae-03e6400b5c1f | -18.27 | -52.7068 | 2026-08-31 14:50:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 165.9 |
| 3a617eb5-b948-32cf-972d-f1bba22a98d3 | -13.9474 | -54.4179 | 2026-08-31 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 195.6 |
| 43facbde-23d2-34f9-8900-6ccbf44926d9 | -6.912 | -59.4927 | 2026-08-31 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 8df73f85-640b-315f-b489-67c422a67f50 | -6.8027 | -43.5521 | 2026-08-31 14:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 99493795-782e-3951-a6a5-2b1ad96aa5ef | -8.7631 | -46.4418 | 2026-08-31 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 401.9 |
| 56d112a4-929b-3c56-815e-54ab7e6eee50 | -13.394 | -51.7808 | 2026-08-31 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 052ea733-3142-34f3-a221-0f409451d6ed | -9.5967 | -47.5983 | 2026-08-31 14:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 187.2 |
| 80081f12-ba60-3648-8b3a-32c5a7f3432d | -9.5961 | -47.6424 | 2026-08-31 14:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 26ea8610-f3b9-3fd1-8a92-edd841541041 | -11.0247 | -49.6656 | 2026-08-31 14:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| bbe38bc9-4004-32c4-ab6d-1a71601c4c06 | -15.6336 | -56.3876 | 2026-08-31 14:50:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 79cfc565-a7ed-3369-826f-e01360b25cb0 | -10.8617 | -50.4772 | 2026-08-31 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 2f1cdcb6-9476-30de-8a84-a3eea50a2f86 | -19.4706 | -57.5636 | 2026-08-31 14:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 128.7 |
| 9be074be-a7ee-391f-aabf-9caf607b39d6 | -3.1998 | -61.161 | 2026-08-31 14:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 570215ba-2248-3ed9-aaaf-270a599d5bfa | -7.9239 | -44.2327 | 2026-08-31 14:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 161.5 |
| edeba11e-e5f6-34d6-98af-d7595c90f03d | -15.8649 | -56.4841 | 2026-08-31 14:50:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 3e1d77fc-046f-352a-95df-8a744b43e4b4 | -10.1538 | -45.6982 | 2026-08-31 14:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 123.4 |
| d89c8035-3bc1-35a4-b545-c8558ce615c5 | -5.5832 | -60.2116 | 2026-08-31 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 7c2c1a08-8616-3061-ada1-46ba1b323924 | -13.4324 | -51.776 | 2026-08-31 14:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 51df4661-005d-3f8a-8b3b-c7b61dd23e2d | -15.2478 | -53.8666 | 2026-08-31 14:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 6b2bc827-9011-3afe-b267-57e6b1b57086 | -4.1515 | -60.7068 | 2026-08-31 14:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 987c7d23-4cb2-3eb8-8948-3e2b67b5e25e | -14.5871 | -54.0944 | 2026-08-31 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 114.1 |
| c21c5ac4-9c94-3ecc-bdf3-3c3247598b0a | -10.1528 | -45.7665 | 2026-08-31 14:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 252.6 |
| 3e224582-4530-3b41-9325-9a3e818601a8 | -3.6215 | -60.566 | 2026-08-31 14:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 130.2 |
| fb0570eb-c0fb-3872-bd05-a937a396a968 | -5.4876 | -57.1416 | 2026-08-31 14:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 2d0a4ec2-137e-384a-a998-0e6900073322 | -6.9177 | -55.6967 | 2026-08-31 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| f6de8be8-5f86-340c-aaaa-33c868a8a530 | -7.3478 | -55.1744 | 2026-08-31 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| f6bb797c-4a96-3c6d-a089-712771549fc4 | -8.7442 | -46.4437 | 2026-08-31 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 236.3 |
| 9cb40600-76fc-30bb-af4a-4d1dddac12f0 | -10.1084 | -50.299 | 2026-08-31 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 245.2 |
| 29eb93e4-de6f-3e8c-baab-368ff3833beb | -10.7593 | -54.0589 | 2026-08-31 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 4fcfd372-dee7-37c9-bfab-ff98cd5a38f5 | -7.9907 | -46.5177 | 2026-08-31 14:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 3c2c117d-d9ae-3167-86f4-f9ce4c5bf1bd | -15.346 | -53.7912 | 2026-08-31 14:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 173.6 |
| ec83a566-77cb-38a8-9d28-ae619182b025 | -10.7598 | -54.0179 | 2026-08-31 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 46510454-3780-3948-bd2c-4ca43a0d7bdb | -15.8844 | -56.4819 | 2026-08-31 14:50:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 119.7 |
| cbc1671f-6c2c-3063-85b7-d4adcb7f631f | -14.5868 | -54.1153 | 2026-08-31 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 142.9 |
| beedb4d8-da78-3cc9-bb3f-96b97785181f | -10.9177 | -50.5352 | 2026-08-31 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| ac228b4b-4c28-3b9d-aa7d-e990aeeeabb0 | -18.2695 | -52.7284 | 2026-08-31 14:50:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 85a72445-bf53-3912-b740-0733995e281e | -14.4197 | -52.5413 | 2026-08-31 14:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 96e61e67-00ba-30e5-b559-430f42785357 | -13.4707 | -57.0574 | 2026-08-31 14:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| b961fa57-227d-3bfc-948c-7c1abdb77a8e | -11.5283 | -45.4933 | 2026-08-31 14:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| cef69edc-c184-30a0-ad98-119ccff525f9 | -9.2092 | -51.5654 | 2026-08-31 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 9924c2b7-daf5-31ec-8bd3-7c6d45c1375a | -14.2792 | -52.8758 | 2026-08-31 14:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 3890dab9-c36e-3c51-a857-d769965a192a | -13.9667 | -54.4157 | 2026-08-31 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 485.6 |
| d7e875af-5b61-3070-9a14-fb2c28383c3d | -3.1997 | -61.1799 | 2026-08-31 14:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| bc3b34b2-0cd6-3424-8227-7a99c83b879f | -10.7428 | -50.8727 | 2026-08-31 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 2151d814-f3d4-3bdf-85e5-924a348a9ae9 | -9.7875 | -59.4285 | 2026-08-31 14:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| a3c156a4-fcef-3bcf-9420-86c10bb73fec | -9.4342 | -45.6704 | 2026-08-31 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 4d942d65-295b-32b7-82b4-f765523dea01 | -11.2295 | -51.2667 | 2026-08-31 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| ca6b36f9-42c4-3bb1-a5df-08d86815066d | -10.9675 | -48.3891 | 2026-08-31 14:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 167.6 |
| acfe5850-7411-37d7-9a9a-158f4075ae2b | -8.799 | -62.4905 | 2026-08-31 14:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 7de78f79-0902-3bed-9f7d-5d948f748ca9 | -13.8563 | -54.0967 | 2026-08-31 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 147.8 |
| ae42f695-9559-3fda-ae7b-e357bbd2ea91 | -11.3423 | -45.1982 | 2026-08-31 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| b5ad5d4c-b9dc-3c9b-8687-fb0aee530d71 | -11.8215 | -51.0109 | 2026-08-31 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 4a29a860-aaa6-36c9-a997-92897f137a2f | -5.2362 | -55.9112 | 2026-08-31 14:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 251.1 |
| bdff60d4-0206-3780-a637-ca9da6c6bd8f | -6.9368 | -55.6161 | 2026-08-31 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 644bb13e-f311-3f61-b2c0-2ab772ac1c88 | -7.9236 | -44.2558 | 2026-08-31 14:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 121.4 |
| e2543201-2c16-3c87-86c9-c9e57c0b7726 | -8.7628 | -46.4642 | 2026-08-31 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 363.1 |
| 07e956fa-84e1-3b41-89f8-745f77da0e8c | -5.9636 | -57.6704 | 2026-08-31 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 5aa70acf-4811-36a6-9a0a-3153ee10e6c7 | -13.4379 | -51.4348 | 2026-08-31 14:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| c7a21aee-5614-35df-917d-c81e33c7e2dc | -8.7439 | -46.4661 | 2026-08-31 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 46b6b83b-2a5b-3354-ab3c-e9ec83838d5d | -13.8371 | -54.0989 | 2026-08-31 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 5f947d2f-5437-35fc-9943-1b6658adc213 | -11.0747 | -51.5153 | 2026-08-31 14:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 5e5fb7bd-04fc-35a7-ba1f-54131c3e336d | -10.9865 | -48.3869 | 2026-08-31 14:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 149.5 |
| a5b75213-88f0-3318-893d-dae88fb7e497 | -9.153 | -59.5415 | 2026-08-31 14:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 7a314e44-9b35-37f8-b8a4-98a2579b433f | -7.1123 | -42.7727 | 2026-08-31 14:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |
| 242ca3f1-a643-3f6c-882c-ceb77387e241 | -15.2275 | -56.3716 | 2026-08-31 14:50:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| e63fc48a-c755-312e-8850-8391c07b5f70 | -6.1109 | -57.684 | 2026-08-31 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 160.7 |
| 22d57c5a-d6d6-3da5-876d-377dad48e0db | -3.6399 | -60.5466 | 2026-08-31 14:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 6db44949-9ebb-3c5d-8ef3-3b202b1b099c | -13.4327 | -51.7547 | 2026-08-31 14:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| ad7c88db-921f-336f-a732-6cf9e9baa8c0 | -6.1295 | -57.6637 | 2026-08-31 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 142.8 |
| 7564a7a0-51b7-3a67-83d9-d61e13a3b663 | -10.1087 | -50.2776 | 2026-08-31 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| d19d5dcf-21b9-3ae8-a76f-9fd6fb4601c3 | -11.9186 | -45.0685 | 2026-08-31 14:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 171.8 |
| 38017195-aa5c-3635-b37d-27cf13567c05 | -9.6939 | -65.1145 | 2026-08-31 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.1 |
| aa6e80b5-9a36-35cc-8c30-378a9f79bb98 | -11.3427 | -45.1751 | 2026-08-31 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 19f890ae-135c-34da-969d-30e7f9163fb4 | -11.8506 | -46.7654 | 2026-08-31 14:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 201f124b-dcfc-3f52-b27b-33217ec61e70 | -11.0049 | -51.0787 | 2026-08-31 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| bfb067a2-fc13-3654-b831-ee4687383259 | -14.5674 | -54.1176 | 2026-08-31 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 5dd0b82c-0a23-3d6f-83cc-287bd230d7d0 | -15.2081 | -56.3738 | 2026-08-31 15:00:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 16f068fa-9fba-39ce-998f-be63731c0c3b | -8.7439 | -46.4661 | 2026-08-31 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 7e6b2e7e-93f8-314a-9cd1-56a4371886bf | -11.2125 | -54.0181 | 2026-08-31 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 652ca3b7-05db-34e1-bd66-56fa6be19308 | -13.8567 | -54.0759 | 2026-08-31 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 130.6 |
| aa2a7abe-1bcc-3715-837b-c6cb0e1047e7 | -8.7442 | -46.4437 | 2026-08-31 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 13ebfe90-c955-3e0e-ada6-18cc4dfdc4e6 | -14.5028 | -52.1913 | 2026-08-31 15:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 837af5f4-6b42-3bde-a12d-83941485fdd6 | -13.8384 | -54.0158 | 2026-08-31 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 104.3 |
| d4a0f337-c6c8-34cd-a414-988c1ab86b1d | -15.2475 | -53.8876 | 2026-08-31 15:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 94af18f9-9c4e-3518-9b99-807486019564 | -15.8649 | -56.4841 | 2026-08-31 15:00:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 67e81492-5a6a-3a74-a74f-f948a8953336 | -10.8212 | -50.6732 | 2026-08-31 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 129.8 |


[Clique aqui para ver as próximas entradas](README97.md)
