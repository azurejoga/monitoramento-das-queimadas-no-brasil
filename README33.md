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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7fc1cf86-1420-31e2-8c68-da264d214559 | -12.82256 | -50.64753 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 662058aa-33b6-34a9-b3f6-05f68f21ff16 | -12.84262 | -50.63813 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5807cfde-9775-3bc4-a88f-530c6839fade | -12.81754 | -50.65528 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8385f322-bb31-35f5-9132-1218f01314ad | -7.75196 | -45.72844 | 2025-10-14 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae2f9969-088c-3f04-bbb9-d0190167ce8c | -12.61624 | -48.30793 | 2025-10-14 04:25:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 44fa8451-616e-34a2-aa5f-21a1d065fa13 | -7.31921 | -45.75972 | 2025-10-14 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d5f64f5-fe79-3ac8-9814-72118e015b93 | -7.53741 | -45.81932 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 40221805-86d7-38ec-910e-881d43a4541f | -11.01943 | -44.53243 | 2025-10-14 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a41a5709-7262-391e-ad63-1ed7c4e6d73a | -12.84333 | -50.63395 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1a9426fb-cd54-3727-9254-2972942e9ccd | -7.7584 | -44.7303 | 2025-10-14 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c765f48-7b90-30e2-94a0-d82e74ea2837 | -7.5363 | -42.69636 | 2025-10-14 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f9a2da26-c428-3891-be87-49e927022a4e | -12.83403 | -50.64524 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 59c2236f-4e7b-3b43-aa5c-4432d67a9509 | -7.93397 | -44.11422 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d2864dee-3415-3157-9558-028e815a0785 | -7.91321 | -47.20448 | 2025-10-14 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2fc1aa13-e79e-31d7-a2f5-12b1d3673075 | -8.11218 | -55.28685 | 2025-10-14 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a44a5ec6-6e66-3f34-950f-5c5516475f5d | -7.95073 | -44.1207 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9ee34021-b50c-3cd3-bf7c-eb2fd797d8f2 | -7.5341 | -45.8188 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8575fac6-4b27-399e-a6e4-47d147d9f454 | -7.49192 | -42.14738 | 2025-10-14 04:25:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 60bdd38e-883e-3fcb-88f2-44b7a58bf671 | -10.33881 | -47.75898 | 2025-10-14 04:25:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08ddff81-b7bc-32e1-b44f-6480f1cfc67f | -8.43775 | -46.18636 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 430e2155-abbb-38b6-a870-c4c155c3e427 | -7.67736 | -42.37955 | 2025-10-14 04:25:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e28f88a7-d049-3d42-9426-58aeb421c3ef | -12.85389 | -43.81648 | 2025-10-14 04:25:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7cdcdfaf-d60a-3f8c-b85a-556739fe8a6d | -7.75082 | -45.71392 | 2025-10-14 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30f81616-abdf-38cf-829c-aa327acddb2b | -8.43168 | -46.18185 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4abc7549-5e28-345d-ac0d-ea188670713e | -7.30924 | -46.68534 | 2025-10-14 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 66c2bfdd-3b51-3329-ac7e-daab442862a8 | -8.44375 | -46.1481 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3679716b-c4f9-3684-bd3d-d3315d65fd26 | -12.81898 | -50.64689 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4ac7339d-57fc-3897-addc-e5f4c4ab4bac | -7.7481 | -45.7314 | 2025-10-14 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f77def5-8a06-3725-8f92-efb23d186d0c | -7.42089 | -45.41396 | 2025-10-14 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 749282fa-f8d7-34dc-828a-9f4696632ec8 | -12.6831 | -38.55662 | 2025-10-14 04:25:00 | NOAA-20 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 17b4eca1-2ea7-3f48-bfd2-2a90921a75b2 | -12.7942 | -50.65268 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3f9544f2-a4f1-3a2d-b9d5-2f4c492f76a2 | -8.43503 | -46.20375 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abcb2ff2-686a-3631-84fc-9056aeb1163c | -7.43421 | -45.41606 | 2025-10-14 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2702dd3-f190-3b31-afd2-a882d659244c | -12.80608 | -50.63599 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2df12e5b-50cb-3f57-b322-91100df7f680 | -12.61349 | -48.30384 | 2025-10-14 04:25:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e15bb5c-2c91-3be2-9299-03bf7ee4d216 | -7.67614 | -40.40886 | 2025-10-14 04:25:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ea928614-9584-3e25-819b-4f1d5308037a | -12.84549 | -50.64296 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10afff7d-4e35-352e-ac9b-7dc95340294e | -8.43717 | -46.16846 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ba3402c-6f39-3c04-a08b-83794e2ce870 | -12.85194 | -50.64842 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24281a56-773a-31fd-b963-ddf71908d59b | -8.4476 | -46.14512 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a17386cb-4e79-35de-adb4-577c70e71416 | -8.45458 | -40.54978 | 2025-10-14 04:25:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 84b9a8ce-b223-3d7b-be8f-8753a8369032 | -12.82973 | -50.6488 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6975b5b2-b6fc-3ed7-86f6-79c1b164cdda | -8.54748 | -44.58743 | 2025-10-14 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a1d10cd-4420-3b30-ad15-f0496c10bd02 | -12.20869 | -51.031 | 2025-10-14 04:25:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 132aeb06-d353-3b96-81ac-1331490dfe6f | -7.74524 | -42.44415 | 2025-10-14 04:25:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 40a62791-3041-33ef-9413-403003a3a88d | -8.43331 | -46.17142 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f5957b3-4fa4-3705-8aa0-4fe0459ccd57 | -8.43448 | -46.20723 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28ff7d10-b7a3-31b0-bd52-b9e49aa94e1e | -12.7949 | -50.64848 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 23bf59c1-e730-3640-85f3-8b19c299ea9f | -8.44052 | -46.19036 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01c1d571-b596-3434-8383-f02c483d5cf4 | -7.91263 | -47.2296 | 2025-10-14 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4994a0c-8d2d-37de-a019-c3dee91bdd04 | -12.22786 | -51.02985 | 2025-10-14 04:25:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6f86a223-86d3-32ad-880c-dce37f49a53e | -12.85623 | -50.64487 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 678d126f-a64a-371c-bccc-7e2f236dddf5 | -7.92874 | -44.12521 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a07cba62-f331-354a-9781-710939f39274 | -7.92298 | -44.11647 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e031b30c-d868-3d18-84d1-0be9abf16913 | -12.89726 | -44.60386 | 2025-10-14 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e55a6286-e17c-3a88-800c-60389cd02849 | -7.50307 | -43.06392 | 2025-10-14 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 3af5be55-e1c2-37f6-917a-45f940e2737b | -7.75251 | -45.72494 | 2025-10-14 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16a5927f-6614-37a8-a30f-926c1583c2f0 | -8.43834 | -46.20427 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea56faab-7408-3a71-9539-7bd9cd677ac2 | -7.49574 | -42.14793 | 2025-10-14 04:25:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 13e1a3b5-9112-3a69-be73-2c336acf72e6 | -12.99519 | -43.99738 | 2025-10-14 04:25:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 523ff69d-d854-3bf6-9b26-240404c27bae | -8.43343 | -46.23555 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 41e6a201-11c0-39c6-a7f1-eabe2e622e7d | -7.30926 | -45.75816 | 2025-10-14 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e11b7b1d-43c2-3d64-b719-5dc935a8f07a | -7.75219 | -44.72559 | 2025-10-14 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d570671e-4df4-3cea-a22d-e1334ac17452 | -11.52282 | -43.50754 | 2025-10-14 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac1682fa-1013-3cb6-83e5-ece4d7a49854 | -7.75473 | -45.73245 | 2025-10-14 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80ddd9ab-0d90-313c-9f63-c7eb1ffe5dbb | -8.54471 | -44.58429 | 2025-10-14 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19b6f2bd-7bff-3c5b-b597-580236410714 | -12.79061 | -50.65205 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5aa962cd-c97a-31bc-aaa8-cc46e07fe662 | -7.16738 | -42.19732 | 2025-10-14 04:25:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8880536f-2d69-3e9e-b634-658965624a29 | -10.73376 | -42.7207 | 2025-10-14 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fe7168e-6c3f-3861-8b7b-07895f51cd6a | -12.81181 | -50.64562 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 18726908-c169-38be-8b21-c21e2b18083b | -14.47852 | -41.45636 | 2025-10-14 04:25:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5596c4e0-4fa7-3101-8700-781caa0b282b | -12.81037 | -50.65401 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bbca0881-4f45-3975-86b8-58bd89ae81ef | -11.74064 | -43.2883 | 2025-10-14 04:25:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ad14dbd6-a60d-342b-9d69-ba7656a79897 | -8.43997 | -46.19382 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b600fd90-e0cd-31e3-b442-587b40842b9a | -6.88524 | -44.6907 | 2025-10-14 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01f53069-5f84-376c-9d7c-99f671af5552 | -12.04288 | -54.2472 | 2025-10-14 04:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8fc0bc5-cf5c-3509-8bc4-40eba1f14f12 | -11.29344 | -44.0245 | 2025-10-14 04:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ae3ad122-25ce-301c-9de2-5bcc734e2d86 | -8.44496 | -46.20529 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 513d2b5d-981c-3b7f-a1bc-98269c36fe30 | -8.43662 | -46.17194 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd59e4cd-e5c8-3d5a-92b7-87cba66917fd | -12.83761 | -50.64588 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ba4d6f62-dcc6-33cb-9383-2f9905185742 | -7.75192 | -45.70691 | 2025-10-14 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0503c2c3-be2e-33aa-9375-a10a87f6cb7b | -12.63106 | -44.11977 | 2025-10-14 04:25:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 002a0b86-4e66-3797-91e3-d732c968df0f | -7.94497 | -44.11196 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 98690710-bf90-375c-a122-fd0ca3427f36 | -13.54045 | -43.0121 | 2025-10-14 04:25:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 12a41a3c-8e72-36f5-b1b7-9394ab279081 | -7.4174 | -46.70977 | 2025-10-14 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d6586550-a2ab-3ff2-b30f-3f37794e48e2 | -7.69442 | -42.37059 | 2025-10-14 04:25:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 58570fe0-381c-3f22-a868-f0847eec837d | -7.91265 | -47.20798 | 2025-10-14 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| de1575cb-cf70-3d4a-8a4b-c309528748da | -7.1535 | -42.49974 | 2025-10-14 04:25:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 874cb926-f962-37fe-9c7a-569a99dc1ab6 | -7.41796 | -46.70631 | 2025-10-14 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c20c3f7a-77fc-3f0b-b677-ed944cdeeecc | -7.84197 | -41.76474 | 2025-10-14 04:25:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0887836a-287a-3197-ad5e-123d03a6f41c | -12.80536 | -50.64017 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f20bdfc5-2c6e-3c9c-8655-efe60222c4cc | -12.8576 | -43.81704 | 2025-10-14 04:25:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 418bf3be-7a5e-3abd-84c4-6d8af6373430 | -8.42946 | -46.17439 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fde6e012-ae4e-36bc-a875-8fd9cb05e876 | -12.78991 | -50.65625 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fba3a374-d372-383f-bc7b-31f6c019945a | -7.43505 | -42.96877 | 2025-10-14 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| fda62e91-5958-3c0c-8992-7d4d42d8b5d0 | -7.93744 | -44.11475 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13c2b5e2-5f20-32b0-9840-e142919a66b9 | -7.45489 | -45.95585 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e96c1d38-4323-3091-afde-5d9c852a80b4 | -12.80178 | -50.63954 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a1e4138f-73d2-38b8-8910-a1a210904b21 | -9.33031 | -40.87749 | 2025-10-14 04:25:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f804cd96-b666-36a4-ac14-d4c5472427d4 | -7.45104 | -45.95879 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README34.md)
