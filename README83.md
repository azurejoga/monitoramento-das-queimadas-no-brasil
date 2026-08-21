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
| af77dfcc-3b30-308d-8052-93aad048fc55 | -8.09331 | -51.674 | 2026-08-21 05:42:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4c9ba60-627f-3cbd-8de0-39f2b3d17162 | -6.42353 | -52.75019 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9d7bda0-15d8-32b3-89ab-23bcc8e45f10 | -7.86762 | -63.76729 | 2026-08-21 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e01fc42-5bf8-3709-a144-f8a0f53a916c | -8.56853 | -54.66353 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49b6587b-e976-3ff9-b03e-82ee882cc97d | -6.77251 | -59.45389 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 590272ee-7a9b-3473-923e-ad16eb18b42b | -8.18177 | -54.99265 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6c5e803-2944-39b5-9ec6-708080867782 | -9.12311 | -61.59922 | 2026-08-21 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 877ee66e-cd0f-324e-8bc8-90486aad4ba5 | -9.01029 | -60.44808 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32418e83-08d2-3475-a771-bf07e2b046dd | -6.24714 | -55.42556 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd24ffa0-abc2-3418-bd73-581a19bc7f6c | -6.6542 | -56.34766 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23a5b275-4d56-3084-9ee5-9dde1d32a792 | -6.95601 | -59.05069 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7eed7749-01f4-3030-bf5f-e8a0669b53bf | -6.22242 | -55.48864 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9086975-1d41-39f6-91c4-e871896eba0e | -9.1207 | -60.92468 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bc754726-5399-3bd1-82ff-5701e26cf32c | -10.24064 | -54.37116 | 2026-08-21 05:42:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82b04783-039a-3e0d-9ea6-19acb08946dd | -10.3842 | -61.20685 | 2026-08-21 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a693c39-8da2-3441-ae73-7e32edf40830 | -8.37347 | -62.6983 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 5cc93306-251f-3e7e-9acc-cfdeddd9f18c | -8.16494 | -54.99516 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1155d311-1cc7-3ccb-b5a2-dbc002e93673 | -9.06167 | -60.44142 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f2a42216-8552-3f8d-8604-6da2530bda70 | -5.86778 | -57.6637 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f57a07f-0c30-38c3-911d-9612bc326a45 | -6.17164 | -55.44501 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8744ad65-1a3f-34f6-8266-b8254dd92671 | -9.40428 | -60.55392 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6e61442-f9dd-32c8-83bb-ba6cf10c0234 | -6.57824 | -58.95956 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae68d17d-59a1-3a78-9719-4908dcc2daa6 | -6.5716 | -58.97646 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 347112a4-7d7e-38f2-8184-83531e903cc8 | -9.23885 | -60.39031 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08eceacf-e81c-3fbb-bf7c-c7afa4ad51d7 | -6.43852 | -54.95224 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69a7597e-bd2c-352a-9172-608d45339301 | -9.45238 | -51.60507 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d3c9c1b-094b-326e-9084-081df968b7fd | -6.22973 | -55.40199 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d206ff9-12a3-3ae7-9e36-7761d01a8467 | -7.60806 | -60.94783 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66db857b-63c6-3674-9e59-dd0840898c04 | -6.80503 | -59.42316 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4114b72f-ae13-3749-bbb0-13851cb11e51 | -7.57147 | -60.86592 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79e8f372-0c00-3b05-8089-b152efad0c12 | -8.37574 | -62.70618 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ebd4df50-e9bd-3ed6-8175-9ae727df91bd | -6.66612 | -52.89423 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5915d2df-85e1-37bb-9328-1882326d0e0f | -6.44059 | -52.76189 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88b5af49-ed80-37f4-836d-1dd523e6c3ca | -6.007 | -57.86764 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbc89938-695d-319c-b379-01f448f833ce | -6.75396 | -59.46916 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 05ba6ca7-73a6-3e25-8191-598534227816 | -5.82113 | -55.71898 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54341437-3405-3489-b120-11379a4211eb | -6.01245 | -57.80222 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6850a4cc-0ac2-3f0a-aac6-3bb2c722b958 | -6.43413 | -52.71602 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b83ee23a-7dd7-34a9-bbef-e57c89247b6a | -6.09086 | -57.91241 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8395b934-64d6-3494-97ba-cb8f88f9f197 | -6.57701 | -58.99512 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0342af20-9991-322c-b23d-5b200da87727 | -6.43348 | -52.7206 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a5f5684-c8cf-3c93-8cf4-5fe893da7976 | -6.69723 | -58.9413 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdead419-3dd1-3106-b7b9-4ea2e02e1eb3 | -8.38026 | -62.69937 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2a24d787-3685-3d67-8949-4b0c74c30a20 | -6.88856 | -59.42786 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5e860510-c09e-35a7-b930-751070702d9e | -9.41233 | -60.41603 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 566cae34-e06f-33e8-bab5-f8a91cd8eecd | -6.75471 | -59.46423 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b75b0f55-3d34-3e46-8f81-4e981a78821c | -9.39903 | -60.56508 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d8647a4-6751-3243-8208-ea125fbd0780 | -11.67935 | -54.57555 | 2026-08-21 05:42:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8d98b97-fd44-3511-907c-c0efb6b3ed02 | -12.51821 | -54.75843 | 2026-08-21 05:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 231bc3fe-fd97-31cf-b0bb-5400ca452c44 | -12.51276 | -54.75715 | 2026-08-21 05:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1835838-d7d0-39b3-b0c1-c1862b3c1ad1 | -12.51773 | -54.76266 | 2026-08-21 05:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1712146f-eaed-3cc4-816f-4dd3e65e8ae0 | -14.31546 | -51.90596 | 2026-08-21 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| df66a243-d39f-3689-a765-57f8cab87051 | -12.51907 | -54.75378 | 2026-08-21 05:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bdeb1d6b-4fff-35cd-b35c-ecd63d0e49c7 | -13.93703 | -53.86221 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 95986f54-261e-366b-b394-4932fc3a22e2 | -12.51856 | -54.75798 | 2026-08-21 05:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7344f70-68a8-3db1-b6db-cc20dfffcd68 | -14.05311 | -58.86275 | 2026-08-21 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b29cbde-1a13-36db-9491-d2ffa812e3f8 | -12.51724 | -54.76692 | 2026-08-21 05:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d724c5a-2706-3702-83b0-a205f2f07656 | -14.08466 | -58.86726 | 2026-08-21 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa82d269-f739-31dd-a143-8491367067b3 | -13.38826 | -54.37601 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9f2bdbcc-35a7-328f-836b-9018703d8756 | -14.32578 | -51.9007 | 2026-08-21 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c8c06e8c-148d-3418-bd40-7c2315304d16 | -12.03379 | -63.0954 | 2026-08-21 05:44:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc5ee691-586a-3bfc-bc0d-ecba5a8ccbf7 | -14.07956 | -58.8713 | 2026-08-21 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6dfe2375-f0ef-3272-a647-91d488e99d52 | -12.51173 | -54.76558 | 2026-08-21 05:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c207707c-f025-3c2a-adcb-d7d82e2a8bd6 | -13.38723 | -54.38494 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| eff7c4fa-e061-3c26-8a39-629c5207846d | -14.09576 | -58.81656 | 2026-08-21 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ccc3894-9d0b-321f-85a5-5eb5ea94be96 | -12.50646 | -54.76043 | 2026-08-21 05:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46f253a1-059b-33ee-87f2-12e06756e0c0 | -13.36971 | -54.37801 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1908c6d2-80e8-3491-b8b9-39d3b43a005f | -14.05551 | -58.86494 | 2026-08-21 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4acf7e3-a864-3198-9ab1-9bad49adf29d | -14.02783 | -58.86598 | 2026-08-21 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 417e138c-370c-3ad9-965f-020ff41b2b1f | -14.32952 | -51.908 | 2026-08-21 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cc3f1036-a05f-3dad-9ff6-bcc549ffc44a | -14.31801 | -51.90675 | 2026-08-21 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fbabe3d2-a0e1-3f3b-8f0b-e124c2636e98 | -13.38879 | -54.37148 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 88974bb5-3f69-3d95-b09b-32419097180b | -12.51805 | -54.76219 | 2026-08-21 05:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e79a5396-282a-3a2e-af29-d1440cf00e88 | -13.37625 | -54.3743 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 35dce498-4f01-3829-825c-a4499bfd9593 | -14.33208 | -51.9087 | 2026-08-21 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c05474f9-c4f0-3dd9-9653-f6f6459c7df6 | -13.10268 | -51.5871 | 2026-08-21 05:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| be478a27-65d2-31b4-886f-1d89490b9c4c | -13.39375 | -54.38134 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2ff7b87e-3937-3567-a968-511038f07433 | -14.34767 | -51.8962 | 2026-08-21 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 35d57a7c-50e6-306e-96d9-f127bd8df7c1 | -13.09957 | -51.58619 | 2026-08-21 05:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7a44d26c-79c3-3a9c-ae39-252d6db9b411 | -14.09488 | -58.8592 | 2026-08-21 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47ad37eb-46aa-310a-b7bf-195fb5d41975 | -13.3867 | -54.3895 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d39bf5f9-9919-3c07-a944-19bd295e3f8e | -14.03234 | -58.86659 | 2026-08-21 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1f03ea27-d45f-3c2c-a17c-83c66597d46c | -14.32504 | -51.90775 | 2026-08-21 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7d907977-620c-3022-862c-192b3e0779d5 | -14.10029 | -58.81718 | 2026-08-21 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b90b96b7-14b8-32a6-ab38-0ab26b54c332 | -14.09123 | -58.81593 | 2026-08-21 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0516e37c-7cbc-3466-b855-b29e9638cf31 | -14.02272 | -58.86999 | 2026-08-21 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9908744f-5d0d-3a53-8104-d00f17768ca9 | -14.34063 | -51.89529 | 2026-08-21 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 069250d4-723f-3068-9ddb-4b046fa66852 | -13.38122 | -54.38417 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 2f23e271-80fa-3c9e-983d-7a1611759edd | -15.00031 | -52.68147 | 2026-08-21 05:44:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 76622d21-80e8-336b-8702-6a84935fed17 | -14.32882 | -51.91514 | 2026-08-21 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ffead57f-884a-3b2c-a6de-8e1d079cd39e | -14.31873 | -51.8998 | 2026-08-21 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d90c42f4-e396-32f0-be59-e65a71a5a0b8 | -13.38278 | -54.37057 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| ce77409e-ed4a-309b-98c8-24085409ee0a | -14.03684 | -58.86721 | 2026-08-21 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f76f4f64-8092-3514-9b28-6c944c60a896 | -14.33912 | -51.90963 | 2026-08-21 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a81ba3f-b9f2-3f65-bfcb-d6cec5145361 | -13.94949 | -53.86428 | 2026-08-21 05:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0578edc-7d58-3220-b87d-09b9854392cd | -14.30909 | -51.898 | 2026-08-21 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b3dc7432-a4e5-3c2f-aac1-ac9e82c6ec14 | -14.30537 | -51.89096 | 2026-08-21 05:44:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| eb057d74-e353-370b-a037-d5de23912603 | -13.73535 | -51.85761 | 2026-08-21 05:44:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1cbabbe5-714a-3d1f-a612-6efb2f8e061d | -14.07445 | -58.87533 | 2026-08-21 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d957670e-9c09-3f59-b78d-055400c36796 | -14.08977 | -58.86323 | 2026-08-21 05:44:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README84.md)
