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
| 8d0964d5-43e4-3e45-b32d-938b03b41ecf | -2.8556 | -53.3256 | 2024-10-21 03:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| c94d8a90-2e1a-31df-bddf-8ad6c2388cf1 | -2.905 | -45.2143 | 2024-10-21 03:15:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 12248a99-27aa-36c5-8c6c-88810c4502c7 | -2.9051 | -45.1918 | 2024-10-21 03:15:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 12bacd77-aed2-328c-80ed-4ef69f2c0043 | -3.0036 | -53.0583 | 2024-10-21 03:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| caacd332-4e06-3db9-8179-a2bda28e6a3b | -3.0037 | -53.038 | 2024-10-21 03:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 84627d18-41da-306b-b115-df2df63e363d | -3.1137 | -53.1366 | 2024-10-21 03:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 34c22a08-88da-3786-967c-d661ad76a6e4 | -3.1138 | -53.1163 | 2024-10-21 03:15:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 8410970f-f63e-3ec8-9f4a-6d29802a000a | -3.2146 | -50.8093 | 2024-10-21 03:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 5a834cdd-fed6-39e5-98dd-3b70f984bd26 | -3.2147 | -50.7884 | 2024-10-21 03:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 6bf73e23-4a48-3852-81c7-e75363e6fdcb | -5.6894 | -46.435 | 2024-10-21 03:15:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 373fc6fd-3284-30c2-b02b-7685ace071f3 | -12.4778 | -63.1885 | 2024-10-21 03:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 27.5 |
| f600052f-f240-3276-9716-5c1312684e45 | -12.5357 | -63.0319 | 2024-10-21 03:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| d9540726-09fa-3e84-a29c-9c6617b83789 | -12.5147 | -63.3014 | 2024-10-21 03:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 42.2 |
| da9d04dc-603c-331f-8131-6c1777f80524 | -12.5168 | -63.0329 | 2024-10-21 03:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 294f4088-99eb-37e5-95c6-42ce2f76d9e2 | -12.5336 | -63.3003 | 2024-10-21 03:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 8c40c582-04d8-3e54-8a39-595deabdc12b | -12.5356 | -63.051 | 2024-10-21 03:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 5df15e60-a15b-3f3b-b748-feea499c6406 | -18.2828 | -56.0994 | 2024-10-21 03:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.0 |
| 62e4d260-c8c8-3c6e-828b-406950a153ba | -1.1834 | -53.6368 | 2024-10-21 03:25:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 1f5f79ee-29c1-3fb2-8d6e-bae029b790f9 | -1.2018 | -53.6366 | 2024-10-21 03:25:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| bc76015d-5d55-37d3-8986-608acdba9b40 | -2.4824 | -49.1233 | 2024-10-21 03:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 7667421c-7867-362e-8ebc-46641a320814 | -2.4824 | -49.102 | 2024-10-21 03:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| b34a1382-68b9-3ad8-9c1e-a3d14a5bfc8e | -2.8556 | -53.3256 | 2024-10-21 03:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| c02478f3-ebbb-3eff-b773-9cdea6d6bf64 | -2.905 | -45.2143 | 2024-10-21 03:25:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 4048c10a-218e-3e97-9b64-a32da5a22846 | -2.9051 | -45.1918 | 2024-10-21 03:25:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 5f98c3c4-acb9-39da-b85a-4616b0f18d1a | -3.1138 | -53.1163 | 2024-10-21 03:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 1bcbcafb-d733-301c-aa57-e3a80e435ef7 | -3.2146 | -50.8093 | 2024-10-21 03:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 955c5ba1-6f41-395e-ba0c-34c034abf510 | -5.6894 | -46.435 | 2024-10-21 03:25:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 895ec384-fdb4-3ee8-bdba-4c97ace69aad | -5.6896 | -46.4128 | 2024-10-21 03:25:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 19cc07dd-6de6-3848-bb88-e56f18bcd259 | -12.5147 | -63.3014 | 2024-10-21 03:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 55e7654a-f0a5-33fb-8b2d-53bfd8ddcc8b | -12.5167 | -63.0521 | 2024-10-21 03:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 04c91310-7f6a-36ed-abe0-cc4f681a8b47 | -12.5168 | -63.0329 | 2024-10-21 03:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 6a75a6c8-d64d-305a-88ca-552816095c6a | -12.5356 | -63.051 | 2024-10-21 03:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 21149574-2dd6-30df-abfe-275965999412 | -12.5357 | -63.0319 | 2024-10-21 03:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 00b37ff9-0d45-343d-98d5-2bb068fdaa3b | -18.2828 | -56.0994 | 2024-10-21 03:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.8 |
| b9e18f85-22bc-3f2f-a577-efb21ca1ede5 | -1.1834 | -53.6368 | 2024-10-21 03:35:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 22f83e33-2589-35e2-8365-9ff63e42a36e | -1.2018 | -53.6366 | 2024-10-21 03:35:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 2b4f2f41-2786-3d12-9389-40677afa4acf | -2.4824 | -49.1233 | 2024-10-21 03:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| bc0484e4-b457-3902-ac8c-0824feb126ef | -2.4824 | -49.102 | 2024-10-21 03:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| b5454f3f-b1db-3ee6-a9fe-f9aa15122c66 | -2.7885 | -51.3618 | 2024-10-21 03:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 3866fd44-ce76-3dca-8ef9-126f8c02a1d8 | -2.905 | -45.2143 | 2024-10-21 03:35:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 67.0 |
| cf15bc09-03ce-3e76-ba76-1dbe2412c39e | -2.9051 | -45.1918 | 2024-10-21 03:35:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 24c8fa0d-9742-3051-86e4-1f7de07dfe7f | -3.1138 | -53.1163 | 2024-10-21 03:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 44ed7339-8dfc-3d01-9301-b74e5ff96e6b | -3.2146 | -50.8093 | 2024-10-21 03:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| d0452641-fce1-3460-b1d3-a37a3135ee4b | -5.6894 | -46.435 | 2024-10-21 03:35:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| fc0d248f-5363-37e7-9847-156e2c2b97f5 | -5.6896 | -46.4128 | 2024-10-21 03:35:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| d5baa84d-4e18-3b8e-9030-0664b77ee890 | -12.5147 | -63.3014 | 2024-10-21 03:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 26.8 |
| bbb3e950-38c0-33cc-b203-d180e2d5de1e | -12.5167 | -63.0521 | 2024-10-21 03:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 0e2650c8-44a3-3d55-9ff1-4b7b4b385144 | -12.5357 | -63.0319 | 2024-10-21 03:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 27.2 |
| d987ce44-63d7-32d5-8eb7-777d32151dc9 | -17.0213 | -57.3333 | 2024-10-21 03:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.0 |
| 3557abb9-7376-3093-b28a-7af28507739e | -18.2828 | -56.0994 | 2024-10-21 03:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.8 |
| 9cfd5d9c-392a-3103-9b75-33584bba9c9d | -1.1834 | -53.6368 | 2024-10-21 03:45:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| d7b51faf-6cd7-320f-8e53-1f194baf3f20 | -1.2018 | -53.6366 | 2024-10-21 03:45:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 50696625-1c00-3b34-941b-422175697307 | -2.464 | -49.1024 | 2024-10-21 03:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 9d314faa-6b68-3349-8c09-f5bbfdb603bf | -2.4824 | -49.1233 | 2024-10-21 03:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 18689c5b-41f3-3c76-951c-b2fbde184490 | -2.4824 | -49.102 | 2024-10-21 03:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 8e4dfdac-8c3b-3b7d-9684-c81f9ffc02a3 | -2.7885 | -51.3618 | 2024-10-21 03:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| f44ddda5-c186-37ab-adbc-3213788ee34c | -2.8555 | -53.3459 | 2024-10-21 03:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 7319390f-3518-332d-88e2-50573fd2f451 | -2.905 | -45.2143 | 2024-10-21 03:45:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 66.3 |
| a96056c7-7a6d-3208-a268-cf1f7886efff | -3.1138 | -53.1163 | 2024-10-21 03:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 2850a878-12f2-3f69-8e8c-01c9bcba122f | -3.2146 | -50.8093 | 2024-10-21 03:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 0e2dfd44-549f-3507-a4d5-bfabac473ee9 | -4.2356 | -43.7391 | 2024-10-21 03:45:30 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 1a8a128e-a02b-31f7-95a6-c881e6804527 | -4.2357 | -43.716 | 2024-10-21 03:45:30 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| e9356fda-4138-353c-a097-409f88755fda | -4.2542 | -43.7381 | 2024-10-21 03:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| f232e507-a978-3ae0-bd28-ada206b1ee16 | -5.6894 | -46.435 | 2024-10-21 03:45:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| ac159f2f-3f74-369a-98f8-575ee252f5e5 | -12.4778 | -63.1885 | 2024-10-21 03:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 27.5 |
| b0b841a4-f737-3225-80bd-0c9712c1b412 | -12.5357 | -63.0319 | 2024-10-21 03:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 26.3 |
| be457522-b544-37bf-b971-47111702882f | -18.2828 | -56.0994 | 2024-10-21 03:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.7 |
| cb46dd3f-4c90-323c-a526-73ef176e3579 | -4.86567 | -43.25295 | 2024-10-21 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f064bdeb-c4bc-3afb-8988-e93cc35ca459 | -6.32746 | -35.06104 | 2024-10-21 03:47:00 | NOAA-21 | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 23d7a87f-2360-3a34-a59d-8c7dc27989ad | -6.01508 | -38.13339 | 2024-10-21 03:47:00 | NOAA-21 | FRANCISCO DANTAS | RIO GRANDE DO NORTE | Brasil | 2403905 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1132978a-52f2-3543-9934-62d2ae68e152 | -5.92552 | -38.35797 | 2024-10-21 03:47:00 | NOAA-21 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 82eb5243-8157-3d2c-8f83-7f3b281b7e3f | -5.59382 | -37.44621 | 2024-10-21 03:47:00 | NOAA-21 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ae2dd34d-1572-388d-99bc-82cd786a78e5 | -5.38305 | -42.89343 | 2024-10-21 03:47:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a9093cfd-5cda-3f9d-ac7d-f68e60b0072d | -5.32704 | -35.48129 | 2024-10-21 03:47:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| c989f4d3-af9b-3adc-a5b7-fb2141ead4ac | -5.22069 | -43.41107 | 2024-10-21 03:47:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d29fe51e-8993-399b-ad16-644edbdc52ab | -5.0714 | -37.71681 | 2024-10-21 03:47:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3c3d91bd-f1c1-3a30-bf5d-b98e51275d1e | -5.053 | -37.9966 | 2024-10-21 03:47:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d14578c5-68b2-331f-a4aa-c9bd7b7d03ff | -5.03558 | -40.90977 | 2024-10-21 03:47:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 27f90ef1-e02b-3f8c-88a6-53d79a564fe4 | -4.99084 | -39.25565 | 2024-10-21 03:47:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7a40f21d-d63a-3b2c-86f5-f4198d0defde | -4.78331 | -41.39431 | 2024-10-21 03:47:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f081694f-419f-30f5-9488-5ac9fcad0a4f | -4.7009 | -37.79746 | 2024-10-21 03:47:00 | NOAA-21 | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 21098463-ddef-3b54-8f0c-18aa2f723527 | -4.24952 | -43.72264 | 2024-10-21 03:47:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 167fe223-cf78-360d-b994-e771db2a1c54 | -4.24868 | -43.7276 | 2024-10-21 03:47:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 265e4853-8969-3b28-8204-fccdf26b60e5 | -4.24782 | -43.73271 | 2024-10-21 03:47:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| db09d401-748d-3bfc-b007-c7527df4b6c8 | -4.24694 | -43.73794 | 2024-10-21 03:47:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a2c09ad3-1f44-3198-9154-8a35a08b0e22 | -4.24477 | -43.72189 | 2024-10-21 03:47:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 15588716-4856-3dfd-8e0b-0cecb7baad4e | -4.24395 | -43.72677 | 2024-10-21 03:47:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7b5d827b-86cd-3704-b980-28d4606cec30 | -4.24309 | -43.73184 | 2024-10-21 03:47:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 3dbae7a2-71bb-35a4-9d4a-95be4c6a2838 | -4.24221 | -43.73706 | 2024-10-21 03:47:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a22fa4f3-2e50-340c-a4e2-2bef343c57e2 | -4.24135 | -43.74217 | 2024-10-21 03:47:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c26b355-74f0-38f8-9b3d-ef4644dc1c60 | -4.24003 | -43.72106 | 2024-10-21 03:47:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e411a304-cf39-3624-8705-b275a0deff1f | -4.23919 | -43.72604 | 2024-10-21 03:47:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a6af54c6-46e0-3b58-8476-c21a4f2de7fd | -4.23834 | -43.73107 | 2024-10-21 03:47:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3a8e1d52-c49d-3be3-82f2-dd76a10145c8 | -4.23747 | -43.7362 | 2024-10-21 03:47:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 17639b6c-a5ce-318a-82da-7b2088a28a44 | -4.2353 | -43.72021 | 2024-10-21 03:47:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cde95230-4d1b-3f05-8cd8-f9e48aecf93a | -4.23445 | -43.72522 | 2024-10-21 03:47:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 677a86c4-6d82-39cd-b0bb-f8edb33bb07c | -4.2336 | -43.73024 | 2024-10-21 03:47:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c0f32e14-8e51-3fcf-9252-2af353dda19e | -4.23274 | -43.73532 | 2024-10-21 03:47:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 44ae74c6-d15b-3088-9583-3529bf3330f9 | -3.80729 | -38.49022 | 2024-10-21 03:47:00 | NOAA-21 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f80e40ad-57d3-35c6-a337-ab771ddf71c5 | -3.35224 | -42.77243 | 2024-10-21 03:47:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README21.md)
