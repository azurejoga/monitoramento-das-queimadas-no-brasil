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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63bfb201-6fc4-3ccf-a460-bf916a7af1c4 | -5.83434 | -44.66045 | 2024-10-22 05:10:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37d72ca8-a765-34c3-ac8a-ba8964325152 | -5.82772 | -44.65936 | 2024-10-22 05:10:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd0f8b22-ac5b-362b-906d-cdae696721ee | -5.59278 | -44.87693 | 2024-10-22 05:10:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 056f6028-50b4-3ba8-ba8d-fc985fba380c | -5.59203 | -44.88243 | 2024-10-22 05:10:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 54c66aa6-d3e1-3931-8de4-c88866584dfb | -5.58698 | -44.87067 | 2024-10-22 05:10:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| c6161364-84eb-3bff-8d33-ccd0c4762b57 | -5.58622 | -44.87622 | 2024-10-22 05:10:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 5f598492-0a58-3f69-902a-626cfebbd6d0 | -5.58548 | -44.88165 | 2024-10-22 05:10:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| bb9dac47-3de5-339d-89f8-c0ad00aa6403 | -5.58043 | -44.86992 | 2024-10-22 05:10:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| e0de079f-5638-3e3c-b547-732cee2b3176 | -5.57967 | -44.87543 | 2024-10-22 05:10:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 1776925d-f7cb-3785-a612-2aca329c645b | -5.57893 | -44.88087 | 2024-10-22 05:10:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| c9ec2997-fc61-3f25-82b8-5d3da765b2eb | -2.99398 | -45.61386 | 2024-10-22 05:10:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a1f6b600-5973-359d-ba6b-58de74f5dbe7 | -2.99051 | -45.61145 | 2024-10-22 05:10:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a2f5dafc-7f58-3d93-8c4f-558d291b2d4b | -2.98797 | -45.61292 | 2024-10-22 05:10:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 32f50de0-999e-3343-972b-f226c017afac | -2.9845 | -45.61045 | 2024-10-22 05:10:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3f372011-ab1b-33cc-ad24-4c2b702f5120 | -2.98385 | -45.61499 | 2024-10-22 05:10:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2f1656a2-8117-373f-b788-bf5596e43b98 | -2.85458 | -45.46112 | 2024-10-22 05:10:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c88938a7-499f-3c7d-a38b-8ae65a71ced6 | -2.85391 | -45.46565 | 2024-10-22 05:10:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ecf09e8-5423-3eaa-8e1e-0a10ae40dec2 | -4.94772 | -45.42186 | 2024-10-22 05:10:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2357f6d7-ae76-318e-ba39-576b2258873b | -4.94706 | -45.42663 | 2024-10-22 05:10:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ad05d27-91aa-3514-8728-d2cca2d3c7c7 | -4.94638 | -45.43154 | 2024-10-22 05:10:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15b955ac-f965-3b37-8bf8-87c59fd0c80b | -4.90388 | -45.8293 | 2024-10-22 05:10:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e31b015-668a-3a7d-86f9-77d9ec38eb22 | -4.90325 | -45.83381 | 2024-10-22 05:10:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd35a77b-4e03-30fb-9dea-4bd45a01b841 | -4.90263 | -45.83824 | 2024-10-22 05:10:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b19953cf-7219-3574-9dbc-e4858ba0f87f | -4.89713 | -45.8331 | 2024-10-22 05:10:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ab8fc161-60aa-39a2-91f9-d42b2c312fd2 | -4.89654 | -45.83732 | 2024-10-22 05:10:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cd82d26b-530e-377b-8b75-921ab08d40de | -4.83578 | -45.86333 | 2024-10-22 05:10:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 107939c8-054f-3b46-a611-26a2f5a60bdc | -4.56274 | -45.80427 | 2024-10-22 05:10:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 036acb9c-47f3-33ea-85aa-5d122c6863ba | -4.56209 | -45.80889 | 2024-10-22 05:10:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fc04121e-3535-3a86-888f-157e80f8de01 | -4.56153 | -45.80539 | 2024-10-22 05:10:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ec4b8c92-b091-3398-8eb2-59dc711f5d9e | -4.56087 | -45.80996 | 2024-10-22 05:10:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 02516dfc-7e55-351d-a9b9-eb063fb0e5e8 | -4.5566 | -45.80377 | 2024-10-22 05:10:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 503f0c1b-e4b4-34f7-8a02-61f51634c252 | -4.55597 | -45.80831 | 2024-10-22 05:10:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c0ac6ef4-533b-3063-a2f0-7f09bb879aba | -4.5554 | -45.80489 | 2024-10-22 05:10:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9a33873e-c199-3939-a5bf-95f998143ef0 | -4.01715 | -46.02336 | 2024-10-22 05:10:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4df26f2-cd54-357b-a34a-9d6d0ee399fe | -4.01646 | -46.02821 | 2024-10-22 05:10:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 612e2c60-fee6-3347-9dc8-2690015d8116 | -4.01581 | -46.03275 | 2024-10-22 05:10:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e429dc3c-ce72-38f3-b33c-5495f96911d0 | -4.01182 | -46.01812 | 2024-10-22 05:10:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| aa89037d-cf66-324f-9aa0-f97244e43e57 | -4.01114 | -46.0229 | 2024-10-22 05:10:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 631cfd53-5839-350e-81a0-317f72a3ea7c | -4.01043 | -46.0279 | 2024-10-22 05:10:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1110402e-9973-33c6-bd4b-90d688a80b21 | -4.00982 | -46.03222 | 2024-10-22 05:10:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bca357ad-5664-3ef1-aca8-e197f098aa4b | -4.00571 | -46.01833 | 2024-10-22 05:10:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 73c7722d-2d3d-3591-a67c-e99d2d0851b9 | -4.00507 | -46.02292 | 2024-10-22 05:10:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8b974b58-1c64-31f6-bb78-f64da7ee407e | -4.00446 | -46.02719 | 2024-10-22 05:10:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f044780f-6342-35d8-ba67-9d6045f02419 | -4.00231 | -46.01735 | 2024-10-22 05:10:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a611db72-7db6-317b-b322-8e232ba21dc5 | -4.00164 | -46.02182 | 2024-10-22 05:10:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f70a06d0-4ff6-3f4a-bb27-d725fa46ca69 | -4.00102 | -46.02602 | 2024-10-22 05:10:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fbf1531-b7a3-3f1c-8900-ce466253bbaa | -3.73157 | -45.34499 | 2024-10-22 05:10:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b29de27a-a61b-31e5-8b1b-cd20560091da | -3.73086 | -45.34987 | 2024-10-22 05:10:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 16352bc9-431a-3cb9-be25-8288f2d2141b | -5.65904 | -45.93922 | 2024-10-22 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a7e49a0-1ef0-3d92-92cc-034ca43b8031 | -1.11332 | -46.83135 | 2024-10-22 05:10:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 629b0ca1-b4e3-3c13-9002-1392dce555f9 | -2.56155 | -45.99181 | 2024-10-22 05:10:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7778a977-798f-3777-9d18-089dfce9423a | -2.56092 | -45.99602 | 2024-10-22 05:10:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a63763ef-6ba5-346f-975b-d6672c8e810f | -6.63949 | -47.34315 | 2024-10-22 05:10:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9f40245-b015-3827-b02d-dd5ef02372b3 | -1.97791 | -48.68679 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1e1d0d1e-b21d-3d08-8caf-aebd48b4de80 | -1.97709 | -48.69205 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8acba11d-892a-3bcb-ba5b-bf671b648bcd | -1.97699 | -48.68762 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f3bd32ea-fbae-3600-9592-de8f69d82877 | -2.96403 | -48.00436 | 2024-10-22 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9033c760-01d1-384a-ab1c-bbb97c8768e7 | -2.96358 | -48.00743 | 2024-10-22 05:10:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a75583c-d9ae-38f5-ba1e-e3d90cff2792 | -2.9221 | -48.95798 | 2024-10-22 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9ea4415c-f7c2-37fc-b5c2-fc6f6cc4d5d1 | -2.78969 | -48.08157 | 2024-10-22 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a6595c3-278f-35cf-9922-5ccb63bd35cf | -2.7846 | -48.08076 | 2024-10-22 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70445062-dc93-3e9f-8461-984bcf86c7ab | -2.74304 | -48.68792 | 2024-10-22 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e08060d5-bdf2-3947-b8eb-79e1b8731166 | -2.74109 | -48.68808 | 2024-10-22 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05beaae6-fbf0-31db-91c4-eff9ab89a105 | -2.42272 | -48.63464 | 2024-10-22 05:10:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fe2590d8-1482-3293-a649-a86eeef72563 | -2.4207 | -48.63501 | 2024-10-22 05:10:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4b301216-02ee-309a-896f-5b9f208d10e8 | -4.24029 | -48.1319 | 2024-10-22 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e0b127f2-76af-315e-a6dd-bfbc6671c92c | -4.23984 | -48.13503 | 2024-10-22 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dccf9ba2-d415-3e7a-b341-068bbff6f0f2 | -3.80516 | -47.79904 | 2024-10-22 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| de74ce76-dd59-30a7-9578-d88dad4cf570 | -3.80468 | -47.80225 | 2024-10-22 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 131be7b2-b39b-36e2-b8c5-29c8004db6a5 | -2.87268 | -49.45498 | 2024-10-22 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03bb8dd8-caeb-3e1c-aafc-daee93c572b0 | -2.87196 | -49.45981 | 2024-10-22 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f3022c39-a3fd-38b2-848e-7f872185c8ea | -2.78365 | -49.29522 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cd4d7d4f-50dc-394e-bc2f-ef10ec9427cd | -2.77824 | -49.29942 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e6060c84-f42d-30e7-9c6b-2acc7640bb7e | -2.77751 | -49.30433 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 22cbb93f-a544-3935-8a2f-8f060ee4230b | -2.77356 | -49.29868 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 42f3ccf0-eac6-335d-800f-75d9eb2fe07f | -2.77283 | -49.30359 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c9e60b6a-9f80-3ea5-b58e-3309dd35a23b | -2.77211 | -49.3085 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf6a9b2d-b452-39ed-8028-ceeb2b053fad | -2.77138 | -49.31343 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 31068179-e1d0-3d3b-aaf3-dee28020b6ca | -2.77066 | -49.31829 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 4a946a3e-5383-3dba-9d15-58df9189fc06 | -2.76993 | -49.3232 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 64375c3c-824c-3b62-bcff-e126b1d096f9 | -2.76921 | -49.32808 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7a039200-5625-37e1-9fc2-9ce3b95e4edf | -2.76848 | -49.33299 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| deb63035-4cf3-3527-8761-7afd3418dc87 | -2.76816 | -49.30287 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cd0a0931-9208-3b6c-8d9e-cf558de649d2 | -2.76743 | -49.3078 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e5998090-0641-3532-8c4f-9547edc3c330 | -2.7667 | -49.31272 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 96a91e9d-8ef6-30ee-ab20-88f1f95948c0 | -2.76598 | -49.31763 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| bc0623be-c75a-37d9-970c-23d33e7a4162 | -2.76525 | -49.32252 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 980955a0-8220-3945-b4f0-5bd9462ce88b | -2.76486 | -49.35744 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f7376863-946c-30ed-960b-651a7ca5d1c5 | -2.76454 | -49.32737 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a436fa71-f42d-37dd-a1e0-bcc2f84bed8a | -2.7642 | -49.29725 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3b09a1d-7366-35fa-a57c-744823a3e5a1 | -2.76415 | -49.36226 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6c037391-14fb-388c-84bb-7c05d2bfa8af | -2.76381 | -49.33227 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8becdb7e-c734-39d9-9226-52f418ef3ec2 | -2.76347 | -49.30217 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 012d2ad1-832f-30fe-a91f-275163abe3e5 | -2.76275 | -49.3071 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| a99db093-4254-3e3c-b341-c5a376869384 | -2.76202 | -49.31202 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 95818c4e-ef6d-31fb-b5de-108c82461a8f | -2.7613 | -49.31694 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 939eae24-4a34-3fe3-9136-98b6963002c5 | -2.76058 | -49.32182 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 9cbfe040-867b-33a3-b006-012dda0b1fcc | -2.76057 | -49.30428 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1b847ce7-cce3-3543-83c5-99773b739c01 | -2.7602 | -49.35673 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fb1e21e9-d4de-31ed-ae16-7d2c8ced7334 | -2.75986 | -49.32669 | 2024-10-22 05:10:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README27.md)
