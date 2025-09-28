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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ec4510c-b75c-3185-be55-245b999956c8 | -6.20509 | -42.84706 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7e1c53ef-79c9-3a89-8431-a1fdcdc10486 | -7.03684 | -44.77496 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f268fd9d-88e6-3e30-a7d1-5fddb0ec1fa9 | -9.29831 | -49.10203 | 2025-09-28 04:25:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa2a2da7-93a5-3b23-b95b-ac158076dba2 | -6.53677 | -44.97503 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19270c3e-f656-37ea-98ad-c0610a83c5c0 | -9.32021 | -48.953 | 2025-09-28 04:25:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 33c3be7a-7a6c-32ce-86bd-eb9ba6dfc1cc | -5.54122 | -46.27729 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54f2970b-d245-3f0d-952a-b17700027564 | -11.3585 | -45.0539 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a561744c-4ee8-3b53-bdc4-15f9f910e417 | -11.98666 | -47.8969 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8f81d3df-e525-369a-8529-9a34805eef6b | -7.81001 | -47.00863 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 91b7ca60-5e55-311e-9eb3-cf560c3d253e | -7.75491 | -46.9713 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 867c2d8d-4670-372f-bbcf-fcc25b192862 | -11.98668 | -47.07793 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5add0cb8-4ec0-3b73-958d-67a6f39cfff1 | -5.88332 | -43.20214 | 2025-09-28 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 5.9 |
| cb6c6384-6ecc-37d1-9f07-8328fc748573 | -8.4833 | -47.7077 | 2025-09-28 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| db44a393-18a1-3cbd-bf19-f892cca747de | -6.56374 | -45.10281 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f7ea6379-9a95-3c14-b171-714ca4d7a383 | -5.636 | -44.93704 | 2025-09-28 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6f7ef298-c3af-36b2-8655-11f1be319581 | -7.0329 | -44.77802 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6df506b3-abd5-39f8-b24e-d91bcfaede7f | -7.87249 | -44.55747 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3df72c0-f8b5-3714-bf77-1b6c6df32247 | -8.51868 | -44.61157 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dfdefdb7-19c0-3322-b404-434e3c15160e | -5.89415 | -46.04355 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4cad77ac-6514-39fd-a7be-1dc303ade1ca | -5.68427 | -46.31795 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c021602-e52a-3f83-8f02-71340e0ed84f | -6.30498 | -45.89214 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87b9db7f-2cd3-3b49-bce7-03030874a2d6 | -6.78343 | -44.08035 | 2025-09-28 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 41b27548-f6e1-34ac-899c-2c1e489034d0 | -6.79495 | -46.18943 | 2025-09-28 04:25:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78105bf6-a75e-31a5-8b37-bbe652fa0b96 | -6.6975 | -44.57068 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 196e012d-5b97-308d-865a-4380036e20a5 | -11.7144 | -44.42773 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61c41f96-f1ec-32cf-b1e1-6d9b01043a0a | -11.99403 | -47.95588 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb619e38-64ef-3de2-b066-e29e5e2617ed | -6.4284 | -43.07153 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 92941e55-7df9-3f41-9761-a153611d465e | -8.85656 | -46.59885 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a846ad22-e224-392f-8fb1-04a5c379dede | -11.36364 | -45.04318 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bef2caf5-6c32-345f-8418-a166a6772fcd | -11.37054 | -45.0206 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5fadec50-3ecd-3512-8984-0f1e8a56f8d2 | -11.94733 | -47.93028 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90fc0182-f368-3881-9aff-3c0a62e0bc48 | -6.77441 | -41.75171 | 2025-09-28 04:25:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 515353f3-3ee4-3c2f-bc3d-9ff3c7d8fbbe | -11.37517 | -44.94125 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc73b0a7-3c50-3148-aa98-4cc7a0575118 | -12.65673 | -47.39594 | 2025-09-28 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1a491d3-ba53-3b01-b639-adbdf315f098 | -12.45532 | -43.52881 | 2025-09-28 04:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d71e745f-cac5-393a-ae13-c600bf581434 | -8.10354 | -49.08425 | 2025-09-28 04:25:00 | NOAA-20 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d46d013a-7ff6-3e74-a2a1-4b7f671260bd | -5.94843 | -42.71601 | 2025-09-28 04:25:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e1852616-489f-35ed-b854-7b725290cfe6 | -10.5974 | -46.27827 | 2025-09-28 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 42859c3d-3a1d-34aa-b7a5-144dc6543f8d | -9.30988 | -45.69054 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da8d08d9-aa12-388a-9e8d-89c2f77f7fc1 | -5.86474 | -45.58162 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5a7a9e4f-c641-3301-aa6b-b6a36e3bdbbb | -11.40211 | -46.93012 | 2025-09-28 04:25:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c86a4c7-7cae-3224-90dd-42029adece93 | -10.90811 | -44.82198 | 2025-09-28 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05c0303c-5962-36bb-96ea-fbf33441f59d | -12.21591 | -43.74776 | 2025-09-28 04:25:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbcf85c7-0a18-3f38-a933-f20f49c45f32 | -6.98958 | -44.85653 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 278b7a9c-2e10-37c2-98de-92737f85fe25 | -7.79399 | -47.00251 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 52f8699f-4e86-3610-952a-9d96e5476da6 | -7.15888 | -45.51214 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4abd3400-fc46-39eb-8854-d87634e6d7bd | -10.50229 | -49.14394 | 2025-09-28 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 75c6303e-3ba7-3069-99ed-f0ad4e4e0185 | -11.58397 | -45.4884 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6614bc69-915b-3f62-9c91-b9abb1915bd0 | -6.99725 | -44.69464 | 2025-09-28 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1253ec9d-4cca-38cb-9c93-0a004d043229 | -11.97892 | -48.00776 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7406c8eb-e6e3-3004-ac1c-8d8d380c6a4e | -8.2839 | -45.45869 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3c7ceb9d-6e2a-3c6e-b27b-c9d00039891c | -5.55206 | -45.47558 | 2025-09-28 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e19077f4-457a-31ee-bc92-0cdd9e66c9e4 | -6.61055 | -45.08823 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f63b9c88-e733-3edc-9671-692be154e6ab | -9.11277 | -46.67501 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21065ea7-cef4-31a0-b905-013dd614dd25 | -8.58147 | -47.00721 | 2025-09-28 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9276eba6-8c65-3e93-9f4a-5439cfb7770c | -10.10843 | -45.66337 | 2025-09-28 04:25:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72fe1051-5878-3f39-ba3c-c3a0105f6cf1 | -12.9296 | -45.12236 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d457b9c-5e67-3c66-a9e8-f80a4034c0ba | -10.7637 | -45.38436 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae345b5e-0cc4-38fe-9d52-68f0aea2983d | -10.71684 | -47.99664 | 2025-09-28 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8cef1d54-5c96-3558-9438-356c0aa8db4e | -7.79066 | -47.02343 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a298227d-f15c-313a-9edf-b69243f2c8d0 | -12.00249 | -47.90292 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 176feda5-9e33-37cb-a714-f22ce4ddc9f7 | -6.4958 | -44.12689 | 2025-09-28 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82ffd371-ffb3-360f-951c-1fda9652c495 | -11.42159 | -44.91652 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2d3b6844-50f1-3480-b574-fd66ee3e2d7a | -5.64099 | -44.92699 | 2025-09-28 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f07baccd-2307-3e3d-936c-2d68361a309b | -7.19612 | -48.60023 | 2025-09-28 04:25:00 | NOAA-20 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d5dc0c1-31d5-3dc2-a65d-e6f173a7ad8c | -11.99184 | -47.94829 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a732a7ed-9eb0-3d99-a389-bc4938941e41 | -6.70032 | -44.57492 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a423cae9-ae99-3fdd-a7b9-61353e1eed9f | -9.43524 | -43.70304 | 2025-09-28 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ca378642-6dd3-3c2c-98d2-6575dfb0ab34 | -5.44999 | -46.61791 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b69812f-19b0-35ec-b321-8c78f64013a2 | -6.39946 | -43.96149 | 2025-09-28 04:25:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82fb7bab-f60f-300d-8d77-380dbaf94cd5 | -12.4371 | -45.2078 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b74c3cc5-ac11-3686-8bb0-a7bf297eed40 | -8.16559 | -46.41372 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2ea2ba3b-1320-3e8c-8b85-9d95e9a339fc | -12.01187 | -47.90808 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff5a151d-0d3f-36ec-9353-f39fe4fa5f6f | -11.42971 | -44.95752 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09320de9-c33c-3859-a823-aa2df7622400 | -11.40489 | -46.95584 | 2025-09-28 04:25:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a4bfce9-b61a-347b-92ee-363acda7b7aa | -11.98726 | -47.99824 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce4debd3-2c0c-3a1e-bfab-be1c152234f7 | -6.89833 | -45.72618 | 2025-09-28 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 165ac758-c485-33bc-a455-32bc1f0c5527 | -6.25132 | -42.46542 | 2025-09-28 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e9d55b35-6cc3-393e-8cec-e724dcc3c209 | -7.03062 | -44.77038 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 44268d2d-f7b9-3960-9748-89ea750781f3 | -8.84344 | -47.77322 | 2025-09-28 04:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04f58fe1-7982-32e0-99a9-d1bf0a8cbb42 | -8.49527 | -44.7197 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc500784-e2f7-35f1-9244-0eb9aa9c49a6 | -11.99918 | -47.90239 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a7cd2957-d9e7-3a1d-b4cd-897e526ae41e | -12.89161 | -45.16124 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7db1ee2c-2510-3c46-aa09-cdeddf933d6b | -12.53329 | -48.30303 | 2025-09-28 04:25:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5d6dd99-5f57-3001-b52c-2255d088616b | -8.16948 | -46.4321 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f15a52c4-26a5-3a3e-820d-7ac588c15fbb | -7.8685 | -44.56065 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ef89182-2d08-35e3-926e-be026ebe90f7 | -6.55292 | -43.81924 | 2025-09-28 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 316f5a1b-4e9b-3117-8b13-ea1538247dff | -7.7433 | -47.02304 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03ee6221-4026-3d77-9dcf-8b4b84f5fd7b | -11.98782 | -47.99471 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2981db6-b256-3b0e-ba3e-55dbcc0763ed | -8.86642 | -47.81666 | 2025-09-28 04:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0df21421-07b5-39ce-83c8-1f7fce57a9b8 | -5.95622 | -43.76751 | 2025-09-28 04:25:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 648f3f69-dd18-30fd-8546-fdcaf73cb84d | -10.45265 | -48.20168 | 2025-09-28 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2b44479-cafa-35ca-9595-1e442149fecb | -7.4243 | -40.07734 | 2025-09-28 04:25:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 88d30b7c-e38d-3eba-9cfc-29ef92adad3b | -6.49925 | -44.12737 | 2025-09-28 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 319d698d-9129-32c1-819c-fa3b148081a1 | -7.79453 | -47.02047 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c101e223-214d-3042-b4b0-2e2efd51820b | -11.4355 | -44.96631 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b87ae0d2-a9f6-3a2f-862a-94281633bf89 | -10.45246 | -44.96709 | 2025-09-28 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 570066e7-6eba-3503-965e-51803f55a823 | -12.69158 | -45.47073 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 53a23fe2-2b9e-39cc-9f9b-6877fabccbf9 | -8.8635 | -48.56746 | 2025-09-28 04:25:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 971091ca-7688-3540-aa71-041a60593bea | -9.28935 | -45.69852 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README71.md)
