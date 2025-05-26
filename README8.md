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
| e93bf20c-7757-39f2-8eb5-bc2a0ef4cd6f | -21.96226 | -56.07569 | 2025-05-26 04:53:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14314ef6-32bc-3eef-9cf6-3829bbd57d56 | -22.21377 | -56.20169 | 2025-05-26 04:53:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f5040f6-470f-3eed-a151-f3b525d8ed93 | -23.18476 | -47.10691 | 2025-05-26 04:53:00 | NPP-375D | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8f9d21bd-372b-3a61-9613-31fe81cbf2d2 | -8.0312 | -43.1964 | 2025-05-26 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |
| 3d6d3ab4-8d97-3504-b5dc-59439abf97fe | -8.0123 | -43.1984 | 2025-05-26 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.3 |
| 4313b9ac-3b5e-3034-bd58-5d313d95f1fe | -7.65288 | -46.10985 | 2025-05-26 05:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98eb60a4-c55b-33cb-bdd0-5a7fdba956b4 | -7.65973 | -46.10615 | 2025-05-26 05:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6f4e44ee-0d17-308b-9cb6-9ef0c0b1181f | -7.54016 | -45.82503 | 2025-05-26 05:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 13228b9c-af29-38e3-8101-ab8947589489 | -7.59812 | -46.28172 | 2025-05-26 05:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61570d7e-5d91-36b7-a3ff-3e171301ce42 | -6.63503 | -55.01019 | 2025-05-26 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ca4fae6-2278-3c95-b5d6-e4cc8ad77979 | -3.94782 | -56.1067 | 2025-05-26 05:08:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c59088fa-722a-3a00-b7ff-2ae056fa5180 | -5.68317 | -44.12589 | 2025-05-26 05:08:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf921888-2f4f-3a72-9b43-65b5f0a1ef1f | -4.28927 | -48.27356 | 2025-05-26 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efe33e65-0dd4-33c4-94fc-3aa9e576cb52 | -7.65762 | -46.10765 | 2025-05-26 05:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| aa66f7ef-4922-3cc0-a20f-2374991b6715 | -7.65351 | -46.10526 | 2025-05-26 05:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e60aca59-8bdc-37c4-a0d0-74119a4f3a21 | -7.59874 | -46.27711 | 2025-05-26 05:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5903b2b3-a1b4-36b3-8a1b-6ccf3fee166f | -7.54646 | -45.82607 | 2025-05-26 05:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9dcb45c6-3d21-3c22-95fb-f2ebe189a389 | -7.65823 | -46.10299 | 2025-05-26 05:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6b09a299-96bc-36ac-bf16-51766d2b015d | -8.0312 | -43.1964 | 2025-05-26 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| f6f8feca-9f8d-3f0a-9225-1e6b98e27921 | -11.87092 | -52.25443 | 2025-05-26 05:10:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8a9b0e24-0904-316c-849f-2b9999aca8e7 | -11.29162 | -54.01876 | 2025-05-26 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56b3b6c9-ab0a-3711-97e7-b587d91e71ef | -10.69911 | -48.59217 | 2025-05-26 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a468a73-5756-3820-9d7e-42d191dcd2e3 | -9.37518 | -48.41359 | 2025-05-26 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 477b6871-488a-34c9-9bd5-a680748ca687 | -10.70504 | -48.58977 | 2025-05-26 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 244648e5-e5c6-3bda-9442-377bd0737934 | -11.29473 | -54.01716 | 2025-05-26 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1340e31f-5462-375a-8e0f-5e076d1c6e4a | -8.44253 | -49.63341 | 2025-05-26 05:10:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1d1ff30-5427-3978-8ddb-5e3369bb0247 | -10.45646 | -47.94516 | 2025-05-26 05:10:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78e5b4ba-e8f8-3ac4-8897-addecc39c094 | -8.44333 | -49.62652 | 2025-05-26 05:10:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 42d2c691-2073-352d-acfb-0dfa0e8a003d | -11.2955 | -54.01933 | 2025-05-26 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92a987a5-950c-3133-9e14-1e2c2580bd1d | -11.3674 | -55.11754 | 2025-05-26 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0512baa8-8fc4-3d82-b351-9c7300005287 | -11.6073 | -54.49293 | 2025-05-26 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2040a94-2aed-30a1-8660-011717a24c30 | -10.45698 | -47.94105 | 2025-05-26 05:10:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9347bc0-eb6a-3977-93b4-8170b56db975 | -11.14392 | -53.92814 | 2025-05-26 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af4ce4aa-6bd5-3c50-8c90-ad3d787350ea | -8.44329 | -49.62764 | 2025-05-26 05:10:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| be8f0070-6ce7-37ba-8c0c-efd86d273f6e | -9.37589 | -48.41232 | 2025-05-26 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae63a9f7-83ab-3091-8a31-65efdff3292c | -14.03675 | -55.12836 | 2025-05-26 05:10:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c72fd276-6098-33ec-9c79-fe8511042367 | -14.04294 | -55.13874 | 2025-05-26 05:10:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ad8cf042-fcc2-3e71-8f3b-8aece0dd46b8 | -9.38092 | -48.41674 | 2025-05-26 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1cba5123-3a7b-32af-bb85-775aa075ba7f | -9.37567 | -48.40997 | 2025-05-26 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a12c2ebd-9419-3112-9103-7c270f29125b | -11.14003 | -53.92756 | 2025-05-26 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2248f825-8b14-3dcc-adb7-9ce55d9437fd | -15.07578 | -48.94559 | 2025-05-26 05:10:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 335861e4-ba8a-36e3-9776-e0b45f4045c4 | -11.30006 | -54.01499 | 2025-05-26 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0788abcd-820e-3f28-abf1-0226c9d570c0 | -11.86655 | -52.25377 | 2025-05-26 05:10:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ebcb5736-f894-3fee-9171-421e77196125 | -14.04388 | -55.13686 | 2025-05-26 05:10:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 09a2e1ad-79bf-3a74-b839-ca119b4c5e8c | -11.86598 | -52.25808 | 2025-05-26 05:10:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5456965-42ea-3e11-9cfd-6deddead4154 | -11.14074 | -53.9226 | 2025-05-26 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0267674e-19ec-3258-849c-4b57bab55863 | -10.69952 | -48.589 | 2025-05-26 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04fb4920-c1c0-3e3e-84d8-920ce8f2bb14 | -13.78425 | -54.31527 | 2025-05-26 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a3131028-71a6-3915-9959-3fe06f5980ba | -9.85998 | -65.26122 | 2025-05-26 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4bfacb3-b0e3-3dd7-b6a5-320ccfe9bdd2 | -9.98164 | -52.13529 | 2025-05-26 05:10:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 406f582d-7648-3e16-883d-04f7b52cabaa | -11.91922 | -54.4151 | 2025-05-26 05:10:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25c846f7-e22f-38ea-a871-bef6f2de0e98 | -11.99354 | -52.47217 | 2025-05-26 05:10:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f5d2e348-2b01-31d7-a884-94ecb9303010 | -8.30816 | -55.10778 | 2025-05-26 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7349b5d-d201-34ae-8e1b-3ee5467fb6f4 | -10.65421 | -46.96631 | 2025-05-26 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92233126-8b44-3ed7-b830-b87667da1abb | -9.98107 | -52.1394 | 2025-05-26 05:10:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ff0a5fc-7fed-312d-9aaa-77d989cf86cd | -10.6419 | -46.96512 | 2025-05-26 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2bb91824-e972-3b45-941d-3570e0bbbbfd | -9.37543 | -48.41594 | 2025-05-26 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7197289-b742-376d-ab9c-0314d1ec3153 | -9.97679 | -52.13869 | 2025-05-26 05:10:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dc41f09-778d-3c99-8315-5f80155ba072 | -10.45072 | -47.94436 | 2025-05-26 05:10:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16bed1ed-7fb7-33af-bdd3-e76099c5fecc | -8.44252 | -49.63227 | 2025-05-26 05:10:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d4c2dfde-50dd-3671-84aa-2ee44dc57f23 | -11.29618 | -54.01443 | 2025-05-26 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c2f827a-4334-3dd9-9e0c-7f8e343173f2 | -10.64806 | -46.96564 | 2025-05-26 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 552565e7-b932-340b-b3d9-afa329bcfbd9 | -9.37636 | -48.40869 | 2025-05-26 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c358b0ba-7df3-3974-a03f-4a0680d5033b | -9.97622 | -52.14281 | 2025-05-26 05:10:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cd51b0d-3da7-3266-b1d9-e762789060d6 | -13.78818 | -54.31587 | 2025-05-26 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 751d5e3d-5dcd-3a83-b6cf-6b73bef05ef6 | -9.97193 | -52.14214 | 2025-05-26 05:10:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ae5fbc2-f83e-39c3-8053-586dcaab782e | -14.02413 | -55.13605 | 2025-05-26 05:10:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83981f1c-763e-3c42-8f5a-ecf07e2e010a | -19.71143 | -54.61692 | 2025-05-26 05:12:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9bef34e2-8e66-3596-9a82-9c59d507ed3b | -19.87976 | -54.36798 | 2025-05-26 05:12:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5c70f464-4987-3d72-92cb-3bca8dfd4d99 | -15.62766 | -57.30839 | 2025-05-26 05:12:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b3e7297-fb09-3522-b38b-a7ebf6b4ca11 | -20.60686 | -48.86431 | 2025-05-26 05:12:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 3689b0a2-65f4-3054-8e74-49116051116c | -19.71257 | -54.61639 | 2025-05-26 05:12:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4049ec2-a20d-3b13-8195-426da0b47259 | -19.87175 | -54.36253 | 2025-05-26 05:12:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0622e919-fd51-394f-a8dc-2a1d7e4a5aa2 | -19.88026 | -54.36389 | 2025-05-26 05:12:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 906ada00-7918-37b3-a322-f04684545f2b | -17.53641 | -46.90232 | 2025-05-26 05:12:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1bf0c720-f33f-3cb8-a110-3bc06a6cc038 | -20.61299 | -48.86501 | 2025-05-26 05:12:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5222b1e3-e939-305c-b1d7-a756d9777f31 | -19.87551 | -54.36733 | 2025-05-26 05:12:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a41fc716-1902-3d16-b58c-d149128d5517 | -19.71563 | -54.61744 | 2025-05-26 05:12:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35868f0f-606c-38fe-8858-7c8eb656feed | -20.60644 | -48.86908 | 2025-05-26 05:12:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 2015b984-1f71-3893-9824-588c1bfa927b | -19.71306 | -54.61231 | 2025-05-26 05:12:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fa0af9f-63ea-390f-bbea-a36ce405d344 | -19.876 | -54.36323 | 2025-05-26 05:12:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ebf6a207-1e60-3f7e-b008-60bcf9675e82 | -19.71195 | -54.61285 | 2025-05-26 05:12:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d9464cc-4d3c-3965-a835-4f733c695d86 | -19.87126 | -54.36663 | 2025-05-26 05:12:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82c5f73a-3ec5-3121-83f0-1eeecbef0c65 | -20.93988 | -56.5925 | 2025-05-26 05:14:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91d935e1-17e1-31c2-95f3-26cc398b1256 | -20.93923 | -56.5973 | 2025-05-26 05:14:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1a53cbb-095c-3252-8b6f-21e855ed67a6 | -22.21211 | -56.20063 | 2025-05-26 05:14:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f78113ca-21a3-3a9f-a9b1-eae116a7b0c0 | -22.21275 | -56.19921 | 2025-05-26 05:14:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22d0e948-31f4-31b4-8bc5-d5b0b9236df4 | -8.0312 | -43.1964 | 2025-05-26 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.3 |
| 921cedb2-66bc-33cd-b47b-12b84eb834ab | -8.0312 | -43.1964 | 2025-05-26 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.0 |
| 056785e8-ceb7-313d-96d2-984170a0d021 | -7.6574 | -46.1013 | 2025-05-26 05:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 38.5 |
| e3561f63-507e-33eb-b3aa-f9ef9c6a3e78 | -10.45396 | -47.93958 | 2025-05-26 06:01:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d77c1219-b8bb-3c27-b0d3-b9efcb8442e0 | -7.66512 | -46.09786 | 2025-05-26 06:01:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| ae6fbaef-8305-3242-9347-3740eb08b00b | -8.06121 | -43.13729 | 2025-05-26 06:01:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.4 |
| dd4b877d-f091-3fc6-9168-7f136d16b513 | -11.87043 | -52.25127 | 2025-05-26 06:01:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ab6aba07-64a6-3df2-9411-849042c5e230 | -8.06483 | -43.10937 | 2025-05-26 06:01:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 35708e4f-b336-3204-ae65-39c4418c2d10 | -7.67674 | -46.09937 | 2025-05-26 06:01:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 9aae6e84-2384-39ba-8179-ed9e171ee7a9 | -8.02364 | -43.18375 | 2025-05-26 06:01:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.8 |
| 710f0190-fb8a-3872-ae6a-41c86f5fa6db | -8.02445 | -43.1884 | 2025-05-26 06:01:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.8 |
| bede1965-7f0d-383c-93ae-0a413f29a065 | -7.65351 | -46.0963 | 2025-05-26 06:01:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 2292574e-8b1f-3ece-893a-69151a1458aa | -11.14429 | -53.92128 | 2025-05-26 06:01:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |


[Clique aqui para ver as próximas entradas](README9.md)
