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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 411662dd-8d70-307b-85e9-dee165bac0c2 | -11.70039 | -44.3554 | 2025-09-24 04:51:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50342a32-961b-3592-bb4b-b15f0bf93d36 | -11.52175 | -43.66963 | 2025-09-24 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dbb9d6a0-c645-3672-89a4-ef207340880d | -6.41475 | -43.0849 | 2025-09-24 04:51:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| bfeb48ac-90fd-3812-a447-bb24ced5232a | -3.79173 | -52.41046 | 2025-09-24 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51f6f86e-cd38-3f92-b26c-cb657a0cecd8 | -4.11779 | -49.10334 | 2025-09-24 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2ed6f5c-be0b-3130-baa4-024fe2426f1e | -10.18824 | -54.27894 | 2025-09-24 04:51:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c51c6d2-fd62-373a-973c-e2f52d13960a | -5.6452 | -43.60955 | 2025-09-24 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89924439-07e9-30f0-a868-99b982804cd4 | -11.52796 | -43.66622 | 2025-09-24 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 434e82cc-2f3c-34a4-863b-361f9a42b7d1 | -6.25682 | -46.1183 | 2025-09-24 04:51:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d36bfb4c-d3ce-3e27-a1e0-ada40179fee3 | -8.43795 | -49.57594 | 2025-09-24 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1da61b35-9ce5-3ed3-bc93-50676908e20f | -5.63809 | -45.94876 | 2025-09-24 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb981575-bb67-39e0-b7c4-08acefffd2bf | -7.82777 | -47.86035 | 2025-09-24 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dec53499-b8e5-3eaa-a4a9-aa6827ee8365 | -12.01619 | -47.78773 | 2025-09-24 04:51:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 557758ec-1f36-3ce2-925b-a8f4b6ea3d4b | -6.11602 | -41.79053 | 2025-09-24 04:51:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 299f3fb8-98bd-37f2-af27-0d8995861c90 | -5.18185 | -46.12255 | 2025-09-24 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| baa9640a-e848-3d2e-89f2-90096709950f | -3.71917 | -53.30248 | 2025-09-24 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 886df889-1195-39de-b92d-6844ae7168d3 | -4.56765 | -48.02322 | 2025-09-24 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25c17498-480c-3157-b263-9af0b21668d0 | -7.77342 | -46.19532 | 2025-09-24 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| afd4cf50-8e81-35b9-9d07-1343a682fa38 | -11.51654 | -43.66512 | 2025-09-24 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3dd22e40-cb0e-31db-a1cc-ba609e90ba8a | -7.80372 | -43.17933 | 2025-09-24 04:51:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 13b58610-503a-31c4-9d12-b2869b1bab5f | -9.58375 | -47.59092 | 2025-09-24 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ed51077c-36fe-3b91-8ad1-53a5e5edbc64 | -11.6806 | -44.38166 | 2025-09-24 04:51:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5879f724-0980-32ab-8b89-6c8117916b3b | -5.30559 | -44.998 | 2025-09-24 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 719373ee-a6c1-3422-9552-61862e6aa069 | -8.1716 | -46.2653 | 2025-09-24 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a292e73-2a32-354e-b541-c74a1b79d99d | -5.30085 | -44.99718 | 2025-09-24 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b2add71d-371e-3711-a1e7-aab819ca1600 | -7.27776 | -42.98838 | 2025-09-24 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4652e1b0-07ec-37a6-9e2c-5b0f922045ac | -4.31529 | -48.10055 | 2025-09-24 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c6279c1-51b4-37c1-8c42-25877fa02d0e | -5.91552 | -43.85898 | 2025-09-24 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 06bfc9d2-8f5b-38fc-962d-700f48d4922a | -11.51705 | -43.66107 | 2025-09-24 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a3b5bd2f-c99d-35e1-865f-205470339901 | -3.8166 | -51.26794 | 2025-09-24 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ed18b3d-ec22-33a5-8afb-af97604d1a2f | -9.10942 | -48.89717 | 2025-09-24 04:51:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42aa0879-edb1-3fc7-96d3-f92803cda220 | -5.1571 | -45.24502 | 2025-09-24 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85e88bec-a120-3ea7-9a47-19902a9834bf | -8.16864 | -46.24463 | 2025-09-24 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5cbc5eee-c718-3b3b-8e0f-e4a675ea122d | -8.68455 | -44.0246 | 2025-09-24 04:51:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fcdd5d8d-1720-365c-b43b-e8b50d6c73dc | -5.63473 | -45.9513 | 2025-09-24 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5961485e-fe59-3ea4-890b-4d8b9300be60 | -10.58847 | -44.07561 | 2025-09-24 04:51:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c5bcd03-44f3-33e8-a89f-348802a557d3 | -10.74252 | -48.17868 | 2025-09-24 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e7ebcb83-bd65-31a2-8553-ce565011c48d | -4.39436 | -47.28249 | 2025-09-24 04:51:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7c37b62-e667-3381-8af4-08b2cbe207c9 | -5.63074 | -45.72823 | 2025-09-24 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9ed82b21-a898-3e1f-bb9b-8ec417234018 | -5.51871 | -43.86526 | 2025-09-24 04:51:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 87feee84-829f-39ed-bfad-8ddaa59fd259 | -11.66929 | -44.38377 | 2025-09-24 04:51:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e710e556-7756-3478-bd38-ba1a810480c6 | -3.80746 | -51.34848 | 2025-09-24 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc5355ae-c82b-32b3-aa19-3f32ceb94046 | -10.62875 | -49.06256 | 2025-09-24 04:51:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4b67709-bcea-3c74-a207-a77ce7e9789f | -8.53051 | -45.01688 | 2025-09-24 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f3661bb-2adc-38f3-ba75-86c9d5bd00a0 | -9.11399 | -49.62707 | 2025-09-24 04:51:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa4d835a-1820-3136-b488-b5ccf330f6fc | -4.59214 | -49.6763 | 2025-09-24 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cb1cd61-00d2-3cf5-a812-d5e5e33bf7ba | -5.63958 | -43.91823 | 2025-09-24 04:51:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 959f8c62-db5e-3840-a785-cdfad121fded | -5.91597 | -43.85583 | 2025-09-24 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5daf0e43-cdfd-3e8f-b51c-afd846e21371 | -11.81593 | -45.31502 | 2025-09-24 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 25560527-471d-3a34-baa8-9175bc3c9611 | -5.52385 | -43.86618 | 2025-09-24 04:51:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 36e37855-7c0e-364e-92ac-961e37bd2985 | -5.46812 | -44.68924 | 2025-09-24 04:51:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef447a06-4a1b-3c9f-bf55-08db4c17f435 | -6.41925 | -43.093 | 2025-09-24 04:51:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| c5b49348-a183-3d81-8318-839cd3a0dbf1 | -7.38466 | -47.04036 | 2025-09-24 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1d925c2b-fa72-37c3-b21e-61d40daea915 | -5.88741 | -49.6374 | 2025-09-24 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7205d7d-2209-3571-bfcb-2845f33db6bd | -3.79646 | -52.09432 | 2025-09-24 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b801057-8c19-3195-9ee6-840a43fdc8ca | -11.63641 | -44.3667 | 2025-09-24 04:51:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1955ce36-a684-3823-a4b5-97a70872c258 | -5.60275 | -45.36448 | 2025-09-24 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e6ab5900-95ca-3c77-b48a-8b299ebf7b97 | -8.78974 | -43.03303 | 2025-09-24 04:51:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f70a02b7-b2a1-302d-bfa2-59f8fb09f104 | -3.78732 | -52.30364 | 2025-09-24 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cc2ffb8-9894-30e4-90a5-9428f60ed829 | -5.94095 | -42.9262 | 2025-09-24 04:51:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 81624f95-b88a-3471-919c-b4bab88ff6d6 | -11.41179 | -44.95888 | 2025-09-24 04:51:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b7ad544-a816-3425-a6da-86a00a8570b3 | -5.76742 | -42.60087 | 2025-09-24 04:51:00 | NOAA-21 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c9d46f26-b4f3-3439-8641-540b462c2ab8 | -7.64826 | -46.01488 | 2025-09-24 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6589d791-e7ec-3d25-bc6c-dd22c89a6263 | -6.3756 | -46.42313 | 2025-09-24 04:51:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2002344-41ff-3b71-afcb-1526aedb04db | -8.68623 | -44.02452 | 2025-09-24 04:51:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| adc2f56e-daf7-36e3-86eb-cf5e4226c4c8 | -12.07554 | -44.77913 | 2025-09-24 04:51:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 032f7acc-a56d-3765-96b3-deb06daa1e01 | -11.00864 | -44.50331 | 2025-09-24 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 307305f7-4f3d-3cf9-82d2-6fa5b61e2f7a | -7.49407 | -47.547 | 2025-09-24 04:51:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19e7ce21-e74a-3601-b455-91cf09859c83 | -5.38808 | -42.26933 | 2025-09-24 04:51:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2629ae9a-733e-395f-9038-045c057e5927 | -5.64038 | -43.60553 | 2025-09-24 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd280cb4-eb0e-34bd-8b0b-558ccf14379a | -5.63921 | -45.95191 | 2025-09-24 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b06e3034-0b00-39ad-8d21-70ff6754264c | -11.63134 | -44.31886 | 2025-09-24 04:51:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21c63b0c-f8ff-35ac-857c-16d3c7b1b1a5 | -7.76829 | -46.19895 | 2025-09-24 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 77ce6e45-16b9-3b85-97b7-5a769463803c | -8.5293 | -45.02573 | 2025-09-24 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d6425626-695f-3179-b33a-78cbdc84b605 | -10.09863 | -55.86355 | 2025-09-24 04:51:00 | NOAA-21 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 532fb1ad-b429-3602-b480-e5aea13fcd6c | -5.51784 | -43.87153 | 2025-09-24 04:51:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 855e89f9-023e-3a8b-a168-8a30ea325eea | -6.66554 | -47.74801 | 2025-09-24 04:51:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b9a1d03-1397-36ad-907b-d4ba8e53b629 | -7.50114 | -43.67469 | 2025-09-24 04:51:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c127648b-e380-3338-a9ec-75e6befa5ef5 | -11.66886 | -44.38733 | 2025-09-24 04:51:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d22784e8-c278-31fd-92f3-ce922ccb3482 | -8.18542 | -46.36776 | 2025-09-24 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c6fda7cf-df2e-35cd-89c4-3e40a5466940 | -7.36761 | -47.03797 | 2025-09-24 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8546b4f3-2932-3193-b216-837003a58e7d | -9.64152 | -48.56318 | 2025-09-24 04:51:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b723308-179c-3111-b182-61fad59dd294 | -9.73751 | -46.66488 | 2025-09-24 04:51:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 61ff262f-26b5-330a-99cb-638940a980d1 | -6.42523 | -43.09032 | 2025-09-24 04:51:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 218339f2-d7a8-3eef-a50c-30ca77413ee0 | -5.92142 | -43.92819 | 2025-09-24 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 050bd500-ddb1-3b43-8ae2-45e1f0fda03f | -8.17472 | -46.24215 | 2025-09-24 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6395a1b-a215-36d4-942b-9437fb8b50b8 | -8.17649 | -46.36569 | 2025-09-24 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0923814f-3e31-39b4-b1cf-2a0e02f45106 | -7.17561 | -42.24376 | 2025-09-24 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 36877138-f5b3-397a-8b6e-899b5a3c9766 | -10.58801 | -44.0792 | 2025-09-24 04:51:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e921f0f-040b-3ff3-961e-c295bfad2db9 | -10.97516 | -48.33326 | 2025-09-24 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11801715-53a4-3d5d-814b-7fe92aa95b35 | -7.76892 | -46.19439 | 2025-09-24 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8f9f6af4-b591-3fbe-94e2-707a164194c7 | -11.63097 | -44.36596 | 2025-09-24 04:51:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46725571-b5a7-3345-80c8-18e9dcfa01ed | -3.79016 | -52.32863 | 2025-09-24 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bc3f214-b012-30db-be69-9922039a26ee | -7.82424 | -47.85617 | 2025-09-24 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71c868f8-0c96-30da-91cc-cc626dd8e70d | -5.17176 | -45.43214 | 2025-09-24 04:51:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 001e32e1-cad7-3b19-8ccc-c35160bcfa2f | -8.55343 | -44.96095 | 2025-09-24 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3fd9b8b9-fbbe-31f9-b214-da1e7dc108fa | -10.94751 | -45.59558 | 2025-09-24 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d1ce1807-560b-3e7b-9bc8-5fd66dfba986 | -10.17459 | -55.39119 | 2025-09-24 04:51:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fc7268ad-becd-3f26-abdc-408e4c4eb938 | -7.28144 | -41.8647 | 2025-09-24 04:51:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 78a733e6-30b3-3e17-94bb-d4e42cf681a9 | -12.06696 | -44.80502 | 2025-09-24 04:51:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README15.md)
