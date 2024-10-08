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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24c97195-d992-3b79-9e4b-903c699d442c | -3.60854 | -44.78814 | 2024-10-08 04:32:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c577789b-3edc-3633-a6b2-1dea8221f889 | -3.48037 | -45.00644 | 2024-10-08 04:32:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d7e8ef2-f698-3708-9495-639c703be056 | -3.43952 | -44.49646 | 2024-10-08 04:32:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8111d5fd-b870-301c-8fab-15ec049dc773 | -3.15131 | -45.04574 | 2024-10-08 04:32:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 670de268-e76b-33b6-9c46-2864e3a74ec0 | -5.07945 | -45.19297 | 2024-10-08 04:32:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f2f6ee5-4a48-3896-b264-4298a0c90b2d | -5.07598 | -45.19244 | 2024-10-08 04:32:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e2c2430-4731-3097-b323-0bb381f55bc2 | -4.92832 | -45.65054 | 2024-10-08 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 918aeae8-238f-31f6-adad-65dc46d02710 | -4.92491 | -45.65007 | 2024-10-08 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b027f54-423e-3d52-8415-a8266fe107ac | -4.92434 | -45.65376 | 2024-10-08 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 208d8d46-02cb-32a1-b9dc-df89a1491861 | -4.46952 | -45.91252 | 2024-10-08 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60d80f99-24fe-319c-a8b7-240696c6b906 | -4.13144 | -45.78686 | 2024-10-08 04:32:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fdb75a3-917c-3434-b701-3317e3b9a1d8 | -3.92036 | -44.74242 | 2024-10-08 04:32:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b91d050-dc6e-3cf5-9376-a5dab6a39233 | -3.70034 | -45.08186 | 2024-10-08 04:32:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b9a9a2fc-c37a-38a6-8f27-01339e1ffdcb | -5.91839 | -45.39455 | 2024-10-08 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1583ea2a-8f67-3b0b-ae0f-cdee7245323f | -5.91779 | -45.39843 | 2024-10-08 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ab885c6-8557-345c-9286-76b4648f9beb | -5.91491 | -45.39405 | 2024-10-08 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de1c7336-09f7-3be3-8cb7-cd983ea81d3b | -5.91432 | -45.39793 | 2024-10-08 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a061e9cd-0c0d-391f-ae43-f5979361555d | -5.90186 | -46.23401 | 2024-10-08 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 568b9542-b12d-3122-b2e2-e475b4135859 | -5.74433 | -46.19151 | 2024-10-08 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eeb6a8d6-8c6a-397a-a717-2f2dbb7aecf7 | -5.71329 | -46.46125 | 2024-10-08 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 899bde8a-0b9e-3804-83c4-00d0a76529c5 | -5.66707 | -46.34498 | 2024-10-08 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2506f72-b04b-3ea9-a896-e5d6e478bbae | -5.6571 | -45.86197 | 2024-10-08 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e16e6daf-8374-30e2-ab98-c8160e6050f8 | -5.56344 | -46.28873 | 2024-10-08 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b28f9ee-886b-3a2d-9992-8225749ad445 | -5.56289 | -46.2923 | 2024-10-08 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 913e9bc4-cb76-376d-9e93-c7cd3258a0d7 | -5.56008 | -46.28821 | 2024-10-08 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 930c58e2-f790-3746-bfb5-77a55ebe0945 | -5.55657 | -46.1994 | 2024-10-08 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4bd50d1-c338-30ec-8270-9e5c86c69d66 | -5.52216 | -45.25804 | 2024-10-08 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c410f5a-b596-3327-81f9-97e18243cd04 | -5.51869 | -45.25747 | 2024-10-08 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 90135959-402e-35a1-bb21-b0acd15892b1 | -5.51109 | -45.49035 | 2024-10-08 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ab1deafd-5f9c-33ba-8828-08e8611732d1 | -5.5045 | -46.38164 | 2024-10-08 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90a18a21-c823-3091-a056-e22e8f93f546 | -5.50115 | -46.38113 | 2024-10-08 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e96fb75-7965-3a4a-82f9-49f1618229b5 | -5.39921 | -44.95254 | 2024-10-08 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20f7c7b1-66a8-3ec9-bbec-8fcebc20ed16 | -5.39629 | -44.94803 | 2024-10-08 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de880e19-5a7e-3550-8f18-a45c2f25906d | -5.39569 | -44.95201 | 2024-10-08 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1654a0f-d95a-389d-be46-2738adcdf458 | -5.28192 | -45.38293 | 2024-10-08 04:32:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f80eac8-3c99-3fc8-9c16-f8e032fdb08f | -5.27549 | -45.12292 | 2024-10-08 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3943d2fa-3092-3475-aaa1-071dfa0bdf9c | -5.2726 | -45.11846 | 2024-10-08 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2109f522-546b-39cb-8916-71620d55ed66 | -5.27201 | -45.12236 | 2024-10-08 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0f947e8-b8a6-3068-9eed-d133e2ca3aef | -5.12277 | -45.27358 | 2024-10-08 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61ea73f9-c1d6-30a1-a26c-09be474c0a6a | -5.0985 | -46.19181 | 2024-10-08 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb589117-9dfb-3846-b167-053203dc205a | -1.17624 | -46.73016 | 2024-10-08 04:32:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1de4c580-1751-3faa-8e2f-6ea23b9b2f2e | -1.17295 | -46.72966 | 2024-10-08 04:32:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 93880713-3445-3fce-a65d-31bfc41787b4 | -3.31058 | -47.01074 | 2024-10-08 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f17fc1c4-c666-3a30-be7d-4342d8ebf45a | -3.30782 | -47.0068 | 2024-10-08 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1840146-a862-3ca3-b0ac-d4c4c368570b | -3.30728 | -47.01022 | 2024-10-08 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 949b82f7-16b5-3fd1-8101-ac024a19e51f | -3.28953 | -47.12334 | 2024-10-08 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6534d70d-27f4-38e6-8327-c6f61e6d82f2 | -3.28899 | -47.12677 | 2024-10-08 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b1c88c64-b500-37ad-b45f-92a9e86c4fd9 | -3.28623 | -47.12283 | 2024-10-08 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64e838ed-b3e7-3794-853f-bdeb4e4311e6 | -3.27895 | -46.34529 | 2024-10-08 04:32:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 093f510a-efeb-3e79-add3-c095945eecc2 | -3.15379 | -46.51389 | 2024-10-08 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c2be526-bf6b-3ffb-ae71-9ede5d3d55a4 | -2.95395 | -47.44281 | 2024-10-08 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90783ed0-16c0-3067-91d8-62162915b91e | -2.72284 | -46.81266 | 2024-10-08 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81f62687-5fcb-3116-831e-96e566965502 | -2.71954 | -46.81215 | 2024-10-08 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 781fc4cd-c12d-30a3-89f2-bb5dae4f7251 | -2.71625 | -46.81164 | 2024-10-08 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae9ee19f-68a9-3fda-b1d5-46c6495b6e26 | -2.71571 | -46.81507 | 2024-10-08 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1c32f0f-addf-3790-9309-e4d2e89835ac | -2.60456 | -47.3454 | 2024-10-08 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f70a7829-60c8-326c-8ae3-093318c37777 | -2.54335 | -46.15256 | 2024-10-08 04:32:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ce2102d-f7c9-3812-98df-c93c6b7913cb | -2.40828 | -46.75613 | 2024-10-08 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1df8ff5-4396-3c60-8dab-37677d60e2d7 | -2.23925 | -46.7467 | 2024-10-08 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 765884a6-7166-3c72-b1ca-85a5edb57a6c | -2.23871 | -46.75013 | 2024-10-08 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8221e965-1ef0-3779-b312-306cc7ae38b4 | -2.23817 | -46.75355 | 2024-10-08 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06bbcb78-3253-3937-bed6-e75390c721c0 | -2.23588 | -46.72512 | 2024-10-08 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cb5f49c-9067-356d-83e5-b29bb9eee408 | -2.23534 | -46.72855 | 2024-10-08 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4da44b66-5df2-35f1-982c-ac281f490276 | -2.2338 | -46.7599 | 2024-10-08 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e182057d-9db3-3616-aa7e-629426cd70bf | -2.23204 | -46.72804 | 2024-10-08 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a134961-d822-392a-8cf2-701d5ee498ca | -2.2305 | -46.75938 | 2024-10-08 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b37f1323-8fed-3870-bb96-c0bb294f2d02 | -4.47377 | -47.73278 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9996bd4-24b8-30f5-ba65-8f69f504dff7 | -4.47322 | -47.73623 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2164721a-e4e1-3dc9-b0d6-dbd54d16bfd7 | -4.31868 | -47.70436 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a5be0ba-4f68-39d9-8e5b-b4a176c9e401 | -4.31814 | -47.70779 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b4475373-73f0-3210-ac2f-78e614846380 | -4.31484 | -47.70728 | 2024-10-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 02a148a1-4034-3521-bef6-7d6e37b0af53 | -3.70193 | -47.59958 | 2024-10-08 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a2c7183-d132-34c7-9ca5-e43706aa26ff | -3.70139 | -47.60301 | 2024-10-08 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4503b290-149b-3bb8-8e0c-5765fab88fdb | -3.70085 | -47.60645 | 2024-10-08 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a01496ce-ce28-3e4c-9744-d805a03e41eb | -4.58526 | -47.17323 | 2024-10-08 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cf5e98e1-080d-3fa9-a5f5-e829d1711a5f | -4.35459 | -47.29842 | 2024-10-08 04:32:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 885994c1-fe32-3b26-a82a-48b6a139609b | -4.33595 | -47.30958 | 2024-10-08 04:32:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1bf645f6-4a26-3a57-8bb5-f61ed91560b5 | -4.27492 | -46.28576 | 2024-10-08 04:32:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 850fcdc0-fd5c-331b-9599-4cbb56b005a6 | -4.27213 | -46.28177 | 2024-10-08 04:32:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 043a8b9d-b8c1-3320-9602-3741296c0acd | -4.27159 | -46.28526 | 2024-10-08 04:32:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff312749-a9fb-3d37-91e9-7840b99556ca | -4.2688 | -46.28126 | 2024-10-08 04:32:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06636855-1733-3161-ae9c-52ece0db55fe | -4.03596 | -46.94556 | 2024-10-08 04:32:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 646a48ea-52ae-3b66-82e3-51b23f254e03 | -3.93991 | -46.44862 | 2024-10-08 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| fc07164a-b085-30fc-b09d-362271839a35 | -3.93714 | -46.44463 | 2024-10-08 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c7b6b495-fe42-3f50-ae97-692966928ba8 | -3.93659 | -46.44811 | 2024-10-08 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 9955ee87-c8bb-3c30-b1b1-492ab46479a4 | -3.93436 | -46.44063 | 2024-10-08 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6106aa1d-975b-3d6d-9101-e4dd2633f390 | -3.93382 | -46.44411 | 2024-10-08 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7754e118-6498-386d-ba53-948f354ffed9 | -3.93327 | -46.4476 | 2024-10-08 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e3c784cc-a098-3ede-8d66-113474ddd921 | -3.93105 | -46.44012 | 2024-10-08 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c2aeb01-ba40-3559-a616-6d800654652b | -3.9305 | -46.4436 | 2024-10-08 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 64672312-bf7d-3fdb-981b-7cd668298426 | -3.92104 | -46.41711 | 2024-10-08 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1657c39-a344-3cb2-97e0-753af7cdf926 | -3.90505 | -46.43247 | 2024-10-08 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 22522ca2-a962-325b-9e27-8a9659d2ddee | -3.85595 | -46.46412 | 2024-10-08 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a77192f-35ee-3154-855f-7447025852ec | -3.84824 | -46.47005 | 2024-10-08 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 022ebf5d-084d-3f45-aed6-87cc5fcf52af | -4.95103 | -47.40335 | 2024-10-08 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17e73322-c9d6-3327-82d1-6e7c70ce4ef3 | -4.92365 | -46.77367 | 2024-10-08 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d132df7a-c3e5-3002-b491-4041e2e2f78d | -5.97244 | -46.67918 | 2024-10-08 04:32:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6866bd2-fe47-32e8-a5f9-3bfd4ab17b54 | -5.88937 | -47.08136 | 2024-10-08 04:32:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ee0c505-9148-34ea-ac7a-b000371307f9 | -5.16402 | -47.6062 | 2024-10-08 04:32:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc8f3cf1-12dc-3602-a413-5015cc9ceb9d | -1.61536 | -47.46807 | 2024-10-08 04:32:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README50.md)
