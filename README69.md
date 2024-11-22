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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd76ee3d-e954-306c-9a96-5276b789c810 | -5.4548 | -43.2426 | 2024-11-22 13:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 3583988d-975c-3473-90bf-ba8400e1e148 | -6.9118 | -47.5382 | 2024-11-22 13:20:00 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 6ff7a681-f974-34f5-9f48-637559487215 | -3.1438 | -42.0369 | 2024-11-22 13:20:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 321.1 |
| b8e6aa8e-6c87-37bd-af93-79c051f5ba20 | -5.455 | -43.2192 | 2024-11-22 13:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| a8ee731c-33ac-399d-9104-a09d21b4fe2f | -3.5544 | -42.1363 | 2024-11-22 13:20:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| 608b8c4e-1b95-39b2-8827-9985a18df3c2 | -1.5621 | -47.7248 | 2024-11-22 13:20:00 | GOES-16 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 1a4c4b32-7030-3814-b82c-663ed1ab5056 | -3.1251 | -42.0377 | 2024-11-22 13:20:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 05e4a12d-b2ec-3746-9fd0-d8274e9ab76e | 1.3819 | -55.9455 | 2024-11-22 13:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| cafbb6f0-bfcb-36c8-9c47-473febe672e5 | -1.1287 | -53.3951 | 2024-11-22 13:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 867330eb-1f52-3b2a-b692-b852b3ede6b6 | -3.1625 | -42.0361 | 2024-11-22 13:20:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| adb38d9b-cc97-3957-9206-c4a4ea6a84a7 | -5.4548 | -43.2426 | 2024-11-22 13:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 013419e2-f9ea-31d2-9d4b-f90fbc956b01 | -6.912 | -47.5163 | 2024-11-22 13:30:00 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| fbb1a28c-67cd-3f6c-becb-755f940d0bb7 | -5.4736 | -43.2412 | 2024-11-22 13:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 6a15ee8f-832f-352f-b9ae-a3122e6a8a5f | -6.9118 | -47.5382 | 2024-11-22 13:30:00 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 0ef4a065-f019-3c56-a118-315dba081551 | -3.1438 | -42.0369 | 2024-11-22 13:30:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 27f500c8-aec5-35c4-be80-af7975f38874 | -5.455 | -43.2192 | 2024-11-22 13:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| edd66ae0-b9ad-31e7-b091-5d6d3d761759 | -5.7146 | -43.5261 | 2024-11-22 13:30:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 874345e3-ad2d-3b88-ab00-a329c3a8d0b4 | -3.1251 | -42.0377 | 2024-11-22 13:30:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 2413b590-9f71-3042-a003-3f8ad37c7fd9 | -3.1625 | -42.0361 | 2024-11-22 13:30:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 9a929991-c8c8-3e0d-93fe-930122c9e815 | -1.2572 | -53.3736 | 2024-11-22 13:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 9d401d37-b98b-3804-81ca-97ae04fceccf | -5.4736 | -43.2412 | 2024-11-22 13:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| c8ff54e9-0b6d-3573-ae70-75b4bc9ad85a | -3.1251 | -42.0377 | 2024-11-22 13:40:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 954f28eb-eb6f-38d2-8260-16434e6aa055 | -5.455 | -43.2192 | 2024-11-22 13:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 3a5409cf-bf8c-3077-bc73-7670f01ce0c0 | -5.7146 | -43.5261 | 2024-11-22 13:40:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 34bd1a1b-3ff5-3445-b8ec-999e5547d9dc | -5.4546 | -43.2659 | 2024-11-22 13:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 0aa71eee-87b6-3844-aa43-8181db5ef3eb | -4.1968 | -43.9489 | 2024-11-22 13:40:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 466e82ad-0abd-37f5-bedd-4b4e50faed37 | -1.2572 | -53.3534 | 2024-11-22 13:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 2aa6ed77-4940-38d6-816a-910fd745d260 | -3.1438 | -42.0369 | 2024-11-22 13:40:00 | GOES-16 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 906de54f-2f2c-3366-b207-ccae7e3cc2f7 | -7.4432 | -41.9061 | 2024-11-22 13:40:00 | GOES-16 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 76.4 |
| 078b9710-7916-332e-a84f-dfc7a71ff5ef | -6.912 | -47.5163 | 2024-11-22 13:40:00 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| af6ae1d0-5fbb-3fa3-82e7-e87daffdf1f5 | -3.6634 | -42.674 | 2024-11-22 13:40:00 | GOES-16 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 37d15039-feb0-396c-a8e1-254b2d1f1743 | -0.2667 | -51.5629 | 2024-11-22 13:40:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 7bbbf30d-3d42-33c0-bbf6-cb15f15e37e5 | -6.9118 | -47.5382 | 2024-11-22 13:40:00 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 6b997ffa-0b0a-32e7-b2af-4dac1ab33869 | -1.1287 | -53.3951 | 2024-11-22 13:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| ddbcfa64-ac5e-3235-8be1-87e479286415 | -0.0092 | -51.2532 | 2024-11-22 13:40:00 | GOES-16 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 1f17562b-d727-3ca9-b31e-58f12370cc60 | -1.2572 | -53.3534 | 2024-11-22 13:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 28de8ba4-00ca-3628-9a2d-4e69fd877bb0 | -6.9118 | -47.5382 | 2024-11-22 13:50:00 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 178.5 |
| 152febaf-e251-36ad-b18a-aae35f3e3a77 | -7.4432 | -41.9061 | 2024-11-22 13:50:00 | GOES-16 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| e09ad78c-dbe3-3ba3-9fda-7ebf5b09e51a | -5.4736 | -43.2412 | 2024-11-22 13:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 99265336-1ae7-3b07-8c72-64cc4c9ba9bf | -5.455 | -43.2192 | 2024-11-22 13:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| e5b68cbc-6161-32c3-b4ec-1c44cf17c6aa | -4.3408 | -44.742 | 2024-11-22 13:50:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| e13dd7d7-23a0-3455-ae07-17a4421696f1 | -3.6634 | -42.674 | 2024-11-22 13:50:00 | GOES-16 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 134.1 |
| f60462ae-d2f2-3231-ba3d-f4912674cff7 | -3.446 | -41.4735 | 2024-11-22 13:50:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| f55be627-32e7-33e7-bdc4-0cafbc49c557 | -6.912 | -47.5163 | 2024-11-22 13:50:00 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| fd0b3a71-25d5-3ce7-acaf-3e1e3c9a9edb | -2.3188 | -54.7634 | 2024-11-22 13:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| f2aaf5d1-15d1-35cb-bbac-24df0a39706e | -1.2572 | -53.3736 | 2024-11-22 13:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 6570da34-c802-3c63-98ff-eab1c1201bed | -5.6942 | -43.7133 | 2024-11-22 13:50:00 | GOES-16 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 38db2bcb-294c-3fda-8642-0329a3cbabd8 | -5.4546 | -43.2659 | 2024-11-22 13:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 71001c00-3795-3fe0-ba08-1697043f2046 | -5.7146 | -43.5261 | 2024-11-22 13:50:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 062f6fc9-9344-3910-ae26-312e552004e7 | -6.9118 | -47.5382 | 2024-11-22 14:00:00 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 182.1 |
| 4b7e3e53-8684-3111-9bf3-16f560393bd3 | -5.4736 | -43.2412 | 2024-11-22 14:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 5c48c945-1b60-34d0-a318-10bac12f7506 | -3.9646 | -45.3272 | 2024-11-22 14:00:00 | GOES-16 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| ceea354b-b225-3d33-9056-3761a35d024a | 2.2002 | -50.9189 | 2024-11-22 14:00:00 | GOES-16 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 7a4293ec-2a7e-3cb2-871d-3b4f3217db91 | -3.6634 | -42.674 | 2024-11-22 14:00:00 | GOES-16 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| bac3f589-a7d1-307b-b723-20da7920a1ee | -3.4102 | -44.6055 | 2024-11-22 14:00:00 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 42366296-edcc-3d01-bb70-1f861a656df5 | -3.1509 | -44.3426 | 2024-11-22 14:00:00 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 48cf140c-a635-324a-a17a-73af9db620d6 | -7.7501 | -36.0116 | 2024-11-22 14:00:00 | GOES-16 | ALCANTIL | PARAÍBA | Brasil | 2500536 | 25 | 33 | nan | nan | nan | Caatinga | 94.9 |
| 7a9584d9-293c-303c-9dd9-8a60660ef38d | -3.1785 | -42.5557 | 2024-11-22 14:00:00 | GOES-16 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 73c94098-3f36-3875-9f3b-2016c15fa123 | -5.7146 | -43.5261 | 2024-11-22 14:00:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 78185855-10bb-3ae3-afae-8960cefce2ba | -7.4432 | -41.9061 | 2024-11-22 14:00:00 | GOES-16 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| 5089b7bc-67fe-3822-af4c-7d44f09455f0 | -5.6942 | -43.7133 | 2024-11-22 14:00:00 | GOES-16 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| fd2029bf-54f4-36ce-bc53-74c3661ce369 | -3.1598 | -42.5565 | 2024-11-22 14:00:00 | GOES-16 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| e0ea95c8-8fb1-3d3c-a63c-59c810751b46 | -5.4546 | -43.2659 | 2024-11-22 14:00:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| a7df99ef-c172-3294-b30a-7ecedefeb840 | -5.7336 | -43.5014 | 2024-11-22 14:00:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| c99c2bc7-ae8d-32df-977c-97960ab9e74f | -8.0943 | -38.5624 | 2024-11-22 14:00:00 | GOES-16 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 96.2 |
| c2359cf6-af75-3b3a-a978-6221ec1c46f3 | -5.7146 | -43.5261 | 2024-11-22 14:10:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 66f45cd0-e4d4-3e33-9031-88964f5c5546 | -4.1782 | -43.9499 | 2024-11-22 14:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 719711a4-4714-3621-80b6-03a034af3686 | -3.6634 | -42.674 | 2024-11-22 14:10:00 | GOES-16 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| f31a980d-670a-3ace-b896-50fcd5250c69 | -3.9646 | -45.3272 | 2024-11-22 14:10:00 | GOES-16 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 806b3064-e00b-3b47-a9ad-e1faa1a3da89 | -5.4736 | -43.2412 | 2024-11-22 14:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| d1eb7030-a156-3bf2-89cf-8a21113c0a6f | 2.2002 | -50.9189 | 2024-11-22 14:10:00 | GOES-16 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 76.4 |
| b8d6ba5e-7110-3241-b20a-12641514d04b | -5.6942 | -43.7133 | 2024-11-22 14:10:00 | GOES-16 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 891a3a83-90fa-3c3f-9d99-a9d69efabee5 | -4.1968 | -43.9489 | 2024-11-22 14:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 2ae2691b-6c6d-343c-9d84-770326332076 | -8.5992 | -35.5335 | 2024-11-22 14:10:00 | GOES-16 | JOAQUIM NABUCO | PERNAMBUCO | Brasil | 2608206 | 26 | 33 | nan | nan | nan | Mata Atlântica | 96.6 |
| b01e57ea-f0fd-35f3-8709-059018237db0 | -3.6132 | -41.6807 | 2024-11-22 14:10:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 92.2 |
| 3bb0987d-e153-37c9-af60-0facd815013e | -8.0943 | -38.5624 | 2024-11-22 14:10:00 | GOES-16 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 102.5 |
| 6fea2a2a-cae4-3c72-9aa6-aad32f164a54 | 1.3819 | -55.9455 | 2024-11-22 14:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 2fd514df-72a0-3f65-923e-43c508445f74 | -5.2464 | -43.5369 | 2024-11-22 14:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 890846a6-178e-372e-9645-2fd0a622912f | -4.1783 | -43.9268 | 2024-11-22 14:10:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 00361bbb-bf82-314a-b2a9-43fa4ee82945 | -5.4546 | -43.2659 | 2024-11-22 14:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| e27680a7-a32c-3740-af68-f8d81394c0df | -7.4432 | -41.9061 | 2024-11-22 14:10:00 | GOES-16 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 86.2 |
| 4212245f-8bbb-3b73-8d4d-c62bb1209851 | -3.6634 | -42.674 | 2024-11-22 14:20:00 | GOES-16 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 409f1bae-ef80-31f9-8819-01b12e1ace01 | -1.9458 | -49.5177 | 2024-11-22 14:20:00 | GOES-16 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 9734d433-d3a6-3ed1-8fbd-08add8bb620f | -5.4546 | -43.2659 | 2024-11-22 14:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 8b96526d-dc37-3847-8d19-3c50067590c6 | -4.1782 | -43.9499 | 2024-11-22 14:20:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 35598724-6438-366b-ae50-0886a7031813 | -5.5325 | -42.9325 | 2024-11-22 14:20:00 | GOES-16 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 76.6 |
| 708847f7-eed2-3f8a-8858-b66c3940dba9 | 1.4002 | -55.965 | 2024-11-22 14:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 194dcef0-8356-32d1-a98b-bf2902b948ef | 1.4002 | -55.9847 | 2024-11-22 14:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| b51a6a66-234a-3dfb-a3b9-317cffc5d09f | -5.8462 | -41.5052 | 2024-11-22 14:20:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| 1e211c01-cbe1-3b65-bbfa-b63fcac7fa7c | -5.4736 | -43.2412 | 2024-11-22 14:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 0b826a89-3f89-3776-b990-63771538d229 | -0.1931 | -51.5218 | 2024-11-22 14:20:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 033de47b-6680-3aaf-969d-70d9dc3eb2e6 | -5.529 | -43.3304 | 2024-11-22 14:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 9720c37f-05c0-341d-aa73-830d34fc450e | -3.1879 | -44.3868 | 2024-11-22 14:20:00 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 30573b9b-2422-37b2-8552-5126df8c3291 | -3.7719 | -43.2534 | 2024-11-22 14:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 2d0d81f6-e483-3817-8e85-c1b643a9aba5 | -3.5144 | -42.5873 | 2024-11-22 14:20:00 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 1863cc34-a08a-37e9-b541-28a0ed0f5e37 | -4.3596 | -44.7182 | 2024-11-22 14:20:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 8ced7ad0-7f23-39d3-89b0-62ba5395d30b | 1.4185 | -55.9648 | 2024-11-22 14:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 125.5 |
| a2f6b9cf-678d-3362-9560-1c43a31fb705 | -4.1783 | -43.9268 | 2024-11-22 14:20:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 0c5f1e45-aabb-3d81-956b-23c6d8e67971 | -3.4103 | -44.5827 | 2024-11-22 14:20:00 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 71.7 |
| ef63016f-1333-3dcc-a793-f22ab607b583 | -5.4736 | -43.2412 | 2024-11-22 14:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |


[Clique aqui para ver as próximas entradas](README70.md)
