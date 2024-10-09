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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8296aad8-6bb1-303c-b62b-c8cce4ddb4f4 | -18.41624 | -42.62653 | 2024-10-09 03:25:00 | NOAA-20 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3cd0fd12-56f9-35fe-acee-d9f25cc4a8db | -18.41237 | -42.61877 | 2024-10-09 03:25:00 | NOAA-20 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 77b13510-4272-32ad-a9db-170ce4723069 | -18.41169 | -42.6221 | 2024-10-09 03:25:00 | NOAA-20 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f11605e2-1aba-38c8-a51f-98d2de81af96 | -18.411 | -42.62543 | 2024-10-09 03:25:00 | NOAA-20 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 732ff263-fa41-3c0d-8610-a34c8df08577 | -18.24348 | -42.96261 | 2024-10-09 03:25:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8029ed16-3c79-34d7-89a3-5faeba31f2ed | -18.24193 | -42.95492 | 2024-10-09 03:25:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a0fa53f7-0890-3b80-8a21-2f18024e6bec | -18.24112 | -42.95869 | 2024-10-09 03:25:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fa7671e9-89c5-3758-ad98-1fc6f74b2d35 | -18.24032 | -42.96242 | 2024-10-09 03:25:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c365962d-71f9-39b8-9f1c-52c766646525 | -17.93146 | -44.56767 | 2024-10-09 03:25:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dca6677f-6af0-32df-8fe2-b2e4e0ef1b0d | -17.92554 | -44.56623 | 2024-10-09 03:25:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e76675d2-b219-30d2-9228-5bb20c3c4db6 | -20.16123 | -44.40796 | 2024-10-09 03:25:00 | NOAA-20 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 456516e6-b16e-3857-9675-962d661e1567 | -20.16029 | -44.41215 | 2024-10-09 03:25:00 | NOAA-20 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 30e12b1d-36ec-36fa-a47e-29d19622bafa | -20.14954 | -43.83592 | 2024-10-09 03:25:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6f22aaf6-fcca-32f5-9a8c-df3861966cbb | -20.1487 | -43.83973 | 2024-10-09 03:25:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7ecbb88b-53d2-30eb-a311-3a3fabb94e63 | -20.14783 | -43.84366 | 2024-10-09 03:25:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| db3b46d5-87cb-3adf-b9bf-85d689c5599d | -20.14418 | -43.83427 | 2024-10-09 03:25:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 73e01361-67ba-38a0-ad7d-d8da239ca207 | -20.11309 | -43.47953 | 2024-10-09 03:25:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 45edd6d2-f04e-3368-8fc1-59a177700b0d | -20.11232 | -43.48305 | 2024-10-09 03:25:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 609440d7-fcb1-31d7-bbb3-41dfcf417e75 | -20.10976 | -43.4819 | 2024-10-09 03:25:00 | NOAA-20 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4f97c508-e905-3efb-9ed6-719a69032769 | -20.05124 | -46.37695 | 2024-10-09 03:25:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cfa44c6b-fe49-3ebc-ab7a-0044deaefb6c | -20.05 | -46.38225 | 2024-10-09 03:25:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 330b4cd0-15d7-3c25-b0e3-99c64ed3b72b | -20.0449 | -46.37548 | 2024-10-09 03:25:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1ce879b8-44ac-3e4b-89f3-b217417e878e | -20.04366 | -46.38076 | 2024-10-09 03:25:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0e3715db-a5b2-31db-bdc0-c1db3e227b12 | -20.01785 | -46.69239 | 2024-10-09 03:25:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2adc65b5-6856-3933-97da-7ff8fcea5a3a | -20.01645 | -46.69821 | 2024-10-09 03:25:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87008d2d-360c-38ee-8652-7f0aed896727 | -20.00837 | -42.44396 | 2024-10-09 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| beb74017-3479-3d04-9c06-4adce1fbdb9f | -20.00768 | -42.44725 | 2024-10-09 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 5a9d44c1-e2c7-30e1-b164-cde2cdff76cb | -20.00702 | -42.45034 | 2024-10-09 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 9a1e6f0f-1d77-387a-84d2-4192e56c8f2b | -20.00418 | -42.43897 | 2024-10-09 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 99bbee0a-e77d-3fe6-8c1e-cfe6ec22dd69 | -20.00343 | -42.44254 | 2024-10-09 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ad6ba5ce-a4a8-31c4-887a-a9d4a3da9ebc | -20.00268 | -42.44604 | 2024-10-09 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9786941a-bfca-3837-8eab-9cbde329c09d | -20.00016 | -42.4391 | 2024-10-09 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| cf042fec-cd79-34d7-8186-a1235036313f | -19.99942 | -42.44272 | 2024-10-09 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| dc972a51-1f18-31c2-9cf7-a1508af75e18 | -19.99919 | -42.43778 | 2024-10-09 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 41883f3d-7314-3641-b735-b6d4997895cc | -19.99871 | -42.44618 | 2024-10-09 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6ef99e1b-cf47-3b3d-afc4-e442e0eb023f | -19.99845 | -42.44125 | 2024-10-09 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5d6500b2-b864-3979-802d-c0b8b124f485 | -19.99769 | -42.44483 | 2024-10-09 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9cd46864-9d92-35a7-bd41-441caee68042 | -19.99516 | -42.4379 | 2024-10-09 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 17ee4cd8-10c1-3387-9ac2-426459a55603 | -19.99446 | -42.44132 | 2024-10-09 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5a8dc89a-1db2-38a2-bae4-ac2b4b65f099 | -19.99419 | -42.43659 | 2024-10-09 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ad0872af-e798-38be-ad9e-0d6933893b76 | -19.9935 | -42.43985 | 2024-10-09 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 88340a4c-cb81-35b5-9404-8ccd18e7f4d7 | -19.9902 | -42.4365 | 2024-10-09 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 434ead5b-492f-3392-ab31-dd9ce20a8f60 | -19.98922 | -42.43526 | 2024-10-09 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b97647f6-5d61-3339-9b80-602d1840e3fd | -19.98857 | -42.43833 | 2024-10-09 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 56237b08-ca09-3888-902b-aa582bcdaea7 | -19.97459 | -42.43588 | 2024-10-09 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 411ac5a7-a7d4-3c94-a02e-28c5c82b9780 | -19.97389 | -42.43929 | 2024-10-09 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 71a9927f-8fc5-361a-a929-aeb74979348b | -19.97319 | -42.44269 | 2024-10-09 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| aef5830f-9f59-39a3-b1c7-9c417d61e350 | -19.97251 | -42.446 | 2024-10-09 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 9e6733fb-6302-306c-9bc2-ca927951e24c | -19.8903 | -42.63725 | 2024-10-09 03:25:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cb58a8e2-bd8e-3342-b0d6-85adcb98f930 | -19.88964 | -42.64038 | 2024-10-09 03:25:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| db2caf16-80ae-3e4a-8edf-9f6f5811aad4 | -19.82998 | -43.80188 | 2024-10-09 03:25:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| cec058e6-908f-33a0-8124-502a9ca68b84 | -19.82904 | -43.80617 | 2024-10-09 03:25:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2dbaf93-9d6b-3243-a093-202fba6103bd | -19.8287 | -42.38553 | 2024-10-09 03:25:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 81d48543-940e-3237-916c-a63417ebc979 | -19.82792 | -42.38924 | 2024-10-09 03:25:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4a75a345-a88e-3d6c-90d6-0504b37cf26b | -19.82655 | -42.07021 | 2024-10-09 03:25:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 4d2a447f-6926-3c62-8695-d9c34c38e679 | -19.8252 | -42.07681 | 2024-10-09 03:25:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| bbca784b-db0b-3ed1-83e1-e2cd97fac21f | -19.82376 | -42.38406 | 2024-10-09 03:25:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d070d58d-88b7-31ef-8a68-be39641639b6 | -19.80413 | -45.62044 | 2024-10-09 03:25:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| edde6af2-e7b2-3fa9-acaf-2a61014b8c1a | -19.80309 | -42.40743 | 2024-10-09 03:25:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 717639bc-538b-367f-85b9-2574da60c5f7 | -19.80302 | -45.62531 | 2024-10-09 03:25:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 401a5654-a564-3bfa-8177-8f358ca65e84 | -19.80189 | -45.63026 | 2024-10-09 03:25:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 25c43164-f332-3889-be22-c4cf2af8d386 | -19.79693 | -45.62387 | 2024-10-09 03:25:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2790902f-cb75-32f4-b72a-119b16a494d8 | -19.7958 | -45.6288 | 2024-10-09 03:25:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c2a2284e-0ccd-3b21-9cc2-4b40e5fb77c3 | -19.77175 | -42.33707 | 2024-10-09 03:25:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 1cec94a7-8b6f-3d8f-b2cb-249ea6ac2dfe | -19.77116 | -42.33996 | 2024-10-09 03:25:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 825a366b-8b79-35c6-9b09-8e1277b4a309 | -19.7702 | -42.84255 | 2024-10-09 03:25:00 | NOAA-20 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c438ad42-5c23-3b55-a421-21ece56ce360 | -20.79151 | -47.21418 | 2024-10-09 03:25:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e8ade42-6528-3a6f-a41b-805f2ea2195e | -20.79076 | -47.21019 | 2024-10-09 03:25:00 | NOAA-20 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ba29d82-d2b8-3753-9829-b489f5a8b3c8 | -20.79018 | -47.24103 | 2024-10-09 03:25:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 97dec4d1-3612-31fb-ac8f-4dd4a7c3ad22 | -20.78931 | -47.21615 | 2024-10-09 03:25:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e28e555-5117-3a3c-b6cb-7880ec9776b2 | -20.78908 | -47.25372 | 2024-10-09 03:25:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 276f803f-ee13-3c1b-b036-5bf3e72c91b8 | -20.78723 | -47.2616 | 2024-10-09 03:25:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8e3fb5e-9e10-39e2-99a1-10b28aa55457 | -20.78655 | -47.25596 | 2024-10-09 03:25:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17fed478-3f2e-3c13-991b-2a42cfd41cf1 | -20.78568 | -47.23885 | 2024-10-09 03:25:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4215f2d7-6555-3bd2-82fd-8d64dca8c59d | -20.78423 | -47.24498 | 2024-10-09 03:25:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85a566ec-82fd-37c6-a32f-0c8c6a5b58f6 | -20.78318 | -47.22021 | 2024-10-09 03:25:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cf5a0b19-efb7-3505-8e67-3081e1d400f1 | -20.78245 | -47.25253 | 2024-10-09 03:25:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e29f207-36c7-3881-b6b6-1bb42c0d8f19 | -20.78159 | -47.24788 | 2024-10-09 03:25:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d48db514-c2fe-39c1-9fd8-4ebe04e73901 | -20.78084 | -47.22254 | 2024-10-09 03:25:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eb007209-75bd-33ae-8b6b-7703b8cdea51 | -20.78078 | -47.25959 | 2024-10-09 03:25:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ee5d568-73bb-31b3-97ff-7dbc04a8f639 | -20.77988 | -47.25489 | 2024-10-09 03:25:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 708635ae-f800-3f85-a533-bbd9e062db1f | -20.76631 | -48.57654 | 2024-10-09 03:25:00 | NOAA-20 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bc2b97a3-1232-3556-b8c1-8aeb58845c5c | -20.76451 | -48.58382 | 2024-10-09 03:25:00 | NOAA-20 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b8129268-a376-3d69-bb61-0ebb5623ac46 | -20.76255 | -48.57801 | 2024-10-09 03:25:00 | NOAA-20 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 51e22011-d2ac-3bf4-9fd2-ab5ba116a1ca | -20.72287 | -43.81297 | 2024-10-09 03:25:00 | NOAA-20 | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b698579e-90d6-3292-b725-3cf2af9424db | -20.7175 | -43.81171 | 2024-10-09 03:25:00 | NOAA-20 | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 55945377-7d92-361d-9fe9-e9608597aaa8 | -20.6869 | -45.00644 | 2024-10-09 03:25:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | MINAS GERAIS | Brasil | 3161205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 72a1d3b1-f135-3fd8-bf04-c344cc805c68 | -20.68175 | -42.33323 | 2024-10-09 03:25:00 | NOAA-20 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 79c0d78a-7af0-380a-88ff-aa3644077ef0 | -20.68094 | -42.33218 | 2024-10-09 03:25:00 | NOAA-20 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0fd36828-adf2-3f26-8979-14ffd2138fe8 | -20.67971 | -42.33821 | 2024-10-09 03:25:00 | NOAA-20 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9dc2758d-c2ab-3c5b-9e04-974b034db1b0 | -20.67688 | -42.33195 | 2024-10-09 03:25:00 | NOAA-20 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fa5eaae1-feb1-3175-b39d-e8d414d6ae11 | -20.66785 | -45.9002 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5e7af34-309a-3052-aa47-50e03618d76e | -20.66756 | -45.90245 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15070a0c-ae59-37ff-8740-308f5e546ea2 | -20.66306 | -45.89399 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6abc24af-fa80-3bbe-a4b8-248346bc55c2 | -20.66198 | -45.8987 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df799aae-da0d-35da-88ea-f7a5526f2152 | -20.66112 | -45.90151 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 03a8bc41-3b2d-327b-bfb4-8faaed3ecefc | -20.66084 | -45.90374 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93280be7-c5ea-35d1-bd5c-dd9b9b3c1f2f | -20.65968 | -45.90884 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb3390b7-44e6-358d-b231-c5ecf2007f39 | -20.65846 | -45.9142 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2531a06a-a7ba-3a5d-a2bf-6e5d77006665 | -20.65507 | -45.90085 | 2024-10-09 03:25:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README63.md)
