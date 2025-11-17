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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f00d3766-fd45-354d-ba49-37dc669697f5 | -2.51103 | -47.80227 | 2025-11-17 00:54:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 73d66edf-e50e-3490-bf95-74e033790c00 | -3.57323 | -52.09265 | 2025-11-17 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 72e24224-3a5c-3280-a203-97ee2f630fd9 | -5.83563 | -48.82858 | 2025-11-17 00:54:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| f4c32c10-9e8b-38e7-93ba-f0c4c3e9d02e | -3.59784 | -50.72088 | 2025-11-17 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 616ac8f6-bc8d-3c6d-8a57-ac4b8b7cd2cf | -3.40806 | -50.13586 | 2025-11-17 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 88422a9d-f144-33cb-83eb-c881d2af4f06 | -3.18769 | -50.65177 | 2025-11-17 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| e1fb9e8a-7621-3c2f-9872-073687ba593c | -3.75704 | -51.10445 | 2025-11-17 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 52283147-9b5f-3421-b977-cbd10c7e97b7 | -4.06856 | -47.51372 | 2025-11-17 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| d6a28f05-924b-38e9-a71f-9677adbb7e3b | -4.1002 | -48.02146 | 2025-11-17 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 7a645c33-4189-3a99-be36-5238c1035300 | -4.04596 | -50.48025 | 2025-11-17 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| a4363fb4-2621-3472-b202-fdafd97fdc2c | -3.14515 | -51.32412 | 2025-11-17 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| adcbf403-5911-3c5b-8050-861c5b63a692 | -1.5347 | -55.52084 | 2025-11-17 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c3d8d2ca-f9e1-338e-9d88-b516c01a7cbf | -4.01302 | -48.81147 | 2025-11-17 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 83b4332b-d688-3a42-b00e-8fa09de99e32 | -3.52389 | -51.24411 | 2025-11-17 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 48882a92-b5f5-368f-b1cf-df1b8eb6f23f | -5.83874 | -48.8484 | 2025-11-17 00:54:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 4b11d979-1cff-380a-92f9-bf339a81c872 | -4.06469 | -47.4917 | 2025-11-17 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| ccd936ca-4841-3472-91e9-9fc5ed5d0fa0 | -2.51173 | -47.8076 | 2025-11-17 00:54:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 125.1 |
| db82136d-0b0d-36b4-8a42-7767c5a33b9c | -3.28898 | -51.43393 | 2025-11-17 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b484fb8b-1b40-3fa8-b09d-7a575217261c | -3.40369 | -50.18966 | 2025-11-17 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| d53cb601-3a4c-3fce-8830-40d78c9bae4e | -3.30873 | -50.08513 | 2025-11-17 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 39ccc907-e7ef-3473-80ee-4146cd111227 | -2.47691 | -50.25061 | 2025-11-17 00:54:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| c79573e3-06d5-3cb6-baf7-8ba8b2c22f17 | -4.73494 | -46.38013 | 2025-11-17 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 6588d934-610a-3253-8863-c5ddc780635c | -3.17605 | -50.65353 | 2025-11-17 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e2dea9ee-7e02-31bf-87c0-f72b0dc75a96 | -3.46666 | -49.99543 | 2025-11-17 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 706f4ef9-8bac-37d0-a3af-81e375ee724c | -1.69104 | -53.68018 | 2025-11-17 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7e3e0568-3d17-394a-8076-00a0ec9c25f7 | -3.40552 | -50.11866 | 2025-11-17 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 7878e509-ab66-3cb3-b46f-107d57c245af | -3.76196 | -51.05964 | 2025-11-17 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 924988fa-56a4-313f-bb0d-45ceccdad6b3 | -5.12499 | -55.97214 | 2025-11-17 00:54:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ca4cf68e-c2a4-3835-b1d2-7dfe7fc2bc93 | -3.58634 | -50.72252 | 2025-11-17 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 1b4361b8-81f2-381d-9239-942a4ab2d140 | -5.82222 | -48.99834 | 2025-11-17 00:54:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 882eefdf-bea5-3ff5-a759-ab0b6b6d60d5 | -3.42608 | -52.93016 | 2025-11-17 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 92bdc379-80bd-3c01-8877-09bcfe8ec9c6 | -3.00887 | -51.3413 | 2025-11-17 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 71658c9e-a408-3457-8c7e-37219f9cba2c | -2.89065 | -53.28026 | 2025-11-17 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5765b60f-9aab-3dd7-9d1c-55868e512790 | -2.48048 | -50.24434 | 2025-11-17 00:54:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 1f7c8cdd-08ec-3e6c-b9fb-697e9ec1e3f2 | -6.8038 | -59.13937 | 2025-11-17 00:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f423043c-3a58-3ae7-b324-cce48ac1cfde | -2.5238 | -47.8332 | 2025-11-17 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| ac8fc3b1-3eb2-31ea-adba-088be12fe4e4 | -11.8295 | -49.2242 | 2025-11-17 01:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 18bb2e39-b4ec-306d-9524-0f20b5b6a20c | -3.2344 | -50.4952 | 2025-11-17 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 9fae0a75-d168-3af1-8532-38d4eccab485 | -4.7209 | -46.3832 | 2025-11-17 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 89142dba-c2b0-3232-8a2d-2142a3fbb01b | -9.5339 | -40.3531 | 2025-11-17 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 196.9 |
| f39eae4d-6e74-3498-ada2-7696f108717e | -6.6684 | -42.0553 | 2025-11-17 01:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 101.4 |
| ba7e0e06-2be9-33a9-a6a8-0a2e9400455c | -2.5053 | -47.812 | 2025-11-17 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| b16c3ede-1437-3d7d-9a43-e2e64d440355 | -9.5147 | -40.3558 | 2025-11-17 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 308.1 |
| 61bd68d5-8bb9-37ed-ba3d-fc951f2fa31c | -4.1596 | -50.2098 | 2025-11-17 01:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| dc48bca6-961a-3c26-8f36-12d482148c78 | -6.6875 | -42.0296 | 2025-11-17 01:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 298.0 |
| c61a2404-c284-3ed7-8bb1-44796e16290d | -9.5343 | -40.3282 | 2025-11-17 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 485.5 |
| 7d4d606d-b5d0-3338-abce-4e2e5dd4d30c | -2.5238 | -47.8115 | 2025-11-17 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 0925570c-a4dc-3b0a-bfaf-d2cff9632d14 | -11.849 | -49.2 | 2025-11-17 01:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| f4502fb1-b9cb-3c94-8000-e31377d5588c | -10.669 | -49.3597 | 2025-11-17 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 75b55c2c-2576-3a03-a1a6-d4c93a5bb996 | -6.6873 | -42.0535 | 2025-11-17 01:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 207.1 |
| 5652b78f-1a2b-3794-8f10-187346c50edd | -4.7395 | -46.3821 | 2025-11-17 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.4 |
| bc521113-5c7a-35b1-a7ec-5c3a92588eb0 | -11.8486 | -49.2218 | 2025-11-17 01:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| f3cd7f8b-492b-3969-bfaf-0771dc7e3821 | -9.5156 | -40.3061 | 2025-11-17 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 70.3 |
| 355d8c13-3d22-32cb-8b56-5c34a83ae90f | -4.0634 | -47.4943 | 2025-11-17 01:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 7b67a054-6541-3087-a843-311f33de6e80 | -6.6687 | -42.0314 | 2025-11-17 01:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 181.7 |
| 0548e273-3128-3bc5-ab68-e3a5d57da06a | -10.6687 | -49.3813 | 2025-11-17 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| ed300707-cca2-3589-a2ef-ad9affbc1a54 | -2.5053 | -47.8337 | 2025-11-17 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| d68bd5a9-17ca-3e78-95e2-81a98cd09aeb | -11.7017 | -48.8692 | 2025-11-17 01:00:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 6e9f9477-d923-3632-a40f-cfb64a008c92 | -9.5152 | -40.331 | 2025-11-17 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 857.0 |
| 914f8833-dae2-34e8-b81a-25946797eded | -11.7208 | -48.8669 | 2025-11-17 01:00:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 0efc0724-1eaf-3410-90ef-0e43f341e5ac | -2.5053 | -47.8337 | 2025-11-17 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 45bd27d7-01e7-39a7-9684-288828f4aa9b | -6.6687 | -42.0314 | 2025-11-17 01:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 154.1 |
| ad8a1bbb-207c-3fed-bb65-40bbf6ad5c68 | -4.8995 | -44.8686 | 2025-11-17 01:10:00 | GOES-19 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 9dc56c9a-d5f8-39c7-b150-776909fab2c7 | -11.849 | -49.2 | 2025-11-17 01:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| c2a03cef-8ecb-36ee-979d-ec235196f22c | -3.776 | -49.2517 | 2025-11-17 01:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 91ac713a-dc19-3ead-a75c-eab820bb3b19 | -2.5238 | -47.8115 | 2025-11-17 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 144b0c1a-34aa-331d-9086-4d09e99db75a | -4.7209 | -46.3832 | 2025-11-17 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 64ac7faa-82e1-3375-8d8c-fb0b1531175c | -11.8987 | -46.1934 | 2025-11-17 01:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 03ae3444-97a1-3966-b72e-7ab6556eca3c | -9.5152 | -40.331 | 2025-11-17 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1265.9 |
| d5948124-c167-3bd4-a88f-d3d69d7ec1e0 | -9.5147 | -40.3558 | 2025-11-17 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 414.1 |
| ca868a8b-6e3d-3b5e-8bb6-119f3687f226 | -11.8295 | -49.2242 | 2025-11-17 01:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 12a599af-b370-3836-9930-9482a4b82b5b | -9.5347 | -40.3033 | 2025-11-17 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 87.0 |
| d7a0a3c3-5bdb-3000-83c4-db660f681a21 | -2.5053 | -47.812 | 2025-11-17 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 1802d681-2be8-3dd2-97f7-861e44a91aa3 | -9.5339 | -40.3531 | 2025-11-17 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 211.2 |
| a5ab3837-ad88-352d-aee4-9ffbaf3ca3bd | -6.6684 | -42.0553 | 2025-11-17 01:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| 9b016732-512c-3cda-b7de-81a120473c66 | -9.5343 | -40.3282 | 2025-11-17 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 604.5 |
| 02345967-6873-3047-b1eb-34ca2ceb8821 | -6.6875 | -42.0296 | 2025-11-17 01:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 282.8 |
| 4d164528-fe31-3ab3-8bda-72d22fab763d | -9.5156 | -40.3061 | 2025-11-17 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 152.4 |
| 1fe94330-427e-3cbd-9a92-51bac4e4fd20 | -11.8486 | -49.2218 | 2025-11-17 01:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 06413b1f-9b0e-3ca8-ba21-9aebfc86fd43 | -6.6873 | -42.0535 | 2025-11-17 01:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 162.5 |
| 56245bbf-ed7f-3ce4-94ad-aeb36d9c3bcb | -11.7017 | -48.8692 | 2025-11-17 01:10:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| c667a98c-340d-31bb-81dd-328a96974cf4 | -3.2344 | -50.4952 | 2025-11-17 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 16c2d608-fd17-390b-ab32-8ff5e1a4a872 | -10.6687 | -49.3813 | 2025-11-17 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 688f7483-37a3-3d8b-9690-9d2885681790 | -10.669 | -49.3597 | 2025-11-17 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 9b738952-834b-3102-881f-0f7456133cca | -2.5238 | -47.8332 | 2025-11-17 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 54a72c5b-a1ac-3a12-9618-8a2e37a5ff79 | -11.7021 | -48.8474 | 2025-11-17 01:10:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| bc633b92-5119-3bd7-93fe-31cf2751585b | -4.7395 | -46.3821 | 2025-11-17 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 76.7 |
| fb22ab23-4e72-3266-b54a-9cf0c7f013e0 | -12.6971 | -46.774799 | 2025-11-17 01:12:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 70e22cdf-b8c2-35f1-ad73-82389d750e04 | -16.0086 | -59.895699 | 2025-11-17 01:12:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c10b6a4c-b373-339a-81d1-2c69ea36a305 | -11.8855 | -46.1679 | 2025-11-17 01:12:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d66979ad-1264-3ccd-bd5b-877188a63a2b | -12.8515 | -46.4599 | 2025-11-17 01:12:00 | METOP-C | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 355b5280-ab4b-3fb6-b4ec-7a26cdef1d00 | -11.9009 | -46.186901 | 2025-11-17 01:12:00 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 46593e39-2986-3548-830c-b5b8fa3afc0f | -16.0107 | -59.9062 | 2025-11-17 01:12:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 35b4fb04-fa82-3448-b196-82cc3dfff835 | -12.8568 | -46.4799 | 2025-11-17 01:12:00 | METOP-C | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| edf12d0a-2caf-3039-9b4a-1584db677b77 | -11.8912 | -46.189499 | 2025-11-17 01:12:00 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c8ec5b68-4c35-3e38-b843-03b15f2f9d74 | -13.7297 | -51.458401 | 2025-11-17 01:12:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 539a0b17-ffaa-3df7-b86f-4dc501504399 | -11.897 | -46.211102 | 2025-11-17 01:12:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 75c2fe00-2c91-3948-b944-4d1ee382d47d | -11.8172 | -47.598499 | 2025-11-17 01:12:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6596caa8-295e-3657-94a6-55324f276e76 | -12.7068 | -46.772202 | 2025-11-17 01:12:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 71793341-adb5-3f7a-b222-d5efb5ac54dc | -11.8224 | -47.578499 | 2025-11-17 01:12:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README8.md)
