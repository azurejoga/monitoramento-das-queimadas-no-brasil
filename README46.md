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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6acfcf2a-36cb-34a4-88de-674ffeea6f2e | -7.6469 | -45.27607 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06b20a45-45d0-3476-abe6-20341b8f9623 | -10.81942 | -43.28205 | 2025-08-20 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 26f13b86-c399-3a89-a80d-dd76e9dbdc1b | -13.19148 | -46.89912 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1a0d45a8-d2b5-3203-8bec-b35f9139130c | -13.08283 | -46.82783 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7d1f5583-3477-3fb9-beed-1527bc37b091 | -12.98461 | -45.1918 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 52a436a7-f359-34b3-9b79-89d2d0302750 | -13.00352 | -45.17749 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 225932a2-fce0-3f3d-8e1c-5273012d3f2f | -7.54738 | -63.84689 | 2025-08-20 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4818939-faa2-3b7b-b8fb-5654d511dee4 | -9.51727 | -60.54115 | 2025-08-20 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f60c0e6c-2e9e-31b4-9103-21c724bb9d2a | -8.0287 | -47.67056 | 2025-08-20 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| fba56556-7a00-3074-96dc-863851938275 | -11.31179 | -44.92616 | 2025-08-20 04:57:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ad773f3-a9c8-3910-9fb0-208097d7dbbd | -6.18791 | -55.46318 | 2025-08-20 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c1be343-d010-3d0f-a4c6-27f64fc8b726 | -10.91208 | -57.50403 | 2025-08-20 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7fd8423-ec3a-35c8-b120-fea5e287a0e4 | -7.28991 | -43.68372 | 2025-08-20 04:57:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ac86665-97bb-342f-910e-83573e13fd3e | -10.0108 | -47.80761 | 2025-08-20 04:57:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e6511fc-ef65-34c3-b1ad-881f31c5e342 | -7.07007 | -46.87782 | 2025-08-20 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa98a1fe-5324-3df9-bbda-64641fb9ea3d | -11.67138 | -60.18285 | 2025-08-20 04:57:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a3e41ce6-d143-3ca3-85fa-578d0eaef96b | -9.07431 | -60.418 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e366f40-cd01-3c97-9dfa-daa0265dca4d | -10.27559 | -46.77164 | 2025-08-20 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 412bb7c9-8311-316a-b092-b642e7784dd2 | -12.50928 | -57.77811 | 2025-08-20 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2d20972-46c6-366b-838c-035e3afbb432 | -13.0036 | -45.18129 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13e6ec1c-6d6b-3ef8-8da4-1639836c7762 | -14.16441 | -45.28281 | 2025-08-20 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f889bd0a-f826-3ffd-b0c9-808dc6364058 | -11.31582 | -55.13252 | 2025-08-20 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 354e88c9-5659-3a21-99fd-9ed43cf09efa | -7.44656 | -50.27452 | 2025-08-20 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0e2099f1-55b1-3a41-87ee-952c9bd2ce45 | -12.98855 | -45.20546 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fe784584-565b-3b7b-8939-fca7bff88909 | -9.25148 | -44.49717 | 2025-08-20 04:57:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d6501bd8-6059-3264-aa42-a1eb51bba4ae | -12.91381 | -46.10205 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ea8a7af-ea28-31a4-92c0-db9c4ea00c96 | -8.8743 | -62.39219 | 2025-08-20 04:57:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60959d41-e922-34d3-afa6-92eaa6af9110 | -12.98411 | -45.19598 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16a98add-e8cb-3803-a2c4-a30b04bc082a | -12.98793 | -45.21339 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee46ecf2-7693-30d7-b662-0d54d5d6d33b | -10.11262 | -57.76 | 2025-08-20 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b302424-6313-3e1a-ace9-fe64663e89c9 | -7.59434 | -55.18967 | 2025-08-20 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 846e0aa7-fc73-36b3-9cf5-7eb56e4575fe | -13.48625 | -47.06066 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f503494f-0211-3256-8da1-3d757d6619fc | -10.60249 | -48.5999 | 2025-08-20 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bbb19bd5-2af8-31b8-a506-926858a0a003 | -9.2263 | -60.33941 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e27581da-8b08-39ed-8af8-aa981e4a21fb | -8.13995 | -49.51391 | 2025-08-20 04:57:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f4621e7-5772-3ce4-87d3-b5ed3e64dd23 | -7.23042 | -44.7056 | 2025-08-20 04:57:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f41e9de-9a2e-31f7-887c-c1b9d5cc4ad3 | -6.46015 | -53.37637 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba5a98f3-b8d9-373d-8220-e4027dc35cd8 | -13.02654 | -46.80868 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9dbe64d1-14b1-353c-aa87-67930b973b5a | -8.02478 | -47.66508 | 2025-08-20 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 610ab2f2-0a24-3dfd-bd7d-3db3920c6bd9 | -12.37054 | -54.16806 | 2025-08-20 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6efeaff4-0ba8-39ad-b196-8b1aa16fa4a9 | -7.12627 | -44.64314 | 2025-08-20 04:57:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2bad64f4-c790-3ec0-884c-6aeb784c6cac | -7.39441 | -44.27393 | 2025-08-20 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e3cb41b-f261-3be6-8449-30bf5103af23 | -13.57755 | -47.01514 | 2025-08-20 04:57:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 316fb690-0dd8-3640-8555-ab5874f7c178 | -9.26439 | -44.5351 | 2025-08-20 04:57:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cfdd16f-afc1-3f06-8385-6892286f8d32 | -11.58517 | -50.54349 | 2025-08-20 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bde136f6-a59b-3850-aebd-81c52b63754f | -9.24565 | -44.49658 | 2025-08-20 04:57:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 973cf336-5eee-3292-81d1-0d39e52f7887 | -13.03934 | -46.79134 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25e623ac-6582-3360-a129-2a94226d0bdb | -11.31251 | -55.13199 | 2025-08-20 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e3bec9c-de27-3352-91af-9d2442e9f18d | -8.69577 | -54.51754 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 69eeb4a5-8414-3e77-95ba-dd5df1d371ff | -9.81122 | -46.89083 | 2025-08-20 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14ea65d7-0078-357f-986d-fa0f5a6ebf88 | -14.15755 | -45.28114 | 2025-08-20 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 439a00db-6b1e-32c4-9afd-bd7a968045a5 | -10.39043 | -54.13953 | 2025-08-20 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa1daf2a-33e6-3942-b3b0-dec2cd632676 | -9.1763 | -59.61466 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9ec19148-e1a9-3b38-9736-6fa35453b0d4 | -13.02952 | -46.78519 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8350826-5fe9-3f91-b51f-889f1be71901 | -7.59174 | -44.39268 | 2025-08-20 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8c80b2d4-7851-3247-876f-8ff922e9fd9a | -9.17894 | -59.59949 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 519fcd4b-e2be-3cfb-a68b-dbedc7cb48be | -9.1951 | -59.623 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 14404869-da95-3ba9-b32c-2b20906fa1e7 | -7.50045 | -63.83114 | 2025-08-20 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23088471-cd56-3626-bf2d-898aabbe5814 | -9.23084 | -59.60326 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b8574e0-3610-3330-841d-77d4082bf00a | -10.24403 | -64.48425 | 2025-08-20 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6a610875-11f0-36a9-b978-df2d9c237d38 | -8.17065 | -47.35533 | 2025-08-20 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67e63454-7909-379f-a9a7-0695674e5c05 | -6.46458 | -53.36986 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be850891-87da-32f2-bb45-b4ed27049742 | -13.02912 | -46.78839 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 79986ad7-51d1-325f-a230-b9ee274160eb | -13.58198 | -47.02219 | 2025-08-20 04:57:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5275754-9c08-3e5f-b63f-8b9435778993 | -12.98902 | -45.20127 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| db75b53c-3cd0-3478-bc70-2a4a9edc3f67 | -10.46762 | -48.3524 | 2025-08-20 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d67129f9-f241-3044-adb3-64de615656fa | -8.87247 | -62.40261 | 2025-08-20 04:57:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8b5dab20-4e76-32c6-b4e1-ff1aede04c11 | -7.63179 | -45.26611 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| aa17ba89-cb06-3f62-9b47-1e47e00e2bfe | -13.39702 | -47.49141 | 2025-08-20 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ffbb4026-ac98-35a9-98d2-a5045884588f | -9.87112 | -45.9761 | 2025-08-20 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 30c932c0-a751-3a32-a082-eb26381a9be8 | -12.11069 | -47.90175 | 2025-08-20 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dda1c6b2-d05a-30b4-8322-a121620c08bd | -12.36716 | -54.16753 | 2025-08-20 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a37802d-6d57-3116-ba82-6cd0991a3077 | -7.58987 | -44.39357 | 2025-08-20 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4a50ede2-3d4c-3214-95d1-a3d7c419d2b6 | -13.55623 | -44.45912 | 2025-08-20 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61a3716e-9372-3396-930b-f3a8dbc1284e | -6.26711 | -52.82264 | 2025-08-20 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50e197b1-5f1f-3582-ad26-6e86dc0253d0 | -13.18084 | -46.89942 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d729356-f399-330c-958f-97741b1a8f55 | -10.24774 | -64.48138 | 2025-08-20 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 70a9db1d-2cfb-35d0-bafd-9612b30bb363 | -6.45682 | -53.37585 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c725b1c7-4570-3ef3-8169-0efbc367d6a8 | -12.81075 | -48.56358 | 2025-08-20 04:57:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b34f7b2-2ab9-38ca-9be5-7a829b5d88b2 | -10.43326 | -62.12906 | 2025-08-20 04:57:00 | NOAA-20 | VALE DO PARAÍSO | RONDÔNIA | Brasil | 1101807 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 122b6b80-2719-32c4-9e6e-15dabce4242b | -13.18051 | -46.90213 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| baa816e8-a663-377b-8b6b-2fa400582bfe | -12.58864 | -47.07436 | 2025-08-20 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9fc34e6e-8aaf-3f0e-9074-236257a7c09a | -7.66592 | -45.25787 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb62a331-3df0-3568-93ee-9dc0bc934cdf | -7.25941 | -50.18331 | 2025-08-20 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2a88a4d-9f02-362e-9dbf-de8c058bcade | -9.22777 | -59.59754 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c46c03f9-86bc-3bc2-ad3b-f87842fb2190 | -12.98943 | -45.20087 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 05e4896f-72a4-3d95-a2ab-ba105aab0b4a | -14.15755 | -45.29062 | 2025-08-20 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf102191-cf42-3b88-84af-89ab9ed6d558 | -7.65468 | -45.25954 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa4d592c-b694-3954-ad5f-a6274485c2b9 | -6.26656 | -52.82624 | 2025-08-20 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b6f5b0f-6d93-34ff-bbfd-c05ac2f7c671 | -9.31279 | -48.93268 | 2025-08-20 04:57:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfbbf75c-9620-3e4a-bd67-53d5f75fbfb1 | -8.02412 | -47.66982 | 2025-08-20 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5cc92811-1188-3fc3-af90-f90096e14f8b | -8.69447 | -62.10072 | 2025-08-20 04:57:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f21d738-1749-3c65-9015-e196ecdd1ec1 | -8.79442 | -45.48062 | 2025-08-20 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27b59b93-dcb2-3958-83a0-f0db3ef378ca | -9.18942 | -59.63246 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bb2e4dc3-b0f4-315b-8b8c-727ed16c8fb1 | -7.25484 | -50.18763 | 2025-08-20 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5d53bbf6-7ecb-3e36-bbbc-3a1101fd9d40 | -13.40307 | -46.37318 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 87f87fdb-45c5-3526-8904-2272a0864e6d | -5.80071 | -59.21571 | 2025-08-20 04:57:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9694120-23ce-3930-a46d-d9f2ca2b705f | -10.46302 | -64.46838 | 2025-08-20 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17b96e38-9942-3629-aa82-b3bdca72f739 | -7.04923 | -59.23291 | 2025-08-20 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bde52450-79fe-3c99-b96a-c0c5e0c25769 | -13.87211 | -45.56649 | 2025-08-20 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README47.md)
