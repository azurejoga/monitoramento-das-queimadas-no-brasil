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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08a39b00-48a3-345b-83dc-a5abdff03eb8 | -2.89208 | -53.28193 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f838b80a-b6d0-3933-93a8-201e9bf63285 | -3.46585 | -50.11996 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 570951f9-7bcd-3f69-8782-038e5254630d | -3.02149 | -51.60261 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c739f559-8633-37c2-b80b-4068ff21a133 | -3.86611 | -54.35735 | 2025-11-16 04:55:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f94e58d9-d61b-35f7-805b-7fa8e4b37411 | -1.83635 | -53.80674 | 2025-11-16 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66aa6e0d-28e9-343c-ac01-eb3915f4809e | -3.21998 | -51.34229 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c60138ff-5815-3afe-97f0-e29047a402d2 | -3.13064 | -50.28818 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 93a68911-3e4e-379e-b3c7-3563cf416a7d | -3.23615 | -53.62412 | 2025-11-16 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08976151-c90f-3f60-a48e-ad8102060d33 | -2.96989 | -53.21668 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc1d76b6-1b9c-3515-9b77-23291236246c | -3.9282 | -52.17945 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3dc5e8ea-379c-39de-afb8-23ca5e3deacb | -4.6848 | -46.52629 | 2025-11-16 04:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c41c34e-12e4-3bc7-a600-a3122ee2a31c | -4.73021 | -46.37667 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 37a06249-0b86-37fd-a3b4-377347f3d4eb | -4.80569 | -48.34267 | 2025-11-16 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0976de9f-7914-3d43-8aed-92ad5641dddf | -1.24963 | -55.87862 | 2025-11-16 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d723179-1647-3cab-8b8a-563d9b21adc9 | -3.45408 | -51.02428 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0257df4-e2f4-3d60-ae4d-9b186f757413 | -1.8319 | -53.79186 | 2025-11-16 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10778708-c910-32c7-b1f8-a81e39064062 | -2.71316 | -47.40179 | 2025-11-16 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e61b441-4e61-316a-9ff2-89f8170ec98a | -2.52801 | -47.81681 | 2025-11-16 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| fbe11515-7bfe-3d8a-bdfa-c3ff9f558ad5 | -3.30477 | -50.07457 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a7d725e-73f3-3650-bd6a-c754fda53f60 | -3.45563 | -51.02543 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2f696e1-ca7b-3b72-a6ea-310c7a3bfa96 | -1.84771 | -47.92733 | 2025-11-16 04:55:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ad4bded-9123-379c-8c44-0cd155d97267 | -3.99665 | -44.27106 | 2025-11-16 04:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21ce48e0-69bd-30da-a204-b2031d92bbbc | -0.36385 | -51.75861 | 2025-11-16 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1333653-44bd-3b05-98b2-c3f31e8c893d | -2.47027 | -48.86067 | 2025-11-16 04:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f397bf0-62b5-3bf8-a133-3c039c5c3ccb | -2.30303 | -53.51936 | 2025-11-16 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a98c44d-8dab-3939-bd55-a62042a458c9 | -4.83845 | -47.54801 | 2025-11-16 04:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 80232748-671a-3ad5-b0cb-3b29abd62637 | -4.7097 | -48.31782 | 2025-11-16 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75bb4efb-ed8c-3f65-90d7-341cecda0186 | -2.68896 | -49.07091 | 2025-11-16 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e550ddb7-e7da-3cf3-b268-febc5e332319 | -2.58042 | -51.87403 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6039607b-09d7-3aa1-83cc-2765a22fd670 | -3.09618 | -51.10098 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f5ef5d3b-c9e5-30d2-8fa3-dd1fd5d1f6d3 | -3.73498 | -51.32251 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d6b4d3d3-5f90-369a-8f96-f5d357f2cf78 | -4.68886 | -46.31786 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8456e60c-ccd6-3435-8a97-d2d573824af6 | -5.23326 | -44.34747 | 2025-11-16 04:55:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 16c4aec0-c371-3db5-8f13-5b1eeeb66477 | 0.69215 | -51.46206 | 2025-11-16 04:55:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63cdedb9-c38c-39a6-a5a9-02d73ed012e4 | -3.91488 | -54.13377 | 2025-11-16 04:55:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8d32b04-5167-336a-b805-5ecc81c1ab87 | -3.474 | -52.16817 | 2025-11-16 04:55:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0a18f03-e09e-3898-9a71-513af04400fe | -4.50367 | -50.11696 | 2025-11-16 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a5f7d0d8-27e5-3497-8ba2-cb137a86891d | -4.42789 | -43.39259 | 2025-11-16 04:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f4a6d4b-4efb-360b-b89c-810cab23f1e5 | -3.99615 | -44.27444 | 2025-11-16 04:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3fc7bd3-7c1b-30df-8678-09464dabb4af | -4.97807 | -49.66517 | 2025-11-16 04:55:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6a56e67-2878-34bb-8b2c-9f10c8eedb95 | -4.69981 | -46.30929 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 50110a4e-e310-3a6d-9309-76ebaaa61c76 | -4.6545 | -46.7382 | 2025-11-16 04:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67b155bc-d958-3d23-bdea-48cbaf0d09b8 | -5.9979 | -41.92021 | 2025-11-16 04:55:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 86a884f7-370e-3eec-b7d9-5081cce48f18 | -5.96388 | -43.7454 | 2025-11-16 04:55:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0382ec44-1f6e-36db-9cdc-a8691fb0d5b4 | -3.03844 | -51.20024 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b14f11ab-9b78-3829-98dc-3fca1a9815cb | -3.94412 | -47.20528 | 2025-11-16 04:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8ead82d5-5783-36ea-88df-1cd0d26ef358 | -4.69021 | -46.31884 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5e0ec7ba-97b0-3b5b-b331-ef7fac07a384 | -4.69907 | -46.31425 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 1305a986-749a-3a61-ae93-df7c2d8f4089 | -5.48708 | -46.91403 | 2025-11-16 04:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 325c2576-f8ca-36c2-9027-45806d94d6a0 | -4.01994 | -48.81406 | 2025-11-16 04:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 466778a3-15e0-369d-8ab8-bbf9e6a6af8c | -3.30413 | -50.07878 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6f2052d4-5955-35d7-a206-7f21211c7d42 | -2.78864 | -43.34909 | 2025-11-16 04:55:00 | NOAA-21 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30bee4c2-7630-33a8-a29c-702d840b1aad | -3.79044 | -44.17653 | 2025-11-16 04:55:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 361d28bd-35b6-37b3-a889-9a27564d1d34 | -3.18348 | -49.23694 | 2025-11-16 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c52ced6-90ac-374f-a721-e166b3310af2 | -3.31895 | -51.6101 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f93d5d0-fe4c-37de-85ff-855030e46bd3 | 2.33843 | -51.65143 | 2025-11-16 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68398151-9225-3d18-bc6a-309fa3b8698f | -4.43247 | -43.40155 | 2025-11-16 04:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4e058b2f-df29-3d55-a32a-7af3052a148c | -1.85008 | -56.37623 | 2025-11-16 04:55:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9839e52-a234-3579-b942-d7b9b4345c15 | -2.07171 | -54.1716 | 2025-11-16 04:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 86bbcded-e4a2-3ca6-850f-31665fa0fd89 | -3.38435 | -50.16758 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b90b294a-13a8-3bd2-8321-412394dbc779 | -5.47618 | -40.96845 | 2025-11-16 04:55:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 160337f0-f880-3e7c-a16d-053d18debf23 | -4.6936 | -46.31855 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 033424bf-5393-3d4f-928a-b05f024539d7 | -1.99365 | -47.35205 | 2025-11-16 04:55:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9c5cee29-3437-3eb3-9e6a-961346274c2a | -3.45946 | -46.12225 | 2025-11-16 04:55:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a6edd080-4713-367e-84cf-7ab97717535e | -6.07685 | -42.86842 | 2025-11-16 04:55:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| de103195-c397-3a79-aaa7-8b536b0e574f | -3.59668 | -41.6614 | 2025-11-16 04:55:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 43002361-86a6-3e9e-a47e-66c483bc19fa | -5.77425 | -44.38605 | 2025-11-16 04:55:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f7b305a2-ada9-3e3c-9622-02d48af9713d | -4.31016 | -50.86985 | 2025-11-16 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6fc6e5b-8e0a-341e-b84f-775896af7b64 | -3.16798 | -50.16261 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b17e0ee5-2ba1-3537-95d1-02b39759f5aa | -3.22488 | -49.47184 | 2025-11-16 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47bbfb94-5034-3d26-9554-bc1570f7d0bb | -2.6292 | -51.93607 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 92787550-cd0a-3818-9a53-042cf9e98f67 | -5.69212 | -45.987 | 2025-11-16 04:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff74af4e-b0d0-3294-ad0d-3340e33e1d00 | -2.57761 | -51.86995 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa4d0223-fbca-37d8-a57d-66c24e81319c | -4.76071 | -49.3886 | 2025-11-16 04:55:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67c2baac-3fde-3e66-93e2-07abba819f3f | -4.35367 | -44.35006 | 2025-11-16 04:55:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05aa458a-c862-3627-a2a7-c92d5fa80dd4 | -4.35078 | -44.35085 | 2025-11-16 04:55:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 567bcc0d-856b-3808-8324-d4aed8e8a963 | -4.01703 | -48.81219 | 2025-11-16 04:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2b818fd7-c551-3b52-a10b-a1af9a121b9c | -2.93702 | -49.35076 | 2025-11-16 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12e314ce-9032-3379-ba02-0e8a4e5ec6a6 | -1.64684 | -53.67029 | 2025-11-16 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9838e07a-5e39-3406-8b7d-932f0046d799 | -1.8369 | -53.80328 | 2025-11-16 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63021cfe-d39c-3717-8901-29a719f3fa45 | -2.86992 | -51.47485 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 372d3277-6733-39b2-aff2-8380b3fddc12 | -4.70108 | -46.31029 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 97e3605e-6795-3285-8e3c-7d3201c5d7a1 | -4.42561 | -43.40856 | 2025-11-16 04:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 6e2af675-14f1-32f8-b31c-07b029de837d | -2.17983 | -52.09091 | 2025-11-16 04:55:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e32036c7-ef14-34fd-bb00-e2604e47f352 | -3.63511 | -45.16162 | 2025-11-16 04:55:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a7a078f-bbd6-3971-a2f3-8f89b4eaedab | -3.13614 | -50.28636 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5d0092a-97f3-3e9d-a116-11d3a3a12b0c | -3.63555 | -45.15868 | 2025-11-16 04:55:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4aea1b3a-bf5c-3802-97ae-f5ecbbcc944d | -4.73894 | -46.3829 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 16830271-6f12-38e4-9797-dd45ad0d9c6e | -3.17159 | -50.16314 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f483a106-f693-3983-beb0-0cfdfaa5f9c4 | -3.33743 | -50.27191 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| dbe2955b-5f53-39f4-80ab-8ac128469b12 | -6.07622 | -42.87306 | 2025-11-16 04:55:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| cbee2f76-abcf-31ed-97c8-35620cff0a96 | -2.87049 | -51.47118 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6160709a-179a-3c61-8c8a-4ac3b26c1a8e | -2.80557 | -52.96197 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3ab21be4-ae52-3c1a-b005-ddbf8463fd9c | -1.31991 | -55.38424 | 2025-11-16 04:55:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 923afc90-17da-30f2-bf9b-fa9dea80de3e | -1.18389 | -53.58296 | 2025-11-16 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e7787a3-7e96-3934-baeb-af1405d1412d | -3.25429 | -49.76528 | 2025-11-16 04:55:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 939c5741-e1c9-366a-9a59-06615724a71b | -5.24871 | -43.90713 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60ad9878-81fc-3e87-aeb0-db5403a90089 | -3.99939 | -49.888 | 2025-11-16 04:55:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 68452c8c-b03a-35e6-a99c-67e60dd0941f | -3.02092 | -51.62856 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da313cbd-ef3d-3ea2-b0c7-6171834a5d05 | -2.52743 | -47.82056 | 2025-11-16 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |


[Clique aqui para ver as próximas entradas](README52.md)
