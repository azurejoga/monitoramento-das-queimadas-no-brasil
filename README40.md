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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f0dc3cf-bd1e-3e28-9b4f-8430ee48e054 | -9.97716 | -67.09433 | 2025-09-22 05:57:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac1ab1ea-aebb-3087-b16d-652cd898d15c | -6.62969 | -62.93118 | 2025-09-22 05:57:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81ce444f-177f-3a60-b482-2143412be4ec | -10.16399 | -68.69314 | 2025-09-22 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 117eb1b8-f69c-3464-8723-52d6d5cb3769 | -9.81688 | -68.89492 | 2025-09-22 05:57:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0554f1e3-e3cd-33f5-8a72-f632b7020d2c | -6.5925 | -62.923 | 2025-09-22 05:57:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cab6dcaa-7788-3f2a-a887-13d460c4b013 | -8.98756 | -65.45992 | 2025-09-22 05:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1cd0338-435b-30ad-9274-284247fc5412 | -8.77638 | -68.97726 | 2025-09-22 05:57:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f141c1e-faaf-312d-8e4a-e0642cdcf49b | -6.85949 | -59.96209 | 2025-09-22 05:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a80a2229-9c3f-359f-ae6c-75fcda0faf98 | -10.19243 | -68.78861 | 2025-09-22 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad33aca6-ded9-39c7-bde5-11ab77a45fba | -10.17853 | -68.79001 | 2025-09-22 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ef229df-7303-394c-b0ab-974a16a4e8f1 | -7.31372 | -72.75099 | 2025-09-22 05:57:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ebc510a-4ee8-31d5-9943-baec609b9ac4 | -9.3954 | -68.93199 | 2025-09-22 05:57:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01bb3e81-63a2-34a2-b65c-23077a3a675e | -9.11442 | -65.50858 | 2025-09-22 05:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1f59ce6-604c-3ece-8f5e-eff2c1b6171f | -9.05033 | -65.76122 | 2025-09-22 05:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5db8fb8e-95eb-3c03-884c-988958718998 | -10.17519 | -68.78948 | 2025-09-22 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07b4d0df-f769-314a-a83a-c4ff9c77ffd4 | -7.93999 | -70.71331 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9897ea01-c346-3515-b27b-7fab33563084 | -8.98821 | -65.4555 | 2025-09-22 05:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3957a0cf-9ce1-3db8-966a-48725701cddb | -10.62769 | -69.18657 | 2025-09-22 05:57:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d2dd1c8-a20b-3537-8e77-7fa41309b759 | -10.16216 | -64.73684 | 2025-09-22 05:57:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e08ea1b-dbdc-32cb-aed6-0f1879d97484 | -7.59356 | -69.89074 | 2025-09-22 05:57:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2ebbfb6-e552-3c3e-8f98-7b4536437da3 | -9.48517 | -68.83858 | 2025-09-22 05:57:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e357acb6-8b7d-3e1d-b1f7-2e90d4a3f68d | -10.19632 | -68.78561 | 2025-09-22 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1d18447-311b-34ad-a937-653b2e5405b4 | -8.63967 | -69.26654 | 2025-09-22 05:57:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98405143-3e74-3d09-a83e-767e9942ee5c | -8.52844 | -70.87212 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4721e039-2149-30fa-bf27-6436ccf55526 | -10.02193 | -68.40544 | 2025-09-22 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8349c4b-0d90-3359-978f-41f364a78246 | -8.02423 | -71.05627 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| af17124b-36e1-3f78-8332-4633fe5ac2cc | -8.53395 | -70.34438 | 2025-09-22 05:57:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 53cd623e-310e-3de6-9a04-b212721c8ff3 | -7.59488 | -69.8914 | 2025-09-22 05:57:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a8f1451-c4d8-3be1-b59e-824a79864b93 | -8.0081 | -70.89338 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 316dfcdd-1a8e-3d9d-959e-dbcf75be24e9 | -10.17464 | -68.79301 | 2025-09-22 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 600d35a9-0868-3160-8a47-a1b22e1b1f6a | -10.19509 | -69.35088 | 2025-09-22 05:57:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b94430ca-ea7f-3098-bae1-17c5c8fa000e | -6.59671 | -62.92362 | 2025-09-22 05:57:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 107c7f96-9aca-3b48-a1a3-f03bbe09b02d | -8.48614 | -70.74688 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c751af29-46c4-38bd-99af-5f61fc81bacb | -9.46089 | -68.94962 | 2025-09-22 05:57:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55bfc1d3-be75-36ea-b8cc-cad4381f76d3 | -8.73933 | -69.10387 | 2025-09-22 05:57:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cc7dd39-a191-3164-afda-d097a16e990e | -10.02138 | -68.40901 | 2025-09-22 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f4be8c0-069a-3c0b-850c-59b3dd7f1634 | -9.19236 | -71.83599 | 2025-09-22 05:57:00 | NPP-375D | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fa21017-d7ae-3228-8f34-4a6cf5705857 | -9.88192 | -64.82732 | 2025-09-22 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 120e786e-6e00-3cb0-9271-9f6a4b1cdf3a | -8.20216 | -61.20343 | 2025-09-22 05:57:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd85e189-7443-323d-9066-50e93bc89b5d | -10.91005 | -68.43447 | 2025-09-22 05:57:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 859483d3-371e-38ef-8102-a57ad526a80e | -10.66643 | -69.10597 | 2025-09-22 05:57:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c058525e-89f3-350d-8481-c58cc5155cff | -10.67087 | -69.09946 | 2025-09-22 05:57:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6985d8ad-3a2d-3703-bd3b-b629567e164b | -8.41856 | -67.31199 | 2025-09-22 05:57:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 92020b9e-8ea9-38ec-99a0-7352d4549d20 | -9.36173 | -68.32447 | 2025-09-22 05:57:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d1e9ea21-e27c-3f0f-a69f-d319512c23dc | -8.04642 | -71.23325 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abff313f-4f35-31e3-aed7-39cf79866bb8 | -9.91782 | -65.0481 | 2025-09-22 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f36cf27-e0c6-38a9-adaa-c5fafed188d7 | -10.16682 | -64.73238 | 2025-09-22 05:57:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 527e22b1-ec0c-3bf2-b67b-88eeedbbae74 | -9.87802 | -64.82673 | 2025-09-22 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff1390e5-b643-3e61-860b-39a7e906cc19 | -7.80075 | -72.86425 | 2025-09-22 05:57:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2d33c95-38e0-35ae-a964-ab65bdb7ac60 | -10.27088 | -69.49252 | 2025-09-22 05:57:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b42cf69-871c-3af5-a0f3-112047740e13 | -6.59613 | -62.92747 | 2025-09-22 05:57:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| db2b6593-9c91-36ec-9bd6-74378072d861 | -9.36118 | -68.32802 | 2025-09-22 05:57:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c662691e-023d-3656-97ea-3be2c4385d69 | -9.10517 | -64.00249 | 2025-09-22 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99e1e7e0-baad-3c87-bcf2-8e473255a692 | -8.57143 | -67.86224 | 2025-09-22 05:57:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa596fed-51c7-3f1a-971d-4ee4cf87b374 | -8.72538 | -70.78112 | 2025-09-22 05:57:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| caa06eb6-c369-35b2-823d-1902e7edaf4a | -8.42396 | -70.27055 | 2025-09-22 05:57:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ec7b93f-530a-3afa-8a7c-c8cb8f8be399 | -8.39339 | -70.7393 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f17ce4b2-c6b5-361b-8615-859d64d01813 | -10.27439 | -68.7579 | 2025-09-22 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0337e7bb-0d48-308e-a4bd-df06cf45c3bf | -9.7877 | -65.06582 | 2025-09-22 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a55fe888-8833-3332-88c5-01b60e48c012 | -8.9576 | -68.87672 | 2025-09-22 05:57:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c088b5a0-2257-3c4b-9815-7af042f8ff02 | -10.66698 | -69.10245 | 2025-09-22 05:57:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85c8d1a6-b418-3dd9-9c6c-059b0e9b7146 | -7.5632 | -69.90784 | 2025-09-22 05:57:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 180a7e22-e570-33db-bca3-2dca4c6e0578 | -9.46922 | -67.09417 | 2025-09-22 05:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fd0e83b-9b6f-3a46-bab0-16ae0f2303cb | -8.29306 | -71.22453 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6b891b75-a52e-3a15-80e3-b85a9d90e3fc | -8.02077 | -71.05566 | 2025-09-22 05:57:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67fd41a1-fbf4-327f-a9a3-3a158553c756 | -10.05552 | -68.45457 | 2025-09-22 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee10596a-b9e4-3d82-a12e-4909c3613fe3 | -10.62234 | -68.46267 | 2025-09-22 05:57:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b77181d6-87fe-31f2-a8a8-f263177baac3 | -9.60937 | -67.54816 | 2025-09-22 05:57:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15d32aa3-6f86-34d2-b618-bd482909d8c3 | -7.70791 | -55.45255 | 2025-09-22 05:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d339b3b-b1df-36ae-96f0-69e5209ab4c3 | -9.10059 | -64.00547 | 2025-09-22 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3b194b2-93aa-315c-9327-6ca3218f46e4 | -6.63024 | -62.92733 | 2025-09-22 05:57:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce9264ec-fc19-3220-995d-ab8da7c880f9 | -9.88192 | -64.82914 | 2025-09-22 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c5cd8c6-8573-39ef-938b-d575880a888c | -9.92237 | -65.04388 | 2025-09-22 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b73d25df-e72e-354b-b080-4f9dc499e8e6 | -6.00757 | -44.32495 | 2025-09-22 05:59:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6f99aca0-cc0b-3995-860a-61ef18263555 | -5.568 | -42.11979 | 2025-09-22 05:59:00 | AQUA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 22.0 |
| 2649c51b-ad80-3ced-a187-4967c4ed8040 | -6.03421 | -44.13692 | 2025-09-22 05:59:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3f5cbb06-5cb9-30de-80b4-da98f8ed139b | -5.57009 | -42.13174 | 2025-09-22 05:59:00 | AQUA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 54abf9ea-490c-3c08-8b96-f133d2910a4c | -5.57249 | -42.11516 | 2025-09-22 05:59:00 | AQUA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 24.1 |
| f86a88a2-e99a-35f5-92b0-3a0595691c5c | -3.41881 | -47.60591 | 2025-09-22 05:59:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0f5d2b47-29d4-3ddd-963a-7b1e6e968b7b | -4.30636 | -48.08841 | 2025-09-22 05:59:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 457078f7-14b2-3377-8cd3-c63f2aaaaee4 | -5.5798 | -42.12143 | 2025-09-22 05:59:00 | AQUA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 43b45670-d4ef-3fcc-af6c-249151f5db32 | -4.31522 | -48.08972 | 2025-09-22 05:59:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3264f813-1b02-3c4c-8337-032a40c20d95 | -11.86963 | -64.94204 | 2025-09-22 05:59:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5e10e0f6-9462-3f6c-a9f2-9ba40abc58ec | -11.87508 | -64.93225 | 2025-09-22 05:59:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1c4562e-a9b2-3b9a-aad2-b14f25357620 | -15.94849 | -59.38152 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca4b1c42-f5dd-3df1-9c08-99d39e82d946 | -11.79472 | -64.92578 | 2025-09-22 05:59:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a1c59e6-e32e-32fb-b6ac-d964c6bb594f | -15.77254 | -59.40858 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c49c803-781c-3e3c-89fa-47dfdc5f418b | -11.83055 | -64.93106 | 2025-09-22 05:59:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a4441dc-a633-3670-9724-82b40ba749a3 | -16.0026 | -59.45518 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e85cdea-b2ce-331a-bc19-38ed5e8e3d79 | -16.00117 | -59.46916 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6c78aa2-d9f3-3d4b-b3b6-cf044fc146c1 | -15.84095 | -59.514 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7358737-f6b9-3e1f-8131-ae3d7c07c79d | -12.40602 | -63.8885 | 2025-09-22 05:59:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5124d308-c37b-3151-bb6d-bd1ab5a5b60c | -15.77199 | -59.41393 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ffbfaccd-7006-3e18-9ffd-2bf4d2d1002d | -16.02064 | -59.45852 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c29f863-ed4a-3ca0-980c-1fa00ace3aeb | -16.00255 | -59.44976 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89ed5c7d-d689-387a-9b29-b4f9570fb0c6 | -16.01983 | -59.46623 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bab5a4ee-a6a2-3e47-bf4c-1ac5f8c9e209 | -15.84187 | -59.50543 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 745b1d0c-ba20-3a82-b02e-d32785ca11aa | -16.01421 | -59.46138 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c3c84590-e3f3-3689-a4e2-a7004764efcf | -15.8357 | -59.50611 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 786f76ea-ece7-3a5d-b74e-a402f4e44a17 | -16.01263 | -59.46947 | 2025-09-22 05:59:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README41.md)
