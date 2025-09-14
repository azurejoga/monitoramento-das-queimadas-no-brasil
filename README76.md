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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 479a1a71-9404-356b-aade-6d644a568fc1 | -11.8675 | -50.4718 | 2025-09-14 12:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 6d86deda-60b5-3d8e-a6a1-aa4f03f8c68f | -8.9176 | -46.1565 | 2025-09-14 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 9578541f-8efe-344b-8cdc-db8605cc58d6 | -14.3285 | -46.1088 | 2025-09-14 12:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 204.2 |
| 7d595143-6b2c-3a78-aa91-6dac7ab4590c | -10.75 | -46.4607 | 2025-09-14 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 22399950-7ce4-3d9e-8412-7ad7cd760fc3 | -8.9548 | -46.1975 | 2025-09-14 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 0a46a4bd-b811-35dc-9e66-ae86f810a936 | -12.8212 | -47.1445 | 2025-09-14 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 205.9 |
| b8f4bbf0-ea4f-3565-9347-8aeb2793c78f | -8.9551 | -46.175 | 2025-09-14 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 6f281b03-72b6-3121-b499-ebab169c752b | -14.309 | -46.1121 | 2025-09-14 12:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 041b2281-7af3-3de0-89a2-0349e26e9d56 | -12.6636 | -54.6782 | 2025-09-14 12:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| cc2188c5-7a7e-367b-8ecc-dc537898ec2b | -11.502 | -50.7699 | 2025-09-14 12:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 4be9fde3-b2bf-364f-aabb-b264e70978f7 | -8.9173 | -46.179 | 2025-09-14 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| bd241cec-7e12-3632-b136-8df3a8cbdb71 | -10.7687 | -46.4808 | 2025-09-14 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 8187a258-2081-39d2-b243-ecf4445a65a4 | -8.9079 | -45.457 | 2025-09-14 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 22ad6e06-7dd4-3e88-b5af-7e3606d05fd3 | -12.6826 | -54.6763 | 2025-09-14 12:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| c2ec417b-6b99-3e7a-8f87-19f78af44c0a | -15.7786 | -53.482 | 2025-09-14 12:10:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 76a6c91a-0374-3909-9f75-80489e8e21f4 | -14.3095 | -46.089 | 2025-09-14 12:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 200.1 |
| 45954ce8-52de-300c-9c69-675e231b21eb | -8.9362 | -46.177 | 2025-09-14 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 46f3b898-58be-3ea9-a6e8-ba8da38b0295 | -14.2102 | -46.1979 | 2025-09-14 12:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 92.2 |
| f6b35f1e-a145-3e9d-af99-04d08bb73581 | -11.3831 | -47.3429 | 2025-09-14 12:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 4022dbbd-1977-3f97-8b48-648edc5fb45b | -13.9473 | -44.8541 | 2025-09-14 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 8aaebd9a-b4ef-3b49-a372-eeaea03e0758 | -8.4334 | -47.2306 | 2025-09-14 12:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 240.6 |
| 3f119363-eeaa-3f2f-8bc2-0ff00977c038 | -12.7671 | -48.0236 | 2025-09-14 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| adef682d-7333-3f73-9056-d4bbf5fd8868 | -15.8451 | -47.2358 | 2025-09-14 12:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 0f078aa1-8bba-3f9a-9002-4def865e0723 | -13.9278 | -44.8576 | 2025-09-14 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| a40337c5-dfe9-3c9d-9604-9320ddb6b2f6 | -14.2107 | -46.1749 | 2025-09-14 12:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 158.5 |
| b7549a98-f5f7-3316-821b-dc35fd7c1f85 | -8.9979 | -45.7871 | 2025-09-14 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 1fffffda-92e5-353a-a5fd-f9096d793619 | -8.7683 | -46.0373 | 2025-09-14 12:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 16d6d46c-1892-30d4-ab38-621c385977f4 | -12.8019 | -47.1474 | 2025-09-14 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 2e2749b3-7431-37d5-a8c6-169c40b8aa4a | -12.9294 | -54.7333 | 2025-09-14 12:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 4de57f6b-aec8-310c-9e17-da730bce3a5c | -14.329 | -46.0857 | 2025-09-14 12:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 316.7 |
| cc321e54-95b3-3335-9175-47b18318a215 | -12.7871 | -47.9764 | 2025-09-14 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 15bfc3c3-2b85-3b88-9269-b6d11a32f3c8 | -8.9976 | -45.8098 | 2025-09-14 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 2912936f-cecf-3c71-a375-39e5f3a332f0 | -12.8208 | -47.1671 | 2025-09-14 12:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 152.1 |
| bed9f958-bd9c-3e51-9ff3-9073eec05279 | -4.49483 | -43.94992 | 2025-09-14 12:14:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fee327fe-e90b-30c9-9630-dab251d59112 | -3.59673 | -47.50481 | 2025-09-14 12:14:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| bce2a111-dd41-38df-965e-fc9663ba532b | -3.59391 | -47.52398 | 2025-09-14 12:14:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| da2b2a51-11cd-3a8a-92a5-a664fee54038 | -4.93401 | -43.72034 | 2025-09-14 12:14:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 756dccac-364a-3267-bbaa-0c413c437079 | -3.60453 | -47.51567 | 2025-09-14 12:14:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 694c0a52-c16b-3559-ad5c-598c0708048b | -3.59532 | -47.51439 | 2025-09-14 12:14:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 440bd527-d28b-3b69-bbda-4d299eaa3618 | -4.60218 | -43.32375 | 2025-09-14 12:14:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| ef94ad84-21f4-33e7-a332-39339b37d353 | -4.72485 | -43.55431 | 2025-09-14 12:14:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1b39e761-935e-3c92-8f18-70832e87bc23 | -3.79907 | -47.5754 | 2025-09-14 12:14:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2fbeb0db-47a9-3489-9ed4-c4a5ce5a0ea1 | -3.9795 | -42.51524 | 2025-09-14 12:14:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| c034ef12-4f02-3781-99ba-570f262d52d3 | -4.72628 | -43.54404 | 2025-09-14 12:14:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 5697f097-23da-3b20-a9e6-cd0dd95c2a33 | -4.75483 | -43.54798 | 2025-09-14 12:14:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 07f7903d-569a-3460-b435-3f9aab3581f4 | -3.98955 | -42.51662 | 2025-09-14 12:14:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 68c027d2-7fdd-3023-944a-f7e7ffe88305 | -5.44688 | -45.10284 | 2025-09-14 12:17:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7422ac71-6e6d-3d94-ba17-b0f5973651cb | -11.29225 | -50.7775 | 2025-09-14 12:17:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 2b24a631-b866-3f4d-ba64-7d016b94ff27 | -12.79791 | -47.14016 | 2025-09-14 12:17:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 32475be5-1e09-3fa9-9849-d262f1433598 | -11.50813 | -50.77572 | 2025-09-14 12:17:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 31.3 |
| ef289abf-e622-38ff-ae4e-4e8cad48df1f | -8.95986 | -46.19917 | 2025-09-14 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 80517149-9827-3bb9-b959-dcb9ebe99830 | -6.72989 | -45.28388 | 2025-09-14 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 52ecf229-25c9-361d-85e2-c38557a11784 | -12.77067 | -48.03613 | 2025-09-14 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| aac3298d-9ef4-3e5a-b5cf-84b38b48d620 | -8.77198 | -46.03157 | 2025-09-14 12:17:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 8b16cb7d-5e41-35c2-8a7f-0e56c7130d8b | -12.12194 | -44.83727 | 2025-09-14 12:17:00 | TERRA_M-T | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 7db1216c-7529-30fd-bb12-653896a45108 | -8.64561 | -44.02875 | 2025-09-14 12:17:00 | TERRA_M-T | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| eda3781c-4f54-35be-b6f3-a98843cd1ab0 | -8.79237 | -46.016 | 2025-09-14 12:17:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 92fb3e61-8a2f-34f2-9d5c-ff8a127e065b | -6.42857 | -42.60865 | 2025-09-14 12:17:00 | TERRA_M-T | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 4d3edbc6-c732-3f71-806d-9acdb9c3eb2d | -6.8076 | -38.19027 | 2025-09-14 12:17:00 | TERRA_M-T | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 35.2 |
| 8793eee5-9a67-37c2-a21b-ca846c76af4c | -8.99827 | -45.7972 | 2025-09-14 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| fdf5e70f-d5c2-3c97-b480-fbbe936aa7aa | -10.77718 | -45.98427 | 2025-09-14 12:17:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b6ee59e3-f274-379a-9e2e-ad6bc1afd95a | -8.35457 | -44.73445 | 2025-09-14 12:17:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8f4ec3bf-5edc-320b-ace9-5bbea46adf1a | -8.95224 | -46.18896 | 2025-09-14 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 29.4 |
| bfce6a7d-7ab2-3f81-9368-9edc631a8b78 | -10.14451 | -47.19255 | 2025-09-14 12:17:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 40daac74-8562-33ef-b9d7-1152da46ff7f | -12.57235 | -45.65396 | 2025-09-14 12:17:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 692dca5d-07ec-3cc4-99e8-fb2e30eb7622 | -11.49807 | -50.77415 | 2025-09-14 12:17:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 4c570eac-29e7-3594-b418-1e526db62825 | -12.44935 | -46.87025 | 2025-09-14 12:17:00 | TERRA_M-T | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ef0bac76-6fba-36f6-88af-a974b2f7e9af | -7.71115 | -44.86068 | 2025-09-14 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a79a2bad-6feb-32e4-85d6-477fe0325147 | -11.69921 | -46.899 | 2025-09-14 12:17:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| d3cefd28-26cb-3d6a-a7a4-2b62bb7c7ce9 | -8.9569 | -44.4414 | 2025-09-14 12:17:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 9729894a-b0d4-3884-b506-e869e4885f04 | -11.39586 | -47.34116 | 2025-09-14 12:17:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 545ff33e-9359-3108-bd04-c3f1a1f97d3c | -10.92971 | -47.18838 | 2025-09-14 12:17:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 294b1e01-7d60-32a7-9aec-1c670d7ef205 | -8.50171 | -44.72675 | 2025-09-14 12:17:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| f2d0e93d-e140-3c51-af12-f1bd69d01e94 | -8.96113 | -46.19023 | 2025-09-14 12:17:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 10b05b86-e8a0-3739-9ddd-475b5ff6c09f | -7.72012 | -49.67762 | 2025-09-14 12:17:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 52bfaffd-2930-37e9-b544-d6773bb625fb | -11.44723 | -43.92147 | 2025-09-14 12:17:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e7c883cb-f78a-3093-ba1d-e57e2983cefd | -6.99181 | -44.53479 | 2025-09-14 12:17:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| bf04ff85-6f1f-3bf5-a98c-d7c73c82cd7e | -6.47639 | -45.64165 | 2025-09-14 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0c62122b-40fc-3355-a9e0-3d4f9b9ee688 | -8.8094 | -47.12331 | 2025-09-14 12:17:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| fd05d192-2022-3776-96be-08c2eb4d9971 | -9.73672 | -46.88503 | 2025-09-14 12:17:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 34905121-c3ed-308a-8d46-70e6fd738c79 | -8.81696 | -47.13348 | 2025-09-14 12:17:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 6ecaa8fd-77b4-3704-b1c0-42414aa0231a | -7.72169 | -44.85243 | 2025-09-14 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6962a09b-90a1-3518-a0c9-f6799812c311 | -11.67253 | -46.49879 | 2025-09-14 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 864d91ca-0ac3-39a1-88b3-fca8d1df474c | -10.94098 | -47.23564 | 2025-09-14 12:17:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 02e83103-1eca-3552-9cd5-07ebb4be3af0 | -11.34173 | -50.85861 | 2025-09-14 12:17:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d29650cc-9b95-3ca0-a3ea-d2cef5b5f1cf | -11.78853 | -46.65243 | 2025-09-14 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 97894434-20ea-3bff-92ce-d78509f42f6a | -11.1387 | -47.65741 | 2025-09-14 12:17:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f0ee59a3-fb25-39d1-88a2-13c1a4935f1b | -8.41284 | -47.251 | 2025-09-14 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cbdc1d31-ff34-3d70-9a91-cd2c00d71149 | -10.76181 | -44.76735 | 2025-09-14 12:17:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 0dade434-6ec6-3ead-80f0-f3724c252094 | -11.2866 | -50.81316 | 2025-09-14 12:17:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 9d8bc7dc-c2c0-3b30-8df7-77c5401de2f1 | -7.37622 | -44.3499 | 2025-09-14 12:17:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 93a3e716-f175-3adf-a9cc-d2faaecec97c | -6.89214 | -45.63932 | 2025-09-14 12:17:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| fad2c3e4-db6f-31a5-9a99-ca7e44426a32 | -12.78903 | -47.13888 | 2025-09-14 12:17:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 5a47417d-096c-34a8-b939-db3e5139ae90 | -8.41414 | -47.24207 | 2025-09-14 12:17:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| ff98e5da-3dfe-3449-bef0-b6c7088d27c7 | -13.48129 | -41.46041 | 2025-09-14 12:17:00 | TERRA_M-T | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 79.2 |
| 202acefa-6e1c-3bbf-8cc1-11c923f6fb7e | -10.40093 | -50.58086 | 2025-09-14 12:17:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 437dee3d-6698-3796-a6b8-6d56021871e2 | -10.90443 | -45.46327 | 2025-09-14 12:17:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 1cc0d694-6313-3bbb-ae7f-4ecb9aedf459 | -9.35889 | -45.3905 | 2025-09-14 12:17:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 989c0472-86c7-34c9-bd2b-0ac6f47d6cee | -7.59742 | -46.70068 | 2025-09-14 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 8cf50d91-86e9-320c-9151-996d69743822 | -8.89038 | -45.44851 | 2025-09-14 12:17:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |


[Clique aqui para ver as próximas entradas](README77.md)
