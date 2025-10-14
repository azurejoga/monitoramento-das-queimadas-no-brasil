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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c182d94-ae31-3da9-aa11-8682bcb9f4a3 | 1.7484 | -55.8033 | 2025-10-14 02:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| b1017de2-d9c6-3a63-8405-5bf2f78bc846 | -7.9631 | -44.113 | 2025-10-14 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 18e4a2f0-6fd5-3928-9f6a-7deb3972c4d6 | -7.8086 | -46.02 | 2025-10-14 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| f9e787a4-1bbc-37da-83fb-a72f8206049d | -5.4937 | -43.0761 | 2025-10-14 02:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| fa64fe41-e8bb-368a-b8cc-110f47d769a9 | -7.9628 | -44.1362 | 2025-10-14 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 17cd17c1-f61a-3487-b774-d9c8a4b5e8be | 1.7483 | -55.823 | 2025-10-14 02:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 6e6e9f2f-a753-3707-a440-9dbc75ccb887 | 1.7667 | -55.8228 | 2025-10-14 02:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| a9e9f06a-250c-3348-8edc-d27f5360b9d7 | -4.6509 | -43.1337 | 2025-10-14 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 5a261b5b-c483-36e6-9280-1b06abcdc0eb | -7.7898 | -46.0217 | 2025-10-14 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 407d0b4f-6fc6-3e0b-a12d-9a24eae92e02 | -4.6696 | -43.1326 | 2025-10-14 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 116.3 |
| adc7ada1-dfd5-3141-b1fd-02cfbd6b399e | -7.9253 | -44.1169 | 2025-10-14 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 94.0 |
| ccd89a60-a470-3098-b41f-704f87219a31 | -5.7405 | -40.7628 | 2025-10-14 02:40:00 | GOES-19 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 77.1 |
| da2df5e5-c128-345a-ac7f-181a303b8abe | -11.7594 | -43.2898 | 2025-10-14 02:40:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 105.5 |
| 75548b31-fe59-3922-b692-2b7e5023bc5e | -11.7406 | -43.269 | 2025-10-14 02:40:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 88.1 |
| d1f58c21-f060-3b2c-8f5e-b6c5a26c72df | 1.7484 | -55.8033 | 2025-10-14 02:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 872f3889-476e-3fdc-8106-1b65130a077d | -7.9442 | -44.115 | 2025-10-14 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 145.4 |
| e3489e03-508d-3baa-b4c7-02689c04a723 | -4.6694 | -43.1559 | 2025-10-14 02:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 3edcd691-9612-3000-b5c4-3fee335b2b2b | -7.9439 | -44.1381 | 2025-10-14 02:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 2907d7df-c992-31bd-a6de-5439a840f652 | -7.79 | -45.9993 | 2025-10-14 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| f0590687-4184-3a0a-99d8-e6629ee7079b | 1.7667 | -55.8031 | 2025-10-14 02:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 869eb0b3-9d62-37ad-994f-1065676e6569 | -11.7401 | -43.2928 | 2025-10-14 02:40:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 165.9 |
| 1ce8d59c-75ca-3644-9999-ca4fc6babec5 | -7.9628 | -44.1362 | 2025-10-14 02:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| f245712b-4381-35d6-bd43-f7409cc75078 | -4.6509 | -43.1337 | 2025-10-14 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 142f933f-8729-3285-9eb8-7ba94aac906c | 1.7667 | -55.8031 | 2025-10-14 02:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 12a77715-55d8-321a-b837-034e1b43ef6d | -7.9442 | -44.115 | 2025-10-14 02:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 188.0 |
| 2e7fefed-646a-323f-b65f-8285fbf8a59e | -7.9631 | -44.113 | 2025-10-14 02:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 99.8 |
| e6576a16-d6a9-30ca-8760-8229fc2a7039 | 1.7667 | -55.8228 | 2025-10-14 02:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| ee2345de-27a9-3709-a75d-f7a6b8d0df9e | -4.6696 | -43.1326 | 2025-10-14 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 0bfec479-b154-3c2e-8cb4-79c8fd38e229 | -11.7594 | -43.2898 | 2025-10-14 02:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 93.4 |
| 87ad47a1-a309-3a95-8935-957debaad595 | -11.7401 | -43.2928 | 2025-10-14 02:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 161.6 |
| 10961817-3452-39f9-b1fb-3c35c0a44dff | -11.7406 | -43.269 | 2025-10-14 02:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 110.7 |
| e1b4044a-f26e-34ce-bc43-a91e1d48b2dc | -5.4937 | -43.0761 | 2025-10-14 02:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| a0499767-377d-364d-b4f1-a10d94b6407b | -7.9253 | -44.1169 | 2025-10-14 02:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 481ac8f0-3225-3f84-a0e3-9904240c10ad | -5.1181 | -43.1964 | 2025-10-14 02:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 613d3155-8dcf-36bf-8e9c-c47693d57e27 | -7.9439 | -44.1381 | 2025-10-14 02:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 22e82965-9bf9-3d2b-bd7a-1beca5a0a3fa | 1.7483 | -55.823 | 2025-10-14 02:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 22a29f95-d1ed-3bdc-ae74-0e09a14619da | -12.8568 | -50.6523 | 2025-10-14 03:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 1e29659c-8290-3b55-b27e-94ca1cc58bbf | -7.9442 | -44.115 | 2025-10-14 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 188.2 |
| 8dbe3c6e-d816-3e7d-8bae-d9f69c35a0ab | -12.8376 | -50.6547 | 2025-10-14 03:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 6deb1d54-25d8-3ab0-9791-d29efbe531f2 | -7.9439 | -44.1381 | 2025-10-14 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 9dd933e4-0649-331e-aac0-90f37709f19f | -4.6509 | -43.1337 | 2025-10-14 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 0068d3b0-abf5-39ba-b615-7767b05212fd | -5.9088 | -42.8091 | 2025-10-14 03:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 84.3 |
| a6ccd417-2c52-3764-8265-c09d70eb77e6 | -4.6696 | -43.1326 | 2025-10-14 03:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 3d6a2914-85eb-3e5d-873d-ec0bbca79988 | 1.7667 | -55.8228 | 2025-10-14 03:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| e36d9929-b8b7-3c99-a338-73efd24abf7a | -11.7406 | -43.269 | 2025-10-14 03:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 111.4 |
| 495b5835-c2c6-314a-b0d1-b40bdb0181fc | -12.8188 | -50.6356 | 2025-10-14 03:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 681a1541-767f-3c32-a5ef-46fdf48c42b9 | -11.7401 | -43.2928 | 2025-10-14 03:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 141.2 |
| c659744d-30d9-329f-b82f-6a32a416eec5 | -11.7594 | -43.2898 | 2025-10-14 03:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 90.7 |
| 3645f82a-ae83-33d1-8f92-b8d6bf81988b | -12.8184 | -50.6571 | 2025-10-14 03:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 6eb6e88b-f05e-33bc-a6e5-5cac8d162ba6 | -7.9253 | -44.1169 | 2025-10-14 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 2b9faaae-2f86-3f49-81f4-d91c101c048a | 1.7667 | -55.8031 | 2025-10-14 03:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| d92a776a-cf62-3aa1-a36f-995c1687578a | -7.9631 | -44.113 | 2025-10-14 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 1dafaf95-9edc-3e77-9a96-3e0dc4f630b0 | -12.7993 | -50.6595 | 2025-10-14 03:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| a6dc6523-de8e-36ab-b554-cb7d307d11dc | 1.7483 | -55.823 | 2025-10-14 03:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 2c1debbc-34d4-34a8-8688-d3492494a4a6 | -7.9628 | -44.1362 | 2025-10-14 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 1aaeb303-e362-38de-a39d-630c787f8ad0 | 1.7484 | -55.8033 | 2025-10-14 03:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| de2b484a-6f84-3d6c-b40d-b1ca4c465277 | 1.7483 | -55.823 | 2025-10-14 03:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| e3290098-bab9-3e20-a1d9-e4ca247f0f5e | -5.8893 | -42.8813 | 2025-10-14 03:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 66.6 |
| 8640bb9f-efde-38e2-89fd-0ff99d761a6c | -4.6696 | -43.1326 | 2025-10-14 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 9ccb192d-48b2-3af1-83cf-d983ded61b6b | -11.7598 | -43.2659 | 2025-10-14 03:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 96.4 |
| 6e0ff047-3dd2-311d-add4-5c728cc07fff | -11.7406 | -43.269 | 2025-10-14 03:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 96.8 |
| 7f1a55a8-6f63-3222-b6f4-8a1fc706db87 | -5.0994 | -43.1977 | 2025-10-14 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 59bbbfb7-fba6-393b-93f0-32086e8f93c7 | -4.6509 | -43.1337 | 2025-10-14 03:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 9f3bf147-bb0d-3a2d-b57c-7c2425ba817e | 1.7667 | -55.8031 | 2025-10-14 03:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 9b365842-a442-34a6-871d-f8a1bfdd0bb5 | -11.7401 | -43.2928 | 2025-10-14 03:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 119.9 |
| c613c1be-4987-3a16-b6b8-9c81cd9001e2 | -7.9439 | -44.1381 | 2025-10-14 03:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 113.5 |
| a970b1f8-416a-3b14-b973-ae7e1ec10259 | -7.9253 | -44.1169 | 2025-10-14 03:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| e4d6b2b3-5672-3e81-8716-8c7b50558c07 | -11.7594 | -43.2898 | 2025-10-14 03:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 119.9 |
| e907bb28-c238-3f44-8ac4-088509fc5bf3 | 1.7667 | -55.8228 | 2025-10-14 03:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| d8496bd4-1a3e-3ef5-b902-9c4eaf2ef58c | -7.9442 | -44.115 | 2025-10-14 03:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 183.7 |
| 1a7ce210-5e17-3edd-a9e0-f803c67ab21c | -10.1592 | -36.4078 | 2025-10-14 03:20:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 40.5 |
| 7d4bb1b9-8246-3fff-aa01-e80f93e9644b | 1.8768 | -55.6832 | 2025-10-14 03:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| bb2e24f7-f074-3970-851c-b1728bab536e | -7.9253 | -44.1169 | 2025-10-14 03:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 6d3c1a1f-ade8-3862-b5f7-c62d575e2d4d | -4.6509 | -43.1337 | 2025-10-14 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 68847783-f63f-35d6-856b-d8e930166621 | -7.9442 | -44.115 | 2025-10-14 03:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 221.9 |
| c6aa4264-35a7-3b7e-9e2f-f43c7d774d59 | -4.6696 | -43.1326 | 2025-10-14 03:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 5f1808b3-8c00-321b-bc11-19669930d74a | -7.9439 | -44.1381 | 2025-10-14 03:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 681d22c2-5487-37ea-a4e0-716324cb49ad | 1.1135 | -50.9776 | 2025-10-14 03:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 847993df-350b-318b-b56c-c208d079462e | -7.9631 | -44.113 | 2025-10-14 03:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 0300ef1d-fca4-3b05-abda-a5349a379837 | 1.1135 | -50.9984 | 2025-10-14 03:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 67d03b02-2d89-3aa1-b4ca-866524b5ef10 | -11.7406 | -43.269 | 2025-10-14 03:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 85.6 |
| 9bc79086-368e-3b7f-b060-7c821cefce7d | -11.7401 | -43.2928 | 2025-10-14 03:20:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 119.0 |
| ec378491-1b8b-3504-98f6-5d38e099573c | -10.1592 | -36.4078 | 2025-10-14 03:30:00 | GOES-19 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 45.3 |
| 10e8fda8-44dd-3d2a-94b7-c735f2da0833 | -4.6509 | -43.1337 | 2025-10-14 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 40.7 |
| de62e6a9-3b9a-36d9-8542-18077c339952 | -12.838 | -50.6332 | 2025-10-14 03:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| f25e54e5-32cd-328f-8c59-80bf2bfdeb7a | -7.9253 | -44.1169 | 2025-10-14 03:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 96.7 |
| a5084198-74f8-361a-858e-49dc0c7409ee | -12.8568 | -50.6523 | 2025-10-14 03:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| a7cc0c4f-319d-3ae6-9740-bf40726f5568 | -4.8408 | -42.77 | 2025-10-14 03:30:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 109.9 |
| c76fe4a2-ab03-3269-8055-0123847b2cde | -11.7594 | -43.2898 | 2025-10-14 03:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 89.3 |
| d25c3b60-7bbd-3236-8d0e-8c099c0e4420 | -4.6696 | -43.1326 | 2025-10-14 03:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 26b4916b-92ab-3853-ad91-ea875f565e9f | -11.7401 | -43.2928 | 2025-10-14 03:30:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 988f35ab-52dd-35ff-9f5d-29da9a42a593 | -12.8184 | -50.6571 | 2025-10-14 03:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 87cacce3-9289-35ec-b258-c814b5f10d6d | -7.9439 | -44.1381 | 2025-10-14 03:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 06c38f59-eefe-3d26-a7fc-4ba8922002cb | -7.9442 | -44.115 | 2025-10-14 03:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 195.1 |
| a9a7614c-72e8-3f63-8876-cb8c5f3816e1 | -12.8376 | -50.6547 | 2025-10-14 03:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 08e5f064-7106-338d-8983-0f17a42581bb | -3.29526 | -43.50283 | 2025-10-14 03:34:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d434fe37-c20d-3e0c-a378-5cda4a46a18a | -3.1583 | -42.89146 | 2025-10-14 03:34:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf5506e7-bdd7-381b-8f3a-567a315353db | -3.04726 | -40.11026 | 2025-10-14 03:34:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 493b0344-dc35-37c0-b1d7-7eadba9b6d6a | -3.937 | -42.80765 | 2025-10-14 03:34:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 65db6f3d-9633-34dd-8693-b2873210025c | -3.72813 | -40.42803 | 2025-10-14 03:34:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 11.6 |


[Clique aqui para ver as próximas entradas](README6.md)
