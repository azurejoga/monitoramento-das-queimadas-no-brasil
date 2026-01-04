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
| 5a1f1c78-4031-3826-a2bb-bb9e798203e0 | -15.48112 | -39.13946 | 2026-01-04 03:32:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| db2287a0-9245-3859-8d56-b6494cffdba1 | -15.15564 | -39.87706 | 2026-01-04 03:32:00 | NPP-375D | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 43596e42-31cd-3f5b-be03-62553fb630b0 | -15.15657 | -39.87208 | 2026-01-04 03:32:00 | NPP-375D | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 77c8521a-6f20-3ff2-bea4-ef6261bb2fba | -21.25395 | -48.65454 | 2026-01-04 03:34:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 505990c3-acf7-3436-8506-122180bfa18d | -26.48448 | -50.89753 | 2026-01-04 03:34:00 | NPP-375D | PORTO UNIÃO | SANTA CATARINA | Brasil | 4213609 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fa97fd96-1263-3151-b224-374e0f690fd1 | -21.25225 | -48.66141 | 2026-01-04 03:34:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| bc260eb4-ec09-32e3-8176-842e02223c00 | -21.25012 | -48.65883 | 2026-01-04 03:34:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ce5db6bd-7ae5-3bec-bfe3-7383eca9c4d8 | -21.25704 | -48.66069 | 2026-01-04 03:34:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3e9a588f-26e5-376d-a702-92516f4cc70b | -3.88959 | -42.52512 | 2026-01-04 03:46:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d6926956-3047-3a0d-8f32-e3837a68f0ff | -4.62655 | -37.93888 | 2026-01-04 03:46:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| efeea747-d6c5-3e96-ba74-11d196e60053 | -2.44608 | -47.10633 | 2026-01-04 03:46:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7cde6190-4c87-3397-93d4-cb9ebe349737 | -4.00263 | -38.32744 | 2026-01-04 03:46:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 774dd2fa-a9cb-35a9-97a8-7f57beba8506 | -4.62598 | -37.94247 | 2026-01-04 03:46:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bb0cc7da-6681-3a72-b6f7-0ed00654571b | -2.44664 | -47.10991 | 2026-01-04 03:46:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4377dbeb-999f-399d-ac26-2d801139915e | -2.75843 | -45.09251 | 2026-01-04 03:46:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9f1be6d-774f-325c-accb-97bed21b81d3 | -2.44532 | -47.11095 | 2026-01-04 03:46:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9b023e2-35b0-3cb1-ac9e-aa48811d2d86 | -2.75896 | -45.08923 | 2026-01-04 03:46:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d200d5bd-c29f-3c1f-a3bd-2d20b0adc33c | -4.18515 | -38.48269 | 2026-01-04 03:46:00 | NOAA-20 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 799c4d36-9928-3937-a61c-cfe497074918 | -2.44744 | -47.10527 | 2026-01-04 03:46:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffe81382-b38e-3732-ad79-e4f98feae3bb | -2.54172 | -47.47646 | 2026-01-04 03:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30b88926-eb31-3e2a-9ebb-1441ee47a4f8 | -2.08181 | -47.10568 | 2026-01-04 03:46:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c38b084b-1bb0-3f0f-9f63-c59cdac88a74 | -4.00323 | -38.32372 | 2026-01-04 03:46:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e64b1519-9ea6-3db9-a952-f6384d45bb55 | -3.89464 | -42.52164 | 2026-01-04 03:46:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 30d73d15-68b2-3be5-9416-4d62e8c1dd58 | -5.28868 | -36.27438 | 2026-01-04 03:46:00 | NOAA-20 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 10270c92-a5d2-3abc-b990-7a551309ab6c | -2.54089 | -47.48139 | 2026-01-04 03:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b08e55bd-f05f-3399-8376-bee9cd7c9538 | -2.76425 | -45.09012 | 2026-01-04 03:46:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd93809a-b4c9-3683-9f61-d26dad8f6ddc | -5.04887 | -43.60868 | 2026-01-04 03:49:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d992f3b6-604e-3741-ab6c-3d4e3ca3d979 | -9.94651 | -36.38493 | 2026-01-04 03:49:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ba7b17df-9071-3b93-872f-330756f2a78b | -8.05263 | -38.25003 | 2026-01-04 03:49:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f208b04a-74ad-37da-8341-9d46a693f267 | -5.47782 | -36.62691 | 2026-01-04 03:49:00 | NOAA-20 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ec39cfc2-495c-3205-8781-cfc8ef4a88d1 | -6.56386 | -35.25473 | 2026-01-04 03:49:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| adafe433-8695-3a28-9a08-8512b5f9a02b | -9.8029 | -35.9323 | 2026-01-04 03:49:00 | NOAA-20 | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ef5e614d-f646-311d-89df-e6241d7aed12 | -5.04508 | -43.60308 | 2026-01-04 03:49:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2eb67d3f-998a-36cf-8338-63de2f510fa6 | -5.04966 | -43.60396 | 2026-01-04 03:49:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 239234b4-6fb3-3a64-9dbb-ee3b056c1c0e | -8.20389 | -35.9071 | 2026-01-04 03:49:00 | NOAA-20 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 785f6bb6-1f08-37de-9e01-202418a5bfa5 | -6.56046 | -35.2542 | 2026-01-04 03:49:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 90a41b89-92e7-3849-834c-52b0d81c0c1f | -5.03589 | -43.60146 | 2026-01-04 03:49:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1366893-8c14-3800-8457-c8ccb89da206 | -5.2329 | -38.16021 | 2026-01-04 03:49:00 | NOAA-20 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b1ae08ff-fa99-3730-81ed-9eae639db135 | -5.04048 | -43.60226 | 2026-01-04 03:49:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0db7d4b-d7dd-3ad0-b997-879d8eb97487 | -5.04127 | -43.59756 | 2026-01-04 03:49:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb73d2d3-0819-35dd-9ef8-53a41ac4860b | -7.09571 | -38.78691 | 2026-01-04 03:49:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e054b39b-965f-30c0-bfd6-eb4420afce55 | -7.15847 | -35.09756 | 2026-01-04 03:49:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 85535c30-5487-386e-a790-95ba911a97f2 | -5.04428 | -43.60783 | 2026-01-04 03:49:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94b16dd6-5427-372a-9132-e4551cb67130 | -5.9261 | -35.84597 | 2026-01-04 03:49:00 | NOAA-20 | BARCELONA | RIO GRANDE DO NORTE | Brasil | 2401503 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| dd8025f8-70a6-3419-aac4-54a850a981b5 | -5.37927 | -36.81963 | 2026-01-04 03:49:00 | NOAA-20 | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 9da8415a-4eaf-3c84-a0e1-15ca2302b3ce | -9.51703 | -35.90383 | 2026-01-04 03:49:00 | NOAA-20 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e9028541-9a8a-377d-b529-c1c91817aefa | -7.41634 | -35.26571 | 2026-01-04 03:49:00 | NOAA-20 | CAMUTANGA | PERNAMBUCO | Brasil | 2603603 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1da6303c-c042-35b5-b56b-cc01f96dd912 | -7.38307 | -35.20822 | 2026-01-04 03:49:00 | NOAA-20 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 56bbd9dc-6914-38ee-b612-4f43660d110f | -5.48059 | -36.63089 | 2026-01-04 03:49:00 | NOAA-20 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 72910c12-0f03-32bb-a013-a27d0ba4111f | -6.56102 | -35.25053 | 2026-01-04 03:49:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6c86ed53-6d08-3354-a0bb-778d9354721f | -11.15226 | -38.05059 | 2026-01-04 03:49:00 | NOAA-20 | TOBIAS BARRETO | SERGIPE | Brasil | 2807402 | 28 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ab7b6f29-976b-3721-ae24-7ca0a8206d16 | -9.94595 | -36.38854 | 2026-01-04 03:49:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 85a58fc9-17f9-389f-816b-0603fac5aaf9 | -7.65097 | -34.96975 | 2026-01-04 03:49:00 | NOAA-20 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9b50af7a-8ecb-37d8-b499-0e93dc80f49b | -5.51456 | -39.43469 | 2026-01-04 03:49:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 78a31862-65ec-3642-a800-6aff5f4a42ba | -18.47971 | -39.858 | 2026-01-04 03:51:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7117cfe6-d0ac-3e3b-b7db-181279f1997b | -13.42937 | -43.85537 | 2026-01-04 03:51:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b14ad5fc-993e-3100-bd39-2b853be26336 | -15.48298 | -39.1395 | 2026-01-04 03:51:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a3e8d9b5-525e-3cb4-8ac1-b62e885547f0 | -13.7954 | -39.00833 | 2026-01-04 03:51:00 | NOAA-20 | ITUBERÁ | BAHIA | Brasil | 2917300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| fbb0e12c-6a53-32a6-b21c-d26f0672675c | -13.47267 | -38.94391 | 2026-01-04 03:51:00 | NOAA-20 | CAIRU | BAHIA | Brasil | 2905404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 23d04101-1057-3016-958e-2874e7fa787b | -18.47582 | -39.86106 | 2026-01-04 03:51:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8cc0534e-f98d-3935-9a0c-83fc98f13a73 | -13.79815 | -39.01244 | 2026-01-04 03:51:00 | NOAA-20 | ITUBERÁ | BAHIA | Brasil | 2917300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 5e363b6b-734b-309e-b552-3cbfa2ca549b | -15.48572 | -39.14363 | 2026-01-04 03:51:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9729cd87-5efa-3094-b90d-6037a4db285f | -13.80146 | -39.01299 | 2026-01-04 03:51:00 | NOAA-20 | ITUBERÁ | BAHIA | Brasil | 2917300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e07cd7f5-ecc7-3631-adf1-dae43ede5b0b | -18.47914 | -39.86163 | 2026-01-04 03:51:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 73500ba0-25c5-3b53-a364-c27b7ebd32ee | -15.15493 | -39.87374 | 2026-01-04 03:51:00 | NOAA-20 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 090b60f9-0ffa-3f78-bdba-5953486c7c5a | -13.78876 | -39.00722 | 2026-01-04 03:51:00 | NOAA-20 | ITUBERÁ | BAHIA | Brasil | 2917300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 798141d0-60ba-35d3-8621-f30f1a8e648b | -15.15435 | -39.87737 | 2026-01-04 03:51:00 | NOAA-20 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5cd03c6f-c2c1-37d1-b901-148ceca0cbcd | -13.79208 | -39.00777 | 2026-01-04 03:51:00 | NOAA-20 | ITUBERÁ | BAHIA | Brasil | 2917300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 67f4413d-4f4f-38a5-b6eb-db44376140ef | -18.8235 | -51.61703 | 2026-01-04 03:53:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 554c1e5b-d7b1-32c9-bf5d-3e19ae78cdf5 | -21.25426 | -48.66045 | 2026-01-04 03:53:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 9a70ae7a-b68c-31e9-963b-a4a63e15dc40 | -20.84599 | -49.56551 | 2026-01-04 03:53:00 | NOAA-20 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 84a81a96-a610-30ca-b856-50e121c9eee9 | -21.26367 | -48.63924 | 2026-01-04 03:53:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 954e8e2f-c906-3326-b636-27b1550b70be | -18.81596 | -51.61699 | 2026-01-04 03:53:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 48c5e1b2-6096-3e89-92cf-8dc058c94d73 | -18.81963 | -51.6062 | 2026-01-04 03:53:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2c80b26f-a4f6-36a3-a677-c578df5a5a92 | -18.81805 | -51.60751 | 2026-01-04 03:53:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7fd3ce59-e249-372a-b0c4-9b97ef21da78 | -18.82454 | -51.61243 | 2026-01-04 03:53:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bea5ea4a-00b1-3081-b0e0-52547a59f934 | -18.81642 | -51.62035 | 2026-01-04 03:53:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| eeade2a2-7ef6-3a97-8f84-1d0d4bbc8457 | -21.25542 | -48.65487 | 2026-01-04 03:53:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 2c6ba9d4-3035-33a8-b1e1-06d656f5404f | -20.85107 | -49.5668 | 2026-01-04 03:53:00 | NOAA-20 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 692fa07e-99bc-3ba5-8c7f-72f5b6f360f9 | -18.81748 | -51.61567 | 2026-01-04 03:53:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4d7982a7-afb9-3aa9-8ebc-525134f986e2 | -18.81096 | -51.611 | 2026-01-04 03:53:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f878e060-fcb6-383e-a5e9-84245873ab72 | -18.81252 | -51.60968 | 2026-01-04 03:53:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10bf39f2-077e-3011-9a6c-0a10072cbaa9 | -18.81855 | -51.61097 | 2026-01-04 03:53:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2f2d7959-9217-3533-b926-169010c01d16 | -18.817 | -51.61228 | 2026-01-04 03:53:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ae87cf8a-d097-3a27-a225-6569eed801bd | -26.48244 | -50.89791 | 2026-01-04 03:55:00 | NOAA-20 | PORTO UNIÃO | SANTA CATARINA | Brasil | 4213609 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cf06cdbf-d031-31bf-b539-9e6ad723d1af | -26.48381 | -50.89196 | 2026-01-04 03:55:00 | NOAA-20 | PORTO UNIÃO | SANTA CATARINA | Brasil | 4213609 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8bf91f54-0aae-3dd3-99b1-3ba2a84dcf15 | -26.48239 | -50.89748 | 2026-01-04 03:55:00 | NOAA-20 | PORTO UNIÃO | SANTA CATARINA | Brasil | 4213609 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 73f64746-1955-3b0b-b81f-c2fac58ed467 | -2.39243 | -47.60327 | 2026-01-04 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb5219b7-7b6f-3e40-8c07-aae3f0e73536 | -1.25475 | -53.48163 | 2026-01-04 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d3293b99-b8c5-3722-9b70-6ef1acdc3d2f | -1.01129 | -48.88432 | 2026-01-04 04:38:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee1d8cc4-ab9c-3a38-b0d3-63b38e68b8fd | -1.92801 | -46.45959 | 2026-01-04 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 056df3c9-2191-3043-8322-3ac29ef3e441 | -2.84882 | -46.74291 | 2026-01-04 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed63de70-348a-3943-8125-46f35dca935c | -2.38964 | -47.59924 | 2026-01-04 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0db5eb78-5898-3bf9-9545-6cc59734de23 | 2.55143 | -60.3665 | 2026-01-04 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 14.8 |
| f602ef2f-8b15-3222-8b8d-d8905a2d1397 | -2.39189 | -47.60677 | 2026-01-04 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f7bb61c-9027-345e-9344-f0210458130b | -2.63432 | -47.31458 | 2026-01-04 04:38:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fa7b2ff-da89-3461-bffd-8c29573d5c6a | -2.57861 | -54.72536 | 2026-01-04 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff011985-b97c-3316-a835-08a751dd4476 | -1.14486 | -54.17391 | 2026-01-04 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c3b99e2-a9f6-3f5e-9465-0d59a65cb231 | -2.90263 | -52.63628 | 2026-01-04 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f21389ba-8561-3abe-89cb-d436edfb57ef | -2.3891 | -47.60275 | 2026-01-04 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README3.md)
