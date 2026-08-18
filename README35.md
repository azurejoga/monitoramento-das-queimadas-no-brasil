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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4974e4ab-b320-3b7b-9d22-e30bcbb6b7fa | -10.77043 | -50.36988 | 2026-08-18 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3778f4e4-a5dc-3f72-b4b4-be589ef76ade | -8.57626 | -54.74083 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 27e16f55-a88d-3a50-95c8-8922dcbedfc7 | -11.35134 | -46.38079 | 2026-08-18 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35cbd558-a70d-3883-8a10-fbd81c150c1a | -9.49495 | -51.60558 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ded0838-d0c5-3438-8347-3b536169a51a | -10.2709 | -50.41557 | 2026-08-18 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3104f08c-6e0c-31e7-8555-80958947e269 | -12.46726 | -54.1837 | 2026-08-18 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff9e9f9d-9783-3154-8ff2-8f92a1c01534 | -8.90346 | -60.56741 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 281039a0-0a08-3e81-9cda-9c13a916402f | -11.83201 | -55.2218 | 2026-08-18 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc0fb65a-6183-39b2-af67-e553ba94f49b | -7.56384 | -55.55899 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7334bda-b7ff-3626-9f8a-2a00580e173b | -12.39831 | -54.9551 | 2026-08-18 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e1cd960-9b43-321c-a9b2-0aafb6f0b555 | -7.24098 | -49.88972 | 2026-08-18 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a39d0890-89ac-3ec8-b045-4613c6e63118 | -8.57869 | -54.70416 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a6ab2b2e-5988-38a1-8042-7a511a105e9b | -8.89796 | -60.57137 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3c3a3d0-1e77-3070-9a85-674921fd03b1 | -8.10813 | -51.65566 | 2026-08-18 04:57:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98109ce0-82d1-3b8a-9e23-1d1888acd6eb | -13.28186 | -48.69112 | 2026-08-18 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58a60b8b-3d96-3be0-ace2-eb18fea66d0c | -10.41362 | -61.20758 | 2026-08-18 04:57:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5a104c3-4326-38b9-9a1d-da0450e7f10c | -9.08371 | -50.86725 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af1b172d-0105-367b-8c69-6db084b6cab1 | -9.07029 | -50.83763 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1a99af9e-78dc-316d-a50d-54034f86afb9 | -12.90672 | -52.82561 | 2026-08-18 04:57:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb88736f-9655-302b-92ee-da129e5ee226 | -7.28233 | -44.07496 | 2026-08-18 04:57:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d12a33a4-a3f6-3aec-b4fb-62a816964cbb | -7.90769 | -61.73675 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b769c04-d1a5-382e-a068-72d8ebb4b897 | -12.4667 | -54.18723 | 2026-08-18 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68e09697-4654-3511-973c-3ba354e0d592 | -9.46131 | -51.61957 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c8ab106e-9581-39f6-974b-eee6d1aace8c | -6.34674 | -49.89742 | 2026-08-18 04:57:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 836d88f1-ce77-3b0e-af96-6ef0177149a7 | -6.7526 | -59.16511 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 97f24d42-309c-342f-8254-c1fff5ea8967 | -6.84434 | -58.99648 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0af97bee-6324-396e-9a92-e81b14f9cb85 | -10.28864 | -48.23836 | 2026-08-18 04:57:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65a6611e-42c9-34b1-b00c-6700fa8da3eb | -8.89395 | -60.60303 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f9e63679-04cc-359d-af91-72ed3bc0e31d | -8.95817 | -60.58226 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c0bf65a-bfdf-3886-858f-8ee68974b5b8 | -7.60513 | -60.82833 | 2026-08-18 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ff4aa905-53d3-35a7-8a44-0f035da47ee6 | -12.46559 | -54.19427 | 2026-08-18 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0558ee4-d9bd-3177-b5a6-09ab614c1eef | -12.00815 | -46.42409 | 2026-08-18 04:57:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ad918893-3013-3ec7-b4b5-7cfb0025c6bb | -9.76294 | -46.74269 | 2026-08-18 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb7a1527-de18-3816-9a93-6438f7cb2f8d | -9.46472 | -51.62013 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c86326b1-cd66-31bd-8a6a-184e37da62eb | -6.87437 | -56.41104 | 2026-08-18 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11729b9f-6e87-32d9-89ff-6d9b83feb023 | -8.55415 | -47.39152 | 2026-08-18 04:57:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 557faf16-71f9-3fa4-801a-b8101050ee81 | -7.46067 | -46.15355 | 2026-08-18 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eefbd2f4-9334-3aba-8bed-ba6e34cf7ccd | -8.49119 | -54.90234 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61e71b2b-8ac2-360f-9f1d-cb83284b04a5 | -8.53023 | -54.89738 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b69e6eec-1cff-3f94-960f-60075a82f078 | -8.5583 | -55.30891 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcf2acd2-7728-316d-8064-ceded1ea0d63 | -11.14163 | -49.04092 | 2026-08-18 04:57:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e846817d-a8b8-3c08-896e-65e3a1c94c4f | -9.18266 | -59.66956 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd5d8150-aeb1-3008-b554-b523c8fa52f3 | -8.95381 | -60.52631 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c85cec58-687c-32e2-be0c-3183e8a85065 | -12.26781 | -51.53925 | 2026-08-18 04:57:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1e123e0a-e0cd-3bd4-8f18-306844da4a47 | -10.57765 | -51.96647 | 2026-08-18 04:57:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a28c860-5a3c-3e19-8df5-ced1f767e299 | -11.72155 | -54.6213 | 2026-08-18 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66d87cbc-7d1e-39e9-a379-1008ae71ac7d | -6.74162 | -59.1734 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c02b8eea-75b1-3ca4-9370-201b4cac81a4 | -9.06797 | -50.85288 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6cf901be-5dff-3902-8759-0019c91e02f0 | -7.64134 | -55.61895 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 405c3308-d577-3810-a8eb-707b5938296f | -7.38418 | -59.99412 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41dccbfa-0972-3d4f-a479-37197e7b05ed | -6.9101 | -62.90612 | 2026-08-18 04:57:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9c092f90-df49-3343-9efe-6c0e87df13f0 | -6.74816 | -59.16126 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 21dd165b-d8ed-3190-a71b-b4d4c80c438e | -9.46983 | -51.65519 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f880dc9-1e66-3328-aa40-ee7688bd60ea | -12.26169 | -45.87588 | 2026-08-18 04:57:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf47dd92-1b4f-3921-a9d0-36cedfb28fdb | -7.81764 | -44.60987 | 2026-08-18 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a431673f-e733-308a-993d-007ff65abf00 | -11.19785 | -54.81173 | 2026-08-18 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a1ae2cf-a09d-34ca-af47-5a67a8ff7744 | -9.40743 | -48.24746 | 2026-08-18 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b94b76e-f42b-34a8-a8c9-45dcc876dec1 | -6.86929 | -56.41903 | 2026-08-18 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7bacea69-5b2b-30dd-8d17-2654a204b62d | -8.56247 | -54.59063 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb6cc286-3c55-3e87-b7ec-e7eea4560fa8 | -11.36532 | -55.41618 | 2026-08-18 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e4f27ca-6b85-3cb3-8ddc-c6480d4a7efd | -12.75471 | -48.42096 | 2026-08-18 04:57:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab285e56-1dfd-38e5-9185-4ef34ff58c2f | -9.58953 | -60.50475 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74df28c0-692d-3820-b802-9fbb22239f84 | -7.88256 | -63.76988 | 2026-08-18 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ffcbd74-afbe-3afa-9cd0-d04b447a0a4f | -8.56244 | -54.69778 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4f8b0345-53bf-3109-8a43-ecca8b9115ae | -8.58021 | -54.73778 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 9a3b275d-6ef2-328a-82fb-916b5edea765 | -7.91734 | -61.7417 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74fde2f3-90d5-36f2-a64a-538f69dbeb63 | -8.56128 | -54.705 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c643f7c-aa71-3264-8233-2490da9ba2f1 | -11.2139 | -54.0116 | 2026-08-18 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f35064d-0b28-390b-9f79-1a76ca34a426 | -6.74601 | -59.17407 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d26fef33-3888-3694-acfc-dfc6a675c789 | -11.32184 | -55.2263 | 2026-08-18 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3bc7b2dd-bae6-353a-8a92-527e27b210d2 | -9.1819 | -59.6738 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e92b0f8c-0dd5-31c0-96a3-3e6bdbee22d9 | -9.16764 | -59.69902 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7540bbd0-bfa1-34bd-917f-58ee4c69d510 | -6.85448 | -59.01521 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7b83d86a-d716-3c09-877f-0657e4068ef2 | -11.36135 | -55.41926 | 2026-08-18 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6268d53-1162-3e85-9ad2-6d0ee05d7899 | -11.36012 | -46.38789 | 2026-08-18 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2df78128-e396-3c90-99c0-1230b9649360 | -8.57184 | -54.72526 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| a73d1d42-80af-3dc1-b13e-0d48422fab4b | -8.58253 | -54.72331 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| f7265f82-4a79-35e5-a1c9-1818efdbd828 | -8.59848 | -50.35131 | 2026-08-18 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 5dabf878-42ad-3e62-b4b5-47b8ea1dcc6d | -6.76998 | -59.45784 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba4cdf08-2b37-37de-a585-4d8afa1e64d2 | -8.21602 | -55.01995 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66f78e7e-6532-34ab-b512-0951577d7bd4 | -8.36668 | -46.3639 | 2026-08-18 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d9d26fe7-0774-3c06-a597-ce9589415c07 | -8.08372 | -44.3554 | 2026-08-18 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41032468-50dd-38ca-bd51-f7b06cc89d16 | -7.36517 | -55.48763 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ac65e8c-1d89-3380-9b2e-050e34945c4f | -6.79002 | -59.4478 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81d33383-61f2-36d6-9267-a1f4f094b92e | -11.11026 | -46.4979 | 2026-08-18 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4f17f666-fe0e-333f-a9ec-406e9d75c9c9 | -9.40235 | -48.25385 | 2026-08-18 04:57:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9cc04214-a529-31a7-b5f5-1ed925ee3509 | -8.58148 | -54.70832 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 2af0ee83-5a73-339a-9d71-7ceb3730268a | -9.16721 | -59.70584 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66063e7d-add5-3562-89b2-9342ff367849 | -11.35402 | -46.39751 | 2026-08-18 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be4d874a-a0f0-3957-8329-2e3e425a1738 | -9.54604 | -56.7995 | 2026-08-18 04:57:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c93054a2-d7b9-33f5-8782-43f121a646c0 | -6.79078 | -59.44337 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 967e4282-655c-3e8a-8f61-eef97a4a1c17 | -6.74529 | -59.17834 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2f3d987f-536c-3315-be71-af308b58855a | -8.58473 | -54.73112 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 1fb1b99c-4040-3b32-8468-95071d19b609 | -7.81254 | -44.60905 | 2026-08-18 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c96d1237-4210-36f9-86b5-c6677412486e | -9.01425 | -60.50718 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ea05eff-8562-3a1f-a5ec-bf76bf61fecd | -8.9463 | -60.515 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73bd423b-c642-3114-8133-793f4364e1ec | -12.46506 | -54.17612 | 2026-08-18 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 176f2959-86bd-39f0-a94c-5f766ca5d460 | -6.78557 | -59.44705 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e43bb83-4dcf-3a73-a63d-9c0cbd48b98d | -6.84365 | -59.00053 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2bc897d5-889b-3bfb-9036-c0b7ee80c0e2 | -6.91079 | -62.90233 | 2026-08-18 04:57:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README36.md)
