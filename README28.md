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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 987c2efe-8824-395e-bd3b-d992e65d53d2 | -7.75219 | -48.24971 | 2024-11-03 03:55:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 145763eb-7db3-3f1f-ba7e-5710744e259f | -7.74673 | -48.24879 | 2024-11-03 03:55:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38d1cc97-91a2-35b5-807e-b3e102501ac2 | -5.70146 | -48.99345 | 2024-11-03 03:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 203d35a5-1117-3508-bf05-f9b9e2969966 | -5.70071 | -48.99775 | 2024-11-03 03:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ace1b31-fb35-37c9-bfa5-77d6852468e5 | -8.15973 | -35.31198 | 2024-11-03 03:55:00 | NOAA-20 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3b67111b-e67a-323d-b9a6-b70d2c43e798 | -8.07494 | -34.97697 | 2024-11-03 03:55:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 506ad562-c7cf-3d16-9c1c-5add8ba56819 | -8.68452 | -36.99573 | 2024-11-03 03:55:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1ff72ec7-74db-3144-830b-3f25114023fc | -8.68415 | -36.9958 | 2024-11-03 03:55:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 36c6ea86-e947-349e-a958-dcc1f1b0f592 | -15.40104 | -39.14842 | 2024-11-03 03:55:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 27889209-6afd-30c8-a291-f9fec0080e3c | -15.39768 | -39.14788 | 2024-11-03 03:55:00 | NOAA-20 | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| be245735-4409-3adb-8cf9-88285e3ff00e | -7.43601 | -39.11701 | 2024-11-03 03:55:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 41de020c-e6ff-39c1-ad20-b57d577e5f51 | -15.49717 | -39.44757 | 2024-11-03 03:55:00 | NOAA-20 | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e9ef7ea3-9096-3867-a082-2ef584b8c165 | -15.49533 | -40.79187 | 2024-11-03 03:55:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 594a6d12-070d-32d9-bd2b-b1f2e07137f1 | -7.86542 | -39.55855 | 2024-11-03 03:55:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6cc981f5-a0d8-34fd-9dc2-c62a393ec6b7 | -9.10822 | -40.29003 | 2024-11-03 03:55:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bdcb4c80-e49e-30ca-bbfe-bcb4a8627264 | -8.60852 | -40.54083 | 2024-11-03 03:55:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a43739d1-4dab-3289-8198-be2b3057bc57 | -14.26253 | -41.16678 | 2024-11-03 03:55:00 | NOAA-20 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3f942669-8f47-38e7-89b6-cfb024dcc6b1 | -7.32044 | -41.85822 | 2024-11-03 03:55:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7d9c5c29-b90f-3c91-ac39-17b88bb80210 | -6.92166 | -41.79739 | 2024-11-03 03:55:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a1454d60-4a16-30ef-8d96-908244662ade | -6.91802 | -41.79684 | 2024-11-03 03:55:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c11cf3cd-4d37-3af8-908d-21178ae0cec7 | -8.49534 | -42.09875 | 2024-11-03 03:55:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3eb130bc-ddbb-3174-bed7-6a9042b14ca8 | -13.58888 | -43.18583 | 2024-11-03 03:55:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fa0371e8-7ecb-32eb-8663-da5a7a4b24dc | -13.58816 | -43.19006 | 2024-11-03 03:55:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8330b86d-bf4b-39fd-adad-ce3e219758a6 | -13.56615 | -43.13504 | 2024-11-03 03:55:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 15f6f8b3-dc2d-3b52-a496-a0f8931b6d10 | -13.52898 | -42.5106 | 2024-11-03 03:55:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5523f6c6-1d4e-3bf1-aae3-6108b6258614 | -14.29768 | -43.07602 | 2024-11-03 03:55:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 09623f94-dd35-3539-b2b5-b19cceeec113 | -14.2749 | -43.03835 | 2024-11-03 03:55:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b59924de-fb91-3ddd-b0af-5e19970cc0f2 | -13.93089 | -43.35604 | 2024-11-03 03:55:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3408f358-0b92-37d8-943a-993cfe7fc5d5 | -13.88475 | -43.34333 | 2024-11-03 03:55:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b3000731-fd52-3281-8cc1-da58c9cb970d | -15.55157 | -43.17332 | 2024-11-03 03:55:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8cf352e6-5a37-3523-8964-0fae4459bfd5 | -15.38576 | -43.05856 | 2024-11-03 03:55:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 3.1 |
| eba52893-0d84-3c0b-959c-287756410679 | -15.23348 | -43.33556 | 2024-11-03 03:55:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 571b1d9e-dbdd-38e9-b004-4f88122eaf5f | -15.23134 | -43.32666 | 2024-11-03 03:55:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1ba99f27-b17d-3d44-8e5b-c4ba6cf0fcf2 | -15.23064 | -43.33079 | 2024-11-03 03:55:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 5.2 |
| ef6d3a6c-725f-368e-a2c3-aa514bf95fa5 | -15.2278 | -43.32602 | 2024-11-03 03:55:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 763245c8-87a7-3a5a-b6f6-4b26ccedffc8 | -15.21148 | -43.27187 | 2024-11-03 03:55:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 8c227eb7-ee58-35bd-ad28-e35652fff3e6 | -15.21078 | -43.27597 | 2024-11-03 03:55:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 34.6 |
| 11c2ade1-30cc-34f4-ac57-37cb6d91b3c4 | -15.20795 | -43.27124 | 2024-11-03 03:55:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 7.7 |
| f0870536-7eba-3c22-9e72-3ffa1384af51 | -15.20724 | -43.27534 | 2024-11-03 03:55:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 1565995b-70ba-3b57-9304-56cfd798b8ce | -16.34779 | -43.69685 | 2024-11-03 03:55:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 647a15e7-c4b2-396c-a7ea-e785969bff54 | -15.95527 | -43.55199 | 2024-11-03 03:55:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0b52c31-2d38-3a23-a8c2-994f51708794 | -15.95456 | -43.55617 | 2024-11-03 03:55:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d93c885-190a-3d39-b4c6-f34c2827839d | -15.72869 | -42.91903 | 2024-11-03 03:55:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4badcd4e-c3ec-36d6-abcc-2aa03a43f4cf | -7.87924 | -42.98354 | 2024-11-03 03:55:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4c594f1b-45cf-3b55-9e54-c670b6ca761d | -7.7143 | -43.76389 | 2024-11-03 03:55:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f2986937-2b92-386e-8119-0b69d6388201 | -7.66389 | -42.85459 | 2024-11-03 03:55:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 359dc5f1-eb7c-3ab7-b194-7bb65f2b993f | -7.66017 | -42.76464 | 2024-11-03 03:55:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e78302f3-7877-3c89-8fab-484b50044453 | -7.65998 | -42.76205 | 2024-11-03 03:55:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 13e1ef68-6bdb-3080-83d7-201575c13984 | -7.65983 | -42.78598 | 2024-11-03 03:55:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f262ec72-9721-3809-b1f1-15a9b54d05a8 | -7.65903 | -42.79068 | 2024-11-03 03:55:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5fede97b-dd00-3c72-b5a1-c88833b23ea5 | -7.65714 | -42.75934 | 2024-11-03 03:55:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ff446eb8-bc75-37fb-b233-72b520047329 | -7.65619 | -42.7614 | 2024-11-03 03:55:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1da9940f-dbb2-39e8-a3fc-5c583b70ca46 | -1.2755 | -53.4138 | 2024-11-03 03:55:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 52ab82ed-8d2e-329e-9b3c-ad44b06bac49 | -1.2755 | -53.3936 | 2024-11-03 03:55:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| c49c16d7-9539-35b5-b82e-f007da5f39dc | -1.2756 | -53.3734 | 2024-11-03 03:55:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 0b017911-694d-3046-a76a-f14b42e49b79 | -2.1746 | -53.6834 | 2024-11-03 03:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 7fe7a5a2-94c6-379b-afbf-d5eb33594e5d | -2.6322 | -48.5634 | 2024-11-03 03:55:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 82ea7368-d09b-37a3-8d21-69d3338642a2 | -2.7419 | -54.4353 | 2024-11-03 03:55:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| bd715d18-088b-3ceb-b8dd-9780b9cf34e6 | -2.7419 | -54.4153 | 2024-11-03 03:55:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 306031b5-039b-3292-ad9a-6a1913af84a9 | -2.7602 | -54.4349 | 2024-11-03 03:55:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| dab8451a-bc17-3704-b542-138c27fa0027 | -2.7603 | -54.4149 | 2024-11-03 03:55:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| ece77cca-18bf-3d22-b804-dbff503720c9 | -2.8148 | -49.1567 | 2024-11-03 03:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 52a3ae23-82bd-3cf4-a46e-172e2710b852 | -2.8333 | -49.1562 | 2024-11-03 03:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| fbb970c2-8540-3f66-aacd-1bb39406afb1 | -3.055 | -54.1474 | 2024-11-03 03:55:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 7648b323-9ac3-338a-9f85-35c8c5201b10 | -3.0734 | -54.167 | 2024-11-03 03:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| bdb104c8-0d0f-3741-9875-ad47beea267c | -3.0734 | -54.147 | 2024-11-03 03:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 159e1852-981d-3ec7-9acf-c4a37122758f | -3.0918 | -54.1465 | 2024-11-03 03:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 4538c4b4-2bdc-3f8b-a537-050e9f050cf7 | -3.106 | -50.2896 | 2024-11-03 03:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 23ecbf1d-3f3b-305b-9f37-35b9e921a2f9 | -3.1061 | -50.2686 | 2024-11-03 03:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 9992364b-5f3a-3a9b-8e4d-3eb5f36a0a75 | -3.1501 | -48.5689 | 2024-11-03 03:55:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 590397c5-7dca-3802-bd8b-85e3cc48a2fb | -3.4749 | -50.3826 | 2024-11-03 03:55:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| caba7846-70e2-33dd-827e-3837bb06eff1 | -3.9474 | -48.3451 | 2024-11-03 03:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 8ee94f0a-1786-3916-b752-10f64a0224f3 | -3.967 | -48.15 | 2024-11-03 03:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| e16b2b8b-06b4-3bc7-a517-6c71901346a9 | -6.5239 | -41.4929 | 2024-11-03 03:55:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 0055c35a-0aac-3043-b1bc-3386286228d1 | -22.08249 | -43.07072 | 2024-11-03 03:57:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7f6d9265-d4d3-36f8-96d3-c0432e3d2ca0 | -22.07854 | -43.07384 | 2024-11-03 03:57:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 520facf1-b419-3404-8825-e671933f3f12 | -22.07684 | -43.06992 | 2024-11-03 03:57:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3d18f555-ac54-31c6-9798-81f009178514 | -22.07412 | -43.0655 | 2024-11-03 03:57:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1f3000d1-5e6b-3cdc-bff7-ea7cc4e20593 | -22.07351 | -43.06928 | 2024-11-03 03:57:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7914d783-b6aa-32a3-bcce-c646b67b6f1d | -22.85574 | -42.97937 | 2024-11-03 03:57:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 282b8545-b6ba-30ce-a742-3ff8e5faaf97 | -21.6032 | -44.22715 | 2024-11-03 03:57:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bbfd6f05-4d50-3138-81ff-e36f47dd84fd | -21.59976 | -44.22647 | 2024-11-03 03:57:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 55a71fda-2c2f-34cc-b504-2a52c63f3f2a | -21.18948 | -44.68657 | 2024-11-03 03:57:00 | NOAA-20 | NAZARENO | MINAS GERAIS | Brasil | 3144508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 94fb9f18-1553-3e2c-b64b-153da5eba02e | -2.7218 | -49.3295 | 2024-11-03 04:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 2ae3b0b0-9d2e-3215-af67-dc3b0cd7a599 | -2.6507 | -48.5629 | 2024-11-03 04:05:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| b6d32f0b-48d0-39ad-b9b7-9d302bebf853 | -2.7419 | -54.4353 | 2024-11-03 04:05:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 0e78b1e4-4dc7-30c6-a5d5-fc0617f2177d | -2.7603 | -54.4149 | 2024-11-03 04:05:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| a9f06a0b-9062-3866-a0a1-18a9d74c5727 | -2.7602 | -54.4349 | 2024-11-03 04:05:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 3c94939e-94d6-3de1-aba6-d0a1d35379f0 | -2.7419 | -54.4153 | 2024-11-03 04:05:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 26253faa-baeb-3862-a00b-b116f417d879 | -2.8148 | -49.1567 | 2024-11-03 04:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 60eb95d2-ae53-3802-a218-5de3c77bda4a | -3.055 | -54.1474 | 2024-11-03 04:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 2a74dc0e-08fd-3c26-9b5f-99f3443d7f03 | -3.1501 | -48.5689 | 2024-11-03 04:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| b0d1c83c-6b4b-3bbd-a90c-15e12557391f | -3.1245 | -50.289 | 2024-11-03 04:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 5e910914-ebc1-3218-8d91-82f1516cc43f | -3.1061 | -50.2686 | 2024-11-03 04:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 336b5fee-346b-38d7-8919-92db3f4c83f3 | -3.106 | -50.2896 | 2024-11-03 04:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 07dcbc2b-cf84-3897-9a61-2a9ad587d4d7 | -3.1059 | -50.3105 | 2024-11-03 04:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 467900f7-4bab-38dc-ae37-1d56ae656739 | -3.0918 | -54.1465 | 2024-11-03 04:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 7c4117fd-c0f7-311f-adc6-488d874ff693 | -3.0734 | -54.147 | 2024-11-03 04:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| e78c38bf-d489-3e70-9e8c-48977c622bcd | -3.0734 | -54.167 | 2024-11-03 04:05:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 21d2cc14-35cd-3fdf-885e-f9cf35c3f099 | -3.4749 | -50.3826 | 2024-11-03 04:05:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |


[Clique aqui para ver as próximas entradas](README29.md)
