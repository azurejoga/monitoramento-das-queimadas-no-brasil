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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b586c43f-89ee-3be8-92e5-29271dea776a | -11.3609 | -45.01628 | 2025-09-27 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 653bbefa-682c-34f2-b61a-55f62c930326 | -11.14113 | -43.36908 | 2025-09-27 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e565169d-8880-3a61-8f4c-d8db12d39463 | -11.37769 | -44.94358 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ddc8a838-a4aa-3dcb-ba03-7824fc70d88a | -11.6813 | -44.42075 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93fcc16d-66e4-3835-ad5f-1ce16712263d | -11.98067 | -47.89949 | 2025-09-27 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d21e1247-7eb0-3e55-92a2-f073f89670cd | -7.62949 | -43.80518 | 2025-09-27 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5c959a08-6b61-346f-829e-3604d1295a28 | -7.11075 | -43.7547 | 2025-09-27 03:55:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cca32c6-5501-3439-a7ea-8976f08f3a84 | -11.67337 | -44.46696 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8a52b384-1584-367c-9a3b-0c2d1ed42a16 | -10.1842 | -49.51335 | 2025-09-27 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 62867946-f83f-3a30-aa41-37a9962cc32e | -6.99562 | -46.99465 | 2025-09-27 03:55:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1fa69f25-acb7-3526-a4a2-3057dc172fd4 | -11.43568 | -43.51323 | 2025-09-27 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f32e86a-b438-3cd5-bf8f-5839b5dc3112 | -11.6909 | -44.41192 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f90429c9-ee34-3102-8bf5-60d2c56d061d | -11.77794 | -43.76263 | 2025-09-27 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 93328eeb-cf48-3ad7-8c6e-226c94127257 | -12.26797 | -44.05991 | 2025-09-27 03:55:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff6f80c5-5dc9-3d6a-97c3-98c6f180795b | -11.44213 | -44.93291 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30865618-7314-3488-8615-0a1d3650e6f1 | -7.6236 | -43.84031 | 2025-09-27 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a42e9086-89b0-3301-95d5-f1a34b4132cc | -10.12658 | -45.3087 | 2025-09-27 03:55:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e6f2cf8-eaaa-3b39-bb24-786a11f7d1c4 | -9.71248 | -48.2442 | 2025-09-27 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a4cd20c-f1ff-37b2-8531-8c528facb5ea | -12.09913 | -44.31503 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 603936b9-c4fe-3d0e-b5bf-aa7ac20e561f | -11.43489 | -43.51779 | 2025-09-27 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89d4ae5b-e2a6-3ad5-91a0-902d1b0c83bd | -10.00117 | -44.17829 | 2025-09-27 03:55:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22e4fbfc-61c6-39e1-8012-e0e13d734ddd | -11.69562 | -44.45198 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e4e7c38b-f4b5-3964-bb58-9a64033ea822 | -10.57502 | -44.07266 | 2025-09-27 03:55:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab5722fa-2abf-3a95-9adc-ce0354e0a510 | -6.55215 | -43.84715 | 2025-09-27 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c9c5a19-a58e-32cd-8176-b8cdfb3ad680 | -12.03329 | -47.0629 | 2025-09-27 03:55:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7918bade-1cb3-3415-91a3-015793a487be | -8.80958 | -40.99371 | 2025-09-27 03:55:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 24c084df-32a7-376f-8784-dd5b3fcf9875 | -9.94199 | -48.49717 | 2025-09-27 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26ba1766-9f14-315d-883d-e44840d40657 | -10.29805 | -48.79186 | 2025-09-27 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7bc25d2b-c60c-3673-a21c-4abca5dcdd1a | -7.78428 | -46.94012 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1dfff23e-f1c0-3bdd-b6c7-2c89ad7ca49c | -9.699 | -48.94357 | 2025-09-27 03:55:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69490d69-dfd4-31df-ad34-132ad3b3d975 | -10.86395 | -47.78431 | 2025-09-27 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 516e1605-e1f3-3ed9-98f0-28d14bbf8341 | -11.71533 | -44.41099 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7b1ea132-379e-34bd-abe0-5043ef78ed28 | -12.29051 | -45.65218 | 2025-09-27 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88d3642c-fcbc-3914-801e-eaaa59a76efb | -9.97271 | -43.60358 | 2025-09-27 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b147175d-8d20-33f9-bbfa-5dd91a2fa7e9 | -11.49389 | -43.53288 | 2025-09-27 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10a14bc3-bf45-3d06-be29-9ddb113372e4 | -6.70216 | -44.58437 | 2025-09-27 03:55:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38791d51-4d80-3791-be37-5b148149386e | -13.18218 | -47.42525 | 2025-09-27 03:55:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0afe816b-72a4-3abf-8d48-ed41c8b0d662 | -11.69788 | -44.41844 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 567ef321-2759-3133-85eb-867c5477742b | -9.98136 | -43.57547 | 2025-09-27 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57688b2f-fdc4-31a2-9678-521071364bcd | -10.47216 | -46.52722 | 2025-09-27 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 50671716-ee9f-3a4d-86d8-926ad7253e86 | -11.97081 | -47.89779 | 2025-09-27 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 161d6027-0613-3d09-855a-58fcfcd89550 | -12.2794 | -44.06189 | 2025-09-27 03:55:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42834776-412d-3fd4-94cb-9d5fe21d50a7 | -7.62763 | -43.84097 | 2025-09-27 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cac05ae8-fe05-3157-a0ce-9ed44648f866 | -9.18435 | -46.64669 | 2025-09-27 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15c36a67-af8e-3250-874a-e7ec2810827f | -7.7198 | -47.30687 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e4106e77-f155-30e5-a82a-78f1270ef4ca | -9.94262 | -48.49377 | 2025-09-27 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11012189-e410-3b91-aacf-fd644fa4b796 | -9.11686 | -45.88247 | 2025-09-27 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 472fcc0e-c98a-3bab-878a-0cd48a73aceb | -6.49656 | -43.27845 | 2025-09-27 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a6364a9-c4e9-39a0-83b1-686b70c0be83 | -7.71472 | -47.30592 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a4108679-677d-3ec3-9a4c-119ecb1dd441 | -12.00865 | -47.88584 | 2025-09-27 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 41472bab-ecc7-3d17-b754-9d0b93a3850e | -9.96726 | -43.61253 | 2025-09-27 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee1d2780-39b8-3158-b417-3d7ac0acf403 | -12.55219 | -45.84341 | 2025-09-27 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a008247-7c73-3c8e-bb85-b38e59775c99 | -10.90224 | -43.62619 | 2025-09-27 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5cbd847e-0d04-3d7c-a04e-340b932f3441 | -10.81491 | -45.3775 | 2025-09-27 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e6fd760-c715-396f-8637-c8606b93bd45 | -7.72542 | -47.30473 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81d150fc-b50f-300f-9961-41ae553c63d5 | -11.38724 | -45.02855 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0fe8b4b9-5c7a-3c9d-bdf8-9dd4e36f198c | -7.72086 | -47.30078 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38dcf36e-ec63-377c-8d43-12bac41ebd31 | -10.12217 | -45.33435 | 2025-09-27 03:55:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 84597cd0-d037-3f61-99a1-5218a6bbad3c | -12.9761 | -46.25035 | 2025-09-27 03:55:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f744e807-179a-3c62-ae36-e2a6f72568ed | -10.28694 | -45.21051 | 2025-09-27 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0297a06-a5b0-31f9-9109-dc8c61995fe4 | -7.56808 | -42.41576 | 2025-09-27 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3410f2fb-2ec4-3d35-86af-869bc6cf061a | -11.69701 | -44.42355 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ffa64ce-e507-39d2-a4a7-efc3e45ac7c5 | -12.07118 | -45.04875 | 2025-09-27 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c6b898a2-1373-3885-a4bf-1035eaf9c647 | -10.12003 | -45.34676 | 2025-09-27 03:55:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1b87abe-f880-34ff-9e9e-d605a506b15b | -7.61392 | -43.82389 | 2025-09-27 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee68fc03-907f-3383-8658-39cb6b644246 | -11.78812 | -41.20004 | 2025-09-27 03:55:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6517bf62-7e2d-3360-bc92-dc87eb855fb6 | -6.12259 | -45.62577 | 2025-09-27 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4903122c-e637-3411-8635-eef8f2fd326e | -7.71927 | -47.30994 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 59a82b3e-3f67-3a38-a39e-dd510435b59e | -12.294 | -45.65696 | 2025-09-27 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b042ba91-295e-3e8e-bd07-5bc75309054e | -11.35549 | -45.02306 | 2025-09-27 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ac5faed1-260e-3903-877b-894d3de2afa4 | -6.81195 | -44.47558 | 2025-09-27 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b976db31-6298-39ee-9259-69b32d6ebce7 | -11.71375 | -44.41825 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 681a7014-b531-387a-a9ae-7a5082093103 | -8.91332 | -46.09986 | 2025-09-27 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0155608-342e-3b05-af50-6b1e66322236 | -10.47563 | -46.53035 | 2025-09-27 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2cf03b6f-af02-3efa-9896-6da60538d8c2 | -10.28623 | -45.21452 | 2025-09-27 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c7c84bd4-8aa1-3906-8078-16e44163f5ce | -7.05151 | -46.41021 | 2025-09-27 03:55:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a535a842-c9b5-3000-899d-0cd1e9094e8e | -7.7241 | -47.30103 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4a12707-4b1d-3d64-9ce9-d498eea933ca | -11.97621 | -46.5955 | 2025-09-27 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 47d10a51-8b78-351e-bfa5-56da607902f7 | -7.37608 | -47.02854 | 2025-09-27 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5d7f4b0d-9e3a-3e29-802d-9c20b03d1da4 | -11.66161 | -45.34561 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9dc5b5bc-b1b2-3e2f-ad62-bf37df5d6267 | -10.94201 | -44.31019 | 2025-09-27 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ea2d238-a603-3525-b4e9-2a6d5326d31c | -11.54748 | -45.29391 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5e0e70c-3684-349b-94e0-8fb644495846 | -7.58687 | -42.32343 | 2025-09-27 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 95b21e68-158d-3369-aacb-ecca78f7a57d | -10.59559 | -46.28194 | 2025-09-27 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9773ae4-492a-3cc6-a7e4-4f0b7fde1fd9 | -6.49678 | -43.65045 | 2025-09-27 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc3ca459-8a3b-30f2-93ef-b2cf0d1092ce | -12.26249 | -44.06896 | 2025-09-27 03:55:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8dffab41-7870-3482-8452-349508012583 | -11.79208 | -41.19691 | 2025-09-27 03:55:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2cb8a8d7-6e53-35ec-af91-173507f06dcf | -11.38645 | -44.94154 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2cd7a28e-8a29-3ab1-81fd-d1d3c44b75b2 | -12.88351 | -47.09702 | 2025-09-27 03:55:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d597f836-8dfa-3f14-a460-540b4108d7c6 | -9.42326 | -40.72076 | 2025-09-27 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| be13b95d-00de-326e-8197-e5940deff45e | -8.52302 | -44.62046 | 2025-09-27 03:55:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6cc33dd-e027-30ae-84ba-144290a82da6 | -11.36284 | -45.00506 | 2025-09-27 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a112e17-b3a3-317c-bf94-ef13f546fa15 | -7.67294 | -47.42419 | 2025-09-27 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3766ac3-c722-3026-9193-dbea53dbfdea | -6.63515 | -43.82385 | 2025-09-27 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1aef185a-f0ed-31c3-8cf7-88a4a541162a | -11.65449 | -44.2958 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9372ca2-7520-376f-a118-f23ce404ee12 | -12.07053 | -45.05243 | 2025-09-27 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 8f9f2732-f983-374a-9c49-e513f614bdc3 | -8.72922 | -46.68115 | 2025-09-27 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ab55ee0-66a1-374e-947c-548b6c86c2d6 | -11.71619 | -44.40588 | 2025-09-27 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f986d1b-596d-3696-8630-8b7370bce5b4 | -11.38115 | -44.94786 | 2025-09-27 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c9579ab5-93c6-3313-8cb6-6de1b9be6baa | -11.97466 | -47.90438 | 2025-09-27 03:55:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |


[Clique aqui para ver as próximas entradas](README18.md)
