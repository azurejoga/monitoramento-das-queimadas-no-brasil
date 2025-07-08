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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 263e27a9-d76b-34db-80ea-ffa301c8ca61 | -10.6489 | -49.4483 | 2025-07-08 03:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 25dad60f-05e1-3ac2-bd60-b1bbf2de9375 | -10.6299 | -49.4504 | 2025-07-08 03:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| e50653df-f2b7-370f-bfd3-9c267901c7bd | -11.4201 | -45.1181 | 2025-07-08 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 0630e234-d11f-3988-8aff-6b59e4e00b6a | -11.4393 | -45.1154 | 2025-07-08 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 85c2947c-31a2-3a50-b3dc-a8c7c442cb1f | -10.6489 | -49.4483 | 2025-07-08 03:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 6ccc7363-3c77-3ecf-84fc-bf84c64f167b | -11.4205 | -45.095 | 2025-07-08 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 9ff35081-affb-32d8-bc70-3bb33556e2ca | -11.4397 | -45.0923 | 2025-07-08 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 3e237c99-f5bd-3df2-8bd2-8ff9c85365c7 | -10.6486 | -49.47 | 2025-07-08 03:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 172cf601-be84-3f84-98ac-1c2141e85189 | -11.4201 | -45.1181 | 2025-07-08 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.7 |
| efc0ed4c-8f4e-32b7-be84-2e2967736644 | -11.4397 | -45.0923 | 2025-07-08 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 922dade4-8f58-31a2-8932-9bfa2e133c76 | -10.6486 | -49.47 | 2025-07-08 04:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| ea1b799e-df70-3c68-90f9-894908fbcc96 | -11.4205 | -45.095 | 2025-07-08 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 56f2e7c0-024c-3ae4-bc7c-9f0eba2ca8c5 | -11.4393 | -45.1154 | 2025-07-08 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 5c203fff-6ad9-3b71-96d7-ceb79eb7b690 | -10.6489 | -49.4483 | 2025-07-08 04:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| acef201f-1cde-395f-a36e-13eabd42d6f3 | -10.6299 | -49.4504 | 2025-07-08 04:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 2e2c2ab5-5033-3df7-9dd3-c6e9e3e2f2a2 | -11.4393 | -45.1154 | 2025-07-08 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| da34f7bf-1038-38e4-9ba5-5ec463252e98 | -10.6489 | -49.4483 | 2025-07-08 04:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 7867a12b-d4ee-392e-a1c3-66f4421775e0 | -11.4397 | -45.0923 | 2025-07-08 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 848b3e0c-1c52-3665-bea4-e2095b812152 | -10.6486 | -49.47 | 2025-07-08 04:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 498fe4a2-0c04-39ac-966d-67629dad4d2a | -11.4205 | -45.095 | 2025-07-08 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 63d067f2-ab98-3bb4-9b4b-1dc4ba6ad46a | -10.6299 | -49.4504 | 2025-07-08 04:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 53a3c923-c618-39e6-b0aa-b4742906e755 | -11.4201 | -45.1181 | 2025-07-08 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 95d1aeaa-b568-38ee-84f6-5b25d5671b41 | -6.82542 | -43.59134 | 2025-07-08 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11480865-d1dc-38d9-80a6-88a606a75b94 | -6.67212 | -43.76574 | 2025-07-08 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e53b51f-505d-3137-b278-d7ca75db6a5c | -5.32373 | -50.05817 | 2025-07-08 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bd8734b-c904-32a4-9dbf-2cbade83672e | -7.78634 | -44.57374 | 2025-07-08 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 824826cd-1dcb-363a-87c1-cc3e549be452 | -7.10393 | -44.15506 | 2025-07-08 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d1d099e-09b3-3719-aa7e-86dc3a1dbd0c | -7.25844 | -43.08287 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 09ced86c-4a3c-365d-9473-4ab7de8e863a | -6.84282 | -42.84722 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9a2f2695-fcbd-33f0-bc7d-ac575763725e | -10.18921 | -43.30485 | 2025-07-08 04:14:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b3ac15c9-be5d-348f-9635-84c7ac400705 | -9.37448 | -48.95489 | 2025-07-08 04:14:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe35841e-7dbf-31e3-8997-d9e54adad637 | -9.18024 | -50.1803 | 2025-07-08 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 56da71fd-f030-3a5b-83b6-fd20472a5576 | -5.40969 | -46.07034 | 2025-07-08 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a251e7e7-ce70-3e22-bcf9-7b382e04f7c8 | -7.10448 | -44.17315 | 2025-07-08 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 464b4192-00bd-31d0-a552-222de18ba69c | -6.82212 | -43.59082 | 2025-07-08 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 17ed5c6e-70fd-3d01-82ed-5ee1db8dbeb1 | -7.10835 | -44.17017 | 2025-07-08 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8849117-f827-3e8a-ac6f-5706deefb085 | -8.95949 | -47.27825 | 2025-07-08 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2f9e659c-7cf1-35fa-b461-b506a75dc681 | -4.30887 | -48.07354 | 2025-07-08 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a366d2f-e7d7-3d2e-a8dd-4af5398ef9c2 | -6.76106 | -43.41495 | 2025-07-08 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c1d594fa-37aa-3db9-aafe-890fc974dd07 | -5.79377 | -47.02245 | 2025-07-08 04:14:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83b12d37-0db1-3ec0-9dc6-151999526fdf | -7.09618 | -44.16106 | 2025-07-08 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2668adc8-5795-3a63-82a1-a987507c2100 | -6.8829 | -45.23955 | 2025-07-08 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6484125c-08aa-3f03-88df-3e483f8bf14d | -7.23075 | -49.59449 | 2025-07-08 04:14:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3625515-b1f4-3655-893f-b521f6bb46ce | -6.89053 | -47.39771 | 2025-07-08 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a164cba-1a56-3c6c-ab26-2ea0f19f217b | -4.30478 | -48.07286 | 2025-07-08 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 90321ff7-2bc3-37c7-bf0b-fe4eb6ee2ee2 | -7.14962 | -44.01589 | 2025-07-08 04:14:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 485641ee-4be2-3649-8d2d-0f92ef15df35 | -7.25513 | -43.08235 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a6efaefc-7a4d-395c-a39b-63aa6d5464a2 | -7.20133 | -43.12361 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 08f82a0c-55dc-3b99-95e5-c1ee320f6783 | -6.75998 | -43.42185 | 2025-07-08 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9d90a60c-ae0d-3bbd-b67f-51e893f6a9dd | -4.42583 | -48.14609 | 2025-07-08 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a333bc6c-6ec2-36eb-bee4-02fbd7195863 | -7.14631 | -44.01537 | 2025-07-08 04:14:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24857cf1-f948-340a-8076-7152592f0b56 | -7.31887 | -43.87183 | 2025-07-08 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4eb52c4-61be-3e74-8748-cdfb1be98a60 | -9.17971 | -50.17716 | 2025-07-08 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bb9dd78a-5169-33bd-a6c3-dcdbe79e7ebe | -7.0995 | -44.16158 | 2025-07-08 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3e0dcf9-4414-37c2-a97f-bd64cb70e161 | -6.26636 | -45.27244 | 2025-07-08 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 051c0f2d-31b2-3424-8f17-5525f8fe4166 | -7.48522 | -43.9376 | 2025-07-08 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e7f58ccb-c6fd-350d-b21f-738886167b31 | -6.97851 | -44.28185 | 2025-07-08 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99d1b1b6-9922-3d4b-aff7-b18afff61e3a | -7.57222 | -47.06249 | 2025-07-08 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a364ccc-1ad6-38f2-a1f4-8a3dbb371fd3 | -9.20252 | -45.34038 | 2025-07-08 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0d42dba-7a62-3ad9-8a1a-ac1bcbb7861e | -4.28158 | -48.19039 | 2025-07-08 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 36a477c6-6829-3d78-a2dc-1f5ca8d40299 | -7.74295 | -41.96828 | 2025-07-08 04:14:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f7afb858-395f-3c98-85de-73c9146b840a | -8.15473 | -47.62622 | 2025-07-08 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c4be8d58-2732-3f2e-82eb-84f78bc68125 | -8.21448 | -44.9377 | 2025-07-08 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2255d5fa-e04e-330f-b1ab-2a100b491e72 | -8.30074 | -45.14304 | 2025-07-08 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f34c8c47-c834-3f10-ae6f-7b1e48d23a23 | -5.65611 | -46.59312 | 2025-07-08 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5458338-d6a9-3994-b739-17adf0219ce9 | -8.0666 | -43.11411 | 2025-07-08 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8d46d00e-bcb1-3850-9c0b-c53e01f21f47 | -9.19916 | -45.33983 | 2025-07-08 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1bb1911c-4fd1-3335-8b44-2c828f2f728a | -5.41558 | -46.07038 | 2025-07-08 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 82ba968d-7e44-3691-9158-9fa4c90fbad0 | -7.19088 | -43.12552 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 6f88f931-5fab-386e-aa4e-8fa62b64e8b4 | -7.11 | -44.15966 | 2025-07-08 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c971593c-4756-3350-8187-0d3c8f91fc3e | -6.52985 | -43.54426 | 2025-07-08 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b64112cd-215d-32e6-a6c6-2997e72141f3 | -7.03856 | -43.44786 | 2025-07-08 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c52026ef-0375-3427-b289-d44caa2739e7 | -7.25183 | -43.08184 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2a55c711-96e2-3bc4-aafc-b33f38819b1f | -6.19042 | -45.17632 | 2025-07-08 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd99e08a-529f-31a1-8931-6b1e714b31d4 | -7.28162 | -44.6422 | 2025-07-08 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cadc4f54-e462-3309-80a2-9168c559d4b8 | -7.24437 | -46.7261 | 2025-07-08 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2ba9ffc-859a-3e83-9db5-1727ab96fcba | -7.73957 | -41.96776 | 2025-07-08 04:14:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 062ef6dd-e61e-3105-a09a-d77ad9516e59 | -6.88973 | -45.24059 | 2025-07-08 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6586d406-9bdd-3bb8-bd9f-1f70b8cb79a4 | -6.96108 | -42.80864 | 2025-07-08 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 885bb08a-8b19-3e5c-949d-3830f6e25d02 | -7.28024 | -44.61246 | 2025-07-08 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8016852c-f971-3d51-a04d-409ed298bd12 | -6.34762 | -46.36313 | 2025-07-08 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3126be19-ae6f-3a7a-8afe-9c2cce69a4a4 | -7.28091 | -44.49984 | 2025-07-08 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ca4e505-7459-3acf-baae-862bcd3a96b3 | -6.6739 | -43.86195 | 2025-07-08 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6af68605-5f70-3d41-8170-927ddae29232 | -5.41261 | -46.07508 | 2025-07-08 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a3ee41a5-caa9-37cd-bed3-3108dc48e3ae | -5.2361 | -46.03863 | 2025-07-08 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 32a50a43-eb0c-33be-9957-65c44f1c2b3e | -7.11222 | -44.16721 | 2025-07-08 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e80e0d74-7501-3bc4-bf71-55de9b02f63d | -4.42681 | -48.14631 | 2025-07-08 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 87cafae5-32e3-3861-afbb-61ee16d040c5 | -7.19364 | -43.12949 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a6f3fc7b-8e97-35b0-8e80-73d259bd78b6 | -7.2529 | -43.07491 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 3fc9ee10-7d57-38c7-9f23-1791be2a69b2 | -8.71231 | -50.00431 | 2025-07-08 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d368763-2a3d-3aa6-9929-d0229ee04d7b | -6.26293 | -45.27186 | 2025-07-08 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e2d3d27c-3f00-32c7-a003-1b40b6b03ae3 | -8.98424 | -49.18443 | 2025-07-08 04:14:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6ea3de2-c674-3589-a16a-fe6c049c23d0 | -8.9602 | -47.27397 | 2025-07-08 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9084e6c8-e961-32fa-9532-b84ae44c4868 | -8.70577 | -50.01616 | 2025-07-08 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bbf90c2-64b9-357e-9867-a8efc0fdf491 | -6.00952 | -44.53124 | 2025-07-08 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67224718-33a0-3261-8493-f973553e5d1b | -7.20355 | -43.13104 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 162c2653-5238-3804-8bc0-8465bea1dcbc | -7.25898 | -43.07941 | 2025-07-08 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| af44e9ac-25dc-3b25-8ff7-61dacd3975bb | -7.31237 | -44.98896 | 2025-07-08 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cbf49a8f-ea8c-3681-9642-0d8d9c18655a | -6.67542 | -43.76627 | 2025-07-08 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee1f5fa6-1fe1-3dd1-9cea-ac18782d6bd3 | -9.2213 | -48.59635 | 2025-07-08 04:14:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |


[Clique aqui para ver as próximas entradas](README6.md)
