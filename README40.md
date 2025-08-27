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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0702f9b-c093-36b2-9c47-d28fc73705d6 | -6.88237 | -44.40615 | 2025-08-27 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4d9c8e9-9443-38ad-a0eb-367f708a9c73 | -9.19951 | -46.73753 | 2025-08-27 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66858434-c1f8-31ac-97fd-0c25e3688937 | -9.08255 | -49.58071 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 17c3cd9d-0753-3890-84a3-e0032a803441 | -7.475 | -45.03793 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 559f1966-1c98-3800-846d-1451f2869a10 | -5.36304 | -46.32005 | 2025-08-27 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d531cc24-4f0b-347b-b585-2691d5f97c22 | -11.25263 | -44.97973 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65511012-5611-34ec-ba06-ca3576bd5b2d | -9.18719 | -59.46006 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cfd38637-6182-31fa-8a4c-50c6ccb6b9cc | -7.74342 | -50.28036 | 2025-08-27 04:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d4c955ed-1796-3249-ba11-055de80e8173 | -7.73754 | -50.29308 | 2025-08-27 04:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 93590d24-932b-3413-99ec-8e0e315db616 | -11.10557 | -44.7529 | 2025-08-27 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d91af178-3a55-3720-a807-9cb29b1b3218 | -7.17106 | -44.46367 | 2025-08-27 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20bb4872-7292-3026-9e4e-30e1f3ce8413 | -5.83513 | -43.21306 | 2025-08-27 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46000087-60d6-3f78-9047-5422c2a989f9 | -6.61767 | -53.33737 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9ddf880-0c4d-3c85-b3ad-c7aa3fb234f1 | -11.14819 | -44.78286 | 2025-08-27 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70d2c6cd-f1c4-3b17-a481-0133e7a292c8 | -6.23878 | -60.0102 | 2025-08-27 04:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3510818f-1c5b-351c-81d2-ad876e1e6494 | -6.71628 | -43.10132 | 2025-08-27 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ae7e81b-8d6a-3214-a960-06efdacfab65 | -9.58894 | -55.38021 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 721846c9-b384-3525-abcb-32a26870d67b | -3.98136 | -51.05997 | 2025-08-27 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ac6636c-70bb-3008-8b80-ac19a4797f5d | -4.31257 | -48.09919 | 2025-08-27 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 2b84c9af-951e-3ea7-b420-de06bb4efeaf | -9.96926 | -46.37473 | 2025-08-27 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca7dcc4e-ec79-3e75-a782-fa7e04c7cd1b | -7.16763 | -44.46311 | 2025-08-27 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51045fa0-7d5c-3719-b109-9f7378849b9d | -6.89828 | -43.13426 | 2025-08-27 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cb6ae89a-627e-387b-aa45-a8b88720a56b | -10.82153 | -46.3709 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7601eff6-ffbd-3b86-b39e-ed815cdc7338 | -10.31802 | -46.79428 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0137b57e-b521-3fb7-a35d-c46125a26261 | -7.48065 | -46.00503 | 2025-08-27 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b990d09c-452f-3497-95e4-5d558c9eff72 | -10.31306 | -46.80427 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eba7db7d-1bff-34ed-bf69-8f58053df8a0 | -5.76032 | -53.76798 | 2025-08-27 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a8ec519-908e-35c4-8d28-5e626df3b8c4 | -11.26251 | -44.96137 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02c80025-3684-3955-bf5e-bfe12e8a41af | -7.59301 | -45.22273 | 2025-08-27 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49c3902c-a04b-38b4-b572-f734b7afd7d1 | -6.24038 | -60.0268 | 2025-08-27 04:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5bdfd8de-06df-37f6-8bfe-712ea2ddd891 | -9.5359 | -46.12564 | 2025-08-27 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 31f96843-cb1a-3cac-8a51-b07e35bd8c59 | -10.76872 | -47.01677 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e86c580-5fe4-3d8a-8bc1-652702db511f | -8.54606 | -51.38824 | 2025-08-27 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3ab8720-3d78-332a-bde9-277dc3816ac2 | -9.56888 | -55.37845 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ecaa46b-fbca-33ac-b5a9-a580ac9315a7 | -6.52186 | -42.9795 | 2025-08-27 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eef7052d-86fa-3cbf-9cc4-aa1b53096350 | -6.23603 | -60.01144 | 2025-08-27 04:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d637ec5-0b67-3777-94e5-97e4418138c7 | -7.2903 | -46.99883 | 2025-08-27 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9195ec89-e619-33b0-95ad-9ab7824318a9 | -9.5828 | -55.3872 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4026255-cf1c-3132-b5b9-66ffd1c7a932 | -9.10717 | -49.58477 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 43e7110d-006b-37a9-8be4-5aaf24d06b6c | -6.70396 | -58.5675 | 2025-08-27 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0914afcb-eb5b-3b78-ae7d-0bb5f1ef7ddf | -5.52939 | -51.99747 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f15944a-3197-311e-b2d4-bb2594802bfa | -6.76234 | -59.6761 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2b53620d-701c-3d01-b150-b1c7b61a4cc3 | -7.70078 | -45.77097 | 2025-08-27 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 36df935d-4b9f-3794-be36-723a3411193c | -11.15171 | -44.78342 | 2025-08-27 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3010cbdf-270e-33f3-90d2-5dc5e851deb2 | -9.95007 | -46.49815 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75c04e95-1c01-3eb2-9db3-900a484e66e1 | -9.13256 | -45.23684 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb2f2414-f58b-3ed6-8ef9-80ef6ad07695 | -7.66245 | -42.65909 | 2025-08-27 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e25d7f3f-0a62-3e4b-8228-25837426433d | -9.42298 | -48.25716 | 2025-08-27 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7da6259f-bbdc-3d6a-b2dd-c82e82bb37ed | -6.90856 | -59.36154 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| faae33aa-9762-3de3-a0e1-b9ebd0c863a9 | -11.25321 | -44.97585 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c70234b5-c44a-3651-bc63-8a8f0e5d9d3e | -6.81155 | -58.96097 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a8c6c32d-1fc6-3990-aaed-c548a11f3841 | -10.85952 | -47.32525 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ecd1d950-31cd-3730-afaa-b63ab6e4fc6d | -6.13086 | -42.94721 | 2025-08-27 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 64386418-f408-34bf-89b2-1b65b234ffcc | -10.31631 | -46.76173 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aef98700-7101-3085-b937-c6ca9e43922b | -6.41549 | -44.68824 | 2025-08-27 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80226874-f5ac-30b5-bec5-c32fa63b1183 | -5.11254 | -43.20512 | 2025-08-27 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e41b3d61-a648-3a32-9d0a-379e53dcec86 | -9.58937 | -55.37928 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b1f50729-d500-35e6-922b-380e3b6ecb32 | -6.41493 | -44.69192 | 2025-08-27 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 434f1830-797a-328d-ba14-06ed708c7ae0 | -8.13336 | -55.36986 | 2025-08-27 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01296ebf-16eb-3f92-86fa-c66c31c3a760 | -8.46377 | -43.67965 | 2025-08-27 04:25:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1c75f35-4b34-3ed7-9cf7-defcce81b6a2 | -6.78446 | -59.637 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e76253ea-4b8f-3f91-a02d-215e6f47910f | -9.17525 | -60.86163 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fff7c13-0d6e-3140-9cb7-339845c97cbc | -10.31911 | -46.7873 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ed870ed-976f-3e56-8ec2-13dff0444775 | -4.11496 | -56.34286 | 2025-08-27 04:25:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 533cbe59-f80f-3d3c-b829-1e884a74ae79 | -5.82441 | -43.21132 | 2025-08-27 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 110358a4-ccaa-3663-9d7f-63ac5d169095 | -4.48046 | -47.66703 | 2025-08-27 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7c36d53-c79c-3189-80bc-1a147da6316d | -7.16976 | -45.1508 | 2025-08-27 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cff2d7b3-fc7b-3476-abeb-fde015fa4cdc | -5.46974 | -47.46723 | 2025-08-27 04:25:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73a90a41-c308-3b21-beb5-1142959fb1ea | -7.8799 | -45.90634 | 2025-08-27 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2b0ab9f-ce6f-346f-9612-78846a764e49 | -8.45845 | -43.66605 | 2025-08-27 04:25:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c392c397-9a66-3f22-86f2-75bc8aa66880 | -6.2859 | -43.78344 | 2025-08-27 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7abc3d86-5f73-3a6e-9b6c-7e95b6770c71 | -6.84438 | -58.96701 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 81bf62e2-1ad9-3675-be4a-8f1b61af9342 | -10.78526 | -47.0625 | 2025-08-27 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d524ed19-2b95-3e03-9bde-e84240876df0 | -5.63411 | -45.7189 | 2025-08-27 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd21dfb4-a4d8-3fa6-8912-502727aad2fd | -6.32005 | -42.88177 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66bedf91-7bc7-3674-b485-636e2aaaa93d | -9.20006 | -46.73405 | 2025-08-27 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8dc2c2a-4b17-3958-a880-4df59b15f3f4 | -6.82363 | -58.96906 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f9474347-0267-3d92-821c-069fefffdb47 | -8.07168 | -44.98639 | 2025-08-27 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7bc3890d-18ce-3c5c-8ab5-ad51b3567e79 | -8.90231 | -60.7692 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b7764138-dce6-3e91-9ac5-3a1640c9b305 | -10.78596 | -46.37995 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 40cafc76-cfa6-3404-be6d-041c64ca27c9 | -9.58438 | -55.37835 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9be7c8d3-2859-3948-b16e-90a92e9e2f00 | -10.12246 | -47.43238 | 2025-08-27 04:25:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7852699e-22b1-375d-9d41-5ba10a78f932 | -9.95507 | -46.50973 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d92c2c45-ac2f-3b4b-83bb-4a8636166c75 | -3.91962 | -47.68966 | 2025-08-27 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07e8d681-5cbd-3b93-8a33-d7fddac5eec1 | -3.97726 | -51.0593 | 2025-08-27 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 679a0856-f425-352c-8095-2a02fb3d1bfb | -10.32075 | -46.77679 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5df34ed7-d1b9-3189-8d20-4773abe07c0d | -6.96165 | -44.09535 | 2025-08-27 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7cad1bdd-fd1c-35dc-9dd9-1773bf84f7c2 | -9.58395 | -55.37926 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6a65a54b-3315-3b4a-80c0-12f4c30c120b | -6.23748 | -60.01722 | 2025-08-27 04:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c0e291ac-7a7b-360c-8902-64b3a9a42fa1 | -6.64799 | -53.18967 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50e2ded6-10a3-3fa7-8f2c-3c1fc80afaab | -7.16974 | -59.74604 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dc561751-e806-361c-9e52-77586c5b1043 | -5.76121 | -53.76287 | 2025-08-27 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16ebe258-0a96-3838-a74e-9836f5915f2c | -10.31856 | -46.79079 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c851c3ca-7676-3e05-a2d3-d05af54dc3db | -5.39845 | -45.12111 | 2025-08-27 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4976e61b-fa57-3e77-b2f5-8fe0266995fc | -4.96238 | -55.81505 | 2025-08-27 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a9fd4a4-ad76-3ecb-80a2-3d20b10cc1c4 | -7.12138 | -43.68811 | 2025-08-27 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f40dfc1a-d779-3d11-a954-3ced5f1ade6e | -7.65491 | -42.65799 | 2025-08-27 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bdc2a599-0387-392a-8c11-92c39d35a2f0 | -7.25908 | -45.35471 | 2025-08-27 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7afda7db-34b5-3b57-a712-61ac4c4ec086 | -6.5741 | -47.38023 | 2025-08-27 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 83226213-6ae9-382a-8abd-228f5631a16e | -6.78324 | -44.2989 | 2025-08-27 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README41.md)
