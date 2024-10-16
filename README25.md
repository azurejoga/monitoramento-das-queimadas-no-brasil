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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31b5611e-7082-3f30-965d-7b4fc2572967 | -3.49474 | -39.67049 | 2024-10-16 03:42:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4830a2c4-ae17-305f-bf79-061b441d5bc7 | -4.79272 | -39.77958 | 2024-10-16 03:42:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8354cbe6-f8cb-3331-8b6a-d14ab036ca99 | -4.79216 | -39.78304 | 2024-10-16 03:42:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d203e020-f41a-373a-a33f-6f9e1a77d53e | -4.78813 | -39.78252 | 2024-10-16 03:42:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bacea4f0-cb4d-394a-818c-97c2157e0ad5 | -4.78756 | -39.78604 | 2024-10-16 03:42:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 31e2075f-1ad8-3c08-8d65-d30e7747c045 | -4.55239 | -38.59347 | 2024-10-16 03:42:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 55e7004d-297d-3185-820e-d94a65296368 | -4.33702 | -39.13626 | 2024-10-16 03:42:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 69ebaf04-3a74-3ca4-9505-566507924f90 | -4.33624 | -39.14112 | 2024-10-16 03:42:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 21bea2ab-8ee5-3270-b84b-e6b228724ed5 | -4.33315 | -39.13567 | 2024-10-16 03:42:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 61ecada9-8006-306a-a95e-2bf3e340e2d6 | -6.83977 | -40.08091 | 2024-10-16 03:42:00 | NOAA-21 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cf2b4b68-e403-3d6e-a0c6-22ba5e556f24 | -4.24751 | -40.64824 | 2024-10-16 03:42:00 | NOAA-21 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e171a6a6-a812-38ff-b12f-4210d8b5873a | -4.00751 | -40.3948 | 2024-10-16 03:42:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5404f25e-b34a-3303-b14d-9d192a7cfed4 | -3.5163 | -43.24289 | 2024-10-16 03:42:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8e10021-dd99-3857-a7ce-2a0889693ec1 | -3.51577 | -43.24603 | 2024-10-16 03:42:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32fbd27a-58a6-3271-81a7-85a58e899a90 | -3.51525 | -43.24914 | 2024-10-16 03:42:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0dd77d9e-b97e-360c-aaae-1436c0e2dd32 | -3.51473 | -43.25225 | 2024-10-16 03:42:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0244620-7de9-30d9-ab7c-e8bce11ba10d | -3.5142 | -43.25537 | 2024-10-16 03:42:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bbf0d8b3-a3c1-302a-ad25-02761893fa15 | -3.51216 | -43.23584 | 2024-10-16 03:42:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d0fff270-be03-3434-b9f0-f0a6b56b79a0 | -3.51164 | -43.23896 | 2024-10-16 03:42:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 80bbcedc-555b-34c7-981f-36612d09b484 | -3.51111 | -43.24208 | 2024-10-16 03:42:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 393c46cb-6d1e-3a2f-a7d7-2793a5c2828e | -3.51059 | -43.2452 | 2024-10-16 03:42:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e13866b-6eb9-3fb8-96f6-2219b738ecd6 | -3.51007 | -43.24831 | 2024-10-16 03:42:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 328b1a90-b58c-32d7-99a7-ca088a118430 | -3.50954 | -43.25141 | 2024-10-16 03:42:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a8e468d5-9188-3500-a11a-86c7bad69fb9 | -3.50902 | -43.25451 | 2024-10-16 03:42:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 29942ad9-1b42-331e-9d4a-b8efcf473263 | -3.50698 | -43.23504 | 2024-10-16 03:42:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5b62672b-451b-31ad-8495-c57758837571 | -3.50646 | -43.23815 | 2024-10-16 03:42:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ed25ef1-1228-3590-80e1-94287f188e31 | -3.50593 | -43.24126 | 2024-10-16 03:42:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56a8c0ee-fa16-3c29-876e-4b13dc553cf4 | -3.50541 | -43.24437 | 2024-10-16 03:42:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f5ed8bd-9fa1-32f5-ba07-39f77ef23346 | -3.96357 | -44.05182 | 2024-10-16 03:42:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af386950-c0db-364c-974b-cbe229bc307d | -3.96298 | -44.05537 | 2024-10-16 03:42:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 836f5414-993d-3eda-9557-736a797483b5 | -5.68831 | -44.49143 | 2024-10-16 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7b054ae-6e42-3da3-828a-cef1e8a9e1b9 | -5.68287 | -44.49058 | 2024-10-16 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c657e35-bfaf-32ab-bd05-6fb5be048c35 | -5.57987 | -44.88107 | 2024-10-16 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 59487ace-6071-328f-8acf-a2656e988368 | -5.97626 | -43.79339 | 2024-10-16 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c93504d-24db-3efc-9ef2-780234e80c34 | -3.4081 | -44.5564 | 2024-10-16 03:42:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d377398-6c34-3bec-9b5f-9644083f4b85 | -3.40744 | -44.56027 | 2024-10-16 03:42:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c773bcf-740d-36a4-a48f-3338a95ac9fc | -4.44971 | -44.82867 | 2024-10-16 03:42:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf9f450a-d7de-367b-a125-ef21916916bf | -4.44904 | -44.83258 | 2024-10-16 03:42:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| beed0b9c-2c7e-3bcc-8b40-9758b05f1b44 | -4.44405 | -44.82765 | 2024-10-16 03:42:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e06ba2be-8a56-34a5-a9e2-08ee77a7142a | -4.44338 | -44.83156 | 2024-10-16 03:42:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 894fcfab-0241-3aeb-b64a-f553c0af97fb | -5.0599 | -45.58446 | 2024-10-16 03:42:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c71b34b-f6cd-3828-a6c4-39f3ebb3dd94 | -5.05912 | -45.58884 | 2024-10-16 03:42:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd078a6f-0dca-32b7-a704-5d8bfc4ccbe7 | -5.05393 | -45.58388 | 2024-10-16 03:42:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5bf2b19f-8c29-3762-ac25-d3b6fd479eb3 | -5.05319 | -45.5881 | 2024-10-16 03:42:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b1df50c0-4830-348a-90c9-8d2311b71a0d | -5.05265 | -45.35347 | 2024-10-16 03:42:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f262c81-da09-3096-9363-84db8a4d8abe | -4.9041 | -45.96462 | 2024-10-16 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 710f74fa-a426-3ef1-ab30-ff807098e023 | -4.84402 | -45.98693 | 2024-10-16 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c605fb44-d8f7-32b2-9258-4887ed9dc501 | -4.84345 | -45.98364 | 2024-10-16 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15b25a17-275d-3045-bec1-722c5d55076e | -4.84257 | -45.98881 | 2024-10-16 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f4acc1f-edae-3abd-a503-b4a3519c45be | -4.68983 | -45.78465 | 2024-10-16 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff6e2dbd-27dd-3495-9857-48693da9534b | -4.68459 | -45.77934 | 2024-10-16 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84876581-9d7d-3dad-ab40-3fd15acbf750 | -4.68383 | -45.78363 | 2024-10-16 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 733d1f9c-d695-3f6c-8625-f991ac81a730 | -4.51502 | -45.42577 | 2024-10-16 03:42:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a551d1c1-bce4-3d6f-bfed-77a6e2ca5985 | -4.51407 | -45.4222 | 2024-10-16 03:42:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6f171d2-25be-397a-a95f-c76ab84f5f1e | -4.41989 | -46.0258 | 2024-10-16 03:42:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| de86f331-9685-3ba5-b9db-54c6f39938ae | -4.38476 | -45.79243 | 2024-10-16 03:42:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b11eaa2e-0927-32e8-b995-bdb8fd778056 | -4.37873 | -45.79139 | 2024-10-16 03:42:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 08f9d93c-658c-3be1-b19e-7608316b82f9 | -4.32825 | -45.32409 | 2024-10-16 03:42:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f0c9f25b-dbca-3fc5-bf94-4c9bbc4d4093 | -4.14117 | -45.37177 | 2024-10-16 03:42:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 879ccc44-8a1d-32f7-8955-b389db325f6e | -5.60772 | -45.19689 | 2024-10-16 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca0e17db-e864-3fe7-9460-d465dad4122b | -5.60701 | -45.20086 | 2024-10-16 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 88d6eb57-2526-3472-b4ee-f873221de240 | -5.60629 | -45.20483 | 2024-10-16 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5b273764-afe6-31a1-9228-fa61b2e50d81 | -5.60533 | -45.19902 | 2024-10-16 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6c47b099-566e-3cb4-89d3-1480bbe6a7bc | -5.60464 | -45.20304 | 2024-10-16 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 26600d52-b250-3c9b-8d02-d88b5ef63da9 | -5.51734 | -45.39779 | 2024-10-16 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6dca6701-c3c0-3fb6-9995-4b64948616ee | -5.51656 | -45.40215 | 2024-10-16 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fbd3878-15c9-3191-87af-47523a7feb23 | -5.51155 | -45.39685 | 2024-10-16 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7062738c-1b22-3b91-aed5-387a9edb6cf6 | -5.40922 | -46.00642 | 2024-10-16 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d68d5021-1572-3b9e-aa8c-45f4a902d1e4 | -5.40323 | -46.00529 | 2024-10-16 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0bd4e1f4-876b-3313-8db0-14522b24698d | -5.30596 | -45.4094 | 2024-10-16 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 340478a2-b372-3598-8adb-71668bc34248 | -5.30019 | -45.40824 | 2024-10-16 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87c7624c-869b-3c5a-b9ae-2774de1850a7 | -5.04768 | -46.08034 | 2024-10-16 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a37ef20e-58a9-3251-b1bd-4a5629210254 | -3.29518 | -46.5526 | 2024-10-16 03:42:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| debdec75-b1ea-3f55-895a-81ae749a3bc1 | -3.28944 | -47.12948 | 2024-10-16 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9cae0a3e-34d6-3cf5-9c9b-f8563a4214d7 | -3.28779 | -46.5571 | 2024-10-16 03:42:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae1228f8-d6f7-3f79-8c31-3da346bafecc | -3.28686 | -46.52405 | 2024-10-16 03:42:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9179255-a829-3836-8f89-42c876849f45 | -3.28388 | -47.12203 | 2024-10-16 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bb4dbf22-1acd-3a8c-868a-42551643e38f | -3.2828 | -47.12825 | 2024-10-16 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1945a4a2-4920-34cf-84e1-3165ef51ff7c | -3.25197 | -46.88346 | 2024-10-16 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 817de284-65ef-3917-b955-50e8e0a7c176 | -3.25103 | -46.88897 | 2024-10-16 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 481ef84b-2400-35fb-ab28-421233eda240 | -3.24544 | -46.88218 | 2024-10-16 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 291b6e4d-7679-34da-b1d9-83f37ad7e8f7 | -3.24454 | -46.88744 | 2024-10-16 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7faac383-4c53-3254-93aa-e3e196aadae7 | -2.5328 | -47.22637 | 2024-10-16 03:42:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 051c9cc7-237b-341e-abc7-76fd52991a7d | -2.53176 | -47.23248 | 2024-10-16 03:42:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 236355dd-60a3-3dca-9d44-0085950c617a | -2.33201 | -46.48183 | 2024-10-16 03:42:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d2e4c2f5-2428-340f-ab23-a8f23604cd69 | -2.3311 | -46.48723 | 2024-10-16 03:42:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 67bc0632-8ff2-3947-827c-1204be1bbe3a | -2.33017 | -46.49274 | 2024-10-16 03:42:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 09369f83-36aa-3264-b3e3-e4909607374f | -2.32461 | -46.48615 | 2024-10-16 03:42:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 51694077-136e-3d40-a93b-5ac8ef0c4608 | -2.28886 | -45.88786 | 2024-10-16 03:42:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 408da657-792a-3e2f-b151-6aa7d61cce09 | -2.28685 | -45.88458 | 2024-10-16 03:42:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53dab325-4a2f-3bf9-82a1-a7a6bd20263b | -2.286 | -45.88954 | 2024-10-16 03:42:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb053742-29c1-3c79-b158-fef7210a3d58 | -2.28258 | -45.88685 | 2024-10-16 03:42:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71b1bbd8-1b08-3aec-a476-56865042c69f | -4.73403 | -46.5456 | 2024-10-16 03:42:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9fc90005-42fa-3ede-b86c-2c7fb23a4d75 | -4.73159 | -46.54248 | 2024-10-16 03:42:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 756f40cf-68cd-3c25-9933-f152281b361f | -4.73077 | -46.54705 | 2024-10-16 03:42:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 17.9 |
| c7684627-b53d-37cb-933d-9c02c42e5c3d | -4.72856 | -46.53982 | 2024-10-16 03:42:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 0a8e5033-4404-3924-a7ec-0f086b1e5d4c | -4.72775 | -46.54449 | 2024-10-16 03:42:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 71632480-dfa1-31de-a766-507d1c93bda7 | -4.72691 | -46.5493 | 2024-10-16 03:42:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2baf50a3-27a6-3b8d-abc3-e34f5c483b52 | -4.72528 | -46.54156 | 2024-10-16 03:42:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| b2f57a32-5071-3933-ad2e-8a30bf96fd37 | -4.47162 | -47.7346 | 2024-10-16 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README26.md)
