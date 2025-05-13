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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d42395c-1b7a-30ae-88f6-a2445461c3cc | -13.55795 | -52.87521 | 2025-05-13 04:14:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4c089ae5-733a-38d8-85c3-0182d8f86fa8 | -13.98411 | -56.80795 | 2025-05-13 04:14:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8a249c08-f8e1-3232-85ea-2d2b5e0d2fec | -11.61481 | -48.00534 | 2025-05-13 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2424f670-6cff-305b-869f-d8d3f6ac697a | -14.18836 | -45.47893 | 2025-05-13 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af2a8579-99d3-323c-84d6-bbc973b03f40 | -13.06493 | -52.02023 | 2025-05-13 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1339c187-0705-3622-9944-1054bd9847e5 | -11.78891 | -47.354 | 2025-05-13 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c6f7164-e5c9-3d9c-a706-c37a87817ef1 | -13.39594 | -47.63142 | 2025-05-13 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a958e04-7acf-31de-996b-308150cb6d2b | -13.09298 | -52.28922 | 2025-05-13 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df24602b-45a5-31c2-a8b7-11615b08a4da | -12.17519 | -44.34211 | 2025-05-13 04:14:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae6e5fb8-2bc9-3dbf-9396-90abf876ba5d | -13.55902 | -52.86968 | 2025-05-13 04:14:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d6b62bab-0972-3622-8242-1c299e6377cb | -12.17575 | -44.33859 | 2025-05-13 04:14:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ef5ee94-b88e-3809-91ae-1bd804cae96c | -13.98018 | -56.7958 | 2025-05-13 04:14:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d5012ba9-e9b9-37b9-90bf-33c1a08269b6 | -13.97397 | -56.79442 | 2025-05-13 04:14:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 78ac8b7f-fa33-3144-b961-be9823c2582c | -11.99795 | -43.78235 | 2025-05-13 04:14:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92ced695-99b7-3282-8b08-efc891e4057b | -11.25317 | -52.47083 | 2025-05-13 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 233d8b2a-c31c-3ba9-b312-ce56da42ea50 | -13.36813 | -47.60043 | 2025-05-13 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 842f8500-6b0f-3a56-a035-a243ff64562b | -12.179 | -46.71054 | 2025-05-13 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49e73c05-cea0-3b50-bbb7-af7b02ecd775 | -15.60775 | -46.60096 | 2025-05-13 04:14:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e56edd1d-1371-34b6-bf58-55cc765478d0 | -10.65684 | -44.40818 | 2025-05-13 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ffb23ab-1c52-3f86-869f-348d6bc71474 | -13.55305 | -52.87424 | 2025-05-13 04:14:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fe5c7e09-dbf8-36e9-b869-9e508d8c198f | -11.79781 | -47.41158 | 2025-05-13 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e52caefe-cc16-3d5b-bb1c-573de8dca286 | -16.55334 | -46.84762 | 2025-05-13 04:14:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 476033c5-bf3b-3359-be45-26f49e39dbc4 | -13.56284 | -52.87618 | 2025-05-13 04:14:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 43b9adb1-0b4d-3b56-97cd-ca9b323b1b8e | -14.19226 | -45.47591 | 2025-05-13 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a31d2a26-5b0f-391e-ab9c-ed8b980be809 | -14.18324 | -45.47156 | 2025-05-13 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce2566fd-4443-32b6-a85e-fa6f1f67ece4 | -13.39417 | -47.63408 | 2025-05-13 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cbaad27f-ab93-3aa6-8c56-c68428f6307e | -11.61032 | -48.00922 | 2025-05-13 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b8a0e11-946d-3421-b7ae-5f67be6beb80 | -13.3906 | -47.63348 | 2025-05-13 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e34cea80-cd9a-302b-8726-96ed11271741 | -11.77519 | -48.20292 | 2025-05-13 04:14:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1386a5b7-69fb-3227-bf99-8012c1b0ac02 | -12.2861 | -52.49229 | 2025-05-13 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3a94638-e780-3b7c-a597-bca8b852d17f | -10.49783 | -46.18056 | 2025-05-13 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ab55737-df31-3221-ab2e-971a4cab47fb | -14.18438 | -45.46441 | 2025-05-13 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4354d58d-6e68-3fbc-bdc6-16424f82a71f | -14.19111 | -45.48306 | 2025-05-13 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60366bcc-39c7-3981-ab85-e65fbcd4ca3d | -13.3949 | -47.62982 | 2025-05-13 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20a6aebe-faee-3785-b244-c6071ba554d1 | -13.5552 | -52.86315 | 2025-05-13 04:14:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 090823f0-460f-39c4-93dc-6b0b9c008e9a | -12.83725 | -47.41368 | 2025-05-13 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62a04f5a-7844-38cb-888b-9d497ef50d02 | -13.07176 | -47.80396 | 2025-05-13 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf8c3cd7-b727-32a6-a14d-e0368af2cbbd | -13.5688 | -52.87166 | 2025-05-13 04:14:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 02d7a6b9-d475-37b5-9682-915586ea57d4 | -11.79824 | -44.27685 | 2025-05-13 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8b86cd56-110a-32e1-b40b-6d35e314cf18 | -11.58108 | -47.6117 | 2025-05-13 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a59035a7-a5e0-3d82-a285-0a0cffa7711f | -10.04605 | -49.6622 | 2025-05-13 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce7fbe71-9761-3c71-9434-6fd90741791e | -15.56995 | -47.85677 | 2025-05-13 04:14:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59d67834-ad77-3dfb-84cb-ba385c56aef3 | -11.79491 | -47.40675 | 2025-05-13 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 87c81c5e-cd14-361d-a3d3-f0d91273d9ab | -11.78499 | -44.2747 | 2025-05-13 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2270ee4-d3e1-3576-a6b8-4b4e3470f8c6 | -13.39524 | -47.63568 | 2025-05-13 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7845063-e4b3-3075-a536-d998b6c0bfe4 | -14.18951 | -45.47178 | 2025-05-13 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9afeaf0d-b76d-36ef-96d1-87d409d70706 | -10.66001 | -44.40864 | 2025-05-13 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4e152aa-8fda-312e-80ea-01214f5395c3 | -13.3717 | -47.60098 | 2025-05-13 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4b20df34-1aeb-3169-acf7-7f3c7bacf43b | -20.21635 | -46.74248 | 2025-05-13 04:17:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b848ce21-fd39-3191-bbd1-d47f7600d79a | -20.34838 | -47.03886 | 2025-05-13 04:17:00 | NOAA-20 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f06a4793-99b8-3e9f-a5db-551e0d061104 | -20.21576 | -46.74615 | 2025-05-13 04:17:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1cf135d7-bf5b-3da8-b97f-ffbc4f002074 | -20.21539 | -46.72717 | 2025-05-13 04:17:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebe4cf9d-8201-3c8e-8937-d0a1a3aac99f | -20.22085 | -46.73572 | 2025-05-13 04:17:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 832ecfb0-cbb2-337f-aef5-381c6ee19d15 | -19.15883 | -47.81867 | 2025-05-13 04:17:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1f438554-af9c-341e-a18a-baa44f8f3a74 | -20.4775 | -53.67712 | 2025-05-13 04:17:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a917c3fc-b6c2-3f29-8731-61be7999ceae | -20.21849 | -46.75041 | 2025-05-13 04:17:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c19d81ec-ab51-3356-a5cb-9fb01c66a23e | -29.32459 | -51.91525 | 2025-05-13 04:17:00 | NOAA-20 | ARROIO DO MEIO | RIO GRANDE DO SUL | Brasil | 4301008 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| aaff5f1c-634a-3089-9ba6-069fc7ee8f7b | -19.90151 | -44.69783 | 2025-05-13 04:17:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a31a966-fd23-3681-bb00-ed39b8499c7d | -21.78751 | -52.74046 | 2025-05-13 04:17:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e25be6c-e847-3aa7-b6e0-3ef1a354b10b | -20.21753 | -46.73513 | 2025-05-13 04:17:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0f96c1d-cd03-3a98-910b-4baed835d43b | -20.22298 | -46.74367 | 2025-05-13 04:17:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c09c9a3d-c2a9-3fd7-aa9d-535ee9da994d | -20.21517 | -46.74983 | 2025-05-13 04:17:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63b85703-00b6-378b-9aa2-8f717b35e0ac | -19.15948 | -47.81477 | 2025-05-13 04:17:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3512bce3-8cd6-31f4-829f-8780abb98a49 | -19.36156 | -55.26131 | 2025-05-13 04:17:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 0445748c-c7ae-3de2-85db-07581e11b411 | -16.60323 | -53.39991 | 2025-05-13 04:17:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bc668f6-d3cc-3538-8956-232d30d9ed00 | -19.36222 | -55.25809 | 2025-05-13 04:17:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 92ed8276-b4a7-3e94-86c2-97136e36f2d6 | -30.15091 | -52.02556 | 2025-05-13 04:17:00 | NOAA-20 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 5b806714-e02c-3b5d-81e3-2e5b0fd02dde | -22.98336 | -50.84825 | 2025-05-13 04:17:00 | NOAA-20 | SERTANEJA | PARANÁ | Brasil | 4126405 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| aa67d004-1f1f-3cae-b1ef-cf68001f6ca7 | -23.54893 | -47.63253 | 2025-05-13 04:17:00 | NOAA-20 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c9c6412f-57eb-30ee-a1f5-ab2ddb197f44 | -20.21812 | -46.73145 | 2025-05-13 04:17:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93c6ceb8-bf83-38ef-8763-df63c3160f09 | -19.36344 | -55.26036 | 2025-05-13 04:17:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| fb4b72d4-e958-3f0c-83e8-9a05348fb53f | -20.21791 | -46.75407 | 2025-05-13 04:17:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed38cb14-9681-3be0-b47e-e387dbe94b50 | -19.41581 | -44.34225 | 2025-05-13 04:17:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19873f9b-3e9e-3edf-a5d5-ea8503f06465 | -21.77835 | -52.74277 | 2025-05-13 04:17:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c187393a-5cd6-31d3-9233-627aa5f658ea | -20.99511 | -51.79304 | 2025-05-13 04:17:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e1044f11-7ca1-3462-80e8-d12fde91a70d | -21.78253 | -52.7437 | 2025-05-13 04:17:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48c18285-d505-3005-8eeb-ff9462250a3e | -8.07 | -43.1216 | 2025-05-13 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.9 |
| 293b1838-6eaf-38ff-b970-e56e70d4145a | -13.9902 | -56.8058 | 2025-05-13 04:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 2a98fecd-8d60-3f0d-a00a-69ac280f2edb | -8.0889 | -43.1196 | 2025-05-13 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.0 |
| 9eeaf568-6e53-3036-9a20-8e7c496b2d58 | -13.5683 | -52.8783 | 2025-05-13 04:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| a7c884d5-dde9-31ac-a110-1955dc934168 | -8.07 | -43.1216 | 2025-05-13 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 67e27848-fc1c-312b-8865-da0bfb12b18d | -13.5683 | -52.8783 | 2025-05-13 04:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 5bab3f37-c320-3b0e-bbf2-4c17c6c67740 | -8.0889 | -43.1196 | 2025-05-13 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.6 |
| c6b2a5d7-f5a6-3d60-84ec-cd852845a605 | -13.9905 | -56.7855 | 2025-05-13 04:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 8cb9efc2-17b4-3f84-b5fa-dd01e26795bf | -13.9902 | -56.8058 | 2025-05-13 04:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 94e94b52-b4a8-346d-8d4e-e6aabcb883b5 | -8.07 | -43.1216 | 2025-05-13 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 57.7 |
| fc43c8a9-7376-3993-96ed-9c6c481705a4 | -13.971 | -56.8077 | 2025-05-13 04:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| aa8a77bc-6731-3f6e-b411-52367bae3780 | -13.5683 | -52.8783 | 2025-05-13 04:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| a25430ee-3133-3fe3-9c3b-78810c8325f6 | -13.9902 | -56.8058 | 2025-05-13 04:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 229935ce-b8af-321c-b88c-cdc222acd141 | -13.9905 | -56.7855 | 2025-05-13 04:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 0a10631a-95ab-3cb6-b334-fdc092f3037d | -8.0696 | -43.1452 | 2025-05-13 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.5 |
| e012f5b9-1f75-38f3-adb8-aa457c45b391 | -13.9902 | -56.8058 | 2025-05-13 04:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 7fdf655b-8b74-3085-8a67-ebe4b81d8228 | -13.5683 | -52.8783 | 2025-05-13 04:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 8b435c3c-d144-30b8-add7-cf8181497192 | -8.07 | -43.1216 | 2025-05-13 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.9 |
| 689a1b23-5c70-3887-a055-f1da46cc8c1e | -13.971 | -56.8077 | 2025-05-13 04:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 45.9 |
| daacd15b-4d6a-3d38-a3f0-c21cb95b8e5f | -8.0886 | -43.1431 | 2025-05-13 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 47.0 |
| 6a60b720-f658-3731-93fe-c52ee0108984 | -8.0889 | -43.1196 | 2025-05-13 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.4 |
| ad64b3a8-acf5-32ae-87a6-5c4040ca2884 | -13.9905 | -56.7855 | 2025-05-13 04:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 39.5 |
| a13fce02-70d9-3803-a6a8-fe8da35e1942 | -8.07 | -43.1216 | 2025-05-13 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 121.3 |
| 9407962f-d057-3ffb-9444-429d249d274f | -13.5683 | -52.8783 | 2025-05-13 05:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |


[Clique aqui para ver as próximas entradas](README9.md)
