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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f579d7f3-0eb3-393e-ab9a-0900623566d5 | -11.1587 | -44.7627 | 2025-08-26 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 318.0 |
| 653de00c-7530-3b74-bb53-727f0eed17f5 | -6.8228 | -58.9753 | 2025-08-26 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 457.9 |
| 9a85f7be-8663-33e1-b83b-ec47f60a8184 | -8.8734 | -62.4495 | 2025-08-26 01:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 6a57b9a3-a9e6-38d0-ae65-0793ab542113 | -6.8044 | -58.9568 | 2025-08-26 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 1130d46c-1f83-3d95-93c4-eca12506cde7 | -6.246 | -59.9982 | 2025-08-26 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| d7fc5fad-b736-3e89-bc27-77bf0b13a182 | -9.1677 | -40.6026 | 2025-08-26 01:40:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 70.5 |
| c9c28890-c8c9-30e5-917c-c76021d0d446 | -6.9128 | -59.3578 | 2025-08-26 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 74f07896-240b-30aa-8280-4d9a0829da21 | -11.3126 | -55.1112 | 2025-08-26 01:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 104a62ae-00eb-3b74-8d08-d277fa72693c | -8.9873 | -65.4379 | 2025-08-26 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 7c2ef361-b409-3555-8e4f-c20e2431a2d9 | -9.1722 | -59.4629 | 2025-08-26 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 709f68f2-b091-36a4-8dfe-c3773c030e54 | -7.3669 | -64.3667 | 2025-08-26 01:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 120749d3-934e-303a-ba9c-3dbafa47e267 | -9.0415 | -65.7349 | 2025-08-26 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 535a9d1b-b4a2-3e14-8986-f27383949895 | -6.7144 | -58.5732 | 2025-08-26 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| a764a69d-829d-30eb-997e-001ebb17556a | -6.7819 | -59.6711 | 2025-08-26 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 39d4a5dc-8496-3b12-9c69-05d1f10d5b8a | -6.8413 | -58.9552 | 2025-08-26 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 418d9f49-9ec4-39df-b841-a370c057a15a | -8.3206 | -50.5879 | 2025-08-26 01:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 4712e750-dd5c-3338-90a6-3bf14c8409b4 | -5.5281 | -60.2133 | 2025-08-26 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 968c27b8-9cb2-39b7-b5b5-6b887c9aa4ae | -6.7635 | -59.6718 | 2025-08-26 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 59e941ae-ab46-362e-8c6f-994b91acce56 | -8.3209 | -50.5667 | 2025-08-26 01:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 1d278ddf-85ec-3f07-8797-1d53b78875fc | -23.0478 | -50.364 | 2025-08-26 01:40:00 | GOES-19 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 190.7 |
| 4f20d1b5-c1c1-3a17-b32c-9aadf239dc94 | -6.8043 | -58.9761 | 2025-08-26 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 123.7 |
| ea0d2ecd-30e1-3139-ac95-b2a91c3ce5c1 | -9.191 | -59.4425 | 2025-08-26 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 85e1b0c9-3a4a-378d-84a6-3a8bb161cc0a | -7.367 | -64.348 | 2025-08-26 01:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 7efe8d48-11a7-3d09-a4c0-bc56822bc8f0 | -9.023 | -65.7355 | 2025-08-26 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 5e949f24-44f5-3ebd-9482-12e92d80ac16 | -6.2459 | -60.0174 | 2025-08-26 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 114.4 |
| a5d09ff0-79fc-34b6-9e36-b6bca3e0b741 | -6.7145 | -58.5539 | 2025-08-26 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 95f74c0d-b5bc-3b5b-9866-2a67c1179653 | -7.3854 | -64.3662 | 2025-08-26 01:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 105.6 |
| a18eb049-0592-3cfd-a9a8-100e2a5ddc71 | -9.1909 | -59.4619 | 2025-08-26 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| aea3b70c-c2d5-31ea-a3bb-1cc19ba0038e | -9.1724 | -59.4436 | 2025-08-26 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 32ce3d58-4389-3354-914d-14f2753e2434 | -20.8768 | -49.0237 | 2025-08-26 01:40:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.3 |
| f0871621-6b66-36a0-9d4a-1ceae53af26b | -8.8548 | -62.4503 | 2025-08-26 01:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 185.3 |
| fca62e75-ff37-3ce2-9d77-cf9d127869f5 | -8.3394 | -50.5863 | 2025-08-26 01:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 4fa4664f-eab1-3145-b83d-ee9e97327eed | -6.766 | -62.8659 | 2025-08-26 01:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| a52bcc1f-b2bf-30da-a960-15f5a911b93e | -8.3396 | -50.5652 | 2025-08-26 01:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 77b70827-0185-3823-a877-32d3276b21cd | -6.2275 | -60.018 | 2025-08-26 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 08122fb1-c29f-30d4-8bd1-c3b6b3dd754e | -8.855 | -62.4313 | 2025-08-26 01:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 4e301915-7bfd-3db6-a461-227c5d9064a5 | -11.14 | -44.7422 | 2025-08-26 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| b526dc9f-5623-3338-bdcf-c94afb6f71e3 | -6.9127 | -59.3771 | 2025-08-26 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 6b4cd5bf-08f2-3fcc-8336-f757b7c6869e | -6.9128 | -59.3578 | 2025-08-26 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 55695146-8ef1-3f0b-8050-d6064ef01951 | -11.5207 | -52.142 | 2025-08-26 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 8fcb3c3d-bf3f-3735-8b26-a6d4f5ad00ea | -7.3669 | -64.3667 | 2025-08-26 01:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 462677f6-68d3-355d-9410-35bad994e01f | -11.6273 | -46.4126 | 2025-08-26 01:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 38.6 |
| dbb2b47a-fc64-3d9e-b84e-3b8acc68256e | -11.1779 | -44.76 | 2025-08-26 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| b58818e2-6401-3b8a-bfca-c99b3148df79 | -9.0415 | -65.7349 | 2025-08-26 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 7ad10875-c730-37ee-aeb0-45554bf54c67 | -11.54 | -52.119 | 2025-08-26 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 555.6 |
| 0a9e310d-f439-3732-9c1b-d3932c7cc2cc | -6.8043 | -58.9761 | 2025-08-26 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 136.2 |
| cf301f4d-12e3-3c12-a563-8ee6893e1121 | -11.1396 | -44.7654 | 2025-08-26 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| fe43dbd4-0f14-37bf-8263-1dae90e9fc3f | -11.559 | -52.117 | 2025-08-26 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 235.7 |
| cdd0aa6d-9374-327e-a27a-e42e7cedc7f6 | -8.3209 | -50.5667 | 2025-08-26 01:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 37f3bc0d-a30a-3fbd-8933-546b4af5fb83 | -8.3396 | -50.5652 | 2025-08-26 01:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 6955eee2-38ba-3e9d-a3e4-3aca9f5f5bad | -8.3394 | -50.5863 | 2025-08-26 01:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 0594c6c6-9b57-3916-9921-793e7518ad15 | -9.1677 | -40.6026 | 2025-08-26 01:50:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 63.9 |
| 3a9d3494-d5de-3e51-96be-509b94861a5d | -6.8412 | -58.9746 | 2025-08-26 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| cc4c0946-8b72-3a39-8bf8-a7da7b5bde68 | -7.3854 | -64.3475 | 2025-08-26 01:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 149.0 |
| fe91ae0b-0e7a-3a9d-a29f-79aab85e61ce | -8.8364 | -62.4321 | 2025-08-26 01:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 7727e4fa-df2d-30da-810b-6a9fdce45ba3 | -11.2937 | -55.1129 | 2025-08-26 01:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 3e17545f-672a-3033-913e-c93eb66e34c0 | -9.1724 | -59.4436 | 2025-08-26 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| d0fffeaa-f7fe-3eca-ab32-7ff1e89ab3af | -6.8413 | -58.9552 | 2025-08-26 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 08f30110-0e2c-3aa7-b8a6-3cbf7e21a578 | -7.3854 | -64.3662 | 2025-08-26 01:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 45d173b3-f9df-3668-a7a2-a514ae0a1e6d | -11.521 | -52.1209 | 2025-08-26 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 8e3ce1b4-0a78-362c-83e8-38e9d7a6310b | -11.6351 | -44.8561 | 2025-08-26 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| e438e336-76a3-33b6-9ee4-15b96dacfa66 | -8.8363 | -62.451 | 2025-08-26 01:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 12d3c6b1-8245-3017-9a6f-1f0ebfcfae2f | -11.3126 | -55.1112 | 2025-08-26 01:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 188326be-7d4b-31d7-812c-4b8cda6279a8 | -11.1583 | -44.7859 | 2025-08-26 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| fce0ae5c-f776-37c3-aa22-cca6f5fb2a93 | -7.367 | -64.348 | 2025-08-26 01:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| b359d2be-ab6f-34e8-ae5e-f320a1ffbf0a | -6.8228 | -58.9753 | 2025-08-26 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 330.2 |
| bc9c1aa7-6249-3b94-9de2-4f227b9203ec | -11.5397 | -52.14 | 2025-08-26 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 382.9 |
| c61c908b-a69b-3b1b-a04b-08839643293d | -4.9605 | -55.8226 | 2025-08-26 01:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 0075dd86-8f18-3c4e-8cc0-9dbd5c9f4098 | -11.5587 | -52.138 | 2025-08-26 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 178.6 |
| f960b190-cdc5-3896-848f-d8a244889637 | -6.7819 | -59.6711 | 2025-08-26 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| c252faf5-a6ad-35ab-9c00-ce4d32d185db | -6.7144 | -58.5732 | 2025-08-26 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 40dc4a0a-ecfa-3afc-aa74-5bcfffddf75b | -9.191 | -59.4425 | 2025-08-26 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 589ee51c-8b04-3f4b-9821-815a3edaf74c | -9.1722 | -59.4629 | 2025-08-26 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| ec8c7608-6baf-397d-9425-08e1d8627e34 | -8.9874 | -65.4192 | 2025-08-26 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| c9faec8f-9a3b-33a5-8fd1-86d2de979388 | -6.2459 | -60.0174 | 2025-08-26 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 6e980d20-bfa1-39d4-8028-1de3f50b034c | -6.246 | -59.9982 | 2025-08-26 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 6797c6b6-0734-3a3e-8572-fde20cbd908b | -8.8734 | -62.4495 | 2025-08-26 01:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 944ad705-277f-315b-8e86-c188ed37d13d | -8.3206 | -50.5879 | 2025-08-26 01:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| aedb1293-9bd5-31fb-a4bf-e168c501c76e | -11.1591 | -44.7395 | 2025-08-26 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 246.6 |
| dd88f8fc-4bf1-3801-934c-7047b4eac6a5 | -13.1644 | -45.2897 | 2025-08-26 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| e83d07b1-7172-3329-af95-bafd6e2cc049 | -9.1909 | -59.4619 | 2025-08-26 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 4a66cc61-7965-39d7-bfd8-db0dcfb5e3d2 | -8.9873 | -65.4379 | 2025-08-26 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 90752f81-ed43-3f4a-9774-99f6bbeee502 | -7.4224 | -60.6236 | 2025-08-26 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 5b574602-b33f-33b8-9753-9b377a5683a7 | -6.7635 | -59.6718 | 2025-08-26 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| a42df307-f29d-3cbd-befe-c4429e0e0944 | -6.8044 | -58.9568 | 2025-08-26 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.0 |
| c053ebd3-45b6-3a16-8ad2-620bb2403569 | -8.8548 | -62.4503 | 2025-08-26 01:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 177.6 |
| 8f767cd0-6aa1-3c57-a1f8-b39183b7fd80 | -11.1587 | -44.7627 | 2025-08-26 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 494.4 |
| 63d4a0ea-de71-37fc-ae84-c2d1dd14be39 | -6.8229 | -58.956 | 2025-08-26 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 247.2 |
| 24a60226-3184-3058-9864-3e001a5aa920 | -9.191 | -59.4425 | 2025-08-26 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| b7edc4c1-c6dd-3456-a488-25e3acdf15c2 | -6.8412 | -58.9746 | 2025-08-26 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| b32494b1-972d-3b52-afce-182ec7110768 | -6.7476 | -62.8664 | 2025-08-26 02:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 7527afe1-0d8f-3d3b-b9d8-31c95f9cb575 | -7.3854 | -64.3662 | 2025-08-26 02:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| b1afff84-d4f2-3a2b-85e0-53f54683647b | -6.8043 | -58.9761 | 2025-08-26 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 1b09b3b1-4c14-3da7-9032-540ccd8e18a1 | -11.1583 | -44.7859 | 2025-08-26 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 06a9978d-4164-3d4c-bcaf-cf76237ccec0 | -8.3394 | -50.5863 | 2025-08-26 02:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 0b5093fd-8239-3a37-83d0-78322d5049ec | -6.9128 | -59.3578 | 2025-08-26 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 189a1518-d667-3923-874e-b2c6d2f3220a | -8.9874 | -65.4192 | 2025-08-26 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| eeb8453e-41c0-3336-9289-39a99a49b98b | -11.5587 | -52.138 | 2025-08-26 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 6e0e15c1-1c0f-39ac-a647-74eb0ab21919 | -11.1591 | -44.7395 | 2025-08-26 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 5bb061cf-2b0e-3f84-9d3e-5168db258973 | -4.9605 | -55.8226 | 2025-08-26 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |


[Clique aqui para ver as próximas entradas](README20.md)
