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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a36ded4-3d3f-3d1b-88da-0a846c7c0aac | -10.94031 | -43.06496 | 2026-07-27 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6137a22a-797f-3d8b-bc00-53167ed33e21 | -14.50934 | -48.93878 | 2026-07-27 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c9fe2f33-00c3-3e76-b951-8d0dc7c15d84 | -14.24087 | -54.56016 | 2026-07-27 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 045a7430-19bb-3002-aabc-a15c09626bc9 | -10.9414 | -43.0578 | 2026-07-27 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| e47a26af-f2b2-3263-8fce-c98884345d24 | -10.895 | -45.21128 | 2026-07-27 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36900b27-2e3a-3dc5-bb2c-ea821f930221 | -12.29711 | -50.37093 | 2026-07-27 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 05297f65-317e-3b30-a74c-3ceef4299fac | -13.69282 | -51.91045 | 2026-07-27 04:17:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 05dce78a-6e1b-3507-9677-605a69b55f04 | -11.99183 | -45.56423 | 2026-07-27 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d0ceaba-a8a9-37d2-ad01-5aa08baab97f | -11.45711 | -47.53149 | 2026-07-27 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3466c181-1613-3fa1-9310-b9f8af914fcd | -11.89058 | -43.82863 | 2026-07-27 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 94d05dfb-a1d6-3758-926f-9660bc4590b1 | -14.23556 | -54.55877 | 2026-07-27 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a7a7a15-5582-3c6b-bcb7-2237a412e561 | -9.45411 | -51.82814 | 2026-07-27 04:17:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d0bfebd8-b095-3302-a854-df1077d8f74d | -11.46583 | -47.52383 | 2026-07-27 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fde5a63-1fc6-3e29-9c5e-43739cb4cd85 | -10.54305 | -48.61075 | 2026-07-27 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09d7f049-4a72-30e4-86cd-cc7d01cfa74f | -14.0415 | -43.85193 | 2026-07-27 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dd7617d3-d677-310b-a429-92717e1c68d9 | -13.70165 | -51.88786 | 2026-07-27 04:17:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9deeadb2-1a70-3849-a387-6c01594af1d2 | -10.53446 | -48.6142 | 2026-07-27 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af03f8dd-7f17-35b2-8625-af03e2129b55 | -11.4897 | -47.53652 | 2026-07-27 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e63940f5-c101-3f62-bf8d-5e317620fbd9 | -13.6384 | -44.4418 | 2026-07-27 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed63e460-98f8-3c07-ac7a-c212c97a69f2 | -13.69369 | -51.90568 | 2026-07-27 04:17:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b250c66b-d171-3678-853d-3e68ee09baa8 | -14.50562 | -48.93803 | 2026-07-27 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8c07b2e8-921a-353d-af5e-dfe03bbcf559 | -12.32369 | -47.19373 | 2026-07-27 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6c495487-be3f-3705-928c-4828d098498e | -10.83663 | -49.39026 | 2026-07-27 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb10acb8-fc97-38e0-a3c8-09895ddb1fe8 | -13.69196 | -51.91518 | 2026-07-27 04:17:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| bd012a6c-a53d-3154-ba29-5579133dbc3a | -11.49036 | -47.55486 | 2026-07-27 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85a589d0-82db-383a-8287-fddcfdf2cfb7 | -14.7 | -44.65462 | 2026-07-27 04:17:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6692da26-f2e7-332d-97a4-0a13e4c31e57 | -14.24155 | -54.55671 | 2026-07-27 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c451d26d-eead-3d7b-be1b-fce878980005 | -10.93593 | -43.0531 | 2026-07-27 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.7 |
| ae25611a-976e-3318-b607-3746a929c10d | -9.69758 | -47.69806 | 2026-07-27 04:17:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3813fe05-6b1d-3d8f-a3c7-f79e0a233051 | -10.53919 | -48.60996 | 2026-07-27 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db5ebc25-888b-363d-896c-ef932e9488ad | -10.94086 | -43.06138 | 2026-07-27 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 83515aa3-9d3f-3e70-aa59-2d97832e21f5 | -14.35458 | -54.93722 | 2026-07-27 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a47e2cd4-dc2a-3912-9a2f-1ad5cb988045 | -11.48673 | -47.55436 | 2026-07-27 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d355cce7-70e5-3e04-bcc1-1cfdd3804baf | -12.2936 | -50.36616 | 2026-07-27 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f7722b88-13c5-3c9b-8653-f34bfdc94751 | -19.10911 | -44.34052 | 2026-07-27 04:19:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f995d55-a898-3c45-bb48-0f0758f4d89e | -19.10829 | -44.34124 | 2026-07-27 04:19:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f2692eac-0324-31ee-a369-84a47f5b4204 | -18.26958 | -50.34457 | 2026-07-27 04:19:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 807ca6a7-a95b-359b-8f0d-a61fc2f433ae | -20.06256 | -43.69782 | 2026-07-27 04:19:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f376b933-facb-3693-9a22-2f9ec2c80da9 | -20.06607 | -43.69829 | 2026-07-27 04:19:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 94654c29-23ec-305b-badf-a5fb3f5470ce | -19.78842 | -42.69949 | 2026-07-27 04:19:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 10f7528f-8b01-3743-a19b-1f0e1b64c461 | -19.10771 | -44.34515 | 2026-07-27 04:19:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0c54fb6-59b3-30a3-b4aa-b65a36245ec7 | -18.64156 | -40.91291 | 2026-07-27 04:19:00 | NOAA-21 | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 887b9ae3-3246-3dec-aabb-ab05b64f3090 | -17.16543 | -46.83395 | 2026-07-27 04:19:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| df4f3749-b110-3f54-a0f3-cc2fcfa5ea56 | -18.44452 | -44.45736 | 2026-07-27 04:19:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6eb7b331-a047-3af4-96d4-970277ea8c33 | -19.11251 | -44.34105 | 2026-07-27 04:19:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67add35d-9324-3145-8f80-a1e82515c00d | -18.26575 | -50.34381 | 2026-07-27 04:19:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 36cc81ff-4a2c-325d-aeb3-c2fcfe52c461 | -16.96375 | -51.88363 | 2026-07-27 04:19:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 95b6a62a-4d8e-381b-abb2-766f12f73816 | -16.96522 | -51.88708 | 2026-07-27 04:19:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| d73dd054-c645-3334-a18d-c83bbaea005b | -16.963 | -51.88771 | 2026-07-27 04:19:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 3dd07bf8-fbb7-3b0b-a041-08a4f3e0dfe5 | -20.06203 | -43.70161 | 2026-07-27 04:19:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a4ed05b9-8662-34cd-8a97-79e398b4ccc4 | -19.10855 | -44.34445 | 2026-07-27 04:19:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa849f63-c027-3d6e-a32e-ca1f5bd89740 | -10.9401 | -43.0355 | 2026-07-27 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 145.8 |
| a3c801a5-573d-3efe-bb67-d6d4ec161130 | -10.9205 | -43.0622 | 2026-07-27 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| fff57f60-e2de-322d-9be8-52e6a98f0c9c | -10.9397 | -43.0593 | 2026-07-27 04:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 291.3 |
| 30944ca6-531f-3dd1-a011-04cd1ab8d76c | -10.9397 | -43.0593 | 2026-07-27 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 184.4 |
| 5c625e6f-e281-39cb-8bd6-b06d316874b1 | -10.9205 | -43.0622 | 2026-07-27 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.3 |
| dd028be0-937e-3dcc-89b2-4f0afcdef08a | -10.9588 | -43.0565 | 2026-07-27 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| b0438818-771b-32dc-b289-ba7055a16561 | -10.9401 | -43.0355 | 2026-07-27 04:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.8 |
| b8f6a462-bbe5-3b6f-be77-840ae3fb4a06 | -10.9397 | -43.0593 | 2026-07-27 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 224.6 |
| 9d578e0b-4df7-3283-b2d7-c63f3aaa6c29 | -10.9401 | -43.0355 | 2026-07-27 04:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 023addaa-ac75-370b-a101-5bc35ce3c89c | -2.04639 | -48.04126 | 2026-07-27 04:46:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55bac978-a3b4-38ad-a8a7-996d364be311 | -1.54559 | -53.69798 | 2026-07-27 04:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3bb255d-82d4-3e29-80bc-a8963f2506b2 | -1.54671 | -53.69094 | 2026-07-27 04:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 22c3dff7-1fb9-3283-99e4-d735bcb04307 | -1.54152 | -53.69725 | 2026-07-27 04:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb9e3ee9-81a8-3240-8dcc-912fa230fe57 | -1.54208 | -53.6937 | 2026-07-27 04:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2a5cf059-5983-3db2-83da-701b98a9f67d | -1.54615 | -53.69445 | 2026-07-27 04:46:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c9754dbe-bd68-3c1b-8255-d8d98109a8e8 | 0.08249 | -51.09376 | 2026-07-27 04:46:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0754969e-fc6d-3dc3-bbb4-6fc3548353e9 | -2.80771 | -48.6673 | 2026-07-27 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 94752d80-c880-33e6-a5a3-8cc969c30159 | -3.51732 | -48.03179 | 2026-07-27 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb7f1457-a296-3041-9944-2a8e38c1fc96 | -2.94087 | -48.78688 | 2026-07-27 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbdcecc0-a851-3429-b337-285418b58244 | -3.96155 | -49.41804 | 2026-07-27 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9b29afb-8aef-3407-ba20-32cb2d0a4771 | -7.69663 | -46.49298 | 2026-07-27 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17cd6785-bbb0-346b-839f-12121e8dfe23 | -8.8327 | -47.08583 | 2026-07-27 04:49:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9c11ab8-0cc4-3478-84b2-cd2c002f4e5e | -10.94092 | -43.05793 | 2026-07-27 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 7e4e3381-28ba-3880-8fb0-b659fddada38 | -2.85901 | -54.02139 | 2026-07-27 04:49:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 798d7dc1-31fa-3405-88fe-492f71e4b651 | -5.3555 | -43.13499 | 2026-07-27 04:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ae898d9-8b42-370c-8f04-8123b3dd8fec | -7.17465 | -59.31474 | 2026-07-27 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c938c0a9-e694-3a06-b603-20e5816ba6aa | -4.91257 | -43.46858 | 2026-07-27 04:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 625be275-3d41-3e4e-ace0-81abdcb1987a | -5.93713 | -43.64791 | 2026-07-27 04:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a27f5827-7317-37b3-89fa-26c9c321bb58 | -3.92196 | -47.81926 | 2026-07-27 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3de02294-4517-3f42-9f5a-e8e96d20bcb8 | -10.94021 | -43.0632 | 2026-07-27 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 2d6f35ee-a849-39dd-9a13-266554f92bad | -7.7003 | -46.49355 | 2026-07-27 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 14b06a18-1c35-3c82-865e-2ede05e9f198 | -6.92795 | -42.81715 | 2026-07-27 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 444157cc-56e3-3a1b-bb95-aaa0ed25f358 | -2.94964 | -50.33182 | 2026-07-27 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16d497b3-fe88-3b34-a439-008e546fb845 | -5.93533 | -43.65991 | 2026-07-27 04:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d87d5e4-0598-3ff5-bd3f-4d81668af830 | -2.80716 | -48.67074 | 2026-07-27 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| babf74f3-bcb3-3ac5-b2ab-d8f208a101a0 | -10.94572 | -43.05859 | 2026-07-27 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.0 |
| a248f0ea-98fd-3106-a3e5-2267075cd83e | -5.46758 | -45.39878 | 2026-07-27 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75afe1c8-8c59-375e-9d0f-df07fa189e0b | -2.76577 | -49.46361 | 2026-07-27 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e9bd081-e66b-3d83-b422-3e2d0a8af703 | -2.82552 | -52.30379 | 2026-07-27 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c0e956b-6c39-3941-8c22-9bd388e6cf40 | -2.95079 | -50.32462 | 2026-07-27 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c391cd5-7461-3860-8925-760427481c64 | -6.92431 | -42.81846 | 2026-07-27 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cc1d0f0e-9a74-3956-aee3-1c194b08aae6 | -8.82847 | -47.08942 | 2026-07-27 04:49:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18e4a9c7-d862-39d5-a4f8-8af11d1e0b88 | -3.26058 | -49.52406 | 2026-07-27 04:49:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e92042a-5df2-3a9b-8051-f89dad0a793e | -3.9186 | -47.81873 | 2026-07-27 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8c41b1b-4c01-3a45-b75a-460bc461c173 | -7.902 | -48.05131 | 2026-07-27 04:49:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8d28177-b461-38ac-9a99-ed0b4edc6252 | -7.16376 | -59.31272 | 2026-07-27 04:49:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bf84b4f-2ab1-3733-8fe6-cc13b3ba1f39 | -6.9296 | -42.81443 | 2026-07-27 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a7c88ce2-d757-3324-b45b-1e1e45f75957 | -8.73246 | -44.31818 | 2026-07-27 04:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b6db84a-ecb9-33d0-9092-4224a8f3c33c | -9.0283 | -48.57825 | 2026-07-27 04:49:00 | NPP-375D | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README5.md)
