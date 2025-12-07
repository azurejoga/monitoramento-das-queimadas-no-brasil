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
| db7c945f-4492-34e1-ba90-19c53ccc192d | -23.29306 | -47.09567 | 2025-12-07 04:18:00 | NOAA-20 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| cf9038d0-271d-3086-8552-c52ddce9c5f4 | -20.72428 | -47.3514 | 2025-12-07 04:18:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b7251a2-1c6c-3009-a058-c873325fa1c6 | -19.72641 | -49.27584 | 2025-12-07 04:18:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5ff9895b-7446-36f8-a5c5-9de0b27a9c9a | -20.64599 | -47.22628 | 2025-12-07 04:18:00 | NOAA-20 | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20d67450-5c6e-35ea-b882-15d1d68fbff9 | -22.02604 | -45.93946 | 2025-12-07 04:18:00 | NOAA-20 | ESPÍRITO SANTO DO DOURADO | MINAS GERAIS | Brasil | 3124401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ee51814a-97ef-3be2-9615-adeea942a1d0 | -19.43221 | -46.99931 | 2025-12-07 04:18:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 896ac568-7cb0-3df2-843c-f2799ec34681 | -19.43995 | -54.12993 | 2025-12-07 04:18:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1e4b4ed-82f2-305e-838c-aa6831e2c37b | -19.80644 | -44.99254 | 2025-12-07 04:18:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 82dbef64-b86e-36fd-98c5-24743f1f426e | -20.91547 | -56.37315 | 2025-12-07 04:18:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87bca5ab-7af7-30b2-88eb-55419cb9770d | -23.80172 | -47.82598 | 2025-12-07 04:21:00 | NOAA-20 | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7d473cdd-cb7b-33f0-8ff9-7d94d89aff47 | -26.10278 | -50.17284 | 2025-12-07 04:21:00 | NOAA-20 | MAFRA | SANTA CATARINA | Brasil | 4210100 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c2971c2f-8f0d-30e2-8a8d-79b7216e8d44 | -23.97887 | -48.94284 | 2025-12-07 04:21:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87817112-cce3-3dc3-a3d3-f7b798ec65f8 | -28.89915 | -51.04888 | 2025-12-07 04:21:00 | NOAA-20 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d8736b41-405a-3878-8f0b-808856ea515e | -24.12321 | -46.71143 | 2025-12-07 04:21:00 | NOAA-20 | MONGAGUÁ | SÃO PAULO | Brasil | 3531100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ad67df91-3318-3d55-81f2-a1ba946013bc | -23.80504 | -47.82661 | 2025-12-07 04:21:00 | NOAA-20 | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f813ec3d-0d61-3d6a-ad30-fbfa9d2a6221 | -26.10019 | -50.17335 | 2025-12-07 04:21:00 | NOAA-20 | MAFRA | SANTA CATARINA | Brasil | 4210100 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e58914d4-5d9a-3d6a-8708-ffbeb5e2859b | -26.20535 | -51.56283 | 2025-12-07 04:21:00 | NOAA-20 | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 6df98259-bc12-3bfe-867a-2f5e7936d4a8 | -26.20895 | -51.56364 | 2025-12-07 04:21:00 | NOAA-20 | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| f29f80d4-446e-3e40-8782-7bb7ec9508a2 | -26.10205 | -50.17698 | 2025-12-07 04:21:00 | NOAA-20 | MAFRA | SANTA CATARINA | Brasil | 4210100 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6aa017d4-912f-3c00-bb55-17787197768f | -29.08275 | -50.62541 | 2025-12-07 04:21:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| cb913a61-1b98-37f6-bbc9-e54818777945 | -24.81612 | -51.12532 | 2025-12-07 04:21:00 | NOAA-20 | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 882cb3d5-c592-3ed1-8eb6-31a4657464c6 | -29.48542 | -54.62564 | 2025-12-07 04:21:00 | NOAA-20 | JAGUARI | RIO GRANDE DO SUL | Brasil | 4311106 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 10e8f6ae-b504-304e-849a-14d9df5f24c0 | -23.81013 | -47.56411 | 2025-12-07 04:21:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2bb5cc69-5ee9-3c87-ae8a-d4a9f1c00dfd | -28.72829 | -49.44503 | 2025-12-07 04:21:00 | NOAA-20 | FORQUILHINHA | SANTA CATARINA | Brasil | 4205456 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dfc7a0bf-8aa6-379f-9f8f-c0d0fdb1a5ec | -29.08203 | -50.62958 | 2025-12-07 04:21:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 17a132fa-ce49-3e5c-a0de-8fa8c8c75e8b | -25.77488 | -50.74802 | 2025-12-07 04:21:00 | NOAA-20 | RIO AZUL | PARANÁ | Brasil | 4122008 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5ee5681e-7c6b-39c4-a2f6-181f30f59d0a | -25.77838 | -50.74878 | 2025-12-07 04:21:00 | NOAA-20 | RIO AZUL | PARANÁ | Brasil | 4122008 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ddda316f-e211-3bd0-9178-96e8aa42888b | -29.08705 | -52.26858 | 2025-12-07 04:21:00 | NOAA-20 | SÃO JOSÉ DO HERVAL | RIO GRANDE DO SUL | Brasil | 4318465 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 306b7924-7825-3952-97cc-734d7f7fca6e | -26.20452 | -51.56727 | 2025-12-07 04:21:00 | NOAA-20 | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1516055a-e109-32ef-8428-322e85674035 | -26.08048 | -51.58629 | 2025-12-07 04:21:00 | NOAA-20 | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f0a15567-60e3-3102-ab25-a64d3cbd637e | -30.52871 | -51.71271 | 2025-12-07 04:21:00 | NOAA-20 | CERRO GRANDE DO SUL | RIO GRANDE DO SUL | Brasil | 4305173 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| 5bd8465c-10ab-3d8c-92db-d8ba56f2ebd7 | -26.53376 | -50.18795 | 2025-12-07 04:21:00 | NOAA-20 | PAPANDUVA | SANTA CATARINA | Brasil | 4212205 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7e012295-a9a4-361a-9c2a-3e64053bafcc | -30.72763 | -52.36637 | 2025-12-07 04:23:00 | NOAA-20 | AMARAL FERRADOR | RIO GRANDE DO SUL | Brasil | 4300638 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 18c05a88-9c58-3067-a759-55ac960ae282 | -31.63447 | -52.36954 | 2025-12-07 04:23:00 | NOAA-20 | PELOTAS | RIO GRANDE DO SUL | Brasil | 4314407 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 28a49c2e-3a7e-3695-9e94-b860b6b998ad | -30.72493 | -52.36093 | 2025-12-07 04:23:00 | NOAA-20 | AMARAL FERRADOR | RIO GRANDE DO SUL | Brasil | 4300638 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| 6a71bbd7-72ab-3132-9177-b08bec5723d1 | 3.41545 | -51.25547 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8d11f5f-e307-3d9e-af4c-d09a970b7b5c | 2.34075 | -51.64859 | 2025-12-07 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 387bcec0-27e2-3e28-ab57-09d65c00f44d | 3.41033 | -51.25984 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2c0706f3-5a42-3710-b039-87660152434a | 3.41198 | -51.25602 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0b36d4b7-7347-3eec-91c6-e93be684cb5a | 3.404 | -51.26477 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9f8d1a32-ca3a-34ec-a534-76b5b0cfa8f8 | 2.00772 | -55.68337 | 2025-12-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74d47c47-5ca6-3c28-86cf-fcd0d0a05d4c | 2.00829 | -55.68703 | 2025-12-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cba789cd-a72d-3516-be99-620bc1bf273c | 2.19139 | -55.77915 | 2025-12-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3677e422-b999-3053-a937-573d9ad7820c | 2.67687 | -51.33657 | 2025-12-07 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe38100f-2f39-326b-a72f-9c2665967137 | 1.96753 | -55.69339 | 2025-12-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e95f101-59dd-315c-a0c5-be538b969e1f | 3.97828 | -51.67807 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18b414bf-0e2a-3d3d-8560-759bfa614ee4 | 3.44667 | -51.25052 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87a522cd-2ee5-305c-b31e-fc3edeb88fd9 | 3.4034 | -51.26094 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7de8c31-fdae-3d46-915b-9ef17d7b6f9c | 2.18057 | -55.77694 | 2025-12-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b14f7087-9a69-3f66-9afd-37f27f8af061 | 2.52878 | -50.84081 | 2025-12-07 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd4bb474-2955-3d36-816c-34abc73579aa | 2.52942 | -50.84488 | 2025-12-07 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2250ba53-8e24-36d3-b157-1b1b0426450e | 1.32805 | -50.95403 | 2025-12-07 05:01:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f61467cd-6e7e-3662-8172-b3a7a9826e11 | -1.14626 | -46.75747 | 2025-12-07 05:01:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8b2f7f86-792d-35c5-8e3b-7613278bcc57 | 2.00603 | -55.69482 | 2025-12-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b6e07358-ba80-33e6-be44-75b77ee24eb6 | 3.33441 | -51.31884 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e46fe96c-2ca0-3b33-a69d-06a8a7d6aa68 | 3.44381 | -51.25489 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ffaecc04-6546-31c6-ba50-d002015b5dd4 | 3.45586 | -51.24121 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6195ff8d-0077-369b-bb32-a60e184eac7b | 3.40053 | -51.26532 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a0a96880-a97a-3a9c-9a6f-61881f3898bb | 3.45872 | -51.23684 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd403c11-0ac9-3f8b-a29f-df7995311ef8 | 3.9845 | -51.67333 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82aae9df-ab91-39c8-b7c9-af613a3bdedf | 3.40113 | -51.26915 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7928de80-b10b-30d2-be70-81fdc1853550 | 3.40913 | -51.26039 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cd6a994a-9ec5-3c68-a657-8adb005b7f59 | 3.3338 | -51.31504 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 529328e6-651a-3a28-aa0b-da8c5946255d | 3.41892 | -51.25492 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e46a25f-59dc-3aa3-8bb9-84714d64fefc | 3.45239 | -51.24177 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d642d35e-4bd3-30fc-a061-f8cc1d498f6c | 0.45907 | -60.42783 | 2025-12-07 05:01:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f86d3d0f-4b3a-3047-bc83-8e5257d14bb3 | 3.44442 | -51.25871 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3065fbc-69dd-33eb-bf8e-aa5b90ac4b2a | 2.71768 | -60.74085 | 2025-12-07 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b86c1ef-c877-3820-920e-c42f35be95f9 | 1.97093 | -55.69286 | 2025-12-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45f2ff61-4e3d-3560-bc3a-4b0468486732 | 3.45525 | -51.23739 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4eb6a8e8-d029-3b3e-9d0d-8e4cf0979e8e | 3.44892 | -51.24232 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 373fba19-8070-3a6b-838f-3e4883d8546e | 3.44606 | -51.2467 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b13367d9-3a9f-3737-a5e9-58dc1401c5d1 | 3.9811 | -51.67387 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 867676f9-256f-3615-956b-d6169dffa468 | 3.40851 | -51.25657 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bf2bd852-b3f9-330c-bae5-03046b294603 | 3.4432 | -51.25107 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a29e75fa-b12a-3fa4-b34c-6240f9057256 | 3.40974 | -51.25602 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 60cae0d9-4013-3fe2-9329-e2530078c1dd | 2.00375 | -55.68024 | 2025-12-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6717d1f6-abac-3c4e-9c4d-40bb9d245e78 | -1.10988 | -53.65563 | 2025-12-07 05:01:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bebf97d2-5247-340c-b612-1d21a4884d1b | 3.40687 | -51.26039 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| de294145-d2cc-3dfb-a609-40cef7e0f678 | 2.52358 | -50.85412 | 2025-12-07 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed42bd20-877c-3c85-ac0f-c3ce4dcf5ba6 | 1.97432 | -55.69229 | 2025-12-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59c4f431-7818-3a64-9372-e2113c7cf167 | 1.33165 | -50.95345 | 2025-12-07 05:01:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0936cb99-c291-304c-8d8e-505de9a7c801 | 1.331 | -50.94934 | 2025-12-07 05:01:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 670b728f-11ce-3c8c-a7f3-55892e31b2c5 | 3.44953 | -51.24614 | 2025-12-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ef8704d0-0d1a-3b2f-9cfb-0958083dabe2 | 2.18114 | -55.78066 | 2025-12-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9eff804f-b622-3da6-9af0-9bac076ca86f | -1.17565 | -54.19141 | 2025-12-07 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5fd08fe-95df-38ca-8812-cbd8bcecc4c8 | -1.46892 | -55.09889 | 2025-12-07 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f32d753c-4d76-3445-8d63-813e96159118 | -2.11061 | -53.45583 | 2025-12-07 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3a151a7-f2e3-3765-9677-631074c2f638 | -3.95994 | -49.37767 | 2025-12-07 05:03:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c3d09c1-f45b-3f20-b86b-7fe51fcffb9f | -1.58914 | -53.80889 | 2025-12-07 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b6a8cdb-49e7-3e92-98f9-9571eb728736 | -2.38645 | -56.05508 | 2025-12-07 05:03:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1166054-6283-313c-a900-d6e9eb24dd0b | -3.23443 | -50.80542 | 2025-12-07 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23a88ceb-a6f1-3d5d-9e9f-f959b5b22d00 | -1.40932 | -55.06499 | 2025-12-07 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| a1743f0d-3912-3724-98c0-52d8e6c94319 | -1.71542 | -53.5222 | 2025-12-07 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 289d20c2-f443-33d7-a046-feefa75eedf1 | -2.88081 | -52.19459 | 2025-12-07 05:03:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6172a106-d060-3cb3-b9f7-8880f7c87545 | -1.35059 | -54.61584 | 2025-12-07 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f8cbfb5-d79c-3ba3-857b-7e106843ec74 | -4.32332 | -49.35032 | 2025-12-07 05:03:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e38cac3e-29cc-3feb-bfbf-a38ac14860f7 | -1.72267 | -53.51969 | 2025-12-07 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2705b414-fa08-307b-bb9a-89c45049de56 | -2.14587 | -52.80489 | 2025-12-07 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed1081fa-e285-3641-9088-f8560f756060 | -2.44233 | -53.83322 | 2025-12-07 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README4.md)
