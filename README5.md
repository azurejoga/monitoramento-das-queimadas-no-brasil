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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b1f1657-64b1-384c-90dc-0c3b4d40e263 | -10.8671 | -43.9428 | 2025-10-19 01:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 42e3e108-1b9e-3cc9-9961-570ab74b2df3 | -5.3105 | -44.8423 | 2025-10-19 01:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 479e7f2f-1006-3e08-95da-885eae34169d | -9.14004 | -61.46099 | 2025-10-19 01:32:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 71a1ad59-c693-3eb9-9e07-ddce82b89582 | -10.04607 | -59.36974 | 2025-10-19 01:32:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 0d7fd32a-913a-38e1-8111-ff395ed0a427 | -10.93982 | -60.92846 | 2025-10-19 01:32:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 5859c1bd-f03a-376a-999e-909cf717d9db | -7.41685 | -63.74654 | 2025-10-19 01:32:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bcf26ab0-4809-3728-817e-320a318ac51b | -9.64106 | -65.2497 | 2025-10-19 01:32:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| dab15cee-91f1-320b-b311-26f3bc292cdf | -9.73589 | -65.88728 | 2025-10-19 01:32:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.5 |
| e8c0e0f4-b3d5-36c1-8a4d-16c2fd31bc6e | -9.96867 | -63.73425 | 2025-10-19 01:32:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b215398d-b3cf-3bf2-897d-6cdbf3b05046 | -9.59513 | -63.50389 | 2025-10-19 01:32:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0c28d983-80be-3fbe-9a0f-de0de70ffee9 | -7.85996 | -61.59979 | 2025-10-19 01:32:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3be33741-13a6-3e6d-b854-646b7b4360a0 | -9.1128 | -65.35988 | 2025-10-19 01:32:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 7fa8da31-f3e7-3931-83b2-46c74d356dfc | -7.62988 | -60.92862 | 2025-10-19 01:32:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 888429aa-f730-3628-a188-8a4eb577b03f | -9.91704 | -64.09337 | 2025-10-19 01:32:00 | TERRA_M-M | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| dc47c7c8-937c-3107-a7bc-8c50e292781d | -7.62501 | -60.96485 | 2025-10-19 01:32:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 444660ae-d80d-3459-85e1-547edc18479e | -10.04129 | -59.3628 | 2025-10-19 01:32:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 09d4883b-a063-3ea5-9369-4d05afa9bb18 | -9.91581 | -64.08444 | 2025-10-19 01:32:00 | TERRA_M-M | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 11407a66-0663-33ef-a041-9274114401ab | -7.12594 | -63.05207 | 2025-10-19 01:32:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6a7d8300-2ac3-3d17-8724-7bb29bb9a2bb | -9.18218 | -61.38457 | 2025-10-19 01:32:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7aca440f-6da1-3943-a798-e44c11e1c706 | -9.64233 | -65.25911 | 2025-10-19 01:32:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 8f7517d4-7228-3187-8044-a0eade431f22 | -9.11407 | -65.36927 | 2025-10-19 01:32:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 2fd187f0-c04d-3469-8b04-665939da94e7 | -9.85448 | -68.11343 | 2025-10-19 01:32:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 6960ad31-cacb-3ab9-891b-7e4ba4c6ccfb | -7.61986 | -60.93013 | 2025-10-19 01:32:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 3deeccc2-f3c3-3899-87ea-88d64ec97c9f | -11.75706 | -61.07308 | 2025-10-19 01:32:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 783646d9-664c-3c6a-b754-1269a2e362c8 | -9.19172 | -61.38316 | 2025-10-19 01:32:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 8d44ed8d-a1d9-3e0c-a4c1-2acb427ee83a | -10.93184 | -60.94057 | 2025-10-19 01:32:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0a33215d-898d-342e-9f5a-d58d961e59c3 | -10.04393 | -59.356 | 2025-10-19 01:32:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2c2379c8-c996-3116-9c33-b7489a95ca04 | -9.12186 | -65.35863 | 2025-10-19 01:32:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 826792b3-eb9d-3671-a469-4a3cc754c12d | -7.62158 | -60.9417 | 2025-10-19 01:32:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| c2956dd5-633e-3f5e-af60-fe8389805042 | -9.232 | -63.60813 | 2025-10-19 01:32:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 738a742e-8506-3fe8-94da-cf8e75d9c258 | -10.0331 | -59.35761 | 2025-10-19 01:32:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| df5d77c9-5f01-3a92-921a-c9e5b34da863 | -9.12313 | -65.36801 | 2025-10-19 01:32:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1be2948f-342d-3d36-9b16-ba565895b98e | -10.93025 | -60.92994 | 2025-10-19 01:32:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 7aeaa4c5-f715-3756-8014-20c43aece26c | -6.52753 | -60.03484 | 2025-10-19 01:32:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| fec5744b-b8a6-3c35-97f3-069956fc87b8 | -9.19324 | -61.3936 | 2025-10-19 01:32:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5c9f3b49-b4c1-3d84-91e5-5306e680949e | -9.58863 | -64.31959 | 2025-10-19 01:32:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4428aa6f-493e-3861-997a-94f922f96992 | -10.9414 | -60.93907 | 2025-10-19 01:32:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| f9d29210-79b4-3c92-80b0-b9d75217588b | -9.31207 | -60.87712 | 2025-10-19 01:32:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| cc297f75-fbc7-30a7-bc81-29bbe26510f1 | -7.61813 | -60.91852 | 2025-10-19 01:32:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f1bb74c1-2ffb-36f0-8f97-0f3b05748b8e | -9.5863 | -63.50518 | 2025-10-19 01:32:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d60fa7aa-6160-3201-97ef-9cf8c9c6fdce | -7.12463 | -63.04281 | 2025-10-19 01:32:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| aa202a9c-2cf1-358d-b95c-06f95f0f3879 | -7.6233 | -60.95332 | 2025-10-19 01:32:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 8c9a992e-dfcc-32cb-8939-00c65480c774 | -6.64544 | -62.9146 | 2025-10-19 01:34:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9bd522b7-03a7-39cd-a84f-0880bd7963c3 | -6.6307 | -62.81052 | 2025-10-19 01:34:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 50f0c636-e34f-3edd-911a-a6436fcd4eb9 | -2.9128 | -52.7146 | 2025-10-19 01:40:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| d3ae953e-64dd-31e2-9298-a12ad5e1ceca | -2.9127 | -52.735 | 2025-10-19 01:40:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 581000ca-507f-3f5c-a65a-bd14700ec25e | -10.8891 | -46.0814 | 2025-10-19 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 16b18fd7-577c-3c25-b3c9-0b62b756d30a | -8.6219 | -40.2058 | 2025-10-19 01:40:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 70.1 |
| 8c4226e2-0ea8-3359-9a54-805d33cd96a7 | -12.4493 | -45.4262 | 2025-10-19 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| ef71f19c-d240-39d5-88a1-ed6057c9a801 | -14.4759 | -45.5751 | 2025-10-19 01:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 27e0cbd1-9296-398f-929b-67db44980fde | -5.3086 | -45.0695 | 2025-10-19 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 8b3f2ae7-96aa-3dc6-bad0-9e5f405da4f2 | -5.3105 | -44.8423 | 2025-10-19 01:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| ff08eae1-6922-3f3f-ba3a-5228f4debb5a | -2.7026 | -49.5422 | 2025-10-19 01:40:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| a45a34e6-887e-3c33-902a-581cff9f3bb6 | -14.4949 | -45.5949 | 2025-10-19 01:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 41b93d7a-2d1b-3b5b-b5cb-351a5801727f | -10.5522 | -43.3761 | 2025-10-19 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 95b9fd72-be00-35c8-b634-57bfe9c70ee2 | -11.6301 | -44.0649 | 2025-10-19 01:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 656e68e3-fecb-37ba-9e82-ebf45d6d414c | -2.6841 | -49.5427 | 2025-10-19 01:40:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 012d185b-3098-3ca5-ab89-ecb085db01a1 | -7.6238 | -60.9212 | 2025-10-19 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 3fee1fa7-b650-3d09-a1f5-6225b0c52467 | -11.6109 | -44.0678 | 2025-10-19 01:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| b9463fe3-06af-315b-bcbc-057003175e18 | -8.6223 | -40.1809 | 2025-10-19 01:40:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 85.8 |
| 2085bb27-955a-3e8e-9fbb-9a2c900b1df7 | -16.1528 | -41.1524 | 2025-10-19 01:40:00 | GOES-19 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.1 |
| bf08ed62-a31f-3816-b11e-e14fbf437074 | -11.6113 | -44.0443 | 2025-10-19 01:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 8fc69e7e-6acd-3d87-bdbc-29ce02a95364 | -5.3291 | -44.8411 | 2025-10-19 01:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 57951e2b-8ce6-391f-ada5-e061b42e8f38 | -7.6237 | -60.9403 | 2025-10-19 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 114d8b77-1c10-39c7-a8f3-3a715c7db3f2 | -5.6283 | -44.8205 | 2025-10-19 01:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| b78954a7-1cb2-3e77-b848-82da94abf5f5 | -13.5405 | -43.0077 | 2025-10-19 01:50:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 71.5 |
| b2ae0012-b6a1-3642-9b73-1ea4f342afad | -10.5522 | -43.3761 | 2025-10-19 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| b5d49693-8ff4-3c8f-932c-6a8254f7b212 | -8.6223 | -40.1809 | 2025-10-19 01:50:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 77.0 |
| 9e231738-876a-3691-90e2-ef1e0cc1c274 | -12.4686 | -45.4232 | 2025-10-19 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| f441b72f-01de-3bbf-91e3-1703b5372620 | -2.7026 | -49.5422 | 2025-10-19 01:50:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 868a338e-ed6d-3810-af58-55449ff3616b | -16.1528 | -41.1524 | 2025-10-19 01:50:00 | GOES-19 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.5 |
| ce5ddec3-b2fc-3154-a53c-96e591d857c5 | -5.6472 | -44.7964 | 2025-10-19 01:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 125.0 |
| c5c9840c-1555-3eb2-ad79-97457db0798e | -16.7641 | -42.7467 | 2025-10-19 01:50:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 492daf1a-5919-32f8-8b3b-24abe56d5f93 | -16.7635 | -42.7714 | 2025-10-19 01:50:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 62c23fb8-a4dd-3e70-be70-65b13a449617 | -2.9127 | -52.735 | 2025-10-19 01:50:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| f8d1d2ea-b841-3d02-9340-b93befa59b9a | -2.9128 | -52.7146 | 2025-10-19 01:50:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 0d55ba5c-961a-39a3-b9b3-e3815cdc8a21 | -12.4493 | -45.4262 | 2025-10-19 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 0ac65a1e-1942-3605-b691-4dba305a8cee | -5.6285 | -44.7977 | 2025-10-19 01:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| db4035f8-fed8-399a-9d55-862e07ce08b6 | -8.6029 | -40.2083 | 2025-10-19 01:50:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 59.2 |
| 0c01054e-9ac0-3c09-8249-2d77da01e147 | -10.8891 | -46.0814 | 2025-10-19 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 1a455a02-31bb-35b8-8260-a3730c8e8826 | -2.6841 | -49.5427 | 2025-10-19 01:50:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| fb0d89da-f688-3c37-ab2a-e1a80bd49cce | -8.6032 | -40.1834 | 2025-10-19 01:50:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 103.8 |
| 749b262c-21c8-34bd-99da-25ac4abc59dd | -16.7834 | -42.7668 | 2025-10-19 01:50:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 55b4e7cb-fd8c-37e5-ac90-68acd3d56f50 | -5.647 | -44.8192 | 2025-10-19 01:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 675e0ccf-e594-306c-8733-d63f8f91155a | -5.3086 | -45.0695 | 2025-10-19 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| a8387da6-b712-31b4-ae6c-e888c41f7c9c | -5.3084 | -45.0921 | 2025-10-19 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 914299e8-a368-3458-bd5f-e15534e13e95 | -7.6238 | -60.9212 | 2025-10-19 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 385dfc4c-1c67-3dae-afb0-501638321f56 | -2.9312 | -52.7142 | 2025-10-19 01:50:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 0ebe52d2-977d-337b-a8b1-2fb7f2cc3e26 | -8.2476 | -43.9903 | 2025-10-19 01:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| a436de2d-ab9b-309e-8576-ee4f25d67a02 | -14.4759 | -45.5751 | 2025-10-19 01:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 45e41696-850c-309a-a4de-df9f939f1186 | -5.1017 | -47.79 | 2025-10-19 01:50:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 7b88b5eb-d3d5-3c26-8ee7-08ba71f6b890 | -11.6301 | -44.0649 | 2025-10-19 02:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| d95d3e19-1668-3c2c-8ba9-64cd6665391c | -10.8891 | -46.0814 | 2025-10-19 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 6d27db25-5773-385b-bb81-f2a19d9e6e70 | -13.5405 | -43.0077 | 2025-10-19 02:00:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 8764e562-e3bd-36b3-8264-fbef1805cd3a | -2.9127 | -52.735 | 2025-10-19 02:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| d07f2212-341b-389f-8c34-f100b797fd26 | -11.6109 | -44.0678 | 2025-10-19 02:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 52c15f4b-67da-3905-9197-cad8a410a2bc | -7.6238 | -60.9212 | 2025-10-19 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 8a518377-1e9d-3d37-8987-735343459fb6 | -5.3086 | -45.0695 | 2025-10-19 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| d5c6c464-9337-3c8f-b330-9f919969ea26 | -16.1528 | -41.1524 | 2025-10-19 02:00:00 | GOES-19 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 46.7 |
| 82b5f84c-3cb5-3a8a-906d-1c2a41c13172 | -2.9128 | -52.7146 | 2025-10-19 02:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |


[Clique aqui para ver as próximas entradas](README6.md)
