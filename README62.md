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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a30284db-e44f-3daf-a757-a334120bfb57 | -2.05415 | -56.8702 | 2024-10-27 05:16:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe61f1f1-d0fc-36dc-bf83-990817a40c61 | -2.73406 | -57.48543 | 2024-10-27 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68845841-e2dd-3b1d-84f3-ce5422286ed6 | -2.73075 | -57.48491 | 2024-10-27 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c441ea47-b65d-3296-b14a-b5a3b0e5d397 | -2.71689 | -57.46508 | 2024-10-27 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0cbec75f-0fe8-3b3c-93f7-62c5340c1d2f | -2.71635 | -57.46854 | 2024-10-27 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc8081e9-7fad-3fd3-b620-ae6da2582194 | -2.59775 | -57.57386 | 2024-10-27 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 729bb380-1133-35fd-9d3f-ab960773f310 | -2.4267 | -57.05701 | 2024-10-27 05:16:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e795effa-b651-38c7-aa9e-8e511e47bc07 | -3.54921 | -57.62343 | 2024-10-27 05:16:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9885e349-e805-3ce3-abc1-2cad2fb98286 | -3.24693 | -58.16145 | 2024-10-27 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e2943d9-3835-3d65-bfe2-f0c658b6827e | -3.00612 | -56.78904 | 2024-10-27 05:16:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef6c31dc-052c-3fbd-9947-0c4a76cea9af | -3.00556 | -56.7926 | 2024-10-27 05:16:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f00fb222-8f59-398f-beb6-b082c23af76e | -2.73352 | -57.48888 | 2024-10-27 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fe39b300-ee1b-3f0c-a86c-79eaa377f49a | -2.73021 | -57.48837 | 2024-10-27 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cfd92b04-6149-31cf-8296-fc3b740f4b2c | -2.71358 | -57.46457 | 2024-10-27 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca1f9408-05b6-30d7-acad-1d6bc2295df4 | -2.62036 | -57.27583 | 2024-10-27 05:16:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9d284cf-4062-3296-ba6e-f1ec22ebe520 | -2.67936 | -59.43351 | 2024-10-27 05:16:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e0c5f853-013a-33dd-a5f7-ac9ea1ed5e44 | -3.42005 | -59.24656 | 2024-10-27 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56f3e9e7-6966-31e0-a1aa-8ee969c5772c | -3.98786 | -59.1436 | 2024-10-27 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d8e38588-2e0c-34df-8abf-1ea5572758d6 | -3.98731 | -59.14708 | 2024-10-27 05:16:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6b71644c-af8f-3ef9-a409-802ff536ab4b | 0.17477 | -59.42603 | 2024-10-27 05:16:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f50fe8cf-614d-3844-890e-c169f8c118f1 | 0.70507 | -59.74401 | 2024-10-27 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe480bd1-8859-37d3-8e2a-a3c2a37515d2 | 0.70447 | -59.74016 | 2024-10-27 05:16:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b961c7dc-78c9-36d4-987f-ce28cb2a69ef | -1.91484 | -59.98155 | 2024-10-27 05:16:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 615974d8-c8e1-3061-a492-7bde06a5b854 | -1.81908 | -60.23384 | 2024-10-27 05:16:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78827d67-ac18-3c66-957c-bf6037c2e891 | -1.49816 | -60.24451 | 2024-10-27 05:16:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50577d0c-21d9-38c4-86b1-40c98b81b54f | -1.91425 | -59.98529 | 2024-10-27 05:16:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58fd4fe8-6176-358a-83d8-a1b209d0abbf | -3.20537 | -60.69689 | 2024-10-27 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 38f093f2-75b8-3ed2-b419-cd4ac4588491 | 2.71709 | -61.49209 | 2024-10-27 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f9d964d-598f-322f-a0db-78938f28f397 | 2.30218 | -61.32954 | 2024-10-27 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| df6b22e3-3259-397b-98b9-9ae7247862ba | 2.29904 | -61.33483 | 2024-10-27 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e2186d2-b160-39d7-821f-2a87ccd88bad | 2.89977 | -60.27309 | 2024-10-27 05:16:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2cf75125-8adb-3ff9-b8a9-36c8c35e1936 | -0.38385 | -61.09118 | 2024-10-27 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d86ff5f-20a9-3a39-a96c-65354dfe3cea | -0.15248 | -60.86946 | 2024-10-27 05:16:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b1173a2-f6c4-3304-82e2-481684a7ccf6 | 0.10431 | -62.55093 | 2024-10-27 05:16:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11d94e64-f5c6-3960-9ce5-41f15e30e073 | 0.11184 | -62.54615 | 2024-10-27 05:16:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a24eba79-3192-33d5-adee-a9ae6808c2f3 | -7.2364 | -46.04756 | 2024-10-27 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1985e0f-aefa-308f-b250-8f5f5304c84d | -7.23556 | -46.05402 | 2024-10-27 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b006e7aa-dd54-3138-aa79-c4c19946e1ea | -5.95921 | -49.31782 | 2024-10-27 05:18:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c2345551-a98d-3257-8ead-b1e91897ddaf | -5.95427 | -49.31337 | 2024-10-27 05:18:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0610c14f-ba76-3a80-94e2-2083ab641e47 | -5.95376 | -49.31698 | 2024-10-27 05:18:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 43b4f313-5e8c-39b6-87fe-b9a63c15344c | -5.81867 | -49.39619 | 2024-10-27 05:18:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21a0079f-f861-3d49-a8a4-29903dfa9455 | -5.81324 | -49.39543 | 2024-10-27 05:18:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd84abe6-bd18-3c58-be93-feb383744896 | -5.67892 | -50.01059 | 2024-10-27 05:18:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d1847ac-0691-3e48-990f-54036e179b19 | -5.23735 | -56.06194 | 2024-10-27 05:18:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1906966d-5693-3a3d-a5c3-579e65086c5e | -9.82903 | -59.47887 | 2024-10-27 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7a02d6c0-d139-39ab-82b4-06040fb39d1f | -4.26086 | -63.14819 | 2024-10-27 05:18:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba1bb481-18f7-3672-ac15-4c3d6989bd4f | -4.26004 | -63.15322 | 2024-10-27 05:18:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04347ef3-6374-3693-993c-70360f43ae30 | -4.25692 | -63.14756 | 2024-10-27 05:18:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b01eeb0-e043-3949-9009-a74e649f4b51 | -4.2561 | -63.15258 | 2024-10-27 05:18:00 | NOAA-21 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e67f80cc-0698-3a0c-a4d9-a61aadbe008d | -3.44371 | -68.93576 | 2024-10-27 05:18:00 | NOAA-21 | SÃO PAULO DE OLIVENÇA | AMAZONAS | Brasil | 1303908 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4ef3e97e-4890-33c3-b45a-1a085b593ce9 | -0.9815 | -53.7192 | 2024-10-27 05:25:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 26f74fff-ce3c-3bfe-94b8-31519b33cfae | -0.9815 | -53.699 | 2024-10-27 05:25:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| c67cda36-3b3d-3388-9e1c-8e9d82a30218 | -0.9815 | -53.6789 | 2024-10-27 05:25:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| a4bda32c-dc02-3b91-a27d-c4b37a8154e1 | -0.9998 | -53.6989 | 2024-10-27 05:25:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 3a692da2-6bf9-3b5f-a1af-7fa34c60adaf | -2.5311 | -51.1816 | 2024-10-27 05:25:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 38f34b45-7cc9-32e4-95bf-8b78560f96eb | -2.5312 | -51.1609 | 2024-10-27 05:25:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| da763b44-d1db-3eb2-a42c-8b197f911400 | -2.5495 | -51.1812 | 2024-10-27 05:25:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 398e3afd-b8b5-35a9-98e8-84e96fc61d89 | -2.5496 | -51.1604 | 2024-10-27 05:25:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| f6b1a0fd-6abc-3f3f-9168-85e4fed43b30 | -2.7034 | -49.3088 | 2024-10-27 05:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| b095b0a9-e538-3ae0-8b8d-531f3f37ec28 | -2.8515 | -49.2408 | 2024-10-27 05:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 4e71c712-18e4-388f-9d0d-b09e4737b03f | -2.9345 | -51.7505 | 2024-10-27 05:25:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 8654986b-8247-390f-87df-7b936d4bb2ba | -2.8329 | -49.2626 | 2024-10-27 05:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 35cab701-5bcc-3edb-b9d7-ec2d33375ae0 | -2.833 | -49.2413 | 2024-10-27 05:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| a3fae639-5ad8-3f67-88b8-48d215631fce | -2.8514 | -49.262 | 2024-10-27 05:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| dbaa32e3-77e0-3baf-b733-db83863c95af | -0.9998 | -53.6989 | 2024-10-27 05:35:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 2ebc7c2b-91b2-35c5-8ac2-d58b19340eca | -0.9815 | -53.7192 | 2024-10-27 05:35:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| cc6a5fa2-7dc8-3053-b5e4-f30068b2a789 | -0.9815 | -53.699 | 2024-10-27 05:35:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| f4dcf540-bf3e-36cb-adf9-e2893f047e42 | -0.9815 | -53.6789 | 2024-10-27 05:35:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| e55c6e5b-e075-3460-8275-bb376058b239 | -2.5311 | -51.1816 | 2024-10-27 05:35:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 131.3 |
| f6e02938-3398-31c0-9706-c43a89281bbd | -2.5312 | -51.1609 | 2024-10-27 05:35:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| ea88bac4-2d4d-366d-b511-cb085cc302ad | -2.5495 | -51.1812 | 2024-10-27 05:35:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| bbd7d4f8-9ea9-3289-b4f2-14e565cbfb1b | -2.7033 | -49.33 | 2024-10-27 05:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 358626e7-2d95-3d4c-90b2-62e2e5198b13 | -2.7034 | -49.3088 | 2024-10-27 05:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 2d2f621c-c1fe-3a63-9ac1-eff64fd3a7af | -2.8329 | -49.2626 | 2024-10-27 05:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| a20b4586-54cf-386e-9d3f-fb2062edde1b | -2.833 | -49.2413 | 2024-10-27 05:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 7abf01f3-4f26-3bf4-9277-af7fba723b12 | -2.8514 | -49.262 | 2024-10-27 05:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 87b97a9a-71a8-375e-a24e-b6765c693832 | -2.8515 | -49.2408 | 2024-10-27 05:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| bd6df98f-305d-39c7-a0e4-0bcf9a950cef | -2.9215 | -50.274 | 2024-10-27 05:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 05f92012-ff12-3b93-98ab-6ab8d5964b9e | -2.9345 | -51.7505 | 2024-10-27 05:35:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| e4d484f5-ebfc-3642-a161-2e5bc7a310ff | 1.78402 | -50.45511 | 2024-10-27 05:38:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95a0a696-d24a-392e-aca9-904e29e5a55f | 1.77927 | -50.46847 | 2024-10-27 05:38:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 98c85248-2835-3052-858a-d6ca45399bce | 1.77825 | -50.46237 | 2024-10-27 05:38:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1d1eac45-2211-370a-9bf1-47a700afb0a2 | 1.77722 | -50.45626 | 2024-10-27 05:38:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6643dac7-4759-3919-ba9a-93a364b7254a | 1.77145 | -50.46348 | 2024-10-27 05:38:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b955ad3-6bd8-3528-a3b9-8dd6724adb1c | 3.6258 | -51.28896 | 2024-10-27 05:38:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 141b770d-3a88-30a0-a48f-3208dab8e230 | 3.60519 | -51.28223 | 2024-10-27 05:38:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 226dfb48-870a-3710-b13e-f5c29d7a1abd | 3.5989 | -51.28332 | 2024-10-27 05:38:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bc696342-ea26-3894-9781-104befc4740e | 3.39346 | -51.29044 | 2024-10-27 05:38:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 30dc2677-8ab7-3fcd-8f32-74856eb5c964 | 3.39259 | -51.28542 | 2024-10-27 05:38:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c4b791e3-5f6f-366f-b82c-359b38654baa | 3.38628 | -51.28651 | 2024-10-27 05:38:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13d94ab2-614e-3758-a47b-7eec945e1b3d | 4.93772 | -60.2692 | 2024-10-27 05:38:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f27116e4-2002-3dab-a161-67d8760ed5e5 | 4.93543 | -60.27721 | 2024-10-27 05:38:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36818ecc-5402-3491-9141-6f17bb327548 | 4.93362 | -60.26589 | 2024-10-27 05:38:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80ce887d-25cf-3d15-bd88-d39a6f4facc2 | 2.90011 | -60.27269 | 2024-10-27 05:38:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 288b77c4-7ad2-3079-b6d1-f67cde04927f | 2.71825 | -61.49115 | 2024-10-27 05:38:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a61ab993-9a4b-3cc4-8d83-4f859649f434 | 2.30487 | -61.32883 | 2024-10-27 05:38:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60ab1135-8c06-3b65-b700-c38012495c79 | 2.30203 | -61.33314 | 2024-10-27 05:38:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 14e51c8c-53b5-3627-8971-fd0dffd79a0a | 2.29859 | -61.33365 | 2024-10-27 05:38:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f835d268-8a27-314d-9b70-44ad20e0729e | -0.11147 | -51.62706 | 2024-10-27 05:40:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 362fa84f-faad-38d9-8b54-bbb517ee985e | -0.10578 | -51.6207 | 2024-10-27 05:40:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README63.md)
