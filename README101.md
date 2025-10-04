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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b55ed413-1f10-3a04-ac7f-7ca384fa707e | -8.95797 | -48.68614 | 2025-10-04 05:04:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0fbb590d-509d-3a59-b69e-3cd7869d8a27 | -9.99701 | -48.27328 | 2025-10-04 05:04:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 810f1519-3261-399f-a7f9-0b294499eeb4 | -8.51105 | -54.59796 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05057f09-85bc-3ed0-afbf-58a0a269fd76 | -5.69324 | -49.30533 | 2025-10-04 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e4c5f644-92bc-3e2f-99da-85c046e0d029 | -4.95311 | -45.06651 | 2025-10-04 05:04:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b72e3c1a-e52d-31b9-ab76-08d84ba2e0d8 | -8.76017 | -49.90837 | 2025-10-04 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a81bc29f-1a44-391a-a542-44591cc05b54 | -10.20841 | -48.18589 | 2025-10-04 05:04:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e514df89-febe-3fea-8581-c2ad16df0988 | -4.21807 | -51.126 | 2025-10-04 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c97b9c54-dc87-3415-b04f-123de563981c | -9.67136 | -48.22868 | 2025-10-04 05:04:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cbb6d8a3-b6c9-36bb-9f06-df7c35ffa13d | -5.24196 | -45.55133 | 2025-10-04 05:04:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| edb46357-c67e-360d-8acc-acc2f1edb985 | -7.35379 | -44.34568 | 2025-10-04 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4c95b771-501b-3c38-8690-64f38225f1a7 | -6.8778 | -47.24087 | 2025-10-04 05:04:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 5fd8af39-4561-3cd9-aa56-d0eaa9fe72f3 | -8.17653 | -44.13083 | 2025-10-04 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1204b364-9618-3633-b414-b635e817b653 | -7.73807 | -46.31602 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| cf3cd250-65c8-3e0c-98bb-fc07beb1445d | -6.31354 | -44.27155 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92073023-001d-34ac-a888-39e2c9bee3ce | -7.04283 | -42.77988 | 2025-10-04 05:04:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6d6a7fd4-e147-380c-a191-377351b43cf2 | -5.33084 | -43.34955 | 2025-10-04 05:04:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d565f5b-ded9-3e3b-982e-50d1f1f26a66 | -7.91655 | -49.64164 | 2025-10-04 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 740f8305-83d2-39eb-b8fd-5a11fd6f97b7 | -6.66243 | -42.82357 | 2025-10-04 05:04:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 83dfb5eb-a5ca-35d8-9352-5683381edf51 | -5.66231 | -42.71732 | 2025-10-04 05:04:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| d475b300-012c-3a84-b526-e9124bf1db20 | -8.62571 | -55.00151 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 12e93c40-eb94-336e-bab8-d67d12e137dd | -6.87307 | -47.23703 | 2025-10-04 05:04:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| d00a41a3-f668-3f5a-8f9a-f391f3e853ca | -6.09502 | -43.48386 | 2025-10-04 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8ec28553-ebc2-3c70-8dc3-3e004a2fff16 | -7.76649 | -42.61523 | 2025-10-04 05:04:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6b7262be-4ffe-3dcb-81ca-f45396ed2f7b | -7.05657 | -42.78204 | 2025-10-04 05:04:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f514714a-ba03-39bb-99a9-d1be3a71f690 | -7.75077 | -42.5266 | 2025-10-04 05:04:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 1fb69a7b-8218-3202-9774-f6c06a503539 | -9.98123 | -50.24128 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b57a9b02-d68c-3bde-ab3c-a858cf94aaad | -5.69701 | -49.31034 | 2025-10-04 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8eb12273-4fee-3371-b3b0-a3ded2b051a0 | -7.64882 | -45.47379 | 2025-10-04 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f6424e0-c7b2-3a5b-8a40-14b60b7cba67 | -9.34579 | -45.79881 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 78655015-4a39-3b51-aac9-b38919faa076 | -6.34473 | -43.45259 | 2025-10-04 05:04:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 86544dad-f8fc-3348-9f08-75d4f6596f80 | -9.95423 | -50.24186 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e2a6663-039d-364b-b56c-80e310fd7ccc | -6.72722 | -45.97088 | 2025-10-04 05:04:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7393d7d9-18e0-3f9f-9a3e-d3952720087c | -3.84675 | -41.56278 | 2025-10-04 05:04:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| dd20c5b4-1e97-3763-9719-ab42bcdcae56 | -3.8496 | -41.56268 | 2025-10-04 05:04:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 6fa0ebfb-e8a9-3f8f-aef7-fb46d6c90c46 | -2.93394 | -54.17631 | 2025-10-04 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 483d8703-86cc-34ed-b451-24398bf0f2b3 | -9.91492 | -50.50122 | 2025-10-04 05:04:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b793c6d7-8988-3477-860a-3ac08cf7acea | -5.14035 | -46.04053 | 2025-10-04 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db9023c2-e15d-3d33-9828-5a668b79f592 | -9.88357 | -47.81416 | 2025-10-04 05:04:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37f054f3-7d20-3f75-a627-59f441f3487e | -6.28 | -44.04409 | 2025-10-04 05:04:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f73b94e3-022e-3172-b39f-f3cb32a0e7d8 | -9.32473 | -54.53087 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3e171f70-2cfb-3d64-97b6-21481f126ff7 | -9.34294 | -54.52595 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a856cdee-342e-3f6e-a979-30342d24d1c0 | -3.73347 | -51.33566 | 2025-10-04 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce57d015-59ad-354a-96dc-60e44b107569 | -7.00611 | -42.30248 | 2025-10-04 05:04:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ec552229-b6a8-30e1-99ea-3de3c90675ce | -10.53184 | -44.51489 | 2025-10-04 05:04:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81946d07-7ada-38e3-b94f-edd9a6272894 | -8.84634 | -46.78288 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 250700f4-6a40-3a54-9659-c8901d374aac | -2.89854 | -50.7308 | 2025-10-04 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f17c8ab3-b4ba-3308-ae72-80c34857ec8d | -7.72881 | -49.85393 | 2025-10-04 05:04:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cedc3bd6-946f-3bf1-b858-b41b2aa6572a | -5.19503 | -45.07483 | 2025-10-04 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| a182dbb6-86d2-30d6-b6ad-56fe28b8d29b | -5.80048 | -43.60523 | 2025-10-04 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b89c23e3-0e49-34a0-9869-78d7e4db4010 | -6.18664 | -43.59161 | 2025-10-04 05:04:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 815f010f-70cf-3a72-87fd-2ea4debf5866 | -6.37191 | -43.90369 | 2025-10-04 05:04:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8f5be0e5-323c-30aa-aaa3-285304db902b | -5.21797 | -46.17383 | 2025-10-04 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1828f6cc-ee51-3f5c-aacf-c8da808ef740 | -10.01753 | -48.27339 | 2025-10-04 05:04:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbb45d99-c73c-307f-9a3c-ca90de25721d | -8.81719 | -44.82055 | 2025-10-04 05:04:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2fa45d2b-0f10-3c4a-8d71-bff920cc8ff7 | -3.9172 | -52.32993 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b44d77b1-8b82-3f1f-b214-065ed082b869 | -5.78455 | -45.78375 | 2025-10-04 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a8c448e-48dc-3aa3-bb05-94e4c6ac78c7 | -4.60871 | -43.14859 | 2025-10-04 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ff749bce-26fc-3004-967b-1f89167807bf | -8.22396 | -46.80423 | 2025-10-04 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 852558e2-8fc4-31df-8d20-d9e13e630e45 | -8.62899 | -54.97999 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc78a541-48f9-34ea-8227-b3fceef2f951 | -3.84665 | -41.58302 | 2025-10-04 05:04:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| da04a680-0a64-3bea-8c9c-919f485d6067 | -4.51111 | -50.80255 | 2025-10-04 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e248c48a-c0d1-3b5b-a019-e2f0d07baab1 | -9.90925 | -43.73487 | 2025-10-04 05:04:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 18b183ce-59ee-349d-898a-78e372d41789 | -8.01779 | -55.41828 | 2025-10-04 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8c40f57-a92f-32ac-82a9-801b3704593e | -8.90006 | -46.05311 | 2025-10-04 05:04:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 563c275d-4507-3e12-a43f-9acb59ef5d31 | -9.33212 | -54.52814 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 86edcc73-b969-37a2-b459-8f622a01e476 | -3.68548 | -49.0556 | 2025-10-04 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b312e68-9f30-3517-a910-61d15c1feeb2 | -10.04665 | -49.2038 | 2025-10-04 05:04:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7ee5b20f-9f5b-3f8f-853c-02463fd84f58 | -3.39389 | -50.27438 | 2025-10-04 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21e64c11-3537-3525-9247-f99ab8428bef | -8.0211 | -55.4188 | 2025-10-04 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 871ce719-a4b4-3dc9-9ce4-532cc633b37f | -4.27498 | -48.87856 | 2025-10-04 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad82c9d1-d9d9-39fc-a0b8-81eaaae73e2c | -6.17935 | -44.28889 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 70f1ab42-d018-3513-8306-9cf6e9dd95a5 | -9.34636 | -54.52647 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bfc89072-d7ee-3b36-9451-a420bfaae35f | -6.4481 | -44.80237 | 2025-10-04 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d15ffa1-b06e-3072-bc22-8de6b3546042 | -8.65952 | -54.71041 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5f88d6f9-c454-317d-b2bf-9664fb072b6e | -9.99663 | -48.27629 | 2025-10-04 05:04:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c8f631e-d814-3761-9c2c-d125f6608af0 | -7.48218 | -43.03263 | 2025-10-04 05:04:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 99cc631e-aa2b-32e0-a1fb-0664800a6476 | -3.84861 | -41.56952 | 2025-10-04 05:04:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 3152657b-280a-30f3-8940-a9808bbef183 | -9.33664 | -45.77563 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bb7878ab-32a9-3615-8074-dd1481caeb4a | -4.21426 | -51.12536 | 2025-10-04 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f46235e-d948-3951-8eb6-5992218418b8 | -6.65217 | -42.79638 | 2025-10-04 05:04:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 85ff5a44-73a8-3223-a95f-c7946f6cc86a | -3.47074 | -51.59017 | 2025-10-04 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb0b1a46-8aff-3af9-9aa9-715d50e3aa56 | -9.94219 | -50.23123 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0a437ba-9f19-33bb-9e5b-29380c54441c | -9.91981 | -50.49761 | 2025-10-04 05:04:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8483caf4-e61a-38da-a8c2-00742b345750 | -3.09372 | -48.49189 | 2025-10-04 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0b9069c-a009-3975-b0d3-13c189d4846d | -7.0427 | -42.7756 | 2025-10-04 05:04:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| e3e4c356-f40b-3cb2-a07a-4118a5b24624 | -4.32041 | -48.09076 | 2025-10-04 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec6bd397-1d64-36b3-a5a7-5583eb1b0af4 | -8.61439 | -54.96304 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21a9a3d6-0090-398d-aad6-dd9276d574a3 | -7.88 | -61.68094 | 2025-10-04 05:04:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a929cee-3c63-31ac-808a-dacd93e3b0ee | -7.77176 | -46.26563 | 2025-10-04 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6bef6fc-1967-3d09-914f-8abdce32f20d | -9.93439 | -50.89586 | 2025-10-04 05:04:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b03ec403-e353-3b49-9889-8b0c9842ec0b | -9.33896 | -54.52919 | 2025-10-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 38c5a950-1ad8-3d90-b302-6ff71690723d | -7.04812 | -42.79368 | 2025-10-04 05:04:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| eb1350da-90a7-3937-991a-8fad68859f01 | -9.93605 | -50.24181 | 2025-10-04 05:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 714cafa4-5145-3cc6-8708-ceb3291ddac0 | -7.75162 | -42.51999 | 2025-10-04 05:04:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 13fee155-b123-35fb-902f-0190ae9db9bf | -9.5156 | -54.70827 | 2025-10-04 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 142962bd-ddcc-3c21-873b-c338cfd1b345 | -9.34631 | -45.7946 | 2025-10-04 05:04:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| de696b41-a4d0-3e81-af2f-3ca6f3ddff5d | -8.82303 | -44.81223 | 2025-10-04 05:04:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f9faf347-ec94-33ab-9049-367775c96acd | -5.28254 | -47.5202 | 2025-10-04 05:04:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5327df1f-42ef-383e-b946-b71630bdf36d | -6.37764 | -43.89463 | 2025-10-04 05:04:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |


[Clique aqui para ver as próximas entradas](README102.md)
