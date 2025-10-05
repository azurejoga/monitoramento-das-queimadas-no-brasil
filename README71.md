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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2943caca-8718-3721-8cea-6ff3ae71c177 | -8.5956 | -46.2798 | 2025-10-05 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 8bf7e2cd-5387-35c3-a2e0-2358b941fc40 | -10.6572 | -46.3146 | 2025-10-05 04:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| e657ce2b-dad6-3167-b3cd-4556daf2e30b | -10.6568 | -46.3372 | 2025-10-05 04:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 293.8 |
| 39b5581e-015e-39b2-8825-248a490962f9 | -6.1536 | -44.6675 | 2025-10-05 04:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 285.9 |
| 4dd9d174-9b59-32ae-a16b-2cb73acd3887 | -6.1538 | -44.6446 | 2025-10-05 04:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 198.2 |
| 87ab2f1c-1d89-3fd0-869a-4aed3b4b768b | -4.4445 | -43.2397 | 2025-10-05 04:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 670f4530-332c-313a-917e-86442f872b59 | -8.5573 | -46.3285 | 2025-10-05 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| baeec490-6f0b-37e4-9166-4404f3b56c02 | -18.3345 | -45.8734 | 2025-10-05 04:00:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 108285c2-070c-38c2-94e8-931798d878b7 | -6.1349 | -44.6689 | 2025-10-05 04:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 5ef219c5-52ba-3730-9717-af0d894e0f4d | -10.6382 | -46.317 | 2025-10-05 04:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 1e3166a4-b4df-3956-b45f-f8ef473f79ca | -10.6375 | -46.3622 | 2025-10-05 04:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 23a6ed32-539f-3da5-be9e-82faaafd54d6 | -8.5953 | -46.3022 | 2025-10-05 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 165.8 |
| e4c1bf94-f217-36d7-873c-e29529658e50 | -5.7762 | -42.9372 | 2025-10-05 04:00:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 64.6 |
| 26c43aa3-f41c-3f25-9323-7df8920e86d4 | -14.3353 | -47.6755 | 2025-10-05 04:00:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| d114e32c-69c7-3966-9710-a3bfd95caf78 | -8.5761 | -46.3266 | 2025-10-05 04:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 391.5 |
| 95702f54-50a5-32bf-8072-842ac89168e5 | -10.6565 | -46.3598 | 2025-10-05 04:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 5aa995a1-de70-3a90-b9a8-abc67b6ba162 | -6.1723 | -44.666 | 2025-10-05 04:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 7bc3170b-24b2-377b-a409-4e57a11888cd | -5.7764 | -42.9137 | 2025-10-05 04:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 147.9 |
| f0111b9b-0b87-30ca-8492-167b41ffbb78 | -14.3353 | -47.6755 | 2025-10-05 04:10:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 62.2 |
| b14912e8-555d-3abe-af41-b728439055fd | -4.6318 | -43.1816 | 2025-10-05 04:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 47b4676c-40cd-3cf3-b4f7-63f9e00ebfed | -4.6505 | -43.1805 | 2025-10-05 04:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| d7919393-b638-3e35-ae9c-8903c2c07269 | -8.5761 | -46.3266 | 2025-10-05 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 650.6 |
| 94ebc303-032f-34df-8fb3-9d227917f8a3 | -18.3345 | -45.8734 | 2025-10-05 04:10:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 8657a913-5528-34ef-9e4e-b1f020fc517a | -4.8222 | -42.7477 | 2025-10-05 04:10:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 56.9 |
| f7d40721-62d5-3f0c-bdcc-a416c073d96d | -5.7762 | -42.9372 | 2025-10-05 04:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 231.1 |
| fcc72ae0-edd1-382a-91cb-8c8cf28d24e1 | -8.5956 | -46.2798 | 2025-10-05 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 62a6a7a2-4749-3ca7-b421-a1dd7837dfb8 | -8.5947 | -46.3471 | 2025-10-05 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| c4d02268-ca7e-31be-aacc-574a96f20616 | -8.5764 | -46.3041 | 2025-10-05 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 282.5 |
| a24255ee-76e9-3c59-b95e-09f1a481ec09 | -8.595 | -46.3246 | 2025-10-05 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 331.9 |
| 2657188d-db03-3b3b-bb11-934c912af1c0 | -8.5759 | -46.349 | 2025-10-05 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 8d08f8d9-d6e6-3ccd-b616-f14d3e16fe6f | -4.822 | -42.7712 | 2025-10-05 04:10:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 589c84af-0496-3689-83ff-79fc3063ceba | -5.8891 | -42.9048 | 2025-10-05 04:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 62.4 |
| 14b1b797-e864-3efd-b758-56610cff7572 | -13.2934 | -47.6129 | 2025-10-05 04:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 8f73b0a6-1f50-31f2-a94e-271a688dc709 | -11.8777 | -56.8769 | 2025-10-05 04:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 9818f1ea-02ef-3bea-9690-04c3070198ea | -10.5863 | -54.36 | 2025-10-05 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 944c5c4a-3224-30da-99fe-58e4e7ac0b61 | -8.5953 | -46.3022 | 2025-10-05 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 221.4 |
| 7ce272b0-0c78-3fff-8572-3a1d03a9309d | -15.6015 | -52.5102 | 2025-10-05 04:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| c23a51a7-d905-3c66-9826-fe82cae18271 | -5.795 | -42.9358 | 2025-10-05 04:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 122.0 |
| d4b1aa71-faf6-3c49-a9e0-473871079bcb | -14.6902 | -48.3574 | 2025-10-05 04:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |
| eab95de8-5ca9-3f9b-ad58-5b7ce922c002 | -5.7952 | -42.9123 | 2025-10-05 04:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| 857b154b-b6e1-3fdc-bd74-e02b36f62aac | -14.6902 | -48.3574 | 2025-10-05 04:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 64.2 |
| b264794a-f256-341f-a294-d5e0d0297ea9 | -8.5764 | -46.3041 | 2025-10-05 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 254.8 |
| 60b64460-2911-38dd-b261-2f4fabb34fac | -8.5956 | -46.2798 | 2025-10-05 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 0830bb58-0159-343f-a5a1-5aff4790b755 | -12.9844 | -51.0433 | 2025-10-05 04:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 2d3893e4-1b84-30a2-8f60-2df7934dd5bf | -14.3353 | -47.6755 | 2025-10-05 04:20:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 65945b02-2a7b-3122-8920-5287b7d18193 | -13.2741 | -47.6158 | 2025-10-05 04:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 94c1cd91-fcfe-397b-a2bf-138cf1292a7f | -13.2745 | -47.5933 | 2025-10-05 04:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 2e24a770-4eff-3b9c-8e2c-d80b80cf2037 | -8.5759 | -46.349 | 2025-10-05 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 5d961d31-960a-3605-8f98-2dc8119c6043 | -8.5953 | -46.3022 | 2025-10-05 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 186.3 |
| 90cb74d3-30b7-33a9-90b1-035f7c441e29 | -11.8225 | -45.0827 | 2025-10-05 04:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 66e51cb0-be91-33b5-b11c-c661f9096d61 | -16.3884 | -52.1612 | 2025-10-05 04:20:00 | GOES-19 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 64.4 |
| fb998d76-1900-3a75-9321-7014232e4911 | -11.823 | -45.0596 | 2025-10-05 04:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| cab89457-865c-3c46-89a1-d1927f093c79 | -8.595 | -46.3246 | 2025-10-05 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 224.7 |
| fa39e11e-56b6-3d9f-aa05-26fa50766f9c | -18.3345 | -45.8734 | 2025-10-05 04:20:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 82bc1b15-ee22-31a3-aba4-ac9c51b01ca9 | -8.5761 | -46.3266 | 2025-10-05 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 398.4 |
| e20f5a28-5df2-3991-a9b4-786b58f1574e | -4.235 | -46.7404 | 2025-10-05 04:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 49.6 |
| bcd09b4e-e1fe-395c-8a19-a1bcb41a096f | -18.3338 | -45.8971 | 2025-10-05 04:20:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 68154770-a65f-3b9b-a278-a96dcb287fc1 | -13.2741 | -47.6158 | 2025-10-05 04:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 1d6d18d4-ab57-3313-a5d8-259eee9da508 | -14.6902 | -48.3574 | 2025-10-05 04:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 333ebac5-a18f-36c2-8579-45e07d4169bb | -17.9404 | -57.6134 | 2025-10-05 04:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.0 |
| b3801a9e-2edc-3177-b9c6-d752e36a9958 | -17.9605 | -57.5904 | 2025-10-05 04:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.8 |
| 5f6996b1-0924-3a28-9252-181a35afdf29 | -14.7101 | -48.3319 | 2025-10-05 04:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 88.0 |
| ff419fc8-a85a-33c7-9292-14b55293aad9 | -14.6906 | -48.335 | 2025-10-05 04:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 72906697-f407-3e0a-aaf7-559661cf556a | -14.7096 | -48.3542 | 2025-10-05 04:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 75.0 |
| d66ebb5e-3d44-379e-87f3-aee721415555 | -14.6707 | -48.3605 | 2025-10-05 04:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 551d23ff-238b-3643-9f0f-3a2524d4cfbc | -17.9408 | -57.5928 | 2025-10-05 04:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.8 |
| e4208b6e-97ec-3866-988a-39e82d37cba6 | -13.1404 | -50.8739 | 2025-10-05 04:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 80ee479d-0dfd-3210-90f5-3415f1187ea1 | 3.86511 | -51.80359 | 2025-10-05 04:42:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1aeef354-ad0e-30d4-819f-84f1a1e3955d | -6.25209 | -45.37169 | 2025-10-05 04:44:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| caeff1ff-6cad-32f2-8d02-fbf311155066 | -6.40615 | -43.05998 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 49c01a1f-65a2-3404-bb44-250e80f1355b | -6.35812 | -43.91134 | 2025-10-05 04:44:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 13c25336-f1b2-3c4e-a231-f0ffd2e105bd | -5.46542 | -51.00925 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e60e6f0-dbd9-3a6a-aa4b-0031e1fd5617 | -6.12726 | -42.85949 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 92cc711f-09c6-394c-aeab-32da6dfc75c4 | -4.64466 | -43.18773 | 2025-10-05 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 91031820-0dc4-356e-b455-2cd61bbd9070 | -4.5654 | -48.60317 | 2025-10-05 04:44:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed3cf11b-239f-3429-8557-e5d6028abf94 | -6.10885 | -43.1096 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9c396136-6704-3535-9af4-5a2ab3359b3c | -3.84868 | -41.56983 | 2025-10-05 04:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| a436a0b8-bd72-39a5-b1e2-edb086ea90e7 | -6.12223 | -42.85909 | 2025-10-05 04:44:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4e3f47ec-f01b-35ce-9daa-3d7aeb89a3e9 | -2.8951 | -50.72988 | 2025-10-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4513b551-3ef9-3090-8d84-be6f0e88a3c5 | -5.48992 | -42.80148 | 2025-10-05 04:44:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| c217c1ca-a534-32eb-9576-f05c204013e1 | -5.77681 | -45.74877 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 978a16d0-6ced-3250-bf76-0da27547d1d2 | -3.84677 | -41.58255 | 2025-10-05 04:44:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 07b69fd5-c771-309f-98c4-1257993bc7fc | -6.08685 | -44.03891 | 2025-10-05 04:44:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42278c4e-8c59-3c24-aac5-5004f332cb5d | -4.44086 | -43.23851 | 2025-10-05 04:44:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1b2b847d-3578-3bd6-bafa-a7000daba286 | -5.65148 | -43.19838 | 2025-10-05 04:44:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b90eac72-c0f2-3f08-86cb-d2cf2d05e174 | -5.9947 | -45.79588 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5da28546-6726-3d30-9c19-1fabbf189a67 | -3.24217 | -45.52422 | 2025-10-05 04:44:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8279f3a2-99af-351f-860f-0f79c240acec | -5.85452 | -45.81508 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a3d90ec-9796-3dfa-909f-3eae9b0493aa | -5.92315 | -42.89788 | 2025-10-05 04:44:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 9da2c500-6f84-30d0-8a22-146f36d4f6c2 | -5.79284 | -45.7806 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 82b4d1e0-9255-3e61-b213-fdbfffb6c125 | -6.6955 | -41.95575 | 2025-10-05 04:44:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ba66f09a-133c-354f-b8b4-be6bd107f626 | -5.78142 | -45.74568 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e83d40a-ff69-3f66-af95-c07bee064378 | -4.27654 | -46.74784 | 2025-10-05 04:44:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac507781-92f9-3754-8d35-6a0e2065aafb | -3.66447 | -50.27127 | 2025-10-05 04:44:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45b37e77-4a6e-32c1-b1bb-7b0edb592712 | -2.51805 | -51.9318 | 2025-10-05 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0495dfff-f53f-385f-ba39-1595ab321b87 | -5.47095 | -42.79278 | 2025-10-05 04:44:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 01e52e50-5c17-34e9-bbb3-bec60f6a5866 | -5.8181 | -45.80944 | 2025-10-05 04:44:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19c90b65-3b50-388b-abbb-4c0b07ca5c61 | -6.14791 | -44.65837 | 2025-10-05 04:44:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b1c27080-c3c2-307c-bdeb-86b6653852f8 | -6.37549 | -42.88219 | 2025-10-05 04:44:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 99e7bb29-d224-38dd-8641-88185ecc39c8 | -6.34863 | -41.63955 | 2025-10-05 04:44:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |


[Clique aqui para ver as próximas entradas](README72.md)
