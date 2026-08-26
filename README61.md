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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1a32eab-da9f-3f65-b4bf-a9f6028e1813 | -11.96849 | -47.74918 | 2026-08-26 05:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33a59408-015f-34b1-9de6-c479fb50dc22 | -9.97419 | -53.94723 | 2026-08-26 05:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ae94805-d691-3fd3-a7bd-3b07824bd7f6 | -8.67487 | -62.94674 | 2026-08-26 05:29:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 052f5124-5629-3df2-91d2-8f3d990bab03 | -11.75937 | -54.5328 | 2026-08-26 05:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bc3030f-d49e-31c6-8269-d5cc0f5a630a | -13.33303 | -48.22888 | 2026-08-26 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2de7bf86-f7ee-326a-b5a8-461fa469c714 | -9.67625 | -55.07936 | 2026-08-26 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9797010e-4d6e-34c5-a165-b722a2f9933c | -13.29021 | -51.46323 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.0 |
| a714d30d-dd74-3ce5-9baa-18e17abfa1a7 | -13.1779 | -51.33878 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| d0e4066f-c097-33a5-901f-3086bed17447 | -7.80946 | -63.26437 | 2026-08-26 05:29:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 163d2ec4-47f1-39e0-b00b-802d2432c30d | -13.65109 | -51.85326 | 2026-08-26 05:29:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 91038f64-cff5-3b10-9cde-b8114f7562e7 | -14.58132 | -52.02905 | 2026-08-26 05:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b66d590-f6b9-3cab-8fd3-e26ed7e965bd | -13.2513 | -51.51628 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 406a90ec-8272-383a-a14d-67c618ec7e5f | -10.76833 | -54.02942 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d813b6bf-6eca-3edc-99f6-f6e233c0da19 | -12.76366 | -46.44994 | 2026-08-26 05:29:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 71793850-5e71-3fa8-818f-cb20ab47c60b | -13.26231 | -51.38029 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 6f7570d3-bcc1-31cc-ab09-5d9431070bfc | -9.07282 | -60.43771 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a53b54b-2aa0-36ee-bb92-b786050c5e3d | -13.217 | -51.37511 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 794239ea-c022-3854-9dc9-0adb44355b2c | -8.81287 | -62.3148 | 2026-08-26 05:29:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f2988b20-0371-3693-a24d-418ec3b20ccb | -9.48521 | -56.91797 | 2026-08-26 05:29:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 226bb78f-e17d-3bb1-af5b-bcb88f189ed7 | -9.10185 | -60.90599 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56a32b8e-2200-3bc5-82de-ea6de2077def | -12.69481 | -48.41774 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f27871be-cd89-303c-ba3c-f302e184fda0 | -13.85744 | -54.08011 | 2026-08-26 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a97fa50-1cda-373f-9e01-1d1702c9c3a6 | -8.81732 | -62.332 | 2026-08-26 05:29:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 02165ea7-4a20-3a04-886b-10880161f0c1 | -13.16138 | -51.34013 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4ede8e74-362f-3478-bbaa-14299e630c68 | -8.82375 | -62.33721 | 2026-08-26 05:29:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a063fb02-a1c0-39d1-98a5-db340426e3b9 | -11.74675 | -54.53652 | 2026-08-26 05:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 01c6bc94-5433-324b-8b31-b6eacae7ac33 | -8.64993 | -62.89412 | 2026-08-26 05:29:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2b81ebe-d8c1-3bb7-ace8-f57afcae91cc | -13.22896 | -51.38633 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9df18365-1a18-3e63-9d08-73e73f5994ae | -9.67407 | -55.09458 | 2026-08-26 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 34edfc18-88eb-31b0-9c56-07913baf5207 | -9.1058 | -60.90295 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2727ebc9-e1e6-3b29-9ed8-6d24469599ea | -13.17253 | -51.33808 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0604bdbe-5e2a-3f08-9eba-5181fc5d0c91 | -9.18353 | -59.38243 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aaa49780-05c1-3660-8d04-27f1aab20478 | -11.21446 | -55.08115 | 2026-08-26 05:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89216d34-9912-35c4-9129-0f169150d194 | -9.04328 | -60.45098 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2467816-a49b-3572-8b18-24c7a0f0212a | -13.36525 | -48.22143 | 2026-08-26 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ba7b92a-f4a7-3612-8483-d2608bf3ec6e | -10.38775 | -53.50797 | 2026-08-26 05:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0eb9f9a1-63c0-35c1-95ea-22ae2076fab3 | -12.65391 | -48.42187 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e40af6a3-6a22-32d4-8fad-193a764d6a9c | -11.2099 | -55.08413 | 2026-08-26 05:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e04b10c-2be1-3439-bca8-be76538bfbea | -9.17533 | -59.58162 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 296400a6-6318-3f2c-b0b9-715eb3b62abd | -10.76025 | -54.02402 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5fc4d61c-aee0-303a-9f5d-5418344b2eaf | -11.8229 | -47.6576 | 2026-08-26 05:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fe3377be-a773-3d17-b575-e9d0d5ab8f9a | -11.75038 | -54.53552 | 2026-08-26 05:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d64df9cd-a16b-34b5-945d-3ff842b407c3 | -7.78517 | -61.56235 | 2026-08-26 05:29:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bb72436-c41c-31b7-aec0-f7fd18482193 | -13.17665 | -51.34905 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 17377f1c-0420-3d6b-9602-2149cd216f84 | -13.23796 | -51.35627 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9859852f-33b5-3cae-b6e3-f4f9e930bdb5 | -13.85637 | -54.07328 | 2026-08-26 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72c13c18-0f53-3d9d-b97d-8031abbc785f | -13.60623 | -49.00434 | 2026-08-26 05:29:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d89d208b-28ce-3821-8c48-907e539bb423 | -13.18905 | -51.33675 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 10cc0e11-da5d-396d-b325-3d174d7db1a6 | -9.17147 | -59.60606 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 310e5cfa-9c19-3634-904a-55a7c101cfab | -13.27996 | -51.4585 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2f86023d-ff68-3593-a8ef-70df8279288a | -12.89864 | -59.9154 | 2026-08-26 05:29:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c58aba47-b391-3514-a5db-5c1ed2b9fbea | -13.86263 | -54.03931 | 2026-08-26 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8db0e23b-c11a-3cd9-993e-8a0e294fe3be | -9.09825 | -59.40466 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b88ddfc-159a-3ee4-923e-c312536ba0a1 | -9.60473 | -55.10762 | 2026-08-26 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| d9222c45-598e-39b3-b852-ff10f1495c43 | -13.17832 | -51.33535 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 3310697f-25c9-37a2-b68c-edff0c8eba6e | -13.86031 | -54.05758 | 2026-08-26 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cff650ee-705b-3a5e-b47b-37ee72e17a02 | -13.29104 | -51.45648 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 0a39ed4d-b3bd-3c40-b093-e50e2fa10104 | -9.6072 | -55.11832 | 2026-08-26 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 3f98714b-40e5-31ff-baa2-19cd9691d3e2 | -12.17233 | -50.60645 | 2026-08-26 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a7b8665-c455-397a-96e8-1ee1e08994e5 | -11.15955 | -54.00774 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 345bae8d-5d96-3a3d-9a97-8ef526e1e850 | -12.04109 | -46.03616 | 2026-08-26 05:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6c1f0d81-419e-300f-84fa-4e15febab710 | -10.76345 | -54.03293 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 452bdcbf-cfbc-37f8-b84d-5f40ce0f2235 | -12.02729 | -46.02672 | 2026-08-26 05:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 053a6a82-9da9-3c58-ac19-e7caef7538ae | -9.46714 | -56.90433 | 2026-08-26 05:29:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f16301b-daad-3a7a-84e0-a9dc953bd18d | -13.18368 | -51.33605 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 05302dbe-7836-3129-bbb5-c07f83285045 | -9.47197 | -56.89662 | 2026-08-26 05:29:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3571a678-c2fe-33b9-a7de-29ccf6fcc8cb | -9.19969 | -59.57836 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9226f5ab-9f09-3f24-a512-21dd96283a5f | -10.75891 | -54.02454 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 9b5ddbc0-17cc-3681-b48b-71043a1cc9a4 | -12.04137 | -46.04105 | 2026-08-26 05:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 809cfe3d-8359-30ef-a041-383a140783d8 | -9.46222 | -60.54067 | 2026-08-26 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50961fb6-adfb-3a5e-a50a-28d42c3c1ac5 | -14.79257 | -48.80107 | 2026-08-26 05:29:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7f6b3ab9-f74e-320e-8521-3633fab3c0c1 | -13.35889 | -48.23505 | 2026-08-26 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f8793e7-711f-3b14-b261-406cb464091e | -9.47272 | -56.90369 | 2026-08-26 05:29:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e7336fd-f225-355c-bfc7-f30faffc8c5d | -13.36697 | -48.2222 | 2026-08-26 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 99773855-6eb2-3866-9357-c960884c8282 | -9.43732 | -51.68416 | 2026-08-26 05:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d4cd85b1-fdaa-3378-a9d1-7c57dbc16c28 | -13.21742 | -51.37171 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b4e94c85-8d20-3eaf-a03c-6d491a1a4c69 | -13.3062 | -51.46532 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f762822a-09c7-30c8-9b51-ca553c950582 | -12.03545 | -46.02004 | 2026-08-26 05:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| b04d696e-2f38-3495-930c-e4e148cf28c3 | -13.29679 | -51.4538 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 69e68b7a-8e50-34a4-92e2-760d17cd07c4 | -13.85676 | -54.03634 | 2026-08-26 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a09b9c6-9ec3-3c85-9ba9-f92acf531bd7 | -9.97047 | -53.94257 | 2026-08-26 05:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a50abd5e-7624-344c-b196-b383940d7678 | -10.76889 | -54.02531 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6312ab57-ff9f-3d9c-a9e5-2e7352e14b03 | -8.82152 | -62.32856 | 2026-08-26 05:29:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 15b1ea81-b6d8-3fae-88e3-da43bb8f70f3 | -10.43553 | -61.2195 | 2026-08-26 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c031dc8-f5f0-301f-add4-63502c095410 | -9.66761 | -55.08314 | 2026-08-26 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6c5ce79e-c02b-3dba-98f4-ec928f861b0b | -12.08414 | -64.24706 | 2026-08-26 05:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a661c925-fe58-375e-a91f-30aca1a0d804 | -13.1841 | -51.33263 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| eab2d1df-3640-3149-a29a-f0e6396fff5a | -10.76324 | -53.9693 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5da0754c-b1db-3f64-adc9-e52225c2d6e9 | -13.33406 | -48.21955 | 2026-08-26 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c55de84a-1ddc-3d5a-b511-230f2708a074 | -9.06949 | -60.43717 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df1e60fd-b935-3f6a-9db3-da0b2401c26c | -12.65516 | -48.42276 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 46d69524-b75b-3319-9377-a21621bf6444 | -13.22899 | -51.36626 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 3bbfb42c-5487-3448-9220-1345bdf704ab | -9.45048 | -60.53526 | 2026-08-26 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccfd42e2-95fe-3dcf-847e-0c7515e12d4e | -13.26149 | -51.38713 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 34.6 |
| deb12b6c-f8ff-3b90-bc41-aa14a9429095 | -12.66857 | -48.41936 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e8e95253-43eb-30b9-9872-6374fd52cf43 | -9.10127 | -60.90958 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b76fffb-aa67-3d39-ab88-3664648b4e71 | -13.24551 | -51.3649 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 35.3 |
| a253d517-04b0-3089-8f46-016bc2f3a2a1 | -9.47009 | -56.90893 | 2026-08-26 05:29:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 407a5174-08bd-33a3-b665-6076337164d8 | -11.16074 | -53.99928 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ace1be6-f536-3c6f-b7c6-ff9d8175bc22 | -13.23097 | -51.36925 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.6 |


[Clique aqui para ver as próximas entradas](README62.md)
