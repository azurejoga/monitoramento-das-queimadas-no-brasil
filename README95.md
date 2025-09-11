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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eeab896b-2c12-380c-a041-ebe33fd07ec8 | -6.27767 | -53.42262 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ac7c0db-24de-3ae8-9b18-0f843d9c603e | -5.7933 | -45.6826 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 41f7f313-f0ab-3b30-b711-044a84d10031 | -5.87401 | -45.66885 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e7e88d3-06ff-351a-9747-7f95fa3bc285 | -6.83685 | -45.61303 | 2025-09-11 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec122a8e-d47d-3802-880b-1d4f5c5c53c9 | -8.0399 | -49.05337 | 2025-09-11 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dc007d90-023c-338a-b853-d39d8f01214b | -6.81313 | -51.88037 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e939ade-e183-3215-89d8-4e135b66eb74 | -8.03825 | -52.37899 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c7aeeb3-aa11-3657-b5e1-6d6b5a11cc8c | -8.02869 | -48.65518 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 87c23d5f-4eb5-3e90-9f52-df54deb43129 | -8.58314 | -45.58457 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| caf52fac-f21e-3040-a9ed-93a8369e7393 | -4.21804 | -46.35955 | 2025-09-11 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 03f58d2e-f94e-398c-b62f-1e34764cd097 | -7.78676 | -50.76733 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 1adae9c6-5c32-3b48-95e6-f8a75a68202a | -8.56444 | -45.59333 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01edd709-7f71-325a-bc5b-efe465110d4b | -5.22771 | -46.09013 | 2025-09-11 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 774e7d63-98fb-3400-8d80-0643578263cb | -6.25696 | -43.49048 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48653a37-66d2-33b0-b5f6-0c3040bef555 | -6.17337 | -41.06844 | 2025-09-11 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b698f25b-059c-3eec-83eb-2048524d04ac | -8.04712 | -52.38773 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 15554cfa-ef39-3650-9e2d-c442deeb2a86 | -7.49877 | -48.24434 | 2025-09-11 04:44:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42ef2cfb-b897-37fe-a1d2-e864f2d3c900 | -5.8581 | -47.05524 | 2025-09-11 04:44:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d21c58fe-d76c-3396-a82d-66d06918b097 | -6.24844 | -43.41258 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 60688bb2-613a-3fb8-a4a5-d1af2e191cf0 | -4.85993 | -42.7692 | 2025-09-11 04:44:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a5116e39-101f-31a5-adbe-4691deab938c | -9.08446 | -47.09 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 544c6e0d-861c-3ec1-8bf8-bd4e661cc687 | -5.93766 | -45.71606 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10047610-360f-36c7-8ee2-b25c8fd20eec | -5.38311 | -47.73007 | 2025-09-11 04:44:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 507f7242-de26-361e-befb-d3ef06892cf5 | -8.03875 | -48.66053 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 221d35dd-0d88-363e-b1dd-ab2d7925c4a9 | -5.72736 | -49.21917 | 2025-09-11 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 28f5ccfe-e778-383d-bb71-26aac62c2bae | -8.42614 | -49.08542 | 2025-09-11 04:44:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d793e23e-3413-3b20-b941-67ed3448ef12 | -5.55858 | -43.05211 | 2025-09-11 04:44:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ae67e96-5325-352e-a882-0a910284448c | -5.2396 | -45.46156 | 2025-09-11 04:44:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bad2c4f0-3966-3658-b34f-e0c764440e79 | -6.89783 | -47.92009 | 2025-09-11 04:44:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 63f05a00-f6af-3c3d-ae91-a8b892c52689 | -2.78952 | -48.60648 | 2025-09-11 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 583aed6b-fa30-3157-8225-bdcb5481dd00 | -7.86769 | -47.98245 | 2025-09-11 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 07628784-b66a-3431-856a-586879ff3b0b | -5.50741 | -46.65811 | 2025-09-11 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e3fdd29-0c49-3211-aa5d-7a7c376f0147 | -9.06241 | -45.70623 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 050551e7-b679-3986-a0bc-5e1e917de788 | -8.64581 | -45.71928 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 59f4571c-9207-3b4e-a712-5e9a75ed7b29 | -4.04441 | -49.07476 | 2025-09-11 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 981919a2-63f0-30bf-9b94-6fd1e76c5113 | -7.84137 | -45.40211 | 2025-09-11 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 02f900d4-e7a6-3077-bb78-5aa1b41f29d9 | -6.82773 | -44.88876 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa94aa55-17ec-334b-b002-555e1aaf7213 | -5.57689 | -42.92767 | 2025-09-11 04:44:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 6fb82d4c-fbc6-3401-a939-522c0c4dae5e | -6.22106 | -43.5004 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2691703d-eb65-3a15-9a6b-55911a7bcffb | -6.44676 | -44.04235 | 2025-09-11 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f6c09e6c-6acb-347b-931a-721d80758780 | -8.07212 | -50.17949 | 2025-09-11 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3043388c-7fc5-3910-9f77-aa60036c3581 | -9.06892 | -47.08577 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 48e2ec3a-3103-3cb2-b520-9044545f1362 | -7.78622 | -50.77084 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 57b4f1c0-ace5-3ab0-ba04-9276c12b9df3 | -6.21633 | -43.49944 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| de07bb02-5978-3c55-b308-06e8e7e208ec | -7.53925 | -48.23256 | 2025-09-11 04:44:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e57607fb-0a93-3f25-b8a4-43feb5a638f2 | -7.92049 | -44.86996 | 2025-09-11 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e3e3ddf-2eee-3c9c-be51-94884a03f92d | -7.18159 | -44.95651 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d1edc0e-bd9a-3e66-9d4b-5d16f3c64566 | -5.69484 | -45.33061 | 2025-09-11 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db527a09-7844-377b-93e1-de0d8c6f020f | -7.22025 | -45.31456 | 2025-09-11 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c0cd1ec9-694e-3fb0-a948-01bc339ddba5 | -6.81812 | -51.87042 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 423b33ec-83a2-3dbb-ab53-77d6e80595dc | -8.5125 | -45.6893 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 228527e3-d30d-3395-8cd7-bf96ce446cab | -6.69742 | -44.94554 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f441f149-d632-3370-8b7b-4c07fcb9107d | -6.69805 | -44.94128 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8153efd-debc-3519-9456-883d3882f04a | -6.20328 | -43.52256 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29455b52-e254-3452-9aea-8a94a5a5b805 | -7.16079 | -48.89381 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69840598-2be0-3f7f-bf24-d0edc7a3d0c1 | -8.09791 | -48.24141 | 2025-09-11 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 087f7540-2726-3f54-96af-b25d1fe6a184 | -6.24767 | -43.41786 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 482dd54e-e162-3b91-9fa5-86288d77deb8 | -8.6543 | -45.72056 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 6483365c-3019-3f9e-90b3-82dd38d1b6c7 | -8.19839 | -50.11091 | 2025-09-11 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7f86081d-08e8-3296-97fe-f3de3e584339 | -7.50236 | -48.24486 | 2025-09-11 04:44:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e6b01d00-a48b-30b2-967c-f276328c0a1b | -8.04049 | -49.04953 | 2025-09-11 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1614b548-918d-32eb-bf85-b547b6a3017f | -6.83212 | -45.61635 | 2025-09-11 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7e910dd-9ab8-349b-a1b9-041667fdba6d | -6.22182 | -43.49512 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 329ea3c5-39dd-3456-bb3d-9b3c83b4b3cc | -6.20758 | -43.49252 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e30179c-cb22-33f2-b68a-0c511024072c | -8.84226 | -47.26283 | 2025-09-11 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 388acde5-69a2-3bb2-8ec4-03504eb53673 | -8.79291 | -48.08812 | 2025-09-11 04:44:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8421a973-c9a0-308a-bc2c-8579f3a0b72c | -6.80992 | -52.80528 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 44339042-8f30-3a26-a80c-eba10c5da28d | -8.79899 | -48.09774 | 2025-09-11 04:44:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 795c5fae-b2e3-3320-8603-70f7c99db5c6 | -7.73317 | -50.74088 | 2025-09-11 04:44:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acae8673-462d-3bc6-9d2c-80986a9655df | -5.94207 | -45.71654 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c9fab27-e473-36f6-a2a2-57ee48a45403 | -5.54392 | -43.05029 | 2025-09-11 04:44:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00a72d74-4116-3a56-a5dd-27678f4b5d17 | -6.69709 | -44.95745 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55038339-e1d9-38fa-b039-74894113ff01 | -7.20564 | -40.24597 | 2025-09-11 04:44:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 11c2f80b-a4b1-3ec3-ac20-9ff7ce081003 | -6.55879 | -43.14945 | 2025-09-11 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7a893a9-713a-395a-93f7-36198927f189 | -5.78706 | -42.67995 | 2025-09-11 04:44:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a0f9a888-dd63-3121-85e9-3afb2c311423 | -6.85401 | -47.86652 | 2025-09-11 04:44:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00ce38be-714d-3732-a1ea-f8d4c586c5de | -7.73155 | -50.75128 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa9080e0-6182-3763-ae4f-bfa0f5b5b3e6 | -9.0971 | -45.69734 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 01a7476c-b2a3-3440-a022-7812dacfc350 | -7.16511 | -47.61389 | 2025-09-11 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 401886c0-293f-367b-9e51-f0e6ccf63bf8 | -6.28939 | -53.4166 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff48ccd9-e7a1-34e9-83e8-3e38b6d24eac | -5.45582 | -44.00132 | 2025-09-11 04:44:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26a968fb-174e-31f2-892e-9a9f9699feb8 | -7.39427 | -47.38009 | 2025-09-11 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8bcad6d-5320-3502-93d0-297c61c05a11 | -8.75685 | -47.11646 | 2025-09-11 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4cb7deba-a3ad-3d5b-9395-b453ec5c366b | -6.57975 | -47.35096 | 2025-09-11 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30b99d2b-66be-3d28-b038-b3f9a4b8b0c4 | -7.20625 | -40.24146 | 2025-09-11 04:44:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cb4b8ac7-244f-3040-8135-ba1bba9b0acf | -6.1703 | -53.50136 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d88ed17-ef74-313d-aea5-a0b23c95eb7f | -7.38072 | -50.88893 | 2025-09-11 04:44:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af18bf0e-eaae-386a-8ac7-0b160203f2ae | -8.66172 | -45.72943 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 775e82fb-171a-3291-8549-97ba37dd6caa | -5.50377 | -49.21549 | 2025-09-11 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4292cc73-9f75-340e-95ad-d1cfbb99327d | -7.79543 | -47.94079 | 2025-09-11 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9120cf51-d749-38a5-8ab2-da3f59b3a90c | -9.08517 | -47.08498 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77531d5c-7441-38cc-b188-dd4b64b684c7 | -5.54862 | -45.08978 | 2025-09-11 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40888fcd-9c2d-31cb-bed5-2c339b84420b | -4.58163 | -45.61173 | 2025-09-11 04:44:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5141c3d0-ac01-3773-9658-80197757c601 | -9.06728 | -45.70279 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e116b0a1-8c3f-3fc1-90b7-ac5b2a580b7a | -8.01908 | -49.02651 | 2025-09-11 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 23038859-51d0-34f9-94d1-f446a9908504 | -7.50381 | -48.27355 | 2025-09-11 04:44:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1af4ed58-d2ac-31d9-a9aa-d2b31f8c70d7 | -5.6841 | -43.32814 | 2025-09-11 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6ef192d-1bf3-343e-ad53-8d787a47a8cb | -7.53982 | -44.67786 | 2025-09-11 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 698169c1-c390-3b7e-ae3b-4dfdc5032766 | -7.39085 | -47.35166 | 2025-09-11 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78e55126-89a8-3e2e-805a-280922e08388 | -6.3743 | -45.1684 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README96.md)
