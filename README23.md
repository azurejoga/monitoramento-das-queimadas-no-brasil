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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10583274-4ce0-3bb1-a072-c8873ae426fc | -10.2662 | -45.7979 | 2026-08-08 06:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 92083171-ac06-369e-85ba-99557f6407ec | -8.68539 | -62.87362 | 2026-08-08 06:27:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bc5fb61a-cae4-33fe-8d9d-4f2481af25dd | -8.67873 | -62.87275 | 2026-08-08 06:27:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8a04548-38f7-3d5a-84cf-1ddcbcc4ea80 | -6.28138 | -64.15384 | 2026-08-08 06:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5959586b-1f37-3fe9-80c0-693451ade2ad | -8.68271 | -62.87117 | 2026-08-08 06:27:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 27d286f5-2676-31c7-a18c-e5121b7a83db | -6.28474 | -64.15324 | 2026-08-08 06:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 23df9248-8f6e-3881-b76b-1316d19fa7a6 | -6.28414 | -64.15762 | 2026-08-08 06:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5e53f333-9c26-3cb9-8440-f720db1f1358 | -6.28533 | -64.14886 | 2026-08-08 06:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b95c0d19-9e3e-3a57-9d09-e44f5a561b75 | -6.28797 | -64.15028 | 2026-08-08 06:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2f630215-bef7-3e09-8d8d-c9ec6f509f85 | -6.28734 | -64.15465 | 2026-08-08 06:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2db1285d-3032-3f63-91c1-0293064f0cb6 | -8.68937 | -62.87204 | 2026-08-08 06:27:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e6de0dc-1e15-361d-94d4-615118e24de6 | -6.282 | -64.14946 | 2026-08-08 06:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 46ee7fde-91ab-345d-830f-ca2b209f943b | -4.2634 | -48.2016 | 2026-08-08 06:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| cf3d7487-0ea7-35b7-9a96-0c6b5802d41f | -10.2662 | -45.7979 | 2026-08-08 06:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 4d523b58-0229-33b5-bc40-88ca4507d66b | -4.2635 | -48.1799 | 2026-08-08 06:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| b68b8f31-3ac8-3e86-824f-5a431cbce1ac | -10.2659 | -45.8206 | 2026-08-08 06:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| a862ece5-0de3-3cc5-ae14-b18ae38089f6 | -4.2634 | -48.2016 | 2026-08-08 06:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| d730a42b-ff46-30a0-a675-bb2a8b2d891c | -4.2635 | -48.1799 | 2026-08-08 06:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| b3cbd14f-9bf5-30df-9295-ab5687c03b54 | -10.2662 | -45.7979 | 2026-08-08 06:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 41c610ef-b676-3c8d-8b56-e1b0f01c221c | -10.2659 | -45.8206 | 2026-08-08 06:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 086925a4-5466-37f1-9de0-58abd6b8ef7f | -10.2472 | -45.8002 | 2026-08-08 06:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 64229fce-6ec9-3c7a-9a79-f5970d22c3c9 | -10.2662 | -45.7979 | 2026-08-08 06:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 8fec551a-4ea8-31b6-864a-e2fe5c5f59cb | -10.2659 | -45.8206 | 2026-08-08 06:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 7797a5c3-7da4-3585-8a47-befb3e7159fc | -10.26229 | -45.79744 | 2026-08-08 06:59:00 | AQUA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 48bee356-069b-3400-b9da-17a3a43b9932 | -5.87934 | -51.72361 | 2026-08-08 06:59:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fb720bcb-cf17-332b-815d-8e0d51aec71e | -10.23796 | -45.80964 | 2026-08-08 06:59:00 | AQUA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 40.4 |
| dc308887-712a-3d3a-a366-44e0ca8a7480 | -4.4592 | -47.91408 | 2026-08-08 06:59:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 31b282cf-aadd-3acf-bca3-701078e39e62 | -10.24069 | -45.78841 | 2026-08-08 06:59:00 | AQUA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 8de5fd26-3dac-3766-91b0-7799eb498641 | -4.2662 | -48.17915 | 2026-08-08 06:59:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| ea27843b-4362-3ffb-b3b0-066d30a2e93b | -10.26473 | -45.81607 | 2026-08-08 06:59:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 99458d0d-f4a2-3c7e-a007-fa21813bc1d7 | -4.36804 | -47.76523 | 2026-08-08 06:59:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 50aef75f-b3c1-3814-bc1b-2d456ea92532 | -4.26449 | -48.1911 | 2026-08-08 06:59:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 52c04426-5005-3890-a409-12768453ce54 | -10.2595 | -45.82019 | 2026-08-08 06:59:00 | AQUA_M-M | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 43cd129a-b2a5-3c51-b63f-79593ba302f0 | -3.95739 | -48.12186 | 2026-08-08 06:59:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a5299b61-bedf-3df2-8fdd-47282210997d | -2.82273 | -52.29983 | 2026-08-08 06:59:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 952bb2ef-e7c9-3411-9e8d-0c07d8597ccf | -4.2635 | -48.1799 | 2026-08-08 07:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 42842348-e803-3944-9165-486d143688c2 | -10.2662 | -45.7979 | 2026-08-08 07:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 63.1 |
| fe4e2b46-625d-3856-b38b-0a98bb89f0eb | -4.2634 | -48.2016 | 2026-08-08 07:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| c3a61969-12e4-33fa-b5ed-c57aa51f0323 | -10.2659 | -45.8206 | 2026-08-08 07:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 5c3cd2a5-9abc-32ea-abb6-353dde13ae8f | -14.31295 | -54.99871 | 2026-08-08 07:01:00 | AQUA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a92cdcd4-bcf0-3a0a-91a9-cb0c88dc46c5 | -14.3643 | -54.97481 | 2026-08-08 07:01:00 | AQUA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 25.8 |
| f6342b6b-45c0-32e5-ac03-b364673b371c | -15.16047 | -52.74888 | 2026-08-08 07:01:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 077246f7-eab1-3a70-9ef7-5ed87cdbf51e | -15.16182 | -52.7395 | 2026-08-08 07:01:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4bf0308e-54c2-3aaa-8b47-fd61147d1114 | -14.36574 | -54.96556 | 2026-08-08 07:01:00 | AQUA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| cdd2bd6d-dab0-39b5-a2a6-32531043578a | -15.37567 | -53.798 | 2026-08-08 07:01:00 | AQUA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c3e00128-fc2a-361f-bd0a-64d8f398343e | -14.92353 | -48.24174 | 2026-08-08 07:01:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| ec2ee046-88e6-361f-92f1-4ee6ec80a512 | -13.65055 | -50.29241 | 2026-08-08 07:01:00 | AQUA_M-M | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 9aca3253-489e-3cc0-a4b1-8f5f14a05a9b | -14.31439 | -54.98942 | 2026-08-08 07:01:00 | AQUA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 078b161c-0be0-3a62-aea3-56fcb8f85746 | -14.1626 | -53.99751 | 2026-08-08 07:01:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 41f67d16-78a0-3fcc-bd77-24ccf06ac8fe | -14.37461 | -54.96701 | 2026-08-08 07:01:00 | AQUA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 04565d70-0670-31bb-a859-bf110c12a874 | -14.37318 | -54.97624 | 2026-08-08 07:01:00 | AQUA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 9395ed0d-a808-3a44-980c-52890aded999 | -14.9214 | -48.2592 | 2026-08-08 07:01:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ebc27c55-232d-3a65-aebb-264a1e9faa84 | -14.16124 | -54.00648 | 2026-08-08 07:01:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e8abd1d8-4fe9-3592-b929-4d25a6369ab3 | -14.33477 | -54.98898 | 2026-08-08 07:01:00 | AQUA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3f570457-a1f5-3b21-8f3e-7c25de96b4ed | -15.37703 | -53.78894 | 2026-08-08 07:01:00 | AQUA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| dc29490b-38d5-3666-938f-3eafc03cbdbb | -11.27169 | -55.85822 | 2026-08-08 07:01:00 | AQUA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 087e7896-d2da-3ef6-9a87-46c3f1e7fe1c | -14.93339 | -48.26098 | 2026-08-08 07:01:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 906a1c50-6d9d-33fa-a4c3-c1873974416a | -4.2634 | -48.2016 | 2026-08-08 07:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 9ac0038f-aded-39e0-b316-ff22a90e99f0 | -10.2468 | -45.823 | 2026-08-08 07:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| b69cf159-2143-3d14-a950-558606e3ac27 | -4.2635 | -48.1799 | 2026-08-08 07:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| c6d8925d-11c3-3217-b700-122206dfda5d | -10.2662 | -45.7979 | 2026-08-08 07:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 161.3 |
| ce630315-9fc0-3e35-b6ae-6a090e4b4427 | -10.2852 | -45.7955 | 2026-08-08 07:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 1d7dad86-d463-3eda-b1c1-7997d9bc5e75 | -10.2659 | -45.8206 | 2026-08-08 07:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 250.8 |
| d3df88bf-6318-3ab3-92dc-2f33dda9d3d2 | -10.2472 | -45.8002 | 2026-08-08 07:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 70989c71-9f28-350b-bea0-e94e6bbbf5ff | -10.2849 | -45.8183 | 2026-08-08 07:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 01ed4ac0-4446-38bf-b253-8f7b79349ede | -10.2468 | -45.823 | 2026-08-08 07:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 66.1 |
| c4adf27a-a213-374f-b873-3f11ec3c600f | -10.2662 | -45.7979 | 2026-08-08 07:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| ff76026a-118c-33c6-8020-303b702a157f | -4.2634 | -48.2016 | 2026-08-08 07:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| f7a5e851-26df-316e-b693-bbf26096f370 | -4.2635 | -48.1799 | 2026-08-08 07:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 542fa363-75b9-3e9c-b617-51f50cb0510e | -10.2659 | -45.8206 | 2026-08-08 07:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 275.2 |
| 00b498bb-dff7-3158-b577-3540a3d938b0 | -10.2849 | -45.8183 | 2026-08-08 07:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 3f9068fa-f991-3d8c-8ee2-62f6c634440e | -10.2662 | -45.7979 | 2026-08-08 07:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 2bd973b3-e058-3692-aa7a-450b1bcc2aee | -10.2655 | -45.8434 | 2026-08-08 07:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 1cecef1c-d0e1-3661-b0b8-efee83f33762 | -18.0178 | -50.6101 | 2026-08-08 07:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 9338171a-f140-353c-9baf-57eabe1ce198 | -10.2659 | -45.8206 | 2026-08-08 07:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 235.5 |
| 8e6d8871-6da8-386e-86df-06a30cc9618b | -18.0378 | -50.6065 | 2026-08-08 07:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 9ad56d11-7aba-32d9-8385-21f4111708cc | -4.2635 | -48.1799 | 2026-08-08 07:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| d81f5108-f133-35a0-aec0-be1b80c3e23a | -10.2849 | -45.8183 | 2026-08-08 07:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 04ca2758-5492-3817-a1b7-d8c0997e5737 | -4.2634 | -48.2016 | 2026-08-08 07:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 14bf5377-6e30-3bda-b461-dad47806a059 | -10.2845 | -45.841 | 2026-08-08 07:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 19b1a35f-c741-3278-94e0-3e424a613d4c | -10.2662 | -45.7979 | 2026-08-08 07:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 8927bfb5-5642-33c4-83f1-2ac26eb4d432 | -4.2634 | -48.2016 | 2026-08-08 07:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| cc532b2a-1d0e-31fa-a3a5-00a04a99134e | -4.2635 | -48.1799 | 2026-08-08 07:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| becf763d-1ae0-3115-94a6-33db3815e627 | -10.2468 | -45.823 | 2026-08-08 07:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 13982ff4-0520-376b-9991-55ed8daaf122 | -10.2659 | -45.8206 | 2026-08-08 07:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 307.9 |
| 151d1406-68f4-3bad-a169-5d4fcd6e240f | -18.0178 | -50.6101 | 2026-08-08 07:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 3d77634c-9a17-3a00-b049-3a5a357051de | -18.0378 | -50.6065 | 2026-08-08 07:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 5efce463-a743-300f-80d9-de9971398080 | -10.2849 | -45.8183 | 2026-08-08 07:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 204.7 |
| f6655476-361d-3e31-b5ad-6a5bec57c095 | -10.2655 | -45.8434 | 2026-08-08 07:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 1634a08f-0638-3062-b984-45a6656dd2e4 | -18.0378 | -50.6065 | 2026-08-08 07:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 6baae267-8db6-33d7-847e-218c2a33304c | -10.2655 | -45.8434 | 2026-08-08 07:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 861aeebd-f7d9-393c-888f-1a2ae796ddd4 | -10.2845 | -45.841 | 2026-08-08 07:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 1c6262c2-fa33-3ba0-846b-f8fd0b47793f | -10.2849 | -45.8183 | 2026-08-08 07:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 141.8 |
| ca078a95-c87b-3413-9b02-8995f999496c | -18.0178 | -50.6101 | 2026-08-08 07:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 92.5 |
| b433e07e-e49f-39bc-a235-e6f438ffd5a3 | -10.2659 | -45.8206 | 2026-08-08 07:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 227.6 |
| 09379d2b-1366-3123-b025-c4a9811c8a65 | -18.0378 | -50.6065 | 2026-08-08 08:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 6ba14fd8-5ed5-3021-913c-d7f28d539964 | -10.2659 | -45.8206 | 2026-08-08 08:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 3abe9feb-323a-35da-acaf-4e5b6ff94421 | -18.0178 | -50.6101 | 2026-08-08 08:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| eb74badd-27c6-3b2f-8c68-b8fea5945392 | -10.2849 | -45.8183 | 2026-08-08 08:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 31c6785e-8543-350d-8eef-676606e9490b | -10.2655 | -45.8434 | 2026-08-08 08:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |


[Clique aqui para ver as próximas entradas](README24.md)
