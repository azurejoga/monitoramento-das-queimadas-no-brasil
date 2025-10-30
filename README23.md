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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85972cb9-5e90-384f-9e14-7a2bb0b9c931 | -6.13404 | -41.70695 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7087d7c1-c5a5-315d-bf94-4e5332f1e0a9 | -5.63999 | -41.0883 | 2025-10-30 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e80456f0-d5a7-3273-88a0-d37e81e3241f | -2.87841 | -40.41719 | 2025-10-30 04:04:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1ce3484f-bd6a-305a-a02e-c2f00dafa6bc | -6.1059 | -41.72913 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cde3a279-fa71-35a0-a9c5-452a522621d8 | -7.01551 | -46.43669 | 2025-10-30 04:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0d281ee-c72e-34c6-90dd-557d2c495224 | -6.53809 | -43.56839 | 2025-10-30 04:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c095ae13-3ce1-3c0f-beda-800c7f962c26 | -7.78147 | -46.48591 | 2025-10-30 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c270a19-c02c-3a17-b86a-1853f377dacd | -5.1135 | -42.6244 | 2025-10-30 04:04:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3bd693c-90f6-3a08-bddf-11fbe8118d14 | -6.9707 | -39.09737 | 2025-10-30 04:04:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 200a927d-ede9-303a-9b6f-3ae46b026cd9 | -6.42842 | -42.32591 | 2025-10-30 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f316ca3c-c1d0-390b-938b-7d19aa0b5159 | -7.62309 | -43.57723 | 2025-10-30 04:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c05a8554-9ab2-3840-b4df-16d4cf951979 | -5.06252 | -45.3238 | 2025-10-30 04:04:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 893b6cb5-b4e6-3130-a8f8-436a6b30eb1d | -6.17499 | -41.60418 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bfc50b95-d6df-3213-86b8-3c9db26f2ad1 | -4.82698 | -42.73714 | 2025-10-30 04:04:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 85e982ec-2df7-3248-bfb8-6ac3daec5b57 | -4.25665 | -43.7165 | 2025-10-30 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| d7040018-1c70-3c1f-817d-fc80980bf0b5 | -5.40101 | -49.42316 | 2025-10-30 04:04:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33bb8898-8095-33a7-8a56-1ce4953a44f6 | -7.12131 | -47.01619 | 2025-10-30 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bfe963e-ddd1-3d76-bb0d-88decfd7c3c7 | -4.48362 | -43.43793 | 2025-10-30 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3fe26cd5-53ea-32a3-8bc5-7c2b8eccb696 | -7.93024 | -45.50261 | 2025-10-30 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 224a1a17-4841-3618-a03a-dcfb2bcd3bf2 | -7.30981 | -46.7942 | 2025-10-30 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2636adcc-88d2-37a8-953c-c9d2872d1ce9 | -7.27908 | -46.06252 | 2025-10-30 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 13399f10-60d7-3ec3-911b-8cf1749bc950 | -7.31091 | -44.98373 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ad4bfb4e-3080-333b-bb83-7c2da0d1416f | -7.38707 | -42.46862 | 2025-10-30 04:04:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 60ce5c88-9c23-3ea3-812f-6a27d701e255 | -4.78359 | -43.42281 | 2025-10-30 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 745d7f68-93f5-37b3-8708-bf28f4611f27 | -4.84334 | -45.85359 | 2025-10-30 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c3a1b225-04c3-33cf-b874-c5c18045c176 | -7.28374 | -46.78469 | 2025-10-30 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9c4c0c8-fad4-308e-ad1c-a3db24a1732b | -4.15311 | -43.88543 | 2025-10-30 04:04:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 72f6e205-fbe0-3032-b144-a634517bafcf | -5.7999 | -40.80765 | 2025-10-30 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 096102fe-da58-33ad-b47d-f703e59ba60b | -7.81336 | -46.40514 | 2025-10-30 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1fdfb216-1bce-3420-aa3e-7d36fcb55370 | -6.133 | -41.86747 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 265dbdea-4f18-3643-88cd-88b6c7cfd5fd | -6.14667 | -41.58449 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5311fa4c-ce50-38be-817d-beb16d2dd53a | -7.05421 | -46.26554 | 2025-10-30 04:04:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b96e195-3d01-3a61-8ae0-96251f0c8838 | -6.13024 | -41.578 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ae56a427-b8b0-3cd7-9d86-269a4db85c71 | -2.66471 | -47.87335 | 2025-10-30 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4177d72-64ef-3fb3-8c8a-019b180efb0b | -3.80348 | -43.89217 | 2025-10-30 04:04:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0b9e2aa-09a2-3eed-a9d5-8ea57a59a8e9 | -6.52007 | -46.90865 | 2025-10-30 04:04:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 27e23798-4f71-3411-b788-50ec23ee5063 | -5.5829 | -46.47022 | 2025-10-30 04:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9217cb85-731d-3632-9d99-2f0d825ad748 | -6.13824 | -41.57174 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f14c2ab2-7a19-3b8a-ad3a-04a60b5211f4 | -6.56853 | -41.59096 | 2025-10-30 04:04:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5d819b3b-12bf-33db-bbf8-273d62db6d59 | -6.29334 | -42.88218 | 2025-10-30 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 78f35cca-0a40-3fed-bb50-7f5c43204682 | -6.11022 | -42.4404 | 2025-10-30 04:04:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0764ecd2-3fd0-34a0-b7f7-9b3fc89d7f48 | -3.97667 | -38.73283 | 2025-10-30 04:04:00 | NPP-375D | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3237a9f2-207a-3e0c-a5f6-ce040e1c57c6 | -7.29582 | -45.66557 | 2025-10-30 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22f8c111-2b0d-3014-abf0-cc46647423ac | -7.79316 | -46.41865 | 2025-10-30 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2706cb6f-1edb-3e2d-92c3-3c3832d9a464 | -3.35997 | -44.26678 | 2025-10-30 04:04:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0310c3d2-c34b-30b4-8b9c-2bdac361ae15 | -3.6451 | -39.37599 | 2025-10-30 04:04:00 | NPP-375D | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0816949e-23ec-3f33-bbba-27bb97a35142 | -7.11753 | -45.19535 | 2025-10-30 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8e4c282-dde2-3632-b52d-0c370646b928 | -7.65946 | -43.91572 | 2025-10-30 04:04:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fd7a611c-6a27-326a-b431-12756f0d51c9 | -5.29591 | -45.27172 | 2025-10-30 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7064d357-42cb-39a7-98ec-3553365aa858 | -6.70954 | -38.21695 | 2025-10-30 04:04:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 06315506-bd58-3b55-9fd9-e88344944e64 | -7.47787 | -42.72954 | 2025-10-30 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bea5fa29-36ff-39ba-92c6-870e7a8bd69a | -4.25742 | -43.71174 | 2025-10-30 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 7209e496-fcc4-306b-9860-2c4f342565ed | -4.35409 | -48.19943 | 2025-10-30 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d15fdc30-91f8-30b7-9ec6-2adf34ed33c6 | -7.14858 | -40.24928 | 2025-10-30 04:04:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 500b051a-e047-3e1a-b9d2-2772e3e44c7f | -7.38052 | -47.62761 | 2025-10-30 04:04:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2dd01ad3-2c80-319c-9a9b-f39b5c413cb5 | -3.31712 | -44.14864 | 2025-10-30 04:04:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57b9ce6b-eb58-3ab4-a8e6-d5d22d576dfa | -5.772 | -44.38791 | 2025-10-30 04:04:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88d8de9b-cf7b-33ed-9c69-f11ca6f7aedb | -5.79709 | -40.82518 | 2025-10-30 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d1eee242-a34f-3b57-9ef3-639d3ffb3f6c | -3.95588 | -43.26525 | 2025-10-30 04:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e272fe78-da6c-3588-84ba-4ab7310edc80 | -4.05465 | -44.26568 | 2025-10-30 04:04:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1053c1a2-cb5a-3bfa-8c22-e709d86e85e4 | -5.47457 | -45.00209 | 2025-10-30 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a14a25c-5d73-312b-9a79-3bbc174fb652 | -6.69206 | -38.19596 | 2025-10-30 04:04:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 69d95179-ac02-3ef7-87f6-e2116c327db7 | -7.61651 | -43.57173 | 2025-10-30 04:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 347d4d91-1189-3b34-bdca-c90fd78c424b | -7.80038 | -46.45443 | 2025-10-30 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37068720-7d05-3f60-98ed-cc55d80a8210 | -4.88882 | -45.43858 | 2025-10-30 04:04:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 903abaf8-bd18-36e4-8a5d-e40b7043deb6 | -7.62024 | -43.59437 | 2025-10-30 04:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 867568ed-6c5f-32be-afd9-bf1798a12223 | -6.21694 | -41.82309 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8eb45c85-b35d-3213-a164-c2dd82f133a7 | -3.48203 | -41.41256 | 2025-10-30 04:04:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b2136e3b-a660-3aca-b319-2e1b07d416a9 | -4.34188 | -41.83788 | 2025-10-30 04:04:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 70179d33-843a-3a84-8e9c-d41e33ecd09c | -3.67919 | -47.62729 | 2025-10-30 04:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1790d700-6288-3260-a1d0-e7503372ac7b | -6.13811 | -41.59427 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c625bcf8-29a2-3d7b-bd8a-6a373c386b67 | -4.08576 | -46.93797 | 2025-10-30 04:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed786bf0-36a5-3dbd-a670-50965ba4d970 | -4.25821 | -43.70695 | 2025-10-30 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 049bd8ea-3f45-33ed-b038-2d3aa1cba9cc | -3.23046 | -46.87782 | 2025-10-30 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 465d6af7-9a25-3523-87d6-3dff0e9a0489 | -7.96127 | -45.44389 | 2025-10-30 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4297108b-2268-35e3-9078-bebd23542e0f | -5.70229 | -43.15649 | 2025-10-30 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 4cf48212-9cc4-3400-9168-bcbbb52ccdaf | -3.96287 | -40.61224 | 2025-10-30 04:04:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b67dc3e4-5fd2-3ee8-87bd-2b5bbc98e4bf | -7.07822 | -44.93438 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 10256502-901c-3753-9733-d217ce1c0e62 | -5.63151 | -41.09801 | 2025-10-30 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dbb7fe7e-cbaa-3f20-9580-3f640046f55a | -7.86972 | -44.22927 | 2025-10-30 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08a99c83-b79f-312f-9d37-bee79c84d26a | -7.7881 | -46.42206 | 2025-10-30 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b7973d72-e365-36ac-addd-7602e7ec82d7 | -3.82913 | -51.22072 | 2025-10-30 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7e16d5b-51f2-3cf1-becf-d5edba9f642b | -4.67436 | -43.26463 | 2025-10-30 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| edf11327-a719-36df-b1c0-44c3fda34e10 | -5.9296 | -47.32134 | 2025-10-30 04:04:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6de2cc56-080a-330c-a9fe-c417190e06a3 | -6.10255 | -42.44316 | 2025-10-30 04:04:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| bd6987b4-ea80-3aac-85f1-9b2c0cb52ba9 | -6.13076 | -41.8594 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fbc9a483-1c2f-3894-9bb3-b3e94a9ec461 | -2.5773 | -45.79899 | 2025-10-30 04:04:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 0d651133-dcc5-3a3c-aab3-0659a19df075 | -7.30156 | -44.96634 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8623fed-84ac-3b9b-8d6f-26b9355b776c | -6.69516 | -39.69013 | 2025-10-30 04:04:00 | NPP-375D | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1fb88ac6-4669-38fd-ae65-381e3d6879ed | -6.52994 | -43.57167 | 2025-10-30 04:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 24ab0611-1434-3df2-a6a0-aa308b95556a | -6.65044 | -47.28917 | 2025-10-30 04:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab1eefa4-03e9-3a41-a643-7ce227c52d52 | -7.87197 | -44.23902 | 2025-10-30 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1e0bcf8-6621-3a86-a298-eb15459b2f21 | -6.9412 | -41.55692 | 2025-10-30 04:04:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cc87428c-368c-3e9c-940f-c984e571e9b7 | -4.84759 | -45.42323 | 2025-10-30 04:04:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e21a900-0bb7-3052-b5e2-ed04e2855dca | -7.6549 | -38.51072 | 2025-10-30 04:04:00 | NPP-375D | SANTA INÊS | PARAÍBA | Brasil | 2513356 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3d815604-9fb0-3019-8224-66ff631320b6 | -3.9202 | -43.31762 | 2025-10-30 04:04:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c6b10d5-5c6b-3f87-94a1-00b329ff7832 | -8.1615 | -37.61541 | 2025-10-30 04:04:00 | NPP-375D | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 21da04cd-bfe8-3105-88bb-b964dd30b309 | -2.77072 | -45.39825 | 2025-10-30 04:04:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8478dc52-87e7-33bc-bd9b-a1cbd0574ebe | -4.91392 | -45.67376 | 2025-10-30 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34fda86d-c388-3114-ada7-7db66dd94e14 | -5.40035 | -49.42686 | 2025-10-30 04:04:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README24.md)
