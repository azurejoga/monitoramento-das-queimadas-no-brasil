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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3c5c2dc-5a76-3430-8e12-71ebc83e286f | -23.04549 | -46.66089 | 2025-10-01 04:23:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| bb4b0e7b-4d4e-3d9a-8e14-ba7da260f008 | -20.58853 | -45.88478 | 2025-10-01 04:23:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 02990d01-ef74-3caa-b491-21646454eb43 | -17.96609 | -45.0402 | 2025-10-01 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1763270c-a5fe-3230-8fac-3956ec9ff5e1 | -22.26758 | -46.71901 | 2025-10-01 04:23:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 23d5cc8b-c314-3f10-b0a1-28e4420f81e4 | -23.41939 | -49.46155 | 2025-10-01 04:23:00 | NOAA-21 | FARTURA | SÃO PAULO | Brasil | 3515400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 7a819738-7837-3222-8515-0adadb4b4eaa | -22.22133 | -46.13862 | 2025-10-01 04:23:00 | NOAA-21 | BORDA DA MATA | MINAS GERAIS | Brasil | 3108305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 985d301a-b7ed-3986-b57b-2a04cf01b5ed | -17.21584 | -49.6217 | 2025-10-01 04:23:00 | NOAA-21 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cc3e61cd-04d4-3bf7-a0b3-f078333a6dab | -22.0634 | -43.07471 | 2025-10-01 04:23:00 | NOAA-21 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a95a124f-5dc0-36c1-a5e0-4beaab486e3c | -22.58387 | -48.30835 | 2025-10-01 04:23:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59807950-18f1-3561-a457-204437af4012 | -17.95794 | -45.02269 | 2025-10-01 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 746e80ee-cee1-3a95-aa62-8717582dbbde | -21.35432 | -44.89499 | 2025-10-01 04:23:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ebf05f5a-e59a-3c25-bdb3-3201cbcf6436 | -18.70493 | -49.16885 | 2025-10-01 04:23:00 | NOAA-21 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f87f682a-2490-3604-8def-c49f704ba13d | -17.87164 | -47.1389 | 2025-10-01 04:23:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c25e1faa-08d4-3c6d-8855-6591e8eb8275 | -20.58565 | -45.88032 | 2025-10-01 04:23:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e2e6bf5a-af9f-3340-b36d-099633e368e6 | -18.32983 | -43.92455 | 2025-10-01 04:23:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 88c85a1a-473c-3950-b34c-8d797ee76ba3 | -20.02585 | -44.53824 | 2025-10-01 04:23:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 567f9c42-9b59-3d74-96a5-9190f1d03314 | -18.71167 | -49.17002 | 2025-10-01 04:23:00 | NOAA-21 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f510f7f-a4d8-3d60-9183-993307395cdd | -21.49143 | -46.92592 | 2025-10-01 04:23:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 098aa2c2-c95b-3d71-95c3-456e673801a7 | -22.255 | -43.42752 | 2025-10-01 04:23:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6c6c49c8-12ba-3753-a3ab-290750a2350f | -1.71083 | -47.02375 | 2025-10-01 04:46:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6993df3-d144-36cd-895b-a0588c389752 | -1.77063 | -47.26326 | 2025-10-01 04:46:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b1e6e6e6-8842-3900-b21a-767150d552c4 | 1.29154 | -51.24672 | 2025-10-01 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc4ddc4b-b68a-3805-99dd-b855cf783cee | -2.24671 | -47.88749 | 2025-10-01 04:46:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d6ee0706-08a3-3d83-965a-496c229185ea | 2.26092 | -50.72771 | 2025-10-01 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 827ec52e-0cb7-3751-abe2-a7d3519c48a6 | -2.27011 | -47.85193 | 2025-10-01 04:46:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0f353b42-a854-3326-97cb-e3b1e2ebe5b6 | -0.9082 | -47.54806 | 2025-10-01 04:46:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecd8fe53-b12b-3874-84ee-65c65a8faf83 | -2.25079 | -47.8842 | 2025-10-01 04:46:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7580bbf5-6f26-3714-9eed-78eb6a3e90ff | -0.09615 | -51.27742 | 2025-10-01 04:46:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ef947a3-b5a2-3ea6-b3fc-c5b9a1be497f | -2.29984 | -48.57208 | 2025-10-01 04:46:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65d5ede6-b951-37f5-b559-5041aed12b8c | -2.27071 | -47.8481 | 2025-10-01 04:46:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 27bc9901-fb6c-3c82-a2fa-d617725ec80f | -2.26663 | -47.8514 | 2025-10-01 04:46:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 022889b9-4af4-3399-be79-806c9f8bf20a | -2.14379 | -47.50903 | 2025-10-01 04:46:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aabd58ef-0d93-38f6-ab67-bc9a4108890e | -2.26723 | -47.84757 | 2025-10-01 04:46:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 999e5ae5-4835-3f22-95df-e4c5d597be94 | -0.90472 | -47.54751 | 2025-10-01 04:46:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 181a7abd-71b9-39f6-9900-3ed3589af69a | -1.62729 | -47.0537 | 2025-10-01 04:46:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8a685540-04c0-32f3-8735-71c9f6cf4818 | -0.90532 | -47.5437 | 2025-10-01 04:46:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 426930bd-4452-36c8-9d5b-925659207e9d | 1.28809 | -51.24722 | 2025-10-01 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a7ca245-9415-37ca-b8e1-175c9e559497 | -1.87685 | -48.39981 | 2025-10-01 04:46:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f81ee56a-0002-32d8-b5af-9aff516d34d6 | -2.30409 | -48.14325 | 2025-10-01 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 436319f5-4af0-31e9-a755-1483be4a46ce | -0.09956 | -51.27795 | 2025-10-01 04:46:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 256c9648-540f-3c49-80ce-3775e06285b2 | -0.90881 | -47.54425 | 2025-10-01 04:46:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c95b33e6-ecb8-3881-be20-703fbe3c2153 | -2.42393 | -47.2298 | 2025-10-01 04:46:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1308245-ccf0-3b46-bac9-4b6a12607a0c | 1.54265 | -50.91113 | 2025-10-01 04:46:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d82beff6-20fe-3816-b338-fecd6da1493e | -1.69509 | -47.28954 | 2025-10-01 04:46:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 951ea5ac-8bd8-3170-8f7d-4d162eee88b5 | -0.10013 | -51.27431 | 2025-10-01 04:46:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68eb2f21-1a18-39aa-bb59-c33763b5501a | -1.14309 | -47.24546 | 2025-10-01 04:46:00 | NPP-375D | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a6a80c2-15aa-3a7e-ba65-f38762fe0f35 | -1.33161 | -47.95857 | 2025-10-01 04:46:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 94f04815-8617-35d1-b8cf-5d85d4223213 | -2.51345 | -44.12014 | 2025-10-01 04:46:00 | NPP-375D | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68053249-1dc2-3126-aabc-0813e77c79a3 | -2.25019 | -47.88802 | 2025-10-01 04:46:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f0025651-d75d-3e1e-9f9f-583e9c1f9670 | 2.26148 | -50.73134 | 2025-10-01 04:46:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31b12484-e348-3e6b-8b51-23ededc40004 | -1.33276 | -47.57602 | 2025-10-01 04:46:00 | NPP-375D | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 30a28b1b-30e6-3daa-9d26-d93b684543a2 | -2.2473 | -47.88367 | 2025-10-01 04:46:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a35e86ec-bf78-3d62-9dc2-26b336b01204 | -1.14247 | -47.2494 | 2025-10-01 04:46:00 | NPP-375D | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c713c88a-52c1-395d-ba0c-e629fe0ec66d | -1.1178 | -48.03283 | 2025-10-01 04:46:00 | NPP-375D | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33ea0592-0274-371c-b32a-30fb5f04496a | -1.878 | -48.39253 | 2025-10-01 04:46:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8f64fcc-cd64-358a-8f9b-5717673b2bdf | -0.09673 | -51.27378 | 2025-10-01 04:46:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64e18327-bf91-3a66-8a78-9bd7672cc4b1 | -6.35968 | -43.9587 | 2025-10-01 04:49:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5bd16667-c6c4-3c45-89da-3e87ff13fadc | -4.73888 | -43.60791 | 2025-10-01 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f753c7dc-5915-3e86-9cc4-69e6a352d93d | -2.59123 | -48.1209 | 2025-10-01 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 27783b71-a73a-3100-b99c-190d03c481de | -8.22864 | -45.78924 | 2025-10-01 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ba6e03f-fa3e-38f2-bc5f-0378d832beef | -8.87221 | -47.64429 | 2025-10-01 04:49:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60f74c26-35c8-340c-9c95-8d389484d7cd | -7.16318 | -50.5447 | 2025-10-01 04:49:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97773394-ccd0-3e96-8a86-2d504e232b91 | -6.57311 | -43.44942 | 2025-10-01 04:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e3289b59-e771-38ae-96cd-b947797cd0a0 | -6.40858 | -42.8103 | 2025-10-01 04:49:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9be7cae8-45db-3bf4-9156-75764b8cbd7e | -8.51708 | -47.28889 | 2025-10-01 04:49:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6deddbb-1986-3e80-9e3f-ac560a1cae69 | -8.38492 | -48.64857 | 2025-10-01 04:49:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 954772c3-1991-3040-b03b-d6fd5a2a8822 | -7.62783 | -45.45423 | 2025-10-01 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 983c02d1-9717-35ee-a6cd-e592e84c7806 | -8.58246 | -44.74513 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1667777a-ac26-3181-a142-eaebc623e7c9 | -8.40304 | -50.11235 | 2025-10-01 04:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2bcc446-b532-3892-a155-baa604836225 | -3.55425 | -50.32865 | 2025-10-01 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 099cebb8-8028-35df-8dd9-6dcfe520bca6 | -7.44606 | -47.00973 | 2025-10-01 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1ee98e7e-f3fb-3356-ae5d-b4280014dbc7 | -8.57592 | -44.75827 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fd1d04a-630e-3ed0-996f-b48f2b670094 | -6.74065 | -50.92943 | 2025-10-01 04:49:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| abeabe6f-328f-39f4-87fe-5700c4338abe | -8.22529 | -45.79018 | 2025-10-01 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8a7596d-393b-338b-9c33-4ef822c4df7d | -6.20915 | -44.23264 | 2025-10-01 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2f2d1f4c-783e-31d5-9aa2-3c2f052d48b8 | -5.78501 | -43.30564 | 2025-10-01 04:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5222090f-7cd4-3489-ac8e-c8389824dd79 | -2.68842 | -54.76625 | 2025-10-01 04:49:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ff8f619-b614-3d82-aa40-5b536156e95f | -3.25314 | -50.11832 | 2025-10-01 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73854bb4-f7a2-37ef-8db2-18329e474026 | -4.73422 | -43.60717 | 2025-10-01 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 586d087c-0f7f-3651-9f50-0ada31f5760c | -6.83127 | -42.989 | 2025-10-01 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 6fb5dfad-bb73-3ff3-97dd-bdf12e10ae89 | -5.61562 | -52.15879 | 2025-10-01 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 850cfb61-7366-3952-a026-8c4ffb456939 | -3.52148 | -49.44257 | 2025-10-01 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1a6ee8ea-fe6a-3019-8163-8fa4ebc385ef | -6.53141 | -45.22974 | 2025-10-01 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4d99d6d5-8968-3222-89ca-c82a7230dac9 | -8.16031 | -46.25878 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c770f122-415a-377a-991b-496e509ea8a1 | -6.4906 | -45.2397 | 2025-10-01 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2462221d-825d-31cf-b106-e8269bd6d973 | -6.53255 | -45.22191 | 2025-10-01 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04828359-d558-396a-a2e6-f5920fe7d94b | -6.27643 | -44.0595 | 2025-10-01 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 600e59c0-0a47-3111-86ec-0254cfd4a4e8 | -5.93709 | -45.8968 | 2025-10-01 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f4c29e0d-ace5-3183-8211-f4d393468002 | -8.16226 | -46.26199 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aee2b373-b861-3a80-8c69-db3598904bde | -8.28213 | -45.37248 | 2025-10-01 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 47884953-f6e5-344c-84f2-1377714126f4 | -3.09741 | -47.01445 | 2025-10-01 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| f97d0f4b-e0dc-33df-9721-47b5f0e43c23 | -7.84439 | -47.06778 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91dcbc73-63a5-3948-bda1-c33f3d02b6f3 | -6.23448 | -44.15503 | 2025-10-01 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ab0d6876-899f-3014-a459-0b932cdca05c | -3.46439 | -50.08736 | 2025-10-01 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f5ad6f17-cb2e-317e-b280-1579132408a2 | -7.21177 | -44.75471 | 2025-10-01 04:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d06d2fa1-6727-319f-a1d5-f45e458d18c5 | -8.89423 | -45.05011 | 2025-10-01 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 697bd6cc-627f-32ad-b50b-bf19625d2797 | -6.28524 | -43.65693 | 2025-10-01 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3228e7bf-820c-3bb2-ac0f-4f7945a16851 | -5.94007 | -45.90453 | 2025-10-01 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fd7e3a0-7188-31d3-aefb-89114ca79049 | -7.05585 | -45.19081 | 2025-10-01 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf6a94f1-f8c8-319b-bcac-8c36372516fc | -8.53601 | -44.7108 | 2025-10-01 04:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README81.md)
