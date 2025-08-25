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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 878428a4-32f0-3949-a649-223151a7821f | -10.58425 | -47.13995 | 2025-08-25 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09e52fc4-6cca-31c2-9c19-0f4b975369df | -11.10756 | -44.78217 | 2025-08-25 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8976c591-bec4-3b71-a8fa-c51cf6deb412 | -6.63424 | -58.54651 | 2025-08-25 04:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7a18504-19d4-300c-908e-164b2a14f660 | -6.63365 | -58.54985 | 2025-08-25 04:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3264b330-28af-3e85-9ef5-eab7e7b0fd77 | -6.62936 | -58.41928 | 2025-08-25 04:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0bea7929-1048-3465-93c4-bffab88c1bf8 | -8.28027 | -47.24238 | 2025-08-25 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7dc843a-999f-35f3-91a3-ffabf6741d0c | -9.2644 | -59.78768 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 418f947a-3d32-3063-9cea-b73dc9a9929a | -8.07027 | -50.20389 | 2025-08-25 04:42:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f918fce4-e025-3923-a9b6-454742a9aa85 | -13.45087 | -46.91266 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f88fcfeb-06dc-30bf-96eb-41e04ba949ae | -8.50516 | -63.87049 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5c5db509-08f4-3d3d-bcd4-4a1bdd851d99 | -11.18386 | -55.01735 | 2025-08-25 04:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f813cb5-73df-37e9-89ae-44c0c6eb2635 | -11.1791 | -55.02161 | 2025-08-25 04:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb34ad84-976c-3242-8814-942e477db1cb | -11.1065 | -44.78981 | 2025-08-25 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67f0e7a7-f5ad-3de9-a743-47d9d7d60ef5 | -11.54467 | -51.91368 | 2025-08-25 04:42:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ea59012-6dce-3c9d-b73d-8cd4a656a9d7 | -8.88205 | -62.46443 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 75458a9c-5748-3025-bb7a-a1801e73afa0 | -9.518 | -60.56029 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ff7de45-d7e3-3b9c-9bd2-9ce72e9ee704 | -11.61084 | -46.23613 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9df842ec-fb25-366c-9626-7728d35fd59a | -9.15637 | -59.51913 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6103f75a-0414-3231-ab85-9bfd32e72219 | -10.45538 | -59.12915 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c532d593-66e5-3c49-a596-7efaa81de752 | -9.21695 | -59.71313 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90f6fed8-87ed-3a68-a290-077371af80ce | -9.20045 | -59.49817 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b15604ed-023a-3779-b411-c848fce2044d | -8.80851 | -45.46605 | 2025-08-25 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2a91e4e-b814-37ef-9b4b-1e027bb33b14 | -9.23197 | -60.92046 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 381bb42f-61f0-3586-89cd-7952a4978c3a | -12.73064 | -48.13944 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e829220-90dd-3e56-a026-462bbda1847c | -8.90068 | -62.43884 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f4d2f438-013c-3b72-991c-96a519fd6d4d | -11.13828 | -46.33382 | 2025-08-25 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c74a5c24-58f5-3555-9d54-23eb7c5dedd7 | -12.29041 | -49.13345 | 2025-08-25 04:42:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e1171944-e089-3da8-b4f7-e9fcc70fe43d | -6.82275 | -58.9486 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 455558f5-a2e5-3626-b1ec-ef98b36f88a0 | -9.15132 | -59.48532 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90b1f642-e4ff-3c4a-a181-8f3a06bfc423 | -9.18816 | -59.47386 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e713be55-0506-3385-8627-cd7534230869 | -10.53614 | -57.97306 | 2025-08-25 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c3641b3e-0c4c-3bd3-a059-6ea797d9cf96 | -10.77977 | -46.39213 | 2025-08-25 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b3889045-52e7-3aa5-9b83-d3b672de1fae | -13.05778 | -46.32146 | 2025-08-25 04:42:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53676d4a-8f9c-342d-8578-559c94ddd2b2 | -13.43381 | -46.92366 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36f743b6-e6c6-33fa-a88a-aeb5389a649b | -9.1948 | -59.43888 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3164bc5-c810-3d58-8269-fca41631246f | -13.48533 | -46.88444 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 138dce63-47e0-3396-b153-0cd7a804ad2b | -11.26417 | -44.98745 | 2025-08-25 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc0f9e3d-24c8-332a-bd11-4845eabbb238 | -9.19502 | -59.4971 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5955ffa-23aa-391c-bc93-52d9313db9ee | -8.11623 | -62.88838 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cf3dac15-9369-3611-84b5-ce06a68f75e5 | -8.92912 | -62.43264 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05bef555-6925-32c4-9960-c0d226218a5b | -8.23231 | -61.43314 | 2025-08-25 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59b08d11-13f0-3b36-a866-88ea034036f2 | -9.18819 | -59.43763 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fe63f1c-1126-3cd9-a314-858373bc2e76 | -13.44137 | -46.92487 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a046e40-bb05-3a57-b5be-b116f502e7f1 | -8.24534 | -61.46703 | 2025-08-25 04:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e761280-fd70-3419-917e-332032625b0b | -6.91626 | -63.0003 | 2025-08-25 04:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e503e076-9140-331a-afe3-5f69103c0c16 | -9.86476 | -47.83775 | 2025-08-25 04:42:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 007dfe14-df9b-3f99-854e-5abdf37bd042 | -13.45165 | -46.90733 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f7b347d-56d8-3ac2-bb31-c649bd29f031 | -8.31481 | -47.25176 | 2025-08-25 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 269d601f-18d1-3705-9762-44c7c173b156 | -8.80781 | -45.47097 | 2025-08-25 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b31ffc97-7294-3e86-a93c-839e86ad1d3e | -9.25785 | -59.64588 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a224c58-d809-3d7d-9373-f8f40015e7f3 | -12.20194 | -47.21796 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6111cc77-a8d5-3cb0-9ee7-352e6f13bf4e | -10.4019 | -57.68149 | 2025-08-25 04:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f4b51157-d72f-3ac8-95af-be415848cfab | -9.20588 | -59.49926 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02315e7d-9c34-3395-8a43-be6b192f778c | -10.4923 | -46.88361 | 2025-08-25 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2383cf1-3c29-337d-a5ec-cf234193c2ec | -13.61971 | -48.1776 | 2025-08-25 04:42:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c0eeb275-e590-335a-b97f-b9c440f1a457 | -11.28851 | -44.9644 | 2025-08-25 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10d12e78-4711-388b-8653-44188832700a | -9.14982 | -59.46302 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c47e545a-299d-3ffc-a956-68d7305f91b9 | -13.43481 | -47.02498 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41af8a4e-6eee-3345-9859-005582997026 | -13.51059 | -46.89777 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 768f638e-ae13-3c12-ac72-d7fd2d676291 | -6.82148 | -58.9567 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 326eb31f-0d53-3998-be24-d9435b562704 | -9.2003 | -59.49464 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4e1b6f6-75c2-3238-b9d0-22f0e5c2c873 | -13.4299 | -47.03256 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55e55008-a908-3ecc-9e27-ddbe8b37895c | -11.288 | -44.96807 | 2025-08-25 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3762140-d82d-3482-a1e3-8755eb99ef17 | -10.02852 | -51.07366 | 2025-08-25 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49a70806-0ac2-3a7a-8702-a1a63fd8b314 | -9.23112 | -60.92482 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4b22d6fc-2d1e-33ff-b088-89620559380d | -9.18722 | -59.47373 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50bef2fd-9128-3e9d-9f77-ac41651e1684 | -12.29893 | -49.14613 | 2025-08-25 04:42:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6468b59-59a6-3448-be91-c1fbc05f7635 | -10.0463 | -59.35992 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8ab264d-eb03-3790-b81e-f8171200925f | -8.54753 | -48.86306 | 2025-08-25 04:42:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c560a16-4e2c-345b-b5fd-cf81ced53115 | -7.90796 | -63.08578 | 2025-08-25 04:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 93273020-4c60-33d7-806b-f0e2e47b1769 | -16.42311 | -49.94109 | 2025-08-25 04:44:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0bf22ec0-9cff-325a-90e2-ca341ad651d9 | -19.17647 | -44.51958 | 2025-08-25 04:44:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3d8a8bb4-c6df-338b-b872-1040a83156f5 | -14.923 | -45.52959 | 2025-08-25 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a24b03c2-c4a3-3590-8cf3-54dec2103aa6 | -15.06001 | -48.67791 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95d88821-7079-36f2-95ef-ebfd2a533b56 | -20.36448 | -46.7746 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14fe9dfb-4182-3668-9017-9132761e52e6 | -15.07944 | -48.54382 | 2025-08-25 04:44:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e65a4e4-8801-329e-9690-064a1019739f | -17.18857 | -46.83829 | 2025-08-25 04:44:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8bc10763-9a9d-324b-8815-73405198dddb | -15.63919 | -52.7162 | 2025-08-25 04:44:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c038c43-6cb5-3fc0-a883-dc3c38c9afc0 | -15.13225 | -48.65066 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9eec3d43-c970-3ebb-8981-b6560541e90c | -17.84235 | -44.41766 | 2025-08-25 04:44:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f38c781f-ef69-364a-bd3b-91d9f928a42d | -14.2077 | -58.6289 | 2025-08-25 04:44:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec5015d5-fc9a-31b6-8e85-918785175e91 | -17.57887 | -45.38487 | 2025-08-25 04:44:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a275bbae-72f1-3833-84f1-a4513b150daa | -19.17707 | -44.5144 | 2025-08-25 04:44:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 832776d3-c4b1-31fd-949f-4c32a8128966 | -15.08357 | -48.66492 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b18c49b3-1eb2-3f20-8fdc-625a81e70a86 | -18.41782 | -49.20895 | 2025-08-25 04:44:00 | NPP-375D | ARAPORÃ | MINAS GERAIS | Brasil | 3103751 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c2e36766-b7b0-3ff2-9c95-0b734b1e3933 | -20.50808 | -45.991 | 2025-08-25 04:44:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c483864-8ace-37b7-8f8d-0d869a5892e5 | -20.30139 | -47.18292 | 2025-08-25 04:44:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 38b63c13-7db9-372d-bdd4-f09bc391c2e9 | -21.11964 | -48.92012 | 2025-08-25 04:44:00 | NPP-375D | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1adb8f8b-fa75-3247-9a9d-a9a538c8d27d | -22.00898 | -44.29131 | 2025-08-25 04:44:00 | NPP-375D | LIBERDADE | MINAS GERAIS | Brasil | 3138500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d6e48dcf-65f8-3673-9b2f-518caeb6541d | -19.9153 | -50.41334 | 2025-08-25 04:44:00 | NPP-375D | OUROESTE | SÃO PAULO | Brasil | 3534757 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7a80358a-26eb-3a60-a1f1-007e164e0715 | -19.73033 | -46.46923 | 2025-08-25 04:44:00 | NPP-375D | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08417336-fed9-349a-841c-e9de0b828717 | -16.70814 | -49.0845 | 2025-08-25 04:44:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6132825d-0469-399a-8c0c-c41dbbca0709 | -14.92688 | -45.53153 | 2025-08-25 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f13033a-8c8d-386f-b767-78366531612c | -14.7429 | -55.93295 | 2025-08-25 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76d78d8e-ae54-36d8-a304-2961dc56f20e | -19.39018 | -43.74362 | 2025-08-25 04:44:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5db9b541-6118-3a33-8346-4f132f124c70 | -20.36497 | -46.77069 | 2025-08-25 04:44:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf17dee7-3fb1-3b7a-833a-94a47f578b81 | -14.76455 | -47.5104 | 2025-08-25 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf67f3b1-7d96-3696-ae2d-cd4f1f902b0f | -15.14779 | -59.59081 | 2025-08-25 04:44:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 582415af-8030-3958-8523-60a930fd7461 | -15.05941 | -48.68201 | 2025-08-25 04:44:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e08644f8-cac9-36c6-8628-29604e32f850 | -13.00143 | -56.88563 | 2025-08-25 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README53.md)
