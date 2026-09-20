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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec8454c2-2049-3f97-a7b9-4e2867f5ef4d | -10.3168 | -50.2352 | 2026-09-20 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 4a7e0405-862f-3d99-8f3a-1b1be030599f | -9.8502 | -48.4053 | 2026-09-20 13:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 296b2fc7-9e6b-3811-b014-b7c45d4590fc | -10.3917 | -48.8915 | 2026-09-20 13:00:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 2e3ab3c8-eb41-3a5b-8494-acb313c1bad5 | -6.9225 | -42.9088 | 2026-09-20 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 10a3ba39-b598-312a-816b-a71a9c65d0e7 | -9.26 | -45.9616 | 2026-09-20 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 0a068b20-a157-3966-9877-d45a51188a48 | -8.8639 | -45.937 | 2026-09-20 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 5737fcc4-8570-3d4e-8e6b-d2558385e3fc | -10.8364 | -50.9479 | 2026-09-20 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 201.3 |
| a5f6aaa9-4d02-3553-8483-3d576b0a3d79 | -10.473 | -51.2808 | 2026-09-20 13:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| b1c2ca3c-b9a3-333c-8d4a-2dc53542567e | -8.9752 | -44.6722 | 2026-09-20 13:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 171.7 |
| 605087f1-28bb-37ee-a637-367a824f8d45 | -7.0455 | -43.6928 | 2026-09-20 13:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 5543eba1-66da-35b0-8cf6-003995ee7d1a | -9.5539 | -46.5807 | 2026-09-20 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 165.5 |
| f8d2f6ad-bd87-3305-a2d0-5e26d713b1da | -3.6946 | -60.5835 | 2026-09-20 13:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 3c868f3e-9299-3c43-8dc5-9c23017d8fb7 | -6.4486 | -59.9717 | 2026-09-20 13:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 8dbea1de-d8ab-325c-9a55-27bf42d72a23 | -11.8491 | -46.8556 | 2026-09-20 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 87cfd6de-93f6-32e8-bff5-1a33379be532 | -12.2341 | -50.1703 | 2026-09-20 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 6dc2edd3-8ee6-389e-9671-e43d9702a7ba | -12.6423 | -50.9144 | 2026-09-20 13:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 3e439b41-44a0-3c28-a780-16f7bb301e78 | -6.4671 | -59.9711 | 2026-09-20 13:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 7c9fab5d-ff08-3a33-84ce-d696d4d22d27 | -8.05 | -46.2663 | 2026-09-20 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 8224a460-58ca-30cf-bba3-7cdabd296d9d | -10.3171 | -50.2138 | 2026-09-20 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 08f22e5e-31c9-389b-b883-002f6f7c2a52 | -8.7003 | -45.4567 | 2026-09-20 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 544348a0-0eab-3a3e-8d91-1011063a276c | -8.8825 | -45.9576 | 2026-09-20 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 81bce1cb-536c-3075-ae57-0461bc69f69a | -12.2844 | -47.1319 | 2026-09-20 13:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 0dd5b467-3ac5-35fe-b206-bcf0334da7da | -6.4485 | -59.9909 | 2026-09-20 13:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 6f1eae76-6423-3b1b-9065-b58c25d49d67 | -8.7192 | -45.4546 | 2026-09-20 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 99f8232f-b33a-3d5e-b44f-54e7fe1dd221 | -11.1183 | -54.0062 | 2026-09-20 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 24ac4aea-2c3b-3a86-b9bf-bd402cf86e3d | -7.5711 | -45.4333 | 2026-09-20 13:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| cc167718-50f0-3663-8b02-e453dce80b9a | -11.4537 | -45.3892 | 2026-09-20 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 25589e66-7d21-371e-855e-65947a097978 | -13.2222 | -51.7382 | 2026-09-20 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| b1951e0b-1050-3992-8401-ebb1cfceb278 | -11.155 | -42.7885 | 2026-09-20 13:00:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 6f22cd4d-0c3c-328e-92f9-c121fa6c288d | -10.3914 | -48.9133 | 2026-09-20 13:00:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 1e371168-775d-3aac-99c6-dfb25cf6989a | -12.1711 | -47.0356 | 2026-09-20 13:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| fbb2946a-3b1d-3ab1-87d3-7d69de20584d | -10.8553 | -50.9459 | 2026-09-20 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 176.5 |
| ecf22d98-cfc1-3732-b2f1-3842f9536af3 | -13.203 | -51.7406 | 2026-09-20 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 5c7605fe-ef47-397f-be50-b570f4b83eae | -13.2219 | -51.7595 | 2026-09-20 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 21d20762-24e0-3f3f-86c8-75ef2265f6fc | -11.3787 | -51.4412 | 2026-09-20 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 9abea82d-47df-302b-a274-e45e0f8d7086 | -7.3259 | -55.6153 | 2026-09-20 13:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 6e1e95ec-138e-30c5-b81f-5c8edd27bc9f | -10.7902 | -46.3203 | 2026-09-20 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 8824b4f5-b289-35e7-97a1-5e58e24f568c | -11.379 | -51.42 | 2026-09-20 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 184.6 |
| 6f9f2c30-f9fc-3c69-bf7c-d08f4fed5ce7 | -13.2602 | -51.7548 | 2026-09-20 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| f9ea94b0-e06a-306d-b986-985d02b09ae4 | -11.3793 | -51.3989 | 2026-09-20 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 970c73a3-bc5c-3711-8e71-f41f2d68c3a2 | -12.1328 | -47.041 | 2026-09-20 13:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 6866844d-a093-3ac0-9e76-6df2c5e1383b | -14.6856 | -46.6886 | 2026-09-20 13:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 457d1453-1cd6-3b16-a42d-ef727ab0e9cf | -8.7729 | -44.2568 | 2026-09-20 13:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| e8ac45dc-46df-38e3-9beb-9f3a9618cc81 | -10.2787 | -50.2605 | 2026-09-20 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 9ac10a25-1f12-393c-8fa1-36e446edfd08 | -13.241 | -51.7571 | 2026-09-20 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 2adac2ad-1d15-373e-b790-1ddf6d1f0934 | -11.0991 | -54.0285 | 2026-09-20 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 215.5 |
| dd264eba-a312-3266-bcd2-c24fb51910e3 | -11.0259 | -48.2944 | 2026-09-20 13:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 014fc4d5-90b1-3574-974c-00f41e2af56b | -7.156 | -47.4312 | 2026-09-20 13:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 8a48141c-678d-3260-8e66-79d89579aa3e | -14.6861 | -46.6657 | 2026-09-20 13:00:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 0381308d-6f50-32af-bd47-5dc30251b8f5 | -8.8636 | -45.9596 | 2026-09-20 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 7113ea00-3d9f-3c11-9ed7-02983d66f342 | -12.152 | -47.0383 | 2026-09-20 13:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| fdca0b1d-ef60-3cb3-b1bd-e96562509dd6 | -12.7616 | -46.2029 | 2026-09-20 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 193.3 |
| 5647d338-ce90-36fb-bf7b-a402f55d34fe | -11.0256 | -48.3164 | 2026-09-20 13:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| ff7c15f3-7077-3f3d-99ed-58df4d38cc93 | -11.398 | -51.418 | 2026-09-20 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 8025f508-0c3f-3aa9-8154-8cc029f95290 | -7.7444 | -46.7184 | 2026-09-20 13:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 60a6cadc-d102-3f6a-8f76-a939dccdd561 | -13.2606 | -51.7335 | 2026-09-20 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 431b46f8-8b9f-3b11-995b-9a055fb3cc0e | -12.5224 | -50.0484 | 2026-09-20 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| d462a107-bcac-3f23-90bb-0eb667356511 | -8.4314 | -45.8467 | 2026-09-20 13:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 80ab0bb2-8cfb-3d64-8790-43ac27a12684 | -11.118 | -54.0268 | 2026-09-20 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 183.0 |
| 9435ecbf-5712-3c4a-a9ac-3412802e149f | -7.1742 | -47.4736 | 2026-09-20 13:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| a82e93a1-a3da-32e2-aaf4-4680b7646ceb | -8.0689 | -46.2645 | 2026-09-20 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| e3832559-033b-356e-a98a-6155111f6a43 | -11.0802 | -54.0302 | 2026-09-20 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| b8b524c8-edd0-36ff-a4d6-1791ef91a3e3 | -11.8747 | -49.9983 | 2026-09-20 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 966b13bb-e48c-3c5b-8100-36b3d7defda7 | -7.211 | -44.0252 | 2026-09-20 13:00:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| f5445d94-118c-3078-b62d-b0d992de7783 | -12.7653 | -52.8661 | 2026-09-20 13:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 121.4 |
| b6782b0f-4bca-326e-a662-d6dd34aa34bd | -9.8313 | -48.4073 | 2026-09-20 13:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| a3f60455-e879-38ed-af8d-a350f299c871 | -8.1688 | -54.7432 | 2026-09-20 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| caf1c65e-fc55-3410-9f43-cf50e7406612 | -10.2598 | -50.2624 | 2026-09-20 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| c2d46182-0ce5-359d-a5a2-8d4bcf9ee75a | -11.4541 | -45.3662 | 2026-09-20 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 616ea06a-24a0-3e74-9c8c-bb2af4777389 | -10.7899 | -46.3429 | 2026-09-20 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 169dc64b-f8d4-3f5e-9efa-0cd32439a427 | -11.0994 | -54.008 | 2026-09-20 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 3bc530e2-e195-3e16-ac68-98dd65d8eed0 | -11.6609 | -43.4239 | 2026-09-20 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 600f40d4-22b9-377f-94b5-6216ebfc9726 | -7.5334 | -45.4367 | 2026-09-20 13:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 585440c2-ceaa-3879-bc2c-9a1ac8d0412b | -9.3488 | -46.3793 | 2026-09-20 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 22f80b52-c02a-3275-a1da-f8c2387a780f | -11.8487 | -46.8781 | 2026-09-20 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 21dfa9dc-da9e-3ee3-89d1-02e99c2366bd | -7.2881 | -45.5494 | 2026-09-20 13:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| dc77f907-0fff-3fa8-8dda-5909c54c3fbe | -8.3727 | -47.589 | 2026-09-20 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| e81647bc-cfd2-3b75-9375-24475bf761e4 | -11.1369 | -54.0251 | 2026-09-20 13:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 29b351db-3b89-3807-8780-0d7793095218 | -9.8397 | -46.4361 | 2026-09-20 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 1fa234a4-57d3-3437-8999-36754a01f8f5 | -10.2982 | -50.2158 | 2026-09-20 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 152a381b-caf0-33d2-b5a8-3de32df3bdf2 | -9.5536 | -46.6031 | 2026-09-20 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 6723b122-b52d-3910-9c6b-28b1fee6a08c | -8.1376 | -46.8155 | 2026-09-20 13:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 1b2753bc-7a23-32c9-8ac6-e7eead570e62 | -10.3914 | -48.9133 | 2026-09-20 13:10:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 87321bf8-613f-38be-b6e5-56bd0d1d1985 | -10.3168 | -50.2352 | 2026-09-20 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 08982813-0337-3bc4-86e2-8c259b333e90 | -10.473 | -51.2808 | 2026-09-20 13:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 0899a825-9ec5-337a-9d74-8e33709df1c9 | -7.4286 | -44.7409 | 2026-09-20 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| b75bbfe6-3af5-3430-9a08-321c106cbe65 | -6.467 | -59.9902 | 2026-09-20 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 5f8013b1-f6b1-31ee-bd35-16cc4fc73182 | -9.26 | -45.9616 | 2026-09-20 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 0eb731bd-bde7-3e27-8c29-589d485533fc | -11.0994 | -54.008 | 2026-09-20 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| d4fce454-52c4-3a79-8d69-bd194941a075 | -10.3171 | -50.2138 | 2026-09-20 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 137.9 |
| cd0b9d74-4eb3-3569-9929-abda377b0f5a | -11.4541 | -45.3662 | 2026-09-20 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 04f43093-a019-3320-94d5-3a7c420d7559 | -13.2606 | -51.7335 | 2026-09-20 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 112.1 |
| bdd02568-7a35-3339-b848-325713c5b53c | -6.778 | -47.8545 | 2026-09-20 13:10:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 5f98ea5a-b8fb-397f-ab63-9607d4a7730a | -8.9267 | -50.0057 | 2026-09-20 13:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 4e39484e-beee-39d5-99cf-738f2b4d620c | -8.7729 | -44.2568 | 2026-09-20 13:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| dbd8c88a-7280-39ae-8283-f3a454ab6be8 | -11.4924 | -45.3608 | 2026-09-20 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 2286f80e-99be-3236-98c1-ca04cdba2866 | -9.2606 | -45.9164 | 2026-09-20 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| d206f860-e259-36d6-9b32-9e0345e81e64 | -14.1258 | -45.5904 | 2026-09-20 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 3a74843c-d5ea-3e86-865d-5ee93d3100dc | -14.6851 | -46.7115 | 2026-09-20 13:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 104.0 |
| f65b5a7b-52c6-3ac9-87cc-34ff732714f3 | -11.1183 | -54.0062 | 2026-09-20 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.3 |


[Clique aqui para ver as próximas entradas](README116.md)
