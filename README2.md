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
| c96e4e90-981f-3825-af53-3e3fe35a8742 | -17.61442 | -46.69715 | 2025-04-08 03:30:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39251087-7b0a-3f42-a7fb-56978ce8c6c0 | -17.92067 | -45.52929 | 2025-04-08 03:30:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e37ff55-5ccc-3ab6-9a2b-04588a88162a | -17.6182 | -46.69859 | 2025-04-08 03:30:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d977222-15b4-3837-af3f-03cf135b3881 | -20.68094 | -48.81472 | 2025-04-08 03:32:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 8ec036b8-452f-3b37-be4e-03cc2e09973f | -19.7104 | -44.76938 | 2025-04-08 03:32:00 | NOAA-20 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| df914cbe-89ca-3041-a892-21d33ac2b125 | -21.57799 | -48.61588 | 2025-04-08 03:32:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7595f160-610a-3595-9966-1cab63b0d519 | -22.881 | -43.71756 | 2025-04-08 03:32:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c1292dbe-cffe-3200-bd3f-39ecbea50380 | -20.67948 | -48.82083 | 2025-04-08 03:32:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 9e4ce055-1d0d-3657-afa7-8b08a4308441 | -19.7475 | -48.13795 | 2025-04-08 03:32:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d7b53fb4-7b63-39d3-9380-d903eb13f476 | -19.75401 | -48.13934 | 2025-04-08 03:32:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2f86f635-1a47-3897-834c-836f5309836b | -20.99141 | -47.35618 | 2025-04-08 03:32:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9be7ed39-6525-3a45-bd71-f3502946a2b0 | -19.75539 | -48.13359 | 2025-04-08 03:32:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 10454dfd-3f1a-304b-82c9-fcd24ac0d99f | -21.57152 | -48.61453 | 2025-04-08 03:32:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6df104c2-3941-33bd-bf1d-b4ebc7d89608 | -22.67442 | -42.85717 | 2025-04-08 03:32:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| be6134de-b636-3758-b397-ad4722223330 | -20.68443 | -48.81618 | 2025-04-08 03:32:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 87d6e586-3ef9-3dd9-b337-7a122b64adab | -22.67717 | -42.85707 | 2025-04-08 03:32:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a94b8a6f-0005-3b2a-a27f-9fd613bdf555 | -19.74981 | -48.13164 | 2025-04-08 03:32:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| cc082516-dc4e-356b-98b8-4f436bc220bd | -20.68292 | -48.82232 | 2025-04-08 03:32:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| c2b5e5de-4abf-3b13-b415-3740eb48292b | -21.86516 | -44.12149 | 2025-04-08 03:32:00 | NOAA-20 | BOM JARDIM DE MINAS | MINAS GERAIS | Brasil | 3107505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b4e191f7-22de-3828-99ac-e2cfa648b48a | -19.70959 | -44.77314 | 2025-04-08 03:32:00 | NOAA-20 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cbd61228-6bc0-3599-9f8a-203d9a4ec20b | -20.68747 | -48.81659 | 2025-04-08 03:32:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 16384eec-0a22-3096-9dfe-9fb8011d1bd5 | -19.74893 | -48.13203 | 2025-04-08 03:32:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 80b24e7d-eae6-3a70-aa5b-a32a56699861 | -19.74841 | -48.1376 | 2025-04-08 03:32:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 891405ce-9f40-3b31-a4b7-e32a397ee4c4 | -19.75491 | -48.13905 | 2025-04-08 03:32:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82e35451-b9e0-306f-b960-33bd3b4f4d3b | -12.08645 | -45.60986 | 2025-04-08 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b984302-d792-3a8c-b8de-c1ab91869d61 | -12.11029 | -45.63628 | 2025-04-08 04:46:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d98b856-0eac-3f06-b485-6a4ed297a976 | -6.87373 | -41.68517 | 2025-04-08 04:46:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 0bc6dd27-927b-3587-913f-28b449d41f2a | -13.19125 | -38.89451 | 2025-04-08 04:46:00 | NPP-375D | JAGUARIPE | BAHIA | Brasil | 2917805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ecf1d7d6-7c5e-35bc-8914-a9a40e5f7a1c | -12.10876 | -45.62928 | 2025-04-08 04:46:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 101f20df-75ca-3e54-80f1-d08299a4fc08 | -10.70787 | -46.53463 | 2025-04-08 04:46:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6f3f45f-048c-3b3a-9442-a4a696c83791 | -10.72054 | -42.33246 | 2025-04-08 04:46:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e0fec330-8343-3649-8e96-71206173bca8 | -13.19757 | -38.90196 | 2025-04-08 04:46:00 | NPP-375D | JAGUARIPE | BAHIA | Brasil | 2917805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 3d6da9ec-85a8-308d-9b21-f9836a29ebbb | -12.11325 | -45.62989 | 2025-04-08 04:46:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db53255b-e932-34e8-b128-d512b8967741 | -12.11384 | -45.62532 | 2025-04-08 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65225745-e71d-3e3a-988a-389ec29307c4 | -12.26787 | -41.29673 | 2025-04-08 04:46:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3f82e97e-4c60-3b8c-8f8f-f6f712bdcfff | -12.11267 | -45.63438 | 2025-04-08 04:46:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6dfe930-f2ab-35e7-842b-d35a8811f1ae | -12.11091 | -45.63179 | 2025-04-08 04:46:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e9ab120-c9fb-3f07-a7ea-72b52d691c00 | -12.11054 | -45.61548 | 2025-04-08 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97a622ed-435e-3647-939e-cf82bb1ece3f | -12.41616 | -46.81026 | 2025-04-08 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 611774f8-8ba3-3c0b-8cfd-c56096989fb2 | -12.11602 | -45.62785 | 2025-04-08 04:46:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 052b98c8-c803-3bd7-917c-aa6b82157b21 | -10.24058 | -49.17281 | 2025-04-08 04:46:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa1d3728-e8f0-34ff-a98b-9770410e4672 | -13.18351 | -38.90049 | 2025-04-08 04:46:00 | NPP-375D | JAGUARIPE | BAHIA | Brasil | 2917805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| a3a462aa-7f1f-353b-9429-d72693d26046 | -12.41668 | -46.80644 | 2025-04-08 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b4c57b4e-da9c-3a01-90c0-328e41c0c7ff | -6.26803 | -44.96589 | 2025-04-08 04:46:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c0dee62-c801-3eb6-a6ad-16252ed71f46 | -10.7155 | -42.32812 | 2025-04-08 04:46:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 51c9be65-53b8-3913-b2e2-3ca9bdeafd82 | -6.5398 | -43.09058 | 2025-04-08 04:46:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ad36cb1-6b39-39a2-bbb0-f9669ed01a2c | -10.23998 | -49.17685 | 2025-04-08 04:46:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eea5c90e-574f-3c23-acff-d0af7898e818 | -11.96768 | -48.08762 | 2025-04-08 04:46:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03da39b1-145d-3ccc-94d5-e204893f9121 | -12.10829 | -45.61745 | 2025-04-08 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e2853ab-ed4d-3ad0-9788-06308a033b8d | -10.72101 | -42.32884 | 2025-04-08 04:46:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7180604c-9302-3270-8b36-b3c5d6883f28 | -12.10642 | -45.63119 | 2025-04-08 04:46:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae9b32b7-ce8d-3ec6-8dc8-de0e7195fb8c | -10.70582 | -46.5348 | 2025-04-08 04:46:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| efa2a860-4d5d-34f7-862f-d72e90d9621c | -12.11278 | -45.61808 | 2025-04-08 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03f5d870-808f-34fa-876b-fb3f1af43fce | -13.18422 | -38.89375 | 2025-04-08 04:46:00 | NPP-375D | JAGUARIPE | BAHIA | Brasil | 2917805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| a3009549-4869-3560-8830-e7b4423545b0 | -6.68117 | -43.56449 | 2025-04-08 04:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d0175f86-49f3-330d-9bab-62f3ba7b3ead | -12.11215 | -45.62268 | 2025-04-08 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07dbecf5-1637-3896-9fe8-82d3f6d7dc7d | -10.71503 | -42.33175 | 2025-04-08 04:46:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fae4de3b-f02a-3f68-827c-3bb48d43d5ff | -12.11444 | -45.62073 | 2025-04-08 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 609b8d98-720c-3ab6-bcee-7326d121a9b9 | -13.19829 | -38.89516 | 2025-04-08 04:46:00 | NPP-375D | JAGUARIPE | BAHIA | Brasil | 2917805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6fd955b6-6630-3a27-ab18-0d4c3fc206f7 | -6.87916 | -41.68611 | 2025-04-08 04:46:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 6074791d-a885-32c5-be1b-0e9498a0db1a | -12.1154 | -45.63236 | 2025-04-08 04:46:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f58eb163-e130-39ea-ab8c-765a92368aec | -10.24352 | -49.17738 | 2025-04-08 04:46:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26dc8bfe-6282-35f7-b9d2-be8cfb984c6e | -12.10818 | -45.6338 | 2025-04-08 04:46:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6533e9a-ecf3-3a32-ba02-3acdb61c7e83 | -10.24412 | -49.17336 | 2025-04-08 04:46:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26e51ad2-cff8-3234-a7e4-7a3275a172a6 | -6.68523 | -43.57017 | 2025-04-08 04:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3b65a0b-dfd2-3baf-8c2c-1241e04813d9 | -10.71998 | -42.33135 | 2025-04-08 04:46:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 72577636-a6ec-3603-9ce2-8dbdcdf5aedd | -10.70996 | -46.53535 | 2025-04-08 04:46:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 052807a6-faad-31e1-b5e6-5a9c645f4e00 | -12.11153 | -45.62727 | 2025-04-08 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b88b019-b80e-37ea-9b10-7db3b0abcb96 | -17.62157 | -46.6274 | 2025-04-08 04:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc63835b-c55a-321d-8980-153e6e9114b2 | -14.20236 | -44.35342 | 2025-04-08 04:49:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80c3cdf5-7ecd-3100-af62-674012896429 | -17.61734 | -46.69868 | 2025-04-08 04:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32e72406-7ee6-3361-8dc0-4a4c73a5b2f8 | -15.07794 | -48.94363 | 2025-04-08 04:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 582944c9-2c33-3685-a21e-9876bbece2da | -15.56876 | -47.85508 | 2025-04-08 04:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7132cf4-3d9f-39ae-a8e5-1f3be1f95a5e | -17.92127 | -45.53434 | 2025-04-08 04:49:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b68eda89-a0ca-3386-aa3b-e1507e7c0a9f | -14.20171 | -44.35318 | 2025-04-08 04:49:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d08e79b-5e29-332d-9ef8-b44201eedfdb | -17.92192 | -45.52859 | 2025-04-08 04:49:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 409ee3da-1887-3ac8-b2cf-530134bc7404 | -14.19732 | -44.35275 | 2025-04-08 04:49:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aaf220fc-ac25-3c98-8b46-10f457d46b6d | -18.14576 | -47.80097 | 2025-04-08 04:49:00 | NPP-375D | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 868e36ae-4aee-35ee-a6b6-b7c157966816 | -12.27632 | -63.81344 | 2025-04-08 04:49:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9508930d-479f-3ef1-8905-d9f120c35b0a | -15.26456 | -51.47353 | 2025-04-08 04:49:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5140590-8d82-3322-b1e4-7c1b90cee0d6 | -22.54121 | -48.81285 | 2025-04-08 04:51:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 236bc9c3-b43f-3896-b7e3-3d06f9e1afc4 | -21.85666 | -54.78009 | 2025-04-08 04:51:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2ff8f314-5b62-3010-9c1d-ca9c9812eb63 | -20.58393 | -56.04543 | 2025-04-08 04:51:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a1d3afd3-53dd-3840-8fd8-a3ce69716790 | -19.71243 | -44.76902 | 2025-04-08 04:51:00 | NPP-375D | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7787f48f-bbb4-3048-98bf-d35fbacc4e8d | -21.76978 | -55.32167 | 2025-04-08 04:51:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81150bdb-999c-3224-a312-61be49f6fd2d | -20.83264 | -47.76034 | 2025-04-08 04:51:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 15b2582b-ff5d-3dfa-876f-b78c762bcf49 | -22.47417 | -51.71539 | 2025-04-08 04:51:00 | NPP-375D | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 4fb7673e-809e-3652-9d7b-d6cba8ef60fa | -20.68317 | -48.81561 | 2025-04-08 04:51:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 40691306-8351-3bb9-b870-8a85ee90771c | -20.68776 | -48.81242 | 2025-04-08 04:51:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 486b4ec7-940f-322c-a76d-53d08e939b04 | -20.76424 | -46.77002 | 2025-04-08 04:51:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2b34c096-21d8-326c-98eb-408cbfd19d8a | -20.58328 | -56.04932 | 2025-04-08 04:51:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1a92b64e-9910-328c-a744-d973be4ce7ea | -22.00062 | -47.21734 | 2025-04-08 04:51:00 | NPP-375D | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0e4bc3bd-8604-369b-87df-d17889f729fc | -20.83224 | -47.7623 | 2025-04-08 04:51:00 | NPP-375D | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2e28286c-b165-359b-aa52-00f630bc23d9 | -19.16068 | -47.81924 | 2025-04-08 04:51:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 592276de-d21d-3c50-a216-4e67b7b2ea60 | -22.94504 | -49.22267 | 2025-04-08 04:51:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2db83f34-ccea-30ed-b6b1-7fa4cee7c897 | -23.76651 | -53.13546 | 2025-04-08 04:51:00 | NPP-375D | CRUZEIRO DO OESTE | PARANÁ | Brasil | 4106605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bb1a91df-6b46-3b1f-86f6-d61812a68f7a | -21.57816 | -48.61179 | 2025-04-08 04:51:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7456b766-5a65-3fda-b644-5fc9f2cd0e5d | -23.40553 | -46.55927 | 2025-04-08 04:51:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| afdeecb8-485a-318c-8969-9320ba153db9 | -21.77039 | -55.31791 | 2025-04-08 04:51:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a88dd40-3863-3562-b180-44d546111c5d | -21.85726 | -54.77637 | 2025-04-08 04:51:00 | NPP-375D | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |


[Clique aqui para ver as próximas entradas](README3.md)
