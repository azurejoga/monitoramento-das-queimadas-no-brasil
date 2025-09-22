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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a423d2f3-3278-313b-acaa-56010d836ba0 | -17.27485 | -43.44922 | 2025-09-22 04:19:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2301958-d2f1-398a-aa01-d343b9700bb6 | -11.52158 | -43.61944 | 2025-09-22 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 159f1b90-ebcd-37ed-9ca3-1e37bf61b897 | -11.48933 | -43.54842 | 2025-09-22 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b35a2de7-406d-34fb-80c6-1f3f480dc240 | -20.90744 | -46.22052 | 2025-09-22 04:19:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7976eb9b-b7b6-3534-942a-ad8a31e05b28 | -17.13838 | -45.91358 | 2025-09-22 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2ba7ca3-101f-3315-93ed-d1f29ba125dd | -22.41708 | -46.78893 | 2025-09-22 04:19:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92eb32a2-6fb1-30b6-b6ee-e8ea888c0f54 | -15.83409 | -59.52253 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d612292-8ce2-312b-9c53-7b2a2ba04e53 | -10.50352 | -44.05329 | 2025-09-22 04:19:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dec58377-85e2-346b-8f1e-564085795b0b | -17.42483 | -42.3724 | 2025-09-22 04:19:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d98f9e17-510a-3492-a98c-0a5f9d82776e | -20.53742 | -43.72018 | 2025-09-22 04:19:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 82bfbe7d-dced-37ac-a970-f5f4b35777d9 | -15.16086 | -49.58557 | 2025-09-22 04:19:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 01ccfea7-62fa-3e72-813d-1f105025231e | -22.40924 | -46.79519 | 2025-09-22 04:19:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8ab80b13-eb5b-3401-a359-a21c6f7182b4 | -20.86176 | -42.81113 | 2025-09-22 04:19:00 | NPP-375D | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 68f61174-0f83-371e-890f-6453ddfbce05 | -10.37705 | -46.07059 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2eaa33d5-4d17-369d-b5e2-d31f1f728d6e | -17.34749 | -46.82204 | 2025-09-22 04:19:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d974ff0e-807b-3819-b4df-fac5eb266624 | -17.4129 | -44.8528 | 2025-09-22 04:19:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 09cd5d07-eb03-3683-8b07-ccb2c37d2f7e | -10.37141 | -46.06181 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54347e29-1db0-3cd6-a75b-1a4c16f5ef53 | -10.46467 | -44.191 | 2025-09-22 04:19:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26371d1c-8de0-36d1-9847-e84110fa25d4 | -10.41104 | -47.84748 | 2025-09-22 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b6789d9-5904-36bb-913b-32e9e28dcec0 | -10.36732 | -46.06507 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 155d8d93-d337-34dd-9b4d-c6d56e8c9007 | -20.86545 | -42.81175 | 2025-09-22 04:19:00 | NPP-375D | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 27c0ca78-ecb3-357c-aa40-36b214b497b1 | -16.07065 | -43.47342 | 2025-09-22 04:19:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7ad2997-26df-3b10-877b-cd57435a0bf7 | -16.01727 | -59.46709 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2cfa0054-5dc7-32b9-9e12-3b5de9db6bf2 | -9.98724 | -46.24107 | 2025-09-22 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 457c34eb-60d7-3116-bfbf-a98a010a6647 | -20.86504 | -42.24075 | 2025-09-22 04:19:00 | NPP-375D | VIEIRAS | MINAS GERAIS | Brasil | 3171402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b0b6bb5c-56d4-3af0-b67a-1c4a1fb60279 | -20.14246 | -42.48815 | 2025-09-22 04:19:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 964e73f4-aa60-389a-8f9d-40e98f0961e6 | -10.37204 | -46.05798 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00c74424-8f9f-3c3f-a213-0040adbc5819 | -10.68549 | -46.45333 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3c4df6e-e9f3-3a97-9c07-df20cec8d2e8 | -11.70219 | -41.49837 | 2025-09-22 04:19:00 | NPP-375D | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 471ffac8-8957-374a-844d-36bd2f463ac2 | -17.25867 | -43.43837 | 2025-09-22 04:19:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36dd38a0-f2a2-3a49-9a49-0f8c35f07270 | -15.16084 | -49.58373 | 2025-09-22 04:19:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5dbaeef0-56c6-331b-bd72-43b561e0180e | -20.44019 | -43.67325 | 2025-09-22 04:19:00 | NPP-375D | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8dd47451-8cd7-3ea4-b6cb-4f2099ffeb2b | -16.00508 | -59.45631 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 47cdce36-cadf-3f1c-b594-57420ac9f81f | -10.25131 | -46.06979 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e34bffed-5c0f-3940-9fea-13e6e74d7aeb | -20.26049 | -55.50245 | 2025-09-22 04:19:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b538ab4a-76af-3766-8c8e-8834ee977ca9 | -10.41254 | -46.13547 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0e81831-048a-3520-89bf-aa162af0732e | -10.32069 | -46.10136 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe54e8ba-d903-3ce6-89ae-60c543fd5bc3 | -15.9327 | -42.18925 | 2025-09-22 04:19:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ef38ba6b-4fd7-3f2d-918b-b9fcc4afe97f | -16.00582 | -59.46592 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 9120f157-1394-3462-a754-390e513a26ae | -11.45366 | -43.53542 | 2025-09-22 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b80be62-24eb-3113-ae5f-04f49ba74ac3 | -19.43182 | -44.82154 | 2025-09-22 04:19:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44ed9530-52d6-35b6-9d00-1c2de1fac628 | -15.00457 | -55.31531 | 2025-09-22 04:19:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d37d47e7-9939-3e19-a6e5-f3e98b8c5a2a | -22.40865 | -46.79893 | 2025-09-22 04:19:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e432abe1-37dd-39e8-88c6-785c2bdc4979 | -20.3726 | -58.0623 | 2025-09-22 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| eb806128-7267-36fe-862d-d2090a74eb1d | -10.25476 | -46.07037 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c2121a6f-7333-31ef-810c-81cac24fdb56 | -17.06385 | -44.90112 | 2025-09-22 04:19:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc6ae288-97ec-3857-af7f-4100093394cf | -10.68514 | -46.43367 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e9aa1cb-573c-3107-8ab7-4d5706d241b9 | -10.38616 | -46.0799 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5cc313a7-f415-3481-915e-c83ff0d9e809 | -9.73539 | -45.95605 | 2025-09-22 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3dc51f5a-4882-3dbe-88de-02925085b0f5 | -18.35739 | -43.71029 | 2025-09-22 04:19:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 831473c9-178e-3969-8faf-b83d263395b5 | -22.421 | -46.78579 | 2025-09-22 04:19:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bcb91c0a-38fb-36ed-b1c5-82cad29279eb | -20.19366 | -44.61781 | 2025-09-22 04:19:00 | NPP-375D | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3b14033b-bc25-3836-a6f5-decb745a8853 | -9.99245 | -46.23722 | 2025-09-22 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ac90d7f-2781-35db-8a64-f37fd5f8a87e | -15.03386 | -55.28561 | 2025-09-22 04:19:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5be91a9a-a260-3329-95f2-12252de17907 | -17.05939 | -44.90784 | 2025-09-22 04:19:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b43c122e-44c8-31ad-9738-a3fd860f45a4 | -19.27686 | -43.74357 | 2025-09-22 04:19:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1db5f191-797d-3a7c-9e3c-0cb923aaa777 | -18.09772 | -44.2636 | 2025-09-22 04:19:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 295c9e52-4d0a-3b91-8138-dff63e23065b | -20.26249 | -55.49302 | 2025-09-22 04:19:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 27b36482-3f37-3a39-b894-dd8c2454caa7 | -10.46411 | -44.19451 | 2025-09-22 04:19:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5a6b7d7-2f26-3d38-887f-a88aa22b1cc3 | -16.73628 | -43.02384 | 2025-09-22 04:19:00 | NPP-375D | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8886d78e-58d4-3b3d-9b8f-11842375a998 | -20.25606 | -55.49808 | 2025-09-22 04:19:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 689a0d98-63aa-3f08-acd5-4df79532f359 | -10.35415 | -46.05895 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4c3b96b-bc6b-33bf-960f-339459ea8260 | -18.54595 | -43.84731 | 2025-09-22 04:19:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a023cfd-57c6-356c-bff7-4c212b21f3e2 | -20.50935 | -56.88405 | 2025-09-22 04:19:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85de2a82-8fe2-3166-8b98-139fc1a78160 | -15.04325 | -55.29665 | 2025-09-22 04:19:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f9163ac-d52b-3df1-ac8c-0114aa84a6dd | -19.13906 | -42.66349 | 2025-09-22 04:19:00 | NPP-375D | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 186bb32b-7cea-36c8-a7eb-0dd8980a955b | -7.71083 | -55.45507 | 2025-09-22 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d46d78f7-1701-3616-98bf-832e66a1ab7e | -20.37956 | -58.05927 | 2025-09-22 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| d121632a-71c8-3743-be0f-59c9fc05f015 | -15.99272 | -59.47804 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b61f748f-6eae-3baa-b086-9a502bdcd38f | -19.8435 | -42.2006 | 2025-09-22 04:19:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f686c424-640b-327d-8013-f8fb81261653 | -15.92764 | -48.34978 | 2025-09-22 04:19:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a327f0b-bd77-3a0a-abf8-58751a4fa9db | -17.35025 | -46.82637 | 2025-09-22 04:19:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43f348bd-ec9c-3dda-80ab-521ca9ebaca8 | -21.63124 | -43.65169 | 2025-09-22 04:19:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9e36b0bb-d2d0-326d-9d6f-8b97e15a6b27 | -18.84714 | -42.19417 | 2025-09-22 04:19:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a57ccda4-943f-3796-afe0-27dcba272086 | -15.76999 | -59.41659 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f28065d0-68f1-32a6-95fb-a415c2bf12ac | -17.2708 | -43.45264 | 2025-09-22 04:19:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c1bd56b0-1461-3fe4-9ea9-66e85e7298e7 | -11.69862 | -41.49783 | 2025-09-22 04:19:00 | NPP-375D | CAFARNAUM | BAHIA | Brasil | 2905305 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1eab791e-4fe6-3fe5-a410-1800681eb741 | -20.13057 | -42.49145 | 2025-09-22 04:19:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d46beaa6-c72d-3f0d-b325-316f44b29b02 | -15.94365 | -59.41683 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9403a501-7497-33b7-ac92-65b26c7237fa | -17.67595 | -44.08157 | 2025-09-22 04:19:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7cbae8bf-4ea0-3565-8d64-c3a483aa53e0 | -10.25194 | -46.06597 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dd851874-c8c1-3bb5-8b25-b443c062b4b0 | -20.37851 | -58.06388 | 2025-09-22 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 4f940ee5-139f-3854-aa52-1634ba9da871 | -14.61737 | -49.74928 | 2025-09-22 04:19:00 | NPP-375D | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4275d97-d6ea-3395-87be-e1b11e6ad9d3 | -20.61574 | -46.07514 | 2025-09-22 04:19:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7707e64-3bb0-38d6-b8eb-1fa57c1849b2 | -20.26692 | -55.49739 | 2025-09-22 04:19:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| df120e2f-1a5e-363e-ac34-5604a5992d6a | -9.99135 | -46.23781 | 2025-09-22 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b5b7591-ddf0-3c4d-af1e-7f4fac529df3 | -11.50535 | -43.5695 | 2025-09-22 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6a49ba1a-f152-3110-a3df-5e8f42d45236 | -20.39996 | -54.8623 | 2025-09-22 04:19:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 45681137-a5b3-30b8-80b5-506d70680a56 | -20.39242 | -58.05778 | 2025-09-22 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1a8cc4b9-3368-3b66-bed3-02821582ab82 | -19.84799 | -57.28966 | 2025-09-22 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d5be522c-ac78-38f3-bdeb-2b9c374698db | -19.87579 | -42.44827 | 2025-09-22 04:19:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3d334fdf-2f5e-3ffa-ae2e-70027669c773 | -21.5802 | -46.92788 | 2025-09-22 04:19:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ca203e3f-eead-3902-9489-b9d0b998844c | -15.5638 | -44.35932 | 2025-09-22 04:19:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 31cdb214-2516-3589-af07-bbe856b7a3ea | -15.76579 | -59.4165 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5fe17839-a8bd-333d-af0d-80e6788eff6c | -19.13969 | -42.65899 | 2025-09-22 04:19:00 | NPP-375D | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| af6ca182-720b-33d9-afe9-a5d9c177dd1a | -16.01042 | -59.46497 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| f06e68ea-d4a6-37a0-9e0a-c374be302873 | -17.26629 | -46.95724 | 2025-09-22 04:19:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 632cce5a-f75d-307b-8b5c-7f194469682b | -15.15612 | -49.58794 | 2025-09-22 04:19:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6891218a-01ca-3f2c-ac97-335ee73cf786 | -20.50366 | -56.8835 | 2025-09-22 04:19:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 395cb6e6-feeb-38a8-8468-e14abc0c1bdd | -18.98427 | -44.22536 | 2025-09-22 04:19:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README23.md)
