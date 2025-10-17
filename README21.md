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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a531046-401d-368d-88af-477c73733e52 | -3.5028 | -52.4938 | 2025-10-17 03:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| da99b6cd-cad0-3b43-85fa-61f41c2be68c | -2.7401 | -49.3927 | 2025-10-17 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 0c22003a-2c5f-3d32-a3dd-b3dbbb7c5cb9 | -4.4246 | -43.4038 | 2025-10-17 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 3683947e-1df7-32d9-8693-14d2cf4d1a32 | 1.7848 | -55.9014 | 2025-10-17 03:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 9fdfdd7e-4e20-31db-bca7-cb77f827a396 | -11.398 | -44.1933 | 2025-10-17 03:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 4b8dd92c-aa29-310e-9f84-845c85368df6 | -11.3976 | -44.2167 | 2025-10-17 03:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 195.5 |
| abeb045f-bc73-331c-bdd5-1cc3fda4c874 | -10.5132 | -43.4289 | 2025-10-17 03:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| b589eee4-d7a0-3dee-ac95-c890304f70d6 | -11.4939 | -44.179 | 2025-10-17 03:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 7745eb17-8285-327b-850e-ddcd2e13e14e | -14.3227 | -51.4475 | 2025-10-17 03:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| fd3f7843-5bd4-3bcb-bb2b-906a744b5d56 | -10.5337 | -49.5687 | 2025-10-17 03:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| eb7944df-433c-3443-82bb-d7ebed480c58 | -14.3417 | -51.4663 | 2025-10-17 03:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| f215b83a-6735-3d6e-871c-a9d54ac4bbd1 | -14.3231 | -51.426 | 2025-10-17 03:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 8342d720-3569-308c-9052-da2a64bc645a | -11.4168 | -44.2139 | 2025-10-17 03:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 08f8d027-37a0-32c3-853f-09c5925e5dbf | -9.1609 | -41.0458 | 2025-10-17 03:10:00 | GOES-19 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 63.8 |
| 8d5b2958-4906-30eb-a2c2-0565e6ac7fca | -3.2359 | -45.9862 | 2025-10-17 03:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 3c89cc92-a05e-3862-974b-3e1d4fa1af84 | -11.3972 | -44.2401 | 2025-10-17 03:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 1290baff-6f80-34ab-9e1e-a5eb6f283cd5 | -10.2939 | -44.0221 | 2025-10-17 03:10:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 146.1 |
| c6aa0c2a-e035-38a6-b2f2-9fe0c3f3f328 | -10.2745 | -44.0481 | 2025-10-17 03:10:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 33a874a5-e5b9-3f1c-a9c2-cd68d1442419 | -4.4059 | -43.4049 | 2025-10-17 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 141.6 |
| adbe6c7a-33c0-311a-88a5-c620e76dc7ff | -3.236 | -45.9639 | 2025-10-17 03:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 86d7417f-59c0-3e34-aebd-792b74d49a3a | -10.534 | -49.5471 | 2025-10-17 03:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 36311a0b-48b8-3140-b731-2f3ab1636ab5 | -14.3223 | -51.4689 | 2025-10-17 03:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 659dbd9f-0b60-3282-a01f-13677c2499f4 | -9.1567 | -46.6241 | 2025-10-17 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 608bc00c-3fa3-3e25-8256-dda1415f232e | -11.4164 | -44.2373 | 2025-10-17 03:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 7a8f9127-d6f8-3f63-9d5b-52e4e2adfd31 | -10.2748 | -44.0247 | 2025-10-17 03:10:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 992f0db4-d5f9-3696-92eb-cae01d50c062 | -4.4061 | -43.3816 | 2025-10-17 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 916c6284-4158-3cc0-85af-e587e97a22d5 | -9.1378 | -46.6261 | 2025-10-17 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 262.7 |
| 831880a0-1dca-358d-bd53-5ff24bd8c4e3 | -13.7102 | -40.9887 | 2025-10-17 03:10:00 | NPP-375D | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9bdd83a9-5b5e-3762-8a1a-44d98452163f | -12.3234 | -41.39371 | 2025-10-17 03:10:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8f050bbf-2608-39c7-81a2-cca8d8c2f5d9 | -12.32207 | -41.39983 | 2025-10-17 03:10:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 7a204cdd-1fdd-3eb7-b70d-cd31223153e4 | -16.54719 | -41.65123 | 2025-10-17 03:10:00 | NPP-375D | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 10d9905c-7a6e-3765-85f0-ac49c1bc0b2c | -17.96919 | -39.88469 | 2025-10-17 03:10:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 2814d90f-ebdf-3586-8b71-4c566ee8a8e5 | -12.90642 | -41.83193 | 2025-10-17 03:10:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 67ffb54e-6bd2-38a8-b50a-376e66e0b1de | -17.9702 | -39.8801 | 2025-10-17 03:10:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 167f92b1-ec2a-3a65-ab09-b497a954ed31 | -12.91527 | -41.82951 | 2025-10-17 03:10:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 498bbae4-0cfd-34e0-b9f8-eb59f09ce709 | -17.96326 | -39.88324 | 2025-10-17 03:10:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| b45e93f0-3e2b-3361-9ec2-95ea925c63b8 | -12.91342 | -41.8347 | 2025-10-17 03:10:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b1f10600-28bd-379a-8997-28c8a128c6d6 | -12.32151 | -41.39507 | 2025-10-17 03:10:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 28fe301d-1a90-3855-9251-e03235cc1d6d | -16.54663 | -41.6566 | 2025-10-17 03:10:00 | NPP-375D | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 5e65ac3a-26e6-304f-a99e-4f15187c172f | -16.54805 | -41.65042 | 2025-10-17 03:10:00 | NPP-375D | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| df688342-1ed6-3623-b8fa-9b281d18de6c | -13.70896 | -40.99435 | 2025-10-17 03:10:00 | NPP-375D | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3bc85df1-aa8a-3529-965c-1c69977b8932 | -18.6973 | -43.72912 | 2025-10-17 03:13:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03ff7460-4d3f-3ec3-a216-b13bd1929e04 | -10.2935 | -44.0455 | 2025-10-17 03:20:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 200.6 |
| 5082562e-60bb-3ea0-bdce-c859380f1a10 | -9.1564 | -46.6465 | 2025-10-17 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 149.1 |
| d971a054-5019-3d8b-b16f-bb4b6f95338c | -14.3223 | -51.4689 | 2025-10-17 03:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 002c8d7d-4f05-337c-9a87-9fdc91a397d2 | -11.4168 | -44.2139 | 2025-10-17 03:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 9cd277b8-f490-318e-86c9-0c5814a36c75 | -11.398 | -44.1933 | 2025-10-17 03:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| f30da227-8985-36ea-a0c4-fc44fe8c202d | -9.1372 | -46.6708 | 2025-10-17 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 1da12dc2-107d-3664-9f4b-754b81653a3e | -11.4939 | -44.179 | 2025-10-17 03:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 2e4c03f3-011c-3880-b452-0d2c1bcf75d2 | -9.1567 | -46.6241 | 2025-10-17 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 42c2e647-24f0-386e-9e00-273fbe13c197 | -11.4935 | -44.2024 | 2025-10-17 03:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| f9340630-74b8-3374-ae85-fc092513e836 | -10.5136 | -43.4052 | 2025-10-17 03:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 85cf2737-e9f7-3be5-8d80-669f1981d884 | -9.1375 | -46.6485 | 2025-10-17 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 247.4 |
| 16e1bf8b-f3de-3a9a-b1a9-6e2ad8e11006 | -10.5132 | -43.4289 | 2025-10-17 03:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| d14fedba-ffe4-34a2-bc76-11a072ee86a0 | -9.1378 | -46.6261 | 2025-10-17 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 8625699c-39b9-3bad-8aec-6a15f1bc095c | -3.5028 | -52.4938 | 2025-10-17 03:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| ba16b1ab-6b74-3d4f-a16d-573d5f6d69ea | -4.4248 | -43.3805 | 2025-10-17 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| fa8094bc-efa1-3bbb-9c2c-d0d0a92f41d3 | -14.3227 | -51.4475 | 2025-10-17 03:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| efbfcb09-fa3e-396b-a3b7-25b7c4de9b76 | 1.7301 | -55.8035 | 2025-10-17 03:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 9c4e0c8c-95e6-3478-b7d0-bfe101c4d002 | -11.3976 | -44.2167 | 2025-10-17 03:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| ff2a4349-ef87-3ba4-b415-e34951ab00f6 | -14.3417 | -51.4663 | 2025-10-17 03:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 94583376-963d-3cd9-853b-0511f0d79efa | -10.534 | -49.5471 | 2025-10-17 03:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 74390366-0e57-3c93-aabb-39d9b589fa22 | -4.4059 | -43.4049 | 2025-10-17 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 127.1 |
| de6461f3-9bfa-3a0f-b383-20b4f300794d | -4.4061 | -43.3816 | 2025-10-17 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 1e74c7a9-00f2-3ee4-8421-8aebf07e6963 | -10.2748 | -44.0247 | 2025-10-17 03:20:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 2aee9276-729d-3c73-8b2b-8d5c9cd287cf | -2.7401 | -49.3927 | 2025-10-17 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| e4397401-fd7f-392a-ba0e-d0c93bd1e1ff | -10.5337 | -49.5687 | 2025-10-17 03:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 79ea7bd2-2359-3070-a787-5f031de5fcec | 1.803 | -55.9603 | 2025-10-17 03:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| e847cbc4-dba6-3c84-bc5a-f8fa4f8c3901 | -10.2745 | -44.0481 | 2025-10-17 03:20:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 0cd6acee-1b4d-3a24-bf1c-fad6fbc033a1 | -10.2939 | -44.0221 | 2025-10-17 03:20:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 203.4 |
| dc79b9b8-cdff-3bac-823d-939e35419703 | -10.4941 | -43.4315 | 2025-10-17 03:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| a278bf8a-aaa1-36b0-b837-3fd107502b05 | -10.9475 | -49.7605 | 2025-10-17 03:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| a08b9760-9673-302d-b35e-dd891fbf7006 | 1.7668 | -55.7439 | 2025-10-17 03:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| ca9665c1-09ac-3ad6-8825-1c88e09ae0a9 | -14.342 | -51.4449 | 2025-10-17 03:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 3e6f05dd-e17e-32d5-a804-a841369ed303 | -10.9472 | -49.782 | 2025-10-17 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 5e3f5b90-5916-38ef-8060-3fa15cdae866 | -4.4246 | -43.4038 | 2025-10-17 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 690ec21e-9721-3bcb-9485-6cf9f17d7d1d | -11.4172 | -44.1904 | 2025-10-17 03:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| fade3209-c2f8-305b-bb00-04767d4680f9 | -5.88938 | -43.90197 | 2025-10-17 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4297181b-4da6-37b4-96dc-c94d8941abb3 | -7.95289 | -44.12275 | 2025-10-17 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4c1a7d0b-319d-3806-a705-88f7efc956de | -4.39367 | -43.40894 | 2025-10-17 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 855ca169-cc4a-38a5-93e6-291bc97dab17 | -8.72855 | -43.87753 | 2025-10-17 03:28:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 60f30585-c9c9-35ed-baff-68cb586361a9 | -7.27922 | -42.31299 | 2025-10-17 03:28:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3a59aa18-d132-37a2-8eef-bb60ab56270c | -8.23518 | -43.3342 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| de6fd417-ab48-3459-a7f1-0c4ece4e3258 | -7.94856 | -44.11123 | 2025-10-17 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 382c094d-eaed-3fbb-a38b-f8ad4f88771c | -8.38194 | -46.25314 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bce93600-9941-33c4-8a0f-3fa957fdce31 | -5.88754 | -43.19604 | 2025-10-17 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1cd61233-65ec-343a-9c04-a2dbfd406d26 | -8.41157 | -46.28952 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 24fe9357-c469-3e9d-a906-436d008e6c3e | -7.46845 | -42.16812 | 2025-10-17 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 81d1933b-0887-3932-9163-aedb7f3d5ceb | -8.37255 | -46.32067 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| def27405-db83-37ea-97db-7492b7e64472 | -7.89905 | -44.98557 | 2025-10-17 03:28:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 24928b71-6212-3834-a8b4-03751b200f90 | -6.01217 | -41.93841 | 2025-10-17 03:28:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0f21d6e0-e9a8-3559-a453-8dfd34e2f557 | -5.29579 | -43.55519 | 2025-10-17 03:28:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e9817e0b-0388-3a3d-ad4a-7bfbcae50ef7 | -7.02685 | -41.82628 | 2025-10-17 03:28:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e7cde278-e755-332e-ae0b-bca5db29d732 | -6.1366 | -41.72654 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e66286e2-a4ba-3391-ba76-3a92803bd6ea | -8.32104 | -40.38333 | 2025-10-17 03:28:00 | NOAA-20 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2b1a2643-d77b-3e3a-9aea-3aa291b7271f | -7.45699 | -42.68351 | 2025-10-17 03:28:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dc78c29a-85f6-3562-b0b0-407e05004c52 | -7.27773 | -42.32118 | 2025-10-17 03:28:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4cdbbc8f-aca4-32ed-aaaa-df3b59497526 | -3.62896 | -42.77854 | 2025-10-17 03:28:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a83e0c61-4b98-35e2-bf2c-0f61f93c6fa5 | -7.83322 | -45.46642 | 2025-10-17 03:28:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c962bc97-5f00-3039-bea6-6b3710539f3c | -7.45883 | -39.96371 | 2025-10-17 03:28:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README22.md)
