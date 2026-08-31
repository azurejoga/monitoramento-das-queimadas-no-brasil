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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ac17445-a00f-3d1a-b5c4-9ffe3d1561f1 | -6.60213 | -58.59946 | 2026-08-31 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 71998be3-8756-3eaa-872f-9e3aa165dcfa | -6.78941 | -55.68426 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06efbece-8546-3b68-9a4c-429036e4222d | -5.57205 | -60.23095 | 2026-08-31 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f44a2c72-782b-36c5-a422-456f0a6beec1 | -3.61295 | -59.07527 | 2026-08-31 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 997262f9-ab77-3099-bad7-068ff53fcdae | -5.94627 | -57.69056 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 83f78fda-067d-37e0-8f6a-05f536082a7f | -3.93792 | -59.32667 | 2026-08-31 05:33:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9791c568-b78d-30d8-b42d-e258f293cd96 | -4.16089 | -60.69641 | 2026-08-31 05:33:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ca9208c-6828-34b2-8535-98985fb19d9e | -5.24621 | -55.89393 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 61f5ccb0-2d34-3869-826d-11bedb2ba30d | -6.59918 | -59.1143 | 2026-08-31 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62ba4584-2eb9-376b-a1c0-705dd8171b8e | -5.87651 | -57.7716 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6966ae3e-5865-3952-b86b-5f80c3136f02 | 0.14251 | -60.40432 | 2026-08-31 05:33:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89d247d1-5066-329c-a9cf-cb614f4611c0 | -5.96179 | -57.68464 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b046354d-f4e9-3f49-9a16-cd4b819c4b01 | -6.25214 | -55.48261 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71ea18ce-cab5-321c-83c1-a05abe786766 | -6.42086 | -58.23578 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 179f352f-1824-3e80-b86d-c101692f4c4f | -4.85244 | -55.8313 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4871e201-a23c-3204-a0db-7d34a936dc46 | -5.25964 | -55.91087 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| eaaffe16-00f9-3894-bafa-0b3688deca9c | -6.24833 | -55.42709 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40d26f12-346a-313b-9bbd-9f24ccae9bbb | -6.1296 | -57.67559 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cad380bf-e20f-3547-ab39-9277b3152910 | -5.48175 | -57.14421 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99e1f129-4601-3f8e-bab7-0d73256c9218 | -6.78485 | -55.68718 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c4cffa5-d67e-3cd7-8499-92a6e2419a07 | -3.79677 | -59.34725 | 2026-08-31 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27db7867-cb6a-3c6f-848f-cc615c97618c | -5.25497 | -55.91539 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d356276d-6655-38f9-8233-a4daa8201616 | -6.68371 | -58.7499 | 2026-08-31 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 814eee1a-8f68-39c8-9b4e-25ee0e775fce | -5.25869 | -55.89072 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf70a7fe-2aa5-3665-a9b1-655bdce779f3 | -6.92266 | -55.70824 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22e3ca89-63dd-3209-a021-86d6c4ace911 | -3.69135 | -51.99959 | 2026-08-31 05:33:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d597b5b-33de-3fa1-8a9a-a52b975359e0 | -6.91914 | -55.70407 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e2ae331-c412-3caa-bb8e-29f0918c61f5 | -6.79552 | -55.6709 | 2026-08-31 05:33:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be58de3a-6806-3fd8-8c78-45644c42e200 | -5.48111 | -57.14844 | 2026-08-31 05:33:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab59bf06-ac33-3ea5-9b34-46d32720a867 | -4.66264 | -55.92915 | 2026-08-31 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5081c6ca-7a78-30f7-b46b-eacb714a809b | -6.68027 | -58.74939 | 2026-08-31 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7845d620-ce57-3fb0-99e8-7495816152d7 | -3.63428 | -60.55893 | 2026-08-31 05:33:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0967ed5-84b3-3747-a036-aabe4bee9a33 | -3.79343 | -59.34672 | 2026-08-31 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d721b54-667f-3865-a568-29fed9310f8c | -4.157 | -60.69936 | 2026-08-31 05:33:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 190361f1-6ff7-3b34-825a-1707a452eaed | -5.57538 | -60.23146 | 2026-08-31 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 085e1c45-37a9-363b-bbeb-60b3a64828e1 | -4.28956 | -59.95097 | 2026-08-31 05:33:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54d5b88d-b408-332a-b26e-888bd1508c2b | -6.25075 | -53.67288 | 2026-08-31 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ac4d24e-1cb5-3d92-9717-dd84054e1353 | -3.97412 | -55.64555 | 2026-08-31 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bb2d83c-7a26-30cd-917b-b70326041bed | -6.12704 | -57.69194 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4368585b-0f27-3def-9e92-cb41cc0b2b04 | -6.12149 | -57.6946 | 2026-08-31 05:33:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 374163a6-bd78-33ea-a675-6da3e9cad6b2 | -9.48743 | -66.63106 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51753901-d7e9-339f-abfc-c1ad17c60a21 | -10.57217 | -50.36538 | 2026-08-31 05:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bcbd06bd-20aa-30af-a1fa-85fdfb2e280e | -9.05634 | -65.42783 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0df5cfa-266e-3da2-b5cf-726bb67d3d33 | -10.50417 | -59.61972 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8e8c9639-af39-379f-8e08-8b7a3f8ee32e | -8.96595 | -62.39378 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d798819-a9ce-3c25-baf5-26c7c9873d2e | -11.185 | -55.09758 | 2026-08-31 05:36:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 086d6f9b-11db-3fec-8b82-5c93612a1409 | -9.94066 | -60.51751 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea5d496c-287a-3a26-b019-48d0c841dd52 | -9.06176 | -65.41904 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0fc65ce0-bcd5-34fd-96c0-84f4e4b3dc20 | -9.94457 | -60.51448 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 859da93c-2c77-350a-b522-134464b2873d | -7.87394 | -71.79076 | 2026-08-31 05:36:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ca4abd1-3191-3a92-a899-ee0dfe4bf69d | -10.84154 | -48.35836 | 2026-08-31 05:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f2498d0c-89d2-3f5e-8da1-620078b8705a | -10.44375 | -64.46333 | 2026-08-31 05:36:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf4796da-043e-3467-813f-8863499f5e72 | -11.16335 | -50.55886 | 2026-08-31 05:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 02f1f854-408c-37ab-b2f3-349b3abfef4f | -9.24857 | -60.43478 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e81a20b-e0bc-35ab-9b24-7a6b7de4208d | -10.48523 | -59.6052 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96f6f481-6b42-3967-abed-d68dbc259e7f | -9.91195 | -67.02589 | 2026-08-31 05:36:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7b4cef2-a13a-3748-b253-de8a8fe5a178 | -10.81834 | -50.68803 | 2026-08-31 05:36:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ea5551a-efa9-3e35-87c3-acbd2f59e182 | -8.58048 | -66.96743 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 97afe092-e7c6-3183-8d60-b5f61676ae28 | -9.36884 | -60.31128 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43778a80-d5c3-394b-b601-35ffbf64dc83 | -9.01833 | -65.39687 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbdbcedb-daed-34d8-8b6c-e7c8dafee1b7 | -9.00332 | -65.43822 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cad4b906-501d-3f83-90f6-c1644b93328f | -8.68402 | -62.81423 | 2026-08-31 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05f5eda6-7181-3b0f-a865-4dfbcf49657e | -8.70099 | -69.97464 | 2026-08-31 05:36:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 515f6020-b33b-35e3-8413-6722c3806e41 | -10.49098 | -59.61382 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8db2175e-fe40-3c8c-b1b4-7f59d364c526 | -9.939 | -60.52819 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5f84725-5f10-3b44-9f11-3b6a8c2faca3 | -11.16413 | -50.55993 | 2026-08-31 05:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1cb91da2-2973-3236-a6a7-7806ab27d9ea | -10.81456 | -50.66934 | 2026-08-31 05:36:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9fb6573b-e5d2-3528-88ec-adfdaf90b531 | -8.01131 | -70.06492 | 2026-08-31 05:36:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c235634f-c43e-32ca-9fc6-2e0bb02b5eaa | -9.89265 | -60.28631 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3ab11b7-22f4-3ef5-9777-ca2712cf4ecc | -10.84245 | -48.35246 | 2026-08-31 05:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1cc7143c-126e-30fc-9fb2-60daa4f8244e | -9.39874 | -60.5917 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2701e95-0058-325d-becc-5a69541b6beb | -9.1379 | -60.92193 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bf8a50a-b77a-3f1d-ac0d-6b1834c4e75a | -8.79841 | -62.49633 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 097c3406-1183-31dc-bbcf-bd864e572d7a | -8.87146 | -66.7835 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fdbfc186-02ed-3222-be89-82be11c44787 | -9.93842 | -60.50986 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5be45dc0-1716-368b-b631-db71e149cbe2 | -8.22913 | -71.03145 | 2026-08-31 05:36:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e43b2f6-58d0-3a52-a8f5-2d2dd2dd68c3 | -9.21041 | -59.55575 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c18f89e2-cdc0-395a-a062-b8d7f5d4963f | -8.67857 | -62.8474 | 2026-08-31 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56381bd4-63bf-3f92-ba55-1b9694f3ab76 | -8.96654 | -62.3902 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cbace15-8e87-3f01-90ae-81dd14194839 | -9.93676 | -60.52055 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d94f34e2-0a6c-3424-84ec-b8b4ad234eed | -9.85861 | -64.98829 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d696c2d-6452-3776-8154-7275a3e45d51 | -10.73919 | -54.0447 | 2026-08-31 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 50dc7f23-c19f-34ce-8aaa-ffa051295532 | -9.88928 | -60.28578 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcb2d3eb-63f9-35dd-9764-1b0484fe7e73 | -10.47839 | -59.61268 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b29f84b3-8b4e-3697-96ad-e62e164692ff | -11.18438 | -55.10215 | 2026-08-31 05:36:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5aa97355-dc6f-3dc8-8cd4-ada8026935c6 | -9.05794 | -65.41837 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3aced412-ad98-3d86-95f0-fa561e15ffb2 | -10.48009 | -59.61594 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2049a7a-8bc5-344a-80d7-54695adab85f | -11.49756 | -60.5773 | 2026-08-31 05:36:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53b33a04-cc31-3155-b3c6-198a1b06a691 | -10.48353 | -59.61649 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27a0abb2-1885-34bd-a078-8301c6f3df73 | -9.83796 | -64.97572 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03511dcd-9f16-3910-87ad-108f470c2353 | -8.68743 | -62.81479 | 2026-08-31 05:36:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bc8b1c3-e388-3d4f-910c-2ef8bae809c5 | -10.44732 | -64.46394 | 2026-08-31 05:36:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb5ccb3a-805c-324c-9191-7f17de87ab22 | -8.955 | -62.37043 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f01f492d-2042-3b4b-8caa-2df6f3196362 | -8.80458 | -62.50105 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f50e14a9-6081-3805-8093-1b7c7448fab5 | -9.07029 | -60.48641 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a029d99-7c56-3a10-8f91-290cb1550bb5 | -9.94401 | -60.51804 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dfca4082-6518-30aa-b6f9-6188bc32f68f | -8.43456 | -70.41896 | 2026-08-31 05:36:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06d9b7aa-39a7-332b-8121-3e974665edcb | -8.86836 | -66.77896 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 534bfac8-e154-3ccd-bbef-4e814018000a | -10.80363 | -50.65881 | 2026-08-31 05:36:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 888dd25a-ddb5-30cf-962f-7aeedb91ba1f | -10.82435 | -50.6888 | 2026-08-31 05:36:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README62.md)
