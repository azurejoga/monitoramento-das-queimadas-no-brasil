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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f7feb16-cc43-35e0-8781-5bca96a0edab | -5.77698 | -46.56255 | 2024-12-07 01:15:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| b6242070-379b-3d3b-89fa-c488a40d25e0 | -3.52253 | -52.13235 | 2024-12-07 01:15:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f05ba5f1-7cd0-3612-9e6e-ee6170dc9d87 | -4.1692 | -47.53527 | 2024-12-07 01:15:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 2a59f4a3-381a-3d73-a7e3-874d03bfc709 | 2.51775 | -60.99041 | 2024-12-07 01:17:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 2524c62c-ddc4-3b8c-acd8-a6651fa436ea | 2.51932 | -61.00117 | 2024-12-07 01:17:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b71f4cd0-c868-37c1-9c9c-9e1fa6223925 | 2.50768 | -60.99947 | 2024-12-07 01:17:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 59.8 |
| e0a16660-3bcc-33b3-8b3e-27699b4106f7 | 2.73352 | -60.38751 | 2024-12-07 01:17:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 9f1aa513-9098-3a1b-83d9-d47af6dba2cd | 2.94414 | -60.35831 | 2024-12-07 01:17:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e142bbca-9c98-3d37-aa0b-fa8e8b58bb86 | 2.74455 | -60.3891 | 2024-12-07 01:17:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 25786ff2-5be3-3c96-8359-e47c6257d9d2 | 2.7425 | -60.40327 | 2024-12-07 01:17:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 3ca4744b-d645-3123-bd08-939ca464d2cd | 2.50994 | -60.98366 | 2024-12-07 01:17:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 171.7 |
| 976e90e1-4cee-3fe8-a931-304158e190e1 | 2.41926 | -60.65 | 2024-12-07 01:17:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 760bf2b4-f46b-3b78-86c5-cf0f8b34ea05 | 2.5064 | -61.0012 | 2024-12-07 01:20:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 66.2 |
| bf0a4d18-d79a-332b-ab8d-b13b4c5ff249 | 2.5065 | -60.9822 | 2024-12-07 01:20:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 3d8be71b-01f6-369f-82c1-6ff18e4d79be | -12.2944 | -45.4958 | 2024-12-07 01:20:00 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 5d45fd4d-8485-384a-9530-3e480e046c8b | -13.4222 | -41.3234 | 2024-12-07 01:20:00 | GOES-16 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 54.3 |
| d7f62f9f-3508-3d40-9a3b-c023c3264a6b | 2.5247 | -60.982 | 2024-12-07 01:20:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 7c58bedf-d029-3f8c-a34a-d01079acc415 | -13.4027 | -41.3273 | 2024-12-07 01:20:00 | GOES-16 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 69.7 |
| ea2ebe88-2c74-38c6-b167-de9b629b567c | -15.2528 | -53.5723 | 2024-12-07 01:30:00 | GOES-16 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 4aa3451b-7773-3d17-97df-437bcf7ad7b3 | 2.5247 | -60.982 | 2024-12-07 01:30:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 48b56455-5765-3552-803b-09811f5e710c | 2.5065 | -60.9822 | 2024-12-07 01:30:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 7ded7a48-9915-3380-8800-fd4dc0c8f72c | -12.2944 | -45.4958 | 2024-12-07 01:30:00 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 2a861740-5378-38b2-aee7-9ed1cf91cfda | -13.4027 | -41.3273 | 2024-12-07 01:30:00 | GOES-16 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 70.8 |
| 8adbef62-e8f0-3be9-8bd2-bec225185d49 | 2.5247 | -60.982 | 2024-12-07 01:40:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 3b8a328e-bd28-3b7a-9ae9-515afeee5f68 | 2.5065 | -60.9822 | 2024-12-07 01:40:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 237d5f43-8061-3430-9990-5d6dd38ff061 | -13.4027 | -41.3273 | 2024-12-07 01:40:00 | GOES-16 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 3af596dc-aac8-3f81-9150-4d34e1b8fa24 | -13.4027 | -41.3273 | 2024-12-07 01:50:00 | GOES-16 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 64.6 |
| 2473df86-ca7f-36c5-865b-b7bd29feee2b | 2.5065 | -60.9822 | 2024-12-07 01:50:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 82.4 |
| bf8c9f95-8712-3f90-8741-c590a8a599b2 | 2.745 | -60.3913 | 2024-12-07 01:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 1125ce71-6233-397c-af3d-c9e140a11f4f | 2.7373 | -60.3937 | 2024-12-07 01:53:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| aaab17d7-ed74-3453-b90f-a558adadd1af | 2.7317 | -60.373299 | 2024-12-07 01:53:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 017599d8-037f-35ee-b948-58eced3a6ddb | -15.2557 | -53.536999 | 2024-12-07 01:53:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ff91c379-e3c5-32e4-a913-8febe4bf97a1 | 2.7276 | -60.391499 | 2024-12-07 01:53:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 09240c4e-6b75-3f3e-a4e0-08f9990e5c3b | 2.5041 | -60.976398 | 2024-12-07 01:53:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ef2348e0-7ee0-38fb-803c-7f7f76ea3efd | 2.7414 | -60.3755 | 2024-12-07 01:53:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 95e00efd-cf03-3d9a-bd59-3170ef5b9594 | 2.5138 | -60.9785 | 2024-12-07 01:53:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ee6007ea-a419-3bad-832a-9e0a2bd06252 | 2.5004 | -60.992802 | 2024-12-07 01:53:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| dda632f8-f3f4-349c-80ca-18f0175a3e12 | 2.5101 | -60.9949 | 2024-12-07 01:53:00 | METOP-C | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8fca27af-74ce-38aa-af91-f643449ec410 | -15.2633 | -53.563801 | 2024-12-07 01:53:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 24075fc0-8a89-3e8e-bae8-56c5abcef2b4 | -13.4027 | -41.3273 | 2024-12-07 02:00:00 | GOES-16 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 73.5 |
| c5963ebe-7fcc-3146-b69d-90b5eb79969e | -13.4222 | -41.3234 | 2024-12-07 02:00:00 | GOES-16 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 55.0 |
| 5090af3d-27e1-3bbb-9d45-0879d8d1a990 | 2.5065 | -60.9822 | 2024-12-07 02:00:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 27c29b25-26a9-394b-a2b2-3f497fe42a26 | -13.4222 | -41.3234 | 2024-12-07 02:10:00 | GOES-16 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 59.1 |
| e10ab933-2f90-3506-af9b-a5c9ef3a86a7 | -13.4222 | -41.3234 | 2024-12-07 02:20:00 | GOES-16 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 69.4 |
| 69154eb1-3ee8-327d-ab17-acf4e8e7efe2 | 2.5065 | -60.9822 | 2024-12-07 02:20:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 1646dc06-690e-3048-a734-f0251f357798 | -13.4222 | -41.3234 | 2024-12-07 02:30:00 | GOES-16 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 65.0 |
| 189a7797-54ee-3c10-ae7d-5f2931ca7f0a | -13.4027 | -41.3273 | 2024-12-07 02:40:00 | GOES-16 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 59.0 |
| 2172c09d-c1e3-309a-b104-c80fcdb0fa4c | 2.5065 | -60.9822 | 2024-12-07 02:40:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 62.9 |
| c829c4aa-0cc6-3806-a17c-b686bed8c659 | -13.4222 | -41.3234 | 2024-12-07 02:40:00 | GOES-16 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 57.2 |
| 1ca5c3ae-dea4-3b30-aa69-d261aefc53a7 | -13.4222 | -41.3234 | 2024-12-07 02:50:00 | GOES-16 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 80.9 |
| 66fd976a-2ae9-39b0-850e-fe2594d6ee7f | -9.52137 | -35.6803 | 2024-12-07 02:51:00 | NPP-375D | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0411d729-ba07-358f-acff-a2f2b87bd510 | -8.12983 | -35.07171 | 2024-12-07 02:51:00 | NPP-375D | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 8279c96b-84be-36b8-878b-5b84e96d5471 | -9.5203 | -35.68576 | 2024-12-07 02:51:00 | NPP-375D | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 477cb233-17c7-33f7-8c1c-cc937ea4b2a7 | -18.75612 | -40.12928 | 2024-12-07 02:55:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| fcb55084-d8f8-3ec7-baeb-b9e6e78c672e | -18.75789 | -40.12196 | 2024-12-07 02:55:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 7860dc69-20d2-347b-a1cd-3522655b4f9c | -13.4222 | -41.3234 | 2024-12-07 03:00:00 | GOES-16 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 73.0 |
| 5310dccb-40c9-3a75-97e8-00c8e40d321f | -4.4279 | -45.6631 | 2024-12-07 03:00:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 67a3ea3b-6c9d-3cdd-b8b4-817f09ce7030 | -13.4222 | -41.3234 | 2024-12-07 03:10:00 | GOES-16 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 77.7 |
| 808099e1-3ce9-34be-8a3e-28afcc7e32fa | -7.86159 | -35.02431 | 2024-12-07 03:14:00 | NOAA-20 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e467ad38-bfc7-34cc-ac61-72296e5b81f7 | -5.85477 | -35.57174 | 2024-12-07 03:14:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1939c4b0-c732-38a6-aee9-9e5e1166cbde | -7.90969 | -35.24393 | 2024-12-07 03:14:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d90be8ae-aabe-37a6-9c2d-c9bb1f4d0a7f | -7.90833 | -35.2006 | 2024-12-07 03:14:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 269b788a-293d-356c-b0e6-aa8962e7f1af | -6.92492 | -42.84564 | 2024-12-07 03:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dabef4c1-2d36-3545-b39c-7a40754aab02 | -7.90399 | -35.19994 | 2024-12-07 03:14:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| f5764f89-aefd-3823-b137-b3536fdb58e4 | -6.93204 | -42.84712 | 2024-12-07 03:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dee9f837-a380-3053-b1e0-a970de007579 | -7.91041 | -35.23981 | 2024-12-07 03:14:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 83e91e45-b578-321b-864e-b7f74a778adc | -7.90472 | -35.19573 | 2024-12-07 03:14:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 79cb82ca-a654-325c-8a3f-8fcdf649762d | -8.07358 | -34.97723 | 2024-12-07 03:14:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3ab54bd6-1407-3324-99e6-f69b3503a6de | -11.45731 | -43.24921 | 2024-12-07 03:17:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5500477f-7df7-3338-839f-8cbab7669579 | -9.09661 | -43.19964 | 2024-12-07 03:17:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 40156534-aad7-3f0c-9504-6ad7c0668bf9 | -9.52324 | -35.68454 | 2024-12-07 03:17:00 | NOAA-20 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| b8a3648a-3832-3a6f-ad22-8eab5ab96b45 | -11.45852 | -43.24839 | 2024-12-07 03:17:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a4cde563-c9d5-3a88-bb29-5ca6131a9793 | -20.20308 | -41.78834 | 2024-12-07 03:17:00 | NOAA-20 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| e26f72cc-c45a-384c-b64e-c4c7befaaee7 | -9.05892 | -35.70408 | 2024-12-07 03:17:00 | NOAA-20 | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 23166434-5a45-3eac-a31e-38977a811e9c | -20.20583 | -41.78973 | 2024-12-07 03:17:00 | NOAA-20 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 24a38384-9a52-35d7-b629-31af876e46a7 | -13.40331 | -41.33461 | 2024-12-07 03:17:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 23.2 |
| add21850-3f95-34cc-9c57-52c2d502408c | -20.06038 | -41.86853 | 2024-12-07 03:17:00 | NOAA-20 | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f2b30aaa-80fb-3316-9adb-a242e55b6527 | -13.41004 | -41.33165 | 2024-12-07 03:17:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 483d0e8e-426f-3de4-9573-222b1ceff483 | -9.09971 | -43.19869 | 2024-12-07 03:17:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 50e37314-2334-3a3e-b84e-d35528183c10 | -18.89215 | -39.90754 | 2024-12-07 03:17:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f2c140ae-23e9-3038-85c6-3af161e136d9 | -9.07876 | -37.09233 | 2024-12-07 03:17:00 | NOAA-20 | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 500ccefa-3674-3da3-8ac6-23c9a047c522 | -18.60988 | -44.26091 | 2024-12-07 03:17:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b907de57-3eec-345b-bfde-8b4b62d5e769 | -13.40911 | -41.3362 | 2024-12-07 03:17:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 23.2 |
| 0a5f570d-a7f7-3cb7-99ef-5250441af870 | -9.10355 | -43.20154 | 2024-12-07 03:17:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9dd8ee87-cce6-3a80-8575-b1d297b647fe | -11.16179 | -43.57717 | 2024-12-07 03:17:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad8ebffb-efc4-3c0c-b4e6-6f943c40532e | -9.08033 | -37.0912 | 2024-12-07 03:17:00 | NOAA-20 | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fddeabef-1355-3b23-a1bb-adb2c4b4cd35 | -20.06118 | -41.86477 | 2024-12-07 03:17:00 | NOAA-20 | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9d3a62c3-94fd-3ea7-8364-da9fb55898e3 | -20.20053 | -41.78842 | 2024-12-07 03:17:00 | NOAA-20 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2e9eafaa-d608-346a-b9a2-7f0b4f82c4bf | -13.40424 | -41.33005 | 2024-12-07 03:17:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 21.7 |
| c21612cc-8376-37af-b3b6-7d93e3d35145 | -9.09843 | -43.20519 | 2024-12-07 03:17:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5fa9c86b-6ba1-3fec-ad04-cd7237855030 | -18.75836 | -40.12796 | 2024-12-07 03:17:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 16a92eca-a7bb-36d7-b4d7-a6a021c385ea | -9.52398 | -35.68031 | 2024-12-07 03:17:00 | NOAA-20 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 47af6715-f324-3e3b-898b-150160761bc2 | -17.73588 | -39.52466 | 2024-12-07 03:19:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3726afb0-072f-3772-abfb-a12332b1bbe8 | -22.67275 | -42.86383 | 2024-12-07 03:19:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4685d831-a4a5-30e5-a230-b954760a1f7c | -22.67358 | -42.86007 | 2024-12-07 03:19:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2ea34252-6593-3ca6-ba28-3e943db681f4 | -6.74912 | -44.18909 | 2024-12-07 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ce1c36c-1db6-3670-9981-1b905ddfe245 | -2.84119 | -40.30364 | 2024-12-07 04:08:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6912ca55-20ea-3354-8977-7e997cbc8302 | -4.23767 | -46.6153 | 2024-12-07 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f54ef9ca-e302-33b8-a813-11c44578de6c | -6.00795 | -46.40269 | 2024-12-07 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 26408bbd-5c86-3070-a118-117b4b83f300 | -6.00891 | -46.4008 | 2024-12-07 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README4.md)
