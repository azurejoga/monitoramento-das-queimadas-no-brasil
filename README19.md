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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17ac4441-6ceb-39a6-bac0-ecba08eddb0b | -8.03467 | -46.24544 | 2026-07-04 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 96a064de-812a-39b2-860c-9ea529edacf5 | -10.38965 | -56.76541 | 2026-07-04 05:23:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbe2f720-45c1-35ff-84dc-4cedfe9de130 | -11.4289 | -46.58794 | 2026-07-04 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7c8f560c-89e7-34a7-aae5-0e803038f83b | -9.46489 | -68.39153 | 2026-07-04 05:23:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47bea57f-386b-3cae-9cd2-fe5a894cf968 | -13.2383 | -54.36469 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9526307d-6eaa-3f43-af83-feda40a5ce6d | -7.90722 | -48.25153 | 2026-07-04 05:23:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df4aaea9-11c2-3847-acb6-e477bfe25d17 | -13.24591 | -54.33915 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 692443dd-edf7-31dd-9aed-cf3a0ca8c738 | -13.25239 | -54.35086 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c9190260-cae8-3944-929f-132cbb3086ac | -13.25166 | -54.35609 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 949c4348-a05c-387b-95f5-10137ee728f5 | -13.2365 | -54.34844 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 7a6e2d7c-e144-30f0-aa91-980c0b98cb23 | -10.29904 | -57.13136 | 2026-07-04 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fea9558f-b8a9-3ebf-9bb7-08d664314da5 | -13.26034 | -54.35206 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e027c0f5-e7a2-3c26-86aa-56635405d3d7 | -9.57099 | -49.1122 | 2026-07-04 05:23:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0dc706a-74ca-3ff4-89d2-e02793a16820 | -10.12314 | -52.09265 | 2026-07-04 05:23:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e45cc3e5-dfea-333d-8e2b-5ed3c9cfa7d3 | -8.70632 | -54.66563 | 2026-07-04 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6fe62052-097a-3f43-81a7-3bd995ace456 | -11.42278 | -46.58889 | 2026-07-04 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 398b4bdd-3875-3717-87bc-090d7c6b4273 | -13.24518 | -54.34439 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e27294df-2fe8-3b88-a70f-e9c1ee69280b | -19.51536 | -52.74119 | 2026-07-04 05:23:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6984f3d3-b4ab-3abd-bc0e-dc94afcb0646 | -11.42233 | -46.58799 | 2026-07-04 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 87d7509f-096a-3281-81fc-6b31aab5ec03 | -13.22384 | -54.35198 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f57112e-2ad3-34ff-8531-d1646b85b589 | -13.23796 | -54.33791 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9a60606-28dd-3920-aa0d-c34838737603 | -17.54739 | -46.95182 | 2026-07-04 05:23:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83725465-657d-3f15-9d4f-9c37c8b6975c | -13.23398 | -54.33734 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b608a624-d365-3e6f-83e8-9580ae9c4cd8 | -13.25385 | -54.34038 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| c2fc1068-827d-3f3e-aa05-38df60e1f8de | -13.23074 | -54.38991 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 986aeb9e-c659-304e-863d-d1a90505f157 | -13.25061 | -54.33456 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 40d0c1c1-af67-349f-a8a9-e42c30b2781a | -13.22854 | -54.34731 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 758f1fc5-6cfe-342d-b161-c2e9b654870b | -12.51193 | -48.25928 | 2026-07-04 05:23:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef432c8a-a190-3547-a64e-bbfcbace9432 | -13.23179 | -54.35315 | 2026-07-04 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7679ea68-3fe9-3108-b72b-37cf78d01781 | -21.87896 | -55.81515 | 2026-07-04 05:25:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c800e09-2186-363d-bc78-d681ba1c8538 | -21.20332 | -48.60464 | 2026-07-04 05:25:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e8518a80-5e5a-3d3c-90b3-522824a4cd5f | -12.7553 | -44.5194 | 2026-07-04 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| dd10d711-ca17-3826-b562-888a6bb9ed67 | -13.2401 | -54.351 | 2026-07-04 05:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 5197cbce-b7f7-3595-8812-2be9ebee399f | -12.7741 | -44.5396 | 2026-07-04 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| e2970a5a-e0b9-3733-83c1-b27aa5711b93 | -10.9205 | -43.0622 | 2026-07-04 05:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 573dc1b9-1b7b-34a3-9d3b-30dee29f7fc1 | -13.2404 | -54.3303 | 2026-07-04 05:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 2b130481-1cd8-3a47-a720-cbfe26b23cd2 | -13.2595 | -54.3283 | 2026-07-04 05:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 8f2ca66e-0b85-3bc4-8391-3fb6bb92818d | -10.9401 | -43.0355 | 2026-07-04 05:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 38cddd63-35bc-32a4-9dbc-d3768d30cc84 | -12.7548 | -44.5428 | 2026-07-04 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 222.1 |
| 2e597030-6cac-3371-ae95-b92a6f11d51b | -10.9397 | -43.0593 | 2026-07-04 05:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| a28f4709-bdb6-33ac-bd7b-812815797f4a | -13.2592 | -54.3489 | 2026-07-04 05:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| eb5ebbe3-d35e-334e-a60a-991c28269e98 | -10.9209 | -43.0384 | 2026-07-04 05:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 22302be7-9273-3082-b683-3e583cf24e0a | -13.2592 | -54.3489 | 2026-07-04 05:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 0a27f3b7-a0ab-3ffc-b4fa-6c0cce21abb7 | -10.9209 | -43.0384 | 2026-07-04 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 40efeec6-7325-3b36-89c9-a59553bafb9c | -12.7553 | -44.5194 | 2026-07-04 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 0dea4725-2073-3acc-bf00-1c098edaa594 | -10.9397 | -43.0593 | 2026-07-04 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 186f955c-61c8-3fa8-9c93-26f930d63d13 | -10.9401 | -43.0355 | 2026-07-04 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 8174db2d-8d0f-3af1-a0b5-8e457027e945 | -13.2401 | -54.351 | 2026-07-04 05:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 17ce0581-ed1d-39f9-95be-8334d5b895f4 | -10.9205 | -43.0622 | 2026-07-04 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 2c37e6ca-4950-37b3-86e3-2473eef7c58e | -13.2404 | -54.3303 | 2026-07-04 05:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 984e79b2-9283-3bae-a2c3-dfb5c8140b13 | -13.2209 | -54.353 | 2026-07-04 05:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 5346693e-fa72-37a6-924a-5c828fc77395 | -12.7548 | -44.5428 | 2026-07-04 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 167.0 |
| b885b0d7-2d19-3161-be94-a9a07703eaff | -8.85886 | -62.22038 | 2026-07-04 05:40:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f58a6ef1-7f9d-3b27-b706-ff09e99c9964 | -9.38158 | -58.20518 | 2026-07-04 05:40:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11b2a5e3-d5e7-3ffc-a732-3412942ad630 | -8.8623 | -62.22092 | 2026-07-04 05:40:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 15d52258-7ed5-300d-aa2e-89b3653b5b4c | -8.85974 | -62.22122 | 2026-07-04 05:40:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c53cd234-5ac3-3bae-9f45-d15fde8fb263 | -8.86173 | -62.22473 | 2026-07-04 05:40:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| dd0a5e4f-705e-3916-a548-6e9e167a5719 | -6.42652 | -55.79648 | 2026-07-04 05:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2d4fbd07-1ea6-3ff5-ab11-dc5ca9b86684 | -9.43412 | -58.02266 | 2026-07-04 05:40:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5b34bc9-b085-3745-a26c-a8bda758fabc | -10.39141 | -56.76701 | 2026-07-04 05:40:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e48b417c-22bc-3d50-9078-1c2925adbd35 | -10.30059 | -57.12714 | 2026-07-04 05:40:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4214aab0-895e-3aca-a3a8-c48aeed2e3a3 | -8.45159 | -51.56973 | 2026-07-04 05:40:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9cc34702-2748-3daf-9123-07076b2974d8 | -7.23959 | -60.64211 | 2026-07-04 05:40:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3aee8b2-edb2-39c8-bdd6-818aa1967412 | -10.38914 | -56.7661 | 2026-07-04 05:40:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99d7cc3e-6070-3e57-853e-1a44c423c6ac | -9.07317 | -65.41902 | 2026-07-04 05:40:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fdb8bc0-f005-3a5f-b37b-d3419b295e26 | -8.44492 | -51.56862 | 2026-07-04 05:40:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a1c103e3-4d1e-3162-9653-a633b088e53b | -13.24695 | -54.32241 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 172e6807-e796-32a4-99a8-6f978a952824 | -13.23258 | -54.36991 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bea891f-17e4-3036-99fd-a5aab5e67008 | -13.24595 | -54.33146 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8be3dfad-e8a0-398e-88dd-453bb5563c53 | -13.24772 | -54.34444 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9509ac9d-7b29-3aea-bbc4-0bf267e7ea0d | -13.2537 | -54.34528 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2b0a362c-73ba-3411-8e70-37d48733db48 | -13.23846 | -54.34417 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c126519a-f8b1-38ed-bfce-129dbed88e1f | -13.25093 | -54.34131 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 88c72b76-0c73-3e5f-a8ba-50e4d8fe6ff2 | -9.46651 | -68.38643 | 2026-07-04 05:42:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d328776a-f514-366b-9358-7df7d8f1723a | -13.22945 | -54.39643 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ad4e9ec-f3f3-31db-853b-a68422dfe398 | -13.24986 | -54.3264 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8ab892b-fe19-378f-b638-219a1862d00e | -13.2515 | -54.31257 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdbce6f4-995e-301b-bdc7-2e7d8303adbb | -13.23842 | -54.32025 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8c4668f-0d4c-3bf5-90b0-69fef0073c48 | -13.22868 | -54.35144 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3b38baec-fe99-31a1-b4c5-b9f99ed5d4f4 | -13.24991 | -54.35047 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6fc07fb-310f-3bcd-a1c6-f8d246b1bcc5 | -11.63028 | -59.01324 | 2026-07-04 05:42:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd150d18-a18e-3f99-b337-b4ef68098450 | -13.24046 | -54.32608 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9eb2e12-41d1-3fee-a30e-701288d05015 | -13.24495 | -54.34043 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cc402243-6818-3f0b-94b8-fac0f886f292 | -13.24096 | -54.32158 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5111c6f6-f719-3d8a-b4e2-fa3b43045405 | -13.25588 | -54.35132 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56768a6e-d72e-3e6b-82f5-f4f49e51eafc | -13.22609 | -54.37357 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 655f3f54-26b6-340a-8384-91c89f85dfa4 | -11.62973 | -59.01729 | 2026-07-04 05:42:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47694038-084c-32c3-8bfd-3d07ab2c09dc | -9.46277 | -68.38579 | 2026-07-04 05:42:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5a8c156c-e7eb-37e3-bd80-61577e538283 | -13.24545 | -54.3359 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bcaa996-fe31-39ad-b2f8-e2936a8790d7 | -11.63456 | -59.01386 | 2026-07-04 05:42:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3912a4fa-7db5-3a05-8585-4c952d79d9ae | -13.22431 | -54.33689 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eec80995-f860-349b-93bc-5827dd9fea32 | -13.23789 | -54.32475 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2e5fa3c-4709-3d6b-ab9c-524e4a04b450 | -13.2412 | -54.34821 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f19a21f4-817f-3fc4-be0a-74141f689b28 | -13.25695 | -54.31789 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e75dbfb0-69b5-3fbe-83f8-ef36e275b2a3 | -13.24199 | -54.3123 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 727c35e6-374e-37fb-99aa-ebffb49d2b50 | -13.23803 | -54.37511 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 738d0efd-33cf-3e31-9a09-d1ada12fdf2a | -13.23085 | -54.3329 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3f014109-3ee9-3ea7-a67b-c7da1ea7d6fe | -13.25478 | -54.33621 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 24022f47-0da5-395d-b08a-11d7a7a8a831 | -13.25315 | -54.34987 | 2026-07-04 05:42:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d659e49f-7456-3bbb-9787-f16f65132f1b | -9.88937 | -68.36756 | 2026-07-04 05:42:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README20.md)
