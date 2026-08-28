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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 027e2c63-fe4f-3f09-86d1-7f10f9dbcbd0 | -12.0733 | -47.1614 | 2026-08-28 15:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 182.4 |
| 7374ba7a-e1a8-3886-a602-7398a450ab4a | -9.1525 | -49.9639 | 2026-08-28 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| a3a4c84a-d90b-3fd8-8d71-f822f8766bde | -13.3792 | -51.5061 | 2026-08-28 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 7a992f96-9c10-3761-aa8a-2c2e3335b88b | -10.4981 | -64.5005 | 2026-08-28 15:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 266.6 |
| d97f0606-2421-3216-b4d8-b000084c684d | -13.3789 | -51.5275 | 2026-08-28 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 80dc5b86-9df0-3b02-b96c-da24d81e23e2 | -10.7789 | -53.9958 | 2026-08-28 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 60b31958-3803-3ceb-aa54-b8529945a0f4 | -11.7354 | -54.5431 | 2026-08-28 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| b6666769-c67d-3ad1-a9c9-f456b19d016e | -14.6024 | -53.1508 | 2026-08-28 15:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 185.1 |
| 172363a4-a69a-3e9c-8a0d-7f724e890d65 | -10.9589 | -50.2958 | 2026-08-28 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 234693aa-cee1-31f2-9999-8ef3dc71a018 | -8.3717 | -62.716 | 2026-08-28 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 4b3f7a4b-158e-3ea3-b4a8-d7e8fc42251c | -14.4444 | -53.3806 | 2026-08-28 15:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 181.4 |
| cff4a774-9912-3c96-a0a5-1378949587e5 | -11.025 | -49.644 | 2026-08-28 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 4010dd46-6a06-3387-9c9c-e31ea3213e02 | -13.2664 | -51.3711 | 2026-08-28 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| cbccf257-a951-352c-bf15-f8dfb13cfaa7 | -14.1645 | -52.8269 | 2026-08-28 15:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| acb8795a-bca6-3bc1-864a-dba32ecfd5a9 | -11.0413 | -51.1808 | 2026-08-28 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 77481d0d-36f3-36ed-80f7-04d3e907f633 | -13.323 | -51.428 | 2026-08-28 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 6c03c839-401e-3400-90e3-57bcbac52189 | -6.769 | -58.7066 | 2026-08-28 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 118.9 |
| e85b0cc1-d26e-3ce3-8c92-a457f56bd456 | -8.6694 | -49.5369 | 2026-08-28 15:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 164.4 |
| e3d2f853-5f3b-3cca-8ded-8e71c99c808c | -8.5971 | -54.7553 | 2026-08-28 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| fdaf2623-f3ad-3ebd-b258-fd8881052435 | -6.2692 | -53.1526 | 2026-08-28 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 1dbfbde5-a4c4-3412-b006-2dd41381d977 | -10.8993 | -50.4945 | 2026-08-28 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 191ed5da-4e78-3b88-bdef-993b4d55b562 | -6.5865 | -55.4346 | 2026-08-28 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 9dc8cdc3-02a2-37ca-9871-18d7ac61949b | -11.8243 | -47.1954 | 2026-08-28 15:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| b55515ae-10e3-3ad1-9ffd-ffb9143b25d0 | -8.8031 | -70.785 | 2026-08-28 15:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 79.4 |
| b3ebf1e9-3e1d-3214-a5cd-b63b83f21b5a | -14.2102 | -45.274 | 2026-08-28 15:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 94f581e6-31c4-3fe3-b1bf-20af52faf6cf | -10.5596 | -50.4449 | 2026-08-28 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 3814f8e2-8b73-33ed-842d-0cca9bfb5d3e | -9.9706 | -53.9624 | 2026-08-28 15:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 31f4999a-117a-3d2d-a2ea-c15922239af6 | -8.8031 | -70.8033 | 2026-08-28 15:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 0d9d3ec9-47e8-3685-8dca-8162131ea2b8 | -10.3894 | -61.2502 | 2026-08-28 15:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 37371a63-a9db-3f90-b2cd-51f6100a6055 | -6.5323 | -55.2378 | 2026-08-28 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 37353d86-b73c-3ae7-98c1-50748eb1fe47 | -11.2302 | -45.0528 | 2026-08-28 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 27f32cc9-695c-3ffe-b360-7e2907e5dc69 | -10.3205 | -49.9567 | 2026-08-28 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 342a53a9-827b-3f8a-b4c8-5713c6c8493a | -8.3902 | -62.7152 | 2026-08-28 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.3 |
| fe2423dc-18b4-3522-b799-a2986e82650b | -6.9872 | -59.2582 | 2026-08-28 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| a25e9e7b-fb12-3c5f-bf40-d76c44184d73 | -13.8378 | -54.0573 | 2026-08-28 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 126.2 |
| f4b8d13b-9560-3d5d-9819-86dece761b32 | -6.9336 | -58.9514 | 2026-08-28 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 820955c0-abe3-3d85-b124-53310606b7a5 | -14.4842 | -52.1512 | 2026-08-28 15:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 154.4 |
| d7e6029e-fa6c-3156-aa23-ff2d1d8c5ca5 | -10.7596 | -54.0384 | 2026-08-28 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 239.7 |
| bd1a5644-4d75-3569-a413-a0b06ef21e73 | -6.9699 | -59.0658 | 2026-08-28 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 4e828431-0b89-317d-91b5-dfb91c365886 | -10.5166 | -64.5186 | 2026-08-28 15:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 8eea9492-004d-3ffe-83f3-29cba89e46bf | -13.4194 | -51.3945 | 2026-08-28 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 26c56146-8d33-33cc-92eb-061b89ebdbee | -13.3985 | -51.5037 | 2026-08-28 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 113.7 |
| a4f6810f-2de7-3dd5-bed5-a0fa2da116e4 | -13.3607 | -51.4659 | 2026-08-28 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 84b7874f-0632-3cbe-8dad-a877c98dd618 | -6.8571 | -59.4179 | 2026-08-28 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 240165e9-91da-3971-9901-69e04a996160 | -7.4953 | -55.2862 | 2026-08-28 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 147.7 |
| dbe9c6a2-d079-3801-9f74-af21a41319f9 | -12.0541 | -47.164 | 2026-08-28 15:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 0165285e-0c15-38cc-8216-db3169a8a4e7 | -10.5601 | -50.4022 | 2026-08-28 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 8ea30abf-8a08-3642-b8d7-8c1470d18423 | -10.7593 | -54.0589 | 2026-08-28 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| d651fc27-6e1b-3cc9-8afd-94a460841481 | -10.498 | -64.5193 | 2026-08-28 15:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 91320a70-09c0-342b-a7c9-021e20913fa1 | -5.8876 | -52.1064 | 2026-08-28 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| eee2eb6b-4392-3912-9d12-03c7a6e43f66 | -6.6396 | -53.1934 | 2026-08-28 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 4f72ce2b-bc90-33d2-a754-1e40f72f5657 | -10.7787 | -54.0163 | 2026-08-28 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| aff688dc-8a39-33f8-a93b-dfe1dd2f9ae0 | -11.7167 | -54.5244 | 2026-08-28 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| c2a73718-44ec-3ec0-9ab4-b332a6af8aa4 | -6.5138 | -55.2387 | 2026-08-28 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 5cd627a4-872b-34b2-8e91-f17c8d515b32 | -6.7513 | -55.6853 | 2026-08-28 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| a984e6ac-1ad8-3c91-8498-c63f6546b434 | -8.6017 | -70.0173 | 2026-08-28 15:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 59.1 |
| b77bca95-b6bc-3955-95fe-e445501594ad | -7.3663 | -55.1734 | 2026-08-28 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| ce6e2e9b-fd32-3e3b-8002-edded03cc124 | -9.2282 | -51.5428 | 2026-08-28 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| cb2b6d6e-22f5-3260-ac3d-cf807f1c4f30 | -10.4693 | -46.1802 | 2026-08-28 15:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 71a7938c-88e6-3764-8c48-8d6c136264ec | -9.9708 | -53.9419 | 2026-08-28 15:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 341.9 |
| c683b43d-98e0-3f38-962e-4232c45dc057 | -10.3202 | -49.9782 | 2026-08-28 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 199.6 |
| 3dac0867-18ef-3ebe-ae2d-5c2b1ca74add | -7.3478 | -55.1744 | 2026-08-28 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 411af0a2-836b-393c-b72f-06ab455a9717 | -8.7772 | -49.955 | 2026-08-28 15:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 9121230d-05ac-35cb-a6f5-42f1f7fda8fc | -13.432 | -51.7973 | 2026-08-28 15:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| b55c568c-c98e-3847-ac3a-d210dcd22d1f | -10.8801 | -50.5179 | 2026-08-28 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 4bb400c7-1312-3a4a-a3c3-d41a5003cc76 | -10.3391 | -49.9762 | 2026-08-28 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 8edadd4a-fb40-31cb-8ee8-2570160854ce | -10.3895 | -61.231 | 2026-08-28 15:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| f5c955f9-3074-36da-a010-1f8d51c267af | -11.7736 | -54.5191 | 2026-08-28 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 57b4224a-c034-3814-9d1c-93abae689b10 | -11.0247 | -49.6656 | 2026-08-28 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 58186c03-af5a-380a-a4fc-4fd7c4ee2263 | -6.2693 | -53.1322 | 2026-08-28 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 147.3 |
| aaffb228-8c70-3ff3-8f14-626da349cac6 | -11.006 | -49.6461 | 2026-08-28 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| d655e2e6-d6eb-36e7-a350-f065dfef374f | -10.5598 | -50.4236 | 2026-08-28 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| e98ac764-8b73-3e6b-8813-532838c7c259 | -6.5863 | -55.4546 | 2026-08-28 15:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 2ed5309f-4b49-3c3a-9bdf-422a71723125 | -10.559 | -50.4876 | 2026-08-28 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 214a6c14-4c70-337a-bce6-abf30a768e65 | -16.1641 | -58.5851 | 2026-08-28 15:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 286.6 |
| 8ba6b75d-c9f1-3b6c-a9f0-eca329f0bac9 | -12.3038 | -50.5915 | 2026-08-28 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 274.0 |
| ea2296c2-4fa6-3c49-8b9b-4436ba7ed4bd | -10.7978 | -53.9941 | 2026-08-28 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 94de231d-afdc-3b85-a345-70f38fe29c9a | -10.498 | -64.5193 | 2026-08-28 15:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 544fc69e-80e0-3819-b67e-7b8f80655f6f | -14.6021 | -53.1719 | 2026-08-28 15:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 108.2 |
| bdec07ed-8c6c-360b-a534-31e8f8293240 | -8.5363 | -55.3027 | 2026-08-28 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 595cee7f-f7f8-3b45-8616-ddfe1a71c67b | -11.006 | -49.6461 | 2026-08-28 15:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 85b38661-4579-3bb4-9bc4-6ff72c920288 | -6.8542 | -59.9372 | 2026-08-28 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| a7bac25a-99e4-393b-99f4-1c4a8f095c61 | -14.2402 | -51.7576 | 2026-08-28 15:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| eb038b2d-046f-3fae-9f14-91ffa12e78c2 | -10.8801 | -50.5179 | 2026-08-28 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| e180ae41-7937-3249-bc96-39dc4f878ba4 | -10.7593 | -54.0589 | 2026-08-28 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 1c35dfe5-9ac6-3450-8f34-8dc3114785bc | -8.6017 | -70.0173 | 2026-08-28 15:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 2b6a07c7-4822-3b24-a5d2-0f702e7dff2c | -8.6881 | -49.5353 | 2026-08-28 15:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 1f42c5f0-b1c0-371b-b07a-c1a03e24d82c | -6.7513 | -55.6853 | 2026-08-28 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 95676f61-3e6d-34e5-92ef-145ac3e17199 | -11.7354 | -54.5431 | 2026-08-28 15:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| b5dc5951-3477-3fb8-b715-8e594f49a623 | -8.3717 | -62.716 | 2026-08-28 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.6 |
| fbf2c434-2d7d-349f-be27-b3812978497f | -6.1472 | -57.7995 | 2026-08-28 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| b7eac471-e22a-3175-97b4-a2339afb7fa4 | -8.2227 | -54.9613 | 2026-08-28 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| cc508a8e-9320-3be0-8ad1-5fa27e312a2f | -10.3898 | -61.1925 | 2026-08-28 15:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 0a562bc5-aaa2-339d-b542-ac448281de57 | -13.3789 | -51.5275 | 2026-08-28 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| e62481bd-fcc5-3be1-b4b0-464b0c9a2791 | -8.8031 | -70.785 | 2026-08-28 15:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 160.6 |
| 6ad592f3-eadb-37db-91ea-2d5a94c11821 | -12.0566 | -50.5567 | 2026-08-28 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 3223b7b9-876a-39d8-8db6-5e0a88d54d2f | -10.9402 | -50.2764 | 2026-08-28 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| aff5671a-cf62-30b9-b84e-d788a492c538 | -6.8358 | -59.9379 | 2026-08-28 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| ab7f6798-2ad1-3cc4-b970-a05d88a9e091 | -6.598 | -45.201 | 2026-08-28 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 17c1c9a0-4230-36c0-8f4e-982a94017721 | -6.9514 | -59.0666 | 2026-08-28 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |


[Clique aqui para ver as próximas entradas](README84.md)
