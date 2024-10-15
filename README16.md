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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3b6ac42-745b-3b78-bcb3-dac00db4df15 | -13.1473 | -62.3408 | 2024-10-15 01:06:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| f43a7809-f3c0-32aa-8724-ea37428e7072 | -13.3786 | -61.9582 | 2024-10-15 01:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 140.4 |
| c3d68881-37ef-398e-bf2b-3a9c8bf96386 | -13.5136 | -61.7552 | 2024-10-15 01:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 83.9 |
| b4aaf8ea-9523-384a-8788-82d07d7a1602 | 1.0016 | -52.2164 | 2024-10-15 01:15:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 5079db9a-ba15-3a1e-901a-b4168322ff0e | -3.1099 | -54.2263 | 2024-10-15 01:15:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| ed5ef620-a062-3cc3-8dc4-84b95275f722 | -3.1282 | -54.2459 | 2024-10-15 01:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 6052a2b1-228b-3e76-a607-0e823bc3e73f | -3.1283 | -54.2259 | 2024-10-15 01:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 79fbbad1-fa2e-39da-a649-797a7b7ff475 | -4.3959 | -47.7618 | 2024-10-15 01:15:31 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 51a63c6a-2f58-34ee-a431-32eb02c5cd4f | -5.2982 | -46.3936 | 2024-10-15 01:15:36 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 67.1 |
| c65b25cc-e8f4-3aea-8dda-a1eca8b13afa | -5.5732 | -49.3995 | 2024-10-15 01:15:37 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| fdffde91-f745-3a6c-ad52-c2722d9a5722 | -6.1597 | -35.2091 | 2024-10-15 01:15:40 | GOES-16 | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 70.6 |
| 925abd94-f3bf-3d3d-890c-4ce3d044f88f | -6.5691 | -48.2395 | 2024-10-15 01:15:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 4cd88fb0-e82b-3528-b6ac-f04a6d0fd2e0 | -10.3711 | -61.1935 | 2024-10-15 01:16:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 173.2 |
| 128612c8-bf9e-3bb8-abd3-787e6203b828 | -10.3713 | -61.1743 | 2024-10-15 01:16:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 9cd30536-d03a-370a-a946-c41ec56b1b44 | -10.3898 | -61.1925 | 2024-10-15 01:16:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| f0e5798f-bb1b-376f-9406-0ea24c3d2510 | -10.9473 | -54.1037 | 2024-10-15 01:16:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 7e9cd8d7-94e0-3fd3-888e-216f118de2d8 | -11.6915 | -65.2432 | 2024-10-15 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 71.6 |
| d4c6102d-b90a-39c5-b473-e66966fecdfa | -11.6917 | -65.2243 | 2024-10-15 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 68c08c8c-af08-3e78-9a42-9e29a70fb844 | -12.3793 | -63.7294 | 2024-10-15 01:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| ef70b24f-2dde-3d62-ba4e-e994af213220 | -12.3795 | -63.7103 | 2024-10-15 01:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 65913ae5-da79-37e6-92fc-f41122dc6b22 | -12.3982 | -63.7284 | 2024-10-15 01:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 96a35ed5-f80f-38e2-b738-d97fd2584a25 | -12.3983 | -63.7093 | 2024-10-15 01:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 70.1 |
| d854ca55-501d-3560-b8c7-0a0c7d65510c | -12.4602 | -63.0361 | 2024-10-15 01:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 17cb8fd0-bb0f-33bd-8438-a45223e08463 | -12.4603 | -63.0169 | 2024-10-15 01:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 6289b49e-b558-38b4-abbf-e3805512e7d8 | -12.515 | -63.263 | 2024-10-15 01:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 20d4a5ee-28a8-3875-a05a-fcfb6b4e1964 | -12.9728 | -62.7951 | 2024-10-15 01:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 36a8ad34-a2fb-3ae0-b915-f8d344e930ec | -13.1473 | -62.3408 | 2024-10-15 01:16:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 43836999-54fb-3b6d-8853-a34b2db58323 | -13.1475 | -62.3215 | 2024-10-15 01:16:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 0ae8faa7-f4d6-3b5b-bda6-e499f75c26ff | -13.3786 | -61.9582 | 2024-10-15 01:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 75.1 |
| d7c94366-2122-3a6b-845b-c039ce9e428a | -13.5136 | -61.7552 | 2024-10-15 01:16:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 2a45cef6-079f-3865-82c2-1a942e8f47f9 | 1.0016 | -52.2164 | 2024-10-15 01:25:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 9ca61bac-6268-3dd7-b74b-e5bb70659e39 | -3.1099 | -54.2263 | 2024-10-15 01:25:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 6a3c79ff-8ecc-3110-ab6e-d6a138739273 | -3.11 | -54.2063 | 2024-10-15 01:25:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 054e92ec-be36-3ac8-a3d4-ee63555850ed | -3.1282 | -54.2459 | 2024-10-15 01:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 75fc900e-a859-3a54-a1cf-63ea3aecc73c | -3.1283 | -54.2259 | 2024-10-15 01:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 86b9e0eb-2f3a-355a-a955-e6f506ec04a7 | -3.8439 | -46.9127 | 2024-10-15 01:25:28 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 44.0 |
| c5649671-48c3-31d7-b52e-9cfbb8d003ca | -3.958 | -46.4442 | 2024-10-15 01:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 5fcd7c33-e512-3394-b519-91981675bddb | -5.5732 | -49.3995 | 2024-10-15 01:25:37 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 1cbff6ef-47b3-3831-b7da-85058509f283 | -6.5691 | -48.2395 | 2024-10-15 01:25:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 89d6ff5f-053a-32f0-a1d3-c9598df2ba66 | -9.9777 | -47.3795 | 2024-10-15 01:26:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 398aae44-2e61-3e26-b3b4-cf553229015e | -10.0495 | -47.6589 | 2024-10-15 01:26:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| f5d1d87f-815a-355d-b66a-f9b96761ef61 | -10.0498 | -47.6368 | 2024-10-15 01:26:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| f94ea3dd-4cd3-3ce2-aaf5-34fbe89bb60e | -10.3711 | -61.1935 | 2024-10-15 01:26:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 190.1 |
| ed7a754b-5272-32d0-8b4f-ea94e47f4a82 | -10.3713 | -61.1743 | 2024-10-15 01:26:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 8f47aab7-ed76-3c61-a78e-1ed623eb8259 | -10.822 | -49.256 | 2024-10-15 01:26:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| c3ab014f-6c68-37a4-a2e5-489ef320f5f4 | -10.8224 | -49.2343 | 2024-10-15 01:26:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 04f9211c-df49-38a6-8342-5478a8744a79 | -11.6915 | -65.2432 | 2024-10-15 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 6d024d40-633c-392b-854b-1ab1228acd9c | -11.6917 | -65.2243 | 2024-10-15 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 6ef22fb3-21f2-34fa-9e3d-1bd62683bb73 | -12.3793 | -63.7294 | 2024-10-15 01:26:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| f7befb95-4749-3124-9d86-f1888d249b74 | -12.3795 | -63.7103 | 2024-10-15 01:26:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 3bda5ead-a59d-3779-a74b-d4dec96da8d5 | -12.3982 | -63.7284 | 2024-10-15 01:26:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 6f3fb0d4-5764-312f-8ca4-257f347de20a | -12.3983 | -63.7093 | 2024-10-15 01:26:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 07c56f79-6544-3e80-a4b8-0bf61ec65cd4 | -12.4602 | -63.0361 | 2024-10-15 01:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 7ddb6041-f736-3d18-ba6d-fc802052b2b7 | -12.4603 | -63.0169 | 2024-10-15 01:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 109.1 |
| f3131348-ebda-3336-9546-bc73d2ebb519 | -12.4961 | -63.2641 | 2024-10-15 01:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 2b47caa7-9d41-3d76-81e4-b22391fb1f06 | -12.515 | -63.263 | 2024-10-15 01:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 5c4eb840-3278-3210-9353-4de6b4195844 | -12.9538 | -62.7962 | 2024-10-15 01:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 9f9eeeeb-1544-3ddb-8c77-a4638de32f51 | -12.9728 | -62.7951 | 2024-10-15 01:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 75.7 |
| b4062858-08f5-3bff-abd2-9a82f78f16c6 | -13.1475 | -62.3215 | 2024-10-15 01:26:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 6dec06d0-18b8-315b-8cca-7068287ac155 | -13.3786 | -61.9582 | 2024-10-15 01:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 16cb464b-5ec9-36e2-9c5d-e411deccf095 | -17.1758 | -57.479 | 2024-10-15 01:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.6 |
| 5b105566-bb7e-38a6-8ce9-2de40c708d3e | -17.1954 | -57.4767 | 2024-10-15 01:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.4 |
| ba000c12-6f3b-36fc-a3a4-db8ab4f83589 | -17.1957 | -57.4562 | 2024-10-15 01:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.6 |
| a592e212-34d2-3de5-bee9-54da9aeb79a6 | -17.196 | -57.4357 | 2024-10-15 01:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.4 |
| a84b2d3c-bb47-3642-882a-dbfbce74b760 | 1.0016 | -52.2164 | 2024-10-15 01:35:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 2fed2f08-0c18-37de-8d09-35b05dfaecd9 | -3.1099 | -54.2263 | 2024-10-15 01:35:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 555b2755-0a02-31ca-bfd7-d02ce569e0ad | -3.1282 | -54.2459 | 2024-10-15 01:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| e91e515b-2244-3c66-8675-c3a3720b9050 | -3.1283 | -54.2259 | 2024-10-15 01:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 069ca90f-9d9e-34b3-8da2-3542178c7583 | -5.5732 | -49.3995 | 2024-10-15 01:35:37 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 86143dab-77b7-3df6-9f9e-5f888646cf51 | -6.5503 | -48.2625 | 2024-10-15 01:35:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 127ab597-2fd8-3706-95ff-a8bdeddcd53f | -6.5505 | -48.2408 | 2024-10-15 01:35:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 95f914e3-6e31-3098-a694-22cbd7c2f994 | -6.5507 | -48.2191 | 2024-10-15 01:35:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 21821204-4a02-3865-96ea-ed42ea064f7c | -6.5689 | -48.2612 | 2024-10-15 01:35:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 146.1 |
| a9e21eae-11af-3f66-b9c4-4ad932ea3ec1 | -6.5691 | -48.2395 | 2024-10-15 01:35:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 266.1 |
| d5bc50be-191a-3a39-bd03-4d5f4d912d07 | -6.5693 | -48.2178 | 2024-10-15 01:35:43 | GOES-16 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 68.3 |
| d9c29f18-57dd-3bb8-9b4a-09fc617f027f | -10.0495 | -47.6589 | 2024-10-15 01:36:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 58299c7f-6ffe-3c44-8619-a4d0accb0c7c | -10.0498 | -47.6368 | 2024-10-15 01:36:03 | GOES-16 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 0f83065c-0e67-350d-bb28-3aa9ca99900a | -10.3711 | -61.1935 | 2024-10-15 01:36:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 161.3 |
| 0b6856f0-cb0d-3d23-bf72-c1521f5225b9 | -10.3713 | -61.1743 | 2024-10-15 01:36:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 226cd89d-7174-334a-b4ae-35321a4363a7 | -10.822 | -49.256 | 2024-10-15 01:36:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 6b03e8c3-cf48-3d27-aa91-9cd4e36d9c4c | -10.9473 | -54.1037 | 2024-10-15 01:36:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 0c175a52-6758-3e33-ba12-a8cb25eea3de | -11.6917 | -65.2243 | 2024-10-15 01:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 3e32a608-c834-3330-bbb9-1580e5520078 | -11.6915 | -65.2432 | 2024-10-15 01:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 07b2eb90-3e71-33a1-8adc-3135bcf6634b | -12.099 | -50.2728 | 2024-10-15 01:36:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 2686d5e6-b5d1-3d7c-a249-3828d5eacfea | -12.3982 | -63.7284 | 2024-10-15 01:36:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 59.1 |
| e33f330e-3e5b-39a8-b0ab-798e0e1c4b28 | -12.3983 | -63.7093 | 2024-10-15 01:36:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 4fc0a4df-e4f1-347b-8844-c7a4bb653640 | -12.4602 | -63.0361 | 2024-10-15 01:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 59c965a6-cb4a-3d67-a62c-367834c02404 | -12.4603 | -63.0169 | 2024-10-15 01:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 6d849de4-5e8f-3e59-be67-c8e3d1b05fb1 | -12.4961 | -63.2641 | 2024-10-15 01:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 8c1fc0e9-c1a0-3ab5-9e0d-4445a1d60c50 | -12.515 | -63.263 | 2024-10-15 01:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 920c5120-a257-3835-a148-3aa8bbff9211 | -12.9538 | -62.7962 | 2024-10-15 01:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 007febc7-8d4a-3b9d-95ed-3e652acf58af | -12.9728 | -62.7951 | 2024-10-15 01:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 81e3beea-6442-3d5b-a92b-c1ee74ed3631 | -13.3786 | -61.9582 | 2024-10-15 01:36:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 48.2 |
| b95ba62f-6e45-30bc-9163-d5fc946826ca | 1.0199 | -52.2162 | 2024-10-15 01:45:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 56.5 |
| af8948d5-fad8-3e67-af2f-df0bba49d4b5 | 1.0016 | -52.2164 | 2024-10-15 01:45:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 1ddcf8c8-b7a3-3932-892a-e19e8606a032 | -3.1099 | -54.2263 | 2024-10-15 01:45:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 8b61cbea-9d5f-3310-80a8-efea3e000cba | -3.1282 | -54.2459 | 2024-10-15 01:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 9b069716-038c-323b-a7c5-e52a2f380d20 | -3.1283 | -54.2259 | 2024-10-15 01:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 695c9a53-f5aa-3b3c-aba7-17a4027e983d | -3.7218 | -48.9979 | 2024-10-15 01:45:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 131.2 |
| 6b63f3b6-dea1-3dfd-9396-c730c20383a4 | -3.7219 | -48.9766 | 2024-10-15 01:45:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |


[Clique aqui para ver as próximas entradas](README17.md)
