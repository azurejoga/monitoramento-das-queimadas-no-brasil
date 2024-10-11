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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3498711-c7f2-3120-a34d-ad23492d5b86 | -12.69031 | -45.87949 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 771b6558-f5c5-3c13-99f2-3e8c13f0d3aa | -12.69027 | -45.87632 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf850d68-b266-3f2b-958f-3c3164e4d948 | -12.68942 | -45.88048 | 2024-10-11 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f066bf5-c202-3087-b0c7-925137e828ef | -12.65706 | -40.55922 | 2024-10-11 03:38:00 | NOAA-21 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 47a2fff9-5242-3ec2-a98f-f6c718e4c8a8 | -12.4348 | -43.74683 | 2024-10-11 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 590e974c-d3c7-3446-8c76-c966b6e67ddd | -12.43237 | -41.79754 | 2024-10-11 03:38:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0e33bb21-8277-300f-b10d-a559338f601b | -12.42971 | -43.74582 | 2024-10-11 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44ba4eda-e5ec-3398-9899-889057b8c2be | -12.37593 | -44.11447 | 2024-10-11 03:38:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d897826c-a62a-3383-9127-18aaa6424596 | -12.35428 | -43.75261 | 2024-10-11 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| aa8d1edf-866a-30d4-a6b4-368e02b96ed4 | -12.3537 | -43.7556 | 2024-10-11 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| feaaae6c-be71-3961-a703-388d6f0aeb70 | -12.35312 | -43.75855 | 2024-10-11 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ef2cc5fe-b965-3e6f-a0e9-0782958be008 | -12.3519 | -43.75105 | 2024-10-11 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bbbe8683-4997-3263-bd46-4b7619de1452 | -12.35134 | -43.75404 | 2024-10-11 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| f7b0da42-b0e3-305b-8466-4a767b48f29a | -12.35079 | -43.75694 | 2024-10-11 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 94ecae7b-bcd9-39cf-9696-96a6adfae47b | -12.34868 | -43.75415 | 2024-10-11 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 21fd4da3-71b8-3483-baa8-c38dee45f67f | -12.34813 | -43.75698 | 2024-10-11 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 20950dec-f070-398c-97f5-afa2910cf961 | -12.20253 | -38.24912 | 2024-10-11 03:38:00 | NOAA-21 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dfea3c76-a6ab-3fe9-9438-64d1ec495ff0 | -12.1376 | -39.40571 | 2024-10-11 03:38:00 | NOAA-21 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b74e0fe2-cd76-3b62-aabb-23907ee76a3f | -12.11895 | -43.17585 | 2024-10-11 03:38:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 1fcc5d8d-e335-3831-a99b-b3c82c6fc645 | -12.11815 | -43.17404 | 2024-10-11 03:38:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| ccf08c01-fd29-3629-b610-8c276ef13b52 | -11.89326 | -43.88815 | 2024-10-11 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 80143dfe-be7a-3932-b5f4-fff7389b1f60 | -11.89268 | -43.88733 | 2024-10-11 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a99d2c4d-71eb-322a-9635-89680ab80c63 | -11.79104 | -44.49698 | 2024-10-11 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8679c1b3-538d-3bef-a090-a1e65a20f0b7 | -11.79075 | -45.19752 | 2024-10-11 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 396380d5-f4d5-3282-89bf-8cd4053fc82a | -11.78562 | -44.49594 | 2024-10-11 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 627d2d7a-ee46-388d-8863-be7cce3cdd34 | -11.76376 | -44.48431 | 2024-10-11 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2a18da7-0884-3403-887f-704c1fe81fcd | -11.52598 | -43.993 | 2024-10-11 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11926f04-d9a1-3a3a-aae4-42294745e690 | -11.49271 | -43.22778 | 2024-10-11 03:38:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4865411c-62f9-31f3-87d1-0ae38c0c330e | -11.49214 | -43.23074 | 2024-10-11 03:38:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 87cf88f7-ff06-3bc8-afda-f61f61452312 | -11.2179 | -41.60319 | 2024-10-11 03:38:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5ac5003c-ceb5-3ecc-b6dc-7dbfa8c5f1e6 | -11.21707 | -41.60784 | 2024-10-11 03:38:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9a2f0f43-8e5d-3dd4-9960-53294643712b | -11.11083 | -43.33849 | 2024-10-11 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 581ea9f4-911c-33b8-bd13-3656b518af3f | -11.0875 | -42.30479 | 2024-10-11 03:38:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5e651237-06af-31f2-9a55-0d200e6f04dd | -12.17304 | -46.74842 | 2024-10-11 03:38:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3745fbcb-e665-3122-893d-991af6a42b46 | -11.01711 | -42.86934 | 2024-10-11 03:38:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 205e1a2e-1b30-3f6f-a500-7d3385dea2a6 | -11.01603 | -42.87511 | 2024-10-11 03:38:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9320b3ab-1ef0-301c-81a8-489f6ffef5cb | -11.00565 | -45.33752 | 2024-10-11 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6fc859b-ba9d-3fed-b023-b5a295dbfc1a | -10.80703 | -38.2354 | 2024-10-11 03:38:00 | NOAA-21 | POÇO VERDE | SERGIPE | Brasil | 2805505 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 11c4487d-7319-39a5-9bee-8348bb5a793a | -10.79924 | -42.45013 | 2024-10-11 03:38:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6e5e8cf3-229f-3207-b069-e3c0a8551d7d | -10.29987 | -43.41919 | 2024-10-11 03:38:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 932041a9-f309-3d23-b9c0-5cc046237d32 | -10.29923 | -43.42259 | 2024-10-11 03:38:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5da6c038-19a7-3246-87ee-9cbda176923d | -10.23337 | -36.36368 | 2024-10-11 03:38:00 | NOAA-21 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 09dc6bff-ebcf-371b-acec-c86f0f4e9314 | -10.22996 | -36.36314 | 2024-10-11 03:38:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3b6db2e1-b76f-365a-af0f-4856872af062 | -10.04858 | -36.11641 | 2024-10-11 03:38:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1666bec9-d47f-3699-8666-9bd34058f0cd | -9.21008 | -47.55389 | 2024-10-11 03:38:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 182af4a0-4014-30bd-9355-95a705223f39 | -9.11162 | -47.65528 | 2024-10-11 03:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e87896af-59ae-38df-86c4-e7d8ddc909fb | -9.11089 | -47.65967 | 2024-10-11 03:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c4e94c1-4f79-31ea-aee0-01a0a2b3c6ff | -9.10533 | -47.65185 | 2024-10-11 03:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8b64ee53-5ddb-3e02-abab-59cb250d73c5 | -9.10474 | -47.654 | 2024-10-11 03:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 14fbc939-415b-3f06-aad5-1bfa738a7c00 | -9.10401 | -47.6584 | 2024-10-11 03:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a8f4c56f-d05f-30e1-9b8e-b7f1b44b44c9 | -9.09799 | -47.9392 | 2024-10-11 03:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 55af6166-e068-3bc7-a36e-85ad318589ff | -9.09662 | -47.94605 | 2024-10-11 03:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| aa152b5a-4665-3095-b199-5d7e7730b90e | -9.04372 | -47.81905 | 2024-10-11 03:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 86d8cd74-9edc-3332-9895-5ca3df458477 | -8.76855 | -47.79942 | 2024-10-11 03:38:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da69d092-301c-32a1-af0c-997d16dd4ff3 | -8.76222 | -47.80114 | 2024-10-11 03:38:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c5d92e92-3885-32cb-b108-c7cf80743b04 | -8.76164 | -47.79783 | 2024-10-11 03:38:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 61919a57-4e36-3477-b7a1-1c32a2b2622a | -7.25973 | -45.38861 | 2024-10-11 03:38:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8cb1e4ee-157a-364a-9b28-cf40efde8a79 | -7.2535 | -45.38767 | 2024-10-11 03:38:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ee8d58f-3d74-3d46-bdd2-a6823fc534a8 | -7.16099 | -45.7124 | 2024-10-11 03:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 77a8261f-9737-3338-a539-3fbb8b2f007d | -18.29161 | -47.24958 | 2024-10-11 03:40:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 92fdce1c-d7aa-3374-9787-a848c61bed64 | -2.6533 | -53.3506 | 2024-10-11 03:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 8b84a886-0461-33dc-bffb-c87eef6d0114 | -2.6716 | -53.3502 | 2024-10-11 03:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 8794c1ed-8f4d-30bb-b12c-4d52814effd2 | -2.7847 | -52.4933 | 2024-10-11 03:45:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| f67aabff-0859-3af4-b5a1-9f5f3cc2e830 | -2.9673 | -52.9169 | 2024-10-11 03:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 38eaee0d-b83d-3dde-ae0b-ea405ba586c1 | -2.9673 | -52.8966 | 2024-10-11 03:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 34d9f066-e929-3aef-a465-f9286810c474 | -2.9857 | -52.9164 | 2024-10-11 03:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 133.2 |
| 1beb5b83-1c03-3052-90e7-24f5452982ca | -2.9857 | -52.8961 | 2024-10-11 03:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 3d6a4555-0ccf-3886-9f8f-94c93227c423 | -3.1423 | -50.4352 | 2024-10-11 03:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 022dcfe2-afe1-399b-bab5-514a8e37fc77 | -3.1607 | -50.4556 | 2024-10-11 03:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 3e4cb3be-cccc-39b0-80dc-9e37b5c28544 | -3.1608 | -50.4347 | 2024-10-11 03:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 0c3c855a-b23b-3cec-84de-e4137e405470 | -8.4417 | -55.4692 | 2024-10-11 03:45:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| ccef3125-79ae-3090-aec0-0feece44cd6e | -8.4419 | -55.4491 | 2024-10-11 03:45:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 9d7b5d9b-10ee-346b-8c01-430f6426033d | -9.6389 | -64.9664 | 2024-10-11 03:46:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 472a65dc-8947-3126-82b3-4f259609e76c | -9.9481 | -58.1092 | 2024-10-11 03:46:03 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 44b39952-8d96-3fed-b560-9d014a874fa5 | -10.6962 | -53.0354 | 2024-10-11 03:46:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 98d3fe8b-e8d7-3f25-9d12-004bd0993027 | -11.2407 | -53.2738 | 2024-10-11 03:46:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| a7f111f8-e7d3-354f-81a1-f2cc1f33f476 | -11.2906 | -50.9633 | 2024-10-11 03:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.8 |
| edb5a8ef-e5b4-3f74-a0c7-d42960908da7 | -11.2909 | -50.9421 | 2024-10-11 03:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 6126a469-f767-3930-93be-4c0e9f1b2f8b | -12.1138 | -50.55 | 2024-10-11 03:46:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 1cf4c91f-c591-36a9-b169-4b4d77cffab2 | -12.1329 | -50.5477 | 2024-10-11 03:46:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| b768ffaa-82c5-36bf-8d68-5686bedd8cd6 | -12.7673 | -44.8904 | 2024-10-11 03:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 8b3faa1d-5968-3a9b-a79a-88e3f7a60873 | -12.7678 | -44.8671 | 2024-10-11 03:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| fe8f746d-6bd8-39e5-9f47-1f863f20ccb5 | -12.7866 | -44.8873 | 2024-10-11 03:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| ab0d8640-7a64-31f1-80b3-a97fa1361fc8 | -12.7871 | -44.8639 | 2024-10-11 03:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 464ae033-34b3-310b-8ba9-ead9b145da72 | -13.9663 | -45.8025 | 2024-10-11 03:46:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 99059b98-d836-30fc-8ba7-d48183ac4b21 | -18.1773 | -56.4676 | 2024-10-11 03:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.1 |
| 2ffeb390-80c9-30ab-aa5c-b04ed491cf81 | -18.1776 | -56.4468 | 2024-10-11 03:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.7 |
| 7ac1f077-f8a4-3042-a1b9-64cf9f112c20 | -18.1971 | -56.465 | 2024-10-11 03:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.2 |
| c8065293-4d95-3179-b0ee-fb1cfc737313 | -18.1975 | -56.4441 | 2024-10-11 03:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.6 |
| 1effa4d2-4ccc-3d05-b87a-8838151b5f31 | -2.6533 | -53.3506 | 2024-10-11 03:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 24c1eb97-e7b5-3fde-89d7-9d3538c5a936 | -2.6716 | -53.3502 | 2024-10-11 03:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| e824c309-a5d2-3f4b-93c3-7496a15278ff | -2.9673 | -52.9169 | 2024-10-11 03:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 19a92d28-ba1a-3e49-885f-d4e6c96c1654 | -2.9673 | -52.8966 | 2024-10-11 03:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| d2a5be2d-8dd1-3452-874a-75eaf3de85c5 | -2.9857 | -52.9164 | 2024-10-11 03:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 9c46defb-39ae-31a9-8a92-22de03a84bfa | -2.9857 | -52.8961 | 2024-10-11 03:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 569ed399-c03e-3437-8baf-c258ae653455 | -3.1422 | -50.4562 | 2024-10-11 03:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 2e2bb4c3-ac8a-37a8-816a-a2a2378105c1 | -3.1423 | -50.4352 | 2024-10-11 03:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 3a692fd6-1cdc-3778-a508-7dc1c748d6dc | -3.1607 | -50.4556 | 2024-10-11 03:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 9ba902b8-94da-35c1-ab0d-1f5b7edf2b11 | -3.1608 | -50.4347 | 2024-10-11 03:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 84263f61-3635-3317-b2a4-dca641789fd4 | -3.3096 | -50.1781 | 2024-10-11 03:55:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |


[Clique aqui para ver as próximas entradas](README34.md)
