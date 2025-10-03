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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebf6695c-e3da-3fce-8439-5564a2d2764d | -12.7435 | -50.5591 | 2025-10-03 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| e8fc3975-fcf5-3dbc-81f2-3f7693c3e958 | -13.7673 | -51.2643 | 2025-10-03 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 119.7 |
| b3f607b8-5bba-3c3c-a8a2-a55a69286d9d | -12.416 | -45.1545 | 2025-10-03 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 8e778251-55ce-3f5f-b410-686d7ae6d76b | -7.7125 | -46.2082 | 2025-10-03 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 03024a74-0d58-3339-807f-9ceac7a52f9d | -7.2913 | -45.2548 | 2025-10-03 13:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 187.5 |
| 45b4cccc-c273-31a2-ae1e-f4dcdfc40952 | -9.8772 | -47.8103 | 2025-10-03 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 141.8 |
| b7593340-8df6-33d6-a280-2adc58d87b60 | -17.6331 | -44.4626 | 2025-10-03 13:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 309.4 |
| d5a4da0a-e63b-33eb-bded-7cdafb529ce8 | -14.2939 | -45.9076 | 2025-10-03 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 9df5bce4-864b-39a4-8334-cab0a5604b15 | -9.062 | -46.6565 | 2025-10-03 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 29d9cc0b-6fc9-381e-ba7d-6cfc5881de54 | -7.7494 | -46.272 | 2025-10-03 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 128.6 |
| e9d48988-5329-3ae0-8c75-95ae1dce7a80 | -10.345 | -48.176 | 2025-10-03 13:00:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 5e785319-4c19-3079-87bf-1eafd9b96635 | -10.0278 | -44.0108 | 2025-10-03 13:00:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 126.9 |
| ddfba166-0722-3068-8c39-b869b447b98b | -16.0387 | -51.0484 | 2025-10-03 13:00:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 81cf8b83-2be6-342c-a170-cc828e8d7bfd | -7.3101 | -45.2531 | 2025-10-03 13:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 3c475eee-f1b7-392c-927e-7c0602b33dd1 | -9.9962 | -50.2248 | 2025-10-03 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| bd5e3d7e-cf78-3fd7-8403-d25473b5a9a4 | -9.3386 | -45.7493 | 2025-10-03 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 7d4eb9cd-3fed-3b9e-ae37-fb509162b211 | -9.8991 | -43.7237 | 2025-10-03 13:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 99.7 |
| 49ca25cd-66a4-3b2c-9473-be0e5afa871e | -13.7472 | -48.0806 | 2025-10-03 13:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 047809bd-8b47-3204-b99f-3fc8f4a54206 | -8.8343 | -46.7694 | 2025-10-03 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| a420108e-4093-3cbc-9fc9-bbf226c40242 | -13.3418 | -48.1188 | 2025-10-03 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 224.1 |
| 83929d2e-b806-3111-9861-268cfe982504 | -11.9155 | -46.3272 | 2025-10-03 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 488.9 |
| 19103034-c411-35ff-832e-742249f7d224 | -8.1699 | -44.1608 | 2025-10-03 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 179.6 |
| dc2bc8d9-2ea6-37ff-a3b3-8ef026e5ea28 | -13.7858 | -51.3047 | 2025-10-03 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 50f01865-1649-315f-ae85-590f313bb5bd | -13.3422 | -48.0965 | 2025-10-03 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 84.0 |
| fa0972ee-8b49-30f2-a749-814769d9aa3c | -9.8769 | -47.8324 | 2025-10-03 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| ddac7d30-85ef-3b57-8a9b-6c63811b4072 | -11.8818 | -44.9815 | 2025-10-03 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 6dec50bc-7380-35df-9d30-9bba4f86a246 | -9.355 | -45.9284 | 2025-10-03 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| d069cbc6-e263-3266-9421-6ea7efe01e52 | -8.8543 | -46.6781 | 2025-10-03 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| cde36985-bb73-3c64-9354-3fd8b9f0ce6c | -12.6131 | -46.9725 | 2025-10-03 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 4dd767eb-6104-3a89-b602-7f4ffb96778a | -12.6127 | -46.9951 | 2025-10-03 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 1879c86b-38cb-3cd2-8eac-917ce8419bb7 | -14.0032 | -44.961 | 2025-10-03 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 171.5 |
| 75bc3013-a591-30f2-927e-b9c393aa7b76 | -10.9554 | -46.7044 | 2025-10-03 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 2eaf89e1-6848-32c9-9b51-00fc5e739f47 | -11.9159 | -46.3044 | 2025-10-03 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 209.4 |
| 00151d5b-9906-3ee3-8ddc-7be8fdde2e8b | -11.9151 | -46.3499 | 2025-10-03 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 189.3 |
| 27b5bca0-b29d-3d62-99da-e779a37af644 | -8.5389 | -47.8368 | 2025-10-03 13:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 30518996-944b-303d-8955-fb7ef0bbdff1 | -8.1702 | -44.1377 | 2025-10-03 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 875be4c0-f410-3a65-8df1-a84013b82da9 | -9.9182 | -43.7212 | 2025-10-03 13:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 184.0 |
| 253fb8be-f94b-3ebb-821c-4f74e3dd205f | -9.9965 | -50.2034 | 2025-10-03 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 593cb04b-0f05-3fc5-af5e-771916e8c3a4 | -9.3389 | -45.7266 | 2025-10-03 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 5ee5e6bd-9613-3d4f-81db-6f85d0d3f652 | -13.3414 | -48.1411 | 2025-10-03 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 212.0 |
| cb80b084-762a-37d1-9010-3e08d04d35bf | -8.5959 | -44.7833 | 2025-10-03 13:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 100.4 |
| ada37861-2057-3a2f-9ae4-240810e5f54e | -9.3547 | -45.951 | 2025-10-03 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 168.6 |
| b4a896ac-9862-33e8-8ad5-404f1728ff41 | -7.7682 | -46.2703 | 2025-10-03 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 452a1bae-1a4b-38eb-9b87-7591664afffd | -9.9394 | -43.5777 | 2025-10-03 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| b717e02e-da19-3caa-b330-815f24fec746 | -10.9483 | -51.0634 | 2025-10-03 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 6dffd2e4-d625-3ebd-8764-4d4b95814546 | -13.7862 | -51.2833 | 2025-10-03 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 6c41979b-6d5d-3909-ad0a-04b832e57cee | -8.6911 | -47.6906 | 2025-10-03 13:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| ce0e5896-1353-3af1-b613-a0a4c668dbf8 | -6.8763 | -45.4721 | 2025-10-03 13:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 850b1313-2878-3eb3-a667-5f929f0e437f | -9.3354 | -45.9758 | 2025-10-03 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| cc7fa3df-74c4-3956-bc68-1b00c1a05305 | -14.2172 | -44.9463 | 2025-10-03 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 31634709-621c-342c-81f1-07c75fdbbe81 | -11.1172 | -49.8276 | 2025-10-03 13:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| af125e41-21b2-3548-b909-812e13b2110e | -9.9186 | -43.6978 | 2025-10-03 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| b7a5dae2-642b-324a-b59f-3d53ad1a3a73 | -11.1271 | -47.8856 | 2025-10-03 13:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 8f0f73ba-2951-3b7e-8804-955b7b76b245 | -13.1152 | -47.8848 | 2025-10-03 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 3654ee38-019d-3fb9-a28c-94d8f322e97f | -14.6497 | -44.7499 | 2025-10-03 13:00:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 104.5 |
| c96406fc-058c-38c5-8ab3-c76508bfc43a | -12.1088 | -45.1554 | 2025-10-03 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| a1b90c0f-27b4-31f5-b800-5d87c5779340 | -11.1275 | -47.8634 | 2025-10-03 13:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| f68540cd-1c6e-36c8-bf58-b99e7026b42c | -8.8543 | -46.6781 | 2025-10-03 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 61378ddb-7d2b-34a1-b44b-6440894abaf9 | -11.1084 | -47.8658 | 2025-10-03 13:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 82b89fd3-5e6a-36a4-8691-303565638efc | -13.864 | -51.2302 | 2025-10-03 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| dca634b2-6e55-319f-83fe-5e057e7f1c9c | -14.0037 | -44.9376 | 2025-10-03 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| aca70726-51a2-3d60-84f0-d1a06999085b | -13.7673 | -51.2643 | 2025-10-03 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 193.0 |
| e9c7f4e5-05c7-3bab-aa2a-bcbc18ed728d | -9.8991 | -43.7237 | 2025-10-03 13:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 129.6 |
| a71c3d73-269b-3218-ab05-1e338c644f99 | -13.3611 | -48.1159 | 2025-10-03 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 823b476e-d670-3b10-8d12-713bdcc72920 | -13.8447 | -51.2328 | 2025-10-03 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 153.4 |
| a41bc519-03ed-3dd7-94ae-adfa1eb17a97 | -7.7496 | -46.2496 | 2025-10-03 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 5f82829a-6d01-39e8-b143-a649e04bf1aa | -12.7332 | -44.6631 | 2025-10-03 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 25194eea-cbc3-3292-b9d7-ebf9cd8df579 | -14.8063 | -51.424 | 2025-10-03 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 4e51bc7a-75c8-3271-b62e-78d1be67c175 | -13.3221 | -48.1439 | 2025-10-03 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 85.4 |
| fd155aa1-411d-317d-bd4b-97cc38a5d945 | -11.8294 | -51.7725 | 2025-10-03 13:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| aebddc89-e495-3b03-ac75-455e03d5a00c | -8.6911 | -47.6906 | 2025-10-03 13:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 9ede27fe-57ac-3ea1-b7ce-76a49b61245c | -9.9394 | -43.5777 | 2025-10-03 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| b7bd7833-5dcc-3076-aebd-e14796a0b999 | -10.9483 | -51.0634 | 2025-10-03 13:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 84761710-5e0e-38d6-b7f9-37facd676d5c | -8.1699 | -44.1608 | 2025-10-03 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 166.6 |
| e0c0fe28-be88-3b84-a150-be055ea6eb3c | -13.7862 | -51.2833 | 2025-10-03 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 396bcf0e-3059-3534-9617-ff1b6505b5f5 | -14.0032 | -44.961 | 2025-10-03 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| a4d648b4-eb45-35af-b157-33a8620a0bdc | -12.7435 | -50.5591 | 2025-10-03 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| fdadd0da-1c2a-37c3-b315-f1ea279ce56d | -7.7494 | -46.272 | 2025-10-03 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 0ddf5ce8-15cc-3d29-9daf-c1765270f5e9 | -10.1459 | -50.3165 | 2025-10-03 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 920f6836-5791-34f0-a717-1c2e73415248 | -18.9471 | -48.501 | 2025-10-03 13:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 126.3 |
| b31ba2e1-2062-35b6-9e1e-8c8fe7fe6078 | -11.8104 | -51.7746 | 2025-10-03 13:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 8678e0c5-eda6-3fb4-bdc2-ffb28521b260 | -10.0906 | -50.2154 | 2025-10-03 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| d18b048c-6561-37a0-bb33-80e722b6a8b4 | -10.1569 | -45.493 | 2025-10-03 13:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| ac9d2370-f417-3e34-9f97-c63160e1ea9b | -9.9186 | -43.6978 | 2025-10-03 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 69e870b9-29a9-305d-a73e-93a3133287b5 | -10.1092 | -50.2349 | 2025-10-03 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 957c06a4-49ab-3373-b497-d539671ab2eb | -18.9673 | -48.4968 | 2025-10-03 13:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 344.4 |
| 99facf12-4f29-398d-ae40-e73057e69d94 | -10.1084 | -50.299 | 2025-10-03 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 62b0c912-5483-39c5-9413-a69088068a98 | -13.3422 | -48.0965 | 2025-10-03 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 04dd8205-2a5d-3ffb-9fb2-3733dcfd6f23 | -14.2321 | -46.0794 | 2025-10-03 13:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| f33d4610-c076-3e2c-9019-95e724426bc0 | -8.1888 | -44.1588 | 2025-10-03 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 665b1209-eec6-3dd5-b85f-66538a480b38 | -7.2845 | -44.18 | 2025-10-03 13:10:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 5e92d3ac-6560-35a5-8269-e1fe47ce9201 | -14.2316 | -46.1024 | 2025-10-03 13:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 6fd563f8-7114-3b64-b81f-2664f0b0ff23 | -11.8814 | -45.0047 | 2025-10-03 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| e29239dd-b97f-3271-bdb7-67053a4c63c7 | -7.7682 | -46.2703 | 2025-10-03 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| cf6eabf2-05cc-3b8c-8016-28ed08a51dce | -13.38 | -48.1354 | 2025-10-03 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 03695226-4317-3d3f-9561-3f61ec2dcc4e | -7.2913 | -45.2548 | 2025-10-03 13:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 153.4 |
| ca63d9c5-f783-300b-9710-84164d38babc | -11.9167 | -46.259 | 2025-10-03 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 1c8e52b2-47aa-3d23-8e30-768dcef6d29c | -7.4469 | -46.4777 | 2025-10-03 13:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 1493c843-1024-30a4-948f-b883275cbd32 | -11.9155 | -46.3272 | 2025-10-03 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 544.7 |
| a3468692-7fe4-33e7-9fe9-a412f1deecf2 | -9.3357 | -45.9532 | 2025-10-03 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |


[Clique aqui para ver as próximas entradas](README147.md)
