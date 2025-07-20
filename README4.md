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
| 88b28cdf-8515-3ea9-90ef-1f75152bd2a2 | -14.2779 | -58.2466 | 2025-07-20 03:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 7534a8e8-0130-31be-83cb-61b3ae29e041 | -10.6496 | -46.8101 | 2025-07-20 03:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 43.8 |
| ead06008-7d78-377a-828e-f38d503ab374 | -9.5534 | -40.3254 | 2025-07-20 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 82.8 |
| c01ae073-098a-335d-bd52-df4819ffa3a5 | -10.6689 | -46.7853 | 2025-07-20 03:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 5b18c4e6-65ea-36cd-94cc-c5fa1f573d27 | -10.6686 | -46.8077 | 2025-07-20 03:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| a4841fcd-924c-3593-a67b-8cb75c773a60 | -14.2588 | -58.2483 | 2025-07-20 03:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 55.8 |
| e0492967-898f-3f4e-8d5b-5127a5b1b24c | -10.9811 | -45.1104 | 2025-07-20 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| f903266a-9ed1-3110-ba99-411550ec83f2 | -10.9811 | -45.1104 | 2025-07-20 03:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 04d72848-6d90-3aeb-894c-58f4c4e44985 | -9.5534 | -40.3254 | 2025-07-20 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 67.2 |
| dc6a3d0f-668b-37a9-b9ce-81b5b122cea3 | -9.5343 | -40.3282 | 2025-07-20 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 105.9 |
| 14a8093b-84b7-3447-af67-8ad4df114ee9 | -10.6686 | -46.8077 | 2025-07-20 03:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| eb3c3990-1eba-392d-9e79-329e2c2415ff | -9.5339 | -40.3531 | 2025-07-20 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 59.6 |
| f1b91707-25e5-3949-a702-f0f910a7e468 | -10.6689 | -46.7853 | 2025-07-20 03:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 35a4b680-daf5-331a-8e73-558efcf6ab1f | -14.2127 | -54.6567 | 2025-07-20 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 2ea73be9-051c-3bab-b1da-93aafe66bc71 | -10.6689 | -46.7853 | 2025-07-20 03:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| ecb94281-9f37-3238-9479-622d0d959896 | -10.962 | -45.113 | 2025-07-20 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.9 |
| b2aa55ab-dbad-3f1d-a6d9-5e5097f81a53 | -10.6686 | -46.8077 | 2025-07-20 03:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 913379f8-af6d-3ba9-afe6-dba3a99510a6 | -2.91338 | -48.24864 | 2025-07-20 03:47:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3b46d45a-f60c-3649-9e21-de2a39211f89 | -4.12972 | -47.65873 | 2025-07-20 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 24f60b1b-86db-32d3-a0bd-8d687e139ba3 | -4.58411 | -43.31229 | 2025-07-20 03:47:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ade62411-b5b1-3547-ac76-f9213ceffbcb | -3.13555 | -47.0099 | 2025-07-20 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41bfcc7a-82c5-3a5c-9375-fa0f0e2d3adf | -3.11623 | -47.01568 | 2025-07-20 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 95bb04b3-8a3b-385a-86de-88e5bf1741b8 | -5.15419 | -37.72806 | 2025-07-20 03:47:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 067fe3c6-081d-3767-9657-47392cf33466 | -3.0399 | -47.86733 | 2025-07-20 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| b9ed3cae-9643-3ac0-8589-747b43e52a54 | -5.87883 | -45.20664 | 2025-07-20 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 487cb3c1-fad3-3d19-90a1-ffa64b456c77 | -2.90784 | -48.24229 | 2025-07-20 03:47:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cc82d6b9-ba00-3658-8481-ba01dbfc85e0 | -4.66617 | -41.95387 | 2025-07-20 03:47:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 90575489-3dbd-3b58-aca9-36c703127630 | -5.07092 | -37.71803 | 2025-07-20 03:47:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e57c2500-2e87-302e-b56a-8ad3b2d9dd6e | -4.67279 | -41.95483 | 2025-07-20 03:47:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| dd8f142e-41b2-394a-86e6-8481d0390d3f | -2.99388 | -49.31895 | 2025-07-20 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1fc94cb8-a081-38d0-a2b0-f87a89e5e4b3 | -4.58865 | -43.31295 | 2025-07-20 03:47:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1f34e956-6ccf-3643-96ca-4a738670d932 | -3.12291 | -47.01233 | 2025-07-20 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 61a17e02-3991-34c0-8afe-e7a3fa504bd9 | -4.96756 | -43.24004 | 2025-07-20 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da3d0cdc-2e05-3fd5-b2ce-ef2514bfdb25 | -3.58487 | -47.52358 | 2025-07-20 03:47:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 22a806bf-4ece-3fd0-8444-7b48565396d1 | -4.66557 | -41.95761 | 2025-07-20 03:47:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 96901c71-4c24-3a38-bff0-edd8171c73a0 | -3.31698 | -49.0489 | 2025-07-20 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 0e6c8f00-7e1a-3f1a-8f3f-548c5de66b82 | -4.96455 | -43.23041 | 2025-07-20 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 45aeccdf-7778-3da9-b1ed-d6ec2372e391 | -5.61257 | -42.30863 | 2025-07-20 03:47:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0f63e5ee-2b8e-3299-bf16-0b21c0d41b17 | -3.94205 | -48.09132 | 2025-07-20 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f73c636-4210-3eca-a19f-08170311a55b | -6.14721 | -42.92118 | 2025-07-20 03:47:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| cb58cc09-7e9d-33cf-b22f-51ec004a16a2 | -3.79733 | -41.0003 | 2025-07-20 03:47:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a3b16450-9f1d-3e28-b88c-53c4dc6334f0 | -3.59096 | -47.52467 | 2025-07-20 03:47:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0e70fc0a-529f-34ad-a8e9-7f835ca0fab1 | -4.13054 | -47.65408 | 2025-07-20 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 69718d56-4716-3afd-ac72-bf954bf8d728 | -3.58566 | -47.51892 | 2025-07-20 03:47:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d6d77c8f-1d4d-3c6c-8121-79c7f6dd5908 | -3.91905 | -42.41698 | 2025-07-20 03:47:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 34d3d42c-1ddc-3931-a034-4ad9382ce1eb | -3.54094 | -47.37971 | 2025-07-20 03:47:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e323081-8b03-3258-88db-3d440d4a4c06 | -3.12886 | -47.01331 | 2025-07-20 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47d08543-ce3d-391a-9fe4-6ca285d9e975 | -3.79258 | -41.00473 | 2025-07-20 03:47:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 9170d84e-e4da-35d1-a220-e3b48503304e | -5.34883 | -45.26635 | 2025-07-20 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8eb83be5-b6f9-3be4-a9c0-3fc83dc118d5 | -2.90693 | -48.24763 | 2025-07-20 03:47:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9bc5addf-9883-32d7-ba79-bbeafdfea77a | -2.98062 | -49.10446 | 2025-07-20 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4b99b26c-2d6e-351d-b249-e5a84b0d0167 | -3.0345 | -47.8612 | 2025-07-20 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9de94294-f6ed-3e3e-8ec5-7a8a21de7ec1 | -3.11101 | -47.01036 | 2025-07-20 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 30e359e6-51d1-3594-9e06-3f777e8d5482 | -3.94122 | -48.09623 | 2025-07-20 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 839c9fcc-515e-3e11-a4e7-f9a58416d4a0 | -4.1234 | -47.65646 | 2025-07-20 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a7b20d2-0ba9-3508-8b48-6dc291ddb1bc | -4.59242 | -43.31829 | 2025-07-20 03:47:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6f30a9ab-1a34-3a1f-a586-171ace820c27 | -3.93902 | -48.09279 | 2025-07-20 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 25adf3fb-ea59-3d2b-bfac-71cc73e0da03 | -3.59176 | -47.51995 | 2025-07-20 03:47:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7712017b-9d19-3e03-9bd8-3a082ef82b26 | -4.96307 | -43.23933 | 2025-07-20 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 61b47043-c922-316a-8fdd-291747a25717 | -3.13482 | -47.01427 | 2025-07-20 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce07b45d-5726-302c-a957-d0eb8c53b474 | -4.66204 | -41.95321 | 2025-07-20 03:47:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1daac469-6383-32ad-8925-69090817092b | -3.91971 | -42.41289 | 2025-07-20 03:47:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 32be9499-e58d-36a5-87b1-229d5f72d4c6 | -4.66866 | -41.95417 | 2025-07-20 03:47:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| bd52d4b0-56bf-347f-8b63-c2af628d4220 | -4.6703 | -41.95454 | 2025-07-20 03:47:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 9166f08b-c3cf-390d-ad74-1c22c73c8288 | -4.12943 | -47.65788 | 2025-07-20 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2a0b57f9-ce60-3abd-bc5d-944549802004 | -4.1289 | -47.6633 | 2025-07-20 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 59be01d2-f0de-3be0-a1d3-5d9fa46ff67b | -4.66497 | -41.96135 | 2025-07-20 03:47:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 02bf6f2d-3d40-3b60-b720-175e6724fbeb | -4.12865 | -47.66248 | 2025-07-20 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e504b3ba-071d-37c6-b011-2f575bdfb793 | -5.87272 | -45.21181 | 2025-07-20 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d880222-2887-3dee-afaf-16c5a3adfe34 | -4.59772 | -43.31441 | 2025-07-20 03:47:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6c670409-7176-35ce-a27d-f49e1676ae8f | -5.09192 | -48.42287 | 2025-07-20 03:47:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a04a14d-3fdc-34d5-975a-5ce35f709ae3 | -3.83163 | -47.73898 | 2025-07-20 03:47:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 938326ec-6566-30ed-94cc-e2de45a7f71d | -5.34831 | -45.26938 | 2025-07-20 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5e40f98-3ebb-34ab-a261-eaa1ccb20e10 | -2.9143 | -48.24326 | 2025-07-20 03:47:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 35ab9153-883b-3cc2-8a1e-21f30d2ee43f | -4.12367 | -47.65739 | 2025-07-20 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8a50aeb5-4242-3f52-9edd-92661e08bf62 | -3.03359 | -47.86643 | 2025-07-20 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| eca93ba9-2e6e-3e3a-a511-2ef88d129a8f | -4.6674 | -41.9616 | 2025-07-20 03:47:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 76744ce3-1573-3a98-b3e2-f1a0f27703bb | -3.11696 | -47.01136 | 2025-07-20 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f922f0ee-0fee-3a40-897c-91e1cd60cc46 | -4.66803 | -41.95789 | 2025-07-20 03:47:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b8ba56c3-39df-360e-8a31-49cc1796c3e2 | -3.79651 | -41.00534 | 2025-07-20 03:47:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 29ed1e72-b43d-35e3-b025-b319cf15e22e | -3.83078 | -47.74386 | 2025-07-20 03:47:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 99375e47-ee9d-34a1-bef9-556c73f43a90 | -5.87219 | -45.21486 | 2025-07-20 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca8a55bc-d5c2-3e46-8bd7-002f3e834c8c | -3.14077 | -47.01521 | 2025-07-20 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c12123ca-12dc-3428-a142-c7316d51524a | -3.04079 | -47.86217 | 2025-07-20 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| afa8c2c5-de03-3cd6-9bc2-f20191f8413c | -3.7934 | -40.99969 | 2025-07-20 03:47:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| ccf0b772-897c-384e-84dd-466a7fcc04b6 | -3.318 | -49.04299 | 2025-07-20 03:47:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f6f5a7e9-240c-390a-9ebd-18d2069c53f9 | -7.04845 | -37.27882 | 2025-07-20 03:47:00 | NOAA-21 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 53bd8876-ae38-3c06-9b24-11415eeabe46 | -5.09101 | -48.42793 | 2025-07-20 03:47:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bda62762-972f-38c8-9214-9056626ba3c8 | -4.59696 | -43.31899 | 2025-07-20 03:47:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 018be3a7-15a9-3b37-a31d-75098ca83b7d | -3.51809 | -47.21341 | 2025-07-20 03:47:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f89c72f7-8c4f-3c1a-ba70-18d225611d0c | -3.11028 | -47.0147 | 2025-07-20 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| f5530736-150e-3192-9377-312a824b966c | -4.9638 | -43.23489 | 2025-07-20 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7b7c25ce-5ce4-3ee0-992c-01df72178a77 | -3.03682 | -47.86436 | 2025-07-20 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| af19bbab-c936-37a6-9c1b-8bbfcbe97395 | -3.03595 | -47.86963 | 2025-07-20 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| b972bf3b-295a-3375-8f6a-1338adad3fe2 | -9.56161 | -40.65958 | 2025-07-20 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9f5daced-8462-3e3e-84b7-0018b89b3294 | -10.97228 | -45.10503 | 2025-07-20 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 64c6ce24-05c4-3892-956e-7825d6ebd120 | -11.46243 | -48.16607 | 2025-07-20 03:49:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b452f20a-1e5b-34c1-934e-77aa3a93b8a4 | -9.11322 | -48.11916 | 2025-07-20 03:49:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae7bfbff-a3db-30f3-96e4-be16b895653d | -6.36812 | -45.39112 | 2025-07-20 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fa4f665f-48d2-3837-9d62-d7d5d41b605d | -7.70054 | -47.29542 | 2025-07-20 03:49:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README5.md)
