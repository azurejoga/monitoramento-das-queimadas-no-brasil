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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e47d7ead-321b-3a9b-b6a5-68e9da82f16f | -8.38503 | -47.99417 | 2025-09-11 04:44:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dacb6b4d-d4a6-37f7-9a60-ba9e946a52fd | -3.35333 | -39.28098 | 2025-09-11 04:44:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 24d86691-bbfe-3da3-a9ca-f969826fbd84 | -6.8213 | -52.79956 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8b04a55-e57b-33e0-92dd-504e7ad76d0f | -5.92421 | -53.81026 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc44d778-5493-37f1-aa6a-9f1f0f6855c5 | -6.25412 | -51.82704 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80abd552-3a5f-3869-9116-9617ecfb115e | -6.1754 | -41.0806 | 2025-09-11 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 76547585-ab66-399a-96eb-289d9bca2882 | -4.28914 | -50.59228 | 2025-09-11 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81802b91-bf3f-3fa2-96cd-3cffd60aec1a | -2.07444 | -47.14189 | 2025-09-11 04:44:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 823df537-4a4c-34a8-aabc-a04715cb1b99 | -7.92367 | -44.87969 | 2025-09-11 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ad49781-65be-387a-8185-13e49d31101c | -7.3888 | -47.36533 | 2025-09-11 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1221b771-04ca-3c37-8411-d815015986e3 | -7.23673 | -55.05627 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ec44529-099b-3317-942d-2568e04c9035 | -8.04514 | -49.05372 | 2025-09-11 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1ece4295-8683-3f12-9502-8b886c870bb2 | -6.19615 | -42.49008 | 2025-09-11 04:44:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 914f8127-1530-39b3-b75e-a0b8e62efa2d | -6.23777 | -42.8509 | 2025-09-11 04:44:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 48b3160b-ab9a-3588-ad38-28b59d6b8932 | -5.65802 | -43.89959 | 2025-09-11 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27bccc3e-53ff-3aad-a28e-86e0ee428661 | -8.11081 | -44.85214 | 2025-09-11 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92b06b05-98a2-37fe-ad7b-f9aee2a1be93 | -6.85836 | -44.89311 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d744c08-6b8d-3b19-9a43-8f5789736fc5 | -6.48153 | -41.75025 | 2025-09-11 04:44:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0591ebee-6923-394f-960e-df223035da71 | -6.65656 | -44.54372 | 2025-09-11 04:44:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd344c98-1ca5-3b5f-9a5d-f2e52b39b8be | -3.73696 | -49.04588 | 2025-09-11 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c13454c-5a28-3ff2-9222-2aa12675f8ed | -3.31784 | -48.72409 | 2025-09-11 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e1f16b9-b4fb-3069-9a4a-cd216bae3262 | -7.30947 | -49.61518 | 2025-09-11 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f83c453-3c39-3e8d-8e47-7c2c57ceb1e8 | -9.08456 | -47.08801 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02c2c9aa-f18c-30bf-862c-9f541f9ac2b2 | -9.06013 | -45.72207 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 50bfa584-61ac-36a0-b8f9-df9ffee15c1a | -5.78939 | -44.86098 | 2025-09-11 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2caf0bac-d3de-3ebf-a549-34197d2f29a5 | -8.76143 | -47.11213 | 2025-09-11 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 739d4ebd-edfd-30c0-ba42-5835b04d8ef6 | -5.54881 | -43.05087 | 2025-09-11 04:44:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6a22cc26-70d3-306f-8e44-ddebad5928e6 | -6.21709 | -43.49415 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 745aa95f-6b91-372a-ba06-f7fa808f7746 | -7.76201 | -50.7739 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b6a7a26-5b1d-3027-8164-316cb1ac467e | -9.04066 | -45.79675 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77fba339-20a2-3908-ae89-9598987579ae | -5.8107 | -45.67791 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8f72231-eba9-30f7-8239-1da019ed0b47 | -8.03327 | -44.49543 | 2025-09-11 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a341b462-5173-3171-90c5-a5b1ed57fb7e | -9.1472 | -45.5588 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f5e4888a-5a6b-3088-982e-92a7ea7f094e | -8.43048 | -47.26891 | 2025-09-11 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 905660a8-3db4-33b3-845d-6188e2b146d2 | -7.26118 | -44.9014 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4f33b4a8-4cb2-3fb5-9165-b8f54c2b54b3 | -7.38676 | -47.37892 | 2025-09-11 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a32206de-6a9f-3aa5-abbc-b6789d410aea | -6.81432 | -44.88547 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 750cb746-0834-3716-b859-cddf87fd6694 | -7.8499 | -45.40368 | 2025-09-11 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 11774b13-98da-3431-b74a-f3d3c0acd1e8 | -6.46649 | -53.41299 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fe773d4-a6e5-3fd0-bb4a-30cca7ea53da | -8.08702 | -52.34679 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bb1f528-6c51-35ea-9369-cbe271334ad0 | -5.11282 | -46.24095 | 2025-09-11 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 653149a8-f50a-350b-b8d0-79b3689702f1 | -5.10245 | -46.07034 | 2025-09-11 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1cbdd9c0-cd33-3c02-9bca-f8fed6e89a9a | -5.96208 | -45.8337 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2fb5a2a-b993-377a-93f8-7d4adcde10c5 | -6.62308 | -43.99113 | 2025-09-11 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2e16bcb-1cb9-3540-ad4e-05a409f8a81d | -6.19311 | -42.66107 | 2025-09-11 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 99a69110-59c7-37a6-ad50-aed62dda6e65 | -7.6267 | -46.54818 | 2025-09-11 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b6f70d0-c74b-3947-ba2e-97330a3c30bb | -6.73396 | -43.99097 | 2025-09-11 04:44:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| edcfe6fa-aac4-3ead-a032-3cb82dae1026 | -7.1891 | -44.96639 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3edb719b-b8c0-3c70-aaf6-5e9cce548d83 | -5.2355 | -45.46089 | 2025-09-11 04:44:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0418ac5f-a288-3864-9b97-f1e9748d1d46 | -6.24733 | -44.80064 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b9833d7-8264-3e1e-8672-c87dc255b791 | -6.34674 | -45.18489 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2051d99-360b-381e-9581-ab3043dcfb4b | -9.06676 | -47.04602 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 67fa079e-dd8d-37c9-9635-953239d2525f | -6.41005 | -53.65185 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e49d7f6-1ca7-3f95-9deb-0edc9ae16d7d | -8.96719 | -44.93312 | 2025-09-11 04:44:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1626915-297e-3563-b27c-e209de64770a | -6.37005 | -45.16768 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d8eb1c6-159a-30ac-b482-07adb466a40e | -2.82111 | -52.13686 | 2025-09-11 04:44:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0fdcc37-1753-3e24-84e4-5969dd84112f | -5.92776 | -53.81085 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c3a93ff-1792-3022-ac84-d171bc885f21 | -6.7526 | -51.96053 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5f3a007-adc1-38f8-b394-853ac98527ec | -8.64952 | -45.72374 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 537d4676-68f1-377d-94bb-0473cb892af8 | -7.50442 | -48.26943 | 2025-09-11 04:44:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39b23765-dd77-3eff-a3a4-2af10d3d2e06 | -8.31975 | -44.89706 | 2025-09-11 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5fd92c1-8d9b-3194-afc3-4bed8f41acc0 | -7.7304 | -50.73687 | 2025-09-11 04:44:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f44e7771-c222-38da-953c-69bcf68c666c | -9.037 | -45.792 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 661c233a-6d19-3b5b-bfa3-034831c44b7a | -7.23749 | -55.05172 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89799bd4-a131-3eb8-a22e-9e47d706419a | -9.11648 | -46.97685 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68fb6783-c86f-353a-9155-e26a2191eb8c | -8.08955 | -48.22305 | 2025-09-11 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa602148-240b-3549-96a8-fae8a502a87f | -8.02814 | -48.65889 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| df4658d5-2cb6-346a-8192-7eaee03310c8 | -6.69553 | -44.95822 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48427b56-59c4-3f4f-83e7-7a4dee8ca11b | -7.77142 | -50.77894 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b607f743-8c96-335c-a223-3af9529908db | -6.20281 | -43.49183 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 267b425c-7d29-38c3-84b7-d2c900dcddf8 | -7.54935 | -42.53073 | 2025-09-11 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e2acaa75-4e88-3a0f-ae73-a65e067e3a70 | -8.2224 | -49.50353 | 2025-09-11 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d694d045-ec67-3d51-bee1-c9a1244d7086 | -8.06059 | -52.3246 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cd13a82-36a5-39a2-a5dd-d5eea5f4d10e | -8.04978 | -49.02273 | 2025-09-11 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ecdf48c-36a3-3f3d-9649-7f69db9382ad | -1.44528 | -49.45424 | 2025-09-11 04:44:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41e06013-d114-3efe-b1fe-7f42f7002eba | -7.7526 | -50.76883 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 059cd1a6-c47e-36f7-be92-98932f3f6958 | -8.06392 | -52.32517 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 919e32ea-01ac-3dbb-9afe-4921f5e78bc7 | -6.04651 | -44.82029 | 2025-09-11 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43be87b7-3519-3d3e-930b-6f1de22abd41 | -7.11486 | -50.76469 | 2025-09-11 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a01fbbf3-480b-36c2-9d9b-fee2f2bc6e9c | -5.87863 | -45.66584 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| deabaafa-6940-32f6-add0-e4195b0cd508 | -5.40437 | -45.9225 | 2025-09-11 04:44:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5814ecf4-e6d0-39b6-94f0-f4f609ce82cb | -8.51731 | -45.68604 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c472b150-3fc4-34ed-b09b-a40270123976 | -6.28918 | -42.2016 | 2025-09-11 04:44:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a7ec397f-7b18-3d6d-9177-dc349f72b453 | -8.74379 | -47.11698 | 2025-09-11 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18c1693b-c71c-3021-ac3f-8c0f5701774e | -8.04281 | -49.0455 | 2025-09-11 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| beba74aa-16ba-390b-9ab6-89c46433e0b2 | -6.85275 | -47.8749 | 2025-09-11 04:44:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3931740-5c89-37b4-ac2c-006257574bfe | -8.05223 | -52.33416 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90ed99c2-559b-350d-86ec-414450decb90 | -8.19895 | -50.10729 | 2025-09-11 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 23db2565-1bb1-3ce0-9029-73283c99efe1 | -3.14537 | -49.8974 | 2025-09-11 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e23e5e5-6f21-32ba-8b77-6ad45c5f93b1 | -5.51603 | -45.45197 | 2025-09-11 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fb5c1b9-e5db-377c-bd17-83dfaf4cf294 | -6.81646 | -51.88087 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e10333a3-d378-31b3-88bb-55fd4fe326a5 | -9.07674 | -47.08691 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2da977bd-be98-392f-bd88-449c647d36bc | -6.6215 | -43.99372 | 2025-09-11 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 274ae592-7e95-399b-9406-c3a633e1e388 | -8.1045 | -49.24697 | 2025-09-11 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53238d25-8311-3d21-9586-88772804b408 | -8.04947 | -52.33001 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 40157ef7-4ba7-3d77-859b-c5428412c541 | -7.55734 | -48.20992 | 2025-09-11 04:44:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f54842fe-13a4-3a92-8b5d-c6fd555ea1f5 | -8.73116 | -47.09501 | 2025-09-11 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f314a12d-f437-3316-a880-33d51967c8bb | -5.76538 | -42.44415 | 2025-09-11 04:44:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 460aad9d-39cd-3370-9851-f395a6c6d83d | -9.04074 | -45.73568 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49302942-11ba-3743-8151-582491ac011a | -6.85527 | -47.85811 | 2025-09-11 04:44:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README92.md)
