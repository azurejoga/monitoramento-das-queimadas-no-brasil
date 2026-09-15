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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0903bf35-1159-3b9e-9771-f6c0d81130e8 | -6.05268 | -52.18897 | 2026-09-15 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54ef8c9a-2624-3127-ad88-926738daa9ed | -7.22684 | -46.17623 | 2026-09-15 05:18:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d5ee3185-bd7d-32d1-9c55-518a5963ffa7 | -5.13428 | -55.94965 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7c72b24-a004-3bf7-8eac-dcde3e5bfa3b | -9.99509 | -50.27657 | 2026-09-15 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e39b8fda-1922-378e-8fd4-d9f912ddb5c4 | -6.72754 | -48.11818 | 2026-09-15 05:18:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2fa4d162-3458-3626-9547-bf76cc33ca3b | -6.02182 | -59.93583 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 673b7e40-4ffa-32fa-8fdd-42cbe7edd4d2 | -6.79297 | -58.79068 | 2026-09-15 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2085de71-bc68-3fe9-88f9-43a89351e3f2 | -10.8863 | -51.55395 | 2026-09-15 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cfae28f-81bb-30e4-af99-06e3cddbdc28 | -10.93989 | -54.08445 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 092063f2-97de-3d6c-8c4e-45933284434a | -6.7215 | -48.11715 | 2026-09-15 05:18:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58c30f1f-237f-3581-bfb1-7adea7aeb7aa | -6.13911 | -59.88302 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 86f5b239-e229-334c-8e86-5115fc820077 | -6.10436 | -59.88775 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0f26bc1-3710-38c1-be73-53f1b4d9e505 | -6.37566 | -58.30158 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d1f402b-ce8f-33fe-ab7c-a169438681a3 | -8.32816 | -49.99503 | 2026-09-15 05:18:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f19a5ea-ac6b-335c-a2ef-deed35674414 | -6.10302 | -57.71285 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 969c6b0e-986e-3800-905a-383bade96232 | -5.0752 | -56.24545 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ecc0bbf8-f5fa-3f22-8325-acda9953fd7c | -8.46734 | -50.77411 | 2026-09-15 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 042ccdef-a140-3054-89a2-512d80e399ed | -10.67812 | -54.16744 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 83d1bce9-96c4-380a-87db-a8aa642b4b7c | -6.09004 | -57.90761 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1dfec43-4386-3d19-a819-0b5127f7f187 | -10.80731 | -46.21318 | 2026-09-15 05:18:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 728a296d-5246-3c42-9385-5fbc95cbd58e | -10.60058 | -57.31658 | 2026-09-15 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86d3f21d-60c6-36f2-b883-2849d6ba1716 | -6.01849 | -59.93531 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 983253f5-3e3d-325c-99a6-ea24f4de7809 | -9.45486 | -48.90652 | 2026-09-15 05:18:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13245486-0bc7-3a91-a778-122dda394029 | -6.85056 | -55.56049 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 615ccf28-acb4-3117-8d13-a200712d1d2e | -6.10491 | -59.88425 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2ee6432-83ef-3c37-a819-7658202bbf42 | -10.67068 | -54.1581 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e801906d-8ab0-3ba7-af64-d4946c698983 | -6.84818 | -55.55107 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| c51b4be1-a6e1-3424-b1e5-2e5b11289441 | -5.43918 | -60.22051 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e30e002-2812-3440-bed0-0f1eea364e5d | -10.68555 | -54.17676 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 72c3b871-fb91-3bff-8534-ed3f0f77ba51 | -8.50604 | -50.14409 | 2026-09-15 05:18:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1091edfd-9830-3464-b785-7923be40885b | -10.66695 | -54.1535 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b9851cc-f177-3b05-a29a-5df232666554 | -6.11141 | -59.88586 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a69395c4-0345-3606-8868-c7d4cfd7351c | -10.95486 | -57.19601 | 2026-09-15 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18628cd2-83f3-3853-bf07-561216528f75 | -6.36142 | -55.82881 | 2026-09-15 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6f9e0cd-5697-394d-8a87-8c2dd2666d65 | -6.1159 | -55.82104 | 2026-09-15 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e90d67cf-df34-360b-9c31-621685acc7f0 | -6.10689 | -57.68778 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 087c4b9c-1adc-39f4-bc0e-8e2c0be943fe | -6.27188 | -59.92542 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c6cff80-781b-3a5e-b881-fdaa5baeeb78 | -9.53603 | -62.37006 | 2026-09-15 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64b6682c-a66c-3e5f-abf3-4d8e19ae3f3c | -9.26265 | -59.63959 | 2026-09-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bbccfe1-fca3-3845-9823-f5ec0fb51ae5 | -6.01738 | -59.94231 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2eb90a2e-6c67-3b51-8cac-fb1ea04662b2 | -9.41496 | -62.70757 | 2026-09-15 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 17.1 |
| d3db5c0b-36a7-3cbe-a246-c3552ba4816e | -10.58301 | -47.73586 | 2026-09-15 05:18:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d48de813-1e94-3b06-be56-dfb11db5fdb8 | -10.02947 | -52.12432 | 2026-09-15 05:18:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89fbcb8e-e209-3d15-8474-88b94082c760 | -6.26855 | -59.9249 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 906c45a3-5f45-3fca-a653-8dbc8ad3e82e | -6.84209 | -55.54104 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0262920d-f0e8-3fee-bc47-bcdd9e685996 | -10.98399 | -48.32803 | 2026-09-15 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8ff55bb9-c869-39de-a2ff-f131ff16fe4e | -6.69462 | -58.70093 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e69334c-a8a4-38af-b577-0836943ec3cc | -6.20147 | -53.08833 | 2026-09-15 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed92df4f-e351-3a68-b247-7791a1a98895 | -11.2663 | -54.12604 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec9329f8-fb30-3df1-b3f4-db33119d05f6 | -6.85426 | -55.56106 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9286c6e2-8019-3daf-8b3d-f74879aa8967 | -9.71476 | -64.91508 | 2026-09-15 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59b822b1-8436-313e-9da2-1df073239183 | -9.3602 | -50.09882 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 374c4101-ede9-3727-aa6d-3c4f508da735 | -6.85692 | -55.54327 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71a70e37-20d0-3a18-a149-41a1886d169b | -10.99081 | -48.32457 | 2026-09-15 05:18:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f1950328-f87a-313d-bb3b-1192e753af89 | -5.78137 | -56.36658 | 2026-09-15 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17fc4909-0697-346b-bd27-12da4f546b29 | -8.50659 | -54.64125 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0512b60a-3673-30ca-bb47-bb44328ff3d1 | -9.20725 | -65.61984 | 2026-09-15 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c982cce1-b7e7-3335-a6b9-3979b3e27532 | -6.7065 | -51.17427 | 2026-09-15 05:18:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f99c44f7-1a9a-30b3-92c3-67969c63cef9 | -8.53702 | -54.69909 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74fbfa80-4fb3-34f3-ada3-b1e6f677cd28 | -6.10769 | -59.88826 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d3c75d4-474b-3b65-83bf-bcdd53c04edc | -5.59125 | -60.18595 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c1735022-cdf9-338d-bb46-c4c2cff877c8 | -5.16366 | -59.76812 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74e136c6-3329-31c0-bdf1-ad0d6764b3ce | -9.16025 | -49.99583 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9121a4fe-457b-3091-9cd9-cd2bacec467b | -5.08454 | -56.25491 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8a18551-4109-3c43-9d48-7c4d1381ee5b | -6.15833 | -55.71082 | 2026-09-15 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4a8e278f-ddf1-3444-afec-86a768f34ccc | -9.10519 | -65.5571 | 2026-09-15 05:18:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21abeb96-5c06-30dd-b9b7-7585fe13ea35 | -6.15654 | -52.7421 | 2026-09-15 05:18:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f318a8c2-8d82-317d-bd4c-af43239647c3 | -9.99554 | -50.27293 | 2026-09-15 05:18:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04579968-6e9c-3cf3-9dfd-86ba4c7513b6 | -9.52835 | -63.62549 | 2026-09-15 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8d1bed9-23f6-38fa-9066-05859046f204 | -9.41361 | -62.71575 | 2026-09-15 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3f83d607-32eb-349f-9c36-cd7e0e186284 | -10.38743 | -58.39404 | 2026-09-15 05:18:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f5c2b34-c338-3ec9-902e-f7cdeb457fc5 | -10.60353 | -57.32111 | 2026-09-15 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6b745f4-5459-35ef-ad13-d97966d3fa5c | -9.22691 | -59.40889 | 2026-09-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ffa2800-4509-3af8-80d3-d9861b44cfce | -6.03046 | -57.76016 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bde75d8f-6626-3285-99ab-6111a350ba78 | -6.11694 | -57.66725 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60bdba87-ba06-3923-87df-81a7db731353 | -6.85388 | -55.53823 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8e5a8c52-3152-38ed-8432-02ab94eb2588 | -8.26634 | -55.02855 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7c9f6b1-4733-3e26-b43b-94f56881a90c | -10.8859 | -51.55701 | 2026-09-15 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 873b9519-73dd-3477-b48e-1151cbffc664 | -9.30506 | -62.66908 | 2026-09-15 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 526e3422-47bf-30d3-8477-98c7e40aa925 | -6.84143 | -55.54549 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e6d9284d-9505-3715-80b5-c099bafd0576 | -6.10903 | -57.6292 | 2026-09-15 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7fdb4fd5-a1ac-3320-8a37-0ed44eefddde | -6.60362 | -58.58657 | 2026-09-15 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55c1e4b2-b766-317f-89df-ba11011d0aac | -8.08766 | -61.80247 | 2026-09-15 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c305d44-2dbc-3864-9811-a783a253f615 | -6.85322 | -55.5427 | 2026-09-15 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5e835d2-e2c6-31f6-b973-d5799fb0e0df | -8.54052 | -54.70319 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b11cf98-2683-36a7-9b3b-252c74ef6d1a | -9.36353 | -50.20636 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f78fd3f6-61bc-32e7-b031-5287a041e0ae | -10.68129 | -54.17616 | 2026-09-15 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e8e34aa3-fdcd-31e0-a76c-5506fcf9b648 | -9.19894 | -60.39335 | 2026-09-15 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e15ce201-5fcc-3bea-a7e0-a515f1003b79 | -6.15532 | -55.70604 | 2026-09-15 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96447f38-892c-37ce-9993-bc66bde627a3 | -9.96677 | -63.97316 | 2026-09-15 05:18:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79721339-d1f2-3845-8b71-7a67fa31e98f | -5.12363 | -55.94789 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d083113-b3dd-3394-a157-4ba1f883b8cd | -5.07402 | -56.25327 | 2026-09-15 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0ab2553-27d2-31ce-ae1c-bffb0b7a0b94 | -7.22805 | -46.17448 | 2026-09-15 05:18:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4d18e4b9-1e5a-3279-bcbf-023e5f35b066 | -8.41124 | -54.7201 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4beefd55-6236-3eec-b5e2-3184cb3caf96 | -9.69445 | -58.17603 | 2026-09-15 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c3aae83-9495-3f1c-b394-c3a71463fc70 | -9.42739 | -50.10078 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a73f70e2-0312-3478-a1e4-34430d12dd76 | -8.85046 | -62.36332 | 2026-09-15 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0723fac-6e6b-30cd-85f0-8723a9c9004c | -8.80875 | -46.90868 | 2026-09-15 05:18:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3ee05dfc-418f-3777-ac12-b7cb4986ed75 | -9.68993 | -63.4278 | 2026-09-15 05:18:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9700e7e7-c32f-3401-a87b-f7d6ffc6eedb | -6.32613 | -59.99127 | 2026-09-15 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README61.md)
