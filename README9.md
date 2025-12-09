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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27503200-0864-3669-b7dd-84639e1f5bb4 | 1.96552 | -55.68839 | 2025-12-09 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc9b2cfe-4b8a-3461-a8ff-2391e7f4c98e | -2.05718 | -46.50158 | 2025-12-09 05:16:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8cb44875-2a46-36a6-990d-fb2500d73b9a | 1.12729 | -60.5245 | 2025-12-09 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a200954-dbc5-3fcb-8c24-731409f16d8b | -0.64796 | -52.37912 | 2025-12-09 05:16:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65ad23b0-ed75-37df-9358-435f81d0caea | -1.10268 | -52.24126 | 2025-12-09 05:16:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3118a180-c687-35a5-b2a1-c241fc7d06e1 | -2.05091 | -46.5006 | 2025-12-09 05:16:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d6138ec-1848-3dde-86fa-1e73a941e3ef | 2.05459 | -60.87101 | 2025-12-09 05:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8151945-348f-38d5-8fc1-d70bc221b623 | -1.20262 | -52.09914 | 2025-12-09 05:16:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47e32e04-9e5d-34fe-bcfa-1f1ae89e003b | 2.01665 | -55.674 | 2025-12-09 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fdd8b16-f176-3994-8e1f-0c83d6659504 | -1.09967 | -52.26045 | 2025-12-09 05:16:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38dea1dd-5d4a-3fd5-81d1-fa4dfe1c884c | 2.05675 | -60.87214 | 2025-12-09 05:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf0a2407-3303-3d96-81c9-fd98415e1436 | -0.60254 | -51.81347 | 2025-12-09 05:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5808a116-fa00-3228-afb6-df6ecd53df59 | 1.96889 | -55.68785 | 2025-12-09 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e23900b-691f-30ca-9070-9685170d5720 | -1.10328 | -52.23741 | 2025-12-09 05:16:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d09e2383-4c60-329c-b780-7845f8e6c7f4 | -0.84846 | -51.95935 | 2025-12-09 05:16:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e4f8546-ef26-37a1-98b8-8fff811add8f | 2.01607 | -55.67041 | 2025-12-09 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d854fc4a-4167-3616-9d0d-f621d2bc1311 | 2.05529 | -60.87541 | 2025-12-09 05:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 086c4bea-75d5-390a-be2c-892d9b5a3a8d | -0.80416 | -47.862 | 2025-12-09 05:16:00 | NOAA-20 | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da342fdb-7a0d-3723-93a9-4bae2255ff7e | 2.02001 | -55.67346 | 2025-12-09 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 092524b0-7324-3450-8334-b6bd08e314db | 2.01549 | -55.66681 | 2025-12-09 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62b784e4-d55e-3cff-ab6b-bb8421566428 | -2.05642 | -46.50663 | 2025-12-09 05:16:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b66c90a8-0d64-3ea7-b607-770112534481 | 2.01722 | -55.67759 | 2025-12-09 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b73ec6b-0727-3a91-9d4e-a5b0e89c9878 | -0.60191 | -51.81752 | 2025-12-09 05:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45b0c9dc-9e33-3396-ba90-009fd7093cd7 | -3.43791 | -41.64227 | 2025-12-09 05:18:00 | AQUA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 59.7 |
| 053fea3c-51ff-3046-8073-034878e207b7 | -3.43424 | -41.66501 | 2025-12-09 05:18:00 | AQUA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 33.3 |
| 69da6bb9-1397-3ac4-819f-82244e4731c2 | -3.42568 | -41.65834 | 2025-12-09 05:18:00 | AQUA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 39.1 |
| dbe12eb3-a207-3b55-bce8-b97cf09801b4 | -3.4292 | -41.63552 | 2025-12-09 05:18:00 | AQUA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 23.3 |
| 73aa8c33-d764-3d19-ad40-d12d1acac419 | -7.86758 | -38.72935 | 2025-12-09 05:20:00 | AQUA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 398e83e4-a4f6-3e8e-8f4c-6049d3f6b9a9 | -21.53937 | -57.53461 | 2025-12-09 05:22:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe382747-8a41-32b8-ad52-82abf2062fa1 | -21.54408 | -57.52955 | 2025-12-09 05:22:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfa93f68-372c-33bf-8b64-112566760a2d | -21.54187 | -57.53057 | 2025-12-09 05:22:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c9d06f5-8cb7-3204-9d7a-945740fe551e | -21.53719 | -57.53568 | 2025-12-09 05:22:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6cec4750-29ae-370d-b71a-e2ded2557bd0 | 2.05372 | -60.87358 | 2025-12-09 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fd2fdc1-3233-3a4f-8cab-89966665b6be | 2.05321 | -60.87043 | 2025-12-09 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5cbb8c9-3fcb-318b-b424-cbbe70aae3fb | -12.40631 | -63.66324 | 2025-12-09 06:09:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 62981761-9efc-3b53-b1a3-be3a429b7906 | -12.40587 | -63.66669 | 2025-12-09 06:09:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb8846fd-28b7-342d-b5d0-b745ef9ca208 | -2.8503 | -44.9679 | 2025-12-09 06:30:00 | GOES-19 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 5f69c808-222e-3552-a112-79e8150375aa | 1.82506 | -61.13824 | 2025-12-09 06:56:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a4ed03cf-97bc-3406-a415-c2cddc32e82e | -3.6836 | -42.4138 | 2025-12-09 07:10:00 | GOES-19 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 101.3 |
| e5752e92-fb18-3f2c-a671-b75fb3f8d927 | -5.14994 | -38.92596 | 2025-12-09 11:17:00 | TERRA_M-M | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 4deed49d-d275-3445-9ca4-91a1d25d95af | -6.48201 | -35.60179 | 2025-12-09 11:17:00 | TERRA_M-M | TACIMA | PARAÍBA | Brasil | 2516409 | 25 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 52c8410d-dcf0-3357-bc53-6e834f0dae0b | -5.15356 | -38.93365 | 2025-12-09 11:17:00 | TERRA_M-M | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 26.3 |
| 5bed18a8-ca30-3205-868f-d835a31a6495 | -7.80556 | -37.633 | 2025-12-09 11:17:00 | TERRA_M-M | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 28.7 |
| 71edac43-6a00-3d19-8786-fe5b8c54950e | -5.33056 | -38.94817 | 2025-12-09 11:17:00 | TERRA_M-M | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 0ed34b98-54dc-31e7-a8da-a5fcc5b3e2ce | -5.14729 | -38.94392 | 2025-12-09 11:17:00 | TERRA_M-M | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 17.4 |
| dffbfe91-221c-339d-bf19-f06967cd3ab2 | -6.92995 | -35.82078 | 2025-12-09 11:17:00 | TERRA_M-M | REMÍGIO | PARAÍBA | Brasil | 2512705 | 25 | 33 | nan | nan | nan | Caatinga | 12.6 |
| d2d31d2e-a2da-3570-9533-c0bd5aa7a85e | -7.3649 | -38.85332 | 2025-12-09 11:17:00 | TERRA_M-M | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 12.6 |
| f26cde12-3b6d-3a37-aa45-3574f2e560fb | -5.93597 | -38.12008 | 2025-12-09 11:17:00 | TERRA_M-M | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 62.2 |
| 409f470e-1067-3ee9-ab25-88739360a62e | -6.167 | -35.4298 | 2025-12-09 11:17:00 | TERRA_M-M | LAGOA DE PEDRAS | RIO GRANDE DO NORTE | Brasil | 2406304 | 24 | 33 | nan | nan | nan | Caatinga | 19.5 |
| fa0e1497-c60e-3856-b50a-c4766339e988 | -3.4395 | -41.47947 | 2025-12-09 11:17:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 33.0 |
| e9f52219-2743-3689-8861-83b709e2e741 | -7.92702 | -37.62483 | 2025-12-09 11:17:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 26.0 |
| 64ad8b2a-4037-3ce1-8e84-f2eae55f461d | -3.44369 | -41.47264 | 2025-12-09 11:17:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 43.7 |
| 07deb94c-0cfd-36ae-aed6-5ae91dd28584 | -7.92154 | -37.61731 | 2025-12-09 11:17:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 808fd944-96ec-3775-87e6-a86d8c7c260f | -7.91969 | -37.62971 | 2025-12-09 11:17:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 7dc6a66e-d53a-3771-94ff-c78d2fd4adeb | -7.49139 | -37.1307 | 2025-12-09 11:17:00 | TERRA_M-M | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 46bfeacc-20a5-3484-9b37-221e7952ddd4 | -3.4442 | -41.44987 | 2025-12-09 11:17:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 58.5 |
| c00fbf75-1ff1-3035-b4f4-c9b406e07467 | -6.89458 | -35.37507 | 2025-12-09 11:17:00 | TERRA_M-M | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 2b42418e-f27a-3396-ad21-c794861079c3 | -7.80359 | -37.64609 | 2025-12-09 11:17:00 | TERRA_M-M | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 68.5 |
| 755b46f1-1cbb-33a1-b241-4d23a042ac4a | -5.57073 | -37.34996 | 2025-12-09 11:17:00 | TERRA_M-M | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 5f47f242-b460-3c14-950a-125523bf8304 | -5.93369 | -38.13489 | 2025-12-09 11:17:00 | TERRA_M-M | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 395c4de9-ce3e-3155-b252-6bb03405789a | -6.93146 | -35.81067 | 2025-12-09 11:17:00 | TERRA_M-M | REMÍGIO | PARAÍBA | Brasil | 2512705 | 25 | 33 | nan | nan | nan | Caatinga | 6.3 |
| a23472c8-1694-363d-9593-2297df030e95 | -5.14693 | -38.45945 | 2025-12-09 11:17:00 | TERRA_M-M | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 70979bb3-d399-3f1d-851e-fd1e5ef0563d | -3.5731 | -42.1354 | 2025-12-09 12:00:00 | GOES-19 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 87.2 |
| 44c71687-bbbb-37d4-9ae6-c38a998e2c66 | -3.5918 | -42.1344 | 2025-12-09 12:00:00 | GOES-19 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 91.4 |
| f878d497-6857-372c-9bc3-b71a28bec15c | -3.5919 | -42.1107 | 2025-12-09 12:00:00 | GOES-19 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 305.8 |
| 38e02678-d8c9-345e-97ed-ae1877444182 | -3.5919 | -42.1107 | 2025-12-09 12:10:00 | GOES-19 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 348.0 |
| 98d5fc79-baf3-37ba-b0e7-68ac4cdbae58 | -3.5918 | -42.1344 | 2025-12-09 12:10:00 | GOES-19 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 122.8 |
| 823f3056-c8b6-36d2-b5b9-933b696e72cb | -3.5919 | -42.1107 | 2025-12-09 12:20:00 | GOES-19 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 158.1 |
| 39a1add4-1739-3abf-8563-7fbb9ed5914f | -2.9006 | -42.0947 | 2025-12-09 12:20:00 | GOES-19 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 855afc3c-cb4f-3ea1-92ee-093b92789726 | -7.7046 | -37.8666 | 2025-12-09 12:50:00 | GOES-19 | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 101.2 |
| 347682b9-3941-3a9b-8d1f-3d16d7000695 | 3.39631 | -51.24813 | 2025-12-09 12:53:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5a8cc448-6519-3ed7-848f-471c28fbb50d | -0.24128 | -48.78215 | 2025-12-09 12:55:00 | TERRA_M-T | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 46cf109d-bb71-39b4-9c5f-424ad6c16d2a | 0.15063 | -50.02458 | 2025-12-09 12:55:00 | TERRA_M-T | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| cd7b07c4-06f7-328b-8058-512ec54f3704 | 3.3304 | -60.83909 | 2025-12-09 12:55:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 92263b25-7900-3b3c-906d-0f63c45f2087 | -6.74208 | -59.16071 | 2025-12-09 12:55:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f403cb5e-654e-3e1e-a426-e5dd752b57bd | -0.90102 | -51.91871 | 2025-12-09 12:55:00 | TERRA_M-T | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d6df0c51-f86e-3450-9251-a5781d53c59f | -6.74076 | -59.1698 | 2025-12-09 12:55:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 22a9d285-2b2e-388e-a65e-22960202208c | 1.89786 | -50.92801 | 2025-12-09 12:55:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 94fee74b-c8ec-3177-96ba-d1008aa1017c | -2.77991 | -54.53005 | 2025-12-09 12:55:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2330f214-eeab-35d7-89d8-4be3b0aee078 | 0.1536 | -50.04541 | 2025-12-09 12:55:00 | TERRA_M-T | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 62830300-0bbf-3287-8b39-49fbc9fdf032 | -2.54568 | -53.63929 | 2025-12-09 12:55:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 9d085779-8c77-3d8f-b62a-b3db8e0fd5af | -2.78141 | -54.51932 | 2025-12-09 12:55:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2d2db412-294c-30a3-89ce-a9cbde48cd40 | -3.4003 | -42.9681 | 2025-12-09 13:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| c544e572-f6e8-30f4-a617-057352183c0d | -1.678 | -45.6751 | 2025-12-09 14:10:00 | GOES-19 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 139.5 |


