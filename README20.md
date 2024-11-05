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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1648710a-0238-3782-b2a1-a1de7ecc40a2 | -5.02354 | -46.08461 | 2024-11-05 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 213d4930-45c1-376f-9131-9df2481d0846 | -3.03763 | -53.27731 | 2024-11-05 04:08:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11d2c42e-072b-3c6a-8ad1-6a4063823fee | -5.34327 | -41.61205 | 2024-11-05 04:08:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 963e07ca-6ec8-385d-910c-3258a7d3afc7 | -5.47174 | -42.82461 | 2024-11-05 04:08:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e26002bc-665b-3286-9554-16bb9b0bb934 | -5.5822 | -41.67113 | 2024-11-05 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b9a03709-4607-38a5-84db-615244ded03d | -6.10564 | -43.96078 | 2024-11-05 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 89cab4e7-6ab7-31d2-94ef-fc8750bba646 | -3.5446 | -47.3855 | 2024-11-05 04:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 251.2 |
| e09199ed-133f-3f6a-bd7f-d727f3a7b6fe | -2.82 | -52.9409 | 2024-11-05 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 650ef96a-cdcd-34ff-9b62-e93f1a0a36a3 | -3.5444 | -47.4073 | 2024-11-05 04:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 094ac390-5bd3-38e2-b8d1-083e00f89148 | -3.5631 | -47.3847 | 2024-11-05 04:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 338.9 |
| ca5a1a42-6af5-3ace-9219-a6ee04d4a87b | -3.5632 | -47.3629 | 2024-11-05 04:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 806dcb13-ca33-3f1a-a718-31a8ab4cb276 | -3.563 | -47.4066 | 2024-11-05 04:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 1850a573-73ac-35dc-ba87-db5b4a540663 | -2.6691 | -48.5624 | 2024-11-05 04:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| efab2799-7054-3c8b-af17-d1d09da9595e | -6.1041 | -43.9593 | 2024-11-05 04:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 3ea034a0-bb90-3ec6-a8ab-ecef2bcd6516 | -3.5447 | -47.3636 | 2024-11-05 04:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 3d68bf1f-346a-35c3-8307-ddbd45d88718 | -2.6507 | -48.5629 | 2024-11-05 04:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| af4debd4-e1fc-3e37-96eb-02965e17a2c0 | -2.6506 | -48.5844 | 2024-11-05 04:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 7f11b852-f4fb-390a-847f-87d7c45aaf9d | -9.18604 | -44.21981 | 2024-11-05 04:10:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61116b07-b87d-3f4f-b568-3e5080fbea2e | -12.59217 | -45.46284 | 2024-11-05 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 338faa05-fa86-3b6d-b277-13010653721e | -13.77313 | -42.70971 | 2024-11-05 04:10:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1b0e40b7-0276-306a-9865-93f9b9cc3a4d | -10.87075 | -49.10817 | 2024-11-05 04:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4d5035fb-f4a5-3aae-b6e8-fbf632e03c4e | -12.03508 | -43.94274 | 2024-11-05 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 143e431a-3f95-33c9-9805-760ea24c2bfc | -13.40705 | -44.45234 | 2024-11-05 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c90cd44-abee-3217-b31d-0dbaa16a2194 | -11.53196 | -45.02468 | 2024-11-05 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| baf90b05-c10c-3a78-876b-8b28d81d5458 | -12.62861 | -45.5536 | 2024-11-05 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 54c93e45-1064-32ce-9184-4e4bd378c2a8 | -15.21104 | -43.28204 | 2024-11-05 04:10:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bce03dd3-7846-3063-a311-7279595046b3 | -11.25326 | -43.21019 | 2024-11-05 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68cecdd4-0504-3cd5-bc43-72722e93d193 | -12.74623 | -41.82521 | 2024-11-05 04:10:00 | NOAA-21 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a262ce0e-d2a9-383d-83d2-8104692dc939 | -10.00193 | -43.80265 | 2024-11-05 04:10:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d68da03b-5fb5-34a7-ac6b-7292277063ab | -12.16717 | -44.62325 | 2024-11-05 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a19a8e06-3fd1-3db3-9c8a-c13dbae8c855 | -13.48182 | -44.02793 | 2024-11-05 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9f8db35f-d3c3-3e63-ba7b-1d06c7f14f52 | -10.11875 | -43.90353 | 2024-11-05 04:10:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1c22080f-2587-3dc9-af72-b5ac1d9d59ad | -12.27464 | -43.52945 | 2024-11-05 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66dab99c-bac9-338b-aace-a368b6b556e8 | -12.62928 | -45.54963 | 2024-11-05 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b43abd70-84b7-3a06-9c27-79527cd38c69 | -12.15978 | -44.62583 | 2024-11-05 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc404514-b8e1-3b82-baac-435caebeda9c | -11.24436 | -47.91016 | 2024-11-05 04:10:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bdeaa8da-68a7-3732-8d58-ee6a4673a8d4 | -13.41033 | -41.32818 | 2024-11-05 04:10:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 94cf223b-1b55-3e24-8ac1-3c456c2fad89 | -12.59282 | -45.45889 | 2024-11-05 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50faf80b-7bca-357d-a3e7-6fd76abbf07d | -13.76007 | -42.8167 | 2024-11-05 04:10:00 | NOAA-21 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e59e72ed-e70e-3ab6-8f52-fa2efc73fb6a | -12.58998 | -45.45436 | 2024-11-05 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c74533bd-9c8c-3708-a300-2b481fdca049 | -12.62795 | -45.55757 | 2024-11-05 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dbd7c307-5b18-39d0-863f-54688f114cf1 | -10.0996 | -36.1913 | 2024-11-05 04:10:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 7ad9a63e-4441-35ae-ab5b-cc7c9430b56c | -10.10454 | -36.18766 | 2024-11-05 04:10:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 0ce647d7-e5cb-3246-8e1a-eb084558b6c4 | -8.66195 | -44.02818 | 2024-11-05 04:10:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d286cf20-4657-3868-9a36-d988d82eab07 | -9.86908 | -36.4138 | 2024-11-05 04:10:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 84bac34d-b0b1-3d44-ba72-cda392be414f | -12.17056 | -44.62382 | 2024-11-05 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 61e9d3e8-31fd-30f8-878f-902ce7753dc6 | -11.52443 | -49.07698 | 2024-11-05 04:10:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a1a2436-2301-3219-b7b6-722eaf8916c3 | -8.76258 | -44.07911 | 2024-11-05 04:10:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 335a9c15-6f01-3ae3-be52-ee13204252e8 | -11.52522 | -49.07257 | 2024-11-05 04:10:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 848980f0-ca65-3ed3-860a-4dac2fa87b7f | -9.86962 | -36.40974 | 2024-11-05 04:10:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 2f6b5df4-6177-35fe-8e2b-c31f3137f08b | -10.22868 | -42.45673 | 2024-11-05 04:10:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a2b00bf4-fda3-3dfa-aaa1-c8633c395202 | -10.2826 | -42.4367 | 2024-11-05 04:10:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c7d680e5-6477-3e0e-a2fe-a4a854836e3a | -9.56321 | -37.80643 | 2024-11-05 04:10:00 | NOAA-21 | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ced428f9-a671-3b74-98ec-1d1efa0f6253 | -12.22415 | -44.6859 | 2024-11-05 04:10:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d999ef92-505d-33b8-a8de-5160a14fda8d | -15.0231 | -42.28512 | 2024-11-05 04:10:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0fe21ac7-ddd5-3512-9800-7354589f6617 | -11.7552 | -44.22008 | 2024-11-05 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdfa3157-641a-3ca8-b516-edf44d5c7480 | -10.10019 | -36.18706 | 2024-11-05 04:10:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 87f1e0da-659c-39c3-9b66-783d5658cd79 | -11.8591 | -43.87378 | 2024-11-05 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 01d54f17-dbaa-3aeb-b99c-c7aec60f1376 | -12.62579 | -45.54905 | 2024-11-05 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ee8cb68-5ccf-3d85-9040-f316027314b4 | -8.76076 | -44.09038 | 2024-11-05 04:10:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b423bc9-baf4-3589-aafb-e97bb6a05716 | -12.77916 | -43.92992 | 2024-11-05 04:10:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34e0aa2e-cc7b-32d2-a885-c0608b08cbcd | -12.161 | -44.61838 | 2024-11-05 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 260c2cb0-bc94-329e-8b7b-c9935af93112 | -12.16439 | -44.61895 | 2024-11-05 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f4da61a-4ac9-3e68-9203-67e28cac6b4d | -12.74678 | -41.82157 | 2024-11-05 04:10:00 | NOAA-21 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7e876f34-2d41-30a0-8475-5c2737e194e5 | -11.98839 | -42.90557 | 2024-11-05 04:10:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4a5c82e0-5aef-37d1-a6e3-743cec869eae | -12.27409 | -43.53299 | 2024-11-05 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ce6a913-e946-34e1-a890-d0a5649b21d8 | -13.63646 | -44.50867 | 2024-11-05 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82c7a593-7028-34fe-8273-49c63cb4a79f | -9.10575 | -43.19135 | 2024-11-05 04:10:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b2c309d8-8db8-3824-9dbc-968394532b56 | -12.33151 | -43.77155 | 2024-11-05 04:10:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8bc7adb-55b4-33c3-9417-1a51cfffeb29 | -13.60415 | -43.07784 | 2024-11-05 04:10:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 77e41a66-a7ee-3f2f-8883-caa47ac2516d | -11.13273 | -43.30627 | 2024-11-05 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 290f383c-cc42-341a-bd0a-b152abd8f6df | -11.13329 | -43.30275 | 2024-11-05 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 95289cf7-a396-349d-9eaf-03d5a1015501 | -9.79749 | -43.86992 | 2024-11-05 04:10:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a95ed711-22c4-31c0-8f4d-bc834914e2c0 | -10.51271 | -44.16301 | 2024-11-05 04:10:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0f309a7-eb55-341e-9de9-ce2fef8d541e | -12.03842 | -43.94329 | 2024-11-05 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf8ce20e-d4db-34fa-b68a-e833761e9b5a | -12.58933 | -45.45831 | 2024-11-05 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a4f23e1-cde9-30c3-9ef2-266399b17fc0 | -9.10242 | -43.19081 | 2024-11-05 04:10:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e1cdc7b1-8c65-3e73-b116-7c8354ef49d5 | -9.79133 | -43.86518 | 2024-11-05 04:10:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f43694b-9b76-3d72-80b2-84d300dea063 | -12.59347 | -45.45494 | 2024-11-05 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca1915ba-767d-3279-be77-99fdfa807e09 | -9.87056 | -36.41063 | 2024-11-05 04:10:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| b0f6ae20-df56-35b4-9d85-223e9375a56d | -9.78906 | -41.7831 | 2024-11-05 04:10:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 252d4556-1a5b-395e-812f-4049b479b3bd | -9.79237 | -41.78362 | 2024-11-05 04:10:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| a3776645-1ede-3cf7-8303-a6a824c71afc | -11.86244 | -43.87432 | 2024-11-05 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 16cf546e-6d5c-3881-aefa-46e08ce5dca3 | -9.24028 | -43.20247 | 2024-11-05 04:10:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a498a0ee-3015-308e-8214-09d911c0b5bf | -10.89233 | -43.04 | 2024-11-05 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85533609-467b-3c5b-a336-5e6aa02b87d7 | -13.58309 | -43.9896 | 2024-11-05 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb72b403-cfc9-3d1f-8a7c-3bda213a2076 | -11.98563 | -42.90153 | 2024-11-05 04:10:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8ea4edb7-8ed3-338e-a679-faa2f3c3db3a | -11.98178 | -42.90451 | 2024-11-05 04:10:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f00762f9-d0f7-313b-83f7-390f4c175e6f | -10.00251 | -43.79905 | 2024-11-05 04:10:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ba197feb-52cb-39d9-ab43-b74096af780f | -12.47062 | -43.71034 | 2024-11-05 04:10:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55cb24b4-34a5-3e87-a50c-a784a521b3c6 | -14.59487 | -43.15577 | 2024-11-05 04:10:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0258ecf2-8495-3b3e-b4ea-84b9bba2e322 | -11.89316 | -40.92708 | 2024-11-05 04:10:00 | NOAA-21 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dc52e0c1-6771-3f81-b8a3-e9e546ad698d | -11.86187 | -43.8779 | 2024-11-05 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 53ce06df-d42d-380e-b714-61a8f3dfe847 | -10.00645 | -43.79598 | 2024-11-05 04:10:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 524c33bb-3433-3066-beb1-58505062eaa9 | -11.36377 | -44.93812 | 2024-11-05 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4cd10122-5b54-3fe3-88de-6047ab16e7fa | -10.27929 | -42.43618 | 2024-11-05 04:10:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f14e581f-d5dc-3676-b98c-1abc836469a2 | -12.16318 | -44.6264 | 2024-11-05 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 571ac689-9804-3229-9e50-49536b3f4ba7 | -10.34946 | -38.02179 | 2024-11-05 04:10:00 | NOAA-21 | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fc1235ef-0daa-3ce3-9b3b-358e3159e0a6 | -13.45461 | -41.33497 | 2024-11-05 04:10:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e06ddea3-ae96-3712-87ea-069b8db02fde | -10.10394 | -36.1919 | 2024-11-05 04:10:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |


[Clique aqui para ver as próximas entradas](README21.md)
