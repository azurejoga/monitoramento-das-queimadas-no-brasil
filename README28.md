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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e712450-46e7-3715-aa47-4032db98459c | -13.3806 | -46.94835 | 2024-10-16 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c205f9da-fdf7-30df-a5d7-229f2f30f004 | -13.37982 | -46.95216 | 2024-10-16 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8081db87-476e-338c-ab24-e133fb6f8df9 | -12.51284 | -47.42175 | 2024-10-16 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1e8d5866-616b-31ec-8edf-c02336e7fda7 | -12.51197 | -47.42612 | 2024-10-16 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ac47a04d-98d6-3af5-b5ad-cf19b2981718 | -8.80565 | -47.86602 | 2024-10-16 03:45:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef64e3d9-0552-3df9-9bcf-186ac93ad88c | -9.28881 | -47.60559 | 2024-10-16 03:45:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9b29fb96-e088-343c-a042-5305283afccd | -9.28781 | -47.61071 | 2024-10-16 03:45:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ee9b44b-31bd-3134-92d6-2c9534faa8df | -9.2851 | -47.60244 | 2024-10-16 03:45:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d48fad8b-03bf-31ea-a590-973e599c19d7 | -9.28414 | -47.60755 | 2024-10-16 03:45:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e89c39b2-f834-373e-8f2c-5d18f396cf47 | -9.28261 | -47.60428 | 2024-10-16 03:45:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3b7a8f2-7ff9-3b6e-b836-e4c7542507f1 | -9.28161 | -47.60942 | 2024-10-16 03:45:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16b9832f-b630-38d8-87cb-3d9b3876bc2d | -9.20654 | -47.94897 | 2024-10-16 03:45:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cba4bd2-a245-3b7a-9555-f31dd991bdcd | -10.83379 | -47.7833 | 2024-10-16 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cce7d923-9d35-356f-a81c-3ae0283ce257 | -10.83309 | -47.78535 | 2024-10-16 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6b851021-2297-389b-a062-bacdd7c1aa08 | -10.83295 | -47.78757 | 2024-10-16 03:45:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62c9a344-4b80-3030-85db-3d6fce5e6553 | -9.99257 | -48.64261 | 2024-10-16 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 70b04fdd-3a57-3000-ab91-45469ff5f540 | -10.0239 | -47.67834 | 2024-10-16 03:45:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a815a976-1cd4-32ff-b3f7-a5d5d97bf971 | -10.02302 | -47.68295 | 2024-10-16 03:45:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1d22c1f1-c907-3454-b63a-e10b1aa7df7e | -10.02295 | -47.67788 | 2024-10-16 03:45:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 08e3464e-6b2f-30a1-be94-8b469a076a76 | -10.02213 | -47.68761 | 2024-10-16 03:45:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 58540376-9f83-3ffd-8f73-dddd31a5ad41 | -10.02205 | -47.68246 | 2024-10-16 03:45:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7c57fe28-a731-3e64-8e89-1efadb58e571 | -10.02113 | -47.68711 | 2024-10-16 03:45:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 47248101-3648-3c12-9e84-d321362bef08 | -11.20636 | -47.85598 | 2024-10-16 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a8b64a26-12d8-317b-867e-91b4082f2250 | -11.20123 | -47.84982 | 2024-10-16 03:45:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a640ac51-dc19-3fe8-a7cb-241a5e1528f9 | -12.37922 | -48.59276 | 2024-10-16 03:45:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c310d6a6-fa7a-3824-954f-db908d914693 | -8.75423 | -49.78075 | 2024-10-16 03:45:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e9642862-dd6b-31d9-bf0a-7dad52e6bd2b | -8.75067 | -49.77935 | 2024-10-16 03:45:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 12c44d3f-d36a-38d3-94b6-36a5323e6780 | -8.74924 | -49.78646 | 2024-10-16 03:45:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f227151f-e47a-36c8-a7c3-d5dff89b9823 | -10.8323 | -49.24626 | 2024-10-16 03:45:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8d6f89c1-9da5-39ec-b8d7-40b599a9c93d | -10.83108 | -49.25225 | 2024-10-16 03:45:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3d421566-393c-3608-a070-67c26c749381 | -10.82563 | -49.24487 | 2024-10-16 03:45:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e66f5d6b-ed36-3bf3-ac55-0c7f735eaf27 | -10.82437 | -49.25106 | 2024-10-16 03:45:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 298dde9b-0867-3f0c-8ad7-1d62218122fe | -3.1099 | -54.2263 | 2024-10-16 03:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 0accb465-491e-3c4e-8fdc-05710dae4829 | -3.1282 | -54.2459 | 2024-10-16 03:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| b5c7064b-3092-34d9-920c-a2d8acefb91f | -3.1283 | -54.2259 | 2024-10-16 03:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 7851f7c9-5624-3965-be4b-3ebebba1c5b7 | -3.958 | -46.4442 | 2024-10-16 03:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 103.7 |
| c57574e0-6d42-355a-9b69-0720b6c224c2 | -3.9581 | -46.422 | 2024-10-16 03:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 1dff77ba-5263-359a-b841-cda1f786bc9a | -9.114 | -47.0074 | 2024-10-16 03:45:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| f87ce063-6957-3042-a54a-204086d71ada | -9.1142 | -46.9851 | 2024-10-16 03:45:57 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 9e668cfa-fa51-3da9-8b22-446ca88c0e08 | -9.1709 | -46.9792 | 2024-10-16 03:45:58 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 949123fd-86f7-3ca5-9902-3e17e7f429c1 | -9.152 | -46.9812 | 2024-10-16 03:45:58 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 78b017d6-2fba-3a67-82ed-75cb5ba4930d | -9.1706 | -47.0014 | 2024-10-16 03:45:58 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 86846b90-5ac6-3c5e-b17b-6ac3cd2835c8 | -11.7292 | -65.2227 | 2024-10-16 03:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 4a982d82-76bb-3e2f-8f54-32ab189f303a | -11.7104 | -65.2235 | 2024-10-16 03:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 93fec863-d24e-3926-a8a9-be5fd6155d0e | -11.7103 | -65.2424 | 2024-10-16 03:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 6a7d563e-869e-3c7a-9f92-b084ac2b1559 | -11.6917 | -65.2243 | 2024-10-16 03:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 46.8 |
| d68ae571-53de-3861-9039-cab56436b791 | -17.1664 | -56.8439 | 2024-10-16 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.4 |
| 7f099445-4725-3d50-afea-41bf935cd853 | -17.2177 | -57.3102 | 2024-10-16 03:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.8 |
| cdc6fc84-3e26-331b-966d-1346e33ddbdd | -17.2081 | -56.6946 | 2024-10-16 03:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.0 |
| fdacb46b-24d0-37a7-a98d-38be177c6d04 | -18.254 | -56.6029 | 2024-10-16 03:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.9 |
| be583868-ab44-3ae6-a450-b51bfe9d25af | -18.2739 | -56.6003 | 2024-10-16 03:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.7 |
| 8edb9112-1c90-3dbb-9e52-ef0ac9cd1ab5 | -18.2742 | -56.5795 | 2024-10-16 03:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.7 |
| 97c848bc-b8cc-3faa-896b-7e657b91a18c | -19.5808 | -57.0071 | 2024-10-16 03:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.7 |
| 6157467f-1b10-3be1-9f32-994e0c1caed5 | -19.5812 | -56.9862 | 2024-10-16 03:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 207.6 |
| 3372294e-396b-3ebc-95dc-ae069ff9b9bb | -19.5816 | -56.9653 | 2024-10-16 03:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 139.7 |
| b776a287-c68e-3cf8-a395-727407bda200 | -19.6013 | -56.9834 | 2024-10-16 03:46:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 149.3 |
| fe5dcb21-e7d3-326e-abc8-065e144337a3 | -19.22171 | -40.13826 | 2024-10-16 03:47:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d691eebb-230f-37ee-b82c-875b3a4b568e | -19.22106 | -40.14215 | 2024-10-16 03:47:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 892774c6-379b-3ad1-ac63-9fa7149e2c4d | -19.16176 | -40.13919 | 2024-10-16 03:47:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 70d59c78-5e59-38b5-a81d-49de9ef3d665 | -19.37698 | -41.50811 | 2024-10-16 03:47:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 018b0332-6b90-373c-84ca-1cdfda662e67 | -19.13847 | -40.40237 | 2024-10-16 03:47:00 | NOAA-21 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 49218a26-9c65-32a3-94f1-03dfa23ce90a | -19.13779 | -40.40634 | 2024-10-16 03:47:00 | NOAA-21 | GOVERNADOR LINDENBERG | ESPÍRITO SANTO | Brasil | 3202256 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 982c2ef6-e475-3578-b1b2-7472802cdbda | -18.08708 | -41.4349 | 2024-10-16 03:47:00 | NOAA-21 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| af6b419b-35fa-3ff2-a8e9-8953919f9cd0 | -18.01591 | -41.45497 | 2024-10-16 03:47:00 | NOAA-21 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3d6a7f58-865f-3984-b9df-873a14f7295a | -20.02194 | -41.67167 | 2024-10-16 03:47:00 | NOAA-21 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b3a3145e-8267-30e7-bc9c-2f639444fc32 | -19.71723 | -40.35212 | 2024-10-16 03:47:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 179dfe38-58d5-34e6-95fb-3b239a9141a5 | -19.57677 | -41.24154 | 2024-10-16 03:47:00 | NOAA-21 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f418df8d-bf44-369b-b3a5-0984ff2251ee | -21.27485 | -42.10449 | 2024-10-16 03:47:00 | NOAA-21 | LAJE DO MURIAÉ | RIO DE JANEIRO | Brasil | 3302304 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1a786755-d7ab-3f3c-935d-8de042e7eff5 | -16.30522 | -42.04704 | 2024-10-16 03:47:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b4c47e03-85fb-35b5-aabd-db7e88b560af | -16.06223 | -42.2716 | 2024-10-16 03:47:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| dbfd10a2-d2da-3e0e-aa0f-5165208c5e6c | -18.0295 | -42.4152 | 2024-10-16 03:47:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2ffc397c-0f89-360b-b430-7e6abccce34c | -17.79073 | -42.55056 | 2024-10-16 03:47:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0ceb2204-f5b7-3555-b12c-67cffa9a7112 | -17.78627 | -42.05412 | 2024-10-16 03:47:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 16e20f33-1ba5-3dea-ab91-5b6e562a3112 | -17.78083 | -42.80745 | 2024-10-16 03:47:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58c847a6-722a-3d74-811b-f3ad2fbf81b0 | -17.77939 | -42.80929 | 2024-10-16 03:47:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3d5b84e-446d-38eb-9b99-e0d90e25e535 | -17.55802 | -42.32147 | 2024-10-16 03:47:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a756d29-04e8-3c33-b6a8-77aba5dd5b77 | -17.55416 | -42.32081 | 2024-10-16 03:47:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d6b5d7e-99bf-38eb-b060-f5c98ffa5eba | -17.29931 | -42.65033 | 2024-10-16 03:47:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 8abc1ef0-04d8-3be5-beaf-21bbf07181b1 | -17.29538 | -42.64957 | 2024-10-16 03:47:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 565e1ab9-328b-356f-97b3-0124b1730583 | -17.28654 | -42.6533 | 2024-10-16 03:47:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a87a0f9f-2002-388c-ac17-4c80ec0b03f9 | -17.27501 | -42.65384 | 2024-10-16 03:47:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e09c7776-79ed-3981-89c8-10ea7ceb9c0c | -17.27468 | -42.65124 | 2024-10-16 03:47:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 962c4c02-4bdb-384f-9c09-be36d6d523d5 | -17.25696 | -42.65877 | 2024-10-16 03:47:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 088fe021-7bd8-3e1d-bb88-62fdbbf33b7c | -17.25341 | -42.66063 | 2024-10-16 03:47:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 2a467a10-6cea-3ebb-9abd-3a0bece46988 | -17.24946 | -42.6599 | 2024-10-16 03:47:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 1e2ccba3-6be7-3ba8-a521-712884f07e4a | -17.24551 | -42.65919 | 2024-10-16 03:47:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| daf6b9bd-551c-34b5-a2a2-1b6b3ed26a35 | -17.03356 | -42.75061 | 2024-10-16 03:47:00 | NOAA-21 | LEME DO PRADO | MINAS GERAIS | Brasil | 3138351 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5b5eff1-e8c5-3250-9ef0-db14b996c612 | -17.03143 | -42.7503 | 2024-10-16 03:47:00 | NOAA-21 | LEME DO PRADO | MINAS GERAIS | Brasil | 3138351 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2350f1df-6336-359f-a597-403bec5b2868 | -16.81656 | -42.23749 | 2024-10-16 03:47:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 0f7a33c1-4cf2-39b1-aeb6-cf2c12a89480 | -16.67061 | -42.07971 | 2024-10-16 03:47:00 | NOAA-21 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6bf7499c-7df9-3351-9115-09974523f5ac | -19.14954 | -42.66669 | 2024-10-16 03:47:00 | NOAA-21 | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8d9e86cd-f64d-3332-a775-a5f9e32175cb | -19.04303 | -42.37435 | 2024-10-16 03:47:00 | NOAA-21 | AÇUCENA | MINAS GERAIS | Brasil | 3100500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 169faf76-209a-3932-8340-c8a3c56a474b | -18.6582 | -42.32318 | 2024-10-16 03:47:00 | NOAA-21 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1933d1c9-d4b3-3983-ab1f-527944f7dc9e | -18.54592 | -42.64446 | 2024-10-16 03:47:00 | NOAA-21 | CANTAGALO | MINAS GERAIS | Brasil | 3112059 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b2047e51-e1e9-30f4-b633-1f2963ef0d75 | -18.31901 | -41.76082 | 2024-10-16 03:47:00 | NOAA-21 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e171001f-65cf-3bc4-b4bf-8ca34684acb8 | -18.29371 | -41.73891 | 2024-10-16 03:47:00 | NOAA-21 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 0901a724-f489-39de-bcf0-ded75e78e398 | -18.29289 | -41.74356 | 2024-10-16 03:47:00 | NOAA-21 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cec4471d-a5b6-37dd-90f9-6d0587fc462c | -18.29003 | -41.73815 | 2024-10-16 03:47:00 | NOAA-21 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 989a254c-0411-333c-9526-faedbd8d7755 | -18.28921 | -41.74282 | 2024-10-16 03:47:00 | NOAA-21 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8e5b0ab3-cd51-36ac-b9b2-b7cdba6d8fcd | -20.68066 | -42.33349 | 2024-10-16 03:47:00 | NOAA-21 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README29.md)
