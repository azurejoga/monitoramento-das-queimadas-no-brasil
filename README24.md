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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86f4ecc0-e0a4-3ebc-9e5e-a7702c1693ab | -7.10066 | -49.17625 | 2025-07-15 05:25:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dd3209ac-b3ec-3687-bafb-8b9c0b4f1af2 | -6.71083 | -47.8043 | 2025-07-15 05:25:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 66f736c1-80e1-38a7-861e-bf2c5c285a1c | -7.03901 | -55.43974 | 2025-07-15 05:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c647bbbd-66e4-3b2d-84d3-a8528e4001ba | -11.87741 | -58.71176 | 2025-07-15 05:25:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5b04f3b1-da61-3023-beb5-bd114cead2c1 | -6.91322 | -52.86055 | 2025-07-15 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 61c9af7e-0351-3f34-8af4-2c9add3715fb | -7.09438 | -49.17532 | 2025-07-15 05:25:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2e5e7dca-c21a-3934-bf7b-c00d5641e629 | -12.03495 | -63.76781 | 2025-07-15 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b3cf0cd9-cbf8-3b8b-b902-8121a6e94e4c | -18.65694 | -55.72314 | 2025-07-15 05:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a7770d3e-bb7c-39e9-8cd1-b658535f3ee4 | -6.88267 | -50.26867 | 2025-07-15 05:25:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4d8503e6-079b-3d1e-9b37-54d590e0425f | -6.71164 | -47.79807 | 2025-07-15 05:25:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2e717dd2-55fb-3b77-94e6-e69b53e213a4 | -12.44029 | -63.69751 | 2025-07-15 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a8ea1c51-3418-3e84-b945-6c1a71434016 | -12.5825 | -56.98156 | 2025-07-15 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d53e2e62-e758-31da-8ff9-e3b08baee01d | -10.53012 | -68.05333 | 2025-07-15 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb700a28-d4c5-3528-a9aa-91b1e0de74b7 | -18.65277 | -55.71712 | 2025-07-15 05:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 51ef83fa-d586-3dbb-84b9-69706157af37 | -8.59869 | -47.43894 | 2025-07-15 05:25:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54b09e28-a8da-3328-96ff-34c16d6604c7 | -8.61293 | -47.44054 | 2025-07-15 05:25:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e087cd4d-389f-377c-9321-94a3deb23792 | -5.2328 | -56.0156 | 2025-07-15 05:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 49ddc9ed-90be-33bc-adde-84b94d8b8623 | -6.91403 | -52.85472 | 2025-07-15 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3b912610-7ccc-3632-93e9-abecc75afd19 | -12.58152 | -56.98878 | 2025-07-15 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5260a02-ad8f-3f11-bc8e-a0038c136315 | -6.90833 | -52.85962 | 2025-07-15 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 610fada8-46f1-3ae5-8f5b-52bdfb4aab5e | -12.43691 | -63.69694 | 2025-07-15 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9fc5fab4-f2e7-3823-815e-0b6e19f90e67 | -6.87715 | -50.26904 | 2025-07-15 05:25:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3ca65c97-e6b1-3bc8-aa0c-38a2568afde4 | -7.50555 | -55.01488 | 2025-07-15 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a474cb2-1ed2-31c3-ab98-e6d6080b85fe | -8.60581 | -47.43976 | 2025-07-15 05:25:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 06bb4f89-5c0b-358c-83ca-bf542f46395f | -21.86233 | -56.74864 | 2025-07-15 05:27:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eedeaaea-3706-31d4-aeea-633762fafeab | -19.28985 | -55.15765 | 2025-07-15 05:27:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fed72712-2a8f-3fbf-8cad-b52947725ca2 | -19.75533 | -53.9998 | 2025-07-15 05:27:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7738e362-e7ab-3610-ab47-5c9d7a9dd6d4 | -20.14598 | -50.72242 | 2025-07-15 05:27:00 | NOAA-21 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6787017a-b3ff-3bad-90bd-9dc294411b53 | -22.39503 | -49.8033 | 2025-07-15 05:27:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c2e08465-85ca-3ded-89a9-da745ed66167 | -22.40215 | -49.8043 | 2025-07-15 05:27:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d4f59d2e-1230-3b42-8a22-befb8629b145 | -19.75572 | -53.99609 | 2025-07-15 05:27:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 303176f5-63b9-3df6-83a1-607d693edd7d | -11.4588 | -45.0895 | 2025-07-15 05:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 212.3 |
| af758e93-25b2-3706-800a-39fcba980ff4 | -10.5776 | -49.1316 | 2025-07-15 05:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 57d906fb-5160-3790-a9ea-476d310889e6 | -11.4393 | -45.1154 | 2025-07-15 05:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.4 |
| ce2adf74-86f6-330d-93b7-3c20325135ad | -11.4389 | -45.1385 | 2025-07-15 05:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 52c2b86d-3876-3b9c-b862-e68464ce410d | -11.478 | -45.0868 | 2025-07-15 05:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 1198beee-fc48-350a-a3b6-a016db8ed8c3 | -11.4584 | -45.1126 | 2025-07-15 05:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 278ed063-eea6-3cfe-9bb8-46a583e8c259 | -10.5586 | -49.1337 | 2025-07-15 05:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 3f7375f3-5d5c-304e-9314-ce21145611d1 | -11.4397 | -45.0923 | 2025-07-15 05:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 27e0fe62-3825-348e-a019-114396e42fd5 | -11.4397 | -45.0923 | 2025-07-15 05:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 6b724081-6547-3449-9cd3-3e7e930ab071 | -10.5776 | -49.1316 | 2025-07-15 05:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| c122319d-9e90-3765-908a-6e009ca018cd | -11.4393 | -45.1154 | 2025-07-15 05:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 910b26f8-6598-3f9d-ba1f-f9a983c21f1b | -11.4588 | -45.0895 | 2025-07-15 05:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 215.8 |
| c486f234-0a90-33bd-9a6a-ddc16d43863d | -11.4389 | -45.1385 | 2025-07-15 05:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| fa0f9113-04cb-344a-a88e-5e79401229f9 | -11.4584 | -45.1126 | 2025-07-15 05:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| f4a5ce69-7c4e-3c12-9fc3-08794b581257 | -11.45533 | -45.08978 | 2025-07-15 05:40:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 99f683b2-1e00-3dc3-8d6b-15a36a9cbf76 | -10.56574 | -49.12836 | 2025-07-15 05:40:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| b5348ea3-9e1c-3c6d-b3e8-ff14c04219b9 | -7.19883 | -43.09591 | 2025-07-15 05:40:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 2db19609-d6c5-36a6-81dd-d43a84c3ec1d | -5.36709 | -43.9157 | 2025-07-15 05:40:00 | AQUA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 21f553aa-9061-39c6-b45d-b036da5777d8 | -5.36578 | -43.92447 | 2025-07-15 05:40:00 | AQUA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 7a5a537d-7b65-3249-9948-6a106f3bbef3 | -9.80003 | -47.74249 | 2025-07-15 05:40:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 99ba4c9f-54a0-3c7f-bdcb-700108eac23b | -5.53024 | -43.88045 | 2025-07-15 05:40:00 | AQUA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9a4e9e78-d84c-3cd9-afce-24e2b712faeb | -10.89025 | -49.20779 | 2025-07-15 05:40:00 | AQUA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8a079641-d08e-3443-b0bc-e85872c71047 | -6.65375 | -43.03603 | 2025-07-15 05:40:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f63b992e-19ec-3eb1-b174-953321981892 | -3.58579 | -47.51236 | 2025-07-15 05:40:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c5251478-9265-3680-960f-cecc734cf3ad | -6.72675 | -44.33449 | 2025-07-15 05:40:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3bcc599e-2563-3e72-b421-b6ecef2ccf38 | -6.16939 | -45.87552 | 2025-07-15 05:40:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 9e8daa93-582f-38c1-9f66-c3f3ea1aa78a | -7.19749 | -43.10513 | 2025-07-15 05:40:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 4e7c5b7e-4be7-39c5-8af8-7852b3f1414f | -7.88489 | -44.49729 | 2025-07-15 05:40:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 397f35c5-41e0-3d17-af95-04781108da4e | -11.46413 | -45.09109 | 2025-07-15 05:40:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cca738d4-e904-3a8c-849f-31af47ef7d93 | -11.45666 | -45.08084 | 2025-07-15 05:40:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ff48f4a6-d5c8-3233-81bc-2fcc652e2074 | -5.53903 | -43.88174 | 2025-07-15 05:40:00 | AQUA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d82b7e68-ddfc-3b85-a9ea-271dcc927df5 | -4.61654 | -43.31857 | 2025-07-15 05:40:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1d2912b2-cad8-3e08-a4ae-8a578a82732b | -11.45266 | -45.10763 | 2025-07-15 05:40:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 89410e8d-b222-3ed6-823e-f25d3a912904 | -11.46279 | -45.10003 | 2025-07-15 05:40:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 08add446-4a7c-38ec-9796-6c30396c94ff | -9.97446 | -48.0819 | 2025-07-15 05:40:00 | AQUA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| fc3d7029-4b3f-3d41-9773-af80bfb25390 | -3.37988 | -47.46313 | 2025-07-15 05:40:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c80954fe-f3d4-362b-9682-450f18128c0e | -4.78221 | -45.33751 | 2025-07-15 05:40:00 | AQUA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a6ae7974-e57f-372a-b77d-cbc25211a797 | -7.88621 | -44.48848 | 2025-07-15 05:40:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 767ea740-82e9-367f-b557-421aa8de81a0 | -11.44999 | -45.12547 | 2025-07-15 05:40:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7c8edd2d-b657-38d8-ac79-041186e6c080 | -5.77915 | -45.09923 | 2025-07-15 05:40:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 47c60739-3135-38f9-9be4-e44ab6fefafe | -5.78051 | -45.09019 | 2025-07-15 05:40:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 6b885705-6d71-3560-8394-5b51bfbc313d | -6.16793 | -45.88501 | 2025-07-15 05:40:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9af01b97-70fd-35b8-b5f5-c52ba8e97381 | -11.43986 | -45.13306 | 2025-07-15 05:40:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 7995a6a8-c168-3c64-aa2f-bfcb45ed018f | -5.53772 | -43.89051 | 2025-07-15 05:40:00 | AQUA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4752c072-592d-3543-a391-a5ec8dacfd18 | -11.44519 | -45.09738 | 2025-07-15 05:40:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 37.3 |
| f6ff0e8f-bb4c-324f-b605-6f99ea046699 | -11.44119 | -45.12414 | 2025-07-15 05:40:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| f8aabd63-d0d4-3488-8512-474a55866b53 | -12.06897 | -43.47714 | 2025-07-15 05:40:00 | AQUA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9e18c361-d21d-3887-bde5-7bde2f75fe10 | -7.895 | -44.48978 | 2025-07-15 05:40:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dd3a6024-b7d5-372d-b428-f7778883067f | -9.80968 | -47.74402 | 2025-07-15 05:40:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 558c4d53-2923-361c-8ce7-881c4b279365 | -7.64135 | -44.39709 | 2025-07-15 05:40:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5b8e7518-c1f6-3d21-9ec3-917ce4d7a494 | -11.45399 | -45.09871 | 2025-07-15 05:40:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 9bae6df3-9b28-320f-b059-722e6829257d | -5.52892 | -43.88922 | 2025-07-15 05:40:00 | AQUA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7330a98b-294b-3419-b06b-01eebde05628 | -10.56363 | -49.14133 | 2025-07-15 05:40:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| d99678a0-ce83-337b-a767-446333890946 | -11.44653 | -45.08845 | 2025-07-15 05:40:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| acd82c05-ac35-30a8-81da-61bda64b5129 | -7.28041 | -44.0395 | 2025-07-15 05:40:00 | AQUA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 70d706a5-1885-350b-83e0-c841d7e107f0 | -2.91852 | -48.23655 | 2025-07-15 05:40:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| eb9345f6-5b01-3300-adad-c1de6c3d13e9 | -7.6387 | -44.41471 | 2025-07-15 05:40:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8f922616-a2c5-377a-9e34-3485fb92e89d | -12.4024 | -45.37443 | 2025-07-15 05:42:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f076c810-82ea-3cbb-b005-972361f04f33 | -15.22742 | -46.96505 | 2025-07-15 05:42:00 | AQUA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f3a5466f-8a8d-3376-9ece-5583bc956795 | -13.1275 | -47.26713 | 2025-07-15 05:42:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 27182f9b-4def-32ab-9b3a-a8e91dfbd43d | -15.226 | -46.97422 | 2025-07-15 05:42:00 | AQUA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 09cc27b1-bc7a-3e46-8612-c42e03ab9bc5 | -10.5776 | -49.1316 | 2025-07-15 05:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 3b6acf7e-23b5-36d6-b238-55edf4b14231 | -11.4393 | -45.1154 | 2025-07-15 05:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| f8dcaca9-0d0d-30b5-b789-9a708cdd7865 | -11.4584 | -45.1126 | 2025-07-15 05:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 22c6993d-0025-3ac3-afc9-12b3d09e8e90 | -11.4588 | -45.0895 | 2025-07-15 05:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 201.2 |
| 31426609-8f1d-36f5-a64a-2fb3308b7207 | -9.01739 | -61.22491 | 2025-07-15 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fd0d0c3-26b9-3e87-bd1b-30a8ab9f14f8 | -6.91019 | -52.86264 | 2025-07-15 05:50:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ef97b04-1128-3005-bb3a-4cab5394c7b4 | -7.78286 | -61.37067 | 2025-07-15 05:50:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 25021f04-719e-330a-81f9-8d7d8da55db4 | -7.03934 | -55.43777 | 2025-07-15 05:50:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README25.md)
