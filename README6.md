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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0bc35a19-f28f-3158-845a-28c4e8f61337 | -3.77818 | -41.65845 | 2025-05-13 04:10:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 44419498-db59-3bb6-91c6-bdc9e72c3791 | -3.7743 | -41.66142 | 2025-05-13 04:10:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0c7ea348-ae99-3157-8c6f-4b19fb260879 | -3.77763 | -41.66193 | 2025-05-13 04:10:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6b323e62-1230-3db3-8435-abb3a69e5c7d | -3.77097 | -41.6609 | 2025-05-13 04:10:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7808b796-8cee-3c22-95f5-f1407f82b622 | -8.79129 | -49.80532 | 2025-05-13 04:12:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9f70aaf-62b5-3cbc-a820-666f83e0add4 | -8.07705 | -43.13052 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 29.0 |
| cd9d411e-7392-3e27-9778-086ed51cb412 | -8.06929 | -43.11505 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 45d6c7ae-f16a-3b95-a2d0-c12c2597aefd | -8.0809 | -43.12757 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 29.0 |
| 39ee6cac-8928-3a8f-b54e-cd743ba579d5 | -10.54012 | -42.4487 | 2025-05-13 04:12:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bae4f44d-b775-396e-9ce5-a7030233c9c4 | -6.64526 | -41.99549 | 2025-05-13 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ff08fe00-b3b7-35ef-a8c9-de4c8a6fd5fa | -10.53729 | -42.44448 | 2025-05-13 04:12:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 264a41c5-27a9-34f3-8252-db38f169d1ac | -7.58652 | -45.86948 | 2025-05-13 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ba76616-76bb-3942-85ec-ef2e79ce0a2d | -6.65251 | -41.99298 | 2025-05-13 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 29b674db-b05c-32ca-87c0-108d8c0351a3 | -7.31439 | -35.29723 | 2025-05-13 04:12:00 | NOAA-20 | PILAR | PARAÍBA | Brasil | 2511509 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5282b565-7b74-304c-b95e-e528befd35b4 | -8.06489 | -43.12148 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 5c45c0b1-e435-3105-b877-01583ae9cc64 | -8.07537 | -43.11958 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ec7040fd-7197-329b-8757-7732bf77b607 | -6.1109 | -36.47369 | 2025-05-13 04:12:00 | NOAA-20 | LAGOA NOVA | RIO GRANDE DO NORTE | Brasil | 2406502 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0e40120b-20bf-397d-a769-8b6cdecb30be | -9.50623 | -40.60555 | 2025-05-13 04:12:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3342cfec-81f9-312b-8079-a9f7356ac24f | -8.79562 | -49.80612 | 2025-05-13 04:12:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee1ff9b2-ac1c-3024-8b39-87faf6bd643e | -8.07977 | -43.11314 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e3e1bebe-aec5-343d-b9f2-eee0ea54f2cf | -8.06711 | -43.12896 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5e2dc6f4-834d-3788-acdb-f62a79cdb1f6 | -10.54123 | -42.44133 | 2025-05-13 04:12:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ced9502b-3961-3ed3-a82c-685ffd2a2b2e | -6.11422 | -36.47266 | 2025-05-13 04:12:00 | NOAA-20 | LAGOA NOVA | RIO GRANDE DO NORTE | Brasil | 2406502 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 37a75fba-ab09-3583-bead-63407ce2bca2 | -10.53502 | -42.43659 | 2025-05-13 04:12:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 812f7f13-5f68-3832-a553-4186d375344f | -8.0765 | -43.134 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9800fb45-2925-35d9-bbbd-ad206b767296 | -7.11221 | -36.49118 | 2025-05-13 04:12:00 | NOAA-20 | JUAZEIRINHO | PARAÍBA | Brasil | 2507705 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3706caa2-5940-35c0-a7bc-2c97833fa916 | -8.07315 | -43.1121 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| e79b218d-61fa-3b6f-9e8e-fa0ab0c6d4e2 | -8.30737 | -48.05624 | 2025-05-13 04:12:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0bdfe08b-c8fa-37e1-bae3-206086bd01d2 | -4.77797 | -48.07928 | 2025-05-13 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee58836c-cf35-386c-a21c-32bbf14c6812 | -10.54628 | -42.43083 | 2025-05-13 04:12:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d45a67c5-3561-361e-9371-748526f738bd | -8.07759 | -43.12705 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 29.0 |
| bd4cd070-9692-3357-99e3-d444673eb2bb | -8.06984 | -43.11157 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 1a30dff4-87cf-365a-bb48-8a4e570d4e97 | -8.07646 | -43.11262 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| ead91f93-9f66-3cfe-a285-937dc6f2717d | -9.50482 | -40.60684 | 2025-05-13 04:12:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3b737089-5061-3a48-928c-fe8fa0e4a590 | -8.0726 | -43.11557 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 7758993f-bc76-3e43-b75e-415e7373c014 | -8.06875 | -43.11853 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 75593383-5922-32f3-a692-e8a8e6eaefd9 | -8.79921 | -49.81111 | 2025-05-13 04:12:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f781be7-7b06-3454-a0bb-3b716575a50a | -8.71794 | -50.24383 | 2025-05-13 04:12:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e99988c3-40fd-3b79-a9b8-b3b555962588 | -10.54067 | -42.44501 | 2025-05-13 04:12:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fdc0487e-911c-3273-8046-db473bfd94ef | -8.0682 | -43.122 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 67706f92-9374-3e89-93f8-2a7940cf8b3d | -6.78817 | -47.59504 | 2025-05-13 04:12:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abd66d58-c9e5-3c9f-be9c-be73298c1c96 | -8.06766 | -43.12548 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 46c836fa-8a6a-356c-a926-476838678522 | -7.26055 | -43.31364 | 2025-05-13 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7986a99d-d3c7-304a-9a1f-d8f911f63256 | -6.21661 | -37.53411 | 2025-05-13 04:12:00 | NOAA-20 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 842a9c4d-63c0-3dad-8345-b2bbbd153c2c | -8.07814 | -43.12357 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.8 |
| 109b9d1a-2667-3523-946d-7411660a9cde | -8.07373 | -43.13 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.2 |
| 76b98a87-980c-3950-9310-2021db64fd04 | -7.58716 | -45.86553 | 2025-05-13 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33299a76-1060-3b34-bbd7-78ba72217602 | -10.53784 | -42.4408 | 2025-05-13 04:12:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9f9d6551-c48f-3940-aac9-29d7a6aae287 | -8.07592 | -43.1161 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 77c55b4a-f724-3bc3-af3d-8239073a2007 | -8.78695 | -49.80452 | 2025-05-13 04:12:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 819af0c4-1a61-3377-9489-c4e55e9257d8 | -7.5878 | -45.86159 | 2025-05-13 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2a9cea2b-fcca-36f9-a9a4-ba821fb0cc5a | -8.06435 | -43.12496 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8ccbc4d1-80ab-3d14-9e70-b8d2bb0ab507 | -8.07482 | -43.12305 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f7899324-d62b-3cbf-9640-427089da7a44 | -5.86418 | -45.50069 | 2025-05-13 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d074d2d-bc5a-3e72-b355-c8e22ec3e933 | -8.07097 | -43.126 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.2 |
| dcc433f6-082e-3863-ba39-62fd791c44ca | -7.5913 | -45.86217 | 2025-05-13 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf5d1fb9-9a3f-33cd-8584-1c74fec3efad | -9.50262 | -40.60501 | 2025-05-13 04:12:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e24cee11-afcb-3e1b-85b6-b3fe025c0a31 | -8.07923 | -43.11662 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 99d2bb24-fd5d-35e1-a2d6-b19d8843fea7 | -8.06598 | -43.11453 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 804c1ffa-a742-3f44-b5c3-76fbf1520432 | -10.53557 | -42.43291 | 2025-05-13 04:12:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 13febceb-ccbe-34c7-8084-f1f40cf84813 | -7.84714 | -36.84855 | 2025-05-13 04:12:00 | NOAA-20 | CAMALAÚ | PARAÍBA | Brasil | 2503902 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f56d1b7b-c173-3db7-97c9-b6c1751589b6 | -8.06543 | -43.118 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 078d3d9d-b842-381a-8205-33432a7d54c1 | -8.92548 | -36.1986 | 2025-05-13 04:12:00 | NOAA-20 | CANHOTINHO | PERNAMBUCO | Brasil | 2603702 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 79b52075-8f25-3670-88fb-a8fb44ec467f | -8.07042 | -43.12948 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.2 |
| cfbbc201-0680-38a0-99c9-13a96482e3a2 | -8.07151 | -43.12252 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9ef8d34a-7351-3fbc-ad67-517f31c1733b | -10.54179 | -42.43765 | 2025-05-13 04:12:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 40581881-770c-31bc-abb2-480d4fc7e208 | -6.21605 | -37.53788 | 2025-05-13 04:12:00 | NOAA-20 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| aef00821-2ad9-3252-b21c-327cc91dfe89 | -8.07206 | -43.11905 | 2025-05-13 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 18525b67-55d9-3306-9170-e154946d07a1 | -11.58181 | -47.60739 | 2025-05-13 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e853aae-4255-333e-b223-2cf061222525 | -14.66636 | -45.12416 | 2025-05-13 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 17922a7b-d5bc-3765-a7af-6452bf2de118 | -11.78822 | -47.35818 | 2025-05-13 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4506ddf6-b1f8-3f67-90d9-fd514a54a236 | -11.77497 | -48.20054 | 2025-05-13 04:14:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| df6fd89d-b61b-37db-a89b-fbde70da00da | -12.14953 | -48.01635 | 2025-05-13 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 20b81196-224b-3c2f-aec0-4a23c063d761 | -12.81687 | -51.58182 | 2025-05-13 04:14:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 07271262-66dc-3e76-8cce-5d07661686d9 | -14.18504 | -45.47837 | 2025-05-13 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3dbdbf78-911b-3785-a275-7ca74946a579 | -13.39167 | -47.63506 | 2025-05-13 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5996c16-9d74-30ba-948a-125e6200e0b4 | -11.61846 | -48.11813 | 2025-05-13 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8606ac8-972b-3194-978c-fbef190427d4 | -13.96877 | -56.78834 | 2025-05-13 04:14:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1c1b2c7b-0c76-3091-b002-3b52118738ad | -11.79063 | -47.41031 | 2025-05-13 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8d40c0bd-aca6-35c9-a369-1b53fa17e9c5 | -13.56009 | -52.86411 | 2025-05-13 04:14:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 53ca3404-4640-3b38-b10d-6e1da9f07c3d | -17.01666 | -47.42168 | 2025-05-13 04:14:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a85e2ff4-510c-3f64-839e-4b51350a2819 | -14.65862 | -45.13016 | 2025-05-13 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e553fa9c-23de-3d2a-a5e8-bc47bc496186 | -13.5726 | -52.87829 | 2025-05-13 04:14:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e88ba649-06ac-3651-abbd-78813ef4434d | -13.97798 | -56.80623 | 2025-05-13 04:14:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| dda958cf-73a7-3636-9c07-0d3fa1782700 | -11.58471 | -47.61236 | 2025-05-13 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5b0efb2e-eab9-323d-a265-394ee3beb7f5 | -12.15399 | -48.01255 | 2025-05-13 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 8e75e48a-4909-31e8-be9b-9b4dc6c49d4e | -14.18267 | -45.47513 | 2025-05-13 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 553feaf0-8566-3459-a727-7229982eaebb | -12.82326 | -45.47635 | 2025-05-13 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ea341785-6c51-3ccd-bc77-32aaa64626b2 | -11.58397 | -47.61669 | 2025-05-13 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5fa7729b-25d4-3186-b971-108710e559eb | -12.49899 | -44.50652 | 2025-05-13 04:14:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fca5caf-19a3-3d8d-939a-48be083b9789 | -13.67521 | -53.93872 | 2025-05-13 04:14:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4de5a8f1-8d94-342a-9245-fcf349663cf8 | -11.57623 | -48.07315 | 2025-05-13 04:14:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68678d41-1338-3f03-87a0-08e45be791b3 | -10.49438 | -46.17997 | 2025-05-13 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6af84a38-b05c-32ea-8c0e-a1dd32e8a6fc | -10.90184 | -44.34032 | 2025-05-13 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7686113a-2e21-37d3-a68d-cd5535920d84 | -13.09116 | -52.29739 | 2025-05-13 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a054f15-ef1d-3dad-ab10-7f44f18bc52a | -12.29509 | -52.47108 | 2025-05-13 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f0b731a-1ae1-35c9-9953-062f67fd117b | -13.98522 | -56.8027 | 2025-05-13 04:14:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ffe0e2c0-e455-3eac-a88e-d131c37e1ce4 | -13.54922 | -52.86777 | 2025-05-13 04:14:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 015c2309-7ba4-3503-9df8-bb86c35b1d81 | -14.65961 | -46.9896 | 2025-05-13 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3e37afd-ce2d-3df2-ab7c-e40dd9852176 | -14.18381 | -45.46799 | 2025-05-13 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README7.md)
