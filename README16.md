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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 218eb7d8-10f8-338f-a087-f0011f9038d3 | -3.6013 | -51.0259 | 2025-10-05 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 52d024d2-af51-344d-93af-f355ed8ca326 | -12.9844 | -51.0433 | 2025-10-05 01:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| fde17e06-02dc-3c36-bb17-c1afc85e4ecc | -6.1726 | -44.6432 | 2025-10-05 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 986391b8-f5be-3c7e-93ab-bfa02969a967 | -5.6548 | -43.9244 | 2025-10-05 01:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 3f0b91a6-08fd-3cd8-8297-8577a84c467f | -13.1589 | -50.9144 | 2025-10-05 01:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 431d853a-220c-3d27-909e-0abcadf1523d | -4.6504 | -43.2038 | 2025-10-05 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 1800497d-b375-3d97-be6e-cb26dde95bbb | -4.6505 | -43.1805 | 2025-10-05 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 99acf06c-03eb-3529-8a04-1020114ae87e | -11.823 | -45.0596 | 2025-10-05 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 1bf6a638-541e-35b7-bc28-ed89e7acba64 | -3.6196 | -51.0461 | 2025-10-05 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 312bbc8b-f913-335a-985d-a893be8ce15a | -17.9006 | -57.6388 | 2025-10-05 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.2 |
| 2f99da4a-7289-3151-9b83-af03adc1e2b0 | -4.4445 | -43.2397 | 2025-10-05 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 51245e18-ce3c-3ef0-9429-724aed571ce0 | -6.1536 | -44.6675 | 2025-10-05 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 420.8 |
| e167582f-79d5-3f6c-af34-3f4fd60ac278 | -8.5956 | -46.2798 | 2025-10-05 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| c810046e-ffdf-3257-b042-76b71834c24b | -5.6363 | -43.9027 | 2025-10-05 01:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 7abcb2dc-afab-328c-9066-99b7e2ac561c | -5.9879 | -44.3598 | 2025-10-05 01:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 3e13f9fc-e08e-3865-9ffe-6512ae7c59cf | -15.9084 | -48.8254 | 2025-10-05 01:40:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 0c968ddd-29c2-3898-9582-ae039ce639e2 | -13.4345 | -47.2774 | 2025-10-05 01:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 72.0 |
| a171816c-ce23-35d8-93f1-8509a679f54c | -4.3197 | -48.0908 | 2025-10-05 01:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| d343fb28-e8f9-3a63-b9bf-7a68f1ee0377 | -13.1161 | -43.847 | 2025-10-05 01:40:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| c11fa914-0f00-3bab-a1a2-21589ff205b4 | -14.3353 | -47.6755 | 2025-10-05 01:40:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 86.0 |
| fe715858-0549-31c5-bb4c-ce3ce49da960 | -5.655 | -43.9013 | 2025-10-05 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 9d83d1bc-5403-3782-a5c2-b80c42619dac | -14.3348 | -47.6981 | 2025-10-05 01:40:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 58.5 |
| ca362cf5-04e1-34a3-9e11-b37892c2b4e7 | -13.3517 | -47.5818 | 2025-10-05 01:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 00dc3951-f646-3550-aa87-4aaba70e1543 | -6.1351 | -44.6461 | 2025-10-05 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| e69a9113-8d56-31b0-80c5-890a16d6a2e9 | -11.8418 | -45.0799 | 2025-10-05 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 170.8 |
| 73f9e34e-c3e5-383d-8415-47747745d817 | -4.6318 | -43.1816 | 2025-10-05 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 8fe5ca27-a160-38ab-939c-59d45026219b | -11.8221 | -45.1059 | 2025-10-05 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| f0d0bdc5-3d40-324c-810a-685b7b0ec031 | -6.4134 | -43.0489 | 2025-10-05 01:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| b0b5c5a8-3c1b-3c25-94e8-d450d1288d7b | -3.6012 | -51.0467 | 2025-10-05 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| dec26c9e-a638-3a70-9f58-f547d405c9e1 | -6.1723 | -44.666 | 2025-10-05 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 250.4 |
| 507688e9-57e8-3b1b-9c4b-7c92f34d182b | -6.4131 | -43.0724 | 2025-10-05 01:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| c57a52bc-306a-321a-93de-3ee0ee9ad30e | -11.8225 | -45.0827 | 2025-10-05 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 172.0 |
| 084d27a8-422a-312a-8e2e-e3cb9ceb0912 | -6.1349 | -44.6689 | 2025-10-05 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| f2781767-5cb5-3338-b23b-86a9baf1ae79 | -15.928 | -48.822 | 2025-10-05 01:40:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| a56942fd-5504-3d81-87ad-3ccb96319f05 | -13.1585 | -50.9359 | 2025-10-05 01:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 3cfeef5c-8def-318f-afda-1e84492a2103 | -13.1397 | -50.9169 | 2025-10-05 01:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 26d3c175-fbe1-39f2-89c9-7db6081ee366 | -10.4051 | -45.416 | 2025-10-05 01:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 5e0b9125-3ee3-3a49-a1d8-8490c4ae419c | -18.3345 | -45.8734 | 2025-10-05 01:50:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 1f72b6a4-1032-3fe2-97f8-9baddb22016d | -11.8777 | -56.8769 | 2025-10-05 01:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 4f437403-8046-392a-b6c5-b10d9f2d83e7 | -13.0955 | -47.9099 | 2025-10-05 01:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 34a13d9c-39e4-339e-97ac-f5f5dd48a29e | -17.8808 | -57.6412 | 2025-10-05 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.6 |
| 004c38cd-f62f-35fe-a9f8-ddba0857acfd | -4.6505 | -43.1805 | 2025-10-05 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 178.8 |
| 1544d1bb-a5b7-335e-84aa-8449a20a8ab9 | -15.928 | -48.822 | 2025-10-05 01:50:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 88789170-2d90-3394-bef8-f8af9ac2a06c | -11.823 | -45.0596 | 2025-10-05 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 7bb42da2-7ab2-3847-a0bd-fd9c1dede066 | -13.1161 | -43.847 | 2025-10-05 01:50:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| f12a7ead-5cec-37f1-affb-9b6c127f00e2 | -18.3338 | -45.8971 | 2025-10-05 01:50:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 4ba572ff-0453-3ba1-8aa8-73a33c5a0253 | -11.8588 | -56.8785 | 2025-10-05 01:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| da5ba14a-81fa-3f47-a06b-e1ac6dc92fde | -10.4054 | -45.3931 | 2025-10-05 01:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| ee92675d-68f4-3e5e-87b3-8439a4ec006a | -13.1355 | -43.8436 | 2025-10-05 01:50:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 000f50ef-e41d-311b-b4a7-537109ed95e9 | -3.6012 | -51.0467 | 2025-10-05 01:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| eb6fa376-7d8c-390d-87bc-500312a5203d | -17.9006 | -57.6388 | 2025-10-05 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.3 |
| 5fb1bf2a-c8d1-3c5e-97fd-b26fa7c68a03 | -6.4134 | -43.0489 | 2025-10-05 01:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 130.8 |
| e4767637-9225-3a6d-9672-e060464be284 | -11.8225 | -45.0827 | 2025-10-05 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| c94a3b55-9aa0-3dbc-9de1-902fd7df0197 | -6.4131 | -43.0724 | 2025-10-05 01:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 26a6a096-0a92-341a-a217-b2c83fdd3779 | -13.1585 | -50.9359 | 2025-10-05 01:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| cb2d28d1-a10a-34c3-a47a-430a7f538a99 | -13.1589 | -50.9144 | 2025-10-05 01:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 9eadb36a-6416-3831-998a-1f62baf2b2bb | -8.4196 | -46.8108 | 2025-10-05 01:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 346b0ef8-8e93-374b-8c31-4b264a1fc015 | -3.6197 | -51.0253 | 2025-10-05 01:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 68e35ff2-15e4-3435-bba0-29582447fffc | -13.14 | -50.8954 | 2025-10-05 01:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| dbf9cbda-09d6-33eb-bea3-4f9d577d3032 | -14.3353 | -47.6755 | 2025-10-05 01:50:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 2344b03f-9845-3170-86d9-bd20a8515a12 | -5.6363 | -43.9027 | 2025-10-05 01:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 88a0c650-742d-351c-8194-78ec61c295db | -15.9084 | -48.8254 | 2025-10-05 01:50:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 6226e344-2b38-3110-9c1e-c0f3f74e29ef | -4.4445 | -43.2397 | 2025-10-05 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 3a64ff2b-91b6-3184-83ff-14012a4cd770 | -5.6548 | -43.9244 | 2025-10-05 01:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 6dd425c7-96ab-3f7c-aebb-7b720f16c6e1 | -4.6504 | -43.2038 | 2025-10-05 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 8fe20639-a09c-38be-bda4-4b4aa0b3e131 | -3.6196 | -51.0461 | 2025-10-05 01:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| e94a98ad-5016-3eee-bace-6c9865e6362b | -4.6318 | -43.1816 | 2025-10-05 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 123.5 |
| bddee2f6-8e8b-36e8-80b8-7533028ee1fa | -5.6361 | -43.9258 | 2025-10-05 01:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 48dd5b66-98f7-3681-aa80-655350867b54 | -5.655 | -43.9013 | 2025-10-05 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 1e5bf135-acc1-3b72-9a62-89bf90398b5a | -11.8418 | -45.0799 | 2025-10-05 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 0cf3ffe8-433b-3b9f-8ce1-8d3f92c22951 | -13.1355 | -43.8436 | 2025-10-05 02:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 2a577724-9ff1-3e83-a8b3-0747f7762330 | -5.6363 | -43.9027 | 2025-10-05 02:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 408f35f8-843a-379c-99cf-100fe556f5bc | -18.3345 | -45.8734 | 2025-10-05 02:00:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 1ec824c5-8f9d-3314-915c-1350f014f26e | -3.6196 | -51.0461 | 2025-10-05 02:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 6aa71e29-5c81-3d03-b6a5-c81217b9ec6f | -11.823 | -45.0596 | 2025-10-05 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| fac2f7f5-bb6e-31dd-9094-58b1327e8d97 | -17.8808 | -57.6412 | 2025-10-05 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.0 |
| fe671e27-e26f-38aa-9559-1732d0ce38b3 | -13.1161 | -43.847 | 2025-10-05 02:00:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 066e79aa-e324-3605-b110-877b1e873316 | -18.3338 | -45.8971 | 2025-10-05 02:00:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 69.3 |
| a652050c-2b97-3a04-8acd-e882c3d91b9a | -8.5956 | -46.2798 | 2025-10-05 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 59ca7352-9b2c-3c46-9427-4c3002786a36 | -3.6197 | -51.0253 | 2025-10-05 02:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 76006dd4-a5c7-3746-aac2-fa5093bc830b | -6.1726 | -44.6432 | 2025-10-05 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| ffa64f9f-921a-32c9-b3b0-1f9a095e8263 | -6.1723 | -44.666 | 2025-10-05 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 2ada31b6-3ee7-3ca7-9081-a8d25538e227 | -6.1534 | -44.6903 | 2025-10-05 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 5902e773-dfcd-3572-8f20-c776203bdd53 | -10.6382 | -46.317 | 2025-10-05 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| da364f68-9d36-33ab-9ccc-3728377de7e1 | -5.6361 | -43.9258 | 2025-10-05 02:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 59b6c475-e2f4-3ce3-9972-d1a8fb808e03 | -11.8588 | -56.8785 | 2025-10-05 02:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 7444b743-fa82-322a-b9f7-ec49b1d0aead | -14.3353 | -47.6755 | 2025-10-05 02:00:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 2a6ea18d-f609-3cf7-81c9-028b6e8670d3 | -3.6012 | -51.0467 | 2025-10-05 02:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 98a23a6b-da5e-3fa9-aac2-cf3a5b51dd0d | -6.1538 | -44.6446 | 2025-10-05 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 237.3 |
| c6741397-9175-3c5a-973a-661000bd6186 | -17.9006 | -57.6388 | 2025-10-05 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.6 |
| 921cf926-47c9-3c6f-b1f9-fc790346ee63 | -8.6144 | -46.2778 | 2025-10-05 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 2fdf17cf-6211-347c-a16d-7c3a503999dd | -4.4445 | -43.2397 | 2025-10-05 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 19fcb78b-6228-3a9e-b4fc-d19f7b419570 | -5.4775 | -42.7956 | 2025-10-05 02:00:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 60.4 |
| d435fecd-2ed4-39e6-8784-f0b1476015ec | -5.655 | -43.9013 | 2025-10-05 02:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| bb14ddad-1f51-327a-a21f-725dcd93eba3 | -4.6504 | -43.2038 | 2025-10-05 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 746c3618-bec6-3d94-9364-723af5f34bec | -8.5581 | -46.2611 | 2025-10-05 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| b7486bdc-0db0-3a26-8cbd-49e09d405921 | -6.4134 | -43.0489 | 2025-10-05 02:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| c20630e5-0254-353b-91af-8dd29e9e722f | -11.8777 | -56.8769 | 2025-10-05 02:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 3cd6ce40-cf8e-3ea1-adda-a90169d93f6a | -6.1349 | -44.6689 | 2025-10-05 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 6cbb1cd4-fa49-3201-964c-bd1d86975983 | -5.6548 | -43.9244 | 2025-10-05 02:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |


[Clique aqui para ver as próximas entradas](README17.md)
