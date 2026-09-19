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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b322e7d-93a8-34c3-bd79-030c231e51c8 | -8.21496 | -41.08229 | 2026-09-19 04:02:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b9d6b4c5-7bb8-3049-b336-877c6de7bf7a | -9.24801 | -45.91621 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27c10ff5-2188-3087-ac39-7d505360a09a | -9.74548 | -46.08761 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0f384b68-e716-3c04-8d9a-31609c00d7f5 | -7.00276 | -43.88664 | 2026-09-19 04:02:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0560b7a-79bb-30e5-a19c-f43320bd37a7 | -5.61956 | -45.23701 | 2026-09-19 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ec712dea-796f-3632-896a-397f718e09cb | -3.3659 | -50.44788 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a8126276-82d1-3e3a-8112-bc75507093f0 | -8.60459 | -54.60022 | 2026-09-19 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f7d9e283-bc01-3191-9e22-8f839af2eedb | -7.19605 | -39.87654 | 2026-09-19 04:02:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 39506d5d-fb30-35aa-860b-5a1cecc15df5 | -9.90952 | -46.58715 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cca965e-1dd9-3fe8-91ba-d079e679fefa | -7.7925 | -44.84985 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 182e3225-cde5-3c70-a970-8dff21a4e979 | -3.23539 | -46.94937 | 2026-09-19 04:02:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| f88076d0-3555-3bf7-9d88-97531b1002e1 | -6.94426 | -42.55093 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a2c54b96-60d6-340f-b8ed-c19448dd1ab5 | -10.52674 | -46.71758 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f24cc704-d5bc-3bae-a408-5eb04da588ea | -3.37266 | -50.44444 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2471cea9-a34d-3a58-944b-8d9d388b3b7b | -7.63849 | -46.10804 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 769cd380-b904-3ff2-ac1a-12ee2b30025d | -8.12587 | -44.82969 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2b8ee94f-dc0d-34ad-87d0-b1216ed0766f | -5.73577 | -43.27896 | 2026-09-19 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8bb7829e-f878-35bb-bfac-9e422b27b74f | -7.85767 | -44.87307 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 4ec5abb3-d8c1-337b-8e49-b35976a717bb | -2.82186 | -50.45897 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| ba3c1f7e-d4ac-3523-87cc-d1732c4bddfc | -8.76763 | -44.24612 | 2026-09-19 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a90fac56-800e-366d-b19d-74fa93c76154 | -6.65028 | -43.63413 | 2026-09-19 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 12a11ef8-81a5-3a7d-bfc8-2d462f7b04da | -2.66118 | -49.4806 | 2026-09-19 04:02:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c59c6eb7-841d-3e90-a33e-34741a42452f | -8.77006 | -48.66721 | 2026-09-19 04:02:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b83b03c9-1d3c-3e41-9af8-80543f0ad175 | -11.1553 | -42.79429 | 2026-09-19 04:02:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 859caa6a-d5c8-3024-abcb-559be22d14f3 | -3.45369 | -50.60788 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cb63ef87-2ae0-346a-99a3-712c618a631e | -8.61171 | -54.60143 | 2026-09-19 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 25c6bb1a-359f-3dc8-b6b4-7a7ac6af63a4 | -9.68116 | -48.32963 | 2026-09-19 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ad88b1c2-e362-32d8-b136-992a6a21cb66 | -6.02135 | -45.35859 | 2026-09-19 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 594cb9a4-c0b7-3a47-bcb9-182c8966d702 | -9.73744 | -46.92154 | 2026-09-19 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a68cb3c7-252c-3018-b0ef-2828d6ad467d | -9.25251 | -46.2063 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 45ca0a8d-4dc8-3ba3-bc75-3f099c09ca69 | -5.99737 | -51.79016 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b6320ccb-19cb-33dc-b088-44f32c2c90af | -8.76983 | -44.23307 | 2026-09-19 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cafb6218-c6d4-3d0c-8c01-00b460f9322e | -7.65177 | -46.10609 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b8a6a8b-641a-3ad9-aa95-f872f505aff6 | -7.83328 | -45.26515 | 2026-09-19 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f295e41-29cf-371a-b966-25a56d94350b | -9.95473 | -46.54957 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00c5dbc4-7a0a-31ef-88a3-27641a094131 | -8.7689 | -46.91346 | 2026-09-19 04:02:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3b1a0cf7-3243-3cf8-a690-e64571719d24 | -7.56851 | -49.60252 | 2026-09-19 04:02:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ee76bf0-c7b9-3ae6-b16d-be101b9954ef | -7.09828 | -46.4434 | 2026-09-19 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7132c42a-8f0f-30fe-a9a7-cfc38c21cc2d | -3.35977 | -50.45875 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb3d0e84-4958-3969-ae74-01c7c3409da0 | -7.09549 | -42.08857 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1dd2932f-ae54-33ee-807c-6ada7fc76c92 | -9.73204 | -46.14244 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90d1671e-5040-3653-ad78-9274f6cd435e | -6.27048 | -41.66926 | 2026-09-19 04:02:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c4f993c0-a727-3cbf-9444-199e4fef9f07 | -3.42995 | -50.66801 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c57e422-2dbb-3426-84e7-62fb414b38fc | -2.83398 | -50.46793 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c2730af8-505f-354b-9a0d-50b69ae7e4c7 | -9.78988 | -48.33816 | 2026-09-19 04:02:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fe5eabf0-52f8-3560-91f8-3521ecd2ff31 | -7.33188 | -44.62103 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da014495-3878-330a-86f3-ffb50904e874 | -10.31647 | -45.31636 | 2026-09-19 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b2bdf00b-7a6e-3131-a7c0-b6b57b2fc2c0 | -3.45827 | -50.61085 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 79d83e1b-ac4a-34d9-ba8a-c0a6ba23a6d4 | -8.66868 | -45.44226 | 2026-09-19 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f8f11604-a8b3-354d-a576-a13f3303bc1f | -4.5971 | -42.96384 | 2026-09-19 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7277e7bf-bb29-314a-9540-198729c159d5 | -8.23923 | -45.59893 | 2026-09-19 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b2275b9f-cc61-310b-a569-0f8305ebfbe0 | -7.6469 | -46.10938 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f83f62d7-452a-31e8-b2ea-8c74ee17dc06 | -7.0576 | -42.06373 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1cec6b2b-b8ee-3db9-ae7d-4562632cf4fa | -9.94667 | -45.27728 | 2026-09-19 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 71bda684-84bb-3f2b-99c3-59e595fdc4e9 | -8.36749 | -47.2228 | 2026-09-19 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de42ee33-df97-33e0-bdf5-2beac9885cbd | -8.63573 | -47.53635 | 2026-09-19 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 934a90e7-f4c9-321b-8a73-0f27db191e21 | -8.08921 | -50.96605 | 2026-09-19 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59f9950e-298c-300d-9bb4-a01dfc33eb58 | -6.29545 | -41.77388 | 2026-09-19 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8ab68a7c-c863-3766-ab01-53137c9a52c9 | -7.69936 | -46.1105 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea44dd9c-f52a-371c-b71c-d7b254409bcf | -2.82181 | -50.46604 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 61abb3f4-c3e3-31cd-8fa3-c48b98b63a0c | -9.80787 | -46.4115 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1b721d51-6479-3943-8004-4520e138a852 | -6.71407 | -43.54284 | 2026-09-19 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab6f12fb-0853-32e1-af50-0f766337cdf8 | -9.89222 | -46.55552 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db9e00fb-4f4e-34c4-98be-ba073883d32f | -10.58824 | -46.61127 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b1463471-1099-3c2b-8399-f2e774c8fa2f | -7.04322 | -42.0879 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c516ed5f-b63f-305d-be67-6285534dace1 | -9.99823 | -50.27393 | 2026-09-19 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7396f9b8-1123-332a-8e55-e2a5927b0c51 | -11.28398 | -43.51418 | 2026-09-19 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90fa6bb2-0b69-30fb-8969-cc0206bec9d8 | -7.70143 | -46.7248 | 2026-09-19 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63c872e9-aed6-35fc-8006-d99134d675a3 | -10.58755 | -46.61524 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 631bee0e-8918-3216-a7ad-ac45f700ba0e | -7.68954 | -46.1125 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8fdc19f-d389-3d0f-b8f5-66e1eb17d896 | -3.52101 | -50.80077 | 2026-09-19 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9c3c1dbb-52be-34bc-bdb0-497f069f8041 | -9.95192 | -46.54101 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d176cea9-8a44-3f67-a213-6e06163d7160 | -9.24648 | -46.21677 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b6f8c989-c4d9-3037-ad80-91fe2e96d8da | -9.55675 | -46.58533 | 2026-09-19 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 21498c02-25c7-3a2c-ac36-76d7a67b5204 | -7.64757 | -46.1054 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 29ccdcc2-2d2a-3cd6-84ce-25993e6112e6 | -7.08316 | -43.60259 | 2026-09-19 04:02:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db797cdd-6106-3296-9ae4-ea269130c22b | -6.22787 | -44.69464 | 2026-09-19 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 975eeb61-f41b-3b70-a1c9-fe3da21c4a78 | -7.58127 | -43.44305 | 2026-09-19 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 987f5c4b-4582-35f7-bb8f-4894938d6b84 | -8.77208 | -48.66933 | 2026-09-19 04:02:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6b791c76-f5ad-3516-8482-af9ec80cdfc3 | -7.64623 | -46.11336 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| af708757-fdb5-31cc-a697-28502c4c611e | -8.7661 | -48.67442 | 2026-09-19 04:02:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f36173e6-8941-30c0-a5d7-e85f83159f66 | -6.09401 | -44.3072 | 2026-09-19 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| de70df53-45e2-3007-87f8-81bc4cb381db | -10.09401 | -45.6436 | 2026-09-19 04:02:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| af860277-1a43-3cd2-a3d7-af368bcc94d6 | -9.95817 | -45.27934 | 2026-09-19 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0ec808d-de1a-39a7-a9fb-fa670892f6dd | -4.36352 | -47.77938 | 2026-09-19 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a16e9ef1-15f1-3492-bb27-eba58a98a06f | -10.57753 | -46.55092 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 833bcfd3-3251-3ea6-939c-e6cff6f724a8 | -8.88411 | -45.93855 | 2026-09-19 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa87811c-5137-3d70-8dbb-bc6945b5366e | -9.61004 | -45.3836 | 2026-09-19 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5edcc8a1-091f-3ec6-8e33-b2de901af3aa | -3.45446 | -50.60345 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bef355c7-790e-3c04-ba6c-6c35f7138b14 | -7.77303 | -44.87178 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b701f5b2-5f73-3ede-af49-e50ceb498281 | -8.4711 | -47.0113 | 2026-09-19 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d0fe516e-60a2-3879-a949-26c58a5f8abe | -8.75949 | -46.91603 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 387d2221-268c-362b-9f37-cc4ca527024a | -3.23454 | -46.95445 | 2026-09-19 04:02:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 070c5e47-fb0e-3736-83e2-774fca6b7786 | -9.93118 | -46.58632 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ccbfdf57-0cd6-3e0c-99ef-7c8d02b07cc2 | -3.23933 | -46.9552 | 2026-09-19 04:02:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 8c48235b-2097-3f13-b1d8-b2543f64bc67 | -9.24335 | -46.18565 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca42e201-45aa-37ec-9dad-2cd85f73085a | -7.77384 | -44.8668 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2a486ae-637f-348e-a5e8-24598dac5cba | -3.37862 | -50.45725 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ca2ddd29-05ad-31a9-8e8b-2cccded46e57 | -7.60544 | -45.43838 | 2026-09-19 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ac8b40a-5bc0-3ef7-8a9c-295af8869bf6 | -7.19132 | -50.8326 | 2026-09-19 04:02:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README29.md)
