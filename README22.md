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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 356fbede-81a5-3ce2-875d-569ed905ab14 | -15.35087 | -49.13168 | 2025-08-01 05:08:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af8abd39-a6cf-3ec3-9ed2-120e82df7fca | -18.4516 | -46.92531 | 2025-08-01 05:08:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 24a3c908-e460-3807-9cb4-e7cc489a2b89 | -15.09646 | -55.24063 | 2025-08-01 05:08:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e86be02d-b655-3fa7-a108-9649a449a979 | -20.01517 | -47.38448 | 2025-08-01 05:08:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca06e50e-5253-3be8-9c84-16a860d1a63c | -21.44522 | -57.14443 | 2025-08-01 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80deed9d-b4a0-355d-87aa-4fc0b8c0a7ca | -21.48077 | -57.1077 | 2025-08-01 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8abf532-54c5-3312-bedb-188b75724bc3 | -20.44198 | -46.43355 | 2025-08-01 05:08:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 039246a4-c1fe-380d-a7b5-da6a479d8732 | -15.4092 | -55.77969 | 2025-08-01 05:08:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c4b7e8ae-98f6-3777-b1be-c073a369b4f1 | -21.44233 | -57.13984 | 2025-08-01 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 424ce03c-df96-37ac-a0a3-1926eb1e215b | -20.44946 | -46.42205 | 2025-08-01 05:08:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 111937e1-3455-3dea-b688-6b5496f75339 | -18.00839 | -49.39435 | 2025-08-01 05:08:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24f5944a-97d0-3e4d-8fb6-1bd9c5167929 | -15.08343 | -55.20605 | 2025-08-01 05:08:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e7392e7-999d-3e6d-ab42-07d2dc4a1e79 | -20.4422 | -56.99132 | 2025-08-01 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4b9f381-d6c1-34e4-8dc5-b7f3e343d8b2 | -19.01935 | -54.65895 | 2025-08-01 05:08:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75606009-cf37-35f0-a116-8bf7c56f6a0d | -18.13577 | -53.83109 | 2025-08-01 05:08:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98e375d8-084d-3adc-8f03-63b8479fbe38 | -15.40574 | -55.77916 | 2025-08-01 05:08:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5e5028b1-04b0-319e-a0fd-5e1446bdac14 | -15.47504 | -52.63756 | 2025-08-01 05:08:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc0efb70-0639-3676-ae91-c4779b3c5086 | -15.07934 | -55.20942 | 2025-08-01 05:08:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e1905910-d87e-3cab-a800-ea2c9b94c558 | -15.0782 | -55.21727 | 2025-08-01 05:08:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca282ba3-9476-37a4-b401-bee1760c2d63 | -15.08941 | -55.23955 | 2025-08-01 05:08:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a989bc5-9f5c-3c02-aede-4d53a1cf917f | -22.70328 | -48.046 | 2025-08-01 05:08:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8661f4f6-2211-3c58-a386-2b58dcb81f68 | -18.44506 | -46.92843 | 2025-08-01 05:08:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 89c25a63-dbbc-3078-88a1-639a0de5654a | -18.94677 | -54.32617 | 2025-08-01 05:08:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85cbe247-866b-30a9-8d9b-499f087811f5 | -15.40977 | -55.77576 | 2025-08-01 05:08:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb24f02c-0a4c-3fb3-a89f-211aac6f3b5e | -16.13269 | -46.87617 | 2025-08-01 05:08:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0041b69c-0c48-3ad8-b4fb-6ceda78c5df9 | -19.01556 | -54.6583 | 2025-08-01 05:08:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a34887a-f5f5-3a9f-a6be-843cda00e270 | -20.00912 | -47.38309 | 2025-08-01 05:08:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d2254201-a29e-36ee-b3ed-485017a62330 | -15.08646 | -55.23502 | 2025-08-01 05:08:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9716438-f665-3a51-825a-8a9966523948 | -20.41114 | -57.01089 | 2025-08-01 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c1f8cd2-08f6-3ede-b12c-99a3376ab9fb | -15.08285 | -55.21004 | 2025-08-01 05:08:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ad777226-9c59-3c23-9fe2-7ab666d2b5aa | -18.00804 | -49.3975 | 2025-08-01 05:08:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f24a203d-026a-39cb-b44f-b26aeffc736a | -15.07877 | -55.21336 | 2025-08-01 05:08:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 87e09fd5-f352-3669-943a-94c4609def8f | -21.4458 | -57.14041 | 2025-08-01 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6d8fcf7-e4cf-3eec-8479-a0a0ac104a27 | -18.95063 | -54.3268 | 2025-08-01 05:08:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 988e160a-4aba-3eb6-abf9-10cceff35e99 | -15.08695 | -55.20667 | 2025-08-01 05:08:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc46467f-26c1-37c1-8a1b-73d583aa5669 | -18.13661 | -53.83 | 2025-08-01 05:08:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 512391a8-f607-3998-92ce-ca96f00b459a | -20.44243 | -46.42794 | 2025-08-01 05:08:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a282eaf6-7512-31db-ba36-d0a77f235020 | -16.13219 | -46.88089 | 2025-08-01 05:08:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c59a9b6f-650c-31b8-a9df-8d13fa0ee3f9 | -6.7478 | -59.1716 | 2025-08-01 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 101e504c-d74f-35aa-9ab0-2f1fde15d134 | -8.0324 | -43.1022 | 2025-08-01 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.5 |
| a8ed40e0-8890-3d33-9ea4-08cacb0d7c2e | -8.0513 | -43.1001 | 2025-08-01 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 766870fd-6b3d-3bbe-bf7f-e6ebdd709943 | -8.051 | -43.1237 | 2025-08-01 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| dcf6e524-e156-3135-8850-bcfb46d4c124 | -6.7477 | -59.1909 | 2025-08-01 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 23d48f18-ee1e-34ee-8a76-efa456090834 | -6.6376 | -59.0988 | 2025-08-01 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 5699f9f6-e407-34b8-98ea-9816fd28ff81 | -8.0321 | -43.1257 | 2025-08-01 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 128.0 |
| e83c2fbd-38c4-3f66-95c9-bd0abfb96910 | -6.7295 | -59.153 | 2025-08-01 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 14485bee-e458-368b-9e89-820b9f6c7a33 | -6.7293 | -59.1916 | 2025-08-01 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| e9e684dd-d2b9-37ca-b67b-242dc092d1d6 | -6.748 | -59.1523 | 2025-08-01 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| bd64d178-6593-3e6c-8dbb-96de20a555c6 | -6.7294 | -59.1723 | 2025-08-01 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 205.2 |
| 227ff3b7-97af-3b72-acd8-79b49a7656b9 | -23.52531 | -47.83916 | 2025-08-01 05:10:00 | NOAA-21 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| c0d08d30-1a0c-3c6b-9240-5070d1418e69 | -22.70578 | -52.6321 | 2025-08-01 05:10:00 | NOAA-21 | TERRA RICA | PARANÁ | Brasil | 4127304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b712f46e-3e77-36be-8a59-f4571ea11509 | -23.03759 | -50.15905 | 2025-08-01 05:10:00 | NOAA-21 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 70f6de75-9bd9-35e1-8804-5d7e861d029c | -22.27779 | -55.9614 | 2025-08-01 05:10:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9377569-49fb-352e-879d-6dcc1b916694 | -23.51303 | -47.83708 | 2025-08-01 05:10:00 | NOAA-21 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| fc7a7428-1c2a-375a-a68a-9f536a592fd6 | -23.51916 | -47.83823 | 2025-08-01 05:10:00 | NOAA-21 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| a2450783-dcc1-3ba9-9214-1380c86e7e73 | -29.2871 | -50.49177 | 2025-08-01 05:10:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 695015ea-ea8e-3930-a222-6b35c61e205e | -22.27658 | -55.96372 | 2025-08-01 05:10:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac3c063c-4fd0-3991-bd90-c5c735ab8729 | -23.03914 | -50.1607 | 2025-08-01 05:10:00 | NOAA-21 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 79010e25-46d2-3f72-8945-601286990836 | -24.52861 | -50.79619 | 2025-08-01 05:10:00 | NOAA-21 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4fbcd0c6-bed9-3e85-8f0b-a139ea7c6b82 | -28.97947 | -50.44689 | 2025-08-01 05:10:00 | NOAA-21 | JAQUIRANA | RIO GRANDE DO SUL | Brasil | 4311122 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f0abb48b-36bf-34e6-a17c-8a0ef8ddaf52 | -23.5257 | -47.83419 | 2025-08-01 05:10:00 | NOAA-21 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| 83c11ba8-5b7d-3acd-8bae-f7dca22eebb5 | -24.52339 | -50.79574 | 2025-08-01 05:10:00 | NOAA-21 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 394c7f7e-9ba3-3511-90b8-3ea017ff6511 | -28.25355 | -49.70876 | 2025-08-01 05:10:00 | NOAA-21 | BOM JARDIM DA SERRA | SANTA CATARINA | Brasil | 4202503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 955961d0-ac22-3075-b715-1fc0f3854fca | -28.64593 | -50.02201 | 2025-08-01 05:10:00 | NOAA-21 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 13bec5bf-879d-335f-8469-b8414638aaf9 | -22.26774 | -56.06295 | 2025-08-01 05:10:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1843c1c-1133-3b73-9a2c-1274295f461c | -22.26069 | -54.78967 | 2025-08-01 05:10:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d4d04f6d-a38b-3da4-96d4-00e312ee5da2 | -23.51954 | -47.83333 | 2025-08-01 05:10:00 | NOAA-21 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| d63fbd72-5e4a-340a-acc9-3b889a0386a9 | -22.27134 | -56.06136 | 2025-08-01 05:10:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ef751ac-4d0e-3954-98ac-a82eb3d94842 | -22.96168 | -49.12423 | 2025-08-01 05:10:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1032cdbe-0853-3198-8c71-c8bd3ec5ccee | -22.95601 | -49.12352 | 2025-08-01 05:10:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70b83c68-cdcb-32b6-a8a3-86f19ae66427 | -28.25317 | -49.71383 | 2025-08-01 05:10:00 | NOAA-21 | BOM JARDIM DA SERRA | SANTA CATARINA | Brasil | 4202503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4e0d1844-7633-39c2-8737-c91ff183c87f | -23.51341 | -47.83222 | 2025-08-01 05:10:00 | NOAA-21 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 53ce679d-fe2c-3534-9286-6304adb6c001 | -22.27718 | -55.9659 | 2025-08-01 05:10:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 589c21c7-7fa6-383e-9794-7879616b20dd | -23.00291 | -48.6393 | 2025-08-01 05:10:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 303782a0-533f-3614-8504-969134351ba8 | -8.02872 | -43.11869 | 2025-08-01 05:12:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| 2bb2dd31-d870-3919-a366-721282b60f40 | -8.044 | -43.10252 | 2025-08-01 05:12:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.5 |
| 5fc3b326-977f-3a7b-9c48-dad03e71b63f | -9.30339 | -40.24464 | 2025-08-01 05:12:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 7b1115f4-1aba-3aa4-bf53-b9e332253eb0 | -8.05629 | -43.1045 | 2025-08-01 05:12:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| bd2f08cc-a32b-3d69-a79f-dd21ceea9e2e | -10.08104 | -46.72096 | 2025-08-01 05:12:00 | AQUA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 4b99da78-6e95-393d-a5f1-2ca3fa144f5e | -10.07533 | -46.7529 | 2025-08-01 05:12:00 | AQUA_M-M | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| e1dcddca-4476-3a2e-bce2-e853506884b2 | -8.04103 | -43.12069 | 2025-08-01 05:12:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 116.5 |
| 006c2063-6692-3267-8e95-b1f30e7b2b53 | -8.03173 | -43.10041 | 2025-08-01 05:12:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 123f1304-9f40-33cf-a1a2-5b05c1db3600 | -23.51418 | -47.82444 | 2025-08-01 05:16:00 | AQUA_M-M | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.3 |
| 268a962e-ef94-3901-a5ee-18ecc86592ae | -23.5108 | -47.83128 | 2025-08-01 05:16:00 | AQUA_M-M | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 29.8 |
| a4e7844c-b8f4-3e15-8bef-2e7032771efe | -8.0321 | -43.1257 | 2025-08-01 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.5 |
| a3e5c8eb-9d78-3c52-84bc-aecc7632a724 | -6.6376 | -59.0988 | 2025-08-01 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 6146968a-89b6-34ae-b0ce-b7d397eb4d8e | -6.7295 | -59.153 | 2025-08-01 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| ec71f318-169d-35c7-8de9-be6a53ce6c6c | -6.748 | -59.1523 | 2025-08-01 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 558467e9-a7ef-37e3-b321-2f2f78691773 | -8.0513 | -43.1001 | 2025-08-01 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.2 |
| 6a5219fe-cba6-31fc-912b-4a1473996d97 | -6.7477 | -59.1909 | 2025-08-01 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 37fc9c0c-378a-3d21-919d-fe413cef98ff | -6.7294 | -59.1723 | 2025-08-01 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 189.4 |
| ecedca24-f607-335c-b677-50b332102337 | -6.656 | -59.0981 | 2025-08-01 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| ae8439c9-5614-3730-8692-a8cd7dd5f4de | -8.051 | -43.1237 | 2025-08-01 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 9727d1a8-8faf-3ca6-91d7-4b8bf64a9356 | -6.7293 | -59.1916 | 2025-08-01 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 0a65966a-1574-3bd6-bd20-7fd31f82da19 | -6.7478 | -59.1716 | 2025-08-01 05:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 160.8 |
| 47f72164-7a97-3533-a5ae-d74554b4f9de | -8.0324 | -43.1022 | 2025-08-01 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.4 |
| 6a822539-7f39-3a57-b8a4-a393cba41493 | -5.06087 | -56.92778 | 2025-08-01 05:29:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 92672512-e03a-3e6b-ba99-4b39d547964e | -4.30911 | -48.10491 | 2025-08-01 05:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| aa009710-29a6-3aa8-8302-4b35e968ebe5 | -2.60888 | -51.94843 | 2025-08-01 05:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9be7724-b3e0-3d2f-bc0c-99347b01295f | -4.30509 | -48.10563 | 2025-08-01 05:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README23.md)
