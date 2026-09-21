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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61409d78-2adf-3090-978f-699bd89ee522 | -9.5594 | -66.0359 | 2026-09-21 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 76cf0a32-8ece-3a95-890e-26f62da311bc | -7.5891 | -57.6561 | 2026-09-21 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 1860f8fe-7799-31d0-b314-5a3b03d549c5 | -7.5888 | -57.6953 | 2026-09-21 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 683edb6a-8906-3c3e-8158-f717a2edbdb8 | -11.7823 | -49.8152 | 2026-09-21 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| c01cb317-3bda-3e4e-9891-0c2e54985658 | -6.2026 | -57.7778 | 2026-09-21 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 63e078bb-d18d-344e-886b-342104320b89 | -10.0712 | -50.26 | 2026-09-21 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| fd07375d-8531-3bd0-ae41-6e19c7e6eece | -11.1 | -51.0475 | 2026-09-21 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| f2b13f36-ab41-3794-a4b8-f2f065d3afbd | -5.7614 | -57.6002 | 2026-09-21 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 3fc04a11-7582-312c-acf4-afa9911ed9b8 | -9.4567 | -45.4178 | 2026-09-21 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| fd929108-3612-3261-9d78-e23d196c42b7 | -10.4853 | -50.346 | 2026-09-21 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 1031fb3b-ce15-30a0-90d8-4a8e7cd0021d | -10.7626 | -50.8069 | 2026-09-21 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 9376f542-9330-3fe6-a0da-5bbc729bfe4c | -7.5889 | -57.6757 | 2026-09-21 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 126.2 |
| 73edfe7e-b2e9-3821-b23c-0d5de98e7294 | -10.3735 | -50.2294 | 2026-09-21 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 5e83acb8-0bb2-352f-a72e-331b1c46ccc7 | -11.0509 | -54.9106 | 2026-09-21 01:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| d7cd2af6-451c-3cc5-83c0-98afb89f9dd8 | -9.4757 | -45.4156 | 2026-09-21 01:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 4f807c7d-ba4a-31c6-89d7-effa4cc59031 | -10.5039 | -50.3654 | 2026-09-21 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| d28e206a-db0a-3f30-b428-0ff7f8e1f8dc | -3.0717 | -61.2764 | 2026-09-21 01:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 5b11c771-514f-3663-afcd-7a9117e4ddea | -10.2173 | -59.403 | 2026-09-21 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 36666c94-5145-3969-8b2b-114cf86d9a11 | -6.4485 | -59.9909 | 2026-09-21 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 01b96c77-3189-3d46-a910-0bfd01a3fbca | -6.467 | -59.9902 | 2026-09-21 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 55ef4d2d-ea67-38c1-b14b-f27b65f2a4ae | -3.0534 | -61.2767 | 2026-09-21 01:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 8d09b344-cb2d-34e7-aad4-32306c511225 | -10.3924 | -50.2275 | 2026-09-21 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 28ad6b7f-690e-3544-a8c4-92ff54d1c7ed | -10.7437 | -50.8089 | 2026-09-21 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 3cea7bb4-6b3a-32ed-b652-370f8e5d5f0a | -6.4486 | -59.9717 | 2026-09-21 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 8611165b-44e5-31b9-9ffc-df8d39b36d6b | -11.041 | -54.1567 | 2026-09-21 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 3e86ee73-cf74-3d27-b315-db85f2cd14f1 | -11.8204 | -49.8106 | 2026-09-21 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 72266ec7-c42f-38fc-a866-c3d9ac1daa3e | -16.03 | -52.5135 | 2026-09-21 01:00:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 111.7 |
| e7cbf520-2385-317c-ad2e-4bbee98c55fa | -11.8014 | -49.8129 | 2026-09-21 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 169.9 |
| ce8937e7-0112-3582-9708-5538340c7417 | -6.7464 | -59.4223 | 2026-09-21 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 3f0dd6b0-0f35-3d11-a88b-e75038404f49 | -10.8854 | -56.2362 | 2026-09-21 01:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 4d1b836a-2656-310f-b2e8-cfc96a551e60 | -7.5703 | -57.6962 | 2026-09-21 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| f3977d6c-04be-36ca-97fc-8ec99a3017a6 | -10.5042 | -50.344 | 2026-09-21 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 347d0281-4516-3037-aaca-1a58ff1fdc76 | -3.0716 | -61.2953 | 2026-09-21 01:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 26.0 |
| fb7883e8-a02c-36dd-8007-93f0273553ec | -9.5593 | -66.0545 | 2026-09-21 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 6f1cda68-e916-355b-ae95-49f24bb26cfa | -4.3541 | -55.6653 | 2026-09-21 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 3349514a-05bd-3f38-8679-96ad66b932ab | -16.03 | -52.5135 | 2026-09-21 01:10:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 149ee82d-1064-3b0c-9119-b6fec561f5b8 | -7.5889 | -57.6757 | 2026-09-21 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 96fcc4a8-cb81-3427-8b8e-60b60c80b208 | -6.4485 | -59.9909 | 2026-09-21 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| f047c8ba-9e5a-3ca5-b7c1-dae9fc290466 | -7.5888 | -57.6953 | 2026-09-21 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| e1cbc6dc-0f4d-36ed-9082-7649e484a63c | -10.4111 | -50.2469 | 2026-09-21 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 21fab90b-a236-3a78-8519-d27956b060b7 | -3.0534 | -61.2767 | 2026-09-21 01:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 60746a75-d8c8-3182-b655-fb860665a2a8 | -10.0712 | -50.26 | 2026-09-21 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 222801fc-effc-3acc-bb79-c55deffcba99 | -10.3921 | -50.2488 | 2026-09-21 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 6d9c4742-ff9e-3a34-a5d2-70d68d2d1694 | -9.4773 | -40.3116 | 2026-09-21 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 58.8 |
| ce973953-9daf-3919-8809-e479a41d5b01 | -11.8204 | -49.8106 | 2026-09-21 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 83020b9b-130f-361f-9e66-5ac10493ed10 | -6.467 | -59.9902 | 2026-09-21 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| c3f0d6ef-308c-3ba4-ac16-08f3083d5098 | -4.3541 | -55.6653 | 2026-09-21 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 3f03cdff-889a-3c95-aa7a-bdf9cf7a592b | -10.3924 | -50.2275 | 2026-09-21 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 9b8b2364-7bc1-3cb1-ac6e-5622a27eadba | -9.4374 | -45.4428 | 2026-09-21 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| fef01302-8485-30d8-ad0f-59205e09c6bf | -9.5594 | -66.0359 | 2026-09-21 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 9d79d866-de3c-3dcc-a85a-739d7c9b4cd4 | -7.5704 | -57.6766 | 2026-09-21 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| abae4911-4b31-30ac-bd3e-393b265b95a3 | -6.2026 | -57.7778 | 2026-09-21 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| e11ace01-7c7f-3176-b255-829d8353d2c3 | -10.4853 | -50.346 | 2026-09-21 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| fdae08d1-bfaf-3666-9079-d7456a3d92cd | -10.5042 | -50.344 | 2026-09-21 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 957bfb72-35b1-3d5a-b90e-9421195efbd3 | -6.4486 | -59.9717 | 2026-09-21 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 77172ce6-4d5e-3a6a-8f1f-a73915e9b4e9 | -7.5703 | -57.6962 | 2026-09-21 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 531fd912-975e-3141-8ca0-49f0b4093eea | -11.8014 | -49.8129 | 2026-09-21 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 184.7 |
| c9888d41-957e-3c05-aa88-53eb9d92ffd7 | -6.7464 | -59.4223 | 2026-09-21 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 4b654050-c137-3b4c-bc37-5e203d30a064 | -3.0717 | -61.2764 | 2026-09-21 01:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| fa5a98b6-cc39-3275-a0b5-44e8e0731646 | -11.8017 | -49.7913 | 2026-09-21 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 182d3fa0-c2dc-33d5-ba75-10cb1e279681 | -10.2173 | -59.403 | 2026-09-21 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 38.0 |
| d0184878-50d3-3b25-948b-f25946947dff | -6.4671 | -59.9711 | 2026-09-21 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 95cbed86-9784-380f-b2bf-d2aa151e4c8d | -3.4241 | -59.2535 | 2026-09-21 01:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 2fc40926-5059-3f03-b7c9-d3df8eb91a89 | -10.3735 | -50.2294 | 2026-09-21 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| a72f2f24-cd89-3017-aa2b-aa8cc3c7851c | -5.7615 | -57.5807 | 2026-09-21 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 7a6e4c46-f8bd-3177-a9be-766cc743262e | -9.5593 | -66.0545 | 2026-09-21 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |
| b3a72f95-defe-34e0-ab9a-af275bdc671e | -11.041 | -54.1567 | 2026-09-21 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 5e2befca-f8d9-3076-85f4-630f123095f4 | -11.0285 | -54.1628 | 2026-09-21 01:18:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fcf4bed2-8bdb-39b5-a47a-fbaa3681994e | -10.2169 | -59.405899 | 2026-09-21 01:18:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1652cd3-d136-3d78-8644-3cd635594a5a | -4.3411 | -55.666199 | 2026-09-21 01:18:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19d1e757-80f1-36bd-b4e4-8c573d3ce270 | -3.3886 | -59.582802 | 2026-09-21 01:18:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 75ad8c65-669e-3d9d-b6b1-26368b7ac423 | -5.2027 | -56.099499 | 2026-09-21 01:18:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d73f995e-7b1b-37dc-992e-deca32ce9550 | -9.5546 | -66.0103 | 2026-09-21 01:18:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 915f0764-c92b-3959-8c63-082780bf3c0b | -7.5623 | -57.6763 | 2026-09-21 01:18:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1f15415-cce0-3595-b06d-f775c9290fc9 | -10.7033 | -68.702202 | 2026-09-21 01:18:00 | METOP-B | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c62b67d3-ff1f-3ef5-9f74-a95ff412d0d7 | -6.7358 | -59.4119 | 2026-09-21 01:18:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dc70234c-f225-38f7-a99c-a851177655dc | -3.0464 | -61.266399 | 2026-09-21 01:18:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d9e9528b-8692-3c3d-bb4f-1bf9d799b6fb | -9.564 | -66.051804 | 2026-09-21 01:18:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| af73dbcc-8908-3d6e-8e85-3c49b2edb344 | -11.0346 | -54.914902 | 2026-09-21 01:18:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 47fdfefc-0ecf-3c79-a30c-4f60252f148b | -6.4559 | -59.9972 | 2026-09-21 01:18:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 89b17c9d-b207-35d9-b0d1-ae4a6e9bfd8d | -10.1071 | -69.125999 | 2026-09-21 01:18:00 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 51978c17-01fc-3650-91e6-7063a4a35104 | -7.5866 | -57.691101 | 2026-09-21 01:18:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 099338f4-0475-3275-956c-6cfd79e2a96e | -6.3066 | -60.018299 | 2026-09-21 01:18:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 47a6602f-259d-3612-8764-84e5b2ef36d5 | -6.4524 | -59.983002 | 2026-09-21 01:18:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e2ac27e3-d8b1-3163-8a9d-6360a43e13fb | -2.8711 | -57.838001 | 2026-09-21 01:18:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c1034178-6486-3856-92a4-e8ccdd866c49 | -11.9083 | -63.267502 | 2026-09-21 01:18:00 | METOP-B | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6be7c801-8f97-3448-8280-65f1070e50f1 | -7.5454 | -61.316502 | 2026-09-21 01:18:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 974edcdd-d19b-3f5f-9023-883770c30acc | -9.5593 | -66.031097 | 2026-09-21 01:18:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1bc2e160-8e32-33fd-8fac-983b55854462 | -5.7692 | -57.602699 | 2026-09-21 01:18:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49ba4b56-03bb-3ea5-b8aa-2f21e208c8e0 | -9.5526 | -66.047203 | 2026-09-21 01:18:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5aab0146-9b97-3c9e-b333-76f520312dc3 | -9.5609 | -66.038002 | 2026-09-21 01:18:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 44724bb5-a750-3f05-b055-8c1bb2fef3ee | -6.8752 | -63.105202 | 2026-09-21 01:18:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0c24514b-48b6-3723-9277-43b189210d22 | -9.2 | -64.453003 | 2026-09-21 01:18:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5ff0a334-e278-310b-957c-49fa500c24de | -10.5323 | -57.4562 | 2026-09-21 01:18:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 12e8a21e-05f1-3c8e-a529-9affab73fcd8 | -3.4154 | -59.264 | 2026-09-21 01:18:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c8d62aec-4a50-3f45-8a27-b16f96a58c5c | -6.4393 | -59.971001 | 2026-09-21 01:18:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7e45d1cf-6a34-3bde-9546-96d417d5cf50 | -6.7159 | -55.097 | 2026-09-21 01:18:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc80d746-61bf-31f1-8967-93072fe0f4a1 | -9.5531 | -66.003403 | 2026-09-21 01:18:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 39f6be93-db2c-39f7-8225-fe221f67a005 | -10.9234 | -69.539703 | 2026-09-21 01:18:00 | METOP-B | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| d62bd9f5-dc34-341f-87f6-0b1c6013a24e | -8.9887 | -69.505501 | 2026-09-21 01:18:00 | METOP-B | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README12.md)
