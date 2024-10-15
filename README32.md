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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 683a14ca-e817-3d8d-aabe-26a12bf31a47 | -16.68153 | -43.88533 | 2024-10-15 04:04:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7604657a-8f23-3616-af74-d740d75132b4 | -18.25924 | -43.9498 | 2024-10-15 04:04:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d1eef636-d8b9-3699-978c-c527fe7779ea | -18.05952 | -44.31304 | 2024-10-15 04:04:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4dee793f-812f-3a61-bc47-ece791b94b31 | -18.68859 | -43.69501 | 2024-10-15 04:04:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e4054a65-ca01-384a-aa35-b5fcde399769 | -11.88426 | -43.81676 | 2024-10-15 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bcfd1086-7b73-3419-ae9a-2b072abdfcde | -11.0967 | -44.47025 | 2024-10-15 04:04:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6158b07-551f-39b9-83ae-b715747d3ca3 | -11.88143 | -43.81218 | 2024-10-15 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 42285567-15a8-33a1-b8e2-d4fbef0d555f | -12.08279 | -43.89038 | 2024-10-15 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b25142c4-2fb0-3cbe-8ec8-763fac8d7341 | -11.88493 | -43.81277 | 2024-10-15 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cc75087f-7444-3746-95be-88a4b4b170db | -11.13322 | -44.18264 | 2024-10-15 04:04:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e5cabd75-a6c5-37fa-ac29-950240182579 | -11.88776 | -43.81735 | 2024-10-15 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 170da431-a484-374a-a7c2-c76a167855d0 | -11.13392 | -44.17844 | 2024-10-15 04:04:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1ff391c-9a96-31f7-85ef-ce866ee7c80e | -13.27126 | -43.62215 | 2024-10-15 04:04:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e837122-e46c-376d-a03e-02d6e3cad431 | -12.87348 | -44.61057 | 2024-10-15 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| daf84f91-d195-3641-b439-e67c4ea8746d | -12.87277 | -44.61477 | 2024-10-15 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c396a93c-5532-3a8d-a3a2-b7acc8022b36 | -12.86918 | -44.61412 | 2024-10-15 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9d9c36e5-b050-334e-bc4c-b9f4accfe641 | -12.86559 | -44.61347 | 2024-10-15 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e9689b85-12a7-3d22-b0bd-97301035d0ff | -12.86487 | -44.61771 | 2024-10-15 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| daf969bf-ea98-3b83-84a5-a84be5469e23 | -12.86128 | -44.61709 | 2024-10-15 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd6fb64d-46e4-399d-9f3d-7aa68552d5f6 | -12.61413 | -44.78752 | 2024-10-15 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bcaabf5-34e7-35c1-8951-92565967e3a0 | -12.61123 | -44.78255 | 2024-10-15 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d51df2f-c290-3523-8366-034522eca466 | -12.58085 | -44.74172 | 2024-10-15 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c4c73a8-9c0b-35e5-8cce-20d17c08b013 | -12.58002 | -44.74305 | 2024-10-15 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec400be5-c875-314a-880a-6aef79631529 | -12.57722 | -44.74109 | 2024-10-15 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b192b79-e865-3166-b34d-951bc34d29b4 | -12.57639 | -44.74241 | 2024-10-15 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8cad9ceb-fc62-3b16-870a-404e9fb3406d | -12.271 | -44.59137 | 2024-10-15 04:04:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0ae1c57-8ad4-39bf-8400-e2b77f2d8cdc | -14.30997 | -43.86875 | 2024-10-15 04:04:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4a815c69-399d-3f80-b227-2a950bf3dcf7 | -14.09539 | -44.60769 | 2024-10-15 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 120dc1b5-3514-32bd-995f-5b2de201a705 | -14.0947 | -44.61178 | 2024-10-15 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18af67f0-7508-320b-bd72-83a6a9f8b4b6 | -14.09185 | -44.60703 | 2024-10-15 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b67fc59a-db0e-3b85-8ab8-44d476a56de9 | -14.08832 | -44.60637 | 2024-10-15 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c23fcce-4bb8-32fd-9b91-dd04c4189675 | -14.08193 | -44.60099 | 2024-10-15 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a91ddc7c-38b9-36ca-b8fd-032cdc188dec | -14.08094 | -44.78061 | 2024-10-15 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc5a72ef-4ce2-3c93-8fd5-5c8329ee65c5 | -13.82613 | -44.15496 | 2024-10-15 04:04:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b3210d5-5042-342f-83fc-bfac09a9bace | -16.32886 | -45.69037 | 2024-10-15 04:04:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85319cd3-9065-304b-8a3e-c62276e1096e | -16.32809 | -45.69481 | 2024-10-15 04:04:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b11b37a-c37d-3dc6-8794-31a94784b61a | -16.27403 | -44.81952 | 2024-10-15 04:04:00 | NOAA-21 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1bc4087e-0c0b-3b1f-8f2b-cd9ffc4909f5 | -17.93612 | -44.56796 | 2024-10-15 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3069fb5-2a4b-3f1b-8cd6-471dd0b28e76 | -17.2469 | -45.31745 | 2024-10-15 04:04:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6009364-1557-3d8a-8bdc-18605889ca8d | -17.24337 | -45.3168 | 2024-10-15 04:04:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43d4f39a-9d09-30d9-ac1a-b01639125ced | -17.10028 | -44.5797 | 2024-10-15 04:04:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57dff42f-b6d4-3a2d-9cbd-49a5dbd38523 | -17.09962 | -44.58361 | 2024-10-15 04:04:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0b074cb-523d-3df1-8c29-a8a41fc3d35e | -17.0683 | -45.40253 | 2024-10-15 04:04:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3968904c-09ee-3ce3-810f-3c6bf175ce7a | -13.913 | -45.83579 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e947d006-76f8-355c-a8b8-3334c4d5fb67 | -11.91052 | -45.77551 | 2024-10-15 04:04:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f133727b-1fb0-3488-86a9-897d7ea5ef5e | -11.43787 | -45.28905 | 2024-10-15 04:04:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3a19ab95-f41b-3c00-9995-dea982efacbb | -11.05595 | -45.36541 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27a08461-979a-3569-b4cf-9611dc4d5091 | -11.9144 | -45.77619 | 2024-10-15 04:04:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d81908f-deaa-3f06-bd09-78624c762c8e | -11.90966 | -45.78049 | 2024-10-15 04:04:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1f4a5d2-ae9f-3029-a001-526c9df21567 | -11.05676 | -45.3606 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f6c8b75-d3ae-37d1-adbf-84781e8c9d3f | -11.91527 | -45.77121 | 2024-10-15 04:04:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77496b9e-10ad-33e9-8bb0-57d695e0127c | -11.43704 | -45.29387 | 2024-10-15 04:04:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 72915546-30f8-3327-a372-8fe67c904ca0 | -11.0585 | -45.36403 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f729e87-298f-3b4b-83d7-7a183b0a3bd0 | -11.05467 | -45.36333 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5e8a23f7-983b-3d86-8e5f-b4aa8805565c | -11.99936 | -44.95842 | 2024-10-15 04:04:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f0eb116-9753-31a3-9380-c4719f2fc337 | -11.92001 | -45.76693 | 2024-10-15 04:04:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0526a84f-2ed8-3228-a7b5-a3437d99a984 | -11.91915 | -45.7719 | 2024-10-15 04:04:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3dc3a4d5-8493-39b0-b911-bf111230a80f | -13.57955 | -46.58851 | 2024-10-15 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95b33117-c389-30b2-8adc-bfe4780adb1e | -13.57558 | -46.58774 | 2024-10-15 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40f15a19-2e3a-3332-9dcb-128846bf2c6c | -13.56002 | -46.65098 | 2024-10-15 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea03e127-ff6f-3045-b2fd-9022ea2c003c | -13.55837 | -46.6504 | 2024-10-15 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0e048fc-d0fe-388a-8f49-217ee53849b7 | -13.24532 | -46.54729 | 2024-10-15 04:04:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 912e5c99-9760-39e4-9216-9fa4d5c818a6 | -13.923 | -45.82295 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab43a9a7-4c29-354e-a412-5149a8f0926c | -13.92229 | -45.82616 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| adf2435c-46cb-3f38-8f8b-5221b2ca9051 | -13.92219 | -45.82769 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a5c2eae-ec75-33b5-93cf-5ab5ea8aa192 | -13.92145 | -45.83089 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c068c4d8-eb40-33da-a016-e9f351a8fe2a | -13.92137 | -45.83243 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f291e851-f168-316c-aaf2-8d989a18dfc8 | -13.91935 | -45.82076 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f5f6c531-a255-335c-8f15-d7b5c5520a8b | -13.91922 | -45.82227 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 3561709f-7304-3d21-b237-5e7b24ea109b | -13.91841 | -45.82701 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 9ec5506f-b3d7-3703-8b17-5735326dad79 | -13.91767 | -45.83022 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 02ace4df-984c-3829-82aa-8e81a64ca715 | -13.91759 | -45.83175 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 98ca9526-b3af-3a8e-b41a-82b64955b31e | -13.91683 | -45.83495 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| cae4bc6a-955b-3219-9fa0-9fc0dd2c22d5 | -13.91557 | -45.82009 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5b6a0e3f-3d02-3f05-9a35-312ec59ee5f3 | -13.91544 | -45.82159 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 5a446581-14ff-3139-8020-459b54c6de98 | -13.91473 | -45.82481 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 443fd6a1-0014-31d5-8d0d-333d96e09be1 | -13.91463 | -45.82632 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 7d46ea04-8ba4-3855-bde3-27acfe5ed3aa | -13.91389 | -45.82953 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 5789b738-4a9d-30de-931c-a2c6be7f5a81 | -13.91382 | -45.83105 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 39b91069-4699-3ae0-8d86-f6fe83ee475e | -13.91305 | -45.83426 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f9ec7cfe-5e25-382e-af67-2149b71623f3 | -13.91004 | -45.83037 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff865aaf-25ae-39fb-a639-d7d0a68a66d5 | -13.90922 | -45.83511 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 70801e28-7caf-32e8-9499-bfd60aabcba5 | -13.90707 | -45.82495 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b87bf687-f480-3592-9f14-4955f0dd3b5f | -13.90544 | -45.83441 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f0bc5ac9-9bb9-39bf-9d2c-e7fd833da2a3 | -13.90463 | -45.83915 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6a520711-b129-3ae4-9059-c58154a21187 | -13.90084 | -45.83847 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 3c3461db-e01c-3fd5-af29-9a0f32aeb121 | -13.90003 | -45.84322 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 24262386-c493-3d63-aef0-44c19eddc12b | -13.89788 | -45.83304 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 33.7 |
| cdc5215b-1f1b-3bac-b23e-1092e703ec31 | -13.89706 | -45.83778 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 336eda65-1143-39a7-9ead-e1f1b1486c34 | -13.8941 | -45.83236 | 2024-10-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ba60c96-21ff-3941-9543-958b7bf1079f | -15.26077 | -46.03572 | 2024-10-15 04:04:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4b6237c-1cd8-31b2-8a67-7f72978a91dc | -17.23675 | -46.28469 | 2024-10-15 04:04:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc707ccb-c0a2-3c29-ac9f-90195516f494 | -14.11684 | -46.97942 | 2024-10-15 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 036d2388-6ea7-3285-9592-599b550ff283 | -14.11619 | -46.98307 | 2024-10-15 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f4b7ae9-8139-326e-8190-39c0b6707f92 | -10.64045 | -47.84443 | 2024-10-15 04:04:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3ae8ae6d-0689-38a0-a94e-fd1cbdab6864 | -10.62146 | -47.70802 | 2024-10-15 04:04:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ab3aad38-01e0-3d11-9249-7941a08e6cc4 | -10.61618 | -47.71165 | 2024-10-15 04:04:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 83982f75-fb0b-3d4b-b538-84a787fdd323 | -10.60951 | -48.01372 | 2024-10-15 04:04:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28b4c9ef-464c-3092-984f-d88e156929a1 | -10.60491 | -48.01295 | 2024-10-15 04:04:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cde2dada-6b03-3e05-86c1-6efefb01aad6 | -10.45432 | -47.85257 | 2024-10-15 04:04:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README33.md)
