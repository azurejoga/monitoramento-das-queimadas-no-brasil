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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2044fff1-cf74-3f4b-ac62-2366fc4a0495 | -10.82281 | -50.23212 | 2026-07-19 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cd6c7e23-6c8f-3530-ac61-a7bf2a29f260 | -8.35952 | -45.3947 | 2026-07-19 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5c4df17f-8fcd-3400-a6cb-0b3ab6010650 | -9.49673 | -46.66682 | 2026-07-19 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 30675c26-8593-3800-9304-0f0b03edca43 | -15.70805 | -43.37785 | 2026-07-19 04:19:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9b5cd5b-0bb4-3ecf-832d-93df49acb4fe | -9.47527 | -57.32638 | 2026-07-19 04:19:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78dc25c7-4186-3cab-8230-639f66153925 | -9.09609 | -50.61269 | 2026-07-19 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3899e040-23b5-3d56-a3b7-7bcb834e724f | -13.67294 | -48.78471 | 2026-07-19 04:19:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 9ddf2de3-afb5-31f9-90b9-e416b48bb761 | -8.36569 | -45.39962 | 2026-07-19 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 40f55e84-00b4-30ab-9b04-ba6b11460e07 | -11.77144 | -45.96998 | 2026-07-19 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 647e998a-1c6f-3ca3-8a16-2049c3f608d9 | -10.52346 | -42.39606 | 2026-07-19 04:19:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1b95a63b-b0da-360f-a117-bd9617ef129d | -13.6224 | -47.48647 | 2026-07-19 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb495e8b-f36c-3f27-983b-90b19a6625ce | -9.08665 | -50.58754 | 2026-07-19 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a9c8ee6-6dfe-3bd1-a4d2-d1b32cc9642b | -11.62695 | -47.95539 | 2026-07-19 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3c871105-9609-3861-81d8-ad4c33bb5531 | -8.62088 | -50.0244 | 2026-07-19 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e73ef02-8262-314a-a059-e43d8cc50104 | -9.18226 | -45.92477 | 2026-07-19 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc2c3fff-847a-3ede-836c-be614a5a435f | -10.69596 | -46.62605 | 2026-07-19 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9cfa6185-31ed-32e2-9a71-08f8e1c82983 | -10.6966 | -46.62216 | 2026-07-19 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1dd4f7e2-f3ee-35f7-b83a-e3e64cbfd071 | -11.38251 | -47.51484 | 2026-07-19 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d1204c7-f2d2-37c0-b4b6-79c0818ffd74 | -9.4964 | -46.6675 | 2026-07-19 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bff9b1e3-f1ed-36af-b8b2-b94b7ea89e30 | -11.38463 | -47.19845 | 2026-07-19 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a317dca-5016-322a-8c79-90ceacaadc47 | -11.77421 | -45.97422 | 2026-07-19 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4588f2a9-e8f2-3383-a479-7d7b854e3734 | -11.97291 | -47.10925 | 2026-07-19 04:19:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a336180e-cc45-3a04-82b6-a8826c89714e | -9.48211 | -57.32774 | 2026-07-19 04:19:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e915ba2b-21a6-3087-8534-84fd3d393091 | -10.81856 | -50.23133 | 2026-07-19 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ab86ceed-086c-35d8-a674-c7cfb647d906 | -10.89773 | -50.32407 | 2026-07-19 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a053616-9c13-32da-953b-d2d05ef74bfc | -13.67668 | -48.78529 | 2026-07-19 04:19:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 8fbced7e-9260-36ba-b9d9-38996790cd64 | -9.47611 | -57.3253 | 2026-07-19 04:19:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1248a3f-d368-389a-a084-ed62c7b28fee | -12.07994 | -53.35068 | 2026-07-19 04:19:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 00fc1f30-c2e7-3f75-ab2d-2ed009ea9b15 | -11.77362 | -45.97787 | 2026-07-19 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 625c6fc5-be0a-3f60-9bf5-ee253637c319 | -11.97991 | -47.11047 | 2026-07-19 04:19:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9aeb872a-a3cd-3e46-9158-c13aecedb408 | -2.79883 | -49.52332 | 2026-07-19 04:19:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a6851614-c3ef-335d-8006-36efd9b4e9d5 | -13.61823 | -47.48982 | 2026-07-19 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d009345-71e4-378f-a5e7-7c6597e2d615 | -13.55692 | -47.70114 | 2026-07-19 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8215cf84-e9fa-364d-9120-9b075f8991b8 | -2.82938 | -48.86123 | 2026-07-19 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba216072-617d-32e3-aab4-fcd5cd4a7b75 | -13.35094 | -54.31253 | 2026-07-19 04:19:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fe928a7-3c02-3b88-9a6b-a4fe506de9e5 | -11.68235 | -54.58775 | 2026-07-19 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d774abf-2cf3-348a-8577-3162ab39b5bb | -12.07935 | -53.35379 | 2026-07-19 04:19:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e2ff6be8-2148-3e5f-bd21-8fa2eff242d8 | -10.887 | -50.33477 | 2026-07-19 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e844e654-05c0-3e0f-8b9c-4bdc184a004b | -9.4974 | -46.66283 | 2026-07-19 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 62ff548c-2801-3a62-8c90-3fd1aa4ca1be | -5.10924 | -38.06302 | 2026-07-19 04:19:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d8bbd8b7-42d4-3d80-885a-b3aa07414593 | -8.93634 | -47.60318 | 2026-07-19 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8e3d9aa9-7458-3b20-8266-de10f9f60415 | -2.82865 | -48.86555 | 2026-07-19 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2412656-83a8-3c11-aef5-627a83020240 | -11.97707 | -47.10589 | 2026-07-19 04:19:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 29f03e02-faca-315a-9a32-63e6dfe16af6 | -8.36629 | -45.39588 | 2026-07-19 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a8e54066-b553-38e2-9f4d-f050a702caca | -10.71716 | -46.57281 | 2026-07-19 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 057098a9-0d48-353f-b27c-5141107608a6 | -9.48295 | -57.32662 | 2026-07-19 04:19:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 967857c3-3b39-370c-ba02-3345896f1c94 | -13.5646 | -47.78179 | 2026-07-19 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28cdc309-5d10-3199-8082-873a81c2d8db | -8.72467 | -47.8432 | 2026-07-19 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86fc698f-b2e4-3c73-9cfd-c7f6a196e9b3 | -11.38108 | -47.52336 | 2026-07-19 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 917cc87e-430e-3516-9b8b-d16165870750 | -10.90483 | -50.33384 | 2026-07-19 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 28ed947d-c083-3564-a86c-a4fc6a466ba1 | -9.08055 | -50.59578 | 2026-07-19 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2aa9a368-1ada-30cd-8beb-5258b6edd970 | -10.89418 | -50.31919 | 2026-07-19 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ece9f4c6-64d0-3f9b-926f-995679edc619 | -10.66429 | -44.46254 | 2026-07-19 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d203b53-590e-3406-b4fc-dae61de50343 | -8.93558 | -47.60767 | 2026-07-19 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f06b98c-6f16-3546-9c7a-b9a1ee18c3d5 | -8.3623 | -45.39902 | 2026-07-19 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| af8e1bc6-d78d-3b02-9a25-a5776eadb45e | -12.65958 | -48.21571 | 2026-07-19 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bfa6d84b-09fb-39e3-921d-beeace2098f3 | -12.66841 | -48.20821 | 2026-07-19 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 618fc1f1-5d5f-3bbc-815e-14ded34b36bd | -10.89063 | -50.3143 | 2026-07-19 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33fca485-bc49-3f78-a471-53ceab2ca2ee | -3.97079 | -47.20302 | 2026-07-19 04:19:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97f83bb0-b274-3222-94cc-25c651ee2b73 | -8.88218 | -43.93852 | 2026-07-19 04:19:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 46a671d2-1b3b-31d8-b2c9-65c54d633fcb | -2.77591 | -49.46035 | 2026-07-19 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9ff7cd6c-bfc2-3c04-a00a-93b0e8861408 | -12.03721 | -55.45872 | 2026-07-19 04:19:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a53d3ef1-1377-3062-9911-656fe2a575a0 | -11.97357 | -47.10529 | 2026-07-19 04:19:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47b81129-f984-306f-97f9-c729f1895414 | -9.10138 | -50.609 | 2026-07-19 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a94a801d-7f7d-3404-8c39-091aac7cffd2 | -11.38968 | -47.51612 | 2026-07-19 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a95ba92-06e8-37ac-a025-4de927f4ce44 | -8.94378 | -47.60444 | 2026-07-19 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c839e034-8ef8-3012-a9ea-4b06b6950ee8 | -10.923 | -50.36969 | 2026-07-19 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ae193ad-43ca-3981-8c64-5b56df68972a | -2.77974 | -49.46587 | 2026-07-19 04:19:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ce2cdb4c-47dc-30f8-aace-0e7aa7d8510d | -9.47743 | -57.3189 | 2026-07-19 04:19:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4d9b5051-6efe-33bd-9d72-c82d2c75b9a4 | -8.35891 | -45.39845 | 2026-07-19 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8231ff68-1329-3651-9288-194b702d7bd3 | -14.5711 | -52.08245 | 2026-07-19 04:19:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54f34410-d9f2-37d3-bb04-c96b2a5334cd | -10.72063 | -46.57338 | 2026-07-19 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3ba7caf-3541-3be3-987e-59d3edbf3fc0 | -2.83308 | -48.86628 | 2026-07-19 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01b77a6f-4126-3bac-aa11-66f620c64bc8 | -8.94006 | -47.60381 | 2026-07-19 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a1cd8e97-f58a-3e73-a4c2-5ef411aecdc0 | -2.43165 | -47.03059 | 2026-07-19 04:19:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 694af688-e0db-32d4-a4c1-f7641e368101 | -8.94302 | -47.60894 | 2026-07-19 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ee64075-e4e0-3e4d-a085-52e61e8e5b5a | -12.65592 | -48.21507 | 2026-07-19 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33e48c5a-6a56-3753-b65a-a74f3ec6fc70 | -10.52402 | -42.39234 | 2026-07-19 04:19:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| debb5b8c-fb60-3e19-980c-24104c77ef32 | -10.70007 | -46.62279 | 2026-07-19 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df14f00d-57db-3941-90ae-ddeb9b76f5fb | -9.38811 | -40.75702 | 2026-07-19 04:19:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 22e3624a-2879-3277-beee-a9c23cf401e3 | -8.36291 | -45.39526 | 2026-07-19 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 42c05bb6-29d4-3c35-ac2e-1e833cbbaeb7 | -9.49705 | -46.66351 | 2026-07-19 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5bb59f4-8ea6-3b43-8761-bb6e2056fc1f | -10.70237 | -46.61833 | 2026-07-19 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9afeb63-eccb-33fd-880c-97837ab53a9d | -10.42591 | -46.32459 | 2026-07-19 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0325b1de-59a6-3117-84f5-d6fe5209e31c | -10.69724 | -46.61829 | 2026-07-19 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1172d6cf-95fd-3a5d-a10f-7a05e3baad79 | -10.70481 | -46.61563 | 2026-07-19 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0c148cc-8d76-37a9-a605-83261e458535 | -5.10873 | -38.06648 | 2026-07-19 04:19:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| b56ad1d5-055b-3cd3-87f6-3dddc8c695f4 | -9.95407 | -48.85543 | 2026-07-19 04:19:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 21895c9b-4a94-3da8-b0c0-45dbe843b6f0 | -10.84871 | -47.36544 | 2026-07-19 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 578a74f7-1602-3d1b-bd51-a49fcf967ede | -8.73078 | -47.82995 | 2026-07-19 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3743f050-5ff2-3849-ae82-4f1dbd6ab5f8 | -13.6189 | -47.48585 | 2026-07-19 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a19a55ef-6bd7-32e0-8811-39086ff5c5c7 | -14.7198 | -44.65742 | 2026-07-19 04:19:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f057836f-b596-3deb-8443-d3c8be84eafb | -10.92225 | -50.37383 | 2026-07-19 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f82e0d35-b901-32de-b811-62cc9de295f0 | -10.84512 | -47.36483 | 2026-07-19 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f51cf4a7-ec92-36e0-ae3c-86e41552bc4f | -10.70584 | -46.61894 | 2026-07-19 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36783a44-56dc-3f27-9ea9-1803c207ab1d | -8.94674 | -47.60958 | 2026-07-19 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| da033ef4-68db-37a8-a977-91519c5a5a77 | -9.47655 | -57.31995 | 2026-07-19 04:19:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d94078a1-b0d7-3a30-8d92-69bf842e9697 | -10.82139 | -50.24025 | 2026-07-19 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4c74368-3fa8-319b-b17a-5241380524f2 | -13.6692 | -48.78412 | 2026-07-19 04:19:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 59db5bfc-7e41-3a56-8185-3f1322084e3f | -13.66547 | -48.7835 | 2026-07-19 04:19:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |


[Clique aqui para ver as próximas entradas](README7.md)
