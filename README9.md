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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27e7f218-445a-364c-834b-2605cedc7db3 | -17.28424 | -42.65052 | 2025-05-22 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed200a65-ba0b-3ee7-92de-af19c4b85fce | -20.60836 | -48.86749 | 2025-05-22 03:57:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| be2f9763-c802-3c02-ae27-ebdfed02d559 | -17.28023 | -42.6537 | 2025-05-22 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f1e67c2-20c3-3b2c-a28e-3fde238a40f6 | -18.81385 | -48.52457 | 2025-05-22 03:57:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a32c631e-7a91-3e0e-98e9-b33c14034d78 | -17.2717 | -42.65685 | 2025-05-22 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2540acf9-8adc-361c-9b65-4d0f86bcba5f | -17.26831 | -42.65626 | 2025-05-22 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 329639f9-9e58-3f08-a73c-9af991a9db6b | -17.61407 | -54.17448 | 2025-05-22 03:57:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6cd955f4-be39-3411-9af5-b705803de696 | -19.11533 | -52.69557 | 2025-05-22 03:57:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b3477e40-6a95-372d-8e70-917e570f361a | -18.35095 | -46.48602 | 2025-05-22 03:57:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e68f8c4c-e1de-3668-8c91-c7e0a1a3d2bd | -19.7352 | -54.51351 | 2025-05-22 03:57:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 50874a84-40c0-351c-b470-088c32a83d27 | -17.27345 | -42.65255 | 2025-05-22 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f228bb63-71f3-3409-9438-584cda6bd224 | -14.03006 | -53.37457 | 2025-05-22 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab28b315-a6a9-3f6c-b6fc-d1b8238d49fe | -21.21856 | -48.61134 | 2025-05-22 03:57:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| cfb7517a-9111-3403-b41c-f4bf1dd0ed08 | -17.27282 | -42.65633 | 2025-05-22 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6019c74c-d68b-38e6-a11b-213b478f80d2 | -17.61168 | -42.55634 | 2025-05-22 03:57:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f3237fa-777e-3f6d-9356-b914f43ede85 | -20.15305 | -43.67458 | 2025-05-22 03:57:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 378923cb-8e82-37e5-b05c-718a6e787119 | -16.68177 | -43.88313 | 2025-05-22 03:57:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce592669-3a43-3368-b9d7-2a50ad567bec | -15.85084 | -46.48668 | 2025-05-22 03:57:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7eb35fa5-bb0b-3b4e-a3ea-e4d9f999196b | -14.03672 | -53.37601 | 2025-05-22 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 399aa2de-738a-3b96-b5a7-c75aa3208b96 | -17.27684 | -42.65313 | 2025-05-22 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8451bea4-e4da-344b-a592-6ae09809c412 | -20.6074 | -48.87236 | 2025-05-22 03:57:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| b7046672-0b6b-3227-9530-4135ebecd6a5 | -22.16372 | -42.94276 | 2025-05-22 03:57:00 | NOAA-21 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 177bd59f-280e-335a-8db8-ff16c3206c06 | -17.68989 | -43.276 | 2025-05-22 03:57:00 | NOAA-21 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| b16d090b-b70a-3a5b-801b-e43f1183c47a | -13.5456 | -43.6762 | 2025-05-22 04:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 1ded0bcf-16f6-3ffc-b7fd-fab62e3f669f | -12.2943 | -52.4995 | 2025-05-22 04:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| ba84aa20-dcdc-3bec-b23c-64949f31b896 | -11.5719 | -47.4521 | 2025-05-22 04:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| d1b50150-8236-3047-9a1c-c5f8273bd52e | -11.5528 | -47.4546 | 2025-05-22 04:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| fed07299-3048-303d-b504-a1499bc8d5b9 | -20.94648 | -56.58932 | 2025-05-22 04:00:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 25.3 |
| fe0f84af-1135-30e3-ae10-4d86bafe5854 | -23.29333 | -51.58724 | 2025-05-22 04:00:00 | NOAA-21 | SABÁUDIA | PARANÁ | Brasil | 4122701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 153f6058-92b7-3999-9433-2daf8f4643ed | -20.94462 | -56.59661 | 2025-05-22 04:00:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 18.7 |
| e6f0996e-8213-3ba9-93cc-b4a33da0188b | -20.94829 | -56.58221 | 2025-05-22 04:00:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 25.3 |
| b37e0d82-9dce-361e-81dd-403847853328 | -22.9535 | -49.10656 | 2025-05-22 04:00:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35cd8abb-28d8-3c38-a997-41bb41f79f96 | -23.78211 | -45.56144 | 2025-05-22 04:00:00 | NOAA-21 | SÃO SEBASTIÃO | SÃO PAULO | Brasil | 3550704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0a890a23-47df-3c4a-a372-a889cab733a2 | -23.31294 | -49.29377 | 2025-05-22 04:00:00 | NOAA-21 | TEJUPÁ | SÃO PAULO | Brasil | 3554201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e40620cd-7aff-36ec-bd26-6f494ed0f650 | -20.95333 | -56.59158 | 2025-05-22 04:00:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 25.3 |
| bee0ffff-5d6a-33bd-88a3-970defd6ac0b | -22.54201 | -48.81554 | 2025-05-22 04:00:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 149531a0-310a-3cd4-90b9-b9c18554aac6 | -20.94678 | -56.59777 | 2025-05-22 04:00:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 41.3 |
| d5e6860b-d86d-30d6-8bb3-1125fda1fd29 | -20.95032 | -56.58352 | 2025-05-22 04:00:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 02e41761-be6d-3bdc-a837-469f1d694975 | -20.94856 | -56.59059 | 2025-05-22 04:00:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 894cac72-1622-33b0-9828-592ceada7887 | -23.33777 | -46.77367 | 2025-05-22 04:00:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5f7aebcd-1d5d-33b4-8b92-4bd33a5d7979 | -23.40514 | -46.55792 | 2025-05-22 04:00:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2f4a6bf1-b724-3a0f-a06e-1beb76aea22d | -20.95154 | -56.59858 | 2025-05-22 04:00:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 811ae759-9081-3d53-bcce-59ec12d78df8 | -29.77667 | -51.17828 | 2025-05-22 04:02:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| e2f0bac9-3d95-3df3-8c6f-3130d9d36134 | -29.77767 | -51.17353 | 2025-05-22 04:02:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 5e9eda0a-b89d-3d9a-8256-d66b593e8667 | -12.2943 | -52.4995 | 2025-05-22 04:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| a7526cac-bb7f-3421-99be-4b008d426b8e | -11.5528 | -47.4546 | 2025-05-22 04:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 316b045d-c0cf-3a19-9b86-1b764bf72188 | -11.5719 | -47.4521 | 2025-05-22 04:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 6fdfdaf5-cbfe-3fd9-b041-d084d9f34242 | -13.5261 | -43.6797 | 2025-05-22 04:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 2c67c04f-3b73-39b7-8609-741232d277a1 | -2.18936 | -47.05101 | 2025-05-22 04:19:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f66930bc-8fcc-31c4-9aeb-e631c58d0f2c | -5.07009 | -37.71643 | 2025-05-22 04:19:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6c3df6a1-17df-3556-a135-922d95d27e63 | -11.5528 | -47.4546 | 2025-05-22 04:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 185cea3e-1c7e-370c-b71f-738174f09180 | -11.5719 | -47.4521 | 2025-05-22 04:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| e1bd1ce9-3eca-35f3-9d7a-85af1b5c291c | -10.98884 | -42.18311 | 2025-05-22 04:21:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3b3e8fbc-5ca8-383a-ad01-9daea63889bf | -11.56769 | -47.45017 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c88f76e9-518c-33bb-a4fe-2e00cfcf12c7 | -9.79354 | -48.26217 | 2025-05-22 04:21:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0891af2-d52d-3c0b-9810-537be88e51b4 | -7.57968 | -45.86164 | 2025-05-22 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b32d99d4-c2ad-39c4-92b2-36c0422465f6 | -12.83761 | -47.3959 | 2025-05-22 04:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a43cc10-5c9f-3384-9b6b-19c504fc5b59 | -8.48067 | -49.60913 | 2025-05-22 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1bc8c61-14cb-361e-9c2e-8f286356671e | -7.24024 | -44.71545 | 2025-05-22 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46ee6b25-76f7-383e-aa4d-7b3b74fb8f32 | -11.79509 | -49.33489 | 2025-05-22 04:21:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 611c9118-989b-3317-bbd1-27c01b653608 | -11.64579 | -48.1047 | 2025-05-22 04:21:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fab64c85-52f7-3b1d-aad3-fa93d332d385 | -13.5188 | -43.69775 | 2025-05-22 04:21:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 592c9a02-67d8-3a77-9b12-e0bc18e50337 | -11.57556 | -48.37745 | 2025-05-22 04:21:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1308eeb-9205-352c-8dbd-99884bf18f65 | -10.30498 | -47.02894 | 2025-05-22 04:21:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70862888-0e0e-3a88-a769-c136d08a39b9 | -12.35342 | -49.97614 | 2025-05-22 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 592386a8-2c73-35e2-a1e6-24b6d8289684 | -10.93434 | -55.3138 | 2025-05-22 04:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.1 |
| cb78315b-215f-35e2-a941-ac22187c18a4 | -11.97405 | -44.15805 | 2025-05-22 04:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4bbb3726-e981-3dd4-afc8-ee45586a2a0e | -13.51526 | -43.69721 | 2025-05-22 04:21:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34cf4eef-d03c-3746-9ae2-61964c664b9e | -12.34185 | -49.97675 | 2025-05-22 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 829eda49-ce63-36a8-bf7d-925503a5cda2 | -12.34638 | -49.97282 | 2025-05-22 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a7f22ad-d22f-3f7d-ac48-2af9256e6b93 | -13.53658 | -43.67556 | 2025-05-22 04:21:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 54d447cd-f8b5-379a-a503-dc25528ba6be | -11.56608 | -47.43854 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5bb8439b-2fa1-3098-a97f-dee210ce77d1 | -13.50463 | -43.69558 | 2025-05-22 04:21:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7da01b36-6bac-363b-9d46-8c97026d48a4 | -12.3384 | -49.97355 | 2025-05-22 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0ebc0901-75f3-3633-9e4f-c3aec9985d15 | -9.29075 | -57.55436 | 2025-05-22 04:21:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 02799d75-9e96-3348-84b1-03e36eb73cb1 | -11.59638 | -47.6182 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| da0b1e99-4ef8-37af-b18c-8a3c49ee4cd7 | -10.83152 | -56.95554 | 2025-05-22 04:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66aa19b3-23d6-3c97-8690-55b2e99d40c5 | -12.35718 | -49.97681 | 2025-05-22 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b70f7b4-1ccb-3f51-8f9b-2b64f96f8e3c | -11.5763 | -47.86979 | 2025-05-22 04:21:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c2515ca-baaf-33f0-9dfc-0fc1d35c4b26 | -11.79585 | -49.33053 | 2025-05-22 04:21:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| edf44d5b-e497-3acb-8ec3-ba89b103bcc8 | -9.04432 | -47.02744 | 2025-05-22 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fdc5380-6040-3e2d-bdd1-c42e1002566c | -11.57485 | -47.45098 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1a3dd0ac-e8ed-32ce-b001-605e3c88faf3 | -12.84493 | -47.39341 | 2025-05-22 04:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0befc38-12aa-34e7-ac1c-93b9a484913a | -11.55631 | -47.45581 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ae954c8f-924e-392a-bade-51ce95947059 | -11.79875 | -49.33552 | 2025-05-22 04:21:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa9576b1-3903-3118-8559-9b599791622f | -11.56429 | -47.44958 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 52f8d246-6c6a-3141-b9cb-3ee2be72371c | -9.04553 | -47.02007 | 2025-05-22 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 11969180-36dc-31b3-80e5-14a62884615c | -10.65662 | -44.4972 | 2025-05-22 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2de094e7-3dfe-3157-bc1c-adea7cf12c45 | -11.60661 | -47.61997 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1503e322-41d7-35c2-a2a3-a190d3f976ec | -9.67597 | -50.95225 | 2025-05-22 04:21:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17c6e80d-80ac-3c38-9e36-9b20f3609918 | -11.86516 | -52.27484 | 2025-05-22 04:21:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24218e67-947e-3b7b-aefb-51c9688b0d1a | -12.34296 | -49.96962 | 2025-05-22 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55eb53da-6978-30ba-a97c-6018eb652bec | -10.68611 | -57.59988 | 2025-05-22 04:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ba7de40-ab3f-3cc3-ab09-bc197cf50341 | -11.55571 | -47.4595 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0f2bd42d-8d67-3d4d-9752-2ede32bb4a6d | -7.278 | -43.92707 | 2025-05-22 04:21:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 35b4533c-7edb-3f2e-a2d5-e57d9690bd9e | -10.37079 | -47.97645 | 2025-05-22 04:21:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2ffda90-fdc1-3a85-a5f0-58655663ff83 | -11.56992 | -54.56079 | 2025-05-22 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe2cb923-be2f-3f1d-bfea-cc916cb5aa17 | -10.34263 | -51.69064 | 2025-05-22 04:21:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72c98e8f-b69d-337f-8f34-d309612db4f2 | -11.56268 | -47.43798 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dd464c45-8903-38a2-881c-d74a8d06dc3f | -11.5597 | -47.45638 | 2025-05-22 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |


[Clique aqui para ver as próximas entradas](README10.md)
