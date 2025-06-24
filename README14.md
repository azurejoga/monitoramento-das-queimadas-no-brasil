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
| 2a7f0b2c-8c39-3c56-b1d5-d2d5d6f82b65 | -8.58899 | -49.85642 | 2025-06-24 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a8354d9-f572-3dd6-95c6-ba0ae560bfc5 | -8.58126 | -51.5834 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c521f8a1-b5ac-3731-a9d2-ab0a4dea01df | -7.29094 | -43.21217 | 2025-06-24 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d2f96346-caad-316a-8555-f8e31c14fa94 | -7.20721 | -43.09631 | 2025-06-24 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 252e0bf3-c8e2-3f9f-9112-e12e684f5719 | -6.83169 | -47.83736 | 2025-06-24 04:25:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c29db797-549b-3144-8f36-53513297ac32 | -10.5025 | -53.57633 | 2025-06-24 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4415e52f-3326-3930-b4c1-3b4fcd39a8bb | -7.44804 | -45.56734 | 2025-06-24 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a73790f0-7678-3903-bb59-88b8305950a1 | -9.399 | -48.43487 | 2025-06-24 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 079bbfaf-b8a4-3ee9-a130-496af6d3ed94 | -7.05458 | -43.92068 | 2025-06-24 04:25:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5c277af-a713-3603-81df-99de2548ae38 | -9.40338 | -40.31374 | 2025-06-24 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5d986d9f-4a4a-37ba-8e9d-a37a69ac6a72 | -6.96369 | -42.92831 | 2025-06-24 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d5721bb1-3a21-31d6-aa4b-33d1d99b197d | -7.09829 | -44.374 | 2025-06-24 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d61aa00-18fe-31b1-8c84-9ab65299d7a1 | -10.1441 | -48.98618 | 2025-06-24 04:25:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| df712b5a-5b1f-3253-ac39-9bbf87cba9ee | -10.06152 | -49.65443 | 2025-06-24 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3a49db7-f2a0-3ce6-b6fc-2455e1326e73 | -7.8575 | -47.11438 | 2025-06-24 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b52f40f-15fa-3d36-9e17-33c2881ed942 | -8.57249 | -51.58714 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4741ae8-104a-3b31-a0d2-f543ef1f1bf6 | -12.75333 | -44.4086 | 2025-06-24 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 943ac28a-52e6-32ae-aeac-e20848b98aad | -8.49833 | -47.50753 | 2025-06-24 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3f8458e-896a-3fcb-a468-510b9c900911 | -9.12503 | -47.5835 | 2025-06-24 04:25:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 777c837e-d72b-37f3-ba72-d6c1b975a624 | -7.70971 | -49.534 | 2025-06-24 04:25:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20b3fcec-e5f0-3354-8341-b3cb40a2b599 | -8.06476 | -43.10599 | 2025-06-24 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 68ace4d2-82c1-3b10-a31d-7095839c8d6b | -11.57183 | -47.42996 | 2025-06-24 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 034c14d2-fbfd-395b-89fb-0aa1bc1c54ac | -9.42684 | -47.48138 | 2025-06-24 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 508e8068-c331-3c99-9c27-6a0e969cc155 | -11.27976 | -52.4679 | 2025-06-24 04:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c53a1548-465c-368c-8b03-6fcfd074f716 | -6.11983 | -46.82325 | 2025-06-24 04:25:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c3c38d29-ec4a-3fd0-80b3-6985d00e1336 | -11.60722 | -47.61569 | 2025-06-24 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34c33ccc-dad1-3928-9002-ce0bab9b3ba8 | -11.37392 | -48.75699 | 2025-06-24 04:25:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c1eaae09-c4e8-34ce-a236-292dd5ce828e | -7.00806 | -44.61996 | 2025-06-24 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc02d1a7-faf5-39d2-9d7b-59c66ca91420 | -7.34624 | -45.33019 | 2025-06-24 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1d5ba1b0-203b-3b1d-81d4-c0344fbb63a6 | -9.13278 | -47.57757 | 2025-06-24 04:25:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9cc8c3fa-cbdc-3336-8465-759ba8b64775 | -9.64404 | -48.56448 | 2025-06-24 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a756464c-ea76-34f2-9176-2e6a700b8475 | -11.94015 | -48.42639 | 2025-06-24 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8b457c7f-bd94-3c52-830b-e22af99a1785 | -14.20302 | -42.76384 | 2025-06-24 04:25:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 82ee4200-d2f6-3c57-8f5e-f15ca7184d52 | -10.59326 | -49.64394 | 2025-06-24 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7eb85966-6cfa-36dc-a685-221bd97bd8cc | -12.80177 | -48.73437 | 2025-06-24 04:25:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20417124-34b6-3b64-b89f-7905c13f9a44 | -7.34626 | -45.35205 | 2025-06-24 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 40f2685a-2b62-32aa-832e-76d2e9c0fa93 | -9.5027 | -48.7447 | 2025-06-24 04:25:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97037117-bf12-3345-ab5b-652dfd0dd5a8 | -8.98826 | -49.87195 | 2025-06-24 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7b4f097-b80a-3b83-9f8d-dff38a2c4635 | -8.33865 | -48.52305 | 2025-06-24 04:25:00 | NOAA-20 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30a509ea-dbba-3c38-85c8-b8607c2166de | -7.28731 | -43.21161 | 2025-06-24 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d14c3c8f-ec47-3ab3-8dcc-3da8c8e15646 | -7.20594 | -43.10484 | 2025-06-24 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 223da3f9-9c22-36bd-ab39-29292ce364ab | -10.05737 | -49.65778 | 2025-06-24 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba54cea1-e661-31ef-bed5-7ab0e2780d1c | -9.39563 | -48.43432 | 2025-06-24 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab93d021-a0d2-31a7-b7c5-35b60c994d96 | -10.06086 | -49.65837 | 2025-06-24 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38db335a-7fee-3d2b-84a2-52c919077d1f | -8.5852 | -51.58414 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f8386419-bb52-3fc7-af9d-70a765ff709a | -10.1435 | -48.98989 | 2025-06-24 04:25:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9341bd05-f7f4-387e-a268-7adb6a305a01 | -6.17082 | -47.27251 | 2025-06-24 04:25:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bfa471c5-a95a-363c-8da7-a14139d37d34 | -10.07667 | -52.74498 | 2025-06-24 04:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b3852cd1-d62f-345f-aa85-115f7861a9a0 | -8.06411 | -43.11036 | 2025-06-24 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bde41e80-a689-3dc9-8365-e528201009fc | -6.25382 | -44.8369 | 2025-06-24 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30331166-22b0-3063-a905-31df7abc6a30 | -8.34146 | -48.52729 | 2025-06-24 04:25:00 | NOAA-20 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fce64a51-f25b-31b7-b16d-1c7d7fbc0881 | -10.57402 | -49.14746 | 2025-06-24 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ca8d9776-dbd2-336f-a7ed-2ec2e187b527 | -10.95337 | -47.38791 | 2025-06-24 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 931916fd-ad1c-3155-a642-070ff0698192 | -11.20338 | -49.01085 | 2025-06-24 04:25:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7d6fef7-80b6-320e-902a-59b9961c0f79 | -7.13063 | -43.7506 | 2025-06-24 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72fa12e8-f9f9-36f5-a793-828c8e159565 | -11.76369 | -46.32962 | 2025-06-24 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b9967bd-f8e6-3e41-ac61-40fd541abeb6 | -9.11966 | -46.86795 | 2025-06-24 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4e0ea7e-8b44-3973-91cb-fb0577224858 | -8.24292 | -44.94874 | 2025-06-24 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04b56cd7-5270-3a2a-8766-e97c09877ea0 | -12.28741 | -48.80063 | 2025-06-24 04:25:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7e9b5d98-7c18-3b1f-b646-ff8876292889 | -6.63625 | -47.85106 | 2025-06-24 04:25:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02c1af7b-7da5-3d42-a7a2-afedc3c3d121 | -8.70347 | -47.17903 | 2025-06-24 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3eaa11be-2aad-3beb-be41-b79cb6c49a56 | -7.8718 | -47.87508 | 2025-06-24 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afb44ee2-3698-3268-b421-fbf4743f1978 | -10.87682 | -49.54759 | 2025-06-24 04:25:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c6c6d68-075f-3af5-a352-7150af52a34a | -8.98537 | -49.86724 | 2025-06-24 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8cfa442e-34f3-38e9-8342-67988bad0e04 | -8.36757 | -47.43261 | 2025-06-24 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| be9fb916-be48-3c27-9bc1-0fea086b8f75 | -10.23601 | -44.63566 | 2025-06-24 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 20932752-c774-3c9d-8a55-e426ea6ac8a8 | -8.57114 | -51.57121 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 30515f1e-602e-3028-ab29-e39b82d3dcca | -10.08152 | -52.74185 | 2025-06-24 04:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e602ebe5-433c-3f14-8bbb-d8f6def3ed82 | -9.4182 | -48.42314 | 2025-06-24 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b3fdc8d-15d4-361f-bd51-9027dfa9a7cd | -7.21022 | -43.10113 | 2025-06-24 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 87d233e4-fb27-3a63-a39f-4a9c46ec112c | -6.83226 | -47.83376 | 2025-06-24 04:25:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c025eab-d828-3295-919d-ba937576ddf0 | -10.59559 | -49.46665 | 2025-06-24 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9c976c2-450d-3974-95f2-f315bec6066d | -8.58607 | -51.57905 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f2bda0a-cd63-3339-bf01-77043f6a0d89 | -7.0914 | -44.37297 | 2025-06-24 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a8f943e-9434-3eba-ae56-af1a5940bcd1 | -6.95273 | -42.80171 | 2025-06-24 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e9a93021-d318-3433-b44b-7ff89784012b | -9.41483 | -48.42258 | 2025-06-24 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82d631ab-1282-33a8-a1a3-2cf014be3dcd | -13.76642 | -44.10098 | 2025-06-24 04:25:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee2abc40-c43b-37c6-b845-74091aa13c14 | -7.09886 | -44.3702 | 2025-06-24 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c61cfc8e-292f-34cb-88fb-342c7eef921b | -8.57509 | -51.57189 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 127bda4e-539f-3437-bd7a-3530a250071f | -11.65372 | -46.86328 | 2025-06-24 04:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b4ad0d3-d1a4-3a79-89c9-9103c32e752f | -6.16748 | -47.27197 | 2025-06-24 04:25:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 643d0113-882f-3ef6-bc33-b55acd81b550 | -10.57744 | -49.14801 | 2025-06-24 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c6f7501e-b86d-31e9-b228-d4d6fd093395 | -8.57731 | -51.58271 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89a9cc0e-c695-3e8c-a527-025160a2e51d | -8.55314 | -51.55764 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1df0c368-880a-3b31-9f48-6ef6255d5ec4 | -8.57904 | -51.57256 | 2025-06-24 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bac2f1ea-faf0-303f-ad1e-f8799fbcab51 | -19.63946 | -45.18975 | 2025-06-24 04:27:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e86882e-e747-3427-8d2f-35a068ec2d32 | -16.58249 | -43.64831 | 2025-06-24 04:27:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f992fdd-a21a-313f-8526-f6ce0a07ba68 | -16.32619 | -43.61927 | 2025-06-24 04:27:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 52c28a95-6b83-3f29-9bf4-506c449d3d4f | -14.38506 | -47.87728 | 2025-06-24 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c983a3f2-7053-3b5d-9e4a-ee264a8104c3 | -14.16142 | -50.42625 | 2025-06-24 04:27:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43b34908-7721-342e-ab95-6dfffe6ced57 | -19.41159 | -45.13893 | 2025-06-24 04:27:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 29cc6e31-7692-342a-b713-dd91cb545034 | -14.72903 | -48.41064 | 2025-06-24 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f3a87bf-f053-3d97-b6fe-cda71454973e | -14.24617 | -43.75812 | 2025-06-24 04:27:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f305aac-2433-3b95-bfe8-983db413e0b0 | -18.61501 | -44.26443 | 2025-06-24 04:27:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 64c3b07a-bc0e-3714-9d11-9fea118dee40 | -17.33738 | -42.65949 | 2025-06-24 04:27:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77a015f8-3a1e-3069-859d-75d5a4c3f749 | -13.73674 | -47.74571 | 2025-06-24 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 90629b43-82ed-3d55-83d7-f0256a5d1d07 | -14.39389 | -47.86414 | 2025-06-24 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0dd4500c-7549-366b-bc34-8b1c109bb9fc | -14.43763 | -48.91517 | 2025-06-24 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cba3abf-e66a-38f1-9af2-47c5c6eb7b0e | -14.74169 | -48.4164 | 2025-06-24 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee3a3fbb-9d10-396d-b2fd-cfd539e0fc3f | -14.72846 | -48.4142 | 2025-06-24 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README15.md)
