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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0084c995-26a4-3b8c-8f53-a835a82c2128 | -13.59511 | -45.77477 | 2026-08-28 06:37:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1e5d522d-8170-3e27-80a7-c79ddf42a351 | -14.6022 | -47.97264 | 2026-08-28 06:37:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ff80dfc1-e5c1-35f6-853c-ad9cdc3479c5 | -12.26845 | -50.58266 | 2026-08-28 06:37:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b2d5f28c-0523-309e-9143-045a3e868f80 | -14.93014 | -52.60197 | 2026-08-28 06:37:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| a4158a4a-46aa-3d45-8e56-eee435f600b9 | -6.1656 | -57.7988 | 2026-08-28 06:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 3f2423ab-a09b-3ac5-b27f-80756a71a4e2 | -6.1657 | -57.7793 | 2026-08-28 06:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 8537d251-7180-3ea5-995f-c533f64fb849 | -10.9367 | -50.5332 | 2026-08-28 06:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 132.3 |
| bb792f24-f91c-36c7-9f3a-996f7a94f262 | -10.498 | -64.5193 | 2026-08-28 06:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 8bcaf2f0-f49f-3065-bdde-44db2a00dec2 | -16.1641 | -58.5851 | 2026-08-28 06:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.3 |
| fd0d67b9-e99d-37ac-89d6-5c4ce8aadbd4 | -10.937 | -50.5118 | 2026-08-28 06:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| a9f2e005-76e0-3c50-a5ec-494f95b533f4 | -10.4981 | -64.5005 | 2026-08-28 06:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 8afc3e16-66c1-379a-a434-aaab796ddae0 | -10.7839 | -50.6346 | 2026-08-28 06:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.6 |
| a4b514a9-d3e1-3e74-b918-d11946299557 | -10.5168 | -64.4997 | 2026-08-28 06:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 8846eaac-e1d3-3188-abd2-2c692a6d60b9 | -10.5166 | -64.5186 | 2026-08-28 06:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 2e9b972b-fb87-3b20-8d8e-c81c7a0a5f99 | -6.1656 | -57.7988 | 2026-08-28 06:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 9fcd01f5-89ad-36af-96be-247d8f065830 | -10.9177 | -50.5352 | 2026-08-28 06:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 102347bb-e239-3352-8bac-0e6beecd60b0 | -10.498 | -64.5193 | 2026-08-28 06:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 01db74fe-ef86-3961-9ba5-6f1431cb4410 | -10.5168 | -64.4997 | 2026-08-28 06:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 6cd83f4a-6494-3136-84e8-c65df76578c9 | -10.5166 | -64.5186 | 2026-08-28 06:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| bd4103f8-8d90-3f39-986d-4a2c82478b9e | -6.1657 | -57.7793 | 2026-08-28 06:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 044431d6-cd87-364e-940e-3c794313dfea | -10.918 | -50.5138 | 2026-08-28 06:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 392af5f3-0a23-3eac-9203-0ece038153da | -10.9367 | -50.5332 | 2026-08-28 06:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 084138d7-e818-3344-9cef-d286531f2af2 | -6.1472 | -57.7995 | 2026-08-28 06:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 97a70935-4cd6-3ed4-86a8-ae782bc3327b | -10.937 | -50.5118 | 2026-08-28 06:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 129.6 |
| c145c907-4c27-378e-ab0d-40d87330ae98 | -10.4981 | -64.5005 | 2026-08-28 06:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 7ed729d9-9b4d-370b-875c-61477ff52078 | -10.7839 | -50.6346 | 2026-08-28 06:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| bb270bcd-bc8c-3542-b236-216161a51a22 | -8.60452 | -70.21205 | 2026-08-28 06:52:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d9610892-675e-3610-af14-ae35db599569 | -8.59824 | -70.21131 | 2026-08-28 06:52:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 533c9be9-cc26-3365-9628-3c8b0d7a945a | -8.59132 | -70.21548 | 2026-08-28 06:52:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| baf7fa2e-bd22-3fbd-9128-a25234115c52 | -8.59759 | -70.21632 | 2026-08-28 06:52:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8542248e-f8cd-315e-9c8e-9f6569796baf | -8.59889 | -70.20627 | 2026-08-28 06:52:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7db6f0df-cd3b-3a58-bee9-d3707a3d1256 | -7.40091 | -72.62852 | 2026-08-28 06:52:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6400f271-f5fa-343f-9cf9-7a9dbd865b1a | -8.60387 | -70.21709 | 2026-08-28 06:52:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7777b4fc-9c3a-3031-9574-2b26e5042ab4 | -6.1656 | -57.7988 | 2026-08-28 07:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 7f10602d-b341-3c9b-bc2a-d016a91e1372 | -10.498 | -64.5193 | 2026-08-28 07:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 80.8 |
| bf3ae0cc-1ffc-3883-b5d0-57cda45b6966 | -10.5166 | -64.5186 | 2026-08-28 07:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| fe22b824-05b9-32e3-9f12-37f3d8964908 | -10.937 | -50.5118 | 2026-08-28 07:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 1768bdde-fe07-3b1a-9488-cd3471784254 | -6.1657 | -57.7793 | 2026-08-28 07:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 2237292c-e73b-38bb-aa12-dd6de9266b0a | -10.9367 | -50.5332 | 2026-08-28 07:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| b1b097cd-f53f-3682-878d-c80cce2dcacc | -10.4981 | -64.5005 | 2026-08-28 07:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 04ef272c-670c-37ae-a4c8-38f8b4e64c7f | -10.4981 | -64.5005 | 2026-08-28 07:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 801ee806-d807-317f-b4d1-a3ca72d60aed | -6.1656 | -57.7988 | 2026-08-28 07:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 45d86d3c-a72b-3ff7-b0d1-c78741620272 | -10.937 | -50.5118 | 2026-08-28 07:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 055ec4b5-ddb6-398f-98ed-395c64bcbaff | -10.9556 | -50.5311 | 2026-08-28 07:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 1a7cd85e-1530-35c0-980a-d7e0618d6730 | -10.498 | -64.5193 | 2026-08-28 07:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 67.6 |
| e62213f3-e81f-3a1a-a281-908ab681ae8e | -10.9367 | -50.5332 | 2026-08-28 07:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| eb450855-09cc-38e1-9d0e-786ee2c02fce | -6.1657 | -57.7793 | 2026-08-28 07:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 83b860bb-5ce1-3b04-abdf-e2fd7175d613 | -10.5166 | -64.5186 | 2026-08-28 07:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| d282ec25-7e1a-39c1-b9be-e2ef04bb33ad | -10.498 | -64.5193 | 2026-08-28 07:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 70.9 |
| bac1bd90-896c-361f-a3e2-9bc479886554 | -10.5166 | -64.5186 | 2026-08-28 07:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| c8b5c255-131c-359a-9c1d-578c36da87ea | -6.1656 | -57.7988 | 2026-08-28 07:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| ea5c2c3e-cd48-31d1-b818-0566ab1b7c23 | -10.4981 | -64.5005 | 2026-08-28 07:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 8541b0fc-c69c-39db-ae45-0b637d6fe967 | -6.1657 | -57.7793 | 2026-08-28 07:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 2eedff1c-06f7-3ab2-94d3-97a04b553b3d | -10.5168 | -64.4997 | 2026-08-28 07:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 9166252f-f20d-3379-a213-25b5c41a8405 | -10.7839 | -50.6346 | 2026-08-28 07:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 50.8 |
| b5028a4e-1e0a-308d-a80e-cd17cb34d3e1 | -6.1656 | -57.7988 | 2026-08-28 07:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| d03e1f1d-0ac2-343f-98fe-a0ad55ad89eb | -10.498 | -64.5193 | 2026-08-28 07:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| efda6048-90f9-3e96-8461-e0fd77f04b5a | -6.1657 | -57.7793 | 2026-08-28 07:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 75f6fc94-b4b8-3732-95ff-de521e7e5176 | -12.2659 | -50.5747 | 2026-08-28 07:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 5db859b1-faa8-36fe-88fd-7fca24766d08 | -10.4981 | -64.5005 | 2026-08-28 07:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 0bc9c4f7-e192-329b-9e23-77bf7ebb320e | -12.285 | -50.5724 | 2026-08-28 07:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| d485a09c-a414-3170-aadc-ae1a0ffa7579 | -6.1656 | -57.7988 | 2026-08-28 07:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 91268a2e-b766-3983-b699-165e70971938 | -6.1657 | -57.7793 | 2026-08-28 07:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 872aa1d5-88df-323a-bc0a-6c21e9d89266 | -10.498 | -64.5193 | 2026-08-28 07:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 68d0a973-cb7d-3acf-bac5-8dc6717451aa | -10.4981 | -64.5005 | 2026-08-28 07:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 77542b9c-d489-350e-a5f6-b48faa70e498 | -10.5166 | -64.5186 | 2026-08-28 07:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 54.4 |
| a87c98e9-9f85-3e62-94f7-02f30e60077a | -12.2659 | -50.5747 | 2026-08-28 07:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 18236ba0-88d5-3f2f-8596-c14c50afcda8 | -10.5166 | -64.5186 | 2026-08-28 07:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 6eea7dea-6eac-388f-923a-34c626217361 | -6.1656 | -57.7988 | 2026-08-28 07:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 53904872-d175-30ee-b942-f2bc9c3c6c12 | -10.498 | -64.5193 | 2026-08-28 07:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 80.1 |
| da33b2ee-27fa-3930-b7f9-b75f8c224883 | -12.285 | -50.5724 | 2026-08-28 07:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| f854119f-93e7-3687-9c65-e10c69d854e9 | -6.1657 | -57.7793 | 2026-08-28 07:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 39a89fb3-db3a-35dc-9de6-05123661cf18 | -12.2659 | -50.5747 | 2026-08-28 07:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| b8e8b1d2-85e4-35b8-bc9b-581118d1961d | -12.2468 | -50.577 | 2026-08-28 07:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| a9003f1d-1a6f-3509-bbfa-143d2604f30e | -10.4981 | -64.5005 | 2026-08-28 07:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 657ae410-984b-320d-9692-e12be6322e88 | -10.498 | -64.5193 | 2026-08-28 08:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 57.8 |
| fa8b66f9-8d7e-3502-9c54-19dea05c24f6 | -6.1656 | -57.7988 | 2026-08-28 08:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 89c1db9a-dc51-3351-bcdf-d4fddc0cbe7b | -12.2659 | -50.5747 | 2026-08-28 08:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 65fc2818-a5ff-3136-aa86-6cd7f0c2dba2 | -12.285 | -50.5724 | 2026-08-28 08:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 9da0ff19-0bea-3bc5-b242-296cbb32e8aa | -10.5166 | -64.5186 | 2026-08-28 08:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| af235030-6efc-3c13-bd92-abd1816e8999 | -10.4981 | -64.5005 | 2026-08-28 08:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 90a0893d-cb57-3b8e-98ac-ad8629ebce8f | -12.2656 | -50.5961 | 2026-08-28 08:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 65ee779b-732a-326c-bfdb-f894571a3050 | -12.2468 | -50.577 | 2026-08-28 08:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 59098e82-ea96-313c-88bb-be99f1620235 | -10.5166 | -64.5186 | 2026-08-28 08:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 53f92945-4c35-3df0-9333-5f988a7de348 | -10.4981 | -64.5005 | 2026-08-28 08:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 0cafaebd-8cc0-34f4-be08-60660abda46e | -10.498 | -64.5193 | 2026-08-28 08:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 61.2 |
| b124804b-d69b-3002-8037-8aad5cd9fc61 | -8.87246 | -66.90576 | 2026-08-28 08:13:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0bb9fa2c-af6f-3454-8d55-84c893adb697 | -10.49749 | -64.50985 | 2026-08-28 08:13:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 09e43612-75c6-336c-98f1-54ff6563d17b | -10.502 | -64.49883 | 2026-08-28 08:13:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 75.5 |
| c85c3c73-a107-3645-8908-9d30e42705af | -10.51437 | -64.50056 | 2026-08-28 08:13:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 18.9 |
| c9d4ec11-17a3-3282-9755-12854badc196 | -10.49961 | -64.51743 | 2026-08-28 08:13:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 9bf1a96e-d9a5-3f05-b760-ba6b2b782b05 | -10.50002 | -64.49127 | 2026-08-28 08:13:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 36.8 |
| ebe77be8-55c8-3b96-bfe1-3639bcc89f5d | -8.59688 | -70.20418 | 2026-08-28 08:13:00 | AQUA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 25f8ccf9-d555-3273-b886-89cae7129dbf | -8.59555 | -70.21297 | 2026-08-28 08:13:00 | AQUA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 12575f88-9770-37e1-92e4-9962dc4ea3d1 | -8.8732 | -66.90068 | 2026-08-28 08:13:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 9c8b43db-8ddc-388d-878b-b1ae3a670a42 | -8.87415 | -66.89415 | 2026-08-28 08:13:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| cfced0f9-5438-3317-98da-8635467f5f9f | -10.51195 | -64.51924 | 2026-08-28 08:13:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 4813d024-2b51-300b-b800-2913256608bf | -10.4981 | -64.5005 | 2026-08-28 08:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 36bd873b-16e7-31ff-9f3b-79dc7de4aea5 | -16.1447 | -58.5871 | 2026-08-28 08:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.1 |
| 521d0dd9-337b-3e2b-8d7f-c798a31527b8 | -10.5166 | -64.5186 | 2026-08-28 08:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 60.5 |


[Clique aqui para ver as próximas entradas](README70.md)
