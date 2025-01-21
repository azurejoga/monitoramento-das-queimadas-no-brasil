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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3f173b0-a019-3d76-8da5-38cf5c3c9819 | -6.79152 | -35.16624 | 2025-01-21 03:23:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 462511f6-879a-327d-bfe8-a7f85e99fe05 | -7.5201 | -35.16869 | 2025-01-21 03:23:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 62e9ed77-2143-33a1-a90e-207cb3c2042d | -7.38027 | -35.91867 | 2025-01-21 03:23:00 | NOAA-21 | QUEIMADAS | PARAÍBA | Brasil | 2512507 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f9242a7f-20de-3a08-b88e-05421f561eea | -8.06789 | -34.97619 | 2025-01-21 03:23:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 758fe4b5-3c1b-3165-85dd-0880ab7c61f6 | -8.93833 | -44.245 | 2025-01-21 03:23:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 661a397d-20bb-3ab8-9be1-4254078e6f54 | -7.8451 | -35.19984 | 2025-01-21 03:23:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 2d6fe8b5-0764-38d2-bf5a-b11cd9b68134 | -7.84607 | -35.20228 | 2025-01-21 03:23:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| e08666a5-19ae-3e91-a835-93c1282a693e | -8.63545 | -35.41858 | 2025-01-21 03:23:00 | NOAA-21 | GAMELEIRA | PERNAMBUCO | Brasil | 2605905 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| cbbd55e5-8cfd-3677-8508-5844bcbc48e5 | -8.21463 | -35.04895 | 2025-01-21 03:23:00 | NOAA-21 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8db0410d-449e-3d79-8c0a-234740c6ece6 | -9.12039 | -35.48789 | 2025-01-21 03:23:00 | NOAA-21 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| b47ce7bc-3605-36d5-bdd2-6a5b4916d5f2 | -7.84689 | -35.19745 | 2025-01-21 03:23:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 09fe45c3-2354-3594-948f-58b865c69a11 | -6.15701 | -39.44048 | 2025-01-21 03:23:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e8bb9d3b-9a3a-3142-8065-194a2f43bc1d | -8.49872 | -35.65778 | 2025-01-21 03:23:00 | NOAA-21 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| 1c9dffe2-a472-30e8-983e-3930b184115c | -8.50096 | -35.66865 | 2025-01-21 03:23:00 | NOAA-21 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a6332cbb-c2e1-3629-b6f1-a9415934aab6 | -8.50261 | -35.6588 | 2025-01-21 03:23:00 | NOAA-21 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| b33345f7-1c00-363b-93a9-c5e74dc36db8 | -6.16228 | -39.44153 | 2025-01-21 03:23:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4bef2bea-bf55-3242-b6f3-300d994c8dc6 | -8.50179 | -35.66371 | 2025-01-21 03:23:00 | NOAA-21 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 25c5844c-67f1-3a75-a990-8366e3c8a513 | -7.95132 | -35.24004 | 2025-01-21 03:23:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3a635528-2d27-323f-a987-0ba4f484e0f7 | -6.79067 | -35.17133 | 2025-01-21 03:23:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 974463c9-a127-3eda-b31d-d21a1c6512d5 | -17.16913 | -45.46534 | 2025-01-21 03:25:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eff88881-8353-394d-bd09-e97279a444d2 | -16.6838 | -43.88339 | 2025-01-21 03:25:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebd66f90-11a5-3c3b-b02a-6eb85c0db8eb | -11.02899 | -45.05164 | 2025-01-21 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3dab1c7e-65a6-30bb-abeb-1829c2474589 | -18.71232 | -40.00126 | 2025-01-21 03:25:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3518336b-d187-3862-9180-0d6ace19e290 | -15.43631 | -39.12787 | 2025-01-21 03:25:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8fee94d0-5b9e-3e2d-8291-d2439155d99c | -19.2072 | -45.38034 | 2025-01-21 03:27:00 | NOAA-21 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38664673-9d3b-318d-892b-00e2c3d9625e | -22.94573 | -43.7084 | 2025-01-21 03:27:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 45271807-b9dc-3546-b549-fd3f4285b153 | -20.41927 | -43.55571 | 2025-01-21 03:27:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b3e08057-4a4e-39dd-b1a2-606b3345fcff | -22.94646 | -43.70512 | 2025-01-21 03:27:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| bfa60c47-9c20-3325-adcd-267802527dfa | -22.94569 | -42.93475 | 2025-01-21 03:27:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| c8379518-fc79-3eda-8b78-347949e5a446 | -22.73684 | -43.637 | 2025-01-21 03:27:00 | NOAA-21 | QUEIMADOS | RIO DE JANEIRO | Brasil | 3304144 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| fbd41563-c3b5-3624-8202-2a6333ea316f | -1.78637 | -48.43813 | 2025-01-21 04:10:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8bae7809-2fd6-3eba-9c5a-73761d49811b | -2.56705 | -48.06495 | 2025-01-21 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f063b95f-afbc-3c2e-b439-d7dbf5e8b18a | -2.12215 | -48.75873 | 2025-01-21 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e26d2eb2-e174-3874-a91d-67cfe50ae72b | -2.4256 | -48.05516 | 2025-01-21 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a675f80e-b535-32cd-9f53-5b420e9753f0 | -2.65681 | -48.79486 | 2025-01-21 04:10:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c78dc9fe-f420-3524-9456-9df380b88bfb | -2.56768 | -48.06101 | 2025-01-21 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98a240a7-a26b-3271-b0fa-9434d540f9d5 | -2.39764 | -46.86676 | 2025-01-21 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d503c246-ab6b-349b-9afc-efed73fd9b13 | -2.66127 | -48.79559 | 2025-01-21 04:10:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a352c619-fae3-3c9e-b07a-485400a63864 | -2.12143 | -48.76317 | 2025-01-21 04:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e32ecad-ace5-3b42-bf3f-f06b8bae4486 | -8.63626 | -35.41713 | 2025-01-21 04:12:00 | NOAA-20 | GAMELEIRA | PERNAMBUCO | Brasil | 2605905 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8c82a46c-dd42-387c-9a5c-21fea4c15bb7 | -8.07022 | -34.97523 | 2025-01-21 04:12:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 35a211c8-5c07-3830-9e39-643f448057ae | -6.36706 | -39.39472 | 2025-01-21 04:12:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7aa285f4-dfa1-3bd5-90d8-88957aa584c6 | -4.55082 | -50.18581 | 2025-01-21 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a935754f-101a-35ca-a3eb-6609573611b9 | -8.94113 | -44.24715 | 2025-01-21 04:12:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc5565cd-8df8-35ef-9fc4-c2aa68257a13 | -8.06979 | -34.97829 | 2025-01-21 04:12:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 78006158-bbf4-3360-9340-3e94b56be9aa | -8.93837 | -44.24312 | 2025-01-21 04:12:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c063c7b4-3a14-3acd-acf3-bb4c2a00d697 | -9.13233 | -35.88863 | 2025-01-21 04:12:00 | NOAA-20 | UNIÃO DOS PALMARES | ALAGOAS | Brasil | 2709301 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 444cacea-3b48-38c4-a49a-934c776c492a | -8.06767 | -34.97635 | 2025-01-21 04:12:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 209dc4be-4a2f-31ef-8a4a-12110f0d882b | -3.36937 | -52.71909 | 2025-01-21 04:12:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4240905a-b07b-3325-b0fe-79e7655a47df | -10.61392 | -37.01529 | 2025-01-21 04:12:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2f9605da-9070-3536-abc2-9e83f66303b8 | -6.80006 | -35.18392 | 2025-01-21 04:12:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 7d7dea79-19fd-3680-84bf-6dedad6afe93 | -8.5004 | -35.66029 | 2025-01-21 04:12:00 | NOAA-20 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 03e4bf24-3bea-3931-80e6-637e9289d157 | -4.546 | -50.18543 | 2025-01-21 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef1dfe10-738c-3f1e-82cd-c90868afb00f | -3.94641 | -49.44876 | 2025-01-21 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fac2818-76a8-3231-8955-d3d9e5fa5cf1 | -8.93505 | -44.24259 | 2025-01-21 04:12:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de395090-acd6-310e-b9a2-1172e32fd0f3 | -17.16702 | -45.46809 | 2025-01-21 04:14:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56976688-167b-34fb-a04a-ffc50b7c5b99 | -14.13487 | -41.69273 | 2025-01-21 04:14:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 28c79ec1-9876-315a-a133-485b84432d49 | -11.29284 | -40.96497 | 2025-01-21 04:14:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5bda5043-859d-3e23-beac-849ed52b75b4 | -15.3669 | -39.21017 | 2025-01-21 04:14:00 | NOAA-20 | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a73f6a69-e9bf-3be2-986b-c28ab428d512 | -17.16758 | -45.46449 | 2025-01-21 04:14:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f6d5fbf9-bde9-3842-b5e6-7bae956dd652 | -12.95194 | -41.17994 | 2025-01-21 04:14:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c915c54c-2603-336f-96b7-b224c5e0e8ee | -16.67969 | -43.88464 | 2025-01-21 04:14:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94bf42a3-74cb-3af5-94d4-9739e4876a48 | -12.35474 | -44.33099 | 2025-01-21 04:14:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c9741809-11fd-3a90-b6b5-6b1b6819156b | -15.43429 | -39.12677 | 2025-01-21 04:14:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dfaf8a8f-2ae4-30f1-a441-495e189902c2 | -13.47197 | -44.02037 | 2025-01-21 04:14:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 489bd7dc-3797-3067-9899-1f3136ca5db4 | -11.28341 | -44.44915 | 2025-01-21 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| afc45e63-fe73-3f52-a68b-a18d8b3f89db | -17.78147 | -42.80802 | 2025-01-21 04:14:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70f9d7c8-7c44-3f0e-a317-38ce2b0411dc | -11.2327 | -40.3754 | 2025-01-21 04:14:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 89db3d0e-6d62-3d6a-b7e1-9758781796af | -13.47474 | -44.02449 | 2025-01-21 04:14:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 671cb6ed-7376-3da7-848f-5427f9900147 | -17.16427 | -45.46392 | 2025-01-21 04:14:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c99fb81f-f8a4-377f-8f88-933a798569bd | -17.09373 | -43.80448 | 2025-01-21 04:14:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f7c033d-a338-3ba4-ba49-736431c99f68 | -13.22384 | -43.98085 | 2025-01-21 04:14:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 375ea6a6-e749-3c3b-aa89-5b05b360cfb2 | -13.47529 | -44.02092 | 2025-01-21 04:14:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03d7c195-20b7-3c70-9d75-3838662b8703 | -15.0776 | -48.94523 | 2025-01-21 04:14:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3544b9ee-0136-36c4-b9eb-581e1a7fc452 | -20.18857 | -50.3809 | 2025-01-21 04:16:00 | NOAA-20 | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 73da227d-4a05-3df8-90ff-10ac38e14288 | -19.04017 | -52.86105 | 2025-01-21 04:16:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80cb9434-1b68-3878-9807-e26d32b84001 | -23.40453 | -46.55747 | 2025-01-21 04:16:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 622edbd3-1ba0-3e7e-adcd-a3cd8b96d9d1 | -22.94304 | -43.70802 | 2025-01-21 04:16:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 15167c2a-68d5-3dd4-a506-d02b7c47019a | -22.94411 | -42.93498 | 2025-01-21 04:16:00 | NOAA-20 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a165873f-a310-313b-8a3c-cc47c8cb822c | -23.5327 | -47.39135 | 2025-01-21 04:16:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 042f388b-5b8c-3580-97fd-8220ca55e440 | -22.94666 | -43.7086 | 2025-01-21 04:16:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 39554c57-edc0-3caa-a774-5d123f915531 | -18.9958 | -51.37201 | 2025-01-21 04:16:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 00bfc720-9b03-362e-8ff5-4bf7687755b9 | -18.87188 | -51.35895 | 2025-01-21 04:16:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3cacfc09-32c2-3c12-a6a2-097cf4c98da3 | -18.87247 | -51.35851 | 2025-01-21 04:16:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a585547c-649b-3870-b8a8-1e351dc4146b | -21.6276 | -43.46698 | 2025-01-21 04:16:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f5a5ae15-202f-3e95-986e-cb0777d03b0c | -17.87201 | -45.67125 | 2025-01-21 04:16:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d20e79e-c33b-3c6d-9c08-9c4f8acfe37a | -22.67681 | -42.85748 | 2025-01-21 04:16:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 10c8cb36-8c5c-3037-b265-6e13f82b29f0 | -21.6041 | -48.45513 | 2025-01-21 04:16:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cda18666-ee54-3143-b1dd-2d74f12e84a4 | -22.92118 | -45.41442 | 2025-01-21 04:16:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 51440ea0-d5ca-38de-a20b-e584de02a384 | -20.31099 | -45.58506 | 2025-01-21 04:16:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0b4cf49-6cb3-3129-9051-1a4b2cef623e | -20.90118 | -43.81934 | 2025-01-21 04:16:00 | NOAA-20 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fefd71d2-901c-3040-a79e-c419ef43fb26 | -24.18629 | -48.53736 | 2025-01-21 04:16:00 | NOAA-20 | GUAPIARA | SÃO PAULO | Brasil | 3517604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 83f416e7-9e27-3009-8285-b5b91eb8fb8a | -23.33769 | -46.77444 | 2025-01-21 04:16:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 53140b3a-7dff-3c01-80ca-63dda93cc2b2 | -21.60345 | -48.45903 | 2025-01-21 04:16:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7b80925-eca1-399e-8eea-0fec2e898bdf | -20.41589 | -43.55305 | 2025-01-21 04:16:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 0230543e-7b84-3e15-93fd-3de2858aa529 | -20.19143 | -50.38646 | 2025-01-21 04:16:00 | NOAA-20 | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5567d38c-1010-303d-a8bd-0b1eba9a277c | -23.04307 | -47.86023 | 2025-01-21 04:16:00 | NOAA-20 | LARANJAL PAULISTA | SÃO PAULO | Brasil | 3526407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c2f4fa03-520e-37c0-b700-0db65f9315fe | -22.67745 | -42.85262 | 2025-01-21 04:16:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| fa76e5db-c512-3796-a360-d6baed4bd1e1 | -17.00657 | -49.78163 | 2025-01-21 04:16:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd8797b8-2895-334b-be7f-36d229060d00 | -21.35031 | -49.11554 | 2025-01-21 04:16:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |


[Clique aqui para ver as próximas entradas](README3.md)
