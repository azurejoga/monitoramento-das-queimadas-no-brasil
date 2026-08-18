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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49e863fc-54f9-3a55-96d9-a1b8390f6530 | -10.28076 | -50.44254 | 2026-08-18 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34054d80-f156-3e9c-a4de-5e8024b8d116 | -10.28366 | -50.44735 | 2026-08-18 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56f3ecc4-ee97-3a77-8aaa-85ed91597b3e | -14.25864 | -51.92384 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 746687c3-443e-320e-86c7-6cae00898b88 | -17.9484 | -44.42953 | 2026-08-18 04:40:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b931920d-60ad-3a78-8929-d1367aef3858 | -12.75762 | -48.42531 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6feccdce-6976-3d3a-87a3-9fc827334040 | -17.10302 | -46.56425 | 2026-08-18 04:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7291472c-674a-31b3-ab0a-8d24478bd8a5 | -11.11981 | -47.27116 | 2026-08-18 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3ececce-1fda-31b7-b3e7-da9084f8fbee | -11.20153 | -54.8236 | 2026-08-18 04:40:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba008221-46a5-3399-969a-9f87286aa3de | -12.71679 | -48.48808 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a6e1ad83-a3ea-367e-b614-074a41a4507e | -15.07175 | -48.72669 | 2026-08-18 04:40:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ceb02981-46d6-31bd-a01c-4023a47f381d | -14.63307 | -47.27624 | 2026-08-18 04:40:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8eb45e0b-b354-3533-9fc5-c8854f0f09a6 | -12.54534 | -47.8419 | 2026-08-18 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae1c9e27-0a4c-3ab7-902e-54db87d203d6 | -11.32998 | -46.20706 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 45cd678c-a280-30b3-a7e0-b568026c5869 | -14.35904 | -51.87283 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fc6a072d-c924-36d3-a02d-cdb6903f71e0 | -10.51797 | -50.78736 | 2026-08-18 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d465a762-f6f2-3c04-a2d9-d627eda3dad7 | -17.10822 | -46.57729 | 2026-08-18 04:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b668f064-8455-3a47-8af1-9cb793075cb3 | -14.17195 | -52.90302 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 4bdb3b01-0247-3006-8813-fc980be7bc49 | -14.03164 | -53.68062 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 82a3cfd6-51f8-3190-99c0-ef5fd0a7d54e | -14.49704 | -45.66914 | 2026-08-18 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a4b508b-1333-3a2f-a5d7-68d1d9acbc44 | -11.36145 | -46.39021 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ededb716-6542-3249-83e6-5dd774b0465b | -14.36088 | -51.87175 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a80788da-a3b4-3643-822d-ae6a4aded975 | -17.45819 | -47.8682 | 2026-08-18 04:40:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ac8c487-1154-3992-bac8-4a777903e671 | -11.50826 | -46.60822 | 2026-08-18 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9e37992-1511-3558-963f-6a78957ff694 | -14.16522 | -52.91769 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 12347267-af1d-3e56-9d95-144df76dd792 | -15.6301 | -48.89353 | 2026-08-18 04:40:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfabf181-a136-3c8b-b751-47feb8f380f7 | -14.8481 | -46.64393 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 828f3beb-8109-3764-ae29-cda74a4f1692 | -14.1682 | -52.92357 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e969b87a-c829-3e9c-9e3f-f579d592e5f8 | -10.27351 | -50.41971 | 2026-08-18 04:40:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dac6df85-5d77-3754-89a1-0c0bf096ae1a | -16.29939 | -53.18707 | 2026-08-18 04:40:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6e2bd5d-9363-37bc-b48f-cb59d9e74575 | -14.15998 | -52.90847 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b4d80017-062e-3f0d-b825-b5c63d19e4c0 | -16.40977 | -49.47444 | 2026-08-18 04:40:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1da3d32b-e003-33cc-b554-275a4c38dedb | -13.51248 | -46.28184 | 2026-08-18 04:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4221fc4-3778-3195-876b-12644af07cdf | -14.35719 | -51.87108 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c81da5a1-53ba-3e43-9555-62082623c631 | -11.24669 | -54.82335 | 2026-08-18 04:40:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f0223e9-1a59-3750-a023-46e34f374c2e | -16.23771 | -57.65301 | 2026-08-18 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 48ff7792-f135-3877-b73d-87283aef17e4 | -10.11974 | -54.28211 | 2026-08-18 04:40:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ff84cf8a-eb69-30b6-9cad-67ef8c29c08f | -15.30278 | -56.44151 | 2026-08-18 04:40:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e5752611-3a4c-343c-8ed0-8fd307815903 | -14.49646 | -45.67319 | 2026-08-18 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c32035fa-6f29-336c-88b4-ea384476094e | -14.17387 | -52.89249 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| aaf509a0-fbeb-3589-aa26-be5918b301ee | -11.82285 | -56.59895 | 2026-08-18 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b308056-1054-320c-a0d4-c425454dc955 | -14.49939 | -45.67776 | 2026-08-18 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc9cae01-4b5c-348a-aed3-42f6b6406604 | -13.56172 | -51.69518 | 2026-08-18 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bb03634d-3d07-3e9e-84ae-1694e0e80f5a | -14.3612 | -51.88246 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 67751f33-c51b-396f-a6c2-6707a3aa56cc | -12.76653 | -48.42639 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9e41054-5116-3c8b-971d-ba9e6bb4fef8 | -12.76095 | -48.42583 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88e027b0-3656-3e81-9a65-faa5f05ecee4 | -8.89751 | -60.60054 | 2026-08-18 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e830bfd3-7976-32a1-a05f-6c08ed7afe93 | -12.71954 | -48.49221 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6af5a063-a0e9-333c-999c-424e3046ed19 | -15.24462 | -56.48147 | 2026-08-18 04:40:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 37f592ed-5689-32e8-bb58-36c99fb7d0b5 | -15.91713 | -56.49819 | 2026-08-18 04:40:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac5c3e46-f487-3808-997d-92ca8fcb244f | -11.35979 | -46.40104 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33cbb1ce-4850-3f24-8f62-13e23630f981 | -11.71548 | -54.6312 | 2026-08-18 04:40:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| da722982-524f-36d2-a589-3d1cc7d6cf3d | -17.1065 | -46.5648 | 2026-08-18 04:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5d8ff789-d57a-3761-9e2b-cc8649a9e719 | -16.22752 | -49.70604 | 2026-08-18 04:40:00 | NPP-375D | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90d14ef0-c451-38c9-b75c-d2fd91e9b978 | -14.15907 | -52.91364 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| adf2a764-ebfb-3bc3-9c7a-7b749ebd6862 | -13.78958 | -53.84769 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4378a673-a081-3773-8708-ee084ad91d77 | -13.42677 | -57.07141 | 2026-08-18 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ac7854f-e574-361d-913d-4abef3237d2b | -14.12707 | -53.65639 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e3b0d8bb-ecdf-3062-87b0-a52d0da9cedb | -14.35881 | -51.92669 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efef0df7-52ed-3922-9a58-6ffc4c126583 | -11.53057 | -46.64108 | 2026-08-18 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 77c2fc3c-c87c-38df-9b6c-1e7816d45f8b | -11.13199 | -47.28033 | 2026-08-18 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f6bff6d6-5a41-3948-b078-f5e28dec1663 | -14.16901 | -52.92637 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0be3d164-fbae-35a6-90ee-ca644c486226 | -12.7671 | -48.42282 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3190536d-ce0c-3a59-84c0-0b4b653dda9c | -12.54145 | -47.84488 | 2026-08-18 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 707bd15e-ee89-39ff-9420-67968a2a0fb9 | -15.25017 | -56.49303 | 2026-08-18 04:40:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 29c6d30b-41f7-3dc5-b796-61501027a0a2 | -11.1259 | -47.27575 | 2026-08-18 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 93586520-1f17-3810-834c-e3df7cb551a8 | -9.00852 | -60.50624 | 2026-08-18 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be034701-555d-3244-a728-38ee336385a1 | -11.13973 | -47.2744 | 2026-08-18 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e47a6f6-2507-369c-ac6d-1c3da949e962 | -14.81747 | -46.63869 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ce1d2c2a-7c45-39af-83f0-219eb359092e | -14.16181 | -52.89804 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de6eebaa-a184-3503-8457-471c6aba721d | -11.10065 | -49.90912 | 2026-08-18 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1ff4b08f-67c1-3534-a281-1bdad56f333e | -14.83786 | -46.64238 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b979705e-16bf-3fa7-a033-7cc5c3646c46 | -14.49587 | -45.67723 | 2026-08-18 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5749e73c-d351-3c16-95da-3802a02a0425 | -14.35852 | -51.88513 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5299dea3-deeb-31d7-8cc9-5cd88d40635c | -15.28562 | -56.42672 | 2026-08-18 04:40:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c9dc897-e17a-3041-b134-836ec980ac73 | -14.28817 | -47.20606 | 2026-08-18 04:40:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3f18a24-6614-32a4-bd37-2a77d66c9598 | -14.42942 | -51.89354 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aba7354b-1ba9-37c1-9d5a-8b19f035a639 | -14.16598 | -52.92053 | 2026-08-18 04:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5d53ba9c-d762-350b-b417-248f582ded35 | -12.94354 | -56.64471 | 2026-08-18 04:40:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| af471b47-d6e5-31f0-91ca-8f8fdf7b9064 | -11.12037 | -47.26765 | 2026-08-18 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32e8938f-15ae-3cb7-ab29-f188eedc6735 | -8.8962 | -60.60715 | 2026-08-18 04:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f771141-f565-366f-8f45-8891024204ce | -15.92373 | -55.54573 | 2026-08-18 04:40:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4c28f37c-3d7f-353f-a5a5-1ee62e92a38c | -13.42105 | -54.39262 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b72cfe6-ab4c-3aa1-bcaf-9c5c15012400 | -14.3567 | -51.91699 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ddfcb73-698b-3fe0-a9ee-ae81e2a3c2cc | -14.45493 | -51.83369 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8dc82a3-d8a5-3936-b93b-b504710c555a | -13.66739 | -52.1972 | 2026-08-18 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1d984d8-974e-3656-ad4e-ae2e9d67c25d | -14.82144 | -46.63555 | 2026-08-18 04:40:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ae0e2e97-632d-362e-b937-e120bc91115f | -11.11437 | -46.49128 | 2026-08-18 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 104d83d3-8f70-3be9-b05e-bb005280daa0 | -16.24654 | -57.66221 | 2026-08-18 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2482e351-1ba5-319b-9a5b-a2295c58ee99 | -11.10414 | -49.90972 | 2026-08-18 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9fce43f0-12e2-3311-9e41-298facb67390 | -11.33762 | -45.93058 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6239ec17-424c-31cd-b860-47a86651286e | -13.57735 | -51.78127 | 2026-08-18 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 174f4a10-dad8-3197-9a88-6900b9ef4913 | -14.34983 | -51.93426 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5a186cf8-f4a6-39ac-9925-a4e155d70e3f | -14.35612 | -51.86768 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de35b07f-fbb0-376a-866d-c3dcf98f3d13 | -11.36201 | -46.38661 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fee3cacc-d53e-3c70-ad8e-143c8ba5c764 | -11.30313 | -46.33646 | 2026-08-18 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a56237f-05e5-3b65-bf2f-33814361efe7 | -14.25493 | -51.92316 | 2026-08-18 04:40:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e8c8fbd8-6679-38a9-aaea-29753b70b40f | -13.58106 | -51.78196 | 2026-08-18 04:40:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| efa00048-9a08-3e88-8598-087e2b65640d | -12.76595 | -48.42995 | 2026-08-18 04:40:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 114c83c7-b2b0-3af7-96a6-56e8cd0dc435 | -14.0344 | -53.68909 | 2026-08-18 04:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f5925613-8e89-373a-9c7d-30e7ce0e7b70 | -13.28549 | -48.69564 | 2026-08-18 04:40:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README32.md)
