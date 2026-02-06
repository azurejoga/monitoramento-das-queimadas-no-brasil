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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05a17886-d08f-3f29-b780-743c4e5408cf | -3.44377 | -54.09899 | 2026-02-06 05:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4760f70-1c2d-3265-8213-543bc3207348 | -11.18119 | -55.92217 | 2026-02-06 05:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| fca374ad-78e9-30eb-b9a3-8e92cafe3fb1 | -16.58248 | -57.80724 | 2026-02-06 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8a47ee1f-af32-33ce-b904-9aac0e44ad60 | -11.85758 | -63.67765 | 2026-02-06 05:14:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8c810a5-85eb-3a8e-840f-31582eae2352 | -10.21268 | -59.40627 | 2026-02-06 05:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e174991-ef64-3f72-a502-64e8f466074f | -11.17767 | -55.92162 | 2026-02-06 05:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 08c3687b-f194-38a8-bdaf-fe3ea766c559 | -15.79477 | -59.68474 | 2026-02-06 05:14:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec5a9723-e62e-3bc0-8e7e-1cab8c236a78 | -11.1818 | -55.91814 | 2026-02-06 05:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 98a765e5-26d3-319d-ac9e-337d134febf3 | -11.17827 | -55.91759 | 2026-02-06 05:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 534940ca-795f-3272-9efe-93902ac0b2b5 | -10.21326 | -59.40269 | 2026-02-06 05:14:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41c9a3f0-1688-3640-9087-e5b43402dd41 | -16.5894 | -57.80392 | 2026-02-06 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 7e89e6b7-3214-3ff9-a1f4-03b638760517 | -9.18051 | -58.05973 | 2026-02-06 05:14:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79ccc5e2-7fb7-3e0e-b2a8-73d1473771f4 | -16.57962 | -57.80283 | 2026-02-06 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3b005d7d-0c4b-310f-b4fb-8c3cee62e88c | -11.18472 | -55.92271 | 2026-02-06 05:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c66cca4d-2fe0-3ea4-9319-c1fe9f5ac265 | -16.58993 | -57.80449 | 2026-02-06 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 371db7cd-f806-3db1-b857-cd2683761726 | -11.17063 | -55.92049 | 2026-02-06 05:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b798046-c8c9-3ea1-90af-a3fa4085d930 | -16.58649 | -57.80396 | 2026-02-06 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5994dd2a-cfa4-36ee-9462-1dd17818d0eb | -9.18106 | -58.05625 | 2026-02-06 05:14:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09e577c1-6e85-3358-8376-a180279c776a | -11.1824 | -55.9141 | 2026-02-06 05:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc01ebef-3ff6-3c1c-ae50-3df594d3c1ef | -11.18592 | -55.91464 | 2026-02-06 05:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a78cb39-cbfe-36c9-83a3-c0933152ecdf | -16.5802 | -57.79896 | 2026-02-06 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6e2d0fa9-e8a0-3265-a7c7-64aeb0cae93b | -16.58364 | -57.79952 | 2026-02-06 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7671eb1f-3a88-3e90-8bc0-084650908700 | -11.17415 | -55.92105 | 2026-02-06 05:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 76e7a151-7530-3095-a8ec-51598dad9486 | -11.18532 | -55.91868 | 2026-02-06 05:14:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e4e13d54-48cd-383a-9975-80784784ad88 | -14.87394 | -59.49462 | 2026-02-06 05:14:00 | NOAA-20 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1dfc55f7-d0d2-31e6-8aa9-46a2a9659bfa | -16.58306 | -57.80339 | 2026-02-06 05:14:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c61edcd4-6e16-3116-afa2-8fd2c6354420 | -21.72205 | -53.13045 | 2026-02-06 05:16:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ada684a-2ad5-3c11-817d-0a89f7368210 | -11.1903 | -55.9101 | 2026-02-06 05:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 939af3c1-756b-3d8d-a696-c77bfeaf5cb6 | -8.97939 | -35.21587 | 2026-02-06 05:25:00 | AQUA_M-M | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| ee73f428-dec7-30df-8d9d-6316cbab3cbc | -8.98074 | -35.20697 | 2026-02-06 05:25:00 | AQUA_M-M | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| 66db0d12-ce3a-365c-b6d9-4bfbbb2e6980 | -11.1903 | -55.9101 | 2026-02-06 05:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 29ec43cb-468e-3984-8aa9-99fb571aeeb9 | 3.75015 | -60.74717 | 2026-02-06 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 59917845-4f4d-309e-9b30-67c1fe23c3da | 4.33928 | -60.92174 | 2026-02-06 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 659eb596-d949-345a-8ba3-a10ffffb9055 | 4.33823 | -60.94366 | 2026-02-06 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac4ce094-35c1-3858-a4a9-4233795399aa | 4.33466 | -60.92196 | 2026-02-06 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78a26c4f-e558-3d83-b162-037e5dd93ef3 | 4.34387 | -60.9213 | 2026-02-06 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d059a88-efed-3e3e-871c-5e3ea35540f7 | 3.75095 | -60.75202 | 2026-02-06 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c32166a9-924d-3bbf-a566-59ff51392aaf | 4.33553 | -60.9273 | 2026-02-06 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d4e0758-bb92-3bc3-ad52-73899e90a15f | 4.24369 | -59.83377 | 2026-02-06 06:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35ef1d82-def7-3766-beab-6e43578ba12e | 4.24277 | -59.82825 | 2026-02-06 06:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f52345c6-a9e3-3fb7-be08-67b6a24f4c61 | 4.33296 | -60.93999 | 2026-02-06 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7d24273-bf2c-3d18-8e33-878cf3a1f327 | 4.21297 | -59.97868 | 2026-02-06 06:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d1bd936b-6684-3796-9c12-d5e16eea2169 | 4.20415 | -59.98551 | 2026-02-06 06:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80083fdd-8349-3b82-9b7e-b1b16da95724 | 4.56854 | -60.65474 | 2026-02-06 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59564ff4-87cb-3945-8304-9524313bb7fe | 3.70918 | -60.811 | 2026-02-06 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29a64257-5a15-3569-a864-1d0fba7c4d29 | 3.70803 | -60.80884 | 2026-02-06 06:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b615977-05a4-3560-ae04-3370e12dbbdf | 2.82486 | -60.90091 | 2026-02-06 06:31:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 539c80e7-8278-3873-bd83-942761c46b5b | 2.82369 | -60.89418 | 2026-02-06 06:31:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e2e7f63f-5ebc-3489-87db-fa2352ae6897 | 4.24754 | -59.82578 | 2026-02-06 06:58:00 | AQUA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ce08ac77-16c4-3a01-b833-a9cc80c1356c | 4.33214 | -60.92486 | 2026-02-06 06:58:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 41040ea5-6375-35e1-a0f5-0ed18adf8f6b | 4.33988 | -60.92907 | 2026-02-06 06:58:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2e7f8e56-1399-36c7-a2bb-e3c6ea21c322 | 4.33787 | -60.91555 | 2026-02-06 06:58:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3d4aa9a9-77f5-3129-99d5-41e33062284f | -11.18509 | -55.91042 | 2026-02-06 07:03:00 | AQUA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 34.7 |
| a9127bdc-e558-30c0-ae6c-87c598e4f604 | -11.18335 | -55.92334 | 2026-02-06 07:03:00 | AQUA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 125639f5-bb53-3532-b039-a33ed475db35 | -11.17682 | -55.9165 | 2026-02-06 07:03:00 | AQUA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 2513ce08-20a0-3f00-959a-8ddd7deac584 | -3.14854 | -48.14115 | 2026-02-06 12:12:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 730dcba5-a284-34bf-a762-27d524127789 | -4.98775 | -40.02764 | 2026-02-06 12:12:00 | TERRA_M-T | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 19.1 |
| e20e404a-d04f-3555-950b-db6d1025f8dd | -4.73279 | -44.4511 | 2026-02-06 12:12:00 | TERRA_M-T | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 87d64c2b-d265-3cf0-9909-89987814b3b3 | -9.71437 | -51.02578 | 2026-02-06 12:14:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| bf493d73-547a-3f40-b525-903f6298c0de | -11.26915 | -49.47558 | 2026-02-06 12:14:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 52ab3cbc-1b82-37b8-aa7b-4bec5ebee70a | -10.1686 | -49.18015 | 2026-02-06 12:14:00 | TERRA_M-T | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2a8e306d-cab2-3ad2-a34d-7c64be333e43 | -16.81331 | -42.69031 | 2026-02-06 12:14:00 | TERRA_M-T | JOSÉ GONÇALVES DE MINAS | MINAS GERAIS | Brasil | 3136520 | 31 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 0a452c08-c784-37e2-a9e4-5cbadb774ab8 | -11.27798 | -49.47684 | 2026-02-06 12:14:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 45432bfc-5ac7-39ea-84db-b18d710ee2d7 | -11.27925 | -49.46791 | 2026-02-06 12:14:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c236e7dd-1c1d-3247-95d5-4ba59eb33360 | -11.27043 | -49.46665 | 2026-02-06 12:14:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 985d3c89-8271-37d3-ad99-5baa14c6f48e | -10.66649 | -40.04225 | 2026-02-06 12:14:00 | TERRA_M-T | FILADÉLFIA | BAHIA | Brasil | 2910859 | 29 | 33 | nan | nan | nan | Caatinga | 78.6 |
| a3541229-a2cf-3d98-9885-e9b5e9d1b8fc | -9.71294 | -51.03539 | 2026-02-06 12:14:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| bb109835-496a-38af-b496-5bda46dc139d | -20.616 | -51.88013 | 2026-02-06 12:16:00 | TERRA_M-T | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c0bee11a-2262-3139-ad76-b51133be2775 | -22.2573 | -48.20654 | 2026-02-06 12:16:00 | TERRA_M-T | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 0b882ac7-f92a-3f27-8377-79e480036211 | -20.71596 | -48.82521 | 2026-02-06 12:16:00 | TERRA_M-T | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 2c62d70f-610c-3f58-abe2-005379939a5c | -26.96286 | -53.46321 | 2026-02-06 12:18:00 | TERRA_M-T | IPORÃ DO OESTE | SANTA CATARINA | Brasil | 4207650 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 7f6cfd3b-1eec-3305-b2dd-54d92dd8a434 | -26.94914 | -48.74635 | 2026-02-06 12:18:00 | TERRA_M-T | ITAJAÍ | SANTA CATARINA | Brasil | 4208203 | 42 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| b4ed265d-36ae-37c8-9c6e-3c2c0acfecbe | -28.98429 | -50.67804 | 2026-02-06 12:18:00 | TERRA_M-T | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 1972891c-ce31-308c-a167-e9c64614cd3b | -29.33092 | -50.92573 | 2026-02-06 12:18:00 | TERRA_M-T | GRAMADO | RIO GRANDE DO SUL | Brasil | 4309100 | 43 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 5a384432-6bc1-3ded-9135-77b3ffad315a | -29.0027 | -51.24129 | 2026-02-06 12:18:00 | TERRA_M-T | FLORES DA CUNHA | RIO GRANDE DO SUL | Brasil | 4308201 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 8759861d-f35e-38e1-9e33-5b03f449e399 | -27.35285 | -50.77102 | 2026-02-06 12:18:00 | TERRA_M-T | BRUNÓPOLIS | SANTA CATARINA | Brasil | 4202875 | 42 | 33 | nan | nan | nan | Mata Atlântica | 36.7 |
| fb62a85d-4f5a-37e3-a5e4-f047690c9360 | -27.35142 | -50.78253 | 2026-02-06 12:18:00 | TERRA_M-T | BRUNÓPOLIS | SANTA CATARINA | Brasil | 4202875 | 42 | 33 | nan | nan | nan | Mata Atlântica | 71.8 |
| e01a5c61-d110-3ce5-a3b2-2070510b86f6 | -29.00865 | -51.23708 | 2026-02-06 12:18:00 | TERRA_M-T | FLORES DA CUNHA | RIO GRANDE DO SUL | Brasil | 4308201 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| f8a84d76-4f6c-31ed-8fb6-73bf371ecf4d | -28.30306 | -50.81476 | 2026-02-06 12:18:00 | TERRA_M-T | VACARIA | RIO GRANDE DO SUL | Brasil | 4322509 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| fe0f7513-1eea-3d98-a64f-9a4dcadabea6 | -27.3599 | -50.7585 | 2026-02-06 14:00:00 | GOES-19 | BRUNÓPOLIS | SANTA CATARINA | Brasil | 4202875 | 42 | 33 | nan | nan | nan | Mata Atlântica | 101.3 |
| 2a3f5ff8-25cc-364b-85f4-cf4790533e37 | -27.3591 | -50.7826 | 2026-02-06 14:00:00 | GOES-19 | BRUNÓPOLIS | SANTA CATARINA | Brasil | 4202875 | 42 | 33 | nan | nan | nan | Mata Atlântica | 98.5 |
| bf89ed39-97cf-341e-babe-47a9bd3988a6 | -27.3599 | -50.7585 | 2026-02-06 14:10:00 | GOES-19 | BRUNÓPOLIS | SANTA CATARINA | Brasil | 4202875 | 42 | 33 | nan | nan | nan | Mata Atlântica | 114.2 |
| b02d6dc5-e092-3278-b331-7328d0a578bb | -27.3591 | -50.7826 | 2026-02-06 14:10:00 | GOES-19 | BRUNÓPOLIS | SANTA CATARINA | Brasil | 4202875 | 42 | 33 | nan | nan | nan | Mata Atlântica | 134.6 |


