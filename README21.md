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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9de8229-7e1b-38e2-a8e7-b01cbff5c90c | -14.77662 | -48.29484 | 2025-07-19 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e5181c5-d4a8-3ec0-9fc4-af7dc5ddb704 | -9.83628 | -48.37432 | 2025-07-19 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb55ea38-ebdd-3cae-8f2e-378191f4464a | -12.03184 | -48.76151 | 2025-07-19 04:36:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b11d6cf-78a4-3f97-b250-28d0ec0de24c | -12.37448 | -50.33562 | 2025-07-19 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e845b76f-d636-3235-a1cb-89cb31847a0b | -13.79011 | -48.49641 | 2025-07-19 04:36:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37223752-8c60-32ff-a3a8-34e6dfb0fc1a | -12.03461 | -48.76558 | 2025-07-19 04:36:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2c43882-07f3-3c00-a531-1becb6b9678b | -13.0492 | -49.1756 | 2025-07-19 04:36:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| af6768fa-3aa2-3939-a89b-c8aa79694b30 | -10.66757 | -49.67967 | 2025-07-19 04:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b01a42a-137a-3f2f-b410-d57758a0147b | -12.42092 | -45.37059 | 2025-07-19 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a5d252d-36ab-37c1-b3ad-d2cc3c32ffb1 | -9.83905 | -48.37834 | 2025-07-19 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a23f610-cfa3-3e95-a7eb-0045d8a403a6 | -10.03221 | -46.30882 | 2025-07-19 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfe9ff4f-6fba-3e11-b82a-593775d70900 | -9.81667 | -47.74027 | 2025-07-19 04:36:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 96842a21-a905-3eb7-8738-2ab9a8542f24 | -11.96098 | -47.01652 | 2025-07-19 04:36:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49245f5b-9b00-31bd-89fe-83b0e115813a | -12.43217 | -45.37227 | 2025-07-19 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ce0a10d-7ed7-3701-818c-17b6f3b948bc | -11.48489 | -47.33032 | 2025-07-19 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a02bc700-c321-3439-9dca-a45bd3f9ad9f | -14.70062 | -45.07368 | 2025-07-19 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6cc4750a-73c1-3a6d-9837-0f67afd0d148 | -11.55595 | -47.09264 | 2025-07-19 04:36:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f744882-0fb7-3a2e-b9aa-ae07d05a6848 | -9.40221 | -47.96777 | 2025-07-19 04:36:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7452f54c-d8b8-3161-8b26-d8718f76ccea | -11.48205 | -47.32608 | 2025-07-19 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af8f2dfe-3000-305f-b7a1-c600ce7dcba2 | -11.88869 | -55.44915 | 2025-07-19 04:36:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e18d13f7-f45e-30ce-b1b9-9390b7c36050 | -12.03572 | -48.75852 | 2025-07-19 04:36:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fa70c89-7c71-331d-b7c5-68c401622cbb | -12.71516 | -47.79403 | 2025-07-19 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f732d583-913b-31c7-ac4a-cb17c26413d2 | -11.5242 | -48.95409 | 2025-07-19 04:36:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0592e8da-b5e5-3d20-a50d-b7b63dfc75ae | -13.00156 | -46.93674 | 2025-07-19 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e6cb98b-c5a0-32d8-9000-b7a335f4392f | -14.74586 | -48.26376 | 2025-07-19 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4316b89c-8b1c-3fb3-a65a-e425a014de75 | -10.62318 | -44.7639 | 2025-07-19 04:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 92eb9cfe-e204-34f7-9437-a9f74432cd82 | -15.89322 | -43.45554 | 2025-07-19 04:36:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| eb874fff-bad3-3171-bb6a-fe507ed3c276 | -11.96041 | -47.02034 | 2025-07-19 04:36:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c3ad646c-2d4e-3966-9fec-352537015a19 | -10.81423 | -49.29009 | 2025-07-19 04:36:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73d4539c-d160-30cc-8883-7417b906810a | -10.63323 | -44.76739 | 2025-07-19 04:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a48bc7f2-901e-3c9c-ad46-8ded7c067874 | -11.96823 | -45.46886 | 2025-07-19 04:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbd5db53-a160-38b8-8ada-7ea2545ccae5 | -9.94972 | -48.16602 | 2025-07-19 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00207010-8d56-3430-a65a-39cc977514b2 | -12.13915 | -50.23716 | 2025-07-19 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dbdd4991-85c3-3ad4-acfe-9d669149c95b | -11.57311 | -47.09531 | 2025-07-19 04:36:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d477769a-6050-303a-961d-8e4f6be6e7f7 | -12.97536 | -46.92066 | 2025-07-19 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a80a1903-06c7-340f-90ff-b9e65ac86b25 | -12.99687 | -46.94414 | 2025-07-19 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 471eb0f3-2b86-33f1-8fa0-b1154c77e6fc | -8.96761 | -61.51051 | 2025-07-19 04:36:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b58228af-ea03-39d8-b155-aa12d932c3fc | -11.56454 | -47.08236 | 2025-07-19 04:36:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1b4a098-4d08-398c-92df-ea1186b48873 | -11.73566 | -48.19081 | 2025-07-19 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 3e153e1d-24eb-3c8b-a702-dd5b9ef8d91f | -14.48276 | -46.35644 | 2025-07-19 04:36:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5b2ce70-4e60-30f2-955c-0b2fe9ec32d7 | -12.67974 | -46.82805 | 2025-07-19 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| defe5d01-a458-3bfd-8c0c-987e0a70e781 | -10.23138 | -48.24692 | 2025-07-19 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8541eac3-e1ce-3fff-9b6f-9bb6da381301 | -12.06716 | -47.35348 | 2025-07-19 04:36:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24f696fd-38da-3d5a-82dd-10b8809e5e8f | -13.05308 | -49.17261 | 2025-07-19 04:36:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b1befc65-dd3d-34ad-bb19-d6dd72dafde1 | -9.43655 | -48.84737 | 2025-07-19 04:36:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71899547-e2f7-3e5d-a69c-837c1a83e2c4 | -11.48602 | -47.32289 | 2025-07-19 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7809322b-8002-3bd9-b392-c3bed484df6f | -12.0324 | -48.75798 | 2025-07-19 04:36:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8062d77c-0767-3a0b-9f93-29324ede4049 | -9.81054 | -47.73566 | 2025-07-19 04:36:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 864b7337-b7c2-3ff0-9fdd-88a46bb38a01 | -12.98591 | -46.92191 | 2025-07-19 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40d73002-3f31-3666-bee2-48edac6ab375 | -13.60897 | -45.63866 | 2025-07-19 04:36:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76bfcc1b-53d0-3613-89ea-159f25738d8f | -12.36104 | -50.33337 | 2025-07-19 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| faf3e73a-1b46-320e-97b8-af48432fd7e3 | -12.46703 | -46.92565 | 2025-07-19 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4909ed05-31ba-3249-8ec6-84dd81bc7b7b | -11.83037 | -48.21315 | 2025-07-19 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 19238462-23ba-3707-979f-cb482514832f | -8.97305 | -61.51052 | 2025-07-19 04:36:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83e30aee-a12e-3fb5-a742-5a5ee914fc78 | -8.9718 | -61.51706 | 2025-07-19 04:36:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f529170d-40e7-35bc-8a25-16b499aab6fb | -11.72842 | -48.19332 | 2025-07-19 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 0e1eced2-64ea-3d73-ab3d-950ccf7b8862 | -13.00215 | -46.9328 | 2025-07-19 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb949659-36f9-3d45-87af-16965731a612 | -11.33274 | -44.85571 | 2025-07-19 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00c37943-5d84-31fc-a84b-85eb871326e5 | -9.61489 | -49.02367 | 2025-07-19 04:36:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 537d284e-7de7-33bc-981d-93c62ff0f206 | -12.3717 | -50.33144 | 2025-07-19 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45544d07-830a-31e0-93f2-d6f00a1198ea | -9.27271 | -50.26101 | 2025-07-19 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ef3972e-d804-3c5d-9a89-73b36a13ffdc | -11.4732 | -48.22218 | 2025-07-19 04:36:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 93978fbd-0c21-3d12-9ffd-c5fcb6a996e7 | -10.8148 | -49.28657 | 2025-07-19 04:36:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b548e6b-8431-3a3d-ad0d-c22ec69c9a76 | -15.92636 | -43.51413 | 2025-07-19 04:36:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01b82b01-57b4-36a1-9582-e584756f9054 | -12.42401 | -45.37574 | 2025-07-19 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ba7bc96-44f0-308b-9be5-dc991a558f8a | -11.52365 | -48.9576 | 2025-07-19 04:36:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6cdc9365-4f4e-37da-9c37-20d86d7d1d5a | -11.37219 | -54.34356 | 2025-07-19 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6480a89-8ef0-3fa5-873e-8834bd4b684d | -12.98992 | -46.94288 | 2025-07-19 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e696dbe5-6a1d-31ad-ac5c-dddc5b523eda | -10.06074 | -59.10104 | 2025-07-19 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9895001f-995c-3436-a8e8-b8af1360247c | -11.73844 | -48.19492 | 2025-07-19 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87f1d204-f54e-34d5-b453-2413a4b9ad31 | -14.78055 | -48.2918 | 2025-07-19 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 62a38fb4-e37f-3ca0-905f-40502a9c11d1 | -12.09163 | -44.73818 | 2025-07-19 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 02bcffaa-e1b8-356b-8f32-80605de7e865 | -11.72563 | -48.18921 | 2025-07-19 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| e9789fef-df0f-395a-87ef-29055cd495ce | -11.82647 | -48.21618 | 2025-07-19 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f5a24b9c-9e78-3718-aa6d-18efc1bae5e2 | -11.47864 | -47.32555 | 2025-07-19 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8f65805-afcc-31a8-b5d5-fb9acaa43668 | -10.72711 | -46.78744 | 2025-07-19 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71a108ee-9886-3175-8c30-1839b9c86c2c | -10.63456 | -44.76558 | 2025-07-19 04:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 11696747-f927-3d13-b70a-1244fca8b1b1 | -12.06374 | -47.35294 | 2025-07-19 04:36:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d1e1bd3c-9216-3dbe-93c4-108b0574f65d | -9.38122 | -47.95382 | 2025-07-19 04:36:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a6ed799-9f8a-33f5-94f9-6996426ffb30 | -9.80889 | -47.74631 | 2025-07-19 04:36:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84109788-a1cb-3275-8b58-de5b01d5d971 | -10.85477 | -47.16296 | 2025-07-19 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3a46371-6724-3046-a5c5-10fcc74508e7 | -11.55996 | -47.08939 | 2025-07-19 04:36:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 947ca4e0-2657-36bf-802b-0488093e968d | -14.70525 | -45.06911 | 2025-07-19 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fdf1274f-a561-34af-89ab-ffd61d4d34f0 | -10.67931 | -49.67064 | 2025-07-19 04:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ee5615e-9919-3d7f-8fcd-7d36aff71b6e | -10.09317 | -47.23853 | 2025-07-19 04:36:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 81c1738a-c16b-342d-8cae-e0825daa2dcc | -12.3644 | -50.33393 | 2025-07-19 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab743bf2-4f78-35d5-93b7-1d0c967077c7 | -10.76056 | -52.76545 | 2025-07-19 04:36:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 56de4de5-81f6-31a7-a5bb-f4f0b48d3771 | -11.83427 | -48.21011 | 2025-07-19 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e821b095-795a-3463-99d1-6ca48fb86b50 | -9.76679 | -48.75022 | 2025-07-19 04:36:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dee0489c-d6fe-32b9-a0b1-2ef9ca30746d | -11.35999 | -48.72921 | 2025-07-19 04:36:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2712d29-b803-35cf-8683-9ed228bdc27b | -12.42026 | -45.37518 | 2025-07-19 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af91d68d-8659-3e8c-bfa7-9f71031f4b4f | -13.60083 | -45.64205 | 2025-07-19 04:36:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2935bd0e-7909-35cc-8ddb-5bd691d97509 | -14.7602 | -48.2657 | 2025-07-19 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ba330ee-a510-344b-a215-bdd2d80a4d67 | -11.83816 | -48.20708 | 2025-07-19 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 782bedd3-c493-3600-a3da-69e7fae9a4a3 | -11.89384 | -55.44567 | 2025-07-19 04:36:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0991cc47-654d-3817-98e3-5c4593b8a633 | -11.73176 | -48.19385 | 2025-07-19 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 582bb26e-75c9-3557-b564-83f407484ed7 | -9.39176 | -47.95188 | 2025-07-19 04:36:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26ac263e-d92f-3379-9fc4-f9c33ddb49d3 | -10.20886 | -48.36911 | 2025-07-19 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0dd3753f-58ed-315b-9544-4155bf0890f8 | -11.89306 | -55.44997 | 2025-07-19 04:36:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f3edf5a8-e8d0-307d-b934-761e4616b22b | -12.03517 | -48.76205 | 2025-07-19 04:36:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README22.md)
