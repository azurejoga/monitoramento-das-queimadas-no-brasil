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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 715dc030-1427-385f-92d9-b83ddd834865 | -5.8102 | -43.05448 | 2024-12-18 04:01:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| fac5b9bb-f735-3925-b430-600c232ae763 | -6.97517 | -43.57291 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 4aa1cf7d-834b-3f85-a9a4-d74db866b129 | -6.73416 | -34.9902 | 2024-12-18 04:01:00 | NOAA-21 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| ce58a681-4c6f-342e-acfb-0739f7af9f64 | -3.06774 | -40.0457 | 2024-12-18 04:01:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c0685218-445c-3407-a6af-c2a9744d9940 | -6.97358 | -43.55964 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f13dc090-1d2c-3a66-9147-648321e6b0e7 | -6.28993 | -37.243 | 2024-12-18 04:01:00 | NOAA-21 | JARDIM DE PIRANHAS | RIO GRANDE DO NORTE | Brasil | 2405603 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 62a2b8fc-7ea9-332a-87ff-07e6edc4e0d5 | -3.4904 | -43.34308 | 2024-12-18 04:01:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83b21dd9-3486-3350-9b0e-f73e05e557b7 | -5.95529 | -39.67755 | 2024-12-18 04:01:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 7f9a5f08-feb0-3c73-a174-d80359ec4986 | -6.36889 | -35.24159 | 2024-12-18 04:01:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 15d5d044-0d60-33a6-a195-aa4b700f468d | -5.92283 | -42.94137 | 2024-12-18 04:01:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6f66606f-1635-3e10-b780-05e46788b988 | -3.24156 | -46.88103 | 2024-12-18 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 80d137fd-fa80-363f-b433-704fb3771383 | -6.75841 | -40.13266 | 2024-12-18 04:01:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 439c3477-682b-39e9-a37b-b6395ab9df04 | -7.07069 | -39.78868 | 2024-12-18 04:01:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0446da9b-441a-31b1-a810-b46b253dcaeb | -3.14875 | -44.45681 | 2024-12-18 04:01:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5a6380c-3fee-3b45-b253-49e997198a16 | -5.9426 | -48.07106 | 2024-12-18 04:01:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30ff578a-28d8-3ada-89f0-75b25ce1ffb3 | -4.4475 | -38.06303 | 2024-12-18 04:01:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 006ceb56-210b-3477-8dfe-d8e67df9ec4b | -6.73823 | -34.99084 | 2024-12-18 04:01:00 | NOAA-21 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3a360f18-2379-357c-883f-225add3d945d | -3.24398 | -42.41541 | 2024-12-18 04:01:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ad262f6-7799-3f8a-89e0-fd3e185c35ea | -6.96565 | -43.56269 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e6813228-3dd4-3ebc-9d4b-2f01c3253b1e | -8.33991 | -36.63395 | 2024-12-18 04:01:00 | NOAA-21 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5871e95b-d04e-3c29-ae80-f7d7fbd46645 | -4.39415 | -44.20097 | 2024-12-18 04:01:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce054990-e87e-3d04-bd2e-17e3d86c730d | -6.61548 | -41.80109 | 2024-12-18 04:01:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2431a3ac-6930-32ba-a69d-6afa4b1169a1 | -8.47946 | -36.31127 | 2024-12-18 04:01:00 | NOAA-21 | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 822fc7b7-d582-3dd3-b6f7-c851e89ea5d5 | -4.01073 | -43.16464 | 2024-12-18 04:01:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73a7cc11-4440-35e1-8091-a7371080ec2e | -4.15299 | -43.56752 | 2024-12-18 04:01:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fb151d0-1645-3e73-a8ec-2ec925575ccd | -5.22531 | -37.36168 | 2024-12-18 04:01:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b2f6ca8c-7ed5-3a7f-91b8-0672fbb3ee6e | -6.98311 | -43.56983 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 08ea99fa-c357-3c5d-b684-6b9debb0182d | -2.34996 | -47.42338 | 2024-12-18 04:01:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c49f8675-c1c8-351c-8b4d-3397aa9413cf | -1.63032 | -45.85446 | 2024-12-18 04:01:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| aa2d5b46-d33a-3f8a-92ee-03a4e20d99a7 | -7.77639 | -35.0555 | 2024-12-18 04:01:00 | NOAA-21 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 284c4184-a941-37ef-8a28-3a464aab4a58 | -3.94335 | -43.97916 | 2024-12-18 04:01:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4eceff12-90ea-34dd-bb1f-e307a7c3dd8c | -3.05817 | -40.17221 | 2024-12-18 04:01:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 737e578b-af04-391c-a296-c12b6a492a25 | -1.59899 | -45.41039 | 2024-12-18 04:01:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61d1aa1a-4536-381a-94cc-dedb019c7483 | -4.93638 | -45.09455 | 2024-12-18 04:01:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3b64f73d-9331-3705-8c93-bc0c0c360816 | -7.86301 | -43.0851 | 2024-12-18 04:01:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9a59a27b-25b9-3a35-8dc8-a44647ac1a09 | -6.30533 | -38.91196 | 2024-12-18 04:01:00 | NOAA-21 | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2f4b65c8-59a9-3224-9d56-429d58a6c174 | -3.02519 | -45.23449 | 2024-12-18 04:01:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f711519c-43f3-3865-b027-b50afcc664a3 | -6.98152 | -43.55655 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4fd9ed56-6c59-3d42-aa6d-ea5dddd327dd | -2.86192 | -45.49772 | 2024-12-18 04:01:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66ef35b5-e9cb-3e2a-96d5-090108557ba5 | -6.67121 | -38.58902 | 2024-12-18 04:01:00 | NOAA-21 | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 033e6038-8284-328a-ba5c-071337dd1a10 | -5.99836 | -41.57336 | 2024-12-18 04:01:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 86ee1fc9-7562-3757-9bf9-a536200b4c4d | -6.97653 | -43.56445 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 7e3ddce8-79b8-31bc-9813-def9d8a8eb6b | -3.7587 | -43.51062 | 2024-12-18 04:01:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7672c64-d182-3f0a-9292-16472e39085a | -6.66592 | -39.23935 | 2024-12-18 04:01:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 00f8e622-81b8-3894-8ee0-6361aa01fe1a | -3.14119 | -44.47258 | 2024-12-18 04:01:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66ed6ccc-ac5f-3a0b-8677-bf7fb9f0abf3 | -6.1482 | -42.66689 | 2024-12-18 04:01:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5ceb1445-e893-3994-b951-57832eabdeef | -3.24237 | -46.87611 | 2024-12-18 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| af229a64-5787-3ed8-82fe-a10f69bc1303 | -5.22889 | -43.21475 | 2024-12-18 04:01:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 628b6385-fc6c-369c-8c08-c4a1666df422 | -6.96995 | -43.55906 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c480f124-35bf-30ae-aba9-0a42fb9ccd64 | -6.98851 | -43.58681 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e0fb1564-8238-3ad1-8867-0b4186575e73 | -6.3374 | -41.91843 | 2024-12-18 04:01:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b4209784-e8d3-3181-b7f7-774ec78aa21f | -4.52719 | -45.86889 | 2024-12-18 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccc2db41-baf7-3dfa-9aa9-e0267c8e74c3 | -6.21049 | -39.67873 | 2024-12-18 04:01:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ed7aa547-5bd1-3fdd-a841-aabe2f5ece0e | -3.02372 | -45.23873 | 2024-12-18 04:01:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 8469953b-784a-3f8a-a156-73f93eafc07a | -6.98699 | -43.57353 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8ff050b9-6225-3fe0-be5c-e1b19ca2a661 | -4.88165 | -41.40129 | 2024-12-18 04:01:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2a66d04e-9000-3180-ab80-03960f342801 | -6.9877 | -43.5693 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 52d592f8-200a-3b50-a994-06477c3fc431 | -4.12667 | -43.56321 | 2024-12-18 04:01:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8fa86618-25fa-3d52-9b37-3b0049e9c34c | -5.93867 | -48.06449 | 2024-12-18 04:01:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| bcdf4b8e-2d94-32c8-8cd5-bfc3fb126305 | -5.94951 | -48.06044 | 2024-12-18 04:01:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4356bf77-d091-3109-9bbd-6ce731c62155 | -6.98243 | -43.57408 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| e2b5a7ab-24e3-3873-8de7-88406019d613 | -7.25356 | -40.16529 | 2024-12-18 04:01:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 7d0d448f-c6be-395c-ad0d-fe2cf16c4701 | -5.48747 | -40.6904 | 2024-12-18 04:01:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0d268ea5-7cff-3284-97bd-631690b54a72 | -5.61094 | -42.82801 | 2024-12-18 04:01:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 09ab7dd1-6561-303e-ae86-f1f3b5c5efb7 | -7.0826 | -35.02551 | 2024-12-18 04:01:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 8cd29910-8818-378b-9ceb-bbd437ca3dc2 | -5.95943 | -42.5533 | 2024-12-18 04:01:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 853528e1-d87e-351e-8118-d49c05ab688a | -4.8048 | -44.02876 | 2024-12-18 04:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1ea6a2b2-e85e-3f52-83dd-f5d435e0bbcc | -6.96496 | -43.56691 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e84b5420-b059-3a7b-8aa0-801c257eac57 | -4.83139 | -38.37267 | 2024-12-18 04:01:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| abbed510-95bd-3b53-a637-26633b88fcb6 | -6.74928 | -39.04934 | 2024-12-18 04:01:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2d8eaf8c-d9d6-3a4c-81e6-bd5bbb8b548b | -4.51264 | -39.02629 | 2024-12-18 04:01:00 | NOAA-21 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8b3c4d3f-d74a-31d5-be16-87591d434b03 | -6.42892 | -39.67355 | 2024-12-18 04:01:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9f78b304-7e96-38ba-b1cf-aa8aea0299e2 | -7.77997 | -35.05993 | 2024-12-18 04:01:00 | NOAA-21 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| ede105e2-224d-3d9c-b2c9-efa0bc814b31 | -5.01914 | -42.65183 | 2024-12-18 04:01:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d321ce1b-d45e-32a8-b801-78bc860dc3db | -5.0891 | -45.97579 | 2024-12-18 04:01:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 160b89e9-6ce2-35b4-ad1a-dce9180c9a6b | -2.92629 | -45.2515 | 2024-12-18 04:01:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a35386a1-0701-317b-9345-3b06e5c0f986 | -3.0672 | -40.04917 | 2024-12-18 04:01:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8232c3bd-ca78-3763-a10c-dfa9989d4d47 | -4.86821 | -41.37688 | 2024-12-18 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cbcb3029-823c-3a7d-87bf-c8313e60f571 | -5.94552 | -48.0542 | 2024-12-18 04:01:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e43cd6b9-0b1c-3d55-a354-0ad460e4623f | -5.33918 | -41.21918 | 2024-12-18 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1a0087b6-9971-3eac-a9ff-605124165da2 | -3.02863 | -45.23542 | 2024-12-18 04:01:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c2a6b0a2-e4dd-3998-9eee-51f4bf72f2d6 | -8.91989 | -36.11871 | 2024-12-18 04:01:00 | NOAA-21 | CANHOTINHO | PERNAMBUCO | Brasil | 2603702 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4c6cef8f-c673-3412-8efd-c6a99a8f7c2e | -6.98765 | -43.58796 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 610f1525-ef40-3393-9fe4-bd06324e88ae | -6.97468 | -42.83035 | 2024-12-18 04:01:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c8b3b3ac-e567-3b15-a372-90f5fda161c7 | -5.57221 | -45.16578 | 2024-12-18 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6a75815-ad86-3c8e-b258-38a9b0250652 | -3.86635 | -47.02836 | 2024-12-18 04:01:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| f2a1e6c2-4343-36fa-aa20-69628e288ee2 | -1.62891 | -45.85625 | 2024-12-18 04:01:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 134e34e5-1544-30dc-9bb7-74386a4620b8 | -2.9276 | -45.24353 | 2024-12-18 04:01:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bcf03ef8-d1bd-3d85-baf6-470642d8c8a7 | -2.55149 | -45.8017 | 2024-12-18 04:01:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b23e748-ca5a-3e9b-8f5b-ae0190ee2614 | -5.9436 | -48.0653 | 2024-12-18 04:01:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 7390a3d7-3624-3a5e-96b2-9e0af48fdb1e | -3.02456 | -45.23847 | 2024-12-18 04:01:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 59caff7f-7f8c-300b-9890-ded06f8ed382 | -3.14746 | -44.45906 | 2024-12-18 04:01:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc850bb5-d8d4-3bcd-b3c2-77efb53bc435 | -5.57817 | -42.93926 | 2024-12-18 04:01:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4b151bfe-3702-3517-9ec5-9944392c8dde | -5.98464 | -41.66046 | 2024-12-18 04:01:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 356dc1ee-669b-3513-9766-61471eadd797 | -4.11913 | -43.56209 | 2024-12-18 04:01:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f7d08b6-40e9-3b06-80ab-92b960cd961b | -4.1229 | -43.56266 | 2024-12-18 04:01:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fc2b470-a0a2-3970-a39a-a376eeb002f3 | -6.98379 | -43.56561 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 9b431944-9773-3eaf-bd38-a0d34c4e99bc | -7.86236 | -43.08907 | 2024-12-18 04:01:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d12656a9-6d38-3dde-83a2-872922800b9b | -5.93088 | -35.62584 | 2024-12-18 04:01:00 | NOAA-21 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fc1c2dee-129f-34da-b9f3-6ea59c294326 | -8.87838 | -41.10576 | 2024-12-18 04:01:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README11.md)
