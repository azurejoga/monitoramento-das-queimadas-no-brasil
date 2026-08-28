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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 030dac13-3fb5-376e-bd25-2cce21b4eb80 | -8.6881 | -49.5353 | 2026-08-28 15:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 77991be4-8f49-3ce8-893e-3628449d43b7 | -6.2676 | -53.3768 | 2026-08-28 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| c92360a4-49ce-3cc6-a2be-7d28ad4a8b75 | -8.776 | -50.0616 | 2026-08-28 15:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 2ca1cf7d-2123-323a-8b14-98387824bffa | -9.2282 | -51.5428 | 2026-08-28 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 8cad8d1e-4235-33f9-b8b8-5290fdff1a81 | -12.0729 | -47.1838 | 2026-08-28 15:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 153cd12e-09d2-3ee4-916e-d7c3067ac37b | -6.2298 | -53.4805 | 2026-08-28 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| b15fcdd1-a9c3-35ce-a5bb-47aa84f645bc | -13.4194 | -51.3945 | 2026-08-28 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 188.4 |
| 48ded485-c6c8-3a75-88a5-7ac30192f0d4 | -14.6024 | -53.1508 | 2026-08-28 15:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 138.1 |
| f7221269-fffa-3af2-bc49-81f95efd84d0 | -10.3202 | -49.9782 | 2026-08-28 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 2310370e-2636-33f7-b8a0-03ff4133258c | -11.1995 | -55.1008 | 2026-08-28 15:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 39654938-1814-3bdc-82b5-4bb2bfa690fc | -10.3895 | -61.231 | 2026-08-28 15:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 6f393567-e355-355b-bb5a-1a471d81f837 | -10.5598 | -50.4236 | 2026-08-28 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 6e3025c3-bd00-3b0c-875a-102ea47b9825 | -6.7648 | -59.4408 | 2026-08-28 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| e1d227d4-3964-393c-ae0b-9ffb6b291d18 | -6.8018 | -59.4201 | 2026-08-28 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 84ab16cb-6bf5-3594-83b9-c7df51260d97 | -12.0541 | -47.164 | 2026-08-28 15:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 302db993-8267-3fc2-a130-5c50cc8dbd78 | -8.6694 | -49.5369 | 2026-08-28 15:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| c83e5f00-eb2c-36b6-9b31-c1f8ac9fc83f | -14.4847 | -53.2707 | 2026-08-28 15:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 105.0 |
| b6d3aa3b-3970-33c1-90f3-184e34d62cd6 | -11.7354 | -54.5431 | 2026-08-28 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 60b8e2cf-7bab-32c9-98ee-84670c06ea58 | -6.848 | -42.8451 | 2026-08-28 15:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| f0941fb2-8524-3ded-83a8-105f964020eb | -10.559 | -50.4876 | 2026-08-28 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 3e916ec5-7102-35b4-8996-838b033bbbab | -10.3337 | -50.3829 | 2026-08-28 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 9a79eb63-8fcf-3461-8b47-04b9150b2eab | -13.3447 | -46.9304 | 2026-08-28 15:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 9c742ae7-26ea-30eb-b8e7-4ead19ed837a | -8.0551 | -45.839 | 2026-08-28 15:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| eb277e9d-4005-3bac-9503-16ff096dcbe3 | -6.769 | -58.7066 | 2026-08-28 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 145.5 |
| 94b98dae-6da4-37db-bb97-c5ccbb5aae9f | -8.795 | -50.0387 | 2026-08-28 15:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 2457e43e-b323-38d2-9225-3b918787b8cc | -11.006 | -49.6461 | 2026-08-28 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 725f226c-13aa-30bb-ac98-7e53d8df7c56 | -6.1741 | -53.5037 | 2026-08-28 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 1e9fa71e-b31b-36ad-a819-3e06e0500fa2 | -11.2302 | -45.0528 | 2026-08-28 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| b663e06c-0448-3e6b-a6ee-b7e0f06b171e | -11.025 | -49.644 | 2026-08-28 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| e48dc8d1-250c-34e1-95fb-59410a18bd92 | -11.8243 | -47.1954 | 2026-08-28 15:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 3e315ae0-d15c-3a07-8d57-a3d6a3630099 | -13.4132 | -51.7784 | 2026-08-28 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 140.8 |
| e956efdf-38d6-3deb-a1f8-78e13dc1a2ec | -10.5593 | -50.4663 | 2026-08-28 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| c9a6c8a7-5678-369f-9317-6bb6ca42b894 | -10.9592 | -50.2744 | 2026-08-28 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 761a0e07-86e0-3058-bedd-6451d8a3d2e8 | -6.8571 | -59.4179 | 2026-08-28 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| b8aef784-3ae8-3f5f-825f-73ef2a06951a | -8.3717 | -62.716 | 2026-08-28 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.3 |
| accba0c7-a954-3daf-897d-2e6123e69532 | -10.3205 | -49.9567 | 2026-08-28 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 5f0aafa6-27e6-3eb0-b54f-0e42fe6d2e56 | -9.1525 | -49.9639 | 2026-08-28 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| b4c070c7-bc80-33ba-be0b-7c738ba8685d | -8.7757 | -50.083 | 2026-08-28 15:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| ca4a536a-32b0-3f75-a5b7-94d2c86e141c | -15.3846 | -52.689 | 2026-08-28 15:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 502e802f-ce0c-3460-bfe8-c5537a115734 | -6.8019 | -59.4008 | 2026-08-28 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 3f2b58af-34d2-3210-8a61-cafe8e7623a1 | -9.1713 | -49.9622 | 2026-08-28 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 2c55741d-1300-3ce4-8b4d-1c3b987120d0 | -10.3391 | -49.9762 | 2026-08-28 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 952fad93-c3ed-3589-b6c0-88d4afe3c034 | -14.4444 | -53.3806 | 2026-08-28 15:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 7b3c1b81-548d-3208-aa6d-20b25032ad20 | -6.7513 | -55.6853 | 2026-08-28 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| da94374d-d6d8-33ca-b549-3151df8ff1af | -11.7167 | -54.5244 | 2026-08-28 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 639c975c-8ae5-31fd-baad-87439568e72f | -14.1645 | -52.8269 | 2026-08-28 15:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 96.6 |
| d51f6aa9-1d92-36f8-bb16-fdbb52767fe8 | -6.9521 | -58.9506 | 2026-08-28 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 520635f9-d211-3a5f-b3cf-6d002203dfec | -15.4983 | -53.9603 | 2026-08-28 15:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 66502a03-75a5-3266-b282-ed323013f90d | -10.498 | -64.5193 | 2026-08-28 15:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 70.7 |
| de5d2417-491f-383b-a946-0fa1a2d1ff5d | -6.9872 | -59.2582 | 2026-08-28 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| e00960f2-f1e7-3d82-b092-b09278678737 | -11.7736 | -54.5191 | 2026-08-28 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 3e809f04-e5cb-3d3b-9ea0-37bd5fcf4475 | -13.2294 | -51.2904 | 2026-08-28 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 1a4c6eb3-a750-3856-89c0-8da37ba665ff | -9.9708 | -53.9419 | 2026-08-28 15:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 284.1 |
| b02035dd-da27-324f-81d3-4e806fb9ed68 | -11.7165 | -54.5449 | 2026-08-28 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 5f56eaa8-e0b7-30d4-a088-8429fd8fd391 | -8.948 | -62.3894 | 2026-08-28 15:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 133.3 |
| 2d79fc83-7db5-302d-86a1-ffb52a6edf4b | -6.2692 | -53.1526 | 2026-08-28 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 132.8 |
| 500fade8-0c1e-3d9e-ad49-d064349875e7 | -6.7832 | -59.4401 | 2026-08-28 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| bc523df9-0010-3f15-a3e6-21bd693b07a6 | -14.9161 | -40.9358 | 2026-08-28 15:10:00 | GOES-19 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 87.3 |
| f4a9f61e-ea38-3398-9bc8-cd9ef9932079 | -6.5865 | -55.4346 | 2026-08-28 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| cdc0f26c-ff8d-3306-be80-4fcfedde440e | -14.2097 | -45.2973 | 2026-08-28 15:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 02b5e700-54f2-34e4-8503-32f7a1224ca9 | -12.3041 | -50.5701 | 2026-08-28 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 492.2 |
| ade494b8-656c-37eb-a8cf-06867e3a851b | -10.8422 | -50.5219 | 2026-08-28 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 67a1c322-3771-3728-a9e1-ab13457e4ddf | -10.8996 | -46.6216 | 2026-08-28 15:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 68d9077a-4524-3fdc-a9a7-ab59a3cd1fd2 | -6.2693 | -53.1322 | 2026-08-28 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 187.7 |
| 31ccff66-016b-3cb7-aa97-f27544ab8a57 | -12.2854 | -50.5509 | 2026-08-28 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| dd439d68-c63b-319c-9507-81b1a858e073 | -10.899 | -50.5159 | 2026-08-28 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 69c5970d-b452-3c16-b836-502499f065b5 | -10.3897 | -61.2118 | 2026-08-28 15:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| fb01c5f5-2f12-323b-bbc6-3de2ec44661b | -15.4788 | -53.9628 | 2026-08-28 15:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 6f78d026-1ca7-3979-9d15-5a8e0f611091 | -10.5601 | -50.4022 | 2026-08-28 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 5c8878ad-10b2-34c7-9375-b002898c442e | -12.3038 | -50.5915 | 2026-08-28 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 188.3 |
| dfd28c79-51a5-3d86-829f-ae401d495b8b | -7.3665 | -55.1534 | 2026-08-28 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 36d7d823-da4b-3b5a-b70e-60ca62cc8446 | -14.2734 | -52.0726 | 2026-08-28 15:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 2b0eeb35-c0d1-3587-ab66-5cf67c7c987a | -13.5075 | -51.8728 | 2026-08-28 15:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 5ab9337d-b226-3920-be3e-fd4e06bc76bc | -9.8617 | -65.0334 | 2026-08-28 15:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| a93faafb-5e05-3ca5-b2b9-db93804df8bc | -11.7546 | -54.5209 | 2026-08-28 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 5c5fb5ad-bd82-3b29-8bd0-13ef2b8f11b8 | -7.4953 | -55.2862 | 2026-08-28 15:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 5a6718b1-2c68-3b72-a233-d5e018845487 | -6.1556 | -53.5047 | 2026-08-28 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 1b8ae7a6-a620-337b-8a41-51683bebf6c4 | -14.2102 | -45.274 | 2026-08-28 15:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 173.5 |
| dd1c9770-5d91-336c-a715-9cabc4e59a46 | -10.9556 | -50.5311 | 2026-08-28 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| d8cf5063-86fb-3fa6-a164-0011efa24ca8 | -10.4693 | -46.1802 | 2026-08-28 15:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 119.7 |
| ccf7736c-d1f5-351f-ae91-cbe2535105d0 | -11.7357 | -54.5227 | 2026-08-28 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| af319059-d8bf-3c80-a1ee-92e61f3216be | -11.1998 | -55.0805 | 2026-08-28 15:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 0b42e851-0c61-3b77-9ad6-0863f0ab9a49 | -10.4981 | -64.5005 | 2026-08-28 15:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 148.5 |
| 7eb7b3bf-7a95-30e9-892c-57dda8232fa5 | -16.1641 | -58.5851 | 2026-08-28 15:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 395.8 |
| d0773750-2dcd-3d82-b581-b40f9d785dff | -7.3478 | -55.1744 | 2026-08-28 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| c6591dc6-8429-3897-9330-043e9d00b54b | -3.4628 | -39.60181 | 2026-08-28 15:12:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 7ceeb78a-628f-3d68-8315-4ce13a1e09fd | -11.26 | -54.02 | 2026-08-28 15:15:00 | MSG-03 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 20f29a38-3a2d-3d0a-99d4-9ceca16b3e9b | -12.24 | -50.6 | 2026-08-28 15:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b83ab427-e817-305d-a4a8-5796750be9b0 | -10.09 | -46.99 | 2026-08-28 15:15:00 | MSG-03 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| beee0175-51f4-35ec-b935-8a7a866710de | -8.6852 | -62.9496 | 2026-08-28 15:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 133f1f27-4a91-3d1c-9c0d-3dfbd4eb9908 | -10.8422 | -50.5219 | 2026-08-28 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| e02d95f8-d1eb-3687-9fa6-be2c14161c86 | -10.7407 | -54.0401 | 2026-08-28 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| f320072b-d2ac-382e-bb4a-bf33cc0dc30e | -11.7165 | -54.5449 | 2026-08-28 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| f279ea8d-97c3-3f73-97b4-abc0361501e0 | -10.7975 | -54.0146 | 2026-08-28 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| f87f77af-1c81-38db-a213-add1a5b68f3c | -13.3597 | -51.5299 | 2026-08-28 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 39a5582c-0a27-3685-9bcd-b4f4e299981c | -6.6397 | -53.173 | 2026-08-28 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 25a1ea38-b37e-33d9-b411-8ad1982a2584 | -8.1858 | -47.5184 | 2026-08-28 15:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| c3cfb8b0-cd03-3af9-b78f-f17b409ab09c | -8.9478 | -62.4084 | 2026-08-28 15:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 153.7 |
| 22867f16-32c9-37ec-bf40-84e2409b56c9 | -7.3324 | -46.6656 | 2026-08-28 15:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| cd450b96-2e6e-32a2-9170-a44001a28a7a | -8.0742 | -45.8147 | 2026-08-28 15:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 176.8 |


[Clique aqui para ver as próximas entradas](README83.md)
