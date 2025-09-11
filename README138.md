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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0786839-6cab-33e6-b8a0-454a73d3bce9 | -8.5089 | -45.6807 | 2025-09-11 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| c3144e09-2f89-3a28-9133-8d0f9ee34246 | -8.5278 | -45.6787 | 2025-09-11 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 4393c3b5-2924-3ebe-9e09-88ad99d11025 | -9.1331 | -46.9831 | 2025-09-11 12:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 43ac8e07-7323-39e7-bc3d-f05cd40430a9 | -13.2602 | -51.7548 | 2025-09-11 12:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 82cb4f59-02c7-3c14-9655-28ee9233db71 | -12.0665 | -47.5644 | 2025-09-11 12:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| abca9c20-0a87-3f93-b329-3764d3478fd4 | -15.6737 | -47.016 | 2025-09-11 12:30:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 175.9 |
| d7ad7281-ea77-3df3-bb9d-fd5e62517786 | -7.4161 | -45.8536 | 2025-09-11 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 2d7233fd-23e3-39b1-863a-d74a0db8664c | -14.1492 | -45.4009 | 2025-09-11 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 4a73a2c5-a07f-3284-8915-43fb119a098b | -15.1759 | -52.4199 | 2025-09-11 12:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 194332d0-1976-3457-860d-9e81b96f5531 | -8.8753 | -49.5828 | 2025-09-11 12:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| c7ce0395-7178-31de-938f-6cc3d443c3de | -6.2228 | -43.3226 | 2025-09-11 12:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 6f72ed78-7a3b-31cb-a021-ab2871ca20e2 | -10.1844 | -46.1927 | 2025-09-11 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 5602baa5-acba-32b1-9228-ab2a8afab3f2 | -11.7211 | -46.5127 | 2025-09-11 12:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 89b3f18b-95fa-3f57-a20b-34b51ca883b5 | -22.6809 | -53.1309 | 2025-09-11 12:30:00 | GOES-19 | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 147.4 |
| 9b525d11-a3b5-3378-bcc6-6528544a5a14 | -8.7411 | -45.2248 | 2025-09-11 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 439a834d-f87a-3744-a3c8-37363e87a748 | -11.4285 | -43.5544 | 2025-09-11 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 010bd331-a4e1-35bd-8723-4c3c68cc0a5f | -8.7547 | -47.1107 | 2025-09-11 12:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| e90ca2cb-0c93-3cd3-a3a1-90af5c7aae72 | -15.1561 | -52.4439 | 2025-09-11 12:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 60c7070a-bd3e-3306-90ad-74358e0e0bf4 | -15.8014 | -52.2258 | 2025-09-11 12:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 015a75ff-235d-3175-88d6-40e0d1afb4a3 | -11.779 | -46.4821 | 2025-09-11 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 14b579d7-eb4a-3a6c-bbda-bb5aba59567d | -9.0579 | -46.9688 | 2025-09-11 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| bae43d91-1308-375c-90c9-7233b61a8644 | -8.5086 | -45.7033 | 2025-09-11 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| e2d87c9b-bea6-31d4-9e76-bf3ca6bd0bee | -6.2226 | -43.3459 | 2025-09-11 12:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 20f1c6f9-f083-3057-a6c9-9859fe489372 | -12.6632 | -45.3008 | 2025-09-11 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| d32487b4-e336-3ee5-80c8-157e12cc3cbd | -12.6829 | -45.2746 | 2025-09-11 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 522258ae-d3da-3a9d-9e26-342273ce8780 | -11.4285 | -43.5544 | 2025-09-11 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 174.3 |
| 34955434-2b49-3875-b784-3223a46b0912 | -11.3584 | -46.5167 | 2025-09-11 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 226.0 |
| 073cf1a1-50ae-3303-bad3-aec922dd06e3 | -11.7115 | -48.2536 | 2025-09-11 12:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 672f9ac3-e781-3fe9-b7a5-ba8704cd7c5e | -9.0753 | -47.078 | 2025-09-11 12:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| a72026f9-9cf7-3391-8442-5414c1ecafa9 | -9.1331 | -46.9831 | 2025-09-11 12:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| d1d82b65-dc73-318b-aacb-731e0eec6d56 | -8.1649 | -46.0983 | 2025-09-11 12:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 534e9cd2-b6c4-3a22-9555-c650692b466e | -11.4093 | -43.5573 | 2025-09-11 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 169.3 |
| 49350602-6ef8-3ba9-8621-293ffb1d2974 | -8.8753 | -49.5828 | 2025-09-11 12:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 7e9f6086-a65a-3dc3-9a7f-78d4905112ed | -6.4364 | -44.4847 | 2025-09-11 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 3474d631-6e37-30dc-b8e4-3c8fcc8e1619 | -11.4097 | -43.5336 | 2025-09-11 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| f4dbd2bb-7b37-3832-a5c2-60d02241220f | -11.3931 | -45.581 | 2025-09-11 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 09ef9c62-fe0b-35e6-9362-172950377430 | -15.6737 | -47.016 | 2025-09-11 12:40:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 5910e24b-7f92-36dd-ae9d-075ae733c938 | -15.1211 | -50.1438 | 2025-09-11 12:40:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 96.7 |
| ceb44e3c-ff4e-3f43-989c-20a1f0527eaf | -9.0361 | -45.7603 | 2025-09-11 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| ef6f6cb1-3756-31b8-83af-8200fcd6704b | -15.8014 | -52.2258 | 2025-09-11 12:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| d1e2ade0-6d17-3748-963e-b9f2a64bfc56 | -9.0579 | -46.9688 | 2025-09-11 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 123de0e2-8500-31e0-b894-85de800bf152 | -7.4161 | -45.8536 | 2025-09-11 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 40692300-fa65-3fbf-b916-f71f1308a244 | -10.5671 | -47.2442 | 2025-09-11 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 39ecef25-c907-37f9-a3ef-a1a688756827 | -9.0939 | -47.0983 | 2025-09-11 12:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 191.2 |
| 44b37fe2-74b2-3322-a466-cedd7b116cba | -13.2602 | -51.7548 | 2025-09-11 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 158.3 |
| 698b7af6-9742-3229-bff3-60531e63599c | -6.2226 | -43.3459 | 2025-09-11 12:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 379a1da0-eaf2-3984-b083-c1332608ad73 | -9.7445 | -47.8468 | 2025-09-11 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| a2c45ca1-0a5f-33e1-8d63-c469e08e3fdb | -8.5275 | -45.7014 | 2025-09-11 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| bff86193-e504-3658-87a4-d5883ecfddfc | -8.7547 | -47.1107 | 2025-09-11 12:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| d6f483f1-3c51-3c9f-9693-5d0909382f3c | -9.0567 | -47.0577 | 2025-09-11 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 38e97988-2155-31e3-88a1-8795b1f173f4 | -12.6829 | -45.2746 | 2025-09-11 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 086b6e0a-c380-34b1-88a0-7d5e18adbfc5 | -14.5128 | -53.9158 | 2025-09-11 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 23c4ff73-156a-328e-96e8-60168826caf4 | -9.0262 | -49.5261 | 2025-09-11 12:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| e93fd162-ba22-3473-895c-e8e600597942 | -15.8006 | -52.2687 | 2025-09-11 12:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 7ea5a021-fbf8-39ed-962b-f20d1920c2ab | -11.3397 | -46.4967 | 2025-09-11 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| e4e27be5-7252-34fd-bb0e-9eb2bd285e24 | -12.6825 | -45.2977 | 2025-09-11 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 85d7e76d-c8d0-31a5-a686-b10ba317d848 | -12.6632 | -45.3008 | 2025-09-11 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 507bec7e-5240-3d68-9440-6970c11b6712 | -9.0265 | -49.5046 | 2025-09-11 12:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 19a9aa09-84c0-30aa-ab87-ff12bd33da2b | -11.7215 | -46.49 | 2025-09-11 12:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| c96e2956-c14b-3405-a181-03ec09929c29 | -15.1016 | -50.1468 | 2025-09-11 12:40:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 183.3 |
| a010e902-4165-37e6-bf0d-5e4b3a81b499 | -14.1492 | -45.4009 | 2025-09-11 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 969e9ccc-4cfb-303c-9df4-6fff2bf65425 | -22.6809 | -53.1309 | 2025-09-11 12:40:00 | GOES-19 | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 104.2 |
| 2c7f9734-dc1f-33e2-8ad0-edfe6ad66117 | -11.7112 | -48.2757 | 2025-09-11 12:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 3f190baa-b9bf-3626-9961-129c276e0cb0 | -15.6732 | -47.0389 | 2025-09-11 12:40:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 361.0 |
| 12396ae0-c3dc-357e-9216-b0448ba495ce | -9.0074 | -49.5278 | 2025-09-11 12:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| c087d6f4-6cac-34c8-b091-16e8f077052b | -8.8755 | -49.5613 | 2025-09-11 12:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 205.6 |
| 719c21d6-d8fb-358f-b1e0-b318f5f4b146 | -11.779 | -46.4821 | 2025-09-11 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| b9ab4dcd-0cc3-3760-b8d5-6355185bc990 | -11.9898 | -47.5748 | 2025-09-11 12:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 9b5279ba-538d-3719-a1d5-724b326a9281 | -11.7786 | -46.5047 | 2025-09-11 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 43f72877-1068-3020-86d3-f7eb93c70783 | -11.3588 | -46.4941 | 2025-09-11 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 695257c2-419a-3e69-922a-e6099cb7d7fe | -6.2228 | -43.3226 | 2025-09-11 12:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| d84c6585-41a8-31f6-9082-ef877d336ddd | -9.0364 | -45.7377 | 2025-09-11 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| fab7e672-d8cb-306e-a0e7-907f77b10e0e | -9.0942 | -47.076 | 2025-09-11 12:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 048125e2-b633-397e-95ec-5553b7736582 | -8.7411 | -45.2248 | 2025-09-11 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 343280dc-e78c-3016-8616-4c95e30f1b2b | -11.3393 | -46.5193 | 2025-09-11 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.0 |
| cf098d70-8923-3bbc-85c7-8bd189ea49c4 | -11.4281 | -43.578 | 2025-09-11 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 2d7f4036-9820-374d-b4ff-846c957d34da | -9.075 | -47.1002 | 2025-09-11 12:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 78bf4588-f3fe-3f26-879e-6bd3d335c88c | -9.0358 | -45.783 | 2025-09-11 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 4336a220-0c48-34e4-8ff1-7d7d62bd3079 | -11.7211 | -46.5127 | 2025-09-11 12:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 466.7 |
| 8970d026-8154-3760-8902-e66066364ea4 | -12.6829 | -45.2746 | 2025-09-11 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 22c899c5-72e6-3c06-9235-5a15fdf0824b | -15.1211 | -50.1438 | 2025-09-11 12:50:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 95.6 |
| d4994cbb-393c-35eb-b054-3df8b27d9994 | -9.0579 | -46.9688 | 2025-09-11 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 938d1f83-1fab-3015-ab3b-a31491a59b62 | -9.0265 | -49.5046 | 2025-09-11 12:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| b094c5ee-a9fc-3618-927b-b5fb80f061f2 | -11.4285 | -43.5544 | 2025-09-11 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 157.6 |
| ba898146-0367-3f9c-b6ab-e687b32ccf7e | -22.6601 | -53.135 | 2025-09-11 12:50:00 | GOES-19 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 90.0 |
| 0834d26a-713f-3211-8b36-94ce089dff5f | -6.2228 | -43.3226 | 2025-09-11 12:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 48666b0c-9411-392f-b36c-1e5bd5cc50d1 | -15.1176 | -52.4279 | 2025-09-11 12:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 217.8 |
| 46882934-b568-3147-a599-4658b979519d | -9.0753 | -47.078 | 2025-09-11 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 5d7ccd6e-c1ef-3d1e-a8f7-c0f43495be55 | -9.0262 | -49.5261 | 2025-09-11 12:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 085d3cc9-4893-376e-8ebe-670a6626eff1 | -9.0361 | -45.7603 | 2025-09-11 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 5ae4a7d8-2eb5-3bf3-884a-e780b3668120 | -15.6732 | -47.0389 | 2025-09-11 12:50:00 | GOES-19 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 211.8 |
| a2819516-a2af-3587-adb5-379c50a02346 | -11.7786 | -46.5047 | 2025-09-11 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 86ec682f-a639-330a-8e6e-b9ab4e1d4d91 | -6.8525 | -47.8707 | 2025-09-11 12:50:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| cbd02ac7-7d8a-3ea5-a8fc-07b0d57debde | -15.1759 | -52.4199 | 2025-09-11 12:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 2bd9793c-dcc0-3f20-a292-c11c43b8411d | -9.0358 | -45.783 | 2025-09-11 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| c5cd595c-373d-3a82-8e0f-3dc69eae7fdb | -15.118 | -52.4066 | 2025-09-11 12:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 224.4 |
| 3ad004f5-e27e-38a8-9836-b6f1f2eaeeea | -7.4161 | -45.8536 | 2025-09-11 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| bc4fc06d-54c2-3e49-895a-d31354c3a391 | -8.1649 | -46.0983 | 2025-09-11 12:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 0cb05270-96d3-3ece-aaf4-bfd805ab7d54 | -13.2602 | -51.7548 | 2025-09-11 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 180.8 |
| aed35aeb-4d9e-3873-a288-8cca7e72b918 | -13.2599 | -51.7761 | 2025-09-11 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |


[Clique aqui para ver as próximas entradas](README139.md)
