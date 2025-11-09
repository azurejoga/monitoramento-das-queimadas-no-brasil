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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbcc8858-5ec8-3cf4-a36f-a9b1962062a6 | -9.76 | -66.86845 | 2025-11-09 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1f8be803-cfe2-38e3-8e70-9c447f2cc150 | -19.74503 | -58.08715 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| b297ca00-7e0a-3466-b828-d7414be4266a | -19.72243 | -58.11093 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bb4158f3-27aa-32b1-8e77-cf715d2bc4bb | -19.75709 | -58.10781 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 969985ac-d9de-34b0-ac5e-659a49521048 | -19.73555 | -58.1187 | 2025-11-09 06:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 7e320a52-e44b-3af1-964e-65a892ca20be | -9.62265 | -68.59882 | 2025-11-09 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80036a9b-634c-333c-850d-bfa3211e8b54 | -7.99166 | -70.93319 | 2025-11-09 06:01:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8b7997b5-2c00-345e-9b73-c0c12478d6a4 | -3.9824 | -45.4614 | 2025-11-09 06:10:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 139.5 |
| 107bda10-1427-3bd6-951e-eadcb75f9e1b | -4.001 | -45.4604 | 2025-11-09 06:10:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 165.0 |
| 8c336719-291a-3dd7-9e6e-71b995594ae4 | -3.9824 | -45.4614 | 2025-11-09 06:20:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 44cb10a1-d0e7-3df5-a126-76898f0c2b0c | -4.001 | -45.4604 | 2025-11-09 06:20:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 444a542b-1ff2-3869-9a8a-108d1b9b3ef4 | -8.30713 | -72.82342 | 2025-11-09 06:20:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8ac91ae-284c-32a3-83c5-e1e70c68c0c2 | -8.30654 | -72.82728 | 2025-11-09 06:20:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ffddd7d-8617-3765-809e-3793a38b5ffb | -9.62524 | -68.59895 | 2025-11-09 06:20:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7cf58e06-959e-3bde-9051-c94b7895a628 | -8.30365 | -72.8229 | 2025-11-09 06:20:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e56a2422-5791-3b6a-8431-711ee4149fe1 | -19.7413 | -58.1088 | 2025-11-09 10:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 123.5 |
| c5ffa6b5-b022-303c-a889-542f585493ea | -11.25341 | -40.64136 | 2025-11-09 11:19:00 | TERRA_M-M | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 25.2 |
| 7b0f1234-8f39-33f1-95ae-03094589d6de | -7.83922 | -37.55685 | 2025-11-09 11:19:00 | TERRA_M-M | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 2f936490-174b-39b0-9934-b4b800286601 | -7.06831 | -34.91722 | 2025-11-09 11:19:00 | TERRA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 117.7 |
| 2a5709bd-8367-3886-89d5-4a8f984fc6bd | -7.47909 | -37.35605 | 2025-11-09 11:19:00 | TERRA_M-M | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 35.2 |
| 04dc49d5-0576-39ec-ac4d-b17a2a13879f | -6.01689 | -37.05317 | 2025-11-09 11:19:00 | TERRA_M-M | JUCURUTU | RIO GRANDE DO NORTE | Brasil | 2406106 | 24 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 6ecd4714-5fca-3a88-bbda-532913cf5d83 | -7.47713 | -37.36891 | 2025-11-09 11:19:00 | TERRA_M-M | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 22.0 |
| 59f14ee3-614d-371e-88a8-6a54de8fdaa4 | -3.3369 | -44.3806 | 2025-11-09 11:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 24a3e837-445e-354c-a3c8-67ba07cd4f95 | -3.3369 | -44.3806 | 2025-11-09 12:00:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 52e129a1-2503-38a6-a771-48220f6b2ec1 | -3.3369 | -44.3806 | 2025-11-09 12:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| d0c47e90-588a-3e7c-bb54-9b6899ddc001 | -3.337 | -44.3577 | 2025-11-09 12:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 284a3945-a7f1-3604-807c-78ffa8ec653b | -19.7416 | -58.088 | 2025-11-09 12:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.2 |
| 3dcbd932-456a-3d32-adb2-154c8bd7a033 | -3.3182 | -44.3814 | 2025-11-09 12:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 347a5d42-1a91-3025-8600-be72eab16716 | -3.337 | -44.3577 | 2025-11-09 12:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 486a93c4-4a0e-30da-9871-f21ed0f6ddb6 | -19.7614 | -58.1062 | 2025-11-09 12:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 144.6 |
| 33fb4b12-9f01-3c8d-a093-661d445b4d29 | -19.7416 | -58.088 | 2025-11-09 12:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.1 |
| 72314683-f231-3446-b21d-7f6055422112 | -19.761 | -58.1269 | 2025-11-09 12:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.6 |
| 009cfc3f-ff6e-377a-8cc9-baaba8a6e780 | -19.7617 | -58.0854 | 2025-11-09 12:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.2 |
| 48304c68-3edb-3153-a2f4-caa3cdafcef4 | -3.337 | -44.3577 | 2025-11-09 12:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 2454bf5b-9bb8-375f-bb97-a2fe1a456d49 | -3.6707 | -41.462 | 2025-11-09 12:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 145.1 |
| f4f2c9d0-37de-3523-a6c3-85b4d4f71f37 | -5.6057 | -41.0903 | 2025-11-09 12:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 119.2 |
| 1439e4fc-0d75-331e-a63a-e37da8b9eabc | -3.3182 | -44.3814 | 2025-11-09 12:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 13ec49a6-09a5-3c80-9e14-aa46c4d9f115 | -3.3183 | -44.3585 | 2025-11-09 12:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| f00438da-1976-305b-a8ca-0e8ad09d11b5 | -19.8023 | -58.0593 | 2025-11-09 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.8 |
| 1d849d15-ea90-3353-8caf-6728457df41a | -19.7826 | -58.0412 | 2025-11-09 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.3 |
| bc27a9a4-2bc6-3a02-a38a-680dc6f1ef67 | -5.6057 | -41.0903 | 2025-11-09 12:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| 6db5159b-917b-3e13-8b0f-5c78a4869c41 | -3.3182 | -44.3814 | 2025-11-09 12:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 218.1 |
| ec759778-b3bb-3c83-b449-d2363aae8a17 | 1.46713 | -56.0098 | 2025-11-09 12:55:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 144c84c6-5762-365d-8405-125bda9aae07 | -1.29835 | -49.34946 | 2025-11-09 12:55:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 53b09dc2-ff0f-34bd-90a6-4094f70c939e | 1.97368 | -55.86656 | 2025-11-09 12:55:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 7b538e1c-7d49-30e6-90b3-4c20be6c7d81 | -2.61085 | -49.21292 | 2025-11-09 12:55:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 24fd7a42-6558-335e-86b8-1e6e223ffb4e | -1.2463 | -53.80296 | 2025-11-09 12:55:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 9b1b1dd6-597f-370a-a104-bdfc8773373a | 1.97243 | -55.85784 | 2025-11-09 12:55:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| a00cd066-818e-3032-a4e5-39c78098e102 | 1.98246 | -55.86535 | 2025-11-09 12:55:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5731f125-0e4e-384c-9a63-5f5cc7ece739 | 1.47466 | -55.99986 | 2025-11-09 12:55:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| d84d6367-194d-3754-9ef6-b5cf4bf1b612 | -1.24785 | -53.79197 | 2025-11-09 12:55:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 274683aa-e720-3c75-88d8-a588f9becd3e | -1.66698 | -53.71719 | 2025-11-09 12:55:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| ce1fec0c-824a-3bd1-a7cd-5cf2939dbf1d | 0.12475 | -51.44117 | 2025-11-09 12:55:00 | TERRA_M-T | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 14.3 |
| b6455db4-3520-3056-95fa-b2a95ce8da9f | -2.60405 | -49.23234 | 2025-11-09 12:55:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| fa83042f-b7f5-35b6-b410-3d15c96dae1f | 1.47591 | -56.00858 | 2025-11-09 12:55:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 566a8727-5d64-3c8e-b95e-08365a447fde | 1.92677 | -55.87066 | 2025-11-09 12:55:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c06b2167-cd3c-314d-a693-0151e2c21a68 | 1.98121 | -55.85662 | 2025-11-09 12:55:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 3840293d-fb2f-3bca-96df-1c00a47487b9 | -1.65714 | -53.71587 | 2025-11-09 12:55:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 6e832b9c-ebc1-3227-89de-4ae3e7c90258 | -1.73102 | -55.07387 | 2025-11-09 12:55:00 | TERRA_M-T | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 69cfe558-7552-34e4-96c7-859cc396ca29 | -3.33425 | -51.50786 | 2025-11-09 12:57:00 | TERRA_M-T | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 8555b53d-f7c5-3d9f-acf0-aa32bee5e29e | -4.51548 | -48.83445 | 2025-11-09 12:57:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 6865c93c-9b9d-307c-8f1f-1f6ef5301a36 | -6.55565 | -52.8012 | 2025-11-09 12:57:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 9c15976b-2143-36c5-95e8-80ad4bad622a | -3.0835 | -49.20247 | 2025-11-09 12:57:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 28c6a955-1ff0-36df-b55e-556ac6fe91a7 | -6.55938 | -58.48406 | 2025-11-09 12:57:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a961b578-e4d0-3eea-b59f-530034f2647a | -2.08549 | -56.65587 | 2025-11-09 12:57:00 | TERRA_M-T | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 42448122-048a-3f9d-bcd3-5d651d684c0a | -5.86901 | -57.76268 | 2025-11-09 12:57:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 679d2778-d9bc-3297-a668-1bd06236c14f | -5.86775 | -57.77146 | 2025-11-09 12:57:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c58349f9-4020-3dd7-b1b6-15cd2511e794 | -8.62143 | -51.59372 | 2025-11-09 12:57:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| ff47b076-fa48-3620-bcdb-e167cdcaa50c | -3.63063 | -58.61983 | 2025-11-09 12:57:00 | TERRA_M-T | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0cc21adc-e456-3a10-8562-8886bcc68e79 | -3.38748 | -54.89765 | 2025-11-09 12:57:00 | TERRA_M-T | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6ae89890-7c97-3386-9357-5dedb6a7a942 | -2.08424 | -56.66461 | 2025-11-09 12:57:00 | TERRA_M-T | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8558596c-7514-3132-82e4-669d6fa590a6 | -4.09534 | -48.44415 | 2025-11-09 12:57:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| b9bd00f1-0fd3-37da-b709-6b12f2176dde | -8.18678 | -61.38024 | 2025-11-09 12:57:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e0ed5193-c34b-3152-8194-55b18865dfde | -3.33207 | -53.24354 | 2025-11-09 12:57:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 614d4476-bef5-3862-a80a-daad3fedca76 | -8.56092 | -51.55782 | 2025-11-09 12:57:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| a1411c89-666b-38f1-96fe-4e64de8d9bf8 | -19.75252 | -58.11113 | 2025-11-09 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.8 |
| 8ac96bfe-83fd-3019-a20f-ef263861956a | -19.77152 | -58.11379 | 2025-11-09 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| b24a822b-8aa3-31a4-b0b8-50d94e55b864 | -18.21536 | -56.7209 | 2025-11-09 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| f5bb5093-29de-3b73-8253-b69a4ca2a3a2 | -19.76202 | -58.11246 | 2025-11-09 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.0 |
| 40383b9e-bba8-3718-be22-4cc81c66022f | -19.78008 | -58.04834 | 2025-11-09 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.6 |
| 4d0730fa-ba3f-3ec6-9b31-c37bca036fe5 | -19.77054 | -58.04702 | 2025-11-09 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.8 |
| bd08d276-4e47-35c6-84f6-2ba2d829f63a | -18.26483 | -56.48399 | 2025-11-09 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 4d499a0b-8dc1-3b1c-8bed-fd0bb462e438 | -20.53836 | -53.03664 | 2025-11-09 12:59:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 50a2c0e8-27b2-3661-aebf-9c652d5b6402 | -20.60816 | -55.80439 | 2025-11-09 12:59:00 | TERRA_M-T | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 12209080-902e-3931-93ac-b1ee2e72bdac | -19.76344 | -58.10159 | 2025-11-09 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.8 |
| acefeec2-f5c7-3607-9ea0-cfd158d73376 | -19.79467 | -58.04513 | 2025-11-09 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.1 |
| 572e949e-a3d1-35c2-885a-01f21bf5fe09 | -19.74584 | -58.08804 | 2025-11-09 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.7 |
| fc1b2c0e-b41d-390c-9325-ff246a2aab0a | -19.76101 | -58.04568 | 2025-11-09 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.1 |
| 6e15f355-577c-311f-926c-72df45525460 | -19.75535 | -58.08937 | 2025-11-09 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 40.2 |
| a94cf280-9e08-3426-92c4-cdfdff523225 | -20.34512 | -51.68583 | 2025-11-09 12:59:00 | TERRA_M-T | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 49e48271-be6b-355b-a2d9-8f1ed6710e27 | -19.74162 | -58.12067 | 2025-11-09 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.3 |
| 5f606f62-5e9a-3b04-b1c7-b373508e876e | -19.76486 | -58.0907 | 2025-11-09 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| fbffae74-30bd-30b1-b292-c2b8fb086507 | -19.77295 | -58.10291 | 2025-11-09 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.2 |
| dcfbfa9d-d22e-37cd-9ee6-f4ac08657664 | -19.76243 | -58.03473 | 2025-11-09 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 5b42c78c-05d7-3331-b00e-b021864c2b2e | -20.60853 | -55.79858 | 2025-11-09 12:59:00 | TERRA_M-T | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 6a0d719b-edcc-3243-9edb-945b6d5e69b0 | -19.72542 | -58.09628 | 2025-11-09 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.6 |
| e39ce4ff-70fb-39b5-a94e-05854a68e3c5 | -19.73352 | -58.10848 | 2025-11-09 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.6 |
| 182fa6bc-79b2-3972-862b-a07e83d48e80 | -20.6067 | -55.81419 | 2025-11-09 12:59:00 | TERRA_M-T | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8f9e0b29-3e01-306c-9220-c766c1cf6a61 | -19.74302 | -58.10981 | 2025-11-09 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.1 |
| 38613037-8f17-3a07-a1bb-683cba7cf9c4 | 1.9681 | -55.8595 | 2025-11-09 13:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |


[Clique aqui para ver as próximas entradas](README38.md)
