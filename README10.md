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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 187ae26f-0730-3d68-b5c2-426b141c23a5 | -9.1407 | -49.66878 | 2026-08-05 04:02:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c2fede3-905d-3132-a7f2-4af985803827 | -14.2642 | -45.29476 | 2026-08-05 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c7564e6-e528-3eae-a699-95435481345b | -10.60502 | -46.38183 | 2026-08-05 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 96fae053-c374-3cc0-8127-d4b10d476ecd | -10.6368 | -47.4847 | 2026-08-05 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| edbcbe82-9af6-3b46-bf8e-afc89d0f1297 | -11.55328 | -47.7097 | 2026-08-05 04:02:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d9a9341-c92d-3218-be6d-79c9894a3965 | -10.13961 | -46.36975 | 2026-08-05 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf01ec43-bec8-3f8e-88ae-84e44d01b1c8 | -10.63579 | -47.49009 | 2026-08-05 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 956e53fb-600a-3ad0-858d-33f35e184056 | -14.19592 | -54.42773 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 226a3f64-dfe1-3391-8046-64654157fa77 | -11.5558 | -47.7109 | 2026-08-05 04:02:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa40b30b-2bd9-3854-ba4d-ca48d103e614 | -12.92024 | -49.48772 | 2026-08-05 04:02:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52138bb7-d70e-3060-8440-66d9ae7abac3 | -14.26882 | -45.2686 | 2026-08-05 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f7071e7-c97a-35f8-9ddb-ad3b5a423494 | -14.19452 | -54.43415 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1a174c15-1bb6-3f7d-9467-9d8b5fe6dcd6 | -12.49494 | -45.54284 | 2026-08-05 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e7e53931-1d35-3a6e-91c2-8d7aa7e59031 | -14.18257 | -54.44312 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a765689-d77f-35c2-a7ab-cead882da439 | -14.19219 | -54.43298 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 30557378-46fa-356c-a4be-bd9fc3de2a00 | -12.5958 | -46.93325 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cb66eef6-31be-34c0-bfdb-fd7be695d5f2 | -12.58229 | -46.95524 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 37bf8cdc-0f3a-3fb4-993d-673a45e8289d | -11.9834 | -41.05527 | 2026-08-05 04:02:00 | NOAA-20 | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 33297c69-7fc0-313b-9764-c10a3c12c35c | -12.44454 | -50.50731 | 2026-08-05 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f35183d-1742-3764-93b0-1af0ec323f1f | -12.58661 | -46.93217 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b2206992-6242-3497-9e1b-d305347d58ca | -13.79108 | -44.08653 | 2026-08-05 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4047586c-8c2d-3cfa-814f-0b1fda469ac7 | -12.13745 | -48.26338 | 2026-08-05 04:02:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 645ebb0b-9c4f-3abc-a039-2b2ac01ff661 | -12.14185 | -48.26746 | 2026-08-05 04:02:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ff6521d1-42e4-337d-bfec-a55daf9e7d97 | -12.60038 | -46.9339 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 15bf56ef-df27-3f15-95da-0cfa53b2452f | -10.61042 | -46.37793 | 2026-08-05 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a95de538-598b-32e6-b00d-b1bcf2c8f0b0 | -16.99214 | -43.13712 | 2026-08-05 04:02:00 | NOAA-20 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9be9d3a6-1745-30ad-8bbe-71105945ab8b | -12.59915 | -46.91533 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef5418ae-9637-36fa-83e3-f8a45968bbc8 | -14.17019 | -54.4114 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2402056e-fefd-324c-9ee1-819c8b9d6986 | -15.92755 | -43.98268 | 2026-08-05 04:02:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d77bd6e-c4c0-35bb-aa05-97642f9663db | -10.4543 | -50.22241 | 2026-08-05 04:02:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 294dc248-b872-3d02-a863-6b2f78d04b12 | -14.18377 | -54.41629 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fee26834-9a7b-3edc-8d64-b1d174a6ab53 | -12.00471 | -49.26942 | 2026-08-05 04:02:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cf4096cc-fd32-3121-8374-2f8701e0c02b | -14.16247 | -54.40226 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0701333-bf1c-3330-9381-12c4dd2c135c | -14.18526 | -54.40946 | 2026-08-05 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4a5108d9-cbdc-3c25-a8c4-a3e81b494bf6 | -10.75239 | -42.09082 | 2026-08-05 04:02:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4d01b5d0-c830-396f-996b-ca94b78ab322 | -12.60292 | -46.92024 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 875a32f5-33a0-3419-b01f-6ea8668f3c56 | -12.59371 | -46.91934 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 061118e4-652a-3bce-bfca-99b8c49330b6 | -12.44629 | -50.38087 | 2026-08-05 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e4c6c12-a00f-3f5b-ab89-11b80a13988e | -12.1875 | -40.40414 | 2026-08-05 04:02:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| bd7e8a05-f925-3f87-bd60-1d411fd2efe2 | -11.55684 | -47.70545 | 2026-08-05 04:02:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 21ce6629-c758-3179-9744-9402166f3d29 | -11.10408 | -50.42825 | 2026-08-05 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9697a2fe-04d7-36a3-8ba6-e4fcd1ca35f7 | -12.5904 | -46.93705 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e64be2b5-dd9d-3a92-851a-6ee01822ed3c | -12.47551 | -50.38285 | 2026-08-05 04:02:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6bf3395-93fc-3937-874c-db1985b9cc64 | -12.44676 | -44.23853 | 2026-08-05 04:02:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2803e05-48de-3a6e-bad0-c0503bb64f73 | -12.59202 | -46.92834 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c97c744-348c-3d2d-b435-e170734f21a8 | -10.75524 | -42.09539 | 2026-08-05 04:02:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7d4f1d57-9cce-315c-82a8-3ad7be754cf3 | -13.4403 | -43.85197 | 2026-08-05 04:02:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97a36bbe-6de4-3043-a951-2e03fa00013c | -12.20102 | -52.86624 | 2026-08-05 04:02:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37b0cb2e-bc31-3d16-9870-77307b163893 | -12.59496 | -46.93776 | 2026-08-05 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b4f5a527-57b2-32b5-b2ea-6ad717d4b1fe | -15.9261 | -43.98373 | 2026-08-05 04:02:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28f09fb2-3799-3bee-add9-48e4492081e7 | -12.20641 | -52.87352 | 2026-08-05 04:02:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10fab10b-3a1e-39c5-865a-8088574e57e3 | -12.14128 | -48.27046 | 2026-08-05 04:02:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1ae75079-c6f1-3a9a-a36d-a202354bba45 | -15.14318 | -42.15726 | 2026-08-05 04:02:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| fa4149e2-91be-3c24-8353-6fa54acb6463 | -17.99009 | -47.15464 | 2026-08-05 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41bd52dc-f300-3179-a9ab-29ad60f3a74a | -21.33823 | -43.698 | 2026-08-05 04:04:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ed6ce506-05f8-3ea9-af43-413826cd99af | -19.98766 | -42.2813 | 2026-08-05 04:04:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d7b58f21-83c2-3456-a6be-ecfbb2521e1f | -21.2633 | -48.7422 | 2026-08-05 04:04:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2a018167-d593-3b17-8509-cbcb9d68acbe | -18.56172 | -46.24813 | 2026-08-05 04:04:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c83b869-3368-3b42-8cc6-32b63544d00d | -18.3536 | -39.79895 | 2026-08-05 04:04:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 9eb5089a-3050-34ee-bf88-d97dc10559c4 | -23.45865 | -46.36503 | 2026-08-05 04:04:00 | NOAA-20 | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.0 |
| 3b63d908-80a4-3ad3-b8d6-261944561ec1 | -22.10316 | -47.00167 | 2026-08-05 04:04:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b3a80381-d9e9-3433-bc3f-07da994efce6 | -21.33485 | -43.69735 | 2026-08-05 04:04:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 168a8207-f004-3f2e-bbd9-785ab667600d | -18.63106 | -46.47715 | 2026-08-05 04:04:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6370342-37a7-36a2-bbb0-660c2303f865 | -18.88982 | -43.34129 | 2026-08-05 04:04:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 016eb10a-b6a1-3a19-8319-37d07a26829d | -18.98371 | -41.00762 | 2026-08-05 04:04:00 | NOAA-20 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 92d6e031-9e8a-32a0-899c-32c547f7e380 | -17.98237 | -47.14962 | 2026-08-05 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1bb5f81-de96-3db3-8ee8-8f4fea421de9 | -23.45778 | -46.36968 | 2026-08-05 04:04:00 | NOAA-20 | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.0 |
| c2b5ff64-0d49-340c-b4ae-cce1d9117f81 | -21.70353 | -47.16886 | 2026-08-05 04:04:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 025c86ff-3c81-3126-b014-1face705c110 | -19.98825 | -42.27762 | 2026-08-05 04:04:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6d6a76c1-0d60-3ae3-9790-47e8c096e930 | -17.99509 | -47.15121 | 2026-08-05 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6bcaa2d8-dec6-377a-9143-6e5d0309e8a3 | -18.56564 | -46.24893 | 2026-08-05 04:04:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ab0b26e-528c-329a-8f94-f960fadffee0 | -23.45566 | -46.36693 | 2026-08-05 04:04:00 | NOAA-20 | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 40.8 |
| cb780d87-cd7a-36a1-8b14-9cfaba7a965c | -17.72919 | -42.63704 | 2026-08-05 04:04:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c883a9c6-3886-30ca-9e2b-83b18b942b61 | -17.98438 | -47.16175 | 2026-08-05 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3a6df7c-f2f7-37e1-93b6-c976af302c2f | -18.56474 | -46.25103 | 2026-08-05 04:04:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e981c42-fc22-3ce7-b02e-7257e86a0f5e | -17.88563 | -42.41111 | 2026-08-05 04:04:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 35b8ca7e-66c5-3b8d-9e49-ed9fd25a0b09 | -23.14146 | -48.67272 | 2026-08-05 04:04:00 | NOAA-20 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 317bbf93-a2e9-3470-af66-6e3a0fb41f35 | -19.88042 | -43.96157 | 2026-08-05 04:04:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5c13e891-ed6f-34b1-bc32-48e323aaebcd | -22.10604 | -47.00774 | 2026-08-05 04:04:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f8c2395f-9d86-3914-bd11-c11a82bff1f1 | -17.97819 | -47.14882 | 2026-08-05 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85b08f53-ccfd-3dc9-bc9f-5e9769d52be0 | -17.94948 | -43.88871 | 2026-08-05 04:04:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4eda13c9-999b-3be9-904d-a2b7f172413c | -18.738 | -47.46384 | 2026-08-05 04:04:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4ed2387-7825-3701-94ad-e4dfdf16ebf9 | -22.76984 | -43.45903 | 2026-08-05 04:04:00 | NOAA-20 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 79a77d07-e257-3b6c-a60b-a66b1e762610 | -21.03689 | -48.46117 | 2026-08-05 04:04:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2e204ef-f4a8-3906-87d8-755feb8559b9 | -22.85955 | -43.05906 | 2026-08-05 04:04:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b0263469-1cb0-3068-8335-34c0ad55fad6 | -21.29386 | -49.04712 | 2026-08-05 04:04:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fb78b1f1-f48b-37ac-8d63-e7a85739d569 | -18.69512 | -44.55015 | 2026-08-05 04:04:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e96ce8c-d901-32e0-9bab-d39a88bdce96 | -18.46553 | -43.25328 | 2026-08-05 04:04:00 | NOAA-20 | SANTO ANTÔNIO DO ITAMBÉ | MINAS GERAIS | Brasil | 3160207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 73e4af6f-64bd-33df-b34d-aa08b893c956 | -21.26419 | -48.73782 | 2026-08-05 04:04:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dcb2ae4e-913d-3f2b-b0cb-4425e133fff0 | -18.98039 | -41.00705 | 2026-08-05 04:04:00 | NOAA-20 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e8b49ecb-f970-3d05-a99a-d23975805dfd | -19.00161 | -44.443 | 2026-08-05 04:04:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2cf2db27-aadd-367a-b71d-3b8f051585b3 | -18.35304 | -39.80272 | 2026-08-05 04:04:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 218af15e-1c90-3eec-8bff-54a589fb1aa9 | -17.91723 | -44.24414 | 2026-08-05 04:04:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c29923dd-1f3a-35dd-a010-ae11bfcd1fda | -17.98512 | -47.15792 | 2026-08-05 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 64625f73-07cb-328f-8128-3ed2e6027a75 | -20.08925 | -40.51905 | 2026-08-05 04:04:00 | NOAA-20 | SANTA LEOPOLDINA | ESPÍRITO SANTO | Brasil | 3204500 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 801c988d-8337-3937-bd68-90cfd25dd2ba | -17.833 | -44.34653 | 2026-08-05 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93247a1f-f81a-3f24-b5ed-058e9474a4eb | -17.9802 | -47.16094 | 2026-08-05 04:04:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6deb4935-736e-37f2-bad0-dd36a9b9ac23 | -21.90607 | -41.11032 | 2026-08-05 04:04:00 | NOAA-20 | SÃO JOÃO DA BARRA | RIO DE JANEIRO | Brasil | 3305000 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e27c95b0-f64e-333f-a73b-90b56da3c282 | -19.1587 | -47.3193 | 2026-08-05 04:04:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f0b2df38-44ff-3a73-87bf-b1c5c9d80c1b | -21.60596 | -46.29591 | 2026-08-05 04:04:00 | NOAA-20 | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README11.md)
