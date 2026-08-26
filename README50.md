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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fdf53af-1d05-39ef-8a8b-dd583423aa96 | -6.75132 | -56.3331 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e108d44-ce40-34ff-8052-d4ffaf935ac4 | -6.62626 | -58.50156 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ce630671-6b9c-3a2b-8d94-92ac8ed4b52f | -6.98619 | -59.28172 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd39d9ad-1ae0-37fc-af42-425a813ebb03 | -6.83985 | -59.45792 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74f7e21c-8321-3d54-8b54-02950cb4ee99 | -6.6451 | -58.50442 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a7542ba2-27c0-33e8-91e4-b0acd774acee | -7.51701 | -61.38729 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 18992d32-47b4-3607-b1cd-f0b935cb78d8 | -6.07575 | -59.97809 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a95d0eed-ef45-34f4-ac46-b3e3011ef1b0 | -7.02709 | -59.23841 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87193d15-3e09-34f3-a9f1-65e041fae928 | -6.83559 | -52.50405 | 2026-08-26 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa34a74a-6dcf-3291-92c0-7ca1df363017 | -7.37636 | -55.18005 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e630610-f745-3d1f-991d-8e8b869d2c60 | -6.62849 | -58.50907 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 62afe7f6-9441-3309-9215-ef8077faffe1 | -6.28058 | -53.36292 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b8c49fef-3c37-3af2-a69b-34308c48214d | -6.76724 | -59.44629 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fb0fa0c-9ecc-382c-9ac9-7fca32a4a102 | -6.23031 | -55.48282 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c4c0d03-b758-361b-9eac-890d12b7a660 | -5.14812 | -56.26917 | 2026-08-26 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a638fce3-68ec-38cb-9539-e471b8e3ec94 | -7.43586 | -59.77433 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 921b60d7-cf85-3f9c-a554-725c1296b838 | -6.16278 | -53.68729 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c323d94f-ab22-3ea5-b0a5-f20b2935a37c | -8.11332 | -47.46691 | 2026-08-26 05:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a57bc75-b737-3c69-b7b8-f7cc57f09d65 | -6.17008 | -53.49696 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb740ea5-4910-3d4e-a933-46cc16beddce | -6.80431 | -59.40596 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab50ebb4-81ba-34d4-954f-d46f7425cfc1 | -6.98727 | -59.25343 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7690d0d0-afaa-3232-a944-5b909ff7d6f7 | -6.99393 | -59.27584 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 481458bc-b80a-3020-831e-0a7bd30b71f1 | -6.16391 | -57.80129 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3dc7f4e3-e6e9-359a-876d-2d5dd86c1073 | -6.72743 | -59.14494 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbb5604f-4926-3612-a461-b9ee99e171ad | -6.50143 | -53.26429 | 2026-08-26 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f66df151-d4a0-32f2-a087-f8fa81614902 | -6.7169 | -59.1255 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 581e52df-4588-30cb-916a-9fccc25037fa | -6.72798 | -59.14148 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 470f8d80-8f99-3898-8183-0c9e4a52258e | -6.70032 | -56.34313 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c8d6e66-e04f-3e68-86b2-4c499a475d92 | -7.21586 | -60.61706 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 782433d1-7a32-314d-80cc-91990608f4fa | -6.12637 | -57.82095 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 87151476-5ed3-3fdc-ba00-c02406a7d27a | -7.25457 | -49.85201 | 2026-08-26 05:27:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49badc17-0188-3fae-bd84-ef5a9eabdb03 | -7.48029 | -61.37352 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1789f6a-d719-31c3-be3d-1c561daca433 | -6.99893 | -59.30866 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 02693f74-be93-3f91-9330-5703ddae1a82 | -6.24455 | -55.42825 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 075e78bb-4019-3f44-8df1-caeec4ca1212 | -6.71871 | -56.342 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 512f950f-1c8c-3cbe-b5ca-8b9aed83b035 | -6.43739 | -54.97 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbe72f7d-03a8-36ec-9572-a5780898d74e | -7.01879 | -59.22642 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 46ef860d-5ac1-31e3-bcfe-35003b9fcfd2 | -3.53986 | -48.17616 | 2026-08-26 05:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ede70dda-b18c-3527-8111-dff0b7858e82 | -7.74866 | -61.10278 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ce69f9d-f2e3-3f50-9ccd-394e35986338 | -6.80159 | -59.59092 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e9f1eeb-f9da-3323-9c97-c5b7e81518ac | -8.15367 | -47.50941 | 2026-08-26 05:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b98470e7-269d-3ce9-a931-2da8a72247a8 | -6.24931 | -53.37016 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49875ec8-062d-33c8-94a1-2b718ee1597c | -6.615 | -58.3779 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5eea2167-06f0-3341-b8a4-ffef7f6d0f62 | -7.06809 | -59.23491 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0db60ae4-85fe-30ee-86f2-3dad476572a1 | -6.79489 | -59.4009 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdc88c53-eb5e-35fc-83ae-5b9c7f602fdb | -6.12168 | -57.69574 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b620d87-c726-3236-9b7e-0360d2418669 | -6.93405 | -58.94992 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc51ab40-c86c-3eec-b244-63dc5426c2ed | -2.50337 | -48.137 | 2026-08-26 05:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| def89121-e677-3c9f-8666-15604e5c28ad | -6.27464 | -53.3739 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ccc1014d-035d-37b0-8dfe-e9c50f140a7f | -3.09576 | -61.2249 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b3ec9a5-94e6-3f41-b439-7c5a07cb231b | -3.12374 | -61.18787 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 653458d1-45bc-3fa3-af9c-07399a064301 | -8.16292 | -54.95765 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c91a075-be6b-3eda-997e-248d7359b85e | -7.01824 | -59.2299 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e8cb87cd-70c6-3a99-bcce-a60136dbdc8a | -6.84426 | -59.4302 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 789ee96f-bbf5-3b5a-a17d-0312f951e9cf | -6.82719 | -58.6585 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dff7109d-3017-3b28-81b5-7b62943e26a9 | -6.15113 | -57.94862 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11b15c0a-35c9-3645-9028-8165f16bcdae | -6.63953 | -58.49638 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92546915-5ee0-3c22-a347-6b4644f2f3b3 | -8.01498 | -51.81464 | 2026-08-26 05:27:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d50e0d5f-513c-36cd-8da8-600fc0620c48 | -7.01935 | -59.2443 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e762a72f-030d-3c35-8f09-9b447296b809 | -8.62438 | -54.74232 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a1d8aaea-f5b2-3fe4-93ad-0967a747f735 | -6.7938 | -59.63967 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6b19759-0059-37e8-bb0a-4e5d95c8496b | -6.08702 | -57.71277 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfdb1408-fb3a-3798-a0a7-2e4dd030ca6e | -5.94124 | -57.73059 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7bf6bf5-b2df-3620-955f-97c4713b674a | -7.03152 | -59.23201 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f77af4da-3303-31ee-beb7-968794f0ebe0 | -8.61788 | -54.73072 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 05b0db05-2d9a-3f98-bbf0-210f90492848 | -7.50161 | -55.35251 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4752301-3933-313b-a365-d98682a974aa | -6.13067 | -59.89279 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 84dd6a61-2792-3e2b-b68f-3382ab0686c2 | -6.80048 | -59.59787 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 02206292-38e4-32b2-8077-486f3186482c | -8.15029 | -54.98804 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 029413ec-fd40-3208-9675-063dea0fedbc | -8.22439 | -55.00141 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 96e22a22-4414-3546-bcee-03526b242cb2 | -6.70916 | -59.13138 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 447641da-8d2f-3440-87e9-1fd125044302 | -7.38332 | -55.18584 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4374d5b9-fef8-37b2-a562-cf3456291daa | -6.88767 | -59.02799 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b967913-3988-369b-8ecd-933a85045b00 | -2.88915 | -48.80618 | 2026-08-26 05:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 729c27e2-c427-3bda-ad47-09eb259d24db | -6.12979 | -57.86525 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70b2707e-4a06-3231-a0c3-92050443b10f | -2.8518 | -50.46585 | 2026-08-26 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ef12727-439b-3109-9ad3-2eab8f1b7c0b | -6.65509 | -58.506 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b084f576-e96b-35bf-a754-e82ff04909d9 | -6.15168 | -57.94509 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8185e2e0-b751-3e71-8dc9-47695e82099b | -7.55881 | -61.41359 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7d98dac7-66da-3637-bf66-dce1413791c6 | -6.13198 | -57.82917 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b57a24b6-4ecc-3051-bd38-1d913d7be0c3 | -7.01658 | -59.24031 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30a5d1cd-e958-37bb-b899-99c4ca11df07 | -6.02787 | -58.04541 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 524068c5-9b33-3889-bb4c-de1b430a3ece | -6.42988 | -56.18084 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c68e367a-41ce-32b2-9418-0587c2c1db06 | -2.79815 | -49.58338 | 2026-08-26 05:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 048b550c-943c-3f52-9ced-7349cb2e5635 | -6.60444 | -58.37981 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4bcfebc3-0936-348c-9ad0-81093c297269 | -8.53394 | -55.34286 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8358cc2d-b011-37c9-b7cf-5ad51d230aa9 | -6.27579 | -53.36614 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4673f86a-05be-3017-98e1-042474dc2691 | -6.95967 | -59.08921 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6622504d-989a-35c4-a662-46408f2c485c | -7.47401 | -61.36861 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 426734b7-0045-3d2f-ae7f-3500ae3f9cb1 | -2.98302 | -49.27531 | 2026-08-26 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b20d1f8-540f-325d-b8d8-6933903ad1b7 | -6.33154 | -54.73575 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1f079e43-ac00-307a-a483-d8429b20a0a0 | -7.0199 | -59.24083 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 940a0f92-281b-3086-9629-9169b07dd95a | -3.59023 | -50.67519 | 2026-08-26 05:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 75f9c685-434e-38f6-9159-a9dfc6b6cb37 | -6.30053 | -53.57999 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29b0c7df-e8db-3ab6-b5a5-6932e9ef7e69 | -4.59415 | -56.05275 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25c625c9-5e9c-37da-a8d2-63fd87d800f0 | -7.39376 | -55.168 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a64c165-9156-37ce-9568-2170b179865f | -3.09547 | -61.20407 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 02ca1168-7d2b-3c48-b051-fd5c9c5bb8c2 | -6.86474 | -59.40854 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c522c7c-4752-3ae1-8e4a-94832b884b42 | -3.09612 | -61.20003 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c317a4a-d4f9-3fca-84d4-f6db2dec472a | -7.51479 | -61.37917 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 27.9 |


[Clique aqui para ver as próximas entradas](README51.md)
