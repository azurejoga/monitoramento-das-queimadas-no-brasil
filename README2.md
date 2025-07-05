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
| 70a083bb-d447-3cdd-ac0a-eb0ab00693d8 | -8.81434 | -45.97241 | 2025-07-05 00:43:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 9abdad1e-3bfc-3900-8664-71cd3c418c78 | -7.34525 | -49.63293 | 2025-07-05 00:43:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| bdc2dc8e-1ab0-3a96-8b0f-24c1fd738432 | -10.56046 | -49.43826 | 2025-07-05 00:43:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 83e1ff90-4e4f-3a3d-896a-e1d5f4806e3d | -7.09087 | -49.5974 | 2025-07-05 00:43:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d244e947-78d5-3482-8c50-87df7d1d42bd | -7.28821 | -45.70734 | 2025-07-05 00:43:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| ddfc3adf-64ab-3b4f-b9f5-25c37bb3dd17 | -6.68058 | -43.15834 | 2025-07-05 00:43:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 3e2f3322-8179-3a8f-ac13-0b80ba9d6e88 | -6.01354 | -44.53082 | 2025-07-05 00:43:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 6c711ea5-aef0-3d05-ad3b-8b1bb4f37898 | -7.19498 | -45.33361 | 2025-07-05 00:43:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f6c75d7a-d9bd-39f8-a1f2-ba0c9de3224c | -4.11303 | -47.93316 | 2025-07-05 00:43:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| d58bd334-9990-3b25-bfec-9ba0b8f086d0 | -8.8162 | -45.98464 | 2025-07-05 00:43:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 00f8c11e-7183-335c-b9c0-0d3d6fdb245d | -6.85094 | -42.80316 | 2025-07-05 00:43:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| e010fdb8-b0ea-3f3d-a82c-889d2e4e77a9 | -5.42594 | -47.15351 | 2025-07-05 00:43:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| fda0cdd8-993c-331c-8ba9-478e96b52ec5 | -5.72367 | -49.11012 | 2025-07-05 00:43:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 865c2ac7-8801-3ede-8be2-0af186660b89 | -6.88088 | -48.16833 | 2025-07-05 00:43:00 | TERRA_M-M | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 7481f2bc-b456-3337-9b53-f81159e2b051 | -4.11745 | -47.93682 | 2025-07-05 00:43:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 9588b7ec-aff7-3212-9160-6af506dd35e4 | -4.40068 | -48.94187 | 2025-07-05 00:43:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 354ae309-6051-3219-b9d8-2a2ba0b4997c | -7.25876 | -43.08881 | 2025-07-05 00:43:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| c14423f5-84dd-386f-ba7c-3db324132ecd | -8.02021 | -49.7198 | 2025-07-05 00:43:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b34e937f-36d0-33b1-bff8-86ac1c5a70f7 | -5.0624 | -43.72092 | 2025-07-05 00:43:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| d0a69aa2-56c6-32f5-9680-fa99fc674f3f | -10.60565 | -52.84401 | 2025-07-05 00:43:00 | TERRA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5f67b5c5-dc19-39c8-b943-ef3a8972c8c7 | -10.55162 | -49.43954 | 2025-07-05 00:43:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| cc2d7a65-2503-318d-af37-61684409c69a | -10.35886 | -48.71578 | 2025-07-05 00:43:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 96c27d8a-2bb4-3da7-a581-0eb9346de02d | -3.52791 | -48.42786 | 2025-07-05 00:45:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| a5aec8dd-79b5-3c24-bd69-0bf9098d8660 | -3.48227 | -48.44465 | 2025-07-05 00:45:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| f3c81d66-6020-3338-9c17-b8daf2f704ac | -3.51989 | -48.43921 | 2025-07-05 00:45:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 83ca2d1d-6ffb-3640-b545-a929d5c82eb2 | -3.52931 | -48.43792 | 2025-07-05 00:45:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 40e9d706-6320-3b56-b8c4-1a8610dc39cf | -3.49165 | -48.44314 | 2025-07-05 00:45:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| ac1531de-438d-36e9-aa96-337ddfa61997 | -2.99225 | -47.45027 | 2025-07-05 00:45:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6072daaf-498d-39fe-b5ec-c425ca5ff141 | -3.48369 | -48.45465 | 2025-07-05 00:45:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b72cf301-dfce-3a5a-ab4b-47727ec77631 | -7.2405 | -43.0899 | 2025-07-05 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.8 |
| 2bace2fe-d0d4-3283-b703-d5b790f5d5f5 | -10.5586 | -49.1337 | 2025-07-05 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 02906732-7919-3d94-99a6-b128e10f2a74 | -10.5589 | -49.1119 | 2025-07-05 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 25e31966-d1cd-3b81-99fe-779293536027 | -10.5586 | -49.1337 | 2025-07-05 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 64947591-29f3-36ec-81d7-fc8c8f6abbc2 | -10.5544 | -49.437 | 2025-07-05 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| adf4b32c-ed1e-328e-80f8-d6807c4afec5 | -7.2405 | -43.0899 | 2025-07-05 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| f1895934-7389-344f-9020-bc2d4a77d98a | -10.5544 | -49.437 | 2025-07-05 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 1b4562e3-f5b1-356c-9838-1956e56c530a | -10.5586 | -49.1337 | 2025-07-05 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 3797bd1b-a2a6-327f-9069-0c5af8b9f771 | -9.496 | -40.3337 | 2025-07-05 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 108.0 |
| 71bb6c8a-2102-343f-8b46-0d79ca8891cb | -9.4769 | -40.3365 | 2025-07-05 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 56.5 |
| 522f63f5-e557-3609-94dd-7d282983bb69 | -7.2405 | -43.0899 | 2025-07-05 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 63.9 |
| 6af340dd-47c3-326b-aa14-3d25b39563e5 | -10.5586 | -49.1337 | 2025-07-05 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 6056133c-ea83-3b87-bb59-fc81b01db57b | -9.4769 | -40.3365 | 2025-07-05 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 59.6 |
| 54004298-50c4-3be2-a33b-ee03662e3707 | -7.2405 | -43.0899 | 2025-07-05 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.3 |
| 5822baeb-3e4a-3dca-9c41-5e42b5547b53 | -10.5586 | -49.1337 | 2025-07-05 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 34b94917-8bac-333e-88ae-ad7e5b5336ed | -9.496 | -40.3337 | 2025-07-05 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 110.6 |
| 4c22ce01-b1bf-32b0-be79-b95cde61d07a | -9.4956 | -40.3586 | 2025-07-05 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 80.2 |
| 83873ffc-2b54-30ac-a1c5-addb83dec4fb | -9.4765 | -40.3613 | 2025-07-05 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 41.6 |
| 3f44c170-40a0-3fb7-a9db-d6bfb9af47b5 | -9.496 | -40.3337 | 2025-07-05 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 183.0 |
| a6e96ced-1ca5-3f89-8ebb-3186898a8a6c | -9.4769 | -40.3365 | 2025-07-05 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 100.6 |
| 2f98d577-91c5-33ca-80c1-d3812b98718f | -10.5586 | -49.1337 | 2025-07-05 01:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 9bdd291c-1f9d-3565-b8e2-e1f393d59f13 | -9.4956 | -40.3586 | 2025-07-05 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 65.6 |
| 96fc66c6-5b5e-360f-98ae-e86c075fc338 | -9.4769 | -40.3365 | 2025-07-05 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 61.4 |
| 1b4b8d48-5c51-3c36-90b0-17a11d7f2b14 | -10.5586 | -49.1337 | 2025-07-05 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 45404463-dced-3232-941a-2506d124fb28 | -9.496 | -40.3337 | 2025-07-05 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 135.9 |
| caee0dd7-6b54-3ce0-864f-bcf3f1943d45 | -10.5776 | -49.1316 | 2025-07-05 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| ec3d1f36-935e-3d0e-9ab3-29610b5f065c | -10.5586 | -49.1337 | 2025-07-05 02:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| a79a6b97-68c1-3735-9dd0-9db79967f6eb | -9.496 | -40.3337 | 2025-07-05 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 45.4 |
| 32176fa8-6c28-3799-9504-57bbfe9b0fa6 | -10.5586 | -49.1337 | 2025-07-05 02:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| cef2e46d-e6e8-3f20-9533-f3d63d644eb8 | -9.496 | -40.3337 | 2025-07-05 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 130.1 |
| c9260979-fb2a-3003-b36d-de1a7f2c4c2f | -9.4769 | -40.3365 | 2025-07-05 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 62.8 |
| 7044fc66-790d-30d7-9afd-73a3ba02d40c | -9.4956 | -40.3586 | 2025-07-05 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 46.7 |
| d225288c-f033-37e0-9106-5a64c5ddbb4f | -10.5586 | -49.1337 | 2025-07-05 02:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 771b78c8-fd6b-3da9-ad11-35ec378b611f | -9.496 | -40.3337 | 2025-07-05 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 46.4 |
| 0ee80e76-7bf0-3a5d-abf4-6c06046e9e7e | -10.5586 | -49.1337 | 2025-07-05 02:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 628eab38-a8a9-3dc6-9b20-4352d66a54e3 | -10.5586 | -49.1337 | 2025-07-05 02:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 05936545-d054-326e-9176-0113cdc9a117 | -11.8839 | -44.8654 | 2025-07-05 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.4 |
| e55b3a40-e276-3af5-af6b-3b435d6b462f | -11.8839 | -44.8654 | 2025-07-05 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| a8228eb6-feaa-302a-a6ec-ab7aecc0581f | -11.8835 | -44.8887 | 2025-07-05 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 98bb7f1e-01d7-3eef-9c08-d434bf49794c | -6.60699 | -43.89061 | 2025-07-05 03:30:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2bc5b7c2-219b-33d2-9232-7ebf3a29d72c | -8.25208 | -35.71052 | 2025-07-05 03:30:00 | NOAA-21 | SAIRÉ | PERNAMBUCO | Brasil | 2612000 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 187df335-d3ac-3559-8e54-67eeb3f54651 | -7.23533 | -43.09167 | 2025-07-05 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| da513458-0a34-3dc1-b525-c46fbec8baca | -8.38489 | -38.10472 | 2025-07-05 03:30:00 | NOAA-21 | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 670f9247-b18c-319f-a2d6-ba20bee9cece | -5.60847 | -45.17934 | 2025-07-05 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a898e777-e49f-352f-9fdf-28c044fb9fbb | -7.2479 | -43.0894 | 2025-07-05 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 25d9e449-caa9-31bb-b93a-4e9849649253 | -5.06546 | -43.73285 | 2025-07-05 03:30:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ffe770ef-c2c5-3e9c-a4ec-84ebfe88580f | -6.85199 | -42.79995 | 2025-07-05 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b3497dd8-60d2-358c-be5b-c9f1cfc093f5 | -5.05017 | -43.85829 | 2025-07-05 03:30:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 113c2547-5c44-3c14-9ef9-ece51695dd80 | -6.01398 | -44.5322 | 2025-07-05 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9acb89fc-d129-3e5b-aaad-69344c7629fc | -6.01504 | -44.52649 | 2025-07-05 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85c3c050-01d2-3949-b54d-7381adab1485 | -4.00261 | -43.23734 | 2025-07-05 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d57746c3-3540-39ea-8430-d18772057f3e | -7.29848 | -45.36698 | 2025-07-05 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d86541cb-0e7e-373e-a264-9d62e9c2320b | -7.22947 | -43.09057 | 2025-07-05 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| bdf3d13d-de50-363c-af27-36311239857a | -5.99683 | -43.73893 | 2025-07-05 03:30:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 388e5a34-22e1-3acd-91be-50414f41d044 | -5.9977 | -43.73408 | 2025-07-05 03:30:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b15e4d5e-d843-36ae-9121-51eb2f52a37d | -7.22359 | -43.08949 | 2025-07-05 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d700b264-ef46-3b9d-ae5f-bf48e82d1107 | -7.23091 | -43.09173 | 2025-07-05 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 4051220e-fca1-3250-85df-529a2d0103a6 | -6.85273 | -42.79595 | 2025-07-05 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cfc3904f-464d-3f94-a032-5e19692cfbbc | -7.25379 | -43.09035 | 2025-07-05 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 3b6f61c9-2577-3d5e-bc87-4673c5072652 | -5.06929 | -43.72704 | 2025-07-05 03:30:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b42c7e17-3cb5-3e39-b598-e2eba4d14b66 | -5.60963 | -45.17304 | 2025-07-05 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d3bb1e68-d77a-3ea4-b174-68e995e501f9 | -3.99895 | -43.23436 | 2025-07-05 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 806c4670-ddac-3718-ab77-34f19a0cc810 | -7.22504 | -43.09064 | 2025-07-05 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| c9284bf1-957a-3e3c-aaab-448878f39804 | -6.84733 | -42.79372 | 2025-07-05 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| df4bb9d6-779a-3676-befd-67af19ed39e9 | -6.8524 | -42.79895 | 2025-07-05 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f3109c38-328f-39a8-b698-6167a86ebd3a | -7.24418 | -43.08532 | 2025-07-05 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 1f47ac4a-a0e3-3860-a8db-08faeb9f7d97 | -7.2436 | -43.0798 | 2025-07-05 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e5f02150-2403-3b58-bb50-9ef3f7dda330 | -7.22579 | -43.08643 | 2025-07-05 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 6696dabe-8cb9-3947-aa05-1ef7ee915513 | -5.07271 | -43.72865 | 2025-07-05 03:30:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25630d29-03f2-381e-820c-e9c670178d60 | -8.07335 | -34.97617 | 2025-07-05 03:30:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| bc93ad40-8db2-3f7b-b53e-0abfe75bdc00 | -5.04582 | -43.85642 | 2025-07-05 03:30:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README3.md)
