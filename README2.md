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
| 9efc4115-9141-352c-8f3d-ef04d607fe1d | -23.77915 | -55.32372 | 2026-04-03 05:16:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| af7e5d82-d723-37a0-97b2-6290ee76a9cf | -20.54709 | -55.87646 | 2026-04-03 05:16:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c3447ad-7d13-336f-99d4-d214686be276 | -20.54641 | -55.88165 | 2026-04-03 05:16:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25b5ac0f-799f-3ae2-8ee3-446018ce9004 | -30.40613 | -54.26506 | 2026-04-03 05:18:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 6.1 |
| 21b6feaa-6d80-3a21-aec2-1c30c6c2511c | -30.40368 | -54.26392 | 2026-04-03 05:18:00 | NOAA-21 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 4.0 |
| 864bfd62-bc67-3241-9c77-80ca1c0758c2 | 2.82258 | -60.21167 | 2026-04-03 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84a7ebcb-0536-3dfc-baca-dbb0111c7dbf | 1.30745 | -60.65667 | 2026-04-03 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42ce16c5-ae9d-3dc0-bf33-d66ab2be0c5b | 1.30071 | -60.65772 | 2026-04-03 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2421fe1-27ce-3175-bacc-c0ecc5552f14 | 1.30802 | -60.66024 | 2026-04-03 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 036c9f81-8ae5-30c1-bebd-e4f8b7637068 | 1.30465 | -60.66076 | 2026-04-03 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d6773de-9011-321e-8dff-0f2f07dfab37 | 0.96759 | -60.40993 | 2026-04-03 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e8cdede-7784-381a-9c10-65832dfc6d12 | 1.30128 | -60.66129 | 2026-04-03 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc83bcdb-0e2c-3ad2-9bf0-65eeaa18e7bb | 1.30408 | -60.6572 | 2026-04-03 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ec18c91-119c-38c2-963e-fb25e6bbfa47 | 1.28991 | -60.61185 | 2026-04-03 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26c6e0ad-562d-3232-ae45-7557a640f90e | -9.4633 | -59.19743 | 2026-04-03 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f268391a-d80a-38e3-863a-847ecdc541cd | -9.46383 | -59.19376 | 2026-04-03 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0dfdc082-78db-3cd0-9f94-67215fe0ecce | -9.1162 | -61.49079 | 2026-04-03 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f52f2ae-874f-397a-904b-bbcdc5724959 | -9.11977 | -61.49134 | 2026-04-03 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50210dde-1ba7-33bb-aebf-9df61dc95520 | -9.45973 | -59.19313 | 2026-04-03 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3b3d54fe-7347-3c9c-bea6-3ac41989f2b4 | -9.45921 | -59.1968 | 2026-04-03 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6b6f431a-5435-32dd-8e8a-96c4c644d3b3 | -20.54651 | -55.87899 | 2026-04-03 05:46:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a970c3d-e4e7-385e-881e-1e5c80903caa | -20.5435 | -55.87751 | 2026-04-03 05:46:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef39856e-4756-3dd6-a4b3-3e23ce8a7308 | -20.5431 | -55.88198 | 2026-04-03 05:46:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6690f1a9-a84f-3762-b6d0-d32a18b7a1f1 | -21.66637 | -56.31878 | 2026-04-03 05:46:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3113a8c5-45b9-33cc-ae0c-b90e1d059b61 | -21.66599 | -56.3231 | 2026-04-03 05:46:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 985f4425-23d0-3359-8835-e13281735dda | -22.18007 | -56.9702 | 2026-04-03 05:48:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc9effae-7a27-3df7-8392-87742649e316 | -22.18612 | -56.96637 | 2026-04-03 05:48:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1fc955ad-e198-3230-845e-815a1cf9efa7 | -22.18574 | -56.97049 | 2026-04-03 05:48:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d61b72c-7d86-344b-a877-fcf5fa5b06a1 | -30.40426 | -54.2658 | 2026-04-03 05:50:00 | NPP-375D | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 2.4 |
| 5fbad2fb-7f46-3e69-a883-b3dc956682d1 | 2.82308 | -60.21194 | 2026-04-03 05:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4158a2cd-bbbb-3c14-8ff0-11c96c29a6f9 | 2.13063 | -61.25753 | 2026-04-03 06:01:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 578d161f-88ea-35c6-a335-c143d1054676 | 1.30657 | -60.65839 | 2026-04-03 06:01:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 27d82c02-239a-379f-a59e-84acfa9e7b8b | 2.12986 | -61.25283 | 2026-04-03 06:01:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0c332911-bc9a-37c1-80bd-6f62ff8bbf6b | 1.30172 | -60.65915 | 2026-04-03 06:01:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 369aa6b5-9d77-3336-b2d1-d589c0f36d10 | 2.11982 | -61.22032 | 2026-04-03 06:01:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5909b58a-0d27-3e69-81f6-27fdc9dfbaef | -9.46105 | -59.19212 | 2026-04-03 06:03:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d7369164-3eea-3286-9cd1-f8fc0008a0d1 | -9.45808 | -59.19605 | 2026-04-03 06:03:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 769aa423-91d4-3fc9-8e34-81cd259480a1 | -9.4604 | -59.19712 | 2026-04-03 06:03:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c549b73-7709-31be-be55-b8ed36c10cb6 | -22.17876 | -56.96609 | 2026-04-03 06:44:00 | AQUA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 10.4 |
| bdbc2a5d-9be3-335a-a0e4-3ce5762a3a3f | -23.02352 | -52.6805 | 2026-04-03 06:44:00 | AQUA_M-M | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 662e062a-3010-3fb2-9359-06bb2e60a999 | -12.05978 | -45.09998 | 2026-04-03 11:06:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| d903b569-77a2-393d-bb7a-dd404656ed81 | -12.05968 | -45.10784 | 2026-04-03 11:06:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 6792348b-eb2c-3118-8a4f-a855c90d8ffe | -18.92852 | -39.96421 | 2026-04-03 11:08:00 | TERRA_M-M | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| c00f5f66-b6ae-30f8-913f-dd2d8ec4a0e3 | -9.4599 | -55.93452 | 2026-04-03 12:44:00 | TERRA_M-T | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a094dc6f-3530-3119-b24e-915cb27b401f | -9.46627 | -59.19175 | 2026-04-03 12:44:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b36c6604-6bd5-369d-b967-54da310f142f | -18.49224 | -54.72731 | 2026-04-03 12:46:00 | TERRA_M-T | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 13.6 |
| d8c3d06c-6f87-38e0-a1ba-fa38781c3f2f | -20.52578 | -55.52926 | 2026-04-03 12:49:00 | TERRA_M-T | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 9ea46cb4-fcde-38d1-b9ca-dbbce0228a5b | -29.15822 | -56.38906 | 2026-04-03 12:49:00 | TERRA_M-T | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 11.5 |


