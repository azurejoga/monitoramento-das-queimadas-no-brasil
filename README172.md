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

## Dados Diários - Página 172

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c52e827-8d68-3991-aa18-61650c4cb9f3 | -10.58272 | -68.78651 | 2024-10-02 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 697740f6-f09d-3e8d-9dfd-35af940ebaed | -10.58167 | -68.7991 | 2024-10-02 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9d4eee7a-8ebb-390e-810d-9ccce4d3e412 | -10.58107 | -68.796 | 2024-10-02 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a339437b-9243-3d02-ad1a-9be303a9bbc1 | -10.58025 | -68.78414 | 2024-10-02 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 614e81d3-2489-337f-98b6-62f333c1ff49 | -10.58024 | -68.80075 | 2024-10-02 05:36:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92351894-e9ec-3a84-9dd2-4297fef12467 | -9.88752 | -67.89886 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba95b550-cc9d-390a-8146-f7d303735bfb | -9.77571 | -68.41946 | 2024-10-02 05:36:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf0133a3-afa1-3827-95d9-563a4cf9d351 | -9.77533 | -68.42133 | 2024-10-02 05:36:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3e69ee7-4a54-352c-94e7-1400553a3939 | -9.60617 | -67.96862 | 2024-10-02 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cff846cb-42ce-3b74-af9f-674be2c4c756 | -9.58328 | -67.85654 | 2024-10-02 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e9ddee84-994c-356b-9a03-c6c99be63055 | -9.55382 | -68.26005 | 2024-10-02 05:36:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 459adac8-d2a9-3a38-9298-63c267956f9c | -9.54716 | -67.71438 | 2024-10-02 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74dae2b4-61e1-3bf2-891d-ee00811b9db1 | -9.54645 | -67.71869 | 2024-10-02 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c50190c5-697b-31df-af80-f212854b1aae | -9.54352 | -67.71377 | 2024-10-02 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bb633f48-5469-3800-8434-596aa69c3859 | -9.54281 | -67.71807 | 2024-10-02 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec86afa7-1c19-3424-ade4-c5cf57843770 | -9.53988 | -67.71315 | 2024-10-02 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 44547bdd-d0fa-3be5-98ec-b02c86194b0c | -9.53916 | -67.71746 | 2024-10-02 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 682f6639-fada-307f-b2d1-eaa50464070b | -9.53694 | -67.70824 | 2024-10-02 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9232de6c-5730-3d51-b6d8-7ad1360106c3 | -9.53623 | -67.71253 | 2024-10-02 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f50072f0-1db6-372b-964f-d2e20633cd0a | -9.51786 | -68.24447 | 2024-10-02 05:36:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3395483-cec8-319b-a646-fe0bbd533522 | -10.06599 | -68.12966 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ad7a7bc-344a-3caa-ae1c-d9c2a1d92e62 | -10.06103 | -68.03045 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 558e7940-db35-3171-aaeb-31ca4df4b116 | -9.99782 | -69.04316 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da2ef36b-c60a-3ead-8e98-55c910dda3ea | -9.99772 | -69.04411 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a9c0116-61db-3032-b408-6f94f4560f46 | -9.99364 | -68.78398 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b8e1e24-f543-39f8-a155-ff458959ebc4 | -9.95392 | -68.76183 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f713d06-4755-322f-8d28-7708eb3586d4 | -9.93115 | -68.84772 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13e1a326-4ae8-30f7-ac1d-0fd754de666e | -9.91534 | -68.67365 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a54c4ef3-48fa-30c4-85fb-9a1913c9559e | -9.89481 | -68.88969 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28d3424f-c42e-3b95-8887-69c88f63ab65 | -9.89011 | -68.89397 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f1a34f6-64bb-3d7c-ad24-1ccb88a104be | -9.7575 | -68.52888 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e0d3e1ba-9dfc-3ac2-82c8-5ceb983e5484 | -9.7572 | -68.52679 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 50c33678-1c3f-3676-8be7-93c89d25b540 | -9.67478 | -68.81119 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dcafe2f5-1633-3c1e-8267-7b02bd7546ae | -9.67395 | -68.81609 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a8208322-4bce-33ae-8393-df96fcd1dbd7 | -9.67091 | -68.81052 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0690135-5727-36a6-ac8c-a81b06234566 | -9.67008 | -68.8154 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a31e5870-67bf-3c57-8b04-a9207a297813 | -9.66343 | -68.5757 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d497cadb-5a3d-3f2a-a4ad-f3cb5050aae5 | -9.62603 | -68.74741 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97bda4ea-5dc0-319e-ad3b-e366cdbbc121 | -9.61975 | -68.61005 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8b0be041-a172-3d1e-88cf-17ed623a3362 | -9.61036 | -68.73749 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35a6b5be-a7d2-344b-8895-f40d93885dac | -9.6076 | -68.73917 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 263116db-1091-3435-9e6d-8231934ee7e0 | -9.6065 | -68.73685 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49c64e84-7b78-37f8-a751-0e73895b4f0e | -9.60569 | -68.74172 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 001fb75d-a756-303f-9729-027e3ec15c4e | -9.59595 | -68.51806 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1dffd200-7d37-3bcf-b7cf-6b4bdf8b4000 | -9.53825 | -68.56441 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00c64e24-a8c9-377b-a902-30170f2e8895 | -9.53757 | -68.56129 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 324ef9da-2010-37d4-afa4-545cc67d06ca | -9.53674 | -68.56606 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11bc56d2-720d-3393-903c-8c490b42df04 | -9.53443 | -68.56375 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 061e98bb-ce99-3bf4-a104-67e2e5319b65 | -9.53292 | -68.56541 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13d03c05-e58f-38b2-a2c1-436d2f5444c8 | -9.52507 | -68.59653 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a0054441-3cbc-3617-81bf-7e3ce3fe7e8e | -9.52334 | -68.5981 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 98486d88-f4c7-31e7-82b0-ec85a9820f5f | -9.50722 | -68.51517 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bc85db4-d774-36b4-a5e3-fef445381499 | -9.48397 | -68.56001 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab5d9cdb-4a6e-39d7-93ee-a82f25b53152 | -9.48118 | -68.53006 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76f5bced-100c-345d-b2b2-e90b3255b8a6 | -9.48038 | -68.5348 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0bf3f91-1045-3145-abee-bdaf892be75d | -9.47737 | -68.52938 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b93c122b-9a11-3398-a81b-9f33200da09e | -9.47356 | -68.5287 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 788c30c8-3a8d-328d-acf3-c988fc2606e9 | -9.46975 | -68.52803 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 43d1a86c-79af-3a33-8fed-70069cc512a6 | -9.46593 | -68.52738 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b31f0c35-4325-3903-9e80-36c59118a4ae | -9.46292 | -68.522 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c68891cd-2208-3a70-aede-e96aab2c1451 | -9.46212 | -68.52674 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2d334798-4692-375e-85df-49d2d9365f3f | -9.45911 | -68.52135 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f9afabfd-6363-338d-9c70-17cd9c2dbd46 | -9.4583 | -68.52608 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ee1d6d3a-228d-36b2-a29f-d6499c9a94e9 | -9.42994 | -68.56316 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 246ee6d7-e007-3736-84b8-ab18073be70f | -9.42804 | -68.56499 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 297cfea7-9438-31de-958f-f22c585ffa31 | -9.42724 | -68.75413 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ea4d64b-21b0-3076-86e1-158f51b398d0 | -9.4242 | -68.74862 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb79c605-e5d5-30b8-9cd9-a0cf8ebf1f53 | -9.39184 | -68.89046 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b562b2c-86f8-315d-a9e9-26789b930af2 | -9.38359 | -68.69929 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 947213bd-3b7f-3c6f-803a-6a32c7c6f107 | -9.38277 | -68.7042 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0540f3c-c823-3ba3-a73a-90bfe7d993a6 | -9.37622 | -68.84152 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4f77278-229e-30c4-a64e-fdde96ea0347 | -9.37613 | -68.83952 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 668b4a82-f802-3ac7-bc76-89bbf408c9a8 | -9.37233 | -68.84084 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1423b86d-3052-3af0-a8a6-32e2141c4e6a | -9.36389 | -68.81695 | 2024-10-02 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a044a29-0f66-350b-902c-0a36d9197c73 | -10.0549 | -68.58376 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d82be629-04b5-304d-b362-473e3ecfd307 | -10.05411 | -68.58844 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 155061eb-8670-3dcf-a10b-1686aa627022 | -9.89521 | -67.58098 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82c4186f-39b4-3b69-a49b-8e5d6934ff47 | -9.89383 | -67.58936 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35fdafca-0bdb-33d3-823e-267abc72c797 | -9.67137 | -67.50744 | 2024-10-02 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f752be28-5a75-3c49-8755-a50705d44b4b | -9.63081 | -67.44045 | 2024-10-02 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbe9934b-22cc-3d21-a59f-52af10277968 | -9.63021 | -67.46603 | 2024-10-02 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90584a8a-6fd2-3f6c-8e6c-3b1060b10529 | -9.62951 | -67.47018 | 2024-10-02 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ecf12029-5f15-3798-b10b-e2a1f2b27e6f | -9.61724 | -67.4553 | 2024-10-02 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffe7d2f0-bf51-3d78-8f82-a2126b849a14 | -9.61546 | -67.45648 | 2024-10-02 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88c88939-412e-3eb1-a9fe-4175e7fcc025 | -9.61365 | -67.4547 | 2024-10-02 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad36935a-adeb-3dbe-9b41-5398d1e40bfe | -9.61288 | -67.43737 | 2024-10-02 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 245a0ce6-aa02-3f23-8b99-52f4bcb666d7 | -9.61101 | -67.43851 | 2024-10-02 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 784cb7b2-4bc6-354d-9ef1-094659fa36cf | -10.01171 | -67.55676 | 2024-10-02 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8db25e6d-79b6-3943-8277-38e535edb0cf | -10.52576 | -67.85265 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bffd0f70-ea4b-3c6c-a020-318077dacd68 | -10.52483 | -67.85376 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a4ca3c8-7e28-3b5a-ac1e-26238c1c6615 | -10.50257 | -67.89819 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e1d8fe6-969b-308e-9c63-b005d8dd91ba | -10.50187 | -67.90248 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77493589-87d5-38bb-96e0-7c1db5de56de | -10.49823 | -67.90186 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2561364c-9977-3abb-978e-4d859403d8dd | -10.48155 | -67.91227 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 353850c3-224b-3a3b-b766-e29ac8f178a1 | -10.47024 | -67.75706 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed909f93-1602-3f09-a2a7-e7fbee891c03 | -10.45169 | -67.88955 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c76a24e-1145-31ba-ad5a-a5cd35b8a8fd | -10.45098 | -67.89379 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4126ec2b-3acf-3086-adae-87ec56cea48b | -10.44734 | -67.89319 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 52679e88-2a19-337b-b264-5107791f1cc4 | -10.41604 | -67.94538 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 528e2894-d98e-33ed-95d8-cf7284986a38 | -10.39232 | -67.88551 | 2024-10-02 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README173.md)
