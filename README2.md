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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e83a4313-d1f7-330c-943f-fc3458341bfb | -6.74003 | -37.98361 | 2025-03-09 04:08:00 | NPP-375D | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fa5449d9-2dcc-3d7b-8e19-783cb35f92fd | -7.07003 | -44.38045 | 2025-03-09 04:08:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8dda3b7a-6ae3-303f-bb45-f956f66399ff | -13.91158 | -46.11412 | 2025-03-09 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8f6e447-f61e-3654-a939-3ff4d6f33b7b | -13.5624 | -47.93196 | 2025-03-09 04:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 092d55a0-fca6-3eb8-963b-475b62475caf | -16.73149 | -44.21966 | 2025-03-09 04:10:00 | NPP-375D | SÃO JOÃO DA LAGOA | MINAS GERAIS | Brasil | 3162252 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2bb1bea4-5db2-3720-ba42-098e8af3c3b8 | -11.93362 | -43.9988 | 2025-03-09 04:10:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad70b4cb-4937-35b5-88e7-0f79271ff8f7 | -19.1222 | -40.96698 | 2025-03-09 04:10:00 | NPP-375D | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 84c411dd-462b-3213-9669-f3b535bace50 | -19.32501 | -43.70248 | 2025-03-09 04:10:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1943e44-4223-3260-a890-9ebee3c3d0e7 | -19.83213 | -40.11016 | 2025-03-09 04:10:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7d1786f1-40f9-3b66-a448-db29801cddb4 | -15.91396 | -43.9128 | 2025-03-09 04:10:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6df1f3d4-0c7a-3deb-a439-6d5fb5f5510e | -12.4967 | -45.52654 | 2025-03-09 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6151717-c452-3b40-9fc4-fd8afb43dff8 | -19.32003 | -43.69022 | 2025-03-09 04:10:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bd90318-cef6-336e-a291-5d22cc15e419 | -15.56899 | -47.85696 | 2025-03-09 04:10:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a631dbb5-8d4f-311a-83d8-5b33a3540f90 | -14.21201 | -45.77079 | 2025-03-09 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d8439ef-8d7a-3bd9-93f2-981e40c4160c | -15.07757 | -48.9442 | 2025-03-09 04:10:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3746af69-6699-33e6-bc3f-5a53b2fe1e81 | -16.67927 | -43.88572 | 2025-03-09 04:10:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5ca101d-46e6-3036-8521-035c4031709b | -12.00285 | -48.56882 | 2025-03-09 04:10:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fee497f-cf71-34cf-89fb-8824fd03f5f3 | -13.90803 | -46.11349 | 2025-03-09 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57c2943b-142c-345f-9aed-1748de461923 | -17.09462 | -43.80322 | 2025-03-09 04:10:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 102b0d30-a17c-30fc-9103-199d44414258 | -19.12589 | -40.96738 | 2025-03-09 04:10:00 | NPP-375D | RESPLENDOR | MINAS GERAIS | Brasil | 3154309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b613a7e2-1dd4-37b8-9248-c55cd4119a29 | -12.00776 | -48.56565 | 2025-03-09 04:10:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8054dc21-319c-395a-80c4-3192fdfbd9aa | -15.61815 | -43.25718 | 2025-03-09 04:10:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ad5af9e2-e51f-38b5-835a-e9293dc58d8b | -13.08475 | -44.20788 | 2025-03-09 04:10:00 | NPP-375D | CANÁPOLIS | BAHIA | Brasil | 2906105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1c51a41-b94e-3d46-9ba0-d2744a65bccf | -12.00355 | -48.56488 | 2025-03-09 04:10:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91e0bf2d-079d-31f7-9dcd-57f082eb9808 | -19.32558 | -43.69878 | 2025-03-09 04:10:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bca75983-3206-325d-8229-035fcaf4a64c | -11.56971 | -47.62257 | 2025-03-09 04:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9a326b6-de63-3811-851e-e3808e88b74b | -12.50022 | -45.52715 | 2025-03-09 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2687948-651a-32ee-a7d6-9e1b593caeb1 | -15.62147 | -43.25773 | 2025-03-09 04:10:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5562c575-0d61-38a9-8d23-02af1bc0975d | -16.80364 | -43.9583 | 2025-03-09 04:10:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f4dbee3-485e-3b7e-98f4-7134b053ff34 | -12.01196 | -48.56643 | 2025-03-09 04:10:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd61b13f-b32e-38a6-8cbf-ad7eeddbbdc9 | -11.56665 | -47.61664 | 2025-03-09 04:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 660632e4-03fa-3b8a-b8c6-43cbdbdc9641 | -19.83145 | -40.11528 | 2025-03-09 04:10:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0fe35154-7a1c-3580-8cfb-a61a776589c3 | -12.49955 | -45.53115 | 2025-03-09 04:10:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5df30423-8818-3331-a0f4-8a8aa87388dd | -13.90873 | -46.10938 | 2025-03-09 04:10:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54021297-3eb2-3b0a-a4ac-54bfffcd0680 | -21.20663 | -48.55747 | 2025-03-09 04:12:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 329863b4-8c8c-3f47-95fa-2c8346d6a9b7 | -22.11891 | -51.46342 | 2025-03-09 04:12:00 | NPP-375D | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| a33569c6-04d5-3c5d-8a9b-39d2b323dbbd | -22.71873 | -46.12245 | 2025-03-09 04:12:00 | NPP-375D | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| d3d59ef7-a9fa-3b21-b748-195e92de255a | -23.40616 | -46.55825 | 2025-03-09 04:12:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 164dd553-44d4-33fd-9d0e-5bad39718e84 | -23.63054 | -46.42718 | 2025-03-09 04:12:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 0031a53b-54cc-3458-ad55-d2e3db521a75 | -23.592 | -47.43798 | 2025-03-09 04:12:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e33833ba-c077-3d94-b04a-17a9eb30f551 | -22.78485 | -43.75726 | 2025-03-09 04:12:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f3221728-f6d1-3ca1-b5ec-8c064fd83cdd | -23.98294 | -48.91897 | 2025-03-09 04:12:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05c90f96-7b5d-3b43-88ff-37b3c68da3be | -18.8295 | -48.00623 | 2025-03-09 04:12:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 46b788fb-3ce6-3d5d-ba55-906d6f1e27d6 | -20.41469 | -43.55238 | 2025-03-09 04:12:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| df509a11-f287-3ab9-8283-5ff85f4d1552 | -19.96908 | -44.21489 | 2025-03-09 04:12:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7f83ed30-1504-3f4d-a4e5-ec8f9f5166b7 | -20.34796 | -40.36028 | 2025-03-09 04:12:00 | NPP-375D | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6da64ef3-fb69-3602-a8b4-cbb445b1643d | -24.16735 | -46.77764 | 2025-03-09 04:12:00 | NPP-375D | ITANHAÉM | SÃO PAULO | Brasil | 3522109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 79ceebf5-564e-3aff-a514-f7df2e498a65 | -23.03195 | -43.49649 | 2025-03-09 04:12:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 78c2e11b-ed32-3c0b-b01c-29c506cc9750 | -22.71416 | -46.12938 | 2025-03-09 04:12:00 | NPP-375D | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5c70af5d-806c-3c8c-a9b4-306f88ce0d0b | -22.85494 | -42.98194 | 2025-03-09 04:12:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1daed816-9427-33dc-a335-605344c10844 | -19.10221 | -46.91297 | 2025-03-09 04:12:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a00f620c-1db2-3ea9-a33e-6f445433b94f | -22.53968 | -48.81367 | 2025-03-09 04:12:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22043585-a1c0-3956-8abf-0f955326e59d | -21.2744 | -48.5742 | 2025-03-09 04:12:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77096ee5-0d13-3d36-81c7-518aa614615b | -20.90091 | -43.8212 | 2025-03-09 04:12:00 | NPP-375D | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f05c6a8d-1921-3e9e-8a85-aea937d7f35a | -21.14547 | -43.83818 | 2025-03-09 04:12:00 | NPP-375D | RESSAQUINHA | MINAS GERAIS | Brasil | 3154408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3522c997-a113-3bc8-8bff-bc402b208c5b | -22.71478 | -46.12561 | 2025-03-09 04:12:00 | NPP-375D | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 42b481d5-f484-39b5-9e92-cd5fcced110b | -21.18033 | -43.97936 | 2025-03-09 04:12:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 346d051f-a265-32c7-8984-13752a00749d | -20.72532 | -46.16845 | 2025-03-09 04:12:00 | NPP-375D | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 118324d1-076e-3941-982d-8ad21de7d9a3 | -22.71934 | -46.11867 | 2025-03-09 04:12:00 | NPP-375D | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 8ece4ce3-496c-3101-b86f-7acb6feceaed | -22.69845 | -43.34932 | 2025-03-09 04:12:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| df9eeb2d-d5d3-3dae-b0a6-e61b799c4d85 | -20.72145 | -49.43327 | 2025-03-09 04:12:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a308e0e6-0d1a-37d6-89e3-4ae1d854629a | -22.67526 | -42.85666 | 2025-03-09 04:12:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 52737ac9-99fb-3302-bd22-2402908b3afa | -22.7175 | -46.13001 | 2025-03-09 04:12:00 | NPP-375D | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 4bccf784-5e30-3b08-ba4e-2fe2abecd3d2 | -24.1707 | -46.77829 | 2025-03-09 04:12:00 | NPP-375D | ITANHAÉM | SÃO PAULO | Brasil | 3522109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 063803b1-3319-39db-af18-2f4fb79bd3c8 | -20.7253 | -49.43406 | 2025-03-09 04:12:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ebf9b99-579e-354c-b19c-16d5cfa1bd2a | -20.76475 | -46.76822 | 2025-03-09 04:12:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bb8ede5f-cd09-3701-80b1-2d0af18dfb97 | -20.41806 | -43.55294 | 2025-03-09 04:12:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 27dc02b2-584e-3d99-9e67-19ccc4d9c4f1 | -19.10571 | -46.91356 | 2025-03-09 04:12:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16665db5-179a-326b-8461-394f000dba97 | -22.71539 | -46.12183 | 2025-03-09 04:12:00 | NPP-375D | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 8f4baa46-a7fd-316f-9be6-2229b42799d1 | -22.71811 | -46.12624 | 2025-03-09 04:12:00 | NPP-375D | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| fb43e8c9-8b78-381b-8b24-1fa164d51666 | -21.15214 | -48.52941 | 2025-03-09 04:12:00 | NPP-375D | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 232396f0-d4ef-38d2-8bfb-247bcb1945d6 | -21.62619 | -43.46788 | 2025-03-09 04:12:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 06bead36-ae75-38af-b638-08b3b4667007 | -20.66972 | -43.31483 | 2025-03-09 04:12:00 | NPP-375D | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b0f4de75-a624-3b18-a33e-ab74522ef649 | -22.11807 | -51.4677 | 2025-03-09 04:12:00 | NPP-375D | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| dea50c2c-35c6-3ea0-a110-b169cf1b0b95 | -28.65214 | -49.46246 | 2025-03-09 04:14:00 | NPP-375D | NOVA VENEZA | SANTA CATARINA | Brasil | 4211603 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4d544d34-35ba-3a42-b46e-52a8ac89c1f4 | -26.40888 | -53.23635 | 2025-03-09 04:14:00 | NPP-375D | CAMPO ERÊ | SANTA CATARINA | Brasil | 4203501 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 94e4d48e-b703-3039-a1b6-f029c174b30e | -7.04498 | -44.40246 | 2025-03-09 04:29:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56482978-0403-3190-a02b-4caeadbdabe4 | -6.20365 | -44.83193 | 2025-03-09 04:29:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4fab6186-338d-3cad-9959-10ff72500c08 | -7.04433 | -44.40682 | 2025-03-09 04:29:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1283ec0b-194f-38f6-a569-19dabf46eea7 | -11.96248 | -41.42559 | 2025-03-09 04:32:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7ee2071a-a0a5-3b60-b5be-5d8fd2075862 | -12.00913 | -48.56643 | 2025-03-09 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4fd7978c-c3ff-370f-8955-47736b06fd1d | -11.57132 | -47.61966 | 2025-03-09 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3190ebc0-5a9f-3eb2-83d4-ffe247c5a995 | -11.57413 | -47.62382 | 2025-03-09 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4a88a66-bd84-3608-81d3-6f04b9d16738 | -11.56741 | -47.62276 | 2025-03-09 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdd9ad14-8184-3e63-b810-51d95edf6975 | -12.26174 | -45.97556 | 2025-03-09 04:32:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e32cce8a-b5f7-385f-8012-6b62f3d62fd9 | -10.55536 | -46.42216 | 2025-03-09 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4536d09-3c5a-3e71-9576-cc59a41bd043 | -12.00251 | -48.56537 | 2025-03-09 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d874472d-8a37-3cfc-9e75-edc8a081986f | -9.15581 | -43.12327 | 2025-03-09 04:32:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d0bbb45e-1a84-3533-93ac-30165e950277 | -11.57302 | -47.6311 | 2025-03-09 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1b800c1-9448-3ac2-8193-cb344d284fc0 | -8.31426 | -55.11834 | 2025-03-09 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 83f4a95c-860f-3a15-af4a-5008559eeb4a | -11.6257 | -47.57969 | 2025-03-09 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7733898e-dde6-3562-b3fc-296a6d6b5f27 | -12.00582 | -48.5659 | 2025-03-09 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2bae0add-acf4-3daa-b5b4-700b33b49d9b | -11.5646 | -47.6186 | 2025-03-09 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89b956d4-76a5-37f3-b980-0dde36cba89f | -13.91018 | -46.11422 | 2025-03-09 04:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a69ab07-ad08-31ea-8e83-eb44a2aa7d53 | -13.08303 | -44.20661 | 2025-03-09 04:32:00 | NOAA-20 | CANÁPOLIS | BAHIA | Brasil | 2906105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d2bb3aa-f935-3463-8127-a7db4207c928 | -12.49803 | -45.52739 | 2025-03-09 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| de1c231e-38cf-34a1-b036-d85581973bf4 | -11.56851 | -47.61549 | 2025-03-09 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 840a6534-f7a0-34bd-b024-b40ab2e83041 | -12.01245 | -48.56696 | 2025-03-09 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66f3425b-77a8-3117-b178-fb132d00a595 | -13.91079 | -46.10984 | 2025-03-09 04:32:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f414949-134a-3e74-b8f2-118b5abc053b | -13.56161 | -47.93341 | 2025-03-09 04:32:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README3.md)
