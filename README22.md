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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b33ba51e-61db-3dc0-8396-fa600b2aee14 | -7.41436 | -45.19822 | 2025-10-02 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1632805a-80d8-3d9c-8283-54be6e672bff | -6.70279 | -42.81218 | 2025-10-02 04:02:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| ce16d474-cefa-3a08-b41d-b1cacf2a182d | -10.65382 | -48.50415 | 2025-10-02 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fcfe5d7-3b95-3c3a-a1a3-014f350b9a7f | -11.46989 | -45.11646 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebf50d09-234e-310a-a241-aaa0592066ed | -6.97184 | -45.32379 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a3204e7-d7a9-3530-ad88-b5a680d8dce1 | -11.45321 | -44.9644 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d82ade92-e5a8-303a-9693-c3e2f6dd06a1 | -10.25525 | -50.30883 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da015f94-6fa6-3d09-84f3-375cd7aa6032 | -11.94128 | -43.91367 | 2025-10-02 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfeaa356-7bbe-32fc-ba7e-6ecbcbfa1659 | -11.71455 | -44.46344 | 2025-10-02 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6756302a-7aea-362f-a770-23d4afe15e3b | -11.57367 | -47.02274 | 2025-10-02 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f86173ed-32b6-322f-b43f-0152a4ecfec9 | -11.01238 | -46.57887 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 93718607-21e3-3d58-9bf3-fdb45e8cee97 | -11.1955 | -47.1929 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6f6d53fa-348d-3fde-a28c-7f875d0ceb3f | -10.69856 | -48.57992 | 2025-10-02 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6233044-fff9-31a0-8a2b-24be4fa19a0b | -6.48456 | -44.28234 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb595588-6669-31e3-9b6d-b20d37a164c4 | -6.69138 | -48.70421 | 2025-10-02 04:02:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4ae534ea-8b23-3ad3-95ca-08f54bba6a5e | -6.26828 | -43.8929 | 2025-10-02 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 677d06e3-4399-361a-b7be-858e16a701b8 | -10.34651 | -43.73777 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96963fe2-b2dc-3d08-ba4d-db478c816312 | -12.01736 | -46.63228 | 2025-10-02 04:02:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98cc92bb-877d-35e3-89df-aec994f17eda | -9.41269 | -47.58579 | 2025-10-02 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de95cac0-c578-3d4e-beab-713e49bedec0 | -10.8399 | -45.39253 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 81e7728a-45e5-3325-8c90-1db70f20db7f | -7.77589 | -42.53709 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 3eaeb71b-d97a-3442-b843-3183d9f2f548 | -5.91902 | -44.86214 | 2025-10-02 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aae6d7fa-caa9-3b8a-b106-7fd33b9724a6 | -11.85503 | -48.04445 | 2025-10-02 04:02:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dac66c94-99d0-319a-9623-24ca3ef68b95 | -10.25737 | -50.32707 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3744b782-0a28-3dc8-be0d-6d6d976f8ab0 | -11.651 | -45.31295 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83cb9969-5cb4-3c55-83e6-ed33bb67da41 | -11.68036 | -44.28121 | 2025-10-02 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f94f07ee-967d-3304-b672-5ab30521108b | -10.85204 | -46.66504 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3933dd0-781a-3feb-9e9e-9d5a1ccf6884 | -11.46274 | -45.02145 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2d5607f7-e55f-302e-a952-c7bff051d757 | -10.68689 | -48.56337 | 2025-10-02 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 413d60f3-9096-3eb4-b48a-f6ec836c6972 | -11.16067 | -47.19009 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0ee171bb-fee4-39dd-b73a-9c513aaf1e52 | -11.98418 | -46.65344 | 2025-10-02 04:02:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f53dfc0b-320c-344a-a54e-b9ec7d3af9ac | -11.8365 | -45.00516 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17967e9c-fb0f-340f-836c-ca7bf37b0436 | -10.25054 | -50.30438 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 975e9ca6-8a03-3360-95f0-9769a0a62edf | -9.79449 | -45.94967 | 2025-10-02 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dea5c4c9-27c6-3e49-a557-dcf808eec3b6 | -9.40997 | -47.32721 | 2025-10-02 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d11ff83-c3d3-3c81-ae4b-19771b72c239 | -12.80094 | -46.86824 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 826f0cd2-82ee-3d39-99ee-eceecdf03ed3 | -11.80219 | -44.99142 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e48ea14a-bbfe-3d77-99b3-7493903b9714 | -10.66516 | -48.52197 | 2025-10-02 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab09e216-84ce-3003-bb51-2c03d350482a | -11.52331 | -43.54614 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01b3a328-07a2-3406-be1a-9d93bad0b36d | -10.35071 | -43.73433 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 83724717-ee68-3c91-b9b5-f670c38475d4 | -10.99506 | -46.59068 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 9e1dda96-9505-3a52-971d-50ab77d38532 | -8.56757 | -48.64418 | 2025-10-02 04:02:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 447d5252-91ff-35df-b3b6-b76068e8299b | -9.93231 | -43.73915 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 159.4 |
| 69af1c22-ed0f-390e-8ad8-6bd1391e995e | -7.60125 | -45.40854 | 2025-10-02 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e243b4d4-c6e8-30be-8b2b-9002ed5bca91 | -10.48698 | -49.36934 | 2025-10-02 04:02:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 243d8cd5-3947-3546-a62a-2b3be4baa85e | -12.81597 | -47.02003 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30641ad4-9caa-3bf7-8b7f-f66453479302 | -12.81735 | -47.01226 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f04403dd-3206-34e4-a58a-fcf19cd4e2a7 | -12.22731 | -43.76134 | 2025-10-02 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7771d871-21d2-36cb-b4f6-b3b2c9793a73 | -13.01279 | -45.2067 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 95a4ce6e-75e2-35ab-bd15-1cbaaae0ba00 | -10.44311 | -48.08401 | 2025-10-02 04:02:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0fdd8f89-aa2b-3ea4-876a-7cd0937d1150 | -13.4783 | -43.50891 | 2025-10-02 04:02:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cc58fe5-44d7-3f5f-a152-f644a048ab86 | -8.82063 | -46.68424 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ada6b76-c2e9-3a3e-b55e-e340faa55c5f | -11.84351 | -44.9643 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5c0264cf-9653-3861-842b-6b14d8a2c948 | -12.19751 | -47.80764 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb63a1e5-25f5-3a41-87bf-3ac6af0e315e | -12.8653 | -46.93292 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99c531e7-9d48-31a4-ad25-7a39518a90e1 | -10.86824 | -47.8179 | 2025-10-02 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f8efeab0-fcb1-3902-92ab-25d0af23d99d | -9.7964 | -45.94276 | 2025-10-02 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 801c420a-c03d-36c3-a309-778bedf8bd9c | -9.94785 | -43.66638 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de7365e8-a949-3b04-88d3-18bef360c996 | -11.82753 | -48.06797 | 2025-10-02 04:02:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 165567d2-f704-38a7-a3bb-f43a3664dc59 | -11.82134 | -47.68177 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 097b01a0-eb91-34eb-8231-642437d007d6 | -8.70539 | -47.86494 | 2025-10-02 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7544506-946c-3ba2-8c8e-6d1eccb1836f | -11.81786 | -45.02479 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f501c8f5-c306-361d-b3ab-56f276b6b378 | -6.50448 | -44.29769 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c46a5baa-bef3-3dcb-aacb-b9af303ae8b0 | -12.89714 | -46.91572 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b4c554e8-0b17-3c95-be86-5e0caa00cee2 | -10.27217 | -50.33701 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab4f1b8c-ee40-3ef0-bdde-ae20c968e010 | -9.91532 | -43.66513 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9f67809-0499-3005-b6c2-196c82ec2e4d | -6.41032 | -42.80314 | 2025-10-02 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 079115b0-c00a-3caa-8d4f-cf1bbca1c1fa | -7.45256 | -46.47434 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c954d77-ef28-3b2b-b5f4-fb6a7170dff1 | -11.17898 | -47.26194 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 084bfe21-94cb-372c-b021-4b1f8e0df58a | -7.55415 | -42.64726 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cd5f56f4-80eb-3cb9-9513-bf91c7ce7ea1 | -7.557 | -42.65167 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b263c25e-007f-3351-aa33-dd0fc38a8dc0 | -8.443 | -41.48618 | 2025-10-02 04:02:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c1c07bab-1378-3cf4-8c73-6ea2e971bdc1 | -7.48584 | -43.04345 | 2025-10-02 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0a5fc162-56dd-3758-9c17-be4e664da13a | -8.82438 | -44.79529 | 2025-10-02 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cf28f2b-d8d9-3af9-85bf-d969397c21e2 | -5.89994 | -42.52169 | 2025-10-02 04:02:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f272d8fd-5bba-38fe-b848-059dc9dbf066 | -9.43127 | -47.36326 | 2025-10-02 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a70cddb-c7c3-3776-b414-0420c117632a | -9.33075 | -45.92155 | 2025-10-02 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3265868-bb1e-3377-b3d0-baa0013d300f | -8.56956 | -48.64158 | 2025-10-02 04:02:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 851170c5-110a-3882-aad9-806b0ca76c3c | -11.85387 | -48.02545 | 2025-10-02 04:02:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 769ab89d-56ab-3512-9b6e-a8c3840b21dc | -11.80065 | -45.00064 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3025a1ea-86ec-3eb6-8634-4da0a4d02221 | -5.78938 | -45.7533 | 2025-10-02 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81cd62f2-9310-37f7-96bc-487bf79aeda7 | -12.7782 | -44.90717 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91497ae6-1896-3008-99d0-1cb43944c1f2 | -6.31375 | -43.43344 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7878f882-6522-3d7d-8c98-6101d2fa1cf8 | -11.42654 | -43.49403 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d3f5c7b-5c7a-3cb8-b603-40d2266f7643 | -12.68301 | -46.91697 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6f236960-3fd4-371f-a144-c1133f0b2bfb | -6.96594 | -45.33387 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8e0c009f-3112-31cb-9dba-ef526f44be22 | -11.87278 | -45.01587 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 27af3b4f-b23f-3bf1-938c-8cd2cb42f5bd | -12.6433 | -46.9566 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ae449a4e-1aa4-3a1e-b9f9-034f1368bbba | -12.89046 | -46.9339 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e293f57b-8cd4-32c8-ad7e-a832de94f478 | -5.84129 | -42.79878 | 2025-10-02 04:02:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b627dc9c-de29-3e1e-a702-2b4b9be7fc53 | -6.45076 | -43.44528 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e2c5f1f-f0b9-380d-b4b9-04125ce28937 | -11.26977 | -47.82413 | 2025-10-02 04:02:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 15d1edb8-af9d-31b2-8a3a-0e52beecc9f4 | -11.80142 | -44.99602 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d9449820-569b-3157-a126-412b4f3759a3 | -10.60336 | -49.63494 | 2025-10-02 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 074b48c0-51df-3f0d-b7cf-53d2c486746f | -11.48352 | -44.99945 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cec41025-5291-3e76-8ca1-9dcd96955b1d | -7.03287 | -44.46289 | 2025-10-02 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b7da0b87-74a3-3721-8cf3-9f24af5246ae | -10.2273 | -43.0272 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f11dfab3-9bd1-3e8f-80bb-c80160565280 | -11.79708 | -44.97651 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ab907ef8-922e-380c-8612-eccdb501535b | -7.56975 | -42.39931 | 2025-10-02 04:02:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2d91ed5b-4c4a-3c77-b508-6e0c93942d92 | -13.0157 | -45.21182 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README23.md)
