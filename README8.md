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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f421073-f578-385d-b84d-dc8343e51ae1 | -14.47819 | -47.07248 | 2025-08-11 03:38:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f895fc30-b1e6-3d0d-963e-508772443c9b | -15.96136 | -43.01929 | 2025-08-11 03:38:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17dd331b-fd6b-3ebe-a10d-4f6c28ad6c4e | -9.64711 | -43.83137 | 2025-08-11 03:38:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| efe0354f-3839-3bc9-a547-019da96f1c20 | -10.35744 | -46.63655 | 2025-08-11 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c485f5df-3b07-3513-b189-e96872021bcc | -13.11444 | -46.88749 | 2025-08-11 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 536f0ef5-45a6-3912-bda3-079272ca631d | -13.11561 | -46.88497 | 2025-08-11 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 852aa569-3ae7-3e60-891c-c21a456e4432 | -13.80145 | -41.20176 | 2025-08-11 03:38:00 | NOAA-21 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c9513f87-cc49-38cb-a9c5-13d8cb2b1bd8 | -15.57829 | -43.41274 | 2025-08-11 03:38:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98f3292e-09cf-3e51-b4b4-c03e27784042 | -13.9698 | -42.5863 | 2025-08-11 03:38:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| c668f730-a5bc-387c-b064-53f4653c397f | -15.57597 | -42.68985 | 2025-08-11 03:38:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 62f6e759-36a8-3b92-8595-8c165867eb3f | -14.4825 | -47.07309 | 2025-08-11 03:38:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea4d340c-4ffb-3570-9148-fc18244b9935 | -12.04605 | -45.76581 | 2025-08-11 03:38:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bb1f4208-39d4-3d8a-9a7b-f2d74691158b | -10.36452 | -46.63377 | 2025-08-11 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| eae0206a-b1b6-359a-a21b-468d05bb3aa9 | -10.30529 | -48.11559 | 2025-08-11 03:38:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf39da27-35ea-3430-8f8e-86fd98315951 | -14.11328 | -45.39819 | 2025-08-11 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e622e73a-1b8a-377e-a9e5-a2a72e499536 | -13.10942 | -46.88427 | 2025-08-11 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bc1d9c5-7b6f-33bb-990d-37fe2701d618 | -9.62763 | -40.58707 | 2025-08-11 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 32c5d15a-53f9-3051-b4c5-0307be81c1d4 | -8.30348 | -44.98694 | 2025-08-11 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2c18107a-42b1-3903-b92a-68a1cf96d358 | -15.04747 | -42.46404 | 2025-08-11 03:38:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 193b21a8-d7b9-31f9-bcc4-0cb54f0ae9c2 | -7.87328 | -44.97216 | 2025-08-11 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 36a32525-d63b-36da-b4b5-ae832380cdc3 | -10.51151 | -42.40707 | 2025-08-11 03:38:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 77f910ee-a8b7-34d0-bbdf-4b6a15615434 | -14.11255 | -45.40182 | 2025-08-11 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34975ea2-6fdc-3a24-b764-17d7c5abac96 | -10.42304 | -46.24789 | 2025-08-11 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d9f8022-6bd5-3d59-a295-a5b138e339d0 | -12.04643 | -45.7645 | 2025-08-11 03:38:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a5865245-57b9-39be-a5c1-94162d79d695 | -9.64651 | -43.83461 | 2025-08-11 03:38:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c1f9e27c-ddc3-3b2b-8245-081fc02f2ad8 | -12.70693 | -46.36401 | 2025-08-11 03:38:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c547db46-51c6-3ee0-a3d9-7f43cb151380 | -12.70604 | -46.36834 | 2025-08-11 03:38:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| feba0947-05f0-3956-b216-360d3590cc27 | -14.48155 | -47.0777 | 2025-08-11 03:38:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d47f54c-467a-30c6-b54f-8e3bfa3a3f28 | -9.63121 | -40.59195 | 2025-08-11 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 21150fce-b8cc-37c7-89aa-cbb68dd0d8cc | -13.8008 | -41.20526 | 2025-08-11 03:38:00 | NOAA-21 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| af8ea60b-fca2-363a-b37b-6781ef4bbdb5 | -13.96869 | -42.58862 | 2025-08-11 03:38:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| f26348ca-2a7c-309d-b5db-e1c278d8af5c | -14.118 | -44.88559 | 2025-08-11 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a61d46d2-5970-3e11-83e5-d928b629aaf0 | -14.4772 | -47.07709 | 2025-08-11 03:38:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbb9c3d8-d532-33bb-b183-3d7e4317210c | -9.20876 | -44.53269 | 2025-08-11 03:38:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a80d6bbe-4286-337c-be40-6f9435cac823 | -9.21512 | -44.52974 | 2025-08-11 03:38:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| da033245-feaa-35ff-9118-aeb3f43d334e | -12.04686 | -45.76165 | 2025-08-11 03:38:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f523a216-2039-3065-bcc2-04323a06d74e | -15.57363 | -43.4118 | 2025-08-11 03:38:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc1277f9-3aab-310c-880d-9c2fa7aff976 | -12.70316 | -46.3672 | 2025-08-11 03:38:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b836dbc-1fa0-34db-b375-d13a2d28b6c7 | -10.36113 | -46.63337 | 2025-08-11 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 876241bc-4d22-330a-9ab6-bbf371b39758 | -15.57734 | -42.6919 | 2025-08-11 03:38:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b4e64687-d738-3730-99ad-254bc30cbdc7 | -9.21583 | -44.52596 | 2025-08-11 03:38:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a784fe25-a3f7-3f32-90d1-d6d6406221ae | -15.10383 | -46.53826 | 2025-08-11 03:38:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab354630-35ad-32f5-a79b-aa6c8467a8e6 | -11.44896 | -42.22499 | 2025-08-11 03:38:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| c745a589-f8bd-3017-ab11-40992abb7fc2 | -15.57289 | -42.69105 | 2025-08-11 03:38:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 65684000-772a-3a9d-acbd-c38f43d32ec0 | -14.47555 | -47.07644 | 2025-08-11 03:38:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03eceb6d-2377-3327-a35f-2900caacf8f5 | -10.36194 | -46.6292 | 2025-08-11 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| e85c7ac4-74b0-395b-b7c8-69d7f833a4d8 | -13.97048 | -42.57883 | 2025-08-11 03:38:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c538073f-d285-317c-85c3-c18f843b5927 | -8.30117 | -44.99097 | 2025-08-11 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 13898402-d3c3-339e-bff6-4b206f86b2ac | -10.3603 | -46.63763 | 2025-08-11 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 1134ec91-78b7-3f8d-bd85-f194a8dada31 | -9.62691 | -40.5912 | 2025-08-11 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9b514176-3f5a-3cca-a4e0-675faa46e3e3 | -12.70912 | -46.36824 | 2025-08-11 03:38:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0559b2a-6577-3f5a-bd32-f30e8ee98b2c | -10.35829 | -46.63232 | 2025-08-11 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6227fec6-49d7-3b50-bf11-51e7de9cee5b | -10.30648 | -48.10962 | 2025-08-11 03:38:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 499457dc-6be7-3e30-8e02-cd971fa9eb09 | -5.4825 | -44.374 | 2025-08-11 03:40:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 148.1 |
| f5531b82-a118-36cd-9291-b08aabaade6b | -15.4407 | -53.9258 | 2025-08-11 03:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 8de0662c-6389-386f-9c5b-80748d576086 | -5.5011 | -44.3956 | 2025-08-11 03:40:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 236.8 |
| 5f322fc4-4ee0-36a4-a802-a01f6e124c6d | -15.4216 | -53.9073 | 2025-08-11 03:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 271919b8-87ec-304a-9aa9-25c1d4d66eab | -7.0799 | -59.1964 | 2025-08-11 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 0ac9c235-32ad-32c1-bea9-ead4c67f16cc | -5.5013 | -44.3726 | 2025-08-11 03:40:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| ec55ab20-909c-3756-adf3-bb251d5c0a0c | -7.0797 | -59.2157 | 2025-08-11 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 25837238-0893-3408-937e-13dbf2a8b28b | -5.4824 | -44.3969 | 2025-08-11 03:40:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 353.9 |
| e66d6841-2143-3ced-8fc9-672ebb340720 | -15.4212 | -53.9283 | 2025-08-11 03:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 398d72d5-f900-3ca7-ba61-b253bc9bba29 | -7.0613 | -59.2165 | 2025-08-11 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| bd993e36-aca2-33d2-aedd-b998c818bdcc | -7.0614 | -59.1972 | 2025-08-11 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| cd58e160-6613-3416-aec8-c86cfa442420 | -5.4636 | -44.3982 | 2025-08-11 03:40:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| a10974ed-5263-3a1f-8827-cd3dbb0b705e | -18.32369 | -43.67801 | 2025-08-11 03:40:00 | NOAA-21 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 847d9831-3c98-3067-b0aa-bb92209f6a2a | -17.96382 | -44.28303 | 2025-08-11 03:40:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16dcf975-11d6-3ce7-b287-189c932b7e8f | -16.69279 | -47.63364 | 2025-08-11 03:40:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6ef3e23-bcde-3e09-848b-98b1f4c0f399 | -22.51062 | -46.79319 | 2025-08-11 03:40:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 12fbfeab-8d60-354a-a21a-9908e96d7bdd | -19.42076 | -43.36507 | 2025-08-11 03:40:00 | NOAA-21 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4c2c641c-780b-3d82-907a-1b10b8f95f86 | -16.3799 | -42.52882 | 2025-08-11 03:40:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5c777d1-fd05-3bf0-a751-14d73e14452c | -19.90267 | -43.88138 | 2025-08-11 03:40:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| ba2cb58d-6cdb-3b62-abdf-d518da57092b | -22.70283 | -47.35912 | 2025-08-11 03:40:00 | NOAA-21 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ccf0616-d51f-348b-9955-98cf53113bb7 | -16.20283 | -49.99199 | 2025-08-11 03:40:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 30c0580c-a8a4-34a5-8d4e-212ce7815748 | -20.44789 | -41.94644 | 2025-08-11 03:40:00 | NOAA-21 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 063e8b93-5c96-3c67-8f4f-543afb37b067 | -18.18167 | -46.99812 | 2025-08-11 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b85b7795-46f8-310a-927b-92c8af708216 | -16.04602 | -48.48553 | 2025-08-11 03:40:00 | NOAA-21 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0ba6c7a0-1e2e-3ed0-a221-3546265c8bfc | -21.47637 | -44.6912 | 2025-08-11 03:40:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b9b83d04-1258-3a86-800e-f93af9406d7d | -17.25424 | -44.87872 | 2025-08-11 03:40:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 772b7ecb-d793-3438-89dc-43b5e76c78e9 | -16.40858 | -42.5913 | 2025-08-11 03:40:00 | NOAA-21 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2d41b5d-afa5-39a8-9dd8-a76af68a9ee6 | -20.86399 | -46.63725 | 2025-08-11 03:40:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d261319e-d135-3ef5-a9cd-f418513c4f0e | -22.28865 | -46.59476 | 2025-08-11 03:40:00 | NOAA-21 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 1b8c338e-fa7c-3e53-b05b-0a3e74b7670f | -16.21122 | -49.98678 | 2025-08-11 03:40:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 100ab54e-0369-3c8d-9d45-1d31258f77c3 | -16.37854 | -42.53016 | 2025-08-11 03:40:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 369c60b2-24ae-335a-ab2f-703938500245 | -19.22044 | -46.8013 | 2025-08-11 03:40:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bc8c269b-c1a9-3fbc-a2af-df2a0fd38598 | -16.29674 | -47.69589 | 2025-08-11 03:40:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d37bca48-b600-3946-9106-fbf899e79acd | -17.85677 | -44.42279 | 2025-08-11 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8e3bce97-c907-3797-af4d-ef0477acdc52 | -15.39575 | -49.12907 | 2025-08-11 03:40:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 03721a44-193c-3421-aba1-9d785cf4a496 | -20.8632 | -46.64098 | 2025-08-11 03:40:00 | NOAA-21 | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 979ad4c6-0fc6-3577-8bd4-41ad044b804f | -19.16553 | -44.52922 | 2025-08-11 03:40:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 92ec3238-b90c-35e9-ad8d-52cf6d64e7e2 | -18.17411 | -47.00624 | 2025-08-11 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d22d20e-e428-39e3-a496-2aa2f28e465a | -16.39989 | -42.58951 | 2025-08-11 03:40:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15fc86e8-0dd6-3e45-ae13-331c92682457 | -18.6264 | -46.84632 | 2025-08-11 03:40:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a532d6f8-a735-3934-96f7-257d8ce73608 | -19.67456 | -44.88144 | 2025-08-11 03:40:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c66e3701-6daf-3935-9750-25fa79ee4cb1 | -15.54078 | -49.99109 | 2025-08-11 03:40:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5877851b-d4d9-3aa0-a65d-d6c501f793f3 | -20.25658 | -41.95273 | 2025-08-11 03:40:00 | NOAA-21 | REDUTO | MINAS GERAIS | Brasil | 3154150 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fd5cccd6-d92e-3774-be11-de7ff7db5a6b | -19.22165 | -46.80338 | 2025-08-11 03:40:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 11889f27-59e5-3871-9e7e-eb279ba2252b | -16.2044 | -49.98508 | 2025-08-11 03:40:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db46406f-307c-39ee-b471-837ff8075fdb | -18.16472 | -46.99553 | 2025-08-11 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6753a576-2b97-3697-b9a7-1d88169728cd | -19.76734 | -42.10126 | 2025-08-11 03:40:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README9.md)
