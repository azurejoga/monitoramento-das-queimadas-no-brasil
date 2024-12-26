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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38aae774-7920-3cfd-bd7e-0928d6d50022 | -4.45985 | -46.68171 | 2024-12-26 03:36:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 35776b4b-22b1-3f37-9cfa-0a5002d5830b | -5.94809 | -44.43965 | 2024-12-26 03:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c0d212d9-74bb-3895-9f4e-703293bd5b0e | -3.9897 | -43.25394 | 2024-12-26 03:36:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d740686-6de2-3952-b0a8-a79dc9f00580 | -6.31252 | -39.71151 | 2024-12-26 03:36:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fc81a501-148d-392a-89af-839fefdb02ce | -4.46103 | -46.67502 | 2024-12-26 03:36:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8dcb5ec0-45a1-3a1c-8895-920e66e57f86 | -7.4762 | -34.84195 | 2024-12-26 03:36:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1c22acac-695b-32bd-b212-6fd992e7588e | -7.91687 | -35.22287 | 2024-12-26 03:36:00 | NPP-375D | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 9b6980e5-4977-3393-927b-cca94308548d | -5.94212 | -44.44672 | 2024-12-26 03:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| bfb4bae8-4fb5-3d93-a0be-f6ceced16a24 | -4.46806 | -46.67598 | 2024-12-26 03:36:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e1ffd62a-df30-3d02-abcb-c93134932e5b | -5.93698 | -44.44113 | 2024-12-26 03:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49301516-6787-38ca-9ec1-987774b58942 | -7.81561 | -35.22086 | 2024-12-26 03:36:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 4d909948-6cdd-3480-b324-6b3febda422e | -7.76594 | -34.94985 | 2024-12-26 03:36:00 | NPP-375D | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 8e3efd10-f0e1-381f-8455-d349f470328a | -12.02504 | -42.99735 | 2024-12-26 03:38:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bd6390d8-18d5-30a3-9b29-fb7bee2f4bcd | -12.024 | -43.00283 | 2024-12-26 03:38:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| b53e96d1-96a4-38fa-92e5-f164ed744af7 | -15.42467 | -39.47793 | 2024-12-26 03:38:00 | NPP-375D | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e7b88f15-4be7-3baa-a22c-02b3cb1d95fd | -12.02265 | -43.00197 | 2024-12-26 03:38:00 | NPP-375D | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| fe421b19-511c-3b9a-823a-a659d0899929 | -9.9864 | -44.75363 | 2024-12-26 03:38:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 25d055e4-83b4-30b3-8b98-1638334a3ee0 | -9.98074 | -44.75241 | 2024-12-26 03:38:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 11ebf9de-8fc7-3733-8396-baa4e814f3bd | -12.76348 | -38.47884 | 2024-12-26 03:38:00 | NPP-375D | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| bdadc13c-e3a8-3faf-aed0-b844fb6b90e5 | -10.14195 | -42.167 | 2024-12-26 03:38:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e5392fab-01b1-3d99-a90b-ad33dda74198 | -22.84096 | -42.15097 | 2024-12-26 03:40:00 | NPP-375D | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 82a7341d-c39a-348d-b6f4-f831198f1443 | -7.11679 | -41.86662 | 2024-12-26 03:57:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 816912a6-4054-334b-8d8b-bf1ef7cd0e65 | -4.79304 | -37.79403 | 2024-12-26 03:57:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f40fa260-c243-3253-bf7f-9c9d97abdd23 | -6.17604 | -39.28529 | 2024-12-26 03:57:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5c00e7b5-6086-35ec-a4a4-3267bb1c8df1 | -5.21485 | -44.90806 | 2024-12-26 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 36d06802-0a6f-3017-b27d-15706bda6b68 | -4.45867 | -46.68864 | 2024-12-26 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f98c854b-342a-3c54-a444-7935420f66b8 | -3.99312 | -43.25218 | 2024-12-26 03:57:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 68e38cc2-cd19-3725-b9f2-51d977add58b | -6.17273 | -39.28477 | 2024-12-26 03:57:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 802ffc2d-1d56-3e3a-ab52-08544f86d99f | -3.98861 | -43.25615 | 2024-12-26 03:57:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1a5419dd-45d1-309e-9a0e-f084c1c30b2d | -5.98799 | -45.39225 | 2024-12-26 03:57:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94d2b2c7-867f-3ca8-ae7a-4b2d5c55fb43 | -3.52124 | -42.65056 | 2024-12-26 03:57:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 376c0c7d-6ecd-31d6-9fed-66ef32966cbe | -4.62387 | -39.61068 | 2024-12-26 03:57:00 | NOAA-20 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c2aaacf0-929e-39b3-b0a5-fe4f7696d65c | -4.32705 | -43.51312 | 2024-12-26 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3ce25c9c-5478-350b-926d-6186bb3d4920 | -6.17327 | -39.2813 | 2024-12-26 03:57:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d31d7851-b5bb-32d0-bb5c-96c20c6f58c2 | -5.52625 | -38.9234 | 2024-12-26 03:57:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0ae9a3ce-e65e-3c7f-bdc3-2edad1c65d1b | -7.81241 | -35.22203 | 2024-12-26 03:57:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f5a9aae2-c302-3e97-b035-3e4beec4dcab | -5.22751 | -41.24899 | 2024-12-26 03:57:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| caeea614-58f4-3343-bd5e-16b95e997e19 | -7.76418 | -34.94791 | 2024-12-26 03:57:00 | NOAA-20 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3fe8c618-86ac-3fae-8ea3-af0f66134393 | -7.01829 | -35.02275 | 2024-12-26 03:57:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2ad2c548-bcab-3b3b-87d1-1ad294b7f4dc | -7.82951 | -35.18845 | 2024-12-26 03:57:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c47ffaf9-e184-305a-b38b-a2f279808dcd | -2.85155 | -41.77715 | 2024-12-26 03:57:00 | NOAA-20 | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 699fe96c-b48b-3b5f-800f-c321619710b7 | -6.59439 | -35.1588 | 2024-12-26 03:57:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dad04a96-083f-3cec-b11b-2f4ab7a69cb6 | -7.01778 | -35.02625 | 2024-12-26 03:57:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 89ce12b5-6d82-301f-adef-84df3c71319f | -8.50985 | -35.04559 | 2024-12-26 03:57:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3e0dd523-478f-306b-9800-c60834870379 | -4.3163 | -44.56726 | 2024-12-26 03:57:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f542d0a0-dc2b-37b9-b6a0-5f5c69513227 | -4.05353 | -38.28955 | 2024-12-26 03:57:00 | NOAA-20 | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6ae70ae0-b478-3c91-98f7-93f078150236 | -7.76009 | -34.94734 | 2024-12-26 03:57:00 | NOAA-20 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 7ec74b85-62ad-37b7-8689-6c2541892d42 | -7.90962 | -35.20999 | 2024-12-26 03:57:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| db4b6f4d-a775-3cfd-a32f-14da9901e2c9 | -4.45585 | -46.68961 | 2024-12-26 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e3eb362-83ff-38c1-965b-e8248087c4f7 | -5.5476 | -42.90668 | 2024-12-26 03:57:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e44f3b81-86d5-3d7c-b3b1-5ee1737ce3b3 | -7.81592 | -35.22611 | 2024-12-26 03:57:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| a326c373-9c1f-32b4-8588-fe2b16b04886 | -4.58603 | -43.63473 | 2024-12-26 03:57:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 22849690-9334-37e9-a4da-c85756c83179 | -7.81692 | -35.21912 | 2024-12-26 03:57:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 950f5d1d-3e2f-3aad-8cb9-874a202de3b0 | -4.62718 | -39.6112 | 2024-12-26 03:57:00 | NOAA-20 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bdc9dc04-2790-3617-ad7d-974f9c8c66f5 | -5.69477 | -44.80841 | 2024-12-26 03:57:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bebfe18-80dc-370f-be0b-7f1aeef0dd1a | -4.4567 | -46.68468 | 2024-12-26 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 06a18d0d-ebc3-347d-90f2-9fada6b53c9a | -6.30917 | -39.714 | 2024-12-26 03:57:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4c49d4fb-623a-3a9a-a79a-2485f01e7909 | -7.05506 | -38.74407 | 2024-12-26 03:57:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a5147dd4-cc34-38b1-a552-deba17bfa184 | -6.81344 | -38.96106 | 2024-12-26 03:57:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4713f4b1-7ba3-3937-b588-16c73f161181 | -5.27259 | -39.80506 | 2024-12-26 03:57:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 903ad0fc-4160-399e-b5ce-5d2af92fa0fa | -1.55116 | -45.8224 | 2024-12-26 03:57:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1374c8e6-f7b7-3108-9612-061fe546307f | -7.01426 | -35.02224 | 2024-12-26 03:57:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 389f7ab0-20d1-30a2-81a6-54693543a2a7 | -5.52958 | -38.92392 | 2024-12-26 03:57:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c6b72740-07c0-30ca-a5e7-8599e19e235a | -5.21548 | -44.90434 | 2024-12-26 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c0dbc472-064f-3462-859b-8376be2314af | -5.47477 | -39.664 | 2024-12-26 03:57:00 | NOAA-20 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 249d12cd-46fe-3373-a3a0-e2b054b9a19f | -3.40623 | -39.16921 | 2024-12-26 03:57:00 | NOAA-20 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dcd2a986-6edc-37e6-927f-9d8ed9d5cc68 | -3.44844 | -46.30913 | 2024-12-26 03:57:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bd6c306-40fb-37bb-ab87-5293c6c62609 | -5.94325 | -44.44868 | 2024-12-26 03:57:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b55627c-3f26-3676-b3b0-b23429c67fdd | -5.47754 | -39.66796 | 2024-12-26 03:57:00 | NOAA-20 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f494674b-9c83-3dcb-8df1-18f434449171 | -7.81642 | -35.22263 | 2024-12-26 03:57:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| b52907f3-0db7-342c-828b-83f0dea85005 | -5.93932 | -44.44801 | 2024-12-26 03:57:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 175c7d95-ffd2-35a3-bb28-d533cde28649 | -5.94017 | -44.44294 | 2024-12-26 03:57:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de458694-c926-31de-b915-83b140935039 | -4.58761 | -37.80759 | 2024-12-26 03:57:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e9a3c34e-a626-3ffc-9580-4f04687327fc | -4.45395 | -46.68806 | 2024-12-26 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 155ae015-71e6-329c-8018-74eb865fe1b0 | -5.22577 | -41.25994 | 2024-12-26 03:57:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 508f6799-a3a8-3df2-8674-8d41a5dd1f9a | -3.80241 | -39.09017 | 2024-12-26 03:57:00 | NOAA-20 | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2471d38e-7a62-38a6-9a71-003d5235457d | -5.98704 | -45.39241 | 2024-12-26 03:57:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| febed5f6-d350-318a-b562-79cdf64c3c72 | -4.4614 | -46.68538 | 2024-12-26 03:57:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10073631-eddf-333a-9446-f5a4d3d7cdf4 | -6.4656 | -41.61966 | 2024-12-26 03:57:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6df9b34f-cf5d-37ee-b618-a6adbdb45cc2 | -5.93624 | -44.44226 | 2024-12-26 03:57:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20710122-040f-31e7-8585-25bf694f0817 | -7.15202 | -35.07061 | 2024-12-26 03:57:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d6e1e6e6-e1a4-315f-8a1a-6971dfa2fd9e | -3.34442 | -41.7981 | 2024-12-26 03:57:00 | NOAA-20 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dcda1a36-f6f6-31ec-a5fb-52b44fe7b679 | -5.22974 | -41.25685 | 2024-12-26 03:57:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 914c07bc-e1ed-362d-9749-6c2bcbf56730 | -3.94254 | -38.54133 | 2024-12-26 03:57:00 | NOAA-20 | ITAITINGA | CEARÁ | Brasil | 2306256 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8fb8d2d7-e4ee-35f0-93ab-3deeee207bb8 | -3.06518 | -40.07996 | 2024-12-26 03:57:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 99b27752-a6fe-32e1-b8df-f9feceef00cb | -4.3176 | -40.55827 | 2024-12-26 03:57:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2c4eece8-7545-3e12-8b43-69aa80b832b3 | -7.91243 | -35.2115 | 2024-12-26 03:57:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| dd3e4aeb-135f-3c77-9d10-86a3627565db | -5.23032 | -41.2532 | 2024-12-26 03:57:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 83c887b6-fbbc-3e59-a0a7-5f01985d9bc7 | -5.9441 | -44.44362 | 2024-12-26 03:57:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b6afaebc-f97a-37cc-8387-e8be69388cad | -5.99217 | -45.393 | 2024-12-26 03:57:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38bd034f-cff7-32ac-acf4-e23a4c537dd1 | -8.51395 | -35.04618 | 2024-12-26 03:57:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 27c029fb-8390-3311-8241-b47cc3437c07 | -3.99237 | -43.25675 | 2024-12-26 03:57:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1a4d9bb1-4d42-3007-a74f-73b74e763c66 | -5.47423 | -39.66745 | 2024-12-26 03:57:00 | NOAA-20 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9bb8cd99-5adf-355f-913c-7c309c5ff769 | -7.15603 | -35.07126 | 2024-12-26 03:57:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d444ee48-7f7f-34c0-a283-3f7e23b1d38d | -3.45015 | -46.30796 | 2024-12-26 03:57:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 311f0192-75f7-3b22-9076-c650961b9424 | -1.54653 | -45.82161 | 2024-12-26 03:57:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d6284d91-fbd3-3a3f-87f5-99e6a9d424f1 | -6.20196 | -41.05492 | 2024-12-26 03:57:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b054f5af-fc09-3af0-9847-75ff3098d4ec | -13.74666 | -39.36855 | 2024-12-26 03:59:00 | NOAA-20 | PIRAÍ DO NORTE | BAHIA | Brasil | 2924678 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6e488f43-2ee2-3224-811b-57ed6625846e | -12.02164 | -43.00223 | 2024-12-26 03:59:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7f9dbb12-fbcc-3b2a-8e5f-7c2ec288d811 | -11.43218 | -37.99701 | 2024-12-26 03:59:00 | NOAA-20 | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |


[Clique aqui para ver as próximas entradas](README4.md)
