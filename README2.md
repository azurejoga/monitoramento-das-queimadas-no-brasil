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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23f2f23f-4086-3fdc-b11e-81f7f864a974 | -3.42757 | -43.44284 | 2024-11-13 00:02:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| cf8a253f-380e-34b3-a63e-8ca8daa60d32 | -5.79919 | -35.59015 | 2024-11-13 00:02:00 | TERRA_M-M | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 9c63cc63-ade0-34fd-a8c6-a951702f1fd0 | -2.73348 | -45.27595 | 2024-11-13 00:02:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 0b2736bb-d5dc-3096-a3c4-cf2b4f8c0140 | -5.24132 | -37.68583 | 2024-11-13 00:02:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 9.0 |
| bc411741-2f3d-30d6-b66e-0f51bd20f70e | -5.3526 | -43.51446 | 2024-11-13 00:02:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 1a07cce0-a325-3f28-abed-780fffaa7b60 | -3.5851 | -44.4552 | 2024-11-13 00:07:00 | METOP-C | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ce1826fc-471e-35f1-a73f-dfa2f522a09f | -20.6406 | -47.425098 | 2024-11-13 00:07:00 | METOP-C | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b5b2d318-1833-3364-a712-9a50f9d4d6b7 | -8.003 | -35.116199 | 2024-11-13 00:07:00 | METOP-C | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 27861f70-0b3e-3b8f-845a-663899ad691d | -3.9442 | -48.1684 | 2024-11-13 00:07:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bac50211-b00d-3e07-969a-0d0d00f60fd4 | -2.9772 | -51.016602 | 2024-11-13 00:07:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6bcf4ea-d7c5-302a-bc25-37a1368e36b9 | -5.0757 | -44.269199 | 2024-11-13 00:07:00 | METOP-C | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e1a3d49f-727d-3114-8a7b-876ed0bc4812 | -4.2165 | -46.445801 | 2024-11-13 00:07:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7d2e0546-4901-398a-a071-e68307f717b2 | -4.4246 | -45.952702 | 2024-11-13 00:07:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 943dc747-c67f-30f6-a47d-3c88062dc3fd | -2.3566 | -46.9795 | 2024-11-13 00:07:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8b60310-9133-390d-80c4-5dc26ad5537b | -3.0675 | -50.326599 | 2024-11-13 00:07:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 827c5554-f83e-33bd-8cac-27e43a439862 | -3.3101 | -47.0233 | 2024-11-13 00:07:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa5430cb-1f35-3515-9b73-e037c9c4a87c | -4.0701 | -44.141998 | 2024-11-13 00:07:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d34bb24-29d9-357c-b154-68747988a321 | -5.3531 | -43.533298 | 2024-11-13 00:07:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c0a2cf1b-fbb1-38d7-a0d8-fb8e2a2d91e3 | -10.0374 | -36.359299 | 2024-11-13 00:07:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 60a5d06d-1898-3775-bf4a-3ea7c4f99c15 | -3.8432 | -46.0144 | 2024-11-13 00:07:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 94c19e2e-49c8-3965-ae56-973f0c83f011 | -7.5061 | -34.854599 | 2024-11-13 00:07:00 | METOP-C | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 52151280-f7c4-3602-b072-8d3c119254eb | -5.3108 | -39.634201 | 2024-11-13 00:07:00 | METOP-C | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 27e87bc6-21d4-32a3-8f7b-d625403f73ea | -4.219 | -46.456902 | 2024-11-13 00:07:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9061102b-0cfb-3b71-af1c-c7c86f4de23f | -3.9474 | -48.182701 | 2024-11-13 00:07:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 840bd6b3-7b1c-3498-955d-8b84d1625227 | -3.661 | -50.1581 | 2024-11-13 00:07:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79dbfb31-efbf-36c0-b9c7-fc2ba25cd9a5 | -2.9821 | -51.038399 | 2024-11-13 00:07:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9501459-b606-31f0-833e-a950580b40de | -5.7945 | -35.587399 | 2024-11-13 00:07:00 | METOP-C | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 0de4c3b3-d5b6-3e75-bad5-97d1d33df4bf | -2.6969 | -49.3536 | 2024-11-13 00:07:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ca5f226-7b47-3d28-bac2-56309b916cf7 | -5.2423 | -37.699501 | 2024-11-13 00:07:00 | METOP-C | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 1fb37888-de64-3ac9-a546-aa778a6e31a2 | -4.4107 | -48.847599 | 2024-11-13 00:07:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbf4ee22-0cc0-3ce8-b31e-06c5e4ec2fe6 | -2.2912 | -47.9151 | 2024-11-13 00:07:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d0722d6-c952-39c2-8609-568bf2bab489 | -2.7803 | -48.085602 | 2024-11-13 00:07:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 305abc07-b8ff-3965-84f5-26e1b72b95e4 | -2.6567 | -46.808601 | 2024-11-13 00:07:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1d7b366-19b7-36c6-a54d-60421f40a90e | -2.7279 | -45.304501 | 2024-11-13 00:07:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b9522f6e-3196-3b20-9163-9bb53c9e7a46 | -7.1359 | -40.167198 | 2024-11-13 00:07:00 | METOP-C | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ac648817-2f7d-3d15-af54-8b2c66b34900 | -3.2516 | -43.255798 | 2024-11-13 00:07:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eef4e21b-71f4-370b-af08-910ed77d3423 | -5.7971 | -35.598 | 2024-11-13 00:07:00 | METOP-C | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 3c3dce06-9e95-351c-ba84-6fdf2da541b1 | -3.5733 | -53.020901 | 2024-11-13 00:07:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af195f9f-6e2c-33cb-9427-d7f8d3e2646a | -5.3513 | -43.525398 | 2024-11-13 00:07:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 05804827-5ba4-3cf2-a89e-81680e035ef1 | -7.1374 | -40.174099 | 2024-11-13 00:07:00 | METOP-C | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8f1f83a1-8c70-3ec6-abed-ac7327c79c66 | -2.5387 | -45.604801 | 2024-11-13 00:07:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8f48eeb2-269c-334f-8a0f-6644ca21048a | -2.9918 | -51.036301 | 2024-11-13 00:07:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d0f57cc-8930-33f1-bd47-f8e2ad0a4936 | -10.0394 | -36.367802 | 2024-11-13 00:07:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| eef144ae-eac5-3087-8b8f-8abe4b0db2fb | -3.9427 | -46.4132 | 2024-11-13 00:07:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 220e05c5-149a-374b-832a-0ca40c0590c6 | -8.0153 | -35.1245 | 2024-11-13 00:07:00 | METOP-C | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ad49e990-401d-3cd8-b1f6-45fd6f1ae6e1 | -8.0127 | -35.113899 | 2024-11-13 00:07:00 | METOP-C | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a9c45375-9fb0-3950-aac9-98a1ff49fd76 | -2.7003 | -46.000801 | 2024-11-13 00:07:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 74db13c8-8514-3a79-b91d-a7e5587a269c | -2.6029 | -48.253101 | 2024-11-13 00:07:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a53111df-865d-3310-9ad9-da414056eef4 | -2.3592 | -46.9907 | 2024-11-13 00:07:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90608d88-2bd5-38ff-bd58-1be149c0ef0d | -7.139 | -40.180901 | 2024-11-13 00:07:00 | METOP-C | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9b59ef9e-997b-319f-9708-9a9f516bba3b | -2.6543 | -46.7976 | 2024-11-13 00:07:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03851337-6d14-31e0-b973-52e52d670491 | -4.4072 | -48.831501 | 2024-11-13 00:07:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e926236-ab37-350a-8b64-423b4dd8938c | -3.5665 | -52.990299 | 2024-11-13 00:07:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bd7db98-51c0-3954-b1c6-d95b75628cc5 | -4.3697 | -44.101799 | 2024-11-13 00:07:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 52bbba8d-0fce-32e9-8bdb-7119b3add19a | -10.82 | -44.368801 | 2024-11-13 00:07:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8aba1520-3e85-361f-a079-c2eac88c2374 | -4.3179 | -50.417999 | 2024-11-13 00:07:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3b5f07c-df5d-3d17-a54c-a4fd8d196177 | -1.71 | -46.301701 | 2024-11-13 00:07:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8422ee28-3f1c-34fe-b5e9-f8de19eb0bab | -7.8771 | -35.236099 | 2024-11-13 00:07:00 | METOP-C | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 993a64ca-8ad1-319c-8310-e4771e14141d | -5.2349 | -38.683998 | 2024-11-13 00:07:00 | METOP-C | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e5c61a37-5f82-3c61-87ef-e5d8945ad96c | -3.4088 | -51.039101 | 2024-11-13 00:07:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10e25eda-256f-3b4b-86ee-6145706db243 | -3.5472 | -52.9944 | 2024-11-13 00:07:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79c3caf1-16bf-3f67-88a8-aef9531c7526 | -4.6729 | -44.581902 | 2024-11-13 00:07:00 | METOP-C | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd0d7171-85a7-3e9c-a1f4-de32ad73b2ec | -3.8334 | -46.016499 | 2024-11-13 00:07:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9edd2bfa-076f-302a-af06-66b4bebad466 | -3.3305 | -48.945599 | 2024-11-13 00:07:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a442dda3-c43c-32a8-a151-74ace1503811 | -3.2533 | -43.263199 | 2024-11-13 00:07:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0c15ca9b-9e10-3847-9923-2e7750ba00a0 | -5.2442 | -37.707699 | 2024-11-13 00:07:00 | METOP-C | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 7627bfb7-161d-3f15-8992-f0ba9920a34c | -3.2435 | -43.265301 | 2024-11-13 00:07:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d808208e-c008-348b-868c-b6407cf38598 | -2.4619 | -48.444901 | 2024-11-13 00:07:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6ff453f-9717-39de-b6c7-13b165ac48d5 | -3.0436 | -50.311199 | 2024-11-13 00:07:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35cab4d7-536a-37ff-abc1-e7a1a52a69eb | -2.2883 | -47.902199 | 2024-11-13 00:07:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c9dc2ba-a886-3988-8c2f-f59128581c41 | -4.6749 | -44.590599 | 2024-11-13 00:07:00 | METOP-C | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78579e10-981f-33bc-91eb-1d09ec85008b | -3.3582 | -45.318501 | 2024-11-13 00:07:00 | METOP-C | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3fd234f2-6f90-3bb9-b8af-5b25a98fd1e8 | -3.3075 | -47.0116 | 2024-11-13 00:07:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 511bb601-71c4-3819-a288-5674618787a7 | -3.9524 | -46.411098 | 2024-11-13 00:07:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 21ed7679-d5f9-3e0a-a257-a5bc568ab8f8 | -17.7735 | -40.190399 | 2024-11-13 00:07:00 | METOP-C | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5621c63c-d973-3f1b-bf69-fee1f3f710bf | -4.7799 | -45.8433 | 2024-11-13 00:07:00 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3e0a73f0-49cf-31a0-81c0-d8c66f899d24 | -3.3421 | -42.476299 | 2024-11-13 00:07:00 | METOP-C | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa6d325e-f7cf-36fb-858e-3fdeeac104af | -1.4841 | -45.6259 | 2024-11-13 00:07:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 36fbbc82-395e-3cce-ba4c-82eee31f9c4c | -2.716 | -45.2976 | 2024-11-13 00:07:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4fe61e59-cd6d-36cd-acea-10eb893ca9d8 | -2.79 | -48.0835 | 2024-11-13 00:07:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f14f329-0c17-312c-a939-4d37d4bc2f52 | -2.6175 | -46.817101 | 2024-11-13 00:07:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7243c985-0891-3746-8944-d2120e5cd54a | -10.8178 | -44.358601 | 2024-11-13 00:07:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 20deef0b-4797-3192-84ec-d85a251e487c | -5.3433 | -43.5354 | 2024-11-13 00:07:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a6b04afc-7a6e-33c5-989c-38baf4f4a388 | -2.6932 | -49.337101 | 2024-11-13 00:07:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecfacca4-31ea-3f9f-b7a2-cd33a5090fc4 | -8.1218 | -38.6241 | 2024-11-13 00:07:00 | METOP-C | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| becbcc3a-449b-3a4b-9cc3-789381465090 | -4.1972 | -42.338001 | 2024-11-13 00:07:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f5702153-02f1-34f8-ad1e-c71053d6678d | -5.0739 | -44.260799 | 2024-11-13 00:07:00 | METOP-C | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd80c475-9723-337a-bd36-8799b67a89cf | -3.5568 | -52.992298 | 2024-11-13 00:07:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e67bcda9-9324-35fa-ad75-3689eefd6a76 | -3.048 | -50.330799 | 2024-11-13 00:07:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef1e6644-bf42-3ea9-ba19-57cb265e989f | -4.0674 | -45.869598 | 2024-11-13 00:07:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9e2944d8-3476-3806-a3a6-df7aeaa82761 | -2.698 | -45.991001 | 2024-11-13 00:07:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 85fb0e96-7add-382c-a9fc-0290daa22d95 | -6.9676 | -40.378201 | 2024-11-13 00:07:00 | METOP-C | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| edc1bc62-e209-3395-bae9-ee2797ba7ad8 | -4.3377 | -43.822498 | 2024-11-13 00:07:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 781a9326-8ffd-3c13-a3be-e15caa7315a4 | -4.3395 | -43.830502 | 2024-11-13 00:07:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5401ad89-5607-3892-918b-8a782466b8ca | -5.0512 | -44.481098 | 2024-11-13 00:07:00 | METOP-C | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 147ac154-d4e2-3438-9c08-4752f9e69f1e | -2.6592 | -46.819698 | 2024-11-13 00:07:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82921198-c7db-34a7-a135-a16954da90c6 | -5.0531 | -44.489799 | 2024-11-13 00:07:00 | METOP-C | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96cf5444-ad7d-3cd6-9105-c633c8ecb360 | -2.5289 | -45.606899 | 2024-11-13 00:07:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f7c5e378-e47c-3d8a-9dc6-64919d43a900 | -10.5608 | -36.734699 | 2024-11-13 00:07:00 | METOP-C | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a54105e5-9140-3a53-aafd-905a5a4efddb | -2.6518 | -46.786499 | 2024-11-13 00:07:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
