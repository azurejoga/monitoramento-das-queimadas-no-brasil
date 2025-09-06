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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f05af3c8-24ac-3559-b862-39030ac691e5 | -4.8901 | -41.75772 | 2025-09-06 03:47:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 812d5431-06ac-3f3b-8c20-dcbd6389da8c | -5.93543 | -43.02158 | 2025-09-06 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 78fcd949-81bf-35f8-90b6-1fbd0c71abfc | -6.03516 | -43.6974 | 2025-09-06 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91cfe0d4-f35d-3241-a9d0-d594536b5aed | -5.95714 | -43.02539 | 2025-09-06 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 77dacf05-b1d6-32b9-bf3e-d162dc0e3d92 | -5.84534 | -45.30757 | 2025-09-06 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7b047ab-8350-3c03-94d9-b5fd1e314688 | -2.78357 | -49.6232 | 2025-09-06 03:47:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 945abc89-f501-38eb-a890-defd3b1568f8 | -4.79393 | -47.26052 | 2025-09-06 03:47:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abcf2f71-1242-3306-8b2d-b0ff1faeca78 | -6.51705 | -43.06495 | 2025-09-06 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acc78104-c8d3-38c7-ba25-30e983943871 | -5.85043 | -45.30846 | 2025-09-06 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c91babad-daca-38ce-9942-f81cb19a46ce | -5.98868 | -44.72318 | 2025-09-06 03:47:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a8818cfe-1011-3810-b110-9006962bdc05 | -5.86761 | -46.04586 | 2025-09-06 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92591f19-ba02-3d51-9ac9-6d26ab0a3d76 | -5.94623 | -45.66478 | 2025-09-06 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 66452e20-d216-3e6d-81f9-767ec096df1d | -3.69195 | -49.54602 | 2025-09-06 03:47:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bded528-6c08-371d-b380-76ef1c0957fd | -3.16338 | -49.4813 | 2025-09-06 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c2e7c3d4-d6bb-3df0-8c34-b1fcc877431c | -6.3106 | -44.57576 | 2025-09-06 03:47:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b09cb4d2-ee41-39e8-973a-2d85af4ac571 | -3.36179 | -43.37375 | 2025-09-06 03:47:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3d8dd7d-babd-3fe8-a881-e4b195796e70 | -6.38859 | -43.01274 | 2025-09-06 03:47:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6109989d-066b-3954-92fc-aecafb147542 | -5.72609 | -43.90781 | 2025-09-06 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b965d7c3-9adf-3517-8f03-e892f15f903c | -5.82824 | -46.36043 | 2025-09-06 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2393ddaf-b67e-33c1-aaaf-64c239c31927 | -6.21211 | -43.57688 | 2025-09-06 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fa848c0e-9875-343d-b972-1ccad1ff8e5c | -5.21515 | -43.6965 | 2025-09-06 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9765052f-b202-3dc3-b4b9-db6ad05d2fe6 | -6.01618 | -43.69903 | 2025-09-06 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6471706f-b67e-334f-80f9-1daf774bd070 | -6.39208 | -43.81932 | 2025-09-06 03:47:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3fb33397-166a-3606-9fd4-2635685bb6b2 | -6.16852 | -44.30912 | 2025-09-06 03:47:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6ac6f948-aaf0-3ad6-b408-de4c07de1027 | -6.55429 | -42.95017 | 2025-09-06 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b97e037-125a-304a-af13-68c11aa7be46 | -3.16087 | -48.60789 | 2025-09-06 03:47:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dde48fcb-76c6-3fcf-91de-b6ded6641b44 | -5.86995 | -46.04551 | 2025-09-06 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b8597c4-1439-314c-9ce1-734ea08bc9a5 | -5.17989 | -43.05338 | 2025-09-06 03:47:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a408ade-e9df-3003-8884-dcedf16d35ec | -5.98493 | -43.60864 | 2025-09-06 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 48af296c-54ed-3320-8d80-4319253d8fde | -6.15477 | -43.17233 | 2025-09-06 03:47:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7b6197d2-2f87-3f4d-9ed4-79e36f5bdd9e | -5.20971 | -43.7006 | 2025-09-06 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 43c892a8-f7b8-32d7-889e-f1ac91385ae4 | -6.08204 | -43.30787 | 2025-09-06 03:47:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 03a71d3c-6ec3-3b3f-a096-7940092e5781 | -5.84651 | -44.11877 | 2025-09-06 03:47:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e7be26a-1163-3129-9965-5a1f44bc1efb | -3.69881 | -49.54729 | 2025-09-06 03:47:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96abbcf4-e86f-304f-ba44-3991ccb91cc3 | -6.32064 | -43.28722 | 2025-09-06 03:47:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e3e0228e-f17d-37af-bff4-fd8f57413154 | -3.35715 | -43.373 | 2025-09-06 03:47:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a58b26e4-43d8-39c7-a2b9-dbb8249116ae | -5.65797 | -43.61679 | 2025-09-06 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f226ee15-9011-3bc5-ac32-0df93b7b9a97 | -6.18643 | -43.35902 | 2025-09-06 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80f37e5f-d250-302f-9f43-4b8da92bb216 | -3.37958 | -47.61168 | 2025-09-06 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b5458b16-42b2-3db1-8c90-ac6545c5063c | -6.23984 | -43.28372 | 2025-09-06 03:47:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4b5afe5e-adf5-30fd-a0e6-7d9f69e83eb7 | -6.24271 | -43.29275 | 2025-09-06 03:47:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60a31014-7df4-383d-9043-052b79b864f3 | -3.1623 | -48.60642 | 2025-09-06 03:47:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e2d3301a-3071-3bf7-ae6d-49ddfa962321 | -5.88013 | -46.03743 | 2025-09-06 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 225ead4b-e955-350b-ba1d-0ad227482380 | -5.82887 | -46.35688 | 2025-09-06 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51723717-41d0-3f66-a39b-befe6c9d1da6 | -5.87297 | -46.0467 | 2025-09-06 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a06a6437-a147-3b54-9a7a-80caf03c479c | -4.61279 | -41.53885 | 2025-09-06 03:47:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 006ac5a9-fbcd-3ab7-b8c0-6348742572fb | -6.24788 | -43.28906 | 2025-09-06 03:47:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53ae51a1-0040-324c-93e5-9a275a23ac09 | -6.20443 | -43.41518 | 2025-09-06 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5285db72-daab-30f7-b572-e58ba1760625 | -6.19852 | -43.42323 | 2025-09-06 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1c80d83-d989-31d8-bfa7-d5aadce35514 | -6.51272 | -43.06428 | 2025-09-06 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5a41bd1-3327-3384-8964-f59fd2233155 | -6.55069 | -42.94541 | 2025-09-06 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f57fe38-d1f1-330a-afea-d27e7dd34cf5 | -4.49841 | -42.88349 | 2025-09-06 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| be8eebbe-f9a0-32ed-8973-b4a37cb351c5 | -5.20209 | -43.68972 | 2025-09-06 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| acdcfa4b-1de9-35b4-94e5-652c9d0c9322 | -3.7568 | -49.05841 | 2025-09-06 03:47:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bda7f208-1793-3f0b-933b-65879b980f07 | -4.45561 | -44.13897 | 2025-09-06 03:47:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ab65257f-27bb-35d7-8b81-7954b53beba5 | -4.82611 | -42.73729 | 2025-09-06 03:47:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95ac35ef-396a-33ac-b1d5-1e6d07221116 | -5.75202 | -43.70156 | 2025-09-06 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 452f2c60-ceb2-3ee2-b213-588d320753ca | -5.9623 | -44.74332 | 2025-09-06 03:47:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5da46fc1-aa71-3ed7-80ec-ab5b12c8cb63 | -6.51637 | -43.06889 | 2025-09-06 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea9f29d9-54bf-3f20-b4ff-3f3fe946fa6b | -6.20787 | -43.36702 | 2025-09-06 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6a05176-c113-3556-9c8c-c4b5c47bb4ee | -3.3175 | -48.71043 | 2025-09-06 03:47:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54871d66-8912-3956-968d-6c8e75a997b5 | -6.21688 | -43.36327 | 2025-09-06 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 667e5b6c-b234-368d-a151-46a8a5792233 | -6.19672 | -44.77255 | 2025-09-06 03:47:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d2a2b13d-fb8c-3217-a801-2dd42f5f4afc | -5.96079 | -43.03042 | 2025-09-06 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b432af86-5153-3027-bcfe-e97f4688cf48 | -6.20369 | -43.41962 | 2025-09-06 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83eb1da9-c438-3c96-b1fb-4ef7224f1ad6 | -6.19416 | -44.77064 | 2025-09-06 03:47:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3a00265d-ad77-3432-a066-50f39d61b81d | -3.69543 | -49.56661 | 2025-09-06 03:47:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62b75220-7e0e-3d46-b1f8-9602ec106ea2 | -5.72692 | -45.3679 | 2025-09-06 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5709a80f-b3ad-3371-9a1c-93976f90c962 | -6.38927 | -43.00866 | 2025-09-06 03:47:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bdf44cdd-ead2-34f1-ac9a-de8b26a7844d | -5.45006 | -42.80967 | 2025-09-06 03:47:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c813d637-72af-3f70-92a8-966d43815978 | -6.15984 | -44.24521 | 2025-09-06 03:47:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 610ddf86-90fe-3aee-a1a3-2a81120a5c36 | -5.39119 | -43.24634 | 2025-09-06 03:47:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c787d6e-3ee7-38c2-b197-fd1d2a9fb303 | -5.78098 | -40.93047 | 2025-09-06 03:47:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 12f5b28d-eeca-3c80-866e-ad6b479a4d73 | -6.38642 | -43.01149 | 2025-09-06 03:47:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8408ca42-a92d-315b-bcd9-3e9217852b42 | -6.19899 | -43.36563 | 2025-09-06 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 359608d8-49fe-3d0b-8fb3-2b6a71181d6d | -3.31847 | -48.7048 | 2025-09-06 03:47:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 342024e0-9d2d-32cf-a269-0288b1170f40 | -6.55789 | -42.95492 | 2025-09-06 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| db539d91-90a9-3a2b-8277-914d8bbe262f | -5.55804 | -46.53731 | 2025-09-06 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 389a6150-cadf-3f8d-9ed2-071d79ab3e49 | -5.95831 | -44.73721 | 2025-09-06 03:47:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2ff7e22b-184d-3107-b4db-e7faa1bfd092 | -4.79912 | -47.26542 | 2025-09-06 03:47:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8fe2556-3346-3e56-950b-bba27cb75cb0 | -2.47485 | -47.7785 | 2025-09-06 03:47:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a9bbe68-b579-3fe0-9e70-f4cf47c9fb49 | -3.22502 | -42.88432 | 2025-09-06 03:47:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89df123d-a6bf-32a8-b968-6c0cdf05c7e1 | -5.82007 | -43.8294 | 2025-09-06 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 138ca368-39b8-3d08-8fe4-f1fba15ad94f | -4.89881 | -41.75551 | 2025-09-06 03:47:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 47512272-d66d-302f-a7f0-96ad019fe03e | -6.01085 | -43.70286 | 2025-09-06 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 421013bb-7b82-31ef-9f86-cc39771a0347 | -5.93299 | -43.71619 | 2025-09-06 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6fc8926-6481-3f51-bb65-68ff14212aa5 | -5.82808 | -46.35644 | 2025-09-06 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51924905-a7cd-369d-adc2-660a9ca6d25f | -5.86258 | -46.105 | 2025-09-06 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 02d372e8-ccd1-3c38-92f6-3a9e8b4c400b | -6.51567 | -43.07297 | 2025-09-06 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96b5bda7-8155-3272-a591-d982fe6f77e9 | -5.21432 | -43.70138 | 2025-09-06 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d51b3a31-e3d9-3870-99a0-82d91d8f8788 | -5.98453 | -44.73075 | 2025-09-06 03:47:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9b980e76-01cb-3af8-948b-fb05368b74db | -5.83262 | -43.97418 | 2025-09-06 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3ce251a0-70ff-3263-a836-c2fbfffe386b | -5.65344 | -43.61589 | 2025-09-06 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 798d5ca1-8637-3b42-9dd9-0f5bd2fc7f00 | -5.9877 | -44.72872 | 2025-09-06 03:47:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1152eb65-3bf2-3979-a074-70bd900031ca | -6.23635 | -41.829 | 2025-09-06 03:47:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3c8fbbe6-4ed3-3bf1-a4f9-a5ba51871722 | -4.03425 | -42.52091 | 2025-09-06 03:47:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ac61c05c-9120-3a7e-937e-3ef346b8043e | -6.21821 | -43.3596 | 2025-09-06 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7548dc34-8898-33d0-9a4a-9287003a257c | -3.68745 | -49.57167 | 2025-09-06 03:47:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 928189cf-cdad-3a7d-8553-af8adbcfd402 | -5.86406 | -46.03493 | 2025-09-06 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a420ff8d-0ba6-3334-850c-2c21db9802b3 | -5.49764 | -42.15168 | 2025-09-06 03:47:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README21.md)
