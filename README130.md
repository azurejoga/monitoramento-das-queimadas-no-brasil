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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d5baf02-ca0d-33a3-b990-4c37bfccb4d6 | -7.97641 | -54.75866 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ec5325b-1f6a-3457-a2ca-119c8cce27c4 | -7.97595 | -54.76205 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34f4a5b4-39fc-3a29-91d9-7d58a88b47a8 | -7.97549 | -54.76543 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6604dc52-b05f-396c-a749-74c28a0bd1b9 | -7.97503 | -54.76881 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1836141c-120d-35c5-96b6-5780fdf3604a | -7.97457 | -54.77222 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c56ee40d-dbea-348a-bab7-56a6585782fc | -7.9741 | -54.77563 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd8b39b9-cce0-3878-8e96-d06b909f8f33 | -7.97242 | -54.74768 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ee0f592-0df7-3891-ac3f-b2cba94082b3 | -7.97195 | -54.7511 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e32922fd-93ab-3b12-8d59-d0b2c63d4482 | -7.97149 | -54.7545 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60b2280b-a256-341c-a71c-e28b9b6a3cb7 | -7.97104 | -54.75785 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2188de26-fe6c-3463-9471-f03fe10cf5b0 | -7.97058 | -54.76121 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 975ed064-3e3d-3b41-93fc-8c65d17e3cf1 | -7.97012 | -54.76461 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff2e216a-1af6-34f5-8ae6-e7e3264f6463 | -7.96966 | -54.76805 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1963e4cc-7b42-3bb3-9164-892be490742d | -7.96919 | -54.77148 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61cd7c1c-daeb-326f-94d7-287fa8b74272 | -7.96873 | -54.77488 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71f2336f-388d-30de-9211-3a307462bfc2 | -7.96566 | -54.75706 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a08e09e-1a8b-3fd0-9451-75774895e7a9 | -7.96474 | -54.76385 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c039b80c-5f16-3a42-8535-c10e856a3675 | -7.96428 | -54.76727 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db41c7f1-54f8-3eed-908b-a56de3ff7139 | -7.88102 | -54.87919 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a7c59fb-4f0b-3d8a-8b59-0f4132d002fb | -7.87661 | -54.87182 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 93835049-35e9-3f7c-8ab6-646019448962 | -7.87615 | -54.87513 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 050dc561-bed4-3082-9b38-f32e7bb98e13 | -7.87523 | -54.88181 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3114bb60-d35d-3e57-a1c9-9e5fb597cdc6 | -7.87477 | -54.88517 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26ad160c-af96-3e88-a209-ee0891d630fa | -7.87431 | -54.88849 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dcd2709e-08da-33e6-81ec-4ff4a884eccf | -7.86898 | -54.88778 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d519677-6354-3cbe-be27-16287200d557 | -7.86853 | -54.89103 | 2024-10-06 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a2b9258-0b19-3b3f-86f9-5b5713b8ba13 | -1.4647 | -54.96405 | 2024-10-06 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3fa0fe96-eb2d-3445-babe-fc5cd670d390 | -1.46386 | -54.96938 | 2024-10-06 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0bc11c22-81f1-36d7-843c-d6baeebe8f8c | -1.46308 | -54.96625 | 2024-10-06 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dd03d509-1758-3a16-9049-0e714ae9c9ac | -1.45986 | -55.52483 | 2024-10-06 05:33:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 631298b1-707e-365c-9427-13ac050cd12d | -1.45903 | -54.96879 | 2024-10-06 05:33:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9834d1cf-66d6-3f40-9016-bba422211ead | -3.53808 | -55.46202 | 2024-10-06 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 244a1a5c-d765-3be5-826f-5d50ef1f8da9 | -5.08977 | -56.1798 | 2024-10-06 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 688ed18e-7fff-3398-a5d2-60c457df1703 | -4.06231 | -56.31433 | 2024-10-06 05:33:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17cd4250-a3b6-33e1-b7fd-3c88bb342de6 | -5.11562 | -56.26317 | 2024-10-06 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 567fe271-b833-3134-9509-f2d47177fa33 | -5.11097 | -56.26243 | 2024-10-06 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e6ff887-7ba3-3122-97b3-bc6b7176710f | -5.09444 | -56.18053 | 2024-10-06 05:33:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f98b5f6b-d477-3320-b5cb-4a114ce81426 | -1.94348 | -56.65282 | 2024-10-06 05:33:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 69b37113-ed00-35b1-9b61-0226f9f59165 | -6.96476 | -59.06663 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b4e1247-f975-3e21-a673-c709b6966460 | -6.96401 | -59.07165 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 46227382-9ae7-343d-b749-e3c791afd6e6 | -6.96155 | -59.06102 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b490c29a-6f2b-3fff-9e69-fccb8f873b09 | -6.9608 | -59.06604 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7a49ada3-d5d3-381c-9e64-e941977a3f8c | -6.96005 | -59.07107 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d0fb35e6-e81f-3f99-b9d7-186cdd9a8d70 | -6.9593 | -59.07609 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e221e4d2-a13c-3522-8de9-cbae00762f19 | -6.95834 | -59.05539 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2651189c-71b3-357d-8cff-fb4ea385950c | -6.95759 | -59.06043 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a147342f-7718-32f0-be74-f8e5113e9d16 | -6.95684 | -59.06548 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 014783fa-1c10-3fb5-989d-e776df53f18e | -6.95609 | -59.0705 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cd4d51fa-9400-3d41-8a5f-204477c2c234 | -6.95535 | -59.07552 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 31ecd835-06ec-3143-93f6-31bb04244a7f | -6.95439 | -59.0548 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b213d7bb-21f0-3638-a940-eb46e01ffa0c | -6.95363 | -59.05985 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9c6a35f3-1fbe-3c82-9b02-01a262c20dd5 | -6.95289 | -59.06489 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 071fec10-87a0-3044-879a-da2cf91dce53 | -6.94968 | -59.05924 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 63f5720f-e9ab-3e3e-939b-e2f5013ba5ad | -6.94893 | -59.06428 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0beb9c97-7ad8-36c9-a9c3-9e8c561527bb | -6.94573 | -59.05862 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 622ae5da-753e-3ad1-9319-5e93f00ce99a | -6.94498 | -59.06366 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8c897a42-4e90-3b58-9f00-8970c1042dfd | -6.73662 | -59.07031 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8fe63d73-b114-3193-bb27-d4dd2a9ff8e1 | -6.53005 | -58.40257 | 2024-10-06 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 728ebd09-1ba2-381b-a531-69e21cf32e16 | -6.52704 | -58.39461 | 2024-10-06 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5c89cbb-7335-35cb-b03b-691389898d67 | -6.5265 | -58.39827 | 2024-10-06 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bfcad36-8670-3cfe-9b95-6345b17b5489 | -6.52594 | -58.40197 | 2024-10-06 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3531feef-0462-3d29-bbff-ce15bb43aa73 | -6.52539 | -58.40565 | 2024-10-06 05:33:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b428cf21-dbbb-3af8-9694-c66b69abccd3 | -3.52904 | -59.3951 | 2024-10-06 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 093439e2-7add-38b0-ad58-f929508ff8ba | -3.39997 | -59.58029 | 2024-10-06 05:33:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d27dd38c-09d6-315a-a5b8-cc7d42fe2907 | -3.39931 | -59.58454 | 2024-10-06 05:33:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cf2cd55-da54-3fe3-88ec-bd7e20dee472 | -3.39565 | -59.584 | 2024-10-06 05:33:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4911a4b2-3146-322d-a256-6bbace4fa63f | -3.10127 | -59.36841 | 2024-10-06 05:33:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24e4236a-47ae-3d4f-92a0-95a7ba9631b8 | -2.62389 | -59.37441 | 2024-10-06 05:33:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a876cb96-e418-3c43-9ca5-3dce930e475a | -2.62287 | -59.37692 | 2024-10-06 05:33:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0fd52af2-e8bc-397a-a997-e8dc35296f2b | -2.62022 | -59.37386 | 2024-10-06 05:33:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f598305-8b4b-35e3-b74b-9765afe6daa4 | -4.29051 | -60.01633 | 2024-10-06 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54bc487a-0683-36e2-81ea-95a9ce79dd04 | -4.2869 | -60.01577 | 2024-10-06 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fae4b573-d072-3f73-bf95-9fa6a67451a2 | -4.28626 | -60.01992 | 2024-10-06 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c53faee-cdb4-3da1-be25-9a5243fba3cf | -4.28328 | -60.01522 | 2024-10-06 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77e9833c-5a6d-31c4-956d-71fc280e9b32 | -4.28265 | -60.01937 | 2024-10-06 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb6ead96-d37a-39b5-a5fb-5a60d9775fc3 | -4.27966 | -60.01467 | 2024-10-06 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29360ae4-8f00-3fc2-b3c2-332a917da2dd | -4.27903 | -60.01882 | 2024-10-06 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c29654b-a40c-3c89-98e4-8d74b7bd5497 | -4.14486 | -59.92075 | 2024-10-06 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba5771c3-7c06-3bd5-9c83-175d30c3c870 | -3.8917 | -59.72554 | 2024-10-06 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 548bc656-b1b2-3d0f-96af-2c5b34338102 | -3.62301 | -59.50966 | 2024-10-06 05:33:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b6c3c75-31dc-3968-8bb3-40dc218b62c5 | -6.8194 | -60.05779 | 2024-10-06 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7f7f51f-f6dd-31b1-8e92-43db19857d99 | -6.81568 | -60.05725 | 2024-10-06 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 470fcded-2f07-30da-b37f-c5489c447224 | -6.78914 | -60.10715 | 2024-10-06 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 864bf6b1-4476-3f49-9734-bf39bd152df6 | -6.78544 | -60.10658 | 2024-10-06 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5fd9c56a-4f8e-3aa5-a5d9-514e63213afa | -6.78477 | -60.11099 | 2024-10-06 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 53db541b-04f5-36a9-b94a-cdb43c19aac8 | -6.78239 | -60.1016 | 2024-10-06 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b788d774-c831-3899-823b-99c7300ce818 | -6.78173 | -60.10599 | 2024-10-06 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 68ac4e17-0050-3b79-b04a-37504cf4e940 | -6.77868 | -60.10104 | 2024-10-06 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8efec95e-a156-354c-be91-1502c3acd718 | -6.67925 | -60.02081 | 2024-10-06 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca9e5a65-3f93-3242-9087-5eaa2fca9a47 | -6.64118 | -60.04665 | 2024-10-06 05:33:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4167edc3-79c8-33ad-8445-4f9bc0a0cf3a | -6.73675 | -59.63535 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3582319d-b9b2-35bc-859b-43253f33fa94 | -6.72723 | -59.07922 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eaf0eff6-22cb-3f3e-8e38-0f3358a494da | -6.72648 | -59.08427 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e8ae2c3c-33c5-3cd3-8c8a-356941744c38 | -6.7233 | -59.07862 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3d1606ee-9147-3ca0-a2b4-8114441b989a | -7.36488 | -59.65564 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5e181b5-5c00-30b9-8b31-45e5ed392271 | -7.22369 | -59.49925 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca4c59c2-1c4f-3d0d-8597-8b00fcc9e22f | -7.1537 | -59.29828 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 57bf6cb1-6895-3614-900a-0e356b64c2f0 | -7.15053 | -59.29278 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d2ee466-2747-3f25-a971-5a6045bca54a | -7.14979 | -59.2977 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2d6124e5-d9a2-3246-a7fb-fe3741e69521 | -7.14662 | -59.29219 | 2024-10-06 05:33:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README131.md)
