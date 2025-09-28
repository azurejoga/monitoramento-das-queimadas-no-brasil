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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a5433f8-3dac-3f42-b1b8-dce2a92848df | -8.2906 | -45.45975 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a9d8bf0-65c4-3539-a89f-d1375aee40be | -11.42144 | -45.03614 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f94bf5f-6597-377f-8f0a-fb08036889fa | -5.94261 | -42.90455 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 64567783-3685-36b2-8045-1478206fb874 | -11.64311 | -48.57847 | 2025-09-28 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd88e668-92ea-3217-a1c6-7478fd492dcc | -7.93743 | -45.68084 | 2025-09-28 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc63a676-db65-395b-8d39-16f8a31ad601 | -10.90691 | -45.74845 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 13b07255-a473-3932-bda8-72fd190a08a7 | -6.06096 | -44.8651 | 2025-09-28 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22537d0a-afa1-3997-b49a-29f118035433 | -11.59886 | -45.43663 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5bd02f18-8085-3259-984d-82929bf0e6c6 | -11.95385 | -47.97481 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f12c368-7ebb-3711-a6bc-64fb98bc81b4 | -11.97258 | -48.00688 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9ac1564-22e5-3b35-824e-4a6097404335 | -10.54073 | -43.62513 | 2025-09-28 04:25:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0ac8f50c-0b80-3bf0-b9fb-886f9955d9dc | -6.40265 | -42.90015 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| b79c2c6e-98e9-30f6-94d9-d7e138294bfb | -7.3039 | -42.94473 | 2025-09-28 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 19294e37-012f-3e7c-9fe6-e0cdb391a11a | -11.50029 | -43.54061 | 2025-09-28 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 147b2a23-af97-3941-989e-ad25501085d5 | -11.72041 | -44.41174 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe4f024d-b930-3077-8b4b-7c53850f0ef4 | -11.57637 | -49.76586 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bca8316f-3c83-3d16-8db3-59f542c1ffb2 | -7.80503 | -47.01857 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 20cda690-a09a-37fe-b559-de747026e660 | -11.60836 | -44.41309 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 573d2bd3-c9bf-3d4b-92d2-e36ac0d29c7b | -10.9264 | -44.30983 | 2025-09-28 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f630b07-fbd7-3741-aeff-e83c15334674 | -7.80392 | -47.02554 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 1dac8ed1-d889-36a3-b6a0-2f1a3dbb6258 | -12.01098 | -47.05295 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb701c4c-603a-310e-bf0c-22b9f5c87aca | -6.68509 | -44.6061 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4937ab7a-8b4c-3391-9801-fcaf67bcc055 | -6.89909 | -44.76128 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 05b9835c-efa9-36be-b165-1de7bef8f515 | -11.68878 | -44.42807 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2738df65-c204-3f20-bf2c-581d6a32c6c0 | -10.45206 | -48.20532 | 2025-09-28 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ddeed889-95e6-3b1c-a485-9d456b728bc5 | -7.49844 | -46.68104 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cfac63d8-585e-3994-bbfc-2cd3d1e031be | -6.47683 | -44.50336 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72a976e0-0dba-351a-9ec4-70cbb2f32f6a | -6.47796 | -44.51864 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 243a052c-31c3-3459-adb2-d5732ea71cff | -7.80172 | -47.01804 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b5e741c5-a9c3-345e-99b4-f4d4eb7b5f28 | -6.0442 | -43.92487 | 2025-09-28 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc5c1e68-40fc-3250-bac9-3ec03ec53421 | -8.67098 | -43.98405 | 2025-09-28 04:25:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8748fb9-2714-34cc-9951-735b4c90948c | -6.78056 | -44.076 | 2025-09-28 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6a745c2e-99fc-307e-a0da-9a6519bc5e81 | -11.68581 | -44.42341 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f803f538-bf93-33a2-9f26-477e63e32c7f | -6.27393 | -42.49169 | 2025-09-28 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f37e0e80-9695-3be1-9e5c-a51811844ec0 | -6.69922 | -44.6046 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 22a0f5ae-e3c9-3cd1-bc8f-e278ffd50bc2 | -8.82602 | -46.20807 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9402f58b-551a-3fb8-b908-3ee9735b4939 | -7.18587 | -41.70207 | 2025-09-28 04:25:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a9323d84-a751-39a5-877f-77e30651aa3b | -5.45386 | -46.61496 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2e994f6-8dde-3e01-855d-73c71b9f9ee6 | -5.99615 | -45.80478 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94344df7-a634-37e0-8dac-2d7aa547a74d | -11.6558 | -45.33657 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 965ef00e-14f7-331e-aef0-124bbe977e21 | -9.2849 | -45.70512 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56787b45-e0f8-34ef-b457-a63127b7144e | -8.91522 | -46.09316 | 2025-09-28 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4695b73b-c040-3e03-907b-08733e906908 | -11.36132 | -44.95224 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a0d0cb4-72c8-3262-8706-7855a7fd03a0 | -7.30325 | -42.94904 | 2025-09-28 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5492f956-25e2-3a96-8065-0ab4dc8436a0 | -9.525 | -43.50113 | 2025-09-28 04:25:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c9e2c4d2-bf9b-3103-a08f-b0cb6df1a1cd | -9.19624 | -49.00414 | 2025-09-28 04:25:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d99129a-a6b5-3b81-a64f-ac3f1e6b8151 | -6.08593 | -49.40118 | 2025-09-28 04:25:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8e5a373-5f3e-3d78-a4b0-6bfc4a10f6ab | -11.58422 | -54.48569 | 2025-09-28 04:25:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 66480a9c-b11b-37c9-9c8f-ac7815d58179 | -7.74883 | -46.98819 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2d4f5e8-f461-3d95-a27d-24e0c26d036d | -11.97427 | -47.99627 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 062a3ec3-e7d1-37b5-85a3-c1e2e97f3eb5 | -8.43723 | -46.8667 | 2025-09-28 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2408d3ba-e554-3bc3-a2f6-9f7391bd4474 | -11.98944 | -47.08199 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 596d8586-2e29-3f22-b1b6-1ba95fc57a41 | -7.75712 | -47.00021 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7a03f5f1-c1cd-3aee-9b3f-25413a307bda | -8.67431 | -49.93397 | 2025-09-28 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d442ba60-c41c-33db-9c14-9bb7d596ff76 | -6.15493 | -42.80629 | 2025-09-28 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2658ec12-d9a2-39c1-a58b-30be00b34ddb | -12.86841 | -44.60575 | 2025-09-28 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f6897df-8c53-31d8-ae0f-929a61a124a5 | -6.07135 | -44.06837 | 2025-09-28 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f95013b-398b-3b21-80e6-c0236bbbf043 | -7.39909 | -44.4487 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47e7c56e-3d82-30f5-9462-59c6f29dbfb8 | -8.85325 | -46.59832 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee6e8699-e11c-3df7-a491-2dff6d4081a5 | -6.7955 | -46.18597 | 2025-09-28 04:25:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 990f3bfd-628d-3444-a0cf-eb74cc29fb39 | -6.38476 | -43.40215 | 2025-09-28 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| de4e76cd-9a5f-32a0-914d-5efecc81d673 | -6.82405 | -44.20192 | 2025-09-28 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8d5a811-532a-3f0a-bd77-d0957f9bedae | -11.98613 | -47.08146 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59f9ec13-84ae-3821-957d-2e7ebcaf61eb | -8.28721 | -45.43727 | 2025-09-28 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91ae572a-beac-3ae6-9fe1-8e729b328ff2 | -6.43926 | -45.90301 | 2025-09-28 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ba072c5-9b8f-3517-a9e9-897b8316ee89 | -11.99699 | -47.89479 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a02058c7-b9e0-33b4-a15b-3def7d8c0fae | -6.19191 | -44.50961 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4fca87d8-ff12-3102-9c02-13adb14bf5a2 | -7.87193 | -44.56117 | 2025-09-28 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91a16e6b-13d7-3a18-9ec0-a1817012dc97 | -5.94685 | -42.90093 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 83218d8f-86be-3aec-9a6a-aaf1097eb3cf | -8.10463 | -49.08283 | 2025-09-28 04:25:00 | NOAA-20 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03f791b6-c2cd-3ea8-95d9-6a9de1d6f3a3 | -11.71858 | -44.42414 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc0907d3-18cb-344a-8c8a-775662908631 | -5.86625 | -45.74508 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5954a7d-1483-3e79-ae6a-08615b523057 | -5.86901 | -45.74905 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32e6603d-2ae4-3c68-8153-63f43c388505 | -8.67793 | -49.93458 | 2025-09-28 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| bc02ca2a-f3f7-3b3e-bdf9-effbd677885b | -8.27166 | -45.47138 | 2025-09-28 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f2969f4-228c-3686-bc8e-26fe18169997 | -12.69325 | -46.87928 | 2025-09-28 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f6ecffdb-45e9-369c-8135-eec0ffe67138 | -11.71082 | -44.42719 | 2025-09-28 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68adc2b9-b111-3ec1-865b-cc70c960d3a1 | -7.24957 | -44.75906 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9b90387-7a91-3953-9ede-867f0f292151 | -9.21551 | -46.77694 | 2025-09-28 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0f11650-979c-393e-99b5-a616612aa1ba | -7.74385 | -47.01955 | 2025-09-28 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 599bc947-b180-3f37-8f05-be81948c7132 | -8.18083 | -41.65371 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 89636cee-c085-3b63-9894-24fbe946b13d | -11.43779 | -44.97473 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f1cb9520-6b9c-3eb1-8e0d-3a0a553fba86 | -9.05971 | -45.53523 | 2025-09-28 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fdcdb01-86b2-3acc-9f1c-1e8b6442d60f | -10.96153 | -49.56883 | 2025-09-28 04:25:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a118c103-e157-3740-9702-8f5543e20ce9 | -7.94021 | -45.68492 | 2025-09-28 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 593d904f-b746-3fe9-9e41-8455ed849af8 | -11.98834 | -47.88631 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 602a20db-22ce-32b3-8521-89182343f15a | -11.94997 | -47.9778 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d13ecd7-ca47-3141-9bd7-a1aa5057a77c | -6.6072 | -45.08773 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7ef78839-4590-3dd5-828f-f2c5b5dad151 | -6.24147 | -44.48642 | 2025-09-28 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6ddc9a9-5fe5-357d-830d-e530548d6179 | -10.12471 | -45.32908 | 2025-09-28 04:25:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f502431d-b9bc-35cb-b77b-93aaa9159d25 | -6.70118 | -42.73113 | 2025-09-28 04:25:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 39ab1095-2ecf-31ac-a63c-fab5f7673124 | -11.98888 | -47.04216 | 2025-09-28 04:25:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2e9a9613-9fb3-3780-849a-63c3cdc235ce | -11.5783 | -47.19277 | 2025-09-28 04:25:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8d8dfa3-6729-3ffa-9598-0157eafb5068 | -11.95498 | -47.96774 | 2025-09-28 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 672a8266-be12-3302-9fff-cd3955192f41 | -5.86847 | -45.75251 | 2025-09-28 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dae75405-71f2-3ef6-a14a-5ab95523b798 | -7.10226 | -44.23982 | 2025-09-28 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3c754875-2c60-3309-8fae-539784d3183d | -11.79138 | -44.90561 | 2025-09-28 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 737b5956-a081-38bd-8f62-406451c0f764 | -7.034 | -44.77089 | 2025-09-28 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 28121c06-64b3-3f04-85f2-dfae760cb26b | -9.28769 | -45.70921 | 2025-09-28 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 24b18c52-ee7d-3fb9-ac5a-f4633b190627 | -8.51524 | -44.61105 | 2025-09-28 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README64.md)
