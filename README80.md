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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ed6c9a0-0027-3a91-8cea-49b876878f1e | -9.88516 | -60.2169 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e70f4ef4-121e-3779-a409-5666a33faf45 | -9.88198 | -60.82017 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d92c346f-73f1-30c4-8e88-826e7b7fd06e | -9.87066 | -60.10723 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91cd598c-bb0a-37e8-b962-dbd7921fc283 | -9.86944 | -59.8299 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a042f781-8b7d-3f23-9993-0816031840ef | -9.86855 | -59.835 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 00b75595-c421-3d7e-b8da-b36d39e2d8f5 | -9.86674 | -59.82747 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7fb8009-6774-3f09-9250-dc328869d719 | -9.86664 | -60.10653 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 436c02af-53c7-3c05-8bc5-01e1f666a29b | -9.86603 | -60.11006 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| feaa74f5-e1f7-39bb-bd17-3cf1f4d28158 | -9.86297 | -60.12782 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79016912-e4f7-35d6-a339-e0119750cfde | -9.86194 | -59.83187 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aeebe04d-9f81-31d6-8598-8ad39c8795f8 | -9.86155 | -59.82846 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79fed6d9-bb75-3700-a8df-cf534d865059 | -9.8614 | -60.11289 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fcf0ebb-3ea4-30bf-ba20-0b454a7e2eaa | -9.86121 | -60.28378 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d33adc5-0e16-32f6-ba0c-89d797b108da | -9.86079 | -60.11646 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7df51c3-4777-3fc2-b2bf-cc5868fac74d | -9.86058 | -60.28742 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8475d7e2-a872-3fec-bd21-9cbd9dd7fff9 | -9.86017 | -60.12003 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe476545-0b2c-37cb-89d5-c0a0f8e538a4 | -9.85956 | -60.12357 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 527f79de-3a10-3fc4-aaf1-eb1f78223888 | -9.85894 | -60.12712 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fb51a61-b4a2-3b79-a27f-4e418c71a2c7 | -9.85833 | -60.13069 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7c6f9aa-8a63-3194-b092-55c6c51431cc | -9.85772 | -60.32866 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4026cb10-150e-30bb-868e-cc7ff4f99b3d | -9.85737 | -60.11221 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 356b0fef-d9bf-355a-9f38-94dfa21a2402 | -9.85713 | -60.28308 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cbea008b-bcec-30b9-b71e-dbe78ae4f33f | -9.85651 | -60.28672 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4ebc2d17-3759-380b-bfa3-7ac91fc257b2 | -9.85427 | -60.32428 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9100b49-a61c-39b0-bd96-50a93fe05ec6 | -9.85364 | -60.32795 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fac6b9ec-aa08-3094-a05b-af3feb384d18 | -9.85306 | -60.28239 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9bc16feb-0946-345e-93bb-a83c76397031 | -9.85244 | -60.28602 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 56cbc6f9-0ffd-3819-b70a-d0ccea5fdf19 | -9.84962 | -60.27805 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 929fd099-18de-3c58-ae92-deb2c7ff29e8 | -9.84899 | -60.2817 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 671e5666-ca09-3c81-b897-e3d5ad100862 | -9.84836 | -60.28534 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d023c58a-80e8-32b6-8ffd-e31089fcc527 | -9.84774 | -60.28898 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0b5732d-5020-3a90-88e5-810df644d1e7 | -9.84554 | -60.27735 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b44be599-9eb1-375a-835d-95f0c57aa053 | -9.84492 | -60.281 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 76292752-29e4-3147-bc21-0457e225d98c | -9.84429 | -60.28464 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ce931ddc-2396-361e-9b0b-d1cabc21a633 | -9.84366 | -60.28829 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 323aac2d-c940-3290-b8d6-59a0509b6403 | -9.84338 | -60.26561 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b20f87eb-f23e-3052-acc2-2c3a7fb66ccd | -9.84274 | -60.26932 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 077b596d-0aad-322b-984a-520d3bf413f6 | -9.84147 | -60.27666 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe220727-01c6-3b47-8039-3580eea13c9d | -9.84084 | -60.2803 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4099893-167a-3d73-9533-ba10e20e0554 | -9.84021 | -60.28396 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0eb867b-9148-38ba-8ba4-6397a71db6f4 | -9.83959 | -60.28761 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22b17fa9-a2ce-3146-a3ca-56135d319722 | -9.8313 | -60.73826 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecdf6d32-11aa-30b6-a033-c8ee037f1510 | -9.80984 | -60.4352 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f63203dd-be15-3bbc-9144-4e3d527f4a26 | -9.80313 | -60.4495 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 714b5c95-06d1-3bd0-a283-ff8fd42b4471 | -9.78763 | -59.81405 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25821f75-04a7-3c04-8b85-30093c28d186 | -9.75755 | -60.4267 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 336cc958-bc31-34d1-b4e3-ec9117d4ac7c | -9.75635 | -60.42601 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ed8671b-08e0-32a9-857a-58e4e897caf8 | -9.75344 | -60.42593 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64389cef-4678-3b42-b85d-02b53a8dc3e3 | -9.7528 | -60.4297 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 537389c4-3c17-393a-8a1c-0b7f9d952b73 | -9.75216 | -60.43349 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c5f9f7f-45e5-388c-b7e4-fc918aa94d97 | -9.75158 | -60.42903 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1310b880-bed9-37f3-8eec-81214445f092 | -9.75091 | -60.43279 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c00bdcae-352e-3468-8adb-ef6cc72a1c6c | -9.74997 | -60.42142 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09386e17-9f72-3276-8561-705c2af31e92 | -9.48053 | -60.37798 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 492ae0cb-0112-3079-8d7b-f0465a140339 | -9.4764 | -60.37729 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12ad9c5f-38ee-35f6-9c11-b6833e7d9b71 | -9.46458 | -60.54369 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8be197b1-8ce8-355d-8346-1ec856720622 | -9.41651 | -60.29041 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3482abee-4baf-3c1f-806f-5a457560f6d1 | -9.39705 | -60.90683 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0b9fc7b-46c9-30a0-bbd9-32d191565535 | -9.39349 | -60.90203 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fac9ffea-af66-3039-867a-e1f2000f2033 | -9.39279 | -60.90607 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c939f37-288a-3c5e-9230-984ae86de496 | -9.39065 | -60.91827 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ee01b43-14dc-3bbe-9279-d248584ed6ad | -9.38923 | -60.90126 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88825ba6-6dbc-3d54-ac16-37817cb79890 | -9.38852 | -60.90529 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43940f89-5eb9-3a84-87bc-e9491aaeb46c | -9.38781 | -60.90935 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 658bf14c-92c7-3d68-b035-3acccbb7bbdf | -9.3871 | -60.9134 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cb77aff-d14f-3dc8-86db-0d16a61a4b46 | -9.38638 | -60.9175 | 2024-10-12 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60ab2a55-a0c0-3351-84a4-20880a339bed | -10.4631 | -60.10242 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f56fa5d9-0f03-396e-aea0-6ff2485d5225 | -10.46095 | -60.10188 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3766d81b-2fbb-3fa5-9671-a02087ea9b46 | -10.45977 | -60.10886 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bef479ff-8b8b-32a2-a8e9-18c5f05c48a3 | -10.4564 | -60.1045 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f815bbdf-8a0b-3e46-b41d-e12db783cde3 | -10.4558 | -60.10803 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 518cd164-1879-36f2-aea2-cebcf7845645 | -10.449 | -60.09979 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5e3d756-673d-3e10-af9a-d0c5d6a8cd02 | -10.4484 | -60.10331 | 2024-10-12 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1dcb0fea-4ed3-3489-8a64-515260648390 | -10.43291 | -61.00456 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5118275f-93af-308b-ad52-7b893ac5dcb8 | -10.43224 | -60.98388 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a977a7f1-99a0-318e-bf45-de616faeb7a9 | -10.43219 | -61.00858 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3de07dbb-fdeb-323e-8523-897802d0e424 | -10.42801 | -60.98322 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06ac7348-dd8a-3682-b5c0-32aa62916431 | -10.42798 | -61.0077 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01298e3b-20ad-3cdc-80ae-6e45f1d1da8a | -10.42725 | -61.01181 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd8d7c7c-1c81-39cb-b230-dc9790fe7676 | -10.42448 | -61.00294 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86d51d45-ac8e-3cf2-8d93-df7b93a6a369 | -10.42375 | -61.00702 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0afd9b1-f97a-37e2-81b9-7a30e905d305 | -10.41741 | -60.99445 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d35ce4a1-06b6-32b2-83e0-c544ebfd431c | -10.40386 | -61.2164 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 99b9eb21-1274-374b-b876-5daf6d56c84f | -10.4003 | -61.21158 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b975bb5d-4c7b-3c32-acd3-609cee876b3e | -10.39956 | -61.2157 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5229e10-80ee-3b9c-b9e0-fed9df6e40e3 | -10.39527 | -61.215 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86b5b310-b7ed-3b23-9e32-e7dce2046786 | -10.38963 | -61.19714 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 829297b5-fbd1-3ed4-acd2-fcbceb7f409d | -10.38889 | -61.20123 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7081207a-9345-3d43-b770-aac518f2e401 | -10.38742 | -61.20942 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6c4fb20d-ce69-3953-aae0-198fcd1494b5 | -10.38683 | -61.1976 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9ff53ec5-c163-3f81-92fa-06e824e109f2 | -10.38613 | -61.20168 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b9afb487-3953-395b-9842-5f057e1c425a | -10.38542 | -61.20576 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 023543b0-9b1b-32ae-9e35-357d9cadfcbe | -10.38535 | -61.19638 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3ea74d99-2b2e-3c7a-aa28-a5e5f9978b59 | -10.38471 | -61.20987 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fc9db801-15d2-30cd-a3a3-6a3c119cd51e | -10.38461 | -61.20044 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2b9c198d-c839-3a51-95cc-089876da6907 | -10.38388 | -61.20451 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 10feecbd-be60-3653-b659-aa268533c04b | -10.38315 | -61.2086 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eb185f52-e80a-3829-a551-ab09a38725fe | -10.38255 | -61.19679 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9712b681-7221-39e9-8d01-673b36ea7d71 | -10.38185 | -61.20086 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1bc8f607-189d-3244-9c30-9e3594b8a49a | -10.38115 | -61.20494 | 2024-10-12 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README81.md)
