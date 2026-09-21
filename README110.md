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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68cf41f5-4d93-3113-886d-aa660938abbd | -9.97784 | -50.25988 | 2026-09-21 07:01:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 49339414-b105-3c05-a9ad-649d153edfc4 | -7.24645 | -55.60785 | 2026-09-21 07:01:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 9e02d490-260b-393e-8c3e-c245ee0d5452 | -7.43123 | -44.76445 | 2026-09-21 07:01:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 814ca9ce-7bdb-3360-92e1-cb931931ff9a | -9.4532 | -45.39466 | 2026-09-21 07:01:00 | AQUA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 09adf42c-d2b8-35d7-819f-bf68d5ec236e | -3.39098 | -50.43743 | 2026-09-21 07:01:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| a764f953-0ad6-3bef-a89c-fb7dcb4ec25d | -7.41749 | -44.77629 | 2026-09-21 07:01:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 15f3e758-e82a-347e-aa90-5e26bd641b97 | -5.76461 | -57.58038 | 2026-09-21 07:01:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 57e4d978-00bc-39e8-a33a-b2ca4cdcb3a5 | -4.40703 | -55.23762 | 2026-09-21 07:01:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6ff4a856-a05b-371e-a7cc-c33d52698422 | -7.41833 | -44.76255 | 2026-09-21 07:01:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 27.0 |
| d362a5af-ad8e-3f62-8481-18442feb1e51 | -10.42389 | -50.24244 | 2026-09-21 07:01:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 9a94fdcb-eae0-353f-a2dd-fb73c51d9a24 | -7.42036 | -44.75558 | 2026-09-21 07:01:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| b7c5a347-3084-35a4-a0b7-d6d8ce6622b6 | -6.45763 | -59.97858 | 2026-09-21 07:01:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 02398e74-f155-31a5-8eb0-bbeaee00dd88 | -6.46068 | -59.97416 | 2026-09-21 07:01:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 24.2 |
| be64a348-2a60-3e40-a4f9-027be75f4d2a | -8.17257 | -54.76485 | 2026-09-21 07:01:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 90eeb274-af2d-39d9-9398-9533d378b9a2 | -6.35875 | -45.92212 | 2026-09-21 07:01:00 | AQUA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| cd00126b-365d-33ed-b162-427de05edf20 | -4.3522 | -55.64983 | 2026-09-21 07:01:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 7486cae4-cbe9-3005-8fd6-f0706089a55d | -10.48438 | -51.28074 | 2026-09-21 07:01:00 | AQUA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 9e5897ab-28b1-34c7-8ed7-9033b05e7d51 | -4.34111 | -55.65728 | 2026-09-21 07:01:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 9c5b8daa-ac6e-3b20-83fc-eea0d5938ffe | -6.19691 | -57.76072 | 2026-09-21 07:01:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 7d49b31a-fe6a-3cf8-bdc5-9ca868455f1e | -6.72633 | -55.07826 | 2026-09-21 07:01:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d84e5637-df14-3860-be62-897ed6554e0b | -8.79745 | -48.74161 | 2026-09-21 07:01:00 | AQUA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0d75055b-01a1-358f-aec7-cf1065953f9c | -5.85477 | -49.78052 | 2026-09-21 07:01:00 | AQUA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0bc5fbee-2008-31bd-89ec-fad166596494 | -5.21401 | -56.10463 | 2026-09-21 07:01:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 7dbba3de-5136-3da3-8838-d74108c0c34c | -7.56664 | -57.67069 | 2026-09-21 07:01:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| d7b13521-aec4-3312-9fc9-d5522ddaa881 | -9.26045 | -46.18255 | 2026-09-21 07:01:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 171fcb38-c100-3e88-b7c2-95e688d15f91 | -7.32228 | -55.20285 | 2026-09-21 07:01:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| fe572b1b-d701-3805-842d-abad72724248 | -6.19356 | -57.78146 | 2026-09-21 07:01:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 62169baa-bc61-3010-98c7-1a5734c19ecf | -7.05641 | -49.90548 | 2026-09-21 07:01:00 | AQUA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 9bf1c92f-0c4c-3380-a6a5-380ca5d22fd2 | -6.36224 | -45.91551 | 2026-09-21 07:01:00 | AQUA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 43ba0245-b0b4-3510-87fa-0dd1f462146d | -5.87684 | -53.62889 | 2026-09-21 07:01:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7f911b27-818f-39c5-b19c-d7a160dcd6f8 | -10.42248 | -50.25204 | 2026-09-21 07:01:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3fe50f92-7dd2-3880-ae31-7282f0c0f17b | -4.0961 | -52.11463 | 2026-09-21 07:01:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 2ca7684d-bd62-33dd-86ef-116b2ea4f1b1 | -3.35939 | -50.44485 | 2026-09-21 07:01:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0ef3641e-6d84-3b2c-8003-29fa9c28b683 | -6.66146 | -50.88562 | 2026-09-21 07:01:00 | AQUA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| caa36705-44b0-3694-9905-8d5d8a4cc026 | -6.18968 | -57.78811 | 2026-09-21 07:01:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| ae4c4834-04dd-3ad7-ab43-fce6d88bd5fd | -8.17179 | -54.76975 | 2026-09-21 07:01:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e0c32f04-0d68-349c-945a-20db38683b94 | -5.2024 | -56.10288 | 2026-09-21 07:01:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| ad339df2-1b09-3f60-be6a-d9c01afc5541 | -6.56166 | -45.55639 | 2026-09-21 07:01:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 60c689eb-fc1e-3f6f-a561-4b142842f2b1 | -10.47472 | -50.27512 | 2026-09-21 07:01:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| a58068a2-dcc8-3417-a6f2-322f9f65d724 | -8.78617 | -48.75122 | 2026-09-21 07:01:00 | AQUA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 8.9 |
| caa6b59d-c77e-3d7d-926c-9a96f020c490 | -10.46562 | -50.27379 | 2026-09-21 07:01:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 59bfb084-ad44-3772-80a3-c935e252d328 | -9.82429 | -48.44553 | 2026-09-21 07:01:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| a1aaa738-e67d-3c57-8bdf-4ac6e1323b35 | -6.44524 | -59.97147 | 2026-09-21 07:01:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 30.9 |
| db147099-69fd-3ae1-b184-4afd869d3b4b | -10.39935 | -50.21922 | 2026-09-21 07:01:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1f6cddf8-5a73-3a5c-9c2f-99136a27a950 | -5.89321 | -52.09045 | 2026-09-21 07:01:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4c5fc674-385c-3b03-8124-fd8bad943eef | -10.38327 | -48.90829 | 2026-09-21 07:01:00 | AQUA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| dc543084-6845-38fe-af44-745bdc3d895e | -6.1932 | -57.76735 | 2026-09-21 07:01:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| e55e84d9-cb63-3771-9bb7-39fc88a7f6d8 | -10.38485 | -48.89705 | 2026-09-21 07:01:00 | AQUA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 40.6 |
| e0d2cc97-53f7-3aed-b6b2-b0fcd17ff86c | -14.7594 | -48.42702 | 2026-09-21 07:03:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b0be3d04-c748-3bc5-bb4a-469f38fc90f7 | -11.95006 | -46.50575 | 2026-09-21 07:03:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 8b30e3fd-9804-39e8-9978-0defece3c458 | -16.0076 | -52.51815 | 2026-09-21 07:03:00 | AQUA_M-M | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4ef26e31-2312-3753-ba40-29967528a994 | -11.99032 | -58.05931 | 2026-09-21 07:03:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| d79377cd-62d8-37b1-a3df-d75d06bc1468 | -15.45613 | -48.4323 | 2026-09-21 07:03:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 332ed617-9973-3d1b-b8a9-c56950f9f19a | -11.04787 | -54.16019 | 2026-09-21 07:03:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f2b1ec1c-b75c-3b83-8c15-3c854e6a2e26 | -10.74878 | -50.80174 | 2026-09-21 07:03:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 48f086c6-aaea-3f28-8449-669e3806bd1b | -16.39416 | -54.71063 | 2026-09-21 07:03:00 | AQUA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ef771fff-8a94-3738-b843-2e30ded7bcfc | -16.00623 | -52.52737 | 2026-09-21 07:03:00 | AQUA_M-M | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d79c91d0-eafc-3f81-910f-e1e329cb3d4b | -14.65016 | -54.4488 | 2026-09-21 07:03:00 | AQUA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 41d5e07a-f662-30b9-8d47-9785ecae741d | -11.80555 | -49.79998 | 2026-09-21 07:03:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 6fb5cd49-5664-3524-ba77-e4d1867ed1ba | -11.09754 | -51.06634 | 2026-09-21 07:03:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b06d6b73-db14-30a8-8968-6f1c22f32aae | -11.98731 | -58.07657 | 2026-09-21 07:03:00 | AQUA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 0a9bc78d-b36f-3b71-8a31-bbfcbdd53c1e | -16.03101 | -52.4994 | 2026-09-21 07:03:00 | AQUA_M-M | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 133932fb-a4cc-33cb-b30a-4e2c798b1843 | -13.90247 | -48.57766 | 2026-09-21 07:03:00 | AQUA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 19.8 |
| f66f967f-cd58-3cc1-8bb1-d1134a92f229 | -16.04733 | -52.51133 | 2026-09-21 07:03:00 | AQUA_M-M | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 71c10a70-3a64-3ab4-9785-e048213e7e01 | -11.35638 | -51.43039 | 2026-09-21 07:03:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b8aaf6d2-d079-3a51-9f8a-d0f03971e703 | -11.95246 | -46.48761 | 2026-09-21 07:03:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 452703a0-f6df-3d01-a28b-629247afa975 | -16.39266 | -54.7202 | 2026-09-21 07:03:00 | AQUA_M-M | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7fc76629-bc81-3fc0-be3d-fc605bc1c326 | -11.35773 | -51.42138 | 2026-09-21 07:03:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 138f1482-6edc-3598-a014-99df3b8ef4f0 | -10.90203 | -53.97337 | 2026-09-21 07:03:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| d821fdf4-f7e0-3454-8a47-3b6368878d1f | -12.30831 | -49.19329 | 2026-09-21 07:03:00 | AQUA_M-M | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 43f26eae-1994-30ec-bd0a-56635b2757ff | -11.79462 | -49.80907 | 2026-09-21 07:03:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f27a7875-df95-31c7-89d2-472fc47c0ec2 | -11.95639 | -46.49517 | 2026-09-21 07:03:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 8a3972b7-c3d2-3686-846c-f202a429370f | -16.04597 | -52.52053 | 2026-09-21 07:03:00 | AQUA_M-M | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 99a54af5-ae2c-3fd6-9876-f038c171db9f | -10.79901 | -50.77128 | 2026-09-21 07:03:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5b667996-e4d1-3e17-8723-d569fea1e4da | -13.26855 | -51.75312 | 2026-09-21 07:03:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 42765217-1b5e-34a2-82db-316a3a54306b | -12.82713 | -54.03778 | 2026-09-21 07:03:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a20342da-1c82-36ff-a71f-d7169e752114 | -15.45231 | -48.46131 | 2026-09-21 07:03:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f4c3c237-6af5-3d38-8de6-97c5a8de3465 | -15.45042 | -48.47569 | 2026-09-21 07:03:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 25.0 |
| c16d6bc5-2563-351d-a9ee-efd2d6bd24ee | -14.05733 | -52.10565 | 2026-09-21 07:03:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bd1bd7f9-ee0b-3577-9b20-1ee1c8725b66 | -12.76938 | -52.85543 | 2026-09-21 07:03:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 81ac3bee-fe41-3e02-9ee8-669b8bc1360b | -12.77075 | -52.84648 | 2026-09-21 07:03:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| d451c398-01a5-3bd9-a2ae-1a596b023842 | -16.03985 | -52.50076 | 2026-09-21 07:03:00 | AQUA_M-M | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0cf0eea7-7af0-3b34-933e-dd0c55017c15 | -14.04199 | -52.06944 | 2026-09-21 07:03:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5f83ed6e-d2cd-351b-afe7-349d5ae5cf7c | -12.912 | -50.96722 | 2026-09-21 07:03:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 35302e9e-fd57-3950-a4c1-06d6a4781697 | -11.80408 | -49.81043 | 2026-09-21 07:03:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 1c14418a-8989-3487-872a-e054ed52668a | -11.0403 | -54.90471 | 2026-09-21 07:03:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b46411bb-0a73-305b-98f3-1a39ecb4e299 | -10.80797 | -50.7726 | 2026-09-21 07:03:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 98ed5783-838c-3287-b138-5d533a3ed2a9 | -11.47126 | -47.76348 | 2026-09-21 07:03:00 | AQUA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 1bc7e12e-ba8b-37bd-9f17-1d164f27ac6c | -10.85167 | -50.15704 | 2026-09-21 07:03:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8b5e9ed5-e7f7-3b90-97ba-c68cfa9c2478 | -10.91428 | -53.95538 | 2026-09-21 07:03:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 88fa4b80-d923-3723-af53-4969ea1e63e1 | -16.03849 | -52.50997 | 2026-09-21 07:03:00 | AQUA_M-M | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 03fce963-ea3d-3fa5-a4e3-799a37f66106 | -10.80038 | -50.762 | 2026-09-21 07:03:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| d3c53acf-c506-3db4-93da-e3631ff577f5 | -14.05598 | -52.11478 | 2026-09-21 07:03:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 902fd002-a16d-3ad1-8e39-0ccebcdaf136 | -13.9131 | -48.57883 | 2026-09-21 07:03:00 | AQUA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d7cbfe98-faa1-38f0-ae71-872c3050fb52 | -16.02965 | -52.50861 | 2026-09-21 07:03:00 | AQUA_M-M | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| ca70153c-ca40-3fc6-87e8-458ddd4be5d1 | -14.92363 | -49.89091 | 2026-09-21 07:03:00 | AQUA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0f03bac5-0055-3a57-872f-1c9481304b28 | -10.80934 | -50.76332 | 2026-09-21 07:03:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 28.6 |
| c97a08d0-5267-36c5-8427-871f786aca67 | -12.83464 | -54.04874 | 2026-09-21 07:03:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 86b918c0-294f-37cd-9329-4b543aaf9db0 | -12.30992 | -49.18179 | 2026-09-21 07:03:00 | AQUA_M-M | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 5b8a2b63-1389-3ad8-a43e-673dca1cb387 | -12.82562 | -54.04727 | 2026-09-21 07:03:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |


[Clique aqui para ver as próximas entradas](README111.md)
