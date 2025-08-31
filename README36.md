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
| 0e2bfa78-93c4-370f-9f84-cb6173d87155 | -8.35159 | -52.53494 | 2025-08-31 04:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f572aa1f-6d8c-3678-a258-034744186e58 | -7.97686 | -46.41484 | 2025-08-31 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01aa7e41-3f83-37b0-b0ac-ad07f134a0ec | -8.88768 | -45.08912 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a01fc4ee-07d9-3157-b3e4-a92ebb397eb8 | -8.39255 | -48.27157 | 2025-08-31 04:27:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 133f23a6-0513-33a0-978a-d3d0692a88a6 | -9.25337 | -47.06919 | 2025-08-31 04:27:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2538a1c1-8184-3aec-a7fc-4bebc9cfa21f | -7.71864 | -50.26877 | 2025-08-31 04:27:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 20b5793b-cd25-3c25-9115-08d47c04d39c | -7.6377 | -42.6561 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| e22c69e8-e38c-3f8e-a29c-57572c30ef99 | -6.53285 | -42.96407 | 2025-08-31 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 246cb801-f017-383e-b180-3f7c842e73a7 | -6.47898 | -44.40226 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e61073a8-5fb9-3baf-94a6-fef6c2b88014 | -6.16797 | -44.13514 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32884a97-afc2-349a-9caf-d9805433cbf3 | -7.18539 | -43.84076 | 2025-08-31 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 721990b2-4bbe-37b8-b8b7-2147bd0e2485 | -8.71632 | -50.3649 | 2025-08-31 04:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3baf1a32-6904-394c-a223-358442faff49 | -7.633 | -42.65778 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 18f9c186-6104-3fb2-968b-9747d0d08d8c | -6.28585 | -43.5314 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87269e53-e635-39a0-86ec-9d3f4c322586 | -6.24473 | -42.41302 | 2025-08-31 04:27:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7efd3e09-9384-3090-850d-dee9ad84cd9d | -5.69128 | -45.95724 | 2025-08-31 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efc2aa50-2634-375c-9a3d-7e97972ec4bc | -6.0148 | -42.79436 | 2025-08-31 04:27:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bd96b1e3-41ff-3391-9ef7-8563158219de | -9.25116 | -47.06166 | 2025-08-31 04:27:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c672b758-c02b-35da-b126-61b48455484d | -8.8911 | -45.08961 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2ebeeb1-6ced-31c1-a169-799da621d465 | -6.17775 | -44.14035 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8936d760-10cf-364d-ad01-e8fda59d5f00 | -5.46413 | -42.57548 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8b78e0b7-d959-3489-aa7e-7ac7e90a627b | -7.40992 | -47.45182 | 2025-08-31 04:27:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f60d2b1-8b3c-3c3e-a7a4-c2d827eab69d | -8.46447 | -43.62811 | 2025-08-31 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad8866b0-423d-32ec-845b-c9215ec4f9a1 | -5.5302 | -36.85139 | 2025-08-31 04:27:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| eaa7a0de-dc62-31c7-b920-fea439274422 | -7.44707 | -44.81865 | 2025-08-31 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b53367b0-d8f4-36f2-9299-0a9992d2fc81 | -4.27462 | -48.64172 | 2025-08-31 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a46921f5-5f13-3b25-b3d3-3d92682f0ffe | -6.17378 | -43.3184 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1153bcc6-7aa5-3ca1-9220-f14e431751f2 | -6.24628 | -43.38613 | 2025-08-31 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 401687f2-ba4a-37fc-8e93-9a2e7d18a99d | -6.1375 | -43.31709 | 2025-08-31 04:27:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bd153092-d4fa-3865-9ffd-0461d25d32fd | -7.97353 | -46.41431 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad75526e-9802-3223-babf-89c76b85a98d | -7.63745 | -42.65376 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f881e1c3-dcc3-329c-bd82-7bec86eacf29 | -7.62548 | -42.65667 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d87f101c-0f92-31bc-baae-cbf23b3c074f | -6.22977 | -42.41074 | 2025-08-31 04:27:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 98feea92-4de4-3673-86c3-602806886a79 | -6.95669 | -44.33218 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3d2e406-b038-304e-ac16-5c34a409ebbd | -7.7097 | -50.2763 | 2025-08-31 04:27:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0bf62732-5969-3794-876b-1b78d45372e6 | -8.86533 | -45.75183 | 2025-08-31 04:27:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 592d2daf-0d1c-3194-b965-f2c22634a199 | -6.86624 | -45.14767 | 2025-08-31 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 640de494-03e1-328d-a809-378ef7a85c57 | -6.24226 | -41.82167 | 2025-08-31 04:27:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fa86dab6-aaf5-3ffc-847d-f517acb72e81 | -8.84139 | -47.48885 | 2025-08-31 04:27:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ff7bb94-b0fd-383b-aaf0-f6f87143b504 | -7.09535 | -49.92564 | 2025-08-31 04:27:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb1f8144-2b75-3caa-9ea8-47c72c908c08 | -5.48605 | -44.39528 | 2025-08-31 04:27:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ab67aa9e-d3dd-3fe8-99e9-ddb71419997a | -4.26818 | -40.9373 | 2025-08-31 04:27:00 | NPP-375D | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0eefdc01-31db-3b23-814e-875d3fb96ed4 | -7.75339 | -47.44133 | 2025-08-31 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b251737-3edb-347b-9220-c94b3bfdca20 | -8.41787 | -47.34824 | 2025-08-31 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49ce0f9d-a182-3a7e-af49-e7822abb055f | -7.22734 | -44.0654 | 2025-08-31 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64ab624d-2f64-3a84-a46d-e700536d3bf7 | -9.2506 | -47.06516 | 2025-08-31 04:27:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 05be5cca-b7cb-3f79-8a1d-b11b42c6a5ba | -6.64065 | -44.25456 | 2025-08-31 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7189ceb-b7cb-3b91-b294-468d7c9c52f1 | -6.2817 | -43.53486 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a76cf423-bec1-37c5-9573-39e889ea16c2 | -6.26302 | -46.01886 | 2025-08-31 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f25fec9c-054c-3a8a-a43b-49376974109c | -7.95914 | -46.41917 | 2025-08-31 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c51c0cd-9d86-3575-8108-3a66a242fd9c | -6.17255 | -44.12828 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 870e9617-8c81-33f1-8abc-c8116b7c209f | -8.33143 | -47.41747 | 2025-08-31 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f9a1942-aab2-3bcf-a495-ff0d06b2f297 | -3.20493 | -52.24899 | 2025-08-31 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| debdccd7-17da-3664-98cc-d7e104ad0451 | -7.44762 | -44.81504 | 2025-08-31 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e9b82f7-6451-3553-9c60-e85081f1e4f8 | -6.17254 | -44.17408 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a86c886-37f0-343a-96d8-4c8c91880253 | -6.77173 | -44.63118 | 2025-08-31 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ee3f1b65-1a37-3902-8ba1-38b6e6a77f59 | -7.23132 | -44.22636 | 2025-08-31 04:27:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97c3d80a-e957-3c94-b3c2-e9a2e2b7a04b | -7.65733 | -42.70532 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bf4e8740-a8cf-3ca2-b241-71348d93085f | -9.44708 | -40.68196 | 2025-08-31 04:27:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c7150143-e750-3663-9cc6-212b43e007c1 | -4.31085 | -48.08194 | 2025-08-31 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| caba5d48-cc49-337e-9487-a99b0061c85d | -8.88676 | -45.09705 | 2025-08-31 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c21957b6-82ba-30ef-98d1-3f816b467117 | -8.28988 | -46.31386 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 266fbe90-aead-3eaf-a9f5-571b7605ef22 | -6.58259 | -43.63802 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e33066e-771a-39eb-9e7f-413accc8bef4 | -5.4787 | -44.42022 | 2025-08-31 04:27:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 277f9750-5fe8-3d80-aba2-354f20bdb883 | -6.49024 | -43.56051 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dcee965c-3401-38dd-88de-25e025a71dec | -4.62037 | -43.51503 | 2025-08-31 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b55a9a6d-dfe7-3d33-83ae-1d35123d80ed | -6.10407 | -43.1887 | 2025-08-31 04:27:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a3329732-df4e-3685-80a7-9497b99ac68c | -7.97076 | -46.4103 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54c5c310-b3d6-374e-923c-e4a685df601f | -6.44754 | -42.39757 | 2025-08-31 04:27:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 83c0d61d-22c0-3896-ad63-5108f2db3191 | -8.03831 | -45.41608 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42416f02-d785-3ef5-ac17-1272d10ae34b | -7.73604 | -50.26116 | 2025-08-31 04:27:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 92c4542c-ae03-301c-9b89-bef1ce61c7ff | -6.57888 | -43.68573 | 2025-08-31 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b45ec635-0036-3194-88e9-5491bbb545e7 | -6.70979 | -51.41879 | 2025-08-31 04:27:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 9f11c2e8-f3a2-3c59-a524-d785680e5207 | -8.60868 | -47.1878 | 2025-08-31 04:27:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f73f4dba-0435-3ac1-8ade-73eb4b112e56 | -8.91385 | -40.43887 | 2025-08-31 04:27:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.3 |
| d510f37a-8bd3-35cf-be12-a8263de91c64 | -4.31022 | -48.08579 | 2025-08-31 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8a673a4-7ccf-3997-ab67-f94f676e0ac6 | -3.20797 | -52.25887 | 2025-08-31 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc32c9ff-966d-3e01-8a67-fd0caa6ba999 | -6.11183 | -43.28142 | 2025-08-31 04:27:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f873df0a-cab7-3b86-8f3f-192195b36851 | -6.53866 | -44.44532 | 2025-08-31 04:27:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fcc4c3f-21ac-39b2-9eba-5c49305d3d35 | -8.28601 | -46.31682 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de2d450d-6979-375d-a225-7091e91c534f | -7.77458 | -45.45538 | 2025-08-31 04:27:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3f78730-8891-3c88-a9e5-51f7562ffaa1 | -7.20343 | -45.43964 | 2025-08-31 04:27:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ce87606-2e70-3ba2-ad01-e04b4b316198 | -7.96191 | -46.42318 | 2025-08-31 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b2bbbed-33e6-384c-aa40-7cf0d9f2bfe1 | -4.17142 | -42.02908 | 2025-08-31 04:27:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5f619417-9954-31cb-9e6a-9d7213aea5bc | -4.74099 | -44.44799 | 2025-08-31 04:27:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 9ed0048d-caf6-330a-ae64-c0e73507d22d | -8.78084 | -46.5927 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d1ee9f0-7c01-3add-9b8e-18930b405877 | -6.96644 | -44.31445 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ffd8fa9-b0af-305b-ac9e-1492ad6fe956 | -7.09827 | -44.31862 | 2025-08-31 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1bcfc6ae-a8e5-3e5b-85ab-b146d51b43d9 | -6.20079 | -42.75024 | 2025-08-31 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c70592dd-07a7-3c1f-8cda-38237e1c1610 | -4.59743 | -40.61501 | 2025-08-31 04:27:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e43766c9-dce2-3a64-a6f7-8007b58b76bc | -4.27103 | -48.64115 | 2025-08-31 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 563b78a8-4b54-3c13-994c-7fed6009ce19 | -6.11213 | -43.32684 | 2025-08-31 04:27:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03e123e0-ce68-33a2-b67b-e4057f98f603 | -5.85199 | -44.84573 | 2025-08-31 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 346030cf-1107-36eb-a2eb-7b75684a1a58 | -7.73135 | -50.26164 | 2025-08-31 04:27:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 53768fd4-40e4-33ef-9ead-2f2c2493aa44 | -8.34649 | -47.40903 | 2025-08-31 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5d6c089-816f-33a5-9678-08e63dc9960f | -6.18004 | -44.1255 | 2025-08-31 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5aa1a3d2-a666-30e7-aac0-224c4a43b6d3 | -6.01897 | -42.71632 | 2025-08-31 04:27:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b1af4f69-c321-33e4-80b1-a0ea85cefddd | -8.29043 | -46.31037 | 2025-08-31 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fbf3fe76-3d1b-3859-968d-653019871936 | -7.73229 | -50.26056 | 2025-08-31 04:27:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 98b8cd59-4da9-3fc3-8575-f86ae1e251de | -6.24918 | -42.40891 | 2025-08-31 04:27:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README37.md)
