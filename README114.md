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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b622e680-30c9-398c-93db-68fb79e91634 | -7.23932 | -44.8476 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4be8a6f6-799d-3a84-ac37-1b7e592b80a4 | -7.20324 | -44.8574 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 01ab4e1b-2840-3196-80b8-3192035cf63a | -9.34768 | -46.53875 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a2050824-c87f-38e1-82cb-c4b7d075030c | -11.16684 | -48.32046 | 2026-09-28 16:26:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58b31f2d-1e69-32ca-b772-1a210ec49bbc | -9.93425 | -50.24156 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 6c628658-5790-38ab-b992-d55cfe234cc9 | -7.27787 | -39.34435 | 2026-09-28 16:26:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 45.7 |
| 950f37be-e7d2-319c-ac01-fe1c94afb925 | -10.91307 | -43.8633 | 2026-09-28 16:26:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 90b6552b-1e79-336e-b269-30903230bfc3 | -10.70251 | -44.43029 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 50b6bdf9-e6fe-36c3-b6ca-8aa826c84e6b | -10.96876 | -50.69238 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| db96883e-fc8d-39f3-8c3b-c89ef041c9ca | -7.71252 | -44.9003 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2874c1a1-75ca-333b-bf1a-6bbbf4f86188 | -10.70661 | -44.43377 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| c4dbf94c-c0bd-3e99-85e1-674ced8fe77a | -7.25443 | -43.37336 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 6631972b-5663-3f65-b1a8-30d4537c477f | -7.0247 | -44.64753 | 2026-09-28 16:26:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 049e5932-1541-3d21-a21c-2a9fc20a092b | -5.14122 | -42.84241 | 2026-09-28 16:26:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7be68c09-6e42-3009-88d4-2433001e8b43 | -8.98066 | -44.15614 | 2026-09-28 16:26:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 9facecd7-457d-3555-afd5-900211089178 | -6.16324 | -52.81988 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 08147294-7adb-3973-8080-3d79d7b89e32 | -10.21976 | -50.00184 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 34117a6a-7b21-3ded-87f8-4b790a871a47 | -7.46911 | -44.5775 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| f23180e5-30bc-33e1-a564-7a82747dafe5 | -10.01608 | -50.24273 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 78b704b2-50a0-388f-9ded-fecb3b4c5f76 | -10.9841 | -50.68711 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cebf4bba-c773-3b5e-a837-64a30dc2b44c | -11.15099 | -50.07265 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| def02122-c729-3b4b-bc15-297a0d92530c | -8.91205 | -35.23027 | 2026-09-28 16:26:00 | NOAA-20 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 38f091b7-ecbc-36d8-849d-449a5a25e2e2 | -10.75869 | -50.59344 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 44ce5708-5c64-3903-ae05-df452f2066a8 | -6.77288 | -35.28717 | 2026-09-28 16:26:00 | NOAA-20 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 790d6e66-47b7-38f5-9d44-69c1c578c1c3 | -3.33908 | -43.33214 | 2026-09-28 16:26:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5ef74acf-3d23-30b3-909d-e48e6c4e499b | -9.30424 | -45.36755 | 2026-09-28 16:26:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ef395f95-e51b-3420-bd56-287a3507ea9e | -9.65641 | -42.32033 | 2026-09-28 16:26:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 6e761d2b-5aeb-3613-9767-12cf96f59ab1 | -8.83758 | -46.58523 | 2026-09-28 16:26:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7812ce59-7b76-362e-8463-b1a49c938541 | -10.90963 | -43.86378 | 2026-09-28 16:26:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 6c6eae7c-e474-36ff-924d-240b943faa4b | -3.4853 | -43.33422 | 2026-09-28 16:26:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2d85a5ac-b9cc-372b-b513-7c6e2765753b | -10.16019 | -46.57278 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ee088708-614b-3d88-b37e-4ac8f368d989 | -7.4318 | -55.63248 | 2026-09-28 16:26:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 235d3636-b84c-303a-b59d-fc915139f32e | -6.34022 | -41.91781 | 2026-09-28 16:26:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| e08e06f3-40cb-396d-b985-6a73ccc8c1eb | -7.2306 | -44.86057 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d3cba774-2cbc-3ee4-a535-6fadb982ed5e | -9.39712 | -46.38879 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 4ad02d0f-d8d4-3ac8-b933-0ed3bc2a8342 | -6.03575 | -49.56903 | 2026-09-28 16:26:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a452f8ae-a87d-385e-afb6-4642f885d472 | -7.60267 | -55.7007 | 2026-09-28 16:26:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ffe60be1-540e-3897-af8f-521b190a3262 | -11.16297 | -48.32546 | 2026-09-28 16:26:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f5a14b87-8b5f-309a-8252-a0cf9c6aeb36 | -7.23586 | -44.84811 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 9f9a4e04-fb8a-3178-b4dd-84794c5b84e1 | -8.69578 | -47.75063 | 2026-09-28 16:26:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 49eab002-9fa8-377e-87d1-9d0ea5c80c08 | -9.77443 | -45.97887 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 3d2b466a-808d-3a48-86a5-3c40d7683f64 | -4.28488 | -49.88984 | 2026-09-28 16:26:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1ad28453-72ce-3e2d-be43-e201a5f7ab52 | -11.07906 | -46.07246 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| da2b9fe5-fee1-3890-988e-d04876ba75bf | -10.98934 | -50.68644 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 141ceb9f-d828-3d9d-b09c-21742c7746d4 | -8.19447 | -50.1559 | 2026-09-28 16:26:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 052b86b6-fb64-3c05-b17b-5647efa2dfb2 | -9.081 | -46.5008 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 6287a815-d159-3086-a20d-0f22d8ebcf8e | -11.07483 | -48.88908 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 960601e7-6900-3b46-8970-92db7ceed430 | -8.33165 | -44.16563 | 2026-09-28 16:26:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e7e090df-15f5-3c56-bfed-b1c86cbc0d1a | -3.81171 | -44.09548 | 2026-09-28 16:26:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 07b81ee4-1c22-3f77-bc7d-db5c8d3b5473 | -10.23958 | -49.9992 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 4459366b-756e-357f-9cc7-1bc928fa465c | -10.12265 | -50.20095 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| eea07ba5-b912-3056-8a60-b960d88aa7a7 | -9.63208 | -46.82621 | 2026-09-28 16:26:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 72cdd50f-c310-3a22-bd11-2c49eb7d236c | -7.2353 | -44.8443 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 5b8f96fe-8185-3cb6-bf62-f5db89c88841 | -8.68911 | -47.44113 | 2026-09-28 16:26:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8845bf92-e700-3572-adfd-4c54fa245358 | -9.08429 | -49.87777 | 2026-09-28 16:26:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| b5fe77d8-4dc4-33d3-8722-9429d4ed522d | -10.88733 | -50.68326 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 51ac319f-1e6a-3380-9887-01f1db1debc0 | -6.99319 | -42.70297 | 2026-09-28 16:26:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| e51cbd90-b262-3417-a65d-22add713eb7e | -6.15813 | -52.82456 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 17fd8fcc-2cd5-3b1c-97a5-5111d9cde3d8 | -7.43323 | -55.63763 | 2026-09-28 16:26:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| eca8f48f-4003-343a-86a1-4ada820216e7 | -8.37954 | -45.45576 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| ae8886ef-0a51-3d44-8375-3182cdcc5322 | -7.49488 | -54.96894 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 83289061-5c1a-36e2-9fe3-78529ae71cf2 | -3.56098 | -39.03777 | 2026-09-28 16:26:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 3cbf8c1d-8f7c-3f6f-8424-d874d1dd8ed3 | -11.48171 | -49.74764 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 32.3 |
| ddd09381-d12c-38d3-bead-0dabb4100179 | -8.38795 | -45.4629 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 2fcd7c0f-be80-33f9-b802-4b49b371a8e2 | -11.15374 | -50.05432 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 9724c644-85d4-3b51-a6dc-454d5e99f83b | -8.64647 | -49.4812 | 2026-09-28 16:26:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d1ac736f-cf43-36c0-9638-a5793b84e4c9 | -9.77692 | -44.84211 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 243c85cd-f875-3eca-9510-3bd1dffa8b93 | -9.02861 | -50.80634 | 2026-09-28 16:26:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 4e80f34d-7edf-3cf2-bf8d-a8d1d4c1a5f4 | -6.83933 | -43.56781 | 2026-09-28 16:26:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 08301108-bfcb-3db5-bbd5-782d48cfaa4f | -6.7763 | -35.28586 | 2026-09-28 16:26:00 | NOAA-20 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d833a596-aa28-3c6a-a7d5-fb1aa9b80a95 | -11.65632 | -50.6838 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 500ea90c-60c4-39e4-a4bd-b56d28bb0605 | -8.43708 | -39.50111 | 2026-09-28 16:26:00 | NOAA-20 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 03f5315a-39d7-3a81-a71a-725b01b81f62 | -7.53163 | -47.85361 | 2026-09-28 16:26:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 06d71014-e273-357a-a414-814504ae6d85 | -9.97593 | -50.13198 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 80b68c63-0a08-3753-8503-da3cda75890a | -8.0292 | -42.84321 | 2026-09-28 16:26:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 27b9083d-f929-32cb-8fe5-773710e83b4d | -10.86731 | -48.51022 | 2026-09-28 16:26:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f38bf1ea-9a0c-37b0-a94e-68950dca0121 | -7.21161 | -45.08098 | 2026-09-28 16:26:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 0d1db9c2-125f-3bb5-aa7b-1872dcba2d49 | -4.44825 | -42.48427 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| fd762f80-72bd-39de-8eb8-8cae5a0cf3c6 | -7.66735 | -45.48028 | 2026-09-28 16:26:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 0def3e8f-0ffa-3d56-81b5-bd6582f92c29 | -7.69349 | -44.86771 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5875e3d5-e720-30fc-887f-3f05a487fb12 | -11.45622 | -49.74516 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 68314249-b73b-3e38-957f-f1b69530a316 | -7.21103 | -45.07708 | 2026-09-28 16:26:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ec86dfcd-3c7a-3a87-94ec-98476fc166bc | -7.70894 | -44.92443 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 6486e263-5e74-36e9-8f39-a13b138db4cb | -10.78248 | -42.65581 | 2026-09-28 16:26:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 5d2ca1e1-5067-36e3-825f-8a3538c7166b | -10.68781 | -44.45284 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 479b6c1d-9d15-3e0c-bd30-ea28aa376fb6 | -10.13018 | -45.14173 | 2026-09-28 16:26:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 7937060e-9bed-3926-875c-0376acfff408 | -5.8606 | -45.91779 | 2026-09-28 16:26:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 398549d2-85e9-3729-99ad-a304045c51bc | -6.87499 | -42.8392 | 2026-09-28 16:26:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 44751f39-3435-324d-b8e8-5568747fa8ab | -11.08412 | -48.88786 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 142.0 |
| d66d34f6-363d-3604-8cf1-99553ff7ff58 | -11.19183 | -50.0373 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 887ffe56-03e2-36e3-9698-0a64b48ed774 | -8.77659 | -45.82611 | 2026-09-28 16:26:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 3d2c8191-fbd9-3ea9-9d31-d4d525cb5485 | -8.56144 | -44.041 | 2026-09-28 16:26:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3331a052-e422-3dcd-84f4-846f6c903dfd | -7.63747 | -45.51711 | 2026-09-28 16:26:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bae84bbe-fded-3a9d-a621-c2d0ccf4f2ee | -11.13472 | -50.06574 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| db6cfa01-ebec-31df-aedc-c6265f73ad57 | -9.9611 | -46.09772 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 04f05e12-91c3-3585-9f90-d040156a145d | -9.37151 | -49.17572 | 2026-09-28 16:26:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7664bcf0-1ed7-3f7f-9193-a209420e7422 | -10.96795 | -50.68589 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 315bcecf-98b6-3bce-8979-0f0d6738b327 | -10.00078 | -50.12188 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8d25beb6-65b9-31a2-b552-ab228b0bf87b | -9.31618 | -46.56812 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 086d8459-a768-3d7c-9ae1-acdb5afa11ed | -10.89462 | -50.69875 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |


[Clique aqui para ver as próximas entradas](README115.md)
