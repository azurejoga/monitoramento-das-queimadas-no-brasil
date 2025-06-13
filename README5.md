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
| 1700b9ca-7701-3dfd-ace6-4a82f166c42f | -11.3447 | -54.604099 | 2025-06-13 01:09:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 55286d6c-3d00-3805-b7bc-18ddf8576bb5 | -13.9059 | -54.6291 | 2025-06-13 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 106.5 |
| b0f75cc0-d6a9-3af2-9559-b4efad42caaa | -10.6495 | -49.4051 | 2025-06-13 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| a9de7688-c3b9-316b-8093-cb268a1dcd8a | -7.2403 | -43.1134 | 2025-06-13 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 58660d13-7a81-3cde-8375-b7196bfc7fea | -13.8867 | -54.6312 | 2025-06-13 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| c6d288dd-eeeb-3525-a201-5dbaa1fa1196 | -10.6492 | -49.4267 | 2025-06-13 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 78879543-fa82-3971-9e9d-898866b0ef7e | -11.5649 | -54.559 | 2025-06-13 01:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| bf52e238-eb0a-39de-b840-d6dc3f702cad | -6.9422 | -44.5562 | 2025-06-13 01:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 6cc41770-b76a-3267-99d0-5b0f723b9a24 | -7.2214 | -43.1153 | 2025-06-13 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.6 |
| dc3787cd-026e-31b2-af57-9fb206c4db64 | -13.9062 | -54.6084 | 2025-06-13 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 5a855bc4-3fce-3a5c-87aa-27dcbf9a2153 | -10.9167 | -56.8336 | 2025-06-13 01:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 761bd61f-d67b-3c88-8f3d-294a927370c6 | -11.5647 | -54.5794 | 2025-06-13 01:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 470149c6-10d7-3e25-831e-b7d50b9bca9d | -10.7048 | -49.507 | 2025-06-13 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| f1899327-1f75-3f22-9cd9-e01feeda9c81 | -10.6302 | -49.4288 | 2025-06-13 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| d746de29-8f53-3d5c-9050-0d5e71a3e739 | -8.8165 | -46.682 | 2025-06-13 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| b06a72c5-ce35-3c46-9055-5e6c55f3a5a8 | -9.4114 | -57.5529 | 2025-06-13 01:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| aebaf5ff-0e02-36bf-88a2-932a9480fe35 | -10.7051 | -49.4853 | 2025-06-13 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| f046a5f2-d048-3f93-b317-4b4ec1155b6a | -10.9355 | -56.8322 | 2025-06-13 01:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| d1325cba-0085-3e8d-a974-f8c69dce1943 | -13.887 | -54.6106 | 2025-06-13 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 88ef9dd0-92ff-3ba1-a3a5-ff11f7924e62 | -11.5649 | -54.559 | 2025-06-13 01:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 710578dd-999b-3fd4-8e60-166b38ed8803 | -7.2214 | -43.1153 | 2025-06-13 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.0 |
| 249f2bac-5c51-3b7b-9b4f-e01da658877a | -13.9059 | -54.6291 | 2025-06-13 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 2fd305ef-1fc6-3801-83d0-ecf2893be182 | -10.6302 | -49.4288 | 2025-06-13 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 655c456f-0658-376a-97bf-5ae35c3e83e9 | -9.4114 | -57.5529 | 2025-06-13 01:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 57094e8a-fdac-3576-b2c8-0374fae889ea | -11.5647 | -54.5794 | 2025-06-13 01:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| a1b881cb-92ba-3340-a9dc-fbe6cb05e088 | -11.5836 | -54.5777 | 2025-06-13 01:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 03b5f999-31e4-380c-8d4f-8c361167ea1f | -10.6492 | -49.4267 | 2025-06-13 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| e6eae394-1b2c-3051-ba75-90878f06deea | -8.8165 | -46.682 | 2025-06-13 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 6f3a6007-cb44-3178-afd4-7fe3e8ade3c5 | -13.8867 | -54.6312 | 2025-06-13 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| ea514a7c-9197-3ae6-8c3c-faafa9eabcf7 | -6.9422 | -44.5562 | 2025-06-13 01:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 415550fe-b81f-3f5a-8912-b85c6bf4765a | -10.9355 | -56.8322 | 2025-06-13 01:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 047de00a-4553-3a5a-bd2c-bea92ecab496 | -10.9167 | -56.8336 | 2025-06-13 01:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| c2658817-6c5f-347f-b83f-f3d3a9f886ec | -11.5649 | -54.559 | 2025-06-13 01:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 2fd322ac-df90-390e-809f-3442417a891c | -10.9355 | -56.8322 | 2025-06-13 01:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 43.2 |
| c91b4de7-f1d6-316b-b3d1-0be462954bfe | -13.8867 | -54.6312 | 2025-06-13 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 34e8bf96-6947-3dc4-87cb-78f2593b6a77 | -13.9062 | -54.6084 | 2025-06-13 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| ed084764-8e9c-3587-a846-24447a0869e6 | -11.5647 | -54.5794 | 2025-06-13 01:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| d558f059-2092-3585-acb4-bb9df825a778 | -9.4114 | -57.5529 | 2025-06-13 01:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| ecb17b0b-8638-3208-9476-0a9b54fbb14c | -10.9167 | -56.8336 | 2025-06-13 01:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 14462df6-72bf-3290-8de8-419776843fdf | -6.9422 | -44.5562 | 2025-06-13 01:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 84f0b2fe-11bc-3a6e-81e4-124b4a1799b1 | -10.7051 | -49.4853 | 2025-06-13 01:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 84714dae-9818-3611-9376-346ec2e2a95b | -7.2214 | -43.1153 | 2025-06-13 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| ae2f1176-5d34-3f51-97a7-6f13f4f567f5 | -10.7048 | -49.507 | 2025-06-13 01:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| beb1300b-1686-398a-a6c9-4d4c82077524 | -10.6302 | -49.4288 | 2025-06-13 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 1cd4e18c-65cc-354c-b00e-10035acca16a | -10.6492 | -49.4267 | 2025-06-13 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 06ff168e-c19f-3bc7-b17d-7c33bac734c3 | -13.9059 | -54.6291 | 2025-06-13 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 119.0 |
| fa348ba6-52a2-38b1-a7a7-ccfbd8db4630 | -9.3927 | -57.5541 | 2025-06-13 01:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| c00e33c0-4a11-3bdc-ab2e-72111a6fe96e | -7.2214 | -43.1153 | 2025-06-13 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.4 |
| e44998a9-68ef-3c1a-ae80-8799bcebaca6 | -10.6302 | -49.4288 | 2025-06-13 01:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 4392be2b-35e2-3ecc-96be-58a4938586bd | -13.9062 | -54.6084 | 2025-06-13 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 98cc9685-5a05-321c-bc65-d2c6336db9fe | -10.7051 | -49.4853 | 2025-06-13 01:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| f04bfe33-0b3f-38e3-a9b3-5a17697be797 | -10.6492 | -49.4267 | 2025-06-13 01:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| f5501c34-94be-3a7b-a661-9aca0272f8f4 | -9.4114 | -57.5529 | 2025-06-13 01:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| a9aca3a7-1a8b-3d3d-a143-f51b94392882 | -7.2403 | -43.1134 | 2025-06-13 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| d20ed451-44c4-3bc3-9d93-3b319c3a3266 | -10.7048 | -49.507 | 2025-06-13 01:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 4a529456-e979-3342-82af-109612f504d3 | -11.5647 | -54.5794 | 2025-06-13 01:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 206a11d3-3f91-3201-9cf0-8cfffed8f44a | -11.5649 | -54.559 | 2025-06-13 01:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 38c04675-5575-34f9-834e-e9aa043e047c | -6.9422 | -44.5562 | 2025-06-13 01:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 8dd9209c-f89e-3b66-9fd8-74fdc02b308d | -13.8867 | -54.6312 | 2025-06-13 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 955880a5-d497-3153-b365-bb74527bfbe3 | -13.9059 | -54.6291 | 2025-06-13 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 416fc16e-d060-3e08-ae6d-61da0fb3168f | -10.9355 | -56.8322 | 2025-06-13 01:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 11fd4403-fa16-348f-8d15-2b6413c8a52c | -10.7051 | -49.4853 | 2025-06-13 01:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 9581f2cd-40d5-3872-b6a0-e10302043ecb | -13.9062 | -54.6084 | 2025-06-13 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 03124e32-5354-3da8-aacd-66e43037ccaf | -11.5649 | -54.559 | 2025-06-13 01:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 20684d35-686d-35d1-9008-a635f1e95e23 | -6.9422 | -44.5562 | 2025-06-13 01:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| ad43379c-cdda-39bc-b0bd-f461faa8885e | -11.5647 | -54.5794 | 2025-06-13 01:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 690a6ffe-5b76-3732-8fd8-f76484d8cb7c | -7.2214 | -43.1153 | 2025-06-13 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.5 |
| b93fcbe9-7335-333f-9452-b97a8f428d7d | -10.6492 | -49.4267 | 2025-06-13 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 1610f99e-b168-3451-b5e9-4f6d992dc510 | -10.6302 | -49.4288 | 2025-06-13 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 500b745c-0e1e-3da2-859a-3567d5d89b65 | -10.6483 | -44.4861 | 2025-06-13 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 54.8 |
| bb946184-3112-302b-ae8b-57df9f10339e | -9.3927 | -57.5541 | 2025-06-13 01:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 321f1127-3e6e-33ef-883f-0f7cb6adb919 | -9.4114 | -57.5529 | 2025-06-13 01:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| cd5d63db-4508-316f-a736-4b501d4a3fb9 | -13.8867 | -54.6312 | 2025-06-13 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 008219c0-7775-34e4-b836-e109838c5a64 | -13.9059 | -54.6291 | 2025-06-13 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 114.0 |
| e5802324-a501-3159-9028-2564e5770599 | -10.7048 | -49.507 | 2025-06-13 01:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 2c0c818c-a6d9-3357-9d6f-fa4308e81c5f | -7.6671 | -43.6557 | 2025-06-13 01:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 438f6998-d92d-3016-8004-224344f3e813 | -10.9167 | -56.8336 | 2025-06-13 01:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| d781dd7b-767e-3bdf-a3b7-a4904f973cce | -7.6671 | -43.6557 | 2025-06-13 02:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 427.4 |
| eff19f55-16e2-3520-89a0-0f603732296e | -10.6492 | -49.4267 | 2025-06-13 02:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 68883b49-87b2-364d-b42c-110c6b2c90b0 | -10.9167 | -56.8336 | 2025-06-13 02:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 84e65cbe-21e5-325d-8422-db319f2db30b | -11.5647 | -54.5794 | 2025-06-13 02:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| b513fd91-a617-318c-a561-27612a113d3b | -10.7048 | -49.507 | 2025-06-13 02:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 71d9e38a-4862-30ba-ba6c-7221185a412d | -13.9059 | -54.6291 | 2025-06-13 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 64c23b7b-4249-3268-a28c-092b7cfa2cf6 | -13.8867 | -54.6312 | 2025-06-13 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 8b72457d-3230-3a47-910b-228b713adc7d | -11.5649 | -54.559 | 2025-06-13 02:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| a18f8213-c400-3e78-b753-ad1b52676dcc | -7.686 | -43.6538 | 2025-06-13 02:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 707c8c41-5657-3c27-9300-bebe60130a0c | -7.6863 | -43.6304 | 2025-06-13 02:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 65a521ea-a98e-38f4-8591-4712b6ed48fb | -13.9062 | -54.6084 | 2025-06-13 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 64c4435b-1933-351a-b738-89d25cac643c | -10.9355 | -56.8322 | 2025-06-13 02:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 4e99efe7-bae0-323f-b51e-df7c8147875a | -7.6485 | -43.6343 | 2025-06-13 02:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 49.9 |
| de150086-5dff-39de-a642-b52d12584e36 | -7.6483 | -43.6576 | 2025-06-13 02:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 5097a527-4b81-3bf4-befe-cd57838ca201 | -7.6674 | -43.6323 | 2025-06-13 02:00:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 304.8 |
| a55f231a-82ea-35a1-b195-fd5fc1d971cf | -10.9297 | -56.849201 | 2025-06-13 02:03:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b11c5407-8041-3284-99ae-56dc4c00ebe5 | -9.9566 | -64.975899 | 2025-06-13 02:03:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0934b2d7-fd22-37f3-8f13-78a142f0d994 | -10.9201 | -56.851898 | 2025-06-13 02:03:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 48b9eb90-e2a7-3268-a7d0-f13b4db0c73a | -9.9587 | -64.984703 | 2025-06-13 02:03:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 24910a8e-5084-3eb1-adb1-34274b1c09aa | -10.6492 | -49.4267 | 2025-06-13 02:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 871070f5-a7e3-3a49-985f-d197a2828f51 | -13.9062 | -54.6084 | 2025-06-13 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 48.5 |
| ec3a2042-e95f-3b29-ab55-4e0029f1168c | -7.6863 | -43.6304 | 2025-06-13 02:10:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 8d2f6f08-16b8-31cd-b80f-6360ec3edae5 | -11.5647 | -54.5794 | 2025-06-13 02:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |


[Clique aqui para ver as próximas entradas](README6.md)
