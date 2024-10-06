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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ceb813d7-7b59-3987-b024-7c56d7d994aa | -17.09591 | -56.80349 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 6fc65850-4689-3713-b18b-8bbfc03b631c | -17.09562 | -56.79737 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 48a1de88-b5cb-3994-9f6b-0442b72158ff | -17.09503 | -56.8016 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5cc473e5-fe26-334f-b826-37a8f6dce563 | -17.08938 | -56.79818 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 69aea79d-4c18-394c-aa72-d0eb4c45f5a7 | -17.08877 | -56.8024 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 79d91820-2624-31f9-bf26-a11dc427bc31 | -17.08817 | -56.80662 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 17ffddcb-6285-336a-8c51-ce1218a21757 | -17.08224 | -56.79707 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3daed6cd-6b3d-3d51-a633-dd097c4fa79f | -17.08043 | -56.80973 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| a29781a1-244a-3295-9197-c5c555ad7514 | -17.07686 | -56.80918 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 22264cc2-44be-3bf8-a011-0d0fc0d5dbe3 | -17.07329 | -56.80863 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| fed1aea2-cd49-3fd9-beed-e07d203db45c | -17.06973 | -56.80807 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 0e265056-3889-3bc9-a981-2e419fd3c866 | -17.06616 | -56.80752 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| fc50ee71-4f5c-34da-a80a-3719e5a87528 | -17.0626 | -56.80697 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 1d87d201-3947-3ddd-b566-88969685df21 | -17.05903 | -56.80643 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| b0e95449-3801-3c53-8f58-4a04f1759363 | -17.05309 | -56.79689 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c187a855-980b-3be2-bb22-5b678220a636 | -17.04476 | -56.80422 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 052977ee-f15b-3b3d-a104-096c02f81be0 | -17.04416 | -56.80844 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| f8b721b1-fe2a-3394-9249-2f6493dce84d | -17.04357 | -56.81266 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 780dc4e4-e9cd-3b2d-9a37-7da166f99ddd | -17.04297 | -56.81688 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 90a3cac1-2b7e-3475-844c-615b9720f64d | -17.04239 | -56.79523 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| ee0f1886-98ba-34cc-aea3-668b716bab8f | -17.04179 | -56.79945 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b02d721f-bd9d-30d7-9569-19982157656b | -17.04119 | -56.80367 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f2646d5a-7c80-3a8c-8983-b8b47605bfde | -17.0406 | -56.80789 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5666d93d-4fb8-3e5c-ac39-44c956f7d5eb | -17.03823 | -56.7989 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bd9fb532-4971-3fe8-a73c-c163017ca650 | -17.03763 | -56.80312 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2354a38c-9707-38dc-9aab-a80a6d4504df | -17.03584 | -56.81577 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| fdeb9850-3344-372b-994b-bfab8e1dc367 | -17.03525 | -56.81998 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 1d653e1f-b458-3e3c-8bc1-99475ff95275 | -17.02812 | -56.81887 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 31e27b90-b70b-330b-9459-c1a7df97b7a1 | -17.02753 | -56.82309 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 2449bb43-efd8-3cee-b249-7d4fed63b07f | -17.02337 | -56.82675 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| ad24fcb6-6e8c-3b00-a864-f14eecfdaca3 | -17.0204 | -56.82198 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 4ba25352-f05b-3a34-b2b9-10256131eebc | -17.01981 | -56.82619 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 5b228e3d-73e0-390a-b2a9-2eb3a2586b04 | -17.01625 | -56.82564 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 268f8df8-6e9f-3142-8657-a7fe45b6bb52 | -17.01328 | -56.82088 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| cdb80d9b-523f-38c8-981c-17ae2ccd4c30 | -17.01268 | -56.82509 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ba2428d2-c3fb-3a5f-b6bf-6ec196108565 | -17.00971 | -56.82032 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| e693e63a-8594-3fc8-b80c-8464efe1c71c | -16.99844 | -56.82288 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 490fd13a-ea69-3412-abc1-7fdb2e8a347e | -16.99366 | -56.80493 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 7c01513c-6d49-30eb-847c-3f08eff865af | -16.99307 | -56.80915 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| b7d33a74-d110-31e0-a4ec-3387eb27f9fb | -16.99249 | -56.81336 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 4d72db73-a283-3a03-9d8b-6eac2d33c948 | -16.9901 | -56.80438 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 88be21b3-efbb-3c49-acf3-e3e6771875ab | -16.99 | -56.81058 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| cf206654-5bec-394b-bb78-cea61fb573d2 | -16.98951 | -56.80859 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| c2b05d1c-4440-3034-adae-6d19c62776da | -16.98939 | -56.81478 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| eece68cb-c035-3107-958a-c56dd9685769 | -16.98712 | -56.79961 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7594460c-ced3-35f3-bf01-cd10aaedfe78 | -16.98653 | -56.80383 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 71427d33-e89b-3b51-bcec-80bc02e0d12f | -16.98536 | -56.81225 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 1c9b63dd-1e95-358b-861a-4def56d29ae3 | -16.98287 | -56.80947 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| ce9b31d4-6b41-3241-ac19-2c0255e91f30 | -16.97756 | -56.79575 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 6b5827cd-3aa4-37ba-8383-088b7fc093f0 | -16.97696 | -56.79996 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| c4585fe2-8da6-34c2-ae37-3463ba66c882 | -16.97635 | -56.80416 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 498947fe-6e3f-3651-9d03-c8243f3ccd85 | -16.97043 | -56.79465 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 93c3fd44-b447-32ff-aa8c-fdb0612ce0d3 | -19.14404 | -57.51391 | 2024-10-06 05:14:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 0a7a352b-19db-3c61-b68e-b14f90759502 | -19.13641 | -57.51678 | 2024-10-06 05:14:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c4d6e551-5065-3e63-80cd-9f5eda47c097 | -19.11411 | -57.4702 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c873a1c2-25e9-387a-b827-43780c151cd9 | -19.1135 | -57.47458 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a4fdd8e8-4b76-3ae8-8237-d56caaaf3e84 | -19.10997 | -57.47399 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| fbd5d643-11c0-33c7-a80d-5f545e11a99b | -18.88351 | -57.69399 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 2bf0c99a-b9c9-313c-912b-5794f91ecdef | -18.88233 | -57.72715 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 5c34606a-ecb3-3553-b753-97f6e16ee831 | -18.70291 | -57.28669 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 45f82568-239a-3ff2-8c0a-54e34bff24aa | -18.70114 | -57.27348 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3b612ba4-3ab4-331a-9ecb-fd6c30292f2d | -18.69759 | -57.27291 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| fee39b21-d082-35d2-add5-6c330ec682f8 | -18.69462 | -57.26814 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 778ff493-76e3-3829-8802-a175d39733d3 | -18.65577 | -57.26393 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.4 |
| 06fb0fa4-49c6-32c1-8a1b-b0f0429f4570 | -18.65555 | -57.262 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.3 |
| 10bc6b66-e46e-32cf-9999-d5cc150c6e1c | -18.6551 | -57.29395 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 256bf14b-e7a7-3d40-af1a-6b350de8d5da | -18.65497 | -57.26622 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| e1f19c8e-41d6-3034-8f90-07ad4b5f34af | -18.65444 | -57.29628 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 6899dfe1-20b0-3304-b8e1-42f6f6f4e6b6 | -18.65222 | -57.26337 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.0 |
| d17ec90a-743b-396c-8b49-b480e2feba5b | -18.65162 | -57.26759 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.2 |
| 73efdb95-08b2-39a2-b693-8813167038cc | -18.65102 | -57.2718 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.2 |
| eadaa9e3-45aa-357f-9283-f1597726cb01 | -18.64807 | -57.26703 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.2 |
| 75ad4f73-7d13-3978-9a05-e7c301f2bf13 | -18.64801 | -57.29284 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 61cc601e-6fe7-33db-9eb5-8d87a776cd1c | -18.64747 | -57.27124 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.2 |
| 33993f63-6f3a-31fc-bd65-d2d3fa7aaab6 | -18.64687 | -57.27546 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d69f5b12-6d93-36dd-ace2-79f814f27501 | -14.86692 | -58.02949 | 2024-10-06 05:14:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f613304-c2ac-3cd3-92d5-49b499585348 | -14.86412 | -58.02521 | 2024-10-06 05:14:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba5f5a98-e91e-3516-b5a4-f77a7611fcb4 | -16.54831 | -58.21386 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a0195cea-44f7-384a-865c-edd05212b8ca | -16.54775 | -58.21759 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3ec7013f-15f8-3906-a2ea-cdd099a8e85b | -16.54045 | -58.22025 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| de7df05c-9eef-3490-a73a-5caf40cee7c7 | -16.53989 | -58.22397 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 94f9aa9a-9307-3680-8fa8-7f54b296d98b | -16.54157 | -58.21279 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d1481e1c-ba17-3c73-b17f-a8950af594ae | -16.5382 | -58.21224 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e88760b8-a3b3-3339-a5f6-ebbf82767ea1 | -15.26898 | -58.20097 | 2024-10-06 05:14:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c90482f-89b2-3740-baa8-065ba83fc069 | -12.32345 | -59.2136 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0f0d346-bcf4-3257-96ac-5763cb75c524 | -12.31017 | -59.23313 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 56acbeaa-7a46-3581-b807-50e9c92f201e | -13.12305 | -60.14865 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6f98228-035d-38c3-af72-cbcae66525b7 | -13.11971 | -60.14805 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 993dcb4c-1445-35f6-8aec-5d1116cbc083 | -12.97582 | -60.09377 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4324a0bf-cdf7-398b-aaf3-684720f51873 | -12.97307 | -60.08959 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42b3efa1-4524-3cb7-810d-c2d1e6ced803 | -12.97248 | -60.09321 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c118a678-daea-34b2-bf1c-8912f75b4d2d | -13.14822 | -59.6987 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e4a07bb1-fbe4-3246-8a16-ede67928f521 | -13.14766 | -59.70225 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d52d2a1-93d2-3c0e-892e-85d47521bfd8 | -13.14709 | -59.70581 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13175e5a-ee35-306e-9726-4e3b78bc501c | -13.14547 | -59.6946 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 386e6be1-7cfe-3c6d-bd2d-f6bd37ae3c4b | -13.14491 | -59.69815 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba8d8aaa-b845-3f5e-ba46-0dcafd42954e | -13.14434 | -59.7017 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2e07da9-0103-3351-914b-679705dde70c | -13.14159 | -59.6976 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aba490b8-b935-3de3-9d04-afd5c08f351a | -13.14102 | -59.70115 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0073fcf3-9a8b-3af7-9efe-7f099fb57805 | -13.05889 | -59.83039 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README127.md)
