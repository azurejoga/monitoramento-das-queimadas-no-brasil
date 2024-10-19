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
| 531f2926-0624-3d57-a993-439d926f50fd | -3.49299 | -51.6781 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59d6073b-bfb9-31fa-b3b5-62c47944efe7 | -3.31928 | -51.06696 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e893c2f-9b3b-3e46-aa10-ca5193869f9a | -3.28125 | -51.05257 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d50c94a-f671-32b0-8b89-594129228412 | -3.21874 | -51.25452 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78cdae76-b5de-3cb9-b6a8-a64e982947d3 | -3.20716 | -51.03695 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a5f2a92-f8ac-35ce-8063-f14d17f5eed0 | -3.20591 | -51.04449 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93fb5b67-c561-3318-8858-a92ad5b41c35 | -3.20552 | -51.02111 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 71d7dd0e-d913-3bb3-b8a9-d8dc9bf6594b | -3.18644 | -51.29343 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7bc7390f-5e76-3c99-a9ed-3455266bdb6a | -3.15785 | -51.25677 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7220006d-78d1-307b-8a58-36e3e7f3a78e | -3.15429 | -51.30429 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e665f647-4a84-304f-8e84-5414890f057d | -3.15365 | -51.30818 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aeddff34-0d0e-3a88-9354-853378d82461 | -3.14936 | -51.14489 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cd3ced8-891f-3ef5-9f1d-a158b035c9c6 | -3.14577 | -51.35561 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ecff970-d81e-36d6-bf5d-8ca283fa4e04 | -3.09072 | -51.2146 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 61f2eb82-09c9-3f36-93d3-357537368522 | -3.0901 | -51.21842 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ead433f8-cbe9-32a0-b598-8c0e9aba941e | -3.08946 | -51.2223 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| becaf7da-f70d-3213-ab73-d30872b15a02 | -3.08651 | -51.21396 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 829bed8d-23df-3646-aa6e-0d5d23677354 | -3.08588 | -51.21778 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1b7c8659-428e-3b96-96bd-00855593923d | -3.0823 | -51.21326 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 12f7dd21-2500-3815-b2ad-242c5904fecb | -3.07747 | -51.21643 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37edbb80-0194-3e6b-b950-d17853744503 | -4.64033 | -50.9386 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9dcd93a8-7508-33f6-8c9e-e301f5b57101 | -4.43384 | -50.92302 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0244303c-5639-3c57-a40f-ef8d17042705 | -4.25271 | -50.98117 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e58aa6a0-351a-3502-89c8-f2ef9fbfd52b | -4.25214 | -50.9847 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 700d3d2c-98cf-3356-8aae-717572645899 | -4.24751 | -50.9875 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 98806550-9c93-305f-b119-dc797ff653b8 | -4.1685 | -51.03826 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e336858-62ce-3d2d-886f-2bba8fed4746 | -4.1644 | -51.03761 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f0b075f-b0db-3de2-80f0-41f681f3fd3b | -4.16386 | -51.03761 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dff78d5-7128-30b0-8f09-5f5398b559a0 | -4.07967 | -51.11855 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3772111-6635-321c-811b-d42b9e3b6c16 | -4.07722 | -51.13334 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25a0107e-465c-310c-bf8b-79c17baea33a | -4.07661 | -51.13702 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57d92247-6828-3351-b162-120cf83e9127 | -4.07599 | -51.14077 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 281c0571-e533-307a-8002-f98cc83ae7e2 | -4.07374 | -51.12885 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c8a2bc7-3abc-3445-b69b-1a7866c1ab92 | -4.07297 | -50.98168 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| eda65b74-56df-322b-9443-ba2989ea7ef9 | -4.0689 | -50.98098 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b54c21b6-461b-3112-a5ac-00b188bedb0e | -4.06679 | -51.11975 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0129dd8-2842-37de-b555-59c48657dad1 | -4.03727 | -51.10056 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4592a8c8-a534-3a3e-a282-d5e675983588 | -3.86416 | -51.95286 | 2024-10-19 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fdbe2d0c-26bf-3a86-9748-952a63214bc4 | -3.86101 | -52.22285 | 2024-10-19 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26d744ea-457a-3539-995a-e78673b581a9 | -3.82523 | -51.89051 | 2024-10-19 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b56c2976-b15c-3242-b7ae-8dea601366eb | -3.75661 | -52.05884 | 2024-10-19 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 951fbbbc-d598-3cfc-aa79-241e779e0310 | -3.75591 | -52.06311 | 2024-10-19 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb89d285-e129-3bf3-8e76-17020ae25e97 | -3.98647 | -51.02452 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61feed8a-5412-390a-8b47-ee727799900e | -3.73066 | -52.13448 | 2024-10-19 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1001962-c6c0-3f76-951b-d8b8589e27a6 | -3.60615 | -52.12107 | 2024-10-19 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff88ede6-2a48-34de-bd8c-ca7ff86e69e5 | -3.60172 | -52.12033 | 2024-10-19 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa9db522-b4e1-33e3-b35f-44fc8063f106 | -4.64092 | -50.93509 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9c5c6d28-b3cb-3361-b127-47f2e1f6fff9 | -4.63688 | -50.93449 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4bbc40b9-e8a2-3d23-9234-b5a1f5860d84 | -4.6363 | -50.93796 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5e01532d-5d3d-380c-bda4-fe8ed679955c | -4.43041 | -50.91871 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a4bef48-3ca7-3c3e-8043-0482e9ad2d35 | -4.2562 | -50.98543 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ea59043c-11a3-37b1-9955-5f30c9672cdf | -4.25329 | -50.97765 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a9ef5dd-a593-3ae5-be98-8d7a08cea5d9 | -4.24923 | -50.97691 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6da0567-9f37-3e9b-82b3-7f4604576cd6 | -4.24866 | -50.98041 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f701405-924d-31f4-b3ff-8b883066e8a8 | -4.24691 | -50.99116 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0f61c7ad-3894-3f87-b9d4-075b6e67b86a | -3.85892 | -50.75613 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bccbdea4-d772-3e84-852d-6809539ffbe7 | -4.17352 | -51.23318 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8df1245-d024-353a-8e13-77e79a530877 | -4.17001 | -51.22875 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8004c313-5f4a-378a-aedd-21c7f9d3a9c7 | -4.16938 | -51.23251 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c552373c-91dc-328a-80c4-32f0f6eff475 | -4.16795 | -51.03825 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90708175-333e-3319-a15b-32b74b855a16 | -4.07783 | -51.12968 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c00808c-9eab-3995-b673-686380be114c | -4.07537 | -51.14455 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4bae72b7-fe43-3c4e-8ca1-18a465cd0815 | -4.07435 | -51.12513 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 567a947c-d164-3c2b-964d-5000d1df41e3 | -4.07313 | -51.13254 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6137bca4-ba4b-315f-9690-f004bc4b1c2d | -4.07251 | -51.13624 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e1b1f72-257e-321a-9247-94742de341df | -4.07088 | -51.1206 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52908c2e-a591-3383-86ea-0213631dd738 | -4.07026 | -51.1243 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc2df01c-1398-30f3-ba33-a5262f08cf8a | -4.06965 | -51.12802 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1eafb4ba-738d-31cd-97eb-e8aed44c332b | -4.06258 | -50.96906 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 435f279b-a18f-3f13-bbfb-e0a9d6596014 | -4.05852 | -50.96829 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4217e1e9-b97f-30d9-ba19-ec4e0dc451e9 | -3.98908 | -51.08543 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f657c170-de00-379e-9088-5eecec0c9f60 | -3.98586 | -51.02818 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a80c4174-b3e5-302f-baf1-2da606f88c84 | -3.94294 | -50.98677 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d0183c7-311d-3f38-9667-d859d777b98b | -3.92005 | -51.23519 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c4ec92d-4c15-3028-a920-19b2393038d7 | -3.89636 | -51.36142 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 166bbc5a-6f46-3aa3-bcc7-b386f710e3ed | -3.89566 | -51.36092 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad7e5706-16ca-3fc7-836f-da39894cfbe5 | -3.85183 | -51.28677 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 771b9e25-9458-3812-bfd1-2f518c0e8ab1 | -3.8512 | -51.29062 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ec53416a-11ef-3a73-ba49-9368374ffc78 | -3.83386 | -51.29174 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc032d45-a0e4-3274-863f-7e1781020cff | -3.83323 | -51.29553 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af93d26e-e6a4-3aff-b073-223b90a7c729 | -3.82149 | -51.14592 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c608bf4f-258c-3949-aa4b-fa9d7b7d6708 | -3.82092 | -51.14949 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f85b48a0-c81c-3aeb-8932-a5561258b1b1 | -3.8198 | -51.1453 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a7677c5-fb13-3a16-b1f1-c451d533cb31 | -3.8192 | -51.14887 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c7f074a-1ffb-33c0-b418-255fa20fabad | -3.81677 | -51.14887 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46fd83ed-9045-38c6-baab-ca382611c59e | -3.78983 | -51.34395 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea3aa8e8-826f-349d-9cca-45676ed24176 | -3.78661 | -51.34307 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b68daeb-77ac-3b19-bea0-113abe3b7f90 | -3.78559 | -51.34353 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6168ff73-b344-3dcf-897c-053ba756fc9a | -3.78137 | -51.343 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd54c668-7b4e-3797-b683-1615f29148ba | -3.77376 | -51.31011 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3adc6f8e-fec9-33c6-8091-ae5d965ddb1d | -3.76177 | -51.64777 | 2024-10-19 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25f847bf-2ed5-3be5-9ab8-0873ddebeb8e | -3.73918 | -51.36389 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9716515-50d0-3776-ac9e-d479088116aa | -3.7387 | -51.34041 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 593cd50a-fff4-3cbf-ad8f-a374dc01eb47 | -3.73513 | -51.33589 | 2024-10-19 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| baa792d3-5a5a-35b4-8716-b0c9e46b5954 | -3.71683 | -51.11065 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 2b9afc21-96ae-3b73-a1b6-9dcd917400fa | -3.71621 | -51.11438 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 3010b804-2b78-3bd9-984f-676ef8cd6935 | -3.71453 | -51.11028 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 0d0d5472-718f-3ebb-8341-73d4b2815407 | -3.71394 | -51.11403 | 2024-10-19 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 68c86c3f-7a0d-3b00-af3e-87fbc358ae28 | -3.70463 | -51.60218 | 2024-10-19 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ee5cb917-119e-3db7-98ad-a02ef90b283d | -3.70036 | -51.60148 | 2024-10-19 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README23.md)
