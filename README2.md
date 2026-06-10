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
| b54ca8f4-b314-3b21-b667-ffd2475c3b2a | -11.5691 | -56.299999 | 2026-06-10 00:05:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fbc7cce5-ba8a-32d2-a99f-246ef6489e47 | -12.4039 | -47.4897 | 2026-06-10 00:05:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5b6259a2-15eb-33b2-87bc-c91d4c9ce68c | -9.3151 | -45.484901 | 2026-06-10 00:05:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c0d32095-45c8-30a5-8ce6-e3d1cc5f6716 | -7.7192 | -44.562698 | 2026-06-10 00:05:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 27cfd9c3-66cf-3747-8abf-ced00e386342 | -10.0096 | -48.2052 | 2026-06-10 00:05:00 | METOP-B | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e14af775-6ae5-3289-b21e-fd6ec60b38ad | -17.4261 | -43.807098 | 2026-06-10 00:05:00 | METOP-B | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 35a37386-0c87-36fd-b599-c22018ca8168 | -9.0819 | -50.596699 | 2026-06-10 00:05:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0baa5b9-3daf-37db-8144-f489364c9418 | -3.4996 | -48.026501 | 2026-06-10 00:05:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 850281d3-8e9b-37bb-b9a3-3c08c68e2e8e | -7.0905 | -46.508 | 2026-06-10 00:10:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| b3976955-3fbf-3c2f-b02a-9bfd3d50c592 | -7.1092 | -46.5065 | 2026-06-10 00:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| cee8247b-a8b8-35d7-a6bc-2e331399ed6c | -9.3045 | -45.4809 | 2026-06-10 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 5eed927b-565b-3c16-8724-cdd6562a6a6b | -9.3048 | -45.4581 | 2026-06-10 00:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 53.6 |
| da991501-e4f1-3eaa-bb09-ca308b34a926 | -9.3152 | -48.9599 | 2026-06-10 00:10:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| f075854f-adbd-31e0-b486-611fcf5ed751 | -23.4409 | -47.7856 | 2026-06-10 00:10:00 | GOES-19 | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.1 |
| 00c5953e-ff17-3b4e-bdb2-fba20349718d | -9.3234 | -45.4787 | 2026-06-10 00:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| f5996720-385b-3ef4-a773-facab1e453f6 | -7.109 | -46.5287 | 2026-06-10 00:10:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 44cf82fd-26ab-3da6-9c47-4b53ebe3bb8e | -7.1092 | -46.5065 | 2026-06-10 00:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| c96b1623-dab9-307f-982b-c6418476359d | -9.3045 | -45.4809 | 2026-06-10 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 68fe8e6c-b67d-3048-b4f1-172d1041b67b | -7.0905 | -46.508 | 2026-06-10 00:20:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| d7bc8e90-808b-33c1-827d-6d35cceb2768 | -9.3234 | -45.4787 | 2026-06-10 00:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 23fcae44-c2c0-3017-9b77-ef49e116107b | -21.3202 | -48.54067 | 2026-06-10 00:24:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 834f8e57-9fd2-3712-a9c5-fa1bf8171a71 | -13.95778 | -46.18885 | 2026-06-10 00:24:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| dc0b4a21-a84e-3b87-b58a-5617259bdd99 | -15.18118 | -43.86202 | 2026-06-10 00:24:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 4d3ed238-1ea9-3101-acac-4eb1422649bf | -23.4411 | -47.79059 | 2026-06-10 00:24:00 | TERRA_M-M | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.6 |
| 0d96a2e9-81c0-3841-b5d4-4c63c3fccb72 | -23.44269 | -47.80114 | 2026-06-10 00:24:00 | TERRA_M-M | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 5f167709-84a9-31ac-be77-883cef9065c9 | -15.1775 | -43.86914 | 2026-06-10 00:24:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 26.6 |
| efe0416f-f526-3bf9-90b4-754696d26622 | -18.9563 | -52.4638 | 2026-06-10 00:24:00 | TERRA_M-M | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3dbb58f3-cef5-3eb1-b59b-76bb739ce060 | -17.42745 | -43.80951 | 2026-06-10 00:24:00 | TERRA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 20.4 |
| a34139f5-106e-3831-b5e1-83afbe89d442 | -14.36884 | -45.5601 | 2026-06-10 00:24:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f75b40e7-911d-3b3d-beb4-fec26d15ebde | -18.68511 | -52.71323 | 2026-06-10 00:24:00 | TERRA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 68af0868-cbbb-3ea2-bc46-5f83d04b992d | -15.17314 | -43.84357 | 2026-06-10 00:24:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 23.6 |
| aa8359c6-dca8-3ca6-8719-aab69244af72 | -23.43183 | -47.79227 | 2026-06-10 00:24:00 | TERRA_M-M | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 704335a3-5243-3b77-932c-62f8abfa5baf | -11.50935 | -56.12516 | 2026-06-10 00:26:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ee14a933-993c-3fdc-ad9e-6ee89b4810ab | -11.33422 | -51.40081 | 2026-06-10 00:26:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2737ce70-2580-37b9-b108-7935f97f4840 | -10.67295 | -51.74619 | 2026-06-10 00:26:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fc1f7997-0e96-368e-9ab8-e3e3f48e1d29 | -11.57374 | -56.32444 | 2026-06-10 00:26:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5cba82cb-6a47-3c20-b1d4-1f865af79b95 | -9.3106 | -48.96926 | 2026-06-10 00:26:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| db25a156-dd83-336c-b1bb-75fe35a0b7f9 | -7.09765 | -46.52459 | 2026-06-10 00:26:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 129.6 |
| c8fe0cb4-a3cb-3af8-aed0-24f124409e31 | -11.16828 | -44.69223 | 2026-06-10 00:26:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 1a43d53e-a709-3039-b7ee-165c71514a58 | -11.7912 | -56.99267 | 2026-06-10 00:26:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 4017351a-73e0-3e03-90df-e78ad7662d6b | -12.40405 | -47.50406 | 2026-06-10 00:26:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 21e3171f-06a0-3d14-8296-9a545ed07a6b | -9.32081 | -45.48218 | 2026-06-10 00:26:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 6dc186f4-369e-3e36-8416-5ebeb68adbfd | -9.20804 | -48.58408 | 2026-06-10 00:26:00 | TERRA_M-M | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 45063a54-996d-3035-ba07-70ed0e7a28f0 | -9.13911 | -47.99076 | 2026-06-10 00:26:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 9ccecf4c-8016-387b-ab8e-ad25b3b5a7f1 | -8.30179 | -48.23149 | 2026-06-10 00:26:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 0ce6c3af-28d9-3e5b-b4d8-803e614119cb | -9.30692 | -45.48471 | 2026-06-10 00:26:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 113.0 |
| d3272c29-d0ff-3a33-86d3-2d64262f0581 | -5.72859 | -49.10862 | 2026-06-10 00:26:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| b4f13f3d-7e8e-3553-9da4-e1f77d8ebf08 | -9.11411 | -47.96815 | 2026-06-10 00:26:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7d940ccd-af9c-3465-8ba8-f9a07fe81433 | -11.60195 | -55.34084 | 2026-06-10 00:26:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 6fb3fc27-d04d-38f0-9f0b-5fc7a09f9eda | -11.62363 | -55.1782 | 2026-06-10 00:26:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f27d5fc1-8687-33d3-880c-9d8ccd803449 | -5.75801 | -46.04284 | 2026-06-10 00:26:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 7b0d3e4e-8ef2-34e5-83a3-0e896d983853 | -13.49827 | -54.30605 | 2026-06-10 00:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| cdb6a65a-f81f-3a34-bfa6-4c0ac4e80e27 | -11.57528 | -56.33693 | 2026-06-10 00:26:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 5f00ed35-85be-33dc-b446-1dc7a7b09e42 | -7.11101 | -46.52242 | 2026-06-10 00:26:00 | TERRA_M-M | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 62ecb423-bf75-3aa8-b334-d1607cd9245b | -9.32473 | -45.50647 | 2026-06-10 00:26:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 957a9e8c-3109-3b4e-b508-22934f8f1b7b | -13.50761 | -54.30474 | 2026-06-10 00:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 31130d9a-84ad-3308-a0c5-41218581ead7 | -10.01435 | -48.213 | 2026-06-10 00:26:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b8226845-6923-32ee-ac72-aaf83c5dd2f9 | -5.76916 | -46.04778 | 2026-06-10 00:26:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 7bbcfb7a-61e4-3a90-af10-de421a8b7e5d | -12.02481 | -47.80973 | 2026-06-10 00:26:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 88c5918a-74a5-3596-986b-731c0b0e4eff | -9.77475 | -49.74793 | 2026-06-10 00:26:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 41372807-25d0-3965-ba1c-7d3d9301feee | -11.38196 | -47.82319 | 2026-06-10 00:26:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| bd07f6a8-65cd-3b6e-bd9e-21f8ff5c90e2 | -9.31254 | -48.98219 | 2026-06-10 00:26:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 37681a0a-e966-3991-993e-e36fe11fcbc7 | -11.56714 | -56.33102 | 2026-06-10 00:26:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| d0ef396f-c964-348a-9f67-669f61b34f9e | -7.21637 | -44.10892 | 2026-06-10 00:26:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 400e0378-43ac-33c9-a4ea-7bcb4e8a15cc | -11.3819 | -47.81667 | 2026-06-10 00:26:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 04b2f5fc-d103-348b-91be-fde6e8f2fd9f | -11.16577 | -44.69824 | 2026-06-10 00:26:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 4b5fcb63-5200-3bb4-83fa-193e2479fb86 | -9.75541 | -47.88062 | 2026-06-10 00:26:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b1444db8-9fe9-3cf5-9fcc-cf4e98107936 | -12.47215 | -55.11852 | 2026-06-10 00:26:00 | TERRA_M-M | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 913b1d06-b36c-3c24-9388-108e38491767 | -9.74618 | -47.88834 | 2026-06-10 00:26:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4d8ea704-3daf-3548-ab67-5c25140eecbb | -9.08037 | -50.60062 | 2026-06-10 00:26:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ac3bea1c-4ae7-34cb-a445-6cf7f4f30e1e | -5.72643 | -49.094 | 2026-06-10 00:26:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 5b0d3c78-b4e2-3408-a729-50dbc02c893c | -7.2088 | -44.11537 | 2026-06-10 00:26:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 1da7f414-0ad7-3b6e-9563-b9c6360f1b57 | -8.97691 | -47.98085 | 2026-06-10 00:26:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| bb8c904a-6225-3df4-bfb3-c619656d3d99 | -7.09427 | -46.50272 | 2026-06-10 00:26:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| d234860e-7855-3f4b-80e3-759366c207da | -9.44114 | -47.64038 | 2026-06-10 00:26:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 1764e9b8-97e0-3f52-add3-e95698f8cf62 | -9.11133 | -47.96305 | 2026-06-10 00:26:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9d3b09e9-f999-3392-b422-3229a025e479 | -10.67424 | -51.75534 | 2026-06-10 00:26:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 306ef874-ccc0-3f9e-b7b9-c6582724e588 | -12.02552 | -47.80344 | 2026-06-10 00:26:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| ae5ebb2f-f061-3163-9807-94e8ac2d2db1 | -3.80814 | -49.18841 | 2026-06-10 00:28:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 4fe10170-db31-33b8-baf4-1c99c44955a1 | -3.50897 | -48.03512 | 2026-06-10 00:28:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 8f581c6c-e600-3058-9884-0b5cdaccdfc5 | -3.50827 | -48.04152 | 2026-06-10 00:28:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 714f8fd6-9c46-370e-a8e9-3c6e0c1ff81f | -3.4963 | -48.03669 | 2026-06-10 00:28:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| af544334-f3f3-3b4f-bf66-2d8407b7b2cc | -7.106 | -46.5224 | 2026-06-10 00:29:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 706ca10d-7e97-3436-8483-9b5654ba3d04 | -3.5045 | -48.040001 | 2026-06-10 00:29:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88e101b2-caca-370e-898b-94fb36e6da7d | -5.3017 | -47.243599 | 2026-06-10 00:29:00 | METOP-C | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fa78be2c-143a-3082-ba7c-d92128c4fc97 | -5.2884 | -43.9659 | 2026-06-10 00:29:00 | METOP-C | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e101992c-2e33-3152-a4d0-bfde7103ece8 | -7.1029 | -46.508598 | 2026-06-10 00:29:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7e5a8cf0-9076-34d6-89c2-232cd4a007ef | -5.8032 | -45.115601 | 2026-06-10 00:29:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4e458d1-c621-3166-b70e-4e93e384ee1e | -5.7691 | -46.041199 | 2026-06-10 00:29:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6417ba99-f9a9-3b2b-8b2e-cd2dc5339f21 | -7.1044 | -46.515499 | 2026-06-10 00:29:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c603cae4-9371-38bc-8678-b51ec6ddd98b | -5.7707 | -46.048199 | 2026-06-10 00:29:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8850b73c-f3c2-3a43-af40-bb9c062b1afa | -3.8049 | -49.181801 | 2026-06-10 00:29:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db4f3f3c-bce4-36f3-a5f8-d9a0f6170b93 | -5.2865 | -43.957699 | 2026-06-10 00:29:00 | METOP-C | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30ddb9ba-97d4-3b4c-a130-29622f89aae9 | -3.5029 | -48.0331 | 2026-06-10 00:29:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77e23d10-8c4b-3a8b-bc2c-98446bca4c10 | -4.5732 | -48.027599 | 2026-06-10 00:29:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 268d1a31-b119-307f-89f0-bbbd64e3e5ad | -5.6438 | -44.295898 | 2026-06-10 00:29:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f87a89f-a178-3423-955b-3283959c108a | -5.642 | -44.288101 | 2026-06-10 00:29:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c6abd2e-9573-3b9e-bf85-60df981daebf | -9.3234 | -45.4787 | 2026-06-10 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 522085b5-24b5-377c-b430-ed4bac720a5a | -7.1092 | -46.5065 | 2026-06-10 00:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 79feded5-5e42-3c36-a9c4-ec01ef38d8bd | -7.0905 | -46.508 | 2026-06-10 00:30:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |


[Clique aqui para ver as próximas entradas](README3.md)
