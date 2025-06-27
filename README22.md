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
| 0591e84b-b25e-37cb-99cb-8950106e43ea | -9.36085 | -58.85054 | 2025-06-27 04:49:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45c8276e-e18b-3ce5-a7f5-46e9c7668617 | -8.39924 | -46.92233 | 2025-06-27 04:49:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f88b565-a14c-3d41-9757-8f9d8717782f | -10.82353 | -53.74273 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a85aeb59-569c-356b-88d8-dbf50437efe0 | -9.87491 | -48.04896 | 2025-06-27 04:49:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2bb164b6-3c06-3e68-b313-608c95d68e07 | -11.17966 | -55.91292 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a17c85d-5bab-3366-b373-41d4957a35a1 | -11.67552 | -46.72728 | 2025-06-27 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 968af791-4bcc-358e-a976-1726543ae4b4 | -12.5257 | -57.21061 | 2025-06-27 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 809650cc-43be-3dde-bcbc-122593ef4a10 | -10.27405 | -47.60712 | 2025-06-27 04:49:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 922fd20f-6d8f-37f3-8cac-9892fed203b3 | -12.02659 | -47.77738 | 2025-06-27 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0e18cd4c-ce76-3a16-8d6d-8c4d4fd289a8 | -9.11811 | -49.44224 | 2025-06-27 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3edf8da2-fdcb-36b7-8d15-1a3b54d21b80 | -10.29901 | -57.12959 | 2025-06-27 04:49:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9b34bef7-c2d5-3ef7-8fa9-96e175a3a8a6 | -9.75691 | -48.04226 | 2025-06-27 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0dd4e0d-9552-3975-b81b-7c82e5970c59 | -12.78883 | -48.7308 | 2025-06-27 04:49:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dbc2a0c7-eff1-3eab-8474-cba85bca3afd | -11.57615 | -52.11612 | 2025-06-27 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 05732d0f-7e4a-3f86-b473-d82b3e7fd004 | -9.79175 | -48.56555 | 2025-06-27 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e862befb-c204-3d45-9e34-0b952891b3de | -10.17032 | -51.65259 | 2025-06-27 04:49:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b2697d8-1cbc-339f-80d8-720a70df34ca | -11.17719 | -55.92416 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49bf648f-0b1b-35ce-837b-aa6bab23bbcb | -10.0294 | -54.32928 | 2025-06-27 04:49:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b560475f-4812-30d3-ab84-26ae2c28da95 | -9.07249 | -49.42756 | 2025-06-27 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 20f5e0f2-6ab3-3246-96d1-7f3bf222be46 | -8.62412 | -51.5713 | 2025-06-27 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6caaa2d5-129f-3339-ba28-b254021b3408 | -11.74275 | -54.71554 | 2025-06-27 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f88a2a13-bcd1-3676-8720-dcbe28537cd6 | -8.47909 | -48.2629 | 2025-06-27 04:49:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ebbe5942-6b3b-3bd8-9748-1146ef67a3b7 | -11.50318 | -61.82769 | 2025-06-27 04:49:00 | NPP-375D | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a85cb917-c0f1-3b43-ac1b-74ace902d267 | -12.04791 | -48.07711 | 2025-06-27 04:49:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| edb253ae-5cb0-32ab-a2d0-fe69eb037e7a | -12.65514 | -54.10521 | 2025-06-27 04:49:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5256792b-1a28-3c1d-96d1-b77d025c39eb | -11.81948 | -47.52953 | 2025-06-27 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f063f9d-7c30-3f9f-8601-f029289e24e1 | -14.2953 | -41.60123 | 2025-06-27 04:49:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 4c923bda-c10b-346f-a54f-4d9bc1246e4e | -11.82201 | -47.54011 | 2025-06-27 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 48de47a6-0ccc-37d9-ba16-ecbb5297b6cc | -8.37761 | -46.96284 | 2025-06-27 04:49:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f82e826-c59d-3078-b16e-b678764138c6 | -10.17087 | -51.64909 | 2025-06-27 04:49:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea8a8aa2-b854-3d3b-9af9-74c7e2bfa5bc | -10.30369 | -57.12672 | 2025-06-27 04:49:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef9de68a-6583-3539-aa39-04c1ca39c011 | -12.02297 | -57.08294 | 2025-06-27 04:49:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56319b36-8fd0-3f8e-a82b-af059355e39b | -11.18478 | -55.92765 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31d8057b-4035-3213-aef3-4004b02eb517 | -11.17732 | -55.92636 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d1aad6b-1fd3-3c3a-a384-558e69906566 | -11.1742 | -55.91905 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df0f4f3a-2eb4-377d-9f58-fe4dda5a8738 | -9.19723 | -50.49968 | 2025-06-27 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20c6309c-41d9-3c0d-9fce-099de5fbf53b | -11.49806 | -48.07791 | 2025-06-27 04:49:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c11b6bca-2f70-31db-bc56-ae5987f8ff92 | -10.85453 | -54.04016 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56241685-67a1-3d32-ab5d-0bcd17538268 | -10.8614 | -54.04134 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 831f65e9-f1b4-31b5-bc55-d7a1abf38d72 | -11.47084 | -48.53033 | 2025-06-27 04:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 871ad9ae-666f-308c-86ed-7747ebccd87c | -13.5878 | -45.25409 | 2025-06-27 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cced56a-9f51-31f1-b0a8-ebdbfd4e3689 | -11.5756 | -52.11964 | 2025-06-27 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 8ec2a5fc-06eb-3878-b64c-ad2a2c0aec69 | -8.34616 | -49.2316 | 2025-06-27 04:49:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc12e88a-5a58-355d-ae02-ef261c68f0fe | -11.10579 | -44.52108 | 2025-06-27 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59559e1b-cc3d-3a9e-add3-c35866fd0657 | -11.60659 | -55.54367 | 2025-06-27 04:49:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c6280ae-4a91-3241-b167-688d8426849b | -11.18465 | -55.92545 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a8e4279-87aa-367a-b86a-d720afadfbc0 | -10.54204 | -46.35421 | 2025-06-27 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 349dda7c-1af3-3c3f-b8f3-eaf98b46e83f | -10.30651 | -57.13471 | 2025-06-27 04:49:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2bd2d20a-98a9-3d4c-9eeb-dd6b4e4813df | -10.87561 | -53.76677 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38c6e07a-3855-358e-a058-cad6fe04abec | -11.81235 | -47.52267 | 2025-06-27 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c0365d8-7cd9-38cf-910c-516b2d6c5b59 | -10.29963 | -57.12599 | 2025-06-27 04:49:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0a947d7-6ec5-329a-a742-a008983ff658 | -10.30245 | -57.13395 | 2025-06-27 04:49:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eef6c48c-09d7-309f-b979-5ffdd8f7ce8c | -10.82973 | -53.74759 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55528a5a-41ea-3bce-86e8-c1ba4b4e723f | -11.57781 | -52.10555 | 2025-06-27 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 8c4467ce-b107-3953-95e5-10657a08620c | -12.03051 | -47.77796 | 2025-06-27 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 341a939a-525e-3179-ac2b-11ba243ccb93 | -14.23954 | -45.50263 | 2025-06-27 04:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3fb13ba-1a07-34ac-b582-3d5ffd151203 | -11.57283 | -52.11558 | 2025-06-27 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 09417dd6-6976-3d01-847e-d007180b4b0d | -12.01106 | -47.16736 | 2025-06-27 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36377794-4610-33cd-a2c6-157bdc47ad28 | -11.35671 | -44.89455 | 2025-06-27 04:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 587ecf79-0a64-3091-9eac-32475e3355f5 | -8.62025 | -51.57425 | 2025-06-27 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 59a37307-149e-3ca7-b59b-c6a1ec8c14ac | -11.8036 | -47.52723 | 2025-06-27 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 174b322c-b416-327a-8ac8-f86279bb2331 | -11.77728 | -55.02388 | 2025-06-27 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 132f9225-b896-31d7-93ac-49162206bb78 | -8.48638 | -48.264 | 2025-06-27 04:49:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4c95f6ec-67a8-3ea1-a253-2be4dcc6bd3d | -10.24366 | -47.68143 | 2025-06-27 04:49:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e8167ba5-302f-3d2b-9454-2f9037d1d36b | -9.76065 | -48.04284 | 2025-06-27 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b29d47ae-125a-3d00-b2d0-96fc737ab73f | -13.09944 | -52.29699 | 2025-06-27 04:49:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6d8ab93-8df2-3ff4-ab72-aeb0bda39f2b | -13.10277 | -52.29753 | 2025-06-27 04:49:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 278a6d24-ce4f-3851-88e1-35a241d782b4 | -12.00467 | -47.15599 | 2025-06-27 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4003d0b5-410c-39e5-9578-1321dcddc863 | -8.47753 | -50.27825 | 2025-06-27 04:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ceb9ecdd-c991-3cf6-827d-32dbc50e37d2 | -13.64657 | -46.81305 | 2025-06-27 04:49:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ec39269-f209-323d-90b6-60f96c233a2d | -9.96942 | -48.24557 | 2025-06-27 04:49:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c12d07a-10b9-3341-b2c8-edf3a5d1454c | -11.36601 | -48.70494 | 2025-06-27 04:49:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f74f8710-002a-3d08-a065-07481d18ed1f | -10.85796 | -54.04075 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4afb053d-ea1e-3620-990b-7806564e8f2b | -10.23024 | -56.75513 | 2025-06-27 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ec4ceda-b4ff-3b9b-a606-80d322c6f8d0 | -11.06705 | -55.37437 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 658b4818-6069-3f99-9ab1-833380f7593d | -9.1158 | -49.434 | 2025-06-27 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8e821b8d-2b84-3441-b712-5a8dab9eef5e | -11.05543 | -55.37674 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 29346b4c-f0c5-37e3-ac80-ec497c2a553c | -11.92157 | -54.81322 | 2025-06-27 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59011ef4-6bef-37ad-86ef-0c2ec2eade82 | -11.3617 | -48.70877 | 2025-06-27 04:49:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fda4883b-31ae-323f-9239-0a4f68c38a2d | -11.43645 | -54.47268 | 2025-06-27 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31b0448b-5350-3ff5-af79-b245ed0f8bf2 | -11.17888 | -55.91738 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86d1d9e2-8c02-3c19-b0ce-69ab31bf9b97 | -11.0525 | -55.37306 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 654ef0fc-eefa-3262-b2f1-aef0f434714e | -11.77305 | -55.02729 | 2025-06-27 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9590e911-388f-327a-afe8-228654cd8adf | -8.67341 | -49.95942 | 2025-06-27 04:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8594cbb8-fb09-35ce-8456-37c992bf185e | -8.73695 | -47.98352 | 2025-06-27 04:49:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3ac4a30-de1e-3d0e-aaba-05fa2aa5ee97 | -11.75362 | -54.23043 | 2025-06-27 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45c7455a-113e-3704-8f05-f6dde025fa46 | -10.71062 | -59.12506 | 2025-06-27 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f82b1500-0084-3565-b278-a964a4a4fd38 | -10.81435 | -57.75241 | 2025-06-27 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a70177f8-b422-3e73-8dd3-66a16bf255da | -12.7494 | -44.41223 | 2025-06-27 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5a3cef61-94be-374e-8ada-e4bdf0661a38 | -10.8539 | -54.04396 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48943a99-3d3b-3005-b591-5154028a9e0c | -11.13742 | -53.9166 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5acdf96a-ba54-30d9-8109-ed3b32e2771d | -11.75705 | -54.23104 | 2025-06-27 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e88cda59-c534-37da-9dc0-96ec07177d59 | -12.00415 | -47.15963 | 2025-06-27 04:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5f2685d-8e42-3693-b821-a51ede71b50e | -10.8287 | -54.05544 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f144c38-0f8a-3e82-992a-feddaaf771e9 | -11.44057 | -54.4694 | 2025-06-27 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 73980f23-2640-3b3a-93c6-e0121ecfcab2 | -11.1781 | -55.92186 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32387896-1103-3d16-8149-d1f575e0f316 | -8.37683 | -51.07772 | 2025-06-27 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f2749c7-da3b-32af-83e7-ab93217fa343 | -11.06269 | -55.37918 | 2025-06-27 04:49:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8ddbe66f-c6d4-3330-8d64-259d7216def8 | -8.37405 | -51.0737 | 2025-06-27 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 704ad137-ca27-3372-9b35-bdde0bd0d1fb | -10.8586 | -54.03695 | 2025-06-27 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README23.md)
