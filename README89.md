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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03849103-3bd7-3eab-8fd3-df6109e4f110 | -5.83069 | -53.67397 | 2025-10-03 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7520ec35-8134-31a5-8be0-16e63c956ef0 | -9.34047 | -45.74495 | 2025-10-03 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1449b83-b998-3d04-9818-25a1e064da0f | -11.22766 | -48.20023 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12c0e8df-3754-3cd6-b611-67501de8ceda | -11.07376 | -48.35994 | 2025-10-03 04:32:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b9eafae-7b3a-32ed-9baa-79916a7026f2 | -7.75319 | -42.55744 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 2d68c8f8-1938-3e5f-92d0-5d43ae1dd5f0 | -11.14339 | -43.37796 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5f8d1408-651d-352c-9c54-c5b97f32bb50 | -10.87712 | -47.05032 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e356bf5c-8b9a-3a21-96d0-eccdf81c2c88 | -11.68356 | -46.96857 | 2025-10-03 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c7e68f0-c388-36de-adbf-45732d9cabc5 | -10.94644 | -46.70449 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8920f20-903d-32f1-85b5-6eecb96f689e | -5.78251 | -45.75006 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e92ca2c8-063a-3d3b-add9-8c44bacce71f | -7.52298 | -38.00534 | 2025-10-03 04:32:00 | NOAA-20 | NOVA OLINDA | PARAÍBA | Brasil | 2510204 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c94e2345-55d2-3e53-bef3-8ce6c25fa29a | -12.42227 | -44.08452 | 2025-10-03 04:32:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2feeced4-ae4b-35ae-955e-34611e39dcdf | -11.41319 | -43.49105 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fbd5ce7-cb2a-3927-802a-7c55988327d8 | -11.58624 | -47.65681 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ce8f842-9b08-39ae-bfd1-00a7b0756de1 | -11.63029 | -47.98731 | 2025-10-03 04:32:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 102862ea-63f7-3d3e-8b5b-895e09402a19 | -6.13894 | -46.54435 | 2025-10-03 04:32:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3873b23d-9525-3bd0-bcf2-74134eec5357 | -11.06022 | -47.79199 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b9317f4-a7a9-3562-939b-4482a97b8f5b | -11.81239 | -45.02597 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 087447c4-8e65-364a-8e7a-63e339c88a9a | -6.82529 | -45.98244 | 2025-10-03 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd4c77d8-9ce6-371c-88ee-3b87d6f0a265 | -6.27489 | -44.05101 | 2025-10-03 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7cfe2a56-cd4e-3359-876d-8316f6b46811 | -11.80818 | -45.00207 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a36f466d-00d6-3ad5-89c3-48e504a090bc | -7.76135 | -42.58956 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b2f0ca58-8f94-3095-a3d6-2d8d25f1fe23 | -11.11183 | -47.85146 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6be2adf1-6feb-3459-a5e8-8bf6f6e86a6f | -6.46079 | -44.2059 | 2025-10-03 04:32:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4833ab27-97c1-3fbe-b8a3-ced2749ee18e | -6.34143 | -44.30397 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ec88fa9-c444-399b-9674-d650e2918999 | -9.9848 | -48.78374 | 2025-10-03 04:32:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44012017-4d26-3f34-abbe-b35242c5448e | -9.92052 | -43.77419 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| f21199ea-3793-3714-94b8-05893f0287de | -10.2736 | -50.36582 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1bc69d74-fea9-38f2-88b2-15a2dcd9aa05 | -9.10016 | -46.72106 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55044ae1-9475-3319-bb12-e2e0629579e7 | -6.70937 | -44.61699 | 2025-10-03 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 649665e1-bfd1-3665-8012-ddc0ccf1c4b7 | -11.59458 | -47.62476 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ab4d752-58de-3573-af7b-ce7dcfa9dfd6 | -4.50842 | -55.45896 | 2025-10-03 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15ff0a56-6e4a-371b-abb8-32b911dc370f | -7.76525 | -42.53208 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| d421ff21-f111-32a6-a6c6-0cbf7033545d | -7.88744 | -47.3493 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5daab07-3db1-35c7-827e-15a60dd7979d | -7.50048 | -48.8538 | 2025-10-03 04:32:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 43facc2d-d6ef-30b4-a890-d681e523a3fb | -9.58115 | -45.87536 | 2025-10-03 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a0fec3f-8810-30fa-a5bd-10e35d3fdd77 | -11.81796 | -45.04045 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a1d2984-e362-3682-998a-b5b671270ad1 | -8.24509 | -47.03701 | 2025-10-03 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 25d04732-81c0-3da6-905f-221381ccebb8 | -10.97054 | -51.08082 | 2025-10-03 04:32:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40c59d45-f333-346d-9819-5d5b909908ef | -10.33492 | -48.17705 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c4c3684b-5501-3f67-9ae1-30dfd1dbbdc9 | -6.04043 | -46.07758 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ae1cc1d-d496-37cf-b527-0d209501b83e | -11.05966 | -47.79558 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ec9c36a-dded-3d15-b075-3740b90c7f6f | -10.56034 | -56.56349 | 2025-10-03 04:32:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 378205d2-bc4e-3a85-ae44-fa8966559493 | -11.83271 | -45.02112 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d208510-1b53-3fe7-9c5d-f294f956ccc4 | -11.50578 | -43.51079 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1875c4c4-6c51-36e6-85a8-5f6cb65547cb | -10.35049 | -43.73194 | 2025-10-03 04:32:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8504cf21-a40e-3b4b-9f1f-0292364a433a | -11.61514 | -45.03166 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a117f5e2-c5fa-3656-8785-c4761570d5cf | -10.94911 | -51.08115 | 2025-10-03 04:32:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 962b85b9-e46c-36c1-9e74-1119cb00d8a0 | -6.09614 | -43.12413 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e9bd6912-71d4-3e5a-aa59-bf12e2fef78e | -6.72486 | -44.14174 | 2025-10-03 04:32:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 46e0dfca-7713-3484-8973-af7481f236fa | -11.59346 | -47.63206 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a14a7395-e2c5-3102-bd77-e157fed95bee | -11.55992 | -47.64894 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 46bcedee-1aac-3551-92d8-b75430686e29 | -11.11128 | -47.85503 | 2025-10-03 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd48aac6-5a11-353b-b51a-de127e8fa588 | -6.6577 | -42.78779 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 611d9821-c1c9-33a5-bb9b-dd9ee03b563a | -10.87077 | -46.55671 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3dac3c0-424f-349c-b155-7ca80489665d | -10.94473 | -46.71592 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 1faa5b96-950d-3e7f-b6cc-93d4180091dd | -10.95562 | -46.71368 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d482de90-fefb-3b52-adc4-4180d8f670ec | -7.74892 | -42.57256 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bdf1a89b-2094-355c-90f5-e357cc28420b | -11.82891 | -45.02079 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1d4b4464-edde-33ac-b152-0c01cfb2c7f6 | -7.75139 | -42.58442 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e71fe0f1-2a53-30a2-a7e0-3f0962ace8f9 | -7.8209 | -46.97077 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4241954b-c469-3391-9d35-6aba067830d6 | -10.97337 | -51.08528 | 2025-10-03 04:32:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a89f3f52-cb81-3dbc-9311-103ec73a2104 | -11.62695 | -47.98677 | 2025-10-03 04:32:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 450fbb0f-f00c-374a-bdbc-2184a8cf5a24 | -9.75227 | -48.34222 | 2025-10-03 04:32:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c80da0a-ad44-3d0c-9c69-f26b9e87cb7d | -10.2851 | -50.29563 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 47229761-58ac-32af-b606-cf51e52bbcfe | -6.87528 | -45.47728 | 2025-10-03 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0fcfb6f-0658-3a3f-981b-1fca288a7126 | -10.61023 | -48.71652 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46715817-e5ac-3519-8ba0-ceb3ac0c6d09 | -11.83184 | -45.02431 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e0cfc657-1edb-3e5a-972e-7dbc49b57f33 | -9.91071 | -47.71705 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fa66efb-96ae-35a4-b1e1-207f7ffdfaf0 | -10.60417 | -48.71196 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 9690ac91-afce-3f36-9e88-5492ccca9fa5 | -11.55546 | -47.65569 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a3d473d-90f2-3e3d-bb9b-a02c343039e6 | -11.13674 | -43.39552 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5cdf0a38-7dd4-3c9f-9860-1ab04ee6d92f | -11.0591 | -47.79918 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 672ac9eb-d416-38cd-83dd-e0040f0bfcc4 | -7.07501 | -45.81369 | 2025-10-03 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f0a175e-c9b4-387a-960d-47d2e4b4bfcd | -10.16078 | -45.49728 | 2025-10-03 04:32:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9175101c-0281-3d1f-a966-8a389bc45e35 | -10.83425 | -41.27434 | 2025-10-03 04:32:00 | NOAA-20 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 6f3f1a57-42da-3aa8-b60a-227edca02249 | -11.44762 | -44.9591 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bce316fb-31d9-371d-ae00-a8fc807de124 | -7.25072 | -48.48006 | 2025-10-03 04:32:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 203438b1-7e7d-31b6-8f9d-c31fe51c7be7 | -7.7749 | -47.37466 | 2025-10-03 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 94a777a1-93af-3f22-83e8-189bba4eeaf8 | -11.08186 | -47.86852 | 2025-10-03 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ec0b61f2-424a-31c7-9337-19c05706125c | -11.80527 | -47.93457 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0d7ecb9-082b-3bf5-8f9b-bd0d7ea7c8cd | -7.75911 | -46.26297 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| cf36bd27-a1e7-30fe-a7c1-2ed25ec9cb52 | -7.77123 | -49.94017 | 2025-10-03 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 167709d8-fc67-3301-a0ac-c2ef38f525f1 | -12.00469 | -46.57976 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5ab4f16-21d4-34ae-aeb8-ee54135a1b47 | -11.83012 | -45.00988 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b76da31b-8aa5-3999-92c5-1a3a684e0093 | -11.90698 | -46.31477 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a025dba1-445e-382a-a096-762981dc98f9 | -10.89318 | -46.71238 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2add318-d14a-317f-a26a-e6ad451e8203 | -11.59402 | -47.62841 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 556a79e0-9c55-329e-bf13-3f2dc4b89140 | -11.45301 | -45.13315 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cbde7e6-4821-389b-a4f2-272ddc406ef4 | -10.21383 | -50.3217 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3d42c02-7cb6-3423-843f-c8015d90e8d8 | -11.41731 | -43.49164 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83c78356-7425-38c9-9bc9-c6354d1bfb1f | -9.41262 | -47.53756 | 2025-10-03 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90ae5d52-2bbd-3c29-bb78-a0f7ff0fce1b | -5.84247 | -43.37416 | 2025-10-03 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f846ac9b-2ab8-3cf9-a1b5-6ee557971884 | -11.31374 | -47.83926 | 2025-10-03 04:32:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11dd8c33-fe75-3138-8f15-21731ca6d651 | -6.54747 | -43.88177 | 2025-10-03 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3296760-1040-382e-a11c-8ef77f35b73b | -8.98223 | -46.71397 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a73cc84c-8198-3553-9211-48d5ae73310a | -12.11328 | -43.43897 | 2025-10-03 04:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cccbb12-23a1-3f32-8b1f-ebf20ac2b3cb | -7.74433 | -46.24554 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa73af0c-1d3d-3c3e-a611-1b1d36c4c11c | -5.77739 | -45.7607 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94768b12-ec1f-3490-bf99-f6c200152196 | -10.98255 | -46.67502 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |


[Clique aqui para ver as próximas entradas](README90.md)
