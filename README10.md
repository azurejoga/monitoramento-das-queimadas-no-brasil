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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b1609ec-0069-3218-a30a-91560f724db8 | -6.30829 | -43.62642 | 2026-08-17 03:36:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4734e9c-f45c-37db-a7e3-ab8c63e6aa32 | -7.17398 | -43.72626 | 2026-08-17 03:36:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be013019-11b8-3319-8e34-758b0e522eed | -11.12837 | -46.50139 | 2026-08-17 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7a98260-59e4-3175-9df3-1ebaf98870bb | -11.80825 | -44.80865 | 2026-08-17 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| b11692d9-3cde-368d-beb9-9f8ad835f570 | -6.53338 | -43.11721 | 2026-08-17 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a97cea99-241e-3505-89e7-3a59656051ea | -7.45249 | -46.15385 | 2026-08-17 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| abcbbd70-1a43-3e38-b76e-b33899f292f6 | -11.39183 | -46.40003 | 2026-08-17 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 918b5764-0d54-3d45-8cfe-7712874e111c | -11.28748 | -40.38256 | 2026-08-17 03:36:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5010c6e4-0317-31d6-9788-a1f9c72f542a | -6.30296 | -43.62078 | 2026-08-17 03:36:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba28948b-7d5c-3932-97af-b105b0a791a0 | -10.46675 | -46.31432 | 2026-08-17 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed607071-03bc-38a1-9482-87d8c8ef6413 | -6.68997 | -43.98964 | 2026-08-17 03:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17b189a7-30b5-3d17-9bff-3e582ce8ed78 | -7.17485 | -43.72156 | 2026-08-17 03:36:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9eaacb8f-744d-3ffb-9d03-53a44b5b6c3d | -11.46818 | -46.58603 | 2026-08-17 03:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b65ca37d-f76b-3c39-b3ee-44700055b494 | -7.23549 | -43.13693 | 2026-08-17 03:36:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a98bc9c9-388d-39e1-a577-211ade5c9022 | -5.84049 | -44.91537 | 2026-08-17 03:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 75abdfef-0c0f-3956-a004-fe78c7ede5d6 | -9.11907 | -45.18251 | 2026-08-17 03:36:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd57aec4-b2a4-37c5-81c0-727f20f7c71b | -12.24963 | -43.14429 | 2026-08-17 03:36:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 33d4cba5-bbd2-35a4-8a87-24a24490c99d | -12.24426 | -43.14309 | 2026-08-17 03:36:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 54ee9ece-2eed-31f9-93b5-b66745c02dac | -9.26868 | -45.65116 | 2026-08-17 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 435f60ca-014c-3160-8392-22f3cd8e3d7b | -11.44575 | -46.59261 | 2026-08-17 03:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2adcdf68-3356-3fa6-b53f-8e916750709c | -11.10131 | -47.29069 | 2026-08-17 03:36:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 567a1e0f-59b0-3b69-8c2d-d318ccf6ee4e | -11.32275 | -46.21302 | 2026-08-17 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| abec33be-48c6-3a3d-b09b-958467f87a4f | -11.47635 | -46.58035 | 2026-08-17 03:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4001231b-56db-37ef-9d02-c5d2e5d0d71e | -12.24849 | -43.15015 | 2026-08-17 03:36:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 0ba2863b-6094-37ab-ba32-3227cf6f766a | -11.13662 | -46.52966 | 2026-08-17 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 662d414e-dc51-3cee-b4f6-d1d3977a1f63 | -11.46238 | -46.58937 | 2026-08-17 03:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 210facc7-8632-3a01-bb7f-0134fcd87a3a | -11.44454 | -46.59847 | 2026-08-17 03:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e38b5e02-bc8b-3d53-a15d-cb2bad1d50f0 | -6.6909 | -43.98457 | 2026-08-17 03:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 52817a0d-94ff-3e6d-91ea-40995de76555 | -11.49625 | -46.59534 | 2026-08-17 03:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3b459c7b-64f0-3930-80f7-34c6effc8318 | -9.1202 | -45.97673 | 2026-08-17 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 36b9f281-c45d-34d7-85f1-e4313f6ff5ed | -9.11654 | -45.98594 | 2026-08-17 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5136e6e2-2f09-3e20-a184-d362611f270b | -11.12974 | -46.49473 | 2026-08-17 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 39343847-ad9f-3cd1-ad98-a95a5fc9dbee | -9.2053 | -37.48237 | 2026-08-17 03:36:00 | NOAA-20 | CANAPI | ALAGOAS | Brasil | 2701605 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| eb427160-ee8b-3703-8e0c-f5f12ef76766 | -11.45343 | -46.58944 | 2026-08-17 03:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16afecc2-9d00-3ef1-928b-c23db3d53f71 | -12.24906 | -43.14726 | 2026-08-17 03:36:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c1af9504-5774-3563-bfec-c045904ba9d4 | -11.48311 | -46.5816 | 2026-08-17 03:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f364be5-9976-38d6-8426-62aeea502553 | -8.73271 | -45.3111 | 2026-08-17 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c199d85c-c256-3c29-8485-38754bf1d45b | -11.81428 | -44.80989 | 2026-08-17 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| be43fab5-d49a-399c-9fa8-0ddd926b1655 | -11.47733 | -46.58514 | 2026-08-17 03:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6ab0f208-4368-3fa0-aa08-a50e63e7ed16 | -11.13381 | -46.50909 | 2026-08-17 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9d787319-0830-3a69-b65d-69b95968e19d | -11.47068 | -46.58336 | 2026-08-17 03:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b600f3ee-f9f5-322b-b466-9aa1064cca5f | -6.52826 | -43.11157 | 2026-08-17 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 95e27784-1e2c-328f-abbf-73b70f3931ff | -11.09977 | -47.28254 | 2026-08-17 03:36:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1c0418b0-e055-34ca-92b2-6659aab0c7de | -11.28844 | -40.37747 | 2026-08-17 03:36:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6e8535cf-84ad-3fee-b90a-71ee9044d6e4 | -9.11769 | -45.98006 | 2026-08-17 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 060650a9-8926-3b9e-b5b3-2dbf880a8d5c | -9.7604 | -47.23399 | 2026-08-17 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0799f037-9776-35eb-976a-e3afcb2f6347 | -11.48836 | -46.59031 | 2026-08-17 03:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f920dd9-d95c-3dac-bb37-b51b385b5d11 | -11.49531 | -46.59061 | 2026-08-17 03:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4d7d6eb6-bcab-3912-afb6-dc5ecd3e2db6 | -9.75591 | -47.23072 | 2026-08-17 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eb9f79a5-7190-3be0-8d33-1eca65b741ef | -11.1271 | -46.50758 | 2026-08-17 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 56d34351-9e5f-3611-a4f8-e64976c852d7 | -11.14189 | -46.50394 | 2026-08-17 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d62feeef-9b5c-39ba-83a3-b486b03fe335 | -11.47215 | -46.5764 | 2026-08-17 03:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ccb320ff-f403-3a3c-b1d3-2d7f65b1f6db | -9.11898 | -45.98275 | 2026-08-17 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 48359703-628d-3a77-8fbb-d9ef335971ba | -12.24793 | -43.15308 | 2026-08-17 03:36:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9aa804ec-7bd5-3e64-9d32-bc27c2b4382c | -11.3214 | -46.21964 | 2026-08-17 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 848368c1-0eb3-3825-8d8e-7703b2592817 | -11.09532 | -47.30332 | 2026-08-17 03:36:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2c8a5d88-84bb-381f-a40b-e58baaaeb272 | -10.46128 | -46.30679 | 2026-08-17 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1824c7a0-86e6-3bf3-9ae9-1d62860e8b32 | -9.7631 | -47.23208 | 2026-08-17 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10a9f846-4032-3bac-818c-7766735c261c | -11.31131 | -46.30313 | 2026-08-17 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d2ad99e-3167-3dd3-9663-cdefcec7a496 | -11.09835 | -47.28918 | 2026-08-17 03:36:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c4f22a28-a81b-3094-8be6-328c899f6510 | -11.12994 | -46.52793 | 2026-08-17 03:36:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 707172aa-26f1-32b0-8cf5-1a4b86e730ff | -13.50463 | -46.22934 | 2026-08-17 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b808fe87-bfa3-37fb-aa31-051b2992052e | -14.49342 | -45.68494 | 2026-08-17 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5fce2218-4032-3978-8035-1cfe24724223 | -15.08178 | -48.72453 | 2026-08-17 03:38:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8bed3908-53b8-351b-82f8-2961011bdb7a | -12.00962 | -46.4628 | 2026-08-17 03:38:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 603369bc-935f-32b0-b1d1-7240b0261ee7 | -18.80324 | -46.74055 | 2026-08-17 03:38:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e68b3702-117f-3ef8-9eaf-0e033b40f46d | -12.00294 | -46.46167 | 2026-08-17 03:38:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6f9cc98c-7d0b-35b0-bebf-d883061a9bcf | -19.27684 | -44.97022 | 2026-08-17 03:38:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 0da635e3-a6fa-370f-baa1-3c94a0491bde | -13.51064 | -46.29702 | 2026-08-17 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae667ad7-0e4d-3b04-800a-367fdd2e0a98 | -11.97776 | -46.44985 | 2026-08-17 03:38:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0b71768-474a-3a36-b74a-844051d8a22d | -14.46933 | -45.67753 | 2026-08-17 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 41067b4c-fae6-3a7c-952f-cdcdde660fa4 | -14.47529 | -45.68081 | 2026-08-17 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1cbe8113-9b88-3a28-9da8-1b313ccca406 | -18.80424 | -46.73601 | 2026-08-17 03:38:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 04fffcad-1ee2-3a60-b3b4-8684aa4e0fa9 | -13.43984 | -43.8455 | 2026-08-17 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b3d21716-d4bb-391d-8d85-960abf581c62 | -19.27609 | -44.97373 | 2026-08-17 03:38:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 14902dee-138f-37db-a559-66fe3f240945 | -11.90935 | -47.35107 | 2026-08-17 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fe44bcfb-d85d-37d9-8a22-58676e280261 | -14.48134 | -45.68217 | 2026-08-17 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 294a1ddd-ad24-35d4-863d-b1ff704af983 | -14.48235 | -45.67746 | 2026-08-17 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 46a083e6-10ac-3d38-92d2-d8d201b09716 | -14.47631 | -45.67608 | 2026-08-17 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c2bd2fa1-6252-37b4-bd2d-d15e72603480 | -13.5123 | -46.2929 | 2026-08-17 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c592ff0-c0d7-35ce-a34e-c3702100638f | -14.49443 | -45.68023 | 2026-08-17 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2f634ad3-9e2a-3ef8-ad2e-74820a589094 | -13.4454 | -43.84643 | 2026-08-17 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 196ebaba-0f70-34e0-a22c-ecbf9de30eed | -11.97553 | -46.44271 | 2026-08-17 03:38:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5407df33-4a1a-3ae8-aaad-99d921510200 | -12.03955 | -46.48524 | 2026-08-17 03:38:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9572a4ce-51b2-37ac-99ff-e2a1a233a177 | -13.51729 | -46.23819 | 2026-08-17 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e69109d1-b209-330b-879f-ad50e98e918d | -12.00168 | -46.46775 | 2026-08-17 03:38:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3d531a7c-ddd6-38e7-8b2d-06558b98a3b3 | -12.03668 | -46.48439 | 2026-08-17 03:38:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5e72a7ca-5e8d-38e2-825d-942813b08d07 | -19.27535 | -44.97725 | 2026-08-17 03:38:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ae534c1b-2933-35ec-8244-b417b08dd7c1 | -12.04545 | -46.45645 | 2026-08-17 03:38:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c83bfa37-fc23-3619-bfc6-c6958d1c2202 | -15.81709 | -48.17093 | 2026-08-17 03:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 82e1e14d-028c-30a5-a13a-532e3221cb55 | -13.51356 | -46.25055 | 2026-08-17 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 270eacaa-d53d-3cc3-821e-2971ff70bf80 | -12.03812 | -46.49226 | 2026-08-17 03:38:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1e271e5c-2811-34ad-8282-c7d3451fd1f8 | -13.51872 | -46.25783 | 2026-08-17 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3221ab76-8236-3979-9f07-0edef59fec3c | -14.88953 | -46.63277 | 2026-08-17 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d4197f2-e5da-34c6-9df8-5b110f69f16b | -13.43504 | -43.84071 | 2026-08-17 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 96a475ed-3082-3e68-ac4d-8219a6847195 | -14.88864 | -46.63693 | 2026-08-17 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9af9c2c2-2071-30d6-a8ae-88ec272f3ef5 | -12.26436 | -45.91235 | 2026-08-17 03:38:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f4580ce1-0c5d-3f34-a9d0-316f030da22a | -14.49351 | -45.68309 | 2026-08-17 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26759f37-c560-3c17-8e44-32d6ec8ecc4c | -12.03522 | -46.49128 | 2026-08-17 03:38:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 151ab6c2-28aa-335f-9fc9-fc003b535e07 | -13.50593 | -46.22301 | 2026-08-17 03:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README11.md)
