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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df675d2d-58ed-3331-9d7a-20da7317a83c | -8.02022 | -49.68501 | 2025-05-28 04:10:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de51c517-7050-3d9c-9b67-6afd2fd99301 | -7.62877 | -45.7649 | 2025-05-28 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2b3cfaae-4dc0-3003-989a-b52cced69a00 | -12.70364 | -40.18195 | 2025-05-28 04:10:00 | NPP-375D | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 82e8bb24-c86d-3409-b1fc-46b66115ad88 | -8.79046 | -47.94066 | 2025-05-28 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0719d2c6-4c82-3587-902a-3702e195a7f6 | -13.07843 | -45.27962 | 2025-05-28 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 059b00d3-26a6-327f-a323-16b71b0de3ee | -9.15371 | -49.65176 | 2025-05-28 04:10:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 22d6e479-ddd9-3827-87f9-c0448e194cef | -15.10826 | -40.94621 | 2025-05-28 04:10:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| db06e06f-aa6e-3222-90c9-c0aa247d09f1 | -10.6609 | -44.41233 | 2025-05-28 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09aea805-b3c8-3cf5-868f-fd59949b2261 | -11.76765 | -47.26536 | 2025-05-28 04:10:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df85820c-3cda-3938-b5eb-20b07d069e1f | -11.56503 | -47.62659 | 2025-05-28 04:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4817c0e7-70e5-3ad4-aa84-65de7285c4a0 | -10.46801 | -47.94754 | 2025-05-28 04:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f3421d8-1704-33df-8c9e-ae3df4dcdc16 | -10.95179 | -48.14402 | 2025-05-28 04:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5830983b-b4fc-38d9-9977-e3ee1f90ec7c | -11.29969 | -53.98433 | 2025-05-28 04:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d342138-b73e-3f43-a457-3be957fcca41 | -9.19499 | -49.47233 | 2025-05-28 04:10:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 06af0a13-8fac-32fe-bd28-323fe273ceab | -8.01717 | -43.18446 | 2025-05-28 04:10:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1d6e26f5-559e-345d-919a-a2d0ccaff65c | -12.25249 | -53.28266 | 2025-05-28 04:10:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9cc27f5e-5029-347d-8e98-799d2396f053 | -9.60674 | -49.02813 | 2025-05-28 04:10:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20892e18-f93f-34e1-9a53-4d83514c0306 | -11.81209 | -44.27397 | 2025-05-28 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 5edf6db8-4758-32b8-9e66-2101b1a0e42e | -11.81888 | -44.2751 | 2025-05-28 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| ac412595-c713-33c7-a544-ce2e5cabe7d9 | -13.07778 | -45.28348 | 2025-05-28 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12b48f7a-4f40-3513-a22b-72dbba955766 | -11.57391 | -47.62275 | 2025-05-28 04:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9e51443-889f-3112-b421-8faf9b973166 | -11.91759 | -54.42476 | 2025-05-28 04:10:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87dd4e04-67dc-34f9-8f59-e2949ed30e04 | -13.87753 | -43.79532 | 2025-05-28 04:10:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9803224e-b657-32c7-96c2-18b4d2444332 | -10.95271 | -48.14308 | 2025-05-28 04:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62b84171-18aa-3a5f-9c63-1f6a4b153f11 | -10.45361 | -47.94567 | 2025-05-28 04:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6750d433-84ef-33d3-be42-460af29b300f | -11.14026 | -53.92784 | 2025-05-28 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 960ea0fb-bea6-33ae-a855-8cfb15eacffa | -9.51122 | -47.69405 | 2025-05-28 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8cfd167-ac33-3fc7-aa07-51bd24cfddcc | -8.00731 | -46.15884 | 2025-05-28 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dde2a104-ca42-3422-92bf-032c19e540f9 | -7.99653 | -46.1525 | 2025-05-28 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7e26889-9ae4-312c-81d9-6d27db144d4b | -10.7328 | -49.29406 | 2025-05-28 04:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3bc72cb9-2a7f-3262-b1f5-e71a94bf7556 | -13.37646 | -47.93543 | 2025-05-28 04:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f9bfefb-be97-3302-b863-6835cbd78b70 | -7.62575 | -45.75973 | 2025-05-28 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6c52951a-1c2d-3bf7-b402-7bd82973c465 | -11.82286 | -44.27199 | 2025-05-28 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cde4a551-d89b-3019-8307-2cc8c71f5a25 | -9.20076 | -49.47476 | 2025-05-28 04:10:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6f15ab53-4070-37f9-ae2a-321e133ffa0e | -7.67099 | -46.08665 | 2025-05-28 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 751abd4e-d982-36fd-94d1-19a993f818cd | -11.81608 | -44.27085 | 2025-05-28 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 20625a81-5021-39a6-9d9f-1801fb2b4bb6 | -10.47214 | -47.9483 | 2025-05-28 04:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1d469677-95fb-31fd-b433-44cdddab5dd2 | -12.40934 | -50.00092 | 2025-05-28 04:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10b17b4f-2916-3cac-b3ab-a374506951d5 | -10.66319 | -49.44781 | 2025-05-28 04:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4c29bde1-4d7b-373e-b562-25035ed5f87e | -13.93048 | -43.14647 | 2025-05-28 04:10:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a447a96f-ee26-34ba-b926-2ee950c6c432 | -9.89954 | -44.8024 | 2025-05-28 04:10:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ef3b6e0-5141-315d-80bf-1994d2ddce96 | -11.29331 | -54.01624 | 2025-05-28 04:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0eac4214-13cc-3f21-97e0-495642f2cb9e | -12.11457 | -54.66825 | 2025-05-28 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48c8ee9c-054d-37bb-a160-652bd7044b57 | -9.89946 | -44.80552 | 2025-05-28 04:10:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea188c43-5f7d-33ee-b589-9d345caee9df | -11.40011 | -44.82991 | 2025-05-28 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 99d2d19f-72b9-3f83-a437-9a57fd204c34 | -12.29055 | -43.54464 | 2025-05-28 04:10:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8b2a4ad5-06cf-3d9a-ac19-23ba647bd943 | -7.7815 | -43.71277 | 2025-05-28 04:10:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7c2f74eb-a318-3fde-8e4b-32016c59afc8 | -15.80098 | -43.57095 | 2025-05-28 04:12:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17b355ca-8eda-374f-a2dc-616e99eaf181 | -15.80488 | -43.56792 | 2025-05-28 04:12:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d98b826-a452-3895-887e-f875e14fd858 | -18.85732 | -53.62121 | 2025-05-28 04:12:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b38c3902-a2af-3df3-9284-94cd73047f86 | -15.69505 | -43.42441 | 2025-05-28 04:12:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e2aea25-e7f9-3887-8943-ea5a76583449 | -15.91613 | -41.37017 | 2025-05-28 04:12:00 | NPP-375D | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4cb676e9-b136-3e78-bc26-475a6fa6cd1f | -17.27868 | -42.64753 | 2025-05-28 04:12:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37176b0e-59f6-3842-9b7d-d9262fc22f9b | -20.34958 | -40.36118 | 2025-05-28 04:12:00 | NPP-375D | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 047c695d-cb79-3f16-ac15-d5741011a97a | -21.18126 | -43.98043 | 2025-05-28 04:12:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6ff7401e-5a87-3eba-be25-1f617ce9347f | -17.59582 | -43.198 | 2025-05-28 04:12:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1349ffd7-224d-3cd3-b163-458af3becc01 | -17.27847 | -42.64827 | 2025-05-28 04:12:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d4af73e-8012-3eb9-ae3a-1c29bd60c86a | -18.83812 | -53.61016 | 2025-05-28 04:12:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53efd5a3-d049-3a6c-adb0-670ad288aecf | -15.16915 | -52.29535 | 2025-05-28 04:12:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e1ac9701-9394-309f-835a-403eebe3cf45 | -16.75031 | -42.47644 | 2025-05-28 04:12:00 | NPP-375D | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dffd6684-2004-340c-9944-764567e71a93 | -15.69894 | -43.42137 | 2025-05-28 04:12:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48d9ae55-fb85-3804-ad52-bd9f4bcc2001 | -18.83743 | -53.61348 | 2025-05-28 04:12:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18ddb9e7-ea65-3c34-8ed6-2b5750f2def9 | -17.27811 | -42.65134 | 2025-05-28 04:12:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 49168e78-1242-3e06-b8f2-fb6c6ab8071e | -16.0411 | -43.80183 | 2025-05-28 04:12:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 616abfac-9d55-3d5c-ab39-579bd543ed17 | -17.65096 | -47.45803 | 2025-05-28 04:12:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f8ef729-be3d-39d3-bb80-70fe3abf80b3 | -15.08052 | -48.94661 | 2025-05-28 04:12:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e5c4977-0a5f-36c4-9de0-aedecd80a614 | -17.27451 | -42.6515 | 2025-05-28 04:12:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6610382b-72a5-38e7-aa20-bcedbc2dc4a7 | -17.28489 | -42.65249 | 2025-05-28 04:12:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cd5747b9-8b9f-3ad4-a8a5-2aa9217123cb | -17.02488 | -50.29864 | 2025-05-28 04:12:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4db7442d-fc7d-3482-b96d-708aa5b8c403 | -17.67511 | -42.74516 | 2025-05-28 04:12:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3fa9ddb8-e708-3cc3-b530-301eba8f0056 | -15.69561 | -43.42081 | 2025-05-28 04:12:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 947a02a1-e30b-34e7-8c57-66e91a491f0e | -16.62533 | -52.1356 | 2025-05-28 04:12:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d218890f-da2b-3a95-9725-1f24c7bde111 | -16.04499 | -43.7988 | 2025-05-28 04:12:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c06d2f8-b834-34d9-b51c-2b4a25a06269 | -16.60967 | -43.3262 | 2025-05-28 04:12:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c37d6ac-40bc-35ee-a2d0-4122cfefa8fe | -20.35183 | -41.49594 | 2025-05-28 04:12:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9381f079-d908-36b8-9a97-65663915de98 | -15.80155 | -43.56736 | 2025-05-28 04:12:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 954a10b7-ba8e-320b-8cdd-8eaee44ed362 | -17.78032 | -42.80857 | 2025-05-28 04:12:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8f5f4b8-b9c6-38c0-8773-6bf7fc45c38d | -17.2815 | -42.65192 | 2025-05-28 04:12:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f2072e4d-8b15-3cf8-b1e8-6046d2b73abf | -20.57825 | -44.57566 | 2025-05-28 04:12:00 | NPP-375D | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 85beadb0-97da-367c-8cfe-01994f57aa27 | -17.28207 | -42.64811 | 2025-05-28 04:12:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 434acf9a-c217-3e78-8d08-737aab7f6d5c | -15.80431 | -43.57151 | 2025-05-28 04:12:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b0a317d-6001-3034-96ca-04d99cfd7ba0 | -17.95269 | -44.421 | 2025-05-28 04:12:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f73442a-3687-3ffe-bf1b-1b188e185b9a | -15.17424 | -52.2963 | 2025-05-28 04:12:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 055db81a-bc69-36cb-a685-8582d8e1bae3 | -16.04166 | -43.79823 | 2025-05-28 04:12:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6066de91-5c95-3ae6-b3cc-3d7c52adee34 | -17.27789 | -42.65208 | 2025-05-28 04:12:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 27de8a42-c8f9-3fd4-8ecc-3f24b4351ba0 | -17.27755 | -42.65513 | 2025-05-28 04:12:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b4297053-a009-30ed-b713-a51cd4e43e53 | -21.62776 | -43.46589 | 2025-05-28 04:12:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6d2d5f58-dd5a-397c-98f7-6d2fd48caf80 | -19.96048 | -44.85585 | 2025-05-28 04:12:00 | NPP-375D | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8ac3ee45-6e5a-3ffa-9d1f-c851d3d04372 | -20.7633 | -46.76789 | 2025-05-28 04:12:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b4ec6565-dfca-33f8-a24d-2198abd37359 | -16.68088 | -43.88307 | 2025-05-28 04:12:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| caf9ae92-ea31-3bd0-a5ad-80a4e0d2c604 | -18.85661 | -53.62465 | 2025-05-28 04:12:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7c26201-9a25-3db0-98af-176e28deacd9 | -23.40695 | -49.62441 | 2025-05-28 04:14:00 | NPP-375D | CARLÓPOLIS | PARANÁ | Brasil | 4104709 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4d192f4e-b05b-34e5-907d-3d7275b6b59b | -27.45632 | -48.45123 | 2025-05-28 04:14:00 | NPP-375D | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 73552bb2-3358-384f-a8f5-d31f182544c7 | -22.90115 | -43.75348 | 2025-05-28 04:14:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9f98e9cf-864f-3a0c-ba99-fa8086986c39 | -23.01317 | -50.04667 | 2025-05-28 04:14:00 | NPP-375D | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cc407a50-8c02-3fc9-9388-4800468fa276 | -24.39969 | -49.90372 | 2025-05-28 04:14:00 | NPP-375D | PIRAÍ DO SUL | PARANÁ | Brasil | 4119400 | 41 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9439d838-2198-32d8-b61b-a5405be4d33f | -24.08408 | -48.89285 | 2025-05-28 04:14:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a25fd1e3-eba1-3b6b-94e1-6aafbd94f02b | -22.69854 | -43.34844 | 2025-05-28 04:14:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4362150d-5c93-3b6b-84e0-f40c243ce618 | -22.90057 | -43.75743 | 2025-05-28 04:14:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 05293294-e5ab-3fa4-b3e2-1875fc76418d | -23.01412 | -50.04164 | 2025-05-28 04:14:00 | NPP-375D | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |


[Clique aqui para ver as próximas entradas](README10.md)
