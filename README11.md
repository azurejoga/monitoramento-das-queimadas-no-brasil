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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1415e21-90e4-3d47-bc5a-2a5e93716709 | -3.57665 | -43.46786 | 2026-07-21 05:01:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05a32354-370c-3cc4-a21b-49fd0406a808 | -5.58326 | -42.69146 | 2026-07-21 05:01:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bcd84ebb-3b09-3567-b02e-3bca28693828 | -3.16311 | -48.07124 | 2026-07-21 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d741c5c9-0c0f-3d3b-9a82-44eba53017ae | -3.15318 | -48.57729 | 2026-07-21 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9a277fd-7960-3682-a77d-57dae7ee701d | -2.79846 | -48.57679 | 2026-07-21 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e31cf5ef-e65f-3cc8-b47d-69fb0fadeb63 | -7.63876 | -49.75349 | 2026-07-21 05:01:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| df951a1a-b3ab-3900-b06a-5573e3e402aa | -7.63144 | -49.75237 | 2026-07-21 05:01:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| efa8e380-23f2-3a95-bef2-d91aeca02d96 | -0.8555 | -52.71561 | 2026-07-21 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a97e4c2-222f-3778-8939-16541d8d30bd | -3.14881 | -48.58105 | 2026-07-21 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7048652c-db9d-3890-81ec-5099552c10f8 | -5.12379 | -43.23264 | 2026-07-21 05:01:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 884992ec-7f83-3ca9-9a50-70837ca96396 | -3.67256 | -50.94759 | 2026-07-21 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2b2d3a9-c722-37cd-b520-073dba76e1e5 | -7.34833 | -49.60439 | 2026-07-21 05:01:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5e2e9453-810c-347a-aae4-cfd976c65eba | -6.19038 | -55.3869 | 2026-07-21 05:01:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 051fb880-b4f6-3967-a969-c2ad7f0244e7 | -2.31715 | -48.57863 | 2026-07-21 05:01:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c714f8a-9fdf-3cfb-b990-d18fd56b4931 | -2.69904 | -49.02305 | 2026-07-21 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bcafe6cb-10dc-3cc0-afa9-2e5d99093e83 | -5.74769 | -43.26848 | 2026-07-21 05:01:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68f4574b-c805-3794-b36a-06b1a0f8442f | -6.03298 | -43.8752 | 2026-07-21 05:01:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90f82025-bc84-372a-907b-27398aa989b4 | -7.63812 | -49.75777 | 2026-07-21 05:01:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9c75f4ef-1458-32ec-8262-26d0501dd0ac | -7.35264 | -49.60064 | 2026-07-21 05:01:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 58de8e59-b542-3a59-8e42-87a8aa06c241 | -5.91812 | -46.72303 | 2026-07-21 05:01:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25f1d78d-c98a-3c22-b09b-f795a9485c4c | -3.35541 | -51.14171 | 2026-07-21 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 455c7164-6d06-30fc-8505-734819c659ca | -7.62715 | -49.75609 | 2026-07-21 05:01:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d61ceb70-e4a9-37ed-8ea0-96f3b5ef12a8 | -6.13092 | -55.80753 | 2026-07-21 05:01:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42b7cec3-215b-3e6f-8759-9d4c8457216c | -2.79782 | -49.52408 | 2026-07-21 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccc2dbd4-938b-3495-9eac-b1154d9bc4df | -3.26208 | -49.52855 | 2026-07-21 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5b1e546-4c84-33fd-b0bd-d02b5930033b | -6.03913 | -43.86965 | 2026-07-21 05:01:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 82a1ad99-fd20-3c43-9a79-f07279b45a4b | -5.11789 | -43.2351 | 2026-07-21 05:01:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0cac1205-35a2-3652-8f7f-3a6ab613c032 | -7.64991 | -49.72887 | 2026-07-21 05:01:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 671025b5-0001-33f9-a262-865c01f68c87 | -4.16184 | -43.0954 | 2026-07-21 05:01:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91c4bac9-e458-360c-820d-cc0e185357b4 | -6.60204 | -51.70634 | 2026-07-21 05:01:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9722e713-5d8c-36e9-af5a-23ac673ee0f3 | -5.83003 | -43.47713 | 2026-07-21 05:01:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 105672be-c3c5-3058-8d4f-79a7807cb852 | -6.03868 | -43.87283 | 2026-07-21 05:01:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 47466318-816f-3b8e-a0ee-bcee0a3ac25e | -5.91585 | -46.72226 | 2026-07-21 05:01:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f2677ba-17bf-396c-a2a0-724b88c7ac4d | -10.01829 | -65.05545 | 2026-07-21 05:04:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5f0604d-f870-32c6-aca2-8df60bd060b8 | -12.36021 | -47.43348 | 2026-07-21 05:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fad2585-5b6e-31df-a5df-01eb3271c387 | -11.65692 | -49.75567 | 2026-07-21 05:04:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6991a30c-6e7f-3bcf-990c-c642de215d28 | -8.75053 | -49.08283 | 2026-07-21 05:04:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 90fb0c07-4d2e-33f1-8f00-94f069a9dc91 | -8.75823 | -49.08402 | 2026-07-21 05:04:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f50a9739-8071-30af-af80-11c6ff5dd172 | -10.84689 | -50.424 | 2026-07-21 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dfb97e24-abbe-3256-ba01-afaabaecca0f | -15.41773 | -47.58622 | 2026-07-21 05:04:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 032ebffb-9334-363a-b6e4-7b7e02769f84 | -7.68903 | -55.36177 | 2026-07-21 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8ea53b5-0d40-32ef-bd46-c5b70528a47f | -12.08034 | -53.33641 | 2026-07-21 05:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a36b2eab-f05f-34d9-92d3-f7e3643d1852 | -11.98171 | -47.10516 | 2026-07-21 05:04:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63d1bce3-df4a-385d-b674-40e481d535de | -11.83582 | -44.76604 | 2026-07-21 05:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ddd4a797-7db2-30b3-9e0a-64642e3f1f82 | -12.66031 | -48.20441 | 2026-07-21 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d1f3da6-dc30-3003-964e-3287f7dd7cbd | -12.14171 | -48.26252 | 2026-07-21 05:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f19011f5-e0ec-35c7-9ca3-99322358b3a6 | -12.51981 | -48.253 | 2026-07-21 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6285f2a-9e16-3489-8e68-68a3bc20ae09 | -13.08787 | -48.18212 | 2026-07-21 05:04:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d9ad29f-d1b5-3711-8062-2229438c53fd | -12.14228 | -48.25847 | 2026-07-21 05:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9bf19438-5492-3370-aa80-5a43fd9c8839 | -10.55621 | -56.33223 | 2026-07-21 05:04:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 590ebe5a-2660-3ac5-9710-d6703f16bcf7 | -12.99221 | -62.1502 | 2026-07-21 05:04:00 | NPP-375D | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1d12acf-baae-3720-a9b0-8190e9e2b245 | -10.37913 | -48.32824 | 2026-07-21 05:04:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2599461d-4053-3925-ae49-93cd40d5e18f | -16.14007 | -46.63228 | 2026-07-21 05:04:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e1e7c5b-f636-3fec-a9b7-0dc7b7d50679 | -13.31111 | -45.14388 | 2026-07-21 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e8f7c1b5-2cc2-3eca-a5a5-0b0bbc3c8ba0 | -12.98641 | -62.15454 | 2026-07-21 05:04:00 | NPP-375D | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf857bf0-4624-32ae-9f82-ee709650d9ac | -11.39111 | -47.49457 | 2026-07-21 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b289348f-038f-3b1c-965b-5e490108148d | -13.30738 | -45.12952 | 2026-07-21 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 6b76eca1-5b6e-3f32-a1e6-29a7fa06e5af | -13.31317 | -45.12662 | 2026-07-21 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f40ff734-2472-3868-99c5-966e088d124c | -11.38979 | -47.49675 | 2026-07-21 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0cf273c-122c-384a-ad8f-9ba681e9a975 | -13.30243 | -45.12547 | 2026-07-21 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 57abfedf-8eda-37ee-97e9-ff2c583ea53a | -10.58027 | -50.3116 | 2026-07-21 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70ced549-93c7-3400-8d16-d839d84d5f77 | -12.08368 | -53.33695 | 2026-07-21 05:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c05e9d1f-efdf-3d8b-90b6-1e632debb8b2 | -11.37469 | -47.50842 | 2026-07-21 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 257cdc8e-b46a-3913-8153-de9cca87010c | -10.55607 | -50.27862 | 2026-07-21 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d05113b1-dbe2-3218-915d-4a1b01d789fe | -10.52965 | -50.27912 | 2026-07-21 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44d92329-a2e3-3ce0-915f-46f9eff995f2 | -11.41028 | -47.51249 | 2026-07-21 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bba5edde-3f0a-3a4b-8130-a1f5106152e7 | -10.82059 | -50.42445 | 2026-07-21 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7877cc63-a300-3f28-8a1e-beb7b1fa9562 | -12.66663 | -48.22221 | 2026-07-21 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c86c895-5239-338a-8da4-fd11b68517bd | -9.08436 | -50.58337 | 2026-07-21 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c349593-1325-3604-8c93-fe3c4ede6e60 | -7.68841 | -55.36563 | 2026-07-21 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22eb149d-81ad-3a2a-80b2-f668e73f95d9 | -9.08607 | -50.59607 | 2026-07-21 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f37cf5a6-0de3-35b7-baf1-2e16fb5a14ef | -12.16799 | -59.76062 | 2026-07-21 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4f4cd4f-77c0-3edf-8f69-105e60bfa74f | -13.3078 | -45.12605 | 2026-07-21 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 674dfa01-637a-3fb2-991d-3c5f5d731df3 | -8.94424 | -47.60114 | 2026-07-21 05:04:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d388185-568a-3744-afde-6aa72b57ad14 | -11.59696 | -58.51099 | 2026-07-21 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b2e38de3-35e9-349d-bc2b-6cb61ff08ccd | -10.82426 | -50.425 | 2026-07-21 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| de636985-9b0b-39e0-8442-3ad47b1f8177 | -13.55872 | -46.1134 | 2026-07-21 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3bd103c5-d8e5-3c47-829e-e513ddb9ad88 | -12.14091 | -48.26104 | 2026-07-21 05:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 159deb9c-08ea-3ab3-9313-b5d59c4eb60e | -13.31152 | -45.14043 | 2026-07-21 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4185af9a-b9ff-365b-98e5-d1029c6dc645 | -10.6324 | -47.48537 | 2026-07-21 05:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b36db69-967a-3938-a6ff-5670353fbaa1 | -10.741 | -44.83744 | 2026-07-21 05:04:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2b4b953e-bad4-3b27-b807-8fc8fde35be8 | -12.13744 | -48.26196 | 2026-07-21 05:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 607cd60d-c60c-3d2e-8150-15382ea787c6 | -10.51667 | -50.29052 | 2026-07-21 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b1301ca-bda3-35dc-a05f-bafd82735a1c | -11.40588 | -47.51158 | 2026-07-21 05:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29abf266-dc2a-3738-b437-1d2dfdbf51b3 | -12.08646 | -53.34105 | 2026-07-21 05:04:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5e29f24d-5348-3022-94d1-1c3cd4c09df6 | -12.32496 | -50.00935 | 2026-07-21 05:04:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02b71140-ef4a-3eba-95be-dce745b179e4 | -7.68778 | -55.36948 | 2026-07-21 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c554f539-ae30-3b55-9afa-64da19d8334c | -9.17295 | -49.63859 | 2026-07-21 05:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28952c08-2a1d-3b24-b1e5-f1be96e37ccc | -16.52574 | -47.73477 | 2026-07-21 05:04:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eac32f1f-475e-3b89-a770-782933060f01 | -9.08792 | -50.58392 | 2026-07-21 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af8752fa-6e45-356f-b2c2-b6a7be98af53 | -13.31689 | -45.141 | 2026-07-21 05:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 44b585f0-e7d7-37e3-bffe-08d3bbef3126 | -12.46058 | -46.51354 | 2026-07-21 05:04:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 54fbb1ed-b961-3e7c-a62d-451a9c7a448e | -10.79064 | -50.42435 | 2026-07-21 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27627b97-a9f3-36b3-85f0-03e7882ad6f4 | -12.69936 | -45.32887 | 2026-07-21 05:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| efb8ba72-f05e-3c56-8232-94ceefe97824 | -12.16729 | -59.76447 | 2026-07-21 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d456a50-3bf5-3000-845c-31a97c98fbe2 | -11.91211 | -43.84415 | 2026-07-21 05:04:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e0a598d-c095-3117-9007-e1bafe1f1d9b | -10.55973 | -56.33281 | 2026-07-21 05:04:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 698715fa-6600-3c66-9390-d981d69f0e77 | -10.52532 | -50.28292 | 2026-07-21 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fb924df9-7017-3ff3-95de-8727dee8a55e | -13.0922 | -48.18279 | 2026-07-21 05:04:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a752e700-0144-3dd1-8163-c9e7791444c8 | -10.628 | -47.48481 | 2026-07-21 05:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README12.md)
