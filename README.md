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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64f71c23-8d9b-327f-9edb-406780e6a7ca | -5.9565 | -44.4538 | 2025-04-14 00:14:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c8282190-c525-3652-b089-80b03245ce59 | -5.9467 | -44.456001 | 2025-04-14 00:14:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e901870a-b655-38d6-8047-dc0378d57a31 | -7.0615 | -44.372501 | 2025-04-14 00:14:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36e715c1-0823-3882-8f91-139d5ac87ba2 | -7.0731 | -44.377998 | 2025-04-14 00:14:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 169c201a-730c-3f83-a74f-5c71d172c0b1 | -7.0713 | -44.370201 | 2025-04-14 00:14:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e7cdd675-bc61-3f30-a513-9ad201a3a54e | -5.9583 | -44.461601 | 2025-04-14 00:14:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8246c046-f237-32a5-9289-306822c066e1 | -5.9485 | -44.463799 | 2025-04-14 00:14:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee384c11-c30d-3e19-bf06-74be891ef528 | -5.94671 | -44.45895 | 2025-04-14 00:50:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 93535d68-b65c-3dc6-8c10-6b3f2fd81257 | -7.06037 | -44.38615 | 2025-04-14 00:50:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 0b293e67-ea2c-33e8-8dfe-30306a098e22 | -7.06106 | -44.37559 | 2025-04-14 00:50:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| ceed4f8b-d191-3294-8b2e-65b45c5fa793 | -4.8603 | -65.2649 | 2025-04-14 01:04:00 | METOP-C | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ce28913c-2188-3c50-82df-1012e5cad50a | -5.2229 | -36.14718 | 2025-04-14 03:13:00 | NOAA-20 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ca8c78f7-2154-349a-812f-3904dc7ded5f | -16.2704 | -40.07038 | 2025-04-14 03:17:00 | NOAA-20 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 76181ed9-de64-3927-8520-7b31587c31a7 | -16.27106 | -40.0672 | 2025-04-14 03:17:00 | NOAA-20 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3374c522-d76b-37c4-b74d-09dfd17de5da | -5.93678 | -44.35719 | 2025-04-14 04:06:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dabd9ab6-3b88-3f18-9fc7-1b28bc1014e8 | -5.94533 | -44.46423 | 2025-04-14 04:06:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a4258712-0e61-385b-a358-02c11f79978a | -5.95319 | -44.46126 | 2025-04-14 04:06:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0314eb82-7084-3aed-9c81-fb51ce653628 | -5.94599 | -44.46009 | 2025-04-14 04:06:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 573f3928-5463-3937-8e86-8ba9e59534fd | -5.94959 | -44.46068 | 2025-04-14 04:06:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 81e4ba83-055e-3118-a673-341268af57a9 | -5.76395 | -43.64541 | 2025-04-14 04:06:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82a7b864-5e23-36da-9e73-240de6dc3288 | -7.06474 | -44.38138 | 2025-04-14 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7a92a17-901a-30cf-bb9b-72c7c6f2355c | -7.06552 | -44.3765 | 2025-04-14 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f953b7a7-7658-3822-b231-54548eb3fdcc | -7.0612 | -44.38081 | 2025-04-14 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9b09b6e7-cc5f-3bcb-9fcd-9bb93c646634 | -10.98731 | -40.39418 | 2025-04-14 04:08:00 | NOAA-21 | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| fc1866c5-471c-3738-bb15-b1ccf2d66a9a | -7.06487 | -44.38045 | 2025-04-14 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0143ce9-a047-34aa-a688-db286f27456d | -14.11975 | -41.67631 | 2025-04-14 04:08:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 286a31b7-7745-3a95-aeca-8efdd2ed8d42 | -10.5902 | -40.93931 | 2025-04-14 04:08:00 | NOAA-21 | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ccbbd01e-68de-3d43-8cca-97ce7290c5cc | -7.06183 | -44.37685 | 2025-04-14 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f4bc7af7-b062-30a2-a2b5-ebba791c7ec2 | -10.69686 | -37.04891 | 2025-04-14 04:08:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4ff3edb1-eeb9-3cef-96ae-85d65db5f53a | -7.06537 | -44.37741 | 2025-04-14 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f96d2ef2-578d-33a0-8b4c-f47b508f3a5c | -21.45074 | -47.00323 | 2025-04-14 04:10:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f531400c-9743-3f94-9385-4d1f69b87a1a | -17.67864 | -42.7424 | 2025-04-14 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d6bc449-8c93-3104-8ca4-3eb31acae97c | -19.8328 | -40.11424 | 2025-04-14 04:10:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0f418a93-9508-348d-a1f6-8d214d43d54d | -16.27341 | -40.06665 | 2025-04-14 04:10:00 | NOAA-21 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7864326d-4c32-3159-bbed-777412b5ba6e | -16.09183 | -42.28627 | 2025-04-14 04:10:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 32ceec6d-1e6f-3e17-ae77-5e01c4e0e12c | -19.79884 | -41.97248 | 2025-04-14 04:10:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f8616e24-8da4-3dc6-992c-de967337320a | -17.59679 | -43.19734 | 2025-04-14 04:10:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf1e86ce-5c44-3411-95d3-7b232debb2f2 | -17.75423 | -42.89538 | 2025-04-14 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1431ddcd-54a7-3b96-bb0b-b8f6ac850533 | -17.7809 | -42.80864 | 2025-04-14 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3493bd8-67a9-3aef-b931-7995c54783cd | -16.22827 | -39.35192 | 2025-04-14 04:10:00 | NOAA-21 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 736ef110-a7df-338b-a824-5ff4cfb45562 | -16.84586 | -42.07174 | 2025-04-14 04:10:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7e3a8cb5-46df-3556-8bf6-e96750a7e6c6 | -21.45081 | -47.00351 | 2025-04-14 04:10:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f89f8352-8849-313b-bd37-c589e007ad04 | -27.01948 | -48.86694 | 2025-04-14 04:12:00 | NOAA-21 | BRUSQUE | SANTA CATARINA | Brasil | 4202909 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5d6ae0cc-680b-3a4a-94c5-87626ea7ec9d | -23.98413 | -48.91757 | 2025-04-14 04:12:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5e4a65a-37ee-3192-b5d9-6c30b72c536e | -23.04707 | -49.89434 | 2025-04-14 04:12:00 | NOAA-21 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 44c2a7a8-a314-3362-b607-7f078073d79b | -29.85915 | -54.66314 | 2025-04-14 04:14:00 | NOAA-21 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 2.9 |
| 71f91a77-d98b-3ec4-bfd2-a81446190937 | -29.85369 | -54.6669 | 2025-04-14 04:14:00 | NOAA-21 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 5.1 |
| dec2c333-7d1e-3385-9a1f-ee36bc8aa2cf | -29.85519 | -54.66523 | 2025-04-14 04:14:00 | NOAA-21 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 8.1 |
| dfd7ec4b-7d5b-3d4f-8d48-185419c1d8c2 | -29.85477 | -54.66196 | 2025-04-14 04:14:00 | NOAA-21 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 5.1 |
| 68d45d68-b498-3458-a0d2-e5f8e4df9c0b | -5.94593 | -44.46618 | 2025-04-14 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cf264724-ad91-3280-8707-1908d955a0f1 | -5.94658 | -44.46192 | 2025-04-14 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 438f5835-5ecc-3870-bd5b-60e3639b4826 | -5.79602 | -46.30888 | 2025-04-14 04:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e40a6a3-728d-35c2-bb2c-a34ecde52bd0 | -6.29245 | -45.26641 | 2025-04-14 04:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 274aabdd-1a44-373b-b87e-254c2d1b4a5b | -5.95086 | -44.45826 | 2025-04-14 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ddd3d488-023c-3dc3-8807-0cd9b9263ff8 | -5.94722 | -44.45771 | 2025-04-14 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee74af2c-b75b-37c2-9837-cc6dd8d0bebd | -5.93635 | -44.35618 | 2025-04-14 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2062ee8d-fe1e-3634-8cd4-0b73ac8bbe78 | -5.94293 | -44.46138 | 2025-04-14 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e4ffd02-0138-30cc-850f-9d7e95652a60 | -6.28893 | -45.26589 | 2025-04-14 04:32:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0e54882c-2fd1-30fb-99fe-f7cd5934ae69 | -5.95022 | -44.46247 | 2025-04-14 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2cc1f01f-ab30-3142-a21b-345f7ca21ea5 | -7.06548 | -44.37562 | 2025-04-14 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30e68ac7-8646-3ffa-ae6d-7f1ce34bc585 | -7.06177 | -44.37505 | 2025-04-14 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a097aad6-38a0-31e0-bcc8-5eb28c6021fa | -7.06109 | -44.37952 | 2025-04-14 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9cd3f31b-0dee-325f-ab37-f3d675b9c353 | -18.11051 | -42.88459 | 2025-04-14 04:36:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cfb6a6fe-9e22-3b5f-8b3c-776917697662 | -18.11524 | -42.88535 | 2025-04-14 04:36:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8d7f97f4-a3fb-343e-b1fa-159eebd0647b | -17.56919 | -50.66118 | 2025-04-14 04:36:00 | NPP-375D | SANTO ANTÔNIO DA BARRA | GOIÁS | Brasil | 5219712 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 797cd8b7-538d-31e1-ac47-e50dddccddf1 | -16.2744 | -40.06561 | 2025-04-14 04:36:00 | NPP-375D | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a2b78d5c-6283-3d80-a1d7-c4c4181e58fc | -21.19589 | -44.93784 | 2025-04-14 04:38:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 04a4d41d-3793-38e1-bf1e-2044977ab444 | -23.04577 | -49.89487 | 2025-04-14 04:38:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 3de06df6-4ca8-3a24-90a7-14537befd78f | -21.45063 | -47.002 | 2025-04-14 04:38:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 553ee4b4-450f-304f-8820-96f0e25157b6 | -29.85615 | -54.66336 | 2025-04-14 04:40:00 | NPP-375D | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 880cbf25-58c2-3162-877c-40b2c77abc14 | -29.85279 | -54.66262 | 2025-04-14 04:40:00 | NPP-375D | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| bb762996-2fb1-3c1d-acec-930b5c6a3c8b | -30.27604 | -55.18492 | 2025-04-14 04:40:00 | NPP-375D | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 161f7a9b-6464-31a9-bbab-dafefa11ee2e | -29.85951 | -54.66409 | 2025-04-14 04:40:00 | NPP-375D | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 0ec3b47e-8306-3302-8136-454efef83d14 | -5.94693 | -44.4609 | 2025-04-14 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88809d9c-d1e4-317b-86cf-d41e6041adee | -5.94643 | -44.46449 | 2025-04-14 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f1568282-8a79-3baa-9e11-e4ad38192810 | -5.94592 | -44.46815 | 2025-04-14 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb3a3d0e-11fd-31d8-aa26-7ef1118e27b9 | -5.93326 | -44.35711 | 2025-04-14 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ccdd605-c4a8-3443-9332-3adf03691add | -5.94741 | -44.45739 | 2025-04-14 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 747d6a48-9a3a-3562-b88b-5fc27dd6bb95 | -11.39833 | -52.95046 | 2025-04-14 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b48be689-173f-36bb-b55e-c3e08cc143d5 | -5.9524 | -44.46165 | 2025-04-14 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2ef7491-e5a5-35cd-9ce7-0e73e568414f | -16.90609 | -48.19575 | 2025-04-14 04:57:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ec74685-c7b9-3746-861d-0220f6369234 | -17.36878 | -52.34461 | 2025-04-14 04:57:00 | NOAA-20 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfce794f-001f-30ee-828e-e317c87c2855 | -23.04502 | -49.89208 | 2025-04-14 04:59:00 | NOAA-20 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5369f251-b627-3a93-8852-1c786f088bcc | -29.86034 | -54.66503 | 2025-04-14 05:01:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 16c440b7-488d-34d2-9530-3464376d5593 | -29.85644 | -54.66438 | 2025-04-14 05:01:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| c6b0b91a-663e-3c79-afb2-1ad9fb0bb92d | -30.27497 | -55.18584 | 2025-04-14 05:01:00 | NOAA-20 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| f02ee733-c034-3310-bf08-74cd9689501b | -29.85252 | -54.66374 | 2025-04-14 05:01:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 393e2a8f-c3ac-3601-b5bd-7d12d74eb968 | 2.64237 | -61.41505 | 2025-04-14 05:46:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1991b01-1d07-3c66-992f-5f781553a41d | 2.65596 | -61.43027 | 2025-04-14 05:46:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9831d6bf-db73-3d68-90f4-a20a96fa4f5e | -9.86605 | -63.30277 | 2025-04-14 05:50:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 299e8375-2de7-3319-becb-bfffef71b894 | -9.86221 | -63.30214 | 2025-04-14 05:50:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdd94ae2-98ed-3a7d-af3e-d2520d99bb05 | -9.86989 | -63.30339 | 2025-04-14 05:50:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07587cb7-cd53-3573-b0d1-7e32ae4447a4 | -6.3698 | -43.6364 | 2025-04-14 12:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 184.9 |
| 868964a4-5593-3266-b415-6498f94e4151 | -6.3698 | -43.6364 | 2025-04-14 13:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 238.1 |
| a2a2b7d7-5b5a-36c0-8d4e-67eb13c4ec93 | -6.3698 | -43.6364 | 2025-04-14 13:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| c036abac-6850-3502-aeaa-abb699c051e3 | -6.3698 | -43.6364 | 2025-04-14 14:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 185.2 |


