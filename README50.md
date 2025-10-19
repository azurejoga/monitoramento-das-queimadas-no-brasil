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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ea9cc3f-6ccd-3985-9596-14d01de9dc54 | -4.97065 | -56.27481 | 2025-10-19 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eae74a9d-655a-3b46-aaf2-767830b1eea1 | -7.04762 | -41.82815 | 2025-10-19 04:32:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a36387f7-928d-39e8-a11f-627cdaebc901 | -6.00521 | -44.18085 | 2025-10-19 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f296d3e-4897-3ec6-a684-5e842b3d1c5b | -7.35474 | -43.85066 | 2025-10-19 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ad76a228-a4cd-332e-aed7-8a3a40ec13f6 | -4.76794 | -49.4651 | 2025-10-19 04:32:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fbac792-64ac-3f0c-a9f7-13416ed177e6 | -9.53358 | -47.90855 | 2025-10-19 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b502cc7-49ae-3e13-8505-62d0000ce448 | -11.61259 | -44.05827 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e7c38484-4b93-30ed-a790-15f30d7a2179 | -10.98207 | -47.93978 | 2025-10-19 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7eeed57-ea4f-30a9-8f8a-2775158b5e06 | -6.79249 | -46.47328 | 2025-10-19 04:32:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38d6db69-c239-31ad-9731-b50d604ca126 | -9.76604 | -47.87693 | 2025-10-19 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36976276-9d92-37a2-88c2-71134d5c7351 | -7.95434 | -48.12408 | 2025-10-19 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f35ccbf1-1b45-3e2a-82dd-7a81ce462d8b | -9.13229 | -43.24511 | 2025-10-19 04:32:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 209330a7-c281-36c9-9960-d10d31042eb9 | -6.52626 | -60.03667 | 2025-10-19 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e41ce684-11eb-3afb-bec8-e980c9e150bf | -7.23277 | -46.04256 | 2025-10-19 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| afcaae96-306c-373a-b5af-38f0346034b8 | -8.23535 | -43.31661 | 2025-10-19 04:32:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8785ce54-a225-370f-9177-7bd3e43f7671 | -8.24844 | -44.00321 | 2025-10-19 04:32:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59aa59a0-8560-3ba1-af68-763a90abcadc | -10.56071 | -43.38747 | 2025-10-19 04:32:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 258e95ff-3f81-3696-90f2-ebb62f79e6bc | -9.22562 | -46.06211 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 520ab1e9-6b5d-360f-a67a-a0501d16c45c | -5.0858 | -47.18381 | 2025-10-19 04:32:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1b8d7959-0f88-3b01-9c4d-22106caa7a78 | -5.1221 | -49.46223 | 2025-10-19 04:32:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca474745-b113-3eff-b00d-0fd78e48caca | -4.90101 | -48.56469 | 2025-10-19 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce1d28dc-b650-326e-9313-0ad9c96d4caf | -5.68259 | -46.45464 | 2025-10-19 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7cdde96-3ea5-350f-896f-53eb9992f3d0 | -10.03429 | -59.35979 | 2025-10-19 04:32:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4e8c3b8-4eed-32be-8a13-5dd4c3cb7506 | -8.42454 | -44.14373 | 2025-10-19 04:32:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff32276e-72a9-318c-b4f1-2ad47f469efb | -5.19364 | -46.17327 | 2025-10-19 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d088750e-25ab-3452-9c7c-ff0e8432e80c | -9.90934 | -47.65479 | 2025-10-19 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c83e8b9b-986f-3782-bcd0-71c15afdaf03 | -5.1016 | -47.79406 | 2025-10-19 04:32:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 25.4 |
| c7ba6203-5e4b-3423-b930-a6ac21e25594 | -8.36017 | -46.2038 | 2025-10-19 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 411acab9-d71e-34fd-8642-fb60fbdc796a | -5.63489 | -44.8083 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 95643122-dab8-3923-bdf4-6dc9d7d91699 | -6.81576 | -48.29776 | 2025-10-19 04:32:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97819a9a-438c-33d5-96e6-6c38f93ec525 | -10.88968 | -47.45718 | 2025-10-19 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc59e167-aaa1-3507-96a7-44fb30d78e1b | -9.61907 | -49.02353 | 2025-10-19 04:32:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6dbd3944-b1da-36f9-b42c-f68bd9ddacfb | -8.34847 | -46.21051 | 2025-10-19 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3e4714fa-8886-3d9d-8478-fb6c8a70ebb4 | -6.86678 | -47.99673 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35c4bf6f-ff3b-30fc-9730-e506b82a22f2 | -5.7847 | -49.83718 | 2025-10-19 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72335423-df02-35f5-a71d-e903a5057aff | -7.93276 | -50.00097 | 2025-10-19 04:32:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 173df074-dfff-308e-93cc-1ffa4b191db5 | -5.40667 | -44.06029 | 2025-10-19 04:32:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 377b5101-d54f-390e-9c18-e06a57e40e94 | -4.83267 | -49.34425 | 2025-10-19 04:32:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 122a5a25-d4bb-343b-922d-96174a651b56 | -10.12686 | -44.52702 | 2025-10-19 04:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e835b34a-b280-3d66-9f01-e1ca808c7790 | -5.353 | -47.21192 | 2025-10-19 04:32:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 670d93d6-698d-3335-aae2-654511db4f5e | -5.08573 | -47.93696 | 2025-10-19 04:32:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9ac6264-3584-35e6-866b-3d9acd7bc8b2 | -7.41718 | -40.07432 | 2025-10-19 04:32:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4149d660-1496-3ded-a977-40fffe9f8f5c | -9.94261 | -47.66003 | 2025-10-19 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b865ea7-dcde-318e-95a5-256aed740800 | -10.3358 | -47.77251 | 2025-10-19 04:32:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e54ee1f4-d633-309e-9a3f-cfce0501993c | -6.41798 | -43.91406 | 2025-10-19 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ed44c270-d0dc-33dd-b337-825d93cc941f | -6.08517 | -46.46274 | 2025-10-19 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63726f85-3193-3cd2-ad12-691b19188682 | -11.03827 | -44.66069 | 2025-10-19 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54a54f47-e6cd-39bd-8370-3f682e69ce81 | -10.5783 | -41.50351 | 2025-10-19 04:32:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f03636d3-5679-3436-a391-124a5c050d74 | -7.15855 | -46.41228 | 2025-10-19 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a7bacac-a665-3a18-acc0-6c3d7b02e0e5 | -7.57445 | -47.05864 | 2025-10-19 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d681ee97-0195-3bb5-b9a8-4bb6b8ead7e4 | -7.12105 | -46.15399 | 2025-10-19 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c66a964-de0c-33fb-b591-268e0f26c0d0 | -4.96658 | -56.26722 | 2025-10-19 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6b570d90-8ec5-3044-a78f-b1a6635db2b5 | -7.1987 | -42.20714 | 2025-10-19 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0a045a4c-4066-3069-aced-5ab7f91c712f | -11.11041 | -47.65732 | 2025-10-19 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64aeedec-e979-3544-b220-011b6b904466 | -11.64855 | -44.08978 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7afd7b60-75e4-3fc6-a2c8-0ed962a66338 | -6.45662 | -46.53797 | 2025-10-19 04:32:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3ad9886b-2708-39d9-b519-d560b1f38667 | -5.56145 | -46.38179 | 2025-10-19 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 226f8e80-2179-33c7-abc1-1f143365c4e5 | -5.36791 | -44.94336 | 2025-10-19 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df1ca69c-a499-3f04-a1e6-efb320aae6ef | -10.05797 | -48.20366 | 2025-10-19 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62675bf5-7b6f-3fd1-a7d9-385cbecd278f | -6.09945 | -44.02582 | 2025-10-19 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b3bf209-7aff-3723-a84a-f2bb88163025 | -5.70825 | -46.50517 | 2025-10-19 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a4e150a-8312-3879-8e42-b3ee37e335ec | -8.34709 | -46.22092 | 2025-10-19 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8de58495-6681-3648-a9df-81d684a98344 | -7.31245 | -42.47009 | 2025-10-19 04:32:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 11937b33-69e6-3868-b888-9518e4434c05 | -5.908 | -44.25473 | 2025-10-19 04:32:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ffa935d-59d6-3d42-954b-ef39fa230606 | -5.64167 | -46.58513 | 2025-10-19 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 452844cb-c658-3d0d-b5ec-e47019d32d41 | -6.14309 | -49.8925 | 2025-10-19 04:32:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ba81e08-8fc2-3217-ba82-fe2cf1202193 | -9.6658 | -44.55775 | 2025-10-19 04:32:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d98072ad-5977-3ea7-8557-805e56e42b2b | -8.73182 | -48.12711 | 2025-10-19 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a18c5af-ea2d-30a2-ba54-32c403085449 | -10.60933 | -49.52486 | 2025-10-19 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ccb9c7d-9c54-3d0a-880c-03981bc1d9d0 | -8.24217 | -43.9907 | 2025-10-19 04:32:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dcb7654f-50b3-3f98-a745-f9718a6c3694 | -9.22244 | -61.83713 | 2025-10-19 04:32:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b32f66bd-1191-348c-9c68-2c90cf0cf6c0 | -8.65073 | -47.07764 | 2025-10-19 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39bdfc16-738d-3fab-957f-a2fd21b2ec6f | -10.16022 | -42.20819 | 2025-10-19 04:32:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8ac6e8e5-c99f-3af1-adda-9366f9503bc9 | -5.71159 | -46.50568 | 2025-10-19 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6789c5f0-7b69-3095-b1c6-dd01476aa932 | -10.63522 | -48.02974 | 2025-10-19 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d63b9b2-ec0d-3573-8459-ca4510220044 | -9.92543 | -47.66091 | 2025-10-19 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 117b09ff-bdfc-3bc6-98d6-0cc5208722f8 | -5.30219 | -45.59359 | 2025-10-19 04:32:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3730ca1-a768-339d-ad0b-51cbcf98b520 | -5.77496 | -42.72531 | 2025-10-19 04:32:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ddd35c72-1f32-3096-b299-3a1d2cde7269 | -9.26475 | -44.34279 | 2025-10-19 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d831862-bc11-3818-84a6-ce281aafe9b5 | -4.96602 | -56.27043 | 2025-10-19 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7b7143f1-5e9e-325f-bd17-401a55d62acc | -7.41413 | -40.0808 | 2025-10-19 04:32:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e09245ad-9004-39a7-a2b6-55193579abc6 | -11.6527 | -47.32184 | 2025-10-19 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2859dae-45c3-3993-a11b-de8583d7fa17 | -10.89074 | -46.07652 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 570af745-4494-3322-a9dd-52d424a753d2 | -6.86161 | -46.29297 | 2025-10-19 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4b18adc-5742-304e-b1e0-67c911ecd517 | -5.67171 | -47.99079 | 2025-10-19 04:32:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4e680a5-15d0-3b4f-990d-9749b78dbfab | -5.33922 | -46.05978 | 2025-10-19 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b8c2cfd-5e1f-3e6c-8514-a3361a39e82f | -8.24915 | -43.99853 | 2025-10-19 04:32:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2a4de794-bbdf-32db-982f-ead1c6cbe628 | -5.10436 | -47.79804 | 2025-10-19 04:32:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 310a3902-3277-324c-874b-b62339dfaa27 | -6.05623 | -49.39165 | 2025-10-19 04:32:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6bcc34b-82c1-3103-a014-d6ab7bd233d4 | -5.047 | -49.64871 | 2025-10-19 04:32:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3648d8c-6e06-3443-ac86-a64e622a6ca5 | -9.98174 | -47.05083 | 2025-10-19 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ec0035a-1a8c-35aa-80a0-9dc2b642509c | -7.18951 | -42.1822 | 2025-10-19 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5c64222e-5629-3b31-9ac3-0c655d2eff70 | -8.54252 | -45.4924 | 2025-10-19 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd16585c-fadb-3c73-bd31-494746a9d853 | -7.9493 | -44.09105 | 2025-10-19 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 40c9bab0-82a7-35b0-bc24-5cbb9eae9191 | -8.34719 | -49.54036 | 2025-10-19 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc87aafb-4a59-373c-b54c-58f3fb715611 | -8.24597 | -43.99124 | 2025-10-19 04:32:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 920b0b8e-ae00-31e2-af4f-f46a578c2742 | -5.3041 | -45.07972 | 2025-10-19 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7c7e72d2-0cd7-3e5f-8aaf-618611bb75ab | -10.78116 | -40.31322 | 2025-10-19 04:32:00 | NOAA-20 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0dead244-9ac0-369a-b48a-1cd8537e9e55 | -5.71126 | -43.82547 | 2025-10-19 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d67c7ff1-6cf4-3e31-8900-113a34b35006 | -9.9268 | -47.12745 | 2025-10-19 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README51.md)
