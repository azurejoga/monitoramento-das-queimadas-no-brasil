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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18586e08-c75f-352c-92fc-b982c3022d72 | -11.42035 | -55.07476 | 2025-10-06 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a23c5f6f-7e4c-362a-b7d9-ff8581355ab6 | -13.05165 | -47.9049 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c77253d-40dc-34d4-9513-d037f9e00733 | -14.68754 | -48.38825 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2c4e6f3-0370-3040-b36d-54975f42163b | -13.36465 | -48.03566 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b55b53a2-5fa8-3d70-aceb-44c3b9366d7a | -13.27119 | -47.80719 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85996acf-6683-3abe-8861-a77df54b4816 | -9.4232 | -49.21801 | 2025-10-06 04:27:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dff268e5-db00-39b2-8909-8975d9c36b70 | -13.3294 | -47.5639 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 222346db-f48a-3948-8788-232d9b96b0f8 | -13.10298 | -47.92759 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26a7f73e-198e-3efb-9e58-a98d042e0d1a | -14.6293 | -52.51459 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ee9a94e-897e-303d-b07d-85066a96dbaf | -15.56912 | -52.46445 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| d244478e-a476-3b79-8beb-6bee809535f7 | -10.80997 | -48.81617 | 2025-10-06 04:27:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 706ef774-3158-3c08-8b9a-e70a313fbd44 | -14.68758 | -48.36646 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de40cc77-3a2a-3999-8bba-a86c40ffd5b8 | -11.85522 | -45.05935 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5169d00f-5134-3fee-8ed7-c789557a90e0 | -15.65032 | -43.67174 | 2025-10-06 04:27:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba24555f-959b-3465-ac9b-a3b10d836b7d | -14.6685 | -48.27253 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab9fc86f-cdad-31f7-a27a-65bdb7536374 | -15.7692 | -46.25615 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd8ee7e1-8be0-36ac-a31d-886cd72d70d8 | -12.57125 | -48.14691 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15211129-7486-3852-9fd2-6f39a7fd6573 | -11.6443 | -47.02567 | 2025-10-06 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35c76bc0-41b0-3b05-80bc-edd41c949c99 | -13.12158 | -48.00283 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d8d020e4-d591-3303-958e-2195e8a9c6c3 | -11.03215 | -47.78721 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ef180b1-72e9-3191-a4df-fcea31370dc9 | -14.66831 | -48.38144 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e413f83-eba0-3153-89af-f8c46db992b4 | -10.03947 | -52.07052 | 2025-10-06 04:27:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 470eb535-95f6-36eb-a764-d02731910110 | -16.00452 | -50.95217 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 333ccf32-6595-354f-b9ed-6ed3d5168308 | -11.80695 | -45.12083 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b89dddc0-a64f-374b-9ab7-99ce070438ab | -12.37048 | -46.50418 | 2025-10-06 04:27:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da91a607-7894-3423-a3d8-a1f3aff9230a | -11.67257 | -47.47856 | 2025-10-06 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90bebf59-ba35-383a-b82c-215030dc0d84 | -11.95069 | -51.47894 | 2025-10-06 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f333c13-956e-321f-893e-a031b3aa2c93 | -12.58335 | -46.73594 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc990ecd-3bc5-3492-aa93-599cd3b3dd88 | -11.0226 | -46.53726 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f729f47c-b86d-31c7-8735-156cf0136cfe | -15.93138 | -49.00228 | 2025-10-06 04:27:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5936551b-043e-38c5-8e80-b1432ca8ee36 | -10.36481 | -48.15107 | 2025-10-06 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56245fb6-644c-34b6-9e32-ea8b0207dfb1 | -14.36342 | -47.71809 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| c8aee52e-6358-374b-aa6a-6fa0872cf392 | -14.32871 | -47.65789 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eb86a8c0-9e45-39cc-b09b-a3629ef373a2 | -13.29586 | -48.08585 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 575bc8fb-e9bb-33c5-ac4e-3fd503f3eaa9 | -13.62845 | -48.71445 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fdf9d4ab-6078-3069-aa28-25f22b110132 | -11.91815 | -46.23448 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1a2e67a-caf0-35f0-bb96-664c57f8dfb8 | -11.4484 | -44.95597 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99d98771-5337-34a1-81d1-3cb6cdd1d510 | -8.51142 | -54.59624 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c6a60f10-5f56-311a-a02a-c6354f2a5d47 | -15.22266 | -49.28407 | 2025-10-06 04:27:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 921fb3e7-5795-370d-bc5d-8e83b64e3c16 | -11.45916 | -51.52724 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6ef29ba-7222-3e0f-b2f8-61fbd22ef1b7 | -15.68129 | -46.28267 | 2025-10-06 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7edfe1ba-dd68-316a-8789-63b7a1a035c4 | -16.05957 | -50.92123 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b5370ef6-13cd-3a5a-be1d-f9e934f5346c | -10.40287 | -50.32462 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b68f3965-a234-3e4e-942b-cfe178421b80 | -11.01983 | -46.5332 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46d36903-c204-31cd-8825-2e26eabeb1d2 | -15.60379 | -46.94213 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4d63876-6b26-373d-aab9-167166facd63 | -13.25866 | -48.49255 | 2025-10-06 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fda9f1e4-26da-30e1-833c-209d9f154237 | -14.56208 | -46.67675 | 2025-10-06 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 00e3742b-bb24-3db5-9276-193dd03d4595 | -14.63519 | -52.52573 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ca55294-1590-3762-8842-3d112b89f80e | -11.10558 | -47.20788 | 2025-10-06 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 989299af-81ba-327e-a452-dcb1310426bb | -9.33888 | -54.5234 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 837867da-dea2-345e-9619-e8fd123bbbc9 | -8.61115 | -54.96882 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 303683e1-fd83-3861-80f5-c41c5c73a98b | -15.2936 | -46.32298 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55e937d5-eef3-3a81-9be1-df14e6262a2f | -14.56318 | -46.66935 | 2025-10-06 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 598a43d9-d48b-3b85-a0a1-f92fe2bd12c3 | -13.60033 | -48.69884 | 2025-10-06 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46049af4-8e24-3c75-beea-42905c19ea5b | -10.6786 | -48.46902 | 2025-10-06 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98df276b-d2ca-3660-bbc0-4c065255fe5d | -11.87862 | -57.82065 | 2025-10-06 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b4f6ecf-c3be-340f-8968-c7559ff6099c | -16.2924 | -45.24441 | 2025-10-06 04:27:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18663906-9870-3509-bd3d-6511b80ccb20 | -13.6208 | -48.6985 | 2025-10-06 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5dbc497d-4901-327c-987b-3cc2991826e6 | -11.80518 | -45.08468 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c59535a1-6b05-3c00-95e6-8a36d86bb00c | -11.77981 | -47.94498 | 2025-10-06 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| deddc9d6-bc9b-374d-a5ea-23907ae01a72 | -13.12214 | -47.99931 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c09196b3-cc0f-3c26-bdb5-23c35ad3efb2 | -9.68247 | -48.39495 | 2025-10-06 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f406d646-3ee0-3ad7-8f33-d33d157a0c06 | -14.34362 | -47.71474 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e3fae724-bf0f-31ba-b230-0fa8a11530f1 | -14.92056 | -46.82797 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a538555e-f92d-3c3e-86fb-0b80889b0ce0 | -15.49212 | -47.91984 | 2025-10-06 04:27:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0bc35ab-4b7b-378a-b243-ab148897fcf9 | -16.06099 | -50.93421 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d502cdc9-51b3-39f9-955a-76c24a1c68ac | -13.35602 | -47.19457 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 425b7492-940c-3985-acd7-e89d52724c39 | -13.08595 | -47.92843 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48840283-a311-330f-83b2-e1beb04c0164 | -13.3317 | -47.17606 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3fa7d60-40e0-3b82-88fe-2bd314a85c65 | -11.52405 | -47.68777 | 2025-10-06 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b555993e-98fc-30fd-aca4-52e88b82017b | -16.02585 | -51.03807 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9951adcb-b6f5-384b-90a6-58cb8e07c4d3 | -16.02593 | -51.05908 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ea916c38-b978-3565-a3b0-b83a6fbc31a5 | -13.48989 | -47.23077 | 2025-10-06 04:27:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8257d69e-46fa-3126-b6a6-f68c408929ba | -11.83891 | -45.07318 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 41c6760d-0d45-3cc8-bb8b-397aafe7107b | -10.62209 | -45.00636 | 2025-10-06 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d77af97-7964-3c59-81b0-f7c3df4009b4 | -11.82745 | -48.87981 | 2025-10-06 04:27:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dbbd9ff3-6853-3537-b2a6-655ae5d5fe5f | -14.36617 | -47.72217 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 7b53d211-0ddf-3a4b-9ab4-e0b2b2b8c0dc | -13.36049 | -47.2537 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f09ca63-230f-3a6b-894a-2bc799511f44 | -11.04922 | -47.76487 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1ca4953-67f4-320c-b285-34aafbeeb27c | -15.3578 | -47.99678 | 2025-10-06 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e08c06a2-b91a-3831-bf32-48b9d63c4c3c | -12.48164 | -45.55542 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 77936837-3bda-3d25-a674-504f36ab52b3 | -13.09857 | -47.86926 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97576755-7508-3130-8768-ce20f1948b65 | -11.68062 | -45.28767 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97505c9b-2e07-31bd-ad5d-d51575c64d1e | -15.91505 | -48.82702 | 2025-10-06 04:27:00 | NOAA-21 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05bc92d3-98b5-3389-8f89-6219ea6f09d1 | -9.24921 | -51.81313 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fbe0f760-a876-3343-a76b-3d3ee1dbd7c6 | -8.88078 | -50.89592 | 2025-10-06 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 199eac0d-0f53-3fa1-9674-f6e4600b0d42 | -16.02797 | -51.04681 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 26595715-ab46-3db9-b144-3abde5ecc9fd | -13.08869 | -47.93248 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8de16700-c723-394b-8e23-aaf92ac88855 | -10.47354 | -49.09053 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1dcf4ee-dc4e-3cab-b744-859436f3544f | -11.02314 | -46.53372 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 920f5e4c-4b1c-3316-8c20-e37dfbe3fe0d | -15.59104 | -52.44923 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db3aa24d-f47f-36d1-a4f9-60dbc7a8cfbb | -9.62348 | -50.55495 | 2025-10-06 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 134b82e2-aeb6-3f74-9ba1-600074dde539 | -9.67394 | -49.94855 | 2025-10-06 04:27:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 111d6362-2040-3cbb-96b6-96d60a29bf6a | -11.04978 | -47.76137 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 316d8238-a51c-3176-aa2a-20beae0b791d | -14.92502 | -46.82118 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3484c02d-cd09-3665-b3f5-f79252f3e20e | -11.05307 | -47.76191 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecd24a0a-89f3-3679-a799-5c79b62a3918 | -15.75144 | -46.25721 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 983f3aaa-2470-3fe8-8f34-99148c4d3282 | -14.69362 | -48.37109 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3af2d75d-11a6-3484-b4bb-473045c861d4 | -12.48277 | -45.54776 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b9c2cd7e-1d02-3b63-921a-d544c7b6a588 | -13.28048 | -47.61737 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README42.md)
