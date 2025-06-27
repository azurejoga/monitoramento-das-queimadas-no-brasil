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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5cb3bb1-66f8-3aed-8f38-137c42c420f5 | -15.57096 | -47.85459 | 2025-06-27 04:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 295e1805-0468-3745-97e5-01389e3284bd | -13.75935 | -52.31601 | 2025-06-27 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0d4e134-0380-34d9-bb6e-406382aa23b8 | -20.92524 | -45.78968 | 2025-06-27 04:51:00 | NPP-375D | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 632467b2-8074-3226-afd7-ce45af086e2d | -13.93622 | -54.4993 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ee5097d-fced-3848-91ed-555d03f39c7c | -12.49982 | -58.35043 | 2025-06-27 04:51:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3acfe4e5-7f85-38de-9601-558f552361f5 | -12.50405 | -58.35126 | 2025-06-27 04:51:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7e7d38c-d77f-3c5e-bec5-12f5d58584ce | -12.59479 | -57.87566 | 2025-06-27 04:51:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9722f2f-1b1c-3dab-a6cd-0f0df69a8ffa | -21.10931 | -43.81088 | 2025-06-27 04:51:00 | NPP-375D | RESSAQUINHA | MINAS GERAIS | Brasil | 3154408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6f030fa9-1ec2-3488-aa79-a55a7ace468c | -18.66284 | -55.75041 | 2025-06-27 04:51:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 65afb578-6ca9-37b9-98eb-ce755b705e04 | -14.38052 | -50.32517 | 2025-06-27 04:51:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df57e9c8-63de-3f7f-9a05-126853a4d5ec | -18.94956 | -39.90668 | 2025-06-27 04:51:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 38059e2f-771c-3522-bb23-cc69d91fc832 | -14.44494 | -48.86855 | 2025-06-27 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dffe18c1-0f35-3b40-a957-5bb0fe0086af | -13.9415 | -54.48858 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d4b32147-ea5d-3571-bd6a-ebfff88f2026 | -16.25129 | -46.29213 | 2025-06-27 04:51:00 | NPP-375D | URUANA DE MINAS | MINAS GERAIS | Brasil | 3170479 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e6294743-aafd-3ab8-8697-908d0cc1cc8b | -18.65877 | -55.75365 | 2025-06-27 04:51:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d8d707b1-93cc-3c3e-b9ce-ea3caf39c12e | -14.01765 | -54.49412 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 302980c3-e586-34cd-9e3e-e73d432ccb03 | -16.70551 | -49.35691 | 2025-06-27 04:51:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b44b1c5-f9a6-3f90-9fed-972efc7ada1f | -20.47795 | -53.67617 | 2025-06-27 04:51:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c8215aa-8df7-3029-9738-890f7e3fae19 | -17.0453 | -43.77641 | 2025-06-27 04:51:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88ef6c79-e055-377b-bc92-a0c64c46daf8 | -18.44704 | -47.34986 | 2025-06-27 04:51:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91f1131d-4006-35b8-9425-a759b2e41000 | -13.93684 | -54.49552 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72a8c148-19c7-3a78-a2a8-0577c0c00bcb | -17.04215 | -45.88867 | 2025-06-27 04:51:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| efae9efd-f51f-35fe-bc32-4fa98ae10aa3 | -13.94893 | -54.48602 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31f04621-ecbf-34da-8294-8c140f6ab270 | -13.78362 | -54.3012 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3be7ce47-540f-3de2-b652-1e6420e3952f | -21.11065 | -43.80923 | 2025-06-27 04:51:00 | NPP-375D | RESSAQUINHA | MINAS GERAIS | Brasil | 3154408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4f6994cb-0b8d-3b7c-bcfe-79b45edf7756 | -15.0769 | -48.94473 | 2025-06-27 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5d7454f-7b7a-3651-b9db-ab660a62528c | -13.93344 | -54.49495 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb0838e8-ee5f-3746-8da4-03243b061a97 | -13.94025 | -54.49612 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21be4182-5d6a-3a99-b1ad-f182abe62739 | -20.70654 | -54.88899 | 2025-06-27 04:51:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16e85691-c8b4-314a-b453-51dae6e7fe7f | -14.01547 | -54.486 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c676ad6-56c2-3e6e-b36c-6dd10fdb1e92 | -18.42835 | -54.55826 | 2025-06-27 04:51:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 848c51a0-c2fd-39dc-9350-1d9d8725d098 | -20.59727 | -45.11112 | 2025-06-27 04:51:00 | NPP-375D | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fadcdffe-443f-3114-9e30-b4031c75848b | -19.57964 | -49.11013 | 2025-06-27 04:51:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 54cf7160-7422-3239-8f39-ca2259c247f9 | -15.0791 | -48.94697 | 2025-06-27 04:51:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 669e5409-679f-3b34-a731-c7186153352c | -19.58129 | -49.10609 | 2025-06-27 04:51:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 659d03b7-0cb6-3410-802f-47ab9155a06b | -14.66768 | -53.12602 | 2025-06-27 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5e1c29d1-93a0-3d98-b41d-624afef895d1 | -14.66492 | -53.12191 | 2025-06-27 04:51:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6225faa0-9d86-3aa4-b04e-f22be4a84a22 | -13.9449 | -54.48918 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca475503-1b6d-3659-9516-9701911b3fca | -19.5806 | -49.11154 | 2025-06-27 04:51:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 832319ab-b589-3dd6-9915-2ef6a37c2610 | -18.656 | -55.74915 | 2025-06-27 04:51:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0bf7bb2f-baa0-34e7-96d6-ff4f2d0f5c6d | -18.42776 | -54.56194 | 2025-06-27 04:51:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 83c97382-3761-3251-bab6-18561d9052c2 | -19.68331 | -45.37696 | 2025-06-27 04:51:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e80af62c-1e99-3dcd-a6ce-e6bc978ebf9c | -13.78823 | -54.29438 | 2025-06-27 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5633d3c-cdee-3a18-b1d5-203b9534a979 | -12.60233 | -57.88092 | 2025-06-27 04:51:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45554b2c-8335-353c-81b3-b889ae7a7da7 | -22.51159 | -43.50043 | 2025-06-27 04:53:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e0b9677a-0df0-3fe8-a511-664236df5c92 | -22.50827 | -43.49991 | 2025-06-27 04:53:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 9402949b-97c5-35b2-93f1-34a22265a6e0 | -22.51126 | -43.50417 | 2025-06-27 04:53:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 0a5c97fd-97f3-3356-9033-4c756bcd18f7 | -6.9605 | -42.8816 | 2025-06-27 05:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 259.3 |
| 4a64c17e-3711-31ae-85ab-7b7624e5418a | -11.5779 | -52.115 | 2025-06-27 05:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 242.5 |
| 3705a680-8802-3019-90e5-285975b7b178 | -6.9793 | -42.8798 | 2025-06-27 05:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.4 |
| 5fd70999-8a35-3a2d-9759-f52068f1971c | -6.9416 | -42.8834 | 2025-06-27 05:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.8 |
| ec0a2700-cc9f-321a-a0b8-eaaabec3fe5d | -6.9414 | -42.907 | 2025-06-27 05:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.0 |
| 9a53084b-002a-3df0-bdf1-5ac6a5e4ebf1 | -11.5782 | -52.094 | 2025-06-27 05:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| d4a088cc-988f-3da2-a1a3-17b3f8dfb9ee | -11.559 | -52.117 | 2025-06-27 05:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 8d5e30bb-61b0-3361-af92-35e98e25f8a0 | -6.9602 | -42.9052 | 2025-06-27 05:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 320.1 |
| 282f2732-8ead-3e95-bc74-8a7d087b98b7 | -6.9791 | -42.9034 | 2025-06-27 05:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 122.7 |
| dbfc74ea-5b16-356a-9e65-2377e4f1f27e | -6.27312 | -43.68176 | 2025-06-27 05:08:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4cd1a2e1-df5e-3cc4-9f2b-bf42e632e85f | -2.54831 | -47.69828 | 2025-06-27 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b4e2c4f2-22b2-3df6-88da-ba340e76095d | -5.91621 | -43.47303 | 2025-06-27 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 95ede93a-db8b-3b64-a018-c94ac490c8b6 | -2.53123 | -53.95779 | 2025-06-27 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a2ecea3-eb37-3e57-b047-68a47f6f0412 | -2.43975 | -47.46308 | 2025-06-27 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fc9fca9-fbe0-3120-90fd-20b7be44a67d | -6.27651 | -43.68275 | 2025-06-27 05:08:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e1d9b6d6-f6ac-345f-adc8-18ee97f918d4 | -2.28863 | -48.57554 | 2025-06-27 05:08:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 486a6d18-a4c3-35ce-9afb-5dbc2c5d94cc | -3.16794 | -52.44885 | 2025-06-27 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0f1e2c5-2ad7-3519-ae04-c66c0ef2982d | -5.85749 | -43.64191 | 2025-06-27 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd4dedf7-7184-3b53-b5c0-3651e507096e | -2.44337 | -47.46628 | 2025-06-27 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1f2827b-b0fa-34bc-9b78-be414513cd15 | -2.54783 | -47.70145 | 2025-06-27 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5526cd7a-b19e-3308-a88f-55cb5c23ad8b | -5.92339 | -43.4739 | 2025-06-27 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a31765fd-c742-3863-a182-083b823bb40f | -6.47763 | -43.75256 | 2025-06-27 05:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 30ebfd00-ada8-3b68-8c82-a975a04ae55e | -6.26942 | -43.68166 | 2025-06-27 05:08:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ad3b1dee-48b3-328d-9eed-96189d8db775 | 2.75233 | -60.36663 | 2025-06-27 05:08:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 26cc67e9-2c67-3a8a-ab7e-d7d982d3a444 | -5.91529 | -43.47995 | 2025-06-27 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bffaa6d9-bbff-3aba-a783-6e88eeb6697e | -2.88963 | -51.47806 | 2025-06-27 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1ab13e5-f924-30ef-ac4f-01b7535b2132 | -4.34139 | -55.77726 | 2025-06-27 05:08:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73802b8c-7685-3e2d-9806-67466d931b5d | -6.2742 | -43.67348 | 2025-06-27 05:08:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 61ce2acb-6906-3a20-851e-595adec83b32 | -5.8504 | -43.64087 | 2025-06-27 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30c78a30-b754-3230-9711-7cc921cbb9dd | -2.44456 | -47.46714 | 2025-06-27 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d7f1aa1-d38b-39bc-9221-041030f0ff48 | -6.27757 | -43.67499 | 2025-06-27 05:08:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6bd8659a-e495-3ba4-8b53-3f82103a9980 | -2.53475 | -53.95831 | 2025-06-27 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 36e94d0f-934b-33a9-8b99-d7942d941e57 | -3.85783 | -54.08179 | 2025-06-27 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ce02c5f-de6e-3e76-9d9b-1901d35fa241 | -5.92247 | -43.48077 | 2025-06-27 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53077418-f3ea-3ae2-8797-cf3604a8c067 | -4.68691 | -48.86663 | 2025-06-27 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f05871d9-c3aa-3dba-a115-6668ec43e942 | -5.85258 | -43.64832 | 2025-06-27 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 924afde8-9c7e-3ca1-b1b7-73740214f99c | -5.85351 | -43.6416 | 2025-06-27 05:08:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3e28794-7504-37ac-a7eb-33f9076dbf67 | -11.5782 | -52.094 | 2025-06-27 05:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 100.6 |
| c9e90cea-18c9-3ded-a200-558d74c73187 | -6.9602 | -42.9052 | 2025-06-27 05:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 292.4 |
| 8093b38f-0920-3e55-9980-e571663a3d0b | -6.9414 | -42.907 | 2025-06-27 05:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| d1ed0b53-a644-3bac-bfde-54e3913827df | -6.9793 | -42.8798 | 2025-06-27 05:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 126.9 |
| 3d173fbf-0246-32b8-a64e-6e90441e6dba | -6.9416 | -42.8834 | 2025-06-27 05:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| b1193335-4fb1-3fac-92f7-d819e1a3694d | -11.5776 | -52.136 | 2025-06-27 05:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 365fb47a-3dc6-332b-b85d-68c718625a97 | -6.9791 | -42.9034 | 2025-06-27 05:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 162.6 |
| 076bbaaa-0478-3f78-82ac-4be2b5a8ea5f | -6.9605 | -42.8816 | 2025-06-27 05:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 236.6 |
| 96761444-1cc8-3632-b4ab-4ae5d0e66895 | -11.5779 | -52.115 | 2025-06-27 05:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 243.2 |
| 3262dbbf-98c8-34f4-950c-647b2dcccb00 | -11.67116 | -46.73118 | 2025-06-27 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6bb994d-1cb0-3904-9d72-26c8ea0908f2 | -9.11219 | -49.43429 | 2025-06-27 05:10:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72a7d1e0-620e-320d-b573-dcb4146f8596 | -9.50473 | -56.09347 | 2025-06-27 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f106916-714d-3253-8703-45ca0bd28666 | -10.70922 | -59.13431 | 2025-06-27 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 030140de-3b89-3a44-a21f-272cee58c84a | -6.77124 | -46.3325 | 2025-06-27 05:10:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d6578bdc-eaa1-3a00-8fa4-425411081786 | -11.4406 | -54.47557 | 2025-06-27 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 24f43af7-2385-3658-ae6d-de712996b2f2 | -7.55262 | -45.83602 | 2025-06-27 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README25.md)
