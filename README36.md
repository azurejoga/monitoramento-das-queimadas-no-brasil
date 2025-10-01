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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d39e53b-dae1-3091-bf94-606081f49c55 | -7.09438 | -45.55842 | 2025-10-01 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5c3b5d35-30ff-36dc-918f-daf77526db8b | -3.80802 | -47.58982 | 2025-10-01 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f947d35d-f8dd-344d-9f72-e9fdc342a768 | -9.94004 | -43.65022 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6fd32c2-0c41-3463-98a2-bf1ada74ff73 | -7.84068 | -48.20911 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 861a8ab3-eec4-346a-b090-c8cc466ccb0b | -5.77044 | -43.62238 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2139e96-5938-3ebc-8e37-4336acb45828 | -9.94228 | -43.63527 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 135e7f0c-a917-39a5-9f25-b0d0fe40ffdb | -6.02491 | -43.78033 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b5f1bf3-1e5a-3749-a2c3-54c81dd4a940 | -7.77079 | -45.71654 | 2025-10-01 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1134eae5-04df-3886-b118-bcf33b1817b6 | -6.04703 | -42.44969 | 2025-10-01 04:19:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6a84ee82-4b9b-3540-a49b-010f44fc32dd | -7.51528 | -45.43703 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3be6e42c-97c2-35f9-9f58-9bb2a26226fe | -3.78266 | -51.29135 | 2025-10-01 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 018fa88d-684d-3e85-a989-85b6855e8414 | -6.34823 | -44.8306 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd21a16b-ae57-314a-b71a-15646502af8c | -6.38195 | -43.86833 | 2025-10-01 04:19:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5e0aae19-e195-38df-9fd1-2ca08789fc9d | -3.52308 | -41.23333 | 2025-10-01 04:19:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b59746c7-104e-3a79-ad36-7e34483d2172 | -9.27655 | -45.68807 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 686475d7-23ef-313d-9094-b4598f907733 | -5.69723 | -42.6471 | 2025-10-01 04:19:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f2ce3f89-d472-32f5-a3b9-d27d129b2752 | -3.86821 | -40.33562 | 2025-10-01 04:19:00 | NOAA-21 | GROAÍRAS | CEARÁ | Brasil | 2304905 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7cea7ae7-ac14-31f3-80eb-039d147b254f | -4.13266 | -44.28226 | 2025-10-01 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92cfbe59-b504-3587-b488-3e43c72cb23e | -7.07024 | -46.75776 | 2025-10-01 04:19:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58a0b099-0698-3331-8665-0d36a342e8b1 | -5.50528 | -42.75765 | 2025-10-01 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 10be88a6-5b4a-324a-9fe4-fb18c04a136d | -3.2728 | -52.5075 | 2025-10-01 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9acc9a68-773a-3e22-85c8-efab7a49e72e | -5.90519 | -43.91557 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28e46802-2192-32f6-a527-625c50858ddd | -6.14035 | -44.74087 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 71a4776a-4e30-3bb8-bb8a-9c4779652b22 | -6.11534 | -45.89453 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 763f4274-a23f-3666-9962-1276fbf3309e | -8.87684 | -47.64731 | 2025-10-01 04:19:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95e9060e-0962-30c6-903e-84e39566e675 | -5.30166 | -43.13717 | 2025-10-01 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61b6037b-c9be-39d1-83be-5740f12be2f0 | -3.10027 | -47.02009 | 2025-10-01 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09bcc40f-283b-385a-add9-27970144e9de | -3.93971 | -41.59054 | 2025-10-01 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dd91181f-911d-3dd9-9567-f9f619ada2b7 | -6.21451 | -44.22304 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fe37ab69-6596-37af-8b57-bb671db3db56 | -3.46925 | -50.08268 | 2025-10-01 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92041372-9d33-31d9-9de7-5c87909cb28a | -9.93042 | -43.66786 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 89ea1535-082d-311d-b1fc-05eff4a9d4a5 | -9.41619 | -47.33467 | 2025-10-01 04:19:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3d1c425a-99bc-3459-bc80-e8937c6af55d | -7.77051 | -47.38556 | 2025-10-01 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70b0ee41-a594-3455-ad0c-d280e798eb96 | -5.50189 | -42.75712 | 2025-10-01 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f464b9e6-b8b8-3e5e-a031-84f4d6d30db1 | -5.64604 | -43.94224 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 749546e4-2701-3e4a-9b95-3b7434cee3af | -5.18347 | -41.24281 | 2025-10-01 04:19:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 383e36b4-a630-3e95-8092-db6d085a8e97 | -3.84691 | -48.95653 | 2025-10-01 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a630e7a7-4a5c-306a-83d1-b35fa375730a | -5.95179 | -45.87618 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54aaba89-396e-3860-a1e2-12ac3f0f5108 | -4.88489 | -43.40952 | 2025-10-01 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c666d32-c69d-3193-9982-aca909c8a947 | -5.70726 | -42.83703 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 8705ca3c-dc91-356b-9f96-308d87eb0dcf | -9.33263 | -45.69696 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50e6136e-04b7-39b2-8908-f383beb37a3e | -5.71517 | -42.83073 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1903f97c-dd64-3566-83a9-5dbee591bb4f | -6.1482 | -44.73873 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4a4c53f1-9ae5-3360-93e9-94e054d6d94c | -9.93825 | -43.61554 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b6abe81-4086-32df-b64d-e5c190e63297 | -8.89662 | -45.04757 | 2025-10-01 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a8fbb2bd-af24-3959-92d4-69e969d54608 | -8.71313 | -50.05352 | 2025-10-01 04:19:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0afc7030-c90c-3502-adde-fc5d7df19b45 | -7.26263 | -45.48595 | 2025-10-01 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89c5a344-17a8-3a05-8659-e612dc8eb99d | -8.55363 | -44.65162 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e3adae4-58ac-3f7b-a7c3-8f0b84a54185 | -8.89841 | -46.62915 | 2025-10-01 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36a786ca-c433-37a9-84fc-091288caad3d | -6.16892 | -43.09295 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 9395172c-66a2-3267-9acd-0437152ae424 | -7.63132 | -45.45594 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f7345001-9434-37e0-9e48-4c7b73968a4f | -4.43313 | -40.75409 | 2025-10-01 04:19:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2a685990-ec9d-374d-a9af-5c922897ce86 | -7.46846 | -46.48463 | 2025-10-01 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53979397-972f-3d44-8f75-7dbe357791c9 | -5.3813 | -43.58705 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 571c9547-8be0-3375-81b1-1a9da3754a11 | -3.41399 | -40.21507 | 2025-10-01 04:19:00 | NOAA-21 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 67f684ae-086e-33ea-bd20-6cbfec1f0818 | -9.31176 | -45.72216 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4af87c5-d5dd-3c64-a24e-db51ea61682b | -5.74688 | -42.8729 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b497b870-e8cd-33b3-9e57-d554b3881320 | -6.02159 | -43.77982 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d7ba6fa-f40c-3af5-9247-7dc4dfe9d086 | -7.6279 | -46.67707 | 2025-10-01 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3b238eb-5878-33f5-9fc5-d468fc64a984 | -6.57364 | -43.43872 | 2025-10-01 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8b82dd66-9875-32e0-a325-1cd4af8c1332 | -5.45716 | -42.83668 | 2025-10-01 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d7d71ddf-e0fe-36e0-83ff-611521641f67 | -6.34769 | -44.83405 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb6ecf82-ff0d-3f65-b0c0-46875b7bef01 | -7.04031 | -45.20896 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe1a6435-648d-3ee1-9687-65a55790d98a | -7.21351 | -44.75557 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 325d4d14-e6ce-3791-8590-1a332420eec0 | -9.89738 | -45.93803 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2397fb7d-a3c6-34b9-89e8-29880fed495e | -7.43597 | -46.97548 | 2025-10-01 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 87db5353-f692-38a9-99b3-396cb68dd79d | -5.06121 | -45.60817 | 2025-10-01 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7094818-d2a7-38d9-ad9a-6460c84e2481 | -7.05086 | -43.2749 | 2025-10-01 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 286c70e6-c12c-39f3-8182-45cb7dc41bf2 | -5.83266 | -43.87865 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6a89b40-9d2a-3716-bb50-110fe810a0d9 | -9.33373 | -45.69 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aaa9ba8a-78b6-3591-89c9-c9cf4cdd4d0f | -5.16324 | -43.72067 | 2025-10-01 04:19:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 254a3a95-95c8-312f-bb2a-7cb730b4ec4a | -9.2661 | -45.68998 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20968450-3971-37b2-80c0-6b90e044c1b3 | -6.05566 | -44.43441 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a68794ef-fbcf-3bd0-8f46-b8806c30a2dc | -6.09227 | -42.47226 | 2025-10-01 04:19:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 42b0250a-229b-3756-964b-a94bde4c4524 | -6.89831 | -48.00036 | 2025-10-01 04:19:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc342afe-2b24-3291-aff1-dded8707e297 | -7.79351 | -42.50667 | 2025-10-01 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 27c49655-95a4-3325-b1d1-88dcc85ff6a6 | -8.22543 | -45.79 | 2025-10-01 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 199bd71f-81cc-37b6-9531-d37f3a79cb4f | -7.76272 | -47.4119 | 2025-10-01 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36fa1009-1a2a-37ee-856d-b11c509fac5f | -7.05376 | -46.41763 | 2025-10-01 04:19:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2392eab8-1dab-3d42-80d5-04958ad5d317 | -7.63513 | -45.43174 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad7e40ab-420a-360c-9139-9d8af6bfe98f | -5.78918 | -43.30344 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fe951dd-4d2b-3873-9cd3-79ec21068b38 | -6.29335 | -43.36248 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5dd52dc-91e1-37f5-a693-ad0c14a7377d | -5.89459 | -44.2929 | 2025-10-01 04:19:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ea192a82-2f83-3cea-b89e-46cc8e08baa7 | -5.53794 | -43.87224 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 0c82e606-8021-3a1b-ac69-8a5e74841773 | -5.96127 | -45.8595 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 62c002ff-12ca-3340-b8fa-0103d3e85925 | -9.95013 | -43.58288 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74e79073-338c-3597-a414-e797fff89dfa | -6.95635 | -46.8535 | 2025-10-01 04:19:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9ec03d8-4d3b-3576-a1db-c7945f266ca2 | -7.62848 | -46.67342 | 2025-10-01 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e7d32ff-da3a-3195-a2bb-250642d3c9e0 | -8.58062 | -44.6523 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fa84bd1f-3813-3a8a-8bb2-f1277dd930d7 | -5.78078 | -42.86269 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 21b7ba42-ddde-3f87-bcb6-2e6cc53ca001 | -5.63934 | -43.9199 | 2025-10-01 04:19:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 121ecccc-7e68-3596-91ac-e0ec341f0c57 | -6.06122 | -42.44409 | 2025-10-01 04:19:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a4340df3-9536-3470-962a-0f1d468978df | -7.78744 | -42.5148 | 2025-10-01 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 56a32b71-de91-31cb-a415-95aa4b6e54f0 | -6.23388 | -45.33884 | 2025-10-01 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| a51dd94e-cda6-3df9-9f14-8ad25707c95c | -8.57114 | -44.77903 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa76bd7b-28ae-3a52-bb36-65f05fbe731e | -5.87499 | -43.56278 | 2025-10-01 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2ff1ef7-0e6f-39b2-bb2c-0c56541b8e84 | -5.15747 | -42.71605 | 2025-10-01 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3851670-0f9d-37bf-b399-c9d8cdb1f224 | -6.23497 | -45.33191 | 2025-10-01 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f03c2914-32e8-30a2-8636-dbe2f4aa0e47 | -6.30366 | -43.47375 | 2025-10-01 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ef9ad3f-3cf6-3cfb-a983-6a5090d9de5c | -5.77134 | -43.30796 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README37.md)
