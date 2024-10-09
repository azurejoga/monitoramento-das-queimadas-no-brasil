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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5904900-1cab-373f-83c6-8a94e1c14a6d | -20.3352 | -48.7076 | 2024-10-09 04:26:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 272.6 |
| 56685a14-2ed4-39a9-bd6d-ba82a360995e | -20.3551 | -48.7262 | 2024-10-09 04:26:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 272.4 |
| dd9a57d4-e179-373f-ad3d-5559426147d6 | -20.3557 | -48.7031 | 2024-10-09 04:26:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 223.7 |
| 956c6412-a392-3613-a187-077632b9dc84 | -20.6396 | -45.9158 | 2024-10-09 04:27:00 | GOES-16 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 3d818ecd-9b50-3ce7-82b6-b10ef2348060 | -20.6403 | -45.8916 | 2024-10-09 04:27:00 | GOES-16 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 946d8fa2-cd95-360d-b993-57548e1d6feb | -20.6609 | -45.8864 | 2024-10-09 04:27:00 | GOES-16 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 93.8 |
| dd519339-f0e5-34ea-affc-582d18b9446b | -21.5727 | -46.9659 | 2024-10-09 04:27:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 76.2 |
| cd023896-2f7f-3004-aa4e-937741092011 | -4.6577 | -44.36685 | 2024-10-09 04:32:00 | AQUA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 97741cbb-4d54-36bd-adcb-607d7437a21e | -4.65481 | -44.36154 | 2024-10-09 04:32:00 | AQUA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 39.4 |
| f245fe51-7eaa-338a-b681-db9eee3ceb19 | -5.59016 | -43.25496 | 2024-10-09 04:34:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 57c0c249-5fb6-31e5-a763-50c2b19851c0 | -15.62417 | -42.35437 | 2024-10-09 04:34:00 | AQUA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 18.5 |
| fee8dca2-1eef-397f-94b5-8afcec012339 | -15.62089 | -42.37248 | 2024-10-09 04:34:00 | AQUA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 955a8ca5-956d-318d-9187-fc8cd45de0b5 | -15.61569 | -42.36609 | 2024-10-09 04:34:00 | AQUA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 29.9 |
| affbec1b-781a-3449-948e-526c9a2ffe50 | -14.07385 | -44.46301 | 2024-10-09 04:34:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 361e9583-5f15-3226-8e32-8ff9b9e65ba8 | -14.07269 | -44.47035 | 2024-10-09 04:34:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 9a6d3c35-4344-3463-a1da-9ffa46ae0f86 | -13.95002 | -44.54832 | 2024-10-09 04:34:00 | AQUA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 30fb6719-72c1-30f1-82ef-abd63a370357 | -13.92679 | -44.51944 | 2024-10-09 04:34:00 | AQUA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 54807b1f-5125-3134-a91b-61c9ada26587 | -13.92572 | -44.51444 | 2024-10-09 04:34:00 | AQUA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 1457c528-2fa7-36db-82a2-313f1084c7ec | -13.89978 | -44.65561 | 2024-10-09 04:34:00 | AQUA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 6a5eae1f-3ae7-358f-aa7f-6fb4eb2d453f | -13.88493 | -44.65263 | 2024-10-09 04:34:00 | AQUA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 266.0 |
| 757bc066-c801-33e9-aeac-08ab776ef218 | -13.87845 | -44.52615 | 2024-10-09 04:34:00 | AQUA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| fd2c1ff5-f1c4-39ba-9299-8afc095c4f21 | -13.87643 | -44.53362 | 2024-10-09 04:34:00 | AQUA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 80804c8b-613f-3ea9-9edf-d70f12533bd9 | -5.59864 | -44.85265 | 2024-10-09 04:34:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 1a93581b-974d-3e93-b801-903524fc5e83 | -5.59734 | -44.8479 | 2024-10-09 04:34:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 76489c0d-bc1e-37a2-a81b-e10750220b52 | -1.11 | -53.6173 | 2024-10-09 04:35:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 93ff9ba0-7a92-3469-9365-2d12ff035f80 | -3.9023 | -46.4467 | 2024-10-09 04:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 6b3373cb-c1e9-34db-8fb0-579a4df3363f | -3.9394 | -46.445 | 2024-10-09 04:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 9887c66d-a26a-3f8b-a2a0-141892b41c5c | -6.7614 | -60.0559 | 2024-10-09 04:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 128.3 |
| b4aee9ef-702c-3d42-b701-02f64337b62d | -6.7615 | -60.0367 | 2024-10-09 04:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 7bb73ea1-8c73-3c36-ba9c-4b7c64d9c2ce | -6.7798 | -60.0552 | 2024-10-09 04:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 70ff2dc9-0f2f-3d9e-bb52-1e56f90881ac | -6.7799 | -60.036 | 2024-10-09 04:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| a2522e96-eb83-3712-a978-5e692898430d | -22.81339 | -48.42379 | 2024-10-09 04:36:00 | AQUA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 41.8 |
| e59a1bcf-782f-38a6-b623-dd3728f7d64a | -21.69076 | -47.68449 | 2024-10-09 04:36:00 | AQUA_M-M | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 956bdb80-84ce-349a-8b25-5e7d86d03811 | -21.68338 | -47.71957 | 2024-10-09 04:36:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 412.4 |
| d4beac90-dc7c-3b2a-8272-dfd8aa1343f1 | -21.67634 | -47.75294 | 2024-10-09 04:36:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 28.9 |
| ebdb93b9-5830-361a-aeca-bf550a3c92ee | -21.67515 | -47.68055 | 2024-10-09 04:36:00 | AQUA_M-M | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 31652ad2-2ba7-3925-8227-15d411c0c340 | -21.66789 | -47.71484 | 2024-10-09 04:36:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3863.1 |
| 26a27f9d-be9c-38c5-a5cc-10b2cefd7f22 | -21.66077 | -47.74846 | 2024-10-09 04:36:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 277.9 |
| 8c822e78-a8bb-3867-b26c-12c0588b6cce | -21.65791 | -47.70742 | 2024-10-09 04:36:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 464.1 |
| 89c307aa-c774-3556-ad59-0b397cfe399a | -21.65236 | -47.71034 | 2024-10-09 04:36:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 62.7 |
| a5448fe5-67e5-3575-9e0f-605310b55421 | -21.65087 | -47.74166 | 2024-10-09 04:36:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 4112d3b7-00a8-343b-bebd-5f6e6331b12c | -21.62665 | -47.69935 | 2024-10-09 04:36:00 | AQUA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 7a656416-4f68-3934-83c0-c092e49a504a | -21.57723 | -46.96339 | 2024-10-09 04:36:00 | AQUA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 9ab02fb5-d7c3-3c21-9e2b-6c090fb1ed25 | -21.57623 | -46.96832 | 2024-10-09 04:36:00 | AQUA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 601c9a2b-1d6e-31ae-8351-b3a8f12af67b | -20.65074 | -45.89728 | 2024-10-09 04:36:00 | AQUA_M-M | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 8245ae29-1c87-3908-9406-2620cbc74698 | -20.64519 | -45.92506 | 2024-10-09 04:36:00 | AQUA_M-M | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 5d45a9e1-9b84-3a58-a23f-8956a044b7b5 | -20.35905 | -48.72338 | 2024-10-09 04:36:00 | AQUA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 94.1 |
| a8282c08-793d-354e-b186-95bd46e79e7c | -20.35759 | -48.73096 | 2024-10-09 04:36:00 | AQUA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 137874dd-1633-3e2c-96bd-018adb42d40e | -20.34195 | -48.7185 | 2024-10-09 04:36:00 | AQUA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 242.5 |
| a17c93c9-9e32-3b85-a6c0-451eb730d7dd | -20.33992 | -48.71339 | 2024-10-09 04:36:00 | AQUA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 169.4 |
| 4ec89985-dabb-3665-9920-9630b8ab8d06 | -19.81782 | -45.60404 | 2024-10-09 04:36:00 | AQUA_M-M | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 383.4 |
| 0a90a486-87ca-3e1b-83bb-890fda08a621 | -19.81337 | -45.59806 | 2024-10-09 04:36:00 | AQUA_M-M | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 530.6 |
| 89e2b14e-7ce1-3c33-a750-5404ca864a46 | -19.81256 | -45.63008 | 2024-10-09 04:36:00 | AQUA_M-M | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 237.5 |
| 21ca7e21-04e7-3a38-8bd5-82b6ba4f6781 | -19.8083 | -45.62402 | 2024-10-09 04:36:00 | AQUA_M-M | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 611.2 |
| 85cacbd7-9753-335a-938c-1e702b1f22b6 | -19.79931 | -45.59486 | 2024-10-09 04:36:00 | AQUA_M-M | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 9c8a89cb-21e4-349f-8f34-48a4fa98b80e | -19.7942 | -45.62092 | 2024-10-09 04:36:00 | AQUA_M-M | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 4d076867-9130-358c-87b7-ac110037dca9 | -17.8736 | -43.27868 | 2024-10-09 04:36:00 | AQUA_M-M | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ee0f967e-1abb-3321-86b8-d8463dcbb3a4 | -16.66601 | -42.21785 | 2024-10-09 04:36:00 | AQUA_M-M | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e8aa883b-b5f7-31fe-8984-df95cbcb1744 | -16.65716 | -42.22719 | 2024-10-09 04:36:00 | AQUA_M-M | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 48e88c69-0681-32c8-8449-9e83e9ff1240 | -16.22688 | -42.87502 | 2024-10-09 04:36:00 | AQUA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 5e8ff6b1-1080-3be5-bfbe-4c73c5ba800c | -20.3573 | -41.84734 | 2024-10-09 04:36:00 | AQUA_M-M | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 1bd0eaef-1923-3075-9941-fd76dd7cf726 | -20.01844 | -42.43876 | 2024-10-09 04:36:00 | AQUA_M-M | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| 57761775-3ff2-30b7-b3ed-36f99a0c0faf | -20.0074 | -42.43628 | 2024-10-09 04:36:00 | AQUA_M-M | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 8724fe58-2649-39b2-b9f5-c7c7e893954e | -19.98529 | -42.43149 | 2024-10-09 04:36:00 | AQUA_M-M | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.5 |
| f763bffe-dd6c-3c8a-9147-983100a2a810 | -19.98249 | -42.44706 | 2024-10-09 04:36:00 | AQUA_M-M | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 108b0f77-96df-3b58-9b86-e10eb3cd9db4 | -19.78225 | -42.3383 | 2024-10-09 04:36:00 | AQUA_M-M | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| a2829238-ac2c-383c-9601-23ff2f3c1f79 | -19.73728 | -42.20658 | 2024-10-09 04:36:00 | AQUA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 1a33faa8-82ff-308c-99fa-475d4d57bcad | -19.1487 | -42.71551 | 2024-10-09 04:36:00 | AQUA_M-M | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| b53a2902-59e8-3554-b3b4-05a5ef606ba8 | -18.98075 | -40.88905 | 2024-10-09 04:36:00 | AQUA_M-M | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 1c8bb429-1c5e-3d61-9a03-35c903dd2adf | -18.85724 | -43.10231 | 2024-10-09 04:36:00 | AQUA_M-M | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 80514546-d3b2-3682-a55d-50c8b56640b7 | -18.60272 | -42.33321 | 2024-10-09 04:36:00 | AQUA_M-M | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.7 |
| 74cbc24a-62f9-36bf-b086-6c9658e130de | -18.6011 | -42.34343 | 2024-10-09 04:36:00 | AQUA_M-M | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.6 |
| 2800b536-8a4a-3671-9ace-bbd9859387d4 | -18.59989 | -42.34883 | 2024-10-09 04:36:00 | AQUA_M-M | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.9 |
| d568d306-1c2e-3b4e-a4c7-07e48e967d78 | -18.0133 | -42.13099 | 2024-10-09 04:36:00 | AQUA_M-M | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.0 |
| 40be3b14-88a1-3c41-a1af-fee77fcbf3cb | -17.90341 | -41.43373 | 2024-10-09 04:36:00 | AQUA_M-M | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| c2c91671-cf30-3a8b-b3db-cd5b90ffd909 | -3.81951 | -41.60106 | 2024-10-09 04:36:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 5ba92253-aa17-3ac1-8fd1-f035801ac22e | -3.81878 | -41.6059 | 2024-10-09 04:36:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 3c43b071-ff65-38ba-9fc5-336ad39da2f8 | -3.81483 | -41.6004 | 2024-10-09 04:36:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 507d02eb-dfb6-3471-8b17-9e6eb415f568 | -3.8141 | -41.60524 | 2024-10-09 04:36:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 2d75760f-f3a2-38b4-bac8-4d98ecfa2fd6 | -3.81016 | -41.59974 | 2024-10-09 04:36:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8b422982-e52d-38e7-b8e4-3af233c8f3b0 | -3.80943 | -41.60457 | 2024-10-09 04:36:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d2d5faa8-6002-35b0-b46f-4508f3c70d32 | -3.80476 | -41.6039 | 2024-10-09 04:36:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2ef7a35b-fe4a-3e0a-afbc-ef337f646d16 | -3.79936 | -41.60809 | 2024-10-09 04:36:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 297b93ec-6faa-30e9-b53d-e152068efc18 | -3.79864 | -41.61293 | 2024-10-09 04:36:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| eaff995f-7a8f-3632-86db-7f035d366764 | -3.79791 | -41.61777 | 2024-10-09 04:36:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 43dbef0d-c5ec-3307-a83d-46681997e1ce | -3.79396 | -41.61228 | 2024-10-09 04:36:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7d27a48b-87b1-336d-beff-d981c4dbe24d | -3.62195 | -42.759 | 2024-10-09 04:36:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a238530-ef65-3893-9caa-daec8da6c41d | -3.61765 | -42.75837 | 2024-10-09 04:36:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99437d1c-57fd-3a27-a30f-7c019c18ebe0 | -3.61704 | -42.7624 | 2024-10-09 04:36:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7b3d540b-f6a3-3cff-87ee-4d1c44b0aadc | -3.61335 | -42.75772 | 2024-10-09 04:36:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 427f73ee-29fa-3a88-b3c5-e06301026902 | -3.59698 | -42.80836 | 2024-10-09 04:36:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 493576a0-58e9-34bb-b994-3f1c1a374420 | -3.46618 | -43.35747 | 2024-10-09 04:36:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38115c63-c34a-3fd3-a1b0-990c56f6a7ec | -3.46561 | -43.36115 | 2024-10-09 04:36:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6dcf6f44-55a8-37aa-87e7-63e2261e24cd | -3.46206 | -43.35685 | 2024-10-09 04:36:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 606050d2-a30e-393c-977b-ae9467346bcd | -3.46149 | -43.36054 | 2024-10-09 04:36:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7305099-5358-3fd3-8c04-b38159af92d2 | -3.32696 | -42.86411 | 2024-10-09 04:36:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79b54914-8490-3e7d-9b2b-77c78dab1eff | 0.9528 | -50.20722 | 2024-10-09 04:36:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5057bea-02cb-30a4-8af5-745d486f2b94 | 0.82034 | -51.84945 | 2024-10-09 04:36:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1f8a2f8-176b-3508-91bf-e3773a7004c7 | -3.70976 | -45.11815 | 2024-10-09 04:36:00 | NPP-375D | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6b26051-5baa-37ee-96e6-fed06da87c76 | -3.55656 | -45.21692 | 2024-10-09 04:36:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README110.md)
