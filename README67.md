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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb999a34-4c75-3882-8eb4-0be7b217e37d | 1.09599 | -56.01316 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| b1ee3b45-5aef-33de-a0d9-09950c5a3070 | -3.69355 | -47.11663 | 2024-12-02 04:48:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e77a58e-07b9-3dee-8204-f2a02b897a10 | -4.08646 | -51.1169 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fafa80b0-9169-3174-942d-5ab73497b91a | -2.2173 | -53.62671 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bdd0729b-c31f-305b-b3f4-9643fa1fe40b | -3.87652 | -46.58022 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 80dab27c-2470-38da-8295-8d69be184cf1 | -3.137 | -45.23351 | 2024-12-02 04:48:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72d1e01a-e784-3966-940c-f87e310826c7 | -1.23687 | -51.61179 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53a8bc4d-09bf-36fe-8bb9-f29491291bdf | -1.44678 | -55.19431 | 2024-12-02 04:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bb155eb6-de58-3c7d-ab5b-e7466cf4ceca | -1.62692 | -52.28537 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2fa19e49-af8a-3807-a21a-d100ec419388 | -3.35775 | -49.50951 | 2024-12-02 04:48:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da9a0378-93b9-3099-80bb-cc486fe81a30 | -3.26761 | -53.63585 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89fa41b3-8a53-3785-a415-21d3efc99066 | -3.33429 | -53.54533 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b91aa4a0-5a5d-3a9f-b716-f3cf5bf5c059 | -2.89928 | -54.17001 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85411025-f48f-3d98-9454-37495012e0b0 | -3.33203 | -52.22264 | 2024-12-02 04:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6938e2e3-7724-3820-aa62-c9d5c0232079 | -2.83308 | -54.09235 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74b3f67b-3c9f-3e4d-bda7-e3223c61b270 | -4.06742 | -51.06392 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 63aae63f-8b94-3e10-873a-2f3eee9fd45d | -3.4658 | -53.49501 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65d35e1f-902d-3348-8d01-16a226f912a4 | -1.08318 | -52.37227 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbacb063-2867-3d25-90e7-d3cfbb0eb1d1 | -4.56317 | -45.46979 | 2024-12-02 04:48:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ddaef4b6-59a1-3d96-af44-9fb8745ecb11 | -0.76339 | -52.41959 | 2024-12-02 04:48:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ffdb4b2e-6737-3581-acb0-7d5af66759bc | -3.29419 | -52.07559 | 2024-12-02 04:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 510f3da0-22a7-3e0e-911e-2ff13aa546ba | -2.08501 | -50.62462 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52a443eb-a670-308d-8961-99e941f59514 | -2.59628 | -46.27154 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8beeb10c-3a97-359c-9acb-9e3117b63a0f | -4.36042 | -46.26977 | 2024-12-02 04:48:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 274eaba9-34dc-38ce-9dc7-8dbd7f72eec0 | -2.02602 | -52.08098 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fbbdab82-babf-32cd-a7ca-9e21eb652ae3 | -3.4934 | -53.80326 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 76bb0ef6-208a-378f-b5c6-0bf241c8e7e7 | -0.5931 | -51.68697 | 2024-12-02 04:48:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d6ee099-0ac8-3b49-8dd2-607c2e746108 | -4.08697 | -46.13485 | 2024-12-02 04:48:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a9964dc-8f76-3963-941f-c627d7493363 | -2.15272 | -50.62794 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9979f6f-6eee-38ae-997b-aebc07f5bf98 | -3.69158 | -51.34042 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdcc6b33-0704-393c-8d38-6826420536a4 | -3.87708 | -46.57656 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a0b578f-a4a8-345b-9f8c-e6ad92daf667 | -3.17629 | -53.63709 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7374dde-ad6c-38a8-aec8-e58b14af3fde | -0.95059 | -51.6618 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 623a1b3e-806a-37d2-88e6-1e92840162ef | -3.4192 | -54.02586 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 841ab646-c75e-36c9-8748-0fdb39a5e6dc | -1.47541 | -47.33731 | 2024-12-02 04:48:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0cb01a3f-7f6d-32a8-b725-2d06d882acc2 | -4.00152 | -46.65451 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb8c5490-75f1-336a-b9ec-2e4b9e90741e | -2.35973 | -54.48918 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a92e030d-e715-32ed-81bd-97203cb5ba06 | -2.65952 | -54.08623 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 07e40198-0fc0-3e05-aaee-d61b0c5a4d30 | -2.98093 | -53.89294 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1082102d-9369-3275-bcfd-4be0ddfe183b | -2.46887 | -53.96334 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b81d982c-5307-33b5-ae74-454efcdf5118 | -3.2589 | -46.44712 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee66d9ff-b3be-31e8-b37a-8000401c02e5 | -1.88077 | -45.53017 | 2024-12-02 04:48:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 441ee831-6788-32eb-a681-4941c9566a78 | -2.62687 | -54.33635 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90e26214-6913-3958-8b4f-0144ca600e9c | -2.45652 | -53.62162 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2bba93ec-ccf9-32ab-8383-e47d735d5b21 | -1.27876 | -51.64979 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35be8030-9829-3ebd-8922-4c3b1b0e2741 | -1.06861 | -51.79698 | 2024-12-02 04:48:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fa130cb-4651-3bb0-938f-71f6bda41ec5 | -2.04397 | -54.6555 | 2024-12-02 04:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2a0060a1-6538-36ff-b36e-3d1ac5a246c1 | -3.17518 | -54.32663 | 2024-12-02 04:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca1dbfaf-6650-3489-ae16-2294cc470856 | -4.62146 | -48.02076 | 2024-12-02 04:48:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66c0042c-2219-3e02-9bdc-3a6526c8bfc6 | -2.58906 | -46.01086 | 2024-12-02 04:48:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c5f7eb0c-ca84-30c9-9074-40aa2433b9a3 | -2.74053 | -54.16925 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28aeb3ea-3b6d-396d-a574-0e83cdac1493 | -1.7249 | -52.48258 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f048bfb1-a120-30ad-9e2a-5d28217e622a | -5.58125 | -45.14543 | 2024-12-02 04:48:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| f47afd60-1134-3b4f-bb71-481d20768c87 | -3.61696 | -49.91794 | 2024-12-02 04:48:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e71ebe30-fd2f-31bf-8d4e-7a3dd72fe8c6 | -1.18722 | -51.77669 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5189ef8-7de5-3c1e-a558-6dc64cf27156 | -3.31885 | -54.17462 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eae756ab-f35e-3982-98ff-39511db21bbe | -1.58372 | -51.24416 | 2024-12-02 04:48:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39fdd327-9956-3ef1-b5ba-d76e07396cae | -3.09352 | -54.27029 | 2024-12-02 04:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1a70f49-e9e4-349c-910a-80e58d270917 | -0.77453 | -52.39234 | 2024-12-02 04:48:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbd73e5c-1498-3980-b7b2-b787f1601bd2 | -0.96545 | -51.65355 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b7fd26b9-4685-3706-a734-71921fa51194 | -2.99054 | -51.45687 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 566eb3d4-2806-3363-a018-3392477e4802 | -3.27129 | -46.4489 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 52abe340-ab40-3105-a568-6452e201c035 | -1.74288 | -52.65128 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd48afe0-a49a-3947-b93d-0627cb517889 | -2.77695 | -48.58367 | 2024-12-02 04:48:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4b4f8ca5-d3e1-33a5-9598-90a3acbd4579 | -2.9726 | -53.28873 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a011399-a0c5-3dc7-839d-b66b398baade | -1.64787 | -52.75261 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d863bc6-3bf4-373a-82ff-d66c152d44be | -4.19081 | -50.68877 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edc4209b-98d2-3df3-9206-da89cfb2888e | -4.90678 | -41.34163 | 2024-12-02 04:48:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ef01966c-a6d9-3323-a5a1-db6bf203091b | -3.30318 | -51.10991 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36514267-24ac-346f-9706-65a23b6d867b | -3.42992 | -53.89285 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 72950821-65f7-3fe3-bd50-7bc9ebb1985e | -3.8623 | -52.39406 | 2024-12-02 04:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d62c1487-1222-3f10-90b5-56208ff3a8be | -3.85933 | -47.04834 | 2024-12-02 04:48:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82294fb1-ade2-392f-8982-370dab18e782 | -2.55039 | -53.40568 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 611c7b68-2272-32c9-8733-f9300f502fdd | -1.78815 | -52.74928 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08abf09c-1152-32d4-9fa3-b475d9249abe | -3.34599 | -50.75134 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22cea81b-abd2-3776-9081-3ee728cdb622 | -3.90087 | -50.30254 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 044970dd-7ad4-30d8-b848-76bcbc09b15a | -2.99251 | -53.42531 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e941565-9d95-399c-9ec5-7e661c105f97 | -2.80244 | -53.12213 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc9d5ca2-93db-3eb5-bec1-6c3f566d990e | -1.27155 | -51.63107 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 976a67af-62d8-33ca-8444-73bcbcf2c1ca | -1.06656 | -53.38982 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35bf42d0-90c5-387a-af4e-8de9768bf19b | -2.01238 | -51.43423 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ca410ff-2d30-3973-bc3c-83e714c78011 | -3.86834 | -50.17063 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0697000c-4918-3583-a321-ca7e5945d0a3 | -1.37605 | -52.56199 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 835a3f21-4a13-33e0-84b0-9088d2e8660e | -1.07926 | -53.63843 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0c6f6a7-12aa-3004-93d7-28a7d314096c | -3.66541 | -50.19581 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cdcba956-92e7-30dd-875b-d85095c71bac | -4.63851 | -46.90052 | 2024-12-02 04:48:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b44b584-628f-3cf9-a67f-b67e25de20cd | -3.95618 | -49.76125 | 2024-12-02 04:48:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b711408-764e-3ea8-84f6-83c825ad62e1 | -2.20533 | -48.34161 | 2024-12-02 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3eb1312b-a829-3fe4-b25a-365c8824a827 | -1.69712 | -52.63689 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d41f1ad-bc7b-3b41-ac39-4399d0085569 | -3.88344 | -51.41656 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6cbc1866-3ec9-36bb-876d-b46202c6e4b7 | -1.76576 | -52.00814 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f93ab44-e74d-390a-b2ea-c2c0a7bafec3 | -1.28645 | -51.64395 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 688d21eb-fc56-369c-8aba-7fef9d8d5813 | -2.48715 | -46.57714 | 2024-12-02 04:48:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c15cdaa2-9be0-3ed3-89a8-e0140efa5bcf | -1.00587 | -51.71973 | 2024-12-02 04:48:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e7a0faa-042e-3e61-8666-99943f4ba277 | -1.22861 | -53.36108 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8243f476-77c1-339a-bcaa-002d593e4eb9 | -3.2666 | -46.45205 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8598953d-d74d-307b-904d-0cc474e50324 | -2.00942 | -51.19448 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb50034f-9da6-3871-b007-bb5f8224f98f | -4.19529 | -50.68216 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 24692b93-34f5-36c8-95d2-2757147d9d97 | -3.39358 | -51.24823 | 2024-12-02 04:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e1eaa8c4-22d4-3f26-af3f-cae9f1bf7370 | -1.05742 | -53.38075 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README68.md)
