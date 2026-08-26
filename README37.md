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
| 2b76deb2-18a0-3ddb-a815-d9a8a1ca61d7 | -6.86592 | -59.40654 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4284f5fa-e062-3cc7-b0cf-3dbdb0daeb7c | -5.14786 | -56.27225 | 2026-08-26 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38d21c3a-1988-3ef1-96b6-db0db67fb56a | -6.62376 | -58.49564 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af1ea98c-0368-3044-b29b-426f23965f74 | -3.13731 | -61.19067 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b4d353f-08bd-3f77-826d-4ce15eca1665 | -6.71089 | -55.59203 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9c18d5d-7ed5-3c0b-a177-11d69e8492bd | -6.24737 | -55.43015 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 191f93a8-2ad6-3295-a9e5-fe7bfec713e6 | -8.17614 | -54.95617 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 67e1956f-d9ea-3e82-8257-3b11c3d72dfd | -6.25509 | -53.37484 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 834b3f59-667a-3ef7-8f29-b2e1efebac04 | -6.62088 | -58.48722 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 05d39533-2dde-3ae0-a9f5-02ee1f517264 | -8.61263 | -54.68436 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f65aca0-16e0-33a5-b426-aa4380050f70 | -9.39715 | -45.50685 | 2026-08-26 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7065c315-5df5-351f-973f-c75a13d827dd | -6.8312 | -59.94441 | 2026-08-26 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b9ecb2f-0881-3370-bbc1-909a380308c6 | -6.13495 | -57.82821 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 901bbab6-1576-37ef-8586-e51284551518 | -6.13306 | -57.86486 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f63e004-8272-321e-a76e-9721bc9c1acc | -6.14911 | -57.94546 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aaa7d003-d915-3bd1-a031-2c5f71cf8f5d | -9.03819 | -50.80312 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a40c08d4-e078-3a57-8e84-2a373d6aa5a1 | -8.5357 | -54.83984 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bff0a565-e467-3d59-8f0a-bec690046edd | -6.71799 | -59.12984 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ad9ac7d-5c57-36ea-84ac-01f384a88df7 | -7.38317 | -55.18799 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6aec1dcb-0f30-3518-ad9d-df05d6adda4e | -6.30567 | -53.57248 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62b2d4a6-7f70-3854-8ff6-856257d072bc | -3.50811 | -48.0388 | 2026-08-26 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 816ac534-139d-3611-9ea2-4792c4c4b959 | -8.75956 | -44.24729 | 2026-08-26 04:51:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0340e27e-2423-39a1-b9e2-907d25bdd4e3 | -8.76683 | -49.97313 | 2026-08-26 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d6acf02d-3964-3c64-8709-9ad7746ca682 | -6.54644 | -58.51435 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e3d758b-712e-3d44-8cb4-02534f528b61 | -5.77516 | -57.5497 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e28071e-00c2-3665-92e9-91a3c65b0cb3 | -6.3288 | -54.73708 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 666d8475-4c1e-38f5-bec7-c7ebae24dff3 | -8.8199 | -49.60844 | 2026-08-26 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ac443e30-3af2-3f02-bdff-8d3bdaedbe5a | -6.71786 | -59.45086 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d54d4dc9-647c-32a4-b4f2-c2f9be12e14a | -6.42069 | -54.93276 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b96aaa9-b660-38dc-a95a-fb9bcbe34ce3 | -8.61509 | -50.01694 | 2026-08-26 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79aaae77-bd02-3c92-b76e-c8e04e3a2845 | -6.82656 | -58.65668 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| acc5fa8d-6fdf-3655-b6ab-40c8aac85cb2 | -5.94574 | -57.73386 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16693fc8-5d6d-3599-a709-abcb1f8b46f6 | -7.38527 | -55.15335 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a46598a2-b0b2-39eb-bcf9-09338c0df826 | -3.77778 | -59.27883 | 2026-08-26 04:51:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03084835-0f0f-3bdc-8688-6d5d1af0f040 | -9.66141 | -48.31373 | 2026-08-26 04:51:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 135a0279-2f43-3c40-9b0c-0bd6eefec1d9 | -6.81196 | -58.61448 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6313897e-b239-3e22-af13-cafd8ad1ddc0 | -8.60844 | -54.86282 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db2190a2-b8db-329a-ad08-1f379c8c441a | -8.3326 | -46.49502 | 2026-08-26 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9383ec63-62b2-39fe-b3df-2f4ebd421d3d | -3.59445 | -50.67799 | 2026-08-26 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 68a1526b-bb9f-3367-92fc-37b66eb3d11d | -6.43842 | -54.97013 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc13c7bc-de7b-3346-8744-eaa3daf8b0eb | -9.04815 | -50.81535 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8f20f289-a06b-3b21-af65-f258ea22b73a | -8.11101 | -51.6677 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d29094d7-89e2-35a6-a6bf-98d35ac30805 | -8.17233 | -54.95513 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 919b3e58-e30a-349c-b253-c0fd1ccb8ac4 | -6.7753 | -59.43755 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 45579ad0-806b-32bf-810e-b23a18e0e5a6 | -6.80797 | -58.61293 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0058d930-c159-342a-87fb-4a8bfbbd6338 | -6.18559 | -53.49265 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 999263fe-5471-33b4-a5a0-350802dd540c | -8.09793 | -47.56541 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e31893e-bfc1-3fdb-869b-048ec97b8110 | -7.37776 | -55.18383 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43257440-2a92-3eeb-adfc-a7300fc5bcae | -9.04463 | -50.81493 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8527df51-559c-393a-bfa0-27b61fcd1099 | -5.95619 | -53.58885 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49b56e15-898b-3480-861b-8598852d45c1 | -3.51259 | -48.03481 | 2026-08-26 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 981d06b9-fa24-328d-aadc-f491f87b7b69 | -8.59383 | -54.73709 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d1ca44e8-53de-34d6-8ad8-35e67a1367d4 | -6.88891 | -59.40592 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47369101-8001-3e56-a152-14c2aa0487c8 | -9.91262 | -46.47742 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b834243f-b0df-3cf5-8af7-d1420bd0a10d | -5.98301 | -55.71361 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 962efac2-c311-331e-bd62-c377f9d4e8af | -7.76418 | -44.76565 | 2026-08-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a810a74d-a040-35a7-bc48-bf1a9e30a783 | -9.04459 | -50.79083 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bc682458-5521-3d1d-af2e-79b9ebdb79b6 | -6.24659 | -55.47916 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2eec979-19f3-37aa-8855-536016918213 | -7.07235 | -59.22788 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a073bce7-55fd-3b7d-a770-e25cfd9c8b52 | -9.03646 | -50.79084 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ca76a518-d3cf-393d-9d4c-846553f15b30 | -10.06165 | -48.45311 | 2026-08-26 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b97941ab-7a68-3886-92ae-8d905e71097c | -7.51725 | -61.38712 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| c5ddb236-cd7a-372b-a00d-7692b9dc1524 | -6.94109 | -52.79497 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8c8259d-a47a-3b1a-a5d3-2172099c8e63 | -6.01663 | -45.81134 | 2026-08-26 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9e148ac9-c79e-3a42-bb5a-f56e7629a8e4 | -8.16874 | -46.19376 | 2026-08-26 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3915562f-5891-3fa5-8ae5-18eafed2385b | -7.0303 | -59.23553 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5986edcb-25e2-3c28-ba22-c576cf680b38 | -6.25674 | -53.3644 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 252d317c-9711-3c42-9e40-89fc839aaa6d | -6.77722 | -59.44206 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0803960b-3bc2-331a-be2f-72b424f9757b | -7.25883 | -49.85321 | 2026-08-26 04:51:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 898688f6-8771-3ac7-a2a7-25befaa9177c | -6.63371 | -58.51335 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5f3b23d3-3a94-31fd-ae89-2bea615a7f22 | -6.83055 | -52.50084 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca0d6e05-d7c0-3c4f-aa7b-f5e69be98a50 | -8.75905 | -44.24795 | 2026-08-26 04:51:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cb8ea2ab-0ebc-3f1b-929b-61a2b943c4de | -9.44964 | -51.67531 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c45d529a-d8e2-3d59-9f2a-9a9888f9d110 | -6.83663 | -52.50532 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55a5233d-0d2e-3eec-ae4b-7dbce95e92f0 | -8.59672 | -54.71897 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09f441d7-fcf1-3087-bd58-0c65c76eaa42 | -1.85788 | -55.5267 | 2026-08-26 04:51:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7407285-f18b-3ae3-97db-ccad39b21bb4 | -7.02775 | -59.22488 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d9741b2-e4d7-328e-b24d-cef03c33f285 | -7.39095 | -55.16199 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cfa3f0dc-66b5-3eff-ac66-89fa056e6f01 | -8.03019 | -51.81413 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42545ced-d8d0-3040-b2d6-5e326726362f | -3.54594 | -58.65073 | 2026-08-26 04:51:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92cd7c6c-d452-3e7d-a50b-7327a5f3b2c8 | -7.39564 | -55.15491 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 33033e02-6d2a-3220-9e9d-07872e80631a | -7.13657 | -43.17792 | 2026-08-26 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 101ac990-b18a-391e-b7ee-40726e437661 | -4.89069 | -56.27306 | 2026-08-26 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6c9d22a-024c-3c8b-bfee-3cb65313dfa9 | -7.11085 | -56.56921 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc30100b-8e86-37e3-a5c0-bc26f1cbe3d4 | -8.20223 | -54.96776 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c89b1f4e-5e49-3814-a4d1-23e6ee39a1ba | -8.57656 | -55.28051 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da780add-860b-3f1c-bef3-ea088290a9bd | -6.8259 | -58.66055 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2e28aee6-3667-3208-8a62-60c53a7cf96a | -6.33163 | -54.74139 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d7af415c-e693-35e4-8790-bba70d7f83f8 | -6.14684 | -57.70636 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17b536ef-c8ee-3a43-b8be-919573f55481 | -8.6405 | -54.74832 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7702665-fdd7-355f-b895-d54f6a06d084 | -7.28848 | -45.358 | 2026-08-26 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe84390d-3855-34f3-88d5-252ebfa3c163 | -6.11811 | -57.82932 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cd1dcf98-ca7b-3929-ba7d-cff0b9b5fb11 | -3.9671 | -43.1074 | 2026-08-26 04:51:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9f7e69b-84b7-329a-b86e-75a16507c6f4 | -3.5157 | -48.03994 | 2026-08-26 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 23521539-c6e1-35e0-8afc-6a466ebceb6e | -8.62536 | -54.73472 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4fce457-7816-357c-a311-63f9bf768403 | -5.97455 | -57.63365 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0776b4f8-fdc5-3cf7-a3c4-196b502af3e7 | -6.84379 | -52.50288 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2174201-af47-387c-932b-a6bcf2dffddc | -6.81043 | -52.49768 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5320813-4432-3441-b883-f9c2320496e5 | -7.28749 | -44.08641 | 2026-08-26 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3f6e7b39-2eba-378f-8464-93ac5b8d0570 | -8.77471 | -49.96999 | 2026-08-26 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README38.md)
