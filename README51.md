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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae53b58c-bd7b-3190-9eea-79096b9dcd4a | -14.20099 | -52.87945 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94d5c1d0-4f78-3ebb-8f7d-91fa8e8c93d0 | -12.95137 | -45.94487 | 2026-08-31 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 80f58118-e50f-3e7b-93b6-05059b82877b | -9.01328 | -65.40437 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d3741b3-70cd-3ba8-be8d-23e74a83fa41 | -9.92964 | -60.48462 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 253ed519-ed24-3a8b-bba4-ce786a2d833f | -15.66984 | -45.92871 | 2026-08-31 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e5faed93-79b9-3825-a0d4-a11fc5e5ae4f | -14.60237 | -54.09897 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e693f661-019b-30a0-8bc6-41013d919781 | -11.21975 | -45.14543 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea3dbb54-741c-3afb-8d89-f79961a8541c | -11.18686 | -55.10064 | 2026-08-31 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e9db499-e4cf-3ee5-bd37-4f2186290235 | -11.03719 | -57.24558 | 2026-08-31 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69e0c495-0724-3f75-96a8-4bd63a1317ec | -9.01421 | -65.40338 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2706fe4-6def-38ca-9bea-647708f4693f | -11.15566 | -50.5659 | 2026-08-31 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 73aacfb2-77d7-3e67-9c56-d14abd70e9d8 | -9.165 | -58.31166 | 2026-08-31 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3293c69-491b-3ed4-b9f2-63bed3507f97 | -11.69529 | -54.60198 | 2026-08-31 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ecca2a39-66fc-30e5-b7cb-31b067b28722 | -10.81542 | -50.65261 | 2026-08-31 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29dd1e54-0740-3f1f-ab88-38269d40342c | -13.36336 | -46.92116 | 2026-08-31 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a067e6f7-e7af-3eb1-b734-6265fdf51f61 | -14.17202 | -52.79615 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4831091d-d17b-36f2-b327-54b8ceb61fc4 | -14.23059 | -52.85322 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 24bbe7a6-5203-3266-83fa-cae2c6014ce5 | -10.15406 | -45.69729 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 792a1f9a-9ee5-3754-895a-b19616d3ee2e | -10.75154 | -54.0372 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57b5ddf1-2aea-3104-8b02-23c444122992 | -14.58024 | -53.07853 | 2026-08-31 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e59a61b2-ab82-3265-85d9-a3da34edd1ed | -11.78752 | -47.67231 | 2026-08-31 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5fa6df09-632b-33c7-ae04-f92841cfdf98 | -8.61656 | -54.7945 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea84c57d-d76e-3b11-9bf2-4abebbd14c64 | -13.17601 | -55.66582 | 2026-08-31 04:59:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87a6f7b3-466e-3216-9fe8-1a8beaa66634 | -12.91592 | -45.90997 | 2026-08-31 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2080cda8-68e4-3fb3-bba5-56f48135b55c | -15.20236 | -46.22805 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d5951f1-7444-3990-8f94-15255e2260b4 | -11.23835 | -45.13582 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3821b197-bc9f-35c9-9212-3024507ae504 | -11.49289 | -46.93286 | 2026-08-31 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eae4299c-1156-330c-8caf-6ac29e9053cf | -15.67386 | -45.93602 | 2026-08-31 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47aaa174-88e2-3eca-836e-5323117e724b | -14.40761 | -52.52926 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 40a76110-8bab-3cd4-8f00-714f39fc646e | -13.38839 | -51.78543 | 2026-08-31 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c889ccb0-5c61-3350-aa41-484a7bacbbcc | -12.40074 | -46.45467 | 2026-08-31 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 061d5990-407c-37c6-9585-b8fd11b2684c | -10.31515 | -58.08524 | 2026-08-31 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02286bbf-7563-3cbe-ad28-2e94402af2dc | -10.74771 | -54.0625 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b14ea4be-8817-3fec-9009-ef2c6e85f0f9 | -14.41054 | -52.5274 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a25259a5-245d-379a-82f1-79c380b486f6 | -12.13439 | -45.83801 | 2026-08-31 04:59:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5a75e8f-c5fb-31c0-8af3-dde81b4e6f96 | -10.14427 | -45.76049 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a3cfce96-e7db-32f9-80e6-8f30e69611fc | -9.41067 | -51.68699 | 2026-08-31 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9b867235-47a8-3dc7-90fb-c8c4e180fd2a | -7.55864 | -61.31487 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1c8dcc45-71db-3d90-91da-349c9d81105d | -9.14702 | -61.10298 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2362a196-aabd-38a2-b362-a1b9e7408285 | -10.83627 | -45.31574 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49c47338-6255-3142-a97e-2de419bbc2e8 | -14.58384 | -53.07909 | 2026-08-31 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f22fa0e3-1a03-3633-81d9-e4bd5dcffaa8 | -10.73702 | -54.04232 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d51fdafb-9f27-368b-9769-2d4c34dd304b | -9.84609 | -64.97908 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bb28c6e-11ca-3ffd-8d18-1cb480edaff7 | -11.47599 | -58.50729 | 2026-08-31 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fde4fad2-5651-3b60-8848-af5d83669b93 | -13.63938 | -51.83862 | 2026-08-31 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b27aa054-b588-3744-b9c8-129bfb0e79ef | -9.16585 | -59.50933 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f65bd985-df9b-3746-9154-a9b7f661987e | -9.84935 | -60.27227 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d7e6941-831d-386c-bfb0-6074b3f6a5f4 | -15.08939 | -48.10345 | 2026-08-31 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0e72f4ca-d9d1-35df-b187-763427464a22 | -13.18373 | -55.65983 | 2026-08-31 04:59:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| befc9815-3c58-37ca-9d20-a175f0f7f4b5 | -10.49254 | -59.60771 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d6c492b-b970-3d61-a5b9-ea998f275eaa | -8.68341 | -62.81743 | 2026-08-31 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2d76e0eb-c0e5-3a6e-9e1f-df49196e6fa7 | -10.75099 | -54.04081 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90ee26ad-34ab-394e-bb52-a7145a4a4117 | -11.16596 | -45.04733 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a7419dd-dc3f-3c95-8ce6-c70a40b0d2ec | -14.14014 | -52.80654 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fe02eb8-fcc1-3600-8c29-de017a5a2ec6 | -15.19507 | -46.24309 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24c452d7-374e-33e7-85d5-f93a5f945d98 | -10.48462 | -59.61883 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aec2661d-7063-3211-891a-a2e44ab0d4d2 | -11.3521 | -45.21858 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1a1c8a89-f72d-3a1b-b470-420cbb82ab21 | -9.01344 | -65.40744 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 934a0931-8872-36f8-a911-0d1bc648024a | -15.66325 | -45.92661 | 2026-08-31 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b71e8abc-a649-3637-9176-dff84b37baa3 | -14.19736 | -52.87903 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b98e68a9-a4d1-3e07-89c6-60651c88b45d | -14.5812 | -54.12317 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d93a6cd-b63b-3e0c-b0fb-3ce349bf9474 | -8.67376 | -66.51591 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b8a067e6-0e2e-3e12-bfa5-b4493199570c | -10.14044 | -45.7182 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10ac29e0-3526-34da-aab5-98670f6c59ea | -8.94476 | -62.37275 | 2026-08-31 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c8b4b6fb-cc98-39a2-ba85-3ced3f23358d | -8.61488 | -54.78357 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7300402-19d2-36f2-a1d4-e09544ca0c3b | -7.91925 | -61.3389 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 76744a30-843e-3812-b172-bdc6c54731f4 | -11.37264 | -45.21008 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c2c628d-944d-31f6-aae2-08dddec1b9d0 | -7.5845 | -61.3373 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c463201-662c-337b-8b8b-500fc4065019 | -9.39949 | -51.61078 | 2026-08-31 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa0137c8-e17c-3060-bd39-096386e3fe14 | -9.0129 | -60.60348 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31a76dbe-e985-3241-a937-f0e8ed63ba24 | -12.18205 | -50.52788 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aa55e71a-5157-3760-8c40-b5b2cdf397b2 | -9.71789 | -64.99761 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d7e8be1b-9cf8-3719-8c24-6a80fae2e162 | -13.47329 | -57.03773 | 2026-08-31 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fdbf80bf-8368-37cc-8a22-13131fc07dc0 | -11.92541 | -45.07157 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| da9ff977-5ce3-3fd7-8a35-d4ecec809b71 | -11.04022 | -57.22687 | 2026-08-31 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 843f4f68-6aea-3198-880c-d736cc32b62e | -7.58741 | -61.34715 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e6c3483d-7e2d-38c4-9034-866edd42c98e | -10.73521 | -47.96632 | 2026-08-31 04:59:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc10f818-c2a6-3798-b117-c9c0f7a6c909 | -9.88975 | -60.27913 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82cfd895-6e15-3ae6-8add-e406b6618bbb | -11.34273 | -45.20031 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3e29286-486f-3b8f-9950-a29c2dba9d76 | -14.21731 | -52.8426 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7773acf1-0d93-3b3f-8c31-6f4daf635e7d | -14.1829 | -52.87687 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32efb5f4-25a7-3ceb-9c6a-2e405102a392 | -10.14925 | -45.76453 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3a562727-b67e-3f7e-8a2c-6655e9f8e0d7 | -9.00941 | -60.59883 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18c8e71d-aac8-3cf8-813b-52efedd2cf6e | -14.42594 | -52.52499 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 52bdc73f-bda1-3ee1-94a9-9bdde27fdd14 | -10.90761 | -61.67527 | 2026-08-31 04:59:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6ba3d6d4-d5c9-3749-90c1-b8964e027cc4 | -10.74764 | -54.04028 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 113ae6b5-0b1a-3cf3-936d-ee1a2fcbf71a | -8.55926 | -54.79261 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0886ef6e-13e6-3af4-8351-45b535a0f342 | -11.0356 | -57.23379 | 2026-08-31 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8204ffc6-8c7d-3e4b-b0f0-31594489e6fb | -8.59708 | -54.72385 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8543d66-ea04-3c10-89d8-8a95d08267c0 | -10.76263 | -54.00933 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e766a07d-4b77-3401-b3fa-3447f1bc6606 | -10.74264 | -54.0506 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f522327-12b1-3966-ae51-545c27345294 | -8.48877 | -54.58955 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cb451a6-6a0b-30c6-867f-ee6dd2c72d8f | -14.60869 | -54.10383 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5257dffb-99d0-301c-862f-7cf99c65fb24 | -14.40993 | -52.53188 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8c55e49c-aa93-3ce1-8bd1-9da05aaa5288 | -10.48786 | -59.61194 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 969b18b9-ce11-3be3-a28f-e8b9aa4b7be0 | -11.35886 | -45.21073 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c0d88450-717d-3f05-9a27-32f4ac231fd5 | -9.58487 | -47.6077 | 2026-08-31 04:59:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aead0083-0d7a-3d61-a010-1868980714de | -8.6132 | -54.77263 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9df11fc0-c165-3a9b-8f24-a8e51a6a664f | -10.15195 | -45.7016 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92bbbd07-d28f-3d70-9a26-01ff7b367239 | -7.55711 | -61.32386 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README52.md)
