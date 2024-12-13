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
| a95f2ffd-2949-383d-b673-ba37752e2952 | -11.1959 | -53.8348 | 2024-12-13 03:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| d87a8f13-3404-3071-848a-12194889a78d | -11.1962 | -53.8142 | 2024-12-13 03:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| b1b0c49d-8e34-3627-8967-5f12656e6cfe | -5.2108 | -43.3067 | 2024-12-13 03:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 6356e42f-e004-369e-894b-7645b737e242 | -0.94189 | -46.92216 | 2024-12-13 03:53:00 | NOAA-21 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 796571d3-7f26-3333-81e7-2b6b0e5bcc71 | -0.75344 | -47.75788 | 2024-12-13 03:53:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dcb76441-ea28-394d-89e0-7be758e57034 | -3.1403 | -40.05244 | 2024-12-13 03:55:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| f912ab95-07f8-3fba-931f-9fcae47a322b | -9.71231 | -37.3579 | 2024-12-13 03:55:00 | NOAA-21 | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6340b36e-28d1-3b5c-82f4-f926b6df26a1 | -5.73286 | -39.53437 | 2024-12-13 03:55:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 9db49145-1502-305f-97e2-ac4ebb551234 | -4.18676 | -42.42406 | 2024-12-13 03:55:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1dffb3e8-64bd-31a8-9740-2a053cfd03b6 | -3.28732 | -45.59059 | 2024-12-13 03:55:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b313fed9-2a74-31ca-afab-1b39b9090470 | -9.28758 | -39.27414 | 2024-12-13 03:55:00 | NOAA-21 | CHORROCHÓ | BAHIA | Brasil | 2907707 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 26196020-3e67-3136-994e-003ce5a6c1aa | -5.48489 | -40.52131 | 2024-12-13 03:55:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 809b7e65-25a7-3675-bf6f-9ec2db5b4c29 | -5.55277 | -44.69231 | 2024-12-13 03:55:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56795923-e151-3e07-a6e9-8d05d562f722 | -9.07913 | -36.12959 | 2024-12-13 03:55:00 | NOAA-21 | SANTANA DO MUNDAÚ | ALAGOAS | Brasil | 2708105 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4d217f3b-3793-39c1-a4f8-09df7a621aff | -4.3865 | -42.14794 | 2024-12-13 03:55:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a0641c11-e5d2-31db-8548-6a8cad93e32e | -5.21468 | -43.30108 | 2024-12-13 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3773062a-59de-3865-95ea-d1976d7bcdc0 | -2.39539 | -47.03101 | 2024-12-13 03:55:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 390831a0-ba43-3a88-983e-b17bf50c6f90 | -4.6561 | -43.81754 | 2024-12-13 03:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 22d2ab7e-2098-34e4-b0bf-2363dcb5e375 | -7.51476 | -37.44083 | 2024-12-13 03:55:00 | NOAA-21 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a201da5d-4fe2-3c1a-a271-23f9de783dad | -5.82725 | -40.3557 | 2024-12-13 03:55:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8a35135f-b463-377d-9c92-708d77367463 | -5.21181 | -43.2935 | 2024-12-13 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 36454fa3-4447-3106-a935-8c4fc73e0bb9 | -1.62304 | -46.66991 | 2024-12-13 03:55:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 769055ed-b558-31b3-867e-ab4e1f9418ab | -2.72974 | -47.88935 | 2024-12-13 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c528169b-8fd8-3828-8abe-429a99daca29 | -6.05603 | -44.04478 | 2024-12-13 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 203e9156-8b61-3b85-a6af-20191847fa12 | -10.20358 | -36.3717 | 2024-12-13 03:55:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 8e75b4fb-735a-35e7-96d5-58b5bb0d913b | -8.26973 | -48.03082 | 2024-12-13 03:55:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 18db7fe8-1f50-34b8-94a6-e6305f19e5ae | -4.97563 | -44.49184 | 2024-12-13 03:55:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6620ffd1-e648-3efd-9749-3217600f8561 | -6.92956 | -43.54613 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b544fda4-3635-3550-bdc6-c5b24ed05dc8 | -7.42997 | -44.73071 | 2024-12-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eea43bd7-f374-3af2-bddb-4020229edde4 | -5.21722 | -37.28341 | 2024-12-13 03:55:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 59cc3380-94c3-3976-8e5c-64a2b637d5bd | -3.69116 | -42.60227 | 2024-12-13 03:55:00 | NOAA-21 | MATIAS OLÍMPIO | PIAUÍ | Brasil | 2206100 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b84fa6c7-d4b1-3bb5-9d7d-301f989b03d1 | -6.92065 | -43.52615 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9ea8dfdf-00f5-3f79-b737-9312ab08b0e2 | -6.91366 | -43.5435 | 2024-12-13 03:55:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| faeafe7e-5783-3dbb-af7f-1c2da00b0336 | -3.32299 | -45.70611 | 2024-12-13 03:55:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1cbb50b2-0b7e-366d-9078-1e83d0c43254 | -4.67908 | -38.59926 | 2024-12-13 03:55:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6cd6241d-ea43-33a6-a880-0c07feb96609 | -4.7715 | -44.42002 | 2024-12-13 03:55:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63d022a1-ace2-330e-b14e-6d218d8be181 | -4.64022 | -42.87879 | 2024-12-13 03:55:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9d2f8487-8fbc-381c-a196-71dbc547f13d | -3.63793 | -51.13991 | 2024-12-13 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 27479d2b-5530-3c96-8836-a27ed48607dd | -5.19975 | -43.29165 | 2024-12-13 03:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 798911eb-3f1a-3a6e-a09b-c8d11978268a | -4.6553 | -43.81686 | 2024-12-13 03:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 93acdb84-2960-3bd7-9c03-531926229b37 | -8.16799 | -43.82059 | 2024-12-13 03:55:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 410def0b-de88-329f-b44c-f25651e3cc7c | -5.96446 | -43.36802 | 2024-12-13 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a3897cc7-e180-3f57-8f77-cd8d3a2de3dc | -8.65044 | -35.96965 | 2024-12-13 03:55:00 | NOAA-21 | PANELAS | PERNAMBUCO | Brasil | 2610202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fe348b6a-e251-3098-84e3-0cc8979fc539 | -6.1172 | -43.95907 | 2024-12-13 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57ce1e92-a501-32bb-8fb3-c51f0161473b | -4.6519 | -43.81689 | 2024-12-13 03:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 674b5913-27cb-33c6-bcfc-12b294b9e3a7 | -7.43061 | -44.73178 | 2024-12-13 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c99a7f97-c49d-3902-b7b3-27df17d933f8 | -3.26815 | -46.91816 | 2024-12-13 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 173dcbd2-9666-31d9-9a6b-05886db5b548 | -5.45638 | -44.81071 | 2024-12-13 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 82e7c66d-2caa-392f-b4c0-a7968b70286c | -6.76514 | -44.82883 | 2024-12-13 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7683b286-ec37-3450-ae49-8dc3df0bab94 | -4.12515 | -48.74814 | 2024-12-13 03:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f1fd0a0-4268-3df1-9b67-4951f0ed9fa0 | -6.91893 | -43.53645 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2f0cc5aa-de05-38f9-a0d2-57534ec3d32f | -3.36003 | -42.28279 | 2024-12-13 03:55:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3822442b-8eb9-3eb6-9e35-275b69856ec7 | -5.20837 | -43.28941 | 2024-12-13 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 50be3148-0c99-3195-9d2e-d1f12f64772c | -2.50505 | -46.84723 | 2024-12-13 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d05d0db0-7772-3782-8d09-4b619ea3714d | -3.04428 | -44.47916 | 2024-12-13 03:55:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9d1c921f-d429-3d11-87db-356d821be77c | -5.4571 | -44.80635 | 2024-12-13 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d776af44-71ea-3914-ad91-ac444b184ab2 | -8.4804 | -35.3896 | 2024-12-13 03:55:00 | NOAA-21 | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 58e56e28-842f-328b-9114-8011d03f52ee | -3.38027 | -42.33076 | 2024-12-13 03:55:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2e947d77-44d5-3020-ab3c-3fa1daa11b42 | -4.78134 | -48.50809 | 2024-12-13 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| df697d91-0fc5-3d21-bcad-b5e5929ecbbe | -7.36164 | -46.23201 | 2024-12-13 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d3d93d32-a2f2-3095-9b74-7f9faead8361 | -8.64685 | -35.96912 | 2024-12-13 03:55:00 | NOAA-21 | PANELAS | PERNAMBUCO | Brasil | 2610202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a9e0e14c-4549-3889-a4a5-46b570c8a784 | -7.29196 | -39.61495 | 2024-12-13 03:55:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ac3748de-742c-3bbf-b1c7-6fa55b9b4941 | -1.62249 | -46.67324 | 2024-12-13 03:55:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 93c9ab18-5b3d-35f5-8849-4d5273957e7e | -4.45994 | -43.74302 | 2024-12-13 03:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f577e9d-7249-3fc9-8d7d-7df3e07821e7 | -2.39189 | -47.0309 | 2024-12-13 03:55:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1c025e9-d3b7-39c9-bada-cc989d0045c8 | -3.63101 | -51.13907 | 2024-12-13 03:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 17c47ba3-6ff0-30e5-8485-dd355a2de7c3 | -6.93878 | -43.53978 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 103d3174-3525-3aa1-913b-df345a9dd6ec | -4.16355 | -42.44512 | 2024-12-13 03:55:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 5697e6c4-dcd1-3392-9ee2-82035ae397ba | -6.92898 | -43.54958 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33d28c15-4116-3678-8dab-5d7c979d8be8 | -5.2388 | -45.13562 | 2024-12-13 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6fd1ebd1-316d-3e24-af5b-a6617538b2d7 | -3.3639 | -42.28339 | 2024-12-13 03:55:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9a11f880-4bf9-32cc-a909-b62f6759ab79 | -7.57982 | -47.11615 | 2024-12-13 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e878a70-c0b7-3b89-941b-2f123134b267 | -7.92337 | -35.19161 | 2024-12-13 03:55:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 921a2ca9-5291-329a-831b-db87f784ebef | -2.4698 | -49.03092 | 2024-12-13 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 489a2e6d-8d28-3832-a019-8dd56d952942 | -5.98633 | -42.3129 | 2024-12-13 03:55:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7212e5fa-22ac-3484-b7f1-779cffd8c2e9 | -9.47184 | -37.06772 | 2024-12-13 03:55:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 3909af41-a147-3fac-afb3-78ea8140c9d0 | -7.25314 | -39.75338 | 2024-12-13 03:55:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| cf360d98-4d15-3428-b971-5c25dcd44171 | -3.36467 | -42.27856 | 2024-12-13 03:55:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3fa9f3f-a70d-3281-901e-e6e3e4dc69bf | -5.62808 | -44.83661 | 2024-12-13 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 29cc9797-637f-3be6-8be3-2e6078e3b732 | -5.08643 | -42.56718 | 2024-12-13 03:55:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d194150c-ce53-3cee-9d55-1b1fd127ec5f | -3.83231 | -41.56929 | 2024-12-13 03:55:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 39dd43c4-f715-3e31-9351-f898ae34b1a7 | -6.93353 | -43.54678 | 2024-12-13 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1be83629-f110-3c67-9e82-271351e1840e | -3.03825 | -44.47535 | 2024-12-13 03:55:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06cc11d0-ad3c-36c3-9df4-69d77fa58e9e | -5.20779 | -43.29289 | 2024-12-13 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 2fd39699-a355-3125-95af-9bf33ae3dba1 | -5.42486 | -44.86378 | 2024-12-13 03:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 199b1eb3-40eb-3825-a698-6b266781945f | -4.24364 | -41.92727 | 2024-12-13 03:55:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 330451f7-37c8-31b8-a8c7-98b99fda79fb | -3.03978 | -44.47845 | 2024-12-13 03:55:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f6a4a6d8-e3a3-3e40-bb48-cbadf754cf54 | -3.50207 | -39.31512 | 2024-12-13 03:55:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cb87a8bf-1610-3b6c-ac28-3640858e792a | -6.76336 | -44.8299 | 2024-12-13 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7e605ad6-57eb-3929-91a0-939d7b1fea40 | -2.37227 | -48.28376 | 2024-12-13 03:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 048e2be5-a9b9-3d50-8de3-573fa5953220 | -3.37639 | -42.33012 | 2024-12-13 03:55:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a2ac942e-1c21-3e4e-bca3-4183f9adc68b | -5.97713 | -45.36808 | 2024-12-13 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd702ffc-6bbc-35ec-ab52-cdeae0150876 | -5.44857 | -45.40176 | 2024-12-13 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d90804e-4f50-397f-9633-086b97305d2a | -6.62228 | -39.17997 | 2024-12-13 03:55:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9d40a2e3-3889-380e-84cc-395e3e22fa61 | -3.2508 | -42.41579 | 2024-12-13 03:55:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8a3f9ab0-9152-36d2-bf57-ed1471555da4 | -4.51386 | -42.05826 | 2024-12-13 03:55:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d7784dc0-d879-3d7b-ad68-14dd3a3b3f66 | -4.86779 | -38.43856 | 2024-12-13 03:55:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 94284221-773c-3a2f-92d1-32b897930474 | -9.0827 | -36.13025 | 2024-12-13 03:55:00 | NOAA-21 | SANTANA DO MUNDAÚ | ALAGOAS | Brasil | 2708105 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4e8d7d8e-acbf-31ac-b5fe-431d409e1646 | -4.96074 | -38.58362 | 2024-12-13 03:55:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d284262c-b381-388d-98b2-ec72fbaa37a3 | -7.14776 | -41.46692 | 2024-12-13 03:55:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |


[Clique aqui para ver as próximas entradas](README11.md)
