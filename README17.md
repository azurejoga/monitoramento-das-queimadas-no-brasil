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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6e033e8-95ba-3357-ba5b-d1edb5875afa | -3.16337 | -46.30082 | 2024-11-30 03:46:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a2ae3b8a-df29-3098-a09d-4aa90fd72d0f | -3.70884 | -45.68831 | 2024-11-30 03:46:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 35a5a69b-df63-3a4f-adbb-4f54bedf08db | -6.90526 | -43.55632 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ba81f398-6378-3e3f-b593-b27e1790ea08 | -6.90762 | -43.54247 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 134e905b-4217-310d-afdd-1db6ba970dfb | -2.96572 | -48.04206 | 2024-11-30 03:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d1874f9-006c-3322-84ad-f997af80b0f0 | -3.97466 | -41.50965 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 870fede9-19de-3a88-a113-b2edb606d4b3 | -5.42695 | -37.60165 | 2024-11-30 03:46:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 757ab91a-d387-3c8a-8785-cd774744cb33 | -2.31182 | -49.08231 | 2024-11-30 03:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 531eb64c-0e50-3b63-b423-544c31d74f56 | -11.83606 | -43.72577 | 2024-11-30 03:46:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cf1a5f9-26a5-36cf-8ffa-b2f570c03b1c | -4.00282 | -46.94595 | 2024-11-30 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 176c613d-03a2-3102-a13b-88f08bac0ae9 | -2.98294 | -49.59137 | 2024-11-30 03:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d637adc-8bd7-3212-a38c-6bd47621261a | -2.46154 | -46.57383 | 2024-11-30 03:46:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92d06932-9fe3-332e-855b-8de796299add | -2.86522 | -46.82964 | 2024-11-30 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ccb51b8-071e-3dd3-a1db-e98008442777 | -2.27051 | -46.43555 | 2024-11-30 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e62f1c1a-c2f5-30d1-8b46-71792a6f78d1 | -2.24599 | -46.45002 | 2024-11-30 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 487f86a4-bf89-3486-ac99-143a80b89c87 | -5.07121 | -44.99019 | 2024-11-30 03:46:00 | NOAA-20 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04ad9995-8390-3df3-8a6a-cc3c43eeeed8 | -4.44847 | -48.57074 | 2024-11-30 03:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3877a4a4-8ec1-3cb2-842b-a70105800fa9 | -6.70599 | -47.27153 | 2024-11-30 03:46:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ad5dee7-0803-33fd-978c-d0e693badede | -6.13867 | -43.95956 | 2024-11-30 03:46:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e45949a-5639-329a-808a-69744814e63f | -3.98764 | -41.50792 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 42457f6e-7c1d-3dcb-823a-86fd91fbd02c | -3.60226 | -49.99207 | 2024-11-30 03:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f5ff027f-cd2f-3161-9cdd-4f9233eed6e5 | -4.87686 | -41.3002 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f42c22b2-9f24-31b7-b7ba-27f939da622d | -6.07 | -48.04509 | 2024-11-30 03:46:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 75077729-a9af-3b32-af0f-35a7c638ec1d | -1.91579 | -47.90783 | 2024-11-30 03:46:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0ea0bb26-7a07-3690-8a1b-2ba7fc6e9c45 | -7.09182 | -34.98941 | 2024-11-30 03:46:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e4881c96-f37c-3e6a-8bb0-3bfecbcdaade | -5.12398 | -45.1593 | 2024-11-30 03:46:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e00b899-d221-326a-977a-5f9c197479d7 | -3.46269 | -48.93441 | 2024-11-30 03:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b6a5e1b1-cc78-33f5-8cdd-cb7bd3e6663c | -1.68191 | -46.78976 | 2024-11-30 03:46:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ba1534b4-7659-330e-9863-e3d60c569e3f | -2.2453 | -46.45428 | 2024-11-30 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45d89cdf-c477-378e-9efa-0a401ac502b4 | -5.93045 | -43.78537 | 2024-11-30 03:46:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2a618bb1-f868-3fd1-ac7d-5ea98710215a | -4.86961 | -41.31908 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 07cc57df-bd9a-32ac-83a5-15671fca438b | -8.3492 | -35.44284 | 2024-11-30 03:46:00 | NOAA-20 | AMARAJI | PERNAMBUCO | Brasil | 2600906 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 81111cc0-c45a-3c06-9752-491729a7532c | -3.20137 | -46.5651 | 2024-11-30 03:46:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5761afa4-db92-3024-bffd-7af581221fc9 | -2.42983 | -48.17639 | 2024-11-30 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b9065f6-3700-36ae-941c-36cd88e5e6bb | -1.67977 | -45.79464 | 2024-11-30 03:46:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cd8b7a81-1cb9-38ac-9f66-6eaec97d0a2c | -4.87178 | -41.30601 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| e5deaee9-a29d-3b6a-bd21-c5eee27189ed | -3.99684 | -46.94515 | 2024-11-30 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 899fa4cf-16e1-3410-b556-3c85f6d915d5 | -4.82096 | -41.28042 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ff1218eb-8a00-3df7-a098-a814cb66c2c1 | -5.59959 | -39.56546 | 2024-11-30 03:46:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d06a2afe-2502-334f-a1d5-dc1861dedd02 | -2.67219 | -46.10158 | 2024-11-30 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0173d005-53f5-39d6-bd28-88320f1d9a3d | -3.08263 | -49.21263 | 2024-11-30 03:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68454336-dc22-3bde-b519-bc6ffe19c44c | -3.44341 | -40.82941 | 2024-11-30 03:46:00 | NOAA-20 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c60d630c-0c34-3788-8eb2-8dee49e1ab94 | -6.9236 | -45.20937 | 2024-11-30 03:46:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa3b9800-b028-3961-a21b-9677848e0604 | -1.91503 | -47.90857 | 2024-11-30 03:46:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6fe107c-ac0b-3abb-beca-a3e874532cf4 | -4.13389 | -42.15307 | 2024-11-30 03:46:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 390de790-eca0-377e-8dea-214eb9a0a36f | -7.86118 | -45.92147 | 2024-11-30 03:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 36a52ec9-b7e1-393a-b1ef-933319b1d6c2 | -6.13566 | -43.94909 | 2024-11-30 03:46:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e9442ab8-2fe6-3738-8936-378d7c894a2b | -3.99407 | -41.52041 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 74eaa8b9-3e78-3656-9175-1abe1e9d67f0 | -2.51508 | -48.1915 | 2024-11-30 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5411a47c-e975-37df-bcd0-01386dc9f78e | -6.80375 | -35.71476 | 2024-11-30 03:46:00 | NOAA-20 | SOLÂNEA | PARAÍBA | Brasil | 2516003 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 75b29ee7-9c36-35c0-a959-f893aa38350b | -2.62761 | -46.88636 | 2024-11-30 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f7c284f0-05de-38ac-9909-5367da34a0bd | -4.8718 | -41.28104 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f22b55bc-609c-32f3-8511-0f16ef59e709 | -2.05707 | -47.57138 | 2024-11-30 03:46:00 | NOAA-20 | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba6bd48a-d105-3440-b62c-51dbeef9eec1 | -8.27544 | -35.33041 | 2024-11-30 03:46:00 | NOAA-20 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c3437d1e-1d71-3568-b7fd-ee1362b0b465 | -4.07504 | -47.02443 | 2024-11-30 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73227176-af60-300a-ad73-73633294720f | -3.61766 | -42.73623 | 2024-11-30 03:46:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72bbd9b0-bc19-3dec-9b7c-ca7ab3184984 | -3.69978 | -47.14344 | 2024-11-30 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 398f90f9-29eb-336f-a571-b755f2cb7f6e | -4.01785 | -44.37632 | 2024-11-30 03:46:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 575758ff-5fd6-3e7b-87f5-1a7752987f2f | -6.92867 | -45.21017 | 2024-11-30 03:46:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acfd7ec2-c679-3b19-ad32-0045fe26554b | -2.14193 | -46.48961 | 2024-11-30 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 00ca92cf-d904-31ef-9e1b-838ef1ade357 | -2.95262 | -48.00101 | 2024-11-30 03:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad716760-2cfe-3b9a-a017-6d958df3d098 | -4.29047 | -40.60799 | 2024-11-30 03:46:00 | NOAA-20 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8e59cba7-7577-3110-a940-69543e4098f2 | -5.91124 | -43.84278 | 2024-11-30 03:46:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9aacb4ea-b13e-35b0-9e6e-e54e2773d6e4 | -7.23866 | -40.26717 | 2024-11-30 03:46:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9f1f028a-e17b-32f8-b386-c79a49a34942 | -6.90822 | -43.56622 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12a20408-7a7c-3664-92a6-733cb6801e88 | -2.46554 | -46.56636 | 2024-11-30 03:46:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5dc4c874-bfe7-31cb-9650-28bc715736ef | -3.27647 | -45.56758 | 2024-11-30 03:46:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 345bad39-a208-3db4-9114-e045a1b96fe7 | -3.35518 | -49.76766 | 2024-11-30 03:46:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7d74ff7c-4651-3cd7-bbb1-8e9478e79f2a | -2.75758 | -49.41339 | 2024-11-30 03:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70b04c47-e5a9-3d0b-a6a1-fdb058be4f7f | -9.6491 | -36.12318 | 2024-11-30 03:46:00 | NOAA-20 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8a9410de-b331-38ca-8840-da9c8d37954c | -2.27176 | -46.44093 | 2024-11-30 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1d6f1e8-c0ae-395b-8c3f-7b17b7d954d1 | -6.91508 | -43.55324 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 634534a4-1b43-3686-bc7e-5b8aa277e924 | -6.91352 | -43.56239 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9a088351-1525-36ab-90a3-6a8f678cea6d | -5.52326 | -45.40944 | 2024-11-30 03:46:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 903a0478-1f1c-3776-a627-4d7b68a50105 | -2.27122 | -46.43135 | 2024-11-30 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9325a2b-74e4-3521-a137-2461db0117ff | -4.53841 | -46.42417 | 2024-11-30 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 824ef36c-352b-3f5b-b191-4aa4e9f94296 | -4.15158 | -48.99473 | 2024-11-30 03:46:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eba387d7-e6ab-32f4-b322-9764efdef30d | -8.37494 | -44.47917 | 2024-11-30 03:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9b878f5-32df-36a2-b094-6b98b13f89b4 | -6.48388 | -42.8198 | 2024-11-30 03:46:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6d37053c-add5-3a66-ad0d-3b238d09bc42 | -4.87345 | -41.29589 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cc797edd-e8ea-3b37-807a-6a1fee2d266d | -4.86046 | -41.29973 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 07e3b1f5-d8a9-30c5-bdbf-6249e8946c57 | -12.27705 | -40.36 | 2024-11-30 03:46:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 34f09c7b-ac18-323b-9db6-28b6cf96e19f | -3.25666 | -48.89476 | 2024-11-30 03:46:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 36256982-1195-383e-be84-a896ea334811 | -4.44046 | -46.01291 | 2024-11-30 03:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23ead55e-81f6-321a-bed2-9fd687628f0b | -4.87743 | -41.29679 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 54469888-2d94-3bc4-93d0-b33be35d09d7 | -2.18137 | -47.15303 | 2024-11-30 03:46:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b5e2874c-8750-352e-94aa-bd2aed5b2b7b | -8.84308 | -44.75777 | 2024-11-30 03:46:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8dfe7668-8856-31ed-af45-0c78e6406dc3 | -3.82576 | -40.96978 | 2024-11-30 03:46:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| aad107a6-14f3-3732-9496-eba78400ac7a | -2.98687 | -49.5937 | 2024-11-30 03:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9837d8f-764f-3607-843a-2d82c17e0fd3 | -4.01481 | -47.00059 | 2024-11-30 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62a54f5c-3037-3e92-b247-2b85948dd249 | -4.98269 | -44.68958 | 2024-11-30 03:46:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5e3e7c9-2587-32d5-a8bb-746a209a8ea7 | -6.47609 | -39.52294 | 2024-11-30 03:46:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| de1b5520-7be8-36dc-b077-0686c7b68b9c | -6.90604 | -43.55172 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| b8ebc8d6-1472-3ef7-ad7c-284b9d3a39bf | -3.96424 | -48.0959 | 2024-11-30 03:46:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a23d0420-5f04-34a8-aea4-f422308e9183 | -6.59311 | -35.25085 | 2024-11-30 03:46:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9f85979e-9fb8-3d11-82f0-178f0d192b9f | -6.82004 | -46.77686 | 2024-11-30 03:46:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09d96be6-4b8b-3ef2-bc75-36009c07569a | -2.27712 | -46.43234 | 2024-11-30 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 147cd62a-f181-343b-a465-e59c64e6dfc8 | -6.06865 | -48.04824 | 2024-11-30 03:46:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 870d3182-f31e-3a5c-8caf-377c312f5ab0 | -3.69783 | -45.68647 | 2024-11-30 03:46:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64780427-de1e-35cf-9255-1db3092d6a54 | -7.16153 | -38.71323 | 2024-11-30 03:46:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |


[Clique aqui para ver as próximas entradas](README18.md)
