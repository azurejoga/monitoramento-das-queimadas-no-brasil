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
| 436122f6-e77a-3105-ac2b-8e4623d4e673 | -3.7248 | -43.7663 | 2025-12-14 00:18:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4295c13-9739-3384-bf0a-d6d08e831e43 | -2.0935 | -45.292198 | 2025-12-14 00:18:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5ffc1fe4-485b-3f47-a4ce-42873f4aa606 | -5.3948 | -44.68 | 2025-12-14 00:18:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73bf7e72-52f8-3705-916b-fe1d73a5016d | -8.0275 | -43.1092 | 2025-12-14 00:18:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1d6f7bdb-a675-38e0-9f5b-58f57042590b | -7.0128 | -38.5373 | 2025-12-14 00:18:00 | METOP-C | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| b19abc7d-2e68-3054-adf2-559bf853632e | -4.6989 | -43.245499 | 2025-12-14 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cfe36f26-3433-310d-b8c1-d13645d6b37d | -5.6806 | -39.278702 | 2025-12-14 00:18:00 | METOP-C | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| fe1e19a8-6b19-3a7c-a87b-0646f71acd31 | -1.1397 | -46.756199 | 2025-12-14 00:18:00 | METOP-C | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acc0520c-71b9-38f6-a8d0-187c41578ddf | -3.3096 | -42.537601 | 2025-12-14 00:18:00 | METOP-C | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ad998cf-246a-3ec1-be17-796fd2302b83 | -5.4358 | -41.241699 | 2025-12-14 00:18:00 | METOP-C | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 625c360d-4f4c-32ff-b45f-697339ff1a14 | -3.6201 | -45.6656 | 2025-12-14 00:18:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7cd23053-c2c0-3f0a-87d5-ffce1e581b8a | -4.6891 | -43.2477 | 2025-12-14 00:18:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a7ea400-2167-30a3-ae5b-fa5b1a8a46d5 | -4.935 | -43.966801 | 2025-12-14 00:18:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0cbe18c2-e070-3b16-a67f-a2ed97523932 | -3.6237 | -45.6814 | 2025-12-14 00:18:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 41404cc6-6fc9-3eef-8ab5-cb4c8d36fc9e | -3.8826 | -42.516998 | 2025-12-14 00:18:00 | METOP-C | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6cc1286b-d724-3ded-a3a9-8c7664afc41b | -2.851 | -45.4067 | 2025-12-14 00:18:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d478241e-3c17-3ab2-9e42-c341a7dbb196 | -3.7346 | -43.764099 | 2025-12-14 00:18:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b489a35-ea87-3a24-b9ae-080879d87ef9 | -2.2861 | -45.5952 | 2025-12-14 00:18:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ad4fee79-6105-34f8-ad66-654d45a22e3f | -8.0795 | -43.156898 | 2025-12-14 00:18:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2aa7f371-634e-3c73-9a20-4b6bbc7e6b5e | -8.0779 | -43.149899 | 2025-12-14 00:18:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 49bc84ef-425d-32d9-b04b-f6fae7a1e18f | -3.733 | -43.757099 | 2025-12-14 00:18:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 946b9902-a3b6-3f86-a82b-39308af5f3ea | -1.1416 | -46.7645 | 2025-12-14 00:18:00 | METOP-C | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e5dfe9e-6605-3662-b5e2-ced309b3a6a0 | -2.8417 | -46.728401 | 2025-12-14 00:18:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24b2f3ca-cdb8-3812-bf81-ec10fbd7c3ec | -6.5808 | -38.937401 | 2025-12-14 00:18:00 | METOP-C | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1f472e5e-d628-3ecf-9a72-2ad28cdb9827 | -2.4778 | -45.441601 | 2025-12-14 00:18:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e7fd7725-db8e-303f-b406-18a2953575cf | -2.0918 | -45.284901 | 2025-12-14 00:18:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 10aee9b5-1b92-38bf-ab55-25ab6b40caed | -3.308 | -42.530701 | 2025-12-14 00:18:00 | METOP-C | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00856ce9-fadc-326e-a26e-52c08dd37818 | -2.8825 | -44.956001 | 2025-12-14 00:18:00 | METOP-C | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 83680806-0338-3338-a277-e24742300fbe | -2.2152 | -45.6908 | 2025-12-14 00:18:00 | METOP-C | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 52fa2f31-18c9-3a5b-93e4-9f2315f11827 | -1.4446 | -46.287102 | 2025-12-14 00:18:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e6c9c2a-e857-3439-b351-5c6927825384 | -3.4338 | -41.642101 | 2025-12-14 00:18:00 | METOP-C | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4bf37295-40b9-3b97-b6cd-df8853702320 | -4.9318 | -43.952702 | 2025-12-14 00:18:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cb834cb0-cbee-3a9b-aad9-c796e0b3e368 | -5.0055 | -42.781799 | 2025-12-14 00:18:00 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a69571fc-ec82-380e-9c1d-a7170d919785 | -3.503 | -41.9874 | 2025-12-14 00:18:00 | METOP-C | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d315d5dc-4309-344b-bf9b-a76e95da80e0 | -2.2826 | -45.580002 | 2025-12-14 00:18:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 69ec4319-ce2e-335f-88c1-892833f0e911 | -3.6597 | -41.995899 | 2025-12-14 00:18:00 | METOP-C | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8ca7e30e-f469-31cf-a7c8-e0015d762a0e | -3.7314 | -43.750198 | 2025-12-14 00:18:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c989755-ded9-37d0-9513-bc1282f036bd | -8.0326 | -43.0858 | 2025-12-14 00:18:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 37de2f78-20c1-398e-8f7f-ba70394a9e90 | -2.8319 | -46.730598 | 2025-12-14 00:18:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0c8dcff-7989-3812-9d40-cd85eb986878 | -5.6689 | -39.272598 | 2025-12-14 00:18:00 | METOP-C | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 90f50b57-5114-3e17-9a50-bed8454152c0 | -8.0763 | -43.142799 | 2025-12-14 00:18:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 427211f5-141f-3802-805b-3df279cd8d6d | -3.7134 | -43.761398 | 2025-12-14 00:18:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7002b028-7355-3f7e-bb3d-341952fa75b1 | -5.6708 | -39.280899 | 2025-12-14 00:18:00 | METOP-C | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2caba1ee-edcc-3a2c-9d85-e0ca0e01cf21 | -3.7216 | -43.752399 | 2025-12-14 00:18:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d8732f7-ff5c-3df4-bfa5-8ed19d3ebb76 | -1.4544 | -46.284901 | 2025-12-14 00:18:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2a692bc-55af-37c1-874d-5f7fc8788099 | -3.6581 | -41.988998 | 2025-12-14 00:18:00 | METOP-C | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bd82d68f-b892-3025-8040-862870232620 | -8.0244 | -43.0951 | 2025-12-14 00:18:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9b660d47-ce64-3c07-adaf-54d7186f54b5 | -3.72 | -43.745499 | 2025-12-14 00:18:00 | METOP-C | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 11813025-8783-3432-adc2-282e19c957c9 | -2.2906 | -45.5933 | 2025-12-14 00:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 46.5 |
| f03cc2b7-36f1-32ca-96fe-fdec38dd64db | -2.272 | -45.5938 | 2025-12-14 00:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 03925108-15b9-39a6-b739-5de4ee9e0d86 | -2.0768 | -56.4674 | 2025-12-14 00:20:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| e428ad43-73ff-3ff7-bbec-0788b43668e3 | -3.5186 | -48.9201 | 2025-12-14 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 57c00780-c3d4-37e9-b41a-31ef5dedd602 | -16.2188 | -58.8414 | 2025-12-14 00:20:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| 43764c7e-b8ed-3e3e-b069-31b48ebec9d0 | -5.6797 | -39.2841 | 2025-12-14 00:20:00 | GOES-19 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 67.9 |
| 1cbcaab1-5921-3899-a5bd-c7c4e0e58bf3 | -8.0696 | -43.1452 | 2025-12-14 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.9 |
| 5f12b525-42dd-32a8-a3dc-afceee7997a8 | -8.0324 | -43.1022 | 2025-12-14 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 125.7 |
| 641aba31-b6f6-35fe-b52a-259a7761ef1d | -5.68 | -39.259 | 2025-12-14 00:20:00 | GOES-19 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 68.8 |
| 7119ea39-41f7-3022-b852-157957b7054e | -2.8485 | -45.3963 | 2025-12-14 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 4cdf171b-c4e3-361d-be14-6e291cb78714 | -3.4451 | -41.6413 | 2025-12-14 00:20:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| c6a9df77-37dd-30d4-b796-0493e7a76c2d | -8.0327 | -43.0786 | 2025-12-14 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.8 |
| da8887b6-a5b5-3945-bddb-22038fb45657 | -8.0513 | -43.1001 | 2025-12-14 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.9 |
| 9a19a256-bce3-3b82-a9bd-d05627c3e394 | -16.2383 | -58.8395 | 2025-12-14 00:20:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 66.3 |
| 590708b4-d430-3aa6-83d4-0d3d3793a426 | -3.6277 | -45.6797 | 2025-12-14 00:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 5607c593-4883-337c-a74e-46266646b577 | -2.1425 | -45.4628 | 2025-12-14 00:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 05d3ffa9-6877-35ac-821a-cfa1899405eb | -2.2906 | -45.5933 | 2025-12-14 00:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 1f477054-de02-33cc-bab5-a60321853983 | -1.5296 | -45.678 | 2025-12-14 00:30:00 | GOES-19 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 871fbc11-8d55-383a-a3f3-69e3bb556de0 | -8.0513 | -43.1001 | 2025-12-14 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.7 |
| 25cf8287-a7b5-34a6-ac16-acaafa68ec3d | -16.2383 | -58.8395 | 2025-12-14 00:30:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 68.9 |
| 75a828d5-cb47-32d4-935b-c68c1a47bbf8 | -8.0324 | -43.1022 | 2025-12-14 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 138.5 |
| f529a9f1-47eb-3740-942f-0ce5b5e2ca59 | -3.4451 | -41.6413 | 2025-12-14 00:30:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 60.1 |
| 4a027e5f-0505-3ba6-b636-ef5d0651224e | -2.1425 | -45.4628 | 2025-12-14 00:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 44.6 |
| be8e50d3-4015-367e-bb14-3276119a5718 | -5.68 | -39.259 | 2025-12-14 00:30:00 | GOES-19 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 77.2 |
| 0f1ea43d-6d65-314b-9d95-b93fe54d5ed0 | -3.5371 | -48.9195 | 2025-12-14 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| c0ae33b4-fd13-373f-9229-6f2977830ef3 | -5.6797 | -39.2841 | 2025-12-14 00:30:00 | GOES-19 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 67.6 |
| d0eb237b-78d8-3a0a-a1e1-137a86ac304d | -2.8875 | -44.9666 | 2025-12-14 00:30:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| a3f05f49-667e-3b45-82ed-45adb7ee489e | -8.0327 | -43.0786 | 2025-12-14 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.7 |
| 9184395b-cffe-3f89-93ee-cc7d1c1ad2c4 | -3.6277 | -45.6797 | 2025-12-14 00:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 76.0 |
| bda6036f-2781-3e72-b6e2-a82d12ab4659 | -8.0696 | -43.1452 | 2025-12-14 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 237c5d6a-ced9-3f99-a658-e324703ce445 | -16.2188 | -58.8414 | 2025-12-14 00:30:00 | GOES-19 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 9092ac90-8fc4-3556-99fa-49053b94f152 | -3.62061 | -45.68329 | 2025-12-14 00:32:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 22.7 |
| eea27736-2f10-3115-a4ec-1c9db07c947e | -8.0648 | -43.15714 | 2025-12-14 00:32:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 37.6 |
| d5d91d3d-cf95-3ede-a0cf-c6bf43080cf4 | -3.88881 | -42.53107 | 2025-12-14 00:32:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 36.7 |
| 4917e5f3-dd5a-3492-860f-7e9dd5963abe | -3.72485 | -43.75902 | 2025-12-14 00:32:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 215437a7-927b-33a0-8441-f76e7007fa05 | -3.62997 | -45.66491 | 2025-12-14 00:32:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 9a3a16e2-df9c-3487-80d3-db2114396548 | -8.04442 | -43.11535 | 2025-12-14 00:32:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| a2a96969-7939-3699-9c7b-58f468f79f0e | -4.69851 | -43.24586 | 2025-12-14 00:32:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 171d7b68-c2a3-35e5-8a2e-4ca1d401fbd2 | -3.67496 | -44.82255 | 2025-12-14 00:32:00 | TERRA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 23879601-a2c9-3ad6-ba60-3839ac20fd22 | -4.10064 | -48.96263 | 2025-12-14 00:32:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ec53aba8-1085-3925-918d-ee6b69341e61 | -3.71564 | -43.74277 | 2025-12-14 00:32:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 5bc7d1d4-8b61-3fa8-9610-14cd5cf24587 | -8.02741 | -43.09523 | 2025-12-14 00:32:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 112.3 |
| b31e7958-5d78-3c89-a9bd-c9b23c6b767c | -3.71902 | -43.76627 | 2025-12-14 00:32:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 12467402-d483-3ed9-9110-a491a992b96c | -3.63245 | -45.68155 | 2025-12-14 00:32:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 8f0f23de-c540-3f68-be45-df9ff9fe5fb0 | -8.03097 | -43.11752 | 2025-12-14 00:32:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.1 |
| c7040d99-4665-3a94-b98d-c8b516f1cb6a | -8.07824 | -43.15524 | 2025-12-14 00:32:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 49.5 |
| 79f30d00-d408-38d6-8824-47c82511dbf2 | -4.34011 | -43.62829 | 2025-12-14 00:32:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| f1db7641-00c6-3c01-ab6e-a56f26218d01 | -4.68436 | -43.24812 | 2025-12-14 00:32:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| cf5811d6-a4cd-32f1-b58b-8d76991e111a | -9.87227 | -50.56385 | 2025-12-14 00:32:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d5f36024-3e44-39db-bc50-6498c5907d70 | -3.7213 | -43.73553 | 2025-12-14 00:32:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 696ff2f7-c333-3a31-a2c9-1795bb6620f9 | -4.10994 | -48.9613 | 2025-12-14 00:32:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b4437211-e85d-3186-8e2b-51ae86c3f545 | -3.62617 | -45.68911 | 2025-12-14 00:32:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |


[Clique aqui para ver as próximas entradas](README3.md)
