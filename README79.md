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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea08c72b-a321-3fa6-af9b-e6a2c1203b3d | -10.77722 | -54.74831 | 2026-10-01 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| de9140f4-0061-3222-9df0-eb472030a612 | -6.66487 | -58.87465 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 2dd07d19-6eea-3c73-bbfb-417609bec14e | -7.53783 | -47.12559 | 2026-10-01 05:18:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8a412e14-a580-3a2b-9d8e-334233381662 | -10.46842 | -59.12799 | 2026-10-01 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff653247-db6a-3f7f-a13f-1d874b863e54 | -6.1344 | -53.26915 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1509e29c-eb0d-3c80-84a4-3cd7c53fbe54 | -10.54062 | -57.78051 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3ffbb53-6ef3-3ab2-a699-3a0d5331aa83 | -11.79053 | -50.41684 | 2026-10-01 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02b549d8-856e-3929-a5e4-97ea75ccecfa | -9.02487 | -60.53421 | 2026-10-01 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 736bef40-a57d-3024-a7c6-e050ad0e2fad | -5.82256 | -57.74545 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d992232-f412-30ea-aa86-93b7e7b1e0b2 | -10.78915 | -50.52655 | 2026-10-01 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b496cd1f-c33c-3ce8-b8e9-0e31101ce462 | -10.6644 | -58.91422 | 2026-10-01 05:18:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e12892b8-a906-3d1a-9f52-7f6b043b2bab | -11.79612 | -50.41759 | 2026-10-01 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e874298-024d-3837-8cbc-95d3e421ee6f | -5.12509 | -56.01442 | 2026-10-01 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0b560f9-39a5-382e-8022-6d2ac381fd54 | -6.05509 | -59.92296 | 2026-10-01 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42fb1f3d-a061-3193-808b-0b349dcf8da6 | -10.25176 | -49.67421 | 2026-10-01 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb82cafc-b36e-3216-90a2-8a834088664f | -11.41417 | -51.02097 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b1657ceb-5eea-37a2-ac98-b44e38d512d7 | -6.84555 | -59.3558 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3481e9ad-8149-37f1-8560-2903d510ca92 | -10.84177 | -48.69887 | 2026-10-01 05:18:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5d49fde5-bff6-346b-9918-b029f304bae3 | -11.33008 | -50.97035 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4ebcfe45-fe22-30af-9cad-839ffc93e473 | -12.18699 | -48.44008 | 2026-10-01 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| c5406102-f90d-35ff-8551-a6e83982e7c5 | -10.28531 | -53.97186 | 2026-10-01 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c1b60e9-2476-34d6-bb88-d69c933c726c | -7.54788 | -55.04429 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4bcf6fc0-0c61-3d2a-a297-94a561b0e3b9 | -7.35156 | -55.59218 | 2026-10-01 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3c48511f-62e6-369c-a314-9895694ff338 | -6.92778 | -59.28381 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac6e22f3-f430-3387-8d88-7ebf20d62b74 | -8.16362 | -54.83653 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7f181ab-47bc-3f23-ba02-59845768b606 | -8.26612 | -54.73821 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c5f706e8-eb37-3a37-9a04-0e2d0222772d | -11.40306 | -51.02291 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 189220ff-8157-3185-8cf4-fd32278072e4 | -8.27181 | -54.75484 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 620e47f0-3dd1-3a63-9158-995983937ef5 | -7.50352 | -45.8356 | 2026-10-01 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cce96415-6e75-34b8-8d4d-edf8a2874714 | -5.12154 | -56.01389 | 2026-10-01 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7dbe1fb5-9746-319c-b3f2-febfa672cea1 | -10.24279 | -59.02724 | 2026-10-01 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c83e558d-3e49-33f8-acf5-6a7ee9736a7c | -11.73015 | -50.40926 | 2026-10-01 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e9b1ad4a-4e95-349a-a973-44e918d6dd90 | -7.33614 | -55.22307 | 2026-10-01 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8033380-af2a-3daf-8f3f-11d82ec613a7 | -6.13901 | -53.06329 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 505aa8e2-c55a-3e6a-84e3-889ab594feae | -7.49435 | -45.7945 | 2026-10-01 05:18:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5785976f-0757-3d67-a6fc-f882fde6d279 | -6.72747 | -45.53739 | 2026-10-01 05:18:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a67f9272-a74b-39c6-8b6a-684dad9491a6 | -9.88892 | -65.14127 | 2026-10-01 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10b866e7-bda4-34cf-b8c3-edec81480f94 | -10.54646 | -50.00732 | 2026-10-01 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77102b8d-96ee-3591-b911-b7028f30adc7 | -11.16811 | -54.11407 | 2026-10-01 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a5ce113f-dc84-3781-be90-7bc145b62fe0 | -7.80718 | -49.84765 | 2026-10-01 05:18:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| db9fb09e-3c4d-3ef8-b154-456c29201bad | -5.25172 | -57.1196 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09aa3138-ed98-305d-8823-49551cbdfa8b | -7.55771 | -55.03095 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8f6d8f17-eeb5-3a64-8407-d1972b52655e | -7.71257 | -54.79351 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6a9a651-0c20-3f2b-8918-882b158a5976 | -7.99682 | -61.36771 | 2026-10-01 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5386cf89-82e0-3b0a-a1a6-e5049985bdf1 | -6.14402 | -53.26237 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ffc53406-561e-370e-9f3b-63951531eae8 | -5.12214 | -56.00993 | 2026-10-01 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a5aa9b68-ade7-3061-9838-e6e629062b8f | -7.72041 | -54.79474 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5784ea3a-0869-3046-b09f-c1530858f8be | -9.12505 | -60.39624 | 2026-10-01 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76d6e507-bc8a-3607-a64c-82ee40cf164c | -7.57422 | -46.62191 | 2026-10-01 05:18:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9122ee20-525b-308a-bc77-360f83f85529 | -9.78139 | -59.02074 | 2026-10-01 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9bfc2d3-ce9e-35bd-b1ed-782288353acd | -10.56561 | -57.77143 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fea75ef8-bcb3-30ae-84d9-13867bf1486a | -5.85552 | -57.75407 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d500d5f4-a6dd-37cb-905d-0400471d9d87 | -7.45859 | -54.99437 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 554c7fdd-fd65-3180-91fb-1dc262e8cc62 | -6.12448 | -53.27986 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a165f4ff-6363-361e-879c-bca6c8bc5774 | -6.34091 | -55.32427 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94f786db-17ac-314f-95a1-c456c292136b | -5.11502 | -56.00897 | 2026-10-01 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| ee601edf-662e-3a34-a1fb-246e56998568 | -11.26615 | -54.81511 | 2026-10-01 05:18:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40b879c7-7397-364e-a9c3-d62791cbbb9a | -6.6665 | -55.08986 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 00c61bd0-94a8-354a-a3a1-634465d32c3c | -11.39771 | -51.02219 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad6799ae-bb82-376c-8170-e1ac8cd6df43 | -12.18991 | -48.43464 | 2026-10-01 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 11a2db80-776a-3fa3-83b0-f9d094105967 | -10.84656 | -48.71123 | 2026-10-01 05:18:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 67fcd382-ad75-3484-835f-957ece125228 | -10.80949 | -57.23801 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e946d8b-319f-391e-b4bf-2f438c6b0368 | -9.93078 | -63.76075 | 2026-10-01 05:18:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 950da4c0-60c8-3a21-9254-4fdc0d2a5ce1 | -12.19455 | -48.43047 | 2026-10-01 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| aef10293-9291-3e22-8cd6-3a1db3e266fc | -7.78353 | -55.62993 | 2026-10-01 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| df89ebe4-769d-3624-8f3f-7b343e90af62 | -11.83584 | -50.51117 | 2026-10-01 05:18:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 078af95b-c85b-3251-91f3-f1bf3304e384 | -7.59448 | -55.07548 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b605706-8c4e-34bb-acd3-23be701f2499 | -8.18207 | -54.78855 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c609ce51-39da-3908-b4ee-0471942553e5 | -8.84376 | -49.70438 | 2026-10-01 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e692049-c211-365c-b76b-68cf483d5ab4 | -7.49629 | -54.99153 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 69310ff4-b12f-3898-b3bd-d87ed5f5444d | -6.66817 | -58.87516 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.7 |
| c4abf6b6-1320-332b-9a8e-94dc9dc4eca1 | -8.15945 | -54.81005 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb268d95-2d32-320d-b771-fbd6954b955e | -11.28557 | -50.97816 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4ccfbb15-8fa2-3679-b55a-45f20513cee2 | -11.33544 | -50.97108 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5922d104-24e2-368e-b105-2558b2f129c3 | -7.729 | -54.79087 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 295b884a-e87e-38cb-8dd6-6f9b88ab8ba3 | -8.15155 | -54.8089 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cd3d786-beea-3b01-879c-5f271adf0aec | -6.35754 | -55.34053 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e60e97b1-b92f-37a0-a834-fc4aa7d89a03 | -5.85442 | -57.76122 | 2026-10-01 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d279d37f-4e47-3f97-be9c-a5f068166efa | -10.53947 | -57.76453 | 2026-10-01 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| daceab2b-1eeb-3a1b-b563-2d89e06e7c36 | -7.70472 | -54.79234 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a2e1103d-308d-3821-af94-608af2c2e1ca | -9.54869 | -56.16431 | 2026-10-01 05:18:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a40851b6-1e71-3631-a29c-e38f2fc853d2 | -7.54859 | -55.03942 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c27a35cf-7cae-3cb7-ad6e-d4a1e0bd0843 | -6.03469 | -53.36294 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65d40452-b3f8-35c7-a5ae-4cf27a8c72e8 | -10.46449 | -51.76679 | 2026-10-01 05:18:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05cee89a-b04c-39ea-8295-920b0d9247cd | -7.5493 | -55.03459 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 84b788a2-d5da-3f8a-a144-6d0ce4fd7550 | -8.88932 | -50.65348 | 2026-10-01 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12a7a4fe-b8a9-3c84-b657-1e8fed30326e | -6.92832 | -59.28036 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d68b9256-2b68-381c-83e0-97d645b48472 | -10.77206 | -54.7552 | 2026-10-01 05:18:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0c75bba-cefb-3649-b45c-ca8d911927c3 | -11.38217 | -55.12032 | 2026-10-01 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edb2b923-d610-386b-9a67-439102db6d32 | -11.41384 | -50.97922 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1d2ce19-e6ec-36fd-9888-af4e4d291029 | -8.38859 | -46.28698 | 2026-10-01 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6c8158a7-c9ee-39f8-bd32-a57c67f55c20 | -11.28598 | -50.97474 | 2026-10-01 05:18:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| ffd93826-8f39-3678-91f4-17300904538a | -8.24888 | -54.66037 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed3839ea-eafb-3be2-acff-a89e34055122 | -6.68684 | -58.8639 | 2026-10-01 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bdc49b60-3e1e-31f0-b465-8efe49361246 | -6.9234 | -59.2902 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b383c581-5563-3da5-b629-ef6cc33f2732 | -6.66541 | -58.87119 | 2026-10-01 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 7a1cbff3-d058-3bb2-920d-d4e9f9796004 | -6.08852 | -56.47213 | 2026-10-01 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e457d082-6f68-3597-95d0-639ca31e9191 | -10.77259 | -54.75146 | 2026-10-01 05:18:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ced714c8-fd3c-3704-9f5e-3d2471c72ec3 | -6.01105 | -49.55709 | 2026-10-01 05:18:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 5f2fc0ca-cf69-318a-a069-4263c1312fa7 | -8.18218 | -54.7926 | 2026-10-01 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README80.md)
