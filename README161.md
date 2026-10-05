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

## Dados Diários - Página 161

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d167ced-14d5-3e59-86ed-44e8fccd7211 | -6.03731 | -43.39165 | 2026-10-05 18:19:00 | AQUA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 1c2c526f-44e4-3c0a-8c1f-cd098ea9513e | -9.59712 | -43.32975 | 2026-10-05 18:19:00 | AQUA_M-T | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 8479daec-7d6b-33da-96e2-82c051969372 | -6.42708 | -43.46257 | 2026-10-05 18:19:00 | AQUA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 186.2 |
| 435b042a-604d-3a02-b56a-b61aacf4296a | -8.52945 | -39.54892 | 2026-10-05 18:19:00 | AQUA_M-T | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 13.1 |
| de583051-31d4-39b6-a934-c8ecb3670e65 | -11.12 | -45.9701 | 2026-10-05 18:19:00 | AQUA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 450.0 |
| e00ba86c-4442-304e-a5a6-1967346f3eb9 | -5.97383 | -41.37542 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2005.2 |
| a2a63655-f210-3b6a-bf7a-3dc78fa4896b | -6.43596 | -43.47289 | 2026-10-05 18:19:00 | AQUA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 179.2 |
| 6e04f313-e825-39b8-8c6e-161d68ab6c0d | -7.45713 | -40.43124 | 2026-10-05 18:19:00 | AQUA_M-T | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 33.2 |
| 2c6f5165-1999-3896-9df0-8e4dd6979d29 | -6.24322 | -40.60245 | 2026-10-05 18:19:00 | AQUA_M-T | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 22f3c850-9cd2-36a4-ac15-d0df52327dd3 | -4.94003 | -42.72647 | 2026-10-05 18:19:00 | AQUA_M-T | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7f22662b-1cf7-307c-a4c1-4790b51216a2 | -6.11734 | -38.3288 | 2026-10-05 18:19:00 | AQUA_M-T | ENCANTO | RIO GRANDE DO NORTE | Brasil | 2403301 | 24 | 33 | nan | nan | nan | Caatinga | 20.6 |
| 75fe876f-70d7-3329-b929-264a28ca8c9d | -4.8035 | -42.14996 | 2026-10-05 18:19:00 | AQUA_M-T | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 157.1 |
| 77a0ad0f-a7f0-3ff7-b7e5-7d8696a50f1c | -3.89898 | -38.38729 | 2026-10-05 18:19:00 | AQUA_M-T | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 3b463712-0c7b-3611-ab85-be56f5618e0b | -5.72363 | -40.12598 | 2026-10-05 18:19:00 | AQUA_M-T | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 83bfd4a8-e726-3419-9532-05d04f96299b | -11.12106 | -45.94225 | 2026-10-05 18:19:00 | AQUA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 315.8 |
| 6c2a0b1b-ef1f-36b9-ae4a-ca7356a7b8c1 | -5.40839 | -39.10098 | 2026-10-05 18:19:00 | AQUA_M-T | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 29.5 |
| 7a90c5c7-12eb-3b06-8640-e4fc185e3935 | -3.48518 | -41.54318 | 2026-10-05 18:19:00 | AQUA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| d0c2dc21-8e3c-31b9-93fa-34016a0180ce | -11.69285 | -43.65335 | 2026-10-05 18:19:00 | AQUA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.4 |
| c1e9821c-6736-378d-98f7-bb4c4b5c8ab8 | -6.69604 | -45.21701 | 2026-10-05 18:19:00 | AQUA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 846522e3-38a7-3038-8bcf-890dfb41b1b2 | -4.72204 | -45.21728 | 2026-10-05 18:19:00 | AQUA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| b6ac2056-2ec7-3616-b9a1-4f2311118dde | -4.8138 | -42.14848 | 2026-10-05 18:19:00 | AQUA_M-T | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 50.8 |
| c0e8fed5-f3d4-3455-85a1-2d417745befd | -4.91119 | -41.75425 | 2026-10-05 18:19:00 | AQUA_M-T | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 38475326-bd8f-337c-9a64-cdc4aaa9ef82 | -5.46556 | -43.75958 | 2026-10-05 18:19:00 | AQUA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 34c4cb6a-9956-321a-8b1c-105084eb6cd1 | -6.6082 | -37.89678 | 2026-10-05 18:19:00 | AQUA_M-T | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 31.2 |
| a4a6b56d-97b7-393f-a5b9-30088acd2544 | -5.78837 | -43.26273 | 2026-10-05 18:19:00 | AQUA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 6a462bc9-f0c0-392a-8239-2e8d442824d6 | -6.70538 | -45.28695 | 2026-10-05 18:19:00 | AQUA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 176f0331-1a60-3f2a-8b50-efd29038a239 | -6.37239 | -40.79017 | 2026-10-05 18:19:00 | AQUA_M-T | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| b83ae5f3-e170-3ea1-805b-03f2e1a04d11 | -11.21734 | -40.88589 | 2026-10-05 18:19:00 | AQUA_M-T | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| a599bd24-6133-3289-a826-2398d97bd04d | -11.25929 | -43.531 | 2026-10-05 18:19:00 | AQUA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| dad303fc-53c9-32d9-9363-58f8ffbe89dd | -4.51645 | -42.07166 | 2026-10-05 18:19:00 | AQUA_M-T | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| e8ae90cd-867b-37a0-939d-f95d63a342e0 | -5.95087 | -41.36083 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 67.3 |
| b8a65c5c-81df-3817-a666-b309af7df415 | -8.78444 | -47.56355 | 2026-10-05 18:19:00 | AQUA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| f6cbe190-c2e5-3c88-8653-75e3d1bf21a4 | -8.53864 | -39.54756 | 2026-10-05 18:19:00 | AQUA_M-T | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 7.6 |
| d8d29fe3-264f-37a3-a653-cc017e8048e2 | -6.4294 | -43.47886 | 2026-10-05 18:19:00 | AQUA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 166.3 |
| 497896f8-dd30-3fb6-ba5b-8c4ec968edfd | -6.70218 | -45.26294 | 2026-10-05 18:19:00 | AQUA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1081.6 |
| 877aa7ef-930e-3c47-af19-04f03ea65cb0 | -5.17051 | -36.86679 | 2026-10-05 18:19:00 | AQUA_M-T | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 844a823b-94b5-3048-b153-301963b07e89 | -6.89484 | -43.69834 | 2026-10-05 18:19:00 | AQUA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 3ff489ee-6679-3223-b085-b9585a94a099 | -6.21906 | -41.58952 | 2026-10-05 18:19:00 | AQUA_M-T | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| acab6bbb-abc4-3329-9857-e9331f67db4f | -5.47025 | -41.23223 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 29.4 |
| 80506c7b-257f-32de-8971-81cc8995054b | -6.62568 | -37.89413 | 2026-10-05 18:19:00 | AQUA_M-T | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 50.1 |
| fb6b92b2-b389-364d-813d-0296db56d9e4 | -6.11862 | -38.33755 | 2026-10-05 18:19:00 | AQUA_M-T | ENCANTO | RIO GRANDE DO NORTE | Brasil | 2403301 | 24 | 33 | nan | nan | nan | Caatinga | 42.0 |
| 1060d4ce-c5f5-3734-b45a-e3af6bf5cc64 | -4.46126 | -39.00399 | 2026-10-05 18:19:00 | AQUA_M-T | ARATUBA | CEARÁ | Brasil | 2301406 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 0302fd12-129d-3e3c-98e0-4df9af7e16f5 | -6.71917 | -45.28547 | 2026-10-05 18:19:00 | AQUA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 302.0 |
| 30472634-deb1-306b-9046-61c6abc6bb15 | -6.91412 | -43.66037 | 2026-10-05 18:19:00 | AQUA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 556d1d33-0195-3944-bb4c-3f33e30bb00a | -3.83289 | -41.80763 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 56.0 |
| af46259b-7597-314a-b42d-05bf79e3ad46 | -5.9524 | -41.36686 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 121.2 |
| a28f7c97-41d7-32d8-ac6d-5c6af38ecbca | -7.86129 | -44.14941 | 2026-10-05 18:19:00 | AQUA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 225.7 |
| 4c9a453e-f889-3397-b154-e4dc182d2652 | -5.97492 | -43.36794 | 2026-10-05 18:19:00 | AQUA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 38.1 |
| 2d5bb63a-33fa-33ae-872a-0d5fddc159d9 | -7.22509 | -37.06985 | 2026-10-05 18:19:00 | AQUA_M-T | CACIMBAS | PARAÍBA | Brasil | 2503555 | 25 | 33 | nan | nan | nan | Caatinga | 13.0 |
| e5833638-8aa5-3680-8fe4-dfb4da0cc4d8 | -6.74236 | -39.12471 | 2026-10-05 18:19:00 | AQUA_M-T | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 581de25f-fc37-324e-896a-ec25c91d2c91 | -5.88663 | -43.45827 | 2026-10-05 18:19:00 | AQUA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| be3bf82e-c53a-3981-8fad-92ce6f2113e9 | -3.38123 | -42.51543 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 68226aca-0102-32ae-bf0c-7759e554266d | -6.75798 | -35.00441 | 2026-10-05 18:19:00 | AQUA_M-T | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 12575444-2e5d-3c01-8886-e40b31d221d2 | -3.91982 | -43.93578 | 2026-10-05 18:19:00 | AQUA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| e24a991c-7c91-327a-bfc3-647ab1596126 | -6.80601 | -41.24746 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 62fcf749-368e-3bf1-b7ca-5fab0caf84db | -10.06974 | -43.12053 | 2026-10-05 18:19:00 | AQUA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 43e3e243-adc2-3457-8762-2003d6268ac4 | -4.75481 | -42.60693 | 2026-10-05 18:19:00 | AQUA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 45.0 |
| 5b08afee-900d-3805-9953-6ded97700b54 | -8.59703 | -37.14936 | 2026-10-05 18:19:00 | AQUA_M-T | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 436442a5-1b5f-3123-81ca-aab86e3af729 | -6.55199 | -41.33805 | 2026-10-05 18:19:00 | AQUA_M-T | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 54.2 |
| d5d789ea-f4ee-3288-8dbd-4920595142f9 | -5.93933 | -41.35098 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 6fceb565-54bc-38d8-9df8-7af3165b481c | -3.74436 | -39.54485 | 2026-10-05 18:19:00 | AQUA_M-T | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 11.1 |
| afdba201-1536-3015-aa44-66a2479028b7 | -6.49502 | -43.22678 | 2026-10-05 18:19:00 | AQUA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| ea139449-7f61-35af-a8b3-a7fc85463261 | -6.8134 | -39.301 | 2026-10-05 18:19:00 | AQUA_M-T | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 55.9 |
| 4c122538-122c-35f1-8f97-3d76da8fd285 | -3.53769 | -39.8909 | 2026-10-05 18:19:00 | AQUA_M-T | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 808098ef-c84e-38df-837f-c913c985ae41 | -5.8963 | -43.46815 | 2026-10-05 18:19:00 | AQUA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 376db13d-d06b-397b-a846-45a4dc295408 | -6.04773 | -39.30383 | 2026-10-05 18:19:00 | AQUA_M-T | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 1a6ebabc-b91d-3573-b959-dceeaeb147fc | -2.71713 | -43.90604 | 2026-10-05 18:19:00 | AQUA_M-T | ICATU | MARANHÃO | Brasil | 2105104 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 918464c9-f397-3350-9ec5-4fe249cc0507 | -8.79788 | -47.56586 | 2026-10-05 18:19:00 | AQUA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 46d4e2d6-5d89-32b0-9705-514b1a2f1eea | -5.95911 | -41.34256 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| d9da6f57-1106-3ece-b474-6b146c89226d | -6.68314 | -40.38161 | 2026-10-05 18:19:00 | AQUA_M-T | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 02a835f6-4ae9-37c5-8ee0-ab1fb9f5b83d | -6.90969 | -43.67153 | 2026-10-05 18:19:00 | AQUA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 471007a8-607b-383a-b921-cb34454316b7 | -6.14639 | -38.4049 | 2026-10-05 18:19:00 | AQUA_M-T | DOUTOR SEVERIANO | RIO GRANDE DO NORTE | Brasil | 2403202 | 24 | 33 | nan | nan | nan | Caatinga | 12.5 |
| c6f21730-eec3-3cc7-a581-13ee6a11e654 | -5.53309 | -41.02736 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 52.0 |
| 48d6ce9d-e509-338e-bf60-562196ddc73d | -7.10175 | -42.54715 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 55.1 |
| 6b6a30e0-c7bb-3cdc-8ddb-85016aeb9a26 | -7.03551 | -35.19653 | 2026-10-05 18:19:00 | AQUA_M-T | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| 45eaf543-8652-3e3c-b595-7ff3e1947cd2 | -8.31401 | -36.99414 | 2026-10-05 18:19:00 | AQUA_M-T | ARCOVERDE | PERNAMBUCO | Brasil | 2601201 | 26 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 233a6c3a-4870-3ceb-9415-41affafac2d8 | -3.90366 | -41.58514 | 2026-10-05 18:19:00 | AQUA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 76.4 |
| 22effb15-623d-3e75-8226-665c241cdc0f | -5.47404 | -41.23658 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| 4f57e5b5-6bf8-3a36-8984-3a3e3381eb85 | -4.38815 | -37.88358 | 2026-10-05 18:19:00 | AQUA_M-T | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 10.8 |
| e959d433-0b2b-319a-9d90-1ef02f6687d1 | -5.45885 | -43.76744 | 2026-10-05 18:19:00 | AQUA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 4b9c80f1-53d2-3f61-b3c2-f323dd8e551c | -7.10193 | -38.23054 | 2026-10-05 18:19:00 | AQUA_M-T | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 326.5 |
| 2c369ed7-69c1-3ae1-9225-87df4eab3331 | -5.92086 | -43.22317 | 2026-10-05 18:19:00 | AQUA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 29.5 |
| 1c601e52-8368-3f26-8d7f-d79e61476fca | -10.33742 | -39.48904 | 2026-10-05 18:19:00 | AQUA_M-T | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 45.9 |
| e17f689e-8650-3368-b990-48e1a1185680 | -6.95989 | -35.78934 | 2026-10-05 18:19:00 | AQUA_M-T | REMÍGIO | PARAÍBA | Brasil | 2512705 | 25 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 9e313145-1ddb-3d5d-9dee-9f384dc4f7bf | -6.91655 | -43.67762 | 2026-10-05 18:19:00 | AQUA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 35.2 |
| a30072ca-e410-3347-9da2-07da6e839dee | -11.46606 | -43.40329 | 2026-10-05 18:19:00 | AQUA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 59f37eb6-92cb-3ae1-9b63-36ee21c2a982 | -4.73244 | -45.20922 | 2026-10-05 18:19:00 | AQUA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| ec974697-0f29-3ee6-963c-efab4ea5c953 | -5.13062 | -48.13376 | 2026-10-05 18:19:00 | AQUA_M-T | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 830784e5-1273-3cef-93fa-7be9a5292b1a | -4.79745 | -42.60073 | 2026-10-05 18:19:00 | AQUA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 8a9a73fb-5ea8-341e-89b7-e52ba8b6e437 | -6.72955 | -44.29529 | 2026-10-05 18:19:00 | AQUA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 208.3 |
| 4c4a7697-ec23-38b6-8bbb-9f39870408bb | -6.73943 | -44.28016 | 2026-10-05 18:19:00 | AQUA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 44.6 |
| ea1c6083-aa9b-376f-839d-4947d7fa0606 | -8.01326 | -42.91437 | 2026-10-05 18:19:00 | AQUA_M-T | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 98.1 |
| 775107e6-12dc-3014-af17-46d284df61cc | -4.86028 | -39.59193 | 2026-10-05 18:19:00 | AQUA_M-T | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 52281e72-5bd9-39af-b536-e8d877753675 | -5.98163 | -44.86469 | 2026-10-05 18:19:00 | AQUA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 8ba6045e-c542-3cbb-ad0e-40f0b94417aa | -9.85834 | -44.82908 | 2026-10-05 18:19:00 | AQUA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 223.7 |
| e4146b47-fe7e-3987-ba5d-5acc30f17ece | -7.48493 | -39.47228 | 2026-10-05 18:19:00 | AQUA_M-T | MOREILÂNDIA | PERNAMBUCO | Brasil | 2614303 | 26 | 33 | nan | nan | nan | Caatinga | 14.1 |
| c93cded9-4bbc-31b9-b276-eb1faae56166 | -6.92863 | -43.67601 | 2026-10-05 18:19:00 | AQUA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| e7dc1306-5bee-36bc-b2af-df320fe604d6 | -4.56436 | -43.71371 | 2026-10-05 18:19:00 | AQUA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 737a2263-0117-3ee2-963c-10f8e05472f2 | -7.46665 | -40.42988 | 2026-10-05 18:19:00 | AQUA_M-T | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 41.2 |
| a56afae4-b38d-3f7a-9d14-d0aa20e84e82 | -5.49513 | -44.65717 | 2026-10-05 18:19:00 | AQUA_M-T | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 341.5 |


[Clique aqui para ver as próximas entradas](README162.md)
