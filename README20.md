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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e729ce3-53b0-36c1-b6c1-7346a4847974 | -11.9824 | -63.9022 | 2024-10-25 03:06:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 5e46da77-8f36-3d70-b4c5-dcd58fd4a321 | -12.478 | -63.1693 | 2024-10-25 03:06:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| a8a657cb-4bd8-3079-a569-e97d9c465648 | -12.4591 | -63.1704 | 2024-10-25 03:06:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 2c183bfa-31c1-3633-9881-4cae028afc96 | -12.3783 | -63.863 | 2024-10-25 03:06:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 50.0 |
| b1bb9b6b-eeac-3505-8a1f-8b70e142ccfe | -12.3782 | -63.8821 | 2024-10-25 03:06:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| d311720b-2b1f-3ec8-b95c-0c84c5de9d16 | -12.4589 | -63.1895 | 2024-10-25 03:06:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 54165e94-c857-3d56-bd69-6f43e37c1451 | -17.0586 | -57.4517 | 2024-10-25 03:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.5 |
| feb9b124-51f8-369d-a0fe-db0d739f5ace | -17.039 | -57.454 | 2024-10-25 03:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.0 |
| 84703b98-0025-394b-95d5-34fd4a978131 | -17.0381 | -57.5155 | 2024-10-25 03:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.5 |
| 22f81c43-4836-341b-b87c-b15f035ce4c6 | -17.0014 | -57.3561 | 2024-10-25 03:06:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 26109707-bddf-3442-a57c-06ec66a05012 | -16.9792 | -57.5223 | 2024-10-25 03:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.8 |
| c0654a82-0f6b-3dfc-8a51-088f49dd3669 | -16.9596 | -57.5245 | 2024-10-25 03:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 137.7 |
| 74f5ca87-869d-372b-a131-685031936bc5 | -17.2537 | -57.5108 | 2024-10-25 03:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.4 |
| 1ddedad4-3bae-3a13-87e2-6821fe114878 | -17.2386 | -57.2256 | 2024-10-25 03:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.5 |
| 6ee5a5e8-e78f-30aa-b2b9-d28f3b3fcc3c | -17.7671 | -57.3673 | 2024-10-25 03:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.8 |
| 23d0d683-aef7-3d11-a137-4ad3c3312130 | -17.7644 | -57.532 | 2024-10-25 03:06:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.9 |
| 49d96d4b-8e8f-3d6f-8064-d70b04c09eb8 | -17.9473 | -57.2009 | 2024-10-25 03:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.8 |
| 8443b260-c31b-3ded-a5ad-73e25a4ae2ae | -17.9071 | -57.2472 | 2024-10-25 03:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.4 |
| a50bf668-ad37-3888-a42f-449f8f539c37 | -17.9268 | -57.2447 | 2024-10-25 03:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.8 |
| 588029e1-9a13-334e-a269-37576fad9dea | -17.9272 | -57.224 | 2024-10-25 03:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.3 |
| 8d776302-aa3b-3905-9a36-09ddcdc71fa6 | -18.0438 | -57.3332 | 2024-10-25 03:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.8 |
| 207f1b84-90d1-33a7-b3da-6e7123883c39 | -18.0441 | -57.3126 | 2024-10-25 03:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.8 |
| 2a8908c3-2e00-3d51-9257-da0b62501892 | -18.3004 | -56.2222 | 2024-10-25 03:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.6 |
| 2547aa68-fd33-3db3-ba03-eacbaf35853f | -18.3199 | -56.2404 | 2024-10-25 03:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.5 |
| b5ad22f7-c24b-3e01-b365-d6c118f83553 | -18.3203 | -56.2195 | 2024-10-25 03:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.2 |
| 39ebae6e-31a0-37a9-8a3c-71758bfa38f6 | -18.3398 | -56.2377 | 2024-10-25 03:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.2 |
| 948f8e42-86c5-312b-8931-c5bce06137d8 | -18.3401 | -56.2168 | 2024-10-25 03:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.2 |
| 37d10d29-03c3-3df6-bf0e-b68d4343474c | -1.0445 | -47.6237 | 2024-10-25 03:15:11 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| c2449afd-a0a2-30bb-a18b-b4dabc94a1dd | -1.1834 | -53.6569 | 2024-10-25 03:15:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 6f61373d-a3dc-32c3-a058-a462bfa878a9 | -2.796 | -49.2424 | 2024-10-25 03:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 4d353b87-610d-3d61-a015-45e20a207784 | -2.8145 | -49.2418 | 2024-10-25 03:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 566b0cb6-ff7d-3396-aeb4-224e406f4594 | -3.2135 | -46.8063 | 2024-10-25 03:15:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 173.7 |
| 70534da1-56c4-3d06-a601-7d2e188f175d | -3.2136 | -46.7843 | 2024-10-25 03:15:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 46587a67-98a0-3263-8bfd-7ebc06bb37f7 | -3.9581 | -46.422 | 2024-10-25 03:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 62.2 |
| bdd0f622-f19a-3cde-9fd7-9252acee0d06 | -4.2429 | -48.5474 | 2024-10-25 03:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 0c92be52-5c65-3640-849a-b643ba6c4588 | -4.5045 | -48.2117 | 2024-10-25 03:15:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 5622e7fb-a6ff-3cf4-adbd-f85fbb1c0117 | -5.9788 | -45.3621 | 2024-10-25 03:15:39 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 1a849a09-f3c1-3994-ae4e-f49c59847502 | -6.5219 | -60.0457 | 2024-10-25 03:15:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| e069239b-6ad4-307c-aa50-e81a7de8a52a | -12.0012 | -63.9013 | 2024-10-25 03:16:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| b249c910-ad67-3ba3-9fb1-dc783d611efc | -12.4589 | -63.1895 | 2024-10-25 03:16:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| d8220a28-135c-3144-8486-fee997f31fd1 | -12.4591 | -63.1704 | 2024-10-25 03:16:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| f949dc9f-e3e6-369b-b0ea-1d0a46861492 | -16.94 | -57.5268 | 2024-10-25 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.7 |
| 2d2b064f-61ca-3cdd-86bc-6a9ceb9ac705 | -16.9596 | -57.5245 | 2024-10-25 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.6 |
| 7e8adc87-ba52-3ce9-a42a-6cf3e4907cf8 | -16.9792 | -57.5223 | 2024-10-25 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 141.6 |
| 3cff71b5-b83e-3e8d-a6bd-b60ade21d348 | -17.0184 | -57.5178 | 2024-10-25 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.3 |
| ec23ef3b-d61e-359d-9965-6c20fe75ddb3 | -17.0381 | -57.5155 | 2024-10-25 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.3 |
| bc8f0c3a-6e06-35c3-aaf3-92f817a81d34 | -17.0586 | -57.4517 | 2024-10-25 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.5 |
| d16c79e9-7577-34fb-9d15-3476251928fb | -17.2186 | -57.2485 | 2024-10-25 03:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.7 |
| 4aa01cd3-9191-31a9-982f-6ae07b39eff7 | -17.219 | -57.228 | 2024-10-25 03:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.4 |
| 4e356093-30fa-3916-a6de-5561e9fb3539 | -17.2386 | -57.2256 | 2024-10-25 03:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.7 |
| 5804e4ea-7ddb-3e44-88ac-fafaf0e544a1 | -17.2537 | -57.5108 | 2024-10-25 03:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.4 |
| c139c20a-1185-3287-a31d-014f211c7ff9 | -17.9272 | -57.224 | 2024-10-25 03:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.9 |
| 11fd1c40-66a5-3163-b4f5-8d7d09bab393 | -18.0441 | -57.3126 | 2024-10-25 03:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.7 |
| 47866012-849d-3358-a775-2c1f5733631f | -18.0639 | -57.3101 | 2024-10-25 03:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.9 |
| 794fb5b7-4899-3450-bd57-402cadb64c1c | -18.3004 | -56.2222 | 2024-10-25 03:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 77f9c80c-a4d5-38a8-b5df-3d7ead534318 | -18.3199 | -56.2404 | 2024-10-25 03:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.6 |
| 166d02ba-dfb2-3357-b383-20fe78a1dda4 | -18.3203 | -56.2195 | 2024-10-25 03:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.5 |
| 396399e3-f805-3754-aa69-0755531f519e | -18.3398 | -56.2377 | 2024-10-25 03:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.7 |
| f494a85d-16a4-3c95-8013-386888913827 | -18.3401 | -56.2168 | 2024-10-25 03:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.9 |
| 8814718d-a1eb-31be-84c1-b0ec90fbc5d5 | -3.89216 | -41.04101 | 2024-10-25 03:19:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 932c418c-fb1a-3017-b5cf-93c8dc5b9478 | -3.89152 | -41.03984 | 2024-10-25 03:19:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 0a934f54-70c5-317f-9822-d3c987a744f0 | -3.89133 | -41.04572 | 2024-10-25 03:19:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 2d5b3ca1-6af4-370e-84eb-ce4a42679032 | -3.89073 | -41.04456 | 2024-10-25 03:19:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 16921393-b073-312e-acbe-fda22e1ad97e | -3.06258 | -40.04464 | 2024-10-25 03:19:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 66439550-d6ad-3c0c-a738-7a41026f3854 | -11.13445 | -40.19471 | 2024-10-25 03:21:00 | NOAA-20 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 518ac6d0-54fb-372d-85d5-64c73d12aeca | -10.8975 | -44.31604 | 2024-10-25 03:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2fc134cb-3a50-30ab-a270-bc085bc292e6 | -10.87221 | -44.78966 | 2024-10-25 03:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| cfa0f802-714a-3607-9d58-880fa2682fc3 | -10.87092 | -44.79584 | 2024-10-25 03:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| dd568334-e070-3a5e-bfe2-705b2b58c3ce | -10.87014 | -44.79352 | 2024-10-25 03:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9cbdbad4-a942-36fe-9de4-72a948750d1b | -10.86962 | -44.8021 | 2024-10-25 03:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f354dc40-75e8-3406-86bc-23cfdc75eb3f | -10.86888 | -44.79979 | 2024-10-25 03:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1b5eff19-2ff7-3bfd-955d-774506817024 | -10.86545 | -44.78815 | 2024-10-25 03:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| aa5f2210-390b-3586-98d0-f51250280271 | -10.86414 | -44.79442 | 2024-10-25 03:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 77549bd5-2a6a-3796-b41e-ce5a5c132a5f | -10.86337 | -44.79206 | 2024-10-25 03:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ba7125be-302a-3efe-b3a4-755499c18127 | -10.86283 | -44.8007 | 2024-10-25 03:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bde8a2df-5151-37b8-9217-e4e6dc77f750 | -10.86209 | -44.79837 | 2024-10-25 03:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 39c62ec9-6ba1-3460-8ddb-97fa96f80c74 | -10.58717 | -44.29187 | 2024-10-25 03:21:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 829b6ebd-671b-3799-9265-e0702b0847fe | -10.58387 | -44.28881 | 2024-10-25 03:21:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e977ca8e-0192-30be-a80b-560702775b97 | -10.58271 | -44.29471 | 2024-10-25 03:21:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5ea38883-c2ed-3f4d-a597-93efc9b239f6 | -10.58173 | -44.28468 | 2024-10-25 03:21:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4488a6d4-1bd8-3077-9acf-355db0a6ea5c | -10.58055 | -44.29044 | 2024-10-25 03:21:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 78155734-3b45-3894-b4dc-0f93b48dd9bb | -10.57726 | -44.28734 | 2024-10-25 03:21:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dbe34574-57a1-3fd5-a6ef-342eb7eb9eb2 | -10.51015 | -42.39627 | 2024-10-25 03:21:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e2818e6e-b8e4-3333-8a34-3b53d79979f3 | -10.50928 | -42.40068 | 2024-10-25 03:21:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c2f38fd6-b40c-313d-b00c-a1f00e791c49 | -10.25712 | -36.57394 | 2024-10-25 03:21:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| a7671e32-065b-338f-8c53-f3428c0515c3 | -10.08179 | -36.52377 | 2024-10-25 03:21:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| cb039cba-4a14-3405-af6e-2b0650fe547a | -10.08115 | -36.52737 | 2024-10-25 03:21:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| b5038543-6bc9-3110-a446-be04df761727 | -10.00996 | -36.38397 | 2024-10-25 03:21:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| d20bf1c5-a876-3522-915a-249f15c7b76f | -10.00933 | -36.38755 | 2024-10-25 03:21:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 48220fe9-ab14-34b9-9c27-b40349ed9d36 | -9.97215 | -36.02312 | 2024-10-25 03:21:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5a362bca-e59a-3d1d-a107-62d34cac727a | -9.96821 | -36.02243 | 2024-10-25 03:21:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3c398adf-7d1c-3446-99c1-e7af47371450 | -9.84879 | -36.44525 | 2024-10-25 03:21:00 | NOAA-20 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 992df78a-fbb4-3daf-ad66-51752c5e7cd5 | -9.56191 | -35.69311 | 2024-10-25 03:21:00 | NOAA-20 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9cf8b8cf-c878-30d7-8408-45e13b3f0365 | -9.53399 | -40.33994 | 2024-10-25 03:21:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| f8ccf1d6-a603-3682-9ee3-60c860c8672f | -9.5287 | -40.33892 | 2024-10-25 03:21:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 09294c56-b3a8-3024-8479-c6d67f59635a | -9.52746 | -40.3456 | 2024-10-25 03:21:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 77b88ba4-29cc-3f9c-b6b7-29baffb0dde5 | -9.37717 | -38.30516 | 2024-10-25 03:21:00 | NOAA-20 | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 78790656-6bb0-3918-997b-d8535feec629 | -9.35372 | -43.37261 | 2024-10-25 03:21:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6df89d0e-941d-3434-8809-b6eb3f1c5e2e | -9.3527 | -43.37796 | 2024-10-25 03:21:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ea623abb-45b4-3aa8-ab7d-def740d1c8bd | -8.79263 | -44.72594 | 2024-10-25 03:21:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README21.md)
