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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27583a29-caf6-3947-975e-8e8fe5dcefdc | -9.28584 | -45.70109 | 2025-09-28 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efdeccc5-2574-3d43-9e5b-61001191e467 | -7.42514 | -40.08091 | 2025-09-28 04:04:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 95b37684-2b62-3cb4-bee1-0b14e8b07830 | -7.53414 | -46.09387 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d32d9154-5a42-3b2c-af33-05b0e9b565d8 | -6.48581 | -44.50583 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cf9918a-59df-3a7c-9a0c-afd3b6429a54 | -5.73151 | -42.84803 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 322cffd0-3871-3ed3-9aff-075ca1b9a691 | -7.71106 | -41.28663 | 2025-09-28 04:04:00 | NPP-375D | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1f5999b6-fe05-39f7-a783-e4e238aed7ec | -5.9049 | -43.29244 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 683472d2-74fe-3f48-883d-83313d5e665d | -5.7058 | -42.62196 | 2025-09-28 04:04:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 63bd2af3-cb2d-36bb-862a-3579f90da818 | -5.60884 | -43.37009 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9bc7b748-1c20-349f-bb2a-390739628f2f | -7.7105 | -41.29018 | 2025-09-28 04:04:00 | NPP-375D | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f5fac77e-8616-373e-b50a-758554fa9453 | -5.83063 | -44.43201 | 2025-09-28 04:04:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| af959e7c-d418-3506-a068-073a4d066e51 | -4.87103 | -42.95506 | 2025-09-28 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5d9b69cd-7229-392b-9a7c-2ded528379ee | -6.2028 | -42.84801 | 2025-09-28 04:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b996cae0-6e59-34cc-9e1d-b8a5a3537934 | -9.2174 | -46.77351 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 93ee1da9-7a02-3b80-8660-8fc0bf3bd5d7 | -8.672 | -43.986 | 2025-09-28 04:04:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bb48d11-acfe-3777-afa4-1859d5d40050 | -6.41316 | -42.86318 | 2025-09-28 04:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0c15c8b3-5a33-3c21-b786-c4947fed53cc | -7.542 | -46.09932 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8adb474c-bbc1-3bad-a53e-0f8ba3d81b9a | -6.76423 | -44.59187 | 2025-09-28 04:04:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6c6e2060-82d7-3c19-be55-0a634aad5011 | -3.86713 | -40.44868 | 2025-09-28 04:04:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c609d6f6-c1c0-3bd7-8af6-acdbed939e50 | -6.99217 | -44.85575 | 2025-09-28 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b25ab43e-1594-303f-bc5e-18d387bf16ee | -7.59757 | -43.05756 | 2025-09-28 04:04:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| eb6c2c94-1c92-3f49-af6f-190ca40ecfd4 | -7.58442 | -42.32894 | 2025-09-28 04:04:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 79cd6117-0008-377a-9ff8-8a134d73a3fc | -2.58596 | -48.41082 | 2025-09-28 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 157df441-6afe-3e99-9b70-7e4a209f88d5 | -8.48084 | -47.81108 | 2025-09-28 04:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 830d87b1-1a9a-30bd-a9e7-b5802f4fa85d | -3.27478 | -43.53959 | 2025-09-28 04:04:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ccf279ac-f505-3253-b49a-5b06be05cce3 | -5.73821 | -46.18453 | 2025-09-28 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2482beb7-d43b-30ef-b38e-263fb7ec9691 | -6.6972 | -44.60668 | 2025-09-28 04:04:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 97b47bff-5fce-37bb-ae81-e19aa1ea32df | -5.2884 | -43.16187 | 2025-09-28 04:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bc59619-205e-3c34-a0bf-c547b8c67d3c | -8.168 | -46.40881 | 2025-09-28 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0ecd905e-dd09-30ca-941c-cbc33625657d | -5.80422 | -42.86315 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 317dd1cf-018b-3a83-981c-56b86329576a | -8.29047 | -45.44102 | 2025-09-28 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c654a694-54ce-3c9e-8d80-56992e786615 | -6.719 | -47.20325 | 2025-09-28 04:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b416f81-cc41-39fc-aac1-1fd9c78c70d3 | -7.74806 | -47.3772 | 2025-09-28 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d5490407-fc41-3597-a2b7-2b406ea2a444 | -8.64667 | -44.85537 | 2025-09-28 04:04:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7e94b604-9990-3cf5-a0a1-a9a84a2922f4 | -6.60791 | -45.08683 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 840ff0c7-6765-37d1-b049-355d827c740f | -9.06849 | -45.5381 | 2025-09-28 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57d24e08-e2ad-3655-b383-c4efb1ae5fc7 | -8.48827 | -47.82156 | 2025-09-28 04:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 791c720d-8a6e-3f9c-9036-62602466c7ae | -6.15241 | -42.78569 | 2025-09-28 04:04:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| da11db9a-b416-3b37-a0c2-7896dd519483 | -6.61052 | -44.94943 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16b91ca2-934c-3f99-bb0e-08c31a18905b | -6.43019 | -42.9161 | 2025-09-28 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8cbe5f99-34be-3963-8f32-1fc74c601120 | -9.04643 | -46.72036 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad627db8-70e8-3cd3-bc1b-5b47847a9196 | -8.28215 | -45.46524 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1b00086b-25e9-3d9e-8b0b-77715f00adcf | -5.98369 | -44.12784 | 2025-09-28 04:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b9e1aea-f98f-3f95-855c-1b7c46d5e527 | -8.6375 | -44.8387 | 2025-09-28 04:04:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c8f5ba6-84bb-3089-81dd-79f409bb6640 | -5.74299 | -42.84573 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| dd40642f-d625-3c8e-ac9e-1f90fdbe5e7a | -8.64056 | -44.84421 | 2025-09-28 04:04:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a205ae89-04a0-3c3b-8df5-b8b904ca2791 | -8.64247 | -44.0037 | 2025-09-28 04:04:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53eb382e-a1ca-3e74-8b16-4edd7365fcc4 | -6.54201 | -43.82655 | 2025-09-28 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 661c37c2-c911-39f9-94b6-daf3628a7d15 | -7.8131 | -44.5708 | 2025-09-28 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ad9e65c-79cc-3e12-bc1a-353d95d54cf3 | -7.03835 | -44.77436 | 2025-09-28 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eee6c590-4eac-3b36-9de9-6d537b759f89 | -8.17417 | -46.34667 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 77a1b602-9166-3906-bae7-a45ed0f8a234 | -5.78444 | -42.82589 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 58cf9946-f004-3504-a7ee-033a16bda014 | -4.81519 | -48.24222 | 2025-09-28 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd200405-177a-3343-aa85-9665dd4eac9d | -6.47701 | -44.24641 | 2025-09-28 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 087e7b58-80bf-3c9f-aa76-18e3e73a7dc4 | -8.90124 | -46.09077 | 2025-09-28 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d588f753-fa35-3c47-a72d-2b88d903703a | -7.75882 | -45.74482 | 2025-09-28 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bfc1936b-055e-3ee9-9de8-0abba0ed862c | -5.18697 | -45.39154 | 2025-09-28 04:04:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fdf2b752-df1c-385d-b305-56f106692131 | -3.8508 | -40.99211 | 2025-09-28 04:04:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f8e47e82-c5fe-38fb-b5e5-a8ad12ef7d71 | -5.71124 | -42.65582 | 2025-09-28 04:04:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cfcba6df-f59e-32a7-b020-c84b8ca737ed | -4.26127 | -48.55647 | 2025-09-28 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37707e47-0b7c-3005-99c3-ab98003342ad | -6.79283 | -46.19085 | 2025-09-28 04:04:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c96109b-0c22-3c49-b5fb-c832e271ea8d | -7.58566 | -42.32136 | 2025-09-28 04:04:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2854c4ac-00ad-3f38-9665-cb6c3e3d3caa | -5.6044 | -43.37389 | 2025-09-28 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a53c3a40-a982-3a70-8402-50f9361140a6 | -6.70113 | -44.60732 | 2025-09-28 04:04:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8eab406-50eb-3574-b6a6-6c21daa1c69a | -6.38665 | -42.94823 | 2025-09-28 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 5b3e822d-4a56-36a7-b051-a88930e38770 | -7.70714 | -41.28965 | 2025-09-28 04:04:00 | NPP-375D | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 26db4670-e933-321f-ae29-00cc7c906585 | -4.13247 | -44.22556 | 2025-09-28 04:04:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36e5be81-4989-3b9f-a86c-e20f9b80a9d0 | -8.86141 | -48.56623 | 2025-09-28 04:04:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0bc3ace5-5473-319c-8cfa-79a61556d28a | -5.54419 | -42.82863 | 2025-09-28 04:04:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 7ddd3f74-9409-3dba-b2f2-b462c847b286 | -4.48129 | -47.67643 | 2025-09-28 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 87fefcbd-6098-3e4e-b9cb-ccc0cba9a2a0 | -6.26638 | -44.06966 | 2025-09-28 04:04:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1fcf621-237b-38d8-b02f-480287b9aa51 | -5.8121 | -42.79233 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c76a922d-ae2c-385d-947b-a362d2b6ba61 | -5.75084 | -42.84289 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| e555f546-405b-363e-a989-9b6b11eb1df8 | -7.15837 | -45.51445 | 2025-09-28 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc1f51e7-c195-34c1-b707-273c689c5676 | -6.24479 | -44.4857 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 327d73e3-f393-30ef-a480-997e5d02f779 | -6.7624 | -45.52488 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8a2e4bf-7bfa-3d90-9c34-1fad64c2146d | -7.75689 | -47.00344 | 2025-09-28 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3604f9d9-2435-3fc8-9b97-f2cda0766285 | -8.63201 | -44.84767 | 2025-09-28 04:04:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b9eb94aa-5b8e-33a2-b114-70370a7bcc9b | -7.63596 | -45.97943 | 2025-09-28 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ef991c7-9bc1-33c7-b5b7-4b3a683376be | -5.74889 | -42.88407 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 3e2af8a1-d17f-38c4-8d21-a4c851730c65 | -8.29149 | -45.45935 | 2025-09-28 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af3ec333-9dd1-3345-81c7-576d33d3d106 | -5.77656 | -42.82884 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7228c7e1-4ba1-3fd4-bd4e-245c185683a6 | -9.45053 | -43.70338 | 2025-09-28 04:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 85310d7d-cf25-3e17-8ebe-4d6ff1ff4ef7 | -5.16546 | -45.02223 | 2025-09-28 04:04:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d9d1ec1-d359-3252-b6ee-0830f3f420de | -8.17021 | -46.422 | 2025-09-28 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 399cfb1d-8aaa-3fd1-8177-2459a305e68b | -3.97038 | -49.46348 | 2025-09-28 04:04:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec1fd7f9-48db-31ad-bb6b-27ea9674a8b9 | -9.9786 | -43.60971 | 2025-09-28 04:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fd1e804c-c42a-31a3-acf6-2d5a247b61e7 | -7.17498 | -41.71082 | 2025-09-28 04:04:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a5038c20-dc0d-3a55-9ef5-4ecbe919bd37 | -6.5644 | -45.10176 | 2025-09-28 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dcb6e80e-c435-34fe-9c1d-e031d04bf0ab | -5.18273 | -45.39085 | 2025-09-28 04:04:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9cdee37-d854-3ea6-aeb4-da888b740b45 | -7.43845 | -43.18737 | 2025-09-28 04:04:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c4cc3cb6-f24d-3e93-9cc3-fc3eb9dd0c89 | -6.75948 | -44.59623 | 2025-09-28 04:04:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3cb1bbd4-b002-32a3-882f-79d0dda0a2d4 | -5.89212 | -38.47952 | 2025-09-28 04:04:00 | NPP-375D | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e01d37dd-d6a5-3c72-b808-44706f561517 | -9.54109 | -47.7749 | 2025-09-28 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7d6f4c4-d2cb-3268-b925-191e08cf78cf | -6.04033 | -43.58773 | 2025-09-28 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d85426de-7d40-3e25-9da7-e2211fd8cc62 | -6.42975 | -43.07656 | 2025-09-28 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 92c33302-fca5-3872-bdf5-074588c4be01 | -5.42486 | -41.3256 | 2025-09-28 04:04:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ec9a06cf-827f-35a4-b4f1-25bbff888a38 | -5.1962 | -43.71666 | 2025-09-28 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 987f4fad-c6fc-3cb9-932b-f6d65c1ed636 | -10.04725 | -46.13837 | 2025-09-28 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9401ba37-e3cf-388d-afae-0c2f1f0fb871 | -5.77297 | -42.8282 | 2025-09-28 04:04:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |


[Clique aqui para ver as próximas entradas](README31.md)
