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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c7788fb-57cd-3adb-9db7-f9f133177757 | -9.01435 | -70.9003 | 2026-09-04 06:20:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 258d168d-3c2d-3f4c-b131-dc1f1ca0a532 | -9.74286 | -69.07087 | 2026-09-04 06:20:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95b738ba-79e3-3d5f-a59e-0586f6adc626 | -8.87154 | -68.612 | 2026-09-04 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a56bb19-f9c1-3bad-b2d0-3c5580b72a9c | -8.80609 | -69.02641 | 2026-09-04 06:20:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 354002ee-0738-3956-a570-e218e1b34258 | -8.60679 | -67.18863 | 2026-09-04 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| dcf78fd0-b5c9-3574-8980-d3437d65d793 | -9.64992 | -68.61272 | 2026-09-04 06:20:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 44e6b7ab-948d-3044-92cc-3abea13d465b | -9.03495 | -65.7348 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45c69a32-8cfe-3bd5-b87a-2fc0da974632 | -9.03956 | -65.73853 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c455455-a149-38de-b7ec-8305d7f74f5b | -6.67179 | -59.96791 | 2026-09-04 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1f29558c-3982-3a5b-bfaa-702e4e6ea877 | -7.02257 | -71.62511 | 2026-09-04 06:20:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 14bfe0ca-e8b6-367e-9d1c-f6d95682f138 | -7.87751 | -71.75657 | 2026-09-04 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d72417f-c59f-38f0-8493-5e22d1fe5f4f | -9.04843 | -65.74854 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7ed3ca4-763c-3dbc-b6e9-463e44d304c6 | -8.2042 | -62.80189 | 2026-09-04 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5452ce02-88a2-39b9-827f-3d923e4b4442 | -9.17675 | -68.2661 | 2026-09-04 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26d3eeb9-76fc-3fcc-97cc-f27800b75fa2 | -7.7842 | -63.38986 | 2026-09-04 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b52bfbb4-77b7-3643-8e8d-a3e3d19243a2 | -9.03455 | -65.73772 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0273482c-0f74-303b-a98e-3cb95187b4f0 | -6.15548 | -59.94539 | 2026-09-04 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e087e4df-046d-3336-b323-fb8be9525396 | -8.73391 | -69.59052 | 2026-09-04 06:20:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e30ed1a-c66b-31e5-b222-ae808d8e4215 | -8.20479 | -62.79735 | 2026-09-04 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47e98339-ade2-36c5-b429-70e852919b08 | -9.57766 | -64.29564 | 2026-09-04 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 657ce8c9-2743-325b-9e6f-f6dc4a8227dd | -7.55415 | -61.33739 | 2026-09-04 06:20:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 86e70a99-dcad-3e38-8f8f-24fefa838f4d | -6.14932 | -59.93814 | 2026-09-04 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8390e7e6-0bd2-3017-9564-b32f145387a3 | -10.28816 | -68.8552 | 2026-09-04 06:20:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b44e039-ca23-3b03-b73b-af5b343213d7 | -7.55925 | -61.34937 | 2026-09-04 06:20:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5dd41a21-32b3-3654-b52e-ad227dea0ae6 | -6.70093 | -62.86729 | 2026-09-04 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2892ae74-c201-35da-8092-d487e32f42a1 | -8.16427 | -62.77765 | 2026-09-04 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a10be851-75ad-3105-ba2c-bdf7b01f935b | -8.59839 | -67.18276 | 2026-09-04 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 499c3a91-809c-3c75-ada1-e162b5a407d2 | -7.39112 | -72.80057 | 2026-09-04 06:20:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 290d4650-dc32-30a0-8bbc-3facd5e60bd6 | -8.66877 | -66.94997 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f206c547-3b56-38cb-9ba6-1744327d2d0f | -8.7105 | -62.94585 | 2026-09-04 06:20:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f664961-63c3-386e-9ae2-fef0bce27d13 | -7.78841 | -66.95483 | 2026-09-04 06:20:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4727e7f8-dfef-3d07-98c2-40b0ce330f87 | -7.8758 | -71.76782 | 2026-09-04 06:20:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1d0dcf1-d669-3980-be39-3e9092f8116a | -6.69033 | -59.99 | 2026-09-04 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 681d92e3-b931-3dff-9af0-b9944220de46 | -8.59904 | -67.17817 | 2026-09-04 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 557ad748-ec9e-3f3a-84d1-ff5e3c88c2ae | -8.60291 | -67.18341 | 2026-09-04 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 2e81bb37-3596-30bc-aa3e-c78c0dfebf2a | -7.55851 | -61.35499 | 2026-09-04 06:20:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| acd0b72e-0790-3cb7-b841-3566dd04e7fb | -9.24747 | -68.22166 | 2026-09-04 06:20:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96b59ebd-a9a3-3c73-ba28-435684ccd56b | -6.69206 | -59.97699 | 2026-09-04 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a3432614-527e-366c-ae8d-0519e189c7e4 | -8.79798 | -62.88811 | 2026-09-04 06:20:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9351d0c-c27d-37b3-93ad-947e2bda30c0 | -10.54112 | -69.0278 | 2026-09-04 06:22:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecce8537-1e5f-302b-83fc-372a3a5f60ba | -6.6882 | -59.9628 | 2026-09-04 06:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 1ae347b2-bd80-3e68-94bb-0f04ff9e3ec2 | -8.5916 | -67.1788 | 2026-09-04 06:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| cc5073e5-3b32-36fd-9fcc-7d6867808c34 | -8.6101 | -67.1783 | 2026-09-04 06:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 319c2d3d-8b2f-3c15-af34-7bef4d1ce394 | -8.5048 | -54.6606 | 2026-09-04 06:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| d5927884-0106-3cd0-9e2a-1a175a5c1e7e | -8.505 | -54.6404 | 2026-09-04 06:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| f57adf03-b179-3dbc-a9eb-573207dcb13d | -6.6697 | -59.9635 | 2026-09-04 06:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 7986f8d5-0cef-3065-89b0-574439f2ea87 | -6.6696 | -59.9827 | 2026-09-04 06:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| f4beacf2-ade8-3a34-85ca-0b51337cc080 | -6.6881 | -59.982 | 2026-09-04 06:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 100.0 |
| a9b538d2-e8e7-3f15-96ce-397101f20c9b | -6.6881 | -59.982 | 2026-09-04 06:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 2dd9d545-29a5-3fb5-879b-9f76e3c3ef18 | -6.6697 | -59.9635 | 2026-09-04 06:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 456480a6-be31-3849-a70f-6e692a4ed0e3 | -8.6101 | -67.1783 | 2026-09-04 06:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 1fc48d2d-5747-3f20-b852-75befc2c9dcc | -8.1126 | -54.7871 | 2026-09-04 06:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 1169a231-d57f-3dd7-840a-b3e0dda5ebb3 | -6.6882 | -59.9628 | 2026-09-04 06:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 6f4c2fe4-4585-367c-b5b8-055855a049b0 | -7.5476 | -61.3437 | 2026-09-04 06:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 36.8 |
| badce840-cc6b-35bc-9f94-87d47db98444 | -6.6696 | -59.9827 | 2026-09-04 06:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.2 |
| f599d43c-5379-310b-9688-0467fbf466f7 | -8.5916 | -67.1788 | 2026-09-04 06:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 92ae2074-e742-3dd7-a064-3f07f8d7b398 | -10.6358 | -50.3943 | 2026-09-04 06:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 854c4fd5-9212-3762-846a-09d9a7868b16 | -6.6881 | -59.982 | 2026-09-04 06:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 95.0 |
| efc225f6-b02f-332c-9fc4-a7b78df9b15c | -8.6101 | -67.1783 | 2026-09-04 06:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 9db0e1de-9373-39ea-b0f9-bba483c0f2bd | -6.6882 | -59.9628 | 2026-09-04 06:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 5579117c-5df6-31d7-9d7d-4d305c9c7bc2 | -6.7065 | -59.9813 | 2026-09-04 06:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 8400a8ae-7e96-3822-9892-9bb95638a3e8 | -6.6697 | -59.9635 | 2026-09-04 06:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 786e8b43-7767-34ef-824d-50cad766a5d7 | -8.5048 | -54.6606 | 2026-09-04 06:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 1f403a80-c8c7-3214-8e07-b1223d56fc64 | -8.505 | -54.6404 | 2026-09-04 06:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 89fe4098-5a45-3571-8946-c7c4846e0640 | -6.6696 | -59.9827 | 2026-09-04 07:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 04b21cf1-f8c3-3912-a286-d2e9c61af020 | -6.6697 | -59.9635 | 2026-09-04 07:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 14f0f2c2-3774-3b59-8f3e-1167cd43da24 | -8.5048 | -54.6606 | 2026-09-04 07:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 4f15b0e5-5d83-3251-84c0-85ef1a8433e2 | -6.6881 | -59.982 | 2026-09-04 07:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 7362b316-e029-3cf7-ae24-6933e957a64e | -8.5916 | -67.1788 | 2026-09-04 07:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 1ea6c004-8c3f-3b5c-8b31-bd2e365cb3b1 | -6.6882 | -59.9628 | 2026-09-04 07:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 3082d417-aff1-3914-88f3-e8f21f3fb238 | -6.7065 | -59.9813 | 2026-09-04 07:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 31.4 |
| ba6ce7bd-f4eb-3938-9a14-f7fb8e240349 | -8.6101 | -67.1783 | 2026-09-04 07:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| c9e205e3-64ad-3005-97bb-1ad96f566f01 | -7.38935 | -72.80391 | 2026-09-04 07:05:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f5192b95-21b9-3358-a43f-1e328ca41408 | -8.5916 | -67.1788 | 2026-09-04 07:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| db452cd6-334f-384c-905e-4b554cfae1b6 | -6.6882 | -59.9628 | 2026-09-04 07:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 637b8310-0ac9-3499-9a4d-0cb0f0b13536 | -8.6101 | -67.1783 | 2026-09-04 07:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 5bad9550-bb23-38d0-9d8c-9562e06928e7 | -6.6697 | -59.9635 | 2026-09-04 07:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 8be80e5e-c9d9-326f-8abf-83602e982934 | -6.6881 | -59.982 | 2026-09-04 07:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 110.6 |
| bf655c78-efbe-31b9-a949-06aa0312fe2a | -8.6101 | -67.1783 | 2026-09-04 07:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 87.5 |
| bb019b10-c1af-36ea-8347-6b68c6ef0898 | -6.6697 | -59.9635 | 2026-09-04 07:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| a8bf6fac-1885-37b5-aff8-bc173026dca0 | -6.6881 | -59.982 | 2026-09-04 07:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 7a371566-3542-379c-87e1-49ec4ad6a8b2 | -6.6882 | -59.9628 | 2026-09-04 07:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| b52d63de-5836-3e86-be16-4eb340fe6499 | -8.5916 | -67.1788 | 2026-09-04 07:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 3f482cc3-f0ed-3568-9d38-efbdf2680ef1 | -6.6697 | -59.9635 | 2026-09-04 07:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 7edce3ac-3ab0-3c48-9433-86b30459546e | -8.5916 | -67.1788 | 2026-09-04 07:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 28844024-f9b9-37b2-90ec-53d1a4dcfd1c | -6.6881 | -59.982 | 2026-09-04 07:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 101.1 |
| b684ec58-2ad2-305c-8608-c283d60464b4 | -6.6882 | -59.9628 | 2026-09-04 07:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| d7778981-5f59-3347-b5db-2f866ee0375c | -8.6101 | -67.1783 | 2026-09-04 07:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |
| bb5b856b-51a9-35fb-beac-1d811facfdcd | -6.6697 | -59.9635 | 2026-09-04 07:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 94972ff3-7ab1-3c3d-86fd-818c7e3ae93d | -6.6881 | -59.982 | 2026-09-04 07:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 038afa64-1c84-39ea-869e-f586baa9e8f9 | -10.5103 | -51.3194 | 2026-09-04 07:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 6b9f97a3-26fc-351f-94db-0e97f0a23aa9 | -6.6696 | -59.9827 | 2026-09-04 07:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 06c32fa3-fa2f-309c-a47e-39aad59d7da6 | -6.6882 | -59.9628 | 2026-09-04 07:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 7c062302-ef58-39f8-bb66-04d6ebe61e42 | -8.6101 | -67.1783 | 2026-09-04 07:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 39886599-ec47-307a-998e-f4bc662b11ee | 2.44778 | -60.76201 | 2026-09-04 07:41:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c524f72b-cacf-38f5-bc49-974f50ec8269 | -3.2154 | -61.17819 | 2026-09-04 07:44:00 | AQUA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 40590bc7-a8d6-3d95-86cd-1afec7754d14 | -5.33181 | -60.13628 | 2026-09-04 07:44:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b0d6a216-6132-33e1-badd-fc5275373397 | -6.66945 | -59.94891 | 2026-09-04 07:44:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 761c7a27-2c84-375a-b1ce-a49bc1e2d638 | -8.16275 | -62.76906 | 2026-09-04 07:44:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d765bd14-e514-3842-9c8e-6333bd237c8f | -5.55665 | -60.17721 | 2026-09-04 07:44:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |


[Clique aqui para ver as próximas entradas](README40.md)
