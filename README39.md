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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93d25287-4b7e-34a1-be78-f3c728ef5e42 | -12.94185 | -46.3135 | 2025-08-24 04:34:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eab92c76-2c80-3956-80ed-9b4dca7b8e6a | -9.15404 | -59.46874 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 74e0f491-ab4a-319e-a5a8-a154eedc5986 | -5.74146 | -57.59325 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f681eae-2a20-3d98-ba3c-9d54dff1369c | -7.07995 | -44.62286 | 2025-08-24 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78ecba49-8636-3c3d-a745-901a05d520e3 | -11.90278 | -47.1136 | 2025-08-24 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97857f38-d3cf-3864-8b8e-c4deb7974e93 | -5.80726 | -59.222 | 2025-08-24 04:34:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e31b0a8-8ad4-359a-aa08-aba3754f954f | -8.91879 | -62.44289 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 19e0de1f-2dc0-3e5f-8f5f-dc21117a8bba | -13.46678 | -46.8852 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ddd1a802-7b21-35bc-9823-5cc0dd4a7ceb | -10.21499 | -47.56535 | 2025-08-24 04:34:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f323de0-1493-3982-ac38-ae29e264f927 | -6.46259 | -53.40326 | 2025-08-24 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0127a41-754e-3db5-bd24-814709c86b98 | -13.46524 | -47.0177 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 66a287cd-8bd7-3e98-aab0-8a78acd85705 | -9.16016 | -59.50112 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2b084343-5889-3ab5-967f-6bd57a0d8090 | -13.45767 | -47.02033 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 642fd284-7a2d-3628-bb76-dc1182ecbdc5 | -9.15053 | -59.45503 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 403e9657-a0fb-3a6d-9eaa-4f16b2b24548 | -9.15323 | -59.47305 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8df7e37e-ee13-3028-95d6-9b4eab78b85a | -13.4901 | -46.90032 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e5ecd9ec-2d1c-3e3b-9a95-7c8fa4a2396d | -11.54903 | -51.90407 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4784a00-0a22-3f01-af2c-659acb188a78 | -9.95701 | -60.18795 | 2025-08-24 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80a9f463-0e77-3243-9ea7-ca4c6b7e8a15 | -6.88844 | -45.67292 | 2025-08-24 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e33adac-8e18-38af-8424-4fff4abd095e | -9.95096 | -60.18674 | 2025-08-24 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83239604-d7d7-3a6e-ab4b-1da48769c68f | -8.74594 | -46.71727 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4105863d-ac34-331b-bf4f-3f1796c13cf9 | -9.15349 | -59.50429 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bdbbac7b-c181-30e7-b2d9-d9b8f64ec44a | -12.54728 | -45.62255 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50b6f850-a721-39ae-8785-f433a96c79e3 | -6.21156 | -49.86166 | 2025-08-24 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3dd80f0b-2988-30ee-abeb-8f214b970b5f | -5.42928 | -60.1597 | 2025-08-24 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 69a1a121-82a4-3bfe-8d73-ca328a35a1f8 | -5.74843 | -57.58523 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cb168811-bfc4-3acd-bb35-fad90b84c8c6 | -11.32186 | -47.85487 | 2025-08-24 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d87a3580-46a5-36eb-9f5c-edac8d830ab0 | -9.18577 | -59.46142 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a427ca5d-94cf-3e69-aed8-0cf5f32620ce | -9.96483 | -60.17992 | 2025-08-24 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39df44cf-ab11-3d24-b801-3e924947738b | -7.62252 | -45.24582 | 2025-08-24 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c756157f-e082-3e9a-8219-c14c22ffc4a7 | -11.83245 | -55.21257 | 2025-08-24 04:34:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5ddd4ea4-bc1b-3c6a-bc05-0f3c3dc77ffd | -9.67967 | -48.34853 | 2025-08-24 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96c51ce4-79bf-377d-8dda-9b1ddad7a589 | -9.15776 | -59.51404 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5f95fdf7-8a98-38af-84c9-cbc35321f402 | -13.0447 | -45.22236 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b23132d1-928d-38a4-a101-5b0ce107a4a4 | -8.76135 | -46.75386 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c34026db-b65a-355a-9315-eaaf7a6a477a | -9.64777 | -59.64661 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 39f9c590-9d5c-3cd1-9b81-382e4a2f0d6d | -11.18682 | -55.02438 | 2025-08-24 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56c3b77f-7128-3090-80bc-cc9e57a81c47 | -11.53664 | -51.84839 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 803fd5fa-9945-3ca0-b4f2-b690f8d05442 | -5.7403 | -57.59888 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 784402b4-529d-320e-a427-3d5d6869a4d9 | -7.66015 | -46.2236 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab355e32-b2cd-33ce-b254-0559f5e17f92 | -8.90047 | -62.4253 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c0546a11-cebf-36d2-a3ac-993790ee76ef | -9.1564 | -59.45609 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ff1ca9f1-47a9-306b-86f8-b9613d83fc29 | -6.88032 | -45.67945 | 2025-08-24 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db55cc00-d050-3d10-a25e-8d420585b33c | -11.54133 | -51.90686 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73d26f1a-2de1-3491-a6ef-1245f2cf002a | -13.04538 | -45.2175 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3018adb7-dfd5-3b2a-8bc7-8702700b3ddc | -13.1691 | -46.92052 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a1f18d4a-fa8a-344c-97b6-32a804ceac21 | -12.73228 | -48.12138 | 2025-08-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| aa9f7626-2631-374a-8594-5fe16c07018e | -8.91545 | -62.43532 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a6cc5209-5f29-3fe5-8180-e36cedf6ca2b | -5.79997 | -59.22591 | 2025-08-24 04:34:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb46c2be-13da-31a0-b5ac-36e07451e7ba | -7.92296 | -45.92101 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 34ad9a87-cfec-3790-998a-d31ac0852b30 | -9.1963 | -60.77959 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31a650a4-08c5-379c-a85b-b472d2520d2d | -8.27783 | -47.25567 | 2025-08-24 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 070fb820-f341-32de-996f-33649d668eae | -13.12756 | -41.05188 | 2025-08-24 04:34:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7a55a2fa-60af-323a-96cc-adb10b1cfb2f | -11.79382 | -48.78958 | 2025-08-24 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8efbf81-c025-3b8e-9afb-71f2d5835cff | -13.38972 | -47.52191 | 2025-08-24 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8b01434-0a6b-3b2e-848e-c4d91b90851f | -12.9935 | -45.22468 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6e63670b-66ea-3055-ac70-cab63fdf97b3 | -8.9202 | -62.43593 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2094a6ea-5b9a-344d-9bcb-5cc168f0af6c | -8.92721 | -62.43732 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f7313894-4ce6-3679-978c-047e691853ee | -5.80114 | -59.22097 | 2025-08-24 04:34:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7575402f-fc48-382f-a765-b9e119fe73f6 | -10.61071 | -50.14359 | 2025-08-24 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 598d0b01-f7af-354c-b52f-16c547604e23 | -7.50165 | -43.90092 | 2025-08-24 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9a8881e5-9e85-351b-a751-07c1235aa381 | -9.1516 | -59.48178 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 59b3a689-4f6e-3391-b7b4-92d6d001135f | -5.74021 | -57.60052 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b42e4446-bd18-316e-9946-cf6c919e904a | -11.5477 | -51.91211 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 289f59e0-a5fe-3420-9af9-72990bcba41f | -8.05551 | -45.00434 | 2025-08-24 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89607b8c-e003-33f4-b873-7cfb64f47101 | -10.80879 | -46.41776 | 2025-08-24 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6e5d9028-4e4e-3828-bff8-8733154f9deb | -7.60528 | -46.26131 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf16ac9e-2156-38d8-8789-4547e9c5e178 | -7.02016 | -44.64551 | 2025-08-24 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 06783719-3887-33b0-8bbd-0d8d29ffe343 | -11.18281 | -55.02434 | 2025-08-24 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ebdd208-6e6b-3deb-8594-21a8b933872d | -9.16821 | -59.4827 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| dd9aadca-40ea-317d-879d-975c6fcda964 | -13.33151 | -43.19077 | 2025-08-24 04:34:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5afa1e1e-54ee-31b3-9799-3a89b079c4f5 | -5.61669 | -60.23318 | 2025-08-24 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ba294db9-899a-39d3-91af-3555ab2317e5 | -5.74225 | -57.58804 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eef0a1cb-438c-3b27-b2e9-4383ff2bd6b9 | -12.7412 | -48.10798 | 2025-08-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 403ac869-8122-3cea-a608-f6e0b4dae409 | -10.55004 | -47.13993 | 2025-08-24 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fef1b397-06e7-31c9-a767-c09866c89d45 | -7.10606 | -43.69947 | 2025-08-24 04:34:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8f2b067-5208-32b6-9513-620eacd4e4af | -7.75267 | -47.35587 | 2025-08-24 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| e45730c4-3311-3e9a-8bc1-86f3c3a9fb07 | -10.64398 | -51.62283 | 2025-08-24 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99222b02-2915-30ee-a6a8-09357af669ed | -9.13656 | -60.77027 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4c571f6c-cc8a-37d1-80ea-3865851ccd74 | -12.96234 | -46.32477 | 2025-08-24 04:34:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e903654-798b-3df1-9402-64c25a59b695 | -12.73114 | -48.10619 | 2025-08-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72a3aba7-a058-3a09-982b-d0795171a136 | -9.20701 | -60.7924 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 6b9c92d8-a0fa-3c0e-a0bb-6d9378122cbb | -6.60782 | -48.04926 | 2025-08-24 04:34:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6721cc78-3464-3ef1-b5ec-597a02e98481 | -11.1158 | -44.78654 | 2025-08-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fc0443b-62ce-3314-8850-533dc72cb3d2 | -6.23371 | -55.94241 | 2025-08-24 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a489fbd-7f08-3aae-ad77-cf3460e316cd | -8.15885 | -47.29961 | 2025-08-24 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f856bcc3-c282-3f3e-9bd5-62bf0705eb43 | -6.43157 | -53.38676 | 2025-08-24 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1f9cf92-156a-3812-8c5e-71e6bedc2340 | -11.18565 | -55.0331 | 2025-08-24 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b76424b-d3ce-3518-8fbc-84b5f94deb76 | -6.98741 | -44.15776 | 2025-08-24 04:34:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11e9a990-a294-3a92-9a42-738ffcb9b6f1 | -9.15483 | -59.46449 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| a68c8510-37fd-3d01-81c7-011d16e9fe53 | -12.9448 | -46.29281 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96da6363-035e-3d57-b442-b130f1738ac9 | -13.46972 | -47.01775 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| eb23478a-a5f4-30b3-b605-0904e397b2d9 | -13.48684 | -47.02321 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1381e13c-443a-3bf7-ba2d-f71dbc3582db | -5.79551 | -59.21534 | 2025-08-24 04:34:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7fdc42bd-6639-3358-9e1e-b9ca45165ed4 | -9.17005 | -59.48066 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f868afbd-b6da-3c0e-96e8-7f876d74e225 | -12.72503 | -48.12381 | 2025-08-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4940f9c2-5d6e-3a67-896f-913cf0c18647 | -8.75953 | -49.97983 | 2025-08-24 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b59324b6-e194-3afa-85a4-a65228b99db0 | -9.14735 | -59.47199 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d571f8d1-1a51-3611-b08d-89fe96100e79 | -9.15899 | -59.49884 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eaadb2a0-d3ff-3b86-a2f1-66e5d6c133a3 | -11.27833 | -44.97567 | 2025-08-24 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README40.md)
