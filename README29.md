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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82df8a32-134b-33b8-8a64-e4896ee858b9 | -9.48332 | -68.49872 | 2026-09-11 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dcc7a24a-f9b6-36f1-ad8f-554c96ef6bde | -8.9899 | -65.40981 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 592982c0-341d-3d98-8c71-8a386740ba93 | -9.08427 | -65.48682 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87bc3601-c963-3248-acdf-fcb6f58acc30 | -9.37554 | -55.9654 | 2026-09-11 05:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9806752a-59cc-32dd-bd78-4b1bba963cd8 | -11.41478 | -62.12582 | 2026-09-11 05:29:00 | NPP-375D | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b9bc091-0c6d-3af2-bd1e-37e6e4b907af | -9.07406 | -61.03553 | 2026-09-11 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e94d1ade-d051-3808-ae82-975b30cead83 | -8.64618 | -69.79362 | 2026-09-11 05:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79b4f121-15ff-379e-9c25-c0a75f63f582 | -10.63787 | -46.13152 | 2026-09-11 05:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2cd96ce1-344d-3f73-97a9-35bb1bd4d587 | -9.1822 | -68.20297 | 2026-09-11 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22b4b58d-227c-3cd1-90e2-8e296c86018b | -11.81102 | -60.45842 | 2026-09-11 05:29:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56147fe0-54a9-389b-8e48-d29a9ecdd9c0 | -9.31939 | -68.19932 | 2026-09-11 05:29:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a0d552a2-c58b-3d80-9d32-8e306dfad9b8 | -14.58446 | -48.85114 | 2026-09-11 05:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a738b04a-3c51-3768-baf0-c15266ae42cc | -9.75891 | -64.94245 | 2026-09-11 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8af0ea62-79ad-3e19-84c1-c45a744d337d | -9.17204 | -49.94746 | 2026-09-11 05:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddb426c6-867e-3414-8e7f-8bf92ef575e1 | -14.61703 | -48.84856 | 2026-09-11 05:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eabaa53e-aa82-3b6f-abd6-3b918c55f48c | -10.22462 | -68.08606 | 2026-09-11 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c246cf96-51e0-3b66-bf42-91bd34d35291 | -9.8923 | -67.60464 | 2026-09-11 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f69a3588-defb-3acd-8d32-4429f4528b25 | -9.07804 | -61.03245 | 2026-09-11 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc63db99-0b44-3874-a305-a0a67a8fc60e | -9.1585 | -65.807 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3e494e6-d2cb-338f-81c4-b1e21d61d75c | -9.37181 | -55.96478 | 2026-09-11 05:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 671ff63f-94d6-3242-8d6a-6e8001bd7283 | -10.46556 | -48.66 | 2026-09-11 05:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e754af4c-ce6b-3adb-a9f5-c1a6ac58b8a1 | -8.63657 | -66.50541 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9badf0b-1c29-3374-ab4c-17d914b22e3e | -9.08852 | -65.48758 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cf7ea07-a1c0-34d1-9ec5-7c18615cd263 | -9.43653 | -68.26113 | 2026-09-11 05:29:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3adf8df4-ea3e-3966-95f2-e15c2a1df10f | -8.63032 | -66.51406 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 94889550-d10f-3741-84a7-c7015cc642ea | -8.64034 | -66.51098 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6098603a-7847-3e21-acd9-f8f0ab3ecad9 | -8.9355 | -66.84882 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cf18e37-9844-38b0-98c7-18abd599bff0 | -9.4107 | -65.93439 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4239aaf6-cc5c-305b-903d-b280acded5a5 | -12.15935 | -64.13861 | 2026-09-11 05:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8ffa08ba-77ec-34a6-80e0-30412fb9f2aa | -10.29544 | -67.27814 | 2026-09-11 05:29:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9ef9af4c-1fa3-3c49-8e95-85920005a6b6 | -9.03656 | -65.41812 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a5882f56-e8e9-39d3-9aa4-f8bd67237da2 | -9.14448 | -67.81397 | 2026-09-11 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e7259aa-9007-38a2-a9a6-7f84de700d69 | -9.02453 | -65.41186 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab359f9a-5072-3c4b-809d-bfe555be9564 | -11.81434 | -60.45897 | 2026-09-11 05:29:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 240739a5-2ed4-35c7-95a1-e4ff368bdaba | -9.40765 | -67.41116 | 2026-09-11 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eca3089f-42e5-3a13-897f-3a3a1d6ba6c7 | -14.6026 | -48.86288 | 2026-09-11 05:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 36085e94-af3f-38e4-a69c-44faf4de9008 | -9.4242 | -65.85931 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eb4fcc5e-d8f0-30e8-a975-16ba27adfa73 | -9.216 | -65.57954 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f42e8122-1c81-32e1-b649-267e3dc4cf63 | -13.48625 | -48.5592 | 2026-09-11 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 16f0f522-322f-3314-a028-28cf98dee2f2 | -10.6387 | -46.12435 | 2026-09-11 05:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b590835-7de0-3b77-bbe6-d58c761df8b2 | -9.02029 | -65.41109 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8837f68a-66e1-3366-bd40-7519922a1031 | -8.53208 | -66.9903 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb10312c-d209-384a-a1bd-09b5858442d4 | -9.10069 | -67.68891 | 2026-09-11 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7ada94b-55cc-35b0-bac9-0e6a76d93a6c | -10.36645 | -48.14072 | 2026-09-11 05:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ffcf8bcb-64e9-3b33-9935-fff8b07be371 | -9.01181 | -65.40958 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6877441d-e4c0-3866-9768-eb840d210b51 | -9.06653 | -65.48778 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e42f5272-ba8b-3848-940d-4913b27856d7 | -10.67465 | -49.08017 | 2026-09-11 05:29:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9570edaa-cbd8-37eb-b047-2c9bf0f1ae0e | -9.75359 | -64.94898 | 2026-09-11 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62ba8e68-805d-3d34-a7f2-90b2f10f031e | -9.34676 | -65.67708 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f77bf48-ae1d-3304-9207-f6d282458c0f | -8.50654 | -50.14989 | 2026-09-11 05:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d6c7460-2050-3ba2-aa76-f377807f4068 | -9.13951 | -67.81305 | 2026-09-11 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06bca08b-9b92-31a1-bfc2-71d2bed0258b | -10.52755 | -51.3485 | 2026-09-11 05:29:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19c01b97-4d31-3b8e-8f0d-67e644f33a7a | -9.17599 | -68.20813 | 2026-09-11 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0ca548a-c763-3d64-a9c0-eaba216500b5 | -9.03369 | -65.40942 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 391c2af4-2748-3f6d-bf60-4ee28bafc287 | -9.43597 | -68.26416 | 2026-09-11 05:29:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8412b74-48d3-34cf-a6dd-66e5e8da841d | -13.4992 | -48.55959 | 2026-09-11 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3da7be49-39a3-3d83-bab7-29a40115eb3b | -10.05539 | -46.28247 | 2026-09-11 05:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 41774ea0-10f9-34fe-b74a-c56e7614863b | -8.9885 | -65.41775 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3eeece2-bbb9-36db-b520-e6b47487b0b3 | -9.15626 | -49.98248 | 2026-09-11 05:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b366d02d-420f-3bdc-b215-5bdb093bb50d | -9.03588 | -65.42208 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0a55ad43-3b30-3ddd-8eb8-17edd126ab6c | -9.45983 | -68.83131 | 2026-09-11 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d5b1312a-6bb1-3b92-9a13-d79d3e13d539 | -10.05833 | -46.27695 | 2026-09-11 05:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 374e8cc0-9895-3f19-8aad-c4ba6cff9f82 | -7.84947 | -56.58588 | 2026-09-11 05:29:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 434793ef-854e-3737-93f6-6df1882e5414 | -9.14203 | -64.39676 | 2026-09-11 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce47fb4e-928c-351a-bad4-a931fc598069 | -9.00695 | -65.43742 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7225a47a-92ac-3986-9b57-3a3113b9ef03 | -11.81214 | -60.45136 | 2026-09-11 05:29:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf2cdc29-2f60-36a3-a4d5-f59573fa7447 | -9.03793 | -65.41019 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5143fff4-52d0-371d-97ba-38778aeeaf9b | -7.90626 | -56.63442 | 2026-09-11 05:29:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88b0d4f3-0371-351f-9a97-88d3e11a24ce | -9.18675 | -68.20697 | 2026-09-11 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4348939e-9246-34fe-8008-5a7d2ca102e4 | -9.7602 | -65.03266 | 2026-09-11 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcac7465-8f5f-3266-bc15-8444e2ac3613 | -10.47966 | -48.64713 | 2026-09-11 05:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39f9c096-d361-3c61-80dc-e9f921bf87db | -9.18166 | -68.20599 | 2026-09-11 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16a10d65-15b6-3cfb-9bd4-7188ef5b4426 | -9.03861 | -65.40623 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 467e0f45-c95c-3786-bdff-577885912461 | -9.18729 | -68.20398 | 2026-09-11 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2307ae04-515a-3fe4-8292-35d248b76227 | -13.47967 | -48.55352 | 2026-09-11 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 88e6f625-401b-3d2b-b041-054c0fa8c156 | -10.4785 | -48.64819 | 2026-09-11 05:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57efff93-9309-39df-a40a-f3d9832fafef | -10.94436 | -54.08988 | 2026-09-11 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3b7c255-c158-30a6-9ab4-ee4f8b2edbf6 | -7.84592 | -56.58532 | 2026-09-11 05:29:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15fc039d-5c8f-38f2-a6a0-5d2539607f4c | -9.71031 | -65.07697 | 2026-09-11 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a29fc20-f21e-3411-ae9e-1dd7290be5a0 | -11.81378 | -60.46249 | 2026-09-11 05:29:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3cec813a-6114-3c65-8009-bd549fb1179e | -14.58831 | -48.8563 | 2026-09-11 05:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 35a40bac-9cbf-39f5-973f-f374077f0189 | -13.49323 | -48.55477 | 2026-09-11 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 99121644-2705-32b8-b161-5c02478ee4ac | -10.63703 | -46.13883 | 2026-09-11 05:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99e8532b-e7f0-37b6-add3-001f50ae0939 | -10.18268 | -59.63218 | 2026-09-11 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 914919e7-6b8d-3105-9d2c-dfef41120395 | -12.15188 | -64.13725 | 2026-09-11 05:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90a66d7e-8a41-3f55-8072-23238da797a7 | -9.41061 | -65.85767 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a7ea902-41c7-3fc8-9626-637e2238c59c | -8.71196 | -49.62 | 2026-09-11 05:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17d57f25-3e15-3332-bef4-c185eeef9d9f | -9.8696 | -60.21843 | 2026-09-11 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3045f4df-92fb-38fb-b193-87d9d7a39627 | -8.63492 | -66.51491 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e827df8a-d4ea-3e92-908f-78a534efb178 | -9.34901 | -65.67627 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 111eecc4-4559-3796-94e6-f373655094d4 | -9.37337 | -49.3821 | 2026-09-11 05:29:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44b643ce-326e-3fd9-a66d-6538d9d82e3f | -10.60012 | -60.78635 | 2026-09-11 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3f769bc-6804-3e07-9e1f-b6a96f5a71c4 | -10.18324 | -59.62867 | 2026-09-11 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ea7a0fb-646a-334a-9a59-e4bb8f9a1756 | -9.1811 | -68.20904 | 2026-09-11 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 499945b5-1ac7-33b2-a5e1-2b5c489233b2 | -8.63408 | -66.51969 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da0cd087-81e0-3b10-be05-30a4f900ea61 | -12.77258 | -62.0317 | 2026-09-11 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb1dd861-2a30-3cfe-b8b7-1bb11f2fa699 | -11.39944 | -55.24497 | 2026-09-11 05:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f23f74d-66e6-33a7-bcea-ba2024668d04 | -14.60159 | -48.85316 | 2026-09-11 05:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c0459a7-b8f9-3fb3-b8d3-be1cd910fc6b | -9.75612 | -65.0319 | 2026-09-11 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 871736a4-ed3c-3891-948a-0d44cd01a3b1 | -9.01269 | -58.98845 | 2026-09-11 05:29:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README30.md)
