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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 174a9fe6-5be3-3089-8d07-76be35c236ed | -6.75083 | -59.11275 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69f0dd12-2a47-3185-8ac0-76b57bfa94d1 | -4.27621 | -56.25906 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35d8b015-65d4-388b-9174-3238562bba94 | -5.69828 | -50.01156 | 2026-09-22 05:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbc926a9-76e3-3acc-b471-d3bfcfaa52be | -6.34532 | -57.88546 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f08fbb64-e3f7-392c-992b-652fd5e5321b | -6.9737 | -55.70374 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64c593de-8fd1-32c6-8f2b-041da7bc367f | -5.91164 | -57.67983 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b78bd514-8405-3a10-bff6-b35f79d0ec77 | -7.34445 | -55.60712 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5980827d-d90d-3b9a-901a-d73b122fce18 | -5.93581 | -59.97467 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 275677f5-947b-3227-811e-c0bef0c46924 | -6.1383 | -59.88407 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46a09169-649b-3bb0-8870-060d39ab3a19 | -3.65765 | -58.21409 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f32c81b3-d5a9-3e1e-86ec-8505c2a87fb8 | -10.91331 | -53.95713 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09be7fd6-6cf9-315a-b3ef-a81223bfac27 | -5.92089 | -55.69865 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6fdcb1a-2160-3be3-9e38-a2d813a40dbd | -5.76175 | -45.08971 | 2026-09-22 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ec597c15-4b93-3cf8-a6d7-f2590422e896 | -11.50598 | -51.50969 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2e6854d-69ed-3e7e-b8b6-10a303817fc0 | -8.08243 | -70.14928 | 2026-09-22 05:23:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9299fa32-ceb7-3601-8229-bea725f19ce4 | -6.16033 | -57.70904 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45204104-57ea-373d-a847-2e381780da15 | -3.64538 | -58.76968 | 2026-09-22 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 050f926d-df21-3c25-9240-09bf14239bc8 | -4.53252 | -54.97627 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9980655d-7bb7-3601-afc9-55c1f6d063f2 | -2.79293 | -59.88676 | 2026-09-22 05:23:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1012b86-bf1c-31ca-988e-132be42fa9ae | -4.22293 | -48.61475 | 2026-09-22 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 839cc5e9-d90f-3db1-81b1-94ba686228bd | -13.52243 | -51.51107 | 2026-09-22 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 50.7 |
| de689727-31c0-39a6-800f-5aaab63cf342 | -3.48606 | -59.57327 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bef30bb-5a78-3990-820d-c9673e3cebde | -6.76846 | -59.62934 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa977f66-9d05-3b39-8e4a-3c054d6bfc22 | -14.76238 | -48.4492 | 2026-09-22 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f92fdae-8717-3594-b58b-ef8887e6ea57 | -2.54505 | -48.15994 | 2026-09-22 05:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6f4ae4a-b8b6-3c7e-8c2e-91464a37a42c | -5.87338 | -52.05836 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 520f04fe-9ed4-3076-ac7c-f63caee75f5d | -9.69825 | -64.91776 | 2026-09-22 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d30fc5d5-99c0-358d-a623-61df49f0909e | -5.9025 | -51.77404 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2f986e9b-489c-3d81-a82c-b2f61134787b | -2.0707 | -56.57862 | 2026-09-22 05:23:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0a9a928a-752a-396b-b2e7-961f156682b6 | -3.92699 | -56.05434 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbe98593-2c59-316a-b398-00b3f93af566 | -3.39266 | -59.52627 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f8ef7611-209e-372b-9585-4c7824d0a271 | -12.40673 | -47.07837 | 2026-09-22 05:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 72ed6ca1-2109-30f7-9f96-b883287fe1e2 | -6.79948 | -59.15808 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab9d7cf0-ea5f-3db1-acef-72dec8c819ed | -3.60937 | -54.04548 | 2026-09-22 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5ea54b2-6b26-393a-af12-328770af1716 | -4.30619 | -49.12235 | 2026-09-22 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2d9d99f3-1b7b-3c96-97ae-564f978f4598 | -9.55621 | -66.04497 | 2026-09-22 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4bca2a6-9ae0-36ef-b928-80ce84ed80da | -3.79666 | -59.70328 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fff4ed63-2d79-3dc0-ac6a-5d986b3dc0f8 | -2.92 | -57.78595 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a656598-7eaa-33d3-8c5d-0f7b7a58c9df | -10.91475 | -53.94728 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3e39519b-b9e4-3875-97ea-fc0e37e4a5ac | -5.85438 | -49.77901 | 2026-09-22 05:23:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d410c266-5ac4-3aff-b559-1abd12989ff0 | -14.58783 | -52.16972 | 2026-09-22 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91ead339-ac31-3f90-914a-b80ef60faf60 | -1.20673 | -54.22458 | 2026-09-22 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1261073f-1923-3a8e-a152-2fd004cdc1e1 | -6.12082 | -59.95149 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c1b39bc-d43d-3f09-89d7-53fe5b8eabf1 | -6.43833 | -59.97165 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 302a4242-d521-3141-8070-d17bb01b0d7f | -7.33063 | -55.60521 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b6ff7af1-3e62-312e-a5d9-e4ea6d6479ec | -3.42598 | -61.32216 | 2026-09-22 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 58371c4a-4a2e-32c1-a025-9263d552c7a3 | -11.9892 | -52.46364 | 2026-09-22 05:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae5736c2-ea39-31a2-ad72-6b013722698c | -6.75421 | -56.32765 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 27561036-d18b-35b7-a7a1-2d8e41a5952d | -3.47184 | -59.63761 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f37bbe03-c0af-3212-aa81-efc185de3fec | -6.3869 | -60.02018 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63f687f7-51bd-3bd6-ac1c-c7bff0511623 | -6.34868 | -57.86452 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb93a33d-de86-3154-be3b-f4347327a382 | -6.84055 | -58.99202 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df767e08-66b3-3c2b-a2c5-48fd06386f7c | -6.30919 | -60.01284 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f687620-b20d-3d08-a985-239ccb9b3caf | 0.04434 | -60.61553 | 2026-09-22 05:23:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5919debd-9762-3acc-8fc9-507249ee14e4 | -4.77759 | -56.15127 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17607eca-2156-35f5-9714-d90b67733ecf | -5.20356 | -56.10866 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22fefa7a-46c4-357b-9c90-41d636ace846 | -6.19362 | -57.77861 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ebed2e05-b5fa-37f2-b4d0-cbc9befc120f | -4.55443 | -54.90282 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 68781f3b-3846-375c-9356-d6c6c73bf8ed | -3.23822 | -53.95543 | 2026-09-22 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dd90950e-b583-3674-bade-af31b155d6ca | -12.1411 | -47.38858 | 2026-09-22 05:23:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 72da4665-7150-30b5-a00d-157336d6a895 | -3.05463 | -54.41613 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1968ee1-eea8-3310-8062-01273dc22e6f | -2.78546 | -59.95554 | 2026-09-22 05:23:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 336b7408-d44b-380e-8350-5897155f3bec | -6.39397 | -60.02143 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5c1c906c-6fb8-311c-bae3-810bb90e8f21 | -11.25778 | -54.14126 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d2a80e1-c79d-384e-934e-30901169142c | -3.28706 | -52.59716 | 2026-09-22 05:23:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7faaf38d-7485-3c30-b193-08c675206844 | -1.29572 | -54.21969 | 2026-09-22 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eec7cd9e-8e9c-3978-855b-98b542bc931a | -12.9283 | -50.93365 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2a4de550-55e3-35c1-bd00-fd7bddc42127 | -6.09609 | -57.62402 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2345df97-9bc8-3441-bdbc-a6278f531bbd | -3.52077 | -56.90653 | 2026-09-22 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1773f6f6-d86a-38c5-8394-ad07b8157141 | -1.71366 | -54.88512 | 2026-09-22 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d71f67a0-b0ec-366c-bf41-547bfde98f50 | -6.33313 | -60.01546 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1824da3-dd14-37c9-be7e-ee1a0b9a69a8 | -8.32612 | -50.84241 | 2026-09-22 05:23:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c95d2db-34da-3ace-a11f-75a8a782fd28 | -5.86455 | -60.1619 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c612b15-69e8-3206-b4a3-da65ff25e931 | -6.70459 | -59.46372 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9d2bbde-d078-36db-811d-afc9472d74aa | -3.4789 | -59.57213 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e708e39-f9b8-38f4-a0be-0ee790092abe | -3.608 | -60.57072 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7c27520e-2cc0-319c-9fd8-ddd95f00c2eb | -10.45241 | -61.3156 | 2026-09-22 05:23:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4508cd13-1088-3cc4-9c3f-9982dc2667e4 | -6.70618 | -59.00038 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6cc7cb7e-7536-36cf-a4f1-3ef8b66ad330 | -14.67389 | -45.67716 | 2026-09-22 05:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6df4499d-e519-3d06-96a2-a56db0eb6f40 | -2.85848 | -57.8166 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6680bea1-5cd8-3591-ad86-305ce7812d75 | -6.19695 | -57.77913 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7448d6f1-dcbb-3ca4-857b-fc6f245ca1d7 | -5.97567 | -57.78696 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba1c9238-a331-3706-bac9-2bf79429476e | -7.58479 | -57.68639 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba894cfa-d2da-3fc5-ab05-9b482942da2a | -3.38824 | -59.42807 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3eee314-5a8e-3371-a2ca-53d872f5c343 | -4.50445 | -56.07591 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb1a78a5-52f3-39ca-b127-371bcbf9f9fd | -5.42943 | -60.16843 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dda2bc6b-db48-324a-9c14-3eba0e8c548c | -3.48858 | -59.6028 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8edcdc94-da56-371f-a82e-e3468867e34a | -6.27036 | -53.11906 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91c7b945-1c8f-3af2-a58d-ec05218f9be2 | -8.78407 | -44.30592 | 2026-09-22 05:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9509c80f-e025-3374-af1b-1456ca1f0894 | -6.05386 | -57.82438 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44c62ec5-68ab-3d69-ad2e-727decad062e | -7.87924 | -54.73149 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 523ea8b6-96b8-341a-a240-07b5734cfd8a | -6.69654 | -59.95912 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4656c38b-dcd6-3d02-8a98-6861feef5b4c | -2.91699 | -54.18897 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb273a3a-3664-3ce1-98bd-a1bb5e5e6e8e | -4.50659 | -59.55635 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4f40064-7b7d-3b9b-9d40-f11767d5f90b | -13.91098 | -48.56556 | 2026-09-22 05:23:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d7f8904-5ced-360b-9547-a36acc869fd5 | -9.36232 | -65.76039 | 2026-09-22 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4ab32f8-1e2d-3f5f-9bc2-6d78681c72fe | -3.54954 | -55.44247 | 2026-09-22 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 196cd787-c5c2-3d62-bcde-f002ae47ce62 | -7.55005 | -61.31596 | 2026-09-22 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3e58eb1-73d7-3e24-9853-e4f55048672c | -21.45884 | -48.67557 | 2026-09-22 05:25:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a84a5024-9d70-3095-a8f2-df20b4635e20 | -7.5493 | -61.32038 | 2026-09-22 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README99.md)
