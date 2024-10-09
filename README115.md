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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8596e21-c66f-327a-8048-adc8fefb8362 | -4.1712 | -42.99263 | 2024-10-09 04:38:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6c0fe5d5-1397-3689-8e6e-1b38d7e4fcad | -4.16916 | -42.98957 | 2024-10-09 04:38:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1072a916-0453-3901-9c0b-ab74c2eedaa4 | -4.16855 | -42.99357 | 2024-10-09 04:38:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 38483544-7fa6-3821-8a9c-3d424854e8ad | -4.16489 | -42.98897 | 2024-10-09 04:38:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d364ed34-46ed-3de7-82d8-bab60da82c7c | -4.16428 | -42.99292 | 2024-10-09 04:38:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b72b9dcb-515b-348f-87f8-677380e44eae | -9.26709 | -45.78889 | 2024-10-09 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5d259eb2-fc2f-3371-90c9-fe10ca2d2efc | -9.26325 | -45.78843 | 2024-10-09 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b1d83080-fc6f-31c4-ae39-8266e6c4e34f | -9.18341 | -45.70169 | 2024-10-09 04:38:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 737acd22-5647-3856-91e9-7b88a2b7e7af | -8.75758 | -44.1524 | 2024-10-09 04:38:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f47f6a30-c511-3605-86ce-61e66bbb410d | -8.53976 | -45.465 | 2024-10-09 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56c69a59-31a1-3bc1-bfaf-25223ae54b81 | -8.53941 | -45.4631 | 2024-10-09 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45f5d3ee-5f50-366c-a86c-bff7eb001cc1 | -8.42149 | -44.6931 | 2024-10-09 04:38:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c023420f-60c3-3f36-89f5-83af0cde34bc | -8.3385 | -44.10935 | 2024-10-09 04:38:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f92c6e67-ab2d-3c0f-9b57-2204d051c694 | -8.3343 | -44.1087 | 2024-10-09 04:38:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 442b2d3f-d8ac-330d-b280-cff2a06c933f | -8.33064 | -44.10415 | 2024-10-09 04:38:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e2b05db-bdd4-3c3a-9a0c-f655866565e2 | -8.3301 | -44.10804 | 2024-10-09 04:38:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 268716b5-9f38-3c0c-9491-dfd4a4c2ff58 | -8.31872 | -44.09924 | 2024-10-09 04:38:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88950a7f-5f4a-3f19-b045-33112a4dd44d | -8.31454 | -44.09847 | 2024-10-09 04:38:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1720c77a-b9d5-3626-ae25-012013963da0 | -8.30753 | -44.11589 | 2024-10-09 04:38:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dce51df9-bca2-39ce-b1c5-ce18de822714 | -8.30614 | -44.0971 | 2024-10-09 04:38:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4dd5e04b-f6ad-3a18-b363-772ad248f8a7 | -8.30137 | -44.10035 | 2024-10-09 04:38:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85f9c006-4ed5-342c-861f-a586f72d7a78 | -5.89138 | -43.79351 | 2024-10-09 04:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f120daec-1889-3292-aace-e1a179d2b583 | -5.84994 | -43.74588 | 2024-10-09 04:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b2596fd-e87b-31ec-8d09-738d392508e8 | -5.84937 | -43.74966 | 2024-10-09 04:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f431d50c-0d26-39dc-857c-4a994720af98 | -5.83768 | -43.65545 | 2024-10-09 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b498d08b-81c3-37e3-9e0c-389261138570 | -5.81847 | -43.23337 | 2024-10-09 04:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acb2a25e-d207-3be9-b2b8-ebb6aa696f8a | -5.81477 | -43.22863 | 2024-10-09 04:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31377793-f001-372e-834f-342233d1bedf | -5.81416 | -43.23277 | 2024-10-09 04:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be909b8c-a9bf-3c05-8562-488c3c7aafc0 | -5.80777 | -43.97357 | 2024-10-09 04:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d4681ef-9c48-3a82-a162-85f7d4327cda | -5.58711 | -43.25495 | 2024-10-09 04:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5b0a2691-245c-355b-8d90-0b44833d1db5 | -5.58344 | -43.25019 | 2024-10-09 04:38:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 222c1e02-de69-3d87-bc71-1b3057f54338 | -5.58284 | -43.25425 | 2024-10-09 04:38:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 408e5b8f-0083-39b3-a463-bb4a020e4a2a | -5.57857 | -43.25356 | 2024-10-09 04:38:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b2c5952b-7909-326f-a654-fc90fc0b89cc | -5.56482 | -43.69402 | 2024-10-09 04:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e20d513-f454-3915-93ab-ed7f4a69d925 | -6.67467 | -43.95916 | 2024-10-09 04:38:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05ddb478-eb44-39e5-a518-4d201285912f | -6.67412 | -43.96292 | 2024-10-09 04:38:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f87a7f34-81cc-3207-a3aa-732636e91a3a | -6.66557 | -43.4968 | 2024-10-09 04:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5809491b-4122-3b5e-b80a-c3970e7a5b37 | -6.61063 | -43.78072 | 2024-10-09 04:38:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 090ef16a-28b9-3e0c-9408-f22b3a88f68e | -6.60643 | -43.78014 | 2024-10-09 04:38:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f97cd5b7-b280-37e7-9cf1-93d742b1874d | -6.5557 | -43.08532 | 2024-10-09 04:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12d4e31a-0be4-3920-92e3-a64c2696d358 | -6.4856 | -43.34967 | 2024-10-09 04:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed2e2151-dc95-3513-8a69-53b0fc9c893d | -6.48405 | -43.87874 | 2024-10-09 04:38:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5f2c9e82-dfc3-3604-9d67-f288615932ca | -6.4829 | -43.3477 | 2024-10-09 04:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a2f3ead3-84a7-373e-8410-64e94c89d78b | -6.48236 | -43.35154 | 2024-10-09 04:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b3081a70-3ea5-3e9c-85c1-2f4b0a0431fc | -6.48126 | -43.35933 | 2024-10-09 04:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8eac421-1968-38f8-a4ba-96d0123ddb66 | -6.48126 | -43.34925 | 2024-10-09 04:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 434b22f8-add2-3124-814d-c972ae027d2b | -6.47988 | -43.87814 | 2024-10-09 04:38:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b4a115c1-ad6d-3904-a7e0-71ec04840dae | -6.46954 | -43.33916 | 2024-10-09 04:38:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6168a618-321f-3612-a45a-28ccb6a8b7a3 | -6.44442 | -42.93237 | 2024-10-09 04:38:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d4fb308-8813-30ad-acaa-b7998804b54b | -6.41071 | -43.10083 | 2024-10-09 04:38:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8396eed8-a354-3d92-b574-2b1e6f401010 | -6.41013 | -43.10253 | 2024-10-09 04:38:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a648fb0b-59d2-3c51-8e6b-568a8862159f | -6.31271 | -43.37407 | 2024-10-09 04:38:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4665cf3f-e889-3c80-be7e-3a9a53653bb1 | -6.31213 | -43.37808 | 2024-10-09 04:38:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 51381d13-c750-36c0-85ed-c7019c16a497 | -6.31105 | -43.23275 | 2024-10-09 04:38:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4be931bc-7e1c-3aaa-91a0-83ac35a95c24 | -6.30987 | -43.24096 | 2024-10-09 04:38:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 937ce406-b640-39e1-8640-b58a8511c621 | -6.26929 | -43.76072 | 2024-10-09 04:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44348c1b-1754-32a3-8494-fc7290a24b22 | -6.25222 | -43.87691 | 2024-10-09 04:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 437a4025-2971-3ce2-a7f3-e205a76e3956 | -6.20222 | -43.27617 | 2024-10-09 04:38:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae50d184-3194-3104-95ff-fa2b2385aa38 | -6.19791 | -43.27554 | 2024-10-09 04:38:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7835f81-2648-3c71-abdf-3ee071757d0f | -6.16627 | -43.70319 | 2024-10-09 04:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 46d0c873-8622-3d7a-a2ba-8bbee0d05b52 | -6.16572 | -43.707 | 2024-10-09 04:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8139e83a-b22a-334c-801b-db15ad1b2ded | -6.16516 | -43.7108 | 2024-10-09 04:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96ce7486-6e45-30f6-8fb1-55cb72c38118 | -6.16098 | -43.71015 | 2024-10-09 04:38:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0bea5f3-0fc6-3648-ba7c-80dc745b25ac | -6.1323 | -43.37818 | 2024-10-09 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81bf01f3-e1af-3b81-af43-e22252c29cc2 | -6.12624 | -43.3896 | 2024-10-09 04:38:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 820ad752-7d4c-3daf-9fae-37a2acfc057e | -9.95101 | -50.07405 | 2024-10-09 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f17a76a-114d-33d8-af69-58437a19b75a | -9.92995 | -47.72214 | 2024-10-09 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 332828c8-d632-3eb3-b9d8-53373f47ff0c | -9.92644 | -47.72166 | 2024-10-09 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f00ecc69-5761-3159-ac71-1c6df88fd727 | -9.92294 | -47.72119 | 2024-10-09 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ca296a4-815b-3069-8463-c619a15e89eb | -9.88183 | -48.21471 | 2024-10-09 04:38:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06383c72-0cbe-3595-9f58-13a9ee21235f | -9.86202 | -49.16867 | 2024-10-09 04:38:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26c476cc-cab6-3c8a-b331-25b983b8c078 | -9.77751 | -53.17031 | 2024-10-09 04:38:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99634fb7-d736-3ec3-be78-727dadffcaf4 | -9.77391 | -53.16971 | 2024-10-09 04:38:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03fe5a5a-a3a3-3cf7-8808-9017ed028c19 | -9.76308 | -48.69811 | 2024-10-09 04:38:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 18c7797a-0001-3168-aee4-04aca952a887 | -9.75436 | -53.15351 | 2024-10-09 04:38:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db784dbb-9e5d-3dc7-a6d5-8ad141073f6b | -9.75005 | -53.1571 | 2024-10-09 04:38:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a34cf30-c82e-32ee-b4d7-46fc90dce79e | -9.74644 | -53.15651 | 2024-10-09 04:38:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fce58dd9-aebb-31bd-8821-ae3d140ee5ad | -9.74573 | -53.16068 | 2024-10-09 04:38:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58dd68b7-edd2-301b-8513-ae71af9a148a | -9.73232 | -55.62442 | 2024-10-09 04:38:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6a52e25-0dcd-3dfc-a863-134fa03d7468 | -9.72778 | -53.17905 | 2024-10-09 04:38:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47fdf256-74b8-34d3-a724-266174e6e8c1 | -9.72399 | -48.8845 | 2024-10-09 04:38:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 22baefa1-39c0-32eb-b0f0-8d4be5dbae40 | -9.6692 | -52.23447 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d38ed968-5fa6-35fa-a932-b61d78b6c3bb | -9.66857 | -52.2383 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b32a3260-ad91-3fbf-87f5-f312b7d59915 | -9.66792 | -52.24218 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0544fdb4-06ae-39d7-8dfd-ce25c04c3ed2 | -9.66573 | -52.23392 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f08fcaae-390b-369e-9772-49d1f305f785 | -9.66509 | -52.23777 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5182effa-2abe-364a-a311-592036a631fb | -9.66443 | -52.23467 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad7138a2-5c1b-33b7-a4b6-2b8cf7053c1d | -9.66225 | -52.23338 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7aa99d04-85e3-3d06-a7eb-4d5e6819de3e | -9.61672 | -48.69782 | 2024-10-09 04:38:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9cbfbe6-0423-30ec-b128-43685fe010ef | -9.58626 | -56.47555 | 2024-10-09 04:38:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 22f85563-85ff-3f47-bd37-8c6cd1ca4c95 | -9.5849 | -56.47297 | 2024-10-09 04:38:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a50ca89-8f9a-3a19-ba26-305744418ce2 | -9.58411 | -56.47737 | 2024-10-09 04:38:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3fb0374-8178-33cf-ac75-bec04071d155 | -9.58272 | -50.21947 | 2024-10-09 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5897d142-3b4d-3844-90ad-68887d173c4c | -9.58183 | -56.47477 | 2024-10-09 04:38:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 234ec0be-8817-387c-8473-f36b3028a455 | -9.56665 | -50.23483 | 2024-10-09 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fe59e12-1aaa-3131-ae7c-672c72e6362a | -9.55783 | -51.74431 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7d9f6a1-c7fb-3ace-8b06-392464f220f7 | -9.5321 | -49.11408 | 2024-10-09 04:38:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 23add9ac-eb39-30da-8c50-7f88a326b5a5 | -9.49217 | -50.98192 | 2024-10-09 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45fc63ff-ff86-3b29-a9e5-8bd206362868 | -9.48856 | -56.07788 | 2024-10-09 04:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4c860d69-ebd1-340d-9198-10133c2fc5ef | -9.48783 | -56.08205 | 2024-10-09 04:38:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README116.md)
