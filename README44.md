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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0d868c4-e87d-3294-a752-75c79bc89be7 | -4.73006 | -48.30619 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9427a30e-6455-353f-a6ce-06c03d6cdf9b | -7.54631 | -46.24413 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b2dd1ff-9202-39b7-ace6-16d8e0bcef57 | -4.51159 | -42.83732 | 2025-10-28 04:42:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 854888b1-6fa9-334f-b479-d7870dfa8430 | -6.22479 | -42.53595 | 2025-10-28 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| af516824-b6a6-3af0-9429-9015944f95a6 | -7.3875 | -45.12841 | 2025-10-28 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76532584-a9ad-3265-9741-9b8c1601a28f | -7.95101 | -45.47157 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a7ed3940-73d8-3ce3-85c1-55ac2de158e7 | -6.64768 | -43.37996 | 2025-10-28 04:42:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 11ff5fb5-745b-3383-8cb3-bf915cdf3b2d | -6.11896 | -42.45869 | 2025-10-28 04:42:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 687a122f-6599-3f98-9260-ab70d6118e5e | -7.7871 | -46.44822 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4683d5ba-0446-31d4-ba66-74af1325c211 | -7.32568 | -47.21732 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ccbe1e00-8549-3f3a-952c-0913cd5f868e | -7.96505 | -45.5372 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 32e94e9d-72d0-37d4-878e-0be452f4f1fc | -4.14339 | -50.68696 | 2025-10-28 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b3e834b-1a99-3ec7-ab18-26565c5fc352 | -1.69799 | -53.69856 | 2025-10-28 04:42:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a7cecf4-f1a6-3f3e-8ee4-68c9cbdad6de | -7.07091 | -44.94724 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dca73036-61d8-30d7-973a-2f194e96058e | -7.0741 | -44.95301 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4b618601-9e12-3a73-8c67-a62120497535 | -2.47829 | -49.25585 | 2025-10-28 04:42:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5cd2fc1d-e7c5-3048-a509-14867372ff5b | -5.27818 | -45.73428 | 2025-10-28 04:42:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6fb1e59-19b8-3b1d-aa27-e1dd782ea4b1 | -3.04738 | -53.01706 | 2025-10-28 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a613da82-d7a8-3970-9e62-fb283631f36f | -4.45322 | -43.64614 | 2025-10-28 04:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| fa573e12-933e-37e3-8c94-4299b9aadfd1 | -7.76526 | -45.40423 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 00d36da7-1055-32ee-8d73-ac9869e23dc5 | -7.8076 | -46.48626 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 978a6597-101e-3df5-a3d1-ccfc1e66bd81 | -7.46882 | -47.1536 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58b5a7ff-3a8e-316e-a5de-d005dd5b9552 | -3.91262 | -43.32079 | 2025-10-28 04:42:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 795b77a9-1062-32f0-b8e3-ba7b54afa526 | -4.25394 | -53.5442 | 2025-10-28 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e66eacf-56c4-34df-9a2c-e9106e7eaa7c | -6.83364 | -43.99232 | 2025-10-28 04:42:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| caf60f4d-c684-36e3-a808-6f55266929da | -7.94225 | -45.50414 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a3b218c0-4739-3d7c-b1ca-f6f470d6a6f9 | -4.89791 | -47.65876 | 2025-10-28 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe07b5ea-18dd-34e8-bc1b-41e2573d6e06 | -4.5031 | -42.8381 | 2025-10-28 04:42:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 901aafc2-0c0f-37d2-8fd2-3d3acff413ab | -7.94929 | -45.51014 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a8936119-41d6-360c-92c5-b021c740f784 | -8.08296 | -45.95854 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8aabebb6-00d4-3b5c-8bb5-8ffbc40d39d8 | -5.52998 | -41.70987 | 2025-10-28 04:42:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 05b4d188-d794-3e3f-a062-59776c52bb8f | -7.96408 | -45.4637 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 689bc7dc-2746-3e21-ba30-c022d3cda2d2 | -7.83946 | -46.39928 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c3a0a7b3-7dda-3978-aef6-9d7e413ffd89 | -7.96978 | -46.74437 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7f670150-f082-31ef-a437-3ed61ecc3c7f | -2.91859 | -48.72213 | 2025-10-28 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53aed79e-5cf3-37f8-8988-e68239803769 | -3.69075 | -49.57495 | 2025-10-28 04:42:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e73d9a6e-95ef-3163-9ed6-1d50c3ee5ae9 | -7.3929 | -45.11922 | 2025-10-28 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1adbce32-25cb-384c-9742-c8cade8d3a11 | -6.86546 | -43.45129 | 2025-10-28 04:42:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c38e138-6e37-35ad-9c89-b7a7a3d82c1d | -8.15731 | -47.00657 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2225d89-b698-3705-9ce2-14e935692b2e | -3.57333 | -43.62989 | 2025-10-28 04:42:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| acb570ac-e2ac-3d53-b3a6-b47de1861297 | -7.81666 | -45.37976 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6340e98c-5325-354d-8e78-8a6cd4aaaeca | -3.50028 | -50.05003 | 2025-10-28 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b25db2d1-4647-3f5c-b4d8-97bfa0b06c95 | -4.35945 | -50.51524 | 2025-10-28 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e0fe5cf-7727-3439-be05-c9197a5dcfcb | -4.18548 | -46.22957 | 2025-10-28 04:42:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56ce8c90-6a83-3e16-ac9a-2a87a984a082 | -1.49551 | -53.12843 | 2025-10-28 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b9145e04-32f9-3794-bc88-ad2d1dec22e8 | -2.35408 | -48.29084 | 2025-10-28 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd187ede-2447-38ec-8dc9-d0d29082e772 | -7.99355 | -46.19241 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a1efd49-50c7-3e52-940f-4dda125f98bb | -6.63723 | -47.19777 | 2025-10-28 04:42:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8fa290e-6067-3abc-9fa4-1e1371ac9525 | -3.69274 | -43.20981 | 2025-10-28 04:42:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d165c978-9afc-3f81-95e7-6637c08c9de7 | -3.97041 | -44.30978 | 2025-10-28 04:42:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1859aa58-5df9-3db3-8231-38cdff021f68 | -7.83579 | -46.39873 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 834dd3c1-048d-35a2-9064-98fc2aa88564 | -8.4492 | -45.12237 | 2025-10-28 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65883bf1-092f-3a16-8051-4f1cc9c5426a | -6.42538 | -42.33284 | 2025-10-28 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ac975565-55cc-365a-93cd-c0331b2ceb68 | -4.22093 | -48.35565 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84f542cf-9b6b-3c30-b083-cf29f00d461d | -7.47115 | -47.16206 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03a746ad-44ec-3262-b69e-0012a624c2d7 | -7.96791 | -46.75684 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 964f7a53-f639-3248-bf96-5509496442c9 | -6.13469 | -46.691 | 2025-10-28 04:42:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61216faf-1035-3943-84ec-906d02354e6f | -7.45493 | -47.02958 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d8971b7d-ba2d-3e40-a179-ee3881ae5cdd | -2.94764 | -49.35107 | 2025-10-28 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02b6bb92-ad0c-3940-8c76-899f2c5697e9 | -8.04481 | -41.11046 | 2025-10-28 04:42:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2562c3a5-4233-36ad-a607-bfaa1c36e2a2 | -8.19556 | -44.44313 | 2025-10-28 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2f76cd6d-2e89-3589-b5fd-53eb1fc82ffa | -3.95098 | -48.09154 | 2025-10-28 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bb5d17f-60fa-3e71-a52a-07493f66e40a | -6.16098 | -43.09986 | 2025-10-28 04:42:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4bdf2e88-a905-3d04-9381-ffff1d8b9231 | -7.51565 | -46.29726 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d9266b7-686e-3f07-a3c9-6db00db57157 | -7.12442 | -47.02401 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fc8c845-1772-32fc-b214-57821faa50f6 | -5.55688 | -49.47463 | 2025-10-28 04:42:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5bf8e9ab-6c9b-33c5-9c73-b2c0488a0870 | -8.32276 | -46.15794 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b513dd0-65d9-33ec-a694-d32106ad870b | -4.02237 | -42.90843 | 2025-10-28 04:42:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c6b4bc4-a8c2-3d42-8e54-8f11a37f3512 | -3.11906 | -51.208 | 2025-10-28 04:42:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fb27a07-2666-3f81-86cd-ece9df960055 | -3.02679 | -45.36586 | 2025-10-28 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 403cc172-28e0-3389-910d-9a9ab268a91d | -3.40246 | -50.27312 | 2025-10-28 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e1e7adf-4d30-3283-bc42-05b77fc405cf | -3.54589 | -49.43794 | 2025-10-28 04:42:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f66d1c3-fb01-30d9-bf01-2de9e9cf610e | -3.53143 | -53.31326 | 2025-10-28 04:42:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c365c3eb-ca2c-351c-91e5-b3ab90ebfb2e | -1.17697 | -54.20715 | 2025-10-28 04:42:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffcb52e5-cef1-32be-91b5-f58b154c16f5 | -5.5581 | -49.57428 | 2025-10-28 04:42:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02c4d381-20df-3a6e-a579-7303cc58ac84 | -5.70579 | -43.53633 | 2025-10-28 04:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bd5c77d-c610-3dce-8c8e-d3dc95dba6ef | -7.97577 | -46.75371 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c18c46f5-85e9-388c-8cac-4ca45ce1d527 | -7.11972 | -47.03124 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 792fc2a7-de60-3a5b-9896-16187b2dfcaa | -3.87819 | -47.99772 | 2025-10-28 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7510e42-4780-3451-8b22-5ca676f6b868 | -7.25499 | -46.81054 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0dc1777b-eb1c-314a-9fa3-e078547ce392 | -6.77738 | -46.4566 | 2025-10-28 04:42:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45c42159-1d94-3b2f-b5d6-425d79db436e | -7.97841 | -46.71152 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83255554-cf68-340f-aa26-49bb27a852b3 | -3.59252 | -43.61408 | 2025-10-28 04:42:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc7b263b-912e-307e-8c84-06a6d6d4c566 | -5.314 | -49.49323 | 2025-10-28 04:42:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5dfb4041-fb17-38ac-a87d-7f63755c14ae | -3.08291 | -44.44585 | 2025-10-28 04:42:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 517a30c8-6a98-3675-9a6e-e67610bf6f5f | -7.4553 | -49.4085 | 2025-10-28 04:42:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| eb0bdba9-6363-3fd4-9e4b-29b9a602cf0f | -4.33053 | -48.09321 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23656232-34cb-3097-9209-4a988efce882 | -6.24123 | -42.55213 | 2025-10-28 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 98868611-1a2e-3016-950b-70d08ee0d5eb | -7.32276 | -47.21286 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4e7801c0-ea51-3411-b0d0-b602230db299 | -7.75995 | -45.41325 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 499fba30-e06a-3771-a0cf-0651357d3309 | -6.24058 | -42.55658 | 2025-10-28 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 409f55b7-f799-3fb7-9dbf-2425109a238d | -2.91527 | -48.72161 | 2025-10-28 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7f45966-8ab4-37db-b94b-60f89a8a0d87 | -7.946 | -48.02523 | 2025-10-28 04:42:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20f8b565-835a-3ae6-b9d2-8bcd8d6d1a64 | -4.26609 | -48.69695 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 061772dd-5af3-351f-830e-476341491dae | -4.86645 | -48.40244 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9c9e96a-b31b-38b7-9fd2-0dcd85afedca | -4.44411 | -45.97972 | 2025-10-28 04:42:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9a47cbc-923f-3a36-a852-444e33abb575 | -1.50344 | -53.12985 | 2025-10-28 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7df9b7a9-96a9-3aec-a218-ecdde1a74275 | -7.2929 | -45.06568 | 2025-10-28 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80c7d345-069c-3709-9fbd-2f6d36a38845 | -4.22874 | -48.37116 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0deeb2d3-d344-356e-b778-efd719a68d56 | -4.35814 | -48.64737 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README45.md)
