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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f51b028f-82f9-3bdc-b129-3a66593dfd36 | -8.26522 | -46.08265 | 2025-07-19 04:34:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75ee606c-66e1-3044-98d3-31f144b1804f | -8.42474 | -46.88031 | 2025-07-19 04:34:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| acfc132b-6f9e-38f8-92e0-be99623f2c60 | -3.0374 | -49.42743 | 2025-07-19 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75192247-6641-39c2-bffe-2b98b5f9c3a6 | -5.6449 | -43.71576 | 2025-07-19 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c58cc3a-7bc7-383b-a89c-daee501a7efb | -7.48498 | -43.93234 | 2025-07-19 04:34:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be80fda0-e282-3ae6-82a2-daf39a1873c6 | -7.17868 | -44.09976 | 2025-07-19 04:34:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 47d2db53-f856-3d88-b2fc-265e2cb32331 | -8.14421 | -43.43308 | 2025-07-19 04:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 354df764-c1c9-3e62-8df8-d4d375a9c43d | -6.68892 | -43.03728 | 2025-07-19 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa14df42-95e3-38a1-a062-373e29d4eb96 | -2.91205 | -48.2437 | 2025-07-19 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| f58fea66-ac0b-3fe0-aead-f90726ef8a98 | -8.53898 | -47.84584 | 2025-07-19 04:34:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d94640db-f82c-3327-b8a4-a108f5abb649 | -3.1235 | -47.01534 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8c35bc80-b7f6-3281-bc17-494513185337 | -6.87653 | -42.75078 | 2025-07-19 04:34:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f9723fc2-b38b-3c90-a55c-c2dccc60f536 | -4.47958 | -46.07458 | 2025-07-19 04:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e54cc3f0-2329-339f-aa3c-03a284a966c0 | -5.10567 | -43.15349 | 2025-07-19 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d0c57bf-ae7a-3538-a24f-c1dbb971e58b | -6.3306 | -43.74408 | 2025-07-19 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7cbbd67c-0e6f-3e76-910b-a76c77c94d8e | -9.51563 | -43.24309 | 2025-07-19 04:34:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2039451f-4eff-3f7c-b3ea-79fc1f7ec458 | -7.48592 | -47.50475 | 2025-07-19 04:34:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ebbe8feb-e7b9-3179-bced-4f95dd65015f | -6.75698 | -45.51226 | 2025-07-19 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db244405-047d-38ac-bcd9-27a259935f22 | -6.17638 | -45.86889 | 2025-07-19 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5f61cd5c-04a6-3976-a226-c3ddd532164d | -5.18803 | -44.95757 | 2025-07-19 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d5c8fbd5-9c50-3ee1-910f-127b5ebc1fb9 | -6.36535 | -44.59574 | 2025-07-19 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8dcc04c3-efc9-32c4-b795-594fea84526c | -4.87066 | -47.76011 | 2025-07-19 04:34:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb0a351f-4781-34c4-9aa1-37622274f970 | -6.34318 | -44.04703 | 2025-07-19 04:34:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac526ce5-6538-3cd0-8871-e73a32f9eb77 | -3.13785 | -47.01052 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 6cfdb158-22f3-3148-933c-f2e6cb634ed7 | -2.4412 | -47.32831 | 2025-07-19 04:34:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b772f83-76e1-3301-a225-89ad131e0543 | -2.4473 | -47.33281 | 2025-07-19 04:34:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4836d7da-bc38-3971-8470-04900a898d27 | -6.13092 | -47.75044 | 2025-07-19 04:34:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 938e1335-945f-31cd-a9b1-82fe9db1fbbf | -3.11741 | -47.01086 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5949136a-6fdc-367d-a2e1-29d53da78c0b | -4.77802 | -45.34698 | 2025-07-19 04:34:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ef7d437-0eff-36b9-a2ce-64db244df471 | -3.67295 | -45.40594 | 2025-07-19 04:34:00 | NPP-375D | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83fc5a1f-f592-3728-a551-74bfec3f39a6 | -8.26463 | -46.08649 | 2025-07-19 04:34:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be09a3cd-38c0-3b11-aaab-fa250046a4e8 | -8.54509 | -47.85039 | 2025-07-19 04:34:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 898d6085-ae56-396b-a320-6cc0260b360f | -8.25661 | -46.06948 | 2025-07-19 04:34:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a1510c9-3e96-360c-af18-16e3670fcbd1 | -5.65314 | -43.71238 | 2025-07-19 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fef301ef-6261-35a7-9269-af41dd2c2862 | -8.52901 | -47.84426 | 2025-07-19 04:34:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d82f9e2d-1bdc-3335-848d-64584ea02388 | -3.045 | -49.4247 | 2025-07-19 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 081a93d7-a213-32a5-b712-fa3394749c91 | -7.9539 | -43.94347 | 2025-07-19 04:34:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3ce463a-7b4a-30c3-bf94-028b4fd629c9 | -3.17538 | -52.87595 | 2025-07-19 04:34:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e6e8d8f-402f-3927-8a3f-8691cc48fa35 | -8.26007 | -46.07002 | 2025-07-19 04:34:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e8c9aed-f8cc-3a9a-bade-99c7a0f4b808 | -6.16481 | -48.05031 | 2025-07-19 04:34:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 8c0d4e63-dd83-3f37-b092-d2c2cc98a1c8 | -3.38833 | -47.48059 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04585664-f558-3f2c-abf5-0cc024c5b2d5 | -4.11243 | -47.92852 | 2025-07-19 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79b8920b-5d7c-338f-9dc7-12a5881c5d32 | -6.75232 | -45.51944 | 2025-07-19 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 831d789e-0fc4-33cc-a092-f8381dd7ed42 | -3.83097 | -47.74163 | 2025-07-19 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 875cf732-cb00-3aa0-aafe-fbf3cfa7a5ed | -6.44504 | -51.88884 | 2025-07-19 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ed470356-8a9d-3d34-882d-1c85034d5e61 | -7.22811 | -44.13047 | 2025-07-19 04:34:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e63c974-9803-38a1-a3a1-bc1a53863d69 | -3.39111 | -47.48457 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f740715-5ec0-3cf1-b4aa-e036475ab6c4 | -2.91485 | -48.24778 | 2025-07-19 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 8636269a-42b3-3646-82de-00d315ce3c89 | -3.04151 | -49.42415 | 2025-07-19 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 638e62a1-5fd4-3c82-8719-3da58b0233a5 | -8.55173 | -47.84777 | 2025-07-19 04:34:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f68c191c-72c9-3284-8436-0ad7c7d423b2 | -2.91261 | -48.24015 | 2025-07-19 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b459b11d-9917-3adf-9ece-bacc4f7eedfb | -7.95703 | -43.9488 | 2025-07-19 04:34:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 114fa841-a3b7-3ece-b3a2-e1a0f0927cdc | -7.09796 | -44.32838 | 2025-07-19 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca5b8800-cba0-3938-890d-8f7a46a88c43 | -3.57373 | -49.50507 | 2025-07-19 04:34:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3913e5aa-1001-369f-bf26-9d6f834bccff | -7.42486 | -44.85241 | 2025-07-19 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6dbd4c08-d1a7-30be-a9d6-42ede131a5e7 | -3.13067 | -47.01293 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7544988b-77aa-3d7f-956c-91a2f6314a32 | -2.44174 | -47.32486 | 2025-07-19 04:34:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f04cafdb-da93-3502-b83c-317a0ef32c3e | -8.21541 | -47.42455 | 2025-07-19 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d89258c8-ed80-3a87-bcf2-34fbcc4d386d | -9.007 | -48.71736 | 2025-07-19 04:34:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a33b3e56-f492-3cd6-9d1e-ef04e486b763 | -4.03033 | -48.06574 | 2025-07-19 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b2ca6ddf-a6e6-346b-abb0-4db80c87b9b5 | -7.21709 | -49.61827 | 2025-07-19 04:34:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6950ad21-60b2-3cd3-ba42-2db3ba17237e | -9.66118 | -45.23024 | 2025-07-19 04:34:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9431f47c-4854-38bb-91a6-f61e480c2055 | -3.73692 | -48.35415 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c9dd9f4-552d-3569-92e7-e431bd812fb0 | -3.17964 | -52.87656 | 2025-07-19 04:34:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dfd20927-42dd-3ab4-9348-22cca8325b19 | -5.7793 | -44.92841 | 2025-07-19 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 837fadc5-2ce9-3178-babc-f0f1161f006e | -4.12674 | -47.65033 | 2025-07-19 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47d97565-5119-3b27-a49e-c3cea0a1a528 | -7.83445 | -44.82537 | 2025-07-19 04:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8617b068-c156-3a6d-b32c-257005ea5b7f | -3.58748 | -47.52644 | 2025-07-19 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ed2a14c-dca2-3fae-be2d-00d103df3bb2 | -5.64422 | -43.72032 | 2025-07-19 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3e9394a0-f4ce-3928-a19e-735d90008b3d | -5.648 | -43.72092 | 2025-07-19 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 3f0e02b7-0de3-3f7b-b194-dbde8d2e7158 | -2.91541 | -48.24423 | 2025-07-19 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 412f7803-c7af-3886-bfac-91d488a64fac | -3.39888 | -47.49995 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a46a44ff-f21a-3876-8198-8b892f3344eb | -5.80112 | -43.62808 | 2025-07-19 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 573f0d88-5908-3c61-bcb4-415482d22c8e | -7.05659 | -44.0669 | 2025-07-19 04:34:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73c8004b-b03a-3eff-b007-bf3788177c50 | -3.06489 | -40.04691 | 2025-07-19 04:34:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1c6ded7b-495c-3530-af9b-7baf8f4213b7 | -7.22677 | -44.13947 | 2025-07-19 04:34:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9f84cfe-09e9-35be-bde6-57ff10460037 | -9.60623 | -43.85777 | 2025-07-19 04:34:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 527c1273-f6d5-3d6f-bf25-697ba555de06 | -4.30765 | -48.10606 | 2025-07-19 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| dc866fed-173f-3e96-82c1-24c32685fb87 | -4.66861 | -41.95721 | 2025-07-19 04:34:00 | NPP-375D | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| cbc4f4fb-15aa-33bf-a036-7604e1a75583 | -3.39497 | -47.48164 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3d620ba-3a77-3d2c-8179-67850e5231de | -3.50736 | -47.22016 | 2025-07-19 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5bcf5422-5512-376c-904b-769acbca35f1 | -7.95493 | -43.94547 | 2025-07-19 04:34:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5af655d1-e1f4-31db-add7-463b3aee9a87 | -3.80413 | -43.22469 | 2025-07-19 04:34:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40fa143d-23e7-37c5-8f48-355c0535f423 | -3.04089 | -49.42799 | 2025-07-19 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a8507933-1436-3d20-b180-0f76f1378a36 | -3.12736 | -47.01241 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| f820bf37-2648-3b9e-9e88-4cbf4019c99e | -7.94864 | -43.95231 | 2025-07-19 04:34:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d63427b6-3494-3e06-97e2-dc666c377bdb | -6.4234 | -47.22409 | 2025-07-19 04:34:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 364dee91-0648-3e28-a703-52ba0c77f631 | -5.21332 | -44.11709 | 2025-07-19 04:34:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 540f588f-f3c7-333c-b3c9-948a028ab757 | -6.16094 | -48.05325 | 2025-07-19 04:34:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 07b37957-f6e0-3965-8cbc-8da412279946 | -3.29436 | -42.53511 | 2025-07-19 04:34:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5578b10-d941-392d-915c-cd86e638dca8 | -4.4762 | -46.07407 | 2025-07-19 04:34:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c8b6e8a-0d2c-3113-9ab8-b4bbe39f5b90 | -5.53165 | -43.88142 | 2025-07-19 04:34:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 124d6c5d-e666-35d5-a41f-c6cff78f8046 | -9.59436 | -43.85605 | 2025-07-19 04:34:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fa495ddc-030e-3be7-99c2-f0e6abea4c7c | -9.59176 | -43.85393 | 2025-07-19 04:34:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5ccba3af-7b7e-36da-9fb6-cebdce749b7a | -2.05627 | -47.10858 | 2025-07-19 04:34:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88807f13-589c-3792-8a59-31aa9ccb42ed | -7.95425 | -43.95019 | 2025-07-19 04:34:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 704d5424-ed01-3b31-8394-ef5787605280 | -8.53566 | -47.84531 | 2025-07-19 04:34:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 70bf5e23-f2f4-3bc0-9d2d-f16d2a6b68ab | -8.88033 | -50.15991 | 2025-07-19 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3006e6fa-22a4-349a-872e-3aaf7e78e614 | -5.52791 | -43.88082 | 2025-07-19 04:34:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 27f3f742-716e-302b-ad5c-f40122ed65ee | -8.32924 | -47.49692 | 2025-07-19 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README18.md)
