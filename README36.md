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
| 9a10b595-0d0b-3e10-ac8f-5222a0edfeac | -4.82876 | -41.80662 | 2025-09-03 03:53:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2f1867ab-314e-322d-8b41-ab663cb6700f | -4.14911 | -38.48231 | 2025-09-03 03:53:00 | NOAA-20 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d3d619db-2260-3238-abdc-9db20d76c6c9 | -3.81704 | -41.06531 | 2025-09-03 03:53:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d0d03429-59e2-30ba-9d1d-9001fc10991d | -5.74173 | -39.76212 | 2025-09-03 03:53:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f9401348-6091-3173-9035-129b6d9ea2a2 | -5.40636 | -42.33626 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| eb672cee-d4e2-3838-98d7-d600a7c3a509 | -4.73825 | -43.5782 | 2025-09-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bed3d0b6-571a-3654-9eee-684692f72292 | -5.36108 | -42.62225 | 2025-09-03 03:53:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f30c8082-43d7-3065-824b-62dfc8e33f89 | -3.19856 | -49.10734 | 2025-09-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5c5ef656-2873-39a8-87bc-69ef31908475 | -2.90015 | -48.29439 | 2025-09-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ff9362b-a822-3374-b829-875b9a40838c | -4.84663 | -42.74104 | 2025-09-03 03:53:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d975398-d0a4-3bfc-9e18-95277469460a | -4.78994 | -43.66153 | 2025-09-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f13d75d-551d-3a07-ab13-286e37a1683a | -2.89817 | -48.29343 | 2025-09-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87ba03ce-6f85-3b9c-9909-ff7686696d51 | -5.34523 | -43.1071 | 2025-09-03 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d83af788-6a0b-30b2-b2b0-caf0992e6645 | -2.9295 | -49.4636 | 2025-09-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6378a71-3049-3c03-8c08-d016f1d36bb3 | -5.79599 | -43.23008 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b466a70-87d8-31d2-973c-ffffb0cf8f80 | -3.19832 | -49.11635 | 2025-09-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a7a4ed8-ae3e-3066-bd3d-0258bb255766 | -4.7347 | -43.57371 | 2025-09-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dfb224ca-08d6-3cdf-860f-da3f1084ab24 | -3.97098 | -43.2426 | 2025-09-03 03:53:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9d503bc-fdf1-3b95-925a-3c8d33b7e9df | -2.93412 | -49.4615 | 2025-09-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89d49d9f-01bc-3546-9746-58bd958ed6a8 | -4.18604 | -46.84771 | 2025-09-03 03:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c1f0bb56-df4c-33c6-bd8b-d8094e061ad9 | -4.87974 | -43.02339 | 2025-09-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9baa5bdc-89ea-3e45-bd3f-8d28a51f7fce | -4.89887 | -43.20861 | 2025-09-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2d46d0b9-c712-3490-83a9-35afb2250781 | -4.66865 | -41.95965 | 2025-09-03 03:53:00 | NOAA-20 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 25a52393-c67c-3292-97b2-0cc46633251d | -5.16882 | -38.97209 | 2025-09-03 03:53:00 | NOAA-20 | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c908389d-b903-3f96-a432-0ba200b0c7d1 | -3.97751 | -47.00357 | 2025-09-03 03:53:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 438fda72-4552-3a94-aa8b-4aead4c7a5f2 | -4.89421 | -43.21155 | 2025-09-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3f740398-cde2-3b52-bf8b-a983444a0763 | -5.51386 | -42.64417 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1efd76e1-ddc8-3c48-b489-22892581ff81 | -5.44952 | -42.83751 | 2025-09-03 03:53:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2420337c-e058-35ed-9048-987f5606b7f9 | -4.15901 | -46.78385 | 2025-09-03 03:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e2e9c45d-3488-3218-80a5-bf7b39c334f5 | -6.37438 | -37.37558 | 2025-09-03 03:53:00 | NOAA-20 | JARDIM DE PIRANHAS | RIO GRANDE DO NORTE | Brasil | 2405603 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 152d0455-8701-3616-939a-fb69185ff90e | -4.48453 | -48.12099 | 2025-09-03 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c528ff16-3e3c-39e0-8c33-1eab752edae4 | -5.56199 | -43.08352 | 2025-09-03 03:53:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b993a620-00d1-3cb9-a15a-ae26e236ddd4 | -5.79656 | -43.22662 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d3853ac-9c86-3edd-bf92-abf15124a32a | -3.22808 | -47.12759 | 2025-09-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 22cce10f-d3c4-31e3-bc19-e4f9da43306b | -4.79833 | -43.66292 | 2025-09-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 703d2087-0be7-3de7-b593-c4c13f0f709f | -4.6783 | -42.92982 | 2025-09-03 03:53:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16243d4e-442f-3032-a82a-88398d1f15d0 | -5.76192 | -37.92646 | 2025-09-03 03:53:00 | NOAA-20 | SEVERIANO MELO | RIO GRANDE DO NORTE | Brasil | 2413607 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1facb896-aa59-3d7d-8368-dac6803bb1a6 | -4.78511 | -43.66466 | 2025-09-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b46f4f05-5efc-3eaf-9e51-f333992630bc | -5.52877 | -36.84924 | 2025-09-03 03:53:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 01e1b27e-2e2e-3071-bacd-ff5ab480db03 | -3.19773 | -49.11209 | 2025-09-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6511f10f-1598-3e69-aa05-2bcd56ca468c | -4.52092 | -42.08009 | 2025-09-03 03:53:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f1016b24-e713-3946-80f9-07e2c6ac5ca7 | -4.78575 | -43.66084 | 2025-09-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3ae6523-b3ae-38a1-99e8-174df43851c5 | -4.89303 | -43.21873 | 2025-09-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 961dd6d0-40f1-3d5b-ad17-8373455d3b16 | -4.15204 | -46.79305 | 2025-09-03 03:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c7a18b04-deaf-311c-bb36-7488830fd95c | -5.84732 | -43.0148 | 2025-09-03 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2363c92d-1e0a-3d77-b47e-d69a1f1053bd | -3.97807 | -47.00022 | 2025-09-03 03:53:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 534c60b8-d407-3ced-961e-e6c8363a862a | -4.89252 | -43.19648 | 2025-09-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77c158ff-aaf0-36ad-895b-72830d60eb1f | -2.93501 | -49.4561 | 2025-09-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ad1a09b7-e83d-3d67-9591-137006061a45 | -4.78639 | -43.65701 | 2025-09-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b5a1dac-3e26-3e3c-a437-74ab50f3fe15 | -3.19913 | -49.11147 | 2025-09-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58dfcb96-931e-396e-9fa3-3f9fec57c742 | -4.89193 | -43.20004 | 2025-09-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee08f19f-13d1-393b-aa1a-344e7c0e4810 | -3.36925 | -47.16151 | 2025-09-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2aaa3c02-c0c8-3ea7-a3e2-93caaccc8bc2 | -4.68305 | -43.65181 | 2025-09-03 03:53:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0099a890-6a2e-34ae-b228-6cb3c678a9c8 | -5.6696 | -43.64043 | 2025-09-03 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ee5b40e7-2315-3c69-8c34-7b02d450bdce | -3.3747 | -47.16241 | 2025-09-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25982fa8-1218-3c29-89df-667f81cbe652 | -2.90406 | -48.2945 | 2025-09-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27aaf393-c951-33ea-930a-96b04c2c2058 | -4.7893 | -43.66536 | 2025-09-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 40ba15fc-56cf-3743-a33c-a5458a24b1e5 | -4.89658 | -43.19715 | 2025-09-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5f8a7f2-ea2d-3fa4-886b-44d9fed2d662 | -4.68077 | -43.63964 | 2025-09-03 03:53:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb7f629f-71de-3edf-9fe0-a2abe31bdba8 | -5.74227 | -43.13198 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8df31e81-2729-3aa0-a465-18ab236b7d4f | -5.50463 | -42.62764 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 42ec13a9-b42b-3369-ade9-a777f1e50ba0 | -5.65949 | -43.12467 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 4.4 |
| f7d7f746-6382-3c88-8759-544136abebd6 | -5.53494 | -36.85386 | 2025-09-03 03:53:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 889e18c5-5a4b-31d6-992a-cf8ba55065b2 | -5.44474 | -42.8419 | 2025-09-03 03:53:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| dd3d0903-ced8-3659-ac2f-c9becf7475a9 | -4.89244 | -43.22234 | 2025-09-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e1404800-1e67-3db2-9366-cd1ba64fb866 | -5.70737 | -43.10791 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| da02c5f8-2afc-36f2-a95a-fbd215d526db | -2.90334 | -48.29874 | 2025-09-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6475a8c3-83f0-3a72-b247-024978f6e1f0 | -5.51306 | -42.64904 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 11e39ef1-f4a7-36c6-9eaf-ce432c43ae6c | -4.8971 | -43.21943 | 2025-09-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9aab9876-ef4b-3269-8783-f4b0aa22dc7f | -4.89828 | -43.21224 | 2025-09-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 39c8e908-cd2e-3ace-922c-01abea734032 | -3.22748 | -47.13113 | 2025-09-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| b85eb65c-b29e-30bf-a38c-6f43bab514f5 | -5.80057 | -43.2273 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23ece724-dd87-39e3-ac3a-7786db930120 | -4.79286 | -43.66987 | 2025-09-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a8f98915-15e4-38c0-be41-1f9d6370349d | -4.89769 | -43.21584 | 2025-09-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 537399bd-f27f-320e-988a-1b9a6d894533 | -5.20789 | -42.74545 | 2025-09-03 03:53:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9a5a0c2-a2f7-349d-a17f-7a57bb40b9d6 | -5.4404 | -42.8236 | 2025-09-03 03:53:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9feecc00-1fce-38d2-ae80-568d31aa27dd | -3.22142 | -47.13377 | 2025-09-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 65b3eedf-76ac-33c1-869c-085521a4594c | -3.22202 | -47.13023 | 2025-09-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| cb857000-07c4-33e7-8399-eb4be6ed5734 | -3.78988 | -49.43532 | 2025-09-03 03:53:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9fbf426c-14e7-3195-b76c-2d87037c9581 | -5.80514 | -43.22454 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 157c5692-a3b8-31a2-9f7e-f1d2d7b6a9c4 | -4.47314 | -48.119 | 2025-09-03 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8af1238a-c330-3565-adb0-2b50afa367a1 | -5.44081 | -42.84123 | 2025-09-03 03:53:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 11ad5384-0991-31ed-b399-7f331bdcdf1f | -5.74285 | -43.12851 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ffe3e0d9-9532-3db1-9d4d-6a322343faef | -4.02904 | -46.94674 | 2025-09-03 03:53:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 312f3d18-a95c-3aaf-9f36-b03516e42701 | -4.15728 | -46.79395 | 2025-09-03 03:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2abf0763-463e-372c-8568-b1693eda29d5 | -4.16311 | -46.79144 | 2025-09-03 03:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f5b6d754-ba73-3f61-a557-335c0e48000e | -4.85058 | -42.74165 | 2025-09-03 03:53:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a58c14fe-ac1e-3a0a-ae63-baf3b3dfa1e7 | -3.19992 | -49.10676 | 2025-09-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b4f20f8a-cedc-33e1-9b7b-e68d728e2fe8 | -5.49912 | -42.63678 | 2025-09-03 03:53:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 33032cb8-20c7-3c8c-8743-5b8272a8305d | -5.5355 | -36.85028 | 2025-09-03 03:53:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 762ad6a1-f42d-346c-9b2b-8c25d75f3a59 | -4.82503 | -41.806 | 2025-09-03 03:53:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d346fe99-8e40-3d45-a711-4f06bd3a9886 | -5.71137 | -43.1085 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c174eb1a-08e8-3600-8a20-6adc4663e263 | -5.79543 | -43.23352 | 2025-09-03 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b964cf62-0eee-3afd-bf8a-137baaf3510d | -3.21716 | -47.12587 | 2025-09-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| dc03284c-1c2e-3202-8839-16fc0fbb5daa | -5.02493 | -42.48712 | 2025-09-03 03:53:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dd0d4ec7-abb8-3b0b-8235-8e8db06871af | -5.4071 | -42.33162 | 2025-09-03 03:53:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8ed06ccd-5149-3484-9933-5dc89cf6efc6 | -4.82431 | -41.8105 | 2025-09-03 03:53:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1ff120d7-8190-3d25-bb15-94cd54107d32 | -3.21657 | -47.12931 | 2025-09-03 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 056491e4-e7c2-38a4-8746-7385871f52d7 | -4.67658 | -43.63894 | 2025-09-03 03:53:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4d92c77-12f1-392c-84d7-a96b19dcee79 | -2.89425 | -48.29332 | 2025-09-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README37.md)
