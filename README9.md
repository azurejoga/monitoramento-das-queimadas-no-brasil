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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45877266-7602-3f72-8d0f-773279ada3ee | -17.34496 | -43.18713 | 2025-08-09 03:25:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b95cf504-e0e9-3f2f-9412-2e5f6708a19a | -19.8152 | -47.06913 | 2025-08-09 03:25:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 8ae0a920-f91f-3049-988d-bf6e5a13b0af | -16.31934 | -43.62228 | 2025-08-09 03:25:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0e2573d-b411-381f-8e34-1c7cfad10b16 | -20.57881 | -41.68929 | 2025-08-09 03:25:00 | NOAA-20 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| dcd19f37-26d3-3e9b-b60e-f4521ce21afe | -19.59819 | -42.6892 | 2025-08-09 03:25:00 | NOAA-20 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| f2c0e2f7-a1b3-3e73-a8ed-be720bacd614 | -19.07301 | -40.11671 | 2025-08-09 03:25:00 | NOAA-20 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fd9e4f25-d9b8-300f-9b69-565f058fef54 | -21.38393 | -44.127 | 2025-08-09 03:25:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 2c9791a7-8f99-3c33-b596-f417aa4fa3be | -20.4277 | -41.57458 | 2025-08-09 03:25:00 | NOAA-20 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 66e14b5e-c2af-3992-b905-9da84f37ad2f | -19.85607 | -41.43879 | 2025-08-09 03:25:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 6002fac6-cea8-3ac9-a878-7ce54b068d90 | -19.5937 | -42.6853 | 2025-08-09 03:25:00 | NOAA-20 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 6c9ccbc2-49d0-3fe2-8426-acd08d2077f5 | -19.80868 | -47.06745 | 2025-08-09 03:25:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 64e4c4d4-894f-3cd2-8ab6-8a65ff9574cb | -20.57417 | -41.68804 | 2025-08-09 03:25:00 | NOAA-20 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 40d4f3d1-4063-3ab5-9e38-fb4061f4c364 | -19.81993 | -45.01606 | 2025-08-09 03:25:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 237d4a90-fe0f-304c-a85d-cc7723cb85e8 | -21.38315 | -44.13055 | 2025-08-09 03:25:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| ab0036f1-ca61-3eb9-8ae8-f4e2f04527e5 | -19.59747 | -42.69267 | 2025-08-09 03:25:00 | NOAA-20 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 086b8aa6-0eb9-393d-8e51-e65f819fcf76 | -19.81645 | -47.0639 | 2025-08-09 03:25:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| b714e281-cc68-3d53-a54f-9510f7f3e7fc | -17.19694 | -42.82615 | 2025-08-09 03:25:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b320149-908a-3842-acbb-2287785b630f | -19.58862 | -42.68415 | 2025-08-09 03:25:00 | NOAA-20 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 45271271-15f8-3d16-afe3-1c78ea380f45 | -20.44763 | -41.52328 | 2025-08-09 03:25:00 | NOAA-20 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 18d82e8c-21c8-34d0-b8ac-d1124a11dd48 | -16.3197 | -43.62282 | 2025-08-09 03:25:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c79318c9-607f-3f28-8aba-c1c62ac5e8b5 | -16.32057 | -43.61876 | 2025-08-09 03:25:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c574502d-69fb-3ead-afd2-6ce8519bbeca | -19.85247 | -41.43245 | 2025-08-09 03:25:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 3bb4eaad-2a3a-3e06-ac27-70437603becc | -20.42952 | -41.5752 | 2025-08-09 03:25:00 | NOAA-20 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d52d96d1-832a-3a74-9c50-d460728aaf26 | -17.61578 | -46.71021 | 2025-08-09 03:25:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7def7e8-0bbb-3780-ac13-c2fe0e212b4a | -19.85714 | -41.43349 | 2025-08-09 03:25:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| dc03411f-230c-312e-b3c2-f46daec698d0 | -17.19166 | -42.82452 | 2025-08-09 03:25:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9743a071-e15b-3077-ad3a-a876ebed3311 | -15.63588 | -42.55229 | 2025-08-09 03:25:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 949eed9b-2189-369d-afc7-b1833641dd42 | -19.80737 | -47.07295 | 2025-08-09 03:25:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 34.5 |
| c212d6bd-2fd9-3385-bb96-856a3bee7962 | -19.4288 | -40.7321 | 2025-08-09 03:25:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 2f221bb1-f909-3b9b-83d6-b5e6b8429779 | -19.59304 | -42.68841 | 2025-08-09 03:25:00 | NOAA-20 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 2d7bce97-6f2c-38c2-86ad-aef9e15c688d | -19.42429 | -40.73119 | 2025-08-09 03:25:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 64adf182-96df-36d3-b675-f1e9dc541702 | -17.34577 | -43.1832 | 2025-08-09 03:25:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87d12a97-207a-3038-a36c-518a35a26c57 | -19.81 | -47.06194 | 2025-08-09 03:25:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 8b9a9576-4b4e-3ee2-a6a3-a4718dca15e6 | -20.57527 | -41.68266 | 2025-08-09 03:25:00 | NOAA-20 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 68b7e988-6cf7-388f-bb07-a65fad2fdd02 | -22.14396 | -49.44949 | 2025-08-09 03:28:00 | NOAA-20 | PRESIDENTE ALVES | SÃO PAULO | Brasil | 3541109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e30f0de9-d254-3ee9-91f0-9c26086bdcff | -22.14203 | -49.45692 | 2025-08-09 03:28:00 | NOAA-20 | PRESIDENTE ALVES | SÃO PAULO | Brasil | 3541109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c2597b86-99f2-3de8-93d5-5b88d842df2d | -8.9399 | -60.7481 | 2025-08-09 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| a9054c28-a988-38de-b468-331d1298fae5 | -8.9213 | -60.7489 | 2025-08-09 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| a3a06187-e030-3a8c-b95f-1af930da051c | -6.5856 | -44.564 | 2025-08-09 03:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| b3356609-5b66-3020-9195-12963e73f462 | -5.8895 | -57.7513 | 2025-08-09 03:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| ca99033a-5b01-3553-8dfb-a55191815b18 | -8.9213 | -60.7489 | 2025-08-09 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 992c2752-31c7-3b74-bc1b-8b982b1df051 | -8.9399 | -60.7481 | 2025-08-09 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.7 |
| e931fa73-984e-3b58-97e8-0e7b4b9eaba0 | -8.9213 | -60.7489 | 2025-08-09 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 7bba4e40-f3c5-36bd-986e-de347cb2282a | -6.5856 | -44.564 | 2025-08-09 03:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| fe4beb0b-9ed4-351a-8f2b-e448cced4416 | -8.9399 | -60.7481 | 2025-08-09 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 258ab69c-6352-3440-bba7-3071f8a5a689 | -8.9213 | -60.7489 | 2025-08-09 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 45d80394-bd94-3ffb-ba40-8c9c9cb4b109 | -19.8328 | -47.0586 | 2025-08-09 04:10:00 | GOES-19 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 55.3 |
| d037d41f-0bb6-3565-afbc-b8baa34c3c82 | -6.5856 | -44.564 | 2025-08-09 04:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 74c1ca42-b3e3-34a8-9ef1-2e5e1d627ab6 | -19.8124 | -47.0634 | 2025-08-09 04:10:00 | GOES-19 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 5b75062e-6b7e-34a7-9171-9045be566da8 | -7.25482 | -44.63092 | 2025-08-09 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20f544cd-f9a0-3484-9ce4-431e5391717d | -9.89076 | -43.56974 | 2025-08-09 04:14:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a40fdb57-aa5b-3616-9c9d-c3440681a1ee | -6.57516 | -42.80735 | 2025-08-09 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b37fa3c7-23f1-3f3b-b4b5-5ee857acdf02 | -5.2803 | -44.94979 | 2025-08-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3e926af-f6e1-34c6-bcd8-a97f03b355ca | -7.21216 | -41.84717 | 2025-08-09 04:14:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 57dbccc6-f21f-3dc3-85b1-c361a73cbda5 | -6.92838 | -44.69562 | 2025-08-09 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4f5c22e-3e6c-309c-9a30-e7d139163543 | -7.39623 | -39.68246 | 2025-08-09 04:14:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 62108a87-af02-33ce-9c77-bfffaf931e48 | -5.22634 | -43.19278 | 2025-08-09 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8390f45c-6292-3a02-8e77-134828e0027e | -7.42696 | -43.36423 | 2025-08-09 04:14:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f2e31c7-efb4-3b2c-8d93-781a79017c06 | -5.28441 | -41.10692 | 2025-08-09 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c65ab583-d4b0-34a2-a279-a4a60a2094d7 | -9.51897 | -45.41028 | 2025-08-09 04:14:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02eb6708-716a-316a-ae15-13a751210fff | -5.42019 | -41.22565 | 2025-08-09 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b5bb911e-877d-3bbb-bf9b-86e01f5bcd98 | -5.38726 | -41.3259 | 2025-08-09 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4f777d79-e333-30ec-93db-eb75fc71ecc5 | -5.21762 | -46.07229 | 2025-08-09 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cf479cb4-5ed5-3179-acfc-a0b76cbf4221 | -9.06198 | -45.07832 | 2025-08-09 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a5d1933a-f8cb-3e74-a4fb-8b97abe8604a | -3.47629 | -43.24571 | 2025-08-09 04:14:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aaafe92e-deee-36b5-9ae5-289abdd50200 | -5.73403 | -44.50227 | 2025-08-09 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b849358-46ba-36b8-8102-9a743e81e4c6 | -8.88745 | -44.78373 | 2025-08-09 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 163b562f-5e97-3245-8607-b98c4ea79c9a | -5.27377 | -44.94522 | 2025-08-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac502a8b-be3e-30c1-a06c-8a90f162622c | -9.05863 | -45.07776 | 2025-08-09 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 74af4e43-91ad-394e-8f24-1ed079d3da8f | -6.09984 | -42.18924 | 2025-08-09 04:14:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 22e42e05-563c-30ff-986b-026f2129d764 | -6.96044 | -44.4929 | 2025-08-09 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4cac39e5-72f3-375d-9289-b0575fb84017 | -4.29765 | -48.0736 | 2025-08-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0993458-adaf-3458-8b89-77a1a01ae3ac | -7.08215 | -44.51943 | 2025-08-09 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79a271df-daaf-3c1b-8ae1-32ca2f1ee434 | -4.11104 | -42.47068 | 2025-08-09 04:14:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9de00f04-61c0-3684-b6d4-a7bd5b6577b7 | -8.31762 | -45.00257 | 2025-08-09 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ce89005-7c0e-3e80-99e0-1746875d1027 | -6.08996 | -42.23106 | 2025-08-09 04:14:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 49010120-314a-37b8-bbd2-f59b666faf4e | -8.61143 | -39.59408 | 2025-08-09 04:14:00 | NOAA-21 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 865d9a03-0db9-3974-877c-73b385e0835b | -7.5945 | -44.90842 | 2025-08-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 441769f2-7715-3a76-92ec-9ffac45efb3b | -3.48764 | -42.84804 | 2025-08-09 04:14:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e36f6d54-373e-3272-9cbd-9e5d77141042 | -4.47889 | -48.11357 | 2025-08-09 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 131b9991-81bf-3940-bac8-abbbaea5769f | -4.14908 | -48.21586 | 2025-08-09 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a896770-415d-38b1-a963-468737a0cd0a | -4.4742 | -48.11658 | 2025-08-09 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 479ee5ac-2047-33e8-8acb-d2e11d3c1c3f | -9.20217 | -44.53533 | 2025-08-09 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dd49143-aa6f-374e-b2dc-d3606f704c72 | -7.04803 | -43.57003 | 2025-08-09 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27170463-e8db-3acd-92a0-6c651f848628 | -3.9891 | -47.89091 | 2025-08-09 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a81b461d-ab85-3ecf-8a09-9189fc53ac39 | -4.30116 | -48.07788 | 2025-08-09 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9f96da4-70d1-37b6-869e-ccd9e31b68ec | -6.13871 | -42.96941 | 2025-08-09 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3276a009-4d80-32fb-8dd1-773cc61e6e8a | -7.90081 | -45.55799 | 2025-08-09 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b87681a-2339-33a3-b8e0-e3083bbdf57c | -6.06906 | -44.893 | 2025-08-09 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f378bfa-6b41-3fcc-afdb-23f099f36367 | -6.66905 | -43.34003 | 2025-08-09 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 8.4 |
| a5f343ae-2063-383f-9254-27d737487f65 | -3.06968 | -40.81824 | 2025-08-09 04:14:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 5dd12b30-6e0a-3917-83d8-530e0597f2cb | -8.77514 | -46.42344 | 2025-08-09 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6984cd66-ea5f-3c50-be47-75f5ce526477 | -6.28913 | -44.98717 | 2025-08-09 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b686dd7c-1845-34f8-a7c1-7bdb352b8324 | -6.1321 | -42.96838 | 2025-08-09 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d402752a-ad34-38de-8d8a-145867fe55c2 | -7.21161 | -41.8508 | 2025-08-09 04:14:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 84a0d481-4434-32a0-bf04-7ea2ff32e3f6 | -5.48484 | -42.16587 | 2025-08-09 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 41b63bf5-66db-3da0-a34b-e1f6d105e2be | -6.4889 | -44.41807 | 2025-08-09 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9905925-1a7b-3848-9137-be4cd40aadbc | -6.06152 | -43.74317 | 2025-08-09 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 1c21f228-23f3-3d38-9cc4-15867e50fe25 | -3.82122 | -41.55967 | 2025-08-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 985e748f-9394-3a22-85e5-8d3639fc2bff | -7.64347 | -44.60206 | 2025-08-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README10.md)
