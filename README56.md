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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b84bc0c-d5d0-35f5-8a01-7955e017d72d | -3.3818 | -61.3044 | 2026-09-16 05:33:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 447e0d60-136e-3451-b122-c0016327e72c | -3.75746 | -51.14632 | 2026-09-16 05:33:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f95ede9e-43ae-3845-9bcd-6581c16a4dd0 | -2.95802 | -50.40101 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19cd20d5-e651-319c-8eed-3b5b2d3fc9a3 | -3.68483 | -54.17555 | 2026-09-16 05:33:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 85783d61-8c0e-32b0-98c3-3ca2a89bf487 | -2.96477 | -50.39398 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30a519af-f15f-3840-911c-f4f47ed77ef5 | -5.13408 | -55.93767 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32c0cc6b-abc5-3857-b73d-d25ba591fc34 | -2.7105 | -57.60875 | 2026-09-16 05:33:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 548f09f3-e602-3978-b6aa-fb7fd2143704 | -2.82027 | -51.34186 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca47b9a9-fb7c-3cab-a086-6e5aebef3c64 | -2.91223 | -50.40831 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b848713-6019-3118-8eb7-02b0a7f79768 | -2.77249 | -51.36787 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f6c0733-5543-3c8d-a25b-4c794bffc8bd | -3.45627 | -57.9884 | 2026-09-16 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 747b09a1-dfd8-3c30-8c03-934c5a5da30b | -4.54248 | -54.93268 | 2026-09-16 05:33:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc018e01-b420-3f51-aaa1-625d564219ec | -5.14328 | -55.9291 | 2026-09-16 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 65724cf2-e256-33e5-bee9-960c0d07b427 | -3.1072 | -57.67954 | 2026-09-16 05:33:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8ccde71-3307-3955-8a8d-e39153b46697 | -1.28104 | -55.71381 | 2026-09-16 05:33:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcffa67b-07dc-3408-961f-4a71eb4a8eb1 | -3.84829 | -51.76648 | 2026-09-16 05:33:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52293139-b5a5-3c2f-bb82-2947b984648f | -3.31376 | -47.13713 | 2026-09-16 05:33:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c477f871-6595-3d79-b190-0234fd2438c7 | -5.88458 | -52.0889 | 2026-09-16 05:33:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34b6b2aa-e7de-3e25-a3dc-678a1086da13 | -3.38097 | -50.39117 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c258aacb-4336-3b6a-ba78-0009be1d93ef | -1.74219 | -55.25891 | 2026-09-16 05:33:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c00acac-b1fc-3bb0-bbc7-3f22b9ae5066 | -3.05359 | -57.14573 | 2026-09-16 05:33:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 642a03a7-2dae-34eb-8a1d-a1547abb7b34 | -2.90521 | -50.4179 | 2026-09-16 05:33:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92752bf6-eacc-3a99-b6ac-e6248313eb48 | -2.26284 | -57.0864 | 2026-09-16 05:33:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 08cf36df-02dc-3d9f-8c2b-2acf91658a24 | -12.12023 | -57.18632 | 2026-09-16 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| de5db7a0-828f-3935-ac9d-e5dfe31acfa1 | -11.19068 | -55.03643 | 2026-09-16 05:36:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3de62d75-2cc9-3e09-86e2-a84d205cb17b | -12.11161 | -57.19023 | 2026-09-16 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2737bcef-fdc1-34c6-a6a6-40b644ad0844 | -9.7992 | -60.47622 | 2026-09-16 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd5aae2d-7f00-3c01-83aa-5a0699703a59 | -6.13168 | -59.88604 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1409dc65-78c9-3b10-a79b-8029cd16115f | -7.05948 | -59.22538 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94854abd-e5e1-36d4-894d-69b8a329f340 | -11.19131 | -55.03195 | 2026-09-16 05:36:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b473e9b7-d879-3dbf-9123-8639f62d9030 | -6.33859 | -62.68321 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f989f523-1a09-3276-af8b-b18dafda8f37 | -9.05689 | -65.93089 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8af48e5a-8336-3303-acde-a7bf5bf73475 | -9.06377 | -65.9248 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06e9baed-a403-3f1f-8e9d-892c656e1cec | -6.81374 | -59.1687 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f28cd0a7-3bd9-31be-99b8-198c847e3d82 | -6.33452 | -62.68645 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9da72436-dc69-3f82-a6ed-81a88c6cf43e | -10.40089 | -48.63998 | 2026-09-16 05:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6f7b0ad-21c9-3284-85f9-dd6d7a14c26e | -12.11485 | -57.19591 | 2026-09-16 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b57499a7-1726-344a-97b9-b2316530d3d7 | -10.69433 | -54.17296 | 2026-09-16 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| baedeb54-25ed-37aa-b0ac-1f619421cf12 | -9.08998 | -61.00967 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f6639c8-6f33-320a-aadb-5510d58931ae | -10.69908 | -54.17356 | 2026-09-16 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9b087cd3-316d-34ba-8283-d1f5b50b6437 | -9.84694 | -48.35537 | 2026-09-16 05:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 882462f7-391b-3e4d-8ea5-2fbc19c151a1 | -6.33167 | -62.68209 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 011a9754-b141-3e49-ad3b-3893e2f4f72d | -6.79621 | -58.78672 | 2026-09-16 05:36:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e56e3b4f-26d5-3ea2-92c8-91be4ef46e3a | -7.61213 | -57.60868 | 2026-09-16 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ad3c3e0-efb8-3f6a-9ca5-98672571f80d | -6.33391 | -62.69025 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8226e25f-3f44-33db-8a3f-aae9d0992a57 | -9.71052 | -64.97237 | 2026-09-16 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 609bf215-3a6a-3c81-980c-135ce79fd1e9 | -6.81035 | -59.16817 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df44629d-ca0e-3f8a-bae9-55b1d1f27153 | -10.2591 | -57.69684 | 2026-09-16 05:36:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 45db3926-3c75-3c62-853e-e142423c381e | -12.62361 | -50.77251 | 2026-09-16 05:36:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 866d410e-2858-3a54-9a8d-52cf5570dd18 | -9.02401 | -61.03854 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce13f540-87c4-3410-9d83-efe935629d25 | -12.62469 | -50.76321 | 2026-09-16 05:36:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| ecb90f32-f797-38f8-afcc-69897127c63b | -9.08942 | -61.01316 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c260732-ff44-3385-8da2-0003ba4166b7 | -7.6115 | -67.25031 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db695797-cecd-3467-aa6b-56514b4065f0 | -6.80584 | -59.17489 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2435828c-d07a-379e-8759-88c7dda975fe | -6.28741 | -59.92454 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e51ded0b-21d2-3716-8c15-c7ee01d36c00 | -10.41282 | -48.65525 | 2026-09-16 05:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4376b6ab-4bf6-316f-b13a-bd479b50195a | -9.71212 | -64.91791 | 2026-09-16 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a218bf41-6a5e-3d26-9ce4-7024cc646d67 | -10.93868 | -54.08913 | 2026-09-16 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0ba47fd-a6b0-393f-88ea-524a49b89884 | -9.83413 | -57.7052 | 2026-09-16 05:36:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2697978-3639-391e-845d-3107aa6ff171 | -6.13113 | -59.88955 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8042de07-db77-3d4a-95d8-b172811332d9 | -6.11292 | -57.69907 | 2026-09-16 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec7189ec-4d08-3518-8171-f2edbecefd6c | -6.11889 | -59.88044 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d7862e55-965d-319f-b050-a1f6e2a94b3d | -9.79474 | -60.4828 | 2026-09-16 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79f34a61-dffd-3895-9c8c-3403996ba01f | -6.13744 | -57.68211 | 2026-09-16 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27bbcddb-bec0-3a17-be34-e79d52c6624f | -6.32759 | -62.68533 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b9b87638-12c0-34ab-9721-d7a31f06b5c4 | -9.62365 | -61.82447 | 2026-09-16 05:36:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f869d82-1ff4-3134-89db-246ddc2dcf28 | -8.37428 | -54.72694 | 2026-09-16 05:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdf7ba31-a977-3e7e-80c6-81def65a7cab | -6.71719 | -58.80162 | 2026-09-16 05:36:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f07a9068-d4ef-316b-aaed-73116e08594b | -6.57111 | -58.95699 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c77d74e7-c57a-3466-842c-34d48df42d6e | -7.63803 | -67.17506 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64f47192-18db-323c-adce-bd6aaa160c8d | -9.81252 | -67.55828 | 2026-09-16 05:36:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9b0e50d-ceea-3c81-b5f8-62fb767338f6 | -6.80979 | -59.1718 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1e974cb6-df6e-3b88-96ec-f27da74ac742 | -6.4472 | -60.01113 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 162b7316-296f-3f9a-b10b-8e2cd4e15ff2 | -7.65216 | -67.16666 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0c91073e-ae1a-363b-8e7b-4ed7e67ec7ad | -6.62893 | -58.37583 | 2026-09-16 05:36:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2c1ffb5-dac3-3154-adf4-521718dba8b2 | -11.47363 | -62.46385 | 2026-09-16 05:36:00 | NPP-375D | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb69328f-55c7-3c89-bc3d-57b91f62ca5f | -6.3443 | -62.69195 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8d4f7301-e59f-3eee-a1b6-f54889d4302a | -8.60213 | -64.09765 | 2026-09-16 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 30be0776-93ce-3da7-a245-46bb6bb171f6 | -10.47596 | -50.96339 | 2026-09-16 05:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2525af36-c500-3008-a332-41ebaaa94dbe | -6.33228 | -62.67829 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 96279a5b-1c15-3d37-b32d-b0924ef957e7 | -9.06966 | -65.92786 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a31c8496-8261-3c92-9cd3-20eb9ebd38a0 | -9.06997 | -65.93648 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7eb076d-088f-39ce-9975-6a611e033cce | -9.14158 | -65.84117 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d7f4c73-e307-3ed2-b1d7-265b85c44989 | -7.05892 | -59.22901 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1457ee26-4045-3650-8d9a-80a1e83f9ff4 | -9.09608 | -61.01423 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f389a8c0-0ea5-315f-b60a-ffd517077420 | -9.91913 | -60.46564 | 2026-09-16 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8c7da11-af0d-3916-8b33-0293c50e050a | -9.39128 | -60.31741 | 2026-09-16 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1e0f019-91cd-3e33-b5e1-a351a4c18c87 | -6.33513 | -62.68265 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d5c1c409-2df2-356f-94d5-c081d291f252 | -9.2536 | -60.2849 | 2026-09-16 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f7f7261-2871-36f5-8589-66a6743f5911 | -7.63949 | -67.16649 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c5813b5-7b4e-3567-b577-19765884d915 | -8.53971 | -64.00661 | 2026-09-16 05:36:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 447911ff-fdcb-33e7-a4c0-4d950ba836ce | -12.62415 | -50.76786 | 2026-09-16 05:36:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 01a58c18-7286-3583-86d8-cbcf22ca2acc | -7.64462 | -67.16296 | 2026-09-16 05:36:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 79debfa6-7793-3394-9290-45637ae0a7f0 | -6.81318 | -59.17233 | 2026-09-16 05:36:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3385578a-35b0-39d7-89d0-8e9ad899c064 | -12.13282 | -57.18295 | 2026-09-16 05:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fb44a87-b907-3a73-9d3d-b0a70f3f8c97 | -11.26811 | -54.12864 | 2026-09-16 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b1bdfb0-58cc-3462-9d08-c2aece92347a | -9.38624 | -60.30566 | 2026-09-16 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9f01f9de-ee23-39da-96d9-879ba0a3746b | -9.05778 | -65.92578 | 2026-09-16 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 46edd20b-f0d1-35ea-b7e3-3c3b77c98126 | -6.34369 | -62.69575 | 2026-09-16 05:36:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b5f20999-0f17-3ab8-b164-04aa408d1544 | -6.44775 | -60.00763 | 2026-09-16 05:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README57.md)
