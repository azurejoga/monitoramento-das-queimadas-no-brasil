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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9695504-b569-383c-aebf-bc1f487b416f | -12.96254 | -46.94573 | 2025-09-22 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bee48ded-25c8-3ce1-b61b-ac7a19be9a1f | -11.70333 | -41.49573 | 2025-09-22 03:49:00 | NOAA-21 | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9e95ffa5-b8ef-30a6-bdb2-16d0adc54b3c | -7.96552 | -43.89927 | 2025-09-22 03:49:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 203fc714-7f7d-341d-898c-e6299853dfc3 | -7.59647 | -44.47928 | 2025-09-22 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 02207232-97ef-3f26-9ebe-54b10c45a5d6 | -10.18945 | -39.25575 | 2025-09-22 03:49:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 262df76c-530a-3b3f-8868-494fdef35432 | -0.94557 | -47.35402 | 2025-09-22 03:49:00 | NOAA-21 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9970375e-c28f-3560-9cf3-38fad5592c29 | -12.98003 | -46.37691 | 2025-09-22 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c83c1366-c271-3bb4-99ca-656d9301673b | -10.40345 | -47.85316 | 2025-09-22 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5936979f-59c8-3e95-86b3-d49f25520ca8 | -7.60966 | -44.48658 | 2025-09-22 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| fddf2457-38f7-3940-86cd-de3d71ee654a | -13.67655 | -47.86907 | 2025-09-22 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0536d8e0-6c16-3be1-9a52-f57b548c6d7b | -14.25093 | -44.71224 | 2025-09-22 03:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f0bc166-c383-3436-a0f5-a9460a15cebc | -13.50688 | -47.26246 | 2025-09-22 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 251966cc-4f91-3e74-9526-90dbd34262bd | -12.71663 | -47.69466 | 2025-09-22 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6dee87d-2354-3e06-bac3-bf6d429b1d46 | -8.80632 | -43.02299 | 2025-09-22 03:49:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1e1140b2-eb3e-3029-a80f-3e05198d01de | -11.41983 | -43.52143 | 2025-09-22 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d80c5f83-01ef-3de8-8d35-68616edec09e | -7.30057 | -44.11926 | 2025-09-22 03:49:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95cfa88a-feab-36b9-8a19-d27bf1f46a5a | -8.18816 | -42.383 | 2025-09-22 03:49:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bb4858be-afe8-32bf-856f-152ee5a0917a | -11.52 | -43.61745 | 2025-09-22 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 519e3b3a-6830-3b7f-8d3c-9f4b72f727d2 | -10.32199 | -46.10731 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9ca7755c-1458-373c-9a47-dca517e7d1f5 | -10.46327 | -44.19298 | 2025-09-22 03:49:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 265cba4c-3c9b-3311-bc45-0c0a44f92c01 | -8.01123 | -45.72256 | 2025-09-22 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93bec131-7b27-3857-9664-94741f14c17f | -12.72614 | -46.82729 | 2025-09-22 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5cd21448-e688-391d-8292-fdb13b0f321f | -7.61436 | -44.48733 | 2025-09-22 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7c61a2d8-b5b7-343f-98e1-04a5c521d3eb | -13.3044 | -47.29571 | 2025-09-22 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 757e8b61-9356-3a85-a17f-5401adcc54f9 | -12.73061 | -46.83106 | 2025-09-22 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e0bdd4f-dc63-3894-904e-774a9d70efcd | -12.97805 | -46.38769 | 2025-09-22 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b611140f-85c8-3dd5-9d4c-0731f5bf49c6 | -11.92355 | -43.42402 | 2025-09-22 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5359cc3-365c-3a2d-b0d9-7f4c01158f73 | -11.73611 | -47.79788 | 2025-09-22 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| adf8a72d-160d-3a4f-a681-d2cb24f69618 | -10.3566 | -46.05926 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f10d504b-dfbd-39d9-9dad-296bba632b42 | -11.45142 | -43.5348 | 2025-09-22 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad23397c-53e1-3f3c-b832-7e8ea088ff2c | -8.28235 | -41.68285 | 2025-09-22 03:49:00 | NOAA-21 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 76a50036-61e6-3a8f-98b3-30da7082ebd9 | -11.52624 | -43.63025 | 2025-09-22 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f73415d2-be6c-3a57-8598-3045f3062625 | -12.72505 | -46.83303 | 2025-09-22 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| edcf4330-875d-367e-9602-e4102fe4d372 | -8.84575 | -43.01767 | 2025-09-22 03:49:00 | NOAA-21 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| be41919b-1bf1-3a38-94c6-b73b9e3e7df7 | -11.26451 | -49.24613 | 2025-09-22 03:49:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 981f175e-219b-3106-b626-f38581803475 | -12.71232 | -47.69691 | 2025-09-22 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08bc9b43-3927-3052-9f57-45e8e3b46ac8 | -8.00614 | -45.72182 | 2025-09-22 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3191d63f-01c4-32d8-aee3-1156e68dff6d | -7.38271 | -44.57259 | 2025-09-22 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f1cd7793-2912-378c-a49e-9a9d365adf51 | -10.40831 | -47.84988 | 2025-09-22 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2c9036b-aa73-3899-9d8a-f969ff6e4da3 | -3.88234 | -38.39543 | 2025-09-22 03:49:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 469ef360-3e45-3306-ae48-758539667796 | -10.366 | -46.06395 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5932b9a3-0312-3e44-9379-186be0ce2ffa | -8.30178 | -43.67806 | 2025-09-22 03:49:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 766c514f-7fc0-3cc2-a11b-be0e243bf406 | -11.78043 | -43.76337 | 2025-09-22 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a979e7bc-b11c-3f11-a9fe-cf6a51927340 | -7.02535 | -46.30779 | 2025-09-22 03:49:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0e56d3b-e98d-3781-9ff0-7b23d6f6e040 | -13.49718 | -47.25811 | 2025-09-22 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f38c78b1-beb4-3318-97ce-185798ff57ff | -0.94852 | -47.35667 | 2025-09-22 03:49:00 | NOAA-21 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a6e28660-277a-3045-a2ee-acb6734f8c3b | -13.74687 | -47.84494 | 2025-09-22 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fefd6a32-9460-3170-bea1-8a12c36ab9d2 | -7.51192 | -43.69112 | 2025-09-22 03:49:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 31ce22db-484d-327e-8e76-9480582713e1 | -8.90609 | -46.10788 | 2025-09-22 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b5f5e23-af9b-36d8-b16d-cef0c345a07e | -8.30544 | -43.68297 | 2025-09-22 03:49:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b42c518-cc67-352f-bff8-01d006d66d50 | -12.75429 | -47.7557 | 2025-09-22 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db339ba1-fedd-3f50-a67e-2bd0dc38e5e0 | -11.63899 | -44.33794 | 2025-09-22 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2d3b9494-9310-3402-a098-faffe652ff64 | -11.47383 | -46.93635 | 2025-09-22 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0255bb37-2b42-3a77-af1b-4c7e0a20ae96 | -7.35139 | -44.55671 | 2025-09-22 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e797498a-5c90-3569-9f36-dc2f8e7b358c | -8.92954 | -40.02084 | 2025-09-22 03:49:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 55601c73-b43f-39a4-8e9b-5dfb48d41345 | -10.34846 | -46.07554 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54aa8ef2-d0d9-3931-bd39-1445cbb97745 | -7.80099 | -46.19561 | 2025-09-22 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e52858bc-b400-3c29-9b12-16760e99c1c9 | -10.36818 | -46.05212 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a831000-9d89-3d5b-ae16-62bb0c485951 | -10.32253 | -46.10443 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f6dbc090-de4a-3565-83b9-3376ddf6344e | -3.17257 | -41.05834 | 2025-09-22 03:49:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 29239999-af5e-371c-8907-3ac184b8e22a | -10.38879 | -46.0798 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47072ada-53b1-30b4-a848-018e8888d977 | -11.51932 | -43.62125 | 2025-09-22 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85d95aac-16f8-39c6-ae41-a868fd994b4f | -8.88153 | -37.20419 | 2025-09-22 03:49:00 | NOAA-21 | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a4c68625-9060-3060-9c1c-b194850610a0 | -12.98194 | -46.38446 | 2025-09-22 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f4df68d8-d183-3c65-84cb-2d6c0ade3b15 | -10.35715 | -46.0563 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1076127a-3058-3c29-9bf9-fe736681a750 | -11.28893 | -47.50853 | 2025-09-22 03:49:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c806588-4eab-329d-90a8-51872d465412 | -9.73509 | -45.95414 | 2025-09-22 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b80ab07d-d9a1-3381-b0a9-35d52bf8a88c | -9.16296 | -44.61982 | 2025-09-22 03:49:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 09da7223-725c-3754-b773-cf59e6fad894 | -13.27537 | -47.64479 | 2025-09-22 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c4e287c-e193-3048-937b-328ed9c3a2b9 | -12.96311 | -46.94269 | 2025-09-22 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7d89764-c16f-3fbf-b09d-9c25075e5f7c | -7.50822 | -43.68603 | 2025-09-22 03:49:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4f8ade39-f972-377c-91f2-bcd157d6adaa | -11.66109 | -47.49492 | 2025-09-22 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 78edccf8-bb26-3616-b5f6-92191b277f8f | -14.23158 | -44.3209 | 2025-09-22 03:49:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f61edcf3-07a2-3603-b3cd-4fcbafee239f | -7.79699 | -46.18759 | 2025-09-22 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0487a11d-8d4f-3c55-b35a-655de5535542 | -12.74106 | -46.88597 | 2025-09-22 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99646705-1a85-36a6-a9e4-d8d2cb10e5da | -12.97416 | -46.38157 | 2025-09-22 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c7dd273-fa7d-381f-88d2-b751ff0d301c | -10.34406 | -46.07157 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b257e3e8-464e-3222-bb9b-c04dc268ff29 | -14.53073 | -44.87881 | 2025-09-22 03:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb280271-7c93-362b-b023-8ce85870dc62 | -10.36546 | -46.06693 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c8621013-91a0-3c09-9fb4-385a3037ab6e | -10.37774 | -46.08405 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8697459a-d8f2-3bb1-bee6-f855c02cc2af | -12.71825 | -47.69468 | 2025-09-22 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3e3fd022-4176-3f0c-973e-6132230e44c2 | -11.50858 | -43.57235 | 2025-09-22 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2819195e-558d-3dee-a83d-8b81515d2ae6 | -10.37207 | -46.05886 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1bfab1f8-fef0-30e3-8df4-d29c73465296 | -10.33856 | -46.07351 | 2025-09-22 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83d66a91-cad1-3314-bb52-4693feb047d9 | -11.26657 | -47.47997 | 2025-09-22 03:49:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c9032623-46ce-3362-9761-95805fc6c570 | -11.48715 | -43.54896 | 2025-09-22 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59d00b09-5645-3241-a7d8-f21fa2a2b825 | -11.52278 | -43.62575 | 2025-09-22 03:49:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6640fe9-1969-3040-a89d-3f61bae23635 | -7.23442 | -43.75846 | 2025-09-22 03:49:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 61f718fc-aec9-35c7-acf8-6649e6b2e1ec | -12.71167 | -47.70032 | 2025-09-22 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53b943b7-ea57-3a1b-a607-efb22335ab02 | -7.43835 | -42.38883 | 2025-09-22 03:49:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| aaf9db9c-9315-3e10-a77b-974d7bd83c95 | -12.71395 | -47.70823 | 2025-09-22 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b82480b7-f118-3f10-a7cb-23492b511120 | -10.50659 | -44.05023 | 2025-09-22 03:49:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 640f5945-7c7a-3ce7-ad9b-fc46f8638d6a | -7.79755 | -46.18441 | 2025-09-22 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9ba59a3a-7e14-3964-8faf-aff0927fe6b9 | -7.36087 | -44.55817 | 2025-09-22 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 2579416e-d482-33cd-9078-cb39c7bd5ea2 | -7.80089 | -46.19631 | 2025-09-22 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4886d786-0ba6-3181-9f9a-d36b77f2e9b4 | -13.07661 | -47.02163 | 2025-09-22 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 906bc100-97f8-3112-bc9b-f419cd48bda2 | -12.71697 | -47.7014 | 2025-09-22 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1fdeb179-7512-355f-9b89-9efc83f8e873 | -12.74901 | -47.75446 | 2025-09-22 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| afd5037d-a950-32ff-9384-5149c9fdd0e9 | -12.699 | -46.86061 | 2025-09-22 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 86985353-631a-332f-b97d-7e50f721cb32 | -8.84926 | -43.02211 | 2025-09-22 03:49:00 | NOAA-21 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README12.md)
