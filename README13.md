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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a613007-63e5-3ff8-8caa-63562e6bd94f | -3.2344 | -50.4952 | 2025-11-17 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 93fc4563-29f0-3c6a-90c6-210f5983f191 | -10.8597 | -46.739 | 2025-11-17 03:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| d449f3f1-41eb-3a58-9632-d8de300c70ab | -6.6875 | -42.0296 | 2025-11-17 03:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 84.9 |
| 9fe1f548-8773-36a0-91fa-924ad4c035b0 | -12.7189 | -45.4074 | 2025-11-17 03:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| a11180c9-d335-37d4-8ccf-921b8aaf2f30 | -5.0401 | -43.5973 | 2025-11-17 03:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 464a0ea3-575f-36bf-afdf-708e7b999551 | -3.2344 | -50.4952 | 2025-11-17 03:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| a1777ddc-c066-3233-b846-f832f62163fc | -6.37071 | -42.20941 | 2025-11-17 03:46:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7c08dbdd-4c05-3dd9-8c3c-1597c36d6174 | -8.28257 | -41.43039 | 2025-11-17 03:46:00 | NOAA-20 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c7881cd8-afd9-3728-b0db-bc7ff7a8d8a2 | -5.33503 | -43.03755 | 2025-11-17 03:46:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b4089d9a-8820-3219-a100-6fc7cd523095 | -4.12474 | -47.29426 | 2025-11-17 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f500ed47-9db8-338f-9ce4-e7e3fe48145d | -3.80561 | -48.92525 | 2025-11-17 03:46:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 61dee2bd-ff4a-3449-ae31-0abc1047cca6 | -5.20245 | -43.29435 | 2025-11-17 03:46:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2442b057-bc4c-35e1-b17d-d57dd55d1b35 | -5.88172 | -46.44997 | 2025-11-17 03:46:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 943f33fb-c3b1-3457-adee-adc774f374bd | -6.7734 | -41.45044 | 2025-11-17 03:46:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cfc8e6a9-4b24-36e9-819f-ff8e4f4b2d56 | -4.65696 | -46.74462 | 2025-11-17 03:46:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 31c9c5ef-db63-329e-9a5c-9c81f5d78e63 | -6.06375 | -41.64917 | 2025-11-17 03:46:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b8747ad3-ddcd-3d73-b687-9b5aad541529 | -8.11896 | -43.5302 | 2025-11-17 03:46:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 78f92001-9704-3da5-a557-385e38f7ef7e | -6.85648 | -42.85627 | 2025-11-17 03:46:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e5e6b5a0-5611-34a1-bc2a-ba369b5384fe | -6.08277 | -41.60942 | 2025-11-17 03:46:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8b430928-f8a2-310c-bfee-16edc1f8928c | -5.49437 | -39.16804 | 2025-11-17 03:46:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 3a52d777-adbe-382a-88db-6b9d95b08a4a | -6.68926 | -42.04942 | 2025-11-17 03:46:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 82d1ac8e-ddde-3e1c-a6aa-2b35866e6670 | -6.68068 | -47.38844 | 2025-11-17 03:46:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ade6f863-eb55-3e6a-8686-eae99d488e04 | -6.68094 | -47.39017 | 2025-11-17 03:46:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7cd6d9d3-d66a-3215-af92-e064670d930e | -5.83498 | -48.84359 | 2025-11-17 03:46:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6375fcb1-1572-3c88-92a8-9eeed743e99f | -4.11104 | -47.30157 | 2025-11-17 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe86ab00-5cc3-360f-af43-7e4c05ef949d | -6.54208 | -42.20342 | 2025-11-17 03:46:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e197de80-950a-3d81-a895-35d8fb844ce1 | -7.0907 | -42.73052 | 2025-11-17 03:46:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5a533bba-32f9-3cc7-a804-6147305609e7 | -4.69737 | -46.31722 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a02f613d-da41-3ba8-ae2e-61a4a3efe999 | -5.46508 | -40.9701 | 2025-11-17 03:46:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5164ea47-e5f0-3d37-9a7f-87c0525da215 | -4.72606 | -46.38414 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bea4cf27-d0a2-3d81-93e4-27373e2b9d20 | -4.74572 | -46.40438 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19a78342-e246-36b9-b218-a9d1aff2db21 | -5.53847 | -41.76635 | 2025-11-17 03:46:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d0187e36-44c2-3ec7-a3fc-a9cb5dab24ef | -7.49204 | -38.40597 | 2025-11-17 03:46:00 | NOAA-20 | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2e608ac3-7144-3ea1-abc5-79b419eb0493 | -5.79422 | -43.99284 | 2025-11-17 03:46:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74947281-05ff-343a-bf02-69a9f1fce22f | -3.7767 | -49.26046 | 2025-11-17 03:46:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 56584513-0b3c-30b5-8143-485e8d31f047 | -5.0326 | -43.607 | 2025-11-17 03:46:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| e1b5242b-dcf0-3aef-980b-8b171f142d5f | -8.27796 | -41.4344 | 2025-11-17 03:46:00 | NOAA-20 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6bb560a9-300c-3b0f-ac5e-17fca09129a9 | -7.08513 | -42.73765 | 2025-11-17 03:46:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 182c4ba2-f104-3ccb-afed-17b1d25b6ab8 | -5.3247 | -43.04464 | 2025-11-17 03:46:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 710271e2-e8a3-3b02-946d-ccec734578b1 | -5.83597 | -48.83813 | 2025-11-17 03:46:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7f4e5c2a-5558-3aa6-94f8-134d7703cfa8 | -4.9393 | -44.53359 | 2025-11-17 03:46:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2c89a98-b4ba-3f46-b6f8-d1690671db1f | -7.1279 | -47.12853 | 2025-11-17 03:46:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8519749-c9bd-3234-89f4-1caa6dcc9dd9 | -7.06106 | -42.245 | 2025-11-17 03:46:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ece16a61-24c3-3183-b07a-d7552f9fc2c1 | -4.73654 | -46.39051 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1427821b-2a83-359c-a8d6-27e54d116bbb | -4.99916 | -44.36092 | 2025-11-17 03:46:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 26a13d7d-23ab-3b37-8f2c-08362cf3d422 | -6.71605 | -42.93975 | 2025-11-17 03:46:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 6cd170cd-3cdb-3f5c-8b82-f4c5ef46f210 | -6.70386 | -40.79692 | 2025-11-17 03:46:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 21b0cd70-8e92-31bd-b4ec-84feae8724cf | -5.04188 | -43.60855 | 2025-11-17 03:46:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| b75a7884-ba72-3a0c-88fa-8e274d48c04e | -6.74052 | -42.95233 | 2025-11-17 03:46:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 885c553b-e4f5-307e-9b16-c6b9aa41b751 | -6.57861 | -35.1235 | 2025-11-17 03:46:00 | NOAA-20 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 826b8e21-10dd-39c5-9693-0bd1e378e1ed | -5.33577 | -43.03313 | 2025-11-17 03:46:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 6c5f8f58-fe24-342a-96e5-75a5d04cf317 | -4.72117 | -46.37896 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ea19c4f0-4ada-3ce1-a21b-b0bdee96101e | -4.09887 | -47.11063 | 2025-11-17 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2bbd37d-ce64-370b-a9b3-0bdb5763e0cb | -8.11422 | -43.53033 | 2025-11-17 03:46:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 64a07d60-7635-36e3-b56d-9c85e37f6983 | -3.46164 | -49.99961 | 2025-11-17 03:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a2b5853-9c10-3303-99fe-e6b41f22211b | -7.83258 | -39.52444 | 2025-11-17 03:46:00 | NOAA-20 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 378f51ff-ff07-3da3-bff3-db7173c8c2af | -5.2613 | -46.10939 | 2025-11-17 03:46:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf426dc7-f128-32bf-b8a8-04ba20450caf | -6.33645 | -41.76023 | 2025-11-17 03:46:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| db23c713-ee51-36fb-9a13-684efac2b989 | -4.07764 | -46.20201 | 2025-11-17 03:46:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd68eebf-7290-3a12-b32e-e25d13da2f63 | -6.22386 | -47.23907 | 2025-11-17 03:46:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2acc5121-64c2-39d1-bf42-9e3ff7ea0dad | -6.66952 | -42.04258 | 2025-11-17 03:46:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8e4bfc59-5c11-38df-af87-deda9a8ba50d | -4.93438 | -44.53258 | 2025-11-17 03:46:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8a4c847-60a5-36e4-9509-239665ddfdf7 | -6.77033 | -41.44481 | 2025-11-17 03:46:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5f785a22-9960-372d-bf53-c034d9204074 | -7.978 | -42.28111 | 2025-11-17 03:46:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e5f4a41c-a3b4-3570-815c-cb40d73333c9 | -4.67648 | -46.94135 | 2025-11-17 03:46:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b22cce21-e31a-37dd-9072-c24177fdf507 | -4.01206 | -48.80669 | 2025-11-17 03:46:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 03107411-274e-3200-b749-5af16304b7d3 | -6.70686 | -40.80218 | 2025-11-17 03:46:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8cb6bc78-e6d8-3066-9537-fe69c7ba13b7 | -5.34759 | -43.04438 | 2025-11-17 03:46:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1d7c61c3-485f-3d67-b10a-9222e0fc9262 | -8.21247 | -43.56365 | 2025-11-17 03:46:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b48d796-f97d-32da-86a4-3794d55b8793 | -6.48147 | -39.33781 | 2025-11-17 03:46:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 983dbf9e-eac2-3ddb-a5b7-dbb693fb8c40 | -7.26763 | -34.87675 | 2025-11-17 03:46:00 | NOAA-20 | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 49cf1e2f-5f59-3dcb-8101-b2e8fdc1e04a | -5.49351 | -41.3837 | 2025-11-17 03:46:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 6d651b49-1a05-390d-b76e-b8b21c2df017 | -6.36536 | -42.21608 | 2025-11-17 03:46:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ec541dbb-b877-35f4-8ca6-50f3dd4be16e | -6.87673 | -42.94482 | 2025-11-17 03:46:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5e1e0fc3-a13e-3a7d-9dda-69b6f70d8390 | -6.06033 | -41.64507 | 2025-11-17 03:46:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d6b20f1e-315c-367c-a6f7-86721822f821 | -5.47752 | -40.96682 | 2025-11-17 03:46:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 86b82b53-1d9a-3936-b5ac-38620af3a1c8 | -6.98054 | -39.162 | 2025-11-17 03:46:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d0fe7d6b-a92d-3f97-a21e-5b54421e5027 | -4.41836 | -45.54962 | 2025-11-17 03:46:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 75a295a2-1130-3630-8524-2eb991f6425a | -7.09494 | -42.73117 | 2025-11-17 03:46:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4982dafc-46da-3441-a3b0-0de54376bd5f | -6.67483 | -42.03585 | 2025-11-17 03:46:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| a143e8eb-a074-35cf-a6c2-1616d8ed04ce | -5.69636 | -45.98729 | 2025-11-17 03:46:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8be1f92-b645-3e0b-8a63-4b65ad558b31 | -5.48554 | -41.38261 | 2025-11-17 03:46:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 115cf525-c8f8-3b32-926b-944fc8d24eac | -8.49648 | -41.26873 | 2025-11-17 03:46:00 | NOAA-20 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9629a890-2ec1-3bd0-b290-7c6383c86c37 | -4.39628 | -45.8373 | 2025-11-17 03:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6fbbec5-dc77-326f-96c2-de0969f7b44e | -5.3284 | -43.04985 | 2025-11-17 03:46:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 984a5d31-261e-3fba-9dc0-c2ac23686932 | -4.7205 | -46.38281 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fe451043-8749-3f38-8e33-e664e7c3ae09 | -7.12913 | -41.65796 | 2025-11-17 03:46:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 5d76653b-a8e3-3b32-9852-36bb8191056b | -7.03368 | -47.6204 | 2025-11-17 03:46:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27a98ba7-8f64-3b21-9e49-98fbbc6b5ecb | -6.68052 | -42.05166 | 2025-11-17 03:46:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5ef5ad18-0461-3802-a2f5-cdea3d0d80b5 | -6.67422 | -42.03947 | 2025-11-17 03:46:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| ddb99133-ec97-3926-adb4-0fbd5b8464f9 | -3.46287 | -49.99264 | 2025-11-17 03:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37d0c9a7-2e27-3037-a498-b0947758da02 | -6.29683 | -41.75054 | 2025-11-17 03:46:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4d12e2dd-6787-3915-8f82-b07993cd736f | -6.93061 | -39.62854 | 2025-11-17 03:46:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8468e177-1d15-339d-8249-f13923bf4ac7 | -4.73163 | -46.38544 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50b8b52d-1446-3c0e-8991-05ff62a9c597 | -4.0564 | -47.50393 | 2025-11-17 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9f94bd77-0363-3181-bb5f-d286e6b978fc | -7.61476 | -42.58066 | 2025-11-17 03:46:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 35aeb562-9d22-33bf-a774-7cd5622b05b7 | -6.93601 | -41.53648 | 2025-11-17 03:46:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| dd713bc6-9dd6-32a0-9fc6-8cfe4ff7d584 | -7.28917 | -45.45871 | 2025-11-17 03:46:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b679e140-db95-34de-9ef8-413f3d5b510d | -6.41245 | -42.32884 | 2025-11-17 03:46:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6cf1836c-fa9e-36ea-996d-9559b5b64372 | -4.73227 | -46.38175 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README14.md)
