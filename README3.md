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
| 47133573-a6d0-3293-a580-80ad16f0d115 | -8.12344 | -43.14547 | 2025-03-29 04:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 63bb2789-e416-358b-969e-a0246d1bf762 | -8.12747 | -43.14606 | 2025-03-29 04:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b4ae1971-5c8a-3776-9cfb-e8baecc1c6ab | -6.00056 | -44.61589 | 2025-03-29 04:32:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53c3000e-e8ab-318c-9ec1-0d3dc938e315 | -12.08181 | -54.58366 | 2025-03-29 04:34:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73fd6083-cfbf-339c-889c-7c5aad288766 | -12.61111 | -52.12451 | 2025-03-29 04:34:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2651c6a9-f0e6-38a5-be58-25971acc3810 | -9.92839 | -59.90331 | 2025-03-29 04:34:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c10df2e1-e755-3e77-a15a-8e8740bec44b | -15.17834 | -52.29111 | 2025-03-29 04:34:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 409e30db-016b-34ac-a28f-31c5c9d8af12 | -13.95822 | -38.95712 | 2025-03-29 04:34:00 | NPP-375D | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 46935f18-731b-36e3-9fa2-2469d9a92cb0 | -9.26128 | -60.31564 | 2025-03-29 04:34:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b7903bd8-e0ae-3aea-8cf8-42cf021e8851 | -12.61252 | -52.11621 | 2025-03-29 04:34:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55ff3b42-fe41-3b92-862b-edac41b3c652 | -16.35003 | -43.69565 | 2025-03-29 04:34:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 570adaa6-a394-3f6e-a4cd-34b181ae6f27 | -9.2589 | -60.31603 | 2025-03-29 04:34:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2a93ec67-8bdc-3de9-b80d-7b7ed8f3565b | -12.61181 | -52.12034 | 2025-03-29 04:34:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b375da44-2aa4-397f-ab8a-98304195fd4d | -15.56984 | -47.85601 | 2025-03-29 04:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b39e025-9de7-30ea-92e5-437d5a32e5f0 | -11.18666 | -40.51085 | 2025-03-29 04:34:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| eacf5e76-6fe1-322b-9855-31a1fe855d50 | -11.4251 | -54.2986 | 2025-03-29 04:34:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2f730e7-705c-32b8-9b5d-153d522e9910 | -12.0825 | -54.5798 | 2025-03-29 04:34:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04163833-d9bb-3e84-bb16-ae81300e43c9 | -13.95869 | -38.953 | 2025-03-29 04:34:00 | NPP-375D | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6a18487f-7148-3f9a-8b59-e9e68e1358fe | -20.57656 | -56.03984 | 2025-03-29 04:36:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b9cf5db1-a0b3-3bcf-b1e5-fc25c21182ab | -19.14266 | -51.56824 | 2025-03-29 04:36:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf7a7716-d553-3295-92f2-b6e66f9668d4 | -18.53447 | -56.18436 | 2025-03-29 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 2f6ea617-3d90-3ce8-9e17-6aa3bdab681a | -20.57555 | -56.04515 | 2025-03-29 04:36:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4a6a7e75-a763-3c92-a243-7c6b9a8555f5 | -19.8915 | -48.3523 | 2025-03-29 04:36:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d146704-063e-366b-a23a-608078b1b6aa | -20.61105 | -55.70763 | 2025-03-29 04:36:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56c6962e-b3e1-372b-8947-92079a7a707e | -20.44411 | -46.37348 | 2025-03-29 04:36:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9cc624bd-aaef-321c-9bdd-ca53976e2f00 | -20.98869 | -47.35892 | 2025-03-29 04:36:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 06731e0f-19b1-3dc2-a3eb-7cf792db707c | -20.5805 | -56.0407 | 2025-03-29 04:36:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9d04d64f-0c78-3f9b-b174-f932a364bb19 | -20.79205 | -41.12894 | 2025-03-29 04:36:00 | NPP-375D | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dd692856-596a-35c7-8ae7-82b50a48c6ba | -20.98742 | -47.35658 | 2025-03-29 04:36:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f00d3ca8-1b7f-3f40-bb3e-a199b03d55b7 | -20.57949 | -56.046 | 2025-03-29 04:36:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10301972-984b-3305-b7f0-3df90a77ccf4 | -20.15528 | -47.33017 | 2025-03-29 04:36:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 117cc85c-9208-30ff-b616-e010c8eafa8e | -21.48192 | -48.66383 | 2025-03-29 04:36:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a855669-ef40-3c3b-88e5-7ef5cacd103b | -20.57396 | -56.04352 | 2025-03-29 04:36:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e0ac7d92-9148-37bb-8075-a483d5235f34 | -20.57493 | -56.0382 | 2025-03-29 04:36:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 033a4ff1-4f21-31da-a888-4e4d6c12daa6 | -21.12339 | -55.65639 | 2025-03-29 04:36:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ca7aebd-47ce-30f5-8d20-8b30ecb5a4c4 | -22.16061 | -47.37027 | 2025-03-29 04:36:00 | NPP-375D | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1e330150-4b1d-3c78-adb0-e5f8a108727b | -19.96807 | -44.21516 | 2025-03-29 04:36:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 16cf6667-d7f6-39b9-a605-5c5d220ea73e | -18.57531 | -55.53343 | 2025-03-29 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1060201c-bcef-3ffc-a92b-93ec46a4c700 | -21.36834 | -48.54885 | 2025-03-29 04:36:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8c68bd3a-f022-32d0-8975-d79b73f54b0c | -20.99113 | -47.35712 | 2025-03-29 04:36:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 380ca026-2b99-3554-bd01-3683688b02bd | -22.67667 | -42.79381 | 2025-03-29 04:36:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| efd19b72-7939-3877-9620-2c70521d659b | -20.5815 | -56.03538 | 2025-03-29 04:36:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0da75959-bc03-352e-a1e2-d1051d47c7f4 | -19.8801 | -54.6652 | 2025-03-29 04:36:00 | NPP-375D | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29db22af-333c-306d-8967-b083943a6357 | -20.13722 | -50.72069 | 2025-03-29 04:36:00 | NPP-375D | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 101240ef-da88-3950-bb33-bfbc1c1c8620 | -18.53785 | -56.1891 | 2025-03-29 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 429e1496-12ff-30d7-96dc-aaebd5ded1b8 | -18.53858 | -56.18521 | 2025-03-29 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 553af409-ed7d-3755-b67c-52d1e55c58bc | -20.56831 | -55.08552 | 2025-03-29 04:36:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bfda834-03b5-3de8-9049-fedb52681ffb | -15.60131 | -57.34629 | 2025-03-29 04:36:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5fb2de9e-3103-3925-9c3c-54a1ef8edd8f | -16.68217 | -43.88435 | 2025-03-29 04:36:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d2dc32d-b40a-35c3-83ae-32ae04baf507 | -18.38095 | -47.36018 | 2025-03-29 04:36:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e3fa58a-c2f6-362a-b48b-8fd2a954bbed | -17.75225 | -42.8937 | 2025-03-29 04:36:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c6bcd06-393d-3f09-95d0-9f8a44493071 | -15.8581 | -54.12807 | 2025-03-29 04:36:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65ededf7-a68b-3a90-9417-581de5f8bc0b | -17.68619 | -48.63736 | 2025-03-29 04:36:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 02380c32-961f-311d-a74e-cd48a877e5ba | -18.37734 | -47.35967 | 2025-03-29 04:36:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3e95e72-ff73-3926-aaea-28e4bd631eff | -21.46134 | -57.16143 | 2025-03-29 04:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 67213117-1956-37bf-b9f5-d41dec2f9919 | -23.33905 | -46.77298 | 2025-03-29 04:38:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9434080e-3f3a-3587-b6d1-5891fc331cbf | -22.15227 | -56.12389 | 2025-03-29 04:38:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c546dffd-28c7-36b3-a445-22afb4b87466 | -23.44482 | -49.68129 | 2025-03-29 04:38:00 | NPP-375D | CARLÓPOLIS | PARANÁ | Brasil | 4104709 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 496579dd-81b3-3149-b973-5029a569c28e | -21.46213 | -57.15736 | 2025-03-29 04:38:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be270c4d-1077-3be0-a8a0-2ac5461eacca | -23.40605 | -46.55874 | 2025-03-29 04:38:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ec422f7f-325f-3d33-ab9f-3d8e26f3067a | -30.28235 | -50.78429 | 2025-03-29 04:40:00 | NPP-375D | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| 96a12159-96a0-3f78-a9dc-831ea71a4b3e | 3.87343 | -61.50068 | 2025-03-29 04:53:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d73ffce0-8fa8-31ac-8b0d-1ae600b233b3 | 3.879 | -61.49973 | 2025-03-29 04:53:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f92114b-65e1-31b9-b330-0718d80b6d16 | 3.87234 | -61.4932 | 2025-03-29 04:53:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7a04955-9d4a-30e5-a79d-971a83e365db | 3.87845 | -61.49601 | 2025-03-29 04:53:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 08b724eb-9d20-30c1-8abf-bb4f9f3c7a32 | 3.87791 | -61.49231 | 2025-03-29 04:53:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 36ca3776-1114-3d34-891a-0428ff2f532e | 3.88403 | -61.49517 | 2025-03-29 04:53:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91bb7f5e-7115-35ce-b3d5-c44736afbce0 | -5.79279 | -43.62304 | 2025-03-29 04:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ca85014-6558-33fc-8fe0-3d0fa441e0db | 2.01286 | -61.09506 | 2025-03-29 04:55:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 83371d05-8c17-39fd-93a5-221924dcf4c6 | 2.18437 | -61.81333 | 2025-03-29 04:55:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e8350d41-e0e6-3abf-aa53-8fcdd3a9a7e4 | 2.01715 | -61.08781 | 2025-03-29 04:55:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f73bf9b2-5252-37d7-887d-a236b5bed25f | 2.01864 | -61.09749 | 2025-03-29 04:55:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69ac2fb1-e249-39ca-819d-269cf959da37 | 2.23939 | -60.71188 | 2025-03-29 04:55:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4125e900-c734-3fb2-9863-ca8c4a8395fa | 2.01765 | -61.09103 | 2025-03-29 04:55:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d9c53b7-95c3-3648-9864-c5acbc75dafd | 2.24455 | -60.71109 | 2025-03-29 04:55:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15f18566-76ec-38a3-9284-af407e864072 | 1.9463 | -60.83423 | 2025-03-29 04:55:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e19978d3-0b9a-3999-b182-8f79b75baf8c | 1.94677 | -60.83733 | 2025-03-29 04:55:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b537d8b-ae3e-30ab-bb5f-fdd805a7d9bd | 2.01236 | -61.09181 | 2025-03-29 04:55:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 65942e26-ed7e-3079-9375-8bef6b3828bc | 2.0061 | -61.08621 | 2025-03-29 04:55:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d17617b5-5703-37f0-9909-ad5afa107a16 | 2.01666 | -61.0846 | 2025-03-29 04:55:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca705d5b-bb8d-35f1-b667-8e1cda4f52a5 | 2.01187 | -61.08857 | 2025-03-29 04:55:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5f07093f-65d5-3e8a-b5bb-854b3b9a966c | 2.18382 | -61.80967 | 2025-03-29 04:55:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6569e917-27f7-33bd-8a8e-64f9fa7b3048 | 2.01814 | -61.09425 | 2025-03-29 04:55:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ce19a8b-f3f0-38dd-8856-3d443c240cec | 2.01137 | -61.08536 | 2025-03-29 04:55:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0e378be6-d895-38f3-9624-11c80b644221 | 2.00709 | -61.09265 | 2025-03-29 04:55:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 376aeca5-abdc-3e5e-a108-ba635f56f1cc | 2.0066 | -61.08942 | 2025-03-29 04:55:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5887e77f-584f-332b-92a8-3faf66d4c58c | -9.9254 | -59.9026 | 2025-03-29 04:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2fb7c04d-4dae-326a-932e-bc6d5630e51d | -7.23323 | -44.77464 | 2025-03-29 04:55:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e218e84c-3549-361d-8b51-6b21a2e1339a | -9.26075 | -60.3177 | 2025-03-29 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 148b730d-98fe-381a-969a-2381931ac297 | -9.25725 | -60.3131 | 2025-03-29 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8114ce8-0afe-329b-b7df-97e0c9f50551 | -8.13818 | -43.14157 | 2025-03-29 04:55:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ad66854a-7737-3b5a-af78-f3a43d7d63b5 | -5.99406 | -44.61543 | 2025-03-29 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4b81afc-affe-3910-8f53-d2b5b326809a | -5.99997 | -44.61269 | 2025-03-29 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4dba70ce-7807-304d-a8c5-0b9f5960f839 | -5.99946 | -44.6162 | 2025-03-29 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1dc9e98d-38e8-38f6-9170-c1d426af9804 | -6.27266 | -57.91043 | 2025-03-29 04:55:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41a5d636-ee0d-3e27-8390-8b3fa20c4cef | -9.25658 | -60.31696 | 2025-03-29 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68c39cc9-1795-3980-bac3-6ae51ec1af1d | -9.26141 | -60.31387 | 2025-03-29 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d571dff4-35cb-3f3f-8190-f8f487fe82cb | -5.99627 | -44.61649 | 2025-03-29 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8aff962a-a220-398b-862c-d4515c1e4cfd | -5.99676 | -44.61291 | 2025-03-29 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 945d19ec-fc5a-38f8-9312-8d1a5ec92f20 | -8.13751 | -43.1465 | 2025-03-29 04:55:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README4.md)
