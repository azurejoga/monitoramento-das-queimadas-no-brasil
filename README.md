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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b4408f7-ac4c-3a15-b027-8e0f023067ab | -8.1135 | -44.1436 | 2026-05-21 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 5c74a380-7e9a-336b-819d-b26edcd9ca34 | -8.3239 | -47.995602 | 2026-05-21 00:17:00 | METOP-B | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0e1c810-0e9b-3a6c-a8b1-9176d15ed74e | -8.1011 | -44.137001 | 2026-05-21 00:17:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e9e9655b-bff8-3417-a3c8-101fc21d223b | -11.5496 | -54.523201 | 2026-05-21 00:17:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7cbbdb28-6489-32af-aa08-437c9580d26b | -13.0295 | -49.927399 | 2026-05-21 00:17:00 | METOP-B | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0cd3e51b-7b87-3d4e-ac7b-6fadc26a6e9c | -10.1164 | -52.402 | 2026-05-21 00:17:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6c8a44da-c302-3b3e-ab60-0fd73df19103 | -8.5512 | -45.970798 | 2026-05-21 00:17:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1dd4d952-0d84-374a-8645-141df0a9c46b | -10.4933 | -49.363098 | 2026-05-21 00:17:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2ec53747-71d2-3bab-9244-1ca2e775c15c | -8.7333 | -47.981098 | 2026-05-21 00:17:00 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7c82d9b1-ba6d-3c99-a679-7184fa2f1a77 | -8.7315 | -47.9734 | 2026-05-21 00:17:00 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 29dedc7d-01e4-3834-b092-7d83804301dd | -10.5879 | -46.639 | 2026-05-21 00:17:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 245ea05b-a5d3-3279-b0f0-af9c84496c22 | -10.5015 | -49.353802 | 2026-05-21 00:17:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4134e671-77b2-38cb-a062-f741191b01e0 | -9.2887 | -45.470501 | 2026-05-21 00:17:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fc67782e-f14c-3be4-a3d3-1d57abb24930 | -12.2359 | -48.0919 | 2026-05-21 00:17:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd864992-5d69-3e8b-8bf8-a7a08d9f057f | -9.9498 | -52.438499 | 2026-05-21 00:17:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 815f205d-97af-3aec-9b20-da669b5c6c9e | -9.9354 | -48.003601 | 2026-05-21 00:17:00 | METOP-B | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 124d427d-afd8-3f85-a94a-7c343d4e0b0a | -11.3092 | -54.693501 | 2026-05-21 00:17:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 64cdf281-83ce-3eac-8999-a90fdfe435f6 | -8.098 | -44.124199 | 2026-05-21 00:17:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ddefc5ff-9312-33bd-be4d-ec820872b85f | -10.4917 | -49.356098 | 2026-05-21 00:17:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0ddf804a-4cf6-3806-a849-08ad6a41894b | -10.0834 | -51.6385 | 2026-05-21 00:17:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 35fbfebc-b30b-3450-b12c-17914d5f57e4 | -6.3845 | -44.152 | 2026-05-21 00:17:00 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f4c42543-2b50-3150-8ac8-381e8c6d5c2e | -8.6242 | -45.973701 | 2026-05-21 00:17:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e522abd2-c87c-3238-a89c-783dbb725353 | -11.3114 | -54.703999 | 2026-05-21 00:17:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1bd3f11b-2cb2-3d51-862f-81f19478186a | -9.9612 | -52.444 | 2026-05-21 00:17:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 41bf861a-3bb6-3ef6-a36c-1335b03d8d6a | -11.077 | -48.256901 | 2026-05-21 00:17:00 | METOP-B | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1ca47e31-2def-3554-b3f5-1b5c2c3ece2f | -5.9461 | -43.485699 | 2026-05-21 00:17:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a02c5810-7065-3f74-ac7d-b835bfaa72a1 | -8.5558 | -45.990101 | 2026-05-21 00:17:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 380d980b-3046-34cf-a1e8-caf052db4782 | -11.5704 | -56.929001 | 2026-05-21 00:17:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bc42aee6-4c85-373d-869c-0e5123219270 | -11.8285 | -47.0868 | 2026-05-21 00:17:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f95b283-68da-3611-9d87-3c8be5dad443 | -13.0279 | -49.920399 | 2026-05-21 00:17:00 | METOP-B | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3ebc8f0a-6345-3186-a34e-3e973e7b67fb | -10.1147 | -52.394199 | 2026-05-21 00:17:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 40225baa-6785-3536-8a15-b13b507e0740 | -10.6378 | -48.321301 | 2026-05-21 00:17:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f274f14e-8fbd-399a-adae-bb92b712f286 | -11.1902 | -55.9002 | 2026-05-21 00:17:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0e31d1d4-2d65-3aeb-a006-d873ac06445b | -16.8986 | -46.775902 | 2026-05-21 00:17:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 62243864-f9a6-30f1-8032-4b74708d0ca2 | -9.3033 | -45.488201 | 2026-05-21 00:17:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c08f6ccc-4f2c-3465-ab83-3b0bf8c98877 | -9.3009 | -45.4781 | 2026-05-21 00:17:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5195e9a1-f77a-37d2-8e20-596258302c79 | -12.0233 | -47.794701 | 2026-05-21 00:17:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a960cfb-11ad-3519-b71d-606278d15e49 | -10.4386 | -47.9487 | 2026-05-21 00:17:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b773964b-a563-3abf-a99a-2c17815f6c06 | -11.0392 | -48.905499 | 2026-05-21 00:17:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac75b486-bcdf-302a-a54d-4c87e274be94 | -11.0189 | -49.0434 | 2026-05-21 00:17:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a096f413-ab33-3ef8-bb5d-77cb2a98184a | -9.9514 | -52.446201 | 2026-05-21 00:17:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9ebf42cc-6077-3ba5-be84-bc905ba6e714 | -11.6545 | -47.582699 | 2026-05-21 00:17:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dba81d61-2204-37dc-a991-c77532362e17 | -10.4902 | -49.349201 | 2026-05-21 00:17:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3de9bce4-346c-3bf0-9c96-e5db32e4699c | -10.0877 | -52.175301 | 2026-05-21 00:17:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 58ed7516-c529-3ad0-94cb-b057c296bc1f | -14.9002 | -47.742199 | 2026-05-21 00:17:00 | METOP-B | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f8c985a7-d184-3936-a0ae-e369ae35b36d | -10.3966 | -49.4366 | 2026-05-21 00:17:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3958c291-71b2-3aa6-810a-ae06c28b9139 | -20.772301 | -48.5569 | 2026-05-21 00:17:00 | METOP-B | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 969cccf3-b11c-3574-aca7-d03749dd83d0 | -9.2911 | -45.480499 | 2026-05-21 00:17:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| df75572b-c423-3369-8b44-ff3a8c0cbbc7 | -8.5978 | -45.949501 | 2026-05-21 00:17:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 85b56b7f-4803-3f64-a1bd-7d7fb6ad75fb | -10.4467 | -47.9389 | 2026-05-21 00:17:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4651a59b-f9f6-3739-9a5d-37ac3ae4dea0 | -11.3368 | -47.995602 | 2026-05-21 00:17:00 | METOP-B | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f8e5da7d-d4f9-3051-97d0-41d07fea9df3 | -11.9953 | -47.762402 | 2026-05-21 00:17:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 67079896-8884-3cbb-8fa4-6b5145143cb5 | -10.6395 | -48.328499 | 2026-05-21 00:17:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 01ebdfe7-47fb-3c52-8a1d-95fad4191e4d | -11.4766 | -52.907902 | 2026-05-21 00:17:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 00c8b0a8-350d-3c2f-9671-6f678d706206 | -10.4369 | -47.9412 | 2026-05-21 00:17:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 623ab387-1359-31c2-b269-fdcd7ffb98d9 | -8.5535 | -45.980499 | 2026-05-21 00:17:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b6393721-42ea-3465-b4a9-f3e70dc9f6eb | -8.5438 | -45.9828 | 2026-05-21 00:17:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ff0868a-7834-3a1b-95ae-07bb9ffef78c | -8.1042 | -44.1497 | 2026-05-21 00:17:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a4168b5a-b0f0-3a09-bfd6-23f83f71881d | -10.6383 | -42.297798 | 2026-05-21 00:17:00 | METOP-B | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a216015e-f027-3b4e-a058-97ac5fe6e89b | -8.5415 | -45.973099 | 2026-05-21 00:17:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 062df49e-9388-307b-95e2-b3d4c7b9de33 | -11.976 | -52.461498 | 2026-05-21 00:17:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0b72b595-fe21-370f-ad8a-c6ad0919e14a | -11.9528 | -43.386299 | 2026-05-21 00:17:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 81319c1a-d91d-323c-89ed-8802ff9177f3 | -10.355 | -47.809898 | 2026-05-21 00:17:00 | METOP-B | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5cf2abd1-9eb8-3c91-8626-0314e4a2d089 | -6.3877 | -44.165501 | 2026-05-21 00:17:00 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8c98a77-843e-3f55-8dd3-9fdf6bdc9630 | -11.763 | -48.279202 | 2026-05-21 00:17:00 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b6c2a7be-66ac-3fbe-ad9a-23e4561fca08 | -11.1877 | -55.887699 | 2026-05-21 00:17:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 93ec50e6-74e6-3ea7-a23c-bd57cc2f0a78 | -8.3257 | -48.003201 | 2026-05-21 00:17:00 | METOP-B | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| adf34672-fb59-3c68-aeed-f3bab5768111 | -6.2881 | -43.624401 | 2026-05-21 00:17:00 | METOP-B | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 31bf598a-4c33-379b-a457-dd51ea290dc7 | -9.7181 | -50.406601 | 2026-05-21 00:17:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48efb554-ea0e-3f6e-b21e-e4af3cbb8afd | -10.4484 | -47.9464 | 2026-05-21 00:17:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cbec9e06-4281-3520-a9e8-45183d769b40 | -6.2916 | -43.639099 | 2026-05-21 00:17:00 | METOP-B | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4df4ddac-f4f0-37d1-9a1a-67f985725031 | -14.6327 | -48.018398 | 2026-05-21 00:17:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b561d78d-f818-39fd-973e-910ae8827743 | -11.5674 | -56.9142 | 2026-05-21 00:17:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5fe2797-3c74-3522-9b89-88197540404e | -11.3385 | -48.002899 | 2026-05-21 00:17:00 | METOP-B | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 57f6fa30-19db-35ff-a7bc-7f19c35e943e | -8.6092 | -45.997501 | 2026-05-21 00:17:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86b36ab5-29c9-3cbb-aae5-a35b8329d76f | -11.9935 | -47.754902 | 2026-05-21 00:17:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ef838d30-e2a3-3dc3-8095-02363a57db96 | -14.9018 | -47.749401 | 2026-05-21 00:17:00 | METOP-B | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f01c7c96-e597-3204-a47e-44cb91985f55 | -10.3982 | -49.443501 | 2026-05-21 00:17:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 90ca8fde-5bce-3f84-92c8-4409d56e14da | -13.031 | -49.934502 | 2026-05-21 00:17:00 | METOP-B | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8ebb0e56-5630-32a2-b178-01578354b969 | -11.4668 | -52.910099 | 2026-05-21 00:17:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a47bcd59-fbee-3ef9-af17-98943b280c7c | -8.1135 | -44.1436 | 2026-05-21 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 55.4 |
| a57e35e6-6995-30b6-abb5-17800ce23f12 | -16.45716 | -51.71862 | 2026-05-21 00:28:00 | TERRA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| da23c848-cc74-371e-9303-eba77a9203f9 | -14.89953 | -47.75303 | 2026-05-21 00:28:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 7f54eb2d-c70c-34be-975c-548a42c354cc | -20.76889 | -48.57093 | 2026-05-21 00:28:00 | TERRA_M-M | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9c35c006-5667-3ce8-b353-a6b0e5ad45f3 | -16.15239 | -51.72431 | 2026-05-21 00:28:00 | TERRA_M-M | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6f89bc80-6a58-3099-a8ab-9dca43f24b6d | -8.1135 | -44.1436 | 2026-05-21 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 2fcd93e7-1c5d-3997-a2d2-1d48174e8a50 | -11.79788 | -57.36541 | 2026-05-21 00:30:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 0d212631-dd47-3062-b2ba-6dd0487584d5 | -14.2114 | -54.60307 | 2026-05-21 00:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2304d4e3-665d-36f1-8fd5-f4c92cd25742 | -10.49155 | -49.3571 | 2026-05-21 00:30:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| fef01ba6-255c-37c4-9815-ecad2b1e0a0b | -11.57158 | -56.93893 | 2026-05-21 00:30:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d1f4734b-357f-307a-a584-048168f18836 | -13.02673 | -49.92739 | 2026-05-21 00:30:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1ae16236-40d9-3fe3-a22f-b7aae0e0a754 | -11.30058 | -54.71468 | 2026-05-21 00:30:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 077a80d3-fcd2-3a80-9efc-34de505a5446 | -11.47141 | -52.91636 | 2026-05-21 00:30:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1d1375c2-6785-39f6-8d4d-19efa22a28c4 | -11.83349 | -47.09694 | 2026-05-21 00:30:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 9deb0005-a96a-3dae-bd51-d43db7ff2ecc | -13.02836 | -49.93843 | 2026-05-21 00:30:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 57e09ac4-ecd0-33c2-937a-8b607e8ece7a | -11.56119 | -56.94027 | 2026-05-21 00:30:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| cf1b0925-fcc6-3ebf-9325-49a8d9bf22da | -12.5494 | -57.21324 | 2026-05-21 00:30:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 81a96e21-ffdb-357d-9af6-0e5825cfe05d | -11.18304 | -55.90784 | 2026-05-21 00:30:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 0914bacf-6680-39b7-8afd-0342ea6f3474 | -11.07281 | -48.27029 | 2026-05-21 00:30:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 669abb6b-7b10-33a2-b9e0-5c700d1ccf02 | -11.43531 | -55.1044 | 2026-05-21 00:30:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README2.md)
