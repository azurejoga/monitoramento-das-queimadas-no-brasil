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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56292748-b703-3612-9ab8-372fff710268 | -32.12451 | -53.13141 | 2026-02-11 04:33:00 | NOAA-21 | ARROIO GRANDE | RIO GRANDE DO SUL | Brasil | 4301305 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 74886e3e-0358-3f61-939b-d5c87884f03d | -30.29583 | -50.9241 | 2026-02-11 04:33:00 | NOAA-21 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| 092599f7-e38f-3811-918a-da7161618673 | -32.92705 | -52.57361 | 2026-02-11 04:33:00 | NOAA-21 | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| d41b387a-54d8-3486-b0ed-f083fefb262b | -27.49281 | -50.55298 | 2026-02-11 04:33:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ac18e4b5-e8e1-3284-8518-64c342a06836 | -32.40391 | -52.41318 | 2026-02-11 04:33:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 9fbc9678-13f8-3a00-9931-c9293780d019 | -32.92641 | -52.57771 | 2026-02-11 04:33:00 | NOAA-21 | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 4bd5599a-dfbb-35c9-ba40-d646d2e1f6fd | -27.10186 | -50.53019 | 2026-02-11 04:33:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dc8e5267-7b86-3f5c-8be1-020ebf4c47a9 | -29.8602 | -50.81474 | 2026-02-11 04:33:00 | NOAA-21 | GLORINHA | RIO GRANDE DO SUL | Brasil | 4309050 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c5d0b046-4661-3b70-a5f9-cfe219a064d1 | 0.9569 | -60.5233 | 2026-02-11 04:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 9aa18e3e-bfd7-3392-b78c-e9696e4ee84a | 0.9569 | -60.5233 | 2026-02-11 04:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 36.8 |
| e7c95cd5-2543-3de3-870a-3ba78540556d | 2.74762 | -61.25794 | 2026-02-11 04:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a83635e4-1bb3-31bc-a9c4-18a6221acd1a | 2.74108 | -61.25466 | 2026-02-11 04:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08656a51-c624-3055-bc80-b64ddaabc5a9 | 4.05126 | -60.12181 | 2026-02-11 04:55:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10d811b9-1977-3a4d-b77c-6f8e11fa2b64 | 0.96718 | -60.51967 | 2026-02-11 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2bb91baa-3d47-33dd-a0e1-3830f5628fb1 | 3.38554 | -60.65092 | 2026-02-11 04:55:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e6b68e8-95e1-3d87-aca2-84ec1ab5dd81 | 1.35115 | -60.02525 | 2026-02-11 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e710deeb-b061-3e8f-b105-242722fd542f | 1.28459 | -60.4297 | 2026-02-11 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0efddabe-5d0e-382c-922d-25d46cecf17e | 2.74348 | -61.25469 | 2026-02-11 04:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 67a761ca-9983-343d-9c43-a22a80d6605c | 0.95618 | -60.52139 | 2026-02-11 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7aa3a2d4-961d-3626-91e8-2f64514d10d6 | 0.95509 | -60.5143 | 2026-02-11 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e9dbeb1-3a3e-300a-b94f-a21ce03157fc | 1.34579 | -60.02602 | 2026-02-11 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10c34abe-879b-368e-980d-a439e624cd1e | 2.7417 | -61.25889 | 2026-02-11 04:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86f4d85b-0d22-3b24-82be-8f60f305cb6b | 3.38668 | -60.65886 | 2026-02-11 04:55:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 051c68e5-30cb-3407-9011-4627d0fc7de0 | -2.98606 | -54.21455 | 2026-02-11 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab18fd9f-1134-3f00-b0a4-9756358a5181 | 1.28953 | -60.4253 | 2026-02-11 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4681388-5425-31de-b975-48be26da9b09 | 3.39243 | -60.65797 | 2026-02-11 04:55:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c60ad5c7-4036-351b-9c0c-aa881bb9d595 | 0.96222 | -60.52405 | 2026-02-11 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7327878a-cabb-3446-8039-69bf58222f29 | 1.3463 | -60.02929 | 2026-02-11 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c232a2cd-4176-32c6-abbb-b48e74608634 | 1.11803 | -60.51479 | 2026-02-11 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4e60da3-f9d2-3ec4-811c-987cedb99d7c | 4.40958 | -60.7896 | 2026-02-11 04:55:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d31af943-3156-37b7-9442-d857fb0b8e87 | 1.2747 | -60.43851 | 2026-02-11 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca74e99c-022e-3466-9d0b-d710740842bd | 1.28019 | -60.43762 | 2026-02-11 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f61ecc5-e730-394b-95ae-2f313cc0f8c8 | 0.95124 | -60.52584 | 2026-02-11 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 512bfd46-591b-3de5-a44b-f62e0f5202fe | 3.39177 | -60.65597 | 2026-02-11 04:55:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d12b211-a445-33a3-9d51-db174a2366d0 | 0.96058 | -60.51341 | 2026-02-11 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab334733-e928-3eb5-9499-df4a0476909a | 3.38603 | -60.65685 | 2026-02-11 04:55:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6adbb3b-7358-3080-8ae8-af61cae4568d | 3.37909 | -60.64981 | 2026-02-11 04:55:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb3969c6-9356-3c28-8271-374f3abeddcf | 3.38611 | -60.65489 | 2026-02-11 04:55:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e43553d7-c9f4-394d-9850-f6645af7796f | 0.95564 | -60.51783 | 2026-02-11 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1124119e-3568-3a63-8ac2-8d4a2e311de2 | 0.78811 | -60.66967 | 2026-02-11 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e02bbca7-5013-3d12-812e-19f40e53a10b | 0.96168 | -60.52049 | 2026-02-11 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e1e8347-b933-319f-93b8-3d6d940ca2c2 | 1.11691 | -60.50768 | 2026-02-11 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f734b44-c379-32b7-aa40-1f1c88545025 | 3.38483 | -60.64894 | 2026-02-11 04:55:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a022bacd-cb99-3cb0-8427-fcc1d4a9ce97 | 2.74699 | -61.25366 | 2026-02-11 04:55:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dc4c12a-90c9-3ad8-87c5-5664b483b118 | 0.96113 | -60.51695 | 2026-02-11 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96c883d0-912a-331c-8908-dc7c2b83ed7d | 1.11747 | -60.51123 | 2026-02-11 04:55:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af7c71a4-48d3-3eb7-9646-2a6272d80b38 | 4.05076 | -60.11844 | 2026-02-11 04:55:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b92a560a-8165-399c-899c-818759441db7 | 0.95455 | -60.51076 | 2026-02-11 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 365215b9-352b-381e-af09-99f7847cb65f | 3.38543 | -60.65289 | 2026-02-11 04:55:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e1e4312-a1fc-30eb-b0e9-8cac47886866 | 4.40896 | -60.78532 | 2026-02-11 04:55:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d876a6ff-77cf-3347-9edc-20c4de3939a5 | 0.96773 | -60.52323 | 2026-02-11 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17d09aeb-0662-37a0-8feb-dbfb3d875eba | 4.40835 | -60.78101 | 2026-02-11 04:55:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8606533-fe8a-3721-b772-25b8c66a569f | 0.96004 | -60.50988 | 2026-02-11 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ccfb108-ea02-3f47-b6f5-ffbb06f4c5bd | 0.95673 | -60.52494 | 2026-02-11 04:55:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf9ad3f4-83e0-3cdf-aa41-285850c62b91 | -5.6834 | -46.06322 | 2026-02-11 04:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f21e37cb-3017-39a7-af35-1875b1a6cea7 | -16.58367 | -58.21458 | 2026-02-11 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| ff7a69cc-0146-3023-aff0-b1bc7a364b9e | -16.58727 | -58.21522 | 2026-02-11 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ed2a4de4-e67a-39b4-a9e6-d4910587c820 | -15.60463 | -60.0741 | 2026-02-11 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e1e6cf5-831a-38f4-a6af-2a40b21cb063 | 0.9569 | -60.5233 | 2026-02-11 05:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 35.2 |
| c7f0a025-45be-32a1-9ac7-ab86d24da602 | -20.72958 | -55.1549 | 2026-02-11 05:01:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b83e5bc5-fc71-30cb-af24-81116c0bc42d | -18.97086 | -52.92862 | 2026-02-11 05:01:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4967aad-fd4c-3955-8c58-6745f39ffde2 | -20.23701 | -53.01498 | 2026-02-11 05:01:00 | NPP-375D | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d47c3a0e-540d-3bbe-8513-0017ca1c97b1 | -20.24059 | -53.01553 | 2026-02-11 05:01:00 | NPP-375D | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| caba15df-4526-3199-b952-6b504b3942d4 | -18.97321 | -52.92691 | 2026-02-11 05:01:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 432c8537-abfc-378e-af79-f5b084c89246 | -22.71965 | -53.96032 | 2026-02-11 05:01:00 | NPP-375D | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d280fadb-47a4-356c-9800-0ccc3fbeba4b | -18.97261 | -52.9311 | 2026-02-11 05:01:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 799ae404-fc07-35c9-80a2-3f7a8314e08d | -18.9744 | -52.92916 | 2026-02-11 05:01:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a879804-9d8c-3aa5-8ef3-c28e5540ed02 | -21.17287 | -56.50107 | 2026-02-11 05:01:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dabb73b6-4795-36ba-9c84-a8230f822dcf | -20.72565 | -55.15807 | 2026-02-11 05:01:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bec9490-4840-3801-b0b1-d9ade74837e8 | -19.33716 | -53.09955 | 2026-02-11 05:01:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 645e424d-4097-3bf8-9376-5c2a6c8f384a | -18.7038 | -54.98283 | 2026-02-11 05:01:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 94ac1b82-6b3c-3931-9d11-8cac7bddc916 | -20.729 | -55.15865 | 2026-02-11 05:01:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b855337e-c56d-3ddd-a668-c2744a5cd54c | -18.97616 | -52.93165 | 2026-02-11 05:01:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b25cbab7-816d-36b8-a669-bd1e1dc2506b | -18.70324 | -54.9865 | 2026-02-11 05:01:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74839835-ca70-3aef-8ea2-358cc4d0e7be | -18.8936 | -56.05647 | 2026-02-11 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6c23dc71-c5ea-3698-8df7-8e202efd90d2 | -18.6999 | -54.98592 | 2026-02-11 05:01:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5228ddd1-2635-3317-852e-0a8cccde79ba | -20.86507 | -56.04847 | 2026-02-11 05:01:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17bb8041-d401-31f1-a1c5-003cc0aca12e | -19.33304 | -53.10311 | 2026-02-11 05:01:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 23a96abf-f658-39a4-a8bf-eaf244e38f2f | -20.8684 | -56.04906 | 2026-02-11 05:01:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29da90aa-d52a-316d-9cff-1375a620741e | -18.89694 | -56.05706 | 2026-02-11 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| fb5698c4-2736-36ee-97b4-58a341898aab | -30.29288 | -50.92395 | 2026-02-11 05:03:00 | NPP-375D | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| d787c00f-5ded-3f28-8043-9af77c654ba3 | -32.92651 | -52.57743 | 2026-02-11 05:03:00 | NPP-375D | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 7ce6c4bf-92ab-34b8-a265-7078f8e73243 | 0.9569 | -60.5233 | 2026-02-11 05:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 09ae6491-cf2b-3d04-adfa-f3a5ae2bc4bc | 4.40959 | -60.78077 | 2026-02-11 05:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c4b6657-e515-39e0-909e-8e3c934ed1b4 | 0.80125 | -60.27886 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1ca3000-d2da-36f9-b319-302478d655cf | 1.28262 | -60.43669 | 2026-02-11 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05806226-9c98-35ff-879d-b0a35f96d2c0 | 0.95785 | -60.51246 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4bcb7881-ef5d-37df-a054-ec02d5c7fb75 | 0.7875 | -60.66794 | 2026-02-11 05:16:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0ae0666-fca2-38fe-ad2c-2e4cccbe0054 | 0.87695 | -59.58332 | 2026-02-11 05:16:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ee122c5-36e7-35e0-b854-d7c6fa018cb7 | 3.87982 | -60.09407 | 2026-02-11 05:16:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fca2485-9d59-324d-8705-35c062afee29 | 3.38743 | -60.65656 | 2026-02-11 05:16:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8f61936-08cd-3171-b5fa-fe7728fd9ac1 | 3.67796 | -60.98384 | 2026-02-11 05:16:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bec888e9-424f-36e6-8ed4-9b4814ccc37b | 3.62128 | -59.91807 | 2026-02-11 05:16:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c34022ed-5e55-3db1-a222-d92b3945b654 | 3.71898 | -60.99672 | 2026-02-11 05:16:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 917ac858-fc23-32d2-8804-0e519b222abe | 1.11521 | -60.50705 | 2026-02-11 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47346514-42c4-3c33-a283-b992a573a447 | 1.86794 | -60.58454 | 2026-02-11 05:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c7c0ab4c-5fbc-3657-bdb8-212342a1b302 | 3.72042 | -61.00613 | 2026-02-11 05:16:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57d91dd3-7ea6-33e0-bf33-bb3ba7b533cf | 3.7166 | -61.00672 | 2026-02-11 05:16:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edccf09b-82f2-3744-94f5-34e8fdd77abf | 4.8903 | -60.27389 | 2026-02-11 05:16:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f967199-70ea-38b6-b1c6-7929750e25cd | 1.57472 | -60.386 | 2026-02-11 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README3.md)
