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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ae3c415-cbaa-3805-819e-180362d55e20 | -14.68866 | -53.39809 | 2025-05-07 04:04:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fcfdc92a-03a0-3ee4-9d31-f727f63a6f48 | -10.72046 | -42.32653 | 2025-05-07 04:04:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4a46cc79-e724-3b4f-9aac-6f51f44ed19f | -10.98824 | -44.44723 | 2025-05-07 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c1ba887-9c0e-3230-ba05-f47be7c0f32f | -10.98457 | -44.44657 | 2025-05-07 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9dc2b7c7-a579-30ff-a99f-b7daf1323719 | -15.1593 | -45.65987 | 2025-05-07 04:04:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68d77c9b-e2bc-3104-82a5-b2deb161ced2 | -11.79331 | -47.37912 | 2025-05-07 04:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea5d17a1-3275-3fdb-b1e9-40cbc4b0c396 | -18.42155 | -54.71176 | 2025-05-07 04:06:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a73dee2-c01b-32a0-86c2-197152e7a44d | -20.48111 | -48.74166 | 2025-05-07 04:06:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1ca75391-acb4-343f-8886-3824204e3efd | -19.5318 | -43.92144 | 2025-05-07 04:06:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 411de485-1a0d-3499-bb28-f921fdb5a209 | -23.3377 | -46.77487 | 2025-05-07 04:06:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6e06fef8-a609-3f90-8cbf-842714209080 | -22.81025 | -47.13364 | 2025-05-07 04:06:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c473db8d-77f7-3cee-a5a1-856f82f139ba | -22.81105 | -47.1292 | 2025-05-07 04:06:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9cde8835-243e-3392-b05a-2f6e2d0ebceb | -21.56765 | -47.25057 | 2025-05-07 04:06:00 | NPP-375D | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b182e8c3-ccc9-3b45-9706-4c4cda57c90f | -21.05991 | -49.96935 | 2025-05-07 04:06:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4eb066f4-b58a-3322-998b-43bb47f81e0a | -17.14634 | -54.00544 | 2025-05-07 04:06:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fa4e077-f027-37ce-8a31-282b821ba1da | -19.9684 | -44.2173 | 2025-05-07 04:06:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 28e0f4c5-2975-3381-95ee-07c56963f7db | -20.47633 | -48.74458 | 2025-05-07 04:06:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fd251bc9-fbca-3225-a9ba-f38fc1b31dd1 | -21.19556 | -44.93595 | 2025-05-07 04:06:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 201dc0e6-76fe-3a51-915e-779b83ef2943 | -22.80666 | -47.13288 | 2025-05-07 04:06:00 | NPP-375D | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d992efbd-4901-31f0-904b-0b6486e68598 | -18.28931 | -52.99546 | 2025-05-07 04:06:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fc579fb-44fd-3d22-975b-c176a3efdc93 | -20.48039 | -48.74545 | 2025-05-07 04:06:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3cb1e967-0847-37a1-af2b-eaafc01b3f95 | -20.83352 | -49.41933 | 2025-05-07 04:06:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bc8fb64d-4800-3566-83ec-9856690142e4 | -18.41542 | -54.71049 | 2025-05-07 04:06:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fddac96-c1fc-3afc-93fb-9bf04597ed18 | -19.43761 | -44.34021 | 2025-05-07 04:06:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1e2a2ecd-491c-3783-8134-4c28cdac2812 | -20.55957 | -54.0696 | 2025-05-07 04:06:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9873c4a-7851-3c1a-9ccb-fe20af383f3c | -17.14774 | -54.00537 | 2025-05-07 04:06:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5704a467-d620-3efa-b3be-81238b095dc7 | -18.28764 | -53.00321 | 2025-05-07 04:06:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8b607b1-f975-3034-baa8-6b541c01d1ba | -20.76312 | -46.7711 | 2025-05-07 04:06:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ded32e65-475f-3d31-b215-cbfec4372776 | -18.26643 | -52.99417 | 2025-05-07 04:06:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0fc35c53-745a-3fdf-9ca7-700e7ce83a96 | -18.41436 | -54.71528 | 2025-05-07 04:06:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ebe9bdd-dedf-3be7-88d7-3cd4f24b5613 | -20.80181 | -42.95777 | 2025-05-07 04:06:00 | NPP-375D | PAULA CÂNDIDO | MINAS GERAIS | Brasil | 3148301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d93ff2e0-1651-3359-8dcb-ff42cb738d7f | -21.68289 | -45.22116 | 2025-05-07 04:06:00 | NPP-375D | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 68185fb4-507c-3f5d-b7c0-25a5aa6f0f59 | -21.00804 | -48.84891 | 2025-05-07 04:06:00 | NPP-375D | EMBAÚBA | SÃO PAULO | Brasil | 3514957 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8a1f340e-5914-30d3-8d56-16996dd29472 | -18.29395 | -53.00082 | 2025-05-07 04:06:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 089e2b9e-cde9-35a9-9fc9-7bb00bbcf553 | -20.0577 | -49.36789 | 2025-05-07 04:06:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e36ad951-25e4-3e6a-b088-dfa79e6fe81b | -20.41765 | -43.55147 | 2025-05-07 04:06:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cf82e46b-16dc-34ad-89c2-3778dc94deeb | -17.6229 | -50.91872 | 2025-05-07 04:06:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d622189d-a0ed-3321-9bc3-26f0a98a2aa5 | -18.00312 | -44.39111 | 2025-05-07 04:06:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd1e85d3-b234-37ac-b825-c1848e58d61b | -22.09721 | -50.24596 | 2025-05-07 04:06:00 | NPP-375D | POMPÉIA | SÃO PAULO | Brasil | 3540002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a7baa533-81f7-3f65-92c6-66110bbd4586 | -18.2656 | -52.998 | 2025-05-07 04:06:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb144915-8482-38d5-867c-0e040f148743 | -18.29013 | -52.99162 | 2025-05-07 04:06:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb15f9d4-e71a-3d68-ab41-74240b971483 | -19.18858 | -47.20847 | 2025-05-07 04:06:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c037667-d14f-3698-b399-bad3eef99d5d | -20.71998 | -54.40407 | 2025-05-07 04:06:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c49197bf-f828-3827-9647-8f624b9818d3 | -21.38594 | -48.64035 | 2025-05-07 04:06:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c563c699-8984-3ec9-a3fa-595e599f2b29 | -23.40476 | -46.55655 | 2025-05-07 04:06:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 38d95c6e-74c9-3541-9aeb-799fc59fd03e | -20.27526 | -54.63228 | 2025-05-07 04:06:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48088fbb-9a76-316a-803c-4b6c26c6286e | -21.04924 | -56.00077 | 2025-05-07 04:06:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ad25888-9e04-3e7b-a5b6-f0faaca2d04f | -18.42171 | -54.70539 | 2025-05-07 04:06:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e598261-0e77-3b1b-9071-a7a542ff9bcb | -21.38695 | -48.63495 | 2025-05-07 04:06:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56c559cb-a064-3e4c-80a0-60f2a53d4bc0 | -18.28548 | -52.98637 | 2025-05-07 04:06:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e01864d-b47b-3546-a8e6-9de2cb87ea55 | -17.86931 | -44.56367 | 2025-05-07 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6343c57e-933f-339a-a942-def7d106dfce | -18.42263 | -54.70686 | 2025-05-07 04:06:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6b56b1d-0ab4-3f29-b03d-13960d20ceb0 | -22.80746 | -47.12844 | 2025-05-07 04:06:00 | NPP-375D | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a11be2c2-c776-388f-a19d-cf5080876899 | -20.56521 | -54.07092 | 2025-05-07 04:06:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 518b616d-137c-3b8f-bc87-e8a31bde2b86 | -19.24507 | -52.35406 | 2025-05-07 04:06:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d62ed0db-cb16-349e-afeb-cfa6d9398433 | -21.05237 | -56.00061 | 2025-05-07 04:06:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 969f2fac-fc10-3f24-bf21-31e4164396da | -18.14634 | -47.79943 | 2025-05-07 04:06:00 | NPP-375D | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1cbea5d0-a058-3e0d-8716-96c73af8058b | -19.15645 | -47.82172 | 2025-05-07 04:06:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c201e2d1-da8c-3878-8bc0-88987cd13f72 | -21.13799 | -40.91592 | 2025-05-07 04:06:00 | NPP-375D | MARATAÍZES | ESPÍRITO SANTO | Brasil | 3203320 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 61fcda4a-e90e-3a8a-84c8-1b621aad5798 | -19.94494 | -44.71715 | 2025-05-07 04:06:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce844ae6-6328-3bc1-9fad-a96c960b7614 | -20.56607 | -54.06704 | 2025-05-07 04:06:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b77fb023-32ba-3c89-9d33-42ca7eafccc4 | -18.28848 | -52.99932 | 2025-05-07 04:06:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 581f1947-df87-3704-b7a8-6f71acd0293e | -16.64932 | -55.75037 | 2025-05-07 04:06:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 490220c3-0a35-39cd-a997-6e6dd4e0653b | -20.71902 | -54.40837 | 2025-05-07 04:06:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bb6e25c-e288-3663-84b8-72fbf3243c53 | -18.42059 | -54.71028 | 2025-05-07 04:06:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 71bc936b-2673-3ba2-8098-2bfa98bdc940 | -21.15589 | -47.00532 | 2025-05-07 04:06:00 | NPP-375D | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cf8c43b9-eaf1-3e0e-9349-a89f12eae7f8 | -23.33844 | -46.77065 | 2025-05-07 04:06:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5378906f-181e-3890-b356-000126fafea6 | -19.93606 | -44.20355 | 2025-05-07 04:06:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c8d4f560-5dc9-3d52-aad2-ee0953723ff7 | -19.24057 | -52.34943 | 2025-05-07 04:06:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 444acd5d-aeb7-31b1-84d6-548c05dc687a | -18.83159 | -50.33316 | 2025-05-07 04:06:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 95cc64b1-9f0d-35ab-9ba3-bbb79a747ecc | -18.41949 | -54.71513 | 2025-05-07 04:06:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 696648af-0a28-398d-b19e-bd9b49c26d0f | -18.42049 | -54.71661 | 2025-05-07 04:06:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b737eecd-70b6-39e2-89ee-611f7bf4bacb | -20.05689 | -49.37212 | 2025-05-07 04:06:00 | NPP-375D | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| dff9bc8d-53c7-3413-b6f6-cbb77679770b | -17.86867 | -44.56755 | 2025-05-07 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9de8f18-8ce8-3332-a22d-77a4b9b9db69 | -16.65073 | -55.74426 | 2025-05-07 04:06:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 7f8e605b-e322-3251-bea0-c043e2371ca1 | -17.1523 | -54.00695 | 2025-05-07 04:06:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc61eefd-08fb-3e2c-95d9-ce5d9af4dda5 | -16.65541 | -55.74633 | 2025-05-07 04:06:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e98ae674-80be-3780-a40c-c4558b22a31e | -23.60997 | -49.01871 | 2025-05-07 04:08:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0b83a1d-4859-3a56-8dcd-5d4833f3c5f6 | -24.00698 | -48.50823 | 2025-05-07 04:08:00 | NPP-375D | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d10793a8-f6fd-335a-8159-110ab84471c8 | -23.611 | -49.01326 | 2025-05-07 04:08:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf4b0295-f321-3bed-829a-bfc2edf20055 | -23.60522 | -49.00063 | 2025-05-07 04:08:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5407d111-8e43-352a-9c2e-09491ea8aa43 | -23.59499 | -47.43973 | 2025-05-07 04:08:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4b9c04a3-5cf4-347b-be49-9167da6a255e | -23.80156 | -49.04379 | 2025-05-07 04:08:00 | NPP-375D | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61fa2081-3764-32d6-8063-85a735eb7d12 | -30.09278 | -51.03179 | 2025-05-07 04:08:00 | NPP-375D | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 83d597e5-4604-333a-8b61-30d170c9b3a9 | -24.00184 | -53.407 | 2025-05-07 04:08:00 | NPP-375D | ALTO PIQUIRI | PARANÁ | Brasil | 4100707 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 87f3e815-d8df-3231-9788-879d658efa21 | -29.52774 | -50.63779 | 2025-05-07 04:08:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ae94b614-4303-3ffc-b4f1-8aefced29376 | -23.61304 | -49.00234 | 2025-05-07 04:08:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0536fed7-9f4b-324b-af13-1a2bc13d7dea | -23.60913 | -49.00148 | 2025-05-07 04:08:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bf845bd-b67d-3885-8a2b-7b5f59743a52 | -29.52697 | -50.63874 | 2025-05-07 04:08:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| afcb9a8d-bb0a-3fa9-992a-3a9fd4d388c2 | -30.09084 | -51.03225 | 2025-05-07 04:08:00 | NPP-375D | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| f8d740e7-7720-3b04-b7b5-5d88968cffe4 | -23.79662 | -49.04841 | 2025-05-07 04:08:00 | NPP-375D | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6be29c6f-63e8-3992-8b2e-b5a1d4c16177 | -24.09681 | -48.97583 | 2025-05-07 04:08:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e962426-c8c8-302b-96c4-fe2dd51a9015 | -6.69189 | -42.13031 | 2025-05-07 05:08:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| e1a58e69-9800-3184-ae89-f0b23fba62a4 | -6.55281 | -44.4875 | 2025-05-07 05:08:00 | AQUA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 638d08ad-7d87-3c79-ab89-336c2c9f7921 | -6.69468 | -42.12408 | 2025-05-07 05:08:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 826f25f3-b1c3-3374-be82-e3cda2b2a962 | -6.70202 | -42.13191 | 2025-05-07 05:08:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 26.6 |
| a09f1e6c-49db-30b0-9531-317cc038da2b | -6.69285 | -42.13598 | 2025-05-07 05:08:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 6281c2bf-db47-355d-b1a4-84f155850ff8 | -11.3963 | -52.9477 | 2025-05-07 05:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| cd37695f-41b0-36b8-9565-e1f776a14b3e | -8.07595 | -43.11934 | 2025-05-07 05:10:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 4a1dff91-cc03-3d5c-a3d8-964b56c4e8d1 | -7.56327 | -45.84053 | 2025-05-07 05:16:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README6.md)
