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

## Dados Diários - Página 205

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e49e1d22-6dd6-346f-8b78-015d0feda10c | -16.04943 | -40.65216 | 2026-10-07 16:37:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 1bc6eaf0-be3e-3c61-94e7-d55273d178ee | -4.05596 | -42.21476 | 2026-10-07 16:37:00 | NPP-375 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 21.0 |
| 2b309722-4e32-3bc3-8a36-8e1f52b222d5 | -7.34243 | -38.72728 | 2026-10-07 16:37:00 | NPP-375 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| c374225e-e664-387d-9efe-ffbc7137fd32 | -8.78318 | -47.5808 | 2026-10-07 16:37:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 0f84378f-d77d-3ed0-821b-e66a06b913ca | -4.26498 | -50.74447 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a8d195a7-53ae-38c7-a63c-768dd6c1fc59 | -6.88078 | -43.68565 | 2026-10-07 16:37:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 5394831c-0dad-39f8-8a59-c95bf7195e35 | -4.74087 | -49.75535 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2d5ba22f-f429-303e-ac1a-9b094a5f1865 | -4.08617 | -48.90462 | 2026-10-07 16:37:00 | NPP-375 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c0298393-53e6-36e7-8fd6-8bafd1028577 | -8.04607 | -45.61324 | 2026-10-07 16:37:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 753ac01b-8f1b-31e7-bd86-f3864aa77135 | -7.20428 | -55.10899 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 4d6b5c21-d98b-3f75-866c-801018247407 | -6.1749 | -52.93263 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 198dfc0b-d18b-36dd-9391-6ded040fa494 | -5.98427 | -53.56172 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c6d9eb6c-98b0-3c6c-9e5f-d7adcf79433a | -5.9698 | -49.30152 | 2026-10-07 16:37:00 | NPP-375 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| c52130c7-059c-3f01-b133-96d93c339d20 | -10.45761 | -46.83521 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 2a1030a8-b89b-320b-93d9-c61d5e1932c1 | -5.21591 | -37.37038 | 2026-10-07 16:37:00 | NPP-375 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 47.4 |
| 87dc2a61-51c4-3433-aa72-8514d97b4630 | -5.69794 | -53.48156 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 88ccf202-8341-30b3-8d0b-1d673fa1a8ca | -14.92945 | -41.09999 | 2026-10-07 16:37:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| b2fe2a22-bfe3-30b5-b965-00e182dd91cb | -7.88738 | -44.23093 | 2026-10-07 16:37:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e1ba0803-4230-34df-9499-3f079b3696c4 | -9.10036 | -45.10868 | 2026-10-07 16:37:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 8ed41ffd-b7d7-33c6-888c-9329263935cf | -7.87725 | -54.98005 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 4a27e415-1f5b-33cf-ba09-9c678db0a203 | -7.87846 | -54.98941 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| e600f485-9f39-3a89-b32b-f8b55b53fa7f | -3.80675 | -47.49498 | 2026-10-07 16:37:00 | NPP-375 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 21398f71-3537-3cb5-9e72-c7583bae40bc | -6.98295 | -45.12725 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 8af8f893-906a-312b-8395-59684e44da61 | -5.86447 | -45.19899 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b8a1854-53c2-387f-8c2c-9816948c9148 | -6.69014 | -44.9614 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0dbadcb2-3363-3b65-b493-f6babb11fc67 | -3.96768 | -48.1226 | 2026-10-07 16:37:00 | NPP-375 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 68fd5e78-e51b-34bc-a56f-83c63c875f18 | -8.25312 | -54.70963 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0130a6ab-98d6-3688-ac79-adf621e4646a | -3.77578 | -41.8737 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 25.0 |
| ebdc3a1d-9bfb-33a0-9750-426fe8affcb7 | -5.12688 | -42.78038 | 2026-10-07 16:37:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 04f6af7a-0d0a-3cca-b84f-0622e55ba3dd | -11.2312 | -46.24583 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 2c0d4a68-9ffb-3efe-b804-b61bc0fafe92 | -7.17127 | -47.79483 | 2026-10-07 16:37:00 | NPP-375 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 23088a51-ad7a-34bf-9c4e-4c45e01d950e | -3.62723 | -39.41154 | 2026-10-07 16:37:00 | NPP-375 | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| f66efe4b-8f70-3ce2-945a-b99d8a8eccd9 | -4.9785 | -50.57368 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8790a411-a4cc-3c9c-baed-865636fc2a00 | -9.79916 | -48.92193 | 2026-10-07 16:37:00 | NPP-375 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 47ab8578-3c0f-3e48-a9c1-b4050ca8de23 | -7.76746 | -54.94532 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 0500bd2b-7e5c-315b-9ba0-2f1b842b362c | -7.49615 | -44.43602 | 2026-10-07 16:37:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 410e19b1-07be-312b-8097-f3bb45f293e9 | -16.20424 | -42.25901 | 2026-10-07 16:37:00 | NPP-375 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8cdf06a6-ee16-3b6f-a38b-7fcacfb5581f | -5.81855 | -53.86375 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ce4b8de-b484-3081-b6db-e5f43ad2e3e8 | -9.91809 | -44.81902 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5be7b6e3-45ff-3d7c-8f21-7189cc8ca41f | -5.96195 | -40.92702 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 210.3 |
| 45e26b68-909c-32e4-afdc-7094958c1ab3 | -5.26577 | -47.89897 | 2026-10-07 16:37:00 | NPP-375 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 8cb8e479-2b2f-3a8d-ae4e-1c97decd2dfc | -10.18479 | -43.31622 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 7c0d7bb1-2c7f-3993-94c9-6c4ac5809b9d | -3.49318 | -39.50065 | 2026-10-07 16:37:00 | NPP-375 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 2bd006ae-6e37-302e-82ca-c71c32b783eb | -17.20035 | -43.53644 | 2026-10-07 16:37:00 | NPP-375 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bf7d0b34-be3f-3f27-b961-9d60f06cdf6c | -7.95626 | -38.31521 | 2026-10-07 16:37:00 | NPP-375 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 2fc2d912-2cc0-3bd0-ae58-a8dfb17df98f | -11.09725 | -45.67044 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7589d821-7740-364f-b3e6-e07e21702e64 | -10.13233 | -46.84612 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a13413ea-eac4-30ec-b2f0-43fd56857b87 | -5.73038 | -45.16165 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 464b036d-fdc3-3fef-b5e7-7844c90f036e | -10.88533 | -46.66609 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| dddcc89b-b968-37e0-97b7-4488c1838af1 | -7.77385 | -43.82066 | 2026-10-07 16:37:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| b3ae7148-a902-3bf9-a9a4-fcb65f5076bf | -6.32354 | -55.32084 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 6ab5f327-11de-3afa-9a30-c953d2470b12 | -11.07447 | -45.63734 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| e2969abc-4ddb-3741-94a1-faef6c67daad | -5.97326 | -40.95115 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 44.1 |
| e5375e0c-b7c6-38b6-a84a-b825c03ff62b | -5.71228 | -41.67249 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 4f7f8ac2-28d9-3f8e-a8ac-037a76c83076 | -5.23821 | -48.39773 | 2026-10-07 16:37:00 | NPP-375 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 7ebb17d0-a175-3f95-bb29-def9e0cc3cb1 | -8.11286 | -50.92552 | 2026-10-07 16:37:00 | NPP-375 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 59a063b2-21b2-32ac-85cf-fdf08a9dd9de | -6.40705 | -52.72071 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c19906c7-3cbb-37f1-9ac5-252519316ad0 | -6.19776 | -51.4354 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8b519794-ce79-34ac-a4dc-f8dc409c0ce4 | -6.15285 | -51.73477 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f3eeedf1-e550-331c-a9bb-348328652894 | -7.30593 | -37.54161 | 2026-10-07 16:37:00 | NPP-375 | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ff90d983-33d1-315a-ac09-f2e3d1d84afa | -5.35668 | -45.68903 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1da25af2-a302-3205-b504-19f380edc6f9 | -9.14594 | -45.83152 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b032bbeb-9c85-31f2-94d3-23c07af8ff45 | -4.75651 | -42.59798 | 2026-10-07 16:37:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| ad3af835-3d47-3716-a87b-65b7d61938a3 | -4.62574 | -44.25779 | 2026-10-07 16:37:00 | NPP-375 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f890aa97-3e32-3176-acb4-8ddac68fe4d9 | -6.84221 | -39.5574 | 2026-10-07 16:37:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 7e9165b9-ebc7-333d-8edf-0ba1a1e37fd9 | -5.76098 | -42.0447 | 2026-10-07 16:37:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 79868422-34f1-3ba5-af19-3e97d5ba1c4f | -6.93836 | -45.26542 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b83919f6-292a-38e8-87d6-d5396656be66 | -6.07581 | -44.38608 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f32b4332-946a-3f6c-bcca-90ac9a02e989 | -3.77215 | -41.79189 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 32.1 |
| 618ebebc-b8c3-39e6-9c68-36016b254710 | -10.97228 | -45.40149 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 95f7560c-cb92-39e1-ad92-531cb24bbc29 | -4.97747 | -37.62145 | 2026-10-07 16:37:00 | NPP-375 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 32bdca79-5cdd-37b0-aacb-86869abfc181 | -6.47755 | -52.80826 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| cef8e5f4-8222-3df0-a113-2af3504c95a7 | -15.52464 | -41.245 | 2026-10-07 16:37:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| c4d0167c-1a60-3b5f-9cd9-a089cc2947f6 | -10.5254 | -47.28067 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 39558dba-e5e4-3704-b124-09a440371808 | -6.3436 | -43.11235 | 2026-10-07 16:37:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c91330bd-2daf-3cf8-9a55-bb1578690514 | -5.38057 | -45.91861 | 2026-10-07 16:37:00 | NPP-375 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e0f58363-4aee-33e0-a7e7-62a66112aa28 | -8.94459 | -37.61652 | 2026-10-07 16:37:00 | NPP-375 | MANARI | PERNAMBUCO | Brasil | 2609154 | 26 | 33 | nan | nan | nan | Caatinga | 8.2 |
| a2cc8141-ca43-3998-9526-eec7173eb76f | -6.43598 | -38.14065 | 2026-10-07 16:37:00 | NPP-375 | TENENTE ANANIAS | RIO GRANDE DO NORTE | Brasil | 2414100 | 24 | 33 | nan | nan | nan | Caatinga | 6.8 |
| a34fe445-a3b0-357f-886a-3a39657930a6 | -6.9206 | -41.23681 | 2026-10-07 16:37:00 | NPP-375 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 8fca9030-1a42-3c3d-82e6-930be5823b58 | -15.33488 | -42.76333 | 2026-10-07 16:37:00 | NPP-375 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2a1766f5-1f4b-3324-b32e-faa7b4c92639 | -5.68755 | -53.48601 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| ba09693c-dc51-3c52-9c95-d23b36a15d83 | -11.14171 | -46.16616 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6a045a85-bc27-372a-8dd8-50c7040025ef | -9.97008 | -43.50215 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 85424c53-2f68-308c-8801-12bb9538225c | -5.95236 | -46.35996 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 684fbdaf-33dc-3426-a7db-76d582ea8948 | -9.93724 | -45.72886 | 2026-10-07 16:37:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 5acd4d8f-f619-34ef-bb5b-37c52f055602 | -6.21502 | -52.8366 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| dcf2a55d-188a-3131-9a7d-7fbaf7654114 | -10.51707 | -47.27693 | 2026-10-07 16:37:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| bc8a6d4d-6c68-3dfb-a5bb-42e95bda50e7 | -7.86862 | -44.21946 | 2026-10-07 16:37:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 73c98f1f-53ba-3f89-9c05-de828b3525c3 | -17.24436 | -47.47805 | 2026-10-07 16:37:00 | NPP-375 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f62a61e0-53be-355f-921e-4e8ff76b9051 | -6.44035 | -45.2038 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 55805bd5-4c6d-3ca0-bd4f-146b92202b85 | -6.42484 | -54.96915 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 30638137-889a-35f5-a844-a524e2dab560 | -3.88269 | -44.10662 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b24a5a97-e9f4-3a40-aa6c-108a8c6461e1 | -11.00009 | -45.42097 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| c52bbc79-ab8a-3ad7-a010-2e694162497b | -10.77816 | -46.53685 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 3d34d324-67a4-35e8-8e7d-f6886fc190a5 | -17.01616 | -45.91156 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| ab9a92b7-c6dc-30d2-9fea-1347b353251d | -7.53056 | -50.76057 | 2026-10-07 16:37:00 | NPP-375 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5620dcfb-c382-371d-aecb-c1c6ac8b2e9d | -16.01687 | -41.82589 | 2026-10-07 16:37:00 | NPP-375 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 7456efd3-3367-304e-ab3a-c28b89f298cb | -4.45523 | -47.9238 | 2026-10-07 16:37:00 | NPP-375 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 2d1542b4-2319-366a-857d-d9a79931963e | -5.15455 | -43.07603 | 2026-10-07 16:37:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ea6f7b9c-baa7-343c-a6b1-98fd3818ffe8 | -4.8237 | -40.0226 | 2026-10-07 16:37:00 | NPP-375 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |


[Clique aqui para ver as próximas entradas](README206.md)
